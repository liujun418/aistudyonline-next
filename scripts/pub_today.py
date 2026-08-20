"""Publish Aug 20, 2026 — 1 article (OpenCode Desktop guide) + 1 new tool (OpenCode)."""
import os
BASE = r"C:\Users\jun\aistudyonline-next"
os.chdir(BASE)

# ---------- Part 1: articles.ts ----------
with open('src/lib/articles.ts', 'r', encoding='utf-8') as f:
    s = f.read()

a = r"""  {
    slug: "opencode-desktop-complete-beginners-guide",
    title: "OpenCode Desktop: A Complete Beginner's Guide",
    titleZh: "OpenCode Desktop完全入门指南",
    description: "OpenCode Desktop is an open-source AI coding agent (197K+ GitHub stars) that works directly in China with built-in free models. A beginner's guide to installation, Build vs Plan modes, @ / ! commands, and free-model usage rules.",
    descriptionZh: "OpenCode Desktop是开源AI编码代理（197K+ GitHub星标），内置免费模型，国内可直接使用。面向初学者的完整指南：安装、Build与Plan模式、@ / !命令、免费模型使用规则。",
    category: "ai-tutorials",
    tags: ["OpenCode", "AI Coding", "Desktop App", "Open Source", "Free Models", "DeepSeek V4 Flash", "Plan Mode"],
    difficulty: "beginner",
    toolsMentioned: ["OpenCode"],
    date: "2026-08-20",
  },
"""

last = s.rfind('];')
with open('src/lib/articles.ts', 'w', encoding='utf-8', newline='\n') as f:
    f.write(s[:last] + a + '];')
print('Part 1 done')

# ---------- Part 2: article-content.ts ----------
with open('src/lib/article-content.ts', 'r', encoding='utf-8') as f:
    s = f.read()

content = r"""  "opencode-desktop-complete-beginners-guide": {
    content: `<div class="meta-banner">
  <span class="meta-badge">📖 AI Tutorial</span>
  <span class="meta-badge">🕒 6 min read</span>
  <span class="meta-badge">📅 Aug 20, 2026</span>
  <span class="meta-badge">🎯 Beginner</span>
</div>

<h2 id="introduction">Introduction</h2>
<p>Many top AI agents like Claude Code and ChatGPT face three common issues for users:</p>
<ol>
  <li><strong>High barriers to use</strong> — accessing them in China is not straightforward</li>
  <li><strong>Long waiting times</strong> — popular platforms have long queues for trial access</li>
  <li><strong>Lack of privacy</strong> — code and data are controlled by third parties</li>
</ol>
<p>OpenCode solves all these problems with three key advantages:</p>
<ul>
  <li><strong>Open source</strong> with 197K+ GitHub stars, ensuring code transparency</li>
  <li><strong>User-friendly desktop version</strong> that works directly in China</li>
  <li><strong>Built-in free models</strong> that are ready to use</li>
</ul>
<p>This guide will walk you through installation and basic usage.</p>

<h2 id="installation">Installation</h2>
<ol>
  <li>Visit the official OpenCode download page</li>
  <li>Select the version compatible with your operating system</li>
  <li>Download and install the application</li>
</ol>
<p><strong>System Requirements:</strong></p>
<ul>
  <li>For office tasks or small personal projects, a regular home computer or lightweight laptop is sufficient</li>
</ul>

<h2 id="getting-started">Getting Started</h2>

<h3>1. Model Selection</h3>
<p>Choosing the right model is critical:</p>
<ul>
  <li><strong>Free models</strong>: Look for models marked with "Free" in the name (e.g., DeepSeek V4 Flash)</li>
  <li><strong>Model details</strong>: Hover over a model name to see its capabilities</li>
  <li><strong>Multimodal support</strong>: Only the MIMO model supports images, audio, and video in addition to text</li>
</ul>

<h3>2. Work Mode Selection</h3>
<p>OpenCode offers two primary work modes:</p>
<ul>
  <li><strong>Build mode</strong>: Default execution mode with full read/write file and command execution capabilities</li>
  <li><strong>Plan mode</strong>: Analysis and planning mode that only generates solutions without modifying files or running commands</li>
</ul>
<p><strong>When to use Plan mode:</strong></p>
<ul>
  <li>When you have a vague idea and need to clarify your approach</li>
  <li>When extending an existing project</li>
  <li>When you're unsure about the implementation details</li>
</ul>

<h3>3. Adding Work Folders</h3>
<p>OpenCode operates around project folders:</p>
<ul>
  <li><strong>For existing projects</strong>: Select your existing project folder</li>
  <li><strong>For new projects</strong>: Create a new folder with an English name (e.g., <code>test</code>) to avoid potential errors with Chinese paths</li>
</ul>

<h2 id="useful-commands">Useful Commands</h2>
<p>OpenCode provides three essential commands:</p>

<h3>@ Command</h3>
<pre><code class="language-text">@[file_path]</code></pre>
<ul>
  <li>Adds specific files or directories from your project folder as context</li>
  <li>Useful for referencing existing code or documentation</li>
</ul>

<h3>/ Command</h3>
<pre><code class="language-text">/[command_name]</code></pre>
<ul>
  <li>Quickly executes built-in or custom commands</li>
  <li>Common operations are available as one-click buttons</li>
</ul>

<h3>Shell Command</h3>
<pre><code class="language-text">![shell_command]</code></pre>
<ul>
  <li>Runs terminal commands directly in the chat window</li>
  <li>Advanced users can leverage this for system-level operations</li>
</ul>

<h2 id="free-model-rules">Free Model Usage Rules</h2>
<ul>
  <li><strong>No fixed free quota</strong>: Official documentation doesn't specify a fixed limit</li>
  <li><strong>Quota exhaustion</strong>: When your free quota is used up, you'll see a "free usage exceeded" message</li>
  <li><strong>Reset time</strong>: The countdown for quota reset varies (approximately 5 hours in some cases, up to 10+ hours in others)</li>
  <li><strong>For heavy use</strong>: Consider connecting your own API key for stable access</li>
</ul>

<h2 id="custom-models">Configuring Custom Models</h2>
<p>To use your own API key:</p>
<ol>
  <li>Open the model selection window</li>
  <li>Scroll to the bottom and click "View more providers"</li>
  <li>Select your provider from the list</li>
  <li>Enter your API key in the configuration panel</li>
</ol>

<h2 id="conclusion">Conclusion</h2>
<p>OpenCode provides a powerful, user-friendly alternative to traditional AI coding assistants. With its open-source nature, domestic accessibility, and built-in free models, it's an excellent choice for both beginners and experienced developers. Start with the free models to get familiar with the interface, then explore the advanced features as you become more comfortable.</p>

<h2>常见问题</h2>

<h3>Is OpenCode Desktop really free?</h3>
<p>Yes. OpenCode itself is open source under the MIT license, and it bundles free models that work out of the box. There is no fixed free quota documented — when your free usage is exhausted, you'll see a "free usage exceeded" message and the quota resets on a countdown that varies from roughly 5 hours to 10+ hours. If you rely on it for daily heavy work, connecting your own API key gives you stable access.</p>

<h3>What's the difference between Build mode and Plan mode?</h3>
<p>Build mode is the default execution mode: the agent has full read/write access to files and can run commands. Plan mode is analysis-only — it generates solutions and plans without modifying any files or executing commands. Use Plan mode when you have a vague idea that needs clarifying, when you're extending an existing project, or when you're unsure about implementation details and want to explore before committing changes.</p>

<h3>Why does OpenCode bundle DeepSeek V4 Flash?</h3>
<p>DeepSeek V4 Flash is one of the built-in free models in OpenCode, so you can start coding immediately without paying or configuring anything. OpenCode is model-agnostic and supports 75+ providers, so the bundled free models are just the starting point — you can also connect Anthropic, OpenAI, Gemini, local Ollama models, or your own API keys from the "View more providers" section of the model selection window.</p>

<h3>Can I use my own API key in OpenCode?</h3>
<p>Yes. Open the model selection window, scroll to the bottom, and click "View more providers". Pick your provider from the list and enter your API key in the configuration panel. This is the recommended path for heavy production use, since bundled free models may hit quota limits and their reset times vary.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Ready to get the most out of your AI coding tools? Continue with these guides:</p>
  <ul>
    <li><a href="/article/claude-code-install-setup">Claude Code Installation & Setup: From Zero to Your First AI-Generated Web Page</a> — the closed-source counterpart to OpenCode, step by step</li>
    <li><a href="/article/deepseek-v4-flash-official-release-practical-guide">DeepSeek V4 Flash Official Release: A Practical Guide to the Game-Changing AI Model</a> — the free model bundled inside OpenCode, explained in depth</li>
    <li><a href="/article/codex-agent-desktop-jarvis">Codex Agent: Your Desktop Jarvis for Effortless Task Automation</a> — another desktop AI agent for automating your daily workflow</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">📖 AI教程</span>
  <span class="meta-badge">🕒 阅读约6分钟</span>
  <span class="meta-badge">📅 2026年8月20日</span>
  <span class="meta-badge">🎯 入门</span>
</div>

<h2 id="introduction">引言</h2>
<p>许多顶级AI代理（如Claude Code和ChatGPT）给用户带来三个常见问题：</p>
<ol>
  <li><strong>使用门槛高</strong>——在国内访问它们并不容易</li>
  <li><strong>等待时间长</strong>——热门平台的试用通道排队漫长</li>
  <li><strong>缺乏隐私</strong>——代码和数据由第三方控制</li>
</ol>
<p>OpenCode通过三大优势解决了这些问题：</p>
<ul>
  <li><strong>开源</strong>，197K+ GitHub星标，确保代码透明</li>
  <li><strong>友好的桌面版</strong>，国内可直接使用</li>
  <li><strong>内置免费模型</strong>，开箱即用</li>
</ul>
<p>本指南将带你完成安装和基本使用。</p>

<h2 id="installation">安装</h2>
<ol>
  <li>访问OpenCode官方下载页面</li>
  <li>选择与你的操作系统兼容的版本</li>
  <li>下载并安装应用程序</li>
</ol>
<p><strong>系统要求：</strong></p>
<ul>
  <li>办公任务或小型个人项目，普通家用电脑或轻量笔记本即可</li>
</ul>

<h2 id="getting-started">开始使用</h2>

<h3>1. 模型选择</h3>
<p>选择正确的模型至关重要：</p>
<ul>
  <li><strong>免费模型</strong>：查找名称中标注"Free"的模型（如DeepSeek V4 Flash）</li>
  <li><strong>模型详情</strong>：将鼠标悬停在模型名称上查看其能力</li>
  <li><strong>多模态支持</strong>：只有MIMO模型支持文本之外还可处理图片、音频和视频</li>
</ul>

<h3>2. 工作模式选择</h3>
<p>OpenCode提供两种主要工作模式：</p>
<ul>
  <li><strong>Build模式</strong>：默认执行模式，具备完整的文件读写和命令执行能力</li>
  <li><strong>Plan模式</strong>：分析和规划模式，只生成方案，不修改文件也不运行命令</li>
</ul>
<p><strong>何时使用Plan模式：</strong></p>
<ul>
  <li>想法还不清晰，需要理清思路时</li>
  <li>扩展已有项目时</li>
  <li>不确定实现细节时</li>
</ul>

<h3>3. 添加工作文件夹</h3>
<p>OpenCode围绕项目文件夹工作：</p>
<ul>
  <li><strong>已有项目</strong>：选择你的现有项目文件夹</li>
  <li><strong>新项目</strong>：创建一个英文名称的新文件夹（如<code>test</code>），避免中文路径可能导致的错误</li>
</ul>

<h2 id="useful-commands">常用命令</h2>
<p>OpenCode提供三个基本命令：</p>

<h3>@命令</h3>
<pre><code class="language-text">@[file_path]</code></pre>
<ul>
  <li>把项目文件夹中的特定文件或目录添加为上下文</li>
  <li>适合引用现有代码或文档</li>
</ul>

<h3>/命令</h3>
<pre><code class="language-text">/[command_name]</code></pre>
<ul>
  <li>快速执行内置或自定义命令</li>
  <li>常见操作以一键按钮形式提供</li>
</ul>

<h3>Shell命令</h3>
<pre><code class="language-text">![shell_command]</code></pre>
<ul>
  <li>直接在聊天窗口中运行终端命令</li>
  <li>高级用户可借此进行系统级操作</li>
</ul>

<h2 id="free-model-rules">免费模型使用规则</h2>
<ul>
  <li><strong>无固定免费额度</strong>：官方文档未指定固定上限</li>
  <li><strong>额度用尽</strong>：免费额度用完后，会看到"free usage exceeded"提示</li>
  <li><strong>重置时间</strong>：额度重置的倒计时各不相同（有的约5小时，有的可达10小时以上）</li>
  <li><strong>重度使用</strong>：建议接入自己的API Key以获得稳定访问</li>
</ul>

<h2 id="custom-models">配置自定义模型</h2>
<p>要使用你自己的API Key：</p>
<ol>
  <li>打开模型选择窗口</li>
  <li>滚动到底部，点击"View more providers"</li>
  <li>从列表中选择你的供应商</li>
  <li>在配置面板中输入你的API Key</li>
</ol>

<h2 id="conclusion">结语</h2>
<p>OpenCode为传统AI编程助手提供了一个强大而友好的替代方案。凭借其开源特性、国内可用性和内置免费模型，无论新手还是经验丰富的开发者，它都是绝佳选择。先从免费模型入手熟悉界面，再逐步探索高级功能。</p>

<h2>常见问题</h2>

<h3>OpenCode Desktop真的免费吗？</h3>
<p>是的。OpenCode本身以MIT协议开源，并内置开箱即用的免费模型。官方没有设定固定免费额度——免费用量用尽时会看到"free usage exceeded"提示，额度按倒计时重置，时长从约5小时到10小时以上不等。如果每天重度使用，接入自己的API Key可以获得更稳定的访问。</p>

<h3>Build模式和Plan模式有什么区别？</h3>
<p>Build模式是默认执行模式：代理对文件有完整的读写权限，并能运行命令。Plan模式只做分析——它生成方案和计划，但不修改任何文件也不执行命令。当你想法还不清晰需要理清思路、要扩展已有项目，或不确定实现细节想先探索再动手时，就用Plan模式。</p>

<h3>为什么OpenCode内置DeepSeek V4 Flash？</h3>
<p>DeepSeek V4 Flash是OpenCode内置的免费模型之一，所以你可以不花一分钱、不配置任何东西就立即开始编码。OpenCode模型无关，支持75+供应商，内置免费模型只是起点——你还可以从模型选择窗口的"View more providers"接入Anthropic、OpenAI、Gemini、本地Ollama模型，或你自己的API Key。</p>

<h3>我可以在OpenCode里使用自己的API Key吗？</h3>
<p>可以。打开模型选择窗口，滚动到底部，点击"View more providers"。从列表中选择你的供应商，在配置面板中输入API Key。这是重度生产使用的推荐方式，因为内置免费模型可能触达额度上限，且重置时间不固定。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>想充分发挥你的AI编程工具？继续阅读这些指南：</p>
  <ul>
    <li><a href="/article/claude-code-install-setup">Claude Code安装与配置：从零开始到你的第一个AI网页</a> — OpenCode的闭源对标工具，手把手教程</li>
    <li><a href="/article/deepseek-v4-flash-official-release-practical-guide">DeepSeek V4 Flash正式发布：改变游戏规则的AI模型实战指南</a> — OpenCode内置免费模型的深度解读</li>
    <li><a href="/article/codex-agent-desktop-jarvis">Codex Agent：你的桌面贾维斯，轻松实现任务自动化</a> — 另一款桌面AI代理，自动化你的日常工作流</li>
  </ul>
</div>`,
  },
"""

last = s.rfind('};')
with open('src/lib/article-content.ts', 'w', encoding='utf-8', newline='\n') as f:
    f.write(s[:last] + content + '};')
print('Part 2 done')

# ---------- Part 3: tools.ts ----------
with open('src/lib/tools.ts', 'r', encoding='utf-8') as f:
    s = f.read()

t = r"""  {
    id: "opencode",
    name: "OpenCode",
    nameZh: "OpenCode",
    description: "An open-source AI coding agent with 197K+ GitHub stars — model-agnostic (75+ providers), desktop + terminal TUI, and built-in free models like DeepSeek V4 Flash that work directly in China.",
    descriptionZh: "拥有197K+ GitHub星标的开源AI编码代理——模型无关（支持75+供应商）、桌面版+终端TUI、内置DeepSeek V4 Flash等免费模型，国内可直接使用。",
    category: "coding",
    tags: ["opencode", "ai-agent", "coding", "open-source", "desktop", "free-models", "cli"],
    difficulty: "beginner",
    url: "https://opencode.ai",
    rating: r(4.8),
    pricing: "Free (open source, MIT license)",
    useCase: "AI-powered coding in a desktop app or terminal — Build mode for full file/command access, Plan mode for analysis-only, with built-in free models",
    icon: "\u{1F680}",
    company: "SST",
    companyZh: "SST",
    founded: 2025,
    headquarters: "United States",
    descriptionLong: "OpenCode is an open-source AI coding agent built by the SST team (github.com/sst/opencode), MIT-licensed and hosted at opencode.ai. With 197K+ GitHub stars and 950+ contributors, it is the most-starred open-source coding agent. It is fully model-agnostic, supporting 75+ LLM providers including Anthropic Claude, OpenAI, Google Gemini, Amazon Bedrock, Groq, OpenRouter, and local Ollama models. OpenCode runs in three surfaces: a terminal TUI built on the in-house OpenTUI framework, a desktop app (Beta) for macOS, Windows and Linux, and IDE integration. It ships two agent modes — Build mode (full read/write file access and command execution) and Plan mode (analysis-only, generates solutions without modifying files) — plus General and Explore subagents. LSP integration feeds real compiler diagnostics back to the model with 25+ built-in language servers. OpenCode also supports MCP, custom agents, plugins, and a client-server architecture for headless automation in GitHub Actions and CI. For users in China, the desktop version works directly without extra setup and bundles free models such as DeepSeek V4 Flash, making it a practical alternative to Claude Code and ChatGPT for everyday coding.",
    descriptionLongZh: "OpenCode是SST团队构建的开源AI编码代理（github.com/sst/opencode），采用MIT协议，官网opencode.ai。拥有197K+ GitHub星标和950+贡献者，是星标数最高的开源编码代理。它完全模型无关，支持75+ LLM供应商，包括Anthropic Claude、OpenAI、Google Gemini、Amazon Bedrock、Groq、OpenRouter和本地Ollama模型。OpenCode在三种界面运行：基于自研OpenTUI框架的终端TUI、桌面应用（Beta，支持macOS、Windows和Linux）以及IDE集成。它提供两种代理模式——Build模式（完整的文件读写和命令执行能力）和Plan模式（仅分析，生成解决方案而不修改文件）——以及General和Explore子代理。LSP集成通过25+内置语言服务器把真实的编译器诊断反馈给模型。OpenCode还支持MCP、自定义代理、插件，以及用于GitHub Actions和CI无头自动化的客户端-服务器架构。对于中国用户，桌面版无需额外配置即可直接使用，并内置DeepSeek V4 Flash等免费模型，是Claude Code和ChatGPT日常编码的实用替代品。",
    advantages: ["Open source with 197K+ GitHub stars", "Model-agnostic: supports 75+ providers", "Built-in free models work in China", "Desktop app for macOS, Windows, Linux", "Build + Plan dual agent modes", "MCP, plugins and custom agents"],
    advantagesZh: ["开源，197K+ GitHub星标", "模型无关：支持75+供应商", "内置免费模型，国内可直接使用", "macOS、Windows、Linux桌面应用", "Build + Plan双代理模式", "支持MCP、插件和自定义代理"],
    useCases: ["AI coding in a desktop app or terminal", "Free-model coding with DeepSeek V4 Flash", "Plan-only analysis for existing projects", "Headless automation via client-server API", "Local model coding via Ollama"],
    useCasesZh: ["在桌面应用或终端中进行AI编码", "用DeepSeek V4 Flash免费模型编码", "对现有项目做仅分析的规划", "通过客户端-服务器API实现无头自动化", "通过Ollama用本地模型编码"],
    targetAudience: "Developers who want a free, open-source, model-agnostic AI coding assistant that works in China — from beginners to professional teams",
    targetAudienceZh: "希望使用免费、开源、模型无关且国内可用的AI编码助手的开发者——从初学者到专业团队",
    pricingTiers: [
      {
        tier: "Free",
        tierZh: "免费版",
        price: "Free (open source, MIT license)",
        features: ["Desktop app + terminal TUI", "Built-in free models", "75+ model providers", "MCP, plugins, custom agents"],
        featuresZh: ["桌面应用 + 终端TUI", "内置免费模型", "75+模型供应商", "MCP、插件、自定义代理"],
      },
    ],
    pros: ["Completely free and open source", "Model-agnostic with no lock-in", "Works directly in China with free models", "Dual Build/Plan modes for safe exploration", "Fast-growing community (197K+ stars)"],
    prosZh: ["完全免费开源", "模型无关，无绑定", "内置免费模型国内直连可用", "Build/Plan双模式安全探索", "社区增长迅猛（197K+星标）"],
    cons: ["Desktop app still in Beta", "Best experience requires understanding model selection", "Heavy production use may need your own API key"],
    consZh: ["桌面应用仍处于Beta阶段", "最佳体验需要理解模型选择", "重度生产使用可能需要自己的API key"],
    extensions: [],
    skills: ["AI coding", "Agent automation", "Model integration", "Terminal workflows", "Desktop automation"],
    scene: "development",
  },
"""

last = s.rfind('] as Tool[];')
with open('src/lib/tools.ts', 'w', encoding='utf-8', newline='\n') as f:
    f.write(s[:last] + t + '] as Tool[];')
print('Part 3 done')

print('ALL DONE')
