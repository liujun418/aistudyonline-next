"""Publish Aug 25, 2026 — 1 article (WorkBuddy + IMA second brain), add IMA Knowledge Base tool."""
import os

BASE = r"C:\Users\jun\aistudyonline-next"
os.chdir(BASE)

SLUG = "build-ai-second-brain-workbuddy-ima-knowledge-base"

# ---------------------------------------------------------------------------
# Part 1: articles.ts
# ---------------------------------------------------------------------------
a = r"""  {
    slug: "build-ai-second-brain-workbuddy-ima-knowledge-base",
    title: "Step-by-Step Guide: Build Your AI Second Brain with WorkBuddy + IMA Knowledge Base",
    titleZh: "分步指南：用WorkBuddy + IMA知识库打造你的AI第二大脑",
    description: "A step-by-step guide to building an AI second brain with WorkBuddy + IMA Knowledge Base. Master three core steps — Connect (authorize and import documents), Use (the 'Based on IMA Knowledge Base' prefix for hallucination-free answers), and Update (keep your knowledge fresh) — plus the advanced bidirectional closed-loop workflow powered by the IMA OpenAPI that auto-saves AI output back into your knowledge base.",
    descriptionZh: "用WorkBuddy + IMA知识库打造AI“第二大脑”的分步指南。掌握三大核心步骤——连接（授权并导入文档）、使用（“基于IMA知识库”前缀获得低幻觉答案）、更新（保持知识新鲜）——以及基于IMA OpenAPI的双向闭环高级玩法，让AI生成的内容自动回存到知识库。",
    category: "ai-tutorials",
    tags: ["WorkBuddy", "IMA", "Knowledge Base", "Second Brain", "RAG", "Tencent", "Productivity", "Tutorial"],
    difficulty: "beginner",
    toolsMentioned: ["Tencent WorkBuddy", "IMA Knowledge Base"],
    date: "2026-08-25",
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
content = r"""  "build-ai-second-brain-workbuddy-ima-knowledge-base": {
    content: `<div class="meta-banner">
  <span class="meta-badge">📚 AI Tutorials</span>
  <span class="meta-badge">🕒 7 min read</span>
  <span class="meta-badge">📅 Aug 25, 2026</span>
  <span class="meta-badge">🎯 Beginner</span>
</div>

<h2 id="introduction">Introduction</h2>

<p>Many users face a common pain point when using WorkBuddy: it excels at answering general questions but struggles with personalized or company-specific content. This tutorial will walk you through integrating WorkBuddy with IMA Knowledge Base to create an AI "second brain" — enabling your assistant to access your private documents and deliver accurate, context-aware responses instead of generic guesses.</p>

<h2 id="three-core-steps">Three Core Steps to Master IMA Knowledge Base</h2>

<p>The process is divided into three simple phases: <strong>Connect, Use, and Update</strong>. You can implement all of them immediately after reading this guide.</p>

<h2 id="step-1-connect">Step 1: Connect to IMA Knowledge Base (Build Your Knowledge Library)</h2>

<p>Think of this step as building a dedicated library for your AI. You'll store all your notes, documents, and reference materials here, so the AI can retrieve information directly from these files instead of generating generic responses.</p>

<h3>3 Key Operations to Complete the Connection</h3>

<ol>
  <li><strong>Authorize the Connection</strong>
    <ul>
      <li>Click the "+" button next to the input box in WorkBuddy.</li>
      <li>Select "Connector" and choose "IMA Knowledge Base".</li>
      <li>Log in with your account to grant WorkBuddy access permissions.</li>
    </ul>
  </li>
  <li><strong>Create and Import Resources</strong>
    <ul>
      <li>Open the IMA Knowledge Base management page.</li>
      <li>Create a new knowledge base (e.g., "WorkBuddy Mastery Guide").</li>
      <li>Upload your basic files (supports PDF, Word, PPT, Excel, TXT, and other common formats).</li>
    </ul>
  </li>
  <li><strong>Enable Connector Synchronization</strong>
    <ul>
      <li>Return to the main WorkBuddy interface.</li>
      <li>Find the IMA Knowledge Base connector in the added connectors list.</li>
      <li>Turn on the synchronization switch to enable real-time knowledge sharing.</li>
    </ul>
  </li>
</ol>

<h2 id="step-2-use">Step 2: Use the Knowledge Base (One Prefix for Precise Answers)</h2>

<p>Using the integrated system is extremely simple. Just add the prefix <strong>"Based on IMA Knowledge Base"</strong> to your questions, and WorkBuddy will only retrieve answers from your uploaded materials, significantly reducing hallucinations.</p>

<h3>Two Common Usage Scenarios</h3>

<ol>
  <li><strong>Question &amp; Answer Interaction</strong>

<pre><code class="language-text">Based on IMA Knowledge Base, answer: [Your specific question]</code></pre>

<p>This format ensures the AI provides direct, verifiable answers based on your documents.</p>
  </li>
  <li><strong>Creative Generation</strong>

<pre><code class="language-text">Based on IMA Knowledge Base, help me write a report/article/summary</code></pre>

<p>The AI will use factual data from your knowledge base to generate content that fits your business scenario.</p>
  </li>
</ol>

<h2 id="step-3-update">Step 3: Update the Knowledge Base (Manual Upload for Continuous Improvement)</h2>

<p>Building a knowledge base isn't a one-time task — you need to add new content regularly to keep it useful.</p>

<h3>3 Steps to Update Your Knowledge Base</h3>

<ol>
  <li><strong>Open the Knowledge Base</strong>: Log in to the IMA Knowledge Base management interface and navigate to the target directory where you want to add content.</li>
  <li><strong>Trigger the Upload</strong>: Click the "Upload" button in the toolbar and select local files from your computer (supports batch uploads).</li>
  <li><strong>Automatic Parsing and Storage</strong>: Confirm the selected files — the system will automatically identify file formats, extract key information, and complete parsing. The new content will be synchronized to the knowledge base in real time.</li>
</ol>

<h2 id="advanced-closed-loop">Advanced Play: Bidirectional Closed-Loop Workflow</h2>

<p>To make your knowledge base even more powerful, you can set up a bidirectional closed-loop system that automatically saves AI-generated content back into the knowledge base.</p>

<h3>Prerequisite</h3>

<p>First, configure the IMA Knowledge Base API in the "Connector" module — this is the core switch for bidirectional data flow.</p>

<h3>Implementation Steps</h3>

<ol>
  <li><strong>Get OpenAPI Credentials</strong>: Open <code>https://ima.qq.com/agent-interface</code> and log in. Apply for and obtain two values:

<pre><code class="language-text">Client ID
API Key</code></pre>
  </li>
  <li><strong>Configure the API</strong>: Send the obtained API Key to the IMA skill to complete the configuration.</li>
  <li><strong>Automatic Closed-Loop Operation</strong>: After WorkBuddy generates content (such as meeting minutes, reports, or summaries), you can directly instruct it:

<pre><code class="language-text">Save this content as an IMA note and upload it to the knowledge base</code></pre>

<p>The AI will automatically complete the upload, forming a closed loop: <strong>Retrieve from Knowledge Base → AI Process &amp; Generate → Auto-Save Back to Knowledge Base</strong>.</p>
  </li>
</ol>

<h2 id="more-connectors">More Connector Options</h2>

<p>In addition to IMA Knowledge Base, WorkBuddy supports seamless integration with multiple platforms:</p>

<ul>
  <li><strong>Feishu</strong>: Real-time synchronization of document messages and multi-dimensional tables.</li>
  <li><strong>Tencent Docs</strong>: Direct reading and writing of cloud files.</li>
  <li><strong>Lexiang Knowledge Base</strong>: Enterprise internal knowledge linkage.</li>
  <li><strong>Tencent Meeting</strong>: Automatic organization and synchronization of meeting minutes.</li>
</ul>

<h2 id="important-reminders">Important Reminders</h2>

<p>To maintain the accuracy of your knowledge base, follow these best practices:</p>

<ol>
  <li><strong>Clean Up Redundant "Digital Junk"</strong>: Regularly delete expired, invalid, or low-value documents. These files not only occupy storage space but also affect the system's response accuracy.</li>
  <li><strong>Beware of Information Interference</strong>: "Noise" in the knowledge base can interfere with the algorithm's judgment logic — leading to fuzzy search results, incorrect answers, or even unprofessional responses.</li>
  <li><strong>Maintain a "Pure" Knowledge Base</strong>: Keeping the knowledge base "clean and pure" is the key to improving response quality. Pure knowledge allows the system to lock in valid information and output professional answers that meet your needs.</li>
</ol>

<h2 id="conclusion">Conclusion</h2>

<p>The integration follows a simple rhythm: establish a <strong>"weekly self-check + monthly review"</strong> mechanism, let each business department take responsibility for cleaning up the content under its jurisdiction, and set up automatic expiration reminders for key information to ensure the "freshness" and "purity" of the knowledge base from the source.</p>

<p>By following this guide, you'll transform WorkBuddy into a truly personalized AI assistant that grows with your knowledge and business needs. Start building your AI second brain today!</p>

<h2>常见问题</h2>

<h3>What is the difference between this guide and the earlier WorkBuddy + IMA tutorial?</h3>
<p>The earlier guide (<a href="/article/build-personal-ai-knowledge-base-workbuddy-ima-guide">Build Your Personal AI Knowledge Base with WorkBuddy + IMA</a>) focuses on installation, connection, and content management. This guide distills the workflow into three repeatable steps — Connect, Use, Update — and adds the advanced <strong>bidirectional closed-loop workflow</strong>: by configuring the IMA OpenAPI (Client ID + API Key), AI-generated content is automatically saved back into your knowledge base, turning it from a static archive into a self-growing second brain.</p>

<h3>Do I need programming skills to set up the IMA OpenAPI?</h3>
<p>No. You only need to open <code>https://ima.qq.com/agent-interface</code>, log in with your Tencent account, and apply for the <strong>Client ID</strong> and <strong>API Key</strong>. Then send the API Key to the IMA skill in WorkBuddy to complete the configuration. There is no code to write — the entire closed loop is handled by WorkBuddy.</p>

<h3>Can IMA Knowledge Base be used independently of WorkBuddy?</h3>
<p>Yes. IMA Knowledge Base is Tencent's standalone AI knowledge base product — you can create knowledge bases, upload documents, and query them directly. WorkBuddy is just one of its integration channels. This also means your knowledge base stays portable: the same content can be reused across different tools that support IMA or its OpenAPI.</p>

<h3>How often should I update and clean my knowledge base?</h3>
<p>Adopt a <strong>"weekly self-check + monthly review"</strong> rhythm: each business department cleans the content under its jurisdiction weekly, and key information gets automatic expiration reminders. Remember that "noise" hurts retrieval — an overstuffed knowledge base with expired documents returns fuzzier answers than a small, clean one.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Want to go deeper with your AI second brain? Keep exploring:</p>
  <ul>
    <li><a href="/article/build-personal-ai-knowledge-base-workbuddy-ima-guide">Build Your Personal AI Knowledge Base with WorkBuddy + IMA: A Step-by-Step Guide</a> — the companion guide covering installation, connection, and advanced prompts</li>
    <li><a href="/article/tencent-workbuddy-ai-office-workbench">Tencent WorkBuddy: AI Office Workbench</a> — a full overview of WorkBuddy's modes, skills, and expert teams</li>
    <li><a href="/article/karpathy-ai-knowledge-base-3-folders">Build a Karpathy-Style AI Knowledge Base: A 2-Minute Setup with Just 3 Folders</a> — a complementary philosophy for organizing what your AI remembers</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">📚 AI 教程</span>
  <span class="meta-badge">🕒 阅读约7分钟</span>
  <span class="meta-badge">📅 2026年8月25日</span>
  <span class="meta-badge">🎯 入门</span>
</div>

<h2 id="introduction">引言</h2>

<p>许多用户在使用WorkBuddy时都会遇到一个共同的痛点：它能出色地回答通用问题，但在涉及个性化或公司专属内容时却力不从心。本教程将带你将WorkBuddy与IMA知识库打通，打造一个AI“第二大脑”——让助手能够访问你的私有文档，输出准确、贴合上下文的答案，而不是泛泛而谈的猜测。</p>

<h2 id="three-core-steps">掌握IMA知识库的三大核心步骤</h2>

<p>整个流程被拆分为三个简单阶段：<strong>连接、使用、更新</strong>。读完本指南，你就能立刻上手全部三步。</p>

<h2 id="step-1-connect">第一步：连接IMA知识库（搭建你的知识图书馆）</h2>

<p>把这一步想象成给AI建一座专属图书馆。把笔记、文档和参考资料全部存放于此，AI就能直接从这些文件中检索信息，而不是生成泛泛的通用回复。</p>

<h3>完成连接的3个关键操作</h3>

<ol>
  <li><strong>授权连接</strong>
    <ul>
      <li>点击WorkBuddy输入框旁的“+”按钮。</li>
      <li>选择“连接器”，再选择“IMA知识库”。</li>
      <li>登录你的账号，授予WorkBuddy访问权限。</li>
    </ul>
  </li>
  <li><strong>创建并导入资源</strong>
    <ul>
      <li>打开IMA知识库管理页面。</li>
      <li>新建一个知识库（例如“WorkBuddy精通指南”）。</li>
      <li>上传基础文件（支持PDF、Word、PPT、Excel、TXT等常见格式）。</li>
    </ul>
  </li>
  <li><strong>开启连接器同步</strong>
    <ul>
      <li>回到WorkBuddy主界面。</li>
      <li>在已添加的连接器列表中找到IMA知识库。</li>
      <li>打开同步开关，开启实时知识共享。</li>
    </ul>
  </li>
</ol>

<h2 id="step-2-use">第二步：使用知识库（一个前缀拿到精准答案）</h2>

<p>使用打通后的系统极其简单：只需在提问前加上前缀<strong>“基于IMA知识库”</strong>，WorkBuddy就只会从你上传的资料中检索答案，大幅降低幻觉。</p>

<h3>两种常见使用场景</h3>

<ol>
  <li><strong>问答互动</strong>

<pre><code class="language-text">基于IMA知识库，请回答：[你的具体问题]</code></pre>

<p>这种格式确保AI基于你的文档给出直接、可核实的答案。</p>
  </li>
  <li><strong>创意生成</strong>

<pre><code class="language-text">基于IMA知识库，帮我写一份报告/文章/总结</code></pre>

<p>AI会使用知识库中的真实数据来生成贴合你业务场景的内容。</p>
  </li>
</ol>

<h2 id="step-3-update">第三步：更新知识库（持续手动上传，让知识常新）</h2>

<p>搭建知识库不是一次性任务——你需要定期补充新内容，才能让它持续发挥作用。</p>

<h3>更新知识库的3个步骤</h3>

<ol>
  <li><strong>打开知识库</strong>：登录IMA知识库管理界面，进入想添加内容的目标目录。</li>
  <li><strong>触发上传</strong>：点击工具栏的“上传”按钮，从电脑中选择本地文件（支持批量上传）。</li>
  <li><strong>自动解析与存储</strong>：确认所选文件后，系统会自动识别文件格式、提取关键信息并完成解析。新内容会实时同步进知识库。</li>
</ol>

<h2 id="advanced-closed-loop">高级玩法：双向闭环工作流</h2>

<p>想让知识库更强大，你可以搭建一套双向闭环系统，把AI生成的内容自动存回知识库。</p>

<h3>前置条件</h3>

<p>首先在“连接器”模块中配置IMA知识库API——这是双向数据流通的核心开关。</p>

<h3>实现步骤</h3>

<ol>
  <li><strong>获取OpenAPI凭证</strong>：打开 <code>https://ima.qq.com/agent-interface</code> 并登录，申请并获取两个值：

<pre><code class="language-text">Client ID
API Key</code></pre>
  </li>
  <li><strong>配置API</strong>：把获取到的API Key发送给IMA技能，完成配置。</li>
  <li><strong>自动闭环运行</strong>：当WorkBuddy生成内容（如会议纪要、报告或总结）后，你只需直接指示：

<pre><code class="language-text">把这段内容保存为IMA笔记并上传到知识库</code></pre>

<p>AI会自动完成上传，形成闭环：<strong>从知识库检索 → AI处理与生成 → 自动回存知识库</strong>。</p>
  </li>
</ol>

<h2 id="more-connectors">更多连接器选项</h2>

<p>除了IMA知识库，WorkBuddy还支持无缝接入多个平台：</p>

<ul>
  <li><strong>飞书</strong>：文档消息与多维表格实时同步。</li>
  <li><strong>腾讯文档</strong>：云文件的直接读写。</li>
  <li><strong>乐享知识库</strong>：企业内部知识联动。</li>
  <li><strong>腾讯会议</strong>：会议纪要自动整理与同步。</li>
</ul>

<h2 id="important-reminders">重要提醒</h2>

<p>要保持知识库的准确性，请遵循以下最佳实践：</p>

<ol>
  <li><strong>清理冗余的“数字垃圾”</strong>：定期删除过期、失效或低价值的文档。这些文件不仅占用存储空间，还会影响系统回复的准确度。</li>
  <li><strong>警惕信息干扰</strong>：知识库中的“噪音”会干扰算法的判断逻辑，可能导致检索结果模糊、答案错误甚至回复不专业。</li>
  <li><strong>保持知识库“纯净”</strong>：让知识库保持“干净纯粹”是提升回复质量的关键。纯净的知识能让系统锁定有效信息，输出符合你需求的专业答案。</li>
</ol>

<h2 id="conclusion">结语</h2>

<p>这套打通的用法遵循一个简单的节奏：建立<strong>“每周自查+每月复盘”</strong>机制，让每个业务部门负责清理自己管辖范围内的内容，并为关键信息设置自动过期提醒，从源头保证知识库的“新鲜度”和“纯净度”。</p>

<p>照着本指南操作，你就能把WorkBuddy变成真正个性化的AI助手，让它随着你的知识和业务一起成长。现在就动手搭建你的AI第二大脑吧！</p>

<h2>常见问题</h2>

<h3>本指南与之前的WorkBuddy + IMA教程有什么区别？</h3>
<p>之前的教程（<a href="/article/build-personal-ai-knowledge-base-workbuddy-ima-guide">用WorkBuddy + IMA搭建个人AI知识库</a>）重点在安装、连接和内容管理。本指南则把整个流程提炼为三个可复用的步骤——连接、使用、更新——并新增了高级的<strong>双向闭环工作流</strong>：通过配置IMA OpenAPI（Client ID + API Key），AI生成的内容会自动回存到知识库，把它从静态档案变成能自我成长的第二大脑。</p>

<h3>配置IMA OpenAPI需要编程技能吗？</h3>
<p>不需要。你只需打开 <code>https://ima.qq.com/agent-interface</code>，用腾讯账号登录，申请<strong>Client ID</strong>和<strong>API Key</strong>，再把API Key发给WorkBuddy中的IMA技能完成配置即可。全程无需写任何代码，闭环由WorkBuddy自动完成。</p>

<h3>IMA知识库可以不依赖WorkBuddy独立使用吗？</h3>
<p>可以。IMA知识库本身就是腾讯独立推出的AI知识库产品——你可以单独创建知识库、上传文档并直接检索。WorkBuddy只是它的接入渠道之一。这也意味着你的知识库是可迁移的：同样的内容可以在其他支持IMA或OpenAPI的工具中复用。</p>

<h3>知识库应该多久更新、清理一次？</h3>
<p>建议采用<strong>“每周自查+每月复盘”</strong>的节奏：各业务部门每周清理自己管辖的内容，关键信息设置自动过期提醒。请记住，“噪音”会损害检索效果——塞满过期文档的知识库，比一个精炼干净的小知识库返回的答案更模糊。</p>

<div class="next-step">
  <h3>📖 继续学习</h3>
  <p>想深入打造你的AI第二大脑？继续探索：</p>
  <ul>
    <li><a href="/article/build-personal-ai-knowledge-base-workbuddy-ima-guide">用WorkBuddy + IMA搭建个人AI知识库：完整步骤指南</a> — 涵盖安装、连接与高级提示词的姊妹篇</li>
    <li><a href="/article/tencent-workbuddy-ai-office-workbench">腾讯WorkBuddy：一站式AI办公工作台</a> — WorkBuddy的模式、技能与专家团队全景</li>
    <li><a href="/article/karpathy-ai-knowledge-base-3-folders">构建Karpathy风格的AI知识库：3个文件夹2分钟搭建</a> — 另一套组织AI记忆的互补方法论</li>
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

# ---------------------------------------------------------------------------
# Part 3: tools.ts — add IMA Knowledge Base
# ---------------------------------------------------------------------------
tool = r"""  {
    id: "ima-knowledge-base",
    name: "IMA Knowledge Base",
    nameZh: "腾讯IMA知识库",
    description: "Tencent's AI knowledge base (a 'second brain') that stores notes, documents, and materials for retrieval-augmented answers, connects natively to WorkBuddy, and exposes an OpenAPI for bidirectional closed-loop sync.",
    descriptionZh: "腾讯AI知识库（“第二大脑”），存储笔记、文档和资料用于检索增强回答，可原生接入WorkBuddy，并提供OpenAPI支持双向闭环同步。",
    category: "productivity",
    tags: ["productivity", "knowledge-base", "rag", "tencent", "second-brain", "china"],
    difficulty: "beginner",
    url: "https://ima.qq.com",
    rating: 4.4,
    pricing: "Free",
    useCase: "AI-powered knowledge management — store documents, run hallucination-free Q&A over them, and sync bidirectionally with WorkBuddy and other apps",
    icon: "🧠",
    company: "Tencent",
    companyZh: "腾讯",
    founded: 1998,
    headquarters: "Shenzhen, China",
    descriptionLong: "IMA Knowledge Base is Tencent's AI-powered knowledge management product, often called an AI 'second brain'. It lets you create personal or team knowledge bases, upload documents in common formats (PDF, Word, PPT, Excel, TXT), and run retrieval-augmented Q&A — the AI answers only from your own materials, dramatically reducing hallucinations on personalized or company-specific topics. Beyond standalone use, IMA shines through its integration ecosystem: it connects to WorkBuddy as a native connector (authorize once, then add the 'Based on IMA Knowledge Base' prefix to force document-grounded answers), and it exposes an OpenAPI at ima.qq.com/agent-interface where you can obtain a Client ID and API Key. With the API configured, you can build a bidirectional closed loop — retrieve from the knowledge base, have the AI process and generate (meeting minutes, reports, summaries), and automatically save the output back as new IMA notes. IMA also complements a broader Tencent ecosystem (Feishu, Tencent Docs, Lexiang, Tencent Meeting) via WorkBuddy's connector hub. For Chinese users who want a private, growing knowledge layer for their AI assistants without touching RAG infrastructure, IMA Knowledge Base is the most practical option available.",
    descriptionLongZh: "IMA知识库是腾讯推出的AI知识管理产品，常被称为AI“第二大脑”。你可以创建个人或团队知识库，上传PDF、Word、PPT、Excel、TXT等常见格式文档，并进行检索增强问答——AI只基于你自己的资料作答，大幅降低在个性化或公司专属话题上的幻觉。除了独立使用，IMA的优势更体现在其集成生态：它可作为原生连接器接入WorkBuddy（授权一次后，提问加“基于IMA知识库”前缀即可强制文档落地式回答），并在ima.qq.com/agent-interface开放OpenAPI，可申请Client ID和API Key。配置API后即可搭建双向闭环——从知识库检索、由AI处理生成（会议纪要、报告、总结）、再把输出自动存回为新的IMA笔记。IMA还能通过WorkBuddy的连接器中心与飞书、腾讯文档、乐享、腾讯会议等更广泛的腾讯生态联动。对于想要给AI助手构建私有、可成长知识层，又不想碰RAG基础设施的中国用户，IMA知识库是目前最实用的选择。",
    advantages: ["Native WorkBuddy connector with one-click authorization", "Retrieval-augmented answers drastically reduce hallucinations on private topics", "OpenAPI enables a bidirectional closed loop (retrieve → generate → save back)", "Supports common document formats (PDF, Word, PPT, Excel, TXT)", "Free to use with generous Tencent-backed quota"],
    advantagesZh: ["原生WorkBuddy连接器，一键授权", "检索增强回答大幅降低私有话题幻觉", "OpenAPI支持双向闭环（检索→生成→回存）", "支持PDF/Word/PPT/Excel/TXT等常见格式", "免费使用，腾讯背书额度充足"],
    useCases: ["Personal knowledge base / AI second brain", "Company-specific document Q&A", "Automatic saving of AI-generated meeting minutes and reports", "Cross-tool knowledge reuse via OpenAPI"],
    useCasesZh: ["个人知识库/AI第二大脑", "公司专属文档问答", "AI生成的会议纪要、报告自动回存", "通过OpenAPI跨工具复用知识"],
    targetAudience: "Chinese professionals, content creators, and teams who want a private, always-growing knowledge layer their AI assistants can query without hallucinations.",
    targetAudienceZh: "想要为AI助手构建私有、可持续成长知识层，且需要低幻觉回答的中国职场人士、内容创作者和团队。",
    pricingTiers: [
      {
        tier: "Free",
        tierZh: "免费版",
        price: "Free",
        features: ["Create unlimited personal knowledge bases", "Document upload and RAG Q&A", "WorkBuddy connector", "OpenAPI access"],
        featuresZh: ["创建无限个人知识库", "文档上传与RAG问答", "WorkBuddy连接器", "OpenAPI接口"],
      },
    ],
    pros: ["Native integration with WorkBuddy — zero setup friction for Tencent users", "OpenAPI makes a no-code bidirectional knowledge loop possible", "Clean Chinese UI and solid document parsing quality", "Free tier is adequate for personal use"],
    prosZh: ["与WorkBuddy原生集成——腾讯用户零门槛", "OpenAPI让无代码双向知识闭环成为可能", "中文界面和文档解析质量好", "免费版满足个人使用"],
    cons: ["Primarily a Chinese-market product", "Requires a Tencent account", "Third-party integration depends on OpenAPI maturity", "Consider data export and lock-in for long-term knowledge"],
    consZh: ["主要面向中国市场", "需腾讯账号登录", "第三方集成依赖OpenAPI成熟度", "长期知识沉淀需考虑导出与锁定问题"],
    extensions: [],
    skills: ["Knowledge management", "RAG Q&A", "Document parsing", "Second brain", "Tencent ecosystem integration"],
    scene: "office-productivity",
  },
"""
with open("src/lib/tools.ts", encoding="utf-8") as f:
    s = f.read()
last = s.rfind("] as Tool[];")
assert last != -1, "tools.ts: ] as Tool[]; marker not found"
s2 = s[:last] + tool + s[last:]
with open("src/lib/tools.ts", "w", encoding="utf-8", newline="\n") as f:
    f.write(s2)
print("tools.ts updated")
print("Done. Article:", SLUG)
