"""Publish Aug 14, 2026 — 1 article + 1 new tool (DeepSeek Harness)."""
import os; BASE = r"C:\Users\jun\aistudyonline-next"; os.chdir(BASE)

# ---------- Part 1: articles.ts metadata ----------
with open('src/lib/articles.ts', 'r', encoding='utf-8') as f: s = f.read()
a = r"""  {
    slug: "deepseek-harness-comprehensive-guide-installation-architecture-practical-usage",
    title: "DeepSeek Harness: A Comprehensive Guide to Installation, Architecture, and Practical Usage",
    titleZh: "DeepSeek Harness：安装、架构与实用操作完全指南",
    description: "A complete guide to DeepSeek Harness — the MIT-licensed open-source AI agent framework with 34K GitHub stars in 4 hours. Covers the 'Everything is a Plugin' architecture built on Cordis, one-command npm installation, a hands-on portfolio website build, and extending agents with plugins like MOD Lens.",
    descriptionZh: "DeepSeek Harness完全指南——发布4小时获34K GitHub星标的MIT协议开源AI代理框架。详解基于Cordis的'万物皆插件'架构、一条命令的npm安装、实战搭建作品集网站，以及用MOD Lens等插件扩展代理能力。",
    category: "ai-tutorials",
    tags: ["DeepSeek", "DeepSeek Harness", "AI Agent", "Open Source", "Plugin", "Cordis", "Tutorial"],
    difficulty: "intermediate",
    toolsMentioned: ["DeepSeek Harness"],
    date: "2026-08-14",
  },

"""
last = s.rfind('];')
with open('src/lib/articles.ts', 'w', encoding='utf-8') as f: f.write(s[:last] + a + '];')
print('Part 1 done')

# ---------- Part 2: article-content.ts bilingual content ----------
with open('src/lib/article-content.ts', 'r', encoding='utf-8') as f: c = f.read()
n = r'''
  "deepseek-harness-comprehensive-guide-installation-architecture-practical-usage": {
    content: `<div class="meta-banner">
  <span class="meta-badge">📖 AI Tutorial</span>
  <span class="meta-badge">🕒 7 min read</span>
  <span class="meta-badge">📅 Aug 14, 2026</span>
  <span class="meta-badge">🎯 Intermediate</span>
</div>

<h2 id="introduction">Introduction</h2>
<p>DeepSeek Harness has rapidly become one of the most talked-about AI agent projects, amassing an impressive 34K GitHub stars within just four hours of its release. This open-source framework, released under the MIT license, is not just another coding agent or AI assistant — it's a fully customizable harness base built on the principle of "Everything is a Plugin." This guide will walk you through its architecture, installation, practical applications, and how to leverage its powerful plugin system.</p>

<h2 id="what-is">What is DeepSeek Harness?</h2>
<p>DeepSeek Harness represents a paradigm shift in AI agent development. While large language models (LLMs) provide the "intelligence" of an AI, the harness is the runtime environment that enables the model to interact with the real world. Think of it this way: if the model is the engine of a car, the harness is the entire vehicle system that allows the engine to function, including the steering, brakes, and other critical components.</p>
<p>The official formula for this concept is:</p>
<pre><code class="language-text">Agent = Model + Harness</code></pre>
<p>Harness is responsible for:</p>
<ul>
  <li>Managing the model's runtime environment</li>
  <li>Enabling tool usage and integration</li>
  <li>Handling long-running tasks and planning</li>
  <li>Providing context management</li>
  <li>Ensuring task completion and validation</li>
</ul>

<h2 id="architecture">Core Architecture</h2>
<p>DeepSeek Harness is built on the Cordis plugin system, which enables its "Everything is a Plugin" philosophy. This architecture allows every component of the agent to be replaced, extended, or customized through plugins, without modifying the core source code.</p>
<h3>Key Components</h3>
<ul>
  <li><strong>Cordis Kernel</strong>: The meta-framework that manages plugin loading, unloading, and dependencies.</li>
  <li><strong>Plugin System</strong>: Every capability is implemented as a plugin, including model adapters, tool registries, skills and workflows, session management, sandbox environments, storage systems, agent loops, and user interfaces.</li>
  <li><strong>Configuration System</strong>: Developers can select, swap, or extend any capability through configuration files.</li>
</ul>

<h2 id="installation">Installation and Setup</h2>
<p>Installing DeepSeek Harness is straightforward using npm:</p>
<pre><code class="language-bash"># Install and launch the web interface
npx @deepseek-ai/dsh web</code></pre>
<p>When the installation completes, you'll see a local URL (typically <code>http://127.0.0.1:3080</code>). Open this address in your browser to access the Harness interface.</p>
<h3>Initial Configuration</h3>
<ol>
  <li><strong>API Key Setup</strong>: You'll need to provide your DeepSeek API key to use the model capabilities.</li>
  <li><strong>Workspace Selection</strong>: Choose a directory for your project files.</li>
  <li><strong>Model Configuration</strong>: Select the model you want to use (DeepSeek V4, V4 Flash, etc.).</li>
</ol>

<h2 id="practical-usage">Practical Usage Example</h2>
<p>Let's walk through a practical example of using DeepSeek Harness to create a personal portfolio website.</p>
<h3>Step 1: Define the Task</h3>
<p>Provide a detailed prompt describing your requirements:</p>
<pre><code class="language-text">Create a personal portfolio website for an AI product designer. The site should include:
- A hero section with a tagline
- Product design process showcase
- About section
- Project gallery
- Skills and capabilities section

The design should be clean, modern, and responsive. Use appropriate typography and color schemes that reflect a professional yet creative aesthetic.</code></pre>
<h3>Step 2: Execute the Task</h3>
<p>DeepSeek Harness will:</p>
<ol>
  <li>Create a project directory structure</li>
  <li>Generate HTML, CSS, and JavaScript files</li>
  <li>Implement the design and functionality</li>
  <li>Provide a local preview of the website</li>
</ol>
<h3>Step 3: Review and Refine</h3>
<p>Once the task is complete, you can view the generated website, make any necessary adjustments, and deploy the final product.</p>

<h2 id="plugin-system">Plugin System</h2>
<p>DeepSeek Harness's plugin system is its most powerful feature. With plugins, you can:</p>
<ul>
  <li><strong>Extend Capabilities</strong>: Add new tools, skills, or workflows</li>
  <li><strong>Customize Behavior</strong>: Modify how the agent operates</li>
  <li><strong>Integrate Services</strong>: Connect with external APIs and services</li>
  <li><strong>Enhance UI</strong>: Customize the user interface</li>
</ul>
<h3>Example: Adding Visual Capabilities</h3>
<p>To add visual capabilities to DeepSeek Harness, you can install a plugin like MOD Lens:</p>
<pre><code class="language-bash"># Install the plugin
npx -y @llustack/modlens --profile web add --save-exact @llustack/modlens@3.9.1

# Configure the plugin
npx -y @llustack/modlens config set provider openai
npx -y @llustack/modlens config set openai.baseurl "https://your-vision-model-endpoint"
npx -y @llustack/modlens config set openai.model "qwen3-vl-plus"

# Set your API key
export DEEPSEEK_API_KEY="your-api-key"
npx @deepseek-ai/dsh web</code></pre>

<h2 id="performance">Performance and Capabilities</h2>
<p>In performance tests, DeepSeek Harness has shown impressive results:</p>
<ul>
  <li>Comparable to Codex + GPT-5.6 SOI in task completion</li>
  <li>Faster execution speed</li>
  <li>Superior front-end design capabilities</li>
</ul>
<p>This makes it a strong competitor in the AI agent space, offering a flexible and powerful alternative to existing solutions.</p>

<h2 id="conclusion">Conclusion</h2>
<p>DeepSeek Harness represents a significant advancement in AI agent development. Its plugin-based architecture, open-source nature, and powerful capabilities make it an excellent choice for developers looking to build customizable and capable AI agents. Whether you're building coding assistants, productivity tools, or complex workflow automation systems, DeepSeek Harness provides the foundation you need to create powerful, adaptable AI solutions.</p>
<p>With its MIT license and growing community, DeepSeek Harness is poised to become a key player in the future of AI agent development. For more detailed documentation and advanced tutorials, visit the official DeepSeek Harness website or check out the community resources available online.</p>

<h2>常见问题</h2>

<h3>What is DeepSeek Harness, and how is it different from a coding agent?</h3>
<p>DeepSeek Harness is an open-source AI agent framework, not a single coding agent. It's the runtime "vehicle" that lets any model drive real-world tasks — the model is the engine, the harness is the whole car. This is different from tools like Codex that focus on one workflow: Harness is a foundation you build your own agents on. Every capability, from model adapters to tools to sandboxes, is a replaceable plugin, so you're not locked into a fixed set of behaviors.</p>

<h3>Is DeepSeek Harness free to use?</h3>
<p>Yes. DeepSeek Harness is released under the MIT license and is completely open source — you can use it, modify it, and build commercial products on top of it without licensing fees. You only pay for the underlying model API calls, like your DeepSeek API usage. The 34K GitHub stars in its first four hours reflect a large and fast-growing community.</p>

<h3>What is the "Everything is a Plugin" philosophy?</h3>
<p>It means every part of the agent is a modular plugin that can be swapped without touching core code. Built on the Cordis plugin system, the harness treats model adapters, tool registries, skills, workflows, session management, sandboxes, storage, agent loops, and even the UI as plugins. Want a different sandbox or a new tool? Just add a plugin — no forks, no rewrites. This is what makes it customizable at a level most agent tools don't reach.</p>

<h3>What hardware or setup do I need to run DeepSeek Harness?</h3>
<p>None beyond Node.js and npm. Installation is a single command — <code>npx @deepseek-ai/dsh web</code> — which launches a local web interface at <code>http://127.0.0.1:3080</code>. You configure your DeepSeek API key, pick a workspace directory, and select a model. Because the heavy lifting happens in the model API, it runs on a normal laptop, and you can add plugins like MOD Lens for additional capabilities such as vision.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Ready to build agents? Continue with these guides:</p>
  <ul>
    <li><a href="/article/deepseek-v4-flash-vs-gpt-5-6-luna-codex-integration-benchmark">DeepSeek V4 Flash vs GPT-5.6 Luna: Codex Integration & 10-Round Benchmark</a> — how to wire DeepSeek into agent workflows and how it stacks up head-to-head</li>
    <li><a href="/article/codex-skill-bundle-4-skills-professional-websites-one-prompt">Codex Skill Bundle: 4 Skills to Build Professional Websites in One Prompt</a> — a practical agent workflow for building complete sites from a single prompt</li>
    <li><a href="/article/deepseek-v4-pro-0813-real-world-testing-two-ai-development-projects">DeepSeek V4 Pro 0813 Real-World Testing: Two Practical AI Development Projects</a> — what DeepSeek models deliver on real projects, from blogs to 3D games</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">📖 AI教程</span>
  <span class="meta-badge">🕒 阅读约7分钟</span>
  <span class="meta-badge">📅 2026年8月14日</span>
  <span class="meta-badge">🎯 进阶</span>
</div>

<h2 id="introduction">引言</h2>
<p>DeepSeek Harness在发布后短短四小时内就积累了惊人的34K GitHub星标，迅速成为最受关注的AI代理项目之一。这个基于MIT协议发布的开源框架，不只是又一个编程代理或AI助手——它是以"万物皆插件"为核心理念构建的完全可定制底座。本指南将带你了解它的架构、安装、实际应用，以及如何利用其强大的插件系统。</p>

<h2 id="what-is">什么是DeepSeek Harness？</h2>
<p>DeepSeek Harness代表了AI代理开发范式的转变。大语言模型（LLM）提供AI的"智能"，而harness是让模型与真实世界交互的运行时环境。打个比方：如果模型是汽车的引擎，harness就是让引擎运转的整个车辆系统，包括转向、刹车等关键组件。</p>
<p>这个概念的标准公式是：</p>
<pre><code class="language-text">Agent = Model + Harness</code></pre>
<p>Harness负责：</p>
<ul>
  <li>管理模型的运行时环境</li>
  <li>支持工具使用和集成</li>
  <li>处理长任务和规划</li>
  <li>提供上下文管理</li>
  <li>确保任务完成和验证</li>
</ul>

<h2 id="architecture">核心架构</h2>
<p>DeepSeek Harness构建在Cordis插件系统之上，实现了"万物皆插件"的理念。这种架构让代理的每个组件都可以通过插件替换、扩展或定制，而无需修改核心源码。</p>
<h3>关键组件</h3>
<ul>
  <li><strong>Cordis内核</strong>：管理插件加载、卸载和依赖关系的元框架。</li>
  <li><strong>插件系统</strong>：每项能力都实现为插件，包括模型适配器、工具注册表、技能与工作流、会话管理、沙箱环境、存储系统、代理循环和用户界面。</li>
  <li><strong>配置系统</strong>：开发者可以通过配置文件选择、替换或扩展任何能力。</li>
</ul>

<h2 id="installation">安装与设置</h2>
<p>使用npm安装DeepSeek Harness非常简单：</p>
<pre><code class="language-bash"># 安装并启动Web界面
npx @deepseek-ai/dsh web</code></pre>
<p>安装完成后，你会看到一个本地URL（通常是<code>http://127.0.0.1:3080</code>）。在浏览器中打开这个地址即可访问Harness界面。</p>
<h3>初始配置</h3>
<ol>
  <li><strong>API密钥设置</strong>：你需要提供DeepSeek API密钥才能使用模型能力。</li>
  <li><strong>工作区选择</strong>：为项目文件选择一个目录。</li>
  <li><strong>模型配置</strong>：选择要使用的模型（DeepSeek V4、V4 Flash等）。</li>
</ol>

<h2 id="practical-usage">实际使用示例</h2>
<p>让我们通过一个实际示例，看看如何用DeepSeek Harness创建一个个人作品集网站。</p>
<h3>第一步：定义任务</h3>
<p>提供一段描述你需求的详细提示词：</p>
<pre><code class="language-text">为一个AI产品设计师创建一个个人作品集网站。网站应包括：
- 带宣传语的Hero区域
- 产品设计流程展示
- 关于我板块
- 项目画廊
- 技能与能力板块

设计应简洁、现代且响应式。使用体现专业又富有创意的排版和配色。</code></pre>
<h3>第二步：执行任务</h3>
<p>DeepSeek Harness将：</p>
<ol>
  <li>创建项目目录结构</li>
  <li>生成HTML、CSS和JavaScript文件</li>
  <li>实现设计与功能</li>
  <li>提供网站的本地预览</li>
</ol>
<h3>第三步：审阅与优化</h3>
<p>任务完成后，你可以查看生成的网站、做必要的调整，并部署最终产品。</p>

<h2 id="plugin-system">插件系统</h2>
<p>DeepSeek Harness的插件系统是它最强大的特性。通过插件，你可以：</p>
<ul>
  <li><strong>扩展能力</strong>：添加新工具、技能或工作流</li>
  <li><strong>自定义行为</strong>：修改代理的运作方式</li>
  <li><strong>集成服务</strong>：连接外部API和服务</li>
  <li><strong>增强UI</strong>：定制用户界面</li>
</ul>
<h3>示例：添加视觉能力</h3>
<p>要给DeepSeek Harness添加视觉能力，可以安装MOD Lens这样的插件：</p>
<pre><code class="language-bash"># 安装插件
npx -y @llustack/modlens --profile web add --save-exact @llustack/modlens@3.9.1

# 配置插件
npx -y @llustack/modlens config set provider openai
npx -y @llustack/modlens config set openai.baseurl "https://your-vision-model-endpoint"
npx -y @llustack/modlens config set openai.model "qwen3-vl-plus"

# 设置API密钥
export DEEPSEEK_API_KEY="your-api-key"
npx @deepseek-ai/dsh web</code></pre>

<h2 id="performance">性能与能力</h2>
<p>在性能测试中，DeepSeek Harness表现亮眼：</p>
<ul>
  <li>任务完成度可与Codex + GPT-5.6 SOI相媲美</li>
  <li>执行速度更快</li>
  <li>前端设计能力更胜一筹</li>
</ul>
<p>这使它成为AI代理领域的强劲竞争者，为现有方案提供了灵活而强大的替代选择。</p>

<h2 id="conclusion">结语</h2>
<p>DeepSeek Harness代表了AI代理开发的重大进步。它的插件化架构、开源特性和强大能力，使它成为希望构建可定制AI代理的开发者的绝佳选择。无论你在构建编程助手、生产力工具，还是复杂的工作流自动化系统，DeepSeek Harness都能为你提供坚实的基础。</p>
<p>凭借MIT协议和不断壮大的社区，DeepSeek Harness有望成为AI代理开发未来格局中的关键角色。更多详细文档和进阶教程，请访问DeepSeek Harness官网或查看在线社区资源。</p>

<h2>常见问题</h2>

<h3>什么是DeepSeek Harness？它与编程代理有什么不同？</h3>
<p>DeepSeek Harness是一个开源AI代理框架，而不是单一的编程代理。它是让任何模型驱动真实世界任务的运行时"载体"——模型是引擎，harness是整辆车。这与Codex等专注单一工作流的工具不同：Harness是让你自己构建代理的基础。从模型适配器到工具再到沙箱，每项能力都是可替换的插件，你不会被锁定在一套固定的行为上。</p>

<h3>DeepSeek Harness免费吗？</h3>
<p>免费。DeepSeek Harness以MIT协议发布，完全开源——你可以使用、修改并在其上构建商业产品，无需授权费用。你只需要为底层模型的API调用付费，比如你的DeepSeek API用量。发布四小时内获得34K GitHub星标，反映了它庞大且快速增长的社区。</p>

<h3>"万物皆插件"理念是什么意思？</h3>
<p>它的意思是代理的每个部分都是可插拔的模块，无需修改核心代码就能替换。基于Cordis插件系统，harness把模型适配器、工具注册表、技能、工作流、会话管理、沙箱、存储、代理循环甚至UI都视为插件。想要不同的沙箱或新工具？添加一个插件就行——无需fork、无需重写。这让它的可定制程度远超大多数代理工具。</p>

<h3>运行DeepSeek Harness需要什么硬件或环境？</h3>
<p>只需要Node.js和npm。安装只需一条命令——<code>npx @deepseek-ai/dsh web</code>——它会在<code>http://127.0.0.1:3080</code>启动本地Web界面。配置好DeepSeek API密钥、选择一个工作区目录、选好模型即可。因为繁重计算都在模型API里完成，普通笔记本就能运行，你还可以安装MOD Lens等插件获得视觉等额外能力。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>准备好构建代理了吗？继续阅读这些指南：</p>
  <ul>
    <li><a href="/article/deepseek-v4-flash-vs-gpt-5-6-luna-codex-integration-benchmark">DeepSeek V4 Flash vs GPT-5.6 Luna：Codex完整接入与10轮实测</a> — 如何把DeepSeek接入代理工作流以及它的正面实力对比</li>
    <li><a href="/article/codex-skill-bundle-4-skills-professional-websites-one-prompt">Codex技能包：一个提示词构建专业网站的4个技能</a> — 用单个提示词构建完整网站的实用代理工作流</li>
    <li><a href="/article/deepseek-v4-pro-0813-real-world-testing-two-ai-development-projects">DeepSeek V4 Pro 0813实战测试：两个实用AI开发项目</a> — DeepSeek模型在真实项目上能交付什么，从博客到3D游戏</li>
  </ul>
</div>`,
  },

'''
last = c.rfind('};')
with open('src/lib/article-content.ts', 'w', encoding='utf-8') as f: f.write(c[:last] + n + '};')
print('Part 2 done')

# ---------- Part 3: tools.ts new tool ----------
with open('src/lib/tools.ts', 'r', encoding='utf-8') as f: t = f.read()
tool = r'''  {
    id: "deepseek-harness",
    name: "DeepSeek Harness",
    nameZh: "DeepSeek Harness",
    description: "An MIT-licensed, open-source AI agent framework built on the 'Everything is a Plugin' philosophy — 34K GitHub stars in 4 hours, powered by the Cordis plugin system for fully customizable agents.",
    descriptionZh: "基于'万物皆插件'理念的MIT协议开源AI代理框架——发布4小时获34K GitHub星标，由Cordis插件系统驱动，构建完全可定制的AI代理。",
    category: "ai-agent",
    tags: ["deepseek", "ai-agent", "harness", "open-source", "plugin", "cordis"],
    difficulty: "intermediate",
    url: "https://www.npmjs.com/package/@deepseek-ai/dsh",
    rating: r(4.6),
    pricing: "Free (open source, MIT license)",
    useCase: "Building fully customizable AI agents — coding assistants, productivity tools, and workflow automation with pluggable model adapters, tools, and sandboxes",
    icon: "\u{1F527}",
    company: "DeepSeek",
    companyZh: "深度求索",
    founded: 2023,
    headquarters: "Hangzhou, China",
    descriptionLong: "DeepSeek Harness is an open-source AI agent framework from DeepSeek, released under the MIT license and built on the Cordis plugin system with an 'Everything is a Plugin' philosophy. It treats every capability — model adapters, tool registries, skills and workflows, session management, sandbox environments, storage systems, agent loops, and user interfaces — as a swappable plugin, so developers can build, extend, or customize agents without modifying core code. The core concept is Agent = Model + Harness: the model provides intelligence, while the harness is the runtime that lets it interact with the real world through tools, planning, and validation. Installation is a single command — npx @deepseek-ai/dsh web — which launches a local web interface at http://127.0.0.1:3080 where users configure their DeepSeek API key, workspace, and model. It supports practical builds like a 6-style personal blog or a portfolio website from a single natural-language prompt, and plugins like MOD Lens add vision or other capabilities. In performance tests it ranks comparable to Codex + GPT-5.6 SOI in task completion with faster execution and stronger front-end design. The project reached 34K GitHub stars within four hours of release, signaling a large and fast-growing community.",
    descriptionLongZh: "DeepSeek Harness是DeepSeek推出的开源AI代理框架，以MIT协议发布，构建在Cordis插件系统之上，秉持'万物皆插件'理念。它把每项能力——模型适配器、工具注册表、技能与工作流、会话管理、沙箱环境、存储系统、代理循环和用户界面——都视为可替换的插件，开发者无需修改核心代码即可构建、扩展或定制代理。核心概念是Agent = Model + Harness：模型提供智能，而harness是让它通过工具、规划和验证与真实世界交互的运行时。安装只需一条命令——npx @deepseek-ai/dsh web——它会在http://127.0.0.1:3080启动本地Web界面，用户在此配置DeepSeek API密钥、工作区和模型。它支持从单个自然语言提示词构建6风格个人博客或作品集网站等实际项目，MOD Lens等插件可添加视觉或其他能力。在性能测试中，任务完成度与Codex + GPT-5.6 SOI相当，执行速度更快、前端设计能力更强。项目发布四小时内即获34K GitHub星标，标志着庞大且快速增长的社区。",
    advantages: ["MIT-licensed and fully open source", "Everything is a Plugin with the Cordis system", "One-command npm installation with local web UI", "Customizable agents without core code changes", "Comparable to Codex + GPT-5.6 SOI in performance", "Fast-growing community (34K stars in 4 hours)"],
    advantagesZh: ["MIT协议完全开源", "基于Cordis系统实现万物皆插件", "一条npm命令安装，带本地Web界面", "无需修改核心代码即可定制代理", "性能可与Codex + GPT-5.6 SOI媲美", "社区增长迅猛（4小时34K星标）"],
    useCases: ["Building custom coding assistants", "Personal portfolio or blog website generation", "Workflow automation with pluggable tools", "Extending agents with vision or other plugins", "Productivity tool development"],
    useCasesZh: ["构建自定义编程助手", "生成个人作品集或博客网站", "用可插拔工具实现工作流自动化", "通过插件扩展代理的视觉等能力", "生产力工具开发"],
    targetAudience: "Developers and teams who want to build, extend, or customize AI agents without being locked into a fixed set of behaviors — from solo hackers to production teams",
    targetAudienceZh: "希望构建、扩展或定制AI代理而不被锁定在固定行为中的开发者和团队——从独立黑客到生产团队",
    pricingTiers: [
      {
        tier: "Free",
        tierZh: "免费版",
        price: "Free (open source, MIT license)",
        features: ["Full plugin system", "Local web interface", "Model adapter support", "Custom tools and skills"],
        featuresZh: ["完整插件系统", "本地Web界面", "模型适配器支持", "自定义工具和技能"],
      },
    ],
    pros: ["Fully open source with MIT license", "Extreme customizability via plugins", "Simple one-command setup", "Strong real-world task completion", "Rapidly growing community"],
    prosZh: ["MIT协议完全开源", "通过插件实现极高的可定制性", "一条命令轻松安装", "真实任务完成能力强", "社区增长迅速"],
    cons: ["Very new project with a short track record", "Advanced customization requires understanding Cordis", "Best experience tied to DeepSeek model API"],
    consZh: ["项目很新，历史记录较短", "高级定制需要理解Cordis", "最佳体验依赖DeepSeek模型API"],
    extensions: [],
    skills: ["Agent development", "Plugin development", "Tool integration", "Workflow automation", "Website generation"],
    scene: "development",
  },

'''
last_tool = t.rfind('] as Tool[];')
with open('src/lib/tools.ts', 'w', encoding='utf-8') as f: f.write(t[:last_tool] + tool + '] as Tool[];')
print('Part 3 done\n=== Done ===')
