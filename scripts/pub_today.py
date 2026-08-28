"""Publish Aug 28, 2026 — 1 article (7 Agent Architectures decision guide), no new tools."""
import os

BASE = r"C:\Users\jun\aistudyonline-next"
os.chdir(BASE)

SLUG = "how-to-choose-right-agent-architecture-7-mainstream"

# ---------------------------------------------------------------------------
# Part 1: articles.ts
# ---------------------------------------------------------------------------
a = r"""  {
    slug: "how-to-choose-right-agent-architecture-7-mainstream",
    title: "How to Choose the Right Agent Architecture: 7 Mainstream Architectures from Lightweight to Enterprise-Grade",
    titleZh: "如何选择正确的Agent架构：从轻量到企业级的7大主流架构",
    description: "80% of teams pick ReAct or Multi-Agent just because those are the only two they've heard of. This decision guide builds a coordinate system for choosing among 7 mainstream agent architectures — Single Agent, ReAct, Plan and Execute, Multi-Agent, Route + Skill, Blackboard, and Graph Workflow — covering the pros, cons, and fit of each, plus the full evolution line from lightweight to enterprise-grade.",
    descriptionZh: "80%的团队选择ReAct或多Agent，仅仅因为只听说过这两个。本决策指南建立一套坐标系，帮助你在7大主流Agent架构——单Agent、ReAct、计划与执行、多Agent、路由+技能、黑板、图工作流——中做出选择，涵盖各自优缺点与适用场景，以及从轻量到企业级的完整演进线。",
    category: "ai-comparisons",
    tags: ["AI Agent", "Architecture", "ReAct", "Multi-Agent", "Route Skill", "Graph Workflow", "Blackboard", "Enterprise"],
    difficulty: "intermediate",
    toolsMentioned: [],
    date: "2026-08-28",
  },
"""
with open("src/lib/articles.ts", encoding="utf-8") as f:
    s = f.read()
last = s.rfind("];")
assert last != -1, "articles.ts: ]; marker not found"
s2 = s[:last] + a + s[last:]
with open("src/lib/articles.ts", "w", encoding="utf-8", newline="\n") as f:
    f.write(s2)
print("articles.ts updated")

# ---------------------------------------------------------------------------
# Part 2: article-content.ts
# ---------------------------------------------------------------------------
content = r"""  "how-to-choose-right-agent-architecture-7-mainstream": {
    content: `<div class="meta-banner">
  <span class="meta-badge">⚖️ AI Comparisons</span>
  <span class="meta-badge">🕒 8 min read</span>
  <span class="meta-badge">📅 Aug 28, 2026</span>
  <span class="meta-badge">🎯 Intermediate</span>
</div>

<h2 id="introduction">Introduction</h2>

<p>When building an agent system from scratch, 80% of people choose ReAct or Multi-Agent — not because those fit their scenario, but because those are the only two architectures they have ever heard of. Today we will thoroughly compare the 7 mainstream agent architectures, from the most lightweight to those used in enterprise-level production environments. After reading this article, you will know exactly which tier your business should choose.</p>

<h2 id="coordinate-system">Three Core Conclusions to Establish a Coordinate System</h2>

<h3>1. There is no unified standard for agent architecture</h3>
<p>The choice of architecture only depends on two things: the <strong>complexity of the scenario</strong> and the <strong>required level of control</strong>.</p>

<h3>2. The evolution path of agent architectures</h3>
<p>The evolution path runs from <strong>Single Agent → Multi-Agent Collaboration → Graph-based Workflow</strong>.</p>

<h3>3. Route + Skill is the current optimal practice</h3>
<p>For the AI Coding and skill-system directions, <strong>Route + Skill</strong> is currently the relatively optimal practice.</p>

<h2 id="single-agent">1. Single Agent Architecture</h2>
<p>A single large model handles all tasks: user input → LLM thinking → tool invocation → result output. Typical example: early ChatGPT.</p>
<ul>
  <li><strong>Pros</strong>: simple to implement, low cost, low latency.</li>
  <li><strong>Cons</strong>: cognitive overload when tasks get complex, prone to context pollution.</li>
</ul>
<p><strong>Suitable for</strong>: simple dialogue verification scenarios. <strong>Not suitable for</strong>: complex multi-task parallel processing.</p>

<h2 id="react">2. ReAct Architecture</h2>
<p>Core concept: <strong>Reason + Act</strong>. It works in a cycle — think → act → observe → result → think again — until the task is complete.</p>
<ul>
  <li><strong>Pros</strong>: complete chain-of-reasoning, good interpretability.</li>
  <li><strong>Cons</strong>: high token consumption, not stable enough (easy to drift off task), unsuitable for large-scale engineering systems.</li>
</ul>
<p><strong>Suitable for</strong>: multi-step exploration tasks. <strong>Not suitable for</strong>: production systems that need predictable behavior.</p>

<h2 id="plan-execute">3. Plan and Execute Architecture</h2>
<p>An engineering-oriented approach: plan first, then execute.</p>
<ul>
  <li><strong>Plan phase</strong>: generate a complete multi-step plan.</li>
  <li><strong>Execute phase</strong>: implement each step according to the plan.</li>
  <li><strong>Pros</strong>: high stability, great for long processes, code generation, and long-running automation.</li>
  <li><strong>Cons</strong>: if the plan is wrong, the whole task fails; less flexible than ReAct.</li>
</ul>
<p><strong>Suitable for</strong>: engineering tasks with a clear structure. <strong>Not suitable for</strong>: open-ended problems that need constant re-planning.</p>

<h2 id="multi-agent">4. Multi-Agent Architecture</h2>
<p>Multiple agents work together with a division of labor. A coordination and allocation layer at the top manages the work, while planner, reviewer, executor and other role agents sit at the bottom, each with its own responsibility.</p>
<ul>
  <li><strong>Pros</strong>: clear task decomposition, low context pollution, strong scalability.</li>
  <li><strong>Cons</strong>: high cost.</li>
</ul>
<p><strong>Suitable for</strong>: complex industry scenarios with strict process consistency requirements — financial risk control, medical diagnosis, legal review.</p>

<h2 id="route-skill">5. Route + Skill Architecture</h2>
<p>This is the most recommended architecture today. The core idea: instead of letting the model think, let the model <strong>choose</strong>.</p>
<p>The flow: user input → Intent Router recognizes the intent → directly routes to the matching Skill for execution. Each Skill is an executable capability bundled with its own knowledge.</p>
<ul>
  <li><strong>Pros</strong>: extremely stable, enterprise-level controllable and cacheable, high performance, hit rate is easy to evaluate.</li>
  <li><strong>Cons</strong>: high skill-design cost, possible routing conflicts.</li>
</ul>
<p><strong>Suitable for</strong>: AI Coding and intelligent system fields.</p>

<h2 id="blackboard">6. Blackboard System</h2>
<p>Multiple agents can read and write shared state at the same time, and execution is driven by state changes.</p>
<ul>
  <li><strong>Pros</strong>: fits complex collaboration scenarios.</li>
  <li><strong>Cons</strong>: very heavy state management, difficult to track problems.</li>
</ul>
<p><strong>Commonly used in</strong>: workflow engines like LangGraph and distributed systems.</p>

<h2 id="graph-workflow">7. Graph Workflow Architecture</h2>
<p>The heaviest but most stable architecture for enterprise production environments — it orchestrates workflows based on directed acyclic graphs (DAGs).</p>
<ul>
  <li><strong>Pros</strong>: supports conditional branching, parallel execution, backtracking, and retry; enterprise-grade stability and debuggability; built for long processes.</li>
</ul>
<p><strong>Common tools</strong>: LangGraph, Temporal, n8n, Prefect.</p>

<h2 id="evolution-line">The Entire Evolution Line</h2>

<pre><code class="language-text">Single Agent      →  Simple verification
ReAct             →  Multi-step exploration
Plan + Execute    →  Engineering
Multi-Agent       →  Collaboration
Route + Skill     →  Precise skill systems
Blackboard        →  Shared state
Graph Workflow    →  Production</code></pre>

<p>You don't need to implement all these architectures at once — just choose the one that matches the complexity of your scenario.</p>

<h2 id="conclusion">Conclusion</h2>
<p>Remember one sentence: <strong>there is no best architecture, only the most suitable one</strong>.</p>
<p>Start by mapping your scenario's complexity and control requirements onto the coordinate system, then walk the evolution line from left to right until you find the tier that matches. For most AI Coding and skill-system products, Route + Skill gives the best stability-to-effort ratio; for enterprise production pipelines with strict SLAs, Graph Workflow is the safe choice.</p>

<h2>常见问题</h2>

<h3>Why do most people default to ReAct or Multi-Agent?</h3>
<p>Because those are the two architectures most tutorial content covers, so they are the first two people learn. But "popular" is not the same as "suitable" — ReAct burns tokens and drifts on long tasks, while Multi-Agent multiplies cost. Before picking either, run your scenario through the coordinate system: complexity and control level first, architecture second.</p>

<h3>What's the difference between this guide and the earlier 7-architecture breakdown?</h3>
<p>The earlier guide (<a href="/article/7-mainstream-agent-architectures-beginner-enterprise-guide">7 Mainstream Agent Architectures: From Beginner to Enterprise-Grade Guide</a>) explains how each architecture is built — its mechanics, internals, and typical components. This guide is the decision layer on top: it gives you the coordinate system, the per-architecture fit, and the evolution-line decision map, so you can pick the right one instead of just understanding them.</p>

<h3>When should I choose Route + Skill over a single ReAct agent?</h3>
<p>Whenever your use case is a set of well-defined capabilities rather than open-ended reasoning — AI Coding, skill libraries, and productized assistants. ReAct lets the model think freely but is unstable and expensive; Route + Skill replaces free thinking with a predictable intent router, giving you enterprise-level stability, caching, and measurable hit rates. The cost is upfront skill design.</p>

<h3>Is Graph Workflow always the final answer for enterprise?</h3>
<p>For production pipelines with strict reliability requirements — conditional branching, parallel execution, retries, audit trails — yes, DAG-based Graph Workflows (LangGraph, Temporal, n8n, Prefect) are the industry standard. But if your scenario is a simple dialog or a small skill set, adopting Graph Workflow is over-engineering. Start light, escalate only when the complexity justifies it.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Ready to apply this decision framework? Go deeper:</p>
  <ul>
    <li><a href="/article/7-mainstream-agent-architectures-beginner-enterprise-guide">7 Mainstream Agent Architectures: From Beginner to Enterprise-Grade Guide</a> — understand how each of the 7 architectures is actually built</li>
    <li><a href="/article/effective-multi-agent-collaboration-4-structures">Effective Multi-Agent Collaboration: 4 Practical Structures Beyond Just Scaling Agents</a> — design real multi-agent teams once you choose that tier</li>
    <li><a href="/article/mastering-ai-agent-tool-orchestration-meta-tools">Mastering AI Agent Tool Orchestration: The Power of Meta-Tools in Modern Workflows</a> — the tool layer that makes Route + Skill and ReAct agents actually work</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">⚖️ AI 对比</span>
  <span class="meta-badge">🕒 阅读约8分钟</span>
  <span class="meta-badge">📅 2026年8月28日</span>
  <span class="meta-badge">🎯 进阶</span>
</div>

<h2 id="introduction">引言</h2>

<p>从零搭建Agent系统时，80%的人会选择ReAct或多Agent——不是因为它们适合你的场景，而是因为只听说过这两个。今天我们将彻底对比7种主流Agent架构，从最轻量的到企业级生产环境所用的。读完本文，你会清楚自己的业务应该选择哪一层。</p>

<h2 id="coordinate-system">三个核心结论：建立坐标系</h2>

<h3>1. Agent架构没有统一标准</h3>
<p>架构的选择只取决于两件事：<strong>场景的复杂度</strong>和<strong>所需的控制程度</strong>。</p>

<h3>2. Agent架构的演进路径</h3>
<p>演进路径为：<strong>单Agent → 多Agent协作 → 基于图的工作流</strong>。</p>

<h3>3. Route + Skill是目前相对最优实践</h3>
<p>在AI Coding和技能系统方向上，<strong>Route + Skill</strong>是目前相对最优的实践。</p>

<h2 id="single-agent">1. 单Agent架构</h2>
<p>一个大模型处理所有任务：用户输入 → 大模型思考 → 工具调用 → 结果输出。典型例子：早期ChatGPT。</p>
<ul>
  <li><strong>优点</strong>：实现简单、成本低、延迟低。</li>
  <li><strong>缺点</strong>：任务复杂时认知过载，容易产生上下文污染。</li>
</ul>
<p><strong>适用</strong>：简单对话验证场景。<strong>不适用</strong>：复杂多任务并行处理。</p>

<h2 id="react">2. ReAct架构</h2>
<p>核心概念：<strong>推理+行动（Reason + Act）</strong>。它循环运行——思考 → 行动 → 观察 → 结果 → 再次思考——直到任务完成。</p>
<ul>
  <li><strong>优点</strong>：完整的链式推理能力，可解释性好。</li>
  <li><strong>缺点</strong>：Token消耗高，不够稳定（容易偏离任务），不适合大规模工程系统。</li>
</ul>
<p><strong>适用</strong>：多步骤探索类任务。<strong>不适用</strong>：需要可预测行为的生产系统。</p>

<h2 id="plan-execute">3. 计划与执行架构</h2>
<p>工程化思路：先计划，后执行。</p>
<ul>
  <li><strong>计划阶段</strong>：生成完整的多步骤计划。</li>
  <li><strong>执行阶段</strong>：按计划逐步实现。</li>
  <li><strong>优点</strong>：稳定性高，适合长流程、代码生成和长时自动化。</li>
  <li><strong>缺点</strong>：计划出错则整个任务失败；灵活性不如ReAct。</li>
</ul>
<p><strong>适用</strong>：结构清晰的工程任务。<strong>不适用</strong>：需要不断重新规划的开放式问题。</p>

<h2 id="multi-agent">4. 多Agent架构</h2>
<p>多个Agent分工协作。顶层有任务协调与分配系统统筹工作，底层有规划者、审查者、执行者等角色Agent，各司其职。</p>
<ul>
  <li><strong>优点</strong>：任务分解清晰、上下文污染低、可扩展性强。</li>
  <li><strong>缺点</strong>：成本高。</li>
</ul>
<p><strong>适用</strong>：对流程一致性要求极高的复杂行业场景——金融风控、医疗诊断、法律审查。</p>

<h2 id="route-skill">5. 路由+技能架构</h2>
<p>这是目前最推荐的架构。核心思想：不让模型思考，让模型<strong>选择</strong>。</p>
<p>流程：用户输入 → 意图路由器识别意图 → 直接路由到对应技能执行。每个技能都是一个可执行能力，并附带相应知识。</p>
<ul>
  <li><strong>优点</strong>：极其稳定、企业级可控可缓存、性能高、命中率易评估。</li>
  <li><strong>缺点</strong>：技能设计成本高，可能存在路由冲突。</li>
</ul>
<p><strong>适用</strong>：AI Coding和智能系统领域。</p>

<h2 id="blackboard">6. 黑板系统</h2>
<p>多个Agent可同时读写共享状态，执行由状态变化驱动。</p>
<ul>
  <li><strong>优点</strong>：适合复杂协作场景。</li>
  <li><strong>缺点</strong>：状态管理非常重，问题难以追踪。</li>
</ul>
<p><strong>常用于</strong>：LangGraph等工作流引擎和分布式系统。</p>

<h2 id="graph-workflow">7. 图工作流架构</h2>
<p>企业级生产环境中最重但最稳定的架构——基于有向无环图（DAG）编排工作流。</p>
<ul>
  <li><strong>优点</strong>：支持条件分支、并行执行、回溯与重试；企业级稳定、可调试、适合长流程。</li>
</ul>
<p><strong>常用工具</strong>：LangGraph、Temporal、n8n、Prefect。</p>

<h2 id="evolution-line">完整演进线</h2>

<pre><code class="language-text">单Agent          →  简单验证
ReAct            →  多步探索
计划+执行        →  工程化
多Agent          →  协作
路由+技能        →  精准技能系统
黑板             →  共享状态
图工作流         →  生产环境</code></pre>

<p>你不需要一次性实现所有这些架构——只需根据场景复杂度选择合适的那一个。</p>

<h2 id="conclusion">结语</h2>
<p>记住一句话：<strong>没有最好的架构，只有最合适的架构</strong>。</p>
<p>先把自己的场景复杂度和控制需求映射到坐标系上，再从演进线左到右逐个对照，直到找到匹配的那一层。对大多数AI Coding和技能系统产品，Route + Skill的稳定性/投入比最高；对SLA严格的企事业生产管线，图工作流是稳妥之选。</p>

<h2>常见问题</h2>

<h3>为什么大多数人默认选ReAct或多Agent？</h3>
<p>因为这两者是教程内容覆盖最多的架构，也是人们最先学到的两个。但"流行"不等于"适合"——ReAct在长任务上烧Token且易漂移，多Agent则成本倍增。在二选一之前，先用坐标系过一遍你的场景：先定复杂度与控制级别，再定架构。</p>

<h3>本指南与之前的7大架构拆解有什么区别？</h3>
<p>之前的指南（<a href="/article/7-mainstream-agent-architectures-beginner-enterprise-guide">7大主流Agent架构：从入门到企业级完整指南</a>）讲解每种架构如何构建——机制、内部结构、典型组件。本指南是叠加在它之上的决策层：给你坐标系、每种架构的适用性，以及演进线决策地图，让你不仅能理解它们，还能选对它们。</p>

<h3>什么情况下该选Route + Skill而不是单个ReAct Agent？</h3>
<p>只要你的用例是一组明确定义的能力而非开放式推理——比如AI Coding、技能库、产品化助手。ReAct让模型自由思考但不够稳定且成本高；Route + Skill用可预测的意图路由器取代自由思考，带来企业级稳定性、可缓存性和可衡量的命中率。代价是需要前置的技能设计投入。</p>

<h3>图工作流永远是企业的最终答案吗？</h3>
<p>对于可靠性要求严格的生产管线——条件分支、并行执行、重试、审计追踪——是的，基于DAG的图工作流（LangGraph、Temporal、n8n、Prefect）是行业标准。但如果你的场景只是一个简单对话或小型技能集，上图工作流就是过度设计。从轻量起步，只有当复杂度真正需要时才升级。</p>

<div class="next-step">
  <h3>📖 继续学习</h3>
  <p>准备应用这套决策框架？深入探索：</p>
  <ul>
    <li><a href="/article/7-mainstream-agent-architectures-beginner-enterprise-guide">7大主流Agent架构：从入门到企业级完整指南</a> — 理解7种架构各自如何构建</li>
    <li><a href="/article/effective-multi-agent-collaboration-4-structures">高效多Agent协作：超越简单堆量的4种实用结构</a> — 选定该层级后，设计真正的多Agent团队</li>
    <li><a href="/article/mastering-ai-agent-tool-orchestration-meta-tools">掌握AI Agent工具编排：Meta-Tools在现代工作流中的力量</a> — 让Route + Skill和ReAct真正跑起来的工具层</li>
  </ul>
</div>`,
  },
"""
with open("src/lib/article-content.ts", encoding="utf-8") as f:
    s = f.read()
last = s.rfind("};")
assert last != -1, "article-content.ts: }; marker not found"
s2 = s[:last] + content + s[last:]
with open("src/lib/article-content.ts", "w", encoding="utf-8", newline="\n") as f:
    f.write(s2)
print("article-content.ts updated")
print("Done. Article:", SLUG)
