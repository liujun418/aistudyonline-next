"""
Publish July 8, 2026 — 1 article, no new tools.
(Skipped "2026 AI Agent Tool Ranking" — duplicate of July 5 article)
"""
import os

BASE = r"C:\Users\jun\aistudyonline-next"
os.chdir(BASE)

# ===== Part 1: Add 1 article metadata to articles.ts =====
with open('src/lib/articles.ts', 'r', encoding='utf-8') as f:
    articles_src = f.read()

new_articles = r"""  {
    slug: "practical-guide-tencent-workbuddy-ai-office-assistant",
    title: "A Practical Guide to Tencent WorkBuddy: Your All-in-One AI Office Assistant",
    titleZh: "腾讯WorkBuddy实操指南：一站式AI办公助手完全上手",
    description: "A hands-on guide to Tencent WorkBuddy covering installation, interface overview, and 6 practical use cases with specific prompt examples — document generation, data analysis, PPT creation, weekly reports, code development, and design — plus Expert Teams and Skill Library.",
    descriptionZh: "腾讯WorkBuddy上手实操指南，覆盖安装配置、界面概览和6大实战场景（文档生成、数据分析、PPT制作、周报、代码开发、设计创意），每个场景含具体提示词示例，附专家团队和技能库使用说明。",
    category: "AI Tools",
    tags: ["Tencent", "WorkBuddy", "AI Office", "Productivity", "Practical Guide", "China"],
    difficulty: "beginner",
    toolsMentioned: ["Tencent WorkBuddy"],
    date: "2026-07-08",
  },

"""

last_bracket = articles_src.rfind('];')
articles_new = articles_src[:last_bracket] + new_articles + '];'

with open('src/lib/articles.ts', 'w', encoding='utf-8') as f:
    f.write(articles_new)

print('Part 1: 1 new article added to articles.ts')

# ===== Part 2: Add article content to article-content.ts =====
with open('src/lib/article-content.ts', 'r', encoding='utf-8') as f:
    content_src = f.read()

new_contents = r'''
  "practical-guide-tencent-workbuddy-ai-office-assistant": {
    content: `<div class="meta-banner">
  <span class="meta-badge">🔧 AI Tools</span>
  <span class="meta-badge">🕒 7 min read</span>
  <span class="meta-badge">📅 Jul 8, 2026</span>
  <span class="meta-badge">🎯 Beginner</span>
</div>

<h2 id="introduction">Introduction</h2>

<p>Tencent WorkBuddy is an AI-powered office assistant designed to streamline daily work tasks, from document creation to data analysis, PPT generation, and weekly report writing. It integrates with Tencent's ecosystem (WeChat, QQ, Tencent Docs, etc.) to provide a seamless workflow experience. This guide will walk you through its core features, practical use cases, and how to get started.</p>

<h2 id="core-features">Core Features</h2>

<p>WorkBuddy offers three main categories of features:</p>

<ol>
  <li><strong>Daily Office</strong>: Document generation, data analysis, PPT creation, weekly report writing, and email editing.</li>
  <li><strong>Code Development</strong>: Coding assistance, project understanding, and website/application development.</li>
  <li><strong>Design & Creativity</strong>: Product design, PPT design, interactive prototype design, brand design, and poster design.</li>
</ol>

<h2 id="getting-started">Getting Started</h2>

<h3>1. Installation and Setup</h3>

<ul>
  <li>Download WorkBuddy from the official Tencent website.</li>
  <li>Install the application on your computer (supports Windows and macOS).</li>
  <li>Log in with your Tencent account (WeChat/QQ) to sync your existing Tencent ecosystem data.</li>
</ul>

<h3>2. Interface Overview</h3>

<p>WorkBuddy's interface is divided into three main sections:</p>

<ul>
  <li><strong>Left Sidebar</strong>: Quick access to different feature categories (Daily Office, Code Development, Design & Creativity).</li>
  <li><strong>Main Panel</strong>: Displays the current task and AI-generated content.</li>
  <li><strong>Right Sidebar</strong>: Shows task details, history, and collaboration tools.</li>
</ul>

<h2 id="use-cases">Practical Use Cases</h2>

<h3>1. Document Generation</h3>

<p>WorkBuddy can generate various types of documents, such as meeting minutes, project plans, and business proposals.</p>

<ul>
  <li>Example: To generate a meeting minute, simply input:</li>
</ul>

<pre><code class="language-text">Generate a meeting minute for a project kickoff meeting. Include meeting title, date, attendees, agenda, key decisions, and action items.</code></pre>

<ul>
  <li>WorkBuddy will generate a structured document with all required sections.</li>
</ul>

<h3>2. Data Analysis</h3>

<p>WorkBuddy can analyze data from Excel files or databases and generate insights.</p>

<ul>
  <li>Example: To analyze sales data, input:</li>
</ul>

<pre><code class="language-text">Analyze the sales data in this Excel file. Identify top-performing products, regional sales trends, and growth opportunities.</code></pre>

<ul>
  <li>WorkBuddy will generate a detailed report with charts and recommendations.</li>
</ul>

<h3>3. PPT Creation</h3>

<p>WorkBuddy can create professional PPT presentations based on your content.</p>

<ul>
  <li>Example: To create a product launch PPT, input:</li>
</ul>

<pre><code class="language-text">Create a 10-slide PPT for a new product launch. Include product overview, key features, target audience, market analysis, and launch plan.</code></pre>

<ul>
  <li>WorkBuddy will generate a visually appealing PPT with consistent branding.</li>
</ul>

<h3>4. Weekly Report Writing</h3>

<p>WorkBuddy can generate weekly reports based on your work log or project updates.</p>

<ul>
  <li>Example: To generate a weekly report, input:</li>
</ul>

<pre><code class="language-text">Generate a weekly report for the week ending [date]. Include completed tasks, pending tasks, challenges, and next week's plan.</code></pre>

<ul>
  <li>WorkBuddy will generate a structured report with clear sections.</li>
</ul>

<h3>5. Code Development</h3>

<p>WorkBuddy can assist with coding tasks, such as debugging, code review, and feature development.</p>

<ul>
  <li>Example: To debug a Python script, input:</li>
</ul>

<pre><code class="language-text">Debug this Python script. Identify errors and suggest fixes.</code></pre>

<ul>
  <li>WorkBuddy will analyze the code, identify errors, and provide a corrected version.</li>
</ul>

<h3>6. Design & Creativity</h3>

<p>WorkBuddy can assist with design tasks, such as creating posters, logos, and website layouts.</p>

<ul>
  <li>Example: To create a product poster, input:</li>
</ul>

<pre><code class="language-text">Create a poster for a new product launch. Include product image, key features, and call-to-action.</code></pre>

<ul>
  <li>WorkBuddy will generate a high-quality poster with professional design elements.</li>
</ul>

<h2 id="advanced-features">Advanced Features</h2>

<h3>1. Expert Teams</h3>

<p>WorkBuddy offers pre-configured "Expert Teams" for different tasks, such as:</p>

<ul>
  <li><strong>Content Creation Team</strong>: Includes roles like Creative Director, Copywriter, Video Generator, and Graphic Designer.</li>
  <li><strong>Data Analysis Team</strong>: Includes roles like Data Analyst, Statistician, and Report Writer.</li>
  <li><strong>Development Team</strong>: Includes roles like Frontend Developer, Backend Developer, and Tester.</li>
</ul>

<p>To use an Expert Team:</p>
<ol>
  <li>Select the Expert Team from the left sidebar.</li>
  <li>Input your task requirements.</li>
  <li>WorkBuddy will assign tasks to the appropriate team members and generate a final result.</li>
</ol>

<h3>2. Skill Library</h3>

<p>WorkBuddy has a built-in Skill Library with pre-built skills for different tasks, such as:</p>

<ul>
  <li><strong>PPT Generation</strong>: Generates PPTs based on content.</li>
  <li><strong>Data Analysis</strong>: Analyzes data and generates insights.</li>
  <li><strong>Weekly Report Writing</strong>: Generates weekly reports based on work logs.</li>
</ul>

<p>To use a Skill:</p>
<ol>
  <li>Select the Skill from the left sidebar.</li>
  <li>Input your task requirements.</li>
  <li>WorkBuddy will generate a result based on the Skill's logic.</li>
</ol>

<h3>3. Integration with Tencent Ecosystem</h3>

<p>WorkBuddy integrates with Tencent's ecosystem, including:</p>

<ul>
  <li><strong>Tencent Docs</strong>: Syncs with Tencent Docs to access and edit documents.</li>
  <li><strong>Tencent Meeting</strong>: Generates meeting minutes from meeting recordings.</li>
  <li><strong>WeChat</strong>: Sends AI-generated content to WeChat contacts or groups.</li>
</ul>

<h2 id="conclusion">Conclusion</h2>

<p>Tencent WorkBuddy is a powerful AI office assistant that can streamline various work tasks, from document creation to code development. Its integration with Tencent's ecosystem and pre-configured Expert Teams and Skill Library make it a versatile tool for professionals in different fields. By following this guide, you can get started with WorkBuddy and start using it to improve your productivity.</p>

<h2>常见问题</h2>

<h3>What's the difference between this guide and the WorkBuddy overview article?</h3>
<p>This is the <strong>hands-on companion</strong> to the feature overview. The overview article (July 5) covers what WorkBuddy is and why it stands out. This guide focuses on <strong>how to use it</strong> — every section includes concrete prompt examples you can copy and paste. If you've already read the overview and want to start using WorkBuddy today, start here. The two articles are designed to be read together: overview → practical guide → your first automated task.</p>

<h3>Can I use WorkBuddy without connecting it to WeChat or QQ?</h3>
<p>Yes, but you'll miss out on mobile control and ecosystem integration. The core desktop features (document generation, data analysis, PPT creation, code assistance) work without WeChat/QQ binding. Mobile control — sending tasks from your phone and receiving results — requires WeChat, QQ, Feishu, or DingTalk binding. Tencent Docs and Tencent Meeting integration also require ecosystem login. For pure desktop productivity, a standalone login works fine.</p>

<h3>How do I write effective prompts for WorkBuddy?</h3>
<p>WorkBuddy responds best to <strong>structured, specific prompts</strong> with clear output requirements. The examples in this guide follow a proven pattern: (1) State the action verb ("Generate", "Analyze", "Create"), (2) Specify the output format ("a 10-slide PPT", "a meeting minute"), (3) List the required sections or elements. Avoid vague prompts like "help me with sales data" — instead say "Analyze the sales data in this Excel file. Identify top-performing products, regional sales trends, and growth opportunities." The more specific your output requirements, the less manual editing you'll need.</p>

<h3>Which Expert Team should I use for a cross-functional project?</h3>
<p>You can use multiple Expert Teams sequentially. For example, for a product launch: (1) Start with the Content Creation Team to develop the brand strategy and messaging, (2) hand the output to the Design Team for visual assets, (3) use the Development Team if you need a landing page. WorkBuddy doesn't currently support chaining teams automatically, so you'll need to pass outputs between them manually. For smaller projects, the Content Creation Team alone often covers 80% of what you need — it already includes creative director, copywriter, and designer roles.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Ready to put WorkBuddy into action? Explore these related guides:</p>
  <ul>
    <li><a href="/articles/tencent-workbuddy-ai-office-workbench">Tencent WorkBuddy: The Ultimate AI Office Workbench</a> — the feature overview companion to this guide</li>
    <li><a href="/articles/mastering-ai-workflow-beginner-custom-workbench">Mastering AI Workflow: Build Your Custom AI Workbench</a> — integrate WorkBuddy into a broader productivity system</li>
    <li><a href="/articles/2026-ai-agent-guide-choose-right-tool-beginners">2026 AI Agent Guide: How to Choose the Right Tool for Beginners</a> — see how WorkBuddy compares to other AI office tools</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">🔧 AI 工具</span>
  <span class="meta-badge">🕒 阅读约7分钟</span>
  <span class="meta-badge">📅 2026年7月8日</span>
  <span class="meta-badge">🎯 入门</span>
</div>

<h2 id="introduction">引言</h2>

<p>腾讯WorkBuddy是一款AI办公助手，旨在简化从文档创建到数据分析、PPT生成和周报撰写等日常工作。它与腾讯生态（微信、QQ、腾讯文档等）深度集成，提供无缝的工作流体验。本指南将带你了解其核心功能、实战场景和上手步骤。</p>

<h2 id="core-features">核心功能</h2>

<p>WorkBuddy提供三大功能类别：</p>

<ol>
  <li><strong>日常办公</strong>：文档生成、数据分析、PPT制作、周报撰写、邮件编辑。</li>
  <li><strong>代码开发</strong>：编程辅助、项目理解、网站/应用开发。</li>
  <li><strong>设计创意</strong>：产品设计、PPT设计、交互原型设计、品牌设计、海报设计。</li>
</ol>

<h2 id="getting-started">快速上手</h2>

<h3>1. 安装与设置</h3>

<ul>
  <li>从腾讯官网下载WorkBuddy。</li>
  <li>在电脑上安装应用（支持Windows和macOS）。</li>
  <li>用腾讯账号（微信/QQ）登录，同步现有腾讯生态数据。</li>
</ul>

<h3>2. 界面概览</h3>

<p>WorkBuddy界面分为三个主要区域：</p>

<ul>
  <li><strong>左侧边栏</strong>：快速访问不同功能类别（日常办公、代码开发、设计创意）。</li>
  <li><strong>主面板</strong>：显示当前任务和AI生成的内容。</li>
  <li><strong>右侧边栏</strong>：显示任务详情、历史记录和协作工具。</li>
</ul>

<h2 id="use-cases">实战场景</h2>

<h3>1. 文档生成</h3>

<p>WorkBuddy可生成各类文档，如会议纪要、项目计划和商业提案。</p>

<ul>
  <li>示例：生成会议纪要，输入：</li>
</ul>

<pre><code class="language-text">生成一份项目启动会的会议纪要。包含会议标题、日期、参会人员、议程、关键决策和行动项。</code></pre>

<ul>
  <li>WorkBuddy会生成包含所有必要部分的结构化文档。</li>
</ul>

<h3>2. 数据分析</h3>

<p>WorkBuddy可分析Excel文件或数据库中的数据并生成洞察。</p>

<ul>
  <li>示例：分析销售数据，输入：</li>
</ul>

<pre><code class="language-text">分析这个Excel文件中的销售数据。识别表现最好的产品、区域销售趋势和增长机会。</code></pre>

<ul>
  <li>WorkBuddy会生成包含图表和建议的详细报告。</li>
</ul>

<h3>3. PPT制作</h3>

<p>WorkBuddy可根据你的内容创建专业PPT演示文稿。</p>

<ul>
  <li>示例：创建产品发布PPT，输入：</li>
</ul>

<pre><code class="language-text">创建一个10页的新产品发布PPT。包含产品概述、核心功能、目标受众、市场分析和发布计划。</code></pre>

<ul>
  <li>WorkBuddy会生成视觉精美、品牌风格统一的PPT。</li>
</ul>

<h3>4. 周报撰写</h3>

<p>WorkBuddy可根据你的工作日志或项目更新生成周报。</p>

<ul>
  <li>示例：生成周报，输入：</li>
</ul>

<pre><code class="language-text">生成截至[日期]当周的周报。包含已完成任务、待办任务、遇到的挑战和下周计划。</code></pre>

<ul>
  <li>WorkBuddy会生成结构清晰、段落分明的报告。</li>
</ul>

<h3>5. 代码开发</h3>

<p>WorkBuddy可辅助编码任务，如调试、代码审查和功能开发。</p>

<ul>
  <li>示例：调试Python脚本，输入：</li>
</ul>

<pre><code class="language-text">调试这个Python脚本。识别错误并提出修复建议。</code></pre>

<ul>
  <li>WorkBuddy会分析代码，识别错误，提供修正版本。</li>
</ul>

<h3>6. 设计创意</h3>

<p>WorkBuddy可辅助设计任务，如创建海报、Logo和网站布局。</p>

<ul>
  <li>示例：创建产品海报，输入：</li>
</ul>

<pre><code class="language-text">为新产品发布创建一张海报。包含产品图片、核心卖点和行动号召。</code></pre>

<ul>
  <li>WorkBuddy会生成含专业设计元素的高质量海报。</li>
</ul>

<h2 id="advanced-features">高级功能</h2>

<h3>1. 专家团队</h3>

<p>WorkBuddy为不同任务提供预配置的"专家团队"：</p>

<ul>
  <li><strong>内容创作团队</strong>：含创意总监、文案、视频生成、平面设计师等角色。</li>
  <li><strong>数据分析团队</strong>：含数据分析师、统计师和报告撰写人。</li>
  <li><strong>开发团队</strong>：含前端开发、后端开发和测试角色。</li>
</ul>

<p>使用专家团队：</p>
<ol>
  <li>从左侧边栏选择专家团队。</li>
  <li>输入任务需求。</li>
  <li>WorkBuddy会将任务分配给合适的团队成员并生成最终结果。</li>
</ol>

<h3>2. 技能库</h3>

<p>WorkBuddy内置技能库，含预置的各类任务技能：</p>

<ul>
  <li><strong>PPT生成</strong>：基于内容生成PPT。</li>
  <li><strong>数据分析</strong>：分析数据并生成洞察。</li>
  <li><strong>周报撰写</strong>：基于工作日志生成周报。</li>
</ul>

<p>使用技能：</p>
<ol>
  <li>从左侧边栏选择技能。</li>
  <li>输入任务需求。</li>
  <li>WorkBuddy会根据技能逻辑生成结果。</li>
</ol>

<h3>3. 腾讯生态集成</h3>

<p>WorkBuddy与腾讯生态深度集成：</p>

<ul>
  <li><strong>腾讯文档</strong>：同步腾讯文档，访问和编辑文档。</li>
  <li><strong>腾讯会议</strong>：从会议录音生成会议纪要。</li>
  <li><strong>微信</strong>：将AI生成内容发送到微信联系人或群聊。</li>
</ul>

<h2 id="conclusion">总结</h2>

<p>腾讯WorkBuddy是一款强大的AI办公助手，能简化从文档创建到代码开发等各类工作任务。它与腾讯生态的集成以及预配置的专家团队和技能库，使其成为不同领域专业人士的多功能工具。按照本指南，你可以快速上手WorkBuddy，开始用它提升工作效率。</p>

<h2>常见问题</h2>

<h3>这篇指南和之前的WorkBuddy概览文章有什么区别？</h3>
<p>这是概览文章的<strong>实操配套篇</strong>。概览文章（7月5日）介绍WorkBuddy是什么以及为什么它突出。本指南聚焦<strong>怎么用</strong>——每个场景都包含可直接复制粘贴的提示词示例。如果你已经读过概览想今天就开始用WorkBuddy，从这里开始。两篇文章设计为配套阅读：概览→实操指南→你的第一个自动化任务。</p>

<h3>不绑定微信或QQ能用WorkBuddy吗？</h3>
<p>可以，但会失去移动端控制和生态集成功能。核心桌面功能（文档生成、数据分析、PPT制作、代码辅助）无需微信/QQ绑定即可使用。移动端控制——从手机发送任务并接收结果——需要绑定微信、QQ、飞书或钉钉。腾讯文档和腾讯会议集成也需要生态账号登录。纯桌面办公场景，独立登录完全够用。</p>

<h3>怎么写WorkBuddy的提示词效果好？</h3>
<p>WorkBuddy对<strong>结构化、具体、有明确输出要求</strong>的提示词响应最好。本指南中的示例遵循一个验证过的模式：(1) 明确动作动词（"生成""分析""创建"），(2) 指定输出格式（"10页PPT""会议纪要"），(3) 列出所需部分或元素。避免模糊提示词如"帮我处理销售数据"——应该说"分析这个Excel文件中的销售数据，识别表现最好的产品、区域销售趋势和增长机会"。输出要求越具体，需要手动修改的地方越少。</p>

<h3>跨职能项目该用哪个专家团队？</h3>
<p>可以按顺序使用多个专家团队。以产品发布为例：(1) 先用内容创作团队制定品牌策略和文案，(2) 将输出交给设计团队做视觉素材，(3) 如需落地页再用开发团队。WorkBuddy目前不支持自动串联团队，需要手动传递输出。对于较小项目，内容创作团队通常能覆盖80%的需求——它已经包含创意总监、文案和设计师角色。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>准备好让WorkBuddy发挥作用了？探索这些相关指南：</p>
  <ul>
    <li><a href="/articles/tencent-workbuddy-ai-office-workbench">腾讯WorkBuddy：日常办公的终极AI工作台</a> — 本指南的功能概览配套篇</li>
    <li><a href="/articles/mastering-ai-workflow-beginner-custom-workbench">掌握AI工作流：打造你的专属AI工作台</a> — 将WorkBuddy集成到更广泛的生产力系统中</li>
    <li><a href="/articles/2026-ai-agent-guide-choose-right-tool-beginners">2026 AI Agent选型指南：新手如何选择最适合的工具</a> — 看WorkBuddy与其他AI办公工具的对比</li>
  </ul>
</div>`,
  },

'''

last_brace = content_src.rfind('};')
content_new = content_src[:last_brace] + new_contents + '};'

with open('src/lib/article-content.ts', 'w', encoding='utf-8') as f:
    f.write(content_new)

print('Part 2: 1 article content added to article-content.ts')

print('\n=== All done! Run build to verify ===')