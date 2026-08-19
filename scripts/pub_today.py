"""Publish Aug 19, 2026 — 1 article, no new tools."""
import os; BASE = r"C:\Users\jun\aistudyonline-next"; os.chdir(BASE)

# ---------- Part 1: articles.ts metadata ----------
with open('src/lib/articles.ts', 'r', encoding='utf-8') as f: s = f.read()
a = r"""  {
    slug: "10-must-have-plugins-deepseek-harness-complete-installation-usage-guide",
    title: "10 Must-Have Plugins for DeepSeek Harness: Complete Installation & Usage Guide",
    titleZh: "DeepSeek Harness必备10大插件：完整安装与使用指南",
    description: "Unlock DeepSeek Harness's full potential with 10 essential plugins — UI themes and desktop pets, TUI terminal mode, Feishu integration, architecture diagrams, vibe design, prompt optimization, persistent memory, vision, and multi-agent teams. Exact install commands and usage for each.",
    descriptionZh: "用10个必备插件释放DeepSeek Harness的全部潜力——UI主题与桌面宠物、TUI终端模式、飞书集成、架构图、vibe设计、提示词优化、持久记忆、视觉和多Agent团队。每个插件附精确安装命令与用法。",
    category: "ai-tutorials",
    tags: ["DeepSeek Harness", "Plugins", "AI Agents", "TUI", "Feishu", "Multi-Agent", "Vision", "Memory"],
    difficulty: "intermediate",
    toolsMentioned: ["DeepSeek Harness"],
    date: "2026-08-19",
  },

"""
last = s.rfind('];')
with open('src/lib/articles.ts', 'w', encoding='utf-8') as f: f.write(s[:last] + a + '];')
print('Part 1 done')

# ---------- Part 2: article-content.ts bilingual content ----------
with open('src/lib/article-content.ts', 'r', encoding='utf-8') as f: c = f.read()
n = r'''
  "10-must-have-plugins-deepseek-harness-complete-installation-usage-guide": {
    content: `<div class="meta-banner">
  <span class="meta-badge">📖 AI Tutorial</span>
  <span class="meta-badge">🕒 8 min read</span>
  <span class="meta-badge">📅 Aug 19, 2026</span>
  <span class="meta-badge">🎯 Intermediate</span>
</div>

<h2 id="introduction">Introduction</h2>
<p>DeepSeek Harness (DSH) is a powerful AI agent platform, but its full potential is unlocked only when you install the right plugins. This guide covers 10 essential plugins that will transform your DSH experience, from UI customization to multi-agent collaboration. We'll provide exact installation commands and practical usage instructions for each plugin.</p>

<h2 id="ui-plugins">UI & Experience Enhancement Plugins</h2>

<h3>1. dsh-web-ui-all (Theme & UI Plugin)</h3>
<p>This popular plugin completely transforms DSH's appearance with beautiful themes, desktop pets, and advanced UI features.</p>
<p><strong>Key Features:</strong></p>
<ul>
  <li>Custom themes and skins</li>
  <li>Desktop pets (whale and other characters)</li>
  <li>Real-time token and TPS statistics</li>
  <li>Git graph visualization</li>
  <li>Right-side chat panel</li>
  <li>Mobile remote chat support</li>
</ul>
<p><strong>Installation Command:</strong></p>
<pre><code class="language-bash">dsh plugin --profile web add @linxin66/dsh-web-ui-all</code></pre>
<p><strong>Usage:</strong> After installation, you'll see the desktop pet in the bottom-right corner. Access theme settings through the settings menu to customize your interface.</p>

<h3>2. dsh-tui (Terminal UI Plugin)</h3>
<p>Enables pure TUI (Text User Interface) environment for command-line lovers. Perfect for Linux servers without graphical interfaces.</p>
<p><strong>Installation Commands:</strong></p>
<pre><code class="language-bash">npm install -g @deepseek-ai/dsh @deepseek-harness/tui/
dsh-tui</code></pre>
<p><strong>Usage:</strong> Run <code>dsh-tui</code> in your terminal to enter the command-line programming environment, similar to Claude Code or Codex CLI.</p>

<h3>3. dsh-better-sidebar (Sidebar Plugin)</h3>
<p>Adds a powerful sidebar for real-time project file viewing and navigation.</p>
<p><strong>Installation Command:</strong></p>
<pre><code class="language-bash">dsh plugin --profile web add dsh-better-sidebar@0.12.2</code></pre>
<p><strong>Usage:</strong> The sidebar appears on the left, allowing you to browse files, access command-line tools, view browser pages, and monitor project development results.</p>

<h2 id="productivity-plugins">Productivity & Development Plugins</h2>

<h3>4. dsh-lark-channel (Feishu/Lark Integration)</h3>
<p>Connect DSH with Feishu/Lark for seamless team collaboration.</p>
<p><strong>Installation Commands:</strong></p>
<pre><code class="language-bash">npm install --global dsh-lark-channel@0.0.6
dsh-lark-channel start --profile lark --workspace "SPWD"</code></pre>
<p><strong>Usage:</strong> Scan the QR code to bind your Feishu account. Once connected, you can control DSH through Feishu messages, use commands to switch directories, call skills, and manage tasks.</p>

<h3>5. dsh-archify (Architecture Diagram Generator)</h3>
<p>Automatically generates beautiful architecture diagrams from code repositories.</p>
<p><strong>Installation Command:</strong></p>
<pre><code class="language-bash">dsh plugin --profile web add @tt-all/archify-dsh@0.1.0</code></pre>
<p><strong>Usage:</strong> Simply prompt the plugin to generate architecture diagrams, workflow charts, or sequence diagrams. It outputs interactive HTML with features like section navigation and multi-format export.</p>

<h2 id="performance-plugins">Agent Performance Boost Plugins</h2>

<h3>6. dsh-design (Vibe Design Plugin)</h3>
<p>Open-source alternative to Claude Design for AI-powered design work.</p>
<p><strong>Installation Command:</strong></p>
<pre><code class="language-bash">dsh plugin --profile web add deepseek-design@0.2.2</code></pre>
<p><strong>Usage:</strong> After installation, restart DSH and find the "Design" tab in the conversation window. You can edit designs directly, modify pages, or export as HTML.</p>

<h3>7. dsh-prompt-enhancer (Prompt Optimization)</h3>
<p>Automatically enhances and optimizes your prompts for better agent performance.</p>
<p><strong>Installation Command:</strong></p>
<pre><code class="language-bash">dsh plugin --profile web add github:fsisb/dsh-prompt-enhancer#3.15</code></pre>
<p><strong>Usage:</strong> Write your prompt, then use the plugin to optimize it. You can perform multiple rounds of optimization until you're satisfied.</p>

<h3>8. dsh-openviking (Memory System)</h3>
<p>Adds persistent memory management to DSH agents, making them "smarter" over time.</p>
<p><strong>Installation Commands:</strong></p>
<pre><code class="language-bash">CMAKE_ARGS="-DGGML_METAL=ON" uv tool install --force --python 3.12 --with xhash<4" openviking[local-embed] =0.4.14"
dsh plugin --profile web add @github/volcengine/OpenViking/path=/examples/dsh-memory-plugin</code></pre>
<p><strong>Usage:</strong> The plugin works in the background, remembering your preferences and past interactions. Test it by telling the agent something (e.g., "I like iced American coffee") and then asking it later.</p>

<h3>9. dsh-modlens (Vision Enhancement)</h3>
<p>Adds visual capabilities to DSH agents, allowing them to analyze images.</p>
<p><strong>Installation Commands:</strong></p>
<pre><code class="language-bash">npx -y @deepseek-ai/dsh plugin --profile web add @ilustack/modlens@1.6.6
npx -y @ilustack/modlens config set provider openai
npx -y @ilustack/modlens config set openai.baseurl "https://dashscope.aliyuncs.com/compatible-mode/v1"
npx -y @ilustack/modlens config set openai.model qwen3-vl-plus
export DASHSCOPE_API_KEY="your-api-key"
export OPENAI_API_KEY=$DASHSCOPE_API_KEY</code></pre>
<p><strong>Usage:</strong> Upload images and the agent will analyze them using the visual model.</p>

<h3>10. dsh-agent-teams (Multi-Agent Collaboration)</h3>
<p>Create and manage teams of agents for complex tasks.</p>
<p><strong>Installation Command:</strong></p>
<pre><code class="language-bash">dsh plugin --profile web add @nanmicoder/dsh-agent-teams</code></pre>
<p><strong>Usage:</strong> Describe your task and the plugin will automatically create a team of agents (e.g., product designer, developer, security reviewer) that collaborate to complete the task.</p>

<h2 id="installation">Installation Methods</h2>
<h3>Method 1: Command Line Installation</h3>
<p>Use the <code>dsh plugin</code> commands provided for each plugin.</p>
<h3>Method 2: DSH Studio (Recommended)</h3>
<p>For easier installation, use the official DeepSeek Harness Studio:</p>
<ol>
  <li>Download from GitHub: <a href="https://github.com/deepseek-ai/deepseek-harness-studio">deepseek-harness-studio</a></li>
  <li>Open the plugin market</li>
  <li>Search for plugins</li>
  <li>Click to install with one click</li>
</ol>

<h2 id="final-thoughts">Final Thoughts</h2>
<p>These 10 plugins will transform your DeepSeek Harness experience, making it more powerful, flexible, and enjoyable to use. Whether you're a developer, designer, or AI enthusiast, these tools will help you get the most out of your AI agent platform. For the complete installation commands and project source code, check the video description or visit the official GitHub repository.</p>

<h2>常见问题</h2>

<h3>Do I need to install all 10 plugins at once?</h3>
<p>No. The plugins are independent, so you can install only the ones that fit your workflow. If you live in the terminal, start with dsh-tui and dsh-better-sidebar. If you mostly work in the browser, begin with dsh-web-ui-all for the theme and desktop pet experience. The performance plugins (dsh-design, dsh-prompt-enhancer, dsh-openviking, dsh-modlens, dsh-agent-teams) each add a distinct capability, so install them as you need that capability rather than all upfront.</p>

<h3>Are these plugins free and open source?</h3>
<p>Yes, they are all community plugins in the DeepSeek Harness ecosystem and are free to install. They are managed through the <code>dsh plugin</code> command or DSH Studio, and several are explicit open-source alternatives — dsh-design is described as an open-source alternative to Claude Design, and the source for each project is available on GitHub. The only external dependency is when a plugin needs an API key, such as dsh-modlens using DashScope for the vision model.</p>

<h3>Which plugins give the biggest boost for agent performance?</h3>
<p>For raw capability, dsh-modlens (vision) and dsh-openviking (persistent memory) change what the agent can do, not just how it looks. dsh-prompt-enhancer improves every prompt you feed it, which compounds across tasks. dsh-agent-teams scales single agents into a collaborating team for complex projects. If you had to pick a shortlist: dsh-web-ui-all for the interface, dsh-openviking for memory, and dsh-agent-teams for multi-agent work are the three with the most visible day-to-day impact.</p>

<h3>Do I need to configure plugins after installing them?</h3>
<p>Some yes, some no. Pure UI plugins like dsh-web-ui-all, dsh-tui, and dsh-better-sidebar work right after install. Plugins that call external services need configuration: dsh-lark-channel requires scanning a QR code to bind Feishu, and dsh-modlens needs provider settings plus a DashScope API key. Follow the exact commands in each section above — the configuration steps are part of the install snippet for the plugins that need them.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Want to get the most out of DeepSeek Harness? Continue with these guides:</p>
  <ul>
    <li><a href="/article/deepseek-harness-comprehensive-guide-installation-architecture-practical-usage">DeepSeek Harness: A Comprehensive Guide to Installation, Architecture, and Practical Usage</a> — the foundation guide for the platform these plugins extend</li>
    <li><a href="/article/multi-agent-collaboration-architecture">Multi-Agent Collaboration Architecture</a> — the architecture behind plugin #10's agent teams</li>
    <li><a href="/article/why-agents-need-self-evolution-practical-implementation-guide-ai-agents">Why Agents Need Self-Evolution: Practical Implementation Guide for AI Agents</a> — how memory and reflection make agents smarter, like plugin #8</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">📖 AI教程</span>
  <span class="meta-badge">🕒 阅读约8分钟</span>
  <span class="meta-badge">📅 2026年8月19日</span>
  <span class="meta-badge">🎯 进阶</span>
</div>

<h2 id="introduction">引言</h2>
<p>DeepSeek Harness（DSH）是一个强大的AI Agent平台，但只有安装了正确的插件，它的全部潜力才会被解锁。本指南涵盖10个必备插件，它们将彻底改变你的DSH体验——从UI定制到多Agent协作。我们为每个插件提供精确的安装命令和实用用法说明。</p>

<h2 id="ui-plugins">UI与体验增强插件</h2>

<h3>1. dsh-web-ui-all（主题与UI插件）</h3>
<p>这个热门插件用漂亮的主题、桌面宠物和高级UI功能彻底改变DSH的外观。</p>
<p><strong>核心特性：</strong></p>
<ul>
  <li>自定义主题和皮肤</li>
  <li>桌面宠物（鲸鱼等角色）</li>
  <li>实时token和TPS统计</li>
  <li>Git图谱可视化</li>
  <li>右侧聊天面板</li>
  <li>移动端远程聊天支持</li>
</ul>
<p><strong>安装命令：</strong></p>
<pre><code class="language-bash">dsh plugin --profile web add @linxin66/dsh-web-ui-all</code></pre>
<p><strong>用法：</strong>安装后，你会在右下角看到桌面宠物。通过设置菜单进入主题设置来自定义界面。</p>

<h3>2. dsh-tui（终端UI插件）</h3>
<p>为命令行爱好者提供纯TUI（文本用户界面）环境。非常适合没有图形界面的Linux服务器。</p>
<p><strong>安装命令：</strong></p>
<pre><code class="language-bash">npm install -g @deepseek-ai/dsh @deepseek-harness/tui/
dsh-tui</code></pre>
<p><strong>用法：</strong>在终端运行 <code>dsh-tui</code> 进入命令行编程环境，类似Claude Code或Codex CLI。</p>

<h3>3. dsh-better-sidebar（侧边栏插件）</h3>
<p>添加一个功能强大的侧边栏，用于实时查看和导航项目文件。</p>
<p><strong>安装命令：</strong></p>
<pre><code class="language-bash">dsh plugin --profile web add dsh-better-sidebar@0.12.2</code></pre>
<p><strong>用法：</strong>侧边栏出现在左侧，让你浏览文件、访问命令行工具、查看浏览器页面并监控项目开发结果。</p>

<h2 id="productivity-plugins">生产力与开发插件</h2>

<h3>4. dsh-lark-channel（飞书/Lark集成）</h3>
<p>把DSH与飞书/Lark连接起来，实现无缝的团队协作。</p>
<p><strong>安装命令：</strong></p>
<pre><code class="language-bash">npm install --global dsh-lark-channel@0.0.6
dsh-lark-channel start --profile lark --workspace "SPWD"</code></pre>
<p><strong>用法：</strong>扫描二维码绑定你的飞书账号。连接后，你可以通过飞书消息控制DSH，用命令切换目录、调用技能和管理任务。</p>

<h3>5. dsh-archify（架构图生成器）</h3>
<p>从代码仓库自动生成漂亮的架构图。</p>
<p><strong>安装命令：</strong></p>
<pre><code class="language-bash">dsh plugin --profile web add @tt-all/archify-dsh@0.1.0</code></pre>
<p><strong>用法：</strong>直接提示插件生成架构图、流程图或时序图。它输出交互式HTML，支持章节导航和多格式导出。</p>

<h2 id="performance-plugins">Agent性能提升插件</h2>

<h3>6. dsh-design（Vibe设计插件）</h3>
<p>面向AI驱动设计工作的Claude Design开源替代品。</p>
<p><strong>安装命令：</strong></p>
<pre><code class="language-bash">dsh plugin --profile web add deepseek-design@0.2.2</code></pre>
<p><strong>用法：</strong>安装后重启DSH，在对话窗口找到"Design"标签。你可以直接编辑设计、修改页面或导出为HTML。</p>

<h3>7. dsh-prompt-enhancer（提示词优化）</h3>
<p>自动增强和优化你的提示词，获得更好的Agent性能。</p>
<p><strong>安装命令：</strong></p>
<pre><code class="language-bash">dsh plugin --profile web add github:fsisb/dsh-prompt-enhancer#3.15</code></pre>
<p><strong>用法：</strong>写好提示词，然后用插件优化它。你可以进行多轮优化直到满意为止。</p>

<h3>8. dsh-openviking（记忆系统）</h3>
<p>为DSH Agent添加持久记忆管理，让它们随时间的推移变得更"聪明"。</p>
<p><strong>安装命令：</strong></p>
<pre><code class="language-bash">CMAKE_ARGS="-DGGML_METAL=ON" uv tool install --force --python 3.12 --with xhash<4" openviking[local-embed] =0.4.14"
dsh plugin --profile web add @github/volcengine/OpenViking/path=/examples/dsh-memory-plugin</code></pre>
<p><strong>用法：</strong>插件在后台工作，记住你的偏好和过去的交互。测试方法是告诉Agent一些信息（比如"我喜欢冰美式咖啡"），之后再去问它。</p>

<h3>9. dsh-modlens（视觉增强）</h3>
<p>为DSH Agent添加视觉能力，让它们能够分析图片。</p>
<p><strong>安装命令：</strong></p>
<pre><code class="language-bash">npx -y @deepseek-ai/dsh plugin --profile web add @ilustack/modlens@1.6.6
npx -y @ilustack/modlens config set provider openai
npx -y @ilustack/modlens config set openai.baseurl "https://dashscope.aliyuncs.com/compatible-mode/v1"
npx -y @ilustack/modlens config set openai.model qwen3-vl-plus
export DASHSCOPE_API_KEY="your-api-key"
export OPENAI_API_KEY=$DASHSCOPE_API_KEY</code></pre>
<p><strong>用法：</strong>上传图片，Agent会用视觉模型分析它们。</p>

<h3>10. dsh-agent-teams（多Agent协作）</h3>
<p>为复杂任务创建和管理Agent团队。</p>
<p><strong>安装命令：</strong></p>
<pre><code class="language-bash">dsh plugin --profile web add @nanmicoder/dsh-agent-teams</code></pre>
<p><strong>用法：</strong>描述你的任务，插件会自动创建一个Agent团队（如产品设计师、开发者、安全审查员），协作完成任务。</p>

<h2 id="installation">安装方法</h2>
<h3>方法一：命令行安装</h3>
<p>使用每个插件提供的 <code>dsh plugin</code> 命令。</p>
<h3>方法二：DSH Studio（推荐）</h3>
<p>为了更轻松的安装，使用官方的DeepSeek Harness Studio：</p>
<ol>
  <li>从GitHub下载：<a href="https://github.com/deepseek-ai/deepseek-harness-studio">deepseek-harness-studio</a></li>
  <li>打开插件市场</li>
  <li>搜索插件</li>
  <li>一键点击安装</li>
</ol>

<h2 id="final-thoughts">结语</h2>
<p>这10个插件将改变你的DeepSeek Harness体验，让它更强大、更灵活、更好用。无论你是开发者、设计师还是AI爱好者，这些工具都能帮助你充分发挥AI Agent平台的潜力。完整的安装命令和项目源码，请看视频描述或访问官方GitHub仓库。</p>

<h2>常见问题</h2>

<h3>我需要一次性安装全部10个插件吗？</h3>
<p>不需要。插件彼此独立，你只需要安装契合自己工作流的那些。如果你主要在终端工作，从dsh-tui和dsh-better-sidebar开始。如果你主要在浏览器中工作，先用dsh-web-ui-all体验主题和桌面宠物。性能类插件（dsh-design、dsh-prompt-enhancer、dsh-openviking、dsh-modlens、dsh-agent-teams）各自增加一项独特能力，按需安装即可，不必一次全装。</p>

<h3>这些插件免费且开源吗？</h3>
<p>是的，它们都是DeepSeek Harness生态中的社区插件，免费安装。它们通过 <code>dsh plugin</code> 命令或DSH Studio管理，其中几个是明确的开源替代品——dsh-design被描述为Claude Design的开源替代品，每个项目的源码都在GitHub上可查。唯一的外部依赖是插件需要API密钥时，比如dsh-modlens使用DashScope来调用视觉模型。</p>

<h3>哪些插件对Agent性能提升最大？</h3>
<p>从原始能力看，dsh-modlens（视觉）和dsh-openviking（持久记忆）改变的是Agent能做什么，而不只是看起来怎么样。dsh-prompt-enhancer优化你输入的每个提示词，效果会在任务间累积。dsh-agent-teams把单个Agent扩展成协作文档，应对复杂项目。如果只能选三个：dsh-web-ui-all负责界面、dsh-openviking负责记忆、dsh-agent-teams负责多Agent工作，这三个对日常使用的影响最明显。</p>

<h3>安装插件后还需要配置吗？</h3>
<p>有些要，有些不用。纯UI插件如dsh-web-ui-all、dsh-tui和dsh-better-sidebar安装后立即可用。调用外部服务的插件需要配置：dsh-lark-channel需要扫描二维码绑定飞书，dsh-modlens需要provider设置和DashScope API密钥。请按照上文每节的精确命令操作——需要配置的插件，其配置步骤已经包含在安装片段里。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>想充分发挥DeepSeek Harness的潜力？继续阅读这些指南：</p>
  <ul>
    <li><a href="/article/deepseek-harness-comprehensive-guide-installation-architecture-practical-usage">DeepSeek Harness：安装、架构与实用操作完全指南</a> — 这些插件所扩展平台的基础指南</li>
    <li><a href="/article/multi-agent-collaboration-architecture">多Agent协作架构</a> — 插件#10的Agent团队背后的架构</li>
    <li><a href="/article/why-agents-need-self-evolution-practical-implementation-guide-ai-agents">为什么Agent需要自我进化：实用实现指南</a> — 记忆与反思如何让Agent更聪明，正如插件#8</li>
  </ul>
</div>`,
  },

'''
last = c.rfind('};')
with open('src/lib/article-content.ts', 'w', encoding='utf-8') as f: f.write(c[:last] + n + '};')
print('Part 2 done\n=== Done ===')
