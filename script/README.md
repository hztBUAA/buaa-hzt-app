# 日记解析与时间线生成工具

这个工具可以扫描指定文件夹中的Markdown格式日记文件，提取每天的关键内容和活动，生成可以导入到时间线组件的JSON数据。

## 功能特点

- 自动识别日记文件中的日期信息
- 智能提取日记中的关键内容作为摘要
- 自动分析并提取心情指数（5级评分）
- 提取核心关键词（最多5个）
- 支持使用OpenAI API生成更优质的摘要（可选）
- 支持使用Ollama本地模型生成摘要和关键词（可选）
- 从日记内容生成相关标签
- 输出格式与时间线组件兼容的JSON数据

## 使用方法

### 基本用法

```bash
python diary_summarizer.py /path/to/diary/folder
```

这将扫描指定文件夹中的所有Markdown文件，并在当前目录下生成`timeline_data.json`文件。

### 高级选项

```bash
# 使用OpenAI
python diary_summarizer.py /path/to/diary/folder --output custom_output.json --use-openai --api-key YOUR_OPENAI_API_KEY

# 使用Ollama本地模型
python diary_summarizer.py /path/to/diary/folder --output custom_output.json --use-ollama --ollama-model llama3
```

参数说明：
- `directory`：包含Markdown日记文件的目录路径（必需）
- `--output, -o`：指定输出的JSON文件路径（默认为`timeline_data.json`）
- `--use-openai`：使用OpenAI API生成摘要（需要安装openai包）
- `--api-key`：OpenAI API密钥（如未指定，将尝试从环境变量OPENAI_API_KEY获取）
- `--use-ollama`：使用Ollama本地模型生成摘要和关键词
- `--ollama-model`：指定使用的Ollama模型名称（默认为"llama3"）

## 输出格式

生成的JSON文件格式示例：

```json
[
  {
    "date": "2023.01.01",
    "title": "日记: 2023.01.01 😄",
    "content": "完成了: 年度计划制定, 新年祝福发送. 思考了今年的主要目标，决定将重心放在技能提升和健康管理上。",
    "color": "green",
    "mood_level": 5,
    "tags": ["计划", "目标", "新年", "技能", "健康"]
  },
  {
    "date": "2023.01.02",
    "title": "日记: 2023.01.02 🙂",
    "content": "开始执行新的晨间routine，效果不错。阅读了《原子习惯》第三章，有很多启发。",
    "color": "blue",
    "mood_level": 4,
    "tags": ["习惯", "阅读", "morning", "routine", "效率"]
  }
]
```

## 心情指数说明

脚本会分析日记中"总结"部分勾选的选项，自动判断心情级别：

- 5级 (😄): "有收获很开心" - 绿色
- 4级 (🙂): "一般" - 蓝色
- 3级 (😐): "不达标" - 橙色
- 2级 (😞): "糟糕" - 红色
- 1级 (❓): "无记录" - 灰色

心情指数会影响时间线中事件的颜色和标题中显示的表情符号。

## 关键词提取

脚本会分析日记内容，提取最具代表性的5个关键词：

- 使用Ollama时：通过大语言模型提取最相关的主题词
- 不使用Ollama时：基于以下规则提取：
  - 已完成任务中的重要词汇
  - 各部分标题中的关键词
  - 内容中的核心名词和动词

## 导入到时间线

生成的JSON文件可以直接导入到应用的时间线组件中：

1. 在"关于我"页面点击"导入日记数据"按钮
2. 选择生成的JSON文件
3. 导入后，数据将显示在时间线上，并自动显示心情和关键词标签

## 要求

- Python 3.6+
- 依赖包：
  - argparse
  - requests (用于Ollama API调用)
  - openai (可选，用于生成更优质的摘要)

## 安装依赖

```bash
pip install requests
pip install openai  # 可选，如需使用OpenAI
```

## Ollama使用说明

如果要使用Ollama本地模型，请确保：

1. 已安装Ollama (https://ollama.ai)
2. Ollama服务正在运行 (默认端口11434)
3. 已拉取需要使用的模型（如llama3）：`ollama pull llama3`

## 注意事项

- 脚本会尝试从文件名、文件内容或文件修改时间中提取日期
- 脚本会自动跳过模板文本部分，只提取有实际内容的信息
- 如果使用OpenAI功能，请确保有可用的API密钥
- 大型日记库处理可能需要一些时间，请耐心等待 