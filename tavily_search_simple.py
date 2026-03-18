# -*- coding: utf-8 -*-
import sys
import json
import urllib.request
import ssl

# API Key
api_key = "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"

# 搜索关键词
query = "西安 小学 语文老师 招聘 2025"

# 准备请求数据
data = {
    "api_key": api_key,
    "query": query,
    "search_depth": "advanced",
    "max_results": 10
}

# 创建 SSL 上下文（禁用验证以避免证书问题）
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# 发送请求
url = "https://api.tavily.com/search"
headers = {"Content-Type": "application/json"}

try:
    req = urllib.request.Request(
        url,
        data=json.dumps(data).encode('utf-8'),
        headers=headers,
        method='POST'
    )
    
    with urllib.request.urlopen(req, context=ctx, timeout=30) as response:
        result = json.loads(response.read().decode('utf-8'))
        
        # 输出结果
        print("=" * 70)
        print("Tavily 搜索结果 - 西安小学语文教师招聘")
        print("=" * 70)
        
        if 'answer' in result and result['answer']:
            print(f"\n摘要: {result['answer']}\n")
        
        if 'results' in result and result['results']:
            print(f"找到 {len(result['results'])} 个结果:\n")
            
            for i, item in enumerate(result['results'], 1):
                title = item.get('title', '无标题')
                url = item.get('url', '')
                content = item.get('content', '无内容')
                
                print(f"[{i}] {title}")
                print(f"    链接: {url}")
                if len(content) > 200:
                    print(f"    内容: {content[:200]}...")
                else:
                    print(f"    内容: {content}")
                print()
        
        print("=" * 70)
        
except Exception as e:
    print(f"错误: {str(e)}")
    import traceback
    traceback.print_exc()
