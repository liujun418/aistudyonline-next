"""Publish July 29, 2026 — 1 article, no new tools."""
import os; BASE = r"C:\Users\jun\aistudyonline-next"; os.chdir(BASE)

with open('src/lib/articles.ts', 'r', encoding='utf-8') as f: s = f.read()
a = r"""  {
    slug: "correct-way-to-collaborate-with-ai-practical-guide",
    title: "The Correct Way to Collaborate with AI: A Practical Guide",
    titleZh: "与AI正确协作的方式：一份实用指南",
    description: "A practical guide to effective AI collaboration using a 3-step framework — Put It Forward (start with real tasks, not tutorials), Explain It Clearly (break vague feelings into specific parameters), and Keep Asking (build a two-way question loop) — embracing 'learning by doing' over 'learn first, use later.'",
    descriptionZh: "高效AI协作三步框架实操指南——提出来（从真实任务开始而非教程）、说清楚（将模糊感觉拆解为具体参数）、持续追问（构建双向问答循环）——拥抱'做中学'而非'先学后用'。",
    category: "AI Learning",
    tags: ["AI Collaboration", "Prompt Engineering", "Learning by Doing", "Productivity", "Beginner", "Guide"],
    difficulty: "beginner",
    toolsMentioned: [],
    date: "2026-07-29",
  },

"""
last = s.rfind('];')
with open('src/lib/articles.ts', 'w', encoding='utf-8') as f: f.write(s[:last] + a + '];')
print('Part 1 done')

with open('src/lib/article-content.ts', 'r', encoding='utf-8') as f: c = f.read()
n = r'''
  "correct-way-to-collaborate-with-ai-practical-guide": {
    content: `<div class="meta-banner">
  <span class="meta-badge">📚 AI Learning</span>
  <span class="meta-badge">🕒 5 min read</span>
  <span class="meta-badge">📅 Jul 29, 2026</span>
  <span class="meta-badge">🎯 Beginner</span>
</div>

<h2 id="introduction">Introduction</h2>

<p>Many people have taken dozens of AI courses but still struggle to use AI effectively. The problem is not with the courses or the tools themselves. The real issue is that they treat AI as a skill to be fully learned before being applied. In reality, AI is more like swimming, writing, or driving — you can't learn all the theory on land before jumping into the water.</p>

<p>This guide will explain three key questions: Why can't you learn AI first and then use it? What is the truly effective way to collaborate with AI? And a learning path you might never have considered.</p>

<h2 id="step-1">Step 1: Put It Forward</h2>

<p>Let's take an e-commerce scenario as an example. If you run an e-commerce business, you need to calculate the actual profit of a product every day. The profit is determined by four types of variables: exchange rate, shipping cost, platform commission, and return rate.</p>

<p>The traditional way is to open a spreadsheet, fill in the data one by one, and check it repeatedly, which takes at least half an hour. But with AI, you only need to clearly explain your calculation logic, and it can directly turn this process into a usable tool.</p>

<pre><code class="language-python"># Example of profit calculation logic
def calculate_profit(cost, price, exchange_rate, shipping_cost, platform_commission, return_rate):
    revenue = price * exchange_rate
    total_cost = cost + shipping_cost + (revenue * platform_commission)
    profit = revenue - total_cost
    adjusted_profit = profit * (1 - return_rate)
    return adjusted_profit</code></pre>

<p>The first thing to learn about AI is not to learn tools or memorize prompts, but to put forward a real task you encounter.</p>

<h2 id="step-2">Step 2: Explain It Clearly</h2>

<p>Simply throwing out a task is usually not enough. You will find that the first version of the answer from AI is often not deep or accurate enough. Let's take a common scenario: you ask AI to make a poster, but the result always feels a bit off.</p>

<p>You might say "it's not high-end enough", but "high-end" is not an effective instruction for AI. It is a vague feeling, not a set of executable parameters. "High-end" can be broken down into font selection, white space ratio, information density, rhythm control, and color relationship. Each of these is a direction that can be further broken down.</p>

<pre><code class="language-text">Poster design requirements:
- Font selection: Traditional style, bold weight, high contrast
- White space ratio: 24px left and right, 32px top and bottom, 1.5x module spacing
- Information density: 4 information blocks per screen, 3 information levels
- Rhythm control: 6s animation duration, slow movement curve
- Color relationship: Cool main color, strong contrast intensity</code></pre>

<p>The more detailed you break it down, the closer the result from AI will be to what you want. When you are not satisfied with the answer from AI, don't think "why didn't AI answer correctly", but think "where didn't I explain clearly". This process is essentially not asking AI, but using AI to calibrate your own thinking.</p>

<h2 id="step-3">Step 3: Keep Asking</h2>

<p>In life, we are often trapped by emotions and can't find an exit. Many problems are not because you don't understand, but because there is no one who can accompany you to deduce slowly without interrupting or judging you. AI can just play this role.</p>

<p>You can talk to AI about things like: "I always feel something is wrong with this matter", "I have a friend, and I'm not sure if he is using me", "I'm not sure if this life choice is correct".</p>

<p>AI won't interrupt you halfway, and won't end the discussion with "you're thinking too much". You ask, it answers; it asks, you answer; you continue to ask, it continues to supplement. This two-way question-and-answer process is to establish a collaboration loop between you and AI.</p>

<pre><code class="language-text">User: I'm in a very tangled mood, and I don't know whether to find a job first or prepare for the postgraduate entrance examination.
AI: In fact, this is a crossroads that most people will encounter. There is no absolute right or wrong in choosing which path. The key is what you value more. If you want to be financially independent as soon as possible and accumulate work experience, it is more practical to find a job first; if you really want to improve your academic qualifications and change the track, taking the postgraduate entrance examination will give you more choices in the long run.</code></pre>

<h2 id="learning-path">The Learning Path</h2>

<p>The collaboration loop between you and AI is:</p>
<ol>
  <li>Put forward a task</li>
  <li>Get the result</li>
  <li>Find the problem</li>
  <li>Keep asking</li>
  <li>Revise the result</li>
</ol>

<p>You don't gain the ability first and then start using it. You gain the ability gradually in the process of using it. This is "learning by doing". Just like you can only learn to swim in the water, you can only learn to use AI effectively in the process of using it.</p>

<h2>常见问题</h2>

<h3>How is this approach different from traditional prompt engineering courses?</h3>
<p>Traditional prompt engineering courses teach you <strong>techniques first, then application</strong> — memorize frameworks (Role-Task-Context-Format), study examples, practice with exercises. This guide flips that: <strong>start with a real task, learn techniques as you need them</strong>. The profit calculation example in Step 1 came from a real e-commerce problem, not a textbook exercise. The poster design breakdown in Step 2 teaches parameterization because you encountered a "not high-end enough" problem, not because the curriculum said it was time to learn about design parameters. This approach has two advantages: (1) you're motivated because it's your real problem, and (2) you remember the technique because you discovered you needed it, not because you were told to learn it.</p>

<h3>Can AI really help with emotional and life decisions (Step 3)?</h3>
<p>AI is not a therapist and should not replace one. But for <strong>structured thinking</strong> — untangling confused thoughts, exploring options systematically, playing devil's advocate — AI is surprisingly effective. The key mechanism in Step 3 is the <strong>uninterrupted questioning loop</strong>: humans interrupt, judge, offer unsolicited advice, or change the subject. AI doesn't. This creates a space where you can think out loud without social friction. The guide's example (job vs. grad school) is exactly the kind of structured decision where AI adds value: it can list pros/cons you haven't considered, ask clarifying questions about your priorities, and help you separate emotional reactions from factual constraints. For clinical mental health issues, seek professional help. For everyday tangled thinking, AI is an excellent sounding board.</p>

<h3>What if I don't have a "real task" to start with?</h3>
<p>Everyone has real tasks — they just might not recognize them as AI-solvable. The guide's e-commerce example is a spreadsheet task the person was already doing manually for 30 minutes daily. Look for: anything you do repeatedly (weekly reports, email drafts, data entry), anything you've been putting off ("I should organize these files someday"), anything where you feel the output isn't good enough (presentations, designs, writing). If you genuinely can't find a task, steal one: find a work email you need to reply to, a document you need to summarize, a schedule you need to plan. The bar for "real task" is low — it just needs to be something you actually need done, not a practice exercise.</p>

<h3>How long does it take to get good at this collaboration approach?</h3>
<p>The first task takes the longest because you're learning both the tool and the collaboration mindset. Expect 1-2 hours for your first meaningful task (like the profit calculator in Step 1). The second and third tasks go faster — 30-45 minutes each — because you've internalized the loop: put forward → get result → find problem → keep asking → revise. After about 10 real tasks, the loop becomes automatic and each task takes 10-20 minutes. The transition point is when you stop thinking "let me use AI for this" and start thinking "let me describe this problem clearly" — at that point, AI collaboration is no longer a separate skill, it's just how you work.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Ready to apply the collaboration loop? Put it into practice:</p>
  <ul>
    <li><a href="/articles/dont-be-intimidated-ai-jargon-practical-guide-concepts">Don't Be Intimidated by AI Jargon: A Practical Guide to AI Concepts</a> — master the fundamentals while doing</li>
    <li><a href="/articles/workbuddy-10-core-skills-beginner-to-advanced">WorkBuddy: 10 Core Skills to Master from Beginner to Advanced</a> — apply the collaboration loop to WorkBuddy</li>
    <li><a href="/articles/ai-powered-excel-workflow-4-practical-skills-beginners">AI-Powered Excel Workflow: 4 Practical Skills for Beginners</a> — real tasks you can start with today</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">📚 AI 学习</span>
  <span class="meta-badge">🕒 阅读约5分钟</span>
  <span class="meta-badge">📅 2026年7月29日</span>
  <span class="meta-badge">🎯 入门</span>
</div>

<h2 id="introduction">引言</h2>
<p>很多人上了几十门AI课，但仍无法有效使用AI。问题不在课程或工具本身。真正的问题是：他们把AI当作一门需要完全学会才能应用的技能。事实上，AI更像游泳、写作或开车——你不可能在岸上学完所有理论再下水。</p>
<p>本指南解答三个关键问题：为什么不能先学AI再用？真正有效的AI协作方式是什么？以及一条你可能从未想过的学习路径。</p>

<h2 id="step-1">第一步：提出来</h2>
<p>以电商场景为例。如果你经营电商业务，每天需要计算产品实际利润。利润由四类变量决定：汇率、运费、平台佣金和退货率。传统方式是打开表格逐项填写反复核对，至少半小时。但用AI，只需清晰说明计算逻辑，它就能直接把流程变成可用工具。</p>
<pre><code class="language-python"># 利润计算逻辑示例
def calculate_profit(cost, price, exchange_rate, shipping_cost, platform_commission, return_rate):
    revenue = price * exchange_rate
    total_cost = cost + shipping_cost + (revenue * platform_commission)
    profit = revenue - total_cost
    adjusted_profit = profit * (1 - return_rate)
    return adjusted_profit</code></pre>
<p>学AI第一件事不是学工具或背提示词，而是提出你遇到的真实任务。</p>

<h2 id="step-2">第二步：说清楚</h2>
<p>仅仅抛出任务通常不够。你会发现AI的第一版答案往往不够深入或精准。拿常见场景举例：让AI做海报，结果总感觉差一点。你可能会说"不够高级"，但"高级"对AI不是有效指令——它是模糊感觉而非可执行参数。"高级"可以拆解为字体选择、留白比例、信息密度、节奏控制和色彩关系，每一项都是可进一步拆解的方向。</p>
<pre><code class="language-text">海报设计要求：
- 字体选择：传统风格、粗体字重、强对比
- 留白比例：左右24px、上下32px、模块间距1.5倍
- 信息密度：每屏4个信息块、3个信息层级
- 节奏控制：6s动画时长、慢速运动曲线
- 色彩关系：冷色主色、强对比强度</code></pre>
<p>拆解得越细，AI给你的结果就越接近你想要的。对AI答案不满意时，不要想"AI为什么答不对"，而是想"我哪里没说清楚"。这个过程本质上不是在问AI，而是用AI来校准自己的思考。</p>

<h2 id="step-3">第三步：持续追问</h2>
<p>生活中我们常被情绪困住找不到出口。很多问题不是你不懂，而是没有一个能不打断你、不评判你、陪你慢慢推演的人。AI正好可以扮演这个角色。你可以跟AI聊："我总觉得这件事有点不对劲""我有个朋友，不确定他是不是在利用我""我不确定这个人生选择是否正确"。</p>
<p>AI不会半途打断你，也不会用"你想太多了"结束讨论。你问它答，它问你答，你继续问它继续补充。这个双向问答过程就是建立你和AI之间的协作循环。</p>
<pre><code class="language-text">用户：我现在心情特别纠结，不知道是先找工作还是先准备考研。
AI：其实这是大多数人都会遇到的一个十字路口。选择哪条路都没有绝对的对错，关键是你更看重什么。如果你希望尽快经济独立、积累工作经验，那先找工作是更务实的选择；如果你确实想提升学历、换个赛道，考研在长远来看会给你更多选择。</code></pre>

<h2 id="learning-path">学习路径</h2>
<p>你与AI的协作循环：提出任务→得到结果→发现问题→持续追问→修正结果。你不是先获得能力再开始使用，而是在使用的过程中逐渐获得能力。这就是"做中学"。就像只能在水中学会游泳，你只能在使用过程中学会有效使用AI。</p>

<h2>常见问题</h2>

<h3>这种方法与传统提示词工程课程有什么不同？</h3>
<p>传统提示词工程课教你<strong>先学技巧再应用</strong>——背诵框架（角色-任务-背景-格式）、学习案例、做练习。本指南翻转了这一点：<strong>从真实任务开始，需要时再学技巧</strong>。第一步的利润计算示例来自真实电商问题而非教科书练习。第二步的海报设计拆解在你遇到"不够高级"问题时才教参数化，而非因为课程表说该学设计参数了。这种方法有两个优势：(1) 因为是你的真实问题所以有动力，(2) 因为你发现需要这个技巧所以会记住，而非被告知要学。</p>

<h3>AI真能帮助处理情感和人生决策吗（第三步）？</h3>
<p>AI不是心理咨询师，不应替代专业帮助。但对于<strong>结构化思考</strong>——理清混乱思绪、系统探索选项、扮演魔鬼代言人——AI出奇地有效。第三步的关键机制是<strong>不被打断的追问循环</strong>：人会打断、评判、给出不请自来的建议或转移话题。AI不会。这创造了一个你可以无社交摩擦地大声思考的空间。指南示例（工作vs考研）正是AI能增加价值的结构化决策类型：列出你未考虑的利弊、追问你的优先级、帮你区分情绪反应和事实约束。临床心理健康问题请寻求专业帮助。日常纠结思考，AI是出色的共鸣板。</p>

<h3>没有"真实任务"该怎么开始？</h3>
<p>每个人都有真实任务——只是可能没意识到它们可以用AI解决。指南的电商示例是该人每天手动做30分钟的表格任务。寻找：你重复做的任何事（周报、邮件草稿、数据录入）、你一直拖延的事（"总有一天该整理这些文件了"）、你觉得输出不够好的事（演示、设计、写作）。如果真找不到任务，借用：找一封需要回复的工作邮件、一份需要总结的文档、一个需要计划的日程。"真实任务"门槛很低——只需是你真正需要完成的事，而非练习作业。</p>

<h3>掌握这种协作方式需要多长时间？</h3>
<p>第一个任务耗时最长，因为你要同时学习工具和协作心态。第一个有意义的任务（如第一步的利润计算器）预计1-2小时。第二第三个任务更快——各30-45分钟——因为你已内化了循环：提出→得结果→找问题→追问→修正。大约10个真实任务后，循环变得自动，每个任务10-20分钟。转折点是当你不再想"让我用AI做这个"，而是开始想"让我把这个问题描述清楚"——到那时AI协作不再是独立技能，它就是你的工作方式。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>准备好应用协作循环？付诸实践：</p>
  <ul>
    <li><a href="/articles/dont-be-intimidated-ai-jargon-practical-guide-concepts">别被AI术语吓倒：从ChatGPT到Workspace Agent的AI概念实战指南</a> — 边做边掌握基础</li>
    <li><a href="/articles/workbuddy-10-core-skills-beginner-to-advanced">WorkBuddy十大核心技能：从入门到精通</a> — 将协作循环应用于WorkBuddy</li>
    <li><a href="/articles/ai-powered-excel-workflow-4-practical-skills-beginners">AI加持Excel工作流：新手必学的4个实用技能</a> — 今天就能开始的真实任务</li>
  </ul>
</div>`,
  },

'''
last = c.rfind('};')
with open('src/lib/article-content.ts', 'w', encoding='utf-8') as f: f.write(c[:last] + n + '};')
print('Part 2 done\n=== Done ===')