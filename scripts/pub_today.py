"""Publish Aug 12, 2026 — 1 article, no new tools."""
import os; BASE = r"C:\Users\jun\aistudyonline-next"; os.chdir(BASE)

with open('src/lib/articles.ts', 'r', encoding='utf-8') as f: s = f.read()
a = r"""  {
    slug: "beginners-guide-learning-ai-my-journey-practical-tips",
    title: "A Beginner's Guide to Learning AI: My Journey and Practical Tips",
    titleZh: "初学者AI学习指南：我的经历与实用建议",
    description: "A practical AI learning guide from a creator who's been through it — start with a specific problem, learn AI terminology like a baby, learn by doing, and find the right resources without information overload.",
    descriptionZh: "一位过来人创作者分享的实用AI学习指南——从解决具体问题开始、像婴儿一样学AI术语、边做边学、找到合适资源而不被信息淹没。",
    category: "ai-basics",
    tags: ["AI Learning", "Beginner", "AI Basics", "Learning Guide", "Study Tips", "Terminology"],
    difficulty: "beginner",
    toolsMentioned: ["ElevenLabs", "OpenAI Codex CLI"],
    date: "2026-08-12",
  },

"""
last = s.rfind('];')
with open('src/lib/articles.ts', 'w', encoding='utf-8') as f: f.write(s[:last] + a + '];')
print('Part 1 done')

with open('src/lib/article-content.ts', 'r', encoding='utf-8') as f: c = f.read()
n = r'''
  "beginners-guide-learning-ai-my-journey-practical-tips": {
    content: `<div class="meta-banner">
  <span class="meta-badge">🧠 AI Basics</span>
  <span class="meta-badge">🕒 5 min read</span>
  <span class="meta-badge">📅 Aug 12, 2026</span>
  <span class="meta-badge">🎯 Beginner</span>
</div>

<h2 id="introduction">Introduction</h2>
<p>Over the past year, I've been creating AI-related content and receiving numerous questions from people asking, "How do I start learning AI?" In this guide, I'll share my learning journey, practical tips, and recommended resources to help you start your AI learning journey with confidence.</p>

<h2 id="problem">1. Start with Solving a Specific Problem</h2>
<p>The biggest mistake beginners make is starting with "how to learn AI?" This question is too broad and will lead to information overload and confusion. Instead, start with "how can AI help me solve a specific problem?"</p>

<h3>My Example: Knowledge Management</h3>
<p>I started with a specific pain point: managing my reading notes. I read 20-30 minutes every day, but my notes were scattered and hard to review. I wanted AI to help me organize my Obsidian notes.</p>
<p><strong>Practical Steps:</strong></p>
<ol>
  <li>Import highlights from Apple Books</li>
  <li>Use AI to summarize and organize notes</li>
  <li>Create a workflow for continuous note management</li>
</ol>

<h2 id="terminology">2. Learn AI Terminology Like a Baby</h2>
<p>When you first enter the AI world, you'll encounter many new terms. Don't get overwhelmed. Learn them like a baby learning a new language.</p>

<h3>My Experience</h3>
<p>When I first took a course on AI agents, a 30-minute lesson took me an hour to complete because I had to stop and look up every new term.</p>
<p><strong>How to Learn New Terms:</strong></p>
<ol>
  <li>Use conversational AI tools to explain terms in simple language</li>
  <li>Create a personal glossary</li>
  <li>Review and reinforce your understanding</li>
</ol>

<h3>Example: Understanding CLI</h3>
<p>When I first encountered "CLI," I was confused about why there were so many different names like ChatGPT, Codex CLI, and GPT CLI. I used AI to explain the differences in simple terms.</p>

<h2 id="doing">3. Learn by Doing: Solve Problems Step by Step</h2>
<p>Once you have a basic understanding of AI terms, start solving problems. Don't wait until you know everything — learn by doing.</p>

<h3>My Second Project: Auto-Edit Video Agent</h3>
<p>I found editing talking head videos very time-consuming, so I wanted to create an AI agent to help me auto-edit videos.</p>
<p><strong>Practical Steps:</strong></p>
<ol>
  <li>Define the problem clearly</li>
  <li>Ask AI for solutions</li>
  <li>Implement the solution step by step</li>
  <li>Iterate and improve</li>
</ol>

<h2 id="resources">4. Recommended AI Learning Resources</h2>

<h3>Short Videos</h3>
<ul>
  <li><strong>@一枚卓子老师</strong>: Explains AI terms in very easy-to-understand language</li>
  <li><strong>@张咋啦老师</strong>: Provides practical, down-to-earth content that is updated frequently</li>
</ul>

<h3>Long Videos and Courses</h3>
<ul>
  <li><strong>@秋芝 2046's Codex Course</strong>: Great for learning specific tool usage and solving specific problems</li>
  <li><strong>Folder as an App Course</strong>: Excellent for learning how to build AI agents</li>
</ul>

<h3>Official Documentation</h3>
<p>Always check the official documentation of AI tools. No one knows a tool better than its creators.</p>
<p><strong>Example: ElevenLabs API</strong></p>
<p>When I was learning the ElevenLabs API, the official documentation helped me understand:</p>
<ul>
  <li>What the tool can do</li>
  <li>What possibilities it offers</li>
  <li>How to call it specifically</li>
</ul>

<h2 id="conclusion">Conclusion</h2>
<p>AI is developing rapidly, and you can't learn everything. Don't get anxious. Focus on how AI can help you solve specific problems. That's where its real value lies.</p>
<p>Remember:</p>
<ul>
  <li>Start with a specific problem</li>
  <li>Learn terminology gradually</li>
  <li>Learn by doing</li>
  <li>Use a variety of resources</li>
</ul>
<p>I hope this guide helps you start your AI learning journey with confidence. I'll continue to share more practical ways to use AI to solve real-world problems.</p>

<h2>常见问题</h2>

<h3>What's the very first thing I should do to start learning AI?</h3>
<p>Pick one specific problem you already face and ask how AI can help with it. This is the opposite of starting with "how do I learn AI" — a broad question that leads to information overload. A concrete starting point could be organizing your notes, summarizing long articles, writing better emails, or automating a repetitive task. Once you have a target, you'll naturally discover which tools you need, and every new term you learn will stick because you immediately see how it applies to your problem.</p>

<h3>I get overwhelmed by AI terminology. How should I learn it?</h3>
<p>Treat it like a baby learning a language: don't try to memorize everything at once. When you hit an unfamiliar term, ask a conversational AI tool to explain it in plain language, add it to your own personal glossary, and review the terms that come up in your actual work. The CLI example in this article is a perfect case — "ChatGPT, Codex CLI, and GPT CLI" sound like three different things but are really one concept with different contexts. Terms you encounter while solving a real problem are the ones you'll remember, so let your projects drive your vocabulary growth.</p>

<h3>Do I need to understand the math or coding behind AI before using it?</h3>
<p>No. Every project in this guide — organizing notes, auto-editing videos — was built by describing a problem and iterating with AI, not by writing machine learning code from scratch. The value of AI for most people is in applying it to tasks, and the fastest way to get there is by doing, not by studying theory first. You can always go deeper into concepts later if a specific project needs it; starting with hands-on use gets you results immediately and builds the motivation to keep going.</p>

<h3>Which learning resources should I trust most?</h3>
<p>Combine three layers. First, the official documentation of whatever tool you're learning — no one knows a tool better than its creators, and the ElevenLabs API example shows how official docs clarify what a tool can do, what's possible, and how to call it. Second, short explainer videos for quick wins on terminology. Third, longer courses only when you're committed to a specific tool or skill. The key is matching the resource to your current question: docs for specifics, short videos for concepts, and courses for deep dives — not consuming everything at once.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Kicking off your AI journey? Continue with these guides:</p>
  <ul>
    <li><a href="/article/ai-beginners-quick-guide-common-jargon-explained">AI Beginner's Quick Guide: Common Jargon Explained</a> — plain-language definitions of the terms every beginner meets first</li>
    <li><a href="/article/how-to-learn-anything-10x-faster-with-claude-practical-guide">How to Learn Anything 10x Faster with Claude: A Practical Guide</a> — use conversational AI to accelerate your learning of any subject</li>
    <li><a href="/article/dont-be-intimidated-ai-jargon-practical-guide-concepts">Don't Be Intimidated by AI Jargon: A Practical Guide to AI Concepts</a> — from ChatGPT to Workspace Agent, decoded step by step</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">🧠 AI基础</span>
  <span class="meta-badge">🕒 阅读约5分钟</span>
  <span class="meta-badge">📅 2026年8月12日</span>
  <span class="meta-badge">🎯 入门</span>
</div>

<h2 id="introduction">引言</h2>
<p>过去一年里，我持续创作AI相关内容，收到无数人问我："我该怎么开始学习AI？"在这篇指南中，我会分享我的学习经历、实用技巧和推荐资源，帮你满怀信心地开启AI学习之旅。</p>

<h2 id="problem">1. 从解决一个具体问题开始</h2>
<p>初学者最大的错误是从"如何学习AI？"这个问题开始。这个问题太宽泛，会带来信息过载和困惑。相反，从"AI能帮我解决哪个具体问题？"开始。</p>

<h3>我的例子：知识管理</h3>
<p>我最初是从一个具体的痛点出发的：管理我的读书笔记。我每天阅读20-30分钟，但笔记散落各处、难以回顾。我想让AI帮我整理Obsidian笔记。</p>
<p><strong>实操步骤：</strong></p>
<ol>
  <li>导入Apple Books中的高亮标注</li>
  <li>用AI总结并整理笔记</li>
  <li>建立持续笔记管理的工作流</li>
</ol>

<h2 id="terminology">2. 像婴儿一样学习AI术语</h2>
<p>当你初次进入AI世界，会遇到很多新术语。不要被吓倒，像婴儿学新语言一样去学它们。</p>

<h3>我的经历</h3>
<p>我第一次上AI Agent课程时，一节30分钟的课花了我一个小时才上完，因为我不得不停下来查每一个新术语。</p>
<p><strong>如何学习新术语：</strong></p>
<ol>
  <li>用对话式AI工具用简单语言解释术语</li>
  <li>建立个人术语表</li>
  <li>复习并强化你的理解</li>
</ol>

<h3>例子：理解CLI</h3>
<p>当我第一次遇到"CLI"时，我很困惑为什么有这么多不同的名字，比如ChatGPT、Codex CLI和GPT CLI。我用AI以简单的方式解释了它们之间的区别。</p>

<h2 id="doing">3. 边做边学：一步步解决问题</h2>
<p>当你对AI术语有了基本理解后，开始解决问题。不要等到什么都懂了再动手——边做边学。</p>

<h3>我的第二个项目：自动剪辑视频Agent</h3>
<p>我觉得剪辑口播视频非常耗时，于是想创建一个AI Agent帮我自动剪辑视频。</p>
<p><strong>实操步骤：</strong></p>
<ol>
  <li>清晰地定义问题</li>
  <li>向AI询问解决方案</li>
  <li>一步步实施解决方案</li>
  <li>迭代改进</li>
</ol>

<h2 id="resources">4. 推荐的AI学习资源</h2>

<h3>短视频</h3>
<ul>
  <li><strong>@一枚卓子老师</strong>：用非常通俗易懂的语言讲解AI术语</li>
  <li><strong>@张咋啦老师</strong>：提供实用接地气的内容，更新频繁</li>
</ul>

<h3>长视频和课程</h3>
<ul>
  <li><strong>@秋芝 2046的Codex课程</strong>：非常适合学习具体工具用法和解决具体问题</li>
  <li><strong>"文件夹即应用"课程</strong>：非常擅长教如何构建AI Agent</li>
</ul>

<h3>官方文档</h3>
<p>始终查阅AI工具的官方文档。没有人比工具创造者更了解一个工具。</p>
<p><strong>例子：ElevenLabs API</strong></p>
<p>当我学习ElevenLabs API时，官方文档帮助我理解了：</p>
<ul>
  <li>这个工具能做什么</li>
  <li>它提供哪些可能性</li>
  <li>具体如何调用它</li>
</ul>

<h2 id="conclusion">结语</h2>
<p>AI发展日新月异，你不可能学会所有东西。不要焦虑，专注于AI能帮你解决哪些具体问题——那才是它真正的价值所在。</p>
<p>记住：</p>
<ul>
  <li>从具体问题开始</li>
  <li>循序渐进学习术语</li>
  <li>边做边学</li>
  <li>善用多种资源</li>
</ul>
<p>希望这篇指南帮你满怀信心地开启AI学习之旅。我会继续分享更多用AI解决现实问题的实用方法。</p>

<h2>常见问题</h2>

<h3>开始学习AI，我做的第一件事应该是什么？</h3>
<p>选一个你已经在面对的具体问题，问问AI能如何帮你解决它。这与"我该怎么学AI"这种宽泛问题正好相反——宽泛问题会导致信息过载。一个具体起点可以是整理笔记、总结长文章、写出更好的邮件，或者自动化一个重复任务。一旦有了目标，你自然会发现自己需要哪些工具，而每学一个新术语都会因为立刻看到它如何应用而记得更牢。</p>

<h3>我被AI术语淹没了，该怎么学？</h3>
<p>把它当成婴儿学语言：不要试图一次记住所有东西。遇到不熟悉的术语时，让对话式AI工具用大白话解释，加入你自己的个人术语表，然后复习那些在你实际工作中出现的术语。本文中的CLI例子就是绝佳案例——"ChatGPT、Codex CLI和GPT CLI"听起来像三个不同的东西，其实是同一个概念的不同语境。在解决真实问题过程中遇到的术语才最容易被记住，所以让你的项目驱动词汇增长。</p>

<h3>在用它之前，我需要理解AI背后的数学或编程吗？</h3>
<p>不需要。本指南中的每个项目——整理笔记、自动剪辑视频——都是通过描述问题、与AI反复迭代完成的，而不是从零编写机器学习代码。对大多数人来说，AI的价值在于把它应用到任务上，最快的路径是先动手做，而不是先学理论。如果某个具体项目需要，你以后随时可以深入学习概念；从实战上手能立刻看到结果，并建立坚持下去的动力。</p>

<h3>哪些学习资源最值得信赖？</h3>
<p>把三种资源结合使用。第一层是你要学的工具的官方文档——没人比工具创造者更了解它，ElevenLabs API的例子说明了官方文档如何阐明工具能做什么、有哪些可能、以及如何调用。第二层是短视频，用通俗讲解快速搞定术语。第三层是长课程，只在当你决心学某个具体工具或技能时再投入。关键是把资源和当前问题匹配起来：细节问文档、概念看短视频、深度学习选课程——而不是一股脑全看。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>开启你的AI之旅？继续阅读这些指南：</p>
  <ul>
    <li><a href="/article/ai-beginners-quick-guide-common-jargon-explained">AI初学者快速指南：常见术语详解</a> — 用大白话解释初学者最先遇到的每个术语</li>
    <li><a href="/article/how-to-learn-anything-10x-faster-with-claude-practical-guide">用Claude让任何学习提速10倍：实用指南</a> — 用对话式AI加速你对任何学科的学习</li>
    <li><a href="/article/dont-be-intimidated-ai-jargon-practical-guide-concepts">别被AI术语吓到：AI概念实战指南</a> — 从ChatGPT到Workspace Agent，一步步解码</li>
  </ul>
</div>`,
  },

'''
last = c.rfind('};')
with open('src/lib/article-content.ts', 'w', encoding='utf-8') as f: f.write(c[:last] + n + '};')
print('Part 2 done\n=== Done ===')
