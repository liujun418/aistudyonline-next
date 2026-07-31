"""Publish July 31, 2026 — 1 article, no new tools."""
import os; BASE = r"C:\Users\jun\aistudyonline-next"; os.chdir(BASE)

with open('src/lib/articles.ts', 'r', encoding='utf-8') as f: s = f.read()
a = r"""  {
    slug: "how-to-learn-anything-10x-faster-with-claude-practical-guide",
    title: "How to Learn Anything 10x Faster with Claude: A Practical Guide",
    titleZh: "用Claude实现10倍速学习：一份实用指南",
    description: "Six AI-powered learning methods using Claude — build a learning ladder (5 levels), identify the 20% core content (Pareto), get quizzed until stuck (active recall), create one-page cheat sheets, filter signals from noise (resource curation), and use the Feynman Technique to expose fake understanding.",
    descriptionZh: "用Claude实现六种AI加速学习法——搭建学习阶梯（5级）、识别20%核心内容（帕累托）、答题直到卡壳（主动回忆）、创建一页知识卡、从噪音中过滤信号（资源筛选）、用费曼技巧暴露伪理解。",
    category: "ai-tutorials",
    tags: ["Claude", "Learning", "Productivity", "Prompt Engineering", "Feynman Technique", "Tutorial"],
    difficulty: "beginner",
    toolsMentioned: ["Claude"],
    date: "2026-07-31",
  },

"""
last = s.rfind('];')
with open('src/lib/articles.ts', 'w', encoding='utf-8') as f: f.write(s[:last] + a + '];')
print('Part 1 done')

with open('src/lib/article-content.ts', 'r', encoding='utf-8') as f: c = f.read()
n = r'''
  "how-to-learn-anything-10x-faster-with-claude-practical-guide": {
    content: `<div class="meta-banner">
  <span class="meta-badge">📖 AI Tutorials</span>
  <span class="meta-badge">🕒 6 min read</span>
  <span class="meta-badge">📅 Jul 31, 2026</span>
  <span class="meta-badge">🎯 Beginner</span>
</div>

<h2 id="introduction">Introduction</h2>
<p>If you want to learn a new skill quickly, Claude can help you achieve 10x faster learning — if you use it the right way. Don't just treat it as a search box. This guide shares six practical methods to turn Claude into your personal learning coach.</p>

<h2 id="method-1">Method 1: Let AI Build Your Learning Ladder</h2>
<p>Most people struggle to learn not because they lack effort, but because they jump to the wrong level too early. Instead of asking "Help me learn Python", use this prompt:</p>
<pre><code class="language-text">Break Python into 5 learning levels, from a complete beginner to someone who can build independent projects. For each level, tell me:
1. What I should master
2. Common mistakes to avoid
3. The standards I need to meet to move to the next level</code></pre>
<p>Claude will give you a structured learning map, so you know exactly where you are, what to learn next, and when you're ready to advance.</p>

<h2 id="method-2">Method 2: Let AI Identify the Most Important 20%</h2>
<p>Not all content in a skill is equally important. You don't need to learn every plugin when studying video editing — focus on the 20% of core content that delivers 80% of results.</p>
<pre><code class="language-text">I want to learn this topic in 20 hours. Find the most important 20% of content, and design a 10-session learning plan (2 hours per session). Each session should include:
1. Practice resources
2. Review questions
3. Clear learning objectives</code></pre>
<p>This breaks down a large skill into manageable daily tasks, so you only need to focus on 2 hours of learning each day.</p>

<h2 id="method-3">Method 3: Let AI Quiz You Until You Get Stuck</h2>
<p>Many learners only consume content passively — they watch videos or read articles and think they understand, but can't explain concepts when asked. The solution is active recall.</p>
<pre><code class="language-text">I just learned this topic. Ask me one question at a time, starting from easy to hard. After I answer:
1. Grade my answer (correct/incorrect)
2. Point out what I got right, wrong, or incomplete
3. Only re-explain the parts I didn't master</code></pre>
<p>The key is to ask one question at a time. This helps you identify knowledge gaps immediately, like a trainer correcting your form during a workout — faster than practicing alone.</p>

<h2 id="method-4">Method 4: Let AI Create a One-Page Cheat Sheet</h2>
<p>Human brains are better at remembering structures than long texts. Instead of saving long chat logs, ask Claude to condense the knowledge:</p>
<pre><code class="language-text">Condense this topic into a one-page cheat sheet that includes:
1. A one-sentence definition
2. Key concepts
3. Real-world examples
4. Common mistakes
5. A pre-use checklist
6. 5 quick self-test questions</code></pre>
<p>Perfect for quick reviews before exams, interviews, meetings, or projects — refresh in 5 minutes without re-learning everything.</p>

<h2 id="method-5">Method 5: Let AI Filter Signals from Noise</h2>
<p>The biggest learning trap today is too many resources — books, courses, videos can overwhelm you. Most people end up collecting resources instead of learning from them.</p>
<pre><code class="language-text">Find the 5 most valuable resources for learning this topic. For each resource, explain:
1. Who it's for
2. Its difficulty level
3. How to use it
4. What parts to skip to save time
Then design a 7-day learning path using these resources</code></pre>
<p>This eliminates irrelevant options and focuses you on high-quality, actionable resources.</p>

<h2 id="method-6">Method 6: Use the Feynman Technique to Force Understanding</h2>
<p>If you can't explain a concept in simple terms, you don't truly understand it. Use Claude to practice the Feynman Technique:</p>
<pre><code class="language-text">First, explain this concept in language a 12-year-old can understand. Then, I will explain it back in my own words. After I finish:
1. Point out what I explained correctly
2. Point out what I missed
3. Point out where I was confused
4. Highlight any advanced terms I used without understanding
Then ask me to explain again until I can do it clearly</code></pre>
<p>This cycle exposes "fake understanding" — you might think you get it when reading, but explaining it reveals your true knowledge.</p>

<h2 id="system">The Complete AI-Powered Learning System</h2>
<p>These six methods form a complete system: (1) learning ladder = full map, (2) 20-hour method = core content, (3) AI examiner = true level, (4) cheat sheet = compress knowledge, (5) filter = eliminate noise, (6) Feynman cycle = clarify confusion.</p>

<h2>常见问题</h2>

<h3>Do all six methods work with any AI tool, or just Claude?</h3>
<p>All six methods work with any capable AI (ChatGPT, DeepSeek, Kimi, Doubao, etc.). The guide uses Claude as the example, but the prompt templates are tool-agnostic. That said, Claude has two advantages for learning: (1) its explanations tend to be more structured and pedagogical — it naturally breaks concepts into levels and steps without being asked, and (2) its lower hallucination rate means fewer incorrect "facts" slipping into your learning materials. For Methods 1-5, any tool works. For Method 6 (Feynman Technique), Claude's conversational style and willingness to play the student/teacher role makes the back-and-forth feel more natural.</p>

<h3>How do I combine this with the "learning by doing" approach from the July 29 article?</h3>
<p>The July 29 article argues that real tasks beat passive learning. These six methods are <strong>complementary, not contradictory</strong>. Use Methods 1-2 to quickly map out what you need to learn for a real task (not to learn everything theoretically). Use Methods 3 and 6 while working on the task — quiz yourself on the parts you're implementing. Use Methods 4-5 to compress and filter what you've discovered through doing. The ideal workflow: pick a real task (July 29 approach) → use the learning ladder (Method 1) to identify which level you need → learn only the 20% relevant to your task (Method 2) → quiz yourself as you build (Method 3) → create a cheat sheet of what you learned (Method 4).</p>

<h3>How long does a full learning cycle take with these methods?</h3>
<p>For a brand-new skill: initial mapping (Method 1) takes 30 minutes, 20% identification (Method 2) takes 20 minutes, resource curation (Method 5) takes 15 minutes. That's about 1 hour of setup before you start the actual 20-hour learning plan. During the 20 hours of practice, use Methods 3-4-6 at the end of each session (10-15 minutes each) to reinforce. Total: ~1 hour setup + 20 hours practice + ~5 hours of review/quizzing = about one week of focused part-time effort to reach functional competence in most topics. This is the "10x" claim — traditional methods (courses, books, unstructured practice) typically take 100+ hours for the same result.</p>

<h3>What if Claude says something wrong during learning?</h3>
<p>Claude's hallucination rate is low but not zero. For learning, the risk areas are: specific dates/historical facts, API documentation details (version-specific), and highly niche technical details. Mitigate by: (1) using Claude for <strong>learning structures and explanations</strong> (where it excels), not as a primary source for facts; (2) cross-checking critical facts with a quick web search; (3) using Method 3 (quizzing) — Claude catching its own errors during Q&A is surprisingly effective; (4) for code/technical topics, running the code to verify. The guide's methods are designed to minimize the impact of errors — they focus on Claude as a learning <strong>coach and structure builder</strong>, not as an encyclopedia.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Ready to learn faster? Combine with these guides:</p>
  <ul>
    <li><a href="/articles/correct-way-to-collaborate-with-ai-practical-guide">The Correct Way to Collaborate with AI: A Practical Guide</a> — pair learning methods with real tasks</li>
    <li><a href="/articles/ai-beginners-quick-guide-common-jargon-explained">AI Beginner's Quick Guide: Common Jargon Explained</a> — understand the AI concepts behind these methods</li>
    <li><a href="/articles/complete-practical-tutorial-claude-code-core-operations">Complete Practical Tutorial: Master All Core Operations Inside Claude Code</a> — master Claude as a learning tool</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">📖 AI 教程</span>
  <span class="meta-badge">🕒 阅读约6分钟</span>
  <span class="meta-badge">📅 2026年7月31日</span>
  <span class="meta-badge">🎯 入门</span>
</div>

<h2 id="introduction">引言</h2>
<p>想快速学习新技能，Claude能帮你实现10倍速学习——只要用对方法。别只把它当搜索框。本指南分享六种将Claude变成个人学习教练的实用方法。</p>

<h2 id="method-1">方法1：让AI搭建学习阶梯</h2>
<p>大多数人学不好不是因为不努力，而是过早跳到了错误的难度。不要问"帮我学Python"，用这个提示词：</p>
<pre><code class="language-text">把Python拆分为5个学习级别，从零基础到能独立构建项目。每个级别说明：
1. 应掌握的内容
2. 常见错误
3. 进入下一级需达到的标准</code></pre>
<p>Claude给你结构化学习地图，让你清楚知道自己在哪、下一步学什么、何时准备好晋级。</p>

<h2 id="method-2">方法2：让AI识别最重要的20%</h2>
<p>技能中并非所有内容同等重要。学视频剪辑不需要学每个插件——聚焦带来80%效果的20%核心内容。</p>
<pre><code class="language-text">我想在20小时内学习这个主题。找出最重要的20%内容，设计10节课的学习计划（每节2小时）。每节包含：
1. 练习资源
2. 复习问题
3. 清晰的学习目标</code></pre>
<p>将大技能拆解为可管理的日常任务，每天只需专注2小时。</p>

<h2 id="method-3">方法3：让AI考你直到卡壳</h2>
<p>多数学习者只是被动消费内容——看视频读文章自以为懂了，被问到时却说不出。解决方案是主动回忆。</p>
<pre><code class="language-text">我刚学了这个主题。每次问我一个问题，从易到难。我回答后：
1. 打分（正确/错误）
2. 指出对在哪、错在哪、漏了什么
3. 只重新讲解我没掌握的部分</code></pre>
<p>关键是一次一个问题。这帮你立即识别知识盲区，像教练在你锻炼时纠正姿势——比独自练习更快。</p>

<h2 id="method-4">方法4：让AI创建一页知识卡</h2>
<p>人脑更容易记住结构而非长文本。别保存冗长聊天记录，让Claude浓缩知识：</p>
<pre><code class="language-text">把这个主题浓缩成一页知识卡，包含：
1. 一句话定义
2. 核心概念
3. 真实案例
4. 常见错误
5. 使用前检查清单
6. 5道快速自测题</code></pre>
<p>考前、面试前、会议前或项目前5分钟快速复习——无需重新学习全部内容。</p>

<h2 id="method-5">方法5：让AI从噪音中过滤信号</h2>
<p>当今学习最大陷阱是资源太多——书籍、课程、视频能压垮你。大多数人最后是收集资源而非学习资源。</p>
<pre><code class="language-text">找出学习这个主题最有价值的5个资源。每个资源说明：
1. 适合谁
2. 难度级别
3. 如何使用
4. 哪些部分可跳过以节省时间
然后用这些资源设计7天学习路径</code></pre>
<p>消除无关选项，聚焦高质量、可操作的资源。</p>

<h2 id="method-6">方法6：用费曼技巧强迫理解</h2>
<p>不能用简单语言解释概念，就是没有真正理解。用Claude练习费曼技巧：</p>
<pre><code class="language-text">先用12岁孩子能懂的语言解释这个概念。然后我用自己话复述。我讲完后：
1. 指出我解释正确的部分
2. 指出我遗漏的部分
3. 指出我混淆的地方
4. 标出我使用了但不理解的进阶术语
然后让我重新解释直到讲清楚</code></pre>
<p>这个循环暴露"伪理解"——阅读时以为懂了，但讲出来才暴露真实知识水平。</p>

<h2 id="system">完整AI驱动学习系统</h2>
<p>六种方法组成完整系统：(1)学习阶梯=全貌地图 (2)20小时法=核心内容 (3)AI考官=真实水平 (4)知识卡=压缩知识 (5)过滤=消除噪音 (6)费曼循环=澄清混淆。</p>

<h2>常见问题</h2>

<h3>六种方法只能用于Claude，还是所有AI工具都行？</h3>
<p>六种方法适用于任何有能力的AI（ChatGPT、DeepSeek、Kimi、豆包等）。指南以Claude为例，但提示词模板与工具无关。不过Claude在学习方面有两个优势：(1)解释往往更有结构性和教学性——自然将概念分为层级和步骤，无需你额外要求；(2)更低的幻觉率意味着更少的错误"事实"混入学习材料。方法1-5任何工具都行。方法6（费曼技巧），Claude的对话风格和愿意扮演学生/教师角色让来回互动更自然。</p>

<h3>怎么和7月29日"做中学"那篇文章结合？</h3>
<p>7月29日文章强调真实任务胜过被动学习。六种方法是<strong>互补而非矛盾</strong>。用方法1-2快速梳理真实任务需要学什么（而非理论学全部）。用方法3和6在执行任务时——对正在实现的部分自我测试。用方法4-5压缩和过滤通过实践中发现的知识。理想工作流：选真实任务（7月29日方法）→用学习阶梯（方法1）确定需要哪个级别→只学与任务相关的20%（方法2）→边构建边自测（方法3）→创建所学知识卡（方法4）。</p>

<h3>完整学习周期需要多长时间？</h3>
<p>全新技能：初始地图（方法1）30分钟，20%识别（方法2）20分钟，资源筛选（方法5）15分钟。大约1小时完成设置后开始实际的20小时学习计划。20小时练习中，每节结束时用方法3-4-6（各10-15分钟）巩固。总计：~1小时设置+20小时练习+~5小时复习/测试=大约一周集中业余时间达到大多数主题的功能性胜任。"10倍"的含义——传统方法（课程、书籍、无结构练习）达到同样效果通常需要100+小时。</p>

<h3>如果学习过程中Claude说错了怎么办？</h3>
<p>Claude的幻觉率低但非零。学习中的风险领域：具体日期/历史事实、API文档细节（版本特定）、高度细分的技术细节。缓解方法：(1)用Claude做<strong>学习结构和解释</strong>（它擅长之处），而非事实主要来源；(2)快速网页搜索交叉验证关键事实；(3)用方法3（问答测试）——Claude在问答中自我纠错出奇有效；(4)代码/技术主题亲自运行代码验证。指南的方法设计为最小化错误影响——聚焦Claude作为学习<strong>教练和结构构建者</strong>，而非百科全书。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>准备好加速学习？结合这些指南：</p>
  <ul>
    <li><a href="/articles/correct-way-to-collaborate-with-ai-practical-guide">与AI正确协作的方式：一份实用指南</a> — 将学习方法与真实任务结合</li>
    <li><a href="/articles/ai-beginners-quick-guide-common-jargon-explained">AI新手速成指南：常见术语一读就懂</a> — 理解这些方法背后的AI概念</li>
    <li><a href="/articles/complete-practical-tutorial-claude-code-core-operations">Claude Code完全实战教程：掌握所有核心操作</a> — 将Claude命令为学习工具</li>
  </ul>
</div>`,
  },

'''
last = c.rfind('};')
with open('src/lib/article-content.ts', 'w', encoding='utf-8') as f: f.write(c[:last] + n + '};')
print('Part 2 done\n=== Done ===')