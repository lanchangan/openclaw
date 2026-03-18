#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tavily Search Tool for OpenClaw
使用 Tavily API 进行搜索
"""

import sys
import json
import urllib.request
import urllib.parse
import urllib.error

TAVILY_API_KEY = "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"
TAVILY_API_URL = "https://api.tavily.com/search"

def search(query, max_results=10, search_depth="basic"):
    """
    使用 Tavily API 进行搜索
    
    Args:
        query: 搜索关键词
        max_results: 最大返回结果数 (默认10)
        search_depth: 搜索深度 (basic 或 advanced)
    
    Returns:
        dict: 搜索结果
    """
    headers = {
        'Content-Type': 'application/json'
    }
    
    data = {
        'api_key': TAVILY_API_KEY,
        'query': query,
        'max_results': max_results,
        'search_depth': search_depth
    }
    
    try:
        json_data = json.dumps(data).encode('utf-8')
        req = urllib.request.Request(
            TAVILY_API_URL,
            data=json_data,
            headers=headers,
            method='POST'
        )
        
        with urllib.request.urlopen(req, timeout=30) as response:
            result = json.loads(response.read().decode('utf-8'))
            return result
            
    except urllib.error.HTTPError as e:
        error_body = e.read().decode('utf-8')
        return {'error': f'HTTP Error {e.code}: {error_body}'}
    except urllib.error.URLError as e:
        return {'error': f'URL Error: {str(e.reason)}'}
    except Exception as e:
        return {'error': f'Error: {str(e)}'}


def format_results(results):
    """格式化搜索结果"""
    if 'error' in results:
        return f"搜索出错: {results['error']}"
    
    output = []
    output.append("=" * 60)
    output.append("Tavily 搜索结果")
    output.append("=" * 60)
    
    # 搜索答案/摘要
    if 'answer' in results and results['answer']:
        output.append(f"\n📋 智能摘要:\n{results['answer']}\n")
    
    # 搜索结果列表
    if 'results' in results and results['results']:
        output.append(f"\n🔍 找到 {len(results['results'])} 个结果:\n")
        
        for i, result in enumerate(results['results'], 1):
            title = result.get('title', '无标题')
            url = result.get('url', '')
            content = result.get('content', '无内容')
            
            output.append(f"\n[{i}] {title}")
            output.append(f"    🔗 {url}")
            output.append(f"    📝 {content[:200]}..." if len(content) > 200 else f"    📝 {content}")
    
    output.append("\n" + "=" * 60)
    return "\n".join(output)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python tavily_search.py <搜索关键词>")
        print("示例: python tavily_search.py \"西安 小学 语文老师 招聘\"")
        sys.exit(1)
    
    query = sys.argv[1]
    print(f"正在搜索: {query}\n")
    
    results = search(query)
    formatted_output = format_results(results)
    print(formatted_output)