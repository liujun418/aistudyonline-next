"""Publish Aug 3, 2026 — 1 article, no new tools."""
import os; BASE = r"C:\Users\jun\aistudyonline-next"; os.chdir(BASE)

with open('src/lib/articles.ts', 'r', encoding='utf-8') as f: s = f.read()
a = r"""  {
    slug: "how-to-build-high-end-ai-personal-workbench-zero-code-workbuddy",
    title: "How to Build a High-End AI Personal Workbench with Zero Code",
    titleZh: "零代码搭建高端AI个人工作台：WorkBuddy完整教程",
    description: "A step-by-step guide to building a custom AI personal workbench in WorkBuddy with zero code — using /finesse-brief (requirement organization) and /finesse-ui (high-end UI generation) Skills, covering pet daily record workbench, AI workbench, and life management workbench examples.",
    descriptionZh: "用WorkBuddy零代码搭建自定义AI个人工作台——使用/finesse-brief（需求整理）和/finesse-ui（高端UI生成）两个技能，含宠物日常记录、AI工作台、生活管理三个实战案例。",
    category: "ai-tutorials",
    tags: ["WorkBuddy", "No-Code", "Workbench", "Personal Dashboard", "Productivity", "UI Design"],
    difficulty: "beginner",
    toolsMentioned: ["Tencent WorkBuddy"],
    date: "2026-08-03",
  },

"""
last = s.rfind('];')
with open('src/lib/articles.ts', 'w', encoding='utf-8') as f: f.write(s[:last] + a + '];')

with open('src/lib/article-content.ts', 'r', encoding='utf-8') as f: c = f.read()
n = r'''
  "how-to-build-high-end-ai-personal-workbench-zero-code-workbuddy": {
    content: `<div class="meta-banner">
  <span class="meta-badge">📖 AI Tutorials</span>
  <span class="meta-badge">🕒 5 min read</span>
  <span class="meta-badge">📅 Aug 3, 2026</span>
  <span class="meta-badge">🎯 Beginner</span>
</div>

<h2 id="introduction">Introduction</h2>
<p>If you want to build a high-end AI personal workbench without writing a single line of code or having any design experience, WorkBuddy is the perfect tool for you. This guide will walk you through the entire process, from opening the app for the first time to creating a fully functional, visually appealing workbench.</p>

<h2 id="what-is">What is WorkBuddy?</h2>
<p>WorkBuddy is an AI tool that allows you to create custom workbenches using natural language. It uses two core Skills: <strong>Workbench Skill</strong> (organizes your workbench requirements) and <strong>UI Skill</strong> (generates a high-quality, visually appealing interface).</p>

<h2 id="step-1">Step 1: Get Started</h2>
<p>Open WorkBuddy. The interface is simple: left sidebar for your project list, right area for the AI conversation where all operations take place.</p>

<h2 id="step-2">Step 2: Create a New Workspace</h2>
<p>Click "New Workspace", name it (e.g., "My AI Workbench"), and confirm.</p>

<h2 id="step-3">Step 3: Use the Skills</h2>
<p>In the input box, type a forward slash (<code>/</code>) to bring up the two Skills. <code>/finesse-brief</code> organizes requirements. <code>/finesse-ui</code> makes the page look high-end.</p>

<h2 id="step-4">Step 4: Organize Your Requirements</h2>
<p>First, use the Workbench Skill to organize requirements. For a pet daily record workbench:</p>
<pre><code class="language-text">/finesse-brief Help me create a pet daily record workbench.</code></pre>
<p>The AI will ask clarifying questions: what to record daily, what to display on the homepage, what to show when no data exists, etc.</p>

<h2 id="step-5">Step 5: Generate the Interface</h2>
<p>Once requirements are organized, type <code>/finesse-ui</code>. The AI will generate a complete page design based on your requirements — every requirement you specified will be reflected.</p>

<h2 id="step-6">Step 6: Compare the Results</h2>
<p>The default AI-generated workbench has a basic design (gray cards, blue buttons, centered titles). The version using the two Skills is high-end, easy to use, with data-driven sizing to show priority.</p>

<h2 id="step-7">Step 7: Make Changes</h2>
<p>After the page is generated, modifying is easy. For example, "Add a vaccine record" — the AI adds it to the existing page without starting over.</p>

<h2 id="step-8">Step 8: Use for Different Topics</h2>
<p>The same process works for any workbench: pet records, AI workbench (chat + workflow + knowledge base layout), life management (today's plan, records, data view).</p>

<h2 id="conclusion">Conclusion</h2>
<p>Building a high-end AI personal workbench is easy with WorkBuddy. No code, no design experience needed. Just three steps: describe what you want, organize requirements, use the UI Skill to generate the interface.</p>

<h2>常见问题</h2>

<h3>How is this different from the July 5 WorkBuddy overview article?</h3>
<p>The July 5 article covers WorkBuddy's <strong>core features</strong> and general capabilities. This article is a <strong>hands-on tutorial</strong> for building a custom workbench using the /finesse-brief and /finesse-ui Skills. The key difference: the July 5 article is "what can WorkBuddy do?" — this article is "how do I build my own workbench in WorkBuddy?" If you haven't read the July 5 article, start there for context. If you're ready to build, this guide covers the exact steps.</p>

<h3>What kinds of workbenches can I build with this method?</h3>
<p>Any data-driven dashboard that tracks and displays information. The article covers three examples: pet daily records, AI workbench (chat + workflow + knowledge base), and life management (plans + records + data). Extend this to project management (task tracking, milestones, team workload), content creation (editorial calendar, publishing pipeline, analytics), or business operations (sales pipeline, customer records, revenue tracking). The pattern is universal: identify what data you want to track, organize the requirements with /finesse-brief, generate the UI with /finesse-ui, and iterate.</p>

<h3>Do I need to know what "/finesse-brief" and "/finesse-ui" do before using them?</h3>
<p>No — the Skills are designed to guide you through the process. When you type /finesse-brief, the AI asks you a series of questions to clarify your requirements. You answer in natural language. When you're done, type /finesse-ui and the AI generates the interface. The two Skills work as a conversation, not a technical interface. The article's step-by-step format is designed for absolute beginners — if you can describe what you want in plain English, you can build the workbench.</p>

<h3>Can I share my workbench with others?</h3>
<p>WorkBuddy supports multi-person project collaboration (covered in the July 24 WorkBuddy tools comparison article). Within a project workspace, team members can share materials, standards, and professional content. The workbench itself is tied to your WorkBuddy account and workspace. For sharing, invite team members to the workspace. The workbench's data, structure, and Skills are then accessible to the team. For read-only sharing (e.g., showing a dashboard to stakeholders), WorkBuddy's export or screenshot features are the current options.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Built your workbench? Explore more WorkBuddy content:</p>
  <ul>
    <li><a href="/articles/tencent-workbuddy-ai-office-workbench">Tencent WorkBuddy: The Ultimate AI Office Workbench</a> — the feature overview companion</li>
    <li><a href="/articles/workbuddy-10-core-skills-beginner-to-advanced">WorkBuddy: 10 Core Skills to Master from Beginner to Advanced</a> — master WorkBuddy's full capabilities</li>
    <li><a href="/articles/practical-guide-tencent-workbuddy-ai-office-assistant">A Practical Guide to Tencent WorkBuddy</a> — hands-on use cases with prompt examples</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">📖 AI 教程</span>
  <span class="meta-badge">🕒 阅读约5分钟</span>
  <span class="meta-badge">📅 2026年8月3日</span>
  <span class="meta-badge">🎯 入门</span>
</div>

<h2 id="introduction">引言</h2>
<p>想不写一行代码、没有任何设计经验就搭建高端AI个人工作台？WorkBuddy是你的完美工具。本指南带你走完从首次打开App到创建功能完整、视觉精美的个人工作台全流程。</p>

<h2 id="what-is">WorkBuddy是什么？</h2>
<p>WorkBuddy是一个AI工具，让你用自然语言创建自定义工作台。它使用两个核心技能：<strong>工作台技能</strong>（整理需求）和<strong>UI技能</strong>（生成高质量视觉界面）。</p>

<h2 id="step-1">第一步：开始</h2>
<p>打开WorkBuddy。界面简洁：左侧边栏是项目列表，右侧是AI对话区，所有操作都在这里完成。</p>

<h2 id="step-2">第二步：创建工作区</h2>
<p>点击"新建工作区"，命名（如"我的AI工作台"），确认创建。</p>

<h2 id="step-3">第三步：使用技能</h2>
<p>在输入框输入斜杠<code>/</code>调出两个技能。<code>/finesse-brief</code>整理需求，<code>/finesse-ui</code>生成高端界面。</p>

<h2 id="step-4">第四步：整理需求</h2>
<p>先使用工作台技能整理需求。以宠物日常记录工作台为例：</p>
<pre><code class="language-text">/finesse-brief 帮我创建一个宠物日常记录工作台。</code></pre>
<p>AI会追问澄清性问题：每天记录什么、首页展示什么、无数据时显示什么、以后每天会用到什么内容。</p>

<h2 id="step-5">第五步：生成界面</h2>
<p>需求整理完成后，输入<code>/finesse-ui</code>。AI根据你的需求生成完整页面设计——每个需求都会体现在界面中。</p>

<h2 id="step-6">第六步：对比效果</h2>
<p>默认AI生成的工作台是基础设计（灰色卡片、蓝色按钮、居中标题）。使用两个技能生成的工作台高端精致、易用、数据驱动大小显示优先级。</p>

<h2 id="step-7">第七步：修改调整</h2>
<p>页面生成后修改很简单。例如"添加疫苗记录"——AI在现有页面添加，无需从头开始。</p>

<h2 id="step-8">第八步：应用于不同主题</h2>
<p>同样流程可用于任何工作台：宠物记录、AI工作台（聊天+工作流+知识库布局）、生活管理（今日计划+记录+数据查看）。</p>

<h2 id="conclusion">总结</h2>
<p>用WorkBuddy搭建高端AI个人工作台简单易行。无需编码、无需设计经验。只需三步：描述需求、整理需求、用UI技能生成界面。</p>

<h2>常见问题</h2>

<h3>这和7月5日的WorkBuddy概览文章有什么不同？</h3>
<p>7月5日文章覆盖WorkBuddy的<strong>核心功能</strong>和通用能力。本文是使用/finesse-brief和/finesse-ui技能搭建自定义工作台的<strong>实操教程</strong>。关键区别：7月5日文章是"WorkBuddy能做什么？"——本文是"怎么在WorkBuddy中搭建自己的工作台？"如果还没读7月5日文章，先读那篇了解背景。准备好动手了，本指南覆盖具体步骤。</p>

<h3>这种方法能搭建什么样的工作台？</h3>
<p>任何追踪和展示信息的数据驱动仪表盘都行。文章涵盖三个案例：宠物日常记录、AI工作台（聊天+工作流+知识库）、生活管理（计划+记录+数据）。扩展到项目管理（任务追踪、里程碑、团队工作量）、内容创作（编辑日历、发布管线、分析）、或业务运营（销售管道、客户记录、收入追踪）。模式通用：识别要追踪的数据→用/finesse-brief整理需求→用/finesse-ui生成UI→迭代优化。</p>

<h3>使用/finesse-brief和/finesse-ui之前需要先了解它们吗？</h3>
<p>不需要——技能设计为引导你完成整个过程。输入/finesse-brief后，AI会问一系列问题澄清需求。你用自然语言回答。完成后输入/finesse-ui，AI生成界面。两个技能是对话方式而非技术接口。文章的分步格式专为纯新手设计——只要能用自然语言描述需求，就能搭建工作台。</p>

<h3>工作台能分享给他人吗？</h3>
<p>WorkBuddy支持多人项目协作（7月24日工具对比文章有介绍）。项目工作区内团队成员可共享素材、标准和专业内容。工作台本身绑定到你的WorkBuddy账号和工作区。分享方式：邀请团队成员到工作区，工作台的数据、结构和技能对团队可访问。只读分享（如向利益相关者展示仪表盘），目前可用WorkBuddy的导出或截图功能。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>建好了工作台？探索更多WorkBuddy内容：</p>
  <ul>
    <li><a href="/articles/tencent-workbuddy-ai-office-workbench">腾讯WorkBuddy：日常办公的终极AI工作台</a> — 功能概览配套篇</li>
    <li><a href="/articles/workbuddy-10-core-skills-beginner-to-advanced">WorkBuddy十大核心技能：从入门到精通</a> — 掌握WorkBuddy完整能力</li>
    <li><a href="/articles/practical-guide-tencent-workbuddy-ai-office-assistant">腾讯WorkBuddy实操指南：一站式AI办公助手完全上手</a> — 含提示词示例的实战场景</li>
  </ul>
</div>`,
  },

'''
last = c.rfind('};')
with open('src/lib/article-content.ts', 'w', encoding='utf-8') as f: f.write(c[:last] + n + '};')
print('Done')