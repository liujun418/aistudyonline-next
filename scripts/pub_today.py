"""
Publish July 5, 2026 — 2 articles + 1 new tool (Tencent WorkBuddy).
"""
import os

BASE = r"C:\Users\jun\aistudyonline-next"
os.chdir(BASE)

# ===== Part 1: Add 1 new tool to tools.ts =====
with open('src/lib/tools.ts', 'r', encoding='utf-8') as f:
    tools_src = f.read()

new_tools = r"""
  {
    id: "tencent-workbuddy",
    name: "Tencent WorkBuddy",
    nameZh: "腾讯WorkBuddy",
    description: "Tencent's full-scenario AI office workbench that directly operates local files, supports multi-agent parallel execution, expert teams, and mobile control via WeChat/QQ/Feishu.",
    descriptionZh: "腾讯全场景AI办公工作台，直接操作本地文件，支持多Agent并行执行、专家团队和微信/QQ/飞书移动端控制。",
    category: "ai-agent",
    tags: ["ai-agent", "office", "productivity", "tencent", "automation", "china"],
    difficulty: "beginner",
    url: "https://workbuddy.tencent.com",
    rating: 4.3,
    pricing: "Free",
    useCase: "AI-powered office automation — generate reports, analyze data, create PPTs, manage files, and control tasks from mobile",
    icon: "💼",
    company: "Tencent",
    companyZh: "腾讯",
    founded: 1998,
    headquarters: "Shenzhen, China",
    descriptionLong: "Tencent WorkBuddy is a full-scenario AI office workbench that transforms AI from a chat tool into an autonomous task executor. Unlike cloud-based AI assistants, WorkBuddy operates directly on your local files — it can read, edit, and organize documents, spreadsheets, and presentations without uploading them to external servers. It offers three working modes: Craft Mode (autonomous execution for batch tasks like file sorting), Plan Mode (generates an execution plan for user approval before proceeding — ideal for high-risk tasks), and Ask Mode (text-only responses for consultation). For complex tasks, WorkBuddy dynamically decomposes the work and assigns sub-tasks to multiple AI agents running in parallel, dramatically reducing completion time. It ships with over 20 pre-built skills covering daily office work, code development, and design. Its standout feature is Expert Teams — pre-configured multi-agent squads for specific scenarios (Content Creation Team with creative director + copywriter + designer roles, Development Team with frontend/backend/testing roles). Mobile control via WeChat, QQ, Feishu, or DingTalk lets you assign tasks from your phone and receive results back. WorkBuddy supports multiple AI models (DeepSeek, Kimi, GPT, Claude) so you're not locked into a single provider. For Chinese professionals seeking an all-in-one AI office solution with local file security and mobile flexibility, WorkBuddy is the most comprehensive domestic option.",
    descriptionLongZh: "腾讯WorkBuddy是一款全场景AI办公工作台，将AI从聊天工具转变为能自主执行任务的办公助手。与云端AI助手不同，WorkBuddy直接操作本地文件——读取、编辑、整理文档、表格和演示文稿，无需上传到外部服务器。提供三种工作模式：Craft模式（自主执行标准化批量任务，如文件整理）、Plan模式（先生成执行方案待用户确认后执行，适合合同审查等高危任务）、Ask模式（纯文本回答，适合咨询）。复杂任务会自动分解并分配给多个AI Agent并行执行。内置20+预置技能，覆盖日常办公、代码开发和设计创意。亮点功能是专家团队——为不同场景预配置的多Agent协作组（内容创作团队含创意总监+文案+设计师，开发团队含前后端+测试）。支持通过微信、QQ、飞书、钉钉进行移动端控制，手机发任务、电脑执行、结果回传。支持多种AI模型（DeepSeek、Kimi、GPT、Claude），不绑定单一模型。对于追求本地文件安全和移动灵活性的中国职场人士，WorkBuddy是目前最全面的国产AI办公解决方案。",
    advantages: ["Local file operation ensures data privacy", "Three working modes for different risk levels", "Multi-agent parallel execution for complex tasks", "Pre-built expert teams for specific scenarios", "Mobile control via WeChat/QQ/Feishu/DingTalk", "Multi-model support (DeepSeek, Kimi, GPT, Claude)"],
    advantagesZh: ["本地文件操作保障数据隐私", "三种工作模式适配不同风险等级", "多Agent并行执行复杂任务", "预配置专家团队覆盖各类场景", "微信/QQ/飞书/钉钉移动端控制", "多模型支持不锁定单一供应商"],
    useCases: ["Automated weekly/monthly report generation", "Batch file sorting and data processing", "PPT creation from document outlines", "Multi-agent content creation (brand strategy, marketing campaigns)", "Remote task delegation via mobile during meetings or commute"],
    useCasesZh: ["自动生成周报/月报", "批量文件整理和数据处理", "从文档大纲生成PPT", "多Agent内容创作（品牌策略、营销方案）", "会议或通勤途中通过手机远程派发任务"],
    targetAudience: "Chinese office professionals, content creators, developers, and anyone who handles repetitive document/data/PPT tasks daily",
    targetAudienceZh: "中国职场人士、内容创作者、开发者，以及每天处理重复性文档/数据/PPT任务的人",
    pricingTiers: ["Free (basic features)", "Pro (advanced skills and priority queue, pricing TBD)"],
    pros: ["Operates on local files — no data leaves your machine", "Three modes cover everything from safe Q&A to full autonomy", "Expert Teams are genuinely useful for multi-role projects", "Mobile control via apps you already use daily", "Free tier is generous for individual users"],
    prosZh: ["本地文件操作——数据不离开电脑", "三种模式覆盖从安全问答到完全自主", "专家团队对多角色项目真正实用", "通过日常使用的App进行移动端控制", "个人用户免费额度充足"],
    cons: ["Only available in China currently", "Requires Tencent account login", "Pro tier pricing not yet announced", "English UI support limited"],
    consZh: ["目前仅限中国地区使用", "需腾讯账号登录", "Pro版定价尚未公布", "英文界面支持有限"],
    extensions: [],
    skills: ["Document generation", "Data analysis", "PPT creation", "Batch file processing", "Code development", "UI/UX design", "Poster design"],
    scene: "office",
  },
"""

last_tool = tools_src.rfind('] as Tool[];')
tools_new = tools_src[:last_tool] + new_tools + '] as Tool[];'

with open('src/lib/tools.ts', 'w', encoding='utf-8') as f:
    f.write(tools_new)

print('Part 1: 1 new tool added to tools.ts (Tencent WorkBuddy)')

# ===== Part 2: Add 2 article metadata to articles.ts =====
with open('src/lib/articles.ts', 'r', encoding='utf-8') as f:
    articles_src = f.read()

new_articles = r"""  {
    slug: "2026-ai-agent-guide-choose-right-tool-beginners",
    title: "2026 AI Agent Guide: How to Choose the Right Tool for Beginners",
    titleZh: "2026 AI Agent选型指南：新手如何选择最适合的工具",
    description: "A ranked comparison of five mainstream AI Agent tools — Codex, Claude Code, OpenClaw, Hermes Agent, and TRAE — with pros, cons, and best-use recommendations to help beginners pick the right tool for their workflow.",
    descriptionZh: "五款主流AI Agent工具横向排名对比——Codex、Claude Code、OpenClaw、Hermes Agent和TRAE——含优缺点和最佳场景推荐，帮新手选出最适合自己工作流的工具。",
    category: "AI Tools",
    tags: ["AI Agent", "Codex", "Claude Code", "OpenClaw", "Tools Comparison", "Beginner Guide"],
    difficulty: "beginner",
    toolsMentioned: ["Codex Agent", "Claude Code", "OpenClaw", "Hermes Agent", "TRAE Framework"],
    date: "2026-07-05",
  },
  {
    slug: "tencent-workbuddy-ai-office-workbench",
    title: "Tencent WorkBuddy: The Ultimate AI Office Workbench for Everyday Work",
    titleZh: "腾讯WorkBuddy：日常办公的终极AI工作台深度评测",
    description: "A comprehensive review of Tencent WorkBuddy — a full-scenario AI office workbench featuring three working modes, multi-agent parallel execution, 20+ built-in skills, pre-configured expert teams, and mobile control via WeChat/QQ/Feishu.",
    descriptionZh: "腾讯WorkBuddy全面评测——全场景AI办公工作台，三种工作模式、多Agent并行执行、20+内置技能、预配置专家团队、微信/QQ/飞书移动端控制。",
    category: "AI Tools",
    tags: ["Tencent", "WorkBuddy", "AI Office", "Productivity", "AI Agent", "China"],
    difficulty: "beginner",
    toolsMentioned: ["Tencent WorkBuddy"],
    date: "2026-07-05",
  },

"""

last_bracket = articles_src.rfind('];')
articles_new = articles_src[:last_bracket] + new_articles + '];'

with open('src/lib/articles.ts', 'w', encoding='utf-8') as f:
    f.write(articles_new)

print('Part 2: 2 new articles added to articles.ts')

# ===== Part 3: Add article content to article-content.ts =====
with open('src/lib/article-content.ts', 'r', encoding='utf-8') as f:
    content_src = f.read()

new_contents = r'''
  "2026-ai-agent-guide-choose-right-tool-beginners": {
    content: `<div class="meta-banner">
  <span class="meta-badge">🔧 AI Tools</span>
  <span class="meta-badge">🕒 7 min read</span>
  <span class="meta-badge">📅 Jul 5, 2026</span>
  <span class="meta-badge">🎯 Beginner</span>
</div>

<h2 id="introduction">Introduction</h2>

<p>The AI industry's competitive focus has shifted from "which model is more powerful" to "which Agent can get more work done." This guide ranks mainstream Agent tools based on real-world usage and community feedback to help beginners make an informed choice.</p>

<h2 id="5th-trae">5th Place: TRAE</h2>

<p>TRAE is ByteDance's long-standing Agent tool, often mentioned in discussions about domestic AI tools but rarely the first choice. It evolved from a Cursor-like intelligent IDE into TRAE SOLO, a general-purpose desktop Agent with cross-platform sync across mobile, web, and desktop.</p>

<p><strong>Pros:</strong></p>
<ul>
  <li>Beginner-friendly, no complex configuration required</li>
  <li>Three-platform sync (mobile, web, desktop)</li>
  <li>Free for personal use with no usage limits (though peak hours may require waiting)</li>
</ul>

<p><strong>Cons:</strong></p>
<ul>
  <li>Harness engineering capabilities are weaker than mainstream competitors</li>
  <li>Struggles with long multi-step tasks, cross-file edits, and repeated debugging, leading to detours and high rework costs</li>
</ul>

<p><strong>Best For:</strong> Beginners who want to try AI Agents or have strong mobile office needs. Not recommended for heavy-duty work.</p>

<h2 id="4th-hermes">4th Place: Hermes Agent</h2>

<p>A surprise hit after the OpenClaw craze, Hermes Agent gained attention for its long-term memory and self-evolution capabilities, sparking debates between "raising shrimp (OpenClaw)" and "raising horses (Hermes)."</p>

<p><strong>Pros:</strong></p>
<ul>
  <li>Long-term memory that allows the Agent to learn from past experiences</li>
  <li>Self-evolution through autonomous skill creation</li>
</ul>

<p><strong>Cons:</strong></p>
<ul>
  <li>Over-reliance on skills can lead to outdated or incorrect workflows</li>
  <li>Skill selection errors can derail tasks</li>
  <li>Less competitive in terms of ease of use, security, and localization compared to domestic alternatives</li>
</ul>

<p><strong>Best For:</strong> Use as a daily assistant. Not recommended for heavy coding, PPT creation, data analysis, or complex content production.</p>

<h2 id="3rd-openclaw">3rd Place: OpenClaw and Its Domestic Variants</h2>

<p>OpenClaw and its domestic derivatives (often called "domestic shrimp") are ideal for beginners due to their strong ecosystem and extensive optimizations.</p>

<p><strong>Pros:</strong></p>
<ul>
  <li>Best domestic optimization for Chinese users</li>
  <li>Rich ecosystem with free usage quotas</li>
  <li>Easy to get started: no environment setup required, install and use immediately</li>
</ul>

<p><strong>Cons:</strong></p>
<ul>
  <li>Relies heavily on plugins and skills</li>
  <li>Harness capabilities are relatively weak, so performance in heavy tasks depends on plugin/skill selection</li>
</ul>

<p><strong>Best For:</strong> Beginners to get started with AI Agents. Domestic variants allow quick onboarding to experience Agent value, while advanced users can explore plugins, skills, and workflow configurations.</p>

<h2 id="2nd-claude-code">2nd Place: Claude Code</h2>

<p>Claude Code is a staple in the Agent space, known for its exceptional harness engineering capabilities. It was the default recommendation for AI bloggers before Codex rose to prominence.</p>

<p><strong>Pros:</strong></p>
<ul>
  <li>Strongest harness engineering in the industry</li>
  <li>Excellent adaptation to domestic models via CC Switch</li>
  <li>Best coding Agent capabilities</li>
</ul>

<p><strong>Cons:</strong></p>
<ul>
  <li>High usage barriers: CLI version requires terminal operations, which is not beginner-friendly</li>
  <li>Desktop version lacks Chinese language support and has complex model integration</li>
</ul>

<p><strong>Best For:</strong> Professional developers. For non-developers needing PPT creation, document writing, or general workflow integration, Claude Code may not be the most comfortable option.</p>

<h2 id="1st-codex">1st Place: Codex</h2>

<p>Codex is the new favorite in the AI space, often called the "iPhone of Agents." While its raw capabilities may not surpass Claude Code, its user experience is unparalleled.</p>

<p><strong>Pros:</strong></p>
<ul>
  <li>Seamless integration with GPT-5.5, the most powerful general reasoning model</li>
  <li>Excellent plugin ecosystem with a curated marketplace (similar to the App Store)</li>
  <li>Best user experience with "approve for me" mode for smooth, secure operation</li>
</ul>

<p><strong>Cons:</strong></p>
<ul>
  <li>Limited usage quotas for Plus tier</li>
  <li>Poor adaptation to third-party models</li>
</ul>

<p><strong>Best For:</strong> Users with the right conditions who want a one-stop solution. Codex's strength lies in the seamless collaboration between model and execution system, making it ideal for users who prioritize experience over raw power.</p>

<h2 id="recommendations">Final Recommendations</h2>

<ul>
  <li><strong>Beginners on a budget</strong>: Start with domestic OpenClaw variants. Begin with simple tasks and gradually build your AI workflow.</li>
  <li><strong>Professional developers</strong>: Choose Claude Code. Even with domestic model integration, it remains excellent for development work.</li>
  <li><strong>Users with the right conditions</strong>: Opt for Codex for a one-stop, seamless experience.</li>
</ul>

<p><strong>Final Note:</strong> Don't treat any tool as a religion. The best tool is the one that helps you get work done reliably. Focus on building the workflow that works best for you, not on chasing the most famous tool.</p>

<h2>常见问题</h2>

<h3>I'm a total beginner — which Agent should I start with?</h3>
<p>Start with domestic OpenClaw variants. They require zero setup — install and go. The Chinese-language optimization means you won't fight the UI while learning AI concepts. Begin with simple tasks like "summarize this document" or "help me draft an email." Once comfortable, graduate to more complex workflows. TRAE is another good free option if you need mobile sync. Skip Claude Code for now — its CLI interface will frustrate beginners before they see any value.</p>

<h3>Why is Codex ranked #1 over Claude Code when Claude Code has stronger harness engineering?</h3>
<p>This ranking is for <strong>beginners</strong>, not power users. Codex wins on user experience: it's a polished desktop app with a plugin marketplace, "approve for me" mode, and seamless GPT-5.5 integration. Claude Code's harness engineering is technically superior, but that advantage only matters when you're building complex multi-agent workflows — which beginners aren't doing. Think of it like cameras: a professional DSLR (Claude Code) takes better photos in expert hands, but most people get better results from an iPhone (Codex) because it handles the complexity for you.</p>

<h3>Are all these tools free?</h3>
<p>TRAE and domestic OpenClaw variants are free for personal use. Claude Code has a free tier with API key usage (you pay for the model's API calls). Codex requires a subscription (Plus at $20/month recommended). Hermes Agent pricing varies by region. For beginners, start with the free options (OpenClaw variants or TRAE) to learn the Agent paradigm. Only pay for Codex or Claude Code when you've outgrown what the free tools can do.</p>

<h3>Can I use multiple Agents together?</h3>
<p>Yes, and many professionals do. A common pattern: use Claude Code for heavy coding tasks, Codex for general productivity and PPT creation, and an OpenClaw variant for quick daily tasks. The tools don't compete — they complement each other. The key is building a workflow where each tool handles what it does best, rather than trying to make one tool do everything.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Picked your Agent? Master it with these guides:</p>
  <ul>
    <li><a href="/articles/complete-guide-codex-zero-to-advanced">Complete Guide to Codex: From Zero to Advanced Development Workflow</a> — step-by-step Codex mastery</li>
    <li><a href="/articles/mastering-ai-workflow-beginner-custom-workbench">Mastering AI Workflow: Build Your Custom AI Workbench</a> — integrate multiple tools into one system</li>
    <li><a href="/articles/ai-bubble-or-opportunity-guide-ordinary-people">Is AI a Bubble or Opportunity? A Guide for Ordinary People</a> — understand the bigger picture before diving deep</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">🔧 AI 工具</span>
  <span class="meta-badge">🕒 阅读约7分钟</span>
  <span class="meta-badge">📅 2026年7月5日</span>
  <span class="meta-badge">🎯 入门</span>
</div>

<h2 id="introduction">引言</h2>

<p>AI行业的竞争焦点已从"哪个模型更强"转向"哪个Agent能完成更多实际工作"。本文基于真实使用体验和社区反馈，对主流Agent工具进行排名，帮新手做出明智选择。</p>

<h2 id="5th-trae">第5名：TRAE</h2>

<p>TRAE是字节跳动旗下的老牌Agent工具，在国内AI工具讨论中常被提及但很少成为首选。它从类似Cursor的智能IDE演化为TRAE SOLO——一款支持手机、网页、桌面三端同步的通用桌面Agent。</p>

<p><strong>优势：</strong></p>
<ul>
  <li>新手友好，无需复杂配置</li>
  <li>手机、网页、桌面三端同步</li>
  <li>个人免费使用，无限量（高峰期可能需要排队）</li>
</ul>

<p><strong>不足：</strong></p>
<ul>
  <li>Harness工程能力弱于主流竞品</li>
  <li>长链路多步骤任务、跨文件编辑和反复调试容易走弯路，返工成本高</li>
</ul>

<p><strong>最适合：</strong>想尝试AI Agent的新手或有强移动办公需求的人。不建议用于重型工作任务。</p>

<h2 id="4th-hermes">第4名：Hermes Agent</h2>

<p>OpenClaw热潮之后的一匹黑马，Hermes Agent因长期记忆和自我进化能力引发关注，社区出现了"养虾（OpenClaw）"还是"养马（Hermes）"的讨论。</p>

<p><strong>优势：</strong></p>
<ul>
  <li>长期记忆，Agent能从过往经验中学习</li>
  <li>通过自主创建Skill实现自我进化</li>
</ul>

<p><strong>不足：</strong></p>
<ul>
  <li>过度依赖Skill可能导致使用过时或错误的流程</li>
  <li>Skill选择错误可能让任务偏离方向</li>
  <li>在易用性、安全性和本土化方面不如国产替代方案</li>
</ul>

<p><strong>最适合：</strong>作为日常助手使用。不推荐用于重度编码、PPT制作、数据分析或复杂内容生产。</p>

<h2 id="3rd-openclaw">第3名：OpenClaw及其国产变体</h2>

<p>OpenClaw及其国产衍生版（常被称为"国产虾"）因强大生态和深度优化成为新手的理想选择。</p>

<p><strong>优势：</strong></p>
<ul>
  <li>国产优化最佳，中文用户体验最好</li>
  <li>生态丰富，免费使用额度充足</li>
  <li>上手极简：无需环境配置，安装即用</li>
</ul>

<p><strong>不足：</strong></p>
<ul>
  <li>高度依赖插件和Skill</li>
  <li>Harness能力相对较弱，重型任务表现取决于插件/Skill选择</li>
</ul>

<p><strong>最适合：</strong>新手入门AI Agent。国产变体可快速上手体验Agent价值，进阶用户可探索插件、Skill和Workflow配置。</p>

<h2 id="2nd-claude-code">第2名：Claude Code</h2>

<p>Claude Code是Agent领域的中坚力量，以卓越的Harness工程能力著称。在Codex崛起之前，它是AI博主们的默认推荐。</p>

<p><strong>优势：</strong></p>
<ul>
  <li>业界最强的Harness工程能力</li>
  <li>通过CC Switch对国产模型的适配优秀</li>
  <li>最强的编码Agent能力</li>
</ul>

<p><strong>不足：</strong></p>
<ul>
  <li>使用门槛高：CLI版本需要终端操作，对新手不友好</li>
  <li>桌面版缺乏中文支持，模型集成复杂</li>
</ul>

<p><strong>最适合：</strong>专业开发者。对于需要PPT制作、文档撰写或通用工作流集成的非开发者，Claude Code可能不是最舒适的选择。</p>

<h2 id="1st-codex">第1名：Codex</h2>

<p>Codex是AI圈的新宠，常被称为"Agent界的iPhone"。虽然原始能力未必超越Claude Code，但用户体验无与伦比。</p>

<p><strong>优势：</strong></p>
<ul>
  <li>与GPT-5.5（最强通用推理模型）无缝集成</li>
  <li>精选插件市场（类似App Store），生态优秀</li>
  <li>最佳用户体验，"approve for me"模式实现流畅安全操作</li>
</ul>

<p><strong>不足：</strong></p>
<ul>
  <li>Plus套餐使用配额有限</li>
  <li>对第三方模型适配较差</li>
</ul>

<p><strong>最适合：</strong>有条件、想要一站式解决方案的用户。Codex的强项在于模型与执行系统的无缝协作，适合重视体验胜过原始能力的用户。</p>

<h2 id="recommendations">最终推荐</h2>

<ul>
  <li><strong>预算有限的新手</strong>：从国产OpenClaw变体开始。先做简单任务，逐步搭建AI工作流。</li>
  <li><strong>专业开发者</strong>：选Claude Code。即使搭配国产模型，开发能力依然出色。</li>
  <li><strong>有条件的用户</strong>：选Codex，享受一站式无缝体验。</li>
</ul>

<p><strong>最后忠告：</strong>别把任何工具当信仰。最好的工具是能帮你稳定完成工作的那个。专注于构建最适合自己的工作流，而不是追逐最有名的工具。</p>

<h2>常见问题</h2>

<h3>我是纯小白——该从哪个Agent开始？</h3>
<p>从国产OpenClaw变体开始。零配置，安装即用。中文优化意味着你在学习AI概念时不用和界面较劲。从简单任务开始，如"总结这篇文档"或"帮我起草邮件"。熟练后再进阶到更复杂的工作流。TRAE是另一个不错的免费选择（如果你需要手机同步）。暂时别碰Claude Code——它的CLI界面会在新手看到任何价值之前就让人崩溃。</p>

<h3>为什么Codex排名第一？Claude Code的Harness工程不是更强吗？</h3>
<p>这个排名是针对<strong>新手</strong>的，不是针对专业用户。Codex赢在用户体验：它是精致的桌面应用，有插件市场、"approve for me"模式、GPT-5.5无缝集成。Claude Code的Harness工程技术上更强，但这个优势只在构建复杂多Agent工作流时才体现——新手不会做这些。类比相机：专业单反（Claude Code）在专家手里拍得更好，但大多数人用iPhone（Codex）能拍出更好的照片，因为它帮你处理了复杂性。</p>

<h3>这些工具都免费吗？</h3>
<p>TRAE和国产OpenClaw变体个人免费。Claude Code有免费层级，通过API Key使用（需支付模型API调用费）。Codex需要订阅（推荐Plus $20/月）。Hermes Agent定价因地区而异。新手建议从免费选项（OpenClaw变体或TRAE）开始学习Agent范式。只有当免费工具无法满足需求时，再为Codex或Claude Code付费。</p>

<h3>可以同时使用多个Agent吗？</h3>
<p>可以，很多专业人士都这样做。常见模式：Claude Code处理重型编码任务，Codex处理通用办公和PPT制作，OpenClaw变体处理日常快速任务。这些工具不互斥——它们互补。关键是构建一个工作流，让每个工具做它最擅长的事，而不是试图让一个工具包揽一切。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>选好了Agent？用这些指南深入掌握：</p>
  <ul>
    <li><a href="/articles/complete-guide-codex-zero-to-advanced">Codex完全指南：从零基础到高级开发工作流</a> — 一步步掌握Codex</li>
    <li><a href="/articles/mastering-ai-workflow-beginner-custom-workbench">掌握AI工作流：打造你的专属AI工作台</a> — 将多个工具集成到一个系统</li>
    <li><a href="/articles/ai-bubble-or-opportunity-guide-ordinary-people">AI是泡沫还是机遇？普通人应对AI浪潮的生存指南</a> — 深入之前先看清全局</li>
  </ul>
</div>`,
  },

  "tencent-workbuddy-ai-office-workbench": {
    content: `<div class="meta-banner">
  <span class="meta-badge">🔧 AI Tools</span>
  <span class="meta-badge">🕒 6 min read</span>
  <span class="meta-badge">📅 Jul 5, 2026</span>
  <span class="meta-badge">🎯 Beginner</span>
</div>

<h2 id="introduction">Introduction</h2>

<p>Tencent WorkBuddy is a full-scenario AI office workbench designed to help professionals streamline daily tasks like work reports, data organization, PPT creation, and weekly report writing. Unlike traditional AI chat tools that only provide text responses, WorkBuddy can directly operate local files, execute tasks autonomously, and deliver actionable results.</p>

<h2 id="core-features">Core Features</h2>

<h3>1. Three Working Modes</h3>

<p>WorkBuddy offers three flexible modes to suit different task types:</p>

<ul>
  <li><strong>Craft Mode</strong>: Directly operates local files and executes tasks automatically (ideal for standardized batch work like file sorting and data processing).</li>
  <li><strong>Plan Mode</strong>: First generates an execution plan for user confirmation before proceeding (suitable for high-risk tasks like contract review and project planning).</li>
  <li><strong>Ask Mode</strong>: Only provides text answers without accessing local files (perfect for consultation and initial draft writing).</li>
</ul>

<h3>2. Multi-Agent Parallel Execution</h3>

<p>For complex tasks, WorkBuddy dynamically decomposes tasks and assigns them to multiple AI agents for parallel execution. This ensures efficient task completion and reduces waiting time.</p>

<h3>3. Rich Skill Library</h3>

<p>WorkBuddy integrates over 20 pre-built skills, covering:</p>

<ul>
  <li><strong>Daily Office</strong>: Document generation, data analysis, PPT creation, email editing, and batch file processing.</li>
  <li><strong>Code Development</strong>: Coding assistance, project understanding, and website application development.</li>
  <li><strong>Design & Creativity</strong>: Product design, PPT design, interactive prototype design, and poster design.</li>
</ul>

<h3>4. Expert Teams</h3>

<p>WorkBuddy provides pre-configured expert teams for different scenarios, such as:</p>

<ul>
  <li><strong>Content Creation Team</strong>: Includes roles like creative director, copywriter, video generator, and graphic designer.</li>
  <li><strong>Development Team</strong>: Covers front-end, back-end, and testing roles.</li>
  <li><strong>Design Team</strong>: Includes UI/UX designers, brand designers, and illustrators.</li>
</ul>

<h3>5. Mobile Control</h3>

<p>WorkBuddy supports mobile control via WeChat, QQ, Feishu, and DingTalk. Users can send tasks from their phones, and WorkBuddy will execute them on the computer, delivering results back to the mobile device.</p>

<h2 id="practical-usage">Practical Usage Guide</h2>

<h3>1. Initial Setup</h3>

<ul>
  <li>Download and install WorkBuddy from the official website.</li>
  <li>Set up a local working folder for WorkBuddy to access.</li>
  <li>Log in with your Tencent account and connect to your preferred AI model (supports DeepSeek, Kimi, GPT, Claude, etc.).</li>
</ul>

<h3>2. Basic Task Execution</h3>

<ul>
  <li>Open WorkBuddy and enter your task in natural language, e.g., "Generate a weekly report based on the files in the 'Reports' folder."</li>
  <li>WorkBuddy will automatically decompose the task, execute it, and deliver the result in the specified format.</li>
</ul>

<h3>3. Using Expert Teams</h3>

<ul>
  <li>Select the "Content Creation Team" from the expert library.</li>
  <li>Enter your task, e.g., "Help me determine the brand visual direction for a new tech product."</li>
  <li>WorkBuddy will ask clarifying questions (e.g., product category, target audience, brand tone) before generating a complete brand strategy.</li>
</ul>

<h3>4. Mobile Control</h3>

<ul>
  <li>Bind your WeChat account in WorkBuddy settings.</li>
  <li>Send tasks from WeChat, e.g., "Collect the latest AI industry news and save it to an Excel file."</li>
  <li>WorkBuddy will execute the task and send the result back to your WeChat.</li>
</ul>

<h2 id="why-stands-out">Why WorkBuddy Stands Out</h2>

<ol>
  <li><strong>Local File Operation</strong>: Unlike cloud-based AI tools, WorkBuddy operates locally, ensuring data security and privacy.</li>
  <li><strong>Multi-Model Support</strong>: Users can switch between different AI models based on task requirements, avoiding being locked into a single model.</li>
  <li><strong>Expert Teams</strong>: Pre-configured expert teams allow users to leverage professional skills without hiring additional staff.</li>
  <li><strong>Mobile Control</strong>: The ability to control WorkBuddy from mobile devices enables remote work and improves productivity.</li>
</ol>

<h2 id="conclusion">Conclusion</h2>

<p>Tencent WorkBuddy is a powerful AI office workbench that transforms AI from a chat tool into a "colleague" that can execute tasks. With its three working modes, rich skill library, expert teams, and mobile control, WorkBuddy can help professionals streamline daily tasks and focus on more creative work. Whether you're a writer, developer, or designer, WorkBuddy has the tools to boost your productivity.</p>

<h2>常见问题</h2>

<h3>How is WorkBuddy different from Codex or Claude Code?</h3>
<p>WorkBuddy is an <strong>office workbench</strong>, not a coding Agent. It's optimized for document processing, data organization, PPT creation, and multi-role content production — the daily grind of Chinese office workers. Codex and Claude Code are developer-first tools that excel at coding but are overkill for "generate a weekly report from these Excel files." WorkBuddy also has unique advantages for Chinese users: WeChat mobile control, native Chinese UI, and local file operation that keeps data on your machine. Think of it as the office specialist in your AI toolkit, complementing rather than competing with coding-focused Agents.</p>

<h3>Is my data safe with WorkBuddy since it accesses local files?</h3>
<p>WorkBuddy operates locally — files are processed on your machine, not uploaded to Tencent's cloud. This is a key differentiator from cloud-based AI office tools that require you to upload documents to their servers. The three working modes give you granular control: use Ask Mode when you only want text responses (no file access), Plan Mode when you want to review the execution plan before WorkBuddy touches your files, and Craft Mode only for trusted batch tasks. For sensitive documents, stick to Ask and Plan modes.</p>

<h3>Which AI model should I connect to WorkBuddy?</h3>
<p>WorkBuddy supports DeepSeek, Kimi, GPT, Claude, and others. For Chinese-language office tasks, DeepSeek and Kimi offer the best price-performance ratio and native Chinese understanding. For English documents or code-heavy tasks, GPT-4o or Claude Sonnet perform better. The beauty of multi-model support is that you're not locked in — use DeepSeek for daily Chinese reports and switch to GPT-4o when you need higher-quality English output or complex reasoning.</p>

<h3>Can WorkBuddy replace my team's designers or copywriters?</h3>
<p>Not entirely — but it can handle the first 80% of the work. The Expert Teams feature (Content Creation Team with creative director + copywriter + designer roles) produces solid first drafts, brand strategies, and design mockups. What it can't replace is the human judgment to decide if the output actually fits your brand voice, resonates with your audience, or meets unspoken client expectations. Use WorkBuddy to eliminate the blank-page problem and repetitive production work, then apply human creativity to polish and differentiate.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Liking WorkBuddy? Explore more AI office and Agent tools:</p>
  <ul>
    <li><a href="/articles/2026-ai-agent-guide-choose-right-tool-beginners">2026 AI Agent Guide: How to Choose the Right Tool for Beginners</a> — compare WorkBuddy with other Agent options</li>
    <li><a href="/articles/mastering-ai-workflow-beginner-custom-workbench">Mastering AI Workflow: Build Your Custom AI Workbench</a> — integrate WorkBuddy into your broader productivity system</li>
    <li><a href="/articles/top-5-ai-ppt-skills-tested-ranked">Battle of the Best: Top 5 AI PPT Skills Tested and Ranked</a> — if PPT creation is your main use case</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">🔧 AI 工具</span>
  <span class="meta-badge">🕒 阅读约6分钟</span>
  <span class="meta-badge">📅 2026年7月5日</span>
  <span class="meta-badge">🎯 入门</span>
</div>

<h2 id="introduction">引言</h2>

<p>腾讯WorkBuddy是一款全场景AI办公工作台，旨在帮助职场人士简化工作汇报、数据整理、PPT制作和周报撰写等日常任务。与传统仅提供文本回复的AI聊天工具不同，WorkBuddy能直接操作本地文件、自主执行任务并交付可落地的成果。</p>

<h2 id="core-features">核心功能</h2>

<h3>1. 三种工作模式</h3>

<p>WorkBuddy提供三种灵活模式适配不同任务类型：</p>

<ul>
  <li><strong>Craft模式</strong>：直接操作本地文件，自动执行任务（适合文件整理、数据处理等标准化批量工作）。</li>
  <li><strong>Plan模式</strong>：先生成执行方案待用户确认后再执行（适合合同审查、项目规划等高风险任务）。</li>
  <li><strong>Ask模式</strong>：仅提供文本回答，不访问本地文件（适合咨询和初稿撰写）。</li>
</ul>

<h3>2. 多Agent并行执行</h3>

<p>面对复杂任务，WorkBuddy会动态分解并分配给多个AI Agent并行执行，确保高效完成任务，减少等待时间。</p>

<h3>3. 丰富的技能库</h3>

<p>WorkBuddy集成20+预置技能，覆盖：</p>

<ul>
  <li><strong>日常办公</strong>：文档生成、数据分析、PPT制作、邮件编辑、批量文件处理。</li>
  <li><strong>代码开发</strong>：编程辅助、项目理解、网站应用开发。</li>
  <li><strong>设计创意</strong>：产品设计、PPT设计、交互原型设计、海报设计。</li>
</ul>

<h3>4. 专家团队</h3>

<p>WorkBuddy为不同场景提供预配置的专家团队：</p>

<ul>
  <li><strong>内容创作团队</strong>：含创意总监、文案、视频生成、平面设计师等角色。</li>
  <li><strong>开发团队</strong>：覆盖前端、后端、测试角色。</li>
  <li><strong>设计团队</strong>：含UI/UX设计师、品牌设计师、插画师。</li>
</ul>

<h3>5. 移动端控制</h3>

<p>WorkBuddy支持通过微信、QQ、飞书、钉钉进行移动端控制。用户可从手机发送任务，WorkBuddy在电脑上执行并将结果回传至手机。</p>

<h2 id="practical-usage">实战使用指南</h2>

<h3>1. 初始设置</h3>

<ul>
  <li>从官网下载安装WorkBuddy。</li>
  <li>设置本地工作文件夹供WorkBuddy访问。</li>
  <li>用腾讯账号登录，连接你偏好的AI模型（支持DeepSeek、Kimi、GPT、Claude等）。</li>
</ul>

<h3>2. 基础任务执行</h3>

<ul>
  <li>打开WorkBuddy，用自然语言输入任务，如"根据'Reports'文件夹中的文件生成周报"。</li>
  <li>WorkBuddy会自动分解任务、执行并以指定格式交付结果。</li>
</ul>

<h3>3. 使用专家团队</h3>

<ul>
  <li>从专家库中选择"内容创作团队"。</li>
  <li>输入任务，如"帮我确定一款新科技产品的品牌视觉方向"。</li>
  <li>WorkBuddy会先问澄清性问题（产品类别、目标受众、品牌调性），再生成完整品牌策略。</li>
</ul>

<h3>4. 移动端控制</h3>

<ul>
  <li>在WorkBuddy设置中绑定微信账号。</li>
  <li>从微信发送任务，如"收集最新AI行业资讯并保存为Excel文件"。</li>
  <li>WorkBuddy执行任务后将结果发送回微信。</li>
</ul>

<h2 id="why-stands-out">WorkBuddy的独特优势</h2>

<ol>
  <li><strong>本地文件操作</strong>：与云端AI工具不同，WorkBuddy本地运行，确保数据安全和隐私。</li>
  <li><strong>多模型支持</strong>：可根据任务需求切换不同AI模型，避免被单一模型锁定。</li>
  <li><strong>专家团队</strong>：预配置专家团队让你无需额外招聘就能获得专业技能支持。</li>
  <li><strong>移动端控制</strong>：手机控制电脑执行任务，实现远程办公，提升效率。</li>
</ol>

<h2 id="conclusion">总结</h2>

<p>腾讯WorkBuddy是一款强大的AI办公工作台，将AI从聊天工具转变为能执行任务的"同事"。三种工作模式、丰富的技能库、专家团队和移动端控制，帮助职场人士简化日常任务，专注于更有创造性的工作。无论你是文案、开发者还是设计师，WorkBuddy都有工具帮你提升效率。</p>

<h2>常见问题</h2>

<h3>WorkBuddy和Codex、Claude Code有什么不同？</h3>
<p>WorkBuddy是<strong>办公工作台</strong>，不是编码Agent。它针对文档处理、数据整理、PPT制作和多角色内容生产进行了优化——这些是中国职场人士的日常刚需。Codex和Claude Code是开发者优先的工具，编码能力强，但用它们"根据这些Excel生成周报"属于大材小用。WorkBuddy对中国用户还有独特优势：微信移动端控制、原生中文界面、本地文件操作数据不出电脑。把它看作AI工具箱里的办公专家，与编码型Agent互补而非竞争。</p>

<h3>WorkBuddy访问本地文件，我的数据安全吗？</h3>
<p>WorkBuddy在本地运行——文件在你电脑上处理，不会上传到腾讯云端。这是它与需要上传文档到服务器的云端AI办公工具的关键区别。三种工作模式给你精细控制权：只需文本回复时用Ask模式（不访问文件），想先审查执行方案再用Plan模式，只有信任的批量任务才用Craft模式。处理敏感文档时，坚持用Ask和Plan模式。</p>

<h3>WorkBuddy该接哪个AI模型？</h3>
<p>WorkBuddy支持DeepSeek、Kimi、GPT、Claude等。中文办公任务首选DeepSeek或Kimi，性价比最高且中文理解最自然。英文文档或代码密集型任务用GPT-4o或Claude Sonnet效果更好。多模型支持的好处是不被锁定——日常中文报告用DeepSeek，需要高质量英文输出或复杂推理时切换到GPT-4o。</p>

<h3>WorkBuddy能替代团队里的设计师或文案吗？</h3>
<p>不完全能——但它能处理前80%的工作。专家团队功能（内容创作团队含创意总监+文案+设计师）产出的初稿、品牌策略和设计原型质量扎实。它无法替代的是人的判断力：输出是否真正符合品牌调性、是否打动目标受众、是否满足客户未言明的期望。用WorkBuddy消除白纸恐惧和重复性生产工作，然后用人的创造力做打磨和差异化。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>对WorkBuddy感兴趣？探索更多AI办公和Agent工具：</p>
  <ul>
    <li><a href="/articles/2026-ai-agent-guide-choose-right-tool-beginners">2026 AI Agent选型指南：新手如何选择最适合的工具</a> — 对比WorkBuddy与其他Agent选项</li>
    <li><a href="/articles/mastering-ai-workflow-beginner-custom-workbench">掌握AI工作流：打造你的专属AI工作台</a> — 将WorkBuddy集成到更广泛的生产力系统中</li>
    <li><a href="/articles/top-5-ai-ppt-skills-tested-ranked">AI PPT技能大比拼：5款工具实测排名与推荐</a> — 如果PPT制作是你的主要场景</li>
  </ul>
</div>`,
  },

'''

last_brace = content_src.rfind('};')
content_new = content_src[:last_brace] + new_contents + '};'

with open('src/lib/article-content.ts', 'w', encoding='utf-8') as f:
    f.write(content_new)

print('Part 3: 2 article contents added to article-content.ts')

print('\n=== All done! Run build to verify ===')
