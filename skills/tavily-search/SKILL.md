---
name: tavily-search
description: Tavily专业搜索引擎集成，提供高质量的网页搜索、新闻搜索、学术搜索功能。支持深度搜索、结果摘要、来源引用。当用户需要搜索最新信息、事实核查、查找资料时使用。
---

# Tavily Search 搜索引擎技能

## 核心功能
- 🔍 **网页搜索**：高质量全网搜索，返回最新、最相关的结果
- 📰 **新闻搜索**：专门搜索最新新闻资讯，支持按时间范围过滤
- 🎓 **学术搜索**：搜索学术论文、研究报告、专业资料
- 📝 **智能摘要**：自动生成搜索结果的摘要，节省阅读时间
- 📌 **来源引用**：所有结果都带原始来源链接，方便核实
- 🌍 **多语言支持**：支持中英等多种语言搜索

## 配置方法
在配置文件中添加你的Tavily API Key：
```yaml
tavily:
  api_key: "your-tavily-api-key"
  max_results: 5  # 默认返回结果数量
  search_depth: "basic"  # basic/advanced
```

## 使用示例
```python
from tavily import TavilyClient
tavily = TavilyClient(api_key="your-api-key")
response = tavily.search("最新的AI技术发展趋势", search_depth="advanced")
print(response['answer'])  # 自动生成的摘要答案
print(response['results']) # 详细搜索结果列表
```

## 触发场景
- 用户需要搜索最新的信息、新闻、资料
- 需要事实核查、验证信息准确性
- 查找专业知识、学术论文、技术文档
- 需要获取带来源引用的可靠信息
