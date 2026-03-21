# 全局规则配置

> 本文件记录 OpenClaw 的全局配置规则和行为约定

---

## 🔍 默认搜索配置

### 优先搜索技能
**默认搜索技能**: `multi-search-engine`


**配置说明**:
- 优先使用 `multi-search-engine` 技能进行网页搜索
- 该技能支持 17 个搜索引擎（8国内 + 9国际）
- 无需 API Key，即开即用
- 支持高级搜索语法、时间筛选、站点搜索

**备用方案**:
- 如需 Tavily 搜索，需等待 MCP 配置架构更新
- 如需 Brave 搜索，需配置 `BRAVE_API_KEY`

### 搜索技能列表

| 技能名称 | 状态 | 说明 |
|---------|------|------|
| `multi-search-engine` | ✅ 推荐 | 17引擎，无需API Key |
| `web-search-exa` | ⚠️ 需MCP配置 | Tavily/Exa搜索，暂不可用 |
| `web_search` (Brave) | ⚠️ 需API Key | Brave搜索，需配置Key |

---

## 📝 规则说明

1. **优先级**: 多技能可用时，优先使用 `multi-search-engine`
2. **配置更新**: 本文件由用户或Agent更新
3. **生效范围**: 当前 workspace 全局有效

---

*最后更新: 2026-03-21*
*配置状态: ✅ 已启用*