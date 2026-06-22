"""
Publish June 22, 2026 articles.
0 new tools needed — all referenced tools (codex-agent, claude, cursor, github-copilot) already exist.
"""

import os

BASE = r"C:\Users\jun\aistudyonline-next"
os.chdir(BASE)

# ===== Part 1: Add 2 article metadata to articles.ts =====
with open('src/lib/articles.ts', 'r', encoding='utf-8') as f:
    articles_src = f.read()

new_articles = r"""  {
    slug: "codex-superpowers-transform-coding",
    title: "Codex Superpowers: Transform Your AI Coding from Random to Engineering-Grade",
    titleZh: "Codex超能力：将AI编码从随机输出升级为工程级别",
    description: "A 210k-star open-source tool transforms Codex (and Claude Code, Gemini CLI, Cursor, Copilot) from a code-slinging machine into a disciplined software engineer with requirements gathering, TDD, and sub-agent driven development.",
    descriptionZh: "一个21万Star的开源工具将Codex（及Claude Code、Gemini CLI、Cursor、Copilot）从代码机器转变为遵循需求澄清→实现规划→TDD→子代理开发的 disciplined 软件工程师。",
    category: "ai-tutorials",
    tags: ["codex", "tdd", "sub-agents", "requirements", "code-review", "engineering"],
    difficulty: "intermediate",
    toolsMentioned: ["codex-agent", "claude", "cursor", "github-copilot"],
    date: "2026-06-22",
  },
  {
    slug: "upgrade-obsidian-ai-dashboard",
    title: "Upgrade Your Obsidian Homepage: Build AI-Powered Smart Dashboard for Knowledge Workflow",
    titleZh: "升级Obsidian首页：构建AI驱动智能仪表盘赋能知识工作流",
    description: "Replace your static DataviewJS Obsidian homepage with an AI-powered dashboard that connects Claude Code, Codex, RSS feeds, and GitHub — with one-click deep research, auto-tagging, and vault health inspection.",
    descriptionZh: "用AI驱动的仪表盘取代静态DataviewJS Obsidian首页，连接Claude Code、Codex、RSS源和GitHub——实现一键深度研究、自动标签和知识库健康检查。",
    category: "ai-tutorials",
    tags: ["obsidian", "dashboard", "claude-code", "codex", "plugin", "knowledge-base"],
    difficulty: "advanced",
    toolsMentioned: ["claude", "codex-agent"],
    date: "2026-06-22",
  },

"""

last_bracket = articles_src.rfind('];')
articles_new = articles_src[:last_bracket] + new_articles + '];'

with open('src/lib/articles.ts', 'w', encoding='utf-8') as f:
    f.write(articles_new)

print('Part 1: 2 new articles added to articles.ts')

# ===== Part 2: Add 2 article contents to article-content.ts =====
with open('src/lib/article-content.ts', 'r', encoding='utf-8') as f:
    content_src = f.read()

new_contents = r'''
  "codex-superpowers-transform-coding": {
    en: `<div class="meta-banner">
<p><strong>📅 Published:</strong> June 22, 2026 · <strong>🏷️ Category:</strong> AI Tutorials · <strong>📊 Level:</strong> Intermediate · <strong>🛠️ Tools:</strong> Codex, Claude Code, Cursor, GitHub Copilot</p>
</div>

<p>In the world of AI-powered coding, Codex has been a game-changer, but it often suffers from a critical flaw—writing code without clear context or structure. Enter a <strong>210k+ Star open-source tool</strong> that revolutionizes how Codex (and other AI coding agents like Claude Code, Gemini CLI, Cursor, and Copilot) works. This tool turns your AI from a code-slinging machine into a disciplined software engineer, complete with requirements gathering, testing, and project management.</p>

<h2>From Random Coding to Structured Engineering</h2>

<p>Traditional AI coding tools like Codex often jump straight into writing code, leading to mismatched requirements and buggy outputs. This open-source solution flips the script with four phases:</p>

<ol>
<li><strong>Requirement Clarification:</strong> Forces a brainstorming session to turn vague ideas into clear, actionable requirements.</li>
<li><strong>Implementation Planning:</strong> Breaks down the design into small, reviewable chunks, ensuring you understand each step.</li>
<li><strong>Test-Driven Development (TDD):</strong> Follows a red-green-refactor cycle—writing failing tests first, then implementing code, and finally refactoring.</li>
<li><strong>Sub-Agent Driven Development:</strong> Deploys a team of sub-agents to handle tasks like testing, implementation, and code review in parallel.</li>
</ol>

<h2>Step 1: Install the Tool</h2>

<p>This tool is MIT-licensed and free. Install it with a single command:</p>

<pre><code class="language-bash"># Example installation command
npm install -g [tool-name]
# or
pip install [tool-name]</code></pre>

<h2>Step 2: Initialize a Project with Requirement Gathering</h2>

<p>Start by prompting the AI to build something. Instead of coding, it will first ask clarifying questions. For example, if you want a to-do list app:</p>

<pre><code class="language-text">User: Build a to-do list app with storage and task management.
AI: Let's clarify:
- What storage backend? (Local storage, API, database)
- Do you need user authentication?
- What task operations? (Add, delete, mark as done, etc.)
- Any UI preferences? (CLI, web, desktop)</code></pre>

<h2>Step 3: Approve the Implementation Plan</h2>

<p>Once requirements are clear, the AI generates a step-by-step plan:</p>

<pre><code class="language-text">Implementation Plan:
1. Create storage.ts to handle local storage operations.
2. Write tests for addTodo in addTodo.test.ts.
3. Implement addTodo in todo.ts.
4. Build UI component TodoList.vue.</code></pre>

<p>Review and approve each step before proceeding.</p>

<h2>Step 4: Let Sub-Agents Do the Work</h2>

<p>The tool deploys sub-agents for each task:</p>

<ul>
<li><strong>Testing Agent:</strong> Writes failing tests first (red phase).</li>
<li><strong>Implementation Agent:</strong> Writes code to make tests pass (green phase).</li>
<li><strong>Review Agent:</strong> Checks code quality and suggests refactors.</li>
</ul>

<p>Sample test from <code>addTodo.test.ts</code>:</p>

<pre><code class="language-typescript">import { addTodo } from './todo';

test('addTodo adds a task to the list', () => {
  const initialTodos = [];
  const newTodo = { id: 1, text: 'Learn AI Engineering', done: false };
  expect(addTodo(initialTodos, newTodo)).toContain(newTodo);
});</code></pre>

<p>Corresponding implementation in <code>todo.ts</code>:</p>

<pre><code class="language-typescript">export interface Todo {
  id: number;
  text: string;
  done: boolean;
}

export function addTodo(todos: Todo[], newTodo: Todo): Todo[] {
  return [...todos, newTodo];
}</code></pre>

<h2>Step 5: Refactor and Submit</h2>

<p>After tests pass, the refactoring agent optimizes the code. Finally, the tool handles version control:</p>

<pre><code class="language-bash">git add .
git commit -m "Implement addTodo with tests"
git push</code></pre>

<h2>Why This Works Across Multiple AI Coding Agents</h2>

<p>This tool isn't limited to Codex. It works with <strong>Claude Code, Gemini CLI, Cursor, Copilot,</strong> and more. The secret is a standardized interface that adapts to different AI agents, so you get consistent engineering practices regardless of the tool.</p>

<h2>常见问题</h2>

<h3>Is this tool a replacement for Codex or Claude Code?</h3>
<p>No. It's a workflow layer on top of existing AI coding agents. Think of it as a project manager that sits between you and the AI, enforcing structured development practices. You still use Codex or Claude Code for the actual code generation — this tool ensures the output is engineering-grade rather than ad-hoc.</p>

<h3>Do I need to know TDD to use this tool?</h3>
<p>The tool guides you through TDD automatically, so prior TDD knowledge helps but isn't required. The sub-agents handle test writing, implementation, and refactoring in sequence. Over time, you'll naturally absorb TDD principles by watching the workflow.</p>

<h3>Can I use this with my existing projects?</h3>
<p>Yes. The tool works with both new and existing codebases. For existing projects, it can generate tests for uncovered code and suggest refactors based on the established patterns in your codebase.</p>

<div class="next-step">
<p><strong>下一篇：</strong> <a href="/en/article/upgrade-obsidian-ai-dashboard">Upgrade Your Obsidian Homepage: Build AI-Powered Smart Dashboard →</a></p>
</div>`,
    zh: `<div class="meta-banner">
<p><strong>📅 发布日期：</strong>2026年6月22日 · <strong>🏷️ 分类：</strong>AI教程 · <strong>📊 难度：</strong>中级 · <strong>🛠️ 工具：</strong>Codex、Claude Code、Cursor、GitHub Copilot</p>
</div>

<p>在AI编码领域，Codex改变了游戏规则，但它常有一个关键缺陷——在没有清晰上下文或结构的情况下直接写代码。现在有一个<strong>21万Star的开源工具</strong>彻底改变了Codex（以及Claude Code、Gemini CLI、Cursor、Copilot等AI编码代理）的工作方式。这个工具将你的AI从随意写代码的机器转变为遵循规范的软件工程师，具备需求收集、测试和项目管理能力。</p>

<h2>从随机编码到结构化工程</h2>

<p>传统AI编码工具如Codex经常直接跳入写代码，导致需求不匹配和Bug频出。这个开源方案用四个阶段翻转了局面：</p>

<ol>
<li><strong>需求澄清：</strong>强制进行头脑风暴，将模糊想法转化为清晰可操作的需求。</li>
<li><strong>实现规划：</strong>将设计分解为小而可审查的块，确保你理解每一步。</li>
<li><strong>测试驱动开发（TDD）：</strong>遵循红-绿-重构循环——先写失败测试，再实现代码，最后重构。</li>
<li><strong>子代理驱动开发：</strong>部署子代理团队并行处理测试、实现和代码审查。</li>
</ol>

<h2>步骤1：安装工具</h2>

<p>该工具MIT开源免费，一条命令安装：</p>

<pre><code class="language-bash"># 安装命令示例
npm install -g [tool-name]
# 或
pip install [tool-name]</code></pre>

<h2>步骤2：通过需求收集初始化项目</h2>

<p>提示AI构建东西时，它不会直接写代码，而是先提问澄清。比如做一个待办清单应用：</p>

<pre><code class="language-text">用户：构建一个带存储和任务管理的待办清单应用。
AI：让我们澄清：
- 用什么存储后端？（本地存储、API、数据库）
- 需要用户认证吗？
- 支持哪些任务操作？（添加、删除、标记完成等）
- UI偏好？（CLI、Web、桌面）</code></pre>

<h2>步骤3：审批实现计划</h2>

<p>需求明确后，AI生成逐步计划：</p>

<pre><code class="language-text">实现计划：
1. 创建 storage.ts 处理本地存储操作。
2. 在 addTodo.test.ts 中为 addTodo 编写测试。
3. 在 todo.ts 中实现 addTodo。
4. 构建 UI 组件 TodoList.vue。</code></pre>

<p>在继续前审查并批准每一步。</p>

<h2>步骤4：让子代理干活</h2>

<p>该工具为每个任务部署子代理：</p>

<ul>
<li><strong>测试代理：</strong>先写失败测试（红阶段）。</li>
<li><strong>实现代理：</strong>写代码让测试通过（绿阶段）。</li>
<li><strong>审查代理：</strong>检查代码质量并建议重构。</li>
</ul>

<p><code>addTodo.test.ts</code> 示例测试：</p>

<pre><code class="language-typescript">import { addTodo } from './todo';

test('addTodo 向列表添加任务', () => {
  const initialTodos = [];
  const newTodo = { id: 1, text: '学习AI工程', done: false };
  expect(addTodo(initialTodos, newTodo)).toContain(newTodo);
});</code></pre>

<p><code>todo.ts</code> 对应实现：</p>

<pre><code class="language-typescript">export interface Todo {
  id: number;
  text: string;
  done: boolean;
}

export function addTodo(todos: Todo[], newTodo: Todo): Todo[] {
  return [...todos, newTodo];
}</code></pre>

<h2>步骤5：重构并提交</h2>

<p>测试通过后，重构代理优化代码。最后工具处理版本控制：</p>

<pre><code class="language-bash">git add .
git commit -m "实现 addTodo 及测试"
git push</code></pre>

<h2>为什么跨多个AI编码代理都能用</h2>

<p>这个工具不仅限于Codex。它支持<strong>Claude Code、Gemini CLI、Cursor、Copilot</strong>等。秘诀是标准化接口适配不同AI代理，让你无论用什么工具都获得一致的工程实践。</p>

<h2>常见问题</h2>

<h3>这个工具是Codex或Claude Code的替代品吗？</h3>
<p>不是。它是现有AI编码代理之上的工作流层。把它想象成坐在你和AI之间的项目经理，强制执行结构化开发实践。你仍然使用Codex或Claude Code进行实际代码生成——这个工具确保输出是工程级别而非临时拼凑。</p>

<h3>需要用TDD才能使用这个工具吗？</h3>
<p>工具会自动引导你完成TDD，所以有TDD知识有帮助但不是必须的。子代理按顺序处理测试编写、实现和重构。随着时间推移，你会通过观察工作流自然吸收TDD原则。</p>

<h3>能在现有项目中使用吗？</h3>
<p>可以。该工具同时适用于新项目和现有代码库。对于现有项目，它可以为未覆盖的代码生成测试，并基于代码库中已建立的模式建议重构。</p>

<div class="next-step">
<p><strong>下一篇：</strong> <a href="/zh/article/upgrade-obsidian-ai-dashboard">升级Obsidian首页：构建AI驱动智能仪表盘 →</a></p>
</div>`,
  },

  "upgrade-obsidian-ai-dashboard": {
    en: `<div class="meta-banner">
<p><strong>📅 Published:</strong> June 22, 2026 · <strong>🏷️ Category:</strong> AI Tutorials · <strong>📊 Level:</strong> Advanced · <strong>🛠️ Tools:</strong> Claude Code, Codex, Obsidian</p>
</div>

<p>For long-term Obsidian users, most custom home dashboards rely on basic Markdown combined with DataviewJS plugins. These simple layouts can display recent notes, daily task lists, reading heatmaps and file catalogs, but they lack compatibility with modern AI coding tools like Claude Code, Codex, custom Skills, RSS data feeds and GitHub open-source synchronization. This tutorial shares a complete hands-on workflow to rebuild your Obsidian homepage into an automated AI hub that connects your knowledge base with all mainstream LLM coding agents.</p>

<h2>Limitations of Traditional Dataview Homepage Solutions</h2>

<p>The classic DataviewJS homepage only focuses on local vault data queries and static page rendering, with obvious drawbacks in current AI work scenarios:</p>

<ol>
<li>Cannot trigger one-click AI script execution inside the vault</li>
<li>No native integration channels to call Claude Code / Codex coding agents</li>
<li>Unable to load external dynamic data such as GitHub updates and RSS news</li>
<li>Cannot auto-generate structured notes via LLM based on inbox raw materials</li>
<li>Lacks one-click vault health inspection and knowledge sorting automation</li>
</ol>

<p>The upgraded AI dashboard fixes all these pain points while retaining your original note query modules.</p>

<h2>Step 1: Set Up Obsidian Custom Plugin Development Environment</h2>

<p>Build a lightweight custom dashboard plugin to support AI agent docking, running independently without conflicting with existing community plugins:</p>

<pre><code class="language-bash"># Create project directory
mkdir obsidian-ai-dashboard
cd obsidian-ai-dashboard
# Initialize npm environment
npm init -y
# Install official Obsidian API dependency
npm install @obsidianmd/obsidian-api typescript
# Add build script dependency
npm install --save-dev esbuild</code></pre>

<p>Create core entry file <code>main.ts</code>:</p>

<pre><code class="language-typescript">import { Plugin } from "obsidian";

export default class AIDashboardPlugin extends Plugin {
  async onload() {
    // Register homepage dashboard view
    this.registerView("ai-dashboard-view", (leaf) => {
      return new AIDashboardView(leaf, this);
    });
    // Add sidebar button to open dashboard
    this.addRibbonIcon("dashboard", "Open AI Dashboard", () => {
      this.activateView();
    });
  }

  async activateView() {
    const { workspace } = this.app;
    let leaf = workspace.getLeaf(false);
    await leaf.setViewState({ type: "ai-dashboard-view", active: true });
  }
}</code></pre>

<p>Add build configuration in <code>package.json</code>:</p>

<pre><code class="language-json">"scripts": {
  "dev": "esbuild main.ts --outfile=main.js --target=es2020 --watch",
  "build": "esbuild main.ts --outfile=main.js --target=es2020 --minify"
}</code></pre>

<p>Run compilation and copy files to your vault's <code>.obsidian/plugins/obsidian-ai-dashboard/</code> folder, then enable the plugin in Obsidian settings.</p>

<h2>Step 2: Build Integrated Frontend Panel with Frontend-Design Skill</h2>

<p>Instead of bulky UI frameworks, call the official <code>frontend-design</code> Skill from Claude Code to generate lightweight dashboard HTML components. Send this prompt:</p>

<pre><code class="language-text">Create an Obsidian dashboard UI with 4 core sections:
1. Original Dataview module: Recent files, pending tasks, monthly note heatmap
2. AI Agent operation area: Buttons for deep research, code generation, vault sorting
3. External data panel: RSS feed list, GitHub repository update log
4. Inbox processing module: Auto summarize raw markdown via LLM
Use plain HTML + inline CSS, compatible with Obsidian internal view.</code></pre>

<h2>Step 3: Realize One-Click AI Agent Calling</h2>

<p>Add click triggers on dashboard buttons to send tasks to Claude Code or Codex via local API:</p>

<pre><code class="language-typescript">// Trigger deep research task
document.getElementById("btn-deep-research").addEventListener("click", async () => {
  const vaultPath = this.app.vault.getRoot().path;
  const prompt = \`Run deep research on all unprocessed inbox files under \${vaultPath}/Inbox, organize structured knowledge notes and save to /Research folder\`;

  const res = await fetch("http://127.0.0.1:8080/claude-code/run", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ task: prompt })
  });
  const result = await res.json();
  new Notice(\`Deep Research finished: \${result.fileCount} notes generated\`);
});</code></pre>

<p>Start the local Claude Code background service:</p>

<pre><code class="language-bash">claude-code serve --port 8080</code></pre>

<h2>Step 4: Embed Dynamic External Data Modules</h2>

<h3>RSS Real-Time Feed</h3>

<p>Add DataviewJS code block to pull subscription news:</p>

<pre><code class="language-javascript">const RSS = require("rss-parser");
const parser = new RSS();
const feedUrl = "https://example-tech-blog.com/feed.xml";
const feed = await parser.parseURL(feedUrl);
let list = "";
feed.items.slice(0,10).forEach(item => {
  list += \`- [\${item.title}](\${item.link}) | \${item.pubDate}\\n\`
})
dv.header(3, "Latest Tech RSS");
dv.markdown(list);</code></pre>

<h3>GitHub Repository Sync Log</h3>

<p>Call GitHub open API to display commit updates:</p>

<pre><code class="language-bash"># Terminal test request for GitHub latest commits
curl https://api.github.com/repos/your-name/your-project/commits?per_page=5</code></pre>

<p>Wrap the request in the dashboard plugin to auto-refresh commit logs every hour.</p>

<h2>Step 5: Auto Vault Maintenance & Knowledge Sorting</h2>

<p>Add a vault inspection button to execute batch sorting scripts through Codex:</p>

<pre><code class="language-text">Scan the entire Obsidian vault:
1. Mark orphan files without internal links
2. Tag untagged notes by content topic via LLM
3. Merge duplicate concept notes
4. Generate vault structure overview report and save as Vault-Overview.md</code></pre>

<h2>Final Optimization Tips</h2>

<ol>
<li>Retain your original Dataview query code to avoid abandoning existing note statistics</li>
<li>Limit concurrent AI task quantity to prevent local port service overload</li>
<li>Add switch toggles in plugin settings to turn off RSS/GitHub data modules when not needed</li>
<li>Bind hotkeys for core dashboard functions via Obsidian hotkey settings panel</li>
</ol>

<h2>常见问题</h2>

<h3>Will this plugin conflict with my existing Obsidian plugins?</h3>
<p>No. The AI Dashboard plugin is a standalone custom plugin that runs independently. It doesn't modify or interfere with Dataview, Templater, or any other community plugins. You can keep all your existing plugins and simply add this one as a new dashboard layer.</p>

<h3>Do I need to keep Claude Code running in the background?</h3>
<p>Only when you want to trigger AI tasks from the dashboard. The <code>claude-code serve</code> command runs a lightweight HTTP server on port 8080 that listens for dashboard requests. When not in use, you can stop it to free resources. The dashboard itself works fine without it — you just won't have one-click AI execution until the service is running.</p>

<h3>Can I customize which AI agent handles which task?</h3>
<p>Yes. The button handlers in Step 3 are fully customizable. You can route different tasks to different agents — for example, send code generation to Codex, deep research to Claude Code, and vault organization to a local LLM. Just modify the fetch URL and payload for each button.</p>

<div class="next-step">
<p><strong>Previous:</strong> <a href="/en/article/codex-superpowers-transform-coding">Codex Superpowers: Transform Your AI Coding from Random to Engineering-Grade ←</a></p>
</div>`,
    zh: `<div class="meta-banner">
<p><strong>📅 发布日期：</strong>2026年6月22日 · <strong>🏷️ 分类：</strong>AI教程 · <strong>📊 难度：</strong>高级 · <strong>🛠️ 工具：</strong>Claude Code、Codex、Obsidian</p>
</div>

<p>对于长期Obsidian用户来说，大多数自定义首页仪表盘依赖基础Markdown配合DataviewJS插件。这些简单布局能显示最近笔记、每日任务清单、阅读热力图和文件目录，但缺乏与现代AI编码工具（如Claude Code、Codex、自定义Skills、RSS数据源和GitHub开源同步）的兼容性。本教程分享完整实操工作流，将你的Obsidian首页重建为自动化AI中心，连接你的知识库与所有主流LLM编码代理。</p>

<h2>传统Dataview首页方案的局限性</h2>

<p>经典DataviewJS首页只关注本地仓库数据查询和静态页面渲染，在当前AI工作场景中有明显不足：</p>

<ol>
<li>无法在仓库内触发一键AI脚本执行</li>
<li>没有原生集成通道调用Claude Code / Codex编码代理</li>
<li>无法加载外部动态数据，如GitHub更新和RSS新闻</li>
<li>无法基于收件箱原始材料通过LLM自动生成结构化笔记</li>
<li>缺少一键仓库健康检查和知识整理自动化</li>
</ol>

<p>升级后的AI仪表盘解决了所有这些痛点，同时保留你原有的笔记查询模块。</p>

<h2>步骤1：搭建Obsidian自定义插件开发环境</h2>

<p>构建轻量级自定义仪表盘插件，支持AI代理对接，独立运行不与现有社区插件冲突：</p>

<pre><code class="language-bash"># 创建项目目录
mkdir obsidian-ai-dashboard
cd obsidian-ai-dashboard
# 初始化npm环境
npm init -y
# 安装官方Obsidian API依赖
npm install @obsidianmd/obsidian-api typescript
# 添加构建脚本依赖
npm install --save-dev esbuild</code></pre>

<p>创建核心入口文件 <code>main.ts</code>：</p>

<pre><code class="language-typescript">import { Plugin } from "obsidian";

export default class AIDashboardPlugin extends Plugin {
  async onload() {
    // 注册首页仪表盘视图
    this.registerView("ai-dashboard-view", (leaf) => {
      return new AIDashboardView(leaf, this);
    });
    // 添加侧边栏按钮打开仪表盘
    this.addRibbonIcon("dashboard", "打开AI仪表盘", () => {
      this.activateView();
    });
  }

  async activateView() {
    const { workspace } = this.app;
    let leaf = workspace.getLeaf(false);
    await leaf.setViewState({ type: "ai-dashboard-view", active: true });
  }
}</code></pre>

<p>在 <code>package.json</code> 中添加构建配置：</p>

<pre><code class="language-json">"scripts": {
  "dev": "esbuild main.ts --outfile=main.js --target=es2020 --watch",
  "build": "esbuild main.ts --outfile=main.js --target=es2020 --minify"
}</code></pre>

<p>运行编译命令，将生成的文件复制到仓库的 <code>.obsidian/plugins/obsidian-ai-dashboard/</code> 文件夹，然后在Obsidian设置中启用插件。</p>

<h2>步骤2：用Frontend-Design Skill构建集成前端面板</h2>

<p>无需笨重的UI框架，调用Claude Code官方的 <code>frontend-design</code> Skill生成轻量级仪表盘HTML组件。发送此提示：</p>

<pre><code class="language-text">创建一个Obsidian仪表盘UI，包含4个核心区域：
1. 原始Dataview模块：最近文件、待处理任务、月度笔记热力图
2. AI代理操作区：深度研究、代码生成、仓库整理的按钮
3. 外部数据面板：RSS源列表、GitHub仓库更新日志
4. 收件箱处理模块：通过LLM自动摘要原始markdown
使用纯HTML+内联CSS，兼容Obsidian内部视图。</code></pre>

<h2>步骤3：实现一键AI代理调用功能</h2>

<p>在仪表盘按钮上添加点击触发器，通过本地API将任务发送给Claude Code或Codex：</p>

<pre><code class="language-typescript">// 触发深度研究任务
document.getElementById("btn-deep-research").addEventListener("click", async () => {
  const vaultPath = this.app.vault.getRoot().path;
  const prompt = \`对 \${vaultPath}/Inbox 下所有未处理的收件箱文件进行深度研究，整理结构化知识笔记并保存到 /Research 文件夹\`;

  const res = await fetch("http://127.0.0.1:8080/claude-code/run", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ task: prompt })
  });
  const result = await res.json();
  new Notice(\`深度研究完成：已生成 \${result.fileCount} 条笔记\`);
});</code></pre>

<p>先启动本地Claude Code后台服务：</p>

<pre><code class="language-bash">claude-code serve --port 8080</code></pre>

<h2>步骤4：嵌入动态外部数据模块</h2>

<h3>RSS实时订阅</h3>

<p>在仪表盘Markdown容器中添加DataviewJS代码块拉取订阅新闻：</p>

<pre><code class="language-javascript">const RSS = require("rss-parser");
const parser = new RSS();
const feedUrl = "https://example-tech-blog.com/feed.xml";
const feed = await parser.parseURL(feedUrl);
let list = "";
feed.items.slice(0,10).forEach(item => {
  list += \`- [\${item.title}](\${item.link}) | \${item.pubDate}\\n\`
})
dv.header(3, "最新科技RSS");
dv.markdown(list);</code></pre>

<h3>GitHub仓库同步日志</h3>

<p>调用GitHub开放API在首页显示代码仓库提交更新：</p>

<pre><code class="language-bash"># 终端测试请求GitHub最新提交
curl https://api.github.com/repos/your-name/your-project/commits?per_page=5</code></pre>

<p>将请求包装在仪表盘插件中，每小时自动刷新提交日志。</p>

<h2>步骤5：自动仓库维护与知识整理</h2>

<p>添加仓库检查按钮，通过Codex执行批量整理脚本：</p>

<pre><code class="language-text">扫描整个Obsidian仓库：
1. 标记没有内部链接的孤立文件
2. 通过LLM按内容主题为未标记笔记打标签
3. 合并重复概念笔记
4. 生成仓库结构概览报告并保存为 Vault-Overview.md</code></pre>

<h2>最终优化建议</h2>

<ol>
<li>保留原始Dataview查询代码，避免丢弃现有笔记统计</li>
<li>限制并发AI任务数量，防止本地端口服务过载</li>
<li>在插件设置中添加开关，不需要时关闭RSS/GitHub数据模块</li>
<li>通过Obsidian快捷键设置面板为核心仪表盘功能绑定热键</li>
</ol>

<h2>常见问题</h2>

<h3>这个插件会与我现有的Obsidian插件冲突吗？</h3>
<p>不会。AI仪表盘插件是独立的自定义插件，独立运行。它不会修改或干扰Dataview、Templater或任何其他社区插件。你可以保留所有现有插件，只需将此插件添加为新的仪表盘层。</p>

<h3>需要让Claude Code一直在后台运行吗？</h3>
<p>只有想从仪表盘触发AI任务时才需要。<code>claude-code serve</code> 命令在8080端口运行轻量级HTTP服务器，监听仪表盘请求。不使用时可以停止以释放资源。仪表盘本身在没有服务的情况下正常工作——只是在服务运行前无法使用一键AI执行功能。</p>

<h3>能自定义哪个AI代理处理哪个任务吗？</h3>
<p>可以。步骤3中的按钮处理器完全可定制。你可以将不同任务路由到不同代理——例如将代码生成发给Codex，深度研究发给Claude Code，仓库整理发给本地LLM。只需修改每个按钮的fetch URL和负载即可。</p>

<div class="next-step">
<p><strong>上一篇：</strong> <a href="/zh/article/codex-superpowers-transform-coding">Codex超能力：将AI编码从随机输出升级为工程级别 ←</a></p>
</div>`,
  },

'''

last_brace = content_src.rfind('};')
content_new = content_src[:last_brace] + new_contents + '};'

with open('src/lib/article-content.ts', 'w', encoding='utf-8') as f:
    f.write(content_new)

print('Part 2: 2 article contents added to article-content.ts')

print('\n=== All done! Run build to verify ===')
