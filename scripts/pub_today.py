"""
Publish July 19, 2026 — 1 article, no new tools (Coze/kouzi already exists).
"""
import os

BASE = r"C:\Users\jun\aistudyonline-next"
os.chdir(BASE)

# ===== Part 1: Add 1 article metadata to articles.ts =====
with open('src/lib/articles.ts', 'r', encoding='utf-8') as f:
    articles_src = f.read()

new_articles = r"""  {
    slug: "build-ai-team-coze-3-one-person-company",
    title: "8-Minute Guide: Build an AI Team with Coze 3.0 – Complete a Project from Idea to Launch as a One-Person Company",
    titleZh: "8分钟学会用Coze 3.0搭建AI团队：一人公司从创意到上线全流程",
    description: "A step-by-step tutorial on building a multi-agent AI team in Coze 3.0 — Product Manager, Designer, Development Planner (Claude Code), Development Executor (Codex CLI), and Video Producer (Seedance) — to build an anti-procrastination app from scratch, including PRD, UI design, coding, and promotional video generation.",
    descriptionZh: "在Coze 3.0中搭建多Agent AI团队的完整教程——产品经理、设计师、开发规划（Claude Code）、开发执行（Codex CLI）和视频制作（Seedance）——从零构建反拖延App，含PRD、UI设计、编码和宣传视频全流程。",
    category: "AI Tutorials",
    tags: ["Coze", "AI Agent", "Multi-Agent", "No-Code", "Productivity", "Tutorial", "One-Person Company"],
    difficulty: "beginner",
    toolsMentioned: ["Coze", "Claude Code", "Codex Agent"],
    date: "2026-07-19",
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
  "build-ai-team-coze-3-one-person-company": {
    content: `<div class="meta-banner">
  <span class="meta-badge">📚 AI Tutorials</span>
  <span class="meta-badge">🕒 8 min read</span>
  <span class="meta-badge">📅 Jul 19, 2026</span>
  <span class="meta-badge">🎯 Beginner</span>
</div>

<h2 id="introduction">Introduction</h2>

<p>This tutorial shows you how to build a fully functional AI agent team to complete an entire project from idea to launch using Coze 3.0. The example project is an anti-procrastination app called <em>Time Blocks</em>, designed to break large tasks into small, actionable 10–30 minute chunks.</p>

<h2 id="what-you-learn">What You'll Learn</h2>

<ul>
  <li>How to build an AI agent team in Coze 3.0</li>
  <li>How to assign roles like product manager, designer, developer, and video producer to different AI agents</li>
  <li>How to use skill packs to give agents professional capabilities</li>
  <li>How to run a full project workflow: requirement definition → design → development → video production</li>
  <li>How to manage and iterate on your project using AI collaboration</li>
</ul>

<h2 id="prerequisites">Prerequisites</h2>

<ul>
  <li>A Coze 3.0 account</li>
  <li>Basic understanding of AI agents and workflow automation</li>
  <li>No coding experience required (though familiarity with tools like Claude Code or Codex CLI is helpful)</li>
</ul>

<h2 id="step-1">Step 1: Create a New Project in Coze</h2>

<ol>
  <li>Open Coze 3.0 and click the <strong>+</strong> button in the top-left corner</li>
  <li>Select <strong>New Project</strong></li>
  <li>Enter the project name: <code>Time Blocks</code></li>
  <li>Click <strong>Create Project</strong></li>
</ol>

<h2 id="step-2">Step 2: Build Your AI Agent Team</h2>

<h3>Create a Product Manager Agent</h3>
<ol>
  <li>Click <strong>+</strong> → <strong>New Agent</strong> → <strong>Cloud Agent</strong></li>
  <li>Select <strong>Coze Agent</strong> as the base model</li>
  <li>Name it <code>Product Manager</code> and click <strong>Create and Deploy</strong></li>
  <li>In agent settings, select a model (e.g., GPT-4o, Claude 3)</li>
  <li>Go to the <strong>Skill Store</strong> and add the <strong>Product Operations Skill Pack</strong> — includes product strategy, user research, PRD generation, and user flow design</li>
</ol>

<h3>Create a Designer Agent</h3>
<ol>
  <li>Click <strong>+</strong> → <strong>New Agent</strong> → <strong>Cloud Agent</strong>, name it <code>Designer</code></li>
  <li>Add the <strong>UI/UX Design Skill Pack</strong> — includes wireframing, visual design, design system creation, and handoff documentation</li>
</ol>

<h3>Create Developer Agents</h3>
<p>You'll create two developer agents:</p>
<ul>
  <li><strong>Development Planner</strong>: Uses Claude Code to create a detailed development plan. Create as <strong>Local Agent</strong> with Claude Code.</li>
  <li><strong>Development Executor</strong>: Uses Codex CLI to write the actual code. Create as <strong>Local Agent</strong> with Codex CLI.</li>
</ul>

<h3>Create a Video Producer Agent</h3>
<ol>
  <li>Create as <strong>Cloud Agent</strong>, name it <code>Video Producer</code></li>
  <li>Add the <strong>Video Production Skill Pack</strong> — includes script writing, storyboarding, video generation using Seedance, and editing</li>
</ol>

<h2 id="step-3">Step 3: Add Agents to Your Project</h2>

<ol>
  <li>Go to your <code>Time Blocks</code> project</li>
  <li>Click <strong>Project Settings</strong> → <strong>Agent Management</strong> → <strong>Add</strong></li>
  <li>Select all agents: Product Manager, Designer, Development Planner, Development Executor, Video Producer</li>
  <li>Click <strong>Save</strong></li>
</ol>

<h2 id="step-4">Step 4: Run the Project Workflow</h2>

<h3>4.1 Define Requirements with the Product Manager</h3>

<p>Tag the Product Manager agent and send:</p>

<pre><code class="language-text">@ProductManager
I want to build an anti-procrastination app called "Time Blocks". The app should help users break large, overwhelming tasks into small, 10-30 minute time blocks.

Please:
1. Define the product positioning
2. Identify target users and their pain points
3. Outline core features
4. Create a user flow
5. Write a PRD for the designer and developer agents

Use the Product Operations Skill Pack to help you.</code></pre>

<h3>4.2 Design the UI with the Designer</h3>

<p>Tag the Designer agent and send:</p>

<pre><code class="language-text">@Designer
Based on the PRD from the Product Manager, design the UI for the Time Blocks app.

Requirements:
- Single-page layout
- Visual style: clean, minimal, with a focus on time blocks
- Include a time board where users can drag and drop time blocks
- Provide handoff documentation for the developer agents

Use the UI/UX Design Skill Pack to help you.</code></pre>

<h3>4.3 Create a Development Plan</h3>

<p>Tag the Development Planner agent and send:</p>

<pre><code class="language-text">@DevelopmentPlanner
Based on the PRD and design documents, create a detailed development plan for the Time Blocks app.

Include:
- Technology stack
- File structure
- Development phases
- Implementation details for each feature
- Timeline estimates

Use Claude Code to help you.</code></pre>

<h3>4.4 Write Code with the Development Executor</h3>

<p>Tag the Development Executor agent and send:</p>

<pre><code class="language-text">@DevelopmentExecutor
Based on the development plan, write the code for the Time Blocks app.

Requirements:
- Use HTML, CSS, and JavaScript
- Implement the time block drag-and-drop functionality
- Include a timer for each time block
- Make the app responsive

Use Codex CLI to help you.</code></pre>

<h3>4.5 Generate a Promotional Video</h3>

<p>Tag the Video Producer agent and send:</p>

<pre><code class="language-text">@VideoProducer
Create a 60-second promotional video for the Time Blocks app.

Requirements:
- Script: Explain how the app helps users overcome procrastination
- Visuals: Show the app in action, with time blocks being dragged and dropped
- Music: Upbeat and motivating
- Style: Clean and modern

Use the Video Production Skill Pack and Seedance to generate the video.</code></pre>

<h2 id="step-5">Step 5: Test and Iterate</h2>

<ol>
  <li>Test the app to make sure it works correctly</li>
  <li>If you find issues, tag the relevant agent and ask them to fix it:</li>
</ol>

<pre><code class="language-text">@DevelopmentExecutor
The time block drag-and-drop functionality is not working correctly. Please fix it.</code></pre>

<h2 id="step-6">Step 6: Deploy the App</h2>

<ol>
  <li>Once the app is working correctly, deploy it to a hosting service like Vercel or Netlify</li>
  <li>Share the promotional video on social media to promote the app</li>
</ol>

<h2 id="conclusion">Conclusion</h2>

<p>Congratulations! You've just built a complete AI agent team and used it to create a full project from idea to launch. This workflow can be applied to any type of project, from app development to content creation to marketing. Coze 3.0 makes it easy to build and manage AI agent teams, allowing you to focus on the big picture while the AI agents handle the details.</p>

<p><strong>Note</strong>: Some features mentioned in this tutorial, like multiple local agent access and faster video generation, require the Coze 3.0 Pro plan. The free plan includes basic agent collaboration and standard video generation.</p>

<h2>常见问题</h2>

<h3>What's the difference between Cloud Agents and Local Agents in Coze?</h3>
<p><strong>Cloud Agents</strong> run on Coze's servers — they use Coze-hosted models (GPT-4o, Claude 3, etc.) and the Skill Store. They're ideal for knowledge work: product management, design, content creation. <strong>Local Agents</strong> run on your machine using tools you've installed — Claude Code and Codex CLI in this tutorial. They have direct file system access and can execute code, making them essential for development work. The article uses Cloud Agents for PM, Designer, and Video Producer (knowledge roles), and Local Agents for Development Planner and Executor (execution roles). This hybrid approach gives you the best of both: cloud convenience for thinking tasks, local power for building tasks.</p>

<h3>Can I use this workflow for projects other than app development?</h3>
<p>Yes — the agent team pattern (PM → Designer → Developer → Video Producer) is project-type agnostic. For a <strong>content marketing project</strong>: PM defines the content strategy, Designer creates brand assets, Developer builds landing pages or email templates, Video Producer creates promotional content. For a <strong>product launch</strong>: PM writes the go-to-market plan, Designer creates pitch decks, Developer builds the product page, Video Producer makes a demo video. The key insight: you're not limited to software projects. Any creative or business project that benefits from multiple specialized roles can use this workflow. Just swap the Skill Packs to match your domain.</p>

<h3>How much does Coze 3.0 cost for this workflow?</h3>
<p>The free plan supports basic agent collaboration and standard video generation — enough to complete the tutorial project. The Pro plan (pricing varies by region) unlocks multiple local agent access, faster video generation, priority model access, and advanced Skill Packs. For occasional projects, the free tier is sufficient. If you're running a one-person company with daily agent usage, the Pro plan's faster generation and multi-agent concurrency become worth the cost. The models themselves (GPT-4o, Claude) are billed through your Coze account or API keys — expect $20-50/month in model costs for regular usage in addition to the Coze plan.</p>

<h3>How is Coze 3.0 different from just using Claude Code or Codex for everything?</h3>
<p>Claude Code and Codex are single-agent tools — one AI, one conversation. Coze 3.0 is a <strong>multi-agent orchestration platform</strong>. In Claude Code, you'd ask one assistant to be PM, then designer, then developer — switching roles manually and managing context across conversations. In Coze, you have five persistent agents, each with specialized Skill Packs and separate memory. They work on their parts simultaneously (Designer can work on UI while Developer plans architecture). The project chat keeps everything in one shared context. For small solo projects, a single agent is fine. For multi-role projects where you want parallel work and role specialization, Coze's multi-agent approach is more efficient. Think of it as the difference between hiring one generalist freelancer vs. a small specialized team.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Built your first AI team? Explore more multi-agent and no-code content:</p>
  <ul>
    <li><a href="/articles/7-mainstream-agent-architectures-beginner-enterprise-guide">7 Mainstream Agent Architectures: From Beginner to Enterprise-Grade</a> — understand the architecture behind Coze's multi-agent system</li>
    <li><a href="/articles/complete-guide-codex-zero-to-advanced">Complete Guide to Codex: From Zero to Advanced Development Workflow</a> — master the Development Executor's tool</li>
    <li><a href="/articles/lightweight-ai-transformation-traditional-business-workbuddy-cordys-crm">Lightweight AI Transformation for Traditional Business Systems</a> — apply the agent team pattern to enterprise systems</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">📚 AI 教程</span>
  <span class="meta-badge">🕒 阅读约8分钟</span>
  <span class="meta-badge">📅 2026年7月19日</span>
  <span class="meta-badge">🎯 入门</span>
</div>

<h2 id="introduction">引言</h2>

<p>本教程展示如何用Coze 3.0搭建一支功能完整的AI Agent团队，完成从创意到上线的整个项目。示例项目是一款名为<em>Time Blocks</em>的反拖延App，旨在将大任务拆解为10-30分钟的小型可执行时间块。</p>

<h2 id="what-you-learn">你将学到</h2>

<ul>
  <li>如何在Coze 3.0中搭建AI Agent团队</li>
  <li>如何为不同Agent分配产品经理、设计师、开发者和视频制作人等角色</li>
  <li>如何使用技能包赋予Agent专业能力</li>
  <li>如何运行完整项目工作流：需求定义 → 设计 → 开发 → 视频制作</li>
  <li>如何使用AI协作管理和迭代项目</li>
</ul>

<h2 id="prerequisites">前置条件</h2>

<ul>
  <li>Coze 3.0账号</li>
  <li>对AI Agent和工作流自动化的基本理解</li>
  <li>无需编码经验（熟悉Claude Code或Codex CLI等工具会有帮助）</li>
</ul>

<h2 id="step-1">第一步：在Coze中创建新项目</h2>

<ol>
  <li>打开Coze 3.0，点击左上角<strong>+</strong>按钮</li>
  <li>选择<strong>新建项目</strong></li>
  <li>输入项目名称：<code>Time Blocks</code></li>
  <li>点击<strong>创建项目</strong></li>
</ol>

<h2 id="step-2">第二步：搭建AI Agent团队</h2>

<h3>创建产品经理Agent</h3>
<ol>
  <li>点击<strong>+</strong> → <strong>新建Agent</strong> → <strong>云端Agent</strong></li>
  <li>选择<strong>Coze Agent</strong>作为基础模型</li>
  <li>命名为<code>产品经理</code>，点击<strong>创建并部署</strong></li>
  <li>在Agent设置中选择模型（如GPT-4o、Claude 3）</li>
  <li>前往<strong>技能商店</strong>添加<strong>产品运营技能包</strong>——包含产品策略、用户调研、PRD生成和用户流程设计</li>
</ol>

<h3>创建设计师Agent</h3>
<ol>
  <li>点击<strong>+</strong> → <strong>新建Agent</strong> → <strong>云端Agent</strong>，命名为<code>设计师</code></li>
  <li>添加<strong>UI/UX设计技能包</strong>——包含线框图、视觉设计、设计系统创建和交付文档</li>
</ol>

<h3>创建开发者Agent</h3>
<p>创建两个开发者Agent：</p>
<ul>
  <li><strong>开发规划师</strong>：使用Claude Code创建详细开发计划。以<strong>本地Agent</strong>形式创建，选用Claude Code。</li>
  <li><strong>开发执行者</strong>：使用Codex CLI编写实际代码。以<strong>本地Agent</strong>形式创建，选用Codex CLI。</li>
</ul>

<h3>创建视频制作Agent</h3>
<ol>
  <li>以<strong>云端Agent</strong>创建，命名为<code>视频制作</code></li>
  <li>添加<strong>视频制作技能包</strong>——包含脚本撰写、故事板、使用Seedance生成视频和后期编辑</li>
</ol>

<h2 id="step-3">第三步：将Agent添加到项目</h2>

<ol>
  <li>前往<code>Time Blocks</code>项目</li>
  <li>点击<strong>项目设置</strong> → <strong>Agent管理</strong> → <strong>添加</strong></li>
  <li>选择所有Agent：产品经理、设计师、开发规划师、开发执行者、视频制作</li>
  <li>点击<strong>保存</strong></li>
</ol>

<h2 id="step-4">第四步：运行项目工作流</h2>

<h3>4.1 与产品经理定义需求</h3>

<p>@产品经理Agent并发送：</p>

<pre><code class="language-text">@产品经理
我想构建一款叫"Time Blocks"的反拖延App。这款App应帮助用户将庞大、令人望而生畏的任务拆分为10-30分钟的小型时间块。

请：
1. 定义产品定位
2. 识别目标用户及其痛点
3. 梳理核心功能
4. 创建用户流程
5. 为设计师和开发者Agent撰写PRD

使用产品运营技能包辅助你。</code></pre>

<h3>4.2 与设计师设计UI</h3>

<p>@设计师Agent并发送：</p>

<pre><code class="language-text">@设计师
基于产品经理的PRD，为Time Blocks App设计UI。

要求：
- 单页布局
- 视觉风格：简洁、极简、聚焦时间块
- 包含用户可拖拽时间块的时间面板
- 为开发者Agent提供交付文档

使用UI/UX设计技能包辅助你。</code></pre>

<h3>4.3 创建开发计划</h3>

<p>@开发规划师Agent并发送：</p>

<pre><code class="language-text">@开发规划师
基于PRD和设计文档，为Time Blocks App创建详细开发计划。

包含：
- 技术栈
- 文件结构
- 开发阶段
- 每个功能的实现细节
- 时间估算

使用Claude Code辅助你。</code></pre>

<h3>4.4 与开发执行者编写代码</h3>

<p>@开发执行者Agent并发送：</p>

<pre><code class="language-text">@开发执行者
基于开发计划，为Time Blocks App编写代码。

要求：
- 使用HTML、CSS和JavaScript
- 实现时间块拖拽功能
- 为每个时间块添加计时器
- 使App响应式适配

使用Codex CLI辅助你。</code></pre>

<h3>4.5 生成宣传视频</h3>

<p>@视频制作Agent并发送：</p>

<pre><code class="language-text">@视频制作
为Time Blocks App制作一段60秒的宣传视频。

要求：
- 脚本：解释App如何帮助用户克服拖延
- 画面：展示App实际操作，时间块被拖拽的过程
- 音乐：积极向上、激励人心
- 风格：简洁现代

使用视频制作技能包和Seedance生成视频。</code></pre>

<h2 id="step-5">第五步：测试与迭代</h2>

<ol>
  <li>测试App确保功能正常</li>
  <li>发现问题时，@对应Agent请求修复：</li>
</ol>

<pre><code class="language-text">@开发执行者
时间块拖拽功能不工作，请修复。</code></pre>

<h2 id="step-6">第六步：部署App</h2>

<ol>
  <li>App正常运行后，部署到Vercel或Netlify等托管服务</li>
  <li>在社交媒体分享宣传视频推广App</li>
</ol>

<h2 id="conclusion">总结</h2>

<p>恭喜！你已搭建了一支完整的AI Agent团队，并用它完成了从创意到上线的整个项目。这个工作流可应用于任何类型的项目——从App开发到内容创作再到市场营销。Coze 3.0让搭建和管理AI Agent团队变得简单，让你专注于大局，AI Agent处理细节。</p>

<p><strong>注意</strong>：本教程中提到的部分功能，如多本地Agent访问和更快视频生成，需要Coze 3.0 Pro方案。免费方案包含基础Agent协作和标准视频生成。</p>

<h2>常见问题</h2>

<h3>Coze中云端Agent和本地Agent有什么区别？</h3>
<p><strong>云端Agent</strong>在Coze服务器上运行——使用Coze托管的模型（GPT-4o、Claude 3等）和技能商店。适合知识型工作：产品管理、设计、内容创作。<strong>本地Agent</strong>在你电脑上使用已安装的工具运行——本教程中的Claude Code和Codex CLI。它们有直接的文件系统访问权限并可以执行代码，因此对开发工作至关重要。文章用云端Agent做PM、设计师和视频制作（知识角色），本地Agent做开发规划师和执行者（执行角色）。这种混合方式兼顾两者优势：思考任务用云端便利，构建任务用本地能力。</p>

<h3>这个工作流能用于App开发以外的项目吗？</h3>
<p>可以——Agent团队模式（PM → 设计师 → 开发者 → 视频制作）与项目类型无关。<strong>内容营销项目</strong>：PM定义内容策略，设计师创建品牌素材，开发者搭建落地页或邮件模板，视频制作创作推广内容。<strong>产品发布</strong>：PM撰写上市计划，设计师制作路演PPT，开发者搭建产品页面，视频制作做演示视频。关键洞察：你不限于软件项目。任何受益于多专业角色的创意或商业项目都可以使用这个工作流。只需将技能包替换为匹配你领域的即可。</p>

<h3>这个工作流用Coze 3.0要花多少钱？</h3>
<p>免费方案支持基础Agent协作和标准视频生成——足够完成教程项目。Pro方案（价格因地区而异）解锁多本地Agent访问、更快视频生成、优先模型访问和高级技能包。偶尔做项目，免费层足够。如果你运营一家日常使用Agent的一人公司，Pro方案的更快生成和多Agent并发就值得投入了。模型本身（GPT-4o、Claude）通过你的Coze账户或API密钥计费——常规使用预计$20-50/月的模型费用，此外还有Coze方案费用。</p>

<h3>Coze 3.0和只用Claude Code或Codex有什么区别？</h3>
<p>Claude Code和Codex是单Agent工具——一个AI、一个对话。Coze 3.0是<strong>多Agent编排平台</strong>。在Claude Code中，你会让一个助手先当PM、再当设计师、再当开发者——手动切换角色并在不同对话中管理上下文。在Coze中，你有五个持久Agent，每个有专业技能包和独立记忆。它们同时工作（设计师做UI时开发者规划架构）。项目聊天把所有内容放在共享上下文中。小型单人项目用单Agent就行。需要并行工作和角色专业化的多角色项目，Coze的多Agent方式更高效。这就像雇一个全栈自由职业者 vs. 一支小型专业团队的差别。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>搭建了第一支AI团队？探索更多多Agent和无代码内容：</p>
  <ul>
    <li><a href="/articles/7-mainstream-agent-architectures-beginner-enterprise-guide">7大主流Agent架构：从入门到企业级完整指南</a> — 理解Coze多Agent系统背后的架构</li>
    <li><a href="/articles/complete-guide-codex-zero-to-advanced">Codex完全指南：从零基础到高级开发工作流</a> — 掌握开发执行者使用的工具</li>
    <li><a href="/articles/lightweight-ai-transformation-traditional-business-workbuddy-cordys-crm">传统业务系统轻量级AI改造方案</a> — 将Agent团队模式应用到企业系统</li>
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