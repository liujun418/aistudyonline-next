"""Publish Aug 22, 2026 — 1 article (Codex 5 Levels), no new tools."""
import os
BASE = r"C:\Users\jun\aistudyonline-next"
os.chdir(BASE)

# ---------- Part 1: articles.ts ----------
with open('src/lib/articles.ts', 'r', encoding='utf-8') as f:
    s = f.read()

a = r"""  {
    slug: "5-levels-using-codex-demo-production-grade-ai-workflows",
    title: "The 5 Levels of Using Codex: From Demo to Production-Grade AI Workflows",
    titleZh: "使用Codex的5个层级：从Demo到生产级AI工作流",
    description: "Over 18 days, 400 tasks, and 71 billion tokens — how to move Codex from basic chat-box demos to reliable production tooling. Five levels: direct submission, document-driven workflows, Git code management, open source ecosystem integration, and multi-agent collaboration.",
    descriptionZh: "18天、400个任务、710亿token——如何让Codex从基础的聊天框演示进阶为可靠的生产级工具。五个层级：直接提交、文档驱动工作流、Git代码管理、开源生态集成和多Agent协作。",
    category: "ai-tutorials",
    tags: ["Codex", "AI Workflow", "Git", "Multi-Agent", "Open Source", "Production", "Vibe Coding", "Documentation"],
    difficulty: "intermediate",
    toolsMentioned: ["Codex", "Deer Flow"],
    date: "2026-08-22",
  },
"""

last = s.rfind('];')
with open('src/lib/articles.ts', 'w', encoding='utf-8', newline='\n') as f:
    f.write(s[:last] + a + '];')
print('Part 1 done')

# ---------- Part 2: article-content.ts ----------
with open('src/lib/article-content.ts', 'r', encoding='utf-8') as f:
    s = f.read()

content = r"""  "5-levels-using-codex-demo-production-grade-ai-workflows": {
    content: `<div class="meta-banner">
  <span class="meta-badge">📖 AI Tutorial</span>
  <span class="meta-badge">🕒 8 min read</span>
  <span class="meta-badge">📅 Aug 22, 2026</span>
  <span class="meta-badge">🎯 Intermediate</span>
</div>

<h2 id="introduction">Introduction</h2>
<p>Over 18 days, I ran 400 tasks in Codex, consuming 71 billion tokens in total. The longest task ran continuously for 16 hours using GPT-5.6. However, I've noticed many users only use Codex at the most basic level — submitting requests directly in the chat box and stopping once a result is generated. This article breaks down Codex usage into 5 distinct levels, and explains why you need to reach Level 3 to turn Codex into a reliable production tool.</p>

<h2 id="level-1">Level 1: Direct Task Submission</h2>
<p>Level 1 is the simplest way to use Codex: submit tasks directly in the chat box. You can ask Codex to create a webpage, build a small game, or implement a simple feature, and it will usually produce a result that looks good in just a few minutes.</p>
<p>However, this approach has critical limitations. Once tasks become more complex, you'll often run into issues: the functionality doesn't match your expectations, the layout is unreasonable, or a single small change (like modifying one button) can cause the entire page to break. After several rounds of revisions, the work you completed earlier may also stop working. This is why Level 1 outputs are almost always just demos, and rarely evolve into long-term maintainable projects.</p>

<h2 id="level-2">Level 2: Document-Driven Workflow</h2>
<p>When you realize you need to help Codex remember what the project is supposed to do, you move to Level 2: document-driven development.</p>
<p>The workflow is:</p>
<ol>
  <li>Create a dedicated project folder before starting work</li>
  <li>Prepare three core documents:
    <ul>
      <li>Product requirements</li>
      <li>Software architecture</li>
      <li>Current progress</li>
    </ul>
  </li>
  <li>You don't need to write these documents from scratch — ask Codex to ask you clarifying questions, then generate the documents based on your answers</li>
  <li>Before starting each new task, have Codex read these documents first, create a work plan, and confirm the plan with you before execution</li>
  <li>After completing the task, sync the results back to the progress document</li>
</ol>
<p>This effectively gives your project an "external brain". Even if conversations get very long or you create new tasks, Codex will always understand what the product is supposed to do, where the project stands, and which parts should not be modified. At this level, you're no longer just thinking about prompts — you're thinking about product requirements, feature breakdowns, and software architecture.</p>
<p>However, documents can only prevent Codex from forgetting the project. They can't prevent it from breaking the project.</p>

<h2 id="level-3">Level 3: Code Management</h2>
<p>That's where Level 3 comes in: code management. This is the step that most Vibe coders overlook.</p>
<p>Many developers wait until the product is almost finished to save stable versions, but by then it's already too late. You should start using Git from the moment your project has its first working version. Think of Git as a game save system:</p>
<ul>
  <li>Save a version every time you complete a stable feature</li>
  <li>Create a new branch before making major changes</li>
  <li>Merge the branch if changes work, or roll back if they fail</li>
</ul>
<p>This gives you the confidence to let Codex make large-scale modifications without worrying that one mistake will require another AI to fix the problems created by the first one.</p>
<p>Level 2 solves the problem of "AI forgetting what it's doing". Level 3 solves the problem of "what if the AI breaks the project". With documents and version control in place, Codex can already complete projects reliably.</p>

<h2 id="level-4">Level 4: Integrate with the Open Source Ecosystem</h2>
<p>But if you have to build every capability from scratch, the efficiency is still too low. That's why Level 4 is about integrating with the open source ecosystem.</p>
<p>At this level, you can:</p>
<ul>
  <li>Package your own workflows into reusable skills</li>
  <li>Directly use open source skills and complete projects from the community</li>
</ul>
<p>A great example is ByteDance's Deer Flow, which I use frequently for research tasks. Previously, I would have to manually search for information, filter results, compare different viewpoints, and compile reports. Now, I just submit a research topic, and Deer Flow will call tools and agents to handle the entire research process and deliver the final report.</p>
<p>Deer Flow is just one example. GitHub has thousands of ready-made skills, agent frameworks, and open source tools available. You don't even need to understand how every line of code works. Just send the project URL to Codex and ask it to:</p>
<pre><code class="language-text">"Download this project, get it running, and tell me how to use it"</code></pre>
<p>Codex will read the documentation, set up the environment, resolve errors, and deliver a working version to you.</p>
<p>In my own usage, I've called over 1,000 skills, with "superpowers" being the most frequently used. At this level, Codex is no longer just a code generator — it can integrate existing capabilities directly into your workflow.</p>

<h2 id="level-5">Level 5: Multi-Agent Collaboration</h2>
<p>At Level 4, you still need to call skills and open source projects one by one. Level 5 is about multi-agent collaboration, where you submit a final goal and let Codex determine what capabilities it needs to use to complete the entire task.</p>
<p>Level 5 integrates all the previous four levels into a single system:</p>
<ol>
  <li>A main agent first reads the project documents, manages versions with Git, and calls the necessary skills and open source tools</li>
  <li>Then it creates specialized agents for different stages:
    <ul>
      <li>Market research agent</li>
      <li>Requirements organization agent</li>
      <li>Architecture design agent</li>
      <li>Software development agent</li>
      <li>Quality testing agent</li>
    </ul>
  </li>
  <li>These agents work in parallel toward the same goal</li>
  <li>Finally, the main agent summarizes the results and delivers the complete project to you</li>
</ol>
<p>Interestingly, the highest level actually brings you back to a simpler operation. You still submit tasks in the chat box, but there's a critical difference:</p>
<ul>
  <li>Level 1: One AI gets the request and immediately starts generating</li>
  <li>Level 5: A main agent first understands the goal, then organizes an entire team of agents to work for you</li>
</ul>
<p>The 16-hour continuous task I ran was completed using this multi-agent collaboration approach, covering everything from requirements analysis and market research to product design, development, and final delivery.</p>
<p>The power of Level 5 isn't about how many agents run at the same time — it's about you clearly defining the final goal, and letting the system break it down, organize the work, and complete the entire process.</p>

<h2 id="conclusion">Conclusion</h2>
<p>Level 5 seems to come full circle. You're still submitting tasks in the chat box, but what you submit has changed. In Level 1, you submit a single instruction. In Level 5, you submit a complete, well-defined goal.</p>
<p>This is the journey from demo to production: starting with simple generation, moving through documentation and version control, leveraging the open source ecosystem, and finally orchestrating entire agent teams to deliver complete projects.</p>

<h2>常见问题</h2>

<h3>Why do most users get stuck at Level 1?</h3>
<p>Because Level 1 looks deceptively good. You type a task, Codex produces a nice-looking page or demo in minutes, and that feels like success. The problem only appears with complexity: mismatched functionality, broken layouts, and regressions where a tiny change breaks previously working code. Level 1 is fine for throwaway demos, but without documents and version control, those outputs rarely survive into maintainable projects — which is exactly why you need to reach at least Level 3 for real work.</p>

<h3>What are the three core documents in Level 2?</h3>
<p>Product requirements (what the product should do), software architecture (how the pieces fit together), and current progress (what's done and what's pending). You don't write them from scratch — you ask Codex to interview you with clarifying questions, then generate the documents from your answers. Before each new task, Codex reads these documents, drafts a plan, and confirms it with you. After finishing, it syncs the results back into the progress document.</p>

<h3>Why is Git version control the most overlooked step?</h3>
<p>Because most vibe coders only think about saving once the product is nearly finished — and by then it's too late. Git should start at the first working version. Treat it like a game save system: commit after every stable feature, branch before major changes, merge on success or roll back on failure. That safety net is what gives you the confidence to let Codex attempt large-scale modifications without fearing that one mistake will cascade into more AI fixes.</p>

<h3>What's the real difference between Level 1 and Level 5?</h3>
<p>In Level 1 you submit a single instruction and one AI immediately starts generating. In Level 5 you submit a well-defined final goal, and a main agent breaks it down — reading project documents, managing Git versions, calling open source skills — then spawns specialized agents (market research, requirements, architecture, development, testing) that work in parallel. You end up back at the chat box, but what you submit has changed from a prompt to a complete goal.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Ready to move Codex up the levels? Continue with these guides:</p>
  <ul>
    <li><a href="/article/codex-agent-desktop-jarvis">Codex Agent: Your Desktop Jarvis for Effortless Task Automation</a> — the desktop AI agent built around Codex for everyday task automation</li>
    <li><a href="/article/multi-agent-collaboration-architecture">Multi-Agent Collaboration Architecture</a> — the architecture behind Level 5's parallel agent teams</li>
    <li><a href="/article/git-github-beginners-guide">Git &amp; GitHub Beginner's Guide: Core Concepts &amp; Operation</a> — everything you need to set up the Level 3 version-control foundation</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">📖 AI教程</span>
  <span class="meta-badge">🕒 阅读约8分钟</span>
  <span class="meta-badge">📅 2026年8月22日</span>
  <span class="meta-badge">🎯 进阶</span>
</div>

<h2 id="introduction">引言</h2>
<p>18天里，我在Codex中运行了400个任务，总共消耗710亿token。最长的一个任务用GPT-5.6连续跑了16小时。但我发现许多用户只用最基础的Codex——直接在聊天框提交请求，生成结果后就停止。本文将Codex的使用拆解为5个层级，并解释为什么你需要达到Level 3才能把Codex变成可靠的生产工具。</p>

<h2 id="level-1">Level 1：直接任务提交</h2>
<p>Level 1是使用Codex最简单的方式：直接在聊天框提交任务。你可以让Codex创建一个网页、构建一个小游戏或实现一个简单功能，通常几分钟就能得到看起来不错的成果。</p>
<p>然而，这种方法有致命局限。一旦任务变复杂，你常会遇到这些问题：功能不符合预期、布局不合理，或者一个很小的改动（比如改一个按钮）就导致整个页面崩溃。经过几轮修改后，之前完成的工作也可能失效。这就是为什么Level 1的输出几乎永远只是demo，很难成长为长期可维护的项目。</p>

<h2 id="level-2">Level 2：文档驱动工作流</h2>
<p>当你意识到需要帮Codex记住项目应该做什么时，就进入Level 2：文档驱动开发。</p>
<p>工作流如下：</p>
<ol>
  <li>开工前创建一个专用项目文件夹</li>
  <li>准备三份核心文档：
    <ul>
      <li>产品需求</li>
      <li>软件架构</li>
      <li>当前进度</li>
    </ul>
  </li>
  <li>这些文档不需要从零写——让Codex向你提出澄清问题，然后根据你的回答生成文档</li>
  <li>每次开始新任务前，先让Codex阅读这些文档、制定工作计划，并在执行前与你确认</li>
  <li>任务完成后，把结果同步回进度文档</li>
</ol>
<p>这相当于给项目装了一个"外部大脑"。即使对话变得很长或你创建新任务，Codex也始终明白产品要做什么、项目进展到哪、哪些部分不能改。在这个层级，你不再只是思考提示词——你思考的是产品需求、功能拆解和软件架构。</p>
<p>但文档只能防止Codex忘记项目，无法防止它破坏项目。</p>

<h2 id="level-3">Level 3：代码管理</h2>
<p>这就是Level 3登场的地方：代码管理。这一步是大多数Vibe coder最常忽略的。</p>
<p>许多开发者等到产品快做完才保存稳定版本，但那时已经太晚。你应该在项目有第一个可用版本时就使用Git。把Git想成游戏存档系统：</p>
<ul>
  <li>每完成一个稳定功能就保存一个版本</li>
  <li>做大改动前先新建一个分支</li>
  <li>改动成功就合并分支，失败就回滚</li>
</ul>
<p>这给了你让Codex做大规模改动的信心，而不用担心一个失误需要另一个AI来收拾前一个AI闯的祸。</p>
<p>Level 2解决"AI忘记自己在做什么"的问题，Level 3解决"AI搞坏了项目怎么办"的问题。有了文档和版本控制，Codex已经能可靠地完成项目。</p>

<h2 id="level-4">Level 4：集成开源生态</h2>
<p>但如果每个能力都要从零构建，效率仍然太低。这就是Level 4的意义：集成开源生态。</p>
<p>在这个层级，你可以：</p>
<ul>
  <li>把自己的工作流打包成可复用的技能（skills）</li>
  <li>直接使用社区的现成技能和完整项目</li>
</ul>
<p>一个绝佳例子是字节跳动的Deer Flow，我经常用它做研究任务。以前我需要手动搜索信息、筛选结果、对比不同观点、编写报告。现在，我只要提交一个研究主题，Deer Flow就会调用工具和Agent处理整个研究流程并交付最终报告。</p>
<p>Deer Flow只是一个例子。GitHub上有成千上万的现成技能、Agent框架和开源工具。你甚至不需要理解每一行代码。只需把项目URL发给Codex并让它：</p>
<pre><code class="language-text">"下载这个项目，让它跑起来，告诉我怎么用"</code></pre>
<p>Codex会阅读文档、配置环境、解决报错，然后交付一个可用的版本给你。</p>
<p>在我自己的使用中，我已经调用过超过1000个技能，其中最常用的是"superpowers"。在这个层级，Codex不再只是代码生成器——它能把现有能力直接集成到你的工作流中。</p>

<h2 id="level-5">Level 5：多Agent协作</h2>
<p>在Level 4，你仍需要逐个调用技能和开源项目。Level 5是多Agent协作：你提交一个最终目标，让Codex自己决定需要调用哪些能力来完成整个任务。</p>
<p>Level 5把前四个层级整合进一个系统：</p>
<ol>
  <li>主Agent先阅读项目文档、用Git管理版本、调用必要的技能和开源工具</li>
  <li>然后为不同阶段创建专门Agent：
    <ul>
      <li>市场调研Agent</li>
      <li>需求整理Agent</li>
      <li>架构设计Agent</li>
      <li>软件开发Agent</li>
      <li>质量测试Agent</li>
    </ul>
  </li>
  <li>这些Agent并行朝同一目标工作</li>
  <li>最后主Agent汇总结果，把完整项目交付给你</li>
</ol>
<p>有趣的是，最高层级反而回到更简单的操作。你仍然在聊天框提交任务，但有一个关键区别：</p>
<ul>
  <li>Level 1：一个AI收到请求立即开始生成</li>
  <li>Level 5：主Agent先理解目标，再组织一整个Agent团队为你工作</li>
</ul>
<p>我运行的那个16小时连续任务，就是用这种多Agent协作方式完成的，覆盖了从需求分析、市场调研到产品设计、开发和最终交付的全过程。</p>
<p>Level 5的力量不在于同时运行多少个Agent——而在于你清晰定义最终目标，让系统去拆解它、组织工作、完成整个流程。</p>

<h2 id="conclusion">结语</h2>
<p>Level 5似乎回到了起点。你仍然在聊天框提交任务，但提交的内容变了。在Level 1，你提交一条指令。在Level 5，你提交一个完整、定义清晰的目标。</p>
<p>这就是从demo到生产的旅程：从简单生成出发，经过文档和版本控制，利用开源生态，最终编排整个Agent团队来交付完整项目。</p>

<h2>常见问题</h2>

<h3>为什么大多数用户卡在Level 1？</h3>
<p>因为Level 1看起来出奇地好。你输入一个任务，Codex几分钟就产出一个漂亮的页面或demo，这感觉就像成功。问题只在复杂时出现：功能不匹配、布局崩坏、以及"改一处小地方导致之前能用代码失效"的回退。Level 1适合一次性demo，但没有文档和版本控制，这些产出很难长成可维护的项目——这正是为什么真正的项目工作至少要达到Level 3。</p>

<h3>Level 2的三份核心文档是什么？</h3>
<p>产品需求（产品应该做什么）、软件架构（各部分如何组合）、当前进度（什么做完了、什么待办）。这些文档不用从零写——你让Codex用澄清问题来采访你，然后根据回答生成文档。每次新任务前，Codex会阅读这些文档、起草计划并和你确认。完成后，再把结果同步回进度文档。</p>

<h3>为什么Git版本控制是最容易被忽略的一步？</h3>
<p>因为大多数vibe coder只想着等产品快做完再保存，而那时已经太晚。Git应该在第一个可用版本时就启用。把它当作游戏存档系统：每个稳定功能后提交一次，大改动前开分支，成功就合并、失败就回滚。这个安全网给了你让Codex尝试大规模改动的信心，而不用担心一次失误会引发更多AI返工。</p>

<h3>Level 1和Level 5的真正区别是什么？</h3>
<p>Level 1是提交一条指令，一个AI收到后立即开始生成。Level 5是提交一个定义良好的最终目标，主Agent先拆解它——阅读项目文档、管理Git版本、调用开源技能——然后派生专门Agent（市场调研、需求、架构、开发、测试）并行工作。你最终回到聊天框，但提交的内容从提示词变成了完整目标。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>想让Codex升级到更高的层级？继续阅读这些指南：</p>
  <ul>
    <li><a href="/article/codex-agent-desktop-jarvis">Codex Agent：你的桌面贾维斯，轻松实现任务自动化</a> — 围绕Codex构建的桌面AI代理，用于日常任务自动化</li>
    <li><a href="/article/multi-agent-collaboration-architecture">多智能体协作架构：终极版问答工具</a> — Level 5并行Agent团队背后的架构</li>
    <li><a href="/article/git-github-beginners-guide">Git与GitHub初学者指南：核心概念与操作</a> — 搭建Level 3版本控制基础所需的一切</li>
  </ul>
</div>`,
  },
"""

last = s.rfind('};')
with open('src/lib/article-content.ts', 'w', encoding='utf-8', newline='\n') as f:
    f.write(s[:last] + content + '};')
print('Part 2 done')

print('ALL DONE')
