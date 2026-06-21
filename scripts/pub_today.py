"""
Publish June 21, 2026 articles.
0 new tools needed — graphify already exists; other references are plugins/concepts.
"""

import os

BASE = r"C:\Users\jun\aistudyonline-next"
os.chdir(BASE)

# ===== Part 1: Add 2 article metadata to articles.ts =====
with open('src/lib/articles.ts', 'r', encoding='utf-8') as f:
    articles_src = f.read()

new_articles = r"""  {
    slug: "6-practical-claude-code-plugins",
    title: "6 Practical Claude Code Plugins for Boosting Productivity in Real Projects",
    titleZh: "6个实用的Claude Code插件：真实项目中提升效率",
    description: "Discover 6 underrated yet highly practical Claude Code plugins — Grill Me, Codex, Graphify, Claude Obsidian, NotebookLM CLI, and Impeccable — that solve real development problems from planning to frontend polish.",
    descriptionZh: "发现6个被低估但极其实用的Claude Code插件——Grill Me、Codex、Graphify、Claude Obsidian、NotebookLM CLI和Impeccable——从规划到前端美化解决真实开发问题。",
    category: "ai-tutorials",
    tags: ["claude-code", "plugins", "productivity", "code-review", "graphify"],
    difficulty: "intermediate",
    toolsMentioned: ["claude", "codex", "graphify"],
    date: "2026-06-21",
  },
  {
    slug: "demystifying-ai-engineering-function-calling-skills-mcp",
    title: "Demystifying AI Engineering: Function Calling, Skills, and MCP",
    titleZh: "揭秘AI工程：Function Calling、Skills和MCP的层次架构",
    description: "A clear breakdown of the three core AI engineering concepts — Function Calling (microscopic action layer), Skills (mesoscopic module layer), and MCP (macroscopic integration layer) — with practical code examples.",
    descriptionZh: "清晰拆解AI工程三大核心概念——Function Calling（微观动作层）、Skills（中观模块层）和MCP（宏观集成层）——附实战代码示例。",
    category: "ai-basics",
    tags: ["function-calling", "skills", "mcp", "ai-engineering", "architecture"],
    difficulty: "intermediate",
    toolsMentioned: [],
    date: "2026-06-21",
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
  // ====== Article: 6 Practical Claude Code Plugins ======
  "6-practical-claude-code-plugins": {
    content: `
<div class="meta-banner">
  <span>📅 2026-06-21</span>
  <span>📂 <a href="/en/learn/ai-tutorials">AI Tutorials</a></span>
  <span>⏱️ 7 min read</span>
  <span>⚡ Intermediate</span>
</div>

<p><a href="/en/tools/claude">Claude Code</a> has emerged as one of the most powerful AI coding assistants, and its plugin ecosystem is growing at an astonishing pace. New plugins pop up almost daily, each claiming to revolutionize your workflow. But many lack real-world utility. Here are 6 underrated yet highly practical Claude Code plugins that actually deliver.</p>

<h2>1. Grill Me / Grill with Docs: Enhanced Planning & Alignment</h2>

<p>One of the most common pitfalls in AI-assisted development is <strong>misalignment</strong> — thinking the AI understands your requirements only to find out it doesn't. The Grill Me and Grill with Docs plugins solve this by acting as an enhanced planning mode.</p>

<p>Trigger it with:</p>

<pre><code class="language-text">/plan + grill me</code></pre>

<p>This plugin prompts you with questions like:</p>
<ul>
<li>Who is the target user?</li>
<li>What are the edge cases?</li>
<li>What constitutes failure?</li>
<li>Do we need to reference docs?</li>
</ul>

<p>By answering these questions, you and <a href="/en/tools/claude">Claude Code</a> reach a consensus before writing any code. Compared to the default plan mode (which only asks about goals, scope, and timeline), Grill Me digs deeper, ensuring both parties are truly aligned.</p>

<h2>2. Official Codex Plugin: Code Review & Enhancement</h2>

<p>The official <a href="/en/tools/codex">Codex</a> plugin is a hidden gem for Claude Code users. It lets you perform code reviews and even adversarial analysis directly within the terminal.</p>

<p>Basic code review:</p>

<pre><code class="language-text">claude plugins run codex
codex review</code></pre>

<p>For a more in-depth adversarial review (which challenges your implementation from unexpected angles):</p>

<pre><code class="language-text">codex adversarial-review</code></pre>

<p>Another useful command is <code>codex rescue</code>, which lets Codex independently handle specific features:</p>

<pre><code class="language-text">codex rescue feature/auth</code></pre>

<p>This plugin is ideal for checking code quality, finding bugs, and getting improvement suggestions. It's been available for months but remains underutilized in daily workflows.</p>

<h2>3. Graphify: Knowledge Graph for Code Repositories</h2>

<p><a href="/en/tools/graphify">Graphify</a> creates a visual knowledge graph for your code repositories, helping Claude Code answer questions about your codebase more efficiently with less token consumption.</p>

<p>Generate a knowledge graph:</p>

<pre><code class="language-text">/graphify</code></pre>

<p>For Obsidian users, generate an Obsidian vault:</p>

<pre><code class="language-text">/graphify --obsidian</code></pre>

<p>Graphify also has a <code>git commit</code> hook that automatically rebuilds the knowledge graph after each commit. This process is deterministic (no LLM involvement) and thus free of token costs. The knowledge graph acts as a map of "how and why code components connect," making it easier for Claude Code to navigate your codebase.</p>

<h2>4. Claude Obsidian: Structured Knowledge Base</h2>

<p>If you use Obsidian or need a long-term memory layer for <a href="/en/tools/claude">Claude Code</a>, the Claude Obsidian plugin is invaluable. It ingests your documents (notes, specs, meeting minutes), extracts entities and concepts, and organizes them into a structured Obsidian vault.</p>

<p>How it works:</p>
<ul>
<li>Extracts entities and cross-references.</li>
<li>Organizes them into a structured vault.</li>
<li>Maintains a hot cache of recent context, so you don't have to re-explain project history in each session.</li>
</ul>

<p>This isn't just about storing files — it's about building a continuously enriching knowledge base. Each time you add new material, the vault's relationships and content expand, allowing Claude Code to work with a structured knowledge framework instead of scattered documents.</p>

<h2>5. NotebookLM CLI: Seamless Google NotebookLM Integration</h2>

<p>NotebookLM from Google is a powerful tool for document summarization and analysis. The NotebookLM CLI plugin brings this functionality directly into Claude Code, eliminating manual web interactions.</p>

<p>Ask a question about your documents:</p>

<pre><code class="language-text">notebook-lm.py ask</code></pre>

<p>This plugin offloads document processing to NotebookLM, reducing token usage of Claude Code. It's especially useful for summarizing large documents or extracting insights, letting Claude Code focus on reasoning and execution.</p>

<h2>6. Impeccable: Polishing AI-Generated Frontends</h2>

<p>Impeccable is a frontend design enhancement tool designed to fix "AI slop" — messy UIs generated by AI. It comes with 23 commands for tasks like color correction, animation, and onboarding flows.</p>

<p>Improve UI styling:</p>

<pre><code class="language-text">impeccable colorize
impeccable animate</code></pre>

<p>Impeccable also offers a live mode — start a local dev server, point and click on UI elements, and modify them in real-time:</p>

<pre><code class="language-text">impeccable live</code></pre>

<p>The plugin provides visual before-and-after comparisons, making it easy to see the impact of each command. A must-have for anyone working on frontend projects with <a href="/en/tools/claude">Claude Code</a>.</p>

<h2>FAQ</h2>

<h3>Are these plugins free to use?</h3>
<p>Most are open-source and free. Grill Me, Graphify, Claude Obsidian, and Impeccable are community plugins available on GitHub. The Codex plugin requires a <a href="/en/tools/codex">Codex</a> account (free tier available). NotebookLM CLI requires a Google account with NotebookLM access (also free). None require paid subscriptions beyond what you might already have for the underlying services.</p>

<h3>How do I install these plugins in Claude Code?</h3>
<p>Plugin installation varies by plugin. Most community plugins are installed via <code>/plugin install &lt;name&gt;</code> in the Claude Code terminal. For GitHub-hosted plugins, you typically clone the repo and run an install script. Always check the plugin's README for specific installation instructions. The official Codex plugin can be installed through the plugin marketplace within Claude Code.</p>

<h3>Can I use multiple plugins simultaneously?</h3>
<p>Yes. Claude Code supports running multiple plugins concurrently. However, be mindful of context window usage — loading too many plugins at once can consume tokens and slow down responses. A good rule of thumb: activate plugins only when you need them for a specific task, rather than keeping everything loaded all the time.</p>

<div class="next-step">
<p><strong>Next Read:</strong> <a href="/en/article/demystifying-ai-engineering-function-calling-skills-mcp">Demystifying AI Engineering: Function Calling, Skills, and MCP →</a></p>
</div>`,
    contentZh: `
<div class="meta-banner">
  <span>📅 2026-06-21</span>
  <span>📂 <a href="/zh/learn/ai-tutorials">AI教程</a></span>
  <span>⏱️ 7 分钟阅读</span>
  <span>⚡ 中级</span>
</div>

<p><a href="/zh/tools/claude">Claude Code</a>已成为最强大的AI编程助手之一，其插件生态系统以惊人速度增长。新插件几乎每天出现，每个都声称能彻底改变你的工作流。但很多缺乏实际效用。以下是6个被低估但真正实用的Claude Code插件。</p>

<h2>1. Grill Me / Grill with Docs：增强规划与对齐</h2>

<p>AI辅助开发中最常见的陷阱之一是<strong>认知偏差</strong>——你以为AI理解了你的需求，结果发现它并没有。Grill Me和Grill with Docs插件通过增强规划模式来解决这个问题。</p>

<p>触发命令：</p>

<pre><code class="language-text">/plan + grill me</code></pre>

<p>插件会提示你回答：</p>
<ul>
<li>目标用户是谁？</li>
<li>边界情况有哪些？</li>
<li>什么算失败？</li>
<li>需要参考文档吗？</li>
</ul>

<p>通过回答这些问题，你和<a href="/zh/tools/claude">Claude Code</a>在写代码前达成共识。相比默认plan模式（只问目标、范围和时间线），Grill Me挖掘更深，确保双方真正对齐。</p>

<h2>2. 官方Codex插件：代码审查与增强</h2>

<p>官方<a href="/zh/tools/codex">Codex</a>插件是Claude Code用户的隐藏宝藏，可在终端内直接进行代码审查甚至对抗性分析。</p>

<p>基础代码审查：</p>

<pre><code class="language-text">claude plugins run codex
codex review</code></pre>

<p>更深入的对抗性审查（从意想不到的角度挑战你的实现）：</p>

<pre><code class="language-text">codex adversarial-review</code></pre>

<p>另一个有用命令 <code>codex rescue</code>，让Codex独立处理特定功能：</p>

<pre><code class="language-text">codex rescue feature/auth</code></pre>

<p>该插件适合检查代码质量、发现Bug和获取改进建议。已发布数月但日常使用率偏低。</p>

<h2>3. Graphify：代码仓库知识图谱</h2>

<p><a href="/zh/tools/graphify">Graphify</a>为代码仓库创建可视化知识图谱，帮助Claude Code更高效地回答代码库问题，减少Token消耗。</p>

<p>生成知识图谱：</p>

<pre><code class="language-text">/graphify</code></pre>

<p>为Obsidian用户生成Obsidian仓库：</p>

<pre><code class="language-text">/graphify --obsidian</code></pre>

<p>Graphify还有 <code>git commit</code> 钩子，每次提交后自动重建知识图谱。此过程是确定性的（无LLM参与），因此零Token成本。知识图谱如同"代码组件如何及为何连接"的地图，让Claude Code更轻松地导航代码库。</p>

<h2>4. Claude Obsidian：结构化知识库</h2>

<p>如果你使用Obsidian或需要<a href="/zh/tools/claude">Claude Code</a>的长期记忆层，Claude Obsidian插件非常宝贵。它摄入你的文档（笔记、规格、会议记录），提取实体和概念，组织成结构化Obsidian仓库。</p>

<p>工作原理：</p>
<ul>
<li>提取实体和交叉引用。</li>
<li>组织成结构化仓库。</li>
<li>维护最近上下文热缓存，无需每次会话重新解释项目历史。</li>
</ul>

<p>这不仅是存储文件——而是构建持续丰富的知识库。每次添加新材料，仓库的关系和内容都会扩展，让Claude Code基于结构化知识框架而非散乱文档工作。</p>

<h2>5. NotebookLM CLI：无缝集成Google NotebookLM</h2>

<p>Google的NotebookLM是强大的文档摘要和分析工具。NotebookLM CLI插件将此功能直接带入Claude Code，省去手动网页交互。</p>

<p>对文档提问：</p>

<pre><code class="language-text">notebook-lm.py ask</code></pre>

<p>此插件将文档处理卸载到NotebookLM，减少Claude Code的Token使用。特别适合摘要大文档或提取洞察，让Claude Code专注推理和执行。</p>

<h2>6. Impeccable：打磨AI生成的前端</h2>

<p>Impeccable是前端设计增强工具，专门修复"AI垃圾"——AI生成的混乱UI。提供23个命令，涵盖颜色校正、动画、引导流程等。</p>

<p>改善UI样式：</p>

<pre><code class="language-text">impeccable colorize
impeccable animate</code></pre>

<p>Impeccable还提供实时模式——启动本地开发服务器，点击UI元素，实时修改：</p>

<pre><code class="language-text">impeccable live</code></pre>

<p>插件提供可视化前后对比，轻松看到每个命令的效果。使用<a href="/zh/tools/claude">Claude Code</a>做前端项目的必备工具。</p>

<h2>常见问题</h2>

<h3>这些插件免费吗？</h3>
<p>大多数开源免费。Grill Me、Graphify、Claude Obsidian和Impeccable是GitHub上的社区插件。Codex插件需要<a href="/zh/tools/codex">Codex</a>账号（有免费版）。NotebookLM CLI需要Google账号和NotebookLM访问权限（也免费）。都不需要超出已有服务的付费订阅。</p>

<h3>如何在Claude Code中安装这些插件？</h3>
<p>安装方式因插件而异。大多数社区插件通过Claude Code终端中的 <code>/plugin install &lt;名称&gt;</code> 安装。GitHub托管的插件通常克隆仓库后运行安装脚本。始终查看插件的README获取具体安装说明。官方Codex插件可通过Claude Code内的插件市场安装。</p>

<h3>能同时使用多个插件吗？</h3>
<p>可以。Claude Code支持同时运行多个插件。但注意上下文窗口使用——一次加载太多插件会消耗Token并减慢响应。经验法则：仅在需要特定任务时激活插件，而非一直保持全部加载。</p>

<div class="next-step">
<p><strong>下一篇：</strong> <a href="/zh/article/demystifying-ai-engineering-function-calling-skills-mcp">揭秘AI工程：Function Calling、Skills和MCP的层次架构 →</a></p>
</div>`,
  },
"""

article2_content = r"""
  // ====== Article: Demystifying AI Engineering ======
  "demystifying-ai-engineering-function-calling-skills-mcp": {
    content: `
<div class="meta-banner">
  <span>📅 2026-06-21</span>
  <span>📂 <a href="/en/learn/ai-basics">AI Basics</a></span>
  <span>⏱️ 7 min read</span>
  <span>⚡ Intermediate</span>
</div>

<p>In the realm of AI engineering, three core concepts — <strong>Function Calling</strong>, <strong>Skills</strong>, and <strong>MCP</strong> — play pivotal roles in building robust and scalable AI applications. Let's break down each of them with practical insights and actionable code.</p>

<h2>1. Function Calling: The Foundational Mechanism</h2>

<p>Function Calling is not about AI models magically executing code on their own. Think of large language models (LLMs) as <strong>pure text engines running on GPUs</strong> — they have no inherent knowledge of your databases or APIs.</p>

<p>At its core, Function Calling is a <strong>structured output mechanism</strong>. Here's how it works:</p>

<ol>
<li>You provide the model with a <code>Schema</code> that defines your local function's structure.</li>
<li>The model processes natural language input, reasons about it, and outputs a JSON object that strictly adheres to the provided <code>Schema</code>.</li>
<li>Your local code is what actually executes the action.</li>
</ol>

<pre><code class="language-python"># Defining a Schema for a weather-checking function
weather_function_schema = {
    "name": "get_weather",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {"type": "string"},
            "date": {"type": "string", "format": "yyyy-mm-dd"}
        },
        "required": ["city", "date"]
    }
}

# Send the schema to the LLM and get a structured JSON response
llm_response = llm_client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "What's the weather in Tokyo tomorrow?"}],
    tools=[{"type": "function", "function": weather_function_schema}]
)

# Extract and execute the function call
function_call = llm_response.choices[0].message.tool_calls[0].function
weather_data = execute_local_function(function_call.name, function_call.arguments)</code></pre>

<p>Function Calling solves the problem of translating natural language intent into parameters your code can understand. It's like a single function in your codebase — fundamental but limited when used in isolation.</p>

<h2>2. Skills: Modularizing Business Capabilities</h2>

<p>While Function Calling is powerful, stuffing hundreds of individual function schemas into a single prompt leads to <strong>context overload</strong>, causing the model to crash or behave unpredictably. This is where Skills come in.</p>

<p>Skills are <strong>highly cohesive business capability modules</strong>. They package together:</p>

<ul>
<li>Specific prompts (e.g., DevOps guidelines).</li>
<li>Multiple Function Calls.</li>
<li>Even retry logic.</li>
</ul>

<p>Consider a <code>DevOps_Skill</code> module:</p>

<pre><code class="language-python">class DevOpsSkill:
    def __init__(self):
        self.log_schema = self._define_log_function_schema()
        self.git_schema = self._define_git_function_schema()
        self.monitoring_schema = self._define_monitoring_function_schema()
        self.prompt_template = "You are a DevOps assistant. Use tools: {question}"

    def _define_log_function_schema(self):
        return {
            "name": "query_logs",
            "parameters": {
                "type": "object",
                "properties": {"service": {"type": "string"}, "timeframe": {"type": "string"}},
                "required": ["service", "timeframe"]
            }
        }

    def execute(self, user_question):
        prompt = self.prompt_template.format(question=user_question)
        llm_response = llm_client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            tools=[{"type": "function", "function": self._get_relevant_schemas(user_question)}]
        )
        return self._process_llm_response(llm_response)</code></pre>

<p>By encapsulating related functionalities into a Skill, you avoid context overload and make your AI application more maintainable. Skills are like classes or toolkits in your code — they abstract complexity and promote reusability.</p>

<h2>3. MCP: The Standard Interface for AI Ecosystems</h2>

<p>Even with Function Calling and Skills, a critical pain point remains: <strong>system-level tight coupling</strong>. A Skill built for one AI platform often can't be reused on another — moving from a Python script to Claude or Cursor requires rewriting everything.</p>

<p><strong>MCP (Model Context Protocol)</strong> is the standard interface for AI. It decouples the LLM's reasoning "brain" from external tools and data:</p>

<ul>
<li>Your AI application acts as an <strong>MCP Client</strong>.</li>
<li>Your Skills, local files, or databases are wrapped as <strong>MCP Servers</strong>.</li>
<li>They communicate via a standardized protocol, enabling dynamic discovery of tools and data resources, and zero-adaptation code integration (plug-and-play).</li>
</ul>

<pre><code class="language-python"># MCP Server: Exposing a weather service
from mcp import MCPServer, register_tool

class WeatherMCPServer(MCPServer):
    @register_tool(name="get_weather", description="Get weather for a city")
    def get_weather(self, city: str, date: str) -> dict:
        return {"city": city, "date": date, "temperature": "25°C", "condition": "Sunny"}

server = WeatherMCPServer(host="localhost", port=8080)
server.start()

# MCP Client: Using the weather service
from mcp import MCPClient
client = MCPClient()
weather_data = client.call_tool("get_weather", {"city": "Tokyo", "date": "2026-10-31"})
print(weather_data)</code></pre>

<p>MCP eliminates "integration hell" by ensuring tools and data built for one platform work seamlessly across others.</p>

<h2>Putting It All Together: A Hierarchy of AI Engineering</h2>

<ul>
<li><strong>Function Calling</strong> is the <em>microscopic</em> action layer — translating intent to executable parameters.</li>
<li><strong>Skills</strong> are the <em>mesoscopic</em> module layer — packaging related capabilities for reusability.</li>
<li><strong>MCP</strong> is the <em>macroscopic</em> integration layer — enabling standardization and ecosystem interoperability.</li>
</ul>

<p>To build production-ready AI applications:</p>

<ol>
<li>Use Function Calling to handle granular actions.</li>
<li>Bundle related Function Calls and logic into Skills for maintainable business capabilities.</li>
<li>Adopt MCP to ensure your Skills and tools work across platforms and scale with the AI ecosystem.</li>
</ol>

<p>By leveraging these three concepts in tandem, you'll move beyond brittle, single-use AI scripts and build robust, scalable, and interoperable AI solutions.</p>

<h2>FAQ</h2>

<h3>What's the difference between Function Calling and MCP?</h3>
<p>Function Calling is a mechanism within a single LLM interaction — you define a schema, the model outputs structured JSON, and your code executes it. MCP is a broader protocol that standardizes how any AI application discovers and calls external tools across different platforms and languages. Think of Function Calling as a single API call, while MCP is the entire service architecture that makes those calls portable and interoperable. MCP often wraps Function Calling under the hood, but adds discovery, standardization, and cross-platform compatibility.</p>

<h3>Do I need MCP if I'm just building a simple AI app?</h3>
<p>For simple, single-purpose apps, Function Calling alone is sufficient. You only need MCP when you want your tools to be reusable across different AI platforms (Claude, Cursor, custom apps) or when building complex multi-tool systems. Start with Function Calling and Skills. When you find yourself rewriting the same tool integrations for different platforms, that's the signal to adopt MCP.</p>

<h3>How do Skills relate to Claude Code's plugin system?</h3>
<p><a href="/en/tools/claude">Claude Code</a>'s plugin system is essentially a Skills implementation. Each plugin packages prompts, tool schemas, and execution logic into a reusable module — exactly what Skills describe at the architectural level. The same principles apply whether you're building a Claude Code plugin, a LangChain tool, or a custom agent framework. Understanding the Skill concept helps you design better plugins regardless of the platform.</p>

<div class="next-step">
<p><strong>Next Read:</strong> <a href="/en/article/6-practical-claude-code-plugins">6 Practical Claude Code Plugins for Boosting Productivity →</a></p>
</div>`,
    contentZh: `
<div class="meta-banner">
  <span>📅 2026-06-21</span>
  <span>📂 <a href="/zh/learn/ai-basics">AI基础</a></span>
  <span>⏱️ 7 分钟阅读</span>
  <span>⚡ 中级</span>
</div>

<p>在AI工程领域，三个核心概念——<strong>Function Calling</strong>、<strong>Skills</strong>和<strong>MCP</strong>——在构建稳健可扩展的AI应用中扮演关键角色。让我们用实战代码逐一拆解。</p>

<h2>1. Function Calling：基础机制</h2>

<p>Function Calling不是AI模型自己变魔术般地执行代码。把大语言模型（LLM）想象成<strong>运行在GPU上的纯文本引擎</strong>——它们对你的数据库或API一无所知。</p>

<p>本质上，Function Calling是一种<strong>结构化输出机制</strong>：</p>

<ol>
<li>你给模型提供一个定义本地函数结构的 <code>Schema</code>。</li>
<li>模型处理自然语言输入，推理后输出严格遵循 <code>Schema</code> 的JSON对象。</li>
<li>你的本地代码才是真正执行动作的部分。</li>
</ol>

<pre><code class="language-python"># 定义天气查询函数的Schema
weather_function_schema = {
    "name": "get_weather",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {"type": "string"},
            "date": {"type": "string", "format": "yyyy-mm-dd"}
        },
        "required": ["city", "date"]
    }
}

# 将schema发送给LLM，获取结构化JSON响应
llm_response = llm_client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "明天东京天气怎么样？"}],
    tools=[{"type": "function", "function": weather_function_schema}]
)

# 提取并执行函数调用
function_call = llm_response.choices[0].message.tool_calls[0].function
weather_data = execute_local_function(function_call.name, function_call.arguments)</code></pre>

<p>Function Calling解决了将自然语言意图转化为代码可理解参数的问题。它像代码库中的单个函数——基础但单独使用时功能有限。</p>

<h2>2. Skills：模块化业务能力</h2>

<p>Function Calling虽然强大，但把数百个独立函数Schema塞进单个提示词会导致<strong>上下文过载</strong>，模型崩溃或行为不可预测。这就是Skills的用武之地。</p>

<p>Skills是<strong>高内聚的业务能力模块</strong>，打包了：</p>

<ul>
<li>特定提示词（如DevOps指南）。</li>
<li>多个Function Call。</li>
<li>甚至重试逻辑。</li>
</ul>

<p>以 <code>DevOps_Skill</code> 模块为例：</p>

<pre><code class="language-python">class DevOpsSkill:
    def __init__(self):
        self.log_schema = self._define_log_function_schema()
        self.git_schema = self._define_git_function_schema()
        self.monitoring_schema = self._define_monitoring_function_schema()
        self.prompt_template = "你是DevOps助手。使用工具回答：{question}"

    def _define_log_function_schema(self):
        return {
            "name": "query_logs",
            "parameters": {
                "type": "object",
                "properties": {"service": {"type": "string"}, "timeframe": {"type": "string"}},
                "required": ["service", "timeframe"]
            }
        }

    def execute(self, user_question):
        prompt = self.prompt_template.format(question=user_question)
        llm_response = llm_client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            tools=[{"type": "function", "function": self._get_relevant_schemas(user_question)}]
        )
        return self._process_llm_response(llm_response)</code></pre>

<p>将相关功能封装为Skill，避免上下文过载，让AI应用更易维护。Skills就像代码中的类或工具包——抽象复杂性，促进复用。</p>

<h2>3. MCP：AI生态系统的标准接口</h2>

<p>即使有了Function Calling和Skills，一个关键痛点仍然存在：<strong>系统级紧耦合</strong>。为一个AI平台构建的Skill通常无法复用到另一个——从Python脚本迁移到Claude或Cursor需要重写一切。</p>

<p><strong>MCP（Model Context Protocol）</strong>是AI的标准接口。它将LLM的推理"大脑"与外部工具和数据解耦：</p>

<ul>
<li>你的AI应用作为<strong>MCP Client</strong>。</li>
<li>你的Skills、本地文件或数据库包装为<strong>MCP Server</strong>。</li>
<li>通过标准化协议通信，实现工具和数据资源的动态发现、零适配代码集成（即插即用）。</li>
</ul>

<pre><code class="language-python"># MCP Server：暴露天气服务
from mcp import MCPServer, register_tool

class WeatherMCPServer(MCPServer):
    @register_tool(name="get_weather", description="查询城市天气")
    def get_weather(self, city: str, date: str) -> dict:
        return {"city": city, "date": date, "temperature": "25°C", "condition": "晴"}

server = WeatherMCPServer(host="localhost", port=8080)
server.start()

# MCP Client：使用天气服务
from mcp import MCPClient
client = MCPClient()
weather_data = client.call_tool("get_weather", {"city": "东京", "date": "2026-10-31"})
print(weather_data)</code></pre>

<p>MCP消除了"集成地狱"，确保为一个平台构建的工具和数据能无缝跨平台工作。</p>

<h2>三者关系：AI工程的层次架构</h2>

<ul>
<li><strong>Function Calling</strong> 是<em>微观</em>动作层——将意图转化为可执行参数。</li>
<li><strong>Skills</strong> 是<em>中观</em>模块层——打包相关能力实现复用。</li>
<li><strong>MCP</strong> 是<em>宏观</em>集成层——实现标准化和生态系统互操作。</li>
</ul>

<p>构建生产级AI应用：</p>

<ol>
<li>用Function Calling处理细粒度动作。</li>
<li>将相关Function Call和逻辑打包为Skills，实现可维护的业务能力。</li>
<li>采用MCP确保Skills和工具跨平台工作、随AI生态系统扩展。</li>
</ol>

<p>三者协同使用，你将超越脆弱的一次性AI脚本，构建稳健、可扩展、可互操作的AI解决方案。</p>

<h2>常见问题</h2>

<h3>Function Calling和MCP有什么区别？</h3>
<p>Function Calling是单次LLM交互中的机制——你定义Schema，模型输出结构化JSON，你的代码执行。MCP是更广泛的协议，标准化任何AI应用如何跨不同平台和语言发现和调用外部工具。Function Calling像单次API调用，MCP是使这些调用可移植和可互操作的整个服务架构。MCP底层常包装Function Calling，但增加了发现、标准化和跨平台兼容性。</p>

<h3>如果只构建简单AI应用，需要MCP吗？</h3>
<p>简单单一用途应用，Function Calling就够了。只有当你希望工具能跨不同AI平台（Claude、Cursor、自定义应用）复用，或构建复杂多工具系统时才需要MCP。从Function Calling和Skills开始。当你发现自己在为不同平台重写相同的工具集成时，就是采用MCP的信号。</p>

<h3>Skills与Claude Code的插件系统有什么关系？</h3>
<p><a href="/zh/tools/claude">Claude Code</a>的插件系统本质上就是Skills的实现。每个插件将提示词、工具Schema和执行逻辑打包成可复用模块——正是Skills在架构层面描述的内容。无论构建Claude Code插件、LangChain工具还是自定义Agent框架，原理相同。理解Skill概念有助于设计更好的插件，不限于特定平台。</p>

<div class="next-step">
<p><strong>下一篇：</strong> <a href="/zh/article/6-practical-claude-code-plugins">6个实用的Claude Code插件：真实项目中提升效率 →</a></p>
</div>`,
  },
"""

last_brace = content_src.rfind('};')
content_new = content_src[:last_brace] + article1_content + article2_content + '\n};\n'

with open('src/lib/article-content.ts', 'w', encoding='utf-8') as f:
    f.write(content_new)

print('Part 2: 2 article contents added to article-content.ts')
print('\nAll done! 0 new tools, 2 new articles.')
