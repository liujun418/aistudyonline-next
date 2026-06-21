"""
Publish June 20, 2026 articles.
0 new tools needed — all referenced tools (claude, codex, deepseek) already exist.
"""

import os

BASE = r"C:\Users\jun\aistudyonline-next"
os.chdir(BASE)

# ===== Part 1: Add 2 article metadata to articles.ts =====
with open('src/lib/articles.ts', 'r', encoding='utf-8') as f:
    articles_src = f.read()

new_articles = r"""  {
    slug: "claude-dynamic-workflows",
    title: "Claude Dynamic Workflows: Transform One AI into a Team of 100 for Explosive Productivity",
    titleZh: "Claude动态工作流：把一个AI变成百人团队，效率爆炸提升",
    description: "Learn how Claude's Dynamic Workflows feature turns a solo AI assistant into a project manager that orchestrates hundreds of sub-agents in parallel — 10x efficiency for research, writing, and coding.",
    descriptionZh: "了解Claude动态工作流如何将单人AI助手变成能并行调度数百个子代理的项目经理——研究、写作、编码效率提升10倍。",
    category: "ai-tutorials",
    tags: ["claude", "workflow", "productivity", "agent", "parallel"],
    difficulty: "intermediate",
    toolsMentioned: ["claude"],
    date: "2026-06-20",
  },
  {
    slug: "codex-complete-guide-domestic",
    title: "Codex Complete Guide for Domestic Users: Full Installation + Official Plugins Setup (Step-by-Step)",
    titleZh: "Codex国内用户完整指南：安装+官方插件配置全流程（手把手）",
    description: "A spoon-feeding guide for Chinese developers to install Codex with domestic AI models, activate all 8+ official plugins, and troubleshoot common issues — no VPN needed.",
    descriptionZh: "面向国内开发者的手把手教程：用国产AI模型安装Codex、激活全部8+官方插件、解决常见问题——无需VPN。",
    category: "ai-tutorials",
    tags: ["codex", "deepseek", "coding", "plugins", "domestic", "beginner"],
    difficulty: "beginner",
    toolsMentioned: ["codex", "deepseek"],
    date: "2026-06-20",
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
  // ====== Article: Claude Dynamic Workflows ======
  "claude-dynamic-workflows": {
    content: `
<div class="meta-banner">
  <span>📅 2026-06-20</span>
  <span>📂 <a href="/en/learn/ai-tutorials">AI Tutorials</a></span>
  <span>⏱️ 7 min read</span>
  <span>⚡ Intermediate</span>
</div>

<p>In the realm of AI tools, <a href="/en/tools/claude">Claude</a> has quietly rolled out a game-changing feature that's been overshadowed by its model upgrades — <strong>Dynamic Workflows</strong>. This isn't just a minor update; it's a paradigm shift, turning Claude from a solo assistant into a project manager that can orchestrate hundreds of AI sub-agents simultaneously. Whether you're researching, writing, or coding, this feature can multiply your efficiency by 10x.</p>

<h2>1. What Are Dynamic Workflows?</h2>

<p>Officially defined, Dynamic Workflows are JavaScript scripts for large-scale sub-agent orchestration. Here's how it works:</p>

<ul>
<li><strong>Before</strong>: You interact with Claude one-on-one, task by task, sequentially.</li>
<li><strong>After</strong>: Claude writes an execution plan (script), launches dozens or even hundreds of sub-agents simultaneously. These sub-agents work independently while cross-verifying each other's outputs, and finally aggregate the results — all while you continue chatting with Claude without interruption.</li>
</ul>

<p>To distinguish it from Claude's other features:</p>

<ul>
<li><strong>Skills</strong>: Guide Claude on how to perform tasks it already knows (like an operation manual for an employee).</li>
<li><strong>Plugins</strong>: Provide Claude with new external tools (like giving an employee a new wrench).</li>
<li><strong>Dynamic Workflows</strong>: Empower Claude to coordinate a team, scheduling dozens of "workers" to operate in parallel.</li>
</ul>

<h3>Real-World Example: Market Research Report</h3>

<ul>
<li><strong>Traditional Claude</strong>: Generates reports based on templates but with limited data (only a few web pages).</li>
<li><strong>Plugins</strong>: Pulls real-time data but processes it one by one, slowly.</li>
<li><strong>Dynamic Workflows</strong>: Scans hundreds of sources simultaneously, cross-verifies facts via multiple agents, filters out low-quality info, and delivers a verified, comprehensive report.</li>
</ul>

<h2>2. Three Practical Ways to Get Started</h2>

<h3>Method 1: Keyword Trigger</h3>

<p>Simply include the word <code>workflow</code> in your prompt. Claude will automatically switch to orchestration mode, draft a script, show you the plan for approval, and then execute parallel tasks.</p>

<p><strong>Tips:</strong></p>
<ul>
<li>To ignore a highlighted <code>workflow</code> trigger, press <code>Alt+W</code>.</li>
<li>To disable the keyword trigger entirely, go to <code>/config</code> and turn off the "Workflow Keyword Trigger" option.</li>
</ul>

<h3>Method 2: Deep Research Command</h3>

<p>Run the built-in <code>deep research</code> command:</p>

<pre><code class="language-text">/deep-research What are the trends in DeFi protocol TVL for 2026?</code></pre>

<p>Claude will then plan, launch sub-agents for parallel scanning, and deliver a research report with cited sources in minutes — work that would normally take hours manually.</p>

<h3>Method 3: UltraCode Mode</h3>

<p>For the most powerful experience, enable UltraCode mode:</p>

<pre><code class="language-text">/effort ultra code</code></pre>

<p>Once activated, Claude automatically plans workflows for every substantial task without needing the <code>workflow</code> keyword. Note: This mode consumes more tokens (as all sub-agents run in high-inference mode). Use it for critical tasks and stick to regular mode for small, daily tasks.</p>

<h2>3. Monitoring and Controlling Workflows</h2>

<p>To check real-time progress, input <code>/workflows</code>. You'll see how many sub-agents are running at each stage, token usage, and time elapsed. Use these key controls:</p>

<ul>
<li><strong>P</strong>: Pause or resume the entire workflow.</li>
<li><strong>X</strong>: Stop the currently selected sub-agent or the entire workflow.</li>
<li><strong>R</strong>: Restart a failed sub-agent.</li>
<li><strong>S</strong>: Save a successful workflow as a reusable command.</li>
<li><strong>Enter</strong>: Dive into details of a specific sub-agent (prompts, tools used, returned results).</li>
</ul>

<h2>4. Real-World Case: Content Research & Production Pipeline</h2>

<p>Here's a four-stage workflow designed for content teams:</p>

<ol>
<li><strong>Information Collection</strong>: 30 sub-agents scan news sources, social platforms, and research publications in parallel.</li>
<li><strong>Cross-Validation</strong>: Independent verification sub-agents check information consistency and filter contradictory content.</li>
<li><strong>Noise Filtering</strong>: Low-quality content is filtered based on preset criteria.</li>
<li><strong>Ranking & Output</strong>: Results are sorted by importance and timeliness to generate an editorial brief.</li>
</ol>

<p>What used to take a content team 3-4 hours now takes just 10-15 minutes. Save this workflow with <code>S</code> and reuse it with a slash command (e.g., <code>/content-pipeline</code>). You can even schedule it to run daily for automated market intelligence briefs.</p>

<h2>5. Advanced Tips for Optimal Use</h2>

<ol>
<li><strong>Model Check for Large Tasks</strong>: Ensure you're using the right model. Running 100 sub-agents on Opus is costly; switch to Haiku for non-core tasks to save tokens.</li>
<li><strong>Connect MCP Data Sources</strong>: Integrate sources like CoinGecko or DeFiLlama for higher-quality research outputs than web search alone.</li>
<li><strong>Package Existing Skills into Workflows</strong>: String together skills like "transcribe audio to text" and "SEO optimization" into a seamless content production pipeline.</li>
<li><strong>Ask Claude for Workflow Recommendations</strong>: Use <code>Based on everything you know about me, what workflows should we build?</code> to get tailored suggestions.</li>
</ol>

<h2>FAQ</h2>

<h3>How is Dynamic Workflows different from regular Claude agent usage?</h3>
<p>Regular <a href="/en/tools/claude">Claude</a> agent usage is sequential — you ask, Claude responds, one task at a time. Dynamic Workflows let Claude act as an orchestrator: it writes a script, spawns multiple independent sub-agents, and they work in parallel. Think of it as the difference between doing everything yourself vs. managing a team of specialists who each handle their piece simultaneously. The key benefit is parallel processing — 30 research agents scanning different sources at once complete in minutes what would take hours sequentially.</p>

<h3>Does Dynamic Workflows require a specific Claude plan?</h3>
<p>Dynamic Workflows is available on Claude's paid plans (Pro, Team, Enterprise). The number of concurrent sub-agents and total workflow duration may vary by plan tier. The <code>/effort ultra code</code> mode consumes significantly more tokens since every sub-agent runs at maximum inference quality. For budget-conscious usage, use keyword-triggered workflows on regular mode for daily tasks, and reserve UltraCode for critical projects where quality is paramount.</p>

<h3>Can I share my workflows with team members?</h3>
<p>Yes. When you save a successful workflow with <code>S</code>, it becomes a slash command that can be shared. Team members on the same Claude plan can import and run your workflows. This makes Dynamic Workflows particularly powerful for teams — one person designs and refines the workflow, and the whole team benefits from the optimized process.</p>

<div class="next-step">
<p><strong>Next Read:</strong> <a href="/en/article/codex-complete-guide-domestic">Codex Complete Guide for Domestic Users: Full Installation + Official Plugins Setup →</a></p>
</div>`,
    contentZh: `
<div class="meta-banner">
  <span>📅 2026-06-20</span>
  <span>📂 <a href="/zh/learn/ai-tutorials">AI教程</a></span>
  <span>⏱️ 7 分钟阅读</span>
  <span>⚡ 中级</span>
</div>

<p>在AI工具领域，<a href="/zh/tools/claude">Claude</a>悄悄推出了一项被模型升级光环掩盖的革命性功能——<strong>动态工作流（Dynamic Workflows）</strong>。这不是小更新，而是范式转变，将Claude从单人助手变成了能同时调度数百个AI子代理的项目经理。无论你在研究、写作还是编程，这个功能都能让你的效率提升10倍。</p>

<h2>1. 什么是动态工作流？</h2>

<p>官方定义：动态工作流是用于大规模子代理编排的JavaScript脚本。通俗来讲：</p>

<ul>
<li><strong>以前</strong>：你和Claude一对一交互，逐个任务顺序执行。</li>
<li><strong>现在</strong>：Claude编写执行计划（脚本），同时启动数十甚至数百个子代理，这些子代理独立工作、交叉验证彼此的输出，最后汇总结果——全程你可以继续和Claude聊天，不受任何打断。</li>
</ul>

<p>与Claude其他功能的区别：</p>

<ul>
<li><strong>Skills（技能）</strong>：指导Claude如何执行它已经会的任务（像员工操作手册）。</li>
<li><strong>Plugins（插件）</strong>：为Claude提供新的外部工具（像给员工一把新扳手）。</li>
<li><strong>Dynamic Workflows（动态工作流）</strong>：赋予Claude协调团队的能力，调度数十个"工人"并行运作。</li>
</ul>

<h3>实际案例：市场研究报告</h3>

<ul>
<li><strong>传统Claude</strong>：基于模板生成报告，数据有限（仅几页网页）。</li>
<li><strong>插件模式</strong>：拉取实时数据但逐个处理，速度慢。</li>
<li><strong>动态工作流</strong>：同时扫描数百个来源，多代理交叉验证事实，过滤低质量信息，交付经过验证的全面报告。</li>
</ul>

<h2>2. 三种上手方式</h2>

<h3>方法一：关键词触发</h3>

<p>在提示词中包含 <code>workflow</code> 一词，Claude会自动切换到编排模式，起草脚本、展示计划供你批准，然后并行执行任务。</p>

<p><strong>提示：</strong></p>
<ul>
<li>忽略高亮的 <code>workflow</code> 触发词，按 <code>Alt+W</code>。</li>
<li>完全禁用关键词触发，去 <code>/config</code> 关闭"Workflow Keyword Trigger"选项。</li>
</ul>

<h3>方法二：深度研究命令</h3>

<p>运行内置的 <code>/deep-research</code> 命令：</p>

<pre><code class="language-text">/deep-research 2026年DeFi协议TVL趋势是什么？</code></pre>

<p>Claude会规划、启动子代理并行扫描，几分钟内交付带引用来源的研究报告——手动需要几小时的工作。</p>

<h3>方法三：UltraCode模式</h3>

<p>最强体验，启用UltraCode模式：</p>

<pre><code class="language-text">/effort ultra code</code></pre>

<p>激活后，Claude对每个重要任务自动规划工作流，无需 <code>workflow</code> 关键词。注意：此模式消耗更多Token（所有子代理都以高推理模式运行）。关键任务使用，日常小任务保持常规模式。</p>

<h2>3. 监控和控制工作流</h2>

<p>查看实时进度，输入 <code>/workflows</code>。你会看到每个阶段运行多少子代理、Token使用量和已用时间。关键控制：</p>

<ul>
<li><strong>P</strong>：暂停或恢复整个工作流。</li>
<li><strong>X</strong>：停止当前选中的子代理或整个工作流。</li>
<li><strong>R</strong>：重启失败的子代理。</li>
<li><strong>S</strong>：保存成功的工作流为可复用命令。</li>
<li><strong>Enter</strong>：深入查看特定子代理的详情（提示词、使用的工具、返回结果）。</li>
</ul>

<h2>4. 实战案例：内容研究生产流水线</h2>

<p>为内容团队设计的四阶段工作流：</p>

<ol>
<li><strong>信息采集</strong>：30个子代理并行扫描新闻源、社交平台和研究出版物。</li>
<li><strong>交叉验证</strong>：独立验证子代理检查信息一致性，过滤矛盾内容。</li>
<li><strong>噪音过滤</strong>：基于预设标准过滤低质量内容。</li>
<li><strong>排序输出</strong>：按重要性和时效性排序，生成编辑简报。</li>
</ol>

<p>内容团队原来需要3-4小时的工作现在只需10-15分钟。用 <code>S</code> 保存此工作流，用斜杠命令复用（如 <code>/content-pipeline</code>）。甚至可以设置为每天自动运行，获取自动化市场情报简报。</p>

<h2>5. 高级优化技巧</h2>

<ol>
<li><strong>大任务检查模型</strong>：确保使用合适的模型。在Opus上运行100个子代理成本高，非核心任务切换到Haiku节省Token。</li>
<li><strong>连接MCP数据源</strong>：集成CoinGecko或DeFiLlama等数据源，获得比纯网页搜索更高质量的研究输出。</li>
<li><strong>将现有技能打包成工作流</strong>：将"音频转文字"和"SEO优化"等技能串联成无缝内容生产流水线。</li>
<li><strong>让Claude推荐工作流</strong>：使用 <code>根据你对我的了解，我们应该构建哪些工作流？</code> 获取个性化建议。</li>
</ol>

<h2>常见问题</h2>

<h3>动态工作流与普通Claude代理使用有什么不同？</h3>
<p>普通<a href="/zh/tools/claude">Claude</a>代理使用是顺序的——你问、Claude答，一次一个任务。动态工作流让Claude充当编排者：它编写脚本，启动多个独立子代理，它们并行工作。就像自己动手做所有事 vs. 管理一个专家团队各自同时处理自己那部分。关键优势是并行处理——30个研究代理同时扫描不同来源，几分钟完成顺序执行需要几小时的工作。</p>

<h3>动态工作流需要特定的Claude套餐吗？</h3>
<p>动态工作流在Claude的付费套餐（Pro、Team、Enterprise）上可用。并发子代理数量和总工作流时长可能因套餐级别而异。<code>/effort ultra code</code> 模式消耗显著更多的Token，因为每个子代理都以最高推理质量运行。预算敏感时，日常任务使用关键词触发工作流的常规模式，关键项目再使用UltraCode。</p>

<h3>可以和团队成员共享工作流吗？</h3>
<p>可以。用 <code>S</code> 保存成功的工作流后，它变成一个可共享的斜杠命令。同Claude套餐的团队成员可以导入和运行你的工作流。这使得动态工作流对团队特别强大——一个人设计和优化工作流，整个团队受益于优化后的流程。</p>

<div class="next-step">
<p><strong>下一篇：</strong> <a href="/zh/article/codex-complete-guide-domestic">Codex国内用户完整指南：安装+官方插件配置全流程 →</a></p>
</div>`,
  },
"""

article2_content = r"""
  // ====== Article: Codex Complete Guide for Domestic Users ======
  "codex-complete-guide-domestic": {
    content: `
<div class="meta-banner">
  <span>📅 2026-06-20</span>
  <span>📂 <a href="/en/learn/ai-tutorials">AI Tutorials</a></span>
  <span>⏱️ 8 min read</span>
  <span>🔰 Beginner</span>
</div>

<p>For developers in China, accessing and using <a href="/en/tools/codex">Codex</a> effectively — with all official plugins — has long been a challenge due to network restrictions and configuration hurdles. This beginner-friendly, "spoon-feeding" guide breaks down the entire process from installation to plugin activation, ensuring even non-technical users can leverage Codex's full capabilities without complex setups.</p>

<h2>1. Core Advantages of This Domestic-Friendly Setup</h2>

<ul>
<li><strong>No Special Network Required</strong>: Works with regular domestic internet (no VPN needed).</li>
<li><strong>Full Official Plugins Access</strong>: Activate all 8+ official Codex plugins (Browser, Terminal, File Manager, etc.).</li>
<li><strong>Stable Connection</strong>: Uses domestic API gateways to avoid latency or disconnections.</li>
<li><strong>Zero Coding Experience Needed</strong>: Follow copy-paste commands and visual steps.</li>
</ul>

<h2>2. Prerequisites (3 Things You Need)</h2>

<ol>
<li>A Windows 10/11 or macOS 12+ computer (64-bit, 8GB+ RAM recommended).</li>
<li>A free <a href="/en/tools/deepseek">DeepSeek</a> API key (domestic AI model alternative to GPT).</li>
<li>10 minutes of time (the entire process is streamlined to under 10 minutes).</li>
</ol>

<h2>3. Step 1: Download Codex Client (Domestic Mirror)</h2>

<p>The official Codex download may be inaccessible in China — use a trusted domestic mirror:</p>

<ol>
<li>Visit the Codex China Mirror (Alibaba Cloud-hosted).</li>
<li>Select the version for your OS:
<ul>
<li>Windows: Download <code>Codex-Setup-1.8.2.exe</code> (58MB).</li>
<li>macOS: Download <code>Codex-1.8.2.dmg</code> (62MB).</li>
</ul>
</li>
<li>Install by double-clicking — no custom settings needed (just click "Next" → "Install" → "Finish").</li>
</ol>

<h2>4. Step 2: Configure Domestic AI Model Connection</h2>

<p>Codex defaults to ChatGPT, but we'll connect it to <a href="/en/tools/deepseek">DeepSeek</a> for stable access:</p>

<ol>
<li>Open Codex after installation. Click "Settings" (gear icon) in the bottom-left corner.</li>
<li>Select "Model Configuration" → "Custom API".</li>
<li>Fill in the fields:</li>
</ol>

<pre><code class="language-text">API Provider: DeepSeek
API Base URL: https://api.deepseek.com/v1
API Key: [Paste your DeepSeek API key here]
Model: deepseek-chat</code></pre>

<ol start="4">
<li>Click "Test Connection" — a green "Connected Successfully" message means it's working.</li>
<li>Click "Save" to apply the settings.</li>
</ol>

<h3>How to Get a DeepSeek API Key (30-Second Tutorial)</h3>

<ol>
<li>Go to <a href="https://platform.deepseek.com/" target="_blank" rel="noopener">DeepSeek Open Platform</a> and sign up with your phone number.</li>
<li>After logging in, click "API Keys" → "Create New Key".</li>
<li>Name the key (e.g., "Codex Usage") and click "Generate" — copy the key immediately (it won't be shown again).</li>
</ol>

<h2>5. Step 3: Install All Official Codex Plugins</h2>

<p>Codex's power lies in its plugins — here's how to install and enable all official ones:</p>

<ol>
<li>In Codex, click "Plugins" (puzzle icon) in the left sidebar.</li>
<li>Click "Install Official Plugins" → select "All Plugins" (or check individual ones you need):
<ul>
<li><strong>Browser</strong>: Web search and page scraping.</li>
<li><strong>Terminal</strong>: Run shell commands.</li>
<li><strong>File Manager</strong>: Read/write local files.</li>
<li><strong>Code Interpreter</strong>: Execute Python/R code.</li>
<li><strong>PDF Reader</strong>: Analyze PDF documents.</li>
<li><strong>Image Generator</strong>: Create images from text.</li>
<li><strong>Excel Processor</strong>: Edit and analyze Excel files.</li>
<li><strong>Git Integration</strong>: Manage Git repositories.</li>
</ul>
</li>
<li>Click "Install" — wait 20 seconds for all plugins to download.</li>
</ol>

<h3>Verify Plugin Activation</h3>

<p>Run this test prompt to confirm plugins work:</p>

<pre><code class="language-text">Use the Browser plugin to search for "2024 top Python frameworks", then use the File Manager plugin to save the results to a text file named "python-frameworks-2024.txt" on my desktop.</code></pre>

<h2>6. Step 4: Practical Use Cases</h2>

<h3>1. Automate File Organization (File Manager Plugin)</h3>

<pre><code class="language-text">Use the File Manager plugin to organize my "Downloads" folder:
1. Create subfolders: "Documents", "Images", "Videos", "Others".
2. Move all .pdf/.docx/.txt files to "Documents".
3. Move all .jpg/.png/.gif files to "Images".
4. Move all .mp4/.mov files to "Videos".
5. Move remaining files to "Others".
6. Generate a summary of how many files were moved to each folder.</code></pre>

<h3>2. Run Code Snippets (Code Interpreter Plugin)</h3>

<pre><code class="language-text">Use the Code Interpreter plugin to:
1. Calculate the sum of the first 100 prime numbers.
2. Generate a bar chart showing the distribution of these primes.
3. Save the chart as "prime-numbers-chart.png" on my desktop.
4. Output the final sum and the file path.</code></pre>

<h3>3. Analyze PDF Data (PDF Reader Plugin)</h3>

<pre><code class="language-text">Use the PDF Reader plugin to:
1. Open the file "sales-report-2024.pdf" from my Documents folder.
2. Extract all numerical sales data from the first 5 pages.
3. Calculate the total revenue and average units sold per month.
4. Save the analysis as "sales-analysis-2024.txt" in the same folder.</code></pre>

<h2>7. Troubleshooting Common Issues</h2>

<h3>Issue 1: Plugin Installation Fails</h3>

<pre><code class="language-bash"># Windows
cd C:\Program Files\Codex
codex --repair-plugins

# macOS
cd /Applications/Codex.app/Contents/MacOS
./Codex --repair-plugins</code></pre>

<h3>Issue 2: API Connection Error</h3>

<ul>
<li>Ensure your API key is not expired (DeepSeek keys are valid for 90 days).</li>
<li>Check if your internet connection is stable.</li>
<li>Re-enter the API Base URL: <code>https://api.deepseek.com/v1</code> (no typos).</li>
</ul>

<h3>Issue 3: Terminal Plugin Not Working (Windows)</h3>

<ol>
<li>Open Codex → "Plugins" → "Terminal" → "Settings".</li>
<li>Select "Use PowerShell" (default is Command Prompt).</li>
<li>Click "Save" and retry running commands.</li>
</ol>

<h2>FAQ</h2>

<h3>Do I need a ChatGPT account to use Codex with this setup?</h3>
<p>No. By configuring <a href="/en/tools/codex">Codex</a> with <a href="/en/tools/deepseek">DeepSeek</a> as the backend model, you completely bypass ChatGPT. You only need a free DeepSeek API key. This makes Codex accessible regardless of OpenAI account restrictions or regional limitations. The DeepSeek API is also dramatically cheaper — roughly one-twentieth of OpenAI's pricing.</p>

<h3>Can I use other domestic models besides DeepSeek?</h3>
<p>Yes. The same configuration pattern works with any OpenAI-compatible API. You can use Moonshot AI (Kimi), Zhipu AI (GLM), or Baidu ERNIE Bot by changing the API Base URL and model name in the settings. The key is that the model must support an OpenAI-compatible chat completions endpoint. DeepSeek is recommended as the starting point due to its excellent coding performance and low cost.</p>

<h3>What if Codex updates and breaks the configuration?</h3>
<p>Codex updates generally preserve custom API configurations. If a major update resets your settings, simply repeat Step 2 (re-entering the API details). Your DeepSeek API key remains valid. For plugin issues after an update, run <code>codex --repair-plugins</code> as shown in the troubleshooting section above.</p>

<div class="next-step">
<p><strong>Next Read:</strong> <a href="/en/article/claude-dynamic-workflows">Claude Dynamic Workflows: Transform One AI into a Team of 100 →</a></p>
</div>`,
    contentZh: `
<div class="meta-banner">
  <span>📅 2026-06-20</span>
  <span>📂 <a href="/zh/learn/ai-tutorials">AI教程</a></span>
  <span>⏱️ 8 分钟阅读</span>
  <span>🔰 初学者</span>
</div>

<p>对于国内开发者来说，有效使用<a href="/zh/tools/codex">Codex</a>及其全部官方插件一直是个挑战，因为网络限制和配置障碍。这篇新手友好、"手把手喂饭"式指南拆解从安装到插件激活的完整流程，确保即使非技术用户也能无复杂配置地利用Codex的全部能力。</p>

<h2>1. 此国内友好配置的核心优势</h2>

<ul>
<li><strong>无需特殊网络</strong>：普通国内网络即可使用（无需VPN）。</li>
<li><strong>全部官方插件可用</strong>：激活所有8+官方Codex插件（浏览器、终端、文件管理等）。</li>
<li><strong>连接稳定</strong>：使用国内API网关，避免延迟或断连。</li>
<li><strong>零编程经验也能用</strong>：按复制粘贴命令和可视化步骤操作即可。</li>
</ul>

<h2>2. 准备工作（3样东西）</h2>

<ol>
<li>一台Windows 10/11或macOS 12+电脑（64位，建议8GB+内存）。</li>
<li>一个免费的<a href="/zh/tools/deepseek">DeepSeek</a> API Key（替代GPT的国产AI模型）。</li>
<li>10分钟时间（整个流程精简到10分钟以内）。</li>
</ol>

<h2>3. 第一步：下载Codex客户端（国内镜像）</h2>

<p>Codex官方下载在国内可能无法访问——使用可信国内镜像：</p>

<ol>
<li>访问Codex国内镜像（阿里云托管，安全可用）。</li>
<li>选择对应系统版本：
<ul>
<li>Windows：下载 <code>Codex-Setup-1.8.2.exe</code>（58MB）。</li>
<li>macOS：下载 <code>Codex-1.8.2.dmg</code>（62MB）。</li>
</ul>
</li>
<li>双击安装——无需自定义设置（直接点"下一步"→"安装"→"完成"）。</li>
</ol>

<h2>4. 第二步：配置国产AI模型连接</h2>

<p>Codex默认使用ChatGPT，我们将其连接到<a href="/zh/tools/deepseek">DeepSeek</a>实现稳定访问：</p>

<ol>
<li>安装后打开Codex，点击左下角"Settings"（齿轮图标）。</li>
<li>选择"Model Configuration" → "Custom API"。</li>
<li>填写以下信息：</li>
</ol>

<pre><code class="language-text">API Provider: DeepSeek
API Base URL: https://api.deepseek.com/v1
API Key: [在此粘贴你的DeepSeek API key]
Model: deepseek-chat</code></pre>

<ol start="4">
<li>点击"Test Connection"——显示绿色"Connected Successfully"即成功。</li>
<li>点击"Save"保存设置。</li>
</ol>

<h3>如何获取DeepSeek API Key（30秒教程）</h3>

<ol>
<li>前往<a href="https://platform.deepseek.com/" target="_blank" rel="noopener">DeepSeek开放平台</a>，用手机号注册。</li>
<li>登录后点击"API Keys" → "创建新Key"。</li>
<li>命名Key（如"Codex使用"），点击"生成"——立即复制Key（不会再显示）。</li>
</ol>

<h2>5. 第三步：安装全部官方Codex插件</h2>

<p>Codex的强大在于插件——以下是安装和启用全部官方插件的方法：</p>

<ol>
<li>在Codex中点击左侧边栏的"Plugins"（拼图图标）。</li>
<li>点击"Install Official Plugins" → 选择"All Plugins"（或勾选需要的单个插件）：
<ul>
<li><strong>Browser（浏览器）</strong>：网页搜索和页面抓取。</li>
<li><strong>Terminal（终端）</strong>：运行Shell命令。</li>
<li><strong>File Manager（文件管理）</strong>：读写本地文件。</li>
<li><strong>Code Interpreter（代码解释器）</strong>：执行Python/R代码。</li>
<li><strong>PDF Reader（PDF阅读器）</strong>：分析PDF文档。</li>
<li><strong>Image Generator（图片生成器）</strong>：文本生成图片。</li>
<li><strong>Excel Processor（Excel处理器）</strong>：编辑分析Excel文件。</li>
<li><strong>Git Integration（Git集成）</strong>：管理Git仓库。</li>
</ul>
</li>
<li>点击"Install"——等待20秒下载所有插件。</li>
</ol>

<h3>验证插件激活</h3>

<p>运行此测试提示词确认插件工作：</p>

<pre><code class="language-text">使用Browser插件搜索"2024年最佳Python框架"，然后用File Manager插件将结果保存为桌面上的"python-frameworks-2024.txt"文件。</code></pre>

<h2>6. 第四步：实战用例</h2>

<h3>1. 自动化文件整理（File Manager插件）</h3>

<pre><code class="language-text">使用File Manager插件整理我的"下载"文件夹：
1. 创建子文件夹："文档"、"图片"、"视频"、"其他"。
2. 将所有.pdf/.docx/.txt文件移动到"文档"。
3. 将所有.jpg/.png/.gif文件移动到"图片"。
4. 将所有.mp4/.mov文件移动到"视频"。
5. 将剩余文件移动到"其他"。
6. 生成每个文件夹移动了多少文件的摘要。</code></pre>

<h3>2. 运行代码片段（Code Interpreter插件）</h3>

<pre><code class="language-text">使用Code Interpreter插件：
1. 计算前100个质数的和。
2. 生成显示这些质数分布的柱状图。
3. 将图表保存为桌面上的"prime-numbers-chart.png"。
4. 输出最终和及文件路径。</code></pre>

<h3>3. 分析PDF数据（PDF Reader插件）</h3>

<pre><code class="language-text">使用PDF Reader插件：
1. 打开"文档"文件夹中的"sales-report-2024.pdf"。
2. 提取前5页的所有数字销售数据。
3. 计算总收入和月均销量。
4. 将分析结果保存为同文件夹下的"sales-analysis-2024.txt"。</code></pre>

<h2>7. 常见问题排查</h2>

<h3>问题1：插件安装失败</h3>

<pre><code class="language-bash"># Windows
cd C:\Program Files\Codex
codex --repair-plugins

# macOS
cd /Applications/Codex.app/Contents/MacOS
./Codex --repair-plugins</code></pre>

<h3>问题2：API连接错误</h3>

<ul>
<li>确保API Key未过期（DeepSeek Key有效期90天）。</li>
<li>检查网络连接是否稳定。</li>
<li>重新输入API Base URL：<code>https://api.deepseek.com/v1</code>（无拼写错误）。</li>
</ul>

<h3>问题3：Terminal插件不工作（Windows）</h3>

<ol>
<li>打开Codex → "Plugins" → "Terminal" → "Settings"。</li>
<li>选择"Use PowerShell"（默认是Command Prompt）。</li>
<li>点击"Save"后重试运行命令。</li>
</ol>

<h2>常见问题</h2>

<h3>用这个配置使用Codex需要ChatGPT账号吗？</h3>
<p>不需要。通过将<a href="/zh/tools/codex">Codex</a>配置为使用<a href="/zh/tools/deepseek">DeepSeek</a>作为后端模型，你完全绕过了ChatGPT。只需一个免费的DeepSeek API Key。这使得Codex不受OpenAI账号限制或地域约束。DeepSeek API也便宜得多——约为OpenAI定价的二十分之一。</p>

<h3>除了DeepSeek还能用其他国产模型吗？</h3>
<p>可以。同样的配置模式适用于任何OpenAI兼容的API。你可以通过更改设置中的API Base URL和模型名称使用月之暗面（Kimi）、智谱AI（GLM）或百度文心一言。关键是模型必须支持OpenAI兼容的chat completions端点。推荐以DeepSeek作为起点，因为其编码性能出色且成本低。</p>

<h3>如果Codex更新破坏了配置怎么办？</h3>
<p>Codex更新通常保留自定义API配置。如果重大更新重置了你的设置，只需重复第二步（重新输入API详情）。你的DeepSeek API Key仍然有效。对于更新后的插件问题，运行 <code>codex --repair-plugins</code> 如上文排查部分所示。</p>

<div class="next-step">
<p><strong>下一篇：</strong> <a href="/zh/article/claude-dynamic-workflows">Claude动态工作流：把一个AI变成百人团队 →</a></p>
</div>`,
  },
"""

last_brace = content_src.rfind('};')
content_new = content_src[:last_brace] + article1_content + article2_content + '\n};\n'

with open('src/lib/article-content.ts', 'w', encoding='utf-8') as f:
    f.write(content_new)

print('Part 2: 2 article contents added to article-content.ts')
print('\nAll done! 0 new tools, 2 new articles.')
