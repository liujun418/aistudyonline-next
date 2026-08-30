# -*- coding: utf-8 -*-
"""Aug 30, 2026 publish: Agent Harness: Three Engineering Forms for Your AI Workflow"""
import io, os, sys

BASE = r"C:\Users\jun\aistudyonline-next"
os.chdir(BASE)

# ---------- 1. articles.ts ----------
f = r"src\lib\articles.ts"
s = io.open(f, encoding="utf-8").read()

a = r"""  {
    slug: "agent-harness-three-engineering-forms-comparison",
    title: "Agent Harness: Three Engineering Forms for Your AI Workflow (DeepSeek Harness, OpenCode, Pi)",
    titleZh: "Agent Harness：AI工作流的三大工程形态（DeepSeek Harness、OpenCode、Pi）",
    description: "An Agent Harness is the work environment for your AI model, and there is no universal best — only the right fit. This decision guide compares the three leading engineering forms: DeepSeek Harness (full runtime control, everything is a plugin), OpenCode (ready-to-use with extensibility), and Pi (a minimal 4-tool kernel under 1,000 tokens for ~3x context reduction and 50%+ cost savings) — covering core design, key features, install commands, and a concrete how-to-choose framework for your AI workflow.",
    descriptionZh: "Agent Harness是AI模型的工作环境，没有万能最优，只有最适合。本决策指南对比三大主流工程形态：DeepSeek Harness（完全掌控运行时、万物皆插件）、OpenCode（开箱即用且可扩展）、Pi（仅4个工具的极简内核，1000 token以内，约3倍上下文缩减、50%以上成本下降）——涵盖核心设计、关键特性、安装命令与一套可直接套用的选择框架。",
    category: "ai-comparisons",
    tags: ["AI Agent", "Agent Harness", "DeepSeek Harness", "OpenCode", "Pi", "Context Efficiency", "Coding"],
    difficulty: "intermediate",
    toolsMentioned: ["deepseek-harness", "opencode", "pi"],
    date: "2026-08-30",
  },
  """
pos = s.rfind("];")
assert pos > 0
s2 = s[:pos] + a + s[pos:]
io.open(f, "w", encoding="utf-8", newline="\n").write(s2)
print("articles.ts entries:", s2.count('slug: "'))

# ---------- 2. article-content.ts ----------
f = r"src\lib\article-content.ts"
s = io.open(f, encoding="utf-8").read()

content = r"""  "agent-harness-three-engineering-forms-comparison": {
    content: `<div class="meta-banner">
  <span class="meta-badge">⚖️ AI Comparisons</span>
  <span class="meta-badge">🕒 8 min read</span>
  <span class="meta-badge">📅 Aug 30, 2026</span>
  <span class="meta-badge">🎯 Intermediate</span>
</div>

<h2 id="introduction">Introduction</h2>

<p>When choosing an Agent Harness, there is no universal "best" option — only the one that best fits your needs. This guide breaks down three leading Agent Harness solutions: <strong>DeepSeek Harness</strong>, <strong>OpenCode</strong>, and <strong>Pi</strong>. We will explain each one's core design philosophy, key features, real-world use cases, and installation commands, then close with a concrete framework for picking the right harness for your AI workflow.</p>

<h2 id="what-is-agent-harness">What is an Agent Harness?</h2>

<p>Think of an Agent Harness as the "work environment" for your AI model. It decides what the model sees and what the model can do. Concretely, a harness:</p>
<ul>
  <li><strong>Selects content</strong> — decides which files and context get sent to the model.</li>
  <li><strong>Provides tools</strong> — gives the model read, write, search, and execution capabilities.</li>
  <li><strong>Executes tool calls</strong> — runs the model's chosen actions and returns the results.</li>
  <li><strong>Manages the Agent Loop</strong> — the cycle of model reasoning → tool use → result feedback that repeats until the task is done.</li>
</ul>
<p>A well-designed harness turns messy work into structured work. For example, when debugging a login bug, it organizes the relevant files, provides search/edit/test tools, and filters out useless output so the model can reason over exactly what matters.</p>

<h2 id="three-engineering-forms">Three Core Engineering Forms</h2>

<p>All three harnesses share the same goal — creating a structured work environment for AI agents. Their key difference lies in <strong>how much of the environment is pre-configured</strong> and <strong>how much control the user has</strong>. That single axis is what separates the three engineering forms.</p>

<h3>1. DeepSeek Harness (DSH): Full Control Over the Runtime</h3>
<p><strong>Core Philosophy</strong>: <em>Everything is a Plugin</em>.</p>
<p>DeepSeek Harness is built on the <strong>Cordis</strong> plugin system, where every component — tools, model adapters, file access, even the Agent Loop itself — is a replaceable plugin. This gives developers complete control over the agent's runtime behavior.</p>
<ul>
  <li><strong>Modular Design</strong>: swap or extend any capability (models, tools, sessions, sandboxes, storage, loops, scheduling, UI) without changing source code.</li>
  <li><strong>Composable Runtime</strong>: reconfigure the entire workflow pipeline — for example, change tool execution order or add custom context compression.</li>
  <li><strong>Append-Only State Management</strong>: track session history as a sequence of events for easy recovery and audit.</li>
  <li><strong>Multiple Runtime Modes</strong>: <strong>Standard Mode</strong> (full toolset for general tasks), <strong>Code Mode</strong> (model-generated code orchestration), <strong>Minimal Mode</strong> (shell + file editor for benchmarking), and <strong>Creator Mode</strong> (test plugins in memory and build new agent modes).</li>
</ul>
<p><strong>Use cases</strong>: DeepSeek Harness is ideal for developers who need to <strong>build or modify agent systems at the runtime level</strong>. If you want to create custom agents, redefine workflows, or integrate with complex enterprise systems, DSH is the most flexible choice.</p>
<pre><code class="language-bash"># Quick start with Web UI
npx @deepseek-ai/dsh web

# Install from source
git clone https://github.com/deepseek-ai/deepseek-harness
cd deepseek-harness
pnpm install
pnpm run build
pnpm dsh web</code></pre>

<h3>2. OpenCode: Ready-to-Use Product with Extensibility</h3>
<p><strong>Core Philosophy</strong>: <em>Pre-configured, but customizable</em>.</p>
<p>OpenCode is a fully featured, open-source AI coding agent that ships with a complete set of tools out of the box. It is designed for developers who want to <strong>start coding immediately</strong> without setting up a runtime environment.</p>
<ul>
  <li><strong>Out-of-the-Box Capabilities</strong>: terminal interface, desktop app, multi-model support, session persistence, LSP/MCP integration, and permission control.</li>
  <li><strong>TypeScript Plugin System</strong>: extend functionality by adding tools, model providers, or intercepting tool calls.</li>
  <li><strong>GitHub Integration</strong>: use <code>/opencode</code> or <code>/oc</code> in GitHub issues and PRs to execute tasks directly in your repository.</li>
  <li><strong>Multi-Editor Support</strong>: works with VS Code, JetBrains, Neovim, Zed, and Emacs.</li>
</ul>
<p><strong>Use cases</strong>: OpenCode is perfect for <strong>everyday coding tasks</strong> — debugging, refactoring, or feature development. If you want a reliable, production-ready agent that fits your existing workflow, OpenCode is the best choice.</p>
<pre><code class="language-bash"># One-click install (Linux/macOS)
curl -fsSL https://opencode.ai/install | bash

# Install from source
git clone https://github.com/opencode-ai/opencode
cd opencode
go build -o opencode
./opencode</code></pre>

<h3>3. Pi: Minimal Kernel with Maximum Control</h3>
<p><strong>Core Philosophy</strong>: <em>Start small, add only what you need</em>.</p>
<p>Pi is a minimal Agent Harness that defaults to just <strong>four tools</strong>: read files, write files, edit files, and execute bash commands. Its system prompt and tool definitions fit in under <strong>1,000 tokens</strong>, keeping the model's context clean and focused.</p>
<ul>
  <li><strong>Minimal Kernel</strong>: no pre-installed workflows or unnecessary tools — only the essentials.</li>
  <li><strong>Context Efficiency</strong>: reduces context size by ~3x compared to other harnesses, lowering costs by over 50% in real-world tasks.</li>
  <li><strong>Extensible System</strong>: add custom tools, commands, or UI elements via TypeScript extensions.</li>
  <li><strong>Session Management</strong>: save/restore sessions, branch conversations, and compress context.</li>
</ul>
<p><strong>Use cases</strong>: Pi is ideal for <strong>performance-critical tasks</strong> or when you need full transparency into what the model sees. If you want to minimize context pollution, reduce costs, or build lightweight agents, Pi is the most efficient choice.</p>
<pre><code class="language-bash"># Linux/macOS
curl -fsSL https://pi.dev/install.sh | sh

# Windows PowerShell
powershell -c "irm https://pi.dev/install.ps1 | iex"

# npm install
npm install -g --ignore-scripts @earendil-works/pi-coding-agent</code></pre>

<h2 id="how-to-choose">How to Choose the Right Harness</h2>
<ul>
  <li><strong>If you need to build or modify agent systems</strong>: choose <strong>DeepSeek Harness</strong> for full runtime control and plugin-level flexibility.</li>
  <li><strong>If you want a ready-to-use coding agent</strong>: choose <strong>OpenCode</strong> for out-of-the-box functionality that fits your existing workflow.</li>
  <li><strong>If you need minimal context and maximum efficiency</strong>: choose <strong>Pi</strong> for lightweight, cost-effective tasks with full transparency.</li>
</ul>
<p>Remember: the best harness is the one that aligns with your workflow, not the one with the most features.</p>

<h2 id="conclusion">Conclusion</h2>
<p>Agent harnesses are the foundation of modern AI agent systems. Whether you prioritize <strong>control</strong>, <strong>convenience</strong>, or <strong>efficiency</strong>, there is a solution for you: DeepSeek Harness offers unmatched flexibility, OpenCode provides a polished out-of-the-box experience, and Pi delivers minimalism and performance.</p>
<p>Start with the one that matches your current needs, and scale as your workflow evolves.</p>

<h2>常见问题</h2>

<h3>What is the core difference between DeepSeek Harness, OpenCode, and Pi?</h3>
<p>The core difference is how much of the environment is pre-configured and how much control you get. DeepSeek Harness is "everything is a plugin" — full runtime control; OpenCode is pre-configured but customizable — ready to use; Pi is a minimal kernel — start with 4 tools and add only what you need.</p>

<h3>When should I pick Pi over OpenCode?</h3>
<p>Pick Pi when you care about context efficiency and cost — it reduces context size by ~3x and cuts costs by over 50%. Pick OpenCode when you want to start coding immediately with a production-ready, out-of-the-box agent for debugging, refactoring, and feature work.</p>

<h3>Who is DeepSeek Harness best suited for?</h3>
<p>Developers who need to build or modify agent systems at the runtime level — custom agents, redefined workflows, or enterprise system integration. Its four runtime modes (Standard, Code, Minimal, Creator) make it the most flexible option.</p>

<h3>Can I use all three harnesses at the same time?</h3>
<p>Yes, they are complementary. Use Pi for lightweight, low-cost daily tasks, OpenCode for ready-to-use production coding, and DeepSeek Harness for building and experimenting with custom agent systems. Choose the one aligned with your workflow, and scale as it evolves.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Ready to go deeper into this harness ecosystem? Explore:</p>
  <ul>
    <li><a href="/article/deepseek-harness-comprehensive-guide-installation-architecture-practical-usage">DeepSeek Harness: A Comprehensive Guide to Installation, Architecture, and Practical Usage</a> — get started with the "everything is a plugin" runtime</li>
    <li><a href="/article/opencode-desktop-complete-beginners-guide">OpenCode Desktop: A Complete Beginner's Guide</a> — unlock the ready-to-use production coding agent</li>
    <li><a href="/article/10-must-have-plugins-deepseek-harness-complete-installation-usage-guide">10 Must-Have Plugins for DeepSeek Harness: Complete Installation & Usage Guide</a> — extend your agent fast with essential plugins</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">⚖️ AI 对比</span>
  <span class="meta-badge">🕒 阅读约8分钟</span>
  <span class="meta-badge">📅 2026年8月30日</span>
  <span class="meta-badge">🎯 进阶</span>
</div>

<h2 id="introduction">引言</h2>

<p>在选择Agent Harness时，没有放之四海皆准的“最佳”选项——只有最适合你需求的那个。本指南拆解三款主流Agent Harness：<strong>DeepSeek Harness</strong>、<strong>OpenCode</strong>和<strong>Pi</strong>，逐一说明各自的核心设计理念、关键特性、真实使用场景与安装命令，最后给出一套可直接套用的选择框架，帮你的AI工作流做出正确决策。</p>

<h2 id="what-is-agent-harness">什么是Agent Harness？</h2>

<p>可以把Agent Harness理解为AI模型的“工作环境”。它决定模型能看到什么、能做什么。具体来说，一个Harness负责：</p>
<ul>
  <li><strong>筛选内容</strong>——决定把哪些文件和上下文发送给模型。</li>
  <li><strong>提供工具</strong>——赋予模型读取、写入、搜索和执行能力。</li>
  <li><strong>执行工具调用</strong>——运行模型选择的操作并返回结果。</li>
  <li><strong>管理Agent循环</strong>——模型推理 → 工具调用 → 结果反馈的循环，不断重复直到任务完成。</li>
</ul>
<p>设计良好的Harness能把杂乱的工作变成结构化的工作。例如调试登录bug时，它会把相关文件组织好、提供搜索/编辑/测试工具，并过滤掉无用输出，让模型只基于真正重要的信息进行推理。</p>

<h2 id="three-engineering-forms">三大核心工程形态</h2>

<p>三款Harness的目标一致——为AI代理构建结构化的工作环境。它们的关键区别在于<strong>环境预配置了多少</strong>、<strong>用户掌握多少控制权</strong>。这一条轴正是三种工程形态的分界线。</p>

<h3>1. DeepSeek Harness（DSH）：完全掌控运行时</h3>
<p><strong>核心哲学</strong>：<em>万物皆插件</em>。</p>
<p>DeepSeek Harness基于<strong>Cordis</strong>插件系统构建，每个组件——工具、模型适配器、文件访问，甚至Agent循环本身——都是可替换的插件。这让开发者能够完全掌控代理的运行时行为。</p>
<ul>
  <li><strong>模块化设计</strong>：无需改动源码即可替换或扩展任何能力（模型、工具、会话、沙箱、存储、循环、调度、UI）。</li>
  <li><strong>可组合运行时</strong>：可重构整个工作流管线——例如改变工具执行顺序、添加自定义上下文压缩。</li>
  <li><strong>仅追加状态管理</strong>：将会话历史记录为事件序列，便于恢复与审计。</li>
  <li><strong>多种运行时模式</strong>：<strong>标准模式</strong>（通用任务的完整工具集）、<strong>代码模式</strong>（模型生成代码编排）、<strong>极简模式</strong>（shell + 文件编辑器，用于基准测试）、<strong>创建者模式</strong>（在内存中测试插件并构建新的代理模式）。</li>
</ul>
<p><strong>适用场景</strong>：DeepSeek Harness适合需要在<strong>运行时层面构建或改造Agent系统</strong>的开发者。如果你想创建自定义代理、重新定义工作流，或与复杂的企业系统集成，DSH是最灵活的选择。</p>
<pre><code class="language-bash"># Web UI快速启动
npx @deepseek-ai/dsh web

# 源码安装
git clone https://github.com/deepseek-ai/deepseek-harness
cd deepseek-harness
pnpm install
pnpm run build
pnpm dsh web</code></pre>

<h3>2. OpenCode：开箱即用且可扩展</h3>
<p><strong>核心哲学</strong>：<em>预配置，但可定制</em>。</p>
<p>OpenCode是一款功能完备的开源AI编码代理，出厂即自带一整套工具。它专为想要<strong>立即开始编码</strong>、又不想搭建运行环境的开发者设计。</p>
<ul>
  <li><strong>开箱即用能力</strong>：终端界面、桌面应用、多模型支持、会话持久化、LSP/MCP集成和权限控制。</li>
  <li><strong>TypeScript插件系统</strong>：通过添加工具、模型供应商或拦截工具调用来扩展功能。</li>
  <li><strong>GitHub集成</strong>：在GitHub issue/PR中使用<code>/opencode</code>或<code>/oc</code>直接在仓库中执行任务。</li>
  <li><strong>多编辑器支持</strong>：兼容VS Code、JetBrains、Neovim、Zed和Emacs。</li>
</ul>
<p><strong>适用场景</strong>：OpenCode非常适合<strong>日常编码任务</strong>——调试、重构或功能开发。如果你想要一个可靠、生产就绪且融入现有工作流的代理，OpenCode是最佳选择。</p>
<pre><code class="language-bash"># 一键安装（Linux/macOS）
curl -fsSL https://opencode.ai/install | bash

# 源码安装
git clone https://github.com/opencode-ai/opencode
cd opencode
go build -o opencode
./opencode</code></pre>

<h3>3. Pi：极简内核，最大掌控</h3>
<p><strong>核心哲学</strong>：<em>从小处起步，只加你需要的东西</em>。</p>
<p>Pi是一款极简Agent Harness，默认只有<strong>四个工具</strong>：读取文件、写入文件、编辑文件、执行bash命令。它的系统提示词和工具定义加起来不到<strong>1000个token</strong>，让模型的上下文保持干净聚焦。</p>
<ul>
  <li><strong>极简内核</strong>：没有预装的工作流或多余工具——只有必需品。</li>
  <li><strong>上下文高效</strong>：相比其他Harness，上下文体积缩小约3倍，在真实任务中成本降低50%以上。</li>
  <li><strong>可扩展系统</strong>：通过TypeScript扩展添加自定义工具、命令或UI元素。</li>
  <li><strong>会话管理</strong>：保存/恢复会话、分支对话、压缩上下文。</li>
</ul>
<p><strong>适用场景</strong>：Pi适合<strong>性能敏感任务</strong>，或当你需要完全看清模型看到什么时。如果你想减少上下文污染、降低成本或构建轻量代理，Pi是最高效的选择。</p>
<pre><code class="language-bash"># Linux/macOS
curl -fsSL https://pi.dev/install.sh | sh

# Windows PowerShell
powershell -c "irm https://pi.dev/install.ps1 | iex"

# npm安装
npm install -g --ignore-scripts @earendil-works/pi-coding-agent</code></pre>

<h2 id="how-to-choose">如何选择正确的Harness</h2>
<ul>
  <li><strong>需要构建或改造Agent系统</strong>：选<strong>DeepSeek Harness</strong>，获得完整的运行时控制与插件级灵活性。</li>
  <li><strong>想要开箱即用的编码代理</strong>：选<strong>OpenCode</strong>，开箱即用且能融入现有工作流。</li>
  <li><strong>需要极简上下文与最高效率</strong>：选<strong>Pi</strong>，轻量、省钱、完全透明。</li>
</ul>
<p>记住：最好的Harness是与你的工作流对齐的那个，而不是功能最多的那个。</p>

<h2 id="conclusion">结论</h2>
<p>Agent Harness是现代AI代理系统的地基。无论你优先<strong>控制力</strong>、<strong>便利性</strong>还是<strong>效率</strong>，都有对应的方案：DeepSeek Harness提供无与伦比的灵活性，OpenCode提供成熟的开箱即用体验，Pi则带来极简与性能。</p>
<p>从匹配当前需求的那个开始，随着工作流演进再逐步扩展。</p>

<h2>常见问题</h2>

<h3>DeepSeek Harness、OpenCode和Pi的核心区别是什么？</h3>
<p>核心区别在于环境预配置了多少、用户掌握多少控制权。DeepSeek Harness是“万物皆插件”——完全掌控运行时；OpenCode是预配置但可定制——开箱即用；Pi是极简内核——从4个工具起步，只加你需要的东西。</p>

<h3>什么情况下该选Pi而不是OpenCode？</h3>
<p>当你重视上下文效率和成本时选Pi——它能把上下文体积缩小约3倍、成本降低50%以上。当你想要一个生产就绪、开箱即用的代理立刻开始调试、重构和功能开发时，选OpenCode。</p>

<h3>DeepSeek Harness最适合谁？</h3>
<p>需要在运行时层面构建或改造Agent系统的开发者——自定义代理、重新定义工作流或集成企业系统。它的四种运行时模式（标准、代码、极简、创建者）使其成为最灵活的选择。</p>

<h3>这三款Harness能同时使用吗？</h3>
<p>可以，它们是互补的。用Pi处理轻量、低成本的日常任务，用OpenCode做开箱即用的生产编码，用DeepSeek Harness构建和实验自定义Agent系统。选择与工作流对齐的那个，并随其演进逐步扩展。</p>

<div class="next-step">
  <h3>📖 继续学习</h3>
  <p>准备深入这套Harness生态？继续探索：</p>
  <ul>
    <li><a href="/article/deepseek-harness-comprehensive-guide-installation-architecture-practical-usage">DeepSeek Harness：安装、架构与实用操作完全指南</a> — 上手“万物皆插件”的运行时</li>
    <li><a href="/article/opencode-desktop-complete-beginners-guide">OpenCode Desktop完全入门指南</a> — 解锁开箱即用的生产级编码代理</li>
    <li><a href="/article/10-must-have-plugins-deepseek-harness-complete-installation-usage-guide">DeepSeek Harness必备10大插件：完整安装与使用指南</a> — 用必备插件快速扩展你的Agent</li>
  </ul>
</div>`,
  },
  """
pos = s.rfind("};")
assert pos > 0
s2 = s[:pos] + content + s[pos:]
io.open(f, "w", encoding="utf-8", newline="\n").write(s2)
print("article-content.ts entries:", s2.count('content: `'))

# ---------- 3. tools.ts: add Pi ----------
f = r"src\lib\tools.ts"
s = io.open(f, encoding="utf-8").read()

tool = r"""    id: "pi",
    name: "Pi",
    nameZh: "Pi",
    description: "A minimal open-source Agent Harness that starts with just 4 tools (read/write/edit files + bash) — system prompt and tool definitions under 1,000 tokens for ~3x context reduction and 50%+ cost savings, extensible via TypeScript.",
    descriptionZh: "极简开源Agent Harness，默认仅4个工具（读写编辑文件+执行bash）——系统提示词与工具定义合计不到1000个token，实现约3倍上下文缩减和50%以上成本下降，可通过TypeScript扩展。",
    category: "coding",
    tags: ["pi", "agent-harness", "coding", "open-source", "minimal", "context-efficiency", "cli"],
    difficulty: "intermediate",
    url: "https://pi.dev",
    rating: r(4.6),
    pricing: "Free (open source)",
    useCase: "Lightweight, context-efficient AI coding — minimal 4-tool kernel, ~3x context reduction, 50%+ cost savings, TypeScript extensions and full session management",
    icon: "\u{1F4A1}",
    company: "earendil-works",
    companyZh: "earendil-works",
    founded: 2026,
    headquarters: "Open Source",
    descriptionLong: "Pi is a minimal, open-source Agent Harness developed by earendil-works and hosted at pi.dev. Its design philosophy is 'start small, add only what you need': by default it ships just four tools — read files, write files, edit files, and execute bash commands — with no pre-installed workflows or unnecessary tools. Because the system prompt and tool definitions together fit in under 1,000 tokens, the model's context stays clean and focused, which reduces context size by roughly 3x and lowers costs by over 50% in real-world tasks. Pi remains fully extensible: you can add custom tools, commands, or UI elements through TypeScript extensions, and it includes solid session management — save and restore sessions, branch conversations, and compress context. Installation is one line on every platform: curl for Linux/macOS, PowerShell for Windows, or npm with @earendil-works/pi-coding-agent. For developers who want full transparency into what the model sees and maximum cost efficiency in performance-critical tasks, Pi is the most efficient harness choice.",
    descriptionLongZh: "Pi是earendil-works开发的开源极简Agent Harness，官网pi.dev。它的设计哲学是“从小处起步，只加你需要的东西”：默认只提供四个工具——读取文件、写入文件、编辑文件、执行bash命令——没有预装工作流或多余工具。由于系统提示词和工具定义合计不到1000个token，模型上下文保持干净聚焦，在真实任务中可将上下文体积缩小约3倍、成本降低50%以上。Pi仍然完全可扩展：可以通过TypeScript扩展添加自定义工具、命令或UI元素，并内置完善的会话管理——保存/恢复会话、分支对话、压缩上下文。安装只需一行命令：Linux/macOS用curl、Windows用PowerShell，或通过npm安装@earendil-works/pi-coding-agent。对于希望在性能敏感任务中获得完全透明度和最高成本效率的开发者，Pi是最高效的Harness选择。",
    advantages: ["Minimal kernel: only 4 default tools", "System prompt + tool definitions under 1,000 tokens", "~3x context reduction, 50%+ lower costs", "TypeScript extensions for tools, commands, and UI", "Full session management (save/restore, branch, compress)", "One-line install on Linux/macOS/Windows/npm"],
    advantagesZh: ["极简内核：仅4个默认工具", "系统提示词+工具定义不足1000个token", "约3倍上下文缩减，成本降低50%以上", "TypeScript扩展：工具、命令、UI", "完善的会话管理（保存/恢复、分支、压缩）", "Linux/macOS/Windows/npm一键安装"],
    useCases: ["Lightweight, cost-efficient coding tasks", "Performance-critical agent workloads", "Full transparency into model context", "Custom lightweight agents via TypeScript extensions", "Context-compressed session management"],
    useCasesZh: ["轻量、低成本的编码任务", "性能敏感的Agent工作负载", "完全透明的模型上下文", "通过TypeScript扩展构建自定义轻量代理", "上下文压缩的会话管理"],
    targetAudience: "Developers who want a minimal, context-efficient, fully transparent Agent Harness with maximum cost savings — from individual coders to teams building lightweight agents.",
    targetAudienceZh: "希望拥有极简、上下文高效、完全透明，且成本节省最大化的Agent Harness的开发者——从个人开发者到构建轻量代理的团队。",
    pricingTiers: [
      {
        tier: "Free",
        tierZh: "免费版",
        price: "Free (open source)",
        features: ["Minimal 4-tool kernel", "Under 1,000-token system prompt + tools", "TypeScript extensions", "Session management"],
        featuresZh: ["极简4工具内核", "不足1000 token的系统提示词+工具", "TypeScript扩展", "会话管理"],
      },
    ],
    pros: ["Extreme context efficiency (~3x reduction, 50%+ lower costs)", "Full transparency into what the model sees", "Minimal learning curve — start with 4 tools", "Truly minimal and easy to audit"],
    prosZh: ["极致的上下文效率（约3倍缩减，成本降低50%以上）", "模型所见完全透明", "学习曲线极低——从4个工具起步", "真正极简，易于审计"],
    cons: ["No out-of-the-box workflows — you build them", "Fewer built-in tools than OpenCode or DeepSeek Harness", "TypeScript extensions require coding", "Younger ecosystem and community"],
    consZh: ["没有开箱即用的工作流——需要自己构建", "内置工具比OpenCode或DeepSeek Harness少", "TypeScript扩展需要写代码", "生态和社区相对年轻"],
    extensions: [],
    skills: ["Agent harness", "Context efficiency", "Minimal kernel design", "TypeScript extensions", "Session management"],
    scene: "development",
  },
  """
pos = s.rfind("] as Tool[];")
assert pos > 0
s2 = s[:pos] + tool + s[pos:]
io.open(f, "w", encoding="utf-8", newline="\n").write(s2)
print("tools.ts entries:", s2.count('id: "'))
print("DONE")
