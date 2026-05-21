const es = "<p>[Spanish version — pending translation]</p>";
const ar = "<p>[Arabic version — pending translation]</p>";

export const articleContents: Record<string, { content: string; contentEs: string; contentAr: string }> = {
  // ====== Sample: Claude Code Installation (Path: Claude Code × 4, Part 1) ======
  "claude-code-install-setup": {
    content: `<div class="article-meta-banner">
<p><strong>Learning Path:</strong> Claude Code 编程入门 · <strong>Part 1 of 4</strong></p>
<p><strong>Prerequisites:</strong> 一台电脑（Windows/Mac/Linux）、基本命令行操作能力（会用 <code>cd</code> 和 <code>ls</code> 即可）</p>
<p><strong>What you'll build:</strong> 一个可运行的 Claude Code 开发环境，能通过命令行直接调用 Claude 写代码。</p>
</div>

<h2>What is Claude Code?</h2>

<p>Claude Code 是 Anthropic 推出的命令行 AI 编程工具。和 Cursor、GitHub Copilot 不同，它不需要打开 IDE——直接在终端里输入自然语言，Claude 就能读你的代码库、写代码、修 bug、解释逻辑。它最独特的能力是<strong>理解整个项目结构</strong>，而不是只处理当前打开的文件。</p>

<p>在正式开始之前，你需要知道三件事：</p>

<ol>
<li>Claude Code 需要 <strong>Anthropic API Key</strong>（付费），不是 Claude.ai 的网页版订阅。两者独立。</li>
<li>它是<strong>命令行工具</strong>，运行在终端里，没有图形界面。别担心——你不会被要求写任何代码来使用它。</li>
<li>它会<strong>读取和修改你的文件</strong>。建议在测试项目里先试用，不要一上来就在公司代码库里跑。</li>
</ol>

<h2>Step 1: Install Node.js 18+</h2>

<p>Claude Code 基于 Node.js。如果你的电脑上还没有 Node.js，先装它。</p>

<div class="step-card">

<h3>Windows</h3>
<p>去 <a href="https://nodejs.org" target="_blank" rel="noopener">nodejs.org</a>，下载 LTS 版本（推荐 20.x 或 22.x）。运行安装程序，全部默认选项，一路 Next 到底。</p>

<p>安装完成后，打开 <strong>PowerShell</strong>（按 Win 键，输入 PowerShell，回车），验证安装：</p>

<pre><code>node --version
# 应该输出: v20.x.x 或 v22.x.x

npm --version
# 应该输出: 10.x.x</code></pre>
</div>

<div class="step-card">

<h3>Mac</h3>
<p>推荐用 Homebrew。如果你没装过 Homebrew，先打开 <strong>终端（Terminal）</strong> 运行：</p>

<pre><code>/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"</code></pre>

<p>然后安装 Node.js：</p>

<pre><code>brew install node@22</code></pre>

<p>验证安装：</p>

<pre><code>node --version
npm --version</code></pre>
</div>

<div class="step-card">

<h3>Linux (Ubuntu/Debian)</h3>

<pre><code>curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt-get install -y nodejs</code></pre>

<p>验证：</p>

<pre><code>node --version
npm --version</code></pre>
</div>

<h2>Step 2: Get Your Anthropic API Key</h2>

<p>这步容易搞混。你需要的是 <strong>API Key</strong>，不是 Claude.ai 的网页版账号。</p>

<ol>
<li>打开 <a href="https://console.anthropic.com" target="_blank" rel="noopener">console.anthropic.com</a></li>
<li>注册或登录（可以用 Google 账号）</li>
<li>首次使用需要绑定信用卡，设置消费限额（建议先设 $20/月）</li>
<li>左侧菜单 → <strong>API Keys</strong> → 点击 <strong>Create Key</strong></li>
<li>给 key 起个名字（比如 "claude-code-laptop"）→ 复制生成的 key</li>
</ol>

<div class="warning-box">
<p><strong>⚠️ 重要：</strong>Key 只显示一次。关闭页面后无法再次查看。请立即保存到安全的地方（密码管理器、文本文件都行，不要贴到聊天记录里）。</p>
</div>

<h2>Step 3: Install Claude Code</h2>

<p>打开终端（Windows: PowerShell。Mac: Terminal。Linux: Terminal），运行：</p>

<pre><code>npm install -g @anthropic-ai/claude-code</code></pre>

<p>这条命令做了什么：<code>npm install -g</code> 是"全局安装"，安装后你可以在任何目录里使用 <code>claude</code> 命令。<code>@anthropic-ai/claude-code</code> 是 Claude Code 的包名。</p>

<p>安装过程大约 30-60 秒。你可能会看到一些 warning 信息，只要最后没有红色的 <code>ERROR</code>，就可以继续。</p>

<p>验证安装成功：</p>

<pre><code>claude --version
# 应该输出类似: v1.x.x</code></pre>

<h2>Step 4: 配置 API Key</h2>

<p>有两种方式告诉 Claude Code 你的 API Key。推荐方式一：</p>

<div class="step-card">
<p><strong>方式一（推荐）：环境变量</strong>——将 key 设为系统环境变量，所有项目生效：</p>

<h3>Windows (PowerShell, 管理员模式)</h3>

<pre><code>[Environment]::SetEnvironmentVariable('ANTHROPIC_API_KEY', 'sk-ant-api03-your-key-here', 'User')</code></pre>

<p>把 <code>sk-ant-api03-your-key-here</code> 替换成你的真实 key。关闭并重新打开 PowerShell 使其生效。</p>

<h3>Mac / Linux (Terminal)</h3>

<pre><code># 添加到 shell 配置文件中（zsh 用户用 .zshrc，bash 用户用 .bashrc）
echo 'export ANTHROPIC_API_KEY="sk-ant-api03-your-key-here"' >> ~/.zshrc

# 立即生效
source ~/.zshrc</code></pre>
</div>

<div class="step-card">
<p><strong>方式二：项目级配置</strong>——只在当前项目中生效，适用于多个项目用不同 key 的情况：</p>

<pre><code># 在项目根目录创建 .env 文件
echo 'ANTHROPIC_API_KEY=sk-ant-api03-your-key-here' > .env</code></pre>

<p>Claude Code 启动时会自动读取 <code>.env</code> 文件。</p>
</div>

<h2>Step 5: 测试你的第一个 Claude Code 命令</h2>

<p>创建一个测试项目目录，然后启动 Claude Code：</p>

<pre><code># 创建测试目录
mkdir claude-test && cd claude-test

# 初始化 git（Claude Code 需要 git 来跟踪代码变更）
git init

# 启动 Claude Code
claude</code></pre>

<p>第一次启动时，Claude Code 可能会问你是否同意使用条款。输入 <code>y</code> 确认。</p>

<p>看到交互式界面后，输入你的第一个指令：</p>

<pre><code>创建一个简单的 HTML 文件 index.html，内容是一个现代化的"Hello World"页面，有居中的文字和好看的背景色。</code></pre>

<p>Claude 会：</p>

<ol>
<li>分析你的请求</li>
<li>生成代码</li>
<li>显示它打算做什么（可能需要你按 Enter 确认）</li>
<li>创建文件</li>
</ol>

<p>完成后，在浏览器中打开 <code>index.html</code> 查看结果。</p>

<h2>常见问题</h2>

<h3>Q: 提示 "API key not found"</h3>
<p>检查环境变量是否正确设置。运行 <code>echo $ANTHROPIC_API_KEY</code>（Mac/Linux）或 <code>$env:ANTHROPIC_API_KEY</code>（PowerShell）查看当前值。如果为空，回到 Step 4 重新设置。</p>

<h3>Q: 提示 "Insufficient permissions"</h3>
<p>去 <a href="https://console.anthropic.com/settings/billing" target="_blank" rel="noopener">Anthropic Console → Billing</a> 检查：账户余额是否 >$0、是否已绑定信用卡、消费限额是否用完。</p>

<h3>Q: 安装很慢或失败</h3>
<p>这是 npm 网络问题。尝试使用国内镜像：</p>

<pre><code>npm config set registry https://registry.npmmirror.com
npm install -g @anthropic-ai/claude-code
# 安装完成后恢复默认
npm config set registry https://registry.npmjs.org</code></pre>

<h3>Q: Claude Code 和 Cursor / Copilot 有什么区别？</h3>
<p>Claude Code 是<strong>命令行工具</strong>，适合快速改项目、自动化任务、在终端里直接操作。Cursor 是<strong>IDE</strong>（编辑器），适合边写代码边用 AI 辅助。Copilot 是<strong>IDE 插件</strong>，适合在已有编辑器里自动补全。实际工作中三者可以配合使用。</p>

<div class="next-step">
<p><strong>Next in this path:</strong> <a href="/article/claude-code-mcp-configuration">Part 2: Claude Code 环境配置与 MCP 工具集成 →</a></p>
</div>`,
    contentEs: es, contentAr: ar,
  },

  // ====== Existing 25 articles (to be rewritten per new standards) ======
  "llms-in-plain-english": {
    content: `<p>[This article will be rewritten to the new standards — with concrete examples, comparison tables, and copyable key takeaways.]</p>`,
    contentEs: es, contentAr: ar,
  },
  // ... remaining articles stub for build compatibility
  "ai-hallucinations-explained-with-examples": { content: "<p>[Rewriting in progress]</p>", contentEs: es, contentAr: ar },
  "free-vs-paid-ai-tools-worth-it": { content: "<p>[Rewriting in progress]</p>", contentEs: es, contentAr: ar },
  "what-is-a-gpu-non-techie": { content: "<p>[Rewriting in progress]</p>", contentEs: es, contentAr: ar },
  "ai-myths-people-still-believe": { content: "<p>[Rewriting in progress]</p>", contentEs: es, contentAr: ar },
  "chatgpt-voice-mode-job-interview": { content: "<p>[Rewriting in progress]</p>", contentEs: es, contentAr: ar },
  "claude-projects-organize-chats": { content: "<p>[Rewriting in progress]</p>", contentEs: es, contentAr: ar },
  "ai-images-that-dont-look-like-ai": { content: "<p>[Rewriting in progress]</p>", contentEs: es, contentAr: ar },
  "voice-recording-to-meeting-notes-free": { content: "<p>[Rewriting in progress]</p>", contentEs: es, contentAr: ar },
  "first-ai-coding-project-no-experience": { content: "<p>[Rewriting in progress]</p>", contentEs: es, contentAr: ar },
  "etsy-seller-ai-product-descriptions": { content: "<p>[Rewriting in progress]</p>", contentEs: es, contentAr: ar },
  "ai-wedding-planning-free-tools": { content: "<p>[Rewriting in progress]</p>", contentEs: es, contentAr: ar },
  "ai-travel-itinerary-real-prompts": { content: "<p>[Rewriting in progress]</p>", contentEs: es, contentAr: ar },
  "learn-english-with-ai-free-speaking-practice": { content: "<p>[Rewriting in progress]</p>", contentEs: es, contentAr: ar },
  "ai-for-parents-quiet-moments": { content: "<p>[Rewriting in progress]</p>", contentEs: es, contentAr: ar },
  "free-ai-image-generators-same-prompt-test": { content: "<p>[Rewriting in progress]</p>", contentEs: es, contentAr: ar },
  "chatgpt-free-vs-plus-2026-what-you-get": { content: "<p>[Rewriting in progress]</p>", contentEs: es, contentAr: ar },
  "notebooklm-vs-perplexity-research": { content: "<p>[Rewriting in progress]</p>", contentEs: es, contentAr: ar },
  "claude-vs-chatgpt-writing-blind-test": { content: "<p>[Rewriting in progress]</p>", contentEs: es, contentAr: ar },
  "cursor-vs-copilot-complete-beginner": { content: "<p>[Rewriting in progress]</p>", contentEs: es, contentAr: ar },
  "gpt5-for-regular-users": { content: "<p>[Rewriting in progress]</p>", contentEs: es, contentAr: ar },
  "open-source-ai-models-run-on-laptop": { content: "<p>[Rewriting in progress]</p>", contentEs: es, contentAr: ar },
  "eu-ai-act-plain-english": { content: "<p>[Rewriting in progress]</p>", contentEs: es, contentAr: ar },
  "ai-jobs-that-didnt-exist-3-years-ago": { content: "<p>[Rewriting in progress]</p>", contentEs: es, contentAr: ar },
  "apple-intelligence-6-months-later": { content: "<p>[Rewriting in progress]</p>", contentEs: es, contentAr: ar },
};
