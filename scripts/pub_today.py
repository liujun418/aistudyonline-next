"""
Publish July 15, 2026 — 2 articles, no new tools.
"""
import os

BASE = r"C:\Users\jun\aistudyonline-next"
os.chdir(BASE)

# ===== Part 1: Add 2 article metadata to articles.ts =====
with open('src/lib/articles.ts', 'r', encoding='utf-8') as f:
    articles_src = f.read()

new_articles = r"""  {
    slug: "build-personal-ai-knowledge-base-workbuddy-ima-guide",
    title: "Build Your Personal AI Knowledge Base with WorkBuddy + IMA: A Step-by-Step Guide",
    titleZh: "WorkBuddy + IMA：搭建个人AI知识库的完整指南",
    description: "A step-by-step guide to building a personal AI knowledge base using WorkBuddy (AI agent) + IMA Knowledge Base (storage) — tailored for Chinese users as an alternative to Codex+Obsidian, covering installation, connection, content management, and advanced prompts.",
    descriptionZh: "用WorkBuddy（AI Agent）+ IMA知识库（存储）搭建个人AI知识库的完整步骤指南——面向国内用户的Codex+Obsidian替代方案，覆盖安装、连接、内容管理和高级提示词。",
    category: "AI Tutorials",
    tags: ["WorkBuddy", "IMA", "Knowledge Base", "Productivity", "Tencent", "Tutorial", "China"],
    difficulty: "beginner",
    toolsMentioned: ["Tencent WorkBuddy"],
    date: "2026-07-15",
  },
  {
    slug: "workbuddy-10-core-skills-beginner-to-advanced",
    title: "WorkBuddy: 10 Core Skills to Master from Beginner to Advanced",
    titleZh: "WorkBuddy十大核心技能：从入门到精通",
    description: "Ten essential WorkBuddy skills organized into five stages — Communication Foundation, Methodology for Speed, Safety & Risk Management, Amplification Techniques, and Automation & Smart Workflow — with concrete prompt examples and a mastery roadmap.",
    descriptionZh: "WorkBuddy十大必备技能，分五个阶段——沟通基础、提速方法、安全风险管理、放大技巧和自动化智能工作流——含具体提示词示例和掌握路线图。",
    category: "AI Tutorials",
    tags: ["WorkBuddy", "Skills", "Productivity", "Prompt Engineering", "Automation", "Tutorial"],
    difficulty: "beginner",
    toolsMentioned: ["Tencent WorkBuddy"],
    date: "2026-07-15",
  },

"""

last_bracket = articles_src.rfind('];')
articles_new = articles_src[:last_bracket] + new_articles + '];'

with open('src/lib/articles.ts', 'w', encoding='utf-8') as f:
    f.write(articles_new)

print('Part 1: 2 new articles added to articles.ts')

# ===== Part 2: Add article content to article-content.ts =====
with open('src/lib/article-content.ts', 'r', encoding='utf-8') as f:
    content_src = f.read()

new_contents = r'''
  "build-personal-ai-knowledge-base-workbuddy-ima-guide": {
    content: `<div class="meta-banner">
  <span class="meta-badge">📚 AI Tutorials</span>
  <span class="meta-badge">🕒 8 min read</span>
  <span class="meta-badge">📅 Jul 15, 2026</span>
  <span class="meta-badge">🎯 Beginner</span>
</div>

<h2 id="introduction">Introduction</h2>

<p>In 2026, building a personal AI knowledge base is one of the most valuable investments you can make for your productivity. It becomes a long-term digital asset that grows with you, helping you find answers to work problems, create content ideas, or plan travel itineraries faster than ever before.</p>

<p>Many people recommend using Codex + Obsidian, but this combination has two major issues for users in China:</p>

<ol>
  <li><strong>Network Barrier</strong>: Codex is not accessible in China due to network restrictions.</li>
  <li><strong>Learning Barrier</strong>: Obsidian has too many features, making it difficult for beginners to get started quickly.</li>
</ol>

<p>Today, I will introduce a solution tailored for domestic users: <strong>WorkBuddy + IMA Knowledge Base</strong>. This system is designed to be user-friendly, accessible, and powerful.</p>

<h2 id="how-it-works">How the System Works</h2>

<ul>
  <li><strong>WorkBuddy</strong>: An AI agent that automatically reads, analyzes, organizes, and summarizes information.</li>
  <li><strong>IMA Knowledge Base</strong>: A storage system that stores valuable articles, documents, and content.</li>
  <li><strong>You</strong>: The decision-maker who guides the AI and takes action based on its analysis.</li>
</ul>

<p>With this workflow, you can quickly find answers to any question, from creating viral content ideas to planning travel guides or solving work problems.</p>

<h2 id="step-1">Step 1: Download and Install the Tools</h2>

<h3>Download WorkBuddy</h3>
<ol>
  <li>Open your browser and go to the official WorkBuddy website.</li>
  <li>Click the "Download Now" button.</li>
  <li>Select the installation package that matches your operating system (Mac ARM64, Mac x64, Windows x64, iOS, or Android).</li>
  <li>Run the installer and follow the prompts to complete the installation.</li>
</ol>

<h3>Download IMA Knowledge Base</h3>
<ol>
  <li>Open your browser and go to the official IMA website.</li>
  <li>Click the "Download for Desktop" button.</li>
  <li>Run the installer and follow the prompts to complete the installation.</li>
</ol>

<h2 id="step-2">Step 2: Connect WorkBuddy to IMA Knowledge Base</h2>

<p>Since both are products of Tencent, the official connection is already set up. Here's how to link them:</p>

<ol>
  <li>Open WorkBuddy and log in to your account.</li>
  <li>On the main page, find the "More" option in the left sidebar.</li>
  <li>Click "IMA Knowledge Base" and then click "Authorize".</li>
  <li>Scan the QR code with WeChat to complete the authorization process.</li>
  <li>After authorization, you will be redirected to the IMA Knowledge Base interface.</li>
</ol>

<h3>Verify the Connection</h3>

<ol>
  <li>In WorkBuddy, create a new task and ask:</li>
</ol>

<pre><code class="language-text">Please check if IMA Knowledge Base is connected successfully and list all my knowledge bases.</code></pre>

<ol start="2">
  <li>If the connection fails, go to the "Connectors" section in WorkBuddy.</li>
  <li>Find the IMA connector and click "Connect".</li>
  <li>Once the connector shows a green dot, repeat the verification step.</li>
</ol>

<h2 id="step-3">Step 3: Use the Knowledge Base</h2>

<h3>Reference Knowledge Bases in WorkBuddy</h3>
<ol>
  <li>In the WorkBuddy chat box, click the "More" button in the bottom-left corner.</li>
  <li>Select "Add File" and then choose "IMA Knowledge Base".</li>
  <li>Select the knowledge base you want to reference and click "Confirm".</li>
  <li>Now you can ask WorkBuddy questions based on the content in the knowledge base, such as:</li>
</ol>

<pre><code class="language-text">Please summarize the key points of the articles in this knowledge base.</code></pre>

<h3>Add Content to the Knowledge Base</h3>
<ol>
  <li>In WorkBuddy, generate a document or report (e.g., "Create a report on AI agents").</li>
  <li>Once the document is generated, click the "Upload to Cloud" button.</li>
  <li>Select "IMA Knowledge Base" and choose the target knowledge base (e.g., "Learning Materials").</li>
  <li>Click "Confirm" to upload the document.</li>
</ol>

<h2 id="step-4">Step 4: Create and Manage Knowledge Bases</h2>

<h3>Recommended Knowledge Bases</h3>
<p>For beginners, it's best to start with a few basic knowledge bases:</p>
<ul>
  <li><strong>Learning Materials</strong>: Store study notes, courses, and tutorials.</li>
  <li><strong>Current Projects</strong>: Store documents related to ongoing work projects.</li>
  <li><strong>Outputs</strong>: Store finished reports, articles, and other deliverables.</li>
  <li><strong>Comfort Life</strong>: Store travel guides, food recommendations, and lifestyle tips.</li>
</ul>

<h3>Create a New Knowledge Base</h3>
<ol>
  <li>Open the IMA Knowledge Base interface.</li>
  <li>Click the "Create Personal Knowledge Base" button.</li>
  <li>Enter a name for the knowledge base.</li>
  <li>Select an icon for the knowledge base.</li>
  <li>Click "Confirm" to create the knowledge base.</li>
</ol>

<p><strong>Note</strong>: You cannot create a knowledge base directly in WorkBuddy. You must do it in the IMA Knowledge Base interface.</p>

<h2 id="step-5">Step 5: Add Files to the Knowledge Base</h2>

<ol>
  <li>Open the IMA Knowledge Base interface.</li>
  <li>Navigate to the target knowledge base.</li>
  <li>Click the "+" button in the top-right corner.</li>
  <li>Select the type of file to upload: local files, WeChat files, personal knowledge bases, web links, notes, Tencent documents, or voice recordings.</li>
</ol>

<h3>Example: Upload a WeChat Public Account Article</h3>
<ol>
  <li>Open the WeChat public account article in your browser.</li>
  <li>Copy the article link.</li>
  <li>In the IMA Knowledge Base, click "+" and select "Web Link".</li>
  <li>Paste the copied link and click "Import".</li>
  <li>Wait for the system to parse the article.</li>
</ol>

<h2 id="step-6">Step 6: Advanced Tips</h2>

<h3>Regular Maintenance</h3>
<ul>
  <li><strong>Organize Regularly</strong>: Set a schedule to organize your knowledge base weekly or monthly. This prevents it from becoming a "dead collection" of unused content.</li>
  <li><strong>Protect Privacy</strong>: Do not store personal sensitive information, passwords, or confidential documents in the knowledge base, as it is connected to WorkBuddy.</li>
</ul>

<h3>Useful Prompts</h3>

<h4>Prompt 1: Organize Learning Materials</h4>
<pre><code class="language-text">Please organize the articles in the "Learning Materials" knowledge base.
1. Extract the main points, key concepts, and practical steps from each article.
2. Summarize each article in 3-5 bullet points.
3. Highlight any actionable advice or takeaways.
4. If there are conflicting information, note it down.</code></pre>

<h4>Prompt 2: Generate Content Ideas</h4>
<pre><code class="language-text">Based on the content in the "Outputs" knowledge base, generate 5 new content ideas for my blog.
Each idea should include a title, target audience, and key points.</code></pre>

<h2 id="conclusion">Conclusion</h2>

<p>Building a personal AI knowledge base with WorkBuddy and IMA is a powerful way to boost your productivity and organize your digital life. By following these steps, you can create a system that grows with you and helps you find answers faster than ever before.</p>

<p>Remember: (1) Start with a few basic knowledge bases and expand as you get more comfortable. (2) Regularly organize your knowledge base to keep it useful. (3) Protect your privacy by not storing sensitive information. With this system, you'll have a second brain that works for you 24/7, helping you achieve more in less time.</p>

<h2>常见问题</h2>

<h3>Why WorkBuddy + IMA instead of Codex + Obsidian?</h3>
<p>Two reasons specific to Chinese users: (1) <strong>Accessibility</strong> — Codex requires network configurations that are unreliable in China, while WorkBuddy is a domestic product with no access barriers. (2) <strong>Simplicity</strong> — Obsidian is powerful but has a steep learning curve with its plugin system, markdown syntax, and graph views. IMA is designed for simplicity: install, authorize with WeChat, and start adding content. For users who want a knowledge base that works today without weeks of configuration, WorkBuddy + IMA is the pragmatic choice. If you're outside China or already comfortable with Obsidian, Codex + Obsidian remains a strong option.</p>

<h3>Is IMA Knowledge Base free?</h3>
<p>Yes, IMA is a free Tencent product with generous storage for personal use. WorkBuddy's free tier is sufficient for knowledge base management tasks. The only potential cost is if you exceed WorkBuddy's free usage quotas with very large knowledge bases or frequent AI-powered analysis. For most individual users managing a few knowledge bases with hundreds of articles, the free tier is more than adequate.</p>

<h3>Can I share my knowledge base with my team?</h3>
<p>IMA supports shared knowledge bases, but the article focuses on personal use. For team sharing, you'd create a shared knowledge base in IMA and grant access to team members. WorkBuddy's Project function (covered in other WorkBuddy guides) enables team collaboration with shared materials and standards. The combination — IMA for knowledge storage + WorkBuddy Projects for AI-powered collaboration — creates a lightweight team knowledge management system without the overhead of enterprise wiki tools.</p>

<h3>What types of content can I store in IMA?</h3>
<p>IMA supports: local files and folders, WeChat files (direct import from WeChat), web links (auto-parsed articles), personal notes, Tencent documents, and voice recordings. The web link parser is particularly useful — paste a WeChat public account article URL, and IMA extracts the full text with formatting. This makes it easy to build a knowledge base from the content you already consume daily. The only limitation: very large files (100MB+) may take longer to process, and some paywalled content may not parse correctly.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Built your knowledge base? Master WorkBuddy's full capabilities:</p>
  <ul>
    <li><a href="/articles/workbuddy-10-core-skills-beginner-to-advanced">WorkBuddy: 10 Core Skills to Master from Beginner to Advanced</a> — the essential WorkBuddy skill set</li>
    <li><a href="/articles/workbuddy-3-layer-memory-system-make-ai-understand-you">WorkBuddy L05: Master the 3-Layer Memory System</a> — combine memory with your knowledge base</li>
    <li><a href="/articles/practical-guide-tencent-workbuddy-ai-office-assistant">A Practical Guide to Tencent WorkBuddy</a> — hands-on WorkBuddy use cases</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">📚 AI 教程</span>
  <span class="meta-badge">🕒 阅读约8分钟</span>
  <span class="meta-badge">📅 2026年7月15日</span>
  <span class="meta-badge">🎯 入门</span>
</div>

<h2 id="introduction">引言</h2>

<p>2026年，建立个人AI知识库是对生产力最有价值的投资之一。它成为随你成长的长效数字资产，帮你比以往更快地找到工作问题的答案、创造内容创意或规划旅行路线。</p>

<p>很多人推荐Codex + Obsidian组合，但这对国内用户有两个主要问题：</p>

<ol>
  <li><strong>网络障碍</strong>：Codex因网络限制在国内无法访问。</li>
  <li><strong>学习门槛</strong>：Obsidian功能太多，新手难以快速上手。</li>
</ol>

<p>今天，我介绍一套面向国内用户的方案：<strong>WorkBuddy + IMA知识库</strong>。这个系统设计为用户友好、可访问且功能强大。</p>

<h2 id="how-it-works">系统工作原理</h2>

<ul>
  <li><strong>WorkBuddy</strong>：AI Agent，自动读取、分析、整理和总结信息。</li>
  <li><strong>IMA知识库</strong>：存储系统，保存有价值的文章、文档和内容。</li>
  <li><strong>你</strong>：决策者，引导AI并根据其分析采取行动。</li>
</ul>

<p>通过这个工作流，你可以快速找到任何问题的答案——从创造爆款内容创意到规划旅行攻略或解决工作问题。</p>

<h2 id="step-1">第一步：下载安装工具</h2>

<h3>下载WorkBuddy</h3>
<ol>
  <li>打开浏览器访问WorkBuddy官网。</li>
  <li>点击"立即下载"按钮。</li>
  <li>选择匹配你操作系统的安装包（Mac ARM64、Mac x64、Windows x64、iOS或Android）。</li>
  <li>运行安装程序，按提示完成安装。</li>
</ol>

<h3>下载IMA知识库</h3>
<ol>
  <li>打开浏览器访问IMA官网。</li>
  <li>点击"下载桌面版"按钮。</li>
  <li>运行安装程序，按提示完成安装。</li>
</ol>

<h2 id="step-2">第二步：连接WorkBuddy到IMA知识库</h2>

<p>两者都是腾讯产品，官方连接已预设。连接步骤：</p>

<ol>
  <li>打开WorkBuddy并登录账号。</li>
  <li>在主页左侧边栏找到"更多"选项。</li>
  <li>点击"IMA知识库"，然后点击"授权"。</li>
  <li>用微信扫描二维码完成授权。</li>
  <li>授权后，你将跳转到IMA知识库界面。</li>
</ol>

<h3>验证连接</h3>

<ol>
  <li>在WorkBuddy中创建新任务并询问：</li>
</ol>

<pre><code class="language-text">请检查IMA知识库是否连接成功，并列出我所有的知识库。</code></pre>

<ol start="2">
  <li>如果连接失败，前往WorkBuddy的"连接器"部分。</li>
  <li>找到IMA连接器并点击"连接"。</li>
  <li>连接器显示绿点后，重复验证步骤。</li>
</ol>

<h2 id="step-3">第三步：使用知识库</h2>

<h3>在WorkBuddy中引用知识库</h3>
<ol>
  <li>在WorkBuddy聊天框左下角点击"更多"按钮。</li>
  <li>选择"添加文件"，然后选择"IMA知识库"。</li>
  <li>选择要引用的知识库并点击"确认"。</li>
  <li>现在可以基于知识库内容向WorkBuddy提问：</li>
</ol>

<pre><code class="language-text">请总结这个知识库中文章的核心要点。</code></pre>

<h3>向知识库添加内容</h3>
<ol>
  <li>在WorkBuddy中生成文档或报告（如"创建一份AI Agent报告"）。</li>
  <li>文档生成后，点击"上传到云端"按钮。</li>
  <li>选择"IMA知识库"并选择目标知识库（如"学习资料"）。</li>
  <li>点击"确认"上传文档。</li>
</ol>

<h2 id="step-4">第四步：创建和管理知识库</h2>

<h3>推荐的知识库</h3>
<p>新手最好从几个基础知识库开始：</p>
<ul>
  <li><strong>学习资料</strong>：存储学习笔记、课程和教程。</li>
  <li><strong>当前项目</strong>：存储与进行中工作项目相关的文档。</li>
  <li><strong>输出成果</strong>：存储完成的报告、文章和其他交付物。</li>
  <li><strong>舒适生活</strong>：存储旅行攻略、美食推荐和生活方式技巧。</li>
</ul>

<h3>创建新知识库</h3>
<ol>
  <li>打开IMA知识库界面。</li>
  <li>点击"创建个人知识库"按钮。</li>
  <li>输入知识库名称。</li>
  <li>选择知识库图标。</li>
  <li>点击"确认"创建知识库。</li>
</ol>

<p><strong>注意</strong>：不能在WorkBuddy中直接创建知识库，必须在IMA知识库界面操作。</p>

<h2 id="step-5">第五步：向知识库添加文件</h2>

<ol>
  <li>打开IMA知识库界面。</li>
  <li>导航到目标知识库。</li>
  <li>点击右上角"+"按钮。</li>
  <li>选择上传文件类型：本地文件、微信文件、个人知识库、网页链接、笔记、腾讯文档或语音录音。</li>
</ol>

<h3>示例：上传微信公众号文章</h3>
<ol>
  <li>在浏览器中打开微信公众号文章。</li>
  <li>复制文章链接。</li>
  <li>在IMA知识库中点击"+"并选择"网页链接"。</li>
  <li>粘贴链接并点击"导入"。</li>
  <li>等待系统解析文章。</li>
</ol>

<h2 id="step-6">第六步：进阶技巧</h2>

<h3>定期维护</h3>
<ul>
  <li><strong>定期整理</strong>：设定每周或每月整理知识库的时间表，防止变成"死收藏"。</li>
  <li><strong>保护隐私</strong>：不要在知识库中存储个人敏感信息、密码或机密文档，因为它与WorkBuddy相连。</li>
</ul>

<h3>实用提示词</h3>

<h4>提示词1：整理学习资料</h4>
<pre><code class="language-text">请整理"学习资料"知识库中的文章。
1. 提取每篇文章的主要观点、核心概念和实操步骤。
2. 用3-5个要点总结每篇文章。
3. 高亮任何可操作的建议或收获。
4. 如有矛盾信息，请标注。</code></pre>

<h4>提示词2：生成内容创意</h4>
<pre><code class="language-text">基于"输出成果"知识库中的内容，为我的博客生成5个新内容创意。
每个创意包含标题、目标受众和核心要点。</code></pre>

<h2 id="conclusion">总结</h2>

<p>用WorkBuddy和IMA构建个人AI知识库是提升生产力、整理数字生活的强大方式。按这些步骤，你可以创建一个随你成长的系统，比以往更快找到答案。</p>

<p>记住：(1) 从几个基础知识库开始，熟练后扩展。(2) 定期整理知识库保持其有用性。(3) 不存储敏感信息保护隐私。有了这个系统，你将拥有一个24/7为你工作的第二大脑，帮你在更短时间内实现更多。</p>

<h2>常见问题</h2>

<h3>为什么选WorkBuddy + IMA而不是Codex + Obsidian？</h3>
<p>针对中国用户的两个原因：(1) <strong>可访问性</strong>——Codex在国内需要不可靠的网络配置，WorkBuddy是国产产品无访问障碍。(2) <strong>简洁性</strong>——Obsidian功能强大但学习曲线陡峭，插件系统、Markdown语法和关系图谱对新手不友好。IMA为简洁设计：安装、微信授权、开始添加内容。对于想要今天就能用、不需要数周配置的知识库用户，WorkBuddy + IMA是务实选择。如果你在海外或已熟悉Obsidian，Codex + Obsidian仍是强选项。</p>

<h3>IMA知识库免费吗？</h3>
<p>是的，IMA是腾讯免费产品，个人使用存储空间充足。WorkBuddy免费层足够知识库管理任务。唯一潜在成本是如果知识库非常大或频繁进行AI分析超出WorkBuddy免费配额。对大多数管理几个知识库、数百篇文章的个人用户，免费层绰绰有余。</p>

<h3>能和团队共享知识库吗？</h3>
<p>IMA支持共享知识库，但本文聚焦个人使用。团队共享需在IMA中创建共享知识库并授权团队成员访问。WorkBuddy的项目功能（其他WorkBuddy指南有介绍）支持团队协作共享素材和标准。组合——IMA做知识存储 + WorkBuddy项目做AI驱动协作——创建了轻量团队知识管理系统，无需企业Wiki工具的开销。</p>

<h3>IMA能存储什么类型的内容？</h3>
<p>IMA支持：本地文件和文件夹、微信文件（从微信直接导入）、网页链接（自动解析文章）、个人笔记、腾讯文档和语音录音。网页链接解析器特别实用——粘贴微信公众号文章URL，IMA提取带格式的全文。这让从日常消费的内容中构建知识库变得极其容易。唯一限制：超大文件（100MB+）处理时间较长，部分付费内容可能无法正确解析。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>建好了知识库？掌握WorkBuddy的完整能力：</p>
  <ul>
    <li><a href="/articles/workbuddy-10-core-skills-beginner-to-advanced">WorkBuddy十大核心技能：从入门到精通</a> — WorkBuddy必备技能集</li>
    <li><a href="/articles/workbuddy-3-layer-memory-system-make-ai-understand-you">WorkBuddy L05：掌握三层记忆系统，让AI越来越懂你</a> — 将记忆与知识库结合</li>
    <li><a href="/articles/practical-guide-tencent-workbuddy-ai-office-assistant">腾讯WorkBuddy实操指南：一站式AI办公助手完全上手</a> — WorkBuddy实战场景</li>
  </ul>
</div>`,
  },

  "workbuddy-10-core-skills-beginner-to-advanced": {
    content: `<div class="meta-banner">
  <span class="meta-badge">📚 AI Tutorials</span>
  <span class="meta-badge">🕒 8 min read</span>
  <span class="meta-badge">📅 Jul 15, 2026</span>
  <span class="meta-badge">🎯 Beginner</span>
</div>

<h2 id="introduction">Introduction</h2>

<p>Many people use AI assistants as nothing more than search engines, but some have already turned them into virtual teammates that handle work for them. The difference isn't how powerful the AI is — it's how you use it. In this guide, I'll break down the official best practices for WorkBuddy into 10 actionable skills, covering everything from how to communicate clearly to how to let the AI take over repetitive tasks. By the end, you'll realize you've been wasting at least half of your AI's potential.</p>

<h2 id="categories">The 10 Skills, Organized into 5 Categories</h2>

<p>These skills are grouped into five stages: <strong>Communication Foundation</strong>, <strong>Methodology for Speed</strong>, <strong>Safety & Risk Management</strong>, <strong>Amplification Techniques</strong>, and <strong>Automation & Smart Workflow</strong>.</p>

<h2 id="skill-1">Skill 1: Clear Communication – 3 Elements to Get It Right the First Time</h2>

<p>The most important skill of all: <strong>be specific</strong>. When you ask WorkBuddy for help, don't rely on vague descriptions. Instead, define three things:</p>

<ol>
  <li><strong>What to do</strong>: The exact task or goal.</li>
  <li><strong>Conditions</strong>: Any constraints, rules, or context.</li>
  <li><strong>Expected outcome</strong>: What success looks like.</li>
</ol>

<p>Think of it like assigning work to an intern: unclear instructions will always lead to mistakes.</p>

<p><strong>Example of a good prompt</strong>:</p>
<pre><code class="language-text">Write a 500-word blog post about AI productivity tools, targeting small business owners. The tone should be friendly and practical, with 3 actionable tips. Include a call-to-action at the end.</code></pre>

<h2 id="skill-2">Skill 2: Small Steps, Fast Progress – Break Big Tasks Like Peeling an Onion</h2>

<p>Don't expect WorkBuddy to handle a huge, complex task in one go. Instead, break it down into layers:</p>

<ol>
  <li><strong>Analyze the requirement</strong>: Clarify the core goal.</li>
  <li><strong>Build the framework</strong>: Outline the structure.</li>
  <li><strong>Fill in details</strong>: Add content piece by piece.</li>
  <li><strong>Correct as you go</strong>: Adjust and refine at each step.</li>
</ol>

<p><strong>Example workflow for a project plan</strong>:</p>
<ol>
  <li>Ask WorkBuddy to outline the main phases of a marketing campaign.</li>
  <li>Then ask it to detail each phase with timelines.</li>
  <li>Finally, ask it to add budget estimates for each task.</li>
</ol>

<h2 id="skill-3">Skill 3: Embrace Multi-Round Conversations – Don't Expect Perfection on the First Try</h2>

<p>WorkBuddy won't always understand your intent perfectly on the first attempt. Treat its first response as a draft:</p>
<ul>
  <li>Point out specific issues.</li>
  <li>Rephrase your request from a different angle.</li>
  <li>Ask it to switch roles (e.g., "Act as a marketing expert and rewrite this").</li>
</ul>

<p>Great results come from continuous refinement.</p>

<h2 id="skill-4">Skill 4: Safety First – Start Local, Then Go Remote</h2>

<p>For beginners, always start with local tasks before moving to remote or cloud-based work:</p>
<ol>
  <li>Practice on your own computer: Let WorkBuddy organize files, edit documents, or analyze data locally.</li>
  <li>Learn its capabilities: Understand what it can and can't do.</li>
  <li>Move to remote tasks only when you're confident.</li>
</ol>

<h2 id="skill-5">Skill 5: Give WorkBuddy a Role – Built-in Expert Modes</h2>

<p>WorkBuddy has built-in expert roles like Product Manager and Data Analyst. By assigning a role, you instantly get more professional, context-aware responses.</p>

<p><strong>Example prompt with a role</strong>:</p>
<pre><code class="language-text">Act as a Data Analyst. Analyze this sales data and identify 3 key trends. Present the results in a simple table.</code></pre>

<h2 id="skill-6">Skill 6: Provide Examples – A Sample Speaks Louder Than Words</h2>

<p>When you want WorkBuddy to match a specific style or tone, don't just describe it — show it. Give it a sample and say, "Follow this style."</p>

<p><strong>Example</strong>:</p>
<pre><code class="language-text">Write a social media post for our new product launch. Use the same tone and structure as this sample: [paste a sample post here].</code></pre>

<h2 id="skill-7">Skill 7: Manage Conversations – Don't Cram All Tasks into One Chat</h2>

<p>Treat each conversation as a separate workspace:</p>
<ul>
  <li>Use one chat for writing reports.</li>
  <li>Use another for data analysis.</li>
  <li>Use a third for brainstorming ideas.</li>
</ul>

<p>This keeps the context clear, prevents WorkBuddy from getting confused, and lets you work on multiple tasks in parallel.</p>

<h2 id="skill-8">Skill 8: Frequent Backups – Trust the AI, But Protect Your Work</h2>

<p>Even the best AI can make mistakes. Before letting WorkBuddy edit important files:</p>
<ol>
  <li><strong>Make a copy</strong>: Always back up the original file.</li>
  <li><strong>Test changes</strong>: Let WorkBuddy edit the copy first.</li>
  <li><strong>Review before finalizing</strong>: Check the results carefully.</li>
</ol>

<h2 id="skill-9">Skill 9: Automation – Let WorkBuddy Work in the Background</h2>

<p>Once you've mastered the basics, use automation to free up your time:</p>
<ol>
  <li>Set scheduled tasks: Have WorkBuddy send daily reports or weekly summaries automatically.</li>
  <li>Build workflows: Chain tasks together so one action triggers the next.</li>
  <li>Let it run in the background: WorkBuddy can handle repetitive tasks 24/7.</li>
</ol>

<p><strong>Example automation workflow</strong>:</p>
<pre><code class="language-text">Every Monday at 9 AM, analyze the previous week's sales data, create a summary report, and send it to the team email list.</code></pre>

<h2 id="skill-10">Skill 10: Smart Laziness + Motivation – Reach the Ultimate Level</h2>

<p>The final skill is about working smarter, not harder:</p>
<ul>
  <li><strong>Laziness</strong>: Offload repetitive, mechanical tasks to WorkBuddy so you can focus on creative, high-value work.</li>
  <li><strong>Motivation</strong>: Set high expectations for WorkBuddy. Tell it, "You are a senior consultant — give me the best possible advice."</li>
</ul>

<p>This pushes WorkBuddy to deliver deeper, more insightful results.</p>

<h2 id="mastery-roadmap">Step-by-Step Guide to Mastery</h2>

<p>Follow this order to get the most out of WorkBuddy:</p>

<ol>
  <li><strong>Start with clear communication</strong>: Use the 3-element prompt framework.</li>
  <li><strong>Learn to break tasks down</strong>: Use small steps and multi-round conversations.</li>
  <li><strong>Leverage roles, examples, and multiple chats</strong>: Boost output quality and efficiency.</li>
  <li><strong>Automate with confidence</strong>: Once you're comfortable, use automation to scale your work.</li>
</ol>

<p>By following these steps, you'll turn WorkBuddy into a true productivity partner that handles the heavy lifting for you.</p>

<h2>常见问题</h2>

<h3>Which of these 10 skills gives the fastest ROI for a beginner?</h3>
<p>Skills 1, 2, and 5 in combination. <strong>Clear Communication</strong> (Skill 1) immediately improves every prompt you write — even a 30-second investment in structuring your request can turn a useless response into a usable one. <strong>Small Steps</strong> (Skill 2) prevents the most common beginner mistake: asking for too much at once and getting overwhelmed by a messy output. <strong>Role Assignment</strong> (Skill 5) is a one-line addition to any prompt that dramatically improves quality. Master these three and you'll already be in the top 20% of WorkBuddy users. The other skills build on this foundation.</p>

<h3>How is Skill 9 (Automation) different from just scheduling tasks?</h3>
<p>Scheduling is time-based ("do X at 9 AM"). Automation is <strong>workflow-based</strong> ("when X happens, do Y, then Z"). Skill 9 covers both but emphasizes the workflow approach. A scheduled task runs the same prompt every time. An automated workflow can branch: "analyze sales data → if revenue dropped >10%, generate an alert report and send to the manager → if revenue is stable, just update the dashboard." This conditional logic is what separates power users from casual users. WorkBuddy's automation system supports both recurring schedules and trigger-based workflows.</p>

<h3>Should I really use separate chats for different tasks?</h3>
<p>Yes, and here's why: AI models have a context window. When you mix report writing, data analysis, and brainstorming in one chat, the context gets polluted — the AI might reference data from your brainstorming session while writing a report, or apply report-writing formality to a creative brainstorm. Separate chats keep each task's context clean. It also lets you work on multiple tasks in parallel: while WorkBuddy is generating a long report in one chat, you can brainstorm ideas in another. This is a simple habit that costs nothing and prevents the most common AI quality degradation issue.</p>

<h3>What's the biggest mistake beginners make with WorkBuddy?</h3>
<p><strong>Treating it like Google</strong> — typing 3-5 word queries and expecting perfect results. Google is a search engine that finds existing information. WorkBuddy is an AI agent that creates new output based on your instructions. The quality gap between "analyze sales data" and "Analyze this Q3 sales spreadsheet. Identify the top 3 performing products by revenue, flag any products with declining month-over-month trends, and present findings in a table with percentage changes" is enormous. The first prompt gets a generic response. The second gets a professional analysis. The difference is 30 seconds of extra typing. This guide's Skill 1 exists specifically to fix this problem.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Mastered the 10 skills? Put them into practice:</p>
  <ul>
    <li><a href="/articles/build-personal-ai-knowledge-base-workbuddy-ima-guide">Build Your Personal AI Knowledge Base with WorkBuddy + IMA</a> — apply Skills 1-3 to build a real system</li>
    <li><a href="/articles/workbuddy-3-layer-memory-system-make-ai-understand-you">WorkBuddy L05: Master the 3-Layer Memory System</a> — Skills 9-10 in action with automation</li>
    <li><a href="/articles/tencent-workbuddy-ai-office-workbench">Tencent WorkBuddy: The Ultimate AI Office Workbench</a> — the complete WorkBuddy feature reference</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">📚 AI 教程</span>
  <span class="meta-badge">🕒 阅读约8分钟</span>
  <span class="meta-badge">📅 2026年7月15日</span>
  <span class="meta-badge">🎯 入门</span>
</div>

<h2 id="introduction">引言</h2>

<p>很多人把AI助手当搜索引擎用，但有些人已经把它们变成了帮自己干活的虚拟队友。区别不在于AI有多强大——而在于你怎么用它。本指南将WorkBuddy的官方最佳实践拆解为10项可操作技能，覆盖从清晰沟通到让AI接管重复任务的全部内容。读完你会发现，自己至少浪费了AI一半的潜力。</p>

<h2 id="categories">十大技能，五大阶段</h2>

<p>这些技能分为五个阶段：<strong>沟通基础</strong>、<strong>提速方法</strong>、<strong>安全风险管理</strong>、<strong>放大技巧</strong>和<strong>自动化智能工作流</strong>。</p>

<h2 id="skill-1">技能1：清晰沟通——三要素一次到位</h2>

<p>最重要的技能：<strong>具体明确</strong>。向WorkBuddy求助时，不要依赖模糊描述。定义三件事：</p>

<ol>
  <li><strong>做什么</strong>：确切的任务或目标。</li>
  <li><strong>条件</strong>：任何约束、规则或上下文。</li>
  <li><strong>期望结果</strong>：成功的样子。</li>
</ol>

<p>就像给实习生分配工作：不清晰的指令必然导致错误。</p>

<p><strong>好的提示词示例</strong>：</p>
<pre><code class="language-text">写一篇500字的AI生产力工具博客，面向小企业主。语气友好实用，包含3条可操作建议。结尾加上行动号召。</code></pre>

<h2 id="skill-2">技能2：小步快跑——像剥洋葱一样拆解大任务</h2>

<p>别指望WorkBuddy一次处理庞大复杂任务。分层拆解：</p>

<ol>
  <li><strong>分析需求</strong>：明确核心目标。</li>
  <li><strong>搭建框架</strong>：勾勒结构。</li>
  <li><strong>填充细节</strong>：逐块添加内容。</li>
  <li><strong>边做边改</strong>：每步调整优化。</li>
</ol>

<p><strong>项目计划示例工作流</strong>：</p>
<ol>
  <li>让WorkBuddy列出营销活动的主要阶段。</li>
  <li>然后让它为每个阶段添加时间线细节。</li>
  <li>最后让它为每项任务添加预算估算。</li>
</ol>

<h2 id="skill-3">技能3：拥抱多轮对话——别指望一次完美</h2>

<p>WorkBuddy不会每次都一次完美理解你的意图。把首次回复当草稿：</p>
<ul>
  <li>指出具体问题。</li>
  <li>从不同角度重新表述需求。</li>
  <li>让它切换角色（如"以营销专家的身份重写"）。</li>
</ul>

<p>好结果来自持续打磨。</p>

<h2 id="skill-4">技能4：安全第一——先本地，后远程</h2>

<p>新手始终先从本地任务开始，再转向远程或云端工作：</p>
<ol>
  <li>在自己电脑上练习：让WorkBuddy整理文件、编辑文档或分析本地数据。</li>
  <li>了解它的能力边界：理解能做什么、不能做什么。</li>
  <li>有信心后再转向远程任务。</li>
</ol>

<h2 id="skill-5">技能5：给WorkBuddy一个角色——内置专家模式</h2>

<p>WorkBuddy有内置专家角色，如产品经理和数据分析师。分配角色后，立即获得更专业、更有上下文意识的回复。</p>

<p><strong>带角色的提示词示例</strong>：</p>
<pre><code class="language-text">以数据分析师的身份。分析这份销售数据，识别3个关键趋势。用简单表格呈现结果。</code></pre>

<h2 id="skill-6">技能6：提供示例——一个样本胜过千言万语</h2>

<p>想让WorkBuddy匹配特定风格或语气，不要只描述——展示出来。给它一个样本，说"遵循这个风格"。</p>

<p><strong>示例</strong>：</p>
<pre><code class="language-text">为我们的新产品发布写一篇社交媒体帖子。使用与这个样本相同的语气和结构：[在此粘贴样本帖子]。</code></pre>

<h2 id="skill-7">技能7：管理对话——别把所有任务塞进一个聊天</h2>

<p>把每个对话当作独立工作区：</p>
<ul>
  <li>一个聊天写报告。</li>
  <li>另一个做数据分析。</li>
  <li>第三个做头脑风暴。</li>
</ul>

<p>这保持上下文清晰，防止WorkBuddy混淆，还能并行处理多个任务。</p>

<h2 id="skill-8">技能8：频繁备份——信任AI，但保护你的工作</h2>

<p>最好的AI也会犯错。让WorkBuddy编辑重要文件前：</p>
<ol>
  <li><strong>做备份</strong>：始终备份原始文件。</li>
  <li><strong>测试变更</strong>：先让WorkBuddy编辑副本。</li>
  <li><strong>完成后审查</strong>：仔细检查结果。</li>
</ol>

<h2 id="skill-9">技能9：自动化——让WorkBuddy在后台工作</h2>

<p>掌握基础后，用自动化解放时间：</p>
<ol>
  <li>设置定时任务：让WorkBuddy自动发送日报或周报。</li>
  <li>构建工作流：串联任务，一个动作触发下一个。</li>
  <li>后台运行：WorkBuddy可24/7处理重复任务。</li>
</ol>

<p><strong>自动化工作流示例</strong>：</p>
<pre><code class="language-text">每周一上午9点，分析上周销售数据，创建汇总报告，发送到团队邮件列表。</code></pre>

<h2 id="skill-10">技能10：聪明的懒惰 + 动力——达到终极水平</h2>

<p>最后一项技能关于更聪明地工作：</p>
<ul>
  <li><strong>懒惰</strong>：把重复性机械任务交给WorkBuddy，专注创造性高价值工作。</li>
  <li><strong>动力</strong>：对WorkBuddy设高期望。告诉它"你是高级顾问——给我最好的建议"。</li>
</ul>

<p>这推动WorkBuddy产出更深入、更有洞察力的结果。</p>

<h2 id="mastery-roadmap">掌握路线图</h2>

<p>按以下顺序最大化WorkBuddy价值：</p>

<ol>
  <li><strong>从清晰沟通开始</strong>：使用三要素提示词框架。</li>
  <li><strong>学会拆解任务</strong>：使用小步骤和多轮对话。</li>
  <li><strong>善用角色、示例和多聊天</strong>：提升输出质量和效率。</li>
  <li><strong>自信地自动化</strong>：熟练后，用自动化扩展工作规模。</li>
</ol>

<p>按这些步骤，你将把WorkBuddy变成真正的生产力伙伴，帮你承担重活。</p>

<h2>常见问题</h2>

<h3>这10项技能中哪项对新手回报最快？</h3>
<p>技能1、2和5组合使用。<strong>清晰沟通</strong>（技能1）立即改善你写的每个提示词——即使花30秒结构化你的请求，也能把无用回复变成可用输出。<strong>小步快跑</strong>（技能2）防止最常见的初学者错误：一次要太多，被混乱输出淹没。<strong>角色分配</strong>（技能5）是任何提示词加一行就能显著提升质量的做法。掌握这三项，你已经进入WorkBuddy用户的前20%。其他技能建立在这个基础上。</p>

<h3>技能9（自动化）和简单定时任务有什么不同？</h3>
<p>定时任务是基于时间的（"早上9点做X"）。自动化是<strong>基于工作流的</strong>（"当X发生，做Y，然后Z"）。技能9涵盖两者但强调工作流方式。定时任务每次都运行相同提示词。自动化工作流可以分支："分析销售数据→如果收入下降>10%，生成告警报告发送给经理→如果收入稳定，只更新仪表盘。"这种条件逻辑区分了高级用户和普通用户。WorkBuddy的自动化系统支持定时循环和触发式工作流两种模式。</p>

<h3>真的应该为不同任务用不同聊天吗？</h3>
<p>是的，原因如下：AI模型有上下文窗口。当你在一个聊天中混合报告撰写、数据分析和头脑风暴，上下文会被污染——AI可能在写报告时引用头脑风暴的数据，或把报告写作的正式语气应用到创意头脑风暴。独立聊天保持每个任务的上下文干净。它还让你并行处理多个任务：WorkBuddy在一个聊天中生成长报告时，你可以在另一个聊天中头脑风暴创意。这个简单习惯零成本，能预防最常见的AI质量下降问题。</p>

<h3>新手用WorkBuddy最大的错误是什么？</h3>
<p><strong>把它当Google用</strong>——输入3-5个词的查询，期待完美结果。Google是找已有信息的搜索引擎。WorkBuddy是根据你的指令创造新输出的AI Agent。"分析销售数据"和"分析这份Q3销售表格。按收入识别前3名产品，标记环比下降趋势的产品，用百分比变化表格呈现"之间的质量差距巨大。第一个提示词得到通用回复。第二个得到专业分析。区别是30秒的额外打字时间。本指南的技能1就是专门解决这个问题的。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>掌握了10项技能？付诸实践：</p>
  <ul>
    <li><a href="/articles/build-personal-ai-knowledge-base-workbuddy-ima-guide">WorkBuddy + IMA：搭建个人AI知识库的完整指南</a> — 应用技能1-3构建真实系统</li>
    <li><a href="/articles/workbuddy-3-layer-memory-system-make-ai-understand-you">WorkBuddy L05：掌握三层记忆系统，让AI越来越懂你</a> — 技能9-10在自动化中的实战</li>
    <li><a href="/articles/tencent-workbuddy-ai-office-workbench">腾讯WorkBuddy：日常办公的终极AI工作台</a> — 完整WorkBuddy功能参考</li>
  </ul>
</div>`,
  },

'''

last_brace = content_src.rfind('};')
content_new = content_src[:last_brace] + new_contents + '};'

with open('src/lib/article-content.ts', 'w', encoding='utf-8') as f:
    f.write(content_new)

print('Part 2: 2 article contents added to article-content.ts')

print('\n=== All done! Run build to verify ===')