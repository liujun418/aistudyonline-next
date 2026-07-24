"""
Publish July 24, 2026 — 2 articles + 1 new tool (Z-Code).
"""
import os

BASE = r"C:\Users\jun\aistudyonline-next"
os.chdir(BASE)

# ===== Part 1: Add 1 new tool to tools.ts =====
with open('src/lib/tools.ts', 'r', encoding='utf-8') as f:
    tools_src = f.read()

new_tools = r"""
  {
    id: "z-code",
    name: "Z-Code",
    nameZh: "Z码",
    description: "Zhipu AI's desktop AI Agent tool powered by GLM-5.2/GLM-5 models, featuring native Lark and WeChat integration, 500K daily free tokens, and CLI-based agent capabilities for document analysis and PPT generation.",
    descriptionZh: "智谱AI桌面端AI Agent工具，搭载GLM-5.2/GLM-5模型，原生集成飞书和微信，每日50万免费token，CLI驱动的文档分析和PPT生成能力。",
    category: "ai-agent",
    tags: ["ai-agent", "china", "zhipu", "glm", "desktop", "productivity"],
    difficulty: "beginner",
    url: "https://zcode.zhipuai.cn",
    rating: 3.5,
    pricing: "Freemium",
    useCase: "AI-powered desktop agent for Chinese users — document analysis, PPT generation, Lark/WeChat integration, with GLM-5.2 model for daily office tasks",
    icon: "💻",
    company: "Zhipu AI",
    companyZh: "智谱AI",
    founded: 2019,
    headquarters: "Beijing, China",
    descriptionLong: "Z-Code is Zhipu AI's entry into the desktop AI Agent market, powered by their proprietary GLM-5.2 and GLM-5 large language models. It positions itself as a lightweight, domestically-native alternative to Codex and WorkBuddy for Chinese users. The free tier provides 500,000 tokens per day — sufficient for moderate daily use but limiting for heavy workloads. Z-Code's standout features are its native integration with Lark (Feishu) and WeChat, allowing users to trigger AI tasks directly from their daily communication tools. It supports basic Agent capabilities: document analysis, PPT generation, data processing, and code assistance through a CLI interface. However, its skill library is notably smaller than WorkBuddy's, with most available skills developed by Zhipu AI or the open-source community, lacking the third-party developer ecosystem that makes competitors more versatile. For complex multi-step Agent tasks, Z-Code struggles compared to Codex or WorkBuddy. The paid Coding-Plan unlocks GLM-5 advanced models and higher token limits but is frequently out of stock. Z-Code is best suited for users already invested in the Zhipu/GLM ecosystem who need basic desktop Agent capabilities with Lark and WeChat integration, rather than as a primary development Agent tool.",
    descriptionLongZh: "Z-Code（Z码）是智谱AI进军桌面AI Agent市场的产品，搭载其自研GLM-5.2和GLM-5大语言模型。定位为中国用户的轻量级国产Codex和WorkBuddy替代方案。免费层提供每日50万token——中等日常使用足够，但高强度工作受限。Z-Code的突出特性是原生集成飞书和微信，允许用户直接从日常通讯工具触发AI任务。通过CLI界面支持基础Agent能力：文档分析、PPT生成、数据处理和代码辅助。但其技能库明显小于WorkBuddy，大多数可用技能由智谱AI或开源社区开发，缺乏第三方开发者生态。复杂多步骤Agent任务上Z-Code不如Codex或WorkBuddy。付费Coding-Plan解锁GLM-5高级模型和更高token限额，但经常缺货。Z-Code最适合已投入智谱/GLM生态、需要基础桌面Agent能力和飞书/微信集成的用户，而非作为主力开发Agent工具。",
    advantages: ["Native Lark (Feishu) and WeChat integration", "Powered by GLM-5.2 with strong Chinese language performance", "500K daily free tokens for moderate use", "Lightweight CLI interface", "No overseas network or payment required"],
    advantagesZh: ["原生飞书和微信集成", "搭载GLM-5.2，中文能力强", "每日50万免费token中等够用", "轻量级CLI界面", "无需海外网络和支付"],
    useCases: ["Document analysis and summarization", "PPT generation from outlines", "Daily office automation via Lark/WeChat", "Basic code assistance", "Lightweight Agent tasks for GLM ecosystem users"],
    useCasesZh: ["文档分析和摘要", "从大纲生成PPT", "通过飞书/微信进行日常办公自动化", "基础代码辅助", "GLM生态用户轻量Agent任务"],
    targetAudience: "Chinese users already in the Zhipu/GLM ecosystem who need basic desktop Agent capabilities with native Lark and WeChat integration",
    targetAudienceZh: "已使用智谱/GLM生态的中国用户，需要基础桌面Agent能力和原生飞书/微信集成",
    pricingTiers: [
      {
        tier: "Free",
        tierZh: "免费版",
        price: "Free",
        features: ["500K tokens/day", "GLM-5.2 model", "Basic skills library", "Lark/WeChat integration", "CLI interface"],
        featuresZh: ["每日50万token", "GLM-5.2模型", "基础技能库", "飞书/微信集成", "CLI界面"],
      },
      {
        tier: "Coding-Plan",
        tierZh: "编码计划",
        price: "Paid (frequently out of stock)",
        features: ["GLM-5 advanced models", "Higher token limits", "Priority access", "Extended skills"],
        featuresZh: ["GLM-5高级模型", "更高token限额", "优先访问", "扩展技能"],
      },
    ],
    pros: ["Native Chinese ecosystem integration (Lark, WeChat)", "GLM-5.2 strong Chinese language capability", "Free tier usable for moderate daily work", "No overseas access or payment barriers"],
    prosZh: ["原生中文生态集成（飞书、微信）", "GLM-5.2中文能力强", "免费层中等日常可用", "无海外访问和支付障碍"],
    cons: ["Small skill library with limited third-party ecosystem", "Struggles with complex multi-step Agent tasks", "Paid plan frequently out of stock", "Only supports GLM models — no third-party model integration", "Free token limit insufficient for heavy workloads"],
    consZh: ["技能库小、第三方生态有限", "复杂多步骤Agent任务吃力", "付费计划经常缺货", "仅支持GLM模型——无第三方模型集成", "免费token限制不足以应对高强度工作"],
    extensions: [],
    skills: ["Document analysis", "PPT generation", "Data processing", "Code assistance", "Lark/WeChat task triggering"],
    scene: "office-productivity",
  },
"""

last_tool = tools_src.rfind('] as Tool[];')
tools_new = tools_src[:last_tool] + new_tools + '] as Tool[];'

with open('src/lib/tools.ts', 'w', encoding='utf-8') as f:
    f.write(tools_new)

print('Part 1: 1 new tool added (Z-Code)')

# ===== Part 2: Add 2 article metadata to articles.ts =====
with open('src/lib/articles.ts', 'r', encoding='utf-8') as f:
    articles_src = f.read()

new_articles = r"""  {
    slug: "6-popular-ai-agent-tools-reviewed-chinese-beginners-2026",
    title: "6 Popular AI‑Agent Tools Reviewed: Which One Should Chinese Beginners Pick in 2026",
    titleZh: "2026年6款主流AI Agent工具横评：中国新手该选哪个？",
    description: "A practical ranking of 6 AI Agent tools for Chinese beginners — Codex (5/5), WorkBuddy (4/5), Trae & Z-Code (3.5/5), Claude Code (2.5/5), OpenClaw/Hermes (2/5) — with setup steps, pros/cons, and a decision guide based on network/payment accessibility.",
    descriptionZh: "面向中国新手的6款AI Agent工具实用排名——Codex(5/5)、WorkBuddy(4/5)、Trae和Z-Code(3.5/5)、Claude Code(2.5/5)、OpenClaw/Hermes(2/5)——含安装步骤、优缺点和基于网络/支付条件的选型决策指南。",
    category: "AI Tools",
    tags: ["AI Agent", "Tools Comparison", "Codex", "WorkBuddy", "Claude Code", "China", "Beginner"],
    difficulty: "beginner",
    toolsMentioned: ["Codex Agent", "Tencent WorkBuddy", "Claude Code", "TRAE Framework", "Z-Code"],
    date: "2026-07-24",
  },
  {
    slug: "master-ai-driven-development-openspec-practical-guide-beginners",
    title: "Master AI-Driven Development with OpenSpec: A Practical Guide for Beginners",
    titleZh: "用OpenSpec掌握AI驱动开发：新手实操指南",
    description: "A beginner-friendly guide to OpenSpec — a lightweight specification-driven development (SDD) framework that structures AI coding projects through a 4-step workflow (Explore → Generate Docs → Develop → Archive), comparing it with Spec-Kit and Superpowers for different project scales.",
    descriptionZh: "OpenSpec新手实操指南——轻量级规格驱动开发（SDD）框架，通过4步工作流（需求探索→文档生成→开发→归档）结构化AI编码项目，与Spec-Kit和Superpowers的横向对比。",
    category: "AI Tools",
    tags: ["OpenSpec", "SDD", "Specification-Driven Development", "AI Coding", "Framework", "Tutorial"],
    difficulty: "beginner",
    toolsMentioned: ["OpenSpec"],
    date: "2026-07-24",
  },

"""

last_bracket = articles_src.rfind('];')
articles_new = articles_src[:last_bracket] + new_articles + '];'

with open('src/lib/articles.ts', 'w', encoding='utf-8') as f:
    f.write(articles_new)

print('Part 2: 2 articles added')

# ===== Part 3: Add article content =====
with open('src/lib/article-content.ts', 'r', encoding='utf-8') as f:
    content_src = f.read()

new_contents = r'''
  "6-popular-ai-agent-tools-reviewed-chinese-beginners-2026": {
    content: `<div class="meta-banner">
  <span class="meta-badge">🔧 AI Tools</span>
  <span class="meta-badge">🕒 7 min read</span>
  <span class="meta-badge">📅 Jul 24, 2026</span>
  <span class="meta-badge">🎯 Beginner</span>
</div>

<h2 id="introduction">Introduction</h2>

<p>If you are a new-to-AI user based in China, you may feel confused when choosing your first AI-Agent tool. We test six mainstream Agent products, rank them by practicality for domestic beginners, analyze pros, cons and real-world usage limits, and deliver hands-on advice to help you make a wise decision.</p>

<h2 id="rankings">Overall Ranking for Chinese New-comers</h2>

<p>Here is our final score list for reference. Full score is 5.0:</p>

<ol>
  <li><strong>Codex (ChatGPT-powered)</strong>: 5.0/5</li>
  <li><strong>WorkBuddy (Tencent official Agent)</strong>: 4.0/5</li>
  <li><strong>Z-Code & Trae</strong>: 3.5/5 (Tie for third place)</li>
  <li><strong>Claude Code</strong>: 2.5/5</li>
  <li><strong>OpenClaw / Hermes</strong>: 2.0/5</li>
</ol>

<h2 id="codex">1. Codex (Renamed to ChatGPT-Agent Now, Top Recommendation)</h2>

<h3>Core Advantages</h3>

<p>Codex runs on OpenAI's GPT-5.6 series models including Sol, Terra and Luna. Its model performance is comparable with Claude series models, while it comes with lower pricing and much higher token quota. Unlike Claude Code which is built only for developers, Codex fully considers office-workers' daily demands. It has a huge plugin ecosystem for spreadsheets, PPT documents, Figma design and browser automation. Its Agent harness ability, the capability to control large models properly, stays top-tier in the whole industry.</p>

<h3>Practical Setup Steps</h3>
<ol>
  <li>Prepare network access for overseas services and a valid overseas payment method.</li>
  <li>Run this command in your local terminal to install the official desktop client:</li>
</ol>

<pre><code class="language-bash">pip install openai-codex-desktop</code></pre>

<ol start="3">
  <li>Log-in with your ChatGPT account, then enable plugins like <code>Computer-Use</code> from the plugin marketplace.</li>
</ol>

<h3>Disadvantages</h3>
<p>It still has two obvious barriers for Chinese users: you need stable international network access, and it only accepts overseas payment methods for subscription. If you can solve these two problems, Codex is your No.1 choice. If not, skip it and try WorkBuddy instead.</p>

<blockquote><strong>Important Note</strong>: When you connect third-party Chinese models to Codex instead of official GPT models, advanced features such as multi-Agent collaboration and Computer-Use will stop working, and Codex will lose its core advantages.</blockquote>

<h2 id="workbuddy">2. WorkBuddy by Tencent (Best Native-Chinese Option, 4.0/5)</h2>

<h3>Core Highlights</h3>

<p>WorkBuddy is Tencent's official Agent application designed for Chinese users. It supports mainstream open-source Chinese large-models and custom third-party model integration. It connects nearly all Tencent-owned software including WeChat, Lark and QQ. It provides pre-built skills for document processing, Excel analysis, legal consulting and content creation.</p>

<h3>Existing Drawbacks</h3>

<p>The biggest problem comes from its product-design philosophy: it still follows traditional To-C design rather than To-Agent design. For example, the project guideline file is saved as PDF format, which AI cannot parse directly. If you want AI to read instructions automatically, Markdown format is required. Run this code snippet to convert PDF to AI-friendly markdown:</p>

<pre><code class="language-python">from pypdf import PdfReader
def pdf_to_markdown(pdf_path, output_md):
    reader = PdfReader(pdf_path)
    text = "\n".join(page.extract_text() for page in reader.pages)
    with open(output_md,"w",encoding="utf-8") as f:
        f.write(text)
pdf_to_markdown("asset-guide.pdf","asset-guide.md")</code></pre>

<p>In Codex and Claude Code, about 80% of functions run in the background and are called by AI automatically. But for WorkBuddy, users have to manually select every skill. AI cannot choose suitable skills by itself. Also you are not allowed to customize expert agents. Even with these flaws, WorkBuddy is still the top domestic choice for Chinese beginners if Codex is unavailable.</p>

<h2 id="mid-tier">3. Mid-tier Tools: Trae and Z-Code (3.5/5)</h2>

<h3>Trae (Developed by Volcano Engine)</h3>
<p>Trae supports most popular open-source Chinese models and third-party model addition. But its skill library is far smaller than WorkBuddy, and most available skills are developed by Volcano Engine or open-source community contributors. It works fine for basic document analysis and PPT generation but fails on complicated Agent-driven tasks.</p>

<h3>Z-Code by Zhipu AI</h3>
<p>Z-Code only defaults to GLM-5.2 and GLM-5 models. If you want to use advanced versions, you need to subscribe to its paid Coding-Plan, which is frequently out of stock. Free users only get 500,000 tokens per day. Run this command to check your remaining token quota:</p>

<pre><code class="language-bash">zcode quota-check</code></pre>

<p>Its only standout feature is native integration with Lark and WeChat. Apart from that, it has no other competitive advantages. You can pick Z-Code only if you are a big fan of Zhipu's models.</p>

<h2 id="claude-code">4. Claude Code (Only 2.5/5 for Chinese Users)</h2>

<p>Claude Code is the pioneer of modern Agent systems, powered by Fable 5 and Opus 4.8 models, which outperforms GPT-series models in most benchmarks. Its Agent-harness capability sets the industry standard.</p>

<h3>Critical Barriers for Chinese Users</h3>
<ol>
  <li>It needs stable overseas network access.</li>
  <li>It only accepts international payments.</li>
  <li>The strictest restriction from Anthropic: its system continuously detects users' regional information. Once it confirms you are from China, your account will get banned permanently even if you have paid money.</li>
</ol>

<p>Its desktop UI is built for professional developers with full-English interfaces. Most functions are hidden from the graphical interface, making it extremely confusing for new-comers. We do not recommend regular users to try it.</p>

<h2 id="openclaw-hermes">5. OpenClaw / Hermes (2.0/5, Only for Advanced Users)</h2>

<p>OpenClaw and Hermes became popular recently, but they have a steep learning curve. Although desktop versions are available, you must install a standalone app.</p>

<pre><code class="language-bash"># Install Hermes desktop version via command-line
brew install hermes-desktop</code></pre>

<p>It can connect with WeChat and instant-messaging tools so you can assign tasks with one-sentence prompts. However, most users cannot find practical daily scenarios to make full use of its features. Try Codex or WorkBuddy first. Only after you master basic Agent usage should you consider OpenClaw for advanced exploration.</p>

<h2 id="decision-guide">Final Practical Selection Guide</h2>

<ol>
  <li><strong>If you can handle overseas network and payment issues</strong>: choose Codex without hesitation;</li>
  <li><strong>If overseas access is impossible</strong>: WorkBuddy is your primary option;</li>
  <li><strong>If you just want lightweight AI assistance</strong>: pick Trae or Z-Code;</li>
  <li><strong>Avoid Claude Code and OpenClaw at your early-learning stage</strong> to prevent account loss and wasted time.</li>
</ol>

<h2>常见问题</h2>

<h3>Why is Codex ranked #1 for Chinese users despite its access barriers?</h3>
<p>Because if you can overcome the network and payment barriers, Codex delivers objectively the best experience by a wide margin. The GPT-5.6 model family (Sol, Terra, Luna) matches or beats Claude on most benchmarks, the plugin ecosystem covers virtually every office task, and the "approve for me" mode makes Agent automation smooth and safe. The ranking reflects product quality, not accessibility. The guide is explicit: if you can't solve the access issues, skip to #2 WorkBuddy. This isn't a ranking of "easiest to access" — it's a ranking of "best tool for the job if you can use it."</p>

<h3>What's the practical difference between Trae and Z-Code at the same 3.5 rating?</h3>
<p>They're tied because they have complementary strengths and weaknesses. <strong>Trae</strong> supports third-party models (not locked to one provider) but has a tiny skill library. <strong>Z-Code</strong> has native Lark/WeChat integration (genuinely useful for Chinese office workers) but is locked to GLM models and the paid plan is frequently unavailable. Choose Trae if model flexibility matters. Choose Z-Code if you already use Lark/WeChat daily and are in the Zhipu ecosystem. If neither factor matters much to you, WorkBuddy at 4.0/5 is the better pick at a similar accessibility level.</p>

<h3>Is Claude Code really that bad for Chinese users?</h3>
<p>The 2.5/5 rating isn't about Claude Code's quality — it's arguably the most sophisticated Agent system on the market. The rating reflects the catastrophic risk for Chinese users: Anthropic actively detects and bans users from unsupported regions, including China. You can pay for a subscription, use it for weeks, build workflows — and lose everything overnight with a permanent account ban. For developers who understand the risk and use it with appropriate precautions (API-only access via third-party services), Claude Code is excellent. For beginners who might invest time building projects and workflows, the risk of sudden account loss makes it unsuitable. The guide's advice to avoid it at the early-learning stage is a risk-management recommendation, not a quality judgment.</p>

<h3>Can I switch between these tools later, or am I locked in?</h3>
<p>You're not locked in — these tools are independent applications, not platforms with vendor lock-in. Many professionals use multiple tools: Codex for heavy development, WorkBuddy for Chinese office tasks, and Claude Code for specialized coding work. The skills you learn (prompt engineering, workflow design, Agent orchestration) transfer between tools. The guide recommends starting with one tool that matches your access level, mastering it, then adding others as needed. The only thing you can't transfer is project-specific configuration (agent.md files, skill configurations, automation setups) — those are tool-specific and need to be recreated if you switch.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Picked your Agent tool? Master it with these guides:</p>
  <ul>
    <li><a href="/articles/complete-guide-codex-zero-to-advanced">Complete Guide to Codex: From Zero to Advanced</a> — master the #1 ranked tool</li>
    <li><a href="/articles/workbuddy-10-core-skills-beginner-to-advanced">WorkBuddy: 10 Core Skills to Master</a> — get started with the best domestic option</li>
    <li><a href="/articles/mastering-ai-workflow-beginner-custom-workbench">Mastering AI Workflow: Build Your Custom AI Workbench</a> — integrate multiple Agents into one system</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">🔧 AI 工具</span>
  <span class="meta-badge">🕒 阅读约7分钟</span>
  <span class="meta-badge">📅 2026年7月24日</span>
  <span class="meta-badge">🎯 入门</span>
</div>

<h2 id="introduction">引言</h2>

<p>如果你是中国AI新手，选第一款AI Agent工具时可能会感到困惑。我们测试了六款主流Agent产品，按对国内新手的实用性排名，分析优缺点和实际使用限制，提供实操建议帮你做出明智选择。</p>

<h2 id="rankings">中国新手总排名</h2>

<p>最终评分参考，满分5.0：</p>

<ol>
  <li><strong>Codex（ChatGPT驱动）</strong>：5.0/5</li>
  <li><strong>WorkBuddy（腾讯官方Agent）</strong>：4.0/5</li>
  <li><strong>Z-Code和Trae</strong>：3.5/5（并列第三）</li>
  <li><strong>Claude Code</strong>：2.5/5</li>
  <li><strong>OpenClaw / Hermes</strong>：2.0/5</li>
</ol>

<h2 id="codex">1. Codex（现已更名为ChatGPT-Agent，首选推荐）</h2>

<h3>核心优势</h3>

<p>Codex运行在OpenAI GPT-5.6系列的Sol、Terra和Luna模型上。性能与Claude系列不相上下，但价格更低、token配额更高。与仅面向开发者的Claude Code不同，Codex充分考虑职场人士日常需求，拥有电子表格、PPT、Figma设计和浏览器自动化的庞大插件生态。其Agent harness能力——控制大模型的能力——全行业顶级。</p>

<h3>安装步骤</h3>
<ol>
  <li>准备海外网络访问和有效海外支付方式。</li>
  <li>终端运行安装命令：<code>pip install openai-codex-desktop</code></li>
  <li>用ChatGPT账号登录，从插件市场启用Computer-Use等插件。</li>
</ol>

<h3>不足</h3>
<p>对中国用户有两个明显障碍：需要稳定国际网络访问，仅接受海外支付方式。能解决这两个问题，Codex是首选。不能的话跳过选WorkBuddy。</p>

<blockquote><strong>重要提示</strong>：将第三方国产模型接入Codex替代官方GPT模型时，多Agent协作和Computer-Use等高级功能将失效，Codex失去核心优势。</blockquote>

<h2 id="workbuddy">2. WorkBuddy（腾讯出品，国产最佳新手选择，4.0/5）</h2>

<h3>核心亮点</h3>

<p>WorkBuddy是腾讯面向中国用户设计的官方Agent应用。支持主流开源国产大模型和自定义第三方模型集成。连接几乎所有腾讯系软件，包括微信、飞书和QQ。提供文档处理、Excel分析、法律咨询和内容创作的预置技能。多人项目协作功能可拆分任务并追踪AI辅助的项目进度。</p>

<h3>现存问题</h3>

<p>最大问题来自产品设计理念：仍遵循传统To-C设计而非To-Agent设计。例如项目指引文件保存为PDF格式，AI无法直接解析。如需AI自动读取指令，须用Markdown格式。可用Python代码将PDF转为AI友好的markdown（代码见正文）。Codex和Claude Code中约80%功能在后台运行由AI自动调用，但WorkBuddy中用户需手动选择每项技能，AI无法自主选择合适技能，也不允许自定义专家Agent。虽有这些缺陷，若Codex不可用，WorkBuddy仍是中国新手的最佳国产选择。</p>

<h2 id="mid-tier">3. 中游工具：Trae和Z-Code（3.5/5）</h2>

<h3>Trae（火山引擎开发）</h3>
<p>支持大多数流行国产开源模型和第三方模型添加。但技能库远小于WorkBuddy，多数技能由火山引擎或开源社区开发，缺乏第三方开发者资源。基础文档分析和PPT生成还行，复杂Agent驱动任务能力不足。</p>

<h3>Z-Code（智谱AI出品）</h3>
<p>仅默认搭载GLM-5.2和GLM-5模型。高级版本需订阅付费Coding-Plan，但经常缺货。免费用户每日仅50万token。运行<code>zcode quota-check</code>查看剩余配额。唯一亮点是原生集成飞书和微信。除此无其他竞争优势。只有智谱模型的铁粉才适合选Z-Code。</p>

<h2 id="claude-code">4. Claude Code（中国用户仅2.5/5）</h2>

<p>Claude Code是现代Agent系统的先驱，搭载Fable 5和Opus 4.8模型，大多数基准超越GPT系列。Agent-harness能力设定了行业标准。</p>

<h3>中国用户的关键障碍</h3>
<ol>
  <li>需要稳定的海外网络访问。</li>
  <li>仅接受国际支付。</li>
  <li>最严格的限制来自Anthropic：系统持续检测用户地区信息，一旦确认来自中国，即使已付费也会永久封禁账号。</li>
</ol>

<p>桌面UI为专业开发者打造，全英文界面。多数功能隐藏在图形界面之外，对新手极端困惑。不推荐普通用户尝试。</p>

<h2 id="openclaw-hermes">5. OpenClaw / Hermes（2.0/5，仅限进阶用户）</h2>

<p>OpenClaw和Hermes近期流行但学习曲线陡峭。虽有桌面版但需安装独立App。可连接微信和即时通讯工具，一句话提示词分配任务。但多数用户找不到充分发挥其功能的日常场景。建议先用Codex或WorkBuddy，掌握基础Agent用法后再考虑OpenClaw进阶探索。</p>

<h2 id="decision-guide">最终选型指南</h2>

<ol>
  <li><strong>能搞定海外网络和支付</strong>：毫不犹豫选Codex；</li>
  <li><strong>海外访问不可能</strong>：WorkBuddy是首选；</li>
  <li><strong>仅需轻量AI辅助</strong>：选Trae或Z-Code；</li>
  <li><strong>学习早期避免Claude Code和OpenClaw</strong>：防止账号损失和时间浪费。</li>
</ol>

<h2>常见问题</h2>

<h3>Codex有访问障碍为什么还排第一？</h3>
<p>因为如果你能克服网络和支付障碍，Codex在客观上以较大优势提供最佳体验。GPT-5.6模型家族（Sol、Terra、Luna）在大多数基准上匹敌或超越Claude，插件生态几乎覆盖所有办公任务，"approve for me"模式让Agent自动化流畅安全。排名反映产品质量而非可访问性。指南明确说明：搞不定访问问题就跳到第2名WorkBuddy。这不是"最容易访问"的排名——而是"如果能用，哪个工具最好"的排名。</p>

<h3>Trae和Z-Code同样3.5分，实际区别是什么？</h3>
<p>并列因各有互补的优势和短板。<strong>Trae</strong>支持第三方模型（不锁定一家供应商）但技能库极小。<strong>Z-Code</strong>有原生飞书/微信集成（对中国职场人士真正有用）但锁定GLM模型且付费计划经常不可用。模型灵活性重要选Trae。日常已用飞书/微信且在智谱生态中选Z-Code。两个因素都不重要的话，同等可访问性的WorkBuddy 4.0/5更好。</p>

<h3>Claude Code对中国用户真的那么差吗？</h3>
<p>2.5/5的评分不是针对Claude Code的质量——它可能是市面上最复杂的Agent系统。评分反映的是中国用户的灾难性风险：Anthropic主动检测并封禁来自不支持地区（包括中国）的用户。你可能付了费、用了好几周、建了工作流——然后一夜之间全部失去，账号永久封禁。对了解风险并采取适当预防措施的开发者（通过第三方服务仅用API），Claude Code很优秀。对可能花时间构建项目和Workflow的新手，突然账号丢失的风险使其不适合。指南建议学习早期避免，是风险管理建议而非质量判断。</p>

<h3>以后能在这些工具间切换吗，还是会被锁定？</h3>
<p>不会被锁定——这些是独立应用，不是有供应商锁定的平台。很多专业人士使用多个工具：Codex做重型开发、WorkBuddy做中文办公任务、Claude Code做专业编码工作。你学到的技能（提示词工程、工作流设计、Agent编排）在工具间可迁移。指南建议从一款匹配你访问水平的工具开始，掌握后按需添加其他。唯一不能迁移的是项目特定配置（agent.md文件、技能配置、自动化设置）——这些是工具专属的，切换时需重建。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>选好了Agent工具？用这些指南深入掌握：</p>
  <ul>
    <li><a href="/articles/complete-guide-codex-zero-to-advanced">Codex完全指南：从零基础到高级开发工作流</a> — 掌握排名第一的工具</li>
    <li><a href="/articles/workbuddy-10-core-skills-beginner-to-advanced">WorkBuddy十大核心技能：从入门到精通</a> — 入门最佳国产选择</li>
    <li><a href="/articles/mastering-ai-workflow-beginner-custom-workbench">掌握AI工作流：打造你的专属AI工作台</a> — 将多个Agent集成到一个系统</li>
  </ul>
</div>`,
  },

  "master-ai-driven-development-openspec-practical-guide-beginners": {
    content: `<div class="meta-banner">
  <span class="meta-badge">🔧 AI Tools</span>
  <span class="meta-badge">🕒 6 min read</span>
  <span class="meta-badge">📅 Jul 24, 2026</span>
  <span class="meta-badge">🎯 Beginner</span>
</div>

<h2 id="introduction">Introduction</h2>

<p>If you have ever struggled with messy chat logs, lost context, and broken code when working with AI coding tools, this guide will help you solve these problems with <strong>OpenSpec</strong>, a lightweight specification-driven development framework. We will explain how OpenSpec works, how it compares to other popular frameworks, and how you can use it to build stable, maintainable projects with AI.</p>

<h2 id="what-is-sdd">What is Specification-Driven Development?</h2>

<p>Before we dive into OpenSpec, let's understand the core concept: <strong>Specification-Driven Development (SDD)</strong>. This approach ensures that you define clear requirements, designs, and acceptance criteria <em>before</em> writing any code. It solves the common problem of AI forgetting context or breaking existing code when you make changes.</p>

<p>There are two main methodologies: <strong>SDD</strong> (define requirements first, then build) and <strong>TDD</strong> (write tests first, then build). OpenSpec is a flexible SDD framework that forces AI to break down your requirements into three key documents:</p>

<ul>
  <li><strong>Proposal</strong>: Why build this?</li>
  <li><strong>Design</strong>: How to build this?</li>
  <li><strong>Spec</strong>: What to build (with acceptance criteria).</li>
</ul>

<h2 id="workflow">The OpenSpec Workflow: 4 Simple Steps</h2>

<h3>Step 1: Explore Requirements</h3>

<p>Start by describing your idea to AI:</p>

<pre><code class="language-text">Help me build an AI chatbot.</code></pre>

<p>AI will ask follow-up questions: "What frontend framework should we use? Which model should we integrate? What is the project structure?" Answer these to refine your requirements.</p>

<h3>Step 2: Generate Documentation</h3>

<p>Once requirements are clear, AI generates three documents: Proposal, Design, and Spec (with detailed acceptance criteria).</p>

<h3>Step 3: Develop</h3>

<p>AI works through tasks in the Spec document, checking off each item as completed. You can track progress in real time.</p>

<h3>Step 4: Archive</h3>

<p>After development, all documents are archived and changes are merged into a central specification table, ensuring anyone can understand the project's history and current state.</p>

<h2 id="comparison">OpenSpec vs. Other SDD Frameworks</h2>

<table>
  <tr><th>Feature</th><th>OpenSpec</th><th>Spec-Kit</th><th>Superpowers</th></tr>
  <tr><td><strong>Focus</strong></td><td>Lightweight spec management</td><td>Full SDD lifecycle</td><td>Agent behavior constraints</td></tr>
  <tr><td><strong>Use Case</strong></td><td>Small to medium projects</td><td>Large, complex projects</td><td>Ensuring AI follows rules</td></tr>
  <tr><td><strong>Complexity</strong></td><td>Easy to learn</td><td>Steeper learning curve</td><td>Moderate</td></tr>
</table>

<ul>
  <li><strong>OpenSpec</strong>: Best for beginners or small teams — fast setup, flexible.</li>
  <li><strong>Spec-Kit</strong>: Best for large teams or enterprise — enforces complete SDD lifecycle.</li>
  <li><strong>Superpowers</strong>: Best for ensuring AI follows rules and constraints during development.</li>
</ul>

<h2 id="installation">How to Use OpenSpec</h2>

<h3>Installation</h3>

<pre><code class="language-bash">npm install -g openspec</code></pre>

<h3>Basic Commands</h3>

<pre><code class="language-bash"># Initialize a new project
openspec init

# Explore requirements
openspec explore

# Generate documentation
openspec generate

# Develop based on specs
openspec develop

# Archive changes
openspec archive</code></pre>

<h3>Example: Building an AI Learning Assistant</h3>

<ol>
  <li><strong>Explore</strong>: "Help me build an AI learning assistant with a dashboard, study plan CRUD, and user authentication."</li>
  <li><strong>Generate Docs</strong>: AI creates Proposal ("Build an AI learning assistant to track study progress"), Design ("React frontend, Node.js backend, PostgreSQL"), and Spec ("Dashboard should display completed tasks, study plans, and progress charts").</li>
  <li><strong>Develop</strong>: AI implements features, checking off each task.</li>
  <li><strong>Archive</strong>: Documents archived, changes merged.</li>
</ol>

<h2 id="conclusion">Why OpenSpec is Perfect for Beginners</h2>

<ol>
  <li><strong>Low Barrier to Entry</strong>: No advanced technical skills needed.</li>
  <li><strong>Clear Workflow</strong>: The four-step process ensures you never get lost.</li>
  <li><strong>Maintainable Projects</strong>: All changes documented, easy to update or hand off.</li>
  <li><strong>Flexible</strong>: Customize the workflow to fit your needs.</li>
</ol>

<h2>常见问题</h2>

<h3>How is SDD different from just writing good prompts?</h3>
<p>Good prompts produce good single responses. SDD produces good <strong>projects</strong>. The difference is persistence: a well-crafted prompt might generate great code once, but when you come back two weeks later to add a feature, neither you nor the AI remembers the context. SDD solves this by externalizing context into documents (Proposal, Design, Spec) that persist across sessions. When you return to a project, the AI reads the archived specs and understands exactly what was built, why, and what the acceptance criteria were. This is the difference between AI-assisted coding (which works for one-off tasks) and AI-driven development (which works for ongoing projects).</p>

<h3>Do I need to use OpenSpec for every project?</h3>
<p>No. OpenSpec shines for projects that will be worked on over multiple sessions, involve multiple features, or might be handed off to someone else. For one-off scripts or quick experiments, the overhead isn't worth it — just use your AI coding tool directly. A good rule of thumb: if the project will take more than one day of work, use OpenSpec. If it's a single-session task, skip it. The framework is lightweight enough that the setup cost is low (5-10 minutes to generate initial docs), but it's not zero — don't add process for process's sake.</p>

<h3>Can I use OpenSpec with any AI coding tool?</h3>
<p>Yes. OpenSpec is tool-agnostic — it's an npm package that generates and manages specification documents. It works with Claude Code, Codex, Cursor, or any AI coding assistant that can read files from your project. The workflow is the same: run OpenSpec commands to generate docs, then ask your AI tool to read the Proposal/Design/Spec files and implement accordingly. Some tools have built-in OpenSpec integration for smoother workflows, but even without native support, the file-based approach works universally.</p>

<h3>What happens if I change requirements mid-project?</h3>
<p>That's exactly what the archive and spec system is designed for. When requirements change, you run <code>openspec explore</code> again with the new requirements. OpenSpec generates updated Proposal/Design/Spec documents that reference the archived versions, showing what changed and why. The AI then implements only the delta — it doesn't rebuild from scratch. This is the key advantage over ad-hoc AI coding: requirement changes are documented, traceable, and implemented surgically rather than through "let's start over" prompting. The archive ensures you never lose the context of why original decisions were made.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Mastered specification-driven development? Build better AI projects:</p>
  <ul>
    <li><a href="/articles/complete-practical-tutorial-claude-code-core-operations">Complete Practical Tutorial: Master All Core Operations Inside Claude Code</a> — use OpenSpec with your AI coding tool</li>
    <li><a href="/articles/vibe-coding-practical-guide-ai-dev-workflow-part1">Vibe Coding Practical Guide: AI Development Full Workflow (Part 1)</a> — another structured approach to AI development</li>
    <li><a href="/articles/codex-zero-basics-tutorial-part-2-hands-on-guide">Codex Zero-Basics Tutorial Part 2: Hands-On Guide</a> — apply SDD principles in Codex projects</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">🔧 AI 工具</span>
  <span class="meta-badge">🕒 阅读约6分钟</span>
  <span class="meta-badge">📅 2026年7月24日</span>
  <span class="meta-badge">🎯 入门</span>
</div>

<h2 id="introduction">引言</h2>

<p>如果你曾在用AI编码工具时被混乱的聊天记录、丢失的上下文和损坏的代码困扰，本指南将帮你用<strong>OpenSpec</strong>解决这些问题——一个轻量级规格驱动开发框架。我们将讲解OpenSpec的工作原理、与其他流行框架的对比，以及如何用它构建稳定可维护的AI项目。</p>

<h2 id="what-is-sdd">什么是规格驱动开发？</h2>

<p>核心概念：<strong>规格驱动开发（SDD）</strong>——确保在写任何代码<em>之前</em>定义清晰的需求、设计和验收标准。它解决了AI忘记上下文或修改时破坏已有代码的常见问题。</p>

<p>两大方法论：<strong>SDD</strong>（先定义需求再构建）和<strong>TDD</strong>（先写测试再构建）。OpenSpec是灵活的SDD框架，强制AI将需求拆解为三份关键文档：</p>

<ul>
  <li><strong>Proposal（提案）</strong>：为什么构建？</li>
  <li><strong>Design（设计）</strong>：怎么构建？</li>
  <li><strong>Spec（规格）</strong>：构建什么（含验收标准）。</li>
</ul>

<h2 id="workflow">OpenSpec四步工作流</h2>

<h3>第一步：探索需求</h3>
<p>向AI描述你的想法，如"帮我构建一个AI聊天机器人"。AI会追问：用什么前端框架？集成哪个模型？项目结构？回答这些问题完善需求。</p>

<h3>第二步：生成文档</h3>
<p>需求明确后，AI生成Proposal、Design和Spec三份文档。</p>

<h3>第三步：开发</h3>
<p>AI按Spec文档中的任务逐个实现，实时跟踪进度。</p>

<h3>第四步：归档</h3>
<p>开发完成后所有文档归档，变更合并到中央规格表，确保任何人可理解项目历史。</p>

<h2 id="comparison">框架对比</h2>

<table>
  <tr><th>特性</th><th>OpenSpec</th><th>Spec-Kit</th><th>Superpowers</th></tr>
  <tr><td>聚焦</td><td>轻量规格管理</td><td>完整SDD生命周期</td><td>Agent行为约束</td></tr>
  <tr><td>场景</td><td>中小项目</td><td>大型复杂项目</td><td>确保AI遵循规则</td></tr>
  <tr><td>复杂度</td><td>易学</td><td>学习曲线较陡</td><td>中等</td></tr>
</table>

<h2 id="installation">安装使用</h2>

<pre><code class="language-bash">npm install -g openspec

# 初始化新项目
openspec init
# 探索需求
openspec explore
# 生成文档
openspec generate
# 基于规格开发
openspec develop
# 归档变更
openspec archive</code></pre>

<h2 id="conclusion">为什么OpenSpec适合新手</h2>

<ol>
  <li><strong>低门槛</strong>：无需高级技术技能。</li>
  <li><strong>清晰工作流</strong>：四步流程确保不会迷失。</li>
  <li><strong>可维护项目</strong>：所有变更文档化，易于更新或交接。</li>
  <li><strong>灵活</strong>：可自定义工作流适配需求。</li>
</ol>

<h2>常见问题</h2>

<h3>SDD和写好提示词有什么区别？</h3>
<p>好提示词产出好的单次回复。SDD产出好的<strong>项目</strong>。区别在于持久性：精心设计的提示词可能一次生成优秀代码，但两周后回来加功能时，你和AI都忘了上下文。SDD通过将上下文外部化为跨会话持久化的文档（Proposal、Design、Spec）来解决这个问题。当你回到项目，AI读取归档的规格，完全理解构建了什么、为什么构建、验收标准是什么。这是AI辅助编码（适合一次性任务）和AI驱动开发（适合持续项目）的区别。</p>

<h3>每个项目都需要用OpenSpec吗？</h3>
<p>不需要。OpenSpec在跨多会话、涉及多个功能或可能交接给他人的项目上发挥价值。一次性脚本或快速实验不值得这个开销——直接用AI编码工具就好。经验法则：项目需要超过一天工作量就用OpenSpec。单会话任务跳过。框架足够轻量，初始文档生成仅需5-10分钟，但不是零成本——不要为了流程而加流程。</p>

<h3>OpenSpec能用于任何AI编码工具吗？</h3>
<p>可以。OpenSpec与工具无关——它是个npm包，生成和管理规格文档。可与Claude Code、Codex、Cursor或任何能读取项目文件的AI编码助手配合使用。工作流相同：运行OpenSpec命令生成文档，然后让AI工具读取Proposal/Design/Spec文件并实现。部分工具有内置OpenSpec集成提供更流畅体验，但即使没有原生支持，基于文件的方式也能普遍适用。</p>

<h3>项目中途改需求怎么办？</h3>
<p>这正是归档和规格系统的设计目的。需求变更时，用新需求再次运行<code>openspec explore</code>。OpenSpec生成引用归档版本的更新文档，展示变更内容和原因。AI仅实现增量——不从零重建。这是相比临时AI编码的核心优势：需求变更被文档化、可追溯、精准实施，而非靠"从头来过"式提示词。归档确保你永远不会丢失最初决策的上下文。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>掌握了规格驱动开发？构建更好的AI项目：</p>
  <ul>
    <li><a href="/articles/complete-practical-tutorial-claude-code-core-operations">Claude Code完全实战教程：掌握所有核心操作</a> — 将OpenSpec与AI编码工具配合使用</li>
    <li><a href="/articles/vibe-coding-practical-guide-ai-dev-workflow-part1">Vibe Coding实战指南：AI开发完整工作流（上篇）</a> — 另一种结构化AI开发方法</li>
    <li><a href="/articles/codex-zero-basics-tutorial-part-2-hands-on-guide">Codex零基础教程（下）：AI新手实操完全指南</a> — 在Codex项目中应用SDD原则</li>
  </ul>
</div>`,
  },

'''

last_brace = content_src.rfind('};')
content_new = content_src[:last_brace] + new_contents + '};'

with open('src/lib/article-content.ts', 'w', encoding='utf-8') as f:
    f.write(content_new)

print('Part 3: 2 article contents added')
print('\n=== Done ===')