# Tavily Search PowerShell Script
# 使用 Tavily API 进行搜索

$apiKey = "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"
$query = "西安 小学 语文老师 招聘 2025"

$body = @{
    api_key = $apiKey
    query = $query
    search_depth = "basic"
    max_results = 10
} | ConvertTo-Json

try {
    $response = Invoke-RestMethod -Uri "https://api.tavily.com/search" -Method Post -ContentType "application/json" -Body $body -TimeoutSec 30
    
    # 格式化输出
    Write-Host "=" -ForegroundColor Cyan -NoNewline
    Write-Host " Tavily 搜索结果 " -NoNewline
    Write-Host "=" -ForegroundColor Cyan
    
    if ($response.answer) {
        Write-Host "`n📋 智能摘要:" -ForegroundColor Yellow
        Write-Host $response.answer
    }
    
    if ($response.results) {
        Write-Host "`n🔍 找到 $($response.results.Count) 个结果:" -ForegroundColor Green
        
        for ($i = 0; $i -lt $response.results.Count; $i++) {
            $result = $response.results[$i]
            Write-Host "`n[$($i+1)] $($result.title)" -ForegroundColor Cyan
            Write-Host "    🔗 $($result.url)" -ForegroundColor Gray
            $content = $result.content
            if ($content.Length -gt 200) {
                $content = $content.Substring(0, 200) + "..."
            }
            Write-Host "    📝 $content" -ForegroundColor White
        }
    }
    
    Write-Host "`n" -NoNewline
    Write-Host "=" -ForegroundColor Cyan -NoNewline
    Write-Host " 搜索完成 " -NoNewline
    Write-Host "=" -ForegroundColor Cyan
    
} catch {
    Write-Host "Error: $($_.Exception.Message)" -ForegroundColor Red
}
