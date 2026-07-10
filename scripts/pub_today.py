"""
Publish July 10, 2026 — 2 articles, no new tools.
"""
import os

BASE = r"C:\Users\jun\aistudyonline-next"
os.chdir(BASE)

# ===== Part 1: Add 2 article metadata to articles.ts =====
with open('src/lib/articles.ts', 'r', encoding='utf-8') as f:
    articles_src = f.read()

new_articles = r"""  {
    slug: "workbuddy-3-layer-memory-system-make-ai-understand-you",
    title: "WorkBuddy L05: Master the 3-Layer Memory System – Make AI Understand You Better",
    titleZh: "WorkBuddy L05：掌握三层记忆系统，让AI越来越懂你",
    description: "A deep dive into WorkBuddy's 3-layer memory architecture — Cloud Memory (auto profile + cross-conversation search), User-level Local Memory (MEMORY.md), and Workspace Memory (auto daily logs) — plus how Memory integrates with Skills and Automation to create a self-improving AI assistant.",
    descriptionZh: "深度解析WorkBuddy三层记忆架构——云端记忆（自动画像+跨对话搜索）、用户级本地记忆（MEMORY.md）和工作区记忆（自动日志）——以及记忆如何与技能和自动化系统联动，打造越用越聪明的AI助手。",
    category: "AI Tutorials",
    tags: ["WorkBuddy", "Memory", "Automation", "Skills", "Productivity", "AI Assistant"],
    difficulty: "beginner",
    toolsMentioned: ["Tencent WorkBuddy"],
    date: "2026-07-10",
  },
  {
    slug: "codex-zero-basics-tutorial-part-2-hands-on-guide",
    title: "Codex Zero-Basics Tutorial Part 2: Hands-On Guide to Using Codex for AI Beginners",
    titleZh: "Codex零基础教程（下）：AI新手实操完全指南",
    description: "A beginner-friendly Codex hands-on tutorial covering installation (Windows/Mac), project setup, file organization with real café example, Plan Mode for complex tasks, Pet feature, and dashboard creation — zero technical knowledge required.",
    descriptionZh: "Codex新手实操教程，覆盖安装（Windows/Mac）、项目设置、咖啡馆文件整理实战案例、Plan Mode复杂任务模式、Pet宠物功能和Dashboard创建——完全零技术门槛。",
    category: "AI Tutorials",
    tags: ["Codex", "OpenAI", "Tutorial", "Beginner", "Hands-on", "Plan Mode", "Automation"],
    difficulty: "beginner",
    toolsMentioned: ["Codex Agent"],
    date: "2026-07-10",
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
  "workbuddy-3-layer-memory-system-make-ai-understand-you": {
    content: `<div class="meta-banner">
  <span class="meta-badge">📚 AI Tutorials</span>
  <span class="meta-badge">🕒 8 min read</span>
  <span class="meta-badge">📅 Jul 10, 2026</span>
  <span class="meta-badge">🎯 Beginner</span>
</div>

<h2 id="introduction">Introduction</h2>

<p>If you've ever found yourself reintroducing yourself to an AI assistant every time you start a new conversation, or having to re-explain your preferences when switching projects, this tutorial is for you. WorkBuddy's 3-layer memory system is designed to solve these exact problems, allowing AI to truly "remember" you and adapt to your workflow over time.</p>

<h2 id="what-is">What is the 3-Layer Memory System?</h2>

<p>WorkBuddy's memory system is structured into three layers, each serving a unique purpose and working together to create a seamless, personalized experience:</p>

<ol>
  <li><strong>Layer 1: Cloud Memory</strong>
    <ul>
      <li>Automatically learns your habits and preferences over time</li>
      <li>Generates a personal profile that works across all conversations</li>
      <li>Requires no manual management</li>
    </ul>
  </li>
  <li><strong>Layer 2: User-level Local Memory</strong>
    <ul>
      <li>Stores information you explicitly ask WorkBuddy to remember</li>
      <li>Example: "Use this design style for this series of projects"</li>
      <li>Saved in a local file</li>
    </ul>
  </li>
  <li><strong>Layer 3: Workspace Memory</strong>
    <ul>
      <li>Maintains independent records for each project</li>
      <li>Automatically adds daily logs after completing substantive work</li>
      <li>Requires no manual effort from you</li>
    </ul>
  </li>
</ol>

<p>These three layers work together, moving from broad to specific, from passive to active, to create a comprehensive memory system.</p>

<h2 id="deep-dive">Deep Dive into Each Layer</h2>

<h3>Layer 1: Cloud Memory</h3>

<p>Cloud memory has two core capabilities:</p>

<h4>1. Auto Profile Generation</h4>
<ul>
  <li>Servers analyze your conversations to automatically summarize your code preferences, work habits, and commonly used tools</li>
  <li>This profile is automatically loaded every time you start a new conversation</li>
  <li>WorkBuddy "recognizes" you without you having to reintroduce yourself</li>
</ul>

<h4>2. Cross-Conversation History Search</h4>
<ul>
  <li>When you mention something like "the deployment solution we discussed last week," WorkBuddy uses <code>conversation_search</code> to search through all your historical conversations</li>
  <li>It can find the exact discussion, including tools used, configurations, and ports</li>
  <li>You don't have to re-explain everything — it finds the information itself</li>
</ul>

<h3>Layer 2 & 3: Local Memory</h3>

<h4>Layer 2: User-level Local Memory</h4>
<ul>
  <li>Stored in the <code>MEMORY.md</code> file</li>
  <li>When you explicitly state your requirements, those rules are written to this file</li>
  <li>Applies to all projects and conversations moving forward</li>
</ul>

<h4>Layer 3: Workspace Memory</h4>
<ul>
  <li>Stored in the <code>.workbuddy/memory/</code> directory within your project folder</li>
  <li>After you complete substantive work, WorkBuddy automatically adds a daily log entry</li>
  <li>Logs include what you did, what solutions you used, and what problems you encountered</li>
  <li>Logs older than 30 days are refined into long-term project notes</li>
</ul>

<h2 id="memory-skills-automation">Memory System + Skills + Automation: The Complete Workflow</h2>

<h3>Skills System</h3>
<ul>
  <li>Memory is the "brain" of WorkBuddy, while the skills system is its "hands"</li>
  <li>Skills are divided into three categories: user-level, project-level, and built-in marketplace</li>
  <li>A skill is a reusable workflow</li>
  <li>Example: If you have the <code>poster-design-warm-tech</code> skill installed, simply say "help me create a tech poster" and WorkBuddy automatically loads the skill's context and generates it according to the preset workflow</li>
  <li>After completing a complex workflow, WorkBuddy can automatically accumulate it as a new skill, getting smarter with use</li>
</ul>

<h3>Automation System</h3>
<ul>
  <li>Automation is the most "active" form of the memory system</li>
  <li>Supports both recurring tasks and one-time tasks</li>
  <li>Examples:
    <ul>
      <li>"Generate a market briefing every morning at 9 AM"</li>
      <li>"Write a weekly report automatically every Friday at 5 PM"</li>
    </ul>
  </li>
  <li>Can specify which expert to activate automatically and which third-party service to connect to</li>
</ul>

<p>In simple terms:</p>
<ul>
  <li>Cloud memory is passively learned</li>
  <li>Local memory is static rules</li>
  <li>Workspace memory is post-work records</li>
  <li>Automation is "pre-set future memory" that automatically wakes up and executes at specified times</li>
</ul>

<h2 id="practical-guide">Practical Operation Guide</h2>

<h3>Setting Up Automation Tasks</h3>

<ol>
  <li>Open WorkBuddy</li>
  <li>Click "Automation" → "Add Task"</li>
  <li>Fill in: Name, Workspace, Prompt, Connector, Execution frequency</li>
</ol>

<p>Each configuration item corresponds to a piece of memory: the prompt is the "memory body" of automation, and the expert and connector determine the context scope.</p>

<h3>Key Settings Interfaces</h3>

<h4>1. Memory Settings</h4>
<p>The management center for cloud memory. Here you can toggle automatic profile generation, manage existing memory cards, and import habits from other AI platforms.</p>

<h4>2. Conversation Management</h4>
<p>The cost switch for cloud memory. Automatically disconnects context after long periods of inactivity to save tokens. With <code>conversation_search</code>, disconnecting doesn't mean forgetting.</p>

<h4>3. Personalization</h4>
<p>The rule engine for local memory. Custom instructions written here are saved to the <code>MEMORY.md</code> file. Applies to all projects with the highest priority.</p>

<h4>4. Data Management</h4>
<p>The archive for workspace memory. Centralized display of shared files, archived tasks, and installed applications for all projects.</p>

<h4>5. Workspace</h4>
<p>The write trigger for workspace memory. Manually save content to <code>.workbuddy/</code>. Works with automatic log addition to form a complete memory loop.</p>

<h2 id="summary">Summary</h2>

<p>Good AI assistants aren't one-time tools — they remember your every decision and help you accumulate every experience.</p>

<ol>
  <li><strong>Use Memory Wisely</strong>: Say "remember this" to save rules locally. Say "the solution we discussed last time" to use cloud memory. Let it automatically write logs after completing important work.</li>
  <li><strong>Accumulate Skills</strong>: Complex workflows are automatically accumulated. Bug fixes are automatically learned. Reusable workflows mean you don't have to start from scratch every time.</li>
  <li><strong>Free Your Hands</strong>: Set up automation to handle recurring tasks. Let WorkBuddy work for you even when you're not around.</li>
</ol>

<p>This is the WorkBuddy memory system — making AI understand you better, work more efficiently, and become a true partner in your workflow.</p>

<h2>常见问题</h2>

<h3>How is WorkBuddy's memory different from ChatGPT's memory?</h3>
<p>ChatGPT's memory is a single flat layer — it remembers facts you tell it, but doesn't distinguish between personal preferences, project-specific context, and daily work logs. WorkBuddy's 3-layer system separates these concerns: Cloud Memory handles cross-conversation personalization (like "I prefer blue themes"), Local Memory stores explicit rules (like "always use this brand voice"), and Workspace Memory auto-logs what you actually did each day. The key difference: WorkBuddy doesn't just remember facts — it remembers <strong>workflows</strong>. After you complete a complex task, it can automatically save the sequence as a reusable Skill, so next time you just say "do the weekly report" instead of re-explaining the entire process.</p>

<h3>Is my cloud memory data private?</h3>
<p>Cloud memory is processed on Tencent's servers, so it's subject to Tencent's privacy policy. The auto-profile generation and cross-conversation search require server-side processing. If you're concerned about sensitive data, use Local Memory (MEMORY.md) and Workspace Memory (.workbuddy/memory/) — both are stored entirely on your machine and never leave it. You can also toggle off automatic profile generation in Memory Settings while keeping manual cloud memory features. For maximum privacy, use WorkBuddy in local-only mode with cloud features disabled.</p>

<h3>How long does it take for Cloud Memory to build a useful profile?</h3>
<p>About 1-2 weeks of regular use (10-20 conversations). The profile starts with surface-level preferences (preferred tools, common tasks) and deepens over time. After a month, it should reliably know your coding style, design preferences, commonly used project structures, and even your communication tone. The key is consistency — using WorkBuddy as your primary AI assistant accelerates profile building. You can also import habits from other AI platforms in Memory Settings to jumpstart the process.</p>

<h3>Can I use Automation without setting up Memory first?</h3>
<p>Yes, but you'll get less value. Automation without memory is just a scheduler — it runs the same prompt at the same time every day. With memory, Automation becomes contextual: the weekly report knows what you worked on this week (from Workspace Memory), uses your preferred format (from Local Memory), and adapts to your communication style (from Cloud Memory). Start with simple time-based automations, and as your memory layers fill in, the same automations become progressively smarter without any additional configuration.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Mastered WorkBuddy's memory system? Explore the full WorkBuddy ecosystem:</p>
  <ul>
    <li><a href="/articles/tencent-workbuddy-ai-office-workbench">Tencent WorkBuddy: The Ultimate AI Office Workbench</a> — the feature overview</li>
    <li><a href="/articles/practical-guide-tencent-workbuddy-ai-office-assistant">A Practical Guide to Tencent WorkBuddy: Your All-in-One AI Office Assistant</a> — hands-on use cases with prompt examples</li>
    <li><a href="/articles/mastering-ai-workflow-beginner-custom-workbench">Mastering AI Workflow: Build Your Custom AI Workbench</a> — build your own AI productivity system</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">📚 AI 教程</span>
  <span class="meta-badge">🕒 阅读约8分钟</span>
  <span class="meta-badge">📅 2026年7月10日</span>
  <span class="meta-badge">🎯 入门</span>
</div>

<h2 id="introduction">引言</h2>

<p>如果你每次开启新对话都要重新介绍自己，或者切换项目时总要重新解释偏好，这篇教程就是为你写的。WorkBuddy的三层记忆系统正是为了解决这些问题，让AI真正"记住"你，并随着时间推移适应你的工作流。</p>

<h2 id="what-is">什么是三层记忆系统？</h2>

<p>WorkBuddy的记忆系统分为三层，每层有独特功能，协同工作创造无缝的个性化体验：</p>

<ol>
  <li><strong>第一层：云端记忆</strong>
    <ul>
      <li>自动学习你的习惯和偏好</li>
      <li>生成跨对话生效的个人画像</li>
      <li>无需手动管理</li>
    </ul>
  </li>
  <li><strong>第二层：用户级本地记忆</strong>
    <ul>
      <li>存储你明确要求WorkBuddy记住的信息</li>
      <li>示例："这个系列项目用这个设计风格"</li>
      <li>保存在本地文件中</li>
    </ul>
  </li>
  <li><strong>第三层：工作区记忆</strong>
    <ul>
      <li>为每个项目维护独立记录</li>
      <li>完成实质性工作后自动添加每日日志</li>
      <li>无需你手动操作</li>
    </ul>
  </li>
</ol>

<p>三层从宽泛到具体、从被动到主动，协同构建完整的记忆体系。</p>

<h2 id="deep-dive">逐层深度解析</h2>

<h3>第一层：云端记忆</h3>

<p>云端记忆有两大核心能力：</p>

<h4>1. 自动画像生成</h4>
<ul>
  <li>服务器分析你的对话，自动总结代码偏好、工作习惯和常用工具</li>
  <li>每次开启新对话时自动加载此画像</li>
  <li>WorkBuddy"认出"你，无需重新自我介绍</li>
</ul>

<h4>2. 跨对话历史搜索</h4>
<ul>
  <li>当你提到"上周讨论的部署方案"，WorkBuddy使用<code>conversation_search</code>搜索所有历史对话</li>
  <li>能找到具体讨论内容，包括使用的工具、配置和端口</li>
  <li>无需重新解释——它自己找到信息</li>
</ul>

<h3>第二层和第三层：本地记忆</h3>

<h4>第二层：用户级本地记忆</h4>
<ul>
  <li>存储在<code>MEMORY.md</code>文件中</li>
  <li>当你明确陈述需求时，规则写入此文件</li>
  <li>适用于之后所有项目和对话</li>
</ul>

<h4>第三层：工作区记忆</h4>
<ul>
  <li>存储在项目文件夹的<code>.workbuddy/memory/</code>目录中</li>
  <li>完成实质性工作后，WorkBuddy自动添加每日日志条目</li>
  <li>日志包含做了什么、用了什么方案、遇到什么问题</li>
  <li>30天以上的日志被提炼为长期项目笔记</li>
</ul>

<h2 id="memory-skills-automation">记忆系统 + 技能 + 自动化：完整工作流</h2>

<h3>技能系统</h3>
<ul>
  <li>记忆是WorkBuddy的"大脑"，技能系统是它的"双手"</li>
  <li>技能分三类：用户级、项目级和内置市场</li>
  <li>技能是可复用的工作流</li>
  <li>示例：安装了<code>poster-design-warm-tech</code>技能，说"帮我做一张科技海报"，WorkBuddy自动加载技能上下文并按预设流程生成</li>
  <li>完成复杂工作流后，WorkBuddy可自动将其积累为新技能，越用越聪明</li>
</ul>

<h3>自动化系统</h3>
<ul>
  <li>自动化是记忆系统最"主动"的形式</li>
  <li>支持周期性任务和一次性任务</li>
  <li>示例：
    <ul>
      <li>"每天早上9点生成市场简报"</li>
      <li>"每周五下午5点自动写周报"</li>
    </ul>
  </li>
  <li>可指定自动激活哪个专家、连接哪个第三方服务</li>
</ul>

<p>简单来说：</p>
<ul>
  <li>云端记忆是被动学习</li>
  <li>本地记忆是静态规则</li>
  <li>工作区记忆是事后记录</li>
  <li>自动化是"预设的未来记忆"，在指定时间自动唤醒并执行</li>
</ul>

<h2 id="practical-guide">实操指南</h2>

<h3>设置自动化任务</h3>

<ol>
  <li>打开WorkBuddy</li>
  <li>点击"Automation" → "Add Task"</li>
  <li>填写：名称、工作区、提示词、连接器、执行频率</li>
</ol>

<p>每个配置项对应一段记忆：提示词是自动化的"记忆体"，专家和连接器决定上下文范围。</p>

<h3>关键设置界面</h3>

<h4>1. 记忆设置</h4>
<p>云端记忆的管理中心。可开关自动画像生成、管理已有记忆卡片、从其他AI平台导入习惯。</p>

<h4>2. 对话管理</h4>
<p>云端记忆的成本开关。长时间不活跃后自动断开上下文以节省token。有了<code>conversation_search</code>，断开不等于遗忘。</p>

<h4>3. 个性化</h4>
<p>本地记忆的规则引擎。此处编写的自定义指令保存到<code>MEMORY.md</code>文件。适用于所有项目，优先级最高。</p>

<h4>4. 数据管理</h4>
<p>工作区记忆的档案馆。集中展示所有项目的共享文件、归档任务和已安装应用。</p>

<h4>5. 工作区</h4>
<p>工作区记忆的写入触发器。手动保存内容到<code>.workbuddy/</code>。与自动日志添加配合，形成完整的记忆闭环。</p>

<h2 id="summary">总结</h2>

<p>好的AI助手不是一次性工具——它记住你的每个决策，帮你积累每段经验。</p>

<ol>
  <li><strong>善用记忆</strong>：说"记住这个"保存规则到本地。说"上次讨论的方案"使用云端记忆。完成重要工作后让它自动写日志。</li>
  <li><strong>积累技能</strong>：复杂工作流自动积累。Bug修复自动学习。可复用工作流让你不用每次都从零开始。</li>
  <li><strong>解放双手</strong>：设置自动化处理重复任务。让WorkBuddy在你不在时也为你工作。</li>
</ol>

<p>这就是WorkBuddy记忆系统——让AI更懂你、工作更高效、成为你工作流中真正的伙伴。</p>

<h2>常见问题</h2>

<h3>WorkBuddy的记忆和ChatGPT的记忆有什么不同？</h3>
<p>ChatGPT的记忆是单层扁平结构——它记住你告诉它的事实，但不区分个人偏好、项目上下文和日常工作日志。WorkBuddy的三层系统分离了这些关注点：云端记忆处理跨对话个性化（如"我偏好蓝色主题"），本地记忆存储显式规则（如"始终使用这个品牌语调"），工作区记忆自动记录你每天实际做了什么。关键区别：WorkBuddy不只是记住事实——它记住<strong>工作流</strong>。完成复杂任务后，它可以自动将操作序列保存为可复用技能，下次你只需说"做周报"而不用重新解释整个流程。</p>

<h3>我的云端记忆数据安全吗？</h3>
<p>云端记忆在腾讯服务器上处理，受腾讯隐私政策约束。自动画像生成和跨对话搜索需要服务端处理。如果担心敏感数据，使用本地记忆（MEMORY.md）和工作区记忆（.workbuddy/memory/）——两者完全存储在本地，不离开你的电脑。你也可以在记忆设置中关闭自动画像生成，同时保留手动云端记忆功能。最大化隐私保护，使用WorkBuddy的纯本地模式并禁用云端功能。</p>

<h3>云端记忆建立有用的画像需要多久？</h3>
<p>大约1-2周规律使用（10-20次对话）。画像从表层偏好开始（偏好工具、常见任务），随时间加深。一个月后，它应该能可靠地了解你的编码风格、设计偏好、常用项目结构甚至沟通语气。关键是持续性——将WorkBuddy作为主要AI助手能加速画像建立。也可以在记忆设置中从其他AI平台导入习惯来快速起步。</p>

<h3>不先设置记忆就能用自动化吗？</h3>
<p>可以，但价值会打折扣。没有记忆的自动化只是定时器——每天同一时间运行同一提示词。有了记忆，自动化变得有上下文：周报知道你这周做了什么（来自工作区记忆），使用你偏好的格式（来自本地记忆），适配你的沟通风格（来自云端记忆）。从简单的定时自动化开始，随着记忆层逐渐填满，同样的自动化会变得越来越聪明，无需任何额外配置。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>掌握了WorkBuddy的记忆系统？探索完整的WorkBuddy生态：</p>
  <ul>
    <li><a href="/articles/tencent-workbuddy-ai-office-workbench">腾讯WorkBuddy：日常办公的终极AI工作台</a> — 功能概览</li>
    <li><a href="/articles/practical-guide-tencent-workbuddy-ai-office-assistant">腾讯WorkBuddy实操指南：一站式AI办公助手完全上手</a> — 含提示词示例的实战场景</li>
    <li><a href="/articles/mastering-ai-workflow-beginner-custom-workbench">掌握AI工作流：打造你的专属AI工作台</a> — 构建自己的AI生产力系统</li>
  </ul>
</div>`,
  },

  "codex-zero-basics-tutorial-part-2-hands-on-guide": {
    content: `<div class="meta-banner">
  <span class="meta-badge">📚 AI Tutorials</span>
  <span class="meta-badge">🕒 7 min read</span>
  <span class="meta-badge">📅 Jul 10, 2026</span>
  <span class="meta-badge">🎯 Beginner</span>
</div>

<h2 id="introduction">Introduction</h2>

<p>Codex has surpassed Claude Code to become the world's most popular AI Agent tool. If you haven't started using Codex yet, don't hesitate. This tutorial will guide you from scratch, using practical projects as demonstrations, to teach you how to use Codex to assist with your work and learning.</p>

<h2 id="what-is-codex">What is Codex?</h2>

<p>Codex is an AI Agent tool that provides an interface for you to communicate with it through typing, similar to familiar tools like Doubao or DeepSeek. However, the key difference is that while Doubao can only chat with you, Codex can directly operate your computer and help you complete tasks on it.</p>

<h3>What Can Codex Do?</h3>

<ul>
  <li><strong>File Management</strong>: Organize files, read work content, and edit reports</li>
  <li><strong>Document Creation</strong>: Generate PPTs, create spreadsheets, and write weekly reports</li>
  <li><strong>Browser Operations</strong>: Directly control your browser</li>
  <li><strong>Software Development</strong>: Build complex software</li>
  <li><strong>Automation</strong>: Set up tasks to run automatically while you sleep</li>
</ul>

<p>Codex can handle almost any task you can imagine, and you don't need any technical knowledge to use it.</p>

<h2 id="installation">Installation Guide</h2>

<p>Codex is available in the Microsoft Store and Apple App Store, making installation straightforward:</p>

<h3>For Windows Users</h3>
<ol>
  <li>Open the Microsoft Store</li>
  <li>Search for "Codex"</li>
  <li>Click "Install"</li>
</ol>

<h3>For Mac Users</h3>
<ol>
  <li>Open the App Store</li>
  <li>Search for "Codex"</li>
  <li>Click "Get"</li>
</ol>

<h2 id="getting-started">Getting Started with Codex</h2>

<p>After opening Codex, you'll notice it looks similar to the web version of Doubao, with a central input box and a sidebar on the left. The sidebar contains features not found in Doubao, such as plugins and automation workflows, which we'll explore in detail later.</p>

<h3>Initial Configuration</h3>

<p>When you first open Codex, I recommend modifying a simple configuration:</p>
<ol>
  <li>Go to settings</li>
  <li>Find the "Work Mode" option</li>
  <li>Switch it to "Daily Work"</li>
</ol>

<p>This setting allows Codex to remain powerful while avoiding displaying a lot of technical details that might be difficult to understand, making your experience much smoother.</p>

<h2 id="core-concepts">Core Concepts</h2>

<p>Before diving into more advanced usage, let's understand some key concepts that will make using Codex easier and more powerful.</p>

<h3>Projects</h3>

<p>Since Codex works directly on your computer, it needs a working folder. These folders are called "projects" in Codex and are displayed in the sidebar. You can categorize different tasks into different folders (projects), making it easy to find the content you need.</p>

<p>To select a project for your current conversation:</p>
<ol>
  <li>Click on the project selection option below the input box</li>
  <li>Choose the folder you want Codex to work with</li>
</ol>

<p>Codex will then have direct access to all files in that folder to help you complete your tasks.</p>

<h3>Practical Example: Organizing Files</h3>

<p>Let's say you have a folder called "Computer Language Café" on your computer, filled with various files like sales records, invoices, and inventory lists in different formats (Excel, PDF, etc.). You can ask Codex to organize these files and extract the data into an Excel spreadsheet for easy access.</p>

<p><strong>Task Description</strong>:</p>

<pre><code class="language-text">This is a folder related to a café called "Computer Language Café". It looks messy right now. Please organize these files and extract the information and data into an Excel spreadsheet so I can easily access the detailed data of this store.</code></pre>

<p>After sending this task, Codex will analyze the files, move them around, modify their content, and create new files. It will organize the files by their purpose, generate a detailed data table with all the sales data and product rankings, and even extract information from PDF invoices. It will also identify any issues in the files, such as missing transaction records or abnormal invoices.</p>

<h2 id="advanced-usage">Advanced Usage</h2>

<p>Now that we've covered the basics, let's explore some more advanced features of Codex.</p>

<h3>Plan Mode</h3>

<p>For complex tasks, Codex doesn't execute them directly. Instead, it first creates a detailed execution plan, confirms the details with you, and then proceeds. This is called "Plan Mode."</p>

<p>To enable Plan Mode:</p>
<ol>
  <li>When sending a complex task, select "Plan Mode"</li>
  <li>Codex will analyze the task in detail</li>
  <li>If there are any uncertainties, it will ask you questions</li>
  <li>It will then provide a detailed plan for you to review</li>
  <li>You can adjust the plan or submit it for execution</li>
</ol>

<h3>Pet Feature</h3>

<p>Codex has a fun feature called "Pet." To access it:</p>
<ol>
  <li>Type "/" in the input box</li>
  <li>Select "Pet" from the options</li>
</ol>

<p>A small pet will appear on your desktop. You can place it anywhere on your screen, and it will not only be cute but also display all currently running tasks. You can even customize the pet's appearance in the settings.</p>

<h3>Creating a Dashboard</h3>

<p>Let's say you want to create a visual dashboard for the café using the data from the Excel spreadsheet Codex generated earlier. You can:</p>
<ol>
  <li>Attach the Excel file to your message</li>
  <li>Send the following task:</li>
</ol>

<pre><code class="language-text">Please use the data in this spreadsheet to create a visual dashboard for the Computer Language Café, so I can easily view the store's business situation, such as sales, expenses, costs, inventory, etc. Also, please analyze what I need to pay attention to.</code></pre>

<p>Since this is a complex task, enable Plan Mode. Codex will create a detailed plan, ask for any necessary clarifications, and then generate a professional-looking dashboard with all the requested information, along with suggestions and key points to focus on.</p>

<p>You can even ask Codex to modify the dashboard's theme to be more modern and intuitive, like Apple's design style.</p>

<h2 id="conclusion">Conclusion</h2>

<p>This tutorial has covered the basics of using Codex, from installation to advanced features. Codex is a powerful tool that can help you with a wide range of tasks, from file organization to complex data analysis and software development.</p>

<p>Remember, you don't need any technical knowledge to use Codex. With just a few simple commands, you can make Codex do amazing things. So don't be afraid to experiment and explore what Codex can do for you.</p>

<h2>常见问题</h2>

<h3>How is this tutorial different from Part 1?</h3>
<p>Part 1 covered the Codex workflow from a developer's perspective — installation, project setup, Git, refactoring, and plugins. This Part 2 is designed for <strong>absolute beginners with zero technical background</strong>. It uses a real-world café example (organizing messy business files, creating dashboards) instead of code examples. It also covers features Part 1 didn't: the "Daily Work" mode (which hides technical details), the Pet feature, and the Plan Mode workflow from a non-developer's perspective. If you're a developer, read Part 1. If you're new to AI tools entirely, start here.</p>

<h3>Do I really need zero coding knowledge to use Codex?</h3>
<p>Yes. The café example in this tutorial is a real task — organizing invoices, sales records, and inventory lists — that requires no coding. Codex handles the technical complexity internally. You describe what you want in plain language, and it figures out how to do it. The "Daily Work" mode (recommended in the setup section) further simplifies the experience by hiding terminal output, file paths, and technical jargon. That said, Codex becomes even more powerful if you do know some coding — but it's not required to get started and be productive.</p>

<h3>What's the difference between Codex and tools like Doubao/DeepSeek?</h3>
<p>Doubao and DeepSeek are <strong>chat tools</strong> — they answer questions and generate text. Codex is an <strong>Agent</strong> — it can actually operate your computer: open files, edit spreadsheets, organize folders, control your browser, and run software. Think of Doubao as a knowledgeable friend you can ask questions. Think of Codex as a capable assistant who can do the work for you. The chat interface looks similar, but the capabilities are fundamentally different. Codex is closer to having an intern who can use your computer than a chatbot that can answer questions.</p>

<h3>Can I use Codex on my phone?</h3>
<p>Codex has a mobile app (Codex Mobile) that connects to your desktop Codex installation. You can send tasks from your phone, and Codex executes them on your computer. This is covered in detail in the full Codex guide. For the tasks in this tutorial (file organization, dashboard creation), you'll want to be at your computer. Mobile is best for quick tasks like "check my unread messages and summarize them" or "add this event to my calendar."</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Ready to go deeper with Codex? Continue your learning journey:</p>
  <ul>
    <li><a href="/articles/complete-guide-codex-zero-to-advanced">Complete Guide to Codex: From Zero to Advanced Development Workflow</a> — the full developer-oriented guide (Part 1)</li>
    <li><a href="/articles/official-tutorial-three-ways-codex-control-computer">Official Tutorial: Three Ways Codex Can Control Your Computer for You</a> — master Computer Use, Chrome Extension, and In-App Browser</li>
    <li><a href="/articles/2026-ai-agent-guide-choose-right-tool-beginners">2026 AI Agent Guide: How to Choose the Right Tool for Beginners</a> — see why Codex ranks #1</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">📚 AI 教程</span>
  <span class="meta-badge">🕒 阅读约7分钟</span>
  <span class="meta-badge">📅 2026年7月10日</span>
  <span class="meta-badge">🎯 入门</span>
</div>

<h2 id="introduction">引言</h2>

<p>Codex已超越Claude Code成为全球最受欢迎的AI Agent工具。如果你还没开始使用Codex，别再犹豫。本教程将从零开始，以实战项目为演示，教你如何用Codex辅助工作和学习。</p>

<h2 id="what-is-codex">什么是Codex？</h2>

<p>Codex是一个AI Agent工具，通过打字交流的界面与你沟通，类似熟悉的豆包或DeepSeek。但关键区别在于：豆包只能和你聊天，而Codex能直接操作你的电脑，帮你完成电脑上的任务。</p>

<h3>Codex能做什么？</h3>

<ul>
  <li><strong>文件管理</strong>：整理文件、读取工作内容、编辑报告</li>
  <li><strong>文档创建</strong>：生成PPT、创建电子表格、写周报</li>
  <li><strong>浏览器操作</strong>：直接控制你的浏览器</li>
  <li><strong>软件开发</strong>：构建复杂软件</li>
  <li><strong>自动化</strong>：设置任务在你睡觉时自动运行</li>
</ul>

<p>Codex几乎能处理你能想到的任何任务，且完全不需要技术知识。</p>

<h2 id="installation">安装指南</h2>

<p>Codex在Microsoft Store和Apple App Store上架，安装非常简单：</p>

<h3>Windows用户</h3>
<ol>
  <li>打开Microsoft Store</li>
  <li>搜索"Codex"</li>
  <li>点击"安装"</li>
</ol>

<h3>Mac用户</h3>
<ol>
  <li>打开App Store</li>
  <li>搜索"Codex"</li>
  <li>点击"获取"</li>
</ol>

<h2 id="getting-started">Codex入门</h2>

<p>打开Codex后，你会发现界面和豆包网页版很像，中间是输入框，左侧是侧边栏。侧边栏里有豆包没有的功能，比如插件和自动化工作流，我们稍后详细探索。</p>

<h3>初始配置</h3>

<p>首次打开Codex，建议修改一个简单配置：</p>
<ol>
  <li>进入设置</li>
  <li>找到"工作模式"选项</li>
  <li>切换为"日常办公"</li>
</ol>

<p>这个设置让Codex保持强大的同时，避免显示大量难以理解的技术细节，体验会顺畅很多。</p>

<h2 id="core-concepts">核心概念</h2>

<p>在深入更高级用法之前，先了解一些让Codex更易用、更强大的关键概念。</p>

<h3>项目</h3>

<p>因为Codex直接在你的电脑上工作，它需要一个工作文件夹。这些文件夹在Codex中叫"项目"，显示在侧边栏。你可以把不同任务分类到不同文件夹（项目）中，方便找到需要的内容。</p>

<p>为当前对话选择项目：</p>
<ol>
  <li>点击输入框下方的项目选择选项</li>
  <li>选择你想让Codex操作的文件夹</li>
</ol>

<p>Codex就能直接访问该文件夹中的所有文件来帮你完成任务。</p>

<h3>实战案例：整理文件</h3>

<p>假设你电脑上有一个叫"计算机语言咖啡馆"的文件夹，里面塞满了各种文件——销售记录、发票、库存清单，格式各异（Excel、PDF等）。你可以让Codex整理这些文件并把数据提取到Excel表格中方便查看。</p>

<p><strong>任务描述</strong>：</p>

<pre><code class="language-text">这是一个叫"计算机语言咖啡馆"的文件夹，现在看起来比较乱。请帮我整理这些文件，把信息和数据提取到一个Excel表格中，方便我查看这家店的详细数据。</code></pre>

<p>发送这个任务后，Codex会分析文件、移动它们、修改内容、创建新文件。它会按用途整理文件，生成包含所有销售数据和产品排名的详细数据表，甚至从PDF发票中提取信息。它还会识别文件中的问题，如缺失交易记录或异常发票。</p>

<h2 id="advanced-usage">高级用法</h2>

<p>掌握了基础，来探索一些更高级的Codex功能。</p>

<h3>Plan Mode（计划模式）</h3>

<p>对于复杂任务，Codex不会直接执行。它首先创建详细的执行计划，和你确认细节后再继续。这叫"Plan Mode"。</p>

<p>启用Plan Mode：</p>
<ol>
  <li>发送复杂任务时，选择"Plan Mode"</li>
  <li>Codex会详细分析任务</li>
  <li>如有不确定的地方，它会问你问题</li>
  <li>然后提供详细计划供你审阅</li>
  <li>你可以调整计划或提交执行</li>
</ol>

<h3>宠物功能</h3>

<p>Codex有一个有趣的功能叫"宠物"。访问方式：</p>
<ol>
  <li>在输入框中输入"/"</li>
  <li>从选项中选择"Pet"</li>
</ol>

<p>桌面上会出现一只小宠物。你可以把它放在屏幕任意位置，它不仅可爱，还会显示所有正在运行的任务。甚至可以在设置中自定义宠物的外观。</p>

<h3>创建Dashboard</h3>

<p>假设你想用Codex之前生成的Excel表格数据为咖啡馆创建一个可视化仪表盘。你可以：</p>
<ol>
  <li>将Excel文件附加到消息中</li>
  <li>发送以下任务：</li>
</ol>

<pre><code class="language-text">请用这个表格中的数据为计算机语言咖啡馆创建一个可视化仪表盘，让我能直观看到店铺的经营状况，如销售额、支出、成本、库存等。同时帮我分析需要关注的重点。</code></pre>

<p>因为这是复杂任务，启用Plan Mode。Codex会创建详细计划，询问必要的澄清问题，然后生成包含所有请求信息的专业仪表盘，以及建议和需要关注的重点。</p>

<p>你还可以让Codex把仪表盘主题改得更现代直观，比如Apple的设计风格。</p>

<h2 id="conclusion">总结</h2>

<p>本教程覆盖了Codex的基础使用，从安装到高级功能。Codex是一个强大的工具，能帮你处理从文件整理到复杂数据分析和软件开发的各种任务。</p>

<p>记住，使用Codex完全不需要技术知识。只需几条简单指令，就能让Codex做出惊人的事情。所以别怕尝试，尽情探索Codex能为你做什么。</p>

<h2>常见问题</h2>

<h3>这篇教程和上篇有什么区别？</h3>
<p>上篇（Part 1）从开发者视角覆盖Codex工作流——安装、项目设置、Git、重构和插件。这篇（Part 2）专为<strong>零技术背景的纯新手</strong>设计。用真实咖啡馆案例（整理凌乱的业务文件、创建仪表盘）替代代码示例。还涵盖了上篇没讲的功能："日常办公"模式（隐藏技术细节）、宠物功能和从非开发者视角的Plan Mode流程。如果你是开发者，读上篇；如果你完全没用过AI工具，从这里开始。</p>

<h3>真的一点编程都不需要吗？</h3>
<p>是的。本教程的咖啡馆案例是真实任务——整理发票、销售记录和库存清单——完全不需要编程。Codex在内部处理技术复杂性。你用自然语言描述想要什么，它自己想办法实现。推荐在设置中启用的"日常办公"模式进一步简化体验，隐藏终端输出、文件路径和技术术语。不过，如果你懂编程，Codex会更强大——但入门和提高生产力并不需要。</p>

<h3>Codex和豆包/DeepSeek这类工具有什么区别？</h3>
<p>豆包和DeepSeek是<strong>聊天工具</strong>——回答问题、生成文字。Codex是<strong>Agent</strong>——能真正操作你的电脑：打开文件、编辑表格、整理文件夹、控制浏览器、运行软件。把豆包想象成一个可以问问题的知识渊博的朋友。把Codex想象成一个能帮你干活儿的得力助手。聊天界面看起来相似，但能力本质不同。Codex更接近一个能用你电脑的实习生，而不是一个能回答问题的聊天机器人。</p>

<h3>Codex能在手机上用吗？</h3>
<p>Codex有移动端App（Codex Mobile），连接到你桌面上的Codex。你可以从手机发送任务，Codex在电脑上执行。这在完整Codex指南中有详细说明。对于本教程中的任务（文件整理、仪表盘创建），你最好在电脑前操作。手机适合快速任务，如"检查我的未读消息并汇总"或"把这个事件添加到日历"。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>准备好深入学习Codex？继续你的学习之旅：</p>
  <ul>
    <li><a href="/articles/complete-guide-codex-zero-to-advanced">Codex完全指南：从零基础到高级开发工作流</a> — 面向开发者的完整指南（上篇）</li>
    <li><a href="/articles/official-tutorial-three-ways-codex-control-computer">官方教程：Codex控制电脑的三种方式详解</a> — 掌握Computer Use、Chrome扩展和内置浏览器</li>
    <li><a href="/articles/2026-ai-agent-guide-choose-right-tool-beginners">2026 AI Agent选型指南：新手如何选择最适合的工具</a> — 了解Codex为何排名第一</li>
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