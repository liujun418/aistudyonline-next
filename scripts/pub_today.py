"""Publish Aug 21, 2026 — 1 article (DeepSeek Harness beginner's guide), no new tools."""
import os
BASE = r"C:\Users\jun\aistudyonline-next"
os.chdir(BASE)

# ---------- Part 1: articles.ts ----------
with open('src/lib/articles.ts', 'r', encoding='utf-8') as f:
    s = f.read()

a = r"""  {
    slug: "deepseek-harness-complete-beginners-guide",
    title: "DeepSeek Harness: Complete Beginner's Guide",
    titleZh: "DeepSeek Harness完全入门指南",
    description: "A complete beginner's guide to DeepSeek Harness — installation (quick try + permanent + headless + source build), API key setup, the four working modes, permission levels, plugin management, and creating your first plugin.",
    descriptionZh: "DeepSeek Harness完全入门指南——安装（快速试用+永久+无头+源码构建）、API Key配置、四种工作模式、权限级别、插件管理和创建你的第一个插件。",
    category: "ai-tutorials",
    tags: ["DeepSeek Harness", "AI Agents", "Beginner Guide", "Installation", "Plugins", "Creative Mode", "Node.js"],
    difficulty: "beginner",
    toolsMentioned: ["DeepSeek Harness"],
    date: "2026-08-21",
  },
"""

last = s.rfind('];')
with open('src/lib/articles.ts', 'w', encoding='utf-8', newline='\n') as f:
    f.write(s[:last] + a + '];')
print('Part 1 done')

# ---------- Part 2: article-content.ts ----------
with open('src/lib/article-content.ts', 'r', encoding='utf-8') as f:
    s = f.read()

content = r"""  "deepseek-harness-complete-beginners-guide": {
    content: `<div class="meta-banner">
  <span class="meta-badge">📖 AI Tutorial</span>
  <span class="meta-badge">🕒 7 min read</span>
  <span class="meta-badge">📅 Aug 21, 2026</span>
  <span class="meta-badge">🎯 Beginner</span>
</div>

<h2 id="introduction">Introduction</h2>
<p>DeepSeek Harness is a powerful AI agent framework that lets you create, run, and manage plugins with a unique "write on the spot, run on the spot, no restart needed" workflow. This guide walks you through installation, configuration, and creating your first plugin.</p>

<h2 id="prerequisites">Prerequisites</h2>
<p>Before you begin, ensure you have Node.js 22+ installed on your system. Verify your installation with:</p>
<pre><code class="language-bash">node -v</code></pre>

<h2 id="installation">Installation</h2>
<p>There are two installation methods:</p>

<h3>1. Quick Try (Temporary Use)</h3>
<p>For one-time testing, use the npx command:</p>
<pre><code class="language-bash">npx @deepseek-ai/dsh web</code></pre>
<p>This will start Harness temporarily and open it in your browser at <code>http://127.0.0.1:3030</code>.</p>

<h3>2. Permanent Installation (Recommended)</h3>
<p>For long-term use, install it globally:</p>
<pre><code class="language-bash">npm install -g @deepseek-ai/dsh</code></pre>
<p>After installation, start Harness with:</p>
<pre><code class="language-bash">dsh web</code></pre>

<h2 id="advanced-installation">Advanced Installation Options</h2>

<h3>Headless Mode (For Servers)</h3>
<p>To run Harness on a server without a GUI, use headless mode:</p>
<pre><code class="language-bash"># Set your API key first
export DEEPSEEK_API_KEY=your_api_key

# Run a task in headless mode
dsh --profile headless "your task description"</code></pre>

<h3>Source Code Build (For Developers)</h3>
<p>If you want to modify the source code:</p>
<pre><code class="language-bash"># Clone the repository
git clone https://github.com/deepseek-ai/deepseek-harness.git
cd deepseek-harness

# Install dependencies
pnpm install

# Build the project
pnpm run build

# Run the web interface
pnpm run web

# Or run in headless mode
pnpm dsh --profile headless "your task"</code></pre>

<h2 id="configuration">Configuration</h2>

<h3>Setting Up Your API Key</h3>
<ol>
  <li>Open the Harness settings panel</li>
  <li>Navigate to the "Model" section</li>
  <li>Enter your DeepSeek API key</li>
  <li>Save the configuration</li>
</ol>
<p>Your API key will be stored in a secure credentials file with 0600 permissions, ensuring other users cannot access it.</p>

<h3>Adding Model Providers</h3>
<p>Harness supports multiple model providers, not just DeepSeek. To add a new provider:</p>
<ol>
  <li>Go to Settings &gt; Model Providers</li>
  <li>Click "Add Provider"</li>
  <li>Enter the provider details and API key</li>
  <li>Save the configuration</li>
</ol>

<h2 id="working-modes">Working Modes</h2>
<p>Harness offers four working modes:</p>

<h3>1. Standard Mode</h3>
<ul>
  <li>Full-featured agent</li>
  <li>Supports files, terminals, browsers, and skills</li>
  <li>90% of your work will be done in this mode</li>
</ul>

<h3>2. Minimal Mode</h3>
<ul>
  <li>Only two tools: terminal and file editor</li>
  <li>Shortest prompts</li>
  <li>Used for benchmarking and testing</li>
</ul>

<h3>3. PTC Mode</h3>
<ul>
  <li>Optimized for token efficiency</li>
  <li>Combines multiple operations into a single script</li>
  <li>Suitable for advanced users concerned about cost</li>
</ul>

<h3>4. Creative Mode</h3>
<ul>
  <li>Adds additional tools for plugin development</li>
  <li>Allows reading and modifying runtime state</li>
  <li>Used for writing and testing plugins on the fly</li>
</ul>

<h2 id="permission-levels">Permission Levels</h2>
<p>Harness provides three permission levels to control file access:</p>
<ol>
  <li><strong>Read Only</strong>: Safest option, no file modifications allowed</li>
  <li><strong>Workspace Write</strong> (Default): Only modifies files in your specified workspace directory</li>
  <li><strong>Full Access</strong>: Complete system access (use with caution)</li>
</ol>

<h2 id="plugin-management">Plugin Management</h2>

<h3>Finding Plugins</h3>
<p>Browse thousands of community plugins on GitHub by searching for the "dsh plugin" tag.</p>

<h3>Installing Plugins</h3>
<p>Install plugins using the command line:</p>
<pre><code class="language-bash">dsh plugin --profile demo add ./path/to/plugin</code></pre>
<p>Or let Harness install plugins for you through the chat interface.</p>

<h3>Important Notes</h3>
<ul>
  <li>The v0.1 ecosystem is still young, so some plugins may be untested</li>
  <li>Always check the plugin documentation before installation</li>
  <li>Uninstalling plugins is clean and reversible</li>
</ul>

<h2 id="first-plugin">Creating Your First Plugin</h2>
<p>Harness's unique "write on the spot" workflow allows you to create and test plugins in real-time:</p>
<ol>
  <li>Switch to Creative Mode</li>
  <li>Describe your plugin idea in natural language</li>
  <li>Harness will generate the plugin code</li>
  <li>Test the plugin immediately without restarting</li>
  <li>Refine and iterate as needed</li>
</ol>
<p>For permanent plugins, follow the official development workflow to package and distribute your plugin.</p>

<h2 id="conclusion">Conclusion</h2>
<p>DeepSeek Harness provides a unique and powerful platform for AI agent development. With its intuitive interface, flexible plugin system, and innovative "write on the spot" workflow, it's an excellent choice for both beginners and experienced developers. Start with the standard mode to get familiar with the interface, then explore the advanced features and plugin development capabilities as you become more comfortable.</p>

<h2>常见问题</h2>

<h3>Is DeepSeek Harness free to use?</h3>
<p>Yes, DeepSeek Harness itself is free and open source (MIT license), and you can run it locally with the npx or npm install commands in this guide. What you pay for is model usage — you need a DeepSeek API key to power the agent, and those API costs are billed by DeepSeek. The framework itself does not charge anything.</p>

<h3>What's the difference between Quick Try and permanent installation?</h3>
<p>Quick Try (<code>npx @deepseek-ai/dsh web</code>) runs Harness temporarily from the npm cache — perfect for testing whether the tool fits your workflow before committing. It starts a local web interface at <code>http://127.0.0.1:3030</code>. Permanent installation (<code>npm install -g @deepseek-ai/dsh</code>) puts the <code>dsh</code> command on your PATH globally, so you can start it anytime with <code>dsh web</code>. For daily use, install permanently.</p>

<h3>Which working mode should I start with?</h3>
<p>Start with Standard Mode — it's the full-featured agent with files, terminals, browsers, and skills, and handles roughly 90% of real work. Move to Minimal Mode when you're benchmarking or testing. Use PTC Mode if you're cost-sensitive and want token-efficient operation. Switch to Creative Mode specifically when you want to write and test plugins on the fly without restarting.</p>

<h3>Are the permission levels safe?</h3>
<p>Yes, and that's the point. Read Only is the safest — no file modifications at all. Workspace Write (the default) restricts changes to your specified workspace directory, so the agent can't touch anything outside your project. Full Access gives complete system access and should be used with caution — only enable it when you trust the task and the agent completely.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Ready to go deeper with DeepSeek Harness? Continue with these guides:</p>
  <ul>
    <li><a href="/article/deepseek-harness-comprehensive-guide-installation-architecture-practical-usage">DeepSeek Harness: A Comprehensive Guide to Installation, Architecture, and Practical Usage</a> — the deep dive into architecture and real-world use behind this beginner guide</li>
    <li><a href="/article/10-must-have-plugins-deepseek-harness-complete-installation-usage-guide">10 Must-Have Plugins for DeepSeek Harness: Complete Installation &amp; Usage Guide</a> — once you've installed Harness, add these 10 essential plugins</li>
    <li><a href="/article/opencode-desktop-complete-beginners-guide">OpenCode Desktop: A Complete Beginner's Guide</a> — another open-source AI coding agent worth comparing with DeepSeek Harness</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">📖 AI教程</span>
  <span class="meta-badge">🕒 阅读约7分钟</span>
  <span class="meta-badge">📅 2026年8月21日</span>
  <span class="meta-badge">🎯 入门</span>
</div>

<h2 id="introduction">引言</h2>
<p>DeepSeek Harness是一个强大的AI Agent框架，它支持一种独特的"即写即跑、无需重启"的工作流来创建、运行和管理插件。本指南将带你完成安装、配置和创建第一个插件。</p>

<h2 id="prerequisites">前置要求</h2>
<p>开始之前，请确保你的系统已安装Node.js 22+。用以下命令验证安装：</p>
<pre><code class="language-bash">node -v</code></pre>

<h2 id="installation">安装</h2>
<p>有两种安装方式：</p>

<h3>1. 快速试用（临时使用）</h3>
<p>单次测试用npx命令：</p>
<pre><code class="language-bash">npx @deepseek-ai/dsh web</code></pre>
<p>这会临时启动Harness，并在浏览器中打开<code>http://127.0.0.1:3030</code>。</p>

<h3>2. 永久安装（推荐）</h3>
<p>长期使用请全局安装：</p>
<pre><code class="language-bash">npm install -g @deepseek-ai/dsh</code></pre>
<p>安装后，用以下命令启动Harness：</p>
<pre><code class="language-bash">dsh web</code></pre>

<h2 id="advanced-installation">高级安装选项</h2>

<h3>无头模式（用于服务器）</h3>
<p>要在没有图形界面的服务器上运行Harness，请使用无头模式：</p>
<pre><code class="language-bash"># 先设置你的API Key
export DEEPSEEK_API_KEY=your_api_key

# 以无头模式运行任务
dsh --profile headless "你的任务描述"</code></pre>

<h3>源码构建（适用于开发者）</h3>
<p>如果你想修改源代码：</p>
<pre><code class="language-bash"># 克隆仓库
git clone https://github.com/deepseek-ai/deepseek-harness.git
cd deepseek-harness

# 安装依赖
pnpm install

# 构建项目
pnpm run build

# 运行Web界面
pnpm run web

# 或以无头模式运行
pnpm dsh --profile headless "你的任务"</code></pre>

<h2 id="configuration">配置</h2>

<h3>设置你的API Key</h3>
<ol>
  <li>打开Harness设置面板</li>
  <li>进入"Model"（模型）部分</li>
  <li>输入你的DeepSeek API Key</li>
  <li>保存配置</li>
</ol>
<p>你的API Key会存储在权限为0600的安全凭据文件中，确保其他用户无法访问。</p>

<h3>添加模型供应商</h3>
<p>Harness支持多种模型供应商，不只是DeepSeek。要添加新供应商：</p>
<ol>
  <li>进入设置 &gt; Model Providers（模型供应商）</li>
  <li>点击"Add Provider"（添加供应商）</li>
  <li>输入供应商信息和API Key</li>
  <li>保存配置</li>
</ol>

<h2 id="working-modes">工作模式</h2>
<p>Harness提供四种工作模式：</p>

<h3>1. 标准模式</h3>
<ul>
  <li>全功能Agent</li>
  <li>支持文件、终端、浏览器和技能</li>
  <li>90%的工作都在此模式完成</li>
</ul>

<h3>2. 极简模式</h3>
<ul>
  <li>只有两个工具：终端和文件编辑器</li>
  <li>提示词最短</li>
  <li>用于基准测试和测试</li>
</ul>

<h3>3. PTC模式</h3>
<ul>
  <li>针对token效率优化</li>
  <li>把多个操作合并到单个脚本中</li>
  <li>适合关注成本的进阶用户</li>
</ul>

<h3>4. 创意模式</h3>
<ul>
  <li>为插件开发添加额外工具</li>
  <li>允许读取和修改运行时状态</li>
  <li>用于即时编写和测试插件</li>
</ul>

<h2 id="permission-levels">权限级别</h2>
<p>Harness提供三个权限级别来控制文件访问：</p>
<ol>
  <li><strong>只读（Read Only）</strong>：最安全选项，不允许任何文件修改</li>
  <li><strong>工作区写入（Workspace Write）</strong>（默认）：只修改你指定工作区目录中的文件</li>
  <li><strong>完全访问（Full Access）</strong>：完整系统访问权限（请谨慎使用）</li>
</ol>

<h2 id="plugin-management">插件管理</h2>

<h3>查找插件</h3>
<p>在GitHub上搜索"dsh plugin"标签，浏览数千个社区插件。</p>

<h3>安装插件</h3>
<p>用命令行安装插件：</p>
<pre><code class="language-bash">dsh plugin --profile demo add ./path/to/plugin</code></pre>
<p>或者通过聊天界面让Harness帮你安装插件。</p>

<h3>重要提示</h3>
<ul>
  <li>v0.1生态还很年轻，部分插件可能未经测试</li>
  <li>安装前务必查看插件文档</li>
  <li>卸载插件是干净且可逆的</li>
</ul>

<h2 id="first-plugin">创建你的第一个插件</h2>
<p>Harness独特的"即写即跑"工作流让你能实时创建和测试插件：</p>
<ol>
  <li>切换到创意模式</li>
  <li>用自然语言描述你的插件想法</li>
  <li>Harness会生成插件代码</li>
  <li>无需重启即可立即测试插件</li>
  <li>按需优化和迭代</li>
</ol>
<p>对于要长期使用的插件，请遵循官方开发流程来打包和分发。</p>

<h2 id="conclusion">结语</h2>
<p>DeepSeek Harness为AI Agent开发提供了一个独特而强大的平台。凭借其直观的界面、灵活的插件系统和创新的"即写即跑"工作流，无论新手还是经验丰富的开发者，它都是绝佳选择。先从标准模式熟悉界面，再逐步探索高级特性和插件开发能力。</p>

<h2>常见问题</h2>

<h3>DeepSeek Harness免费吗？</h3>
<p>是的，DeepSeek Harness本身免费且开源（MIT协议），你可以用本文中的npx或npm install命令在本地运行。需要付费的是模型使用——你需要一个DeepSeek API Key来驱动Agent，这些API费用由DeepSeek收取。框架本身不收取任何费用。</p>

<h3>快速试用和永久安装有什么区别？</h3>
<p>快速试用（<code>npx @deepseek-ai/dsh web</code>）从npm缓存临时运行Harness，适合在决定长期使用前先测试它是否适合你的工作流。它会在<code>http://127.0.0.1:3030</code>启动一个本地Web界面。永久安装（<code>npm install -g @deepseek-ai/dsh</code>）会把<code>dsh</code>命令全局加入PATH，之后随时用<code>dsh web</code>启动。日常使用请永久安装。</p>

<h3>我应该先使用哪种工作模式？</h3>
<p>先用标准模式——它是支持文件、终端、浏览器和技能的全功能Agent，能处理约90%的真实工作。做基准测试或测试时切换到极简模式。如果你在意成本，用针对token效率优化的PTC模式。只有在想即时编写和测试插件时，才切换到创意模式。</p>

<h3>权限级别安全吗？</h3>
<p>安全，这正是它的设计目的。只读（Read Only）最安全——完全不允许修改文件。工作区写入（默认）把更改限制在你指定的工作区目录内，Agent无法触碰项目之外的东西。完全访问（Full Access）给予完整系统权限，必须谨慎使用——只有当你完全信任任务和Agent时才启用它。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>想深入探索DeepSeek Harness？继续阅读这些指南：</p>
  <ul>
    <li><a href="/article/deepseek-harness-comprehensive-guide-installation-architecture-practical-usage">DeepSeek Harness：安装、架构与实用操作完全指南</a> — 本入门指南背后的架构与实战深度解析</li>
    <li><a href="/article/10-must-have-plugins-deepseek-harness-complete-installation-usage-guide">DeepSeek Harness必备10大插件：完整安装与使用指南</a> — 安装好Harness后，添加这10个必备插件</li>
    <li><a href="/article/opencode-desktop-complete-beginners-guide">OpenCode Desktop完全入门指南</a> — 另一款值得与DeepSeek Harness对比的开源AI编码Agent</li>
  </ul>
</div>`,
  },
"""

last = s.rfind('};')
with open('src/lib/article-content.ts', 'w', encoding='utf-8', newline='\n') as f:
    f.write(s[:last] + content + '};')
print('Part 2 done')

print('ALL DONE')
