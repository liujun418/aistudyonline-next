"""
Publish June 24, 2026 articles.
0 new tools — all referenced tools/concepts already exist or are patterns.
"""

import os

BASE = r"C:\Users\jun\aistudyonline-next"
os.chdir(BASE)

# ===== Part 1: Add 2 article metadata to articles.ts =====
with open('src/lib/articles.ts', 'r', encoding='utf-8') as f:
    articles_src = f.read()

new_articles = r"""  {
    slug: "mastering-ai-agent-tool-orchestration-meta-tools",
    title: "Mastering AI Agent Tool Orchestration: The Power of Meta-Tools in Modern Workflows",
    titleZh: "掌握AI Agent工具编排：Meta-Tools在现代工作流中的力量",
    description: "How meta-tools like web-tools-guide dominate AI skill marketplaces by solving tool orchestration — with a practical 4-step framework for primary tool selection, fallback mechanisms, user transparency, and bilingual trigger coverage, achieving 10x cost reduction.",
    descriptionZh: "Meta-Tools如web-tools-guide如何通过解决工具编排问题主导AI技能市场——包含主工具选择、降级机制、用户透明度和双语触发覆盖的4步实操框架，实现10倍成本降低。",
    category: "ai-tutorials",
    tags: ["agent", "tool-orchestration", "meta-tools", "workflow", "cost-optimization", "fallback"],
    difficulty: "intermediate",
    toolsMentioned: [],
    date: "2026-06-24",
  },
  {
    slug: "effective-multi-agent-collaboration-4-structures",
    title: "Effective Multi-Agent Collaboration: 4 Practical Structures Beyond Just Scaling Agents",
    titleZh: "高效多Agent协作：超越简单堆量的4种实用结构",
    description: "Stop just adding more agents — learn 4 proven collaboration structures (Orchestrator-Workers, Pipeline, Parallelization, Evaluator-Optimizer) with actionable code examples in Python, and when to use multi-agent vs single-agent approaches.",
    descriptionZh: "停止简单添加更多Agent——学习4种经过验证的协作结构（Orchestrator-Workers、Pipeline、Parallelization、Evaluator-Optimizer），附可操作的Python代码示例，以及何时使用多Agent vs 单Agent的决策指南。",
    category: "ai-tutorials",
    tags: ["multi-agent", "collaboration", "orchestrator", "pipeline", "parallelization", "evaluator-optimizer"],
    difficulty: "intermediate",
    toolsMentioned: ["claude", "minimax-m3"],
    date: "2026-06-24",
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

new_contents = r'''
  "mastering-ai-agent-tool-orchestration-meta-tools": {
    content: `<div class="meta-banner">
<p><strong>📅 Published:</strong> June 24, 2026 · <strong>🏷️ Category:</strong> AI Tutorials · <strong>📊 Level:</strong> Intermediate · <strong>🛠️ Concepts:</strong> Meta-Tools, Tool Orchestration, Agent Workflows</p>
</div>

<p>In the rapidly evolving landscape of AI agents, the sheer number of available tools can be overwhelming. However, the true game-changer isn't just having more tools — it's knowing <strong>when and how to use them effectively</strong>. This article dives into the concept of "meta-tools" like <code>web-tools-guide</code>, which dominate skill marketplaces by solving the critical problem of tool orchestration.</p>

<h2>The Rise of Meta-Tools: Doing Nothing to Achieve Everything</h2>

<p>Most AI skills focus on <em>doing tasks</em> — generating code, creating documents, or analyzing data. But <code>web-tools-guide</code>, the top-downloaded skill on many AI platforms, does something entirely different: <strong>it doesn't perform any task directly</strong>. Instead, it acts as a <em>dispatcher</em>, deciding which tool (e.g., <code>web_search</code>, <code>web_fetch</code>, <code>opencli</code>, <code>browser</code>) an AI agent should use for a given scenario.</p>

<h3>Why Meta-Tools Matter</h3>

<ul>
<li><strong>Efficiency:</strong> Reduce token usage and execution time by choosing the right tool first.</li>
<li><strong>Cost-Effectiveness:</strong> Avoid wasting resources on redundant or ill-suited tools.</li>
<li><strong>Reliability:</strong> Handle failures gracefully with predefined fallback strategies.</li>
</ul>

<h2>A Practical Framework for Tool Orchestration</h2>

<p>To implement effective tool orchestration, follow this four-step decision tree, inspired by the <code>web-tools-guide</code> paradigm:</p>

<h3>Step 1: Primary Tool Selection (React Paradigm)</h3>

<p>Start with the most efficient tool for the task:</p>

<pre><code class="language-python">def select_primary_tool(query, context):
    if "url" not in context:
        return "web_search"  # Use web search for keyword queries
    elif is_static_document(context["url"]):
        return "web_fetch"   # Fetch static content directly
    else:
        return "opencli"     # Fall back to structured CLI access</code></pre>

<h3>Step 2: Fallback Mechanisms</h3>

<p>If the primary tool fails, define clear degradation paths:</p>

<pre><code class="language-python">def execute_with_fallbacks(tool, query, context):
    try:
        return run_tool(tool, query, context)
    except WebSearchError:
        return execute_with_fallbacks("opencli", query, context)
    except OpenCliError:
        return execute_with_fallbacks("browser", query, context)
    except Exception as e:
        return f"Error: {str(e)}. Please check your request or try again."</code></pre>

<h3>Step 3: User Transparency</h3>

<p>Never let failures happen in silence. Inform users at every step:</p>

<pre><code class="language-python">def run_tool(tool, query, context):
    if tool == "web_search":
        print(f"Searching for: {query}...")
    elif tool == "opencli":
        print(f"Fetching structured data for: {context['url']}...")</code></pre>

<h3>Step 4: Bilingual Trigger Coverage</h3>

<p>Ensure your tool triggers work for both Chinese and English users:</p>

<pre><code class="language-python">trigger_keywords = {
    "中文": ["搜索", "上网", "查资料", "打开网站"],
    "English": ["web search", "fetch", "browser", "open website"]
}

def detect_trigger(query):
    for lang, keywords in trigger_keywords.items():
        for keyword in keywords:
            if keyword in query:
                return lang, keyword
    return "English", "web search"  # Default</code></pre>

<h2>Real-World Impact: A Cost and Time Comparison</h2>

<p>Let's compare two approaches to fetching Weibo hot searches:</p>

<h3>Approach 1: <code>opencli</code> (Efficient Path)</h3>

<pre><code class="language-bash">opencli weibo hotsearch --format json</code></pre>

<ul>
<li><strong>Time:</strong> ~2 seconds</li>
<li><strong>Token Usage:</strong> ~50 tokens</li>
<li><strong>Output:</strong> Structured JSON ready for AI processing.</li>
</ul>

<h3>Approach 2: <code>browser</code> (Fallback Path)</h3>

<pre><code class="language-python">from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://weibo.com")
# Manually parse HTML for hot searches...
driver.quit()</code></pre>

<ul>
<li><strong>Time:</strong> ~15 seconds</li>
<li><strong>Token Usage:</strong> ~500 tokens</li>
<li><strong>Output:</strong> Raw HTML requiring further parsing.</li>
</ul>

<p>By prioritizing <code>opencli</code> over <code>browser</code>, <code>web-tools-guide</code> reduces costs and delays by <strong>10x</strong> — a massive difference in production environments.</p>

<h2>Building Your Own Meta-Tool: Best Practices</h2>

<ol>
<li><strong>Document Failure Paths Explicitly:</strong> List every possible error and its resolution.</li>
<li><strong>Enforce Tool Ordering:</strong> Define a strict priority list for tools: <code>["web_search", "web_fetch", "opencli", "browser"]</code>.</li>
<li><strong>Include Bilingual Triggers:</strong> Cover both Chinese and English to maximize usability.</li>
</ol>

<pre><code class="language-python">tool_priority = ["web_search", "web_fetch", "opencli", "browser"]

triggers = {
    "search": {"zh": "搜索", "en": "web search"},
    "browse": {"zh": "打开网站", "en": "open website"}
}</code></pre>

<h2>常见问题</h2>

<h3>What's the difference between a meta-tool and a regular AI skill?</h3>
<p>A regular skill <em>does</em> something — generates text, analyzes data, creates images. A meta-tool <em>decides</em> which tool to use. It's the dispatcher, not the worker. Think of it as a traffic controller: it doesn't drive any cars, but without it, everything crashes. The value of a meta-tool scales with the number of tools in your ecosystem — the more tools you have, the more valuable smart orchestration becomes.</p>

<h3>Can I use this pattern with Claude Code's built-in tools?</h3>
<p>Yes. Claude Code already has built-in tools like <code>WebSearch</code>, <code>WebFetch</code>, and <code>Bash</code>. A meta-tool layer on top would decide: "This query needs a live web search" vs "This URL is static documentation — just fetch it" vs "This requires executing a command." The orchestration logic described here maps directly to how Claude Code's agent loop already works internally — understanding the pattern helps you write better prompts that guide the model toward efficient tool choices.</p>

<h3>Is 10x cost reduction realistic?</h3>
<p>Yes, in specific scenarios. The Weibo example is real: using a CLI tool (~50 tokens, 2s) vs launching a full browser (~500 tokens, 15s) gives ~10x savings on both dimensions. The savings compound when your agent makes dozens of tool calls per task. However, the meta-tool itself consumes some tokens for orchestration logic — the net savings come from avoiding even one expensive wrong tool choice per session.</p>

<div class="next-step">
<p><strong>下一篇：</strong> <a href="/en/article/effective-multi-agent-collaboration-4-structures">Effective Multi-Agent Collaboration: 4 Practical Structures Beyond Just Scaling Agents →</a></p>
</div>`,
    contentZh: `<div class="meta-banner">
<p><strong>📅 发布日期：</strong>2026年6月24日 · <strong>🏷️ 分类：</strong>AI教程 · <strong>📊 难度：</strong>中级 · <strong>🛠️ 概念：</strong>Meta-Tools、工具编排、Agent工作流</p>
</div>

<p>在AI Agent快速发展的领域中，可用工具的数量可能让人眼花缭乱。然而，真正的游戏规则改变者不只是拥有更多工具——而是知道<strong>何时以及如何有效使用它们</strong>。本文深入探讨"Meta-Tools"概念，如主导技能市场的<code>web-tools-guide</code>，它解决了工具编排这一关键问题。</p>

<h2>Meta-Tools的崛起：以"无为"成就"无不为"</h2>

<p>大多数AI技能专注于<em>执行任务</em>——生成代码、创建文档或分析数据。但<code>web-tools-guide</code>这个许多AI平台上下载量最高的技能，做的却是完全不同的事：<strong>它不直接执行任何任务</strong>。相反，它充当<em>调度器</em>，决定AI Agent在给定场景下应使用哪个工具（如<code>web_search</code>、<code>web_fetch</code>、<code>opencli</code>、<code>browser</code>）。</p>

<h3>Meta-Tools为何重要</h3>

<ul>
<li><strong>效率：</strong>通过首次选对工具减少token消耗和执行时间。</li>
<li><strong>成本效益：</strong>避免在冗余或不合适的工具上浪费资源。</li>
<li><strong>可靠性：</strong>通过预定义的降级策略优雅处理失败。</li>
</ul>

<h2>工具编排的实操框架</h2>

<p>要实现有效的工具编排，遵循这个受<code>web-tools-guide</code>启发的四步决策树：</p>

<h3>步骤1：主工具选择（React范式）</h3>

<p>从最高效的工具开始：</p>

<pre><code class="language-python">def select_primary_tool(query, context):
    if "url" not in context:
        return "web_search"  # 关键词查询用网页搜索
    elif is_static_document(context["url"]):
        return "web_fetch"   # 静态内容直接抓取
    else:
        return "opencli"     # 降级到结构化CLI访问</code></pre>

<h3>步骤2：降级机制</h3>

<p>主工具失败时定义清晰的降级路径：</p>

<pre><code class="language-python">def execute_with_fallbacks(tool, query, context):
    try:
        return run_tool(tool, query, context)
    except WebSearchError:
        return execute_with_fallbacks("opencli", query, context)
    except OpenCliError:
        return execute_with_fallbacks("browser", query, context)
    except Exception as e:
        return f"错误: {str(e)}。请检查您的请求或重试。"</code></pre>

<h3>步骤3：用户透明</h3>

<p>绝不让失败静默发生。每一步都通知用户：</p>

<pre><code class="language-python">def run_tool(tool, query, context):
    if tool == "web_search":
        print(f"正在搜索: {query}...")
    elif tool == "opencli":
        print(f"正在获取结构化数据: {context['url']}...")</code></pre>

<h3>步骤4：双语触发覆盖</h3>

<p>确保工具触发器同时支持中英文用户：</p>

<pre><code class="language-python">trigger_keywords = {
    "中文": ["搜索", "上网", "查资料", "打开网站"],
    "English": ["web search", "fetch", "browser", "open website"]
}</code></pre>

<h2>真实效果：成本和时间对比</h2>

<p>对比两种获取微博热搜的方法：</p>

<h3>方案1：<code>opencli</code>（高效路径）</h3>

<pre><code class="language-bash">opencli weibo hotsearch --format json</code></pre>

<ul>
<li><strong>时间：</strong>约2秒</li>
<li><strong>Token消耗：</strong>约50 tokens</li>
<li><strong>输出：</strong>结构化JSON，AI可直接处理。</li>
</ul>

<h3>方案2：<code>browser</code>（降级路径）</h3>

<pre><code class="language-python">from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://weibo.com")
# 手动解析HTML获取热搜...
driver.quit()</code></pre>

<ul>
<li><strong>时间：</strong>约15秒</li>
<li><strong>Token消耗：</strong>约500 tokens</li>
<li><strong>输出：</strong>原始HTML需要进一步解析。</li>
</ul>

<p>通过优先使用<code>opencli</code>而非<code>browser</code>，<code>web-tools-guide</code>将成本和延迟降低了<strong>10倍</strong>——在生产环境中这是巨大的差异。</p>

<h2>构建自己的Meta-Tool：最佳实践</h2>

<ol>
<li><strong>明确记录失败路径：</strong>列出每种可能的错误及其解决方案。</li>
<li><strong>强制执行工具排序：</strong>定义严格的工具优先级列表：<code>["web_search", "web_fetch", "opencli", "browser"]</code>。</li>
<li><strong>包含双语触发器：</strong>覆盖中英文以最大化可用性。</li>
</ol>

<pre><code class="language-python">tool_priority = ["web_search", "web_fetch", "opencli", "browser"]

triggers = {
    "search": {"zh": "搜索", "en": "web search"},
    "browse": {"zh": "打开网站", "en": "open website"}
}</code></pre>

<h2>常见问题</h2>

<h3>Meta-Tool和普通AI技能有什么区别？</h3>
<p>普通技能<em>做</em>某事——生成文本、分析数据、创建图像。Meta-Tool<em>决定</em>使用哪个工具。它是调度器，不是执行者。把它想象成交警：它不开任何车，但没有它一切都会撞车。Meta-Tool的价值随你生态系统中工具数量的增加而放大——工具越多，智能编排就越有价值。</p>

<h3>能在Claude Code的内置工具中使用这种模式吗？</h3>
<p>可以。Claude Code已有内置工具如<code>WebSearch</code>、<code>WebFetch</code>和<code>Bash</code>。Meta-Tool层会在上面决定："这个查询需要实时网页搜索" vs "这个URL是静态文档——直接抓取" vs "这需要执行命令"。这里描述的编排逻辑直接映射到Claude Code Agent循环的内部工作方式——理解这种模式有助于你编写更好的提示，引导模型做出高效的工具选择。</p>

<h3>10倍成本降低现实吗？</h3>
<p>在特定场景下是的。微博的例子是真实的：使用CLI工具（约50 tokens，2秒）vs启动完整浏览器（约500 tokens，15秒）在两个维度上都带来约10倍的节省。当你的Agent每个任务进行数十次工具调用时，节省会累积。不过，Meta-Tool本身会消耗一些token用于编排逻辑——净节省来自于避免每次会话中哪怕一次昂贵的错误工具选择。</p>

<div class="next-step">
<p><strong>下一篇：</strong> <a href="/zh/article/effective-multi-agent-collaboration-4-structures">高效多Agent协作：超越简单堆量的4种实用结构 →</a></p>
</div>`,
  },

  "effective-multi-agent-collaboration-4-structures": {
    content: `<div class="meta-banner">
<p><strong>📅 Published:</strong> June 24, 2026 · <strong>🏷️ Category:</strong> AI Tutorials · <strong>📊 Level:</strong> Intermediate · <strong>🛠️ Tools:</strong> Claude Code, MiniMax M3</p>
</div>

<p>In the realm of AI agents, merely increasing the number of agents doesn't equate to effective collaboration. True productivity lies in structured coordination. This article dives into four practical multi-agent structures, complete with actionable code examples, to help you leverage agent collaboration for real-world tasks.</p>

<h2>Why "More Agents" Isn't Synonymous with "Collaboration"</h2>

<p>Opening multiple agent sessions side by side doesn't mean they're working together. For instance, in a development scenario, you might have one agent fixing bugs, another running tests, and others handling frontend and backend tasks. Without shared context, the bug-fixing agent might be unaware that the testing agent has already encountered the same bug, leading to redundant work.</p>

<p>To achieve true collaboration, three core elements must be defined:</p>

<ul>
<li><strong>Division of Labor:</strong> Who is responsible for what task?</li>
<li><strong>Handover Protocol:</strong> How do agents exchange outputs?</li>
<li><strong>Decision Authority:</strong> Who has the final say in disputes or next steps?</li>
</ul>

<h2>4 Practical Multi-Agent Structures for Real-World Use</h2>

<h3>1. Orchestrator-Workers: Dynamic Task Allocation</h3>

<p>This structure is ideal when a single agent can't handle a large task, and the sub-tasks aren't known in advance.</p>

<ul>
<li><strong>How It Works:</strong> A central orchestrator agent analyzes the main task and dynamically splits it into sub-tasks, assigning each to a specialized worker agent. Once all workers complete their tasks, the orchestrator consolidates the results.</li>
</ul>

<pre><code class="language-python"># Main orchestrator logic
def orchestrate_large_task(task):
    sub_tasks = analyze_and_split_task(task)  # Split into, e.g., "debug_error", "scan_code", "run_tests"
    results = []
    for sub_task in sub_tasks:
        # Launch a SubAgent with independent context for each sub-task
        sub_agent = SubAgent(
            api_key="your_api_key",
            context=sub_task,
            model="M3"
        )
        result = sub_agent.run()
        results.append(result)
    return consolidate_results(results)</code></pre>

<ul>
<li><strong>Key Insight:</strong> Sub-tasks are allocated on the fly, and workers only return summarized conclusions to the orchestrator, keeping context manageable.</li>
</ul>

<h3>2. Pipeline: Sequential Task Handover</h3>

<p>Use this when a task can be broken into fixed, sequential steps (e.g., "write code → review code → test code").</p>

<ul>
<li><strong>How It Works:</strong> The output of one agent becomes the input of the next, creating a linear workflow.</li>
</ul>

<pre><code class="language-python"># Agent 1: Write code
def write_code(task):
    code = generate_code(task)
    push_to_git(code, "feature-branch")
    return "Code pushed to feature-branch"

# Agent 2: Review code
def review_code(git_link):
    code = pull_from_git(git_link)
    feedback = analyze_code_quality(code)
    push_feedback(feedback, "feedback-branch")
    return "Feedback pushed to feedback-branch"

# Agent 3: Test code
def test_code(feedback_link):
    feedback = pull_from_git(feedback_link)
    test_results = run_tests(feedback)
    return test_results</code></pre>

<ul>
<li><strong>Best Practice:</strong> Define a fixed output format for each step (e.g., JSON with <code>task_completed</code>, <code>output</code>, and <code>notes</code>) to ensure smooth handover.</li>
</ul>

<h3>3. Parallelization: Simultaneous, Independent Work</h3>

<p>This structure shines when a task can be split into independent sub-tasks that can run concurrently (e.g., developing frontend and backend modules separately).</p>

<ul>
<li><strong>How It Works:</strong> Split the main task into non-overlapping sub-tasks and assign each to a separate agent. Once all agents finish, merge their outputs.</li>
</ul>

<pre><code class="language-python">from concurrent.futures import ThreadPoolExecutor

def parallel_development(task):
    sub_tasks = split_into_independent_tasks(task)  # e.g., "frontend", "backend", "tests"
    results = []
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(run_agent, sub_task) for sub_task in sub_tasks]
        for future in futures:
            results.append(future.result())
    return merge_results(results)

def run_agent(sub_task):
    agent = Agent(api_key="your_api_key", task=sub_task, model="M3")
    return agent.execute()</code></pre>

<ul>
<li><strong>Critical Check:</strong> Ensure sub-tasks are truly independent. If two agents modify the same logic, merging will fail. Use Git worktrees or environment isolation to prevent conflicts.</li>
</ul>

<h3>4. Evaluator-Optimizer: Iterative Refinement</h3>

<p>Use this when you need to verify and improve an agent's output (e.g., "generate a report → critique it → revise it").</p>

<ul>
<li><strong>How It Works:</strong> One agent produces an initial output, a separate evaluator agent critiques it, and the original agent (or a new one) revises based on the feedback. This loops until the output meets standards.</li>
</ul>

<pre><code class="language-python">def iterative_improvement(task):
    # Agent 1: Generate initial output
    generator = Agent(api_key="your_api_key", role="generator", task=task)
    output = generator.execute()

    # Agent 2: Evaluate output
    evaluator = Agent(
        api_key="your_api_key",
        role="evaluator",
        task=f"Critique this output: {output}"
    )
    feedback = evaluator.execute()

    # Agent 1: Revise based on feedback
    revised_output = generator.execute(f"Revise based on feedback: {feedback}")
    return revised_output</code></pre>

<ul>
<li><strong>Must-Do:</strong> Keep the evaluator agent's context independent from the generator's. Sharing context reduces the evaluator's objectivity.</li>
</ul>

<h2>When to Use Multi-Agent vs. Single-Agent</h2>

<ul>
<li><strong>Read-Heavy Tasks</strong> (e.g., research, data scraping, code scanning): Multi-agent parallelization is efficient.</li>
<li><strong>Write-Heavy Tasks</strong> (e.g., code generation, creative writing): A single agent with well-managed context is often more stable, as multi-agent handovers can introduce inconsistencies.</li>
</ul>

<h2>Actionable Workflow for Your Tasks</h2>

<ol>
<li><strong>Define Collaboration Basics:</strong> Clarify who does what, how outputs are handed over, and who makes final decisions.</li>
<li><strong>Assess Task Divisibility:</strong> Determine if the task can be split into independent or sequential steps.</li>
<li><strong>Choose the Right Structure:</strong> Pick from Orchestrator-Workers, Pipeline, Parallelization, or Evaluator-Optimizer (or stick with a single agent if it suffices).</li>
</ol>

<p>By focusing on structure rather than just quantity, you can turn a crowd of agents into a cohesive, productive team.</p>

<h2>常见问题</h2>

<h3>Which structure should I start with for a typical development project?</h3>
<p>Start with <strong>Pipeline</strong> for code generation tasks (write → review → test). It's the simplest to implement and debug because the handover points are fixed. Once you're comfortable, add <strong>Parallelization</strong> for independent modules (frontend + backend simultaneously). Save Orchestrator-Workers for complex, unpredictable tasks where you genuinely don't know the sub-task breakdown upfront.</p>

<h3>How do I prevent agents from overwriting each other's work in Parallelization mode?</h3>
<p>Three techniques: (1) Use Git worktrees so each agent has its own isolated filesystem, (2) assign each agent a non-overlapping file/module scope in the prompt, (3) have a dedicated merge agent that resolves conflicts after all parallel agents complete. The Git worktree approach is the most robust — each agent works in <code>.claude/worktrees/agent-N/</code> and only the merge agent touches the main branch.</p>

<h3>When is single-agent better than multi-agent?</h3>
<p>Single-agent wins when: (1) the task requires deep context that's expensive to replicate across agents, (2) the output needs stylistic consistency (creative writing, UI design), (3) the task is small enough that coordination overhead exceeds execution time. A good rule of thumb: if explaining the task to multiple agents takes longer than doing it with one, stick with single-agent.</p>

<div class="next-step">
<p><strong>Previous:</strong> <a href="/en/article/mastering-ai-agent-tool-orchestration-meta-tools">Mastering AI Agent Tool Orchestration: The Power of Meta-Tools in Modern Workflows ←</a></p>
</div>`,
    contentZh: `<div class="meta-banner">
<p><strong>📅 发布日期：</strong>2026年6月24日 · <strong>🏷️ 分类：</strong>AI教程 · <strong>📊 难度：</strong>中级 · <strong>🛠️ 工具：</strong>Claude Code、MiniMax M3</p>
</div>

<p>在AI Agent领域，仅仅增加Agent数量并不等于有效协作。真正的生产力在于结构化协调。本文深入探讨四种实用的多Agent结构，附完整的可操作代码示例，帮助你利用Agent协作完成真实任务。</p>

<h2>为什么"更多Agent"不等于"协作"</h2>

<p>同时打开多个Agent会话并不意味它们在一起工作。例如，在开发场景中，你可能有一个Agent修Bug，另一个跑测试，还有处理前后端任务的。没有共享上下文，修Bug的Agent可能不知道测试Agent已经遇到了同样的Bug，导致重复工作。</p>

<p>要实现真正的协作，必须定义三个核心要素：</p>

<ul>
<li><strong>分工：</strong>谁负责什么任务？</li>
<li><strong>交接协议：</strong>Agent之间如何交换输出？</li>
<li><strong>决策权：</strong>谁在争议或下一步决策中有最终决定权？</li>
</ul>

<h2>4种实用多Agent结构</h2>

<h3>1. Orchestrator-Workers（编排器-工作者）：动态任务分配</h3>

<p>当单个Agent无法处理大型任务，且子任务事先未知时，此结构最合适。</p>

<ul>
<li><strong>工作原理：</strong>中央编排器Agent分析主任务并动态拆分为子任务，分配给专门的工作者Agent。所有工作者完成后，编排器整合结果。</li>
</ul>

<pre><code class="language-python"># 主编排器逻辑
def orchestrate_large_task(task):
    sub_tasks = analyze_and_split_task(task)  # 拆分为如"debug_error"、"scan_code"、"run_tests"
    results = []
    for sub_task in sub_tasks:
        # 为每个子任务启动独立上下文的SubAgent
        sub_agent = SubAgent(
            api_key="your_api_key",
            context=sub_task,
            model="M3"
        )
        result = sub_agent.run()
        results.append(result)
    return consolidate_results(results)</code></pre>

<ul>
<li><strong>关键洞察：</strong>子任务动态分配，工作者只向编排器返回摘要结论，保持上下文可控。</li>
</ul>

<h3>2. Pipeline（流水线）：顺序任务交接</h3>

<p>当任务可分解为固定的顺序步骤时使用（如"写代码→审代码→测代码"）。</p>

<ul>
<li><strong>工作原理：</strong>一个Agent的输出成为下一个Agent的输入，形成线性工作流。</li>
</ul>

<pre><code class="language-python"># Agent 1: 写代码
def write_code(task):
    code = generate_code(task)
    push_to_git(code, "feature-branch")
    return "代码已推送到 feature-branch"

# Agent 2: 审查代码
def review_code(git_link):
    code = pull_from_git(git_link)
    feedback = analyze_code_quality(code)
    push_feedback(feedback, "feedback-branch")
    return "反馈已推送到 feedback-branch"

# Agent 3: 测试代码
def test_code(feedback_link):
    feedback = pull_from_git(feedback_link)
    test_results = run_tests(feedback)
    return test_results</code></pre>

<ul>
<li><strong>最佳实践：</strong>为每一步定义固定输出格式（如包含<code>task_completed</code>、<code>output</code>和<code>notes</code>的JSON），确保顺利交接。</li>
</ul>

<h3>3. Parallelization（并行化）：同时独立工作</h3>

<p>当任务可拆分为能并发运行的独立子任务时（如分别开发前后端模块）。</p>

<ul>
<li><strong>工作原理：</strong>将主任务拆分为不重叠的子任务，分配给不同Agent。全部完成后合并输出。</li>
</ul>

<pre><code class="language-python">from concurrent.futures import ThreadPoolExecutor

def parallel_development(task):
    sub_tasks = split_into_independent_tasks(task)  # 如"frontend"、"backend"、"tests"
    results = []
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(run_agent, sub_task) for sub_task in sub_tasks]
        for future in futures:
            results.append(future.result())
    return merge_results(results)</code></pre>

<ul>
<li><strong>关键检查：</strong>确保子任务真正独立。如果两个Agent修改同一逻辑，合并会失败。使用Git worktree或环境隔离防止冲突。</li>
</ul>

<h3>4. Evaluator-Optimizer（评估器-优化器）：迭代精炼</h3>

<p>当需要验证和改进Agent输出时使用（如"生成报告→批评→修订"）。</p>

<ul>
<li><strong>工作原理：</strong>一个Agent产出初始结果，独立评估Agent批评它，原Agent（或新Agent）基于反馈修订。循环直到输出达标。</li>
</ul>

<pre><code class="language-python">def iterative_improvement(task):
    # Agent 1: 生成初始输出
    generator = Agent(api_key="your_api_key", role="generator", task=task)
    output = generator.execute()

    # Agent 2: 评估输出
    evaluator = Agent(
        api_key="your_api_key",
        role="evaluator",
        task=f"批评此输出: {output}"
    )
    feedback = evaluator.execute()

    # Agent 1: 基于反馈修订
    revised_output = generator.execute(f"基于反馈修订: {feedback}")
    return revised_output</code></pre>

<ul>
<li><strong>必须做到：</strong>保持评估Agent的上下文与生成Agent独立。共享上下文会降低评估者的客观性。</li>
</ul>

<h2>何时用多Agent vs 单Agent</h2>

<ul>
<li><strong>读密集型任务</strong>（研究、数据抓取、代码扫描）：多Agent并行化效率高。</li>
<li><strong>写密集型任务</strong>（代码生成、创意写作）：管理好上下文的单Agent通常更稳定，因为多Agent交接可能引入不一致。</li>
</ul>

<h2>可操作的工作流程</h2>

<ol>
<li><strong>定义协作基础：</strong>明确谁做什么、输出如何交接、谁做最终决策。</li>
<li><strong>评估任务可拆分性：</strong>确定任务能否拆分为独立或顺序步骤。</li>
<li><strong>选择合适的结构：</strong>从Orchestrator-Workers、Pipeline、Parallelization或Evaluator-Optimizer中选择（单Agent够用就单Agent）。</li>
</ol>

<p>聚焦结构而非数量，你能将一群Agent转变为有凝聚力的高效团队。</p>

<h2>常见问题</h2>

<h3>典型开发项目应该从哪种结构开始？</h3>
<p>从<strong>Pipeline</strong>开始用于代码生成任务（写→审→测）。它最容易实现和调试，因为交接点是固定的。熟练后，为独立模块（前后端同时开发）添加<strong>Parallelization</strong>。将Orchestrator-Workers留给复杂、不可预测的任务——那些你事先真不知道子任务如何拆分的场景。</p>

<h3>如何防止Agent在Parallelization模式下互相覆盖工作？</h3>
<p>三种技术：(1)使用Git worktree让每个Agent有独立的文件系统，(2)在提示中为每个Agent分配不重叠的文件/模块范围，(3)设置专门的合并Agent在所有并行Agent完成后解决冲突。Git worktree方法最稳健——每个Agent在<code>.claude/worktrees/agent-N/</code>中工作，只有合并Agent接触主分支。</p>

<h3>什么时候单Agent优于多Agent？</h3>
<p>单Agent胜出的场景：(1)任务需要深度上下文，跨Agent复制成本高，(2)输出需要风格一致性（创意写作、UI设计），(3)任务小到协调开销超过执行时间。一个好的经验法则：如果向多个Agent解释任务的时间比用一个Agent完成还长，就用单Agent。</p>

<div class="next-step">
<p><strong>上一篇：</strong> <a href="/zh/article/mastering-ai-agent-tool-orchestration-meta-tools">掌握AI Agent工具编排：Meta-Tools在现代工作流中的力量 ←</a></p>
</div>`,
  },

'''

last_brace = content_src.rfind('};')
content_new = content_src[:last_brace] + new_contents + '};'

with open('src/lib/article-content.ts', 'w', encoding='utf-8') as f:
    f.write(content_new)

print('Part 2: 2 article contents added to article-content.ts')

print('\n=== All done! Run build to verify ===')
