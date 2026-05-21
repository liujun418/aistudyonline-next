# AIStudyOnline 文章生产标准与流程

## 一、核心原则

**每篇文章回答一个问题**。用户搜索是因为有具体问题，文章的唯一目的是用最清晰的方式回答它。

## 二、选题策略：追热点，选长尾

### 2.1 热点 vs 关键词的关系

| | 热点 | 关键词 |
|---|---|---|
| 做什么 | 选题方向 | 搜索词 |
| 举例 | "GPT-5 发布了" | "GPT-5 what's new for free users" |
| 策略 | 必须追 | 必须绕开大词 |

**规则：选题追热点，关键词选长尾。**

- ChatGPT 发布了新功能 → 选题方向，必须写
- 但标题不用 "ChatGPT New Features 2026 Guide"（被大站垄断）
- 改为 "How to Use ChatGPT's New Image Editor (Even on Free Plan)"

### 2.2 选题来源

每次选题前，至少扫描以下来源中的 2 个：

1. **Google Trends** — AI 相关趋势，过滤出上升期话题
2. **Twitter/X AI 圈** — 用户在大规模讨论什么
3. **Reddit** r/artificial, r/ChatGPT, r/ClaudeAI — 真实用户问题
4. **Product Hunt AI 分类** — 新工具上线，第一时间出教程
5. **YouTube AI 频道** — 什么教程观看量高但文字版少

### 2.3 关键词选择规则

**✅ 长尾关键词特征**（选这个）：
- 4 个词以上
- 包含限定条件（for beginners, free, vs, step by step, without coding, on iPhone）
- 搜索量 50-500/月即可——不追求量，追求意图精准
- Google 首页没有 DR 50+ 站点垄断
- SERP 中有论坛帖、Reddit、Quora 结果 → 优质信号，说明缺少权威内容

**❌ 避免的关键词**（不选）：
- 2-3 个词的泛化词（"what is AI""AI tools""learn AI"）
- 首页被 Forbes、ZDNet、TechCrunch、OpenAI 官方、Google 官方垄断
- 只有视频结果没有文字结果 → 用户意图不是读文章

### 2.4 选题对照表

| 不写 | 改为写 |
|------|--------|
| "What Is ChatGPT?" | "What Can ChatGPT Actually Do for You? 7 Real Examples" |
| "Best AI Tools 2026" | "5 Free AI Tools for Writing a Resume That Actually Work" |
| "How to Use Midjourney" | "Midjourney for Complete Beginners: Your First AI Image in 10 Minutes" |
| "AI for Business Guide" | "How a Freelance Writer Uses ChatGPT to Draft 3x More Pitches" |
| "Claude vs ChatGPT" | "I Tested ChatGPT and Claude on the Same 5 Tasks — Here's What Happened" |

## 三、文章结构模板

每篇文章固定 6 部分结构：

### 3.1 钩子开头（50-80 词）

```
❌ "In today's rapidly evolving AI landscape, artificial intelligence has become..."
✅ "You opened ChatGPT, typed a question, and got back something that looked right 
   but had completely made-up facts. You're not alone — it's called hallucination."
```

直接痛点/场景/问题，不绕弯。让读者在 3 秒内确认"这就是我要找的"。

### 3.2 快速答案（30-50 词）

正文前给出一段加粗的简短答案：
```
**The short answer:** [1-2 句直接回答标题问题]
```
满足零点击搜索（Google 直接展示答案摘要）。

### 3.3 正文（500-800 词）

- H2 每个是一个步骤/子问题/场景
- H3 用于细节拆解
- 每段不超过 4 句
- 至少 1 个具体操作示例（"here's what you actually type into ChatGPT"）
- 至少 1 个对比/选择建议（"use X when..., use Y when..."）
- 数据引用要有来源链接

### 3.4 实操清单（50-100 词）

```
## Quick Checklist
- [ ] Step 1: [actionable item]
- [ ] Step 2: [actionable item]
- [ ] Step 3: [actionable item]
```

读者可以照着做的 checklist，不是总结。

### 3.5 FAQ（2-3 个问答，30-50 词/个）

- 针对标题关键词衍生出的次级问题
- 每个问题一句话能回答
- FAQPage JSON-LD 结构化数据

### 3.6 工具推荐 + 相关文章（自然融入，非强制堆砌）

```
If you're doing X, [Tool Name] is what we recommend — it's [one reason].
Here's our full walkthrough: [related article link].
```

## 四、内容质量标准

### 4.1 必须做到

- **每句有信息量**：删除所有废话，每段提供新的价值
- **具体到可操作**：不说"use AI for productivity"，说"paste your email draft into ChatGPT and ask 'make this shorter and friendlier'"
- **真实场景**：每条建议对应一个普通人的真实使用场景
- **有观点**：说"用这个，不是那个"，不写"depends on your needs"
- **时效性明确**：标题/正文中提到具体时间（2026年某月），过期后必须更新

### 4.2 禁止

- AI 套话：unleash, revolutionize, game-changing, supercharge, in today's landscape
- 空洞列表："有许多工具可以用" 但没有说哪个/为什么
- 关键词堆砌：同一个词在文中重复超过合理次数
- 假装专业：用技术术语解释技术术语
- 无来源断言："研究表明""专家认为" 无链接
- 标题党：标题和内容不符，只为骗点击

### 4.3 难度标签规范

| 标签 | 标准 | 读者画像 |
|------|------|----------|
| Beginner | 不需要任何前置知识，从零开始 | 第一次用AI的人 |
| Intermediate | 假设读者用过基础AI工具 | 用过ChatGPT但不会深入 |
| Advanced | 涉及API/本地部署/代码 | 有技术背景的读者 |

## 五、SEO 规范

### 5.1 标题

- 格式：`[具体内容] - [限定条件/受众]`
- 长度：40-60 字符（英文）
- 主关键词出现在前 30 个字符
- 不用年份除非是年度综述/版本对比
- 标题和 H1 必须一致

### 5.2 Description

- 130-155 字符
- 包含主关键词的自然变体
- 不要罗列关键词，写一句完整的话
- 告诉读者文章里有什么

### 5.3 正文关键词

- 主关键词密度 < 2%（每 500 词出现不超过 3-4 次）
- 使用自然变体和同义词
- 在 H2 中自然融入次级关键词
- 图片 alt 文本包含描述性关键词

### 5.4 结构化数据

每篇文章必须包含：
- `Article` JSON-LD（headline, datePublished, dateModified, author, description）
- `BreadcrumbList` JSON-LD
- 如有 FAQ 部分：`FAQPage` JSON-LD
- 如提及工具：`WebApplication` JSON-LD

## 六、内容生产流程

```
1. 选题（15min）
   ├── 扫描 2+ 热点来源
   ├── 确定 3-5 个候选长尾关键词
   ├── Google 搜索每个词，检查首页竞争
   └── 选定 1 个主关键词 + 2 个次级关键词

2. 大纲（10min）
   ├── 列出 5-8 个 H2
   ├── 每个 H2 下 1-2 个关键信息点
   └── 确定需要截图的步骤

3. AI 生成初稿（即时）
   ├── 提供大纲 + 关键词 + 风格要求
   ├── 要求：500-800 词，短句，人类语感
   └── 要求：不出现禁用词列表中的词

4. 人工审核编辑（15-20min）
   ├── 删除所有 AI 套话
   ├── 验证所有事实/链接
   ├── 增加个人经验/观点
   ├── 确认关键词分布自然
   ├── 添加截图（如有）
   └── Checklist 可执行性验证

5. 发布
   ├── 填入 frontmatter（title/description/category/tags/difficulty/toolsMentioned）
   ├── 生成三语版本（es/ar）
   ├── 添加到 articles.ts
   ├── 本地验证（npm run dev）
   └── git push → Vercel 部署
```

## 七、三语翻译规范

- 英文是原版，质量最高
- 西班牙语：自然翻译，注意西语语序和表达习惯
- 阿拉伯语：RTL 适配，确保界面词和正文风格一致
- 不是逐句直译——每个语言版本都可以调整例子和文化参照

## 八、质量检查清单

发布前逐条确认：

- [ ] 标题 40-60 字符，含主关键词
- [ ] Description 130-155 字符，一句完整话
- [ ] 快速答案段在正文最前面
- [ ] 无 AI 套话（Ctrl+F 搜索 unleash/revolutionize/supercharge/landscape）
- [ ] 至少 1 个具体操作示例
- [ ] 工具推荐有具体名称和理由
- [ ] 所有外部链接可访问
- [ ] FAQ 至少 2 个问答
- [ ] difficulty 标签准确
- [ ] tags 包含主关键词 + 2-4 个相关词
- [ ] toolsMentioned 引用了实际在 tools.ts 中的工具 ID
- [ ] 三语版本均已生成
- [ ] JSON-LD 结构化数据完整
- [ ] `npm run build` 无错误

## 九、内容日历节奏

| 周期 | 产出 | 备注 |
|------|------|------|
| 每日 | 1-2 篇 | 含三语版本 |
| 每周 | 1 篇对比/测评 | 高价值常青内容 |
| 每月 | 1 篇行业趋势汇总 | 时效性内容，可链接往期文章 |
| 热点 | 即时响应 | 大模型更新/新工具发布，24h 内出稿 |

---

**核心原则再强调一遍：每篇文章回答一个具体问题，像一个真实的人写给另一个真实的人看。**
