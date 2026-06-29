"""
Publish June 29, 2026 articles.
No new tools - both articles reference existing tools (Claude, Codex, Anthropic)
"""
import os

BASE = r"C:\Users\jun\aistudyonline-next"
os.chdir(BASE)

# ===== Part 1: Add 2 article metadata to articles.ts =====
with open('src/lib/articles.ts', 'r', encoding='utf-8') as f:
    articles_src = f.read()

new_articles = r"""  {
    slug: "most-dangerous-idea-ai-self-improvement",
    title: "The Most Dangerous Idea in AI: Let It Improve Itself",
    titleZh: "AI最危险的想法：让它自我改进",
    description: "Deep dive into Anthropic's paper 'When AI Builds Itself' — AI self-improvement loops, the execution-vs-judgment gap, three future scenarios, and why Claude now writes 80% of Anthropic's code. A critical look at the singularity hypothesis.",
    descriptionZh: "深度解析Anthropic论文《当AI自我构建》——AI自我改进循环、执行与判断的鸿沟、三种未来情景、以及Claude现在编写Anthropic 80%代码的现状。对奇点假说的批判性审视。",
    category: "ai-tutorials",
    tags: ["anthropic", "claude", "self-improvement", "singularity", "research", "future"],
    difficulty: "intermediate",
    toolsMentioned: ["claude"],
    date: "2026-06-29",
  },
  {
    slug: "vibe-coding-practical-guide-ai-dev-workflow-part1",
    title: "Vibe Coding Practical Guide: AI Development Full Workflow (Part 1)",
    titleZh: "Vibe Coding实战指南：AI开发完整工作流（上篇）",
    description: "Part 1 of the Vibe Coding series — four key preparation steps before AI writes code: project initiation & feature list, technology stack selection, project architecture setup, and writing an Agent Constitution. Lay the groundwork right.",
    descriptionZh: "Vibe Coding系列上篇——AI写代码前的四个关键准备步骤：项目启动与功能清单、技术栈选择、项目架构搭建、编写Agent Constitution。打好地基才能不出乱子。",
    category: "ai-tutorials",
    tags: ["vibe-coding", "workflow", "agent-constitution", "project-setup", "architecture", "beginner"],
    difficulty: "beginner",
    toolsMentioned: ["codex-agent", "claude", "cursor"],
    date: "2026-06-29",
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
  "most-dangerous-idea-ai-self-improvement": {
    content: `<div class="meta-banner">
<p><strong>📅 Published:</strong> June 29, 2026 · <strong>🏷️ Category:</strong> AI Tutorials · <strong>📊 Level:</strong> Intermediate · <strong>🛠️ Tools:</strong> Claude</p>
</div>

<p>In the current landscape of AI research, one idea stands out as both the most alluring and the most perilous: <strong>letting AI improve itself</strong>. Imagine a scenario where AI writes code, trains the next-generation model, and then that next model turns around to enhance itself, leading to even more powerful subsequent models. Many refer to the realization of this loop as the "singularity" — once operational, AI could break free from human limitations and evolve independently at an exponential pace.</p>

<h2>A Deep Dive into Anthropic's Latest Paper</h2>

<p>Let's delve into a recent paper by Anthropic titled <em>"When AI Builds Itself"</em>. It opens with two intriguing visuals. One is a pixel-art style Claude logo that self-replicates into a larger version, which then becomes the small unit for the next replication cycle. This visual metaphor illustrates that if AI enters a self-building loop, its growth won't be linear but rather a cascading, accelerating process — one cycle nested within another, getting faster and faster.</p>

<p>The second visual depicts the evolution of AI development methods: from engineers writing code by hand, to chatbots with AI assisting, to capable agents modifying files autonomously, to agents dispatching sub-agents for multi-hour tasks. The final stage is labeled <em>"Closing the Loop"</em>, where AI designs, trains, and improves the next-generation model iteratively. This is the core argument: AI research might be entering a cycle of self-acceleration and self-revolution.</p>

<p>While insightful, this paper isn't a rigorous academic paper — it contains data but also PR-oriented framing, like emphasizing the "danger" of their models to garner attention. So take the conclusions with a grain of salt.</p>

<h2>Concrete Numbers and Practical Cases</h2>

<p>Anthropic provides some striking figures:</p>

<ul>
<li>Claude now writes over <strong>80% of the code</strong> in Anthropic's official codebase</li>
<li>A typical engineer's daily code contribution is about <strong>8 times</strong> what it was in 2024</li>
<li>Tasks that used to take a human 4 minutes can now be completed by Claude in 1.5 hours</li>
<li>Some tasks have seen a <strong>52x speedup</strong> in small labs</li>
</ul>

<p>However, approach these numbers with caution. When Anthropic hyped its Mythos model, real-world tests told a different story: a curl developer found only 1 valid low-severity issue among 5 reported vulnerabilities. Mozilla noted Mythos found 271 vulnerabilities, but none beyond human expert capability. Even a demo vulnerability highlighted by the Mythos team was detectable by 8 smaller models. LLMs still rely on predicting the next token — they haven't evolved into a new species capable of inherent truth-judging or direction-setting. Human review remains indispensable in the short term.</p>

<h2>Two Categories of AI Work: Execution and Judgment</h2>

<p>Anthropic categorizes AI work into two types:</p>

<ul>
<li><strong>Execution:</strong> Writing code, running experiments, fixing bugs, creating reports — given a goal, AI figures out how to achieve it</li>
<li><strong>Judgment:</strong> Deciding which research problems are worth pursuing, determining result credibility, knowing when to stop or pivot</li>
</ul>

<p>Current models excel at execution but lag behind humans in judgment. This gap, while significant, might be narrowing faster than we think. Anthropic has observed that as Claude writes code faster, human code review has become the new bottleneck.</p>

<h2>Three Future Scenarios</h2>

<ol>
<li><strong>Stagnation in AI Capabilities:</strong> Even if AI progress slows, existing tools will still transform industries. A 100-person company could achieve what once required 1,000 people.</li>
<li><strong>AI Continues to Strengthen, but Humans Set Direction:</strong> Companies become human-AI hybrids with explosive efficiency, but review, validation, and management become bottlenecks.</li>
<li><strong>AI Sets Its Own Direction:</strong> Humans lose the ability to supervise, validate, or halt progress, leading to complete loss of control over the models.</li>
</ol>

<p>Anthropic's recommendation: humanity should have the option to slow down or pause AI development. It's worth noting the irony — Anthropic is a leading player in the AI race, pressing the accelerator while warning about dangers and calling for speed limits. Take this with your own critical thinking.</p>

<h2>Personal Reflections</h2>

<p>An Anthropic employee shared a telling insight: when agents work smoothly, humans feel irrelevant because automation is faster; when agents fail, humans still feel irrelevant because they can't understand the complex work the agent was doing. Each time you delegate a task to AI and it performs well, you're inclined to delegate more. But each delegation also reduces your ability to judge if the AI's work is correct. We cede ground for what seem like wise, reasoned choices, but when we stop to check, we find we've lost comprehension. Yet looking back, each step feels justified. This is the fascinating predicament we face with AI today.</p>

<h2>常见问题</h2>

<h3>Is AI self-improvement actually happening now, or is this still theoretical?</h3>
<p>It's partially happening. Claude writes 80% of Anthropic's code — that's AI assisting in building the tools used to create the next AI. But the full "closed loop" where AI autonomously designs, trains, and deploys a better model without human intervention hasn't happened yet. The gap is in judgment: AI can execute tasks but can't reliably decide which research directions are worth pursuing or validate the correctness of its own improvements. We're in Scenario 2 (AI strengthens, humans set direction), not Scenario 3 (AI sets its own direction).</p>

<h3>What does the 80% code figure actually mean?</h3>
<p>It means Claude generates the majority of code committed to Anthropic's repositories — but humans still review, approve, and merge that code. Think of it like a senior developer delegating to a very fast junior: the junior writes most of the code, but the senior decides what to build and checks the work. The 8x productivity figure reflects this human-in-the-loop workflow, not fully autonomous development. The code Claude writes still goes through human code review, testing, and validation.</p>

<h3>Should I be worried about AI replacing developers?</h3>
<p>The data suggests AI is more of a force multiplier than a replacement. An engineer at Anthropic is now 8x more productive — they're not eliminated, they're amplified. The real risk isn't AI replacing developers but developers who don't use AI being outpaced by those who do. The bottleneck is shifting from writing code to reviewing AI-generated code and making architectural decisions. Skills like code review, system design, and critical judgment are becoming more valuable, not less.</p>

<div class="next-step">
<p><strong>下一篇：</strong> <a href="/en/article/vibe-coding-practical-guide-ai-dev-workflow-part1">Vibe Coding Practical Guide: AI Development Full Workflow (Part 1) →</a></p>
</div>`,
    contentZh: `<div class="meta-banner">
<p><strong>📅 发布日期：</strong>2026年6月29日 · <strong>🏷️ 分类：</strong>AI教程 · <strong>📊 难度：</strong>中级 · <strong>🛠️ 工具：</strong>Claude</p>
</div>

<p>在当前AI研究格局中，有一个想法既最诱人也最危险：<strong>让AI自我改进</strong>。想象这样一个场景：AI编写代码，训练下一代模型，然后那个下一代模型反过来增强自身，产生更强大的后续模型。许多人将这一循环的实现称为"奇点"——一旦运转起来，AI可能摆脱人类限制，以指数速度独立进化。</p>

<h2>深度解析Anthropic最新论文</h2>

<p>让我们深入Anthropic最近一篇题为<em>《当AI自我构建》</em>的论文。它以两个引人入胜的视觉开篇。一个是像素艺术风格的Claude标志自我复制成更大版本，然后成为下一个复制周期的小单元。这个视觉隐喻说明：如果AI进入自我构建循环，其增长将不是线性的，而是级联加速的过程——一个循环嵌套在另一个循环中，越来越快。</p>

<p>第二个视觉描绘了AI开发方法的演变：从工程师手写代码，到聊天机器人辅助写代码片段，到能自主修改文件和运行代码的Agent，再到Agent派遣子Agent协作完成数小时任务。最终阶段标注为<em>"闭合循环"</em>，AI迭代设计、训练和改进下一代模型。这是核心论点：AI研究可能正进入自我加速和自我革命的循环。</p>

<p>虽然这篇论文有洞察力，但它不是严谨的学术论文——包含数据但也有PR包装，比如强调模型的"危险"来吸引全球关注。所以对结论要持保留态度。</p>

<h2>具体数字和实际案例</h2>

<p>Anthropic提供了一些引人注目的数字：</p>

<ul>
<li>Claude现在编写了Anthropic官方代码库中<strong>超过80%的代码</strong></li>
<li>典型工程师的每日代码贡献量约为2024年的<strong>8倍</strong></li>
<li>过去人类需要4分钟完成的任务，Claude现在可在1.5小时内完成</li>
<li>小型实验室中某些任务实现了<strong>52倍加速</strong></li>
</ul>

<p>但应谨慎看待这些数字。当Anthropic炒作其Mythos模型极其强大时，实际测试讲了不同故事：curl工具的开发者发现Mythos报告的5个漏洞中只有1个是有效的低严重性问题。Mozilla提到Mythos帮助找到271个漏洞，但没有超出人类专家能力范围的。甚至Mythos团队重点展示的一个演示漏洞，8个更小的模型也能检测到。大语言模型仍然依赖预测下一个token——它们没有进化成能够固有判断真伪、评估价值或设定方向的新物种。短期内人类审查仍然不可或缺。</p>

<h2>AI工作的两个类别：执行与判断</h2>

<p>Anthropic将AI工作分为两类：</p>

<ul>
<li><strong>执行：</strong> 编写代码、运行实验、修复Bug、创建报告——给定目标，AI能找出如何实现</li>
<li><strong>判断：</strong> 决定哪些研究问题值得追求、判断结果可信度、知道何时停止或转向</li>
</ul>

<p>当前模型擅长执行但判断力落后于人类。这个差距虽然显著，但可能比我们想象的缩小得更快。Anthropic观察到，随着Claude写代码越来越快，人类代码审查已成为新的瓶颈。</p>

<h2>三种未来情景</h2>

<ol>
<li><strong>AI能力停滞：</strong> 即使AI进展放缓，现有工具仍将改变行业。100人的公司可以实现以前需要1000人的产出。</li>
<li><strong>AI持续增强，但人类设定方向：</strong> 公司成为人机混合体，效率爆发，但审查、验证和管理成为瓶颈。</li>
<li><strong>AI自主设定方向：</strong> 人类失去监督、验证或停止进展的能力，导致对模型完全失控。</li>
</ol>

<p>Anthropic的建议是：人类应保留减缓或暂停AI发展的选项。值得注意的是其讽刺性——Anthropic是AI竞赛的领先玩家，一边踩油门一边警告危险呼吁限速。对此结论要有自己的批判性思考。</p>

<h2>个人反思</h2>

<p>一位Anthropic员工分享了一个有启发性的见解：当Agent顺利工作时，人类感到无关紧要因为自动化更快；当Agent失败时，人类仍然感到无关紧要因为无法理解Agent所做的复杂工作。这种二元性很有道理——每次你把任务委托给AI并且它做得又快又好，你就倾向于委托更多。但每次委托也降低了判断AI工作是否正确的能力。我们因为看似明智、理性的选择而让渡地盘，但当我们停下来检查时，发现自己已经失去了理解力。然而回顾每一步，又似乎都有道理。这就是我们与AI今天面临的迷人困境。</p>

<h2>常见问题</h2>

<h3>AI自我改进现在真的在发生吗，还是仍然只是理论？</h3>
<p>部分在发生。Claude编写了Anthropic 80%的代码——这是AI协助构建用于创造下一个AI的工具。但完整的"闭合循环"——AI在没有人类干预的情况下自主设计、训练和部署更好的模型——尚未发生。差距在于判断力：AI能执行任务但不能可靠地决定哪些研究方向值得追求或验证自身改进的正确性。我们处于情景2（AI增强，人类设定方向），而非情景3（AI自主设定方向）。</p>

<h3>80%代码这个数字到底意味着什么？</h3>
<p>这意味着Claude生成了提交到Anthropic仓库的大部分代码——但人类仍然审查、批准和合并这些代码。可以想象成高级开发人员把工作委托给非常快的初级开发：初级写大部分代码，但高级决定构建什么并检查工作。8倍生产力数字反映的是这种"人在回路中"的工作流，而非完全自主开发。Claude写的代码仍然经过人类代码审查、测试和验证。</p>

<h3>我应该担心AI取代开发者吗？</h3>
<p>数据表明AI更像是力量倍增器而非替代品。Anthropic的工程师现在生产力提升了8倍——他们没有被淘汰，而是被放大了。真正的风险不是AI取代开发者，而是不使用AI的开发者被使用AI的开发者超越。瓶颈正从编写代码转向审查AI生成的代码和做架构决策。代码审查、系统设计和批判性判断等技能正变得更有价值，而非更少。</p>

<div class="next-step">
<p><strong>下一篇：</strong> <a href="/zh/article/vibe-coding-practical-guide-ai-dev-workflow-part1">Vibe Coding实战指南：AI开发完整工作流（上篇） →</a></p>
</div>`,
  },

  "vibe-coding-practical-guide-ai-dev-workflow-part1": {
    content: `<div class="meta-banner">
<p><strong>📅 Published:</strong> June 29, 2026 · <strong>🏷️ Category:</strong> AI Tutorials · <strong>📊 Level:</strong> Beginner · <strong>🛠️ Tools:</strong> Codex, Claude, Cursor</p>
</div>

<p>You might have been in this situation: you open AI excitedly, eager to build your own project, but end up sitting there, clueless about the first step. Your mind is full of ideas, yet you don't know where to start. So you might just say, "Help me build a certain system," throw everything to AI, and then watch helplessly as it writes more and more chaotically, making you increasingly unsure.</p>

<p>This article is Part 1 of the "Vibe Coding" series, focusing on the workflow of AI development from project initiation to before writing code. The entire series covers: project initiation, task breakdown, technology selection, and project architecture. This part focuses on the early preparation phase — how to lay the groundwork and establish rules before writing code.</p>

<h2>Four Key Steps Before AI Writes Business Logic</h2>

<p>Before letting AI handle business functions, there are four crucial steps: <strong>project initiation and feature list</strong>, <strong>technology stack selection</strong>, <strong>project architecture setup</strong>, and <strong>writing an Agent Constitution</strong>. Only after completing these four steps can you say the groundwork and rules are properly established.</p>

<h3>Step 1: Project Initiation and Feature List</h3>

<p>This is the starting point of the entire process, and it's also the step many people are tempted to skip. Project initiation means figuring out what the project is supposed to do. The feature list involves breaking that down into clear, individual features.</p>

<p><strong>Key reminder:</strong> if you skimp on this step, rework is likely later. Because if you don't know what you need, AI will be guessing when building the project. When developing with AI, the only thing that changes is the role in development. Previously, you had to clarify business requirements with programmers. Now, AI is your programmer, so you must clarify requirements with AI clearly. Whether dealing with a professional programmer or AI, ambiguous requirements are always dangerous.</p>

<h3>Step 2: Technology Stack Selection</h3>

<p>Once you've decided what the project will do, you need to decide what technologies to use. You need to determine the front-end tech stack, component library, back-end language, and framework.</p>

<p>The key here isn't to pick the most advanced or powerful technologies, but the ones that best suit your project and that AI is most familiar with. If you choose wrong, problems often surface halfway through, and starting over is very time-consuming.</p>

<p>Once the technology stack is decided, <strong>don't waver</strong>. If the front-end switches from React to Vue overnight, or the back-end from Python to Go, each waver means rebuilding the previous groundwork.</p>

<h3>Step 3: Project Architecture Setup</h3>

<p>After deciding on the technology stack, set up the project architecture. Whether front-end or back-end, before writing business logic, first set up a solid and stable project architecture. It's like building a skyscraper — you don't start by decorating a room; you first set up the foundation, framework, and load-bearing walls.</p>

<p>This step isn't about having AI write all features like login, orders, and payments right away. Instead, first set up a minimal, runnable framework and establish general rules:</p>

<ul>
<li><strong>Back-end:</strong> Ensure the project can start, configurations can be read, interfaces return consistently, error handling is uniform, and set up logging, database connections, and permission entry points.</li>
<li><strong>Front-end:</strong> Decide how to structure directories, standardize components, unify request handling, and manage state.</li>
</ul>

<p>In short, for both front-end and back-end, first establish a set of rules that every feature will follow.</p>

<h3>Step 4: Writing an Agent Constitution</h3>

<p>Once the groundwork is laid, establish an "Agent Constitution" for the project — a set of rules for AI to follow when working on the project, rules that must be adhered to for any feature.</p>

<p><strong>How it works:</strong> Most AI programming tools have a mechanism where if you place the rule file in a specified location, the tool automatically reads it into AI's context every time it starts a task. Before you ask AI to do anything, it "recites" these rules from start to finish. So it actually influences every decision AI makes.</p>

<p><strong>Where to place it:</strong> Different tools require different locations and filenames. The most reliable way is to ask your AI tool directly:</p>

<pre><code class="language-plaintext">Please create an Agent Constitution file in the location
that this tool automatically reads.</code></pre>

<p>Don't confuse it with the project architecture design document. The architecture document describes how the project's code is organized. The Agent Constitution defines the behavioral rules AI must follow, such as:</p>

<ul>
<li>Must follow the architecture design document</li>
<li>If changing the underlying layer, framework, or adding new dependencies, explain the reason first</li>
<li>Use the framework's built-in capabilities instead of writing from scratch whenever possible</li>
<li>Self-inspect after completing each phase</li>
</ul>

<p><strong>How to write it:</strong> Don't create from scratch. Use a general template, but don't just copy it directly. Give the template to AI and say:</p>

<pre><code class="language-plaintext">Please create a project-specific Agent Constitution based
on the actual situation of the current project and this
general template.</code></pre>

<p>The key is "based on your project's actual situation" — your project initiation, feature list, and technology stack aren't in the general template. AI needs to adapt these general rules to your project's specific language, framework, and business for the Constitution to be truly effective.</p>

<p>After customization, glance through it. If there's anything you don't understand, ask AI to explain each rule in plain language.</p>

<h2>Part 1 Summary</h2>

<p>The four steps in Part 1 are:</p>

<ol>
<li><strong>Project Initiation and Feature List:</strong> Clarify what to build and break it into individual features</li>
<li><strong>Technology Stack Selection:</strong> Choose what's best for your project and what AI is familiar with, then stick with it</li>
<li><strong>Project Architecture Setup:</strong> For both front-end and back-end, first set up a runnable framework and establish uniform rules</li>
<li><strong>Write an Agent Constitution:</strong> Document the rules AI must follow for all features, ensuring AI reviews them before each task</li>
</ol>

<p>After these four steps, the groundwork and rules are in place. Remember: once the groundwork is laid, try not to redo it later. Once the groundwork and rules are set, the next step is to have AI start writing code — how to break each major phase into detailed sub-phases and guide AI step by step will be covered in Part 2.</p>

<h2>常见问题</h2>

<h3>What's the difference between an Agent Constitution and a project architecture document?</h3>
<p>The architecture document describes <em>what</em> your project looks like — directory structure, component organization, data flow, and technical decisions. The Agent Constitution describes <em>how</em> AI should behave when working on the project — rules like "explain before changing dependencies" or "use framework built-ins instead of writing from scratch." Think of the architecture as the blueprint of the building, and the Constitution as the safety and quality rules all construction workers must follow. Both are needed; they serve different purposes.</p>

<h3>Can I skip the preparation steps and just start prompting AI to build features?</h3>
<p>You can, and many beginners do. But the cost shows up later: AI writes inconsistent code, makes conflicting technology choices, produces spaghetti architecture, and you spend more time fixing than building. The four preparation steps take 1-2 hours upfront but save days of rework. It's the difference between building a house with blueprints and permits versus just stacking bricks and hoping it stands. For any project you intend to maintain beyond a weekend prototype, the preparation is worth it.</p>

<h3>Which AI tool is best for Vibe Coding — Codex, Claude Code, or Cursor?</h3>
<p>All three work well for this workflow. Codex has the most mature Agent Constitution support (AGENTS.md auto-loading) and strong project scaffolding. Claude Code excels at the architecture setup phase — its agent loop naturally handles multi-file project initialization. Cursor is great for the iterative refinement steps where you're tweaking UI and behavior. Many experienced Vibe Coders use a combination: Claude Code for architecture and initial setup, Codex for feature development, Cursor for polishing. But any single one of these tools can handle the full workflow described in this article.</p>

<div class="next-step">
<p><strong>上一篇：</strong> <a href="/en/article/most-dangerous-idea-ai-self-improvement">The Most Dangerous Idea in AI: Let It Improve Itself ←</a></p>
</div>`,
    contentZh: `<div class="meta-banner">
<p><strong>📅 发布日期：</strong>2026年6月29日 · <strong>🏷️ 分类：</strong>AI教程 · <strong>📊 难度：</strong>初级 · <strong>🛠️ 工具：</strong>Codex、Claude、Cursor</p>
</div>

<p>你可能遇到过这种情况：兴奋地打开AI，渴望构建自己的项目，结果坐在那里不知道第一步该做什么。脑子里满是想法，却不知道从哪里开始。于是你可能会说"帮我建某个系统"，把所有东西丢给AI，然后无奈地看着它写得越来越乱，让你越来越没底。</p>

<p>本文是"Vibe Coding"系列的上篇，聚焦从项目启动到写代码之前的AI开发工作流。整个系列涵盖：项目启动、任务拆解、技术选型和项目架构。本篇专注早期准备阶段——如何在写代码前打好地基、建立规则。</p>

<h2>AI写业务逻辑前的四个关键步骤</h2>

<p>在让AI处理业务功能之前，有四个关键步骤：<strong>项目启动与功能清单</strong>、<strong>技术栈选择</strong>、<strong>项目架构搭建</strong>和<strong>编写Agent Constitution</strong>。只有完成这四步，才能说地基和规则真正建立好了。</p>

<h3>第1步：项目启动与功能清单</h3>

<p>这是整个流程的起点，也是很多人想跳过的步骤。项目启动就是搞清楚项目要做什么。功能清单就是把要做的事拆成清晰、独立的功能点。</p>

<p><strong>关键提醒：</strong> 如果这一步偷懒，后面很可能会返工。因为如果你不知道自己要什么，AI在构建项目时就是在猜。用AI开发时，唯一改变的是开发中的角色。以前做产品，项目方要向程序员讲清业务需求。现在AI是你的程序员，所以你必须向AI清晰地讲清需求。无论是对专业程序员还是对AI，模糊的需求永远是危险的。</p>

<h3>第2步：技术栈选择</h3>

<p>决定项目要做什么之后，就要决定用什么技术。需要确定前端技术栈、组件库、后端语言和框架。</p>

<p>关键不是选最先进或最强大的技术，而是选最适合你项目、AI最熟悉的技术。如果选错了，问题常常在半路暴露出来，重来的时间和人力成本非常高。</p>

<p>技术栈一旦确定，<strong>不要动摇</strong>。如果前端一夜之间从React换成Vue，或后端从Python换成Go，每次动摇都意味着之前的地基要重来。</p>

<h3>第3步：项目架构搭建</h3>

<p>技术栈确定后，搭建项目架构。无论前端还是后端，在写业务逻辑之前，先搭建一个扎实稳定的项目架构。就像盖摩天大楼——不是先装修房间，而是先打好地基、搭好框架和承重墙。</p>

<p>这一步不是让AI立刻写出登录、订单、支付等所有功能。而是先搭一个最小可运行的框架，建立通用规则：</p>

<ul>
<li><strong>后端：</strong> 确保项目能启动、配置能读取、接口返回一致、错误处理统一，搭建日志、数据库连接、权限入口点。</li>
<li><strong>前端：</strong> 决定目录结构、组件标准化、请求处理统一、状态管理方式。</li>
</ul>

<p>总之，前后端都先建立一套所有功能都要遵守的规则。</p>

<h3>第4步：编写Agent Constitution</h3>

<p>地基打好后，为项目建立"Agent Constitution"——一套AI在项目上工作时要遵守的规则，任何功能都必须遵守。</p>

<p><strong>它是如何起作用的：</strong> 大多数AI编程工具有一个机制：如果你把规则文件放在指定位置，工具每次启动任务时自动将其读入AI的上下文。在你让AI做任何事之前，它已经从头到尾"背诵"了这些规则。所以它不是摆设，它实际影响AI做出的每一个决定。</p>

<p><strong>放在哪里：</strong> 不同工具需要不同的位置和文件名。最可靠的方法是直接问你的AI工具：</p>

<pre><code class="language-plaintext">请在本工具会自动读取的位置创建Agent Constitution文件。</code></pre>

<p>不要把它和项目架构设计文档混淆。架构文档描述项目代码如何组织。Agent Constitution定义AI必须遵守的行为规则，如：</p>

<ul>
<li>必须遵循架构设计文档</li>
<li>如果改变底层、框架或添加新依赖，先说明原因</li>
<li>尽可能使用框架内置能力而非从头编写</li>
<li>每完成一个阶段后自我检查</li>
</ul>

<p><strong>如何编写：</strong> 不要从零创建。使用通用模板，但不要直接复制。把模板交给AI并说：</p>

<pre><code class="language-plaintext">请根据当前项目的实际情况和这个通用模板，
创建项目专属的Agent Constitution。</code></pre>

<p>关键是"根据你项目的实际情况"——你的项目启动、功能清单和技术栈不在通用模板里。AI需要将这些通用规则适配到你项目的具体语言、框架和业务，Constitution才能真正有效。</p>

<p>定制完成后浏览一遍。如果有看不懂的地方，不要装懂。让AI用通俗语言解释每条规则。</p>

<h2>上篇总结</h2>

<p>上篇的四个步骤：</p>

<ol>
<li><strong>项目启动与功能清单：</strong> 明确要建什么，拆成独立功能点</li>
<li><strong>技术栈选择：</strong> 选最适合项目和AI最熟悉的，然后坚持不动摇</li>
<li><strong>项目架构搭建：</strong> 前后端都先搭可运行框架，建立统一规则</li>
<li><strong>编写Agent Constitution：</strong> 文档化AI必须遵守的规则，确保AI每次任务前审查</li>
</ol>

<p>完成这四步后，地基和规则就位。记住：地基一旦打好，尽量不要在后面重做。地基和规则就绪后，下一步就是让AI开始写代码——如何将每个大阶段拆成详细子阶段并引导AI一步步走而不跑偏，将在下篇中介绍。</p>

<h2>常见问题</h2>

<h3>Agent Constitution和项目架构文档有什么区别？</h3>
<p>架构文档描述你的项目<em>是什么样子</em>——目录结构、组件组织、数据流和技术决策。Agent Constitution描述AI在项目上工作时<em>应该如何行为</em>——如"更改依赖前先解释原因"或"使用框架内置而非从头编写"等规则。可以把架构想象成建筑的蓝图，Constitution是所有施工人员必须遵守的安全和质量规则。两者都需要，服务于不同目的。</p>

<h3>我可以跳过准备步骤直接让AI构建功能吗？</h3>
<p>可以，很多新手就是这么做的。但代价后来会显现：AI写出不一致的代码、做出冲突的技术选择、产生意大利面式架构，你花在修复上的时间比构建还多。这四个准备步骤前期花1-2小时但能节省数天的返工。这就像盖房子有蓝图和许可证 vs 只是堆砖然后希望它能立住。对于任何你打算维护超过一个周末原型的项目，准备工作是值得的。</p>

<h3>哪个AI工具最适合Vibe Coding——Codex、Claude Code还是Cursor？</h3>
<p>三个工具都适合这个工作流。Codex有最成熟的Agent Constitution支持（AGENTS.md自动加载）和强大的项目脚手架。Claude Code在架构搭建阶段表现出色——其Agent循环自然处理多文件项目初始化。Cursor在迭代细化步骤中很出色，适合调整UI和行为。许多有经验的Vibe Coder组合使用：Claude Code做架构和初始搭建，Codex做功能开发，Cursor做打磨。但任何一个工具都能独立完成本文描述的完整工作流。</p>

<div class="next-step">
<p><strong>上一篇：</strong> <a href="/zh/article/most-dangerous-idea-ai-self-improvement">AI最危险的想法：让它自我改进 ←</a></p>
</div>`,
  },

'''

last_brace = content_src.rfind('};')
content_new = content_src[:last_brace] + new_contents + '};'

with open('src/lib/article-content.ts', 'w', encoding='utf-8') as f:
    f.write(content_new)

print('Part 2: 2 article contents added to article-content.ts')

print('\n=== All done! Run build to verify ===')
