# AIStudyOnline Affiliate 变现流程指南

## 已完成的准备工作

- Tool 接口已支持 `affiliateUrl` 和 `hasAffiliate` 字段
- ToolDetailClient 已支持渲染 Affiliate 链接（`rel="sponsored"` + 佣金披露文案）
- 隐私政策已含 Affiliate 披露
- 4 个工具已配置 Affiliate 链接（ChatGPT Plus, Midjourney, Notion AI, Jasper）

## 整体流程

### Step 1：注册联盟计划

为工具目录中标记为 `paid` 的主流工具逐一注册 Affiliate 计划：

| 工具 | 联盟平台 | 预估佣金 | 注册链接 |
|------|---------|---------|---------|
| ChatGPT Plus | Impact / PartnerStack | ~$5-10/订阅 | https://openai.com/affiliates |
| Claude Pro | PartnerStack | ~$5-15/订阅 | https://anthropic.com/partners |
| Midjourney | 自营联盟 | ~$10/订阅 | https://midjourney.com (联系官方) |
| Notion AI | Impact | ~$10-50/订阅 | https://notion.so/partners |
| Jasper AI | PartnerStack | ~20-30% 佣金 | https://partnerstack.com/jasper |
| Canva Pro | Impact | ~$10-30/订阅 | https://canva.com/affiliates |
| ElevenLabs | FirstPromoter | ~20% 佣金 | https://elevenlabs.io/affiliates |
| Gamma | Rewardful | ~20% 佣金 | https://gamma.app/affiliates |
| Cursor Pro | PartnerStack | ~20-30% 佣金 | https://cursor.com/affiliates |
| Grammarly | Impact | ~$20/订阅 | https://grammarly.com/affiliates |
| Leonardo AI | Rewardful | ~15% 佣金 | https://leonardo.ai/affiliates |
| Copy.ai | PartnerStack | ~30% 佣金 | https://copy.ai/affiliates |
| SurferSEO | PartnerStack | ~25% 佣金 | https://surferseo.com/affiliates |
| Descript | PartnerStack | ~$20/订阅 | https://descript.com/affiliates |
| Synthesia | PartnerStack | ~15% 佣金 | https://synthesia.io/affiliates |

### Step 2：获取 Affiliate 链接

每个平台注册后会生成唯一的 referral link，格式通常为：
```
https://toolname.com/?ref=YOUR_ID
https://toolname.partnerstack.com/redirect?partner=YOUR_ID
```

**重要规则：**
- 使用 UTM 参数标记来源：`?ref=xxx&utm_source=aistudyonline&utm_medium=referral`
- 部分平台要求链接必须 `nofollow` 或 `sponsored`（本站已实现 `rel="sponsored"`）
- 存储时只用干净的 affiliate URL，UTM 参数在代码中拼接

### Step 3：更新 tools.ts 配置

对每个已有 Affiliate 的工具，更新两个字段：

```typescript
{
  id: "chatgpt",
  // ... existing fields ...
  hasAffiliate: true,
  affiliateUrl: "https://chatgpt.com/?ref=YOUR_AFFILIATE_ID",
}
```

**批量操作建议**：用 Python 脚本读取 tools.ts，找到所有 `paid` 标签的工具，手动填入 affiliateUrl。

### Step 4：合规要求

**FTC 披露（美国）：**
- 本站已在隐私政策中声明 Affiliate 关系
- 每个 Affiliate 链接旁显示 "(we may earn a commission)"——代码已实现
- 链接使用 `rel="sponsored"` 属性——代码已实现

**Google 政策：**
- ads.txt 已部署
- 非广告形式的推荐链接（nofollow/sponsored）不会影响 AdSense
- 不可以在 AdSense 广告旁边放 Affiliate 链接误导点击

**Amazon Associates（如有）：**
- 需在页面显眼位置声明："As an Amazon Associate we earn from qualifying purchases."

### Step 5：追踪与优化

1. **GA4 事件追踪**：在 Affiliate 链接点击时发送自定义事件
```javascript
gtag('event', 'affiliate_click', {
  'tool_id': 'chatgpt',
  'affiliate_url': '...',
  'page': window.location.pathname,
});
```

2. **月度回顾**：
   - 按工具统计点击量 → 确定高价值推荐位
   - 在文章中提到相关工具时自然插入链接
   - 对比横幅广告 vs 文字内嵌链接的转化率

3. **A/B 测试**：
   - 工具详情页 "Visit Website" vs "Get Started (Affiliate)" 的 CTR
   - 文章侧边栏推荐 vs 正文内嵌推荐的转化

### Step 6：监控与维护

- 每季度检查联盟链接是否失效（工具改名、联盟平台变更）
- 联盟到期前 30 天设置提醒续签
- 新工具上线时同步检查是否有 Affiliate 计划

## 当前本站 Affiliate 数据位置

- 配置文件：`src/lib/tools.ts`（搜索 `hasAffiliate: true`）
- 渲染组件：`src/app/[locale]/tools/[id]/ToolDetailClient.tsx`（搜索 `affiliateLink`）
- 隐私披露：`src/app/[locale]/privacy/page.tsx`

## 建议优先级

1. 先注册 5-8 个最大的平台（PartnerStack, Impact, Rewardful）
2. 批量配置常用工具（ChatGPT, Claude, Midjourney, Canva, Notion）
3. 上线后监控 2-4 周看点击数据
4. 根据数据决定是否扩充更多工具
