"""
Publish June 18, 2026 articles.
0 new tools needed — all referenced tools already exist in tools.ts.
"""

import os

BASE = r"C:\Users\jun\aistudyonline-next"
os.chdir(BASE)

# ===== Part 1: Add 2 article metadata to articles.ts =====
with open('src/lib/articles.ts', 'r', encoding='utf-8') as f:
    articles_src = f.read()

new_articles = r"""  {
    slug: "open-source-claude-design-local-deploy",
    title: "Open-Source Claude Design Local Deployment Guide: Free Self-Hosted AI UI Design Tool",
    titleZh: "开源Claude Design本地部署指南：免费自托管AI UI设计工具",
    description: "A complete guide to deploying the open-source Claude Design locally on your PC for unlimited, free AI-powered UI design generation — covering environment setup, model configuration, and common pitfalls.",
    descriptionZh: "在本地PC上部署开源Claude Design的完整指南——实现无限免费AI界面设计生成，涵盖环境配置、模型对接和常见问题解决。",
    category: "ai-tutorials",
    tags: ["claude-design", "self-hosted", "open-source", "ollama", "deployment", "beginner"],
    difficulty: "beginner",
    toolsMentioned: ["ollama", "claude-design"],
    date: "2026-06-18",
  },
  {
    slug: "one-claude-code-two-roles",
    title: "One Claude Code, Two Roles: Code Writing and Reviewing Without Codex",
    titleZh: "一个Claude Code，两种角色：无需Codex也能写代码和审代码",
    description: "Learn how to use a single Claude Code model to both write and review code by leveraging isolated contexts and a dedicated code-review agent — no Codex required.",
    descriptionZh: "学习如何通过隔离上下文和专用代码审查代理，用一个Claude Code模型同时完成代码编写和审查——无需Codex。",
    category: "ai-tutorials",
    tags: ["claude-code", "code-review", "agent", "productivity", "workflow"],
    difficulty: "intermediate",
    toolsMentioned: ["claude", "codex"],
    date: "2026-06-18",
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

article1_content = r"""
  // ====== Article: Open-Source Claude Design Local Deployment ======
  "open-source-claude-design-local-deploy": {
    content: `
<div class="meta-banner">
  <span>📅 2026-06-18</span>
  <span>📂 <a href="/en/learn/ai-tutorials">AI Tutorials</a></span>
  <span>⏱️ 8 min read</span>
  <span>🔰 Beginner</span>
</div>

<p>Most creators only use the official cloud version of <a href="/en/tools/claude-design">Claude Design</a> with strict rate limits and paid subscriptions. Few people know there is a fully open-source replica of Claude Design that you can deploy locally on your PC for unlimited design generation without network restrictions or billing fees. This tutorial covers complete environment setup, source code deployment, model docking, and common troubleshooting for self-hosted open-source Claude Design, with executable code blocks for every step.</p>

<h2>1. Core Advantages of Self-Hosted Open-Source Claude Design</h2>

<ol>
<li><strong>Unlimited generation</strong>: No daily request caps, no token billing for local operation.</li>
<li><strong>Data privacy</strong>: All design drafts, prompts, and image assets are stored locally without uploading to third-party servers.</li>
<li><strong>Custom model docking</strong>: Compatible with local open-source vision models, <a href="/en/tools/ollama">Ollama</a>, and remote LLM APIs.</li>
<li><strong>Customizable functions</strong>: Modify source code to add brand templates, batch export, and team collaborative modules.</li>
<li><strong>Low hardware threshold</strong>: Runs smoothly on consumer GPUs with 8GB VRAM, even compatible with CPU-only deployment.</li>
</ol>

<h2>2. Pre-Deployment Environment Preparation</h2>

<h3>2.1 Dependencies Installation</h3>

<p>The open-source project relies on Python 3.10+, Git, and Node.js. Run the following installation commands based on your operating system.</p>

<p><strong>Windows (PowerShell Administrator):</strong></p>

<pre><code class="language-powershell"># Install winget dependencies
winget install Python.Python.3.10 Git.Git OpenJS.NodeJS.LTS
# Verify installation versions
python --version
git --version
node -v
npm -v</code></pre>

<p><strong>macOS (Terminal):</strong></p>

<pre><code class="language-bash"># Install Homebrew if missing
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# Install required runtime
brew install python@3.10 git node</code></pre>

<p><strong>Linux Ubuntu/Debian:</strong></p>

<pre><code class="language-bash">sudo apt update && sudo apt install python3.10 python3-pip git nodejs npm -y</code></pre>

<h3>2.2 GPU Acceleration Setup (Recommended)</h3>

<p>If you have an NVIDIA graphics card, install CUDA toolkit to speed up image rendering:</p>

<pre><code class="language-bash"># Install PyTorch with CUDA support
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121</code></pre>

<h2>3. Clone Open-Source Repository & Install Project Dependencies</h2>

<h3>3.1 Pull Source Code</h3>

<p>Create an empty folder and clone the official open-source repo:</p>

<pre><code class="language-bash"># Create working directory
mkdir claude-design-local && cd claude-design-local
# Clone source repository
git clone https://github.com/open-claude-design/claude-design.git
cd claude-design</code></pre>

<h3>3.2 Backend Python Dependencies Installation</h3>

<pre><code class="language-bash"># Create independent virtual environment to avoid version conflicts
python3 -m venv venv
# Activate virtual env (Windows)
venv\\Scripts\\activate
# Activate virtual env (macOS/Linux)
source venv/bin/activate
# Install all backend requirements
pip install -r requirements.txt</code></pre>

<h3>3.3 Frontend Web Build</h3>

<pre><code class="language-bash"># Enter frontend folder
cd web
# Install npm packages
npm install
# Build static frontend files
npm run build</code></pre>

<h2>4. Model Configuration: Docking Local & Remote Vision Models</h2>

<p>Open-source Claude Design does not embed models by default; you need to configure model access in the config file.</p>

<h3>4.1 Modify Core Configuration File</h3>

<pre><code class="language-bash"># Open configuration file for editing
cp config.example.yaml config.yaml</code></pre>

<p>Edit <code>config.yaml</code> to set model source. Sample <a href="/en/tools/ollama">Ollama</a> local model configuration:</p>

<pre><code class="language-yaml">model_provider: ollama
vision_model: llama3.2-vision:11b
api_base: http://127.0.0.1:11434
api_key: dummy-key
max_image_size: 1024
render_batch: 4</code></pre>

<h3>4.2 Pull Local Vision Model via Ollama</h3>

<p>If using Ollama as model backend, run this command to download the vision model before launching the service:</p>

<pre><code class="language-bash">ollama pull llama3.2-vision:11b</code></pre>

<h2>5. Launch Local Service & Access Web UI</h2>

<h3>5.1 Start Backend Service</h3>

<p>Keep the virtual environment activated and execute:</p>

<pre><code class="language-bash"># Launch backend API service
python main.py --host 0.0.0.0 --port 7890</code></pre>

<h3>5.2 Access Design Panel</h3>

<p>Open your browser and visit <code>http://127.0.0.1:7890</code> — the fully functional open-source <a href="/en/tools/claude-design">Claude Design</a> interface will load. You can input UI design prompts, upload reference sketches, generate page layouts, and export PNG/SVG design files locally without any network limits.</p>

<p>Sample practical design prompt you can directly input in the local tool:</p>

<pre><code class="language-text">Design a minimalist AI tool landing page, mobile-first layout, blue tech tone, include feature card section, download button and footer copyright. Output clean Figma-style layered design.</code></pre>

<h2>6. Common Beginner Pitfalls & Fix Commands</h2>

<h3>Pitfall 1: Port 7890 Occupied, Service Startup Failed</h3>

<p>Check occupied port and kill process:</p>

<pre><code class="language-powershell"># Windows
netstat -ano | findstr "7890"
taskkill /F /PID [target-PID-number]</code></pre>

<pre><code class="language-bash"># macOS/Linux
lsof -i :7890
kill -9 [process-id]</code></pre>

<h3>Pitfall 2: Image Generation Black Screen, Model Connection Error</h3>

<p>Restart Ollama and reload service:</p>

<pre><code class="language-bash">ollama stop llama3.2-vision:11b
ollama start
# Rerun backend
python main.py</code></pre>

<h3>Pitfall 3: Frontend Page Blank After npm Build</h3>

<p>Reinstall frontend dependencies:</p>

<pre><code class="language-bash">cd web
rm -rf node_modules package-lock.json
npm install && npm run build</code></pre>

<h2>7. Advanced Optimization for Long-Term Use</h2>

<ol>
<li><strong>Auto-start service on system boot</strong>: Write a simple startup script to run backend automatically after PC startup.</li>
<li><strong>Batch export script</strong>: Add a Python script to mass export all generated design drafts to a local folder:</li>
</ol>

<pre><code class="language-python"># Batch export all design drafts example
import os
import shutil

export_dir = "./export_designs"
source_dir = "./static/output"
os.makedirs(export_dir, exist_ok=True)

for file in os.listdir(source_dir):
    if file.endswith((".png", ".svg")):
        shutil.copy2(os.path.join(source_dir, file), export_dir)
print("All design files exported successfully")</code></pre>

<ol start="3">
<li><strong>LAN sharing access</strong>: Modify launch command to allow other devices on the same Wi-Fi to visit your design tool:</li>
</ol>

<pre><code class="language-bash">python main.py --host 0.0.0.0 --port 7890</code></pre>

<p>Other devices access via <code>http://[your-local-ip]:7890</code>.</p>

<h2>FAQ</h2>

<h3>Does the open-source Claude Design require a powerful GPU?</h3>
<p>No. While a GPU with 8GB+ VRAM is recommended for optimal performance, the project supports CPU-only deployment. With CPU mode, generation is slower but fully functional. Consumer GPUs like RTX 3060 or even laptop GPUs work well for most design tasks. You can also offload model inference to a remote <a href="/en/tools/ollama">Ollama</a> server on your LAN if your local machine lacks GPU power.</p>

<h3>Is the open-source version feature-complete compared to the official Claude Design?</h3>
<p>The open-source replica covers the core design generation workflow — prompt-to-UI, reference sketch upload, and design export (PNG/SVG). However, the official <a href="/en/tools/claude-design">Claude Design</a> cloud version offers additional features like collaborative editing, version history, and premium design templates. For solo creators and small teams who primarily need AI-powered UI generation, the open-source version is more than sufficient.</p>

<h3>Can I customize the generated UI designs with my own brand styles?</h3>
<p>Yes. Since the source code is fully open, you can modify the prompt templates, color palettes, and layout presets in the config files. You can also add custom brand assets (logos, fonts, color schemes) to the static assets folder, and the generation pipeline will incorporate them. Advanced users can fine-tune the underlying vision model on their own design dataset for brand-specific outputs.</p>

<div class="next-step">
<p><strong>Next Read:</strong> <a href="/en/article/one-claude-code-two-roles">One Claude Code, Two Roles: Code Writing and Reviewing Without Codex →</a></p>
</div>`,
    contentZh: `
<div class="meta-banner">
  <span>📅 2026-06-18</span>
  <span>📂 <a href="/zh/learn/ai-tutorials">AI教程</a></span>
  <span>⏱️ 8 分钟阅读</span>
  <span>🔰 初学者</span>
</div>

<p>大多数创作者只使用<a href="/zh/tools/claude-design">Claude Design</a>的官方云版本，面临严格的速率限制和付费订阅。很少有人知道有一个完全开源的Claude Design复刻版，可以在本地PC上部署，实现无限设计生成，无需网络限制或计费。本教程涵盖自托管开源Claude Design的完整环境配置、源码部署、模型对接和常见故障排除，每一步都配有可执行代码块。</p>

<h2>1. 自托管开源Claude Design的核心优势</h2>

<ol>
<li><strong>无限生成</strong>：本地运行无每日请求上限，无Token计费。</li>
<li><strong>数据隐私</strong>：所有设计稿、提示词和图片素材存储在本地，不上传第三方服务器。</li>
<li><strong>自定义模型对接</strong>：兼容本地开源视觉模型、<a href="/zh/tools/ollama">Ollama</a>和远程LLM API。</li>
<li><strong>功能可定制</strong>：修改源码添加品牌模板、批量导出和团队协作模块。</li>
<li><strong>低硬件门槛</strong>：8GB显存的消费级GPU流畅运行，甚至支持纯CPU部署。</li>
</ol>

<h2>2. 部署前环境准备</h2>

<h3>2.1 依赖安装</h3>

<p>该开源项目依赖Python 3.10+、Git和Node.js。根据操作系统运行以下安装命令。</p>

<p><strong>Windows（PowerShell管理员）：</strong></p>

<pre><code class="language-powershell"># 安装winget依赖
winget install Python.Python.3.10 Git.Git OpenJS.NodeJS.LTS
# 验证安装版本
python --version
git --version
node -v
npm -v</code></pre>

<p><strong>macOS（终端）：</strong></p>

<pre><code class="language-bash"># 如缺少Homebrew则先安装
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# 安装所需运行时
brew install python@3.10 git node</code></pre>

<p><strong>Linux Ubuntu/Debian：</strong></p>

<pre><code class="language-bash">sudo apt update && sudo apt install python3.10 python3-pip git nodejs npm -y</code></pre>

<h3>2.2 GPU加速设置（推荐）</h3>

<p>如果你有NVIDIA显卡，安装CUDA工具包加速图像渲染：</p>

<pre><code class="language-bash"># 安装支持CUDA的PyTorch
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121</code></pre>

<h2>3. 克隆开源仓库并安装项目依赖</h2>

<h3>3.1 拉取源码</h3>

<p>创建空文件夹并克隆官方开源仓库：</p>

<pre><code class="language-bash"># 创建工作目录
mkdir claude-design-local && cd claude-design-local
# 克隆源码仓库
git clone https://github.com/open-claude-design/claude-design.git
cd claude-design</code></pre>

<h3>3.2 后端Python依赖安装</h3>

<pre><code class="language-bash"># 创建独立虚拟环境避免版本冲突
python3 -m venv venv
# 激活虚拟环境（Windows）
venv\\Scripts\\activate
# 激活虚拟环境（macOS/Linux）
source venv/bin/activate
# 安装所有后端依赖
pip install -r requirements.txt</code></pre>

<h3>3.3 前端Web构建</h3>

<pre><code class="language-bash"># 进入前端文件夹
cd web
# 安装npm包
npm install
# 构建静态前端文件
npm run build</code></pre>

<h2>4. 模型配置：对接本地和远程视觉模型</h2>

<p>开源Claude Design默认不嵌入模型，需要在配置文件中设置模型访问。</p>

<h3>4.1 修改核心配置文件</h3>

<pre><code class="language-bash"># 打开配置文件进行编辑
cp config.example.yaml config.yaml</code></pre>

<p>编辑<code>config.yaml</code>设置模型来源，示例<a href="/zh/tools/ollama">Ollama</a>本地模型配置：</p>

<pre><code class="language-yaml">model_provider: ollama
vision_model: llama3.2-vision:11b
api_base: http://127.0.0.1:11434
api_key: dummy-key
max_image_size: 1024
render_batch: 4</code></pre>

<h3>4.2 通过Ollama拉取本地视觉模型</h3>

<p>如果使用Ollama作为模型后端，启动服务前运行此命令下载视觉模型：</p>

<pre><code class="language-bash">ollama pull llama3.2-vision:11b</code></pre>

<h2>5. 启动本地服务并访问Web界面</h2>

<h3>5.1 启动后端服务</h3>

<p>保持虚拟环境激活状态，执行：</p>

<pre><code class="language-bash"># 启动后端API服务
python main.py --host 0.0.0.0 --port 7890</code></pre>

<h3>5.2 访问设计面板</h3>

<p>打开浏览器访问<code>http://127.0.0.1:7890</code>，功能完整的开源<a href="/zh/tools/claude-design">Claude Design</a>界面将加载。你可以输入UI设计提示词、上传参考草图、生成页面布局，并在本地导出PNG/SVG设计文件，无任何网络限制。</p>

<p>可直接在本地工具中输入的实际设计提示词示例：</p>

<pre><code class="language-text">设计一个极简AI工具落地页，移动端优先布局，蓝色科技调，包含功能卡片区、下载按钮和页脚版权信息。输出清晰的Figma风格分层设计。</code></pre>

<h2>6. 常见新手陷阱及修复命令</h2>

<h3>陷阱1：端口7890被占用，服务启动失败</h3>

<p>检查占用端口并终止进程：</p>

<pre><code class="language-powershell"># Windows
netstat -ano | findstr "7890"
taskkill /F /PID [目标PID号]</code></pre>

<pre><code class="language-bash"># macOS/Linux
lsof -i :7890
kill -9 [进程ID]</code></pre>

<h3>陷阱2：图像生成黑屏，模型连接错误</h3>

<p>重启Ollama并重新加载服务：</p>

<pre><code class="language-bash">ollama stop llama3.2-vision:11b
ollama start
# 重新运行后端
python main.py</code></pre>

<h3>陷阱3：npm构建后前端页面空白</h3>

<p>重新安装前端依赖：</p>

<pre><code class="language-bash">cd web
rm -rf node_modules package-lock.json
npm install && npm run build</code></pre>

<h2>7. 长期使用的高级优化</h2>

<ol>
<li><strong>开机自启服务</strong>：编写简单的启动脚本，让PC开机后自动运行后端。</li>
<li><strong>批量导出脚本</strong>：添加Python脚本批量导出所有生成的设计稿到本地文件夹：</li>
</ol>

<pre><code class="language-python"># 批量导出所有设计稿示例
import os
import shutil

export_dir = "./export_designs"
source_dir = "./static/output"
os.makedirs(export_dir, exist_ok=True)

for file in os.listdir(source_dir):
    if file.endswith((".png", ".svg")):
        shutil.copy2(os.path.join(source_dir, file), export_dir)
print("所有设计文件导出成功")</code></pre>

<ol start="3">
<li><strong>局域网共享访问</strong>：修改启动命令，让同一Wi-Fi下的其他设备也能访问你的设计工具：</li>
</ol>

<pre><code class="language-bash">python main.py --host 0.0.0.0 --port 7890</code></pre>

<p>其他设备通过<code>http://[你的本地IP]:7890</code>访问。</p>

<h2>常见问题</h2>

<h3>开源Claude Design需要强大的GPU吗？</h3>
<p>不需要。虽然推荐8GB以上显存的GPU以获得最佳性能，但该项目支持纯CPU部署。CPU模式下生成速度较慢，但功能完整。RTX 3060等消费级GPU甚至笔记本GPU都能很好地处理大多数设计任务。如果本地机器GPU性能不足，也可以将模型推理卸载到局域网中的远程<a href="/zh/tools/ollama">Ollama</a>服务器。</p>

<h3>开源版本与官方Claude Design功能对比如何？</h3>
<p>开源复刻版涵盖了核心设计生成工作流——文本生成UI、参考草图上传和设计导出（PNG/SVG）。然而，官方<a href="/zh/tools/claude-design">Claude Design</a>云版本提供协作编辑、版本历史和高级设计模板等额外功能。对于主要需要AI驱动UI生成的个人创作者和小团队，开源版本完全够用。</p>

<h3>可以用自己的品牌风格自定义生成的UI设计吗？</h3>
<p>可以。由于源码完全开放，你可以修改配置文件中的提示词模板、调色板和布局预设。还可以将自定义品牌素材（Logo、字体、配色方案）添加到静态资源文件夹，生成管道会自动融入。高级用户可以在自己的设计数据集上微调底层视觉模型，以获得品牌专属输出。</p>

<div class="next-step">
<p><strong>下一篇：</strong> <a href="/zh/article/one-claude-code-two-roles">一个Claude Code，两种角色：无需Codex也能写代码和审代码 →</a></p>
</div>`,
  },
"""

article2_content = r"""
  // ====== Article: One Claude Code, Two Roles ======
  "one-claude-code-two-roles": {
    content: `
<div class="meta-banner">
  <span>📅 2026-06-18</span>
  <span>📂 <a href="/en/learn/ai-tutorials">AI Tutorials</a></span>
  <span>⏱️ 6 min read</span>
  <span>⚡ Intermediate</span>
</div>

<p>In the world of AI-assisted coding, many developers think you need two models like <a href="/en/tools/claude">Claude Code</a> and <a href="/en/tools/codex">Codex</a> to handle writing and reviewing. But what if you only have Claude Code? This guide shows you how to use a single Claude Code model to both write and review code by leveraging isolated contexts, with practical steps and code examples.</p>

<h2>Why One Model Can Do Both: Isolated Contexts Matter</h2>

<p>The key isn't having a second model; it's having a <strong>second clean context</strong>. When a model reviews its own code in the same conversation, it's biased by its original implementation. A separate context, however, acts like a fresh pair of eyes — one that hasn't seen the coding process and only focuses on the code itself.</p>

<p>For example, if you ask Claude Code to review its own code in the same chat, it might miss issues like:</p>

<ul>
<li>Memory leaks in idempotent keys that aren't cleaned up.</li>
<li>Race conditions in high-concurrency order systems.</li>
</ul>

<p>A separate review agent in its own context catches these because it's not influenced by how the code was written.</p>

<h2>Setting Up a Code-Review Agent in Claude Code</h2>

<p>To create a dedicated review agent, you need a configuration file. Here's how to do it:</p>

<h3>Step 1: Create the Agent Configuration File</h3>

<p>In your project's <code>.claude/agents/</code> directory, create a file named <code>code-reviewer.md</code>. This file has two parts: frontmatter (configuration) and a prompt (instructions for the reviewer).</p>

<pre><code class="language-markdown">---
name: code-reviewer
description: Review code changes for issues.
tools: Read, Grep, Glob, Bash
model: inherit
---
# Code Review Guidelines
01. Focus only on identifying issues, not fixing them. List problems clearly.
02. Check for memory leaks, especially in idempotent implementations.
03. Verify concurrency safety for high-traffic features.
04. Ensure code follows best practices (readability, maintainability).
05. Use \`git diff\` to understand changes and review only the modified parts.
06. Report issues without suggesting code changes — leave fixes to the main conversation.</code></pre>

<h3>Step 2: Understand the Configuration</h3>

<ul>
<li><strong><code>name</code></strong>: Identifies the agent (e.g., <code>code-reviewer</code>).</li>
<li><strong><code>description</code></strong>: Tells the main Claude Code when to use this agent.</li>
<li><strong><code>tools</code></strong>: Limits the agent to read-only tools (<code>Read</code>, <code>Grep</code>, <code>Glob</code>) and <code>git diff</code> (via Bash) to analyze changes. No write/edit tools to prevent it from fixing code directly.</li>
<li><strong><code>model: inherit</code></strong>: Uses the same model as the main conversation (so you don't need Codex).</li>
</ul>

<h2>How to Use the Review Agent in Practice</h2>

<p>Once set up, using the agent is straightforward:</p>

<ol>
<li><strong>Write Code in the Main Conversation</strong>: Ask Claude Code to write code, e.g., "Implement an idempotent order API to prevent duplicate orders."</li>
<li><strong>Trigger the Review Agent</strong>: After the code is written, request a review: "Use <code>code-reviewer</code> to check the recent idempotent order API changes."</li>
<li><strong>Analyze the Feedback</strong>: The review agent will generate a list of issues. For example, it might point out:
<ul>
<li>"Idempotent keys are not cleaned up, leading to memory bloat."</li>
<li>"Race condition in concurrent order requests."</li>
</ul>
</li>
<li><strong>Fix Issues in the Main Conversation</strong>: Go back to the main chat and address the issues, then repeat the review process for high-risk changes.</li>
</ol>

<h2>When to Use the Review Agent (and When to Skip)</h2>

<p>Not all changes need a full review. Use this <strong>risk-based checklist</strong> to decide:</p>

<ul>
<li><strong>High-Risk Changes (Use the Review Agent)</strong>:
<ul>
<li>Authentication/authorization logic.</li>
<li>Financial transactions (e.g., payment systems).</li>
<li>Data deletion features.</li>
<li>High-concurrency features (e.g., order processing).</li>
</ul>
</li>
<li><strong>Low-Risk Changes (Skip the Review)</strong>:
<ul>
<li>UI text or style tweaks.</li>
<li>Documentation updates.</li>
<li>Small refactors with no business logic changes.</li>
</ul>
</li>
</ul>

<h2>Beyond Claude Code: Applying This to Codex</h2>

<p>This approach isn't limited to Claude Code. If you use <a href="/en/tools/codex">Codex</a>, you can create a similar review agent in <code>.codex/agents/reviewer.md</code> with the same structure. Codex even has a built-in <code>/review</code> command for one-click reviews, working the same way as Claude Code's <code>code-reviewer</code>.</p>

<h2>FAQ</h2>

<h3>Can I use the same approach with other AI coding tools?</h3>
<p>Yes. The core principle — isolated context for review — applies to any AI coding assistant that supports custom agents or separate conversation contexts. <a href="/en/tools/codex">Codex</a> has a built-in <code>/review</code> command, and Cursor supports <code>.cursor/rules</code> for custom review instructions. The key is ensuring the reviewer has no memory of the original coding session, so it evaluates the code objectively.</p>

<h3>What if the review agent misses important issues?</h3>
<p>No review process is perfect. For critical code (auth, payments, data deletion), combine the AI review with traditional methods: peer code review, automated tests, and static analysis tools. The AI review agent is a powerful first-pass filter that catches common issues quickly, but it should complement — not replace — human oversight for high-risk changes.</p>

<h3>How is this different from Claude Code's built-in review features?</h3>
<p><a href="/en/tools/claude">Claude Code</a> has built-in code understanding capabilities, but when reviewing its own output in the same conversation, it carries implementation bias. The dedicated agent approach creates a truly independent review by isolating the reviewer in a separate context. This is the same architectural principle that makes Codex's <code>/review</code> command effective — it spawns a fresh agent instance that only sees the diff, not the development history.</p>

<div class="next-step">
<p><strong>Next Read:</strong> <a href="/en/article/open-source-claude-design-local-deploy">Open-Source Claude Design Local Deployment Guide →</a></p>
</div>`,
    contentZh: `
<div class="meta-banner">
  <span>📅 2026-06-18</span>
  <span>📂 <a href="/zh/learn/ai-tutorials">AI教程</a></span>
  <span>⏱️ 6 分钟阅读</span>
  <span>⚡ 中级</span>
</div>

<p>在AI辅助编程的世界里，很多开发者认为需要两个模型——<a href="/zh/tools/claude">Claude Code</a>和<a href="/zh/tools/codex">Codex</a>——才能分别处理代码编写和审查。但如果只有Claude Code呢？本指南教你如何通过隔离上下文，用单个Claude Code模型同时完成代码编写和审查，配有实操步骤和代码示例。</p>

<h2>为什么一个模型能做两件事：隔离上下文是关键</h2>

<p>关键不在于有第二个模型，而在于有一个<strong>第二个干净的上下文</strong>。当模型在同一对话中审查自己的代码时，它会被原始实现所偏见。而独立上下文就像一双全新的眼睛——它没有看过编码过程，只关注代码本身。</p>

<p>例如，如果你让Claude Code在同一聊天中审查自己的代码，它可能漏掉以下问题：</p>

<ul>
<li>未清理的幂等键导致内存泄漏。</li>
<li>高并发订单系统中的竞态条件。</li>
</ul>

<p>独立上下文中的审查代理能发现这些问题，因为它不受代码编写过程的影响。</p>

<h2>在Claude Code中设置代码审查代理</h2>

<p>要创建专用的审查代理，需要一个配置文件。以下是操作步骤：</p>

<h3>步骤1：创建代理配置文件</h3>

<p>在项目的<code>.claude/agents/</code>目录中，创建名为<code>code-reviewer.md</code>的文件。该文件包含两部分：frontmatter（配置）和prompt（审查者指令）。</p>

<pre><code class="language-markdown">---
name: code-reviewer
description: 审查代码变更中的问题。
tools: Read, Grep, Glob, Bash
model: inherit
---
# 代码审查指南
01. 只关注发现问题，不修复问题。清晰列出问题。
02. 检查内存泄漏，特别是幂等实现中的。
03. 验证高流量功能的并发安全性。
04. 确保代码遵循最佳实践（可读性、可维护性）。
05. 使用 \`git diff\` 理解变更，只审查修改的部分。
06. 报告问题时不建议代码修改——将修复留给主对话。</code></pre>

<h3>步骤2：理解配置</h3>

<ul>
<li><strong><code>name</code></strong>：标识代理（如<code>code-reviewer</code>）。</li>
<li><strong><code>description</code></strong>：告诉主Claude Code何时使用此代理。</li>
<li><strong><code>tools</code></strong>：将代理限制为只读工具（<code>Read</code>、<code>Grep</code>、<code>Glob</code>）和<code>git diff</code>（通过Bash）来分析变更。无写入/编辑工具，防止直接修改代码。</li>
<li><strong><code>model: inherit</code></strong>：使用与主对话相同的模型（因此不需要Codex）。</li>
</ul>

<h2>实践中如何使用审查代理</h2>

<p>设置完成后，使用代理非常简单：</p>

<ol>
<li><strong>在主对话中编写代码</strong>：让Claude Code编写代码，例如"实现幂等订单API以防止重复下单。"</li>
<li><strong>触发审查代理</strong>：代码写完后请求审查："使用<code>code-reviewer</code>检查最近的幂等订单API变更。"</li>
<li><strong>分析反馈</strong>：审查代理会生成问题列表。例如可能指出：
<ul>
<li>"幂等键未清理，导致内存膨胀。"</li>
<li>"并发订单请求中存在竞态条件。"</li>
</ul>
</li>
<li><strong>在主对话中修复问题</strong>：回到主聊天处理问题，然后对高风险变更重复审查流程。</li>
</ol>

<h2>何时使用审查代理（以及何时跳过）</h2>

<p>并非所有变更都需要完整审查。使用此<strong>基于风险的检查清单</strong>来决定：</p>

<ul>
<li><strong>高风险变更（使用审查代理）</strong>：
<ul>
<li>认证/授权逻辑。</li>
<li>金融交易（如支付系统）。</li>
<li>数据删除功能。</li>
<li>高并发功能（如订单处理）。</li>
</ul>
</li>
<li><strong>低风险变更（跳过审查）</strong>：
<ul>
<li>UI文字或样式调整。</li>
<li>文档更新。</li>
<li>不涉及业务逻辑的小重构。</li>
</ul>
</li>
</ul>

<h2>超越Claude Code：将此方法应用到Codex</h2>

<p>这种方法不限于Claude Code。如果你使用<a href="/zh/tools/codex">Codex</a>，可以在<code>.codex/agents/reviewer.md</code>中创建类似的审查代理，结构相同。Codex甚至有内置的<code>/review</code>命令一键审查，工作方式与Claude Code的<code>code-reviewer</code>相同。</p>

<h2>常见问题</h2>

<h3>可以用同样的方法配合其他AI编程工具吗？</h3>
<p>可以。核心原则——隔离上下文进行审查——适用于任何支持自定义代理或独立对话上下文的AI编程助手。<a href="/zh/tools/codex">Codex</a>有内置的<code>/review</code>命令，Cursor支持<code>.cursor/rules</code>用于自定义审查指令。关键是确保审查者没有原始编码会话的记忆，从而客观评估代码。</p>

<h3>如果审查代理漏掉重要问题怎么办？</h3>
<p>没有任何审查流程是完美的。对于关键代码（认证、支付、数据删除），将AI审查与传统方法结合：同行代码审查、自动化测试和静态分析工具。AI审查代理是一个强大的第一道过滤器，能快速发现常见问题，但它应该补充而非替代高风险变更的人工监督。</p>

<h3>这与Claude Code内置的审查功能有何不同？</h3>
<p><a href="/zh/tools/claude">Claude Code</a>具有内置的代码理解能力，但在同一对话中审查自己的输出时会带有实现偏见。专用代理方法通过将审查者隔离在独立上下文中，创建真正独立的审查。这与Codex的<code>/review</code>命令有效的架构原理相同——它启动一个新的代理实例，只看到差异，看不到开发历史。</p>

<div class="next-step">
<p><strong>下一篇：</strong> <a href="/zh/article/open-source-claude-design-local-deploy">开源Claude Design本地部署指南 →</a></p>
</div>`,
  },
"""

last_brace = content_src.rfind('};')
content_new = content_src[:last_brace] + article1_content + article2_content + '\n};\n'

with open('src/lib/article-content.ts', 'w', encoding='utf-8') as f:
    f.write(content_new)

print('Part 2: 2 article contents added to article-content.ts')
print('\nAll done! 0 new tools, 2 new articles.')
