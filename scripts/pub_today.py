"""Publish Aug 18, 2026 — 1 article, no new tools."""
import os; BASE = r"C:\Users\jun\aistudyonline-next"; os.chdir(BASE)

# ---------- Part 1: articles.ts metadata ----------
with open('src/lib/articles.ts', 'r', encoding='utf-8') as f: s = f.read()
a = r"""  {
    slug: "why-agents-need-self-evolution-practical-implementation-guide-ai-agents",
    title: "Why Agents Need Self-Evolution: Practical Implementation Guide for AI Agents",
    titleZh: "为什么Agent需要自我进化：AI Agent实用实现指南",
    description: "Static agents repeat the same mistakes and can't adapt when requirements change. A practical self-evolution guide — execution trace collection, self-reflection module, incremental prompt updates, a Python evolution-memory demo, and the pitfalls to avoid.",
    descriptionZh: "静态Agent重复犯同样的错误，需求变化时无法适应。一份实用的自我进化指南——执行轨迹收集、自我反思模块、增量提示词更新、Python进化记忆演示，以及需要避开的坑。",
    category: "ai-tutorials",
    tags: ["AI Agents", "Self-Evolution", "Prompt Engineering", "Agent Architecture", "Machine Learning", "Python", "Workflow"],
    difficulty: "intermediate",
    toolsMentioned: [],
    date: "2026-08-18",
  },

"""
last = s.rfind('];')
with open('src/lib/articles.ts', 'w', encoding='utf-8') as f: f.write(s[:last] + a + '];')
print('Part 1 done')

# ---------- Part 2: article-content.ts bilingual content ----------
with open('src/lib/article-content.ts', 'r', encoding='utf-8') as f: c = f.read()
n = r'''
  "why-agents-need-self-evolution-practical-implementation-guide-ai-agents": {
    content: `<div class="meta-banner">
  <span class="meta-badge">📖 AI Tutorial</span>
  <span class="meta-badge">🕒 7 min read</span>
  <span class="meta-badge">📅 Aug 18, 2026</span>
  <span class="meta-badge">🎯 Intermediate</span>
</div>

<h2 id="introduction">Introduction</h2>
<p>Regular AI agents follow fixed prompt rules and preset workflows. Once deployed, they keep repeating the same logic. When facing new tasks, changing business requirements or unseen edge cases, performance drops sharply. This is exactly why self-evolution becomes critical for modern AI agents.</p>
<p>Self-evolution means the agent can review its own execution records, find failures and weak points, update its prompts, tool usage strategies and workflow logic automatically, without manual modification from human developers every single time. It does not achieve super intelligence; it lets the agent learn from its past mistakes and get better after every task run.</p>

<h2 id="core-problems">Core Problems of Non-Evolving Static Agents</h2>
<ul>
  <li>Repeatedly makes identical mistakes on similar tasks</li>
  <li>Cannot adapt when task conditions change</li>
  <li>Tool calling sequences stay rigid, unable to optimize execution paths</li>
  <li>Human operators have to manually edit system prompts after every failure</li>
  <li>Scaling up agent workload brings heavy prompt maintenance overhead</li>
</ul>

<h2 id="three-layers">Three Key Layers of Agent Self-Evolution</h2>
<ol>
  <li><strong>Execution Trace Collection</strong>: Save complete logs including task input, tool calls, intermediate outputs, final results and success or failure status.</li>
  <li><strong>Self-Reflection Module</strong>: The agent analyzes historical logs, summarizes root causes for failed runs, figures out which steps went wrong.</li>
  <li><strong>Knowledge &amp; Prompt Update</strong>: Based on reflection conclusions, adjust system prompts, add new constraint rules or optimize tool calling sequences for future tasks.</li>
</ol>

<h2 id="prompt-template">Practical Prompt Template for Agent Self-Reflection Module</h2>
<p>Embed this prompt into your agent's post-task reflection workflow.</p>
<pre><code class="language-text">You are the self-reflection unit of this AI agent.
Review the complete task execution trace below.
1. Judge whether this task run succeeded or failed.
2. If failed, list concrete root causes: prompt flaw, improper tool selection, wrong calling order, missing constraints or insufficient background information.
3. Summarize 2-4 actionable optimization rules for future similar tasks.
4. Output updated prompt snippets that can fix above problems.
Do not generate vague descriptions. All conclusions must be supported by execution log facts.</code></pre>

<h2 id="python-demo">Minimal Python Demo for Self-Evolution Agent Log Handling</h2>
<pre><code class="language-python">class AgentEvolutionMemory:
    def __init__(self):
        self.execution_records = []
        self.optimized_rules = []

    def save_trace(self, task_input, tool_calls, final_output, is_success: bool):
        record = {
            "task": task_input,
            "tool_calls": tool_calls,
            "output": final_output,
            "success": is_success
        }
        self.execution_records.append(record)

    def add_optimized_rule(self, rule_text: str):
        self.optimized_rules.append(rule_text)

    def get_evolved_system_prompt(self, base_prompt: str) -> str:
        rule_block = "\n".join([f"- {r}" for r in self.optimized_rules])
        evolved_prompt = f"{base_prompt}\n\n=== Accumulated Evolution Rules ===\n{rule_block}"
        return evolved_prompt

# Usage example
memory = AgentEvolutionMemory()
memory.save_trace(
    task_input="Query sales data for last quarter",
    tool_calls=["query_database", "format_report"],
    final_output="Missing regional filter data",
    is_success=False
)
memory.add_optimized_rule("Always add region filter parameter when querying quarterly sales data.")
final_prompt = memory.get_evolved_system_prompt(base_prompt="You are a data analysis agent.")
print(final_prompt)</code></pre>

<h2 id="workflow">Real-World Operation Workflow</h2>
<ol>
  <li>The agent runs one task and stores the full execution trace into memory storage.</li>
  <li>Trigger the self-reflection module after task completion, whether success or failure.</li>
  <li>Reflection outputs actionable optimization rules, append them to the agent memory.</li>
  <li>Next-round task loads the evolved system prompt with accumulated rules.</li>
  <li>Periodically clean low-value old rules to prevent prompt bloat.</li>
</ol>

<h2 id="pitfalls">Common Pitfalls You Should Avoid</h2>
<ul>
  <li>Do not let the agent rewrite the whole base prompt, only append incremental optimization rules. Full rewriting may destroy core agent capabilities.</li>
  <li>Avoid over-fitting to one single failure case. Evaluate multiple similar traces before adding new rules.</li>
  <li>Set a maximum limit for rule quantity. Too many accumulated rules will cause prompt inflation and slow down inference speed.</li>
  <li>Keep human oversight. Important business rules still need manual review even with self-evolution enabled.</li>
</ul>

<h2 id="closing">Closing Thoughts</h2>
<p>Self-evolution does not make your agent omnipotent. It solves the pain point that static agents cannot improve automatically. With trace logging, self-reflection and incremental prompt update, your agent gets better continuously as it handles more real-world tasks, and greatly cuts down human prompt maintenance work.</p>

<h2>常见问题</h2>

<h3>What exactly does agent self-evolution mean?</h3>
<p>Self-evolution is the agent's ability to improve its own behavior from its execution history. After each task, the agent saves the full trace, runs a reflection module that analyzes why runs failed, and appends the resulting optimization rules to its system prompt. The next task loads the evolved prompt with those accumulated rules. It's not about becoming "super intelligent" — it's a practical feedback loop that lets the agent stop repeating the same mistakes without a human editing prompts after every failure.</p>

<h3>Does self-evolution require a special framework or a large language model?</h3>
<p>No special framework is required. The core requirement is an LLM capable of following a reflection prompt and a way to store execution traces — the Python demo in this guide is a self-contained memory class you can embed in any agent. What matters more is discipline: reliably saving traces, triggering reflection on both successes and failures, and capping the rule list so it doesn't bloat the prompt over time. A normal agent setup plus this feedback loop is enough to get started.</p>

<h3>How do I avoid the prompt from growing too large with accumulated rules?</h3>
<p>Three guardrails. First, only append incremental rules and never let the agent rewrite the whole base prompt. Second, require multiple similar failed traces before accepting a new rule — don't over-fit to a single case. Third, set a hard maximum on the rule count and periodically prune low-value or outdated rules. This keeps the evolved prompt focused and prevents the latency and cost that come with prompt inflation.</p>

<h3>Can I still trust the agent after it has evolved by itself?</h3>
<p>You should keep human oversight, especially for high-stakes business rules. Self-evolution optimizes prompts and tool-calling strategies, but it is not a substitute for review of important logic — the guide explicitly recommends manual review of critical rules even with evolution enabled. Use self-evolution to reduce the noise of constant manual prompt editing, while keeping a human check on the changes that matter most.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Want to make your agents smarter and more reliable? Continue with these guides:</p>
  <ul>
    <li><a href="/article/write-effective-agents-md-codex">How to Write an Effective AGENTS.md for Codex</a> — encode the base rules and context your agent must follow</li>
    <li><a href="/article/multi-agent-collaboration-architecture">Multi-Agent Collaboration Architecture</a> — how multiple agents share work and communicate</li>
    <li><a href="/article/deepseek-harness-comprehensive-guide-installation-architecture-practical-usage">DeepSeek Harness: A Comprehensive Guide to Installation, Architecture, and Practical Usage</a> — the runtime harness where evolving agents live</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">📖 AI教程</span>
  <span class="meta-badge">🕒 阅读约7分钟</span>
  <span class="meta-badge">📅 2026年8月18日</span>
  <span class="meta-badge">🎯 进阶</span>
</div>

<h2 id="introduction">引言</h2>
<p>普通的AI Agent遵循固定的提示词规则和预设工作流。一旦部署，它们就一直重复同样的逻辑。当遇到新任务、变化的业务需求或从未见过的边界情况时，性能会急剧下降。这正是自我进化对现代AI Agent至关重要的原因。</p>
<p>自我进化意味着Agent可以复盘自己的执行记录，发现失败和薄弱点，自动更新提示词、工具使用策略和工作流逻辑，而无需人类开发人员每次都手动修改。它不是获得超级智能，而是让Agent从过去的错误中学习，每执行一次任务就变得更好。</p>

<h2 id="core-problems">不进化静态Agent的核心问题</h2>
<ul>
  <li>在相似任务上反复犯同样的错误</li>
  <li>任务条件变化时无法适应</li>
  <li>工具调用序列僵硬，无法优化执行路径</li>
  <li>每次失败后操作员都要手动编辑系统提示词</li>
  <li>Agent负载扩展带来沉重的提示词维护开销</li>
</ul>

<h2 id="three-layers">Agent自我进化的三个关键层</h2>
<ol>
  <li><strong>执行轨迹收集</strong>：保存完整日志，包括任务输入、工具调用、中间输出、最终结果以及成功或失败状态。</li>
  <li><strong>自我反思模块</strong>：Agent分析历史日志，总结失败运行的根因，找出哪一步出了问题。</li>
  <li><strong>知识与提示词更新</strong>：基于反思结论，调整系统提示词、添加新的约束规则或优化未来任务的工具调用顺序。</li>
</ol>

<h2 id="prompt-template">Agent自我反思模块的实用提示词模板</h2>
<p>把这个提示词嵌入Agent的任务后反思工作流中。</p>
<pre><code class="language-text">你是这个AI Agent的自我反思单元。
审阅下面的完整任务执行轨迹。
1. 判断这次任务运行是成功还是失败。
2. 如果失败，列出具体根因：提示词缺陷、工具选择不当、调用顺序错误、缺少约束或背景信息不足。
3. 总结2-4条对未来相似任务可执行的优化规则。
4. 输出能够修复上述问题的更新提示词片段。
不要生成模糊的描述。所有结论都必须有执行日志事实支撑。</code></pre>

<h2 id="python-demo">自我进化Agent日志处理的最小Python演示</h2>
<pre><code class="language-python">class AgentEvolutionMemory:
    def __init__(self):
        self.execution_records = []
        self.optimized_rules = []

    def save_trace(self, task_input, tool_calls, final_output, is_success: bool):
        record = {
            "task": task_input,
            "tool_calls": tool_calls,
            "output": final_output,
            "success": is_success
        }
        self.execution_records.append(record)

    def add_optimized_rule(self, rule_text: str):
        self.optimized_rules.append(rule_text)

    def get_evolved_system_prompt(self, base_prompt: str) -> str:
        rule_block = "\n".join([f"- {r}" for r in self.optimized_rules])
        evolved_prompt = f"{base_prompt}\n\n=== 累积进化规则 ===\n{rule_block}"
        return evolved_prompt

# 使用示例
memory = AgentEvolutionMemory()
memory.save_trace(
    task_input="查询上个季度的销售数据",
    tool_calls=["query_database", "format_report"],
    final_output="缺少区域过滤数据",
    is_success=False
)
memory.add_optimized_rule("查询季度销售数据时始终添加区域过滤参数。")
final_prompt = memory.get_evolved_system_prompt(base_prompt="你是一个数据分析Agent。")
print(final_prompt)</code></pre>

<h2 id="workflow">真实世界的运行工作流</h2>
<ol>
  <li>Agent运行一个任务，把完整执行轨迹存入记忆存储。</li>
  <li>任务完成后触发自我反思模块，无论成功还是失败。</li>
  <li>反思输出可执行的优化规则，追加到Agent记忆。</li>
  <li>下一轮任务加载带有累积规则的进化系统提示词。</li>
  <li>定期清理低价值的旧规则，防止提示词膨胀。</li>
</ol>

<h2 id="pitfalls">应该避开的常见坑</h2>
<ul>
  <li>不要让Agent重写整个基础提示词，只追加增量优化规则。完全重写可能破坏Agent的核心能力。</li>
  <li>避免过度拟合单一失败案例。添加新规则前，先评估多个相似的轨迹。</li>
  <li>设置规则数量的上限。积累过多规则会导致提示词膨胀，拖慢推理速度。</li>
  <li>保持人类监督。即使启用了自我进化，重要业务规则仍需要人工审核。</li>
</ul>

<h2 id="closing">结语</h2>
<p>自我进化不会让你的Agent无所不能。它解决的是静态Agent无法自动改进的痛点。通过轨迹日志、自我反思和增量提示词更新，你的Agent在处理更多真实任务的过程中不断变好，同时大幅减少人工提示词维护工作。</p>

<h2>常见问题</h2>

<h3>Agent自我进化到底是什么意思？</h3>
<p>自我进化是Agent从自身执行历史中改进行为的能力。每次任务后，Agent保存完整轨迹，运行反思模块分析失败原因，并把得出的优化规则追加到系统提示词中。下一次任务加载带累积规则的进化提示词。这不是"变超级智能"，而是一个实用的反馈循环，让Agent不再重复同样的错误，无需人类在每次失败后都去编辑提示词。</p>

<h3>自我进化需要特殊框架或大型语言模型吗？</h3>
<p>不需要特殊框架。核心要求是一个能遵循反思提示词的LLM，以及一种存储执行轨迹的方式——本指南中的Python演示就是一个自包含的记忆类，你可以嵌入任何Agent。更重要的是纪律：可靠地保存轨迹、无论成功失败都触发反思、限制规则列表以防提示词随时间膨胀。普通的Agent配置加上这个反馈循环就足够起步了。</p>

<h3>如何避免累积规则让提示词变得过大？</h3>
<p>三道防线。第一，只追加增量规则，绝不让Agent重写整个基础提示词。第二，接受新规则前要求多个相似的失败轨迹——不要过度拟合单一案例。第三，设置规则数量的硬上限，并定期修剪低价值或过时的规则。这能让进化提示词保持聚焦，防止提示词膨胀带来的延迟和成本。</p>

<h3>Agent自我进化后还能信任它吗？</h3>
<p>应该保持人类监督，尤其是高风险业务规则。自我进化优化的是提示词和工具调用策略，不能替代对重要逻辑的审核——本指南明确建议即使启用进化，关键规则仍需人工审阅。用自我进化来减少持续手动编辑提示词的负担，同时对最重要的变更保留人工检查。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>想让你的Agent更聪明、更可靠？继续阅读这些指南：</p>
  <ul>
    <li><a href="/article/write-effective-agents-md-codex">如何为Codex编写有效的AGENTS.md</a> — 固化Agent必须遵循的基础规则和上下文</li>
    <li><a href="/article/multi-agent-collaboration-architecture">多Agent协作架构</a> — 多个Agent如何分工和通信</li>
    <li><a href="/article/deepseek-harness-comprehensive-guide-installation-architecture-practical-usage">DeepSeek Harness：安装、架构与实用操作完全指南</a> — 进化Agent所栖身的运行时框架</li>
  </ul>
</div>`,
  },

'''
last = c.rfind('};')
with open('src/lib/article-content.ts', 'w', encoding='utf-8') as f: f.write(c[:last] + n + '};')
print('Part 2 done\n=== Done ===')
