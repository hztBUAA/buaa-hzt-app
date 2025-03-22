#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
日记文件解析和时间线生成工具

此脚本将扫描指定文件夹中的Markdown格式日记文件，提取每天的关键内容和活动，
并生成一个可以导入到时间线组件的JSON格式数据。
"""

import os
import re
import json
import argparse
from datetime import datetime
import glob
from pathlib import Path
import random

# 尝试导入OpenAI包，用于摘要生成
try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False
    print("警告: OpenAI 包未安装，将使用简单的文本提取方法。如需更好的摘要效果，请安装: pip install openai")

# 设置颜色列表，用于时间线事件
COLORS = ['blue', 'green', 'red', 'orange', 'purple', 'cyan', 'pink', 'amber', 'indigo', 'teal']

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
    """清理Markdown内容，移除图片、链接等标记"""
    # 移除图片标记
    content = re.sub(r'!\[\[.*?\]\]', '', content)
    # 移除内部链接
    content = re.sub(r'\[\[(.*?)\]\]', r'\1', content)
    # 移除任务列表标记
    content = re.sub(r'- \[ \]', '-', content)
    # 移除模板文本部分
    content = re.sub(r'`请在早起后直接投入前一天定下来的一个优先级工作`.*?`在一天结束之后定义一个明天的待办`', '', content)
    # 移除重复的分隔线
    content = re.sub(r'---+\s*---+', '---', content)
    # 移除图片引用
    content = re.sub(r'!\[\[Pasted image \d+\.png\]\]', '', content)
    return content

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
        if section_name not in ['day_summary', 'tomorrow_todo']:
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
        if section_name not in ['day_summary', 'tomorrow_todo']:
            # 将部分标题词也加入标签
            words = re.findall(r'(\w+)', section_name)
            tags.update(words)
    
    # 如果标签太多，只保留几个
    return list(tags)[:5] if tags else []

def process_markdown_file(file_path, use_openai=False, api_key=None):
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
    
    # 生成摘要
    if use_openai:
        summary = get_summary_with_openai(cleaned_content, api_key)
    else:
        summary = None
    
    if not summary:
        summary = simple_summary(sections)
    
    # 生成标签
    tags = generate_tags(sections)
    
    # 随机选择一个颜色
    color = random.choice(COLORS)
    
    # 构建时间线事件
    timeline_event = {
        "date": date,
        "title": f"日记: {date}",
        "content": summary,
        "color": color
    }
    
    if tags:
        timeline_event["tags"] = tags
    
    return timeline_event

def process_directory(directory_path, output_path, use_openai=False, api_key=None):
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
        event = process_markdown_file(file_path, use_openai, api_key)
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
    parser.add_argument("--api-key", help="OpenAI API密钥")
    
    args = parser.parse_args()
    
    if args.use_openai and not OPENAI_AVAILABLE:
        print("无法使用OpenAI: 未安装openai包。请安装后再试: pip install openai")
        args.use_openai = False
    
    process_directory(args.directory, args.output, args.use_openai, args.api_key)

if __name__ == "__main__":
    main() 