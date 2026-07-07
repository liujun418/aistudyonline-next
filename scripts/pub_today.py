"""
Publish July 7, 2026 — 2 articles, no new tools.
"""
import os

BASE = r"C:\Users\jun\aistudyonline-next"
os.chdir(BASE)

# ===== Part 1: Add 2 article metadata to articles.ts =====
with open('src/lib/articles.ts', 'r', encoding='utf-8') as f:
    articles_src = f.read()

new_articles = r"""  {
    slug: "complete-practical-tutorial-claude-code-core-operations",
    title: "Complete Practical Tutorial: Master All Core Operations Inside Claude Code",
    titleZh: "Claude Code完全实战教程：掌握所有核心操作",
    description: "A hands-on tutorial covering every core Claude Code operation — from CLI installation and project import to file analysis, batch refactoring, automatic debugging, claude.md rules, Git integration, Plan Mode, and permission controls — with executable commands for every step.",
    descriptionZh: "从CLI安装、项目导入到文件分析、批量重构、自动调试、claude.md规则、Git联动、Plan模式和权限控制，每一步都有可执行命令，覆盖Claude Code全部核心操作。",
    category: "AI Tutorials",
    tags: ["Claude Code", "CLI", "Tutorial", "Coding", "Debugging", "Refactoring", "Git"],
    difficulty: "intermediate",
    toolsMentioned: ["Claude Code"],
    date: "2026-07-07",
  },
  {
    slug: "7-mainstream-agent-architectures-beginner-enterprise-guide",
    title: "7 Mainstream Agent Architectures: From Beginner to Enterprise-Grade Guide",
    titleZh: "7大主流Agent架构：从入门到企业级完整指南",
    description: "A systematic breakdown of 7 Agent architectures — Single Agent, ReAct, Plan & Execute, Multi-Agent, Router+Skill, Blackboard, and Graph/Workflow — with pros, cons, best-use cases, and a recommended evolution path from beginner to enterprise.",
    descriptionZh: "系统拆解7种Agent架构——单Agent、ReAct、Plan & Execute、多Agent、Router+Skill、黑板架构和Graph/Workflow——含优缺点、最佳场景和从入门到企业级的推荐演进路径。",
    category: "AI Learning",
    tags: ["AI Agent", "Architecture", "ReAct", "Multi-Agent", "Workflow", "LangGraph", "Enterprise"],
    difficulty: "intermediate",
    toolsMentioned: ["LangGraph", "n8n"],
    date: "2026-07-07",
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
  "complete-practical-tutorial-claude-code-core-operations": {
    content: `<div class="meta-banner">
  <span class="meta-badge">📚 AI Tutorials</span>
  <span class="meta-badge">🕒 10 min read</span>
  <span class="meta-badge">📅 Jul 7, 2026</span>
  <span class="meta-badge">🎯 Intermediate</span>
</div>

<h2 id="introduction">Introduction</h2>

<p>Claude Code has become the top AI coding assistant favored by most developers for its powerful file reading, project refactoring, debugging and autonomous running capabilities. This full practical tutorial covers every core operation step by step, helping beginners get started quickly and helping senior developers maximize its productivity. All operations are matched with executable code snippets and command lines for direct replication.</p>

<h2 id="setup">1. Basic Environment Preparation & Project Import</h2>

<h3>1.1 Install and Launch Claude Code CLI</h3>

<p>Open your local terminal and run the installation command:</p>

<pre><code class="language-bash">npm install -g @anthropic-ai/claude-code</code></pre>

<p>After installation, verify successful installation with this command:</p>

<pre><code class="language-bash">claude-code --version</code></pre>

<h3>1.2 Import Local Project Folder</h3>

<p>Switch to your project root directory in terminal first:</p>

<pre><code class="language-bash">cd /Users/yourname/Desktop/my-project</code></pre>

<p>Start Claude Code workspace binding:</p>

<pre><code class="language-bash">claude-code init</code></pre>

<p>This command generates a hidden <code>.claude/</code> configuration folder, which stores project rules, conversation records and permission settings automatically.</p>

<h3>1.3 Configure API Key</h3>

<p>Run the login command to bind your Anthropic API key:</p>

<pre><code class="language-bash">claude-code login</code></pre>

<p>Paste your API key when prompted, and the tool will automatically save credentials locally without repeated input.</p>

<h2 id="file-reading">2. Core File Reading & Batch Analysis Functions</h2>

<p>Claude Code can scan the entire project instead of single files like ordinary chatbots.</p>

<h3>2.1 Read Entire Project Codebase</h3>

<p>Input this natural language instruction inside Claude Code dialogue box:</p>

<pre><code class="language-text">Scan all .js and .ts files under src folder, sort out all unused functions and output a formatted list</code></pre>

<h3>2.2 Targeted Single File Deep Analysis</h3>

<p>Command for analyzing specific files via terminal:</p>

<pre><code class="language-bash">claude-code analyze ./src/utils/request.ts</code></pre>

<p>The output will include code logic explanations, potential bugs, optimization suggestions and redundant code extraction.</p>

<h2 id="refactoring">3. One-Click Code Refactoring Operation</h2>

<h3>3.1 Batch Refactor Old Syntax</h3>

<p>Enter the prompt inside Claude Code panel:</p>

<pre><code class="language-text">Refactor all var declarations in this project to const/let, add standardized JSDoc comments for all exported functions, and run format after modification</code></pre>

<p>Claude Code will traverse all target files, modify code automatically and format files with ESLint/Prettier.</p>

<h3>3.2 Component Structure Optimization (Frontend Demo)</h3>

<p>Sample refactor task prompt for React projects:</p>

<pre><code class="language-text">Split the monolithic Home page component into PageHeader, ContentList and Footer sub-components, extract repeated styles into separate css module files</code></pre>

<h2 id="debugging">4. Automatic Debugging & Error Repair</h2>

<h3>4.1 Upload Error Logs for Intelligent Fixing</h3>

<p>Copy your project crash log and send it with this fixed prompt template:</p>

<pre><code class="language-text">Check the following error log, locate the root cause in project files, write the complete modified code and explain the repair logic:
[Paste your error log here]</code></pre>

<h3>4.2 Run Test Script Automatically to Verify Fixes</h3>

<p>After code modification, execute test commands directly inside Claude Code dialogue:</p>

<pre><code class="language-text">Run npm test and check if all unit tests pass, fix failed test cases automatically</code></pre>

<p>Terminal execution command shortcut:</p>

<pre><code class="language-bash">claude-code run-test</code></pre>

<h2 id="claude-md">5. Custom Project Rules via claude.md</h2>

<p>Create a <code>claude.md</code> file under project root to lock uniform development standards, sample content:</p>

<pre><code class="language-markdown"># Global Code Rules for This Project
1. All new functions must carry type annotations
2. Do not use any deprecated npm packages
3. Every code change needs corresponding unit test writing
4. Automatically generate git commit message after each modification</code></pre>

<p>After saving, every subsequent dialogue task will strictly follow rules in this file without repeated manual reminder.</p>

<h2 id="git">6. Git Linkage & Automated Commit Workflow</h2>

<h3>6.1 Auto Generate Standard Commit Information</h3>

<p>After Claude Code finishes modifying code, input this instruction:</p>

<pre><code class="language-text">Check all changed files, generate concise standardized commit message, execute git add and git commit automatically</code></pre>

<h3>6.2 Terminal Git Operation Command Set</h3>

<pre><code class="language-bash"># View all modified files scanned by Claude Code
claude-code git-diff
# Auto commit changes with AI-generated message
claude-code git-commit</code></pre>

<h2 id="plan-mode">7. Multi-Step Complex Task Planning Mode</h2>

<p>For large-scale cross-file reconstruction, enable Plan Mode first to avoid chaotic modification:</p>

<pre><code class="language-text">Enable plan mode, split the task "transform vanilla js project to Vue3 + Vite project" into detailed executable steps, confirm the plan with me before executing any code changes</code></pre>

<p>Claude Code will output a complete step-by-step plan list, waiting for your manual approval before operating project files.</p>

<h2 id="permissions">8. Permission Control & Safety Settings</h2>

<h3>8.1 Adjust File Operation Permission</h3>

<p>Enter settings command in terminal:</p>

<pre><code class="language-bash">claude-code config permission</code></pre>

<p>Three optional permission modes:</p>
<ol>
  <li>Prompt before every file write operation (recommended for beginners)</li>
  <li>Auto approve safe read/write operations only</li>
  <li>Full access mode (only for trusted local private projects)</li>
</ol>

<h3>8.2 Block Sensitive File Access</h3>

<p>Add paths to blacklist in <code>.claude/config.json</code> to prevent accidental modification of configuration files:</p>

<pre><code class="language-json">{
  "fileBlacklist": [".env", "package-lock.json", "database/config.js"]
}</code></pre>

<h2 id="tips">9. Common Practical Tips to Boost Efficiency</h2>

<ol>
  <li>Shortcut: Use <code>claude-code chat</code> to quickly open dialogue window without opening full desktop client</li>
  <li>Context cleaning command to avoid context overflow: <code>claude-code clear-context</code></li>
  <li>Export conversation records for backup: <code>claude-code export-log chat_record.json</code></li>
  <li>For large projects exceeding token limits: Split tasks by folders, do not scan the whole project at one time</li>
</ol>

<h2 id="conclusion">Conclusion</h2>

<p>Claude Code's core advantage lies in its deep local project interaction capability, far exceeding ordinary web AI chat tools. Master the above terminal commands, file operation logic and plan/refactor workflow, you can cut 70% repetitive coding, debugging and sorting work. Beginners are suggested to start from basic file analysis and single-file refactoring, then gradually try multi-step complex transformation tasks after getting familiar with permission and rule configuration.</p>

<h2>常见问题</h2>

<h3>Claude Code CLI vs desktop app — which should I use?</h3>
<p>The CLI version is more powerful and flexible — it's the one developers use for serious work. The desktop app has a nicer UI but lacks some CLI features like <code>claude-code git-commit</code> and <code>claude-code analyze</code>. If you're comfortable with a terminal, go CLI. If you're a beginner or prefer visual interfaces, start with the desktop app and gradually learn CLI commands as you need more power. The good news: both share the same project configuration (<code>.claude/</code> folder and <code>claude.md</code> rules), so you can switch between them freely.</p>

<h3>How is claude.md different from agent.md (used by Codex)?</h3>
<p>They serve the same purpose — project-level instructions that the AI follows in every conversation — but use different filenames. Claude Code reads <code>claude.md</code> (or <code>CLAUDE.md</code>) from the project root. Codex reads <code>agent.md</code>. If you work with both tools, you can create both files with the same content, or create a symlink. The format is identical: plain markdown with rules, conventions, and preferences. Neither tool reads the other's file, so dual-tool users need both.</p>

<h3>What's the difference between Plan Mode and just asking Claude Code to do a task?</h3>
<p>In normal mode, Claude Code starts executing immediately — it reads files, makes changes, and runs commands as it goes. This works great for small tasks but can go off the rails on complex multi-file refactors. Plan Mode forces Claude Code to <strong>think first, act later</strong>: it outputs a complete step-by-step plan and waits for your approval before touching any files. This is critical for tasks like "migrate from JavaScript to TypeScript" or "restructure the entire component tree" where a wrong first step cascades into hours of cleanup.</p>

<h3>Can I use Claude Code with models other than Claude?</h3>
<p>Yes, via CC Switch (a community tool). It lets you route Claude Code's API calls to alternative models including domestic Chinese models. The experience won't be identical — Claude Code's harness engineering is optimized for Claude models — but for basic coding tasks, the difference is often negligible. Many developers use Claude models for complex refactoring and debugging, then switch to cheaper models for routine tasks like adding comments or formatting. This hybrid approach can cut API costs by 50%+ without sacrificing quality on critical work.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Mastered Claude Code operations? Level up your development workflow:</p>
  <ul>
    <li><a href="/articles/complete-guide-codex-zero-to-advanced">Complete Guide to Codex: From Zero to Advanced Development Workflow</a> — compare with the other leading AI dev tool</li>
    <li><a href="/articles/2026-ai-agent-guide-choose-right-tool-beginners">2026 AI Agent Guide: How to Choose the Right Tool for Beginners</a> — see where Claude Code ranks among all Agents</li>
    <li><a href="/articles/7-mainstream-agent-architectures-beginner-enterprise-guide">7 Mainstream Agent Architectures: From Beginner to Enterprise-Grade Guide</a> — understand the architecture behind Claude Code</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">📚 AI 教程</span>
  <span class="meta-badge">🕒 阅读约10分钟</span>
  <span class="meta-badge">📅 2026年7月7日</span>
  <span class="meta-badge">🎯 中级</span>
</div>

<h2 id="introduction">引言</h2>

<p>Claude Code 凭借强大的文件阅读、项目重构、调试和自主运行能力，已成为大多数开发者首选的 AI 编程助手。这篇完整实战教程逐步覆盖每一项核心操作，帮助新手快速上手，也帮助资深开发者最大化其生产力。所有操作都配有可执行的代码片段和命令行，可直接复制使用。</p>

<h2 id="setup">1. 基础环境准备与项目导入</h2>

<h3>1.1 安装并启动 Claude Code CLI</h3>

<p>打开本地终端，运行安装命令：</p>

<pre><code class="language-bash">npm install -g @anthropic-ai/claude-code</code></pre>

<p>安装后验证是否成功：</p>

<pre><code class="language-bash">claude-code --version</code></pre>

<h3>1.2 导入本地项目文件夹</h3>

<p>先在终端中切换到项目根目录：</p>

<pre><code class="language-bash">cd /Users/yourname/Desktop/my-project</code></pre>

<p>启动 Claude Code 工作区绑定：</p>

<pre><code class="language-bash">claude-code init</code></pre>

<p>该命令会生成隐藏的 <code>.claude/</code> 配置文件夹，自动存储项目规则、对话记录和权限设置。</p>

<h3>1.3 配置 API Key</h3>

<p>运行登录命令绑定 Anthropic API 密钥：</p>

<pre><code class="language-bash">claude-code login</code></pre>

<p>按提示粘贴 API Key，工具会自动在本地保存凭证，无需重复输入。</p>

<h2 id="file-reading">2. 核心文件阅读与批量分析功能</h2>

<p>Claude Code 能扫描整个项目，而非像普通聊天机器人那样只能看单个文件。</p>

<h3>2.1 阅读整个项目代码库</h3>

<p>在 Claude Code 对话框中输入自然语言指令：</p>

<pre><code class="language-text">扫描 src 文件夹下所有 .js 和 .ts 文件，梳理出所有未使用的函数并输出格式化列表</code></pre>

<h3>2.2 针对性单文件深度分析</h3>

<p>通过终端分析特定文件的命令：</p>

<pre><code class="language-bash">claude-code analyze ./src/utils/request.ts</code></pre>

<p>输出将包含代码逻辑解释、潜在 Bug、优化建议和冗余代码提取。</p>

<h2 id="refactoring">3. 一键代码重构操作</h2>

<h3>3.1 批量重构旧语法</h3>

<p>在 Claude Code 面板中输入提示词：</p>

<pre><code class="language-text">将项目中所有 var 声明重构为 const/let，为所有导出函数添加标准化 JSDoc 注释，修改后自动运行格式化</code></pre>

<p>Claude Code 会遍历所有目标文件，自动修改代码并用 ESLint/Prettier 格式化。</p>

<h3>3.2 组件结构优化（前端示例）</h3>

<p>React 项目重构任务提示词示例：</p>

<pre><code class="language-text">将 monolithic 的 Home 页面组件拆分为 PageHeader、ContentList 和 Footer 子组件，将重复样式提取到独立的 css module 文件</code></pre>

<h2 id="debugging">4. 自动调试与报错修复</h2>

<h3>4.1 上传错误日志让 AI 智能修复</h3>

<p>复制项目崩溃日志，搭配这个固定提示词模板发送：</p>

<pre><code class="language-text">检查以下错误日志，在项目文件中定位根本原因，写出完整修改代码并解释修复逻辑：
[在此粘贴你的错误日志]</code></pre>

<h3>4.2 自动运行测试脚本验证修复</h3>

<p>代码修改后，直接在 Claude Code 对话中执行测试命令：</p>

<pre><code class="language-text">运行 npm test 并检查所有单元测试是否通过，自动修复失败的测试用例</code></pre>

<p>终端快捷执行命令：</p>

<pre><code class="language-bash">claude-code run-test</code></pre>

<h2 id="claude-md">5. 通过 claude.md 自定义项目规则</h2>

<p>在项目根目录创建 <code>claude.md</code> 文件锁定统一开发规范，示例内容：</p>

<pre><code class="language-markdown"># 本项目全局代码规则
1. 所有新函数必须携带类型注解
2. 不使用任何已弃用的 npm 包
3. 每次代码变更需编写对应单元测试
4. 每次修改后自动生成 git commit 信息</code></pre>

<p>保存后，后续每次对话任务都会严格遵循此文件中的规则，无需手动重复提醒。</p>

<h2 id="git">6. Git 联动与自动化提交工作流</h2>

<h3>6.1 自动生成规范提交信息</h3>

<p>Claude Code 完成代码修改后，输入指令：</p>

<pre><code class="language-text">检查所有变更文件，生成简洁规范的 commit message，自动执行 git add 和 git commit</code></pre>

<h3>6.2 终端 Git 操作命令集</h3>

<pre><code class="language-bash"># 查看 Claude Code 扫描到的所有修改文件
claude-code git-diff
# 自动提交变更并生成 AI 提交信息
claude-code git-commit</code></pre>

<h2 id="plan-mode">7. 多步骤复杂任务规划模式</h2>

<p>对于大规模跨文件重构，先启用 Plan Mode 避免修改混乱：</p>

<pre><code class="language-text">启用 plan mode，将"原生 JS 项目改造为 Vue3 + Vite 项目"任务拆分为详细可执行步骤，先确认方案再执行任何代码变更</code></pre>

<p>Claude Code 会输出完整的分步计划列表，等待你手动批准后再操作项目文件。</p>

<h2 id="permissions">8. 权限控制与安全设置</h2>

<h3>8.1 调整文件操作权限</h3>

<p>在终端输入设置命令：</p>

<pre><code class="language-bash">claude-code config permission</code></pre>

<p>三种可选权限模式：</p>
<ol>
  <li>每次文件写入前提示（推荐新手使用）</li>
  <li>仅自动批准安全的读写操作</li>
  <li>完全访问模式（仅限可信的本地私有项目）</li>
</ol>

<h3>8.2 阻止敏感文件访问</h3>

<p>在 <code>.claude/config.json</code> 中添加黑名单路径，防止误改配置文件：</p>

<pre><code class="language-json">{
  "fileBlacklist": [".env", "package-lock.json", "database/config.js"]
}</code></pre>

<h2 id="tips">9. 常见提效实用技巧</h2>

<ol>
  <li>快捷方式：使用 <code>claude-code chat</code> 快速打开对话窗口，无需启动完整桌面客户端</li>
  <li>上下文清理命令避免溢出：<code>claude-code clear-context</code></li>
  <li>导出对话记录备份：<code>claude-code export-log chat_record.json</code></li>
  <li>大型项目超出 token 限制：按文件夹拆分任务，不要一次性扫描整个项目</li>
</ol>

<h2 id="conclusion">总结</h2>

<p>Claude Code 的核心优势在于深度本地项目交互能力，远超普通网页 AI 聊天工具。掌握以上终端命令、文件操作逻辑和 Plan/Refactor 工作流，你可以砍掉 70% 的重复编码、调试和整理工作。建议新手从基础文件分析和单文件重构开始，熟悉权限和规则配置后再逐步尝试多步骤复杂改造任务。</p>

<h2>常见问题</h2>

<h3>Claude Code CLI 和桌面版该选哪个？</h3>
<p>CLI 版更强大灵活——是开发者做正经工作的首选。桌面版 UI 更好看但缺少一些 CLI 功能，如 <code>claude-code git-commit</code> 和 <code>claude-code analyze</code>。如果你习惯终端，选 CLI。如果你是新手或偏好可视化界面，从桌面版开始，需要更强能力时逐步学 CLI 命令。好消息：两者共享同一套项目配置（<code>.claude/</code> 文件夹和 <code>claude.md</code> 规则），可自由切换。</p>

<h3>claude.md 和 Codex 的 agent.md 有什么区别？</h3>
<p>它们功能相同——都是 AI 在每次对话中遵循的项目级指令——但文件名不同。Claude Code 读取项目根目录的 <code>claude.md</code>（或 <code>CLAUDE.md</code>）。Codex 读取 <code>agent.md</code>。如果你同时使用两个工具，可以创建两个文件内容相同，或创建软链接。格式完全一致：纯 Markdown 写规则、约定和偏好。两个工具不会读取对方的文件，所以双工具用户两个都需要。</p>

<h3>Plan Mode 和直接让 Claude Code 做任务有什么区别？</h3>
<p>普通模式下，Claude Code 立即开始执行——边读文件、边改代码、边跑命令。小任务没问题，但复杂多文件重构容易跑偏。Plan Mode 强制 Claude Code <strong>先想再做</strong>：输出完整分步计划，等你批准后才会碰任何文件。这对"JS 迁移到 TypeScript"或"重构整个组件树"这类任务至关重要——第一步错了会连锁反应，清理成本数小时。</p>

<h3>Claude Code 能用 Claude 以外的模型吗？</h3>
<p>可以，通过 CC Switch（社区工具）。它能将 Claude Code 的 API 调用路由到替代模型，包括国产中文模型。体验不会完全一致——Claude Code 的 Harness 工程为 Claude 模型优化——但基础编码任务差异通常可忽略。很多开发者的策略：复杂重构和调试用 Claude 模型，加注释、格式化等常规任务切换到更便宜的模型。这种混合方案可削减 50%+ 的 API 成本，同时关键工作质量不受影响。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>掌握了 Claude Code 操作？升级你的开发工作流：</p>
  <ul>
    <li><a href="/articles/complete-guide-codex-zero-to-advanced">Codex 完全指南：从零基础到高级开发工作流</a> — 对比另一款顶级 AI 开发工具</li>
    <li><a href="/articles/2026-ai-agent-guide-choose-right-tool-beginners">2026 AI Agent 选型指南：新手如何选择最适合的工具</a> — 了解 Claude Code 在所有 Agent 中的排名</li>
    <li><a href="/articles/7-mainstream-agent-architectures-beginner-enterprise-guide">7大主流 Agent 架构：从入门到企业级完整指南</a> — 理解 Claude Code 背后的架构原理</li>
  </ul>
</div>`,
  },

  "7-mainstream-agent-architectures-beginner-enterprise-guide": {
    content: `<div class="meta-banner">
  <span class="meta-badge">📚 AI Learning</span>
  <span class="meta-badge">🕒 9 min read</span>
  <span class="meta-badge">📅 Jul 7, 2026</span>
  <span class="meta-badge">🎯 Intermediate</span>
</div>

<h2 id="introduction">Introduction</h2>

<p>Nowadays, everyone is talking about AI Agents, but do you know how they are actually built? This article will break down the 7 most mainstream Agent architectures, from simple beginner-level ones to enterprise-grade solutions. By the end, you'll know which architecture is best suited for your specific use case.</p>

<h3>Core Takeaways Before Diving In</h3>

<ol>
  <li>There's no universal standard for Agent architectures — your choice depends entirely on how complex your scenario is and how much control you need.</li>
  <li>The overall evolution path goes from <strong>single Agent</strong> → <strong>multi-Agent collaboration</strong> → <strong>graph-based workflows</strong>.</li>
  <li>If you're building AI coding tools or skill-based systems, the <strong>Router + Skill</strong> architecture is currently the best practice.</li>
</ol>

<h2 id="single-agent">1. Single Agent Architecture</h2>

<p>The simplest architecture, where one large language model (LLM) handles everything.</p>

<h3>How It Works</h3>
<p>User input → LLM thinks → calls tools → outputs results.</p>

<h3>Pros</h3>
<ul>
  <li>Simple and easy to implement</li>
  <li>Low cost</li>
  <li>Works for basic tasks (like ChatGPT)</li>
</ul>

<h3>Cons</h3>
<ul>
  <li>Struggles with complex tasks: The LLM can get overwhelmed ("thinking explosion")</li>
  <li>Severe context pollution when handling multiple tasks at once</li>
  <li>Not suitable for multi-step or long-running workflows</li>
</ul>

<h3>Best For</h3>
<p>Quick validation of simple tasks, personal assistants, or basic chatbots.</p>

<h2 id="react">2. ReAct Architecture</h2>

<p>Short for <strong>Reason + Act</strong>, this is the classic Agent paradigm.</p>

<h3>How It Works</h3>
<p>It follows a loop:</p>
<ol>
  <li><strong>Think</strong>: Analyze the problem and generate ideas</li>
  <li><strong>Act</strong>: Select and call appropriate tools</li>
  <li><strong>Observe</strong>: Get results from tools</li>
  <li><strong>Repeat</strong>: Adjust thinking based on results until the task is complete</li>
</ol>

<h3>Pros</h3>
<ul>
  <li>Strong chain-of-thought reasoning</li>
  <li>High explainability (you can see the step-by-step process)</li>
  <li>Handles multi-step tasks effectively</li>
</ul>

<h3>Cons</h3>
<ul>
  <li>High token consumption</li>
  <li>Unstable and prone to going off-track</li>
  <li>Not suitable for large-scale engineering systems</li>
</ul>

<h3>Best For</h3>
<p>Exploratory tasks, complex problem-solving, or research scenarios.</p>

<h2 id="plan-execute">3. Plan & Execute Architecture</h2>

<p>A more engineering-focused architecture that separates planning from execution.</p>

<h3>How It Works</h3>
<ol>
  <li><strong>Plan</strong>: A "Planner" generates a complete step-by-step plan</li>
  <li><strong>Execute</strong>: An "Executor" follows each step one by one</li>
</ol>

<h3>Pros</h3>
<ul>
  <li>High stability</li>
  <li>Excellent for code generation, project automation, and long-running tasks</li>
  <li>Predictable workflow</li>
</ul>

<h3>Cons</h3>
<ul>
  <li>If the initial plan is wrong, the entire task fails</li>
  <li>Less flexible than ReAct</li>
</ul>

<h3>Best For</h3>
<p>Code generation, project automation, and long-running workflows.</p>

<h2 id="multi-agent">4. Multi-Agent Architecture</h2>

<p>Multiple Agents work together, each with a specific role.</p>

<h3>How It Works</h3>
<p>An <strong>Orchestrator</strong> coordinates tasks and assigns them to specialized Agents:</p>
<ul>
  <li><strong>Planner</strong>: Breaks down tasks</li>
  <li><strong>Coder</strong>: Writes and tests code</li>
  <li><strong>Reviewer</strong>: Checks and verifies results</li>
  <li><strong>Tool Agent</strong>: Calls external tools</li>
</ul>

<h3>Pros</h3>
<ul>
  <li>Clear task breakdown</li>
  <li>Reduced context pollution</li>
  <li>Highly scalable</li>
</ul>

<h3>Cons</h3>
<ul>
  <li>High development and maintenance cost</li>
  <li>Complex coordination between Agents</li>
</ul>

<h3>Best For</h3>
<p>Team collaboration, complex projects, and enterprise-level applications.</p>

<h2 id="router-skill">5. Router + Skill Architecture</h2>

<p>My personal recommendation for many use cases. The core idea: <strong>Don't let the model "think" — let it "choose."</strong></p>

<h3>How It Works</h3>
<ol>
  <li><strong>Intent Router</strong>: Identifies the user's intent</li>
  <li><strong>Router</strong>: Directs the request to the corresponding <strong>Skill</strong></li>
  <li><strong>Skill</strong>: Each Skill is a self-contained capability with its own logic and knowledge</li>
</ol>

<h3>Pros</h3>
<ul>
  <li>Extremely stable</li>
  <li>Enterprise-grade controllability</li>
  <li>Cacheable (high performance)</li>
  <li>Easy to evaluate success rates</li>
</ul>

<h3>Cons</h3>
<ul>
  <li>High Skill design cost</li>
  <li>Potential for intent matching conflicts</li>
</ul>

<h3>Best For</h3>
<p>AI coding tools, skill-based systems, and scenarios requiring high reliability.</p>

<h2 id="blackboard">6. Blackboard Architecture</h2>

<p>Multiple Agents share a common "blackboard" (shared state) and work together.</p>

<h3>How It Works</h3>
<ul>
  <li>All Agents can read and write to the shared blackboard</li>
  <li>Execution is driven by changes in the shared state</li>
  <li>Agents collaborate by updating and reacting to the blackboard</li>
</ul>

<h3>Pros</h3>
<ul>
  <li>Excellent for complex collaborative scenarios</li>
  <li>Enables dynamic task distribution</li>
</ul>

<h3>Cons</h3>
<ul>
  <li>Complex state management</li>
  <li>Hard to debug when things go wrong</li>
</ul>

<h3>Best For</h3>
<p>Complex collaborative scenarios, workflow engines, and distributed systems.</p>

<h2 id="graph-workflow">7. Graph/Workflow Architecture</h2>

<p>The mainstream enterprise-grade architecture, based on <strong>Directed Acyclic Graphs (DAGs)</strong>.</p>

<h3>How It Works</h3>
<ul>
  <li>Workflows are arranged as DAGs</li>
  <li>Supports conditional branching and parallel execution</li>
  <li>Tasks can be traced, debugged, and retried</li>
</ul>

<h3>Popular Tools</h3>
<ul>
  <li>LangGraph</li>
  <li>Temporal</li>
  <li>Airflow</li>
  <li>n8n</li>
  <li>Prefect</li>
</ul>

<h3>Pros</h3>
<ul>
  <li>Enterprise-grade stability</li>
  <li>Debug-friendly</li>
  <li>Supports long-running workflows</li>
  <li>Ideal for production environments</li>
</ul>

<h3>Cons</h3>
<ul>
  <li>Steeper learning curve</li>
  <li>More complex to set up and maintain</li>
</ul>

<h3>Best For</h3>
<p>Enterprise-level process automation and production environments.</p>

<h2 id="evolution-path">Recommended Evolution Path</h2>

<p>You don't need to jump to the most complex architecture immediately. Follow this path based on your needs:</p>

<ol>
  <li><strong>Single Agent</strong>: Quick validation of simple tasks</li>
  <li><strong>ReAct</strong>: Multi-step exploration</li>
  <li><strong>Plan & Execute</strong>: Engineering implementation</li>
  <li><strong>Multi-Agent</strong>: Collaborative execution</li>
  <li><strong>Router + Skill</strong>: Precision skill systems</li>
  <li><strong>Blackboard</strong>: Shared state management</li>
  <li><strong>Graph/Workflow</strong>: Enterprise-grade production</li>
</ol>

<h2 id="final-note">Final Note</h2>

<p>There's no "best" architecture — only the <strong>most suitable</strong> one for your scenario. Choose based on the complexity of your task, your need for control, and your long-term goals.</p>

<h2>常见问题</h2>

<h3>Which architecture should a beginner start with?</h3>
<p>Start with <strong>Single Agent</strong> to understand the basic loop (input → think → tool → output). Once comfortable, move to <strong>ReAct</strong> to experience multi-step reasoning. Most beginners never need to go beyond ReAct + Plan & Execute for personal projects. The jump to Multi-Agent and Graph/Workflow is an engineering decision, not a learning milestone — you only need those when a single Agent can't handle the task complexity or when you need production-grade reliability and traceability.</p>

<h3>Why is Router + Skill recommended as the current best practice for coding tools?</h3>
<p>Because it solves the biggest problem with Agent-based coding: <strong>unpredictability</strong>. In a ReAct or Plan & Execute architecture, the model decides what to do at each step — which means it can make creative but wrong decisions. Router + Skill flips this: instead of the model thinking "how do I solve this?", it thinks "which pre-built Skill solves this?" Each Skill is a tested, deterministic workflow. The model's job becomes classification (matching intent to Skill), not generation (inventing a solution on the fly). This is dramatically more reliable for production coding tools where correctness matters more than creativity.</p>

<h3>What's the difference between Multi-Agent and Graph/Workflow architectures?</h3>
<p>Multi-Agent is about <strong>who</strong> does the work — multiple specialized Agents collaborating. Graph/Workflow is about <strong>how</strong> the work flows — tasks arranged in a DAG with conditional branching, parallel execution, and retry logic. They're not mutually exclusive: you can have a Graph/Workflow that orchestrates multiple Agents. Think of Multi-Agent as the team structure and Graph/Workflow as the project management methodology. Enterprise systems typically use both: Graph/Workflow for the overall process, with specialized Agents handling individual nodes in the graph.</p>

<h3>When should I NOT use an Agent architecture at all?</h3>
<p>When a simple API call or script does the job. Agent architectures add latency, cost, and complexity. If your task is deterministic (e.g., "resize this image to 800px" or "translate this text to French"), a direct function call is faster, cheaper, and more reliable. The Agent sweet spot is tasks with ambiguity: "review this pull request and suggest improvements" or "research this topic and write a summary." A good rule of thumb: if you can write the logic as a flowchart with no "it depends" branches, you probably don't need an Agent.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Understand the architectures? See them in action:</p>
  <ul>
    <li><a href="/articles/complete-practical-tutorial-claude-code-core-operations">Complete Practical Tutorial: Master All Core Operations Inside Claude Code</a> — see Plan & Execute and Multi-Agent in a real tool</li>
    <li><a href="/articles/2026-ai-agent-guide-choose-right-tool-beginners">2026 AI Agent Guide: How to Choose the Right Tool for Beginners</a> — match architectures to specific tools</li>
    <li><a href="/articles/demystifying-ai-application-layer-3-layers">Demystifying AI Application Layer: From LLMs to Agents in 3 Layers</a> — understand where Agents fit in the broader AI stack</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">📚 AI 学习</span>
  <span class="meta-badge">🕒 阅读约9分钟</span>
  <span class="meta-badge">📅 2026年7月7日</span>
  <span class="meta-badge">🎯 中级</span>
</div>

<h2 id="introduction">引言</h2>

<p>如今人人都在谈论 AI Agent，但你知道它们到底是怎么构建的吗？本文将拆解 7 种最主流的 Agent 架构，从简单入门级到企业级方案。读完你会知道哪种架构最适合你的具体场景。</p>

<h3>开篇核心要点</h3>

<ol>
  <li>Agent 架构没有通用标准——选择完全取决于你的场景有多复杂、你需要多少控制力。</li>
  <li>整体演进路径：<strong>单 Agent</strong> → <strong>多 Agent 协作</strong> → <strong>图驱动工作流</strong>。</li>
  <li>如果你在构建 AI 编码工具或技能系统，<strong>Router + Skill</strong> 架构是当前最佳实践。</li>
</ol>

<h2 id="single-agent">1. 单 Agent 架构</h2>

<p>最简单的架构，一个大语言模型（LLM）包揽一切。</p>

<h3>工作原理</h3>
<p>用户输入 → LLM 思考 → 调用工具 → 输出结果。</p>

<h3>优势</h3>
<ul>
  <li>简单易实现</li>
  <li>成本低</li>
  <li>适用于基础任务（如 ChatGPT）</li>
</ul>

<h3>不足</h3>
<ul>
  <li>复杂任务力不从心：LLM 容易"思考爆炸"</li>
  <li>同时处理多个任务时上下文污染严重</li>
  <li>不适合多步骤或长时间运行的工作流</li>
</ul>

<h3>最适合</h3>
<p>简单任务快速验证、个人助手、基础聊天机器人。</p>

<h2 id="react">2. ReAct 架构</h2>

<p><strong>推理 + 行动</strong>（Reason + Act）的缩写，经典的 Agent 范式。</p>

<h3>工作原理</h3>
<p>遵循一个循环：</p>
<ol>
  <li><strong>思考</strong>：分析问题，产生想法</li>
  <li><strong>行动</strong>：选择并调用合适的工具</li>
  <li><strong>观察</strong>：获取工具返回结果</li>
  <li><strong>重复</strong>：根据结果调整思考，直到任务完成</li>
</ol>

<h3>优势</h3>
<ul>
  <li>思维链推理能力强</li>
  <li>可解释性高（能看清每一步过程）</li>
  <li>有效处理多步骤任务</li>
</ul>

<h3>不足</h3>
<ul>
  <li>Token 消耗高</li>
  <li>不稳定，容易跑偏</li>
  <li>不适合大规模工程系统</li>
</ul>

<h3>最适合</h3>
<p>探索性任务、复杂问题求解、研究场景。</p>

<h2 id="plan-execute">3. Plan & Execute 架构</h2>

<p>更偏工程的架构，将规划与执行分离。</p>

<h3>工作原理</h3>
<ol>
  <li><strong>规划</strong>："规划器"生成完整的分步计划</li>
  <li><strong>执行</strong>："执行器"按步骤逐一执行</li>
</ol>

<h3>优势</h3>
<ul>
  <li>稳定性高</li>
  <li>代码生成、项目自动化和长任务表现出色</li>
  <li>工作流可预测</li>
</ul>

<h3>不足</h3>
<ul>
  <li>初始计划如果出错，整个任务失败</li>
  <li>灵活性不如 ReAct</li>
</ul>

<h3>最适合</h3>
<p>代码生成、项目自动化、长时间运行的工作流。</p>

<h2 id="multi-agent">4. 多 Agent 架构</h2>

<p>多个 Agent 协作，每个有特定角色。</p>

<h3>工作原理</h3>
<p><strong>编排器</strong>协调任务并分配给专业化 Agent：</p>
<ul>
  <li><strong>规划器</strong>：拆解任务</li>
  <li><strong>编码器</strong>：编写和测试代码</li>
  <li><strong>审查器</strong>：检查和验证结果</li>
  <li><strong>工具 Agent</strong>：调用外部工具</li>
</ul>

<h3>优势</h3>
<ul>
  <li>任务分工清晰</li>
  <li>减少上下文污染</li>
  <li>高度可扩展</li>
</ul>

<h3>不足</h3>
<ul>
  <li>开发和维护成本高</li>
  <li>Agent 间协调复杂</li>
</ul>

<h3>最适合</h3>
<p>团队协作、复杂项目、企业级应用。</p>

<h2 id="router-skill">5. Router + Skill 架构</h2>

<p>个人推荐。核心理念：<strong>不要让模型"思考"——让它"选择"。</strong></p>

<h3>工作原理</h3>
<ol>
  <li><strong>意图路由器</strong>：识别用户意图</li>
  <li><strong>路由器</strong>：将请求导向对应的 <strong>Skill</strong></li>
  <li><strong>Skill</strong>：每个 Skill 是自包含的能力单元，有自己的逻辑和知识</li>
</ol>

<h3>优势</h3>
<ul>
  <li>极其稳定</li>
  <li>企业级可控性</li>
  <li>可缓存（高性能）</li>
  <li>易于评估成功率</li>
</ul>

<h3>不足</h3>
<ul>
  <li>Skill 设计成本高</li>
  <li>可能存在意图匹配冲突</li>
</ul>

<h3>最适合</h3>
<p>AI 编码工具、技能系统、需要高可靠性的场景。</p>

<h2 id="blackboard">6. 黑板架构</h2>

<p>多个 Agent 共享一块"黑板"（共享状态）协同工作。</p>

<h3>工作原理</h3>
<ul>
  <li>所有 Agent 可读写共享黑板</li>
  <li>执行由共享状态的变化驱动</li>
  <li>Agent 通过更新和响应黑板来协作</li>
</ul>

<h3>优势</h3>
<ul>
  <li>复杂协作场景表现出色</li>
  <li>支持动态任务分配</li>
</ul>

<h3>不足</h3>
<ul>
  <li>状态管理复杂</li>
  <li>出问题时难以调试</li>
</ul>

<h3>最适合</h3>
<p>复杂协作场景、工作流引擎、分布式系统。</p>

<h2 id="graph-workflow">7. Graph/Workflow 架构</h2>

<p>主流企业级架构，基于<strong>有向无环图（DAG）</strong>。</p>

<h3>工作原理</h3>
<ul>
  <li>工作流以 DAG 形式编排</li>
  <li>支持条件分支和并行执行</li>
  <li>任务可追踪、调试和重试</li>
</ul>

<h3>常用工具</h3>
<ul>
  <li>LangGraph</li>
  <li>Temporal</li>
  <li>Airflow</li>
  <li>n8n</li>
  <li>Prefect</li>
</ul>

<h3>优势</h3>
<ul>
  <li>企业级稳定性</li>
  <li>调试友好</li>
  <li>支持长时间运行的工作流</li>
  <li>适合生产环境</li>
</ul>

<h3>不足</h3>
<ul>
  <li>学习曲线较陡</li>
  <li>搭建和维护更复杂</li>
</ul>

<h3>最适合</h3>
<p>企业级流程自动化、生产环境。</p>

<h2 id="evolution-path">推荐演进路径</h2>

<p>你不需要一步跳到最复杂的架构。根据需求按以下路径演进：</p>

<ol>
  <li><strong>单 Agent</strong>：简单任务快速验证</li>
  <li><strong>ReAct</strong>：多步骤探索</li>
  <li><strong>Plan & Execute</strong>：工程化落地</li>
  <li><strong>多 Agent</strong>：协作执行</li>
  <li><strong>Router + Skill</strong>：精准技能系统</li>
  <li><strong>黑板架构</strong>：共享状态管理</li>
  <li><strong>Graph/Workflow</strong>：企业级生产</li>
</ol>

<h2 id="final-note">最后的话</h2>

<p>没有"最好"的架构——只有<strong>最适合</strong>你场景的架构。根据任务复杂度、对控制力的需求以及长期目标来选择。</p>

<h2>常见问题</h2>

<h3>新手应该从哪个架构开始？</h3>
<p>从<strong>单 Agent</strong>开始理解基本循环（输入→思考→工具→输出）。熟练后过渡到<strong>ReAct</strong>体验多步骤推理。大多数新手在个人项目上永远不需要超越 ReAct + Plan & Execute。跳到多 Agent 和 Graph/Workflow 是工程决策，不是学习里程碑——只有当单个 Agent 无法处理任务复杂度或需要生产级可靠性和可追溯性时才需要。</p>

<h3>为什么 Router + Skill 是当前编码工具的最佳实践？</h3>
<p>因为它解决了 Agent 编码最大的问题：<strong>不可预测性</strong>。在 ReAct 或 Plan & Execute 架构中，模型在每一步决定做什么——这意味着它可能做出有创意但错误的决定。Router + Skill 翻转了这一点：模型不再思考"我怎么解决这个问题？"，而是思考"哪个预置 Skill 能解决这个问题？"每个 Skill 是经过测试的确定性工作流。模型的角色变成了分类（匹配意图到 Skill），而非生成（临时发明方案）。对于正确性比创意更重要的生产级编码工具，这大大提高了可靠性。</p>

<h3>多 Agent 和 Graph/Workflow 架构有什么区别？</h3>
<p>多 Agent 关注<strong>谁</strong>来做——多个专业化 Agent 协作。Graph/Workflow 关注<strong>怎么做</strong>——任务以 DAG 形式编排，支持条件分支、并行执行和重试逻辑。它们不互斥：你可以有一个 Graph/Workflow 来编排多个 Agent。把多 Agent 理解为团队结构，Graph/Workflow 理解为项目管理方法论。企业系统通常两者都用：Graph/Workflow 管整体流程，专业化 Agent 处理图中各个节点。</p>

<h3>什么时候不该用 Agent 架构？</h3>
<p>当一个简单的 API 调用或脚本就能搞定的时候。Agent 架构会增加延迟、成本和复杂度。如果你的任务是确定性的（如"把这张图片缩放到 800px"或"把这段文字翻译成法语"），直接函数调用更快、更便宜、更可靠。Agent 的甜蜜点是带模糊性的任务："审查这个 PR 并建议改进"或"研究这个主题并写一份摘要"。一个实用判断标准：如果你能把逻辑画成流程图上没有任何"看情况"分支，那你大概率不需要 Agent。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>理解了架构？看看它们在实际中如何运作：</p>
  <ul>
    <li><a href="/articles/complete-practical-tutorial-claude-code-core-operations">Claude Code 完全实战教程：掌握所有核心操作</a> — 在真实工具中看 Plan & Execute 和多 Agent 架构</li>
    <li><a href="/articles/2026-ai-agent-guide-choose-right-tool-beginners">2026 AI Agent 选型指南：新手如何选择最适合的工具</a> — 将架构匹配到具体工具</li>
    <li><a href="/articles/demystifying-ai-application-layer-3-layers">拆解 AI 应用层：从大语言模型到智能体的三层体系</a> — 理解 Agent 在更广泛 AI 技术栈中的位置</li>
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