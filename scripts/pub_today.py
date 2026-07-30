"""Publish July 30, 2026 — 1 article, no new tools."""
import os; BASE = r"C:\Users\jun\aistudyonline-next"; os.chdir(BASE)

with open('src/lib/articles.ts', 'r', encoding='utf-8') as f: s = f.read()
a = r"""  {
    slug: "ai-beginners-quick-guide-common-jargon-explained",
    title: "AI Beginner's Quick Guide: Common Jargon Explained",
    titleZh: "AI新手速成指南：常见术语一读就懂",
    description: "A jargon-free introduction to 8 core AI concepts — LLM (brain), Prompt (command), Agent (employee), Codex (coding specialist), Skill (SOP), Workflow (step sequence), API (connector), and Knowledge Base (filter) — explained through everyday analogies a beginner can grasp in one sitting.",
    descriptionZh: "用生活类比轻松理解8个核心AI概念——LLM（大脑）、Prompt（指令）、Agent（员工）、Codex（编程专家）、Skill（标准操作流程）、Workflow（步骤序列）、API（连接器）和知识库（信息过滤器）——新手一次读完就能理解。",
    category: "ai-basics",
    tags: ["AI Basics", "LLM", "Agent", "Prompt", "Skill", "Workflow", "Beginner", "Jargon"],
    difficulty: "beginner",
    toolsMentioned: ["ChatGPT", "Claude", "Codex Agent"],
    date: "2026-07-30",
  },

"""
last = s.rfind('];')
with open('src/lib/articles.ts', 'w', encoding='utf-8') as f: f.write(s[:last] + a + '];')
print('Part 1 done')

with open('src/lib/article-content.ts', 'r', encoding='utf-8') as f: c = f.read()
n = r'''
  "ai-beginners-quick-guide-common-jargon-explained": {
    content: `<div class="meta-banner">
  <span class="meta-badge">🧠 AI Basics</span>
  <span class="meta-badge">🕒 5 min read</span>
  <span class="meta-badge">📅 Jul 30, 2026</span>
  <span class="meta-badge">🎯 Beginner</span>
</div>

<h2 id="introduction">Introduction</h2>

<p>If you've ever tried to learn AI, you've probably felt overwhelmed by terms like "large model," "Codex," "Skill," and "Prompt" floating around online. This guide breaks down these key concepts using real-life examples, so you can understand them clearly and apply them right away.</p>

<h2 id="llm">1. Large Language Model (LLM)</h2>

<p>A large language model is like the <strong>brain</strong> of an AI system. Different models have different capabilities — some are better at reasoning, others at coding, and some at creative writing.</p>

<h3>Example</h3>
<ul>
  <li><strong>Model A</strong>: When told "the table is dirty," it only writes a note saying "the table is dirty" instead of cleaning it.</li>
  <li><strong>Model B</strong>: When told "the table is dirty," it immediately grabs a cloth and cleans the table.</li>
</ul>
<p>This shows that the model you choose directly determines how "smart" your AI will be. Common LLMs: GPT-4o, Claude 3, Gemini, Doubao, DeepSeek.</p>

<h2 id="prompt">2. Prompt</h2>

<p>A prompt is the <strong>command</strong> you give to an AI. The more specific your prompt is, the more accurate the AI's response will be.</p>

<h3>Bad Prompt Example</h3>
<pre><code class="language-text">Give me something to drink.</code></pre>
<p>This vague prompt might result in the AI giving you a watering can instead of a beverage.</p>

<h3>Good Prompt Example</h3>
<pre><code class="language-text">I am a human. It's very hot today, and I want to drink something cold, sweet, tasty, and cheap.</code></pre>
<p>This clear prompt will likely result in the AI giving you a suitable cold drink.</p>

<h2 id="agent">3. Agent</h2>

<p>An Agent is an <strong>AI employee</strong> that can understand tasks, use tools, and work independently to complete them.</p>

<h3>Example</h3>
<p>When you ask an Agent to find a book: it first checks the fridge (no books there), then searches its internal knowledge base (no books there), and finally checks the external library and finds the book you want. This shows that an Agent can take initiative to solve problems without constant guidance.</p>

<h2 id="codex">4. Codex</h2>

<p>Codex is a <strong>programming-savvy AI employee</strong> that specializes in writing and understanding code.</p>

<h3>Example</h3>
<p>If you ask an Agent to find a book, it will search for books. If you ask Codex to find a book, it might write a Python script to search for books automatically:</p>

<pre><code class="language-python">def find_book(book_title):
    library = ["The Great Gatsby", "1984", "To Kill a Mockingbird"]
    for book in library:
        if book_title.lower() in book.lower():
            return f"Found: {book}"
    return "Book not found"

print(find_book("1984"))</code></pre>

<h2 id="skill">5. Skill</h2>

<p>A Skill is a <strong>standard operating procedure (SOP)</strong> for an Agent. It tells the Agent how to perform a specific task consistently.</p>

<h3>Example</h3>
<p>If an Agent keeps finding the wrong books, you can give it a Skill document that says: "Book Search Skill: 1. Only search the bookshelf in the living room. 2. Look for books with red covers. 3. Check the first page to confirm it's the right book." Now, every time the Agent searches for a book, it will follow these steps and find the right one.</p>

<h2 id="workflow">6. Workflow</h2>

<p>A Workflow is a <strong>sequence of steps</strong> that an Agent follows to complete a task. A workflow for finding and returning a book might be: Find the book → Clean the book → Return the book to the shelf.</p>

<h2 id="api">7. API</h2>

<p>An API is a <strong>plug</strong> that connects an AI to other tools or software. If you want your AI to send emails, you can use an email API to connect your AI to an email service. This way, the AI can send emails without having its own built-in email functionality.</p>

<h2 id="knowledge-base">8. Knowledge Base</h2>

<p>A Knowledge Base is a <strong>database</strong> that limits the information an AI can use. If you want your AI to only answer questions about your company's products, you can set up a knowledge base that only contains information about your products. This way, the AI won't use information from the internet or other sources.</p>

<h2 id="summary">Summary</h2>
<ul>
  <li><strong>LLM</strong>: The brain of the AI</li>
  <li><strong>Prompt</strong>: The command you give to the AI</li>
  <li><strong>Agent</strong>: An AI employee that can work independently</li>
  <li><strong>Codex</strong>: An AI employee that specializes in coding</li>
  <li><strong>Skill</strong>: A standard operating procedure for an Agent</li>
  <li><strong>Workflow</strong>: A sequence of steps for completing a task</li>
  <li><strong>API</strong>: A plug that connects an AI to other tools</li>
  <li><strong>Knowledge Base</strong>: A database that limits the AI's information sources</li>
</ul>

<h2>常见问题</h2>

<h3>How is this different from the July 2 "Don't Be Intimidated by AI Jargon" article?</h3>
<p>The July 2 article covers <strong>12 advanced concepts</strong> (Token, RAG, MCP, Context Engineering, Harness Engineering, Workspace Agent, etc.) with code examples — it's designed for intermediate readers who want to understand the full AI stack. This article covers <strong>8 foundational concepts</strong> (LLM, Prompt, Agent, Codex, Skill, Workflow, API, Knowledge Base) using everyday analogies — it's designed for absolute beginners who just want to understand what these terms mean. Read this one first if you're brand new. Read the July 2 article when you're ready to go deeper into AI architecture and implementation.</p>

<h3>Why do these 8 concepts matter for someone who just wants to use AI tools?</h3>
<p>Because every AI tool you'll encounter — whether it's ChatGPT, WorkBuddy, Codex, or Doubao — uses these concepts. <strong>LLM</strong> determines how smart your tool is. <strong>Prompt</strong> determines whether you get useful output or garbage. <strong>Agent</strong> is what separates modern AI tools from simple chatbots. <strong>Skill/Workflow</strong> is how you automate your work. <strong>Knowledge Base</strong> is how you make AI answer from your company's documents instead of making things up. Understanding these 8 concepts isn't academic — it directly impacts how effectively you use whatever AI tool you've chosen.</p>

<h3>Do I need to remember all the technical details in this guide?</h3>
<p>No. Focus on the <strong>analogies</strong>, not the technical details. LLM = brain. Prompt = command. Agent = employee. Skill = SOP. Workflow = step sequence. API = plug. Knowledge Base = filter. If you remember these one-to-one mappings, you'll have the mental model you need to navigate any AI tool. The technical details in this guide are there so you can recognize the terms when you see them, not because you need to memorize them.</p>

<h3>What should I learn after mastering these 8 concepts?</h3>
<p>Move on to <strong>Practicing with real tasks</strong>. Each tool does these 8 things differently. Don't try to memorize — just be aware of these concepts and experience them firsthand.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Understood the basics? Put them into practice:</p>
  <ul>
    <li><a href="/articles/correct-way-to-collaborate-with-ai-practical-guide">The Correct Way to Collaborate with AI: A Practical Guide</a> — apply these concepts to real tasks</li>
    <li><a href="/articles/dont-be-intimidated-ai-jargon-practical-guide-concepts">Don't Be Intimidated by AI Jargon: A Practical Guide to AI Concepts</a> — go deeper into 12 advanced concepts</li>
    <li><a href="/articles/how-to-build-personal-ai-quant-trading-system-2026">How to Build a Personal AI Quant Trading System in 2026</a> — see Agents, Skills and Workflows in a real system</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">🧠 AI 基础</span>
  <span class="meta-badge">🕒 阅读约5分钟</span>
  <span class="meta-badge">📅 2026年7月30日</span>
  <span class="meta-badge">🎯 入门</span>
</div>

<h2 id="introduction">引言</h2>
<p>如果你曾尝试学习AI，大概被网上飘着的"大模型""Codex""Skill""Prompt"等术语搞得一头雾水。本指南用生活实例拆解这些核心概念，让你一次读懂、即刻能用。</p>

<h2 id="llm">1. 大语言模型（LLM）</h2>
<p>大语言模型就像AI系统的<strong>大脑</strong>。不同模型有不同能力——有的擅长推理，有的擅长编码，有的擅长创意写作。</p>
<h3>示例</h3>
<ul>
  <li><strong>模型A</strong>：被告知"桌子脏了"，它只写了张"桌子脏了"的便条而非清理。</li>
  <li><strong>模型B</strong>：被告知"桌子脏了"，立刻拿起抹布擦干净。</li>
</ul>
<p>这说明你选的模型直接决定AI有多"聪明"。常见LLM：GPT-4o、Claude 3、Gemini、豆包、DeepSeek。</p>

<h2 id="prompt">2. Prompt（提示词）</h2>
<p>Prompt是你给AI的<strong>指令</strong>。越具体，AI回复越精准。</p>
<h3>坏提示词</h3>
<pre><code class="language-text">给我喝的。</code></pre>
<h3>好提示词</h3>
<pre><code class="language-text">我是人类。今天很热，我想喝冷的、甜的、好喝的、便宜的东西。</code></pre>

<h2 id="agent">3. Agent（智能体）</h2>
<p>Agent是能理解任务、使用工具、独立完成工作的<strong>AI员工</strong>。如让Agent找书：先查冰箱（没书）→搜内部知识库（没书）→查外部图书馆→找到目标书籍。无需持续指导就能主动解决问题。</p>

<h2 id="codex">4. Codex</h2>
<p>Codex是<strong>精通编程的AI员工</strong>，专长编写和理解代码。让普通Agent找书它会直接搜索；让Codex找书它可能写一段Python自动搜索。</p>

<h2 id="skill">5. Skill（技能）</h2>
<p>Skill是Agent的<strong>标准操作流程（SOP）</strong>，告诉Agent如何始终如一完成特定任务。如"书籍搜索技能：1.只搜索客厅书架 2.找红色封面 3.检查首页确认正确"。之后每次搜书都按此执行。</p>

<h2 id="workflow">6. Workflow（工作流）</h2>
<p>Workflow是Agent完成任务的<strong>步骤序列</strong>。如找书还书流程：找到书→清洁书→放回书架。</p>

<h2 id="api">7. API</h2>
<p>API是连接AI到其他工具软件的<strong>插头</strong>。想让AI发送邮件，用邮件API连接AI到邮件服务，AI无需内置邮件功能就能发邮件。</p>

<h2 id="knowledge-base">8. 知识库</h2>
<p>知识库是限制AI可用信息的<strong>数据库</strong>。想让AI只回答公司产品相关问题，设置只含产品信息的知识库，AI就不会使用互联网或其他来源的信息。</p>

<h2 id="summary">总结</h2>
<ul>
  <li><strong>LLM</strong>：AI的大脑</li>
  <li><strong>Prompt</strong>：给AI的指令</li>
  <li><strong>Agent</strong>：能独立工作的AI员工</li>
  <li><strong>Codex</strong>：专精编程的AI员工</li>
  <li><strong>Skill</strong>：Agent的标准操作流程</li>
  <li><strong>Workflow</strong>：完成任务的步骤序列</li>
  <li><strong>API</strong>：连接AI到其他工具的插头</li>
  <li><strong>知识库</strong>：限制AI信息来源的数据库</li>
</ul>

<h2>常见问题</h2>

<h3>这和7月2日"别被AI术语吓倒"那篇文章有什么不同？</h3>
<p>7月2日文章涵盖<strong>12个进阶概念</strong>（Token、RAG、MCP、上下文工程、Harness工程、Workspace Agent等），含代码示例——为想理解完整AI技术栈的中级读者设计。本文涵盖<strong>8个基础概念</strong>（LLM、Prompt、Agent、Codex、Skill、Workflow、API、知识库），用生活类比——为只想理解这些术语含义的纯新手设计。如果你完全零基础，先读这篇。准备好深入AI架构和实现时再读7月2日那篇。</p>

<h3>对只想用AI工具的人来说，这8个概念为什么重要？</h3>
<p>因为你遇到的每个AI工具——ChatGPT、WorkBuddy、Codex或豆包——都用这些概念。<strong>LLM</strong>决定工具有多聪明。<strong>Prompt</strong>决定你得到有用输出还是垃圾。<strong>Agent</strong>是现代AI工具和简单聊天机器人的分界线。<strong>Skill/Workflow</strong>是你自动化工作的方式。<strong>知识库</strong>是让AI从公司文档而非凭空编造来回答的方式。理解这8个概念不是学术——它直接影响你使用任何AI工具的效能。</p>

<h3>需要记住指南中所有技术细节吗？</h3>
<p>不需要。聚焦<strong>类比</strong>而非技术细节。LLM=大脑。Prompt=指令。Agent=员工。Skill=SOP。Workflow=步骤序列。API=插头。知识库=过滤器。记住这些一一对应关系，你就有了驾驭任何AI工具的心智模型。技术细节只是让你看到术语时能认出它们，而非需要背诵。</p>

<h3>掌握8个概念后该学什么？</h3>
<p>转向<strong>真实任务练习</strong>。每个工具对这8件事的实现方式不同。不要死记硬背——只需知晓这些概念并亲身体验。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>理解了基础？付诸实践：</p>
  <ul>
    <li><a href="/articles/correct-way-to-collaborate-with-ai-practical-guide">与AI正确协作的方式：一份实用指南</a> — 将这些概念应用到真实任务</li>
    <li><a href="/articles/dont-be-intimidated-ai-jargon-practical-guide-concepts">别被AI术语吓倒：从ChatGPT到Workspace Agent的AI概念实战指南</a> — 深入12个进阶概念</li>
    <li><a href="/articles/how-to-build-personal-ai-quant-trading-system-2026">2026个人AI量化交易系统搭建全指南</a> — 看Agent、Skill和Workflow在真实系统中的运作</li>
  </ul>
</div>`,
  },

'''
last = c.rfind('};')
with open('src/lib/article-content.ts', 'w', encoding='utf-8') as f: f.write(c[:last] + n + '};')
print('Part 2 done\n=== Done ===')