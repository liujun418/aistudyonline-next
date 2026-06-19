"""
Publish June 19, 2026 articles.
0 new tools needed — all referenced tools (codex, cc-switch, deepseek, claude) already exist.
GLM 5.2 model already exists in models.ts.
"""

import os

BASE = r"C:\Users\jun\aistudyonline-next"
os.chdir(BASE)

# ===== Part 1: Add 2 article metadata to articles.ts =====
with open('src/lib/articles.ts', 'r', encoding='utf-8') as f:
    articles_src = f.read()

new_articles = r"""  {
    slug: "codex-domestic-ai-models",
    title: "How to Use Codex with Domestic AI Models: A Practical Guide for Everyone",
    titleZh: "Codex搭配国产AI模型使用指南：人人都能用的实操教程",
    description: "Step-by-step guide to configuring Codex with domestic AI models like DeepSeek V4 and Mimo v2.5 using CC Switch — no ChatGPT account or special network setup needed.",
    descriptionZh: "通过CC Switch配置Codex使用DeepSeek V4等国产AI模型的逐步教程——无需ChatGPT账号或特殊网络环境。",
    category: "ai-tutorials",
    tags: ["codex", "deepseek", "cc-switch", "coding", "api", "beginner"],
    difficulty: "beginner",
    toolsMentioned: ["codex", "cc-switch", "deepseek"],
    date: "2026-06-19",
  },
  {
    slug: "long-running-ai-coding-glm-claude",
    title: "Mastering Long-Running AI Coding Tasks with GLM 5.2 and Claude Code",
    titleZh: "用GLM 5.2和Claude Code驾驭长时间AI编程任务",
    description: "A practical case study on running 13-hour AI coding sessions with GLM 5.2's million-token context and Claude Code's goal command for large-scale project porting.",
    descriptionZh: "实战案例：利用GLM 5.2的百万Token上下文和Claude Code的goal命令，运行13小时AI编码任务完成大型项目迁移。",
    category: "ai-tutorials",
    tags: ["glm-5", "claude-code", "long-context", "coding", "workflow", "advanced"],
    difficulty: "advanced",
    toolsMentioned: ["claude", "codex"],
    date: "2026-06-19",
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
  // ====== Article: Codex with Domestic AI Models ======
  "codex-domestic-ai-models": {
    content: `
<div class="meta-banner">
  <span>📅 2026-06-19</span>
  <span>📂 <a href="/en/learn/ai-tutorials">AI Tutorials</a></span>
  <span>⏱️ 6 min read</span>
  <span>🔰 Beginner</span>
</div>

<p>In the realm of AI-assisted coding, <a href="/en/tools/codex">Codex</a> has emerged as a powerful tool, but its reliance on the ChatGPT model can be a barrier for many due to cost and access issues. This guide walks you through using Codex with domestic AI models like <a href="/en/tools/deepseek">DeepSeek V4</a> and Mimo v2.5, making it accessible without a ChatGPT account, phone number verification, or special network configurations.</p>

<h2>1. Understanding Codex and Its Ecosystem</h2>

<p>Codex is an <strong>Agent product</strong> designed to assist with coding tasks. It's often used alongside tools like <a href="/en/tools/cc-switch">CC Switch</a>, which lets you swap out its underlying model. By default, Codex uses the ChatGPT model, but you can replace this "brain" with domestic alternatives like DeepSeek V4 or Mimo v2.5 for better accessibility and cost-effectiveness.</p>

<h3>Why Choose Domestic Models?</h3>

<ul>
<li><strong><a href="/en/tools/deepseek">DeepSeek V4</a></strong>: Highly recommended online, with excellent overall performance. However, it doesn't support multimodal inputs (e.g., image uploads).</li>
<li><strong>Mimo v2.5</strong>: Supports multimodal inputs and offers a great user experience.</li>
</ul>

<h2>2. Download and Install Codex</h2>

<p>Visit the <a href="/en/tools/codex">Codex official website</a> and download the appropriate version for your operating system (Windows or macOS). The tool is free to download.</p>

<h2>3. Install CC Switch</h2>

<p><a href="/en/tools/cc-switch">CC Switch</a> is a tool that lets you swap Codex's underlying model.</p>

<ol>
<li>Go to the <a href="https://github.com/12301230/cc-switch/releases" target="_blank" rel="noopener">CC Switch GitHub page</a>.</li>
<li>Scroll down to find the installation package:
<ul>
<li>For macOS, download the file ending with <code>.dmg</code>.</li>
<li>For Windows, download the file ending with <code>.msi</code>.</li>
</ul>
</li>
<li>If unsure which version to install, ask DeepSeek:</li>
</ol>

<pre><code class="language-text">Which version of CC Switch should I install for my [your OS] system?</code></pre>

<h2>4. Obtain an API Key from DeepSeek</h2>

<p>An <strong>API Key</strong> is like an access credential that allows Codex to communicate with the DeepSeek model.</p>

<ol>
<li>Visit the <a href="https://platform.deepseek.com/" target="_blank" rel="noopener">DeepSeek Open Platform</a>.</li>
<li>Click on "API Keys" in the left menu.</li>
<li>Create a new API Key, give it a name for easy recall, and copy the generated key. Keep it secure — it's your personal access credential.</li>
</ol>

<h2>5. Configure CC Switch</h2>

<ol>
<li>Open CC Switch and click on the third icon (OpenAI icon) at the top.</li>
<li>Click the "+" button on the right to add a model. Select "DeepSeek" (or your chosen domestic model).</li>
<li>Paste the DeepSeek API Key into the designated field. Ensure the toggle for model integration is enabled, then click "Add".</li>
</ol>

<h2>6. Test the Setup</h2>

<ol>
<li>Fully exit Codex and restart it.</li>
<li>In Codex, click on "Settings" in the bottom left corner. You should see that you're logged in via the API Key, and the model should show "DeepSeek".</li>
<li>Send a test message:</li>
</ol>

<pre><code class="language-text">Hello, what can you help me with?</code></pre>

<p>A normal response indicates success.</p>

<h2>FAQ</h2>

<h3>Do I need a ChatGPT account to use Codex?</h3>
<p>Not after this setup. By using <a href="/en/tools/cc-switch">CC Switch</a> with a domestic model's API key, you bypass ChatGPT entirely. You only need a free <a href="/en/tools/deepseek">DeepSeek</a> account (or other domestic provider) to get an API key. This makes Codex accessible to anyone, regardless of OpenAI account restrictions or regional limitations.</p>

<h3>Which domestic model should I choose — DeepSeek V4 or Mimo v2.5?</h3>
<p>It depends on your needs. <a href="/en/tools/deepseek">DeepSeek V4</a> offers better overall reasoning and coding performance, making it the top choice for pure code generation tasks. Mimo v2.5 supports multimodal inputs (you can upload images for the AI to analyze), which is useful for UI debugging or design-to-code workflows. If you mainly write and debug code, go with DeepSeek. If you need image understanding alongside coding, pick Mimo v2.5.</p>

<h3>Is CC Switch free to use?</h3>
<p>Yes, <a href="/en/tools/cc-switch">CC Switch</a> is an open-source tool available for free on GitHub. You only pay for the API usage of the model you connect to — <a href="/en/tools/deepseek">DeepSeek</a>'s API is extremely affordable at roughly one-twentieth of OpenAI's pricing.</p>

<div class="next-step">
<p><strong>Next Read:</strong> <a href="/en/article/long-running-ai-coding-glm-claude">Mastering Long-Running AI Coding Tasks with GLM 5.2 and Claude Code →</a></p>
</div>`,
    contentZh: `
<div class="meta-banner">
  <span>📅 2026-06-19</span>
  <span>📂 <a href="/zh/learn/ai-tutorials">AI教程</a></span>
  <span>⏱️ 6 分钟阅读</span>
  <span>🔰 初学者</span>
</div>

<p>在AI辅助编程领域，<a href="/zh/tools/codex">Codex</a>已成为一款强大的工具，但其对ChatGPT模型的依赖因成本和访问问题成为许多人的障碍。本指南带你通过<a href="/zh/tools/cc-switch">CC Switch</a>配置Codex使用<a href="/zh/tools/deepseek">DeepSeek V4</a>等国产AI模型，无需ChatGPT账号、手机号验证或特殊网络环境。</p>

<h2>1. 理解Codex及其生态系统</h2>

<p>Codex是一款<strong>Agent产品</strong>，专为编程任务设计。它通常配合<a href="/zh/tools/cc-switch">CC Switch</a>使用，后者可以替换其底层模型。默认情况下Codex使用ChatGPT模型，但你可以用DeepSeek V4或Mimo v2.5等国产替代方案替换这个"大脑"，获得更好的可访问性和性价比。</p>

<h3>为什么选择国产模型？</h3>

<ul>
<li><strong><a href="/zh/tools/deepseek">DeepSeek V4</a></strong>：网上评价很高，综合表现优秀。但不支持多模态输入（如图片上传）。</li>
<li><strong>Mimo v2.5</strong>：支持多模态输入，用户体验出色。</li>
</ul>

<h2>2. 下载安装Codex</h2>

<p>访问<a href="/zh/tools/codex">Codex官网</a>，下载适合你操作系统的版本（Windows或macOS）。工具免费下载。</p>

<h2>3. 安装CC Switch</h2>

<p><a href="/zh/tools/cc-switch">CC Switch</a>是让你替换Codex底层模型的工具。</p>

<ol>
<li>前往<a href="https://github.com/12301230/cc-switch/releases" target="_blank" rel="noopener">CC Switch GitHub页面</a>。</li>
<li>向下滚动找到安装包：
<ul>
<li>macOS下载<code>.dmg</code>结尾的文件。</li>
<li>Windows下载<code>.msi</code>结尾的文件。</li>
</ul>
</li>
<li>如果不确定该装哪个版本，直接问DeepSeek：</li>
</ol>

<pre><code class="language-text">我的系统是[你的操作系统]，应该安装哪个版本的CC Switch？</code></pre>

<h2>4. 从DeepSeek获取API Key</h2>

<p><strong>API Key</strong>相当于访问凭证，让Codex能与DeepSeek模型通信。</p>

<ol>
<li>访问<a href="https://platform.deepseek.com/" target="_blank" rel="noopener">DeepSeek开放平台</a>。</li>
<li>点击左侧菜单中的"API Keys"。</li>
<li>创建新API Key，取个好记的名字，复制生成的Key。妥善保管——这是你的个人访问凭证。</li>
</ol>

<h2>5. 配置CC Switch</h2>

<ol>
<li>打开CC Switch，点击顶部的第三个图标（OpenAI图标）。</li>
<li>点击右侧"+"按钮添加模型，选择"DeepSeek"（或你选的国产模型）。</li>
<li>将DeepSeek API Key粘贴到指定字段。确保模型集成开关已开启，点击"添加"。</li>
</ol>

<h2>6. 测试配置</h2>

<ol>
<li>完全退出Codex后重新启动。</li>
<li>在Codex中点击左下角"Settings"，应该看到已通过API Key登录，模型显示为"DeepSeek"。</li>
<li>发送测试消息：</li>
</ol>

<pre><code class="language-text">你好，你能帮我做什么？</code></pre>

<p>正常回复即表示配置成功。</p>

<h2>常见问题</h2>

<h3>使用Codex需要ChatGPT账号吗？</h3>
<p>此配置完成后不需要。通过<a href="/zh/tools/cc-switch">CC Switch</a>配合国产模型的API Key，你完全绕过了ChatGPT。只需一个免费的<a href="/zh/tools/deepseek">DeepSeek</a>账号（或其他国产厂商账号）获取API Key即可。这让任何人都能使用Codex，不受OpenAI账号限制或地域约束。</p>

<h3>该选DeepSeek V4还是Mimo v2.5？</h3>
<p>取决于你的需求。<a href="/zh/tools/deepseek">DeepSeek V4</a>整体推理和编程性能更好，是纯代码生成任务的首选。Mimo v2.5支持多模态输入（可上传图片让AI分析），对UI调试或设计转代码工作流很有用。如果你主要写代码和调试，选DeepSeek。如果需要图像理解配合编程，选Mimo v2.5。</p>

<h3>CC Switch免费吗？</h3>
<p>是的，<a href="/zh/tools/cc-switch">CC Switch</a>是开源工具，在GitHub上免费获取。你只需支付所连接模型的API使用费——<a href="/zh/tools/deepseek">DeepSeek</a>的API价格约为OpenAI的二十分之一，非常实惠。</p>

<div class="next-step">
<p><strong>下一篇：</strong> <a href="/zh/article/long-running-ai-coding-glm-claude">用GLM 5.2和Claude Code驾驭长时间AI编程任务 →</a></p>
</div>`,
  },
"""

article2_content = r"""
  // ====== Article: Long-Running AI Coding with GLM 5.2 and Claude Code ======
  "long-running-ai-coding-glm-claude": {
    content: `
<div class="meta-banner">
  <span>📅 2026-06-19</span>
  <span>📂 <a href="/en/learn/ai-tutorials">AI Tutorials</a></span>
  <span>⏱️ 8 min read</span>
  <span>⚡ Advanced</span>
</div>

<p>In AI-assisted software development, running large-scale projects over extended periods has long been a challenge. With models like Zhipu AI's GLM 5.2 and tools like <a href="/en/tools/claude">Claude Code</a>, it's now feasible to automate complex tasks for hours — even with massive codebases. This article dives into a practical case study: porting the 400,000-line TypeScript project OpenClaw to Python, showcasing the power of long-context AI models and structured task management.</p>

<h2>1. Why GLM 5.2 + Claude Code Matters</h2>

<p>GLM 5.2, released by Zhipu AI, stands out with its <strong>million-token context window</strong> and optimized attention mechanisms, making it capable of handling large-scale, long-duration tasks. Paired with <a href="/en/tools/claude">Claude Code</a>'s <code>goal</code> command for looped execution, you get a robust setup for end-to-end AI-driven development.</p>

<p>Most AI models struggle with "lost in the middle" issues when context windows overflow. GLM 5.2's architectural improvements minimize this, ensuring it stays on track even after 13+ hours of continuous operation — critical for projects like OpenClaw with 10+ core modules and 400,000+ lines of code.</p>

<h2>2. Step 1: Project Analysis and Task Breakdown</h2>

<h3>2.1 Reading and Analyzing the Codebase</h3>

<p>First, clone the repository and use Claude Code's agent capabilities to map the architecture:</p>

<pre><code class="language-bash">git clone --depth 1 &lt;OpenClaw-repo-url&gt;
cd python-openclaw</code></pre>

<p>Then trigger multi-agent analysis via Claude Code:</p>

<pre><code class="language-text">Analyze all .ts files in the 'ts-reference/' directory.
1. Map import dependencies and draw a call graph.
2. Identify core modules (utils, agents, plugins, etc.).
3. Document the dependency hierarchy from bottom to top.
4. List each module's responsibilities and file count.</code></pre>

<p>This generates a structured report outlining the project's architecture:</p>

<ul>
<li><strong>Layer 1 (Utils)</strong>: <code>utils/shared-types</code> (214 files) — pure utility functions.</li>
<li><strong>Layer 2 (Infrastructure)</strong>: <code>logging</code>, <code>infra</code>, <code>terminal</code> (273 files) — logging, environment management, terminal rendering.</li>
<li><strong>Layer 3 (Agent Core)</strong>: <code>agents</code>, <code>auto-reply</code>, <code>context-engine</code> (529 files) — core AI agent logic.</li>
</ul>

<h3>2.2 Breaking Down Tasks</h3>

<p>With the architecture mapped, split the project into granular tasks:</p>

<pre><code class="language-text">For each module in docs/specs/, break down into function-level tasks.
- Each task must include:
  - A clear requirement (e.g., "Implement compaction for message summarization").
  - At least 3 test cases (e.g., test_empty_messages_returns_empty_string).
  - A validation method (e.g., "Run pytest and ensure 100% coverage").
- Generate a progress.json file to track task status.</code></pre>

<p>This yields <strong>443 tasks</strong>, each with precise acceptance criteria. Example task:</p>

<pre><code class="language-text">## Task 154: Compaction for Message Summarization
- Requirement: Implement summarize_messages(messages, model)
- Test Cases:
  1. test_summarize_single_message_returns_text
  2. test_empty_messages_returns_empty_string
  3. test_fallback_truncation_when_model_fails
- Validation: Run pytest --cov=agents, ensure coverage >= 90%</code></pre>

<h2>3. Step 2: Long-Running Execution with goal Command</h2>

<p>Claude Code's <code>goal</code> command enables looped execution — the model fetches tasks from <code>progress.json</code>, executes them, and updates status iteratively.</p>

<pre><code class="language-text">/goal Iterate over all tasks in docs/plans until python check_progress.py returns 0.
- Read progress.json to get the first pending task.
- Execute all test cases defined in the task (at least 3).
- If tests fail (RED), stop and mark as failed.
- If tests pass (GREEN), run ruff check and ruff format --check; fix any issues.
- Commit changes with git commit --task=N.
- Update progress.json (done, completed+1, rounds+1).
- Stop if check_progress.py returns 0; else, continue.</code></pre>

<p>Execute it in Claude Code:</p>

<pre><code class="language-bash">/bypass permissions on
/goal &lt;prompt-text&gt;</code></pre>

<p>During the 13+ hour run, the model handles code generation, automated testing with <code>pytest</code>, linting with <code>ruff</code>, git commits per task, and progress tracking via <code>progress.json</code>.</p>

<h2>4. Step 3: Validation and Iteration</h2>

<p>Post-execution, validate the output:</p>

<ul>
<li><strong>Web Chat</strong>: Functional chat interface at <code>http://localhost:8080</code>.</li>
<li><strong>Skill Execution</strong>: Run pre-installed skills like image generation.</li>
<li><strong>Tool Usage</strong>: Fetch web content and save to local files.</li>
</ul>

<p>If issues arise (e.g., repetitive task execution), simply prompt:</p>

<pre><code class="language-text">The agent is repeating historical tasks. Fix the loop to avoid duplication.</code></pre>

<p>GLM 5.2's improved instruction-following ensures most fixes land in one shot.</p>

<h2>FAQ</h2>

<h3>Can I use this approach with models other than GLM 5.2?</h3>
<p>Yes, any model with a large enough context window can work. The key requirement is maintaining coherence over long sessions without "losing the thread." <a href="/en/tools/claude">Claude</a>'s own Opus and Sonnet models also handle long-context tasks well, though they may have different pricing structures. The million-token window of GLM 5.2 simply makes it particularly cost-effective for marathon coding sessions. You can also experiment with Gemini 2.5 Pro or GPT-5, both of which offer large context windows.</p>

<h3>What happens if the model gets stuck in an infinite loop?</h3>
<p>This is a real risk with looped execution. To mitigate it: (1) set a maximum round limit in your <code>goal</code> prompt, (2) use the progress.json file to detect when the same task is attempted multiple times without completion, and (3) periodically check in on long-running sessions. The <code>check_progress.py</code> script mentioned above should include a guard clause that exits after N consecutive failures on the same task.</p>

<h3>Is this approach suitable for production code, or just experiments?</h3>
<p>It depends on the risk level. For low-risk modules like utility functions and data formatting, AI-generated code with automated testing is production-ready. For security-critical code (authentication, payment processing), combine AI generation with human code review. The 443-task OpenClaw porting project demonstrates that AI can handle the bulk of mechanical translation work, freeing developers to focus on architecture decisions and security audits. Treat it like you'd treat any junior developer's output — test thoroughly, review critical paths, and iterate.</p>

<div class="next-step">
<p><strong>Next Read:</strong> <a href="/en/article/codex-domestic-ai-models">How to Use Codex with Domestic AI Models: A Practical Guide for Everyone →</a></p>
</div>`,
    contentZh: `
<div class="meta-banner">
  <span>📅 2026-06-19</span>
  <span>📂 <a href="/zh/learn/ai-tutorials">AI教程</a></span>
  <span>⏱️ 8 分钟阅读</span>
  <span>⚡ 高级</span>
</div>

<p>在AI辅助软件开发中，长时间运行大型项目一直是个挑战。随着智谱AI的GLM 5.2和<a href="/zh/tools/claude">Claude Code</a>等工具的出现，即使面对海量代码库，自动化复杂任务数小时已成为可行方案。本文深入一个实战案例：将40万行TypeScript项目OpenClaw移植到Python，展示长上下文AI模型与结构化任务管理的强大威力。</p>

<h2>1. 为什么GLM 5.2 + Claude Code如此重要</h2>

<p>智谱AI发布的GLM 5.2以其<strong>百万Token上下文窗口</strong>和优化的注意力机制脱颖而出，能够处理大规模、长时间任务。配合<a href="/zh/tools/claude">Claude Code</a>的<code>goal</code>命令循环执行，你得到了一套端到端AI驱动开发的稳健方案。</p>

<p>大多数AI模型在上下文窗口溢出时会出现"迷失在中间"的问题。GLM 5.2的架构改进最大限度地减少了这一问题，确保连续运行13小时以上仍能保持方向——这对拥有10+核心模块、40万+行代码的OpenClaw项目至关重要。</p>

<h2>2. 第一步：项目分析与任务拆解</h2>

<h3>2.1 阅读和分析代码库</h3>

<p>首先克隆仓库，使用Claude Code的Agent能力绘制架构图：</p>

<pre><code class="language-bash">git clone --depth 1 &lt;OpenClaw仓库地址&gt;
cd python-openclaw</code></pre>

<p>然后通过Claude Code触发多Agent分析：</p>

<pre><code class="language-text">分析'ts-reference/'目录中的所有.ts文件。
1. 绘制导入依赖关系和调用图。
2. 识别核心模块（utils、agents、plugins等）。
3. 记录从底层到顶层的依赖层级。
4. 列出每个模块的职责和文件数量。</code></pre>

<p>这会生成一份结构化报告，描绘项目架构：</p>

<ul>
<li><strong>第一层（工具层）</strong>：<code>utils/shared-types</code>（214个文件）——纯工具函数。</li>
<li><strong>第二层（基础设施）</strong>：<code>logging</code>、<code>infra</code>、<code>terminal</code>（273个文件）——日志、环境管理、终端渲染。</li>
<li><strong>第三层（Agent核心）</strong>：<code>agents</code>、<code>auto-reply</code>、<code>context-engine</code>（529个文件）——核心AI Agent逻辑。</li>
</ul>

<h3>2.2 任务拆解</h3>

<p>架构梳理清楚后，将项目拆分为细粒度任务：</p>

<pre><code class="language-text">对docs/specs/中的每个模块，拆分为函数级任务。
- 每个任务必须包含：
  - 明确需求（如"实现消息摘要的压缩功能"）。
  - 至少3个测试用例（如test_empty_messages_returns_empty_string）。
  - 验证方法（如"运行pytest确保100%覆盖率"）。
- 生成progress.json文件跟踪任务状态。</code></pre>

<p>最终得到<strong>443个任务</strong>，每个都有精确的验收标准。示例任务：</p>

<pre><code class="language-text">## 任务154：消息摘要压缩
- 需求：实现summarize_messages(messages, model)
- 测试用例：
  1. test_summarize_single_message_returns_text
  2. test_empty_messages_returns_empty_string
  3. test_fallback_truncation_when_model_fails
- 验证：运行pytest --cov=agents，确保覆盖率>=90%</code></pre>

<h2>3. 第二步：用goal命令长时间运行</h2>

<p>Claude Code的<code>goal</code>命令实现循环执行——模型从<code>progress.json</code>取任务、执行、迭代更新状态。</p>

<pre><code class="language-text">/goal 遍历docs/plans中的所有任务，直到python check_progress.py返回0。
- 读取progress.json获取第一个待处理任务。
- 执行任务中定义的所有测试用例（至少3个）。
- 如果测试失败（RED），停止并标记为失败。
- 如果测试通过（GREEN），运行ruff check和ruff format --check；修复问题。
- 用git commit --task=N提交更改。
- 更新progress.json（done、completed+1、rounds+1）。
- 如果check_progress.py返回0则停止；否则继续。</code></pre>

<p>在Claude Code中执行：</p>

<pre><code class="language-bash">/bypass permissions on
/goal &lt;提示词文本&gt;</code></pre>

<p>在13+小时运行期间，模型处理代码生成、<code>pytest</code>自动化测试、<code>ruff</code>代码检查、按任务git提交和<code>progress.json</code>进度跟踪。</p>

<h2>4. 第三步：验证与迭代</h2>

<p>执行完成后验证输出：</p>

<ul>
<li><strong>Web聊天</strong>：<code>http://localhost:8080</code>可用的聊天界面。</li>
<li><strong>技能执行</strong>：运行预装技能如图片生成。</li>
<li><strong>工具使用</strong>：获取网页内容并保存到本地文件。</li>
</ul>

<p>如果出现问题（如重复执行任务），直接提示：</p>

<pre><code class="language-text">Agent在重复执行历史任务。修复循环逻辑避免重复。</code></pre>

<p>GLM 5.2改进的指令遵循能力确保大多数修复一次到位。</p>

<h2>常见问题</h2>

<h3>除了GLM 5.2，可以用其他模型吗？</h3>
<p>可以，任何上下文窗口足够大的模型都能胜任。关键是在长会话中保持连贯性不"跑偏"。<a href="/zh/tools/claude">Claude</a>自家的Opus和Sonnet模型也擅长长上下文任务，只是定价结构不同。GLM 5.2的百万Token窗口使其在马拉松式编码任务中性价比特别高。你也可以尝试Gemini 2.5 Pro或GPT-5，它们都提供大上下文窗口。</p>

<h3>模型陷入死循环怎么办？</h3>
<p>这是循环执行的真实风险。缓解措施：(1) 在<code>goal</code>提示词中设置最大轮次限制；(2) 用progress.json检测同一任务多次尝试未完成的情况；(3) 定期检查长时间运行的会话。上述<code>check_progress.py</code>脚本应包含守卫逻辑，同一任务连续失败N次后退出。</p>

<h3>这种方法适合生产代码还是仅限实验？</h3>
<p>取决于风险级别。对于工具函数和数据格式化等低风险模块，AI生成代码配合自动化测试可以达到生产就绪水平。对于安全关键代码（认证、支付处理），应将AI生成与人工代码审查结合。443个任务的OpenClaw移植项目证明，AI可以处理大部分机械性翻译工作，让开发者专注于架构决策和安全审计。把它当作初级开发者的产出对待——充分测试、审查关键路径、迭代改进。</p>

<div class="next-step">
<p><strong>下一篇：</strong> <a href="/zh/article/codex-domestic-ai-models">Codex搭配国产AI模型使用指南：人人都能用的实操教程 →</a></p>
</div>`,
  },
"""

last_brace = content_src.rfind('};')
content_new = content_src[:last_brace] + article1_content + article2_content + '\n};\n'

with open('src/lib/article-content.ts', 'w', encoding='utf-8') as f:
    f.write(content_new)

print('Part 2: 2 article contents added to article-content.ts')
print('\nAll done! 0 new tools, 2 new articles.')
