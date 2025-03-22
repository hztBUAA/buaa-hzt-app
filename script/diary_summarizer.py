#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
日记文件解析和时间线生成工具

此脚本将扫描指定文件夹中的Markdown格式日记文件，提取每天的关键内容和活动，
生成包含心情指数、摘要和关键词的JSON格式数据，可导入到时间线组件。
"""

import os
import re
import json
import argparse
from datetime import datetime
import glob
from pathlib import Path
import random
import subprocess
import requests
import tempfile

# 尝试导入OpenAI包，用于摘要生成
try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False
    print("警告: OpenAI 包未安装，将使用简单的文本提取方法。如需更好的摘要效果，请安装: pip install openai")

# 尝试检测Ollama可用性
try:
    response = requests.get("http://localhost:11434/api/version", timeout=2)
    OLLAMA_AVAILABLE = response.status_code == 200
except:
    OLLAMA_AVAILABLE = False
    print("警告: Ollama服务不可用。如果已安装Ollama，请确保服务正在运行。")

# 设置颜色列表，用于时间线事件
COLORS = ['blue', 'green', 'red', 'orange', 'purple', 'cyan', 'pink', 'amber', 'indigo', 'teal']

# 心情级别映射
MOOD_LEVELS = {
    "有收获很开心": {"level": 5, "emoji": "😄", "color": "green"},
    "一般": {"level": 4, "emoji": "🙂", "color": "blue"},
    "不达标": {"level": 3, "emoji": "😐", "color": "orange"},
    "糟糕": {"level": 2, "emoji": "😞", "color": "red"},
    "无记录": {"level": 1, "emoji": "❓", "color": "grey"}
}

def extract_date_from_filename(filename):
    """从文件名中提取日期"""
    # 尝试从文件名中提取日期 (格式可能为: YYYY-MM-DD 或 YYYYMMDD)
    date_patterns = [
        r'(\d{4}-\d{2}-\d{2})',  # YYYY-MM-DD
        r'(\d{4}\d{2}\d{2})',     # YYYYMMDD
    ]
    
    for pattern in date_patterns:
        match = re.search(pattern, filename)
        if match:
            date_str = match.group(1)
            # 统一日期格式为 YYYY.MM.DD
            if len(date_str) == 8:  # YYYYMMDD
                return f"{date_str[:4]}.{date_str[4:6]}.{date_str[6:]}"
            else:  # YYYY-MM-DD
                return date_str.replace('-', '.')
    
    # 如果文件名中没有日期，尝试从文件修改时间获取
    try:
        mtime = os.path.getmtime(filename)
        date_obj = datetime.fromtimestamp(mtime)
        return date_obj.strftime("%Y.%m.%d")
    except:
        return None

def extract_last_modified_date(content):
    """从内容中提取最近修改日期"""
    modified_pattern = r'最近修改于\s+(\d{4}-\d{2}-\d{2})'
    match = re.search(modified_pattern, content)
    if match:
        date_str = match.group(1)
        return date_str.replace('-', '.')
    return None

def clean_markdown(content):
    """清理Markdown内容，移除图片、链接等标记，也去除模板内容"""
    # 移除图片标记
    content = re.sub(r'!\[\[.*?\]\]', '', content)
    # 移除内部链接
    content = re.sub(r'\[\[(.*?)\]\]', r'\1', content)
    # 移除任务列表标记，但保留文本内容
    content = re.sub(r'- \[ \]', '-', content)
    content = re.sub(r'- \[x\]', '- ✓', content)
    # 移除模板文本部分
    content = re.sub(r'`请在早起后直接投入前一天定下来的一个优先级工作`\s*`在一天结束之后定义一个明天的待办`', '', content)
    # 移除重复的分隔线
    content = re.sub(r'---+\s*---+', '---', content)
    # 移除图片引用
    content = re.sub(r'!\[\[.*?\.jpg.*?\]\]', '', content)
    content = re.sub(r'!\[\[.*?\.png.*?\]\]', '', content)
    return content

def extract_mood_level(content):
    """从总结部分提取心情指数"""
    # 寻找总结部分勾选的选项
    summary_section = re.search(r'## 总结(.*?)(?=^#|\Z)', content, re.DOTALL | re.MULTILINE)
    
    if not summary_section:
        return MOOD_LEVELS["无记录"]
    
    summary_content = summary_section.group(1)
    
    for mood, info in MOOD_LEVELS.items():
        if mood == "无记录":
            continue
        # 查找是否有该心情项被勾选
        if re.search(r'- \[x\]\s*' + re.escape(mood), summary_content):
            return info
    
    # 如果没有找到勾选的心情，检查是否有早睡记录
    early_sleep = re.search(r'- \[x\]\s*是否早睡', summary_content)
    if early_sleep:
        return MOOD_LEVELS["一般"]
    
    return MOOD_LEVELS["无记录"]

def extract_sections(content):
    """提取内容中的不同部分"""
    sections = {}
    
    # 提取"浓缩的一天"部分
    day_summary_match = re.search(r'# 浓缩的一天(.*?)(?=^#|\Z)', content, re.DOTALL | re.MULTILINE)
    if day_summary_match:
        sections['day_summary'] = day_summary_match.group(1).strip()
    
    # 提取各个二级标题部分
    section_pattern = r'## ([^\n]+)(.*?)(?=^##|\Z)'
    for match in re.finditer(section_pattern, content, re.DOTALL | re.MULTILINE):
        section_title = match.group(1).strip()
        section_content = match.group(2).strip()
        if section_content:
            sections[section_title] = section_content
    
    # 提取"明日待办"部分
    todo_match = re.search(r'# 明日待办(.*?)(?=^#|\Z)', content, re.DOTALL | re.MULTILINE)
    if todo_match:
        sections['tomorrow_todo'] = todo_match.group(1).strip()
    
    return sections

def get_summary_with_openai(content, api_key=None):
    """使用OpenAI API生成内容摘要"""
    if not OPENAI_AVAILABLE:
        return None
    
    if api_key:
        openai.api_key = api_key
    elif 'OPENAI_API_KEY' in os.environ:
        openai.api_key = os.environ['OPENAI_API_KEY']
    else:
        print("警告: 未设置OpenAI API密钥，无法使用OpenAI生成摘要")
        return None
    
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "你是一个日记分析助手，擅长从日记中提取最重要的事件、思考和感受，生成简短的总结。"},
                {"role": "user", "content": f"请从以下日记内容中提取关键信息，生成一个100字以内的简短摘要，突出作者当天的主要活动、成就、思考或困扰：\n\n{content}"}
            ],
            max_tokens=200,
            temperature=0.3
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"OpenAI API调用失败: {e}")
        return None

def get_summary_with_ollama(content, model="llama3"):
    """使用Ollama本地模型生成摘要"""
    if not OLLAMA_AVAILABLE:
        print("警告: Ollama服务不可用，无法使用Ollama生成摘要")
        return None
    
    try:
        # 创建一个临时文件存储请求数据
        payload = {
            "model": model,
            "prompt": f"你是一个日记分析助手，擅长从日记中提取最重要的事件和感受。请从以下日记内容中提取关键信息，生成一个100字以内的简短摘要，突出作者当天的主要活动、成就或困扰：\n\n{content}\n\n总结：",
            "stream": False
        }
        
        response = requests.post(
            "http://localhost:11434/api/generate",
            json=payload,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            return result.get("response", "").strip()
        else:
            print(f"Ollama API调用失败: 状态码 {response.status_code}")
            return None
    except Exception as e:
        print(f"Ollama API调用失败: {e}")
        return None

def extract_keywords_with_ollama(content, model="llama3"):
    """使用Ollama本地模型提取关键词"""
    if not OLLAMA_AVAILABLE:
        print("警告: Ollama服务不可用，无法使用Ollama提取关键词")
        return []
    
    try:
        payload = {
            "model": model,
            "prompt": f"请从以下日记内容中提取5个最重要的关键词，这些关键词应该能代表日记的核心主题和活动。只需要列出关键词，用逗号分隔，不需要其他解释：\n\n{content}\n\n关键词：",
            "stream": False
        }
        
        response = requests.post(
            "http://localhost:11434/api/generate",
            json=payload,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            keywords_text = result.get("response", "").strip()
            # 处理返回的文本，提取关键词
            keywords = [k.strip() for k in re.split(r'[,，、\s]+', keywords_text) if k.strip()]
            return keywords[:5]  # 限制最多5个关键词
        else:
            print(f"Ollama API调用失败: 状态码 {response.status_code}")
            return []
    except Exception as e:
        print(f"Ollama API调用失败: {e}")
        return []

def simple_summary(sections):
    """不使用AI时，使用简单规则提取摘要"""
    summary_parts = []
    
    # 从一天的浓缩部分提取已完成的任务
    if 'day_summary' in sections:
        tasks = re.findall(r'-\s*\[x\]\s*(.*?)$', sections['day_summary'], re.MULTILINE)
        if tasks:
            summary_parts.append("完成了: " + ", ".join(tasks[:3]))
    
    # 从各部分中提取非模板的文本行（不是列表项且不是空行）
    for section_name, content in sections.items():
        if section_name not in ['day_summary', 'tomorrow_todo', '总结']:
            # 提取非列表项且不为空的行
            lines = [line.strip() for line in content.split('\n') 
                    if line.strip() and not line.strip().startswith('-') and not line.strip().startswith('#')]
            if lines:
                # 选择最长的2-3行作为有信息量的内容
                lines.sort(key=len, reverse=True)
                for line in lines[:2]:
                    if len(line) > 15:  # 只选择足够长的行，可能包含实质内容
                        summary_parts.append(line)
    
    # 如果提取的内容不足，可以从明日待办中找一些计划
    if len(summary_parts) < 2 and 'tomorrow_todo' in sections:
        important_todos = re.findall(r'-\s*\[\s*\]\s*(.*?)$', sections['tomorrow_todo'], re.MULTILINE)
        if important_todos:
            summary_parts.append("计划: " + important_todos[0])
    
    # 组合摘要，确保长度合适
    summary = " ".join(summary_parts)
    if len(summary) > 150:
        summary = summary[:147] + "..."
    
    return summary if summary else "日常记录"

def generate_tags(sections):
    """从内容中生成标签"""
    tags = set()
    
    # 提取文中的#标签
    all_content = " ".join(sections.values())
    hashtags = re.findall(r'#(\w+)', all_content)
    tags.update(hashtags)
    
    # 从标题中提取关键词作为标签
    for section_name in sections.keys():
        if section_name not in ['day_summary', 'tomorrow_todo', '总结']:
            # 将部分标题词也加入标签
            words = re.findall(r'(\w+)', section_name)
            tags.update(words)
    
    # 如果标签太多，只保留几个
    return list(tags)[:5] if tags else []

def extract_simple_keywords(sections):
    """使用简单规则提取关键词"""
    keywords = set()
    important_keywords = []
    
    # 先尝试从浓缩的一天中提取关键词
    if 'day_summary' in sections:
        # 从勾选的任务中提取名词和动词
        completed_tasks = re.findall(r'-\s*\[x\]\s*(.*?)$', sections['day_summary'], re.MULTILINE)
        for task in completed_tasks:
            # 简单提取，使用中文分词可能更准确但增加依赖
            words = [w for w in re.findall(r'[\u4e00-\u9fa5a-zA-Z]+', task) if len(w) >= 2]
            important_keywords.extend(words[:2])  # 每个任务取最多2个词
    
    # 然后从各个部分提取关键词
    for section_name, content in sections.items():
        if section_name not in ['day_summary', 'tomorrow_todo', '总结']:
            # 部分名称可能是关键词
            if section_name not in ['生活', '论文', '代码题', '开源项目', 'app', '项目', '实习', '英语学习视频', '体育运动', '欲望']:
                keywords.add(section_name)
            
            # 从内容中提取关键词
            # 特别关注：被标记为完成的任务、带有标点的句子（可能是重要陈述）
            completed = re.findall(r'-\s*\[x\]\s*(.*?)$', content, re.MULTILINE)
            for item in completed:
                words = [w for w in re.findall(r'[\u4e00-\u9fa5a-zA-Z]+', item) if len(w) >= 2]
                keywords.update(words[:2])
    
    # 合并重要关键词和普通关键词
    result = important_keywords + list(keywords)
    # 去重并限制数量
    unique_result = []
    for word in result:
        if word not in unique_result and len(unique_result) < 5:
            unique_result.append(word)
    
    return unique_result

def process_markdown_file(file_path, use_openai=False, use_ollama=False, api_key=None, ollama_model="llama3"):
    """处理单个Markdown文件，提取时间线事件数据"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        try:
            with open(file_path, 'r', encoding='gbk') as f:
                content = f.read()
        except:
            print(f"无法读取文件: {file_path}")
            return None
    
    # 提取日期
    date = extract_date_from_filename(file_path)
    if not date:
        date = extract_last_modified_date(content)
        if not date:
            # 无法确定日期，跳过
            print(f"无法确定文件日期: {file_path}")
            return None
    
    # 清理内容
    cleaned_content = clean_markdown(content)
    
    # 提取不同部分
    sections = extract_sections(cleaned_content)
    
    # 提取心情指数
    mood_info = extract_mood_level(cleaned_content)
    
    # 生成摘要
    summary = None
    if use_openai:
        summary = get_summary_with_openai(cleaned_content, api_key)
    elif use_ollama:
        summary = get_summary_with_ollama(cleaned_content, ollama_model)
    
    if not summary:
        summary = simple_summary(sections)
    
    # 提取关键词
    keywords = []
    if use_ollama:
        keywords = extract_keywords_with_ollama(cleaned_content, ollama_model)
    
    if not keywords:
        keywords = extract_simple_keywords(sections) or generate_tags(sections)
    
    # 随机选择一个颜色，优先使用心情对应的颜色
    color = mood_info.get("color", random.choice(COLORS))
    
    # 构建时间线事件
    timeline_event = {
        "date": date,
        "title": f"日记: {date} {mood_info.get('emoji', '')}",
        "content": summary,
        "color": color,
        "mood_level": mood_info.get("level", 0),
        "tags": keywords
    }
    
    return timeline_event

def process_directory(directory_path, output_path, use_openai=False, use_ollama=False, api_key=None, ollama_model="llama3"):
    """处理目录中的所有Markdown文件"""
    # 查找所有Markdown文件
    markdown_files = []
    for ext in ['*.md', '*.markdown']:
        pattern = os.path.join(directory_path, '**', ext)
        markdown_files.extend(glob.glob(pattern, recursive=True))
    
    print(f"找到 {len(markdown_files)} 个Markdown文件")
    
    # 处理每个文件
    timeline_events = []
    for file_path in markdown_files:
        print(f"处理文件: {file_path}")
        event = process_markdown_file(file_path, use_openai, use_ollama, api_key, ollama_model)
        if event:
            timeline_events.append(event)
    
    # 按日期排序
    timeline_events.sort(key=lambda x: x["date"])
    
    # 保存为JSON文件
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(timeline_events, f, ensure_ascii=False, indent=2)
    
    print(f"已生成时间线数据，包含 {len(timeline_events)} 个事件，保存至: {output_path}")
    return timeline_events

def main():
    parser = argparse.ArgumentParser(description="从Markdown日记文件生成时间线数据")
    parser.add_argument("directory", help="包含Markdown日记文件的目录路径")
    parser.add_argument("--output", "-o", default="timeline_data.json", help="输出的JSON文件路径")
    parser.add_argument("--use-openai", action="store_true", help="使用OpenAI API生成摘要")
    parser.add_argument("--use-ollama", action="store_true", help="使用Ollama本地模型生成摘要和关键词")
    parser.add_argument("--api-key", help="OpenAI API密钥")
    parser.add_argument("--ollama-model", default="llama3", help="使用的Ollama模型名称 (默认: llama3)")
    
    args = parser.parse_args()
    
    if args.use_openai and not OPENAI_AVAILABLE:
        print("无法使用OpenAI: 未安装openai包。请安装后再试: pip install openai")
        args.use_openai = False
    
    if args.use_ollama and not OLLAMA_AVAILABLE:
        print("无法使用Ollama: 服务不可用或未响应。请确保Ollama已安装并运行。")
        args.use_ollama = False
    
    process_directory(args.directory, args.output, args.use_openai, args.use_ollama, args.api_key, args.ollama_model)

if __name__ == "__main__":
    main() 