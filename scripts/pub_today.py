"""
Publish July 11, 2026 — 2 articles, no new tools.
"""
import os

BASE = r"C:\Users\jun\aistudyonline-next"
os.chdir(BASE)

# ===== Part 1: Add 2 article metadata to articles.ts =====
with open('src/lib/articles.ts', 'r', encoding='utf-8') as f:
    articles_src = f.read()

new_articles = r"""  {
    slug: "chatgpt-codex-10-core-features-beginners-work-efficiency",
    title: "ChatGPT Codex: 10 Core Features for Beginners to Boost Work Efficiency",
    titleZh: "ChatGPT Codex：新手必学的10个核心提效功能",
    description: "A practical guide to ChatGPT Codex's 10 most useful features — batch file renaming, data analysis with charts, doc-to-web conversion, local file memory, scheduled automation, plugin ecosystem, PPT creation, system cleanup, hand-drawn flowcharts, and article formatting — each with example commands.",
    descriptionZh: "ChatGPT Codex十大实用功能实操指南——批量文件重命名、数据图表分析、文档转网页、本地文件记忆、定时自动化、插件生态、PPT制作、系统清理、手绘流程图和文章格式化，每个功能含示例指令。",
    category: "AI Tools",
    tags: ["ChatGPT", "Codex", "Productivity", "Automation", "Beginner", "Tutorial"],
    difficulty: "beginner",
    toolsMentioned: ["ChatGPT", "Codex Agent"],
    date: "2026-07-11",
  },
  {
    slug: "lightweight-ai-transformation-traditional-business-workbuddy-cordys-crm",
    title: "Lightweight AI Transformation for Traditional Business Systems: WorkBuddy + Cordys CRM Skills",
    titleZh: "传统业务系统轻量级AI改造方案：WorkBuddy + Cordys CRM技能实战",
    description: "A practical enterprise AI transformation blueprint using a three-layer architecture — WorkBuddy (AI entry), Business Skills (capability encapsulation), and Existing Systems (Cordys CRM) — with detailed Skill file anatomy, import process, and web/mobile demonstrations.",
    descriptionZh: "企业AI改造实战方案：三层架构——WorkBuddy（AI入口）+ 业务技能（能力封装）+ 现有系统（Cordys CRM），含Skill文件逐项拆解、导入流程和网页/移动端实操演示。",
    category: "AI Use Cases",
    tags: ["WorkBuddy", "Enterprise", "CRM", "Skills", "Digital Transformation", "Business"],
    difficulty: "intermediate",
    toolsMentioned: ["Tencent WorkBuddy"],
    date: "2026-07-11",
  },

"""

last_bracket = articles_src.rfind('];')
articles_new = articles_src[:last_bracket] + new_articles + '];'

with open('src/lib/articles.ts', 'w', encoding='utf-8') as f:
    f.write(articles_new)

print('Part 1: 2 new articles added to articles.ts')

# ===== Part 2: Add article content to article-content.ts =====
with open('src/lib/article-content.ts', 'r', encoding='utf-8') as f:
    content_src = f.read()

new_contents = r'''
  "chatgpt-codex-10-core-features-beginners-work-efficiency": {
    content: `<div class="meta-banner">
  <span class="meta-badge">🔧 AI Tools</span>
  <span class="meta-badge">🕒 7 min read</span>
  <span class="meta-badge">📅 Jul 11, 2026</span>
  <span class="meta-badge">🎯 Beginner</span>
</div>

<h2 id="introduction">Introduction</h2>

<p>ChatGPT Codex is now integrated with GPT, creating a powerful AI tool that simplifies daily tasks. This guide will walk you through its new interface and 10 practical features that can help you work smarter, not harder.</p>

<h2 id="interface">New Interface Overview</h2>

<p>The updated ChatGPT desktop app features a clean, intuitive layout:</p>

<ul>
  <li><strong>Top Left Corner</strong>: Toggle between <strong>Work</strong> and <strong>Codex</strong> modes</li>
  <li><strong>Bottom Right Corner</strong>: Monitor your remaining TOKEN usage</li>
  <li><strong>Left Sidebar</strong>: Access your past conversations and projects</li>
</ul>

<p>This design makes it easy to switch between different work modes and track your usage.</p>

<h2 id="features">10 Core Features for Daily Use</h2>

<h3>1. Automate Repetitive Office Tasks</h3>

<p>Codex can handle tedious tasks like:</p>
<ul>
  <li><strong>Batch file renaming</strong>: Organize files with consistent naming conventions</li>
  <li><strong>Table organization</strong>: Clean up messy spreadsheets</li>
  <li><strong>Data categorization</strong>: Sort information into logical groups</li>
  <li><strong>Script writing</strong>: Automate tasks like network latency checks</li>
</ul>

<p><strong>Example Command</strong>:</p>
<pre><code class="language-text">Rename all files in the "Q3 Reports" folder using the format: [Date] - [Report Type] - [Department]</code></pre>

<h3>2. Data and Chart Analysis</h3>

<p>Transform raw data into actionable insights:</p>
<ul>
  <li>Upload dozens of receipts or complex Excel spreadsheets</li>
  <li>Let Codex analyze for anomalies and trends</li>
  <li>Generate professional reports with visualizations</li>
</ul>

<p><strong>Example Command</strong>:</p>
<pre><code class="language-text">Analyze the Q3 sales spreadsheet, identify anomalies, and create a trend report with charts</code></pre>

<h3>3. One-Click Document to Website Conversion</h3>

<p>Turn written documents into interactive web pages:</p>
<ul>
  <li>Convert proposals, reports, or presentations into shareable web pages</li>
  <li>Preview applications before deployment</li>
  <li>Easily share with colleagues or clients</li>
</ul>

<p><strong>Example Command</strong>:</p>
<pre><code class="language-text">Convert the "Project Proposal.docx" into an interactive web page with a modern design</code></pre>

<h3>4. Local File Access and Persistent Memory</h3>

<p>Codex works with your local files and remembers your preferences:</p>
<ul>
  <li>Files stay on your computer (no cloud uploads)</li>
  <li>AI learns your preferences over time</li>
  <li>Remembers corrections and adapts to your workflow</li>
</ul>

<p><strong>Example Command</strong>:</p>
<pre><code class="language-text">Remember my preference for using "YYYY-MM-DD - [Project Name]" format for file naming</code></pre>

<h3>5. Scheduled Automation Tasks</h3>

<p>Set up tasks to run automatically:</p>
<ul>
  <li>Schedule daily reports to be generated and updated</li>
  <li>Let Codex work while you sleep</li>
  <li>No need to manually trigger tasks</li>
</ul>

<p><strong>Example Command</strong>:</p>
<pre><code class="language-text">Every weekday at 8 AM, analyze the sales data and update the dashboard</code></pre>

<h3>6. Plugin Ecosystem Integration</h3>

<p>Connect Codex with your favorite tools: Chrome, GitHub, Figma, Notion, Gmail, and many more.</p>

<p><strong>Example Command</strong>:</p>
<pre><code class="language-text">Connect to my GitHub account and automatically create a PR when I push changes</code></pre>

<h3>7. Create Professional Presentations</h3>

<p>Generate beautiful presentations from documents:</p>
<ul>
  <li>Input a document and get a polished PPT</li>
  <li>Choose from different color schemes and styles</li>
  <li>Download and edit easily</li>
</ul>

<p><strong>Example Command</strong>:</p>
<pre><code class="language-text">Create a presentation from the "Q3 Business Review.docx" using a professional blue color scheme</code></pre>

<h3>8. Automatic System Cleanup</h3>

<p>Free up disk space safely:</p>
<ul>
  <li>Scan for leftover files and cache</li>
  <li>Identify unnecessary files</li>
  <li>Release several gigabytes of storage</li>
  <li>Always remember to back up before cleaning</li>
</ul>

<p><strong>Example Command</strong>:</p>
<pre><code class="language-text">Scan my system for unnecessary files and cache, then safely clean them up</code></pre>

<h3>9. Hand-Drawn Style Flowcharts</h3>

<p>Create visual diagrams from text:</p>
<ul>
  <li>Input your ideas and Codex breaks them into nodes</li>
  <li>Generate editable hand-drawn style flowcharts</li>
  <li>Perfect for process documentation</li>
</ul>

<p><strong>Example Command</strong>:</p>
<pre><code class="language-text">Create a hand-drawn style flowchart showing the customer onboarding process</code></pre>

<h3>10. Automatic Article Formatting and Image Suggestions</h3>

<p>Great for content creators:</p>
<ul>
  <li>Input long articles and get formatted HTML</li>
  <li>AI suggests relevant images</li>
  <li>Easily adjust formatting without regenerating</li>
</ul>

<p><strong>Example Command</strong>:</p>
<pre><code class="language-text">Format the "Product Launch Article.docx" into HTML and suggest 5 relevant images</code></pre>

<h2 id="conclusion">Conclusion</h2>

<p>With Codex, you don't need to learn multiple AI tools. Just tell Codex what you want to accomplish, and it will handle the execution. The future of AI is becoming simpler — you just need to speak your mind, and AI will do the work. Stay tuned for more AI tutorials and tips to help you work smarter!</p>

<h2>常见问题</h2>

<h3>Which of these 10 features should I learn first?</h3>
<p>Start with the three that give you the fastest ROI: <strong>Batch file renaming</strong> (saves 10-30 minutes every time you organize a messy folder), <strong>Data and chart analysis</strong> (turns hours of spreadsheet work into a 30-second prompt), and <strong>PPT creation</strong> (eliminates the most universally dreaded office task). These three alone can save 3-5 hours per week for most office workers. Once those feel natural, add scheduled automation to handle recurring tasks while you sleep.</p>

<h3>How is ChatGPT Codex different from the standalone Codex app?</h3>
<p>ChatGPT Codex is the integration of Codex capabilities directly into the ChatGPT desktop app — you can toggle between "Work" mode (standard ChatGPT) and "Codex" mode (agent capabilities) in the top-left corner. The standalone Codex app is a separate download focused purely on agent tasks. For beginners, the integrated version is easier: one app, one subscription, and you can switch modes depending on whether you need a chatbot or an agent. The standalone app is preferred by developers who want Codex as their primary workspace.</p>

<h3>Are my files safe when Codex accesses them locally?</h3>
<p>Yes. Codex's local file access means files stay on your computer — they are not uploaded to OpenAI's cloud. This is different from ChatGPT's web interface where you upload files to the server. Codex reads and processes files locally, similar to how a desktop app like Excel or Photoshop works. For sensitive business documents, this is a significant privacy advantage. The persistent memory feature also stores preferences locally, not in the cloud.</p>

<h3>Can I combine multiple features in one task?</h3>
<p>Yes, and that's where Codex really shines. A typical workflow might be: (1) analyze the Q3 sales spreadsheet (feature 2), (2) create a presentation from the analysis (feature 7), (3) convert the presentation to a web page for sharing (feature 3), and (4) schedule this entire workflow to run every Monday morning (feature 5). You can chain these in a single conversation or set up an automation that runs them sequentially. The plugin ecosystem (feature 6) lets you extend this further — for example, auto-emailing the final web page to your team via Gmail.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Mastered the 10 core features? Deepen your Codex skills:</p>
  <ul>
    <li><a href="/articles/codex-zero-basics-tutorial-part-2-hands-on-guide">Codex Zero-Basics Tutorial Part 2: Hands-On Guide for AI Beginners</a> — more hands-on Codex projects</li>
    <li><a href="/articles/official-tutorial-three-ways-codex-control-computer">Official Tutorial: Three Ways Codex Can Control Your Computer</a> — master Computer Use, Chrome Extension, and In-App Browser</li>
    <li><a href="/articles/complete-guide-codex-zero-to-advanced">Complete Guide to Codex: From Zero to Advanced</a> — the full developer-oriented Codex path</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">🔧 AI 工具</span>
  <span class="meta-badge">🕒 阅读约7分钟</span>
  <span class="meta-badge">📅 2026年7月11日</span>
  <span class="meta-badge">🎯 入门</span>
</div>

<h2 id="introduction">引言</h2>

<p>ChatGPT Codex现已与GPT集成，打造了一个能简化日常任务的强大AI工具。本指南将带你了解新界面和10个实用功能，帮你更聪明地工作。</p>

<h2 id="interface">新界面概览</h2>

<p>更新后的ChatGPT桌面应用拥有简洁直观的布局：</p>

<ul>
  <li><strong>左上角</strong>：在<strong>Work</strong>和<strong>Codex</strong>模式间切换</li>
  <li><strong>右下角</strong>：监控剩余TOKEN用量</li>
  <li><strong>左侧边栏</strong>：访问历史对话和项目</li>
</ul>

<p>这个设计让你能轻松切换工作模式并追踪用量。</p>

<h2 id="features">10个日常核心功能</h2>

<h3>1. 自动化重复办公任务</h3>

<p>Codex能处理繁琐任务：</p>
<ul>
  <li><strong>批量文件重命名</strong>：用统一命名规范整理文件</li>
  <li><strong>表格整理</strong>：清理混乱的电子表格</li>
  <li><strong>数据分类</strong>：将信息归类到逻辑分组</li>
  <li><strong>脚本编写</strong>：自动化网络延迟检查等任务</li>
</ul>

<p><strong>示例指令</strong>：</p>
<pre><code class="language-text">将"Q3报告"文件夹中的所有文件重命名，格式为：[日期] - [报告类型] - [部门]</code></pre>

<h3>2. 数据与图表分析</h3>

<p>将原始数据转化为可操作洞察：</p>
<ul>
  <li>上传数十张收据或复杂Excel表格</li>
  <li>让Codex分析异常和趋势</li>
  <li>生成带可视化图表的专业报告</li>
</ul>

<p><strong>示例指令</strong>：</p>
<pre><code class="language-text">分析Q3销售表格，识别异常，创建带图表的趋势报告</code></pre>

<h3>3. 一键文档转网页</h3>

<p>将书面文档转化为交互式网页：</p>
<ul>
  <li>将提案、报告或演示转为可分享的网页</li>
  <li>部署前预览应用</li>
  <li>轻松分享给同事或客户</li>
</ul>

<p><strong>示例指令</strong>：</p>
<pre><code class="language-text">将"项目方案.docx"转化为现代设计风格的交互式网页</code></pre>

<h3>4. 本地文件访问与持久记忆</h3>

<p>Codex处理本地文件并记住你的偏好：</p>
<ul>
  <li>文件留在电脑上（无需上传云端）</li>
  <li>AI随时间学习你的偏好</li>
  <li>记住纠正内容并适应你的工作流</li>
</ul>

<p><strong>示例指令</strong>：</p>
<pre><code class="language-text">记住我的文件命名偏好：使用"YYYY-MM-DD - [项目名称]"格式</code></pre>

<h3>5. 定时自动化任务</h3>

<p>设置任务自动运行：</p>
<ul>
  <li>安排每日报告自动生成和更新</li>
  <li>让Codex在你睡觉时工作</li>
  <li>无需手动触发任务</li>
</ul>

<p><strong>示例指令</strong>：</p>
<pre><code class="language-text">每个工作日上午8点，分析销售数据并更新仪表盘</code></pre>

<h3>6. 插件生态集成</h3>

<p>将Codex连接到你喜欢的工具：Chrome、GitHub、Figma、Notion、Gmail等。</p>

<p><strong>示例指令</strong>：</p>
<pre><code class="language-text">连接我的GitHub账号，当我推送更改时自动创建PR</code></pre>

<h3>7. 创建专业演示文稿</h3>

<p>从文档生成精美PPT：</p>
<ul>
  <li>输入文档，获得精良PPT</li>
  <li>选择不同配色方案和风格</li>
  <li>轻松下载和编辑</li>
</ul>

<p><strong>示例指令</strong>：</p>
<pre><code class="language-text">用"Q3业务回顾.docx"创建演示文稿，使用专业蓝色配色方案</code></pre>

<h3>8. 自动系统清理</h3>

<p>安全释放磁盘空间：</p>
<ul>
  <li>扫描残留文件和缓存</li>
  <li>识别不必要的文件</li>
  <li>释放数GB存储空间</li>
  <li>清理前务必先备份</li>
</ul>

<p><strong>示例指令</strong>：</p>
<pre><code class="language-text">扫描系统中的不必要文件和缓存，然后安全清理</code></pre>

<h3>9. 手绘风格流程图</h3>

<p>从文本创建可视化图表：</p>
<ul>
  <li>输入你的想法，Codex拆解为节点</li>
  <li>生成可编辑的手绘风格流程图</li>
  <li>非常适合流程文档</li>
</ul>

<p><strong>示例指令</strong>：</p>
<pre><code class="language-text">创建一张手绘风格流程图，展示客户入职流程</code></pre>

<h3>10. 自动文章格式化与图片建议</h3>

<p>内容创作者的福音：</p>
<ul>
  <li>输入长文，获得格式化HTML</li>
  <li>AI推荐相关图片</li>
  <li>轻松调整格式无需重新生成</li>
</ul>

<p><strong>示例指令</strong>：</p>
<pre><code class="language-text">将"产品发布文章.docx"格式化为HTML，并推荐5张相关图片</code></pre>

<h2 id="conclusion">总结</h2>

<p>有了Codex，你不需要学习多个AI工具。只需告诉Codex你想完成什么，它会处理执行。AI的未来正变得越来越简单——你只需说出想法，AI会完成工作。敬请期待更多AI教程和技巧，帮你更聪明地工作！</p>

<h2>常见问题</h2>

<h3>这10个功能应该先学哪个？</h3>
<p>从回报最快的三个开始：<strong>批量文件重命名</strong>（每次整理混乱文件夹节省10-30分钟）、<strong>数据图表分析</strong>（将数小时表格工作变成30秒提示词）和<strong>PPT制作</strong>（消除最普遍令人头疼的办公任务）。仅这三项就能为大多数职场人士每周节省3-5小时。熟练后，加上定时自动化在你睡觉时处理重复任务。</p>

<h3>ChatGPT Codex和独立Codex App有什么区别？</h3>
<p>ChatGPT Codex是将Codex能力直接集成到ChatGPT桌面应用中——你可以在左上角切换"Work"模式（标准ChatGPT）和"Codex"模式（Agent能力）。独立Codex App是专注于Agent任务的单独下载。对新手来说，集成版更简单：一个应用、一个订阅，根据是需要聊天机器人还是Agent来切换模式。独立App更受将Codex作为主力工作区的开发者青睐。</p>

<h3>Codex访问本地文件时我的数据安全吗？</h3>
<p>安全。Codex的本地文件访问意味着文件留在你的电脑上——不会上传到OpenAI云端。这不同于ChatGPT网页版需要上传文件到服务器。Codex在本地读取和处理文件，类似Excel或Photoshop等桌面应用的工作方式。对于敏感商业文档，这是显著的隐私优势。持久记忆功能同样在本地存储偏好，而非云端。</p>

<h3>能在一个任务中组合多个功能吗？</h3>
<p>可以，而且这是Codex真正出彩的地方。一个典型工作流可能是：(1) 分析Q3销售表格（功能2），(2) 基于分析创建演示文稿（功能7），(3) 将演示转为网页分享（功能3），(4) 设定整个流程每周一早上自动运行（功能5）。你可以在单次对话中串联这些步骤，或设置自动化顺序执行。插件生态（功能6）让你进一步扩展——比如自动将最终网页通过Gmail发送给团队。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>掌握了10个核心功能？深化你的Codex技能：</p>
  <ul>
    <li><a href="/articles/codex-zero-basics-tutorial-part-2-hands-on-guide">Codex零基础教程（下）：AI新手实操完全指南</a> — 更多Codex实战项目</li>
    <li><a href="/articles/official-tutorial-three-ways-codex-control-computer">官方教程：Codex控制电脑的三种方式详解</a> — 掌握Computer Use、Chrome扩展和内置浏览器</li>
    <li><a href="/articles/complete-guide-codex-zero-to-advanced">Codex完全指南：从零基础到高级开发工作流</a> — 面向开发者的完整Codex路径</li>
  </ul>
</div>`,
  },

  "lightweight-ai-transformation-traditional-business-workbuddy-cordys-crm": {
    content: `<div class="meta-banner">
  <span class="meta-badge">💼 AI Use Cases</span>
  <span class="meta-badge">🕒 9 min read</span>
  <span class="meta-badge">📅 Jul 11, 2026</span>
  <span class="meta-badge">🎯 Intermediate</span>
</div>

<h2 id="introduction">Introduction</h2>

<p>With the rapid development of large language models and AI agent technologies, more and more enterprises are starting to ask: How can AI truly integrate into business operations, rather than just being a chatbot? In this guide, we will use Cordys CRM as an example to introduce a practical lightweight AI transformation solution: <strong>WorkBuddy + Business Skills</strong>.</p>

<p>This solution allows enterprises to avoid rebuilding existing systems from scratch. Instead, you can gradually encapsulate business capabilities into Skills, enabling AI to participate in business processes quickly and efficiently.</p>

<h2 id="architecture">The Three-Layer Architecture</h2>

<p>The solution can be broken down into three core layers:</p>

<ol>
  <li><strong>Top Layer: WorkBuddy</strong> — Responsible for understanding user queries, interacts with large language models, acts as the unified AI entry point for the entire system.</li>
  <li><strong>Middle Layer: Business Skills</strong> — Encapsulates the enterprise's existing business capabilities, enables AI to understand which business interfaces to call, defines which business operations to perform.</li>
  <li><strong>Bottom Layer: Existing Business Systems</strong> — For example, the Cordys CRM system. Retains all original business logic and data.</li>
</ol>

<p>This architecture means enterprises do not need to rebuild their existing systems. Instead, they can gradually encapsulate business capabilities into Skills, allowing AI to participate in business quickly.</p>

<h2 id="workbuddy-functions">WorkBuddy Core Functions</h2>

<p>WorkBuddy is an AI-native desktop intelligent agent workspace designed to help users complete tasks through natural language interaction. Here are its core functions:</p>

<h3>1. New Task Creation</h3>
<ul>
  <li>Core dialogue area for publishing and processing tasks</li>
  <li>Supports multiple tasks running simultaneously</li>
</ul>

<h3>2. Assistant Function</h3>
<ul>
  <li>Enables remote control capabilities</li>
  <li>Integrates with common chat software: WeChat, QQ, Feishu, DingTalk</li>
  <li>Allows mobile remote control of PC-side WorkBuddy tasks</li>
</ul>

<h3>3. Project Function</h3>
<ul>
  <li>Focuses on team collaboration</li>
  <li>Two-layer architecture: Projects and Tasks</li>
  <li>Teams can share materials, standards, and professional content</li>
</ul>

<h3>4. Expert Module</h3>
<ul>
  <li>Divided into Expert Center and My Experts</li>
  <li>Expert Center allows filtering experts by industry</li>
  <li>My Experts allows users to create their own exclusive experts</li>
</ul>

<h3>5. Skill Function</h3>
<ul>
  <li>The most important function in this solution</li>
  <li>Skills continuously expand WorkBuddy's capabilities</li>
  <li>Integrates scripts, workflows, and third-party APIs</li>
  <li>Not only answers questions but also performs actual business operations</li>
  <li>Achieves the upgrade from "can chat" to "can work"</li>
</ul>

<h3>6. Automation Function</h3>
<ul>
  <li>Set rules for automatic processing of repetitive tasks</li>
  <li>Examples: daily AI news push, weekly work reports, regular data organization</li>
  <li>Automatically saves output files to specified folders</li>
</ul>

<h2 id="cordys-crm">Cordys CRM System Overview</h2>

<p>Cordys CRM is a customer relationship management system designed for enterprise customer management. It covers the entire sales process from lead acquisition, customer management, opportunity tracking, to contracts and orders, helping enterprises achieve digital management of sales operations.</p>

<p>Beyond traditional CRM functions, Cordys CRM deeply integrates AI capabilities: AI-assisted customer creation, opportunity management, follow-up record generation, integrated BI data analysis, visual dashboards, and data-driven business decision support.</p>

<h2 id="skill-anatomy">Anatomy of a Skill File</h2>

<p>Many users find Skill files intimidating at first glance, but they only need to focus on a few key parts:</p>

<h3>1. Basic Information</h3>
<p>Defines the Skill's name, function description, and runtime environment. The <code>description</code> field is particularly important, as it tells AI what tasks to perform.</p>

<h3>2. Role Setting</h3>
<p>Clearly defines the AI's role (e.g., "Cordys CRM business assistant"). Determines how AI responds to questions and ensures AI provides analysis and suggestions rather than just raw data.</p>

<h3>3. Execution Flow</h3>
<p>When a user sends a message, AI: (1) determines the user's intent, (2) selects the appropriate processing logic based on the business scenario, (3) generates the final result. Skills function as complete business workflows, not just simple prompts.</p>

<h3>4. On-Demand Loading</h3>
<p>Enterprise-level Skills do not load all functions at once. Dynamically loads modules based on current tasks. Example: Load query engine for data queries, statistical engine for analysis. Improves response speed and resource efficiency.</p>

<h3>5. Query Rules</h3>
<p>Defines how AI constructs CRM query commands — which fields to query, time ranges, and role-based data access. Acts as the communication rules between AI and CRM systems.</p>

<h3>6. Output Specifications</h3>
<p>AI cannot directly return raw API data. Must summarize key points first, then display core data. Provides exception alerts and processing suggestions. Ensures professional, business-appropriate responses.</p>

<h3>7. Execution Capabilities</h3>
<p>Skills can perform actual business operations: create customers, update opportunities, fill in follow-up records, approve workflows. AI is not just a question-answering tool but a business execution assistant.</p>

<h3>8. Security Mechanisms</h3>
<p>Strict security rules for enterprise data protection. Prohibits output of sensitive information like API keys. Masks sensitive information in error messages.</p>

<h2 id="skill-import">Skill Import Process</h2>

<h3>Method 1: Direct Import</h3>
<ol>
  <li>Click "Skills" → "Import Skills"</li>
  <li>Upload the Skill installation package</li>
  <li>You can obtain source files from GitHub repositories</li>
</ol>

<h3>Method 2: Expert Function Import</h3>
<ol>
  <li>Click "Expert" → "Skills"</li>
  <li>Search for "Cordys CRM" in the search box</li>
  <li>Click "SkillHub" → "Add"</li>
  <li>Return to "New Task" and select the relevant Skill</li>
  <li>Perform initialization tasks</li>
</ol>

<h3>Initialization Process</h3>
<ol>
  <li>Complete initialization tasks in WorkBuddy</li>
  <li>Return to Cordys CRM system → "Personal Center" → "Personal Information" → "API Keys"</li>
  <li>Create new API Keys if needed</li>
  <li>Copy the relevant information back to WorkBuddy</li>
  <li>Configure role-based access through API Keys</li>
</ol>

<h2 id="demo">Practical Demonstration</h2>

<h3>Web-Based Operation</h3>
<ol>
  <li>In WorkBuddy's core dialogue area, input commands like:</li>
</ol>
<pre><code class="language-text">Show me my leads and perform relevant desensitization processing</code></pre>
<ol start="2">
  <li>WorkBuddy automatically connects to the Cordys CRM backend</li>
  <li>Pulls business data and quickly returns lead information</li>
  <li>Input second command:</li>
</ol>
<pre><code class="language-text">Pull data, complete relevant summary, and mark customer information for follow-up</code></pre>

<h3>Mobile Operation</h3>
<ol>
  <li>Complete assistant configuration in WorkBuddy</li>
  <li>Demonstrate WeChat assistant integration</li>
  <li>Scan the QR code to connect mobile devices</li>
  <li>Input tasks on the mobile terminal</li>
  <li>The system calls Cordys CRM backend information</li>
  <li>Perfectly adapts to field work requirements</li>
</ol>

<h2 id="conclusion">Conclusion</h2>

<p>This guide uses Cordys CRM as an example to demonstrate how traditional business systems can quickly achieve AI transformation. The key takeaway is not the CRM case itself, but the methodology:</p>

<ul>
  <li>Use WorkBuddy as the unified AI entry point</li>
  <li>Connect enterprise business capabilities through Business Skills</li>
  <li>Enable AI to participate in business processes without rebuilding existing systems</li>
</ul>

<p>This model is not limited to CRM systems. It can be extended to ERP, OA, MES, and other business systems, helping enterprises accelerate AI transformation with lower costs and faster implementation. The core idea is simple: let AI not just chat, but truly participate in business operations.</p>

<h2>常见问题</h2>

<h3>Does this approach work for non-CRM systems like ERP or OA?</h3>
<p>Yes. The three-layer architecture (WorkBuddy + Business Skills + Existing System) is system-agnostic. Cordys CRM is just the example used here. For ERP, you'd create Skills that encapsulate inventory queries, order processing, and financial report generation. For OA, Skills would handle leave approvals, document workflows, and meeting scheduling. The methodology is identical: (1) identify the business capabilities you want AI to access, (2) encapsulate them as Skills with proper role definitions, query rules, and output specifications, (3) connect via WorkBuddy. The Skill file anatomy section (8 components) is a template you can reuse for any business system.</p>

<h3>How much technical knowledge is needed to create a Business Skill?</h3>
<p>Basic Skills (like "query my leads" or "generate a sales report") can be created by business analysts who understand the API endpoints. The Skill file is mostly configuration — defining roles, query rules, and output formats in plain language. Complex Skills (involving multi-step workflows, conditional logic, or custom API integrations) benefit from a developer's input. The good news: once a Skill is created, it's reusable by everyone in the organization. A common pattern is: developers create the initial Skill library, and business users customize them through WorkBuddy's interface without touching code.</p>

<h3>What about data security — can Skills access data they shouldn't?</h3>
<p>The security mechanisms covered in the Skill anatomy section (part 8) are designed specifically for this. Skills enforce: (1) role-based data access via API Keys — a sales rep's Skill can only see their own leads, not the entire CRM; (2) output filtering — sensitive fields like API keys are automatically masked; (3) query rules — Skills can only query predefined fields and time ranges. Additionally, WorkBuddy's local file operation means business data processed through Skills stays on your machine or your company's servers, not on a third-party cloud. For regulated industries, this local-first architecture is often a compliance requirement.</p>

<h3>How long does it take to implement this for a typical business system?</h3>
<p>A basic integration (one Skill for simple queries, like "show my leads") takes 1-2 hours end-to-end, including API key setup and initialization. A production-ready Skill library covering the main business workflows (create/read/update operations, reporting, approvals) typically takes 1-2 weeks for the initial version, with ongoing refinement based on usage. The lightweight approach means you don't need a months-long IT project — you can start with one Skill, prove value, and expand incrementally. Most enterprises begin with a read-only reporting Skill (low risk, high visibility) and expand to write operations once stakeholders are comfortable.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Interested in enterprise AI? Explore more business transformation content:</p>
  <ul>
    <li><a href="/articles/workbuddy-3-layer-memory-system-make-ai-understand-you">WorkBuddy L05: Master the 3-Layer Memory System</a> — understand how WorkBuddy remembers and adapts</li>
    <li><a href="/articles/tencent-workbuddy-ai-office-workbench">Tencent WorkBuddy: The Ultimate AI Office Workbench</a> — the full WorkBuddy feature overview</li>
    <li><a href="/articles/7-mainstream-agent-architectures-beginner-enterprise-guide">7 Mainstream Agent Architectures: From Beginner to Enterprise-Grade</a> — understand the architecture patterns behind this approach</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">💼 AI 应用</span>
  <span class="meta-badge">🕒 阅读约9分钟</span>
  <span class="meta-badge">📅 2026年7月11日</span>
  <span class="meta-badge">🎯 中级</span>
</div>

<h2 id="introduction">引言</h2>

<p>随着大语言模型和AI Agent技术的快速发展，越来越多的企业开始问：AI如何真正融入业务运营，而不只是聊天机器人？本指南以Cordys CRM为例，介绍一套实用的轻量级AI改造方案：<strong>WorkBuddy + 业务技能</strong>。</p>

<p>这个方案让企业无需从零重建现有系统，而是逐步将业务能力封装为Skills，让AI快速高效地参与业务流程。</p>

<h2 id="architecture">三层架构</h2>

<p>方案分为三个核心层：</p>

<ol>
  <li><strong>顶层：WorkBuddy</strong> — 负责理解用户查询，与大语言模型交互，作为整个系统的统一AI入口。</li>
  <li><strong>中间层：业务技能</strong> — 封装企业现有业务能力，让AI理解该调用哪些业务接口，定义执行哪些业务操作。</li>
  <li><strong>底层：现有业务系统</strong> — 例如Cordys CRM系统。保留所有原有业务逻辑和数据。</li>
</ol>

<p>这个架构意味着企业无需重建现有系统，而是逐步将业务能力封装为Skills，让AI快速参与业务。</p>

<h2 id="workbuddy-functions">WorkBuddy核心功能</h2>

<h3>1. 新建任务</h3>
<ul>
  <li>核心对话区，用于发布和处理任务</li>
  <li>支持多任务同时运行</li>
</ul>

<h3>2. 助手功能</h3>
<ul>
  <li>启用远程控制能力</li>
  <li>集成常用聊天软件：微信、QQ、飞书、钉钉</li>
  <li>支持手机远程控制PC端WorkBuddy任务</li>
</ul>

<h3>3. 项目功能</h3>
<ul>
  <li>专注团队协作</li>
  <li>两层架构：项目和任务</li>
  <li>团队可共享素材、标准和专业内容</li>
</ul>

<h3>4. 专家模块</h3>
<ul>
  <li>分为专家中心和我的专家</li>
  <li>专家中心可按行业筛选专家</li>
  <li>我的专家允许用户创建专属专家</li>
</ul>

<h3>5. 技能功能</h3>
<ul>
  <li>本方案中最重要的功能</li>
  <li>Skills持续扩展WorkBuddy的能力边界</li>
  <li>集成了脚本、工作流和第三方API</li>
  <li>不仅回答问题，还能执行实际业务操作</li>
  <li>实现从"会聊天"到"会干活"的升级</li>
</ul>

<h3>6. 自动化功能</h3>
<ul>
  <li>设定规则自动处理重复任务</li>
  <li>示例：每日AI新闻推送、每周工作报告、定期数据整理</li>
  <li>自动将输出文件保存到指定文件夹</li>
</ul>

<h2 id="cordys-crm">Cordys CRM系统概览</h2>

<p>Cordys CRM是面向企业客户管理的客户关系管理系统，覆盖从线索获取、客户管理、商机跟踪到合同订单的完整销售流程，帮助企业实现销售运营的数字化管理。</p>

<p>除传统CRM功能外，Cordys CRM深度集成AI能力：AI辅助客户创建、商机管理、跟进记录生成、集成BI数据分析、可视化仪表盘和数据驱动的业务决策支持。</p>

<h2 id="skill-anatomy">Skill文件逐项拆解</h2>

<p>很多用户第一眼看到Skill文件觉得复杂，但只需关注几个关键部分：</p>

<h3>1. 基本信息</h3>
<p>定义Skill的名称、功能描述和运行环境。<code>description</code>字段尤其重要，它告诉AI该执行什么任务。</p>

<h3>2. 角色设定</h3>
<p>明确定义AI的角色（如"Cordys CRM业务助手"）。决定AI如何回答问题，确保AI提供分析和建议而非仅返回原始数据。</p>

<h3>3. 执行流程</h3>
<p>用户发送消息时，AI按以下流程：(1) 判断用户意图，(2) 根据业务场景选择合适处理逻辑，(3) 生成最终结果。Skills是完整的业务工作流，而非简单提示词。</p>

<h3>4. 按需加载</h3>
<p>企业级Skill不会一次性加载所有功能。根据当前任务动态加载模块。示例：数据查询加载查询引擎，统计分析加载统计引擎。提高响应速度和资源效率。</p>

<h3>5. 查询规则</h3>
<p>定义AI如何构建CRM查询命令——查询哪些字段、时间范围、基于角色的数据访问权限。是AI与CRM系统之间的通信规则。</p>

<h3>6. 输出规范</h3>
<p>AI不能直接返回原始API数据。必须先总结要点，再展示核心数据。提供异常告警和处理建议。确保专业、符合业务场景的回复。</p>

<h3>7. 执行能力</h3>
<p>Skills可执行实际业务操作：创建客户、更新商机、填写跟进记录、审批工作流。AI不仅是问答工具，更是业务执行助手。</p>

<h3>8. 安全机制</h3>
<p>企业数据保护的严格安全规则。禁止输出API密钥等敏感信息。在错误信息中遮盖敏感内容。</p>

<h2 id="skill-import">Skill导入流程</h2>

<h3>方式一：直接导入</h3>
<ol>
  <li>点击"Skills" → "导入技能"</li>
  <li>上传Skill安装包</li>
  <li>可从GitHub仓库获取源文件</li>
</ol>

<h3>方式二：专家功能导入</h3>
<ol>
  <li>点击"Expert" → "Skills"</li>
  <li>搜索框搜索"Cordys CRM"</li>
  <li>点击"SkillHub" → "添加"</li>
  <li>返回"新建任务"选择相关Skill</li>
  <li>执行初始化任务</li>
</ol>

<h3>初始化流程</h3>
<ol>
  <li>在WorkBuddy中完成初始化任务</li>
  <li>返回Cordys CRM系统 → "个人中心" → "个人信息" → "API Keys"</li>
  <li>如需新建API Keys</li>
  <li>将相关信息复制回WorkBuddy</li>
  <li>通过API Keys配置基于角色的访问权限</li>
</ol>

<h2 id="demo">实操演示</h2>

<h3>网页端操作</h3>
<ol>
  <li>在WorkBuddy核心对话区输入指令：</li>
</ol>
<pre><code class="language-text">展示我的线索，并进行相关脱敏处理</code></pre>
<ol start="2">
  <li>WorkBuddy自动连接Cordys CRM后台</li>
  <li>拉取业务数据，快速返回线索信息</li>
  <li>输入第二条指令：</li>
</ol>
<pre><code class="language-text">拉取数据，完成相关汇总，并标记客户信息进行跟进</code></pre>

<h3>移动端操作</h3>
<ol>
  <li>在WorkBuddy中完成助手配置</li>
  <li>演示微信助手集成</li>
  <li>扫描二维码连接移动设备</li>
  <li>在移动端输入任务</li>
  <li>系统调用Cordys CRM后台信息</li>
  <li>完美适配外勤工作需求</li>
</ol>

<h2 id="conclusion">总结</h2>

<p>本指南以Cordys CRM为例，演示了传统业务系统如何快速实现AI改造。关键的收获不是CRM案例本身，而是方法论：</p>

<ul>
  <li>用WorkBuddy作为统一的AI入口</li>
  <li>通过业务Skills连接企业业务能力</li>
  <li>无需重建现有系统，让AI参与业务流程</li>
</ul>

<p>这个模式不限于CRM系统，可扩展到ERP、OA、MES等业务系统，帮助企业以更低成本、更快速度加速AI转型。核心理念很简单：让AI不只是聊天，而是真正参与业务运营。</p>

<h2>常见问题</h2>

<h3>这个方案适用于ERP或OA等非CRM系统吗？</h3>
<p>适用。三层架构（WorkBuddy + 业务技能 + 现有系统）与具体系统无关。Cordys CRM只是本文使用的示例。对ERP，创建封装库存查询、订单处理和财务报表生成的Skills。对OA，Skills处理请假审批、文档流程和会议安排。方法论完全一致：(1) 确定想让AI访问的业务能力，(2) 封装为Skills，含角色定义、查询规则和输出规范，(3) 通过WorkBuddy连接。Skill文件拆解部分（8个组件）是可复用于任何业务系统的模板。</p>

<h3>创建业务Skill需要多少技术知识？</h3>
<p>基础Skill（如"查询我的线索"或"生成销售报告"）可由了解API端点的业务分析师创建。Skill文件主要是配置——用自然语言定义角色、查询规则和输出格式。复杂Skill（涉及多步工作流、条件逻辑或自定义API集成）需要开发人员参与。好消息：Skill一旦创建，整个组织都可复用。常见模式：开发人员创建初始Skill库，业务用户通过WorkBuddy界面自定义，无需接触代码。</p>

<h3>数据安全方面——Skills会访问不该访问的数据吗？</h3>
<p>Skill拆解部分（第8项）的安全机制正是为此设计。Skills强制实施：(1) 通过API Keys实现基于角色的数据访问——销售代表的Skill只能看到自己的线索，不是整个CRM；(2) 输出过滤——API密钥等敏感字段自动遮盖；(3) 查询规则——Skills只能查询预定义字段和时间范围。此外，WorkBuddy的本地文件操作意味着通过Skills处理的业务数据留在你的电脑或公司服务器上，不在第三方云端。对受监管行业，这种本地优先架构通常是合规要求。</p>

<h3>典型业务系统实施这个方案需要多长时间？</h3>
<p>基础集成（一个查询Skill，如"展示我的线索"）端到端需要1-2小时，包括API密钥设置和初始化。覆盖主要业务工作流（增删改查操作、报表、审批）的生产级Skill库初始版本通常需要1-2周，后续根据使用情况持续优化。轻量级方案意味着不需要数月IT项目——可以从一个Skill开始，证明价值，逐步扩展。大多数企业从只读报表Skill起步（低风险、高可见度），利益相关方认可后再扩展到写操作。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>对企业AI感兴趣？探索更多业务转型内容：</p>
  <ul>
    <li><a href="/articles/workbuddy-3-layer-memory-system-make-ai-understand-you">WorkBuddy L05：掌握三层记忆系统，让AI越来越懂你</a> — 了解WorkBuddy如何记忆和适应</li>
    <li><a href="/articles/tencent-workbuddy-ai-office-workbench">腾讯WorkBuddy：日常办公的终极AI工作台</a> — 完整WorkBuddy功能概览</li>
    <li><a href="/articles/7-mainstream-agent-architectures-beginner-enterprise-guide">7大主流Agent架构：从入门到企业级完整指南</a> — 理解本方案背后的架构模式</li>
  </ul>
</div>`,
  },

'''

last_brace = content_src.rfind('};')
content_new = content_src[:last_brace] + new_contents + '};'

with open('src/lib/article-content.ts', 'w', encoding='utf-8') as f:
    f.write(content_new)

print('Part 2: 2 article contents added to article-content.ts')

print('\n=== All done! Run build to verify ===')