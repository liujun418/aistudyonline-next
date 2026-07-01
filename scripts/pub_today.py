"""
Publish July 1, 2026 articles.
No new tools - GitHub trending projects are not standalone AI tools, TRAE Work is a Trae variant.
"""
import os

BASE = r"C:\Users\jun\aistudyonline-next"
os.chdir(BASE)

# ===== Part 1: Add 2 article metadata to articles.ts =====
with open('src/lib/articles.ts', 'r', encoding='utf-8') as f:
    articles_src = f.read()

new_articles = r"""  {
    slug: "github-weekly-trending-ai-tools-agents-dominate",
    title: "GitHub Weekly Trending: AI Tools and Agents Dominate the Chart",
    titleZh: "GitHub周趋势：AI工具与Agent霸榜",
    description: "This week's top 10 trending GitHub projects — OpenMontage (AI video studio), Agent-Reach (no-API-key web browsing), codebase-memory-mcp (99% token reduction), Cognee (Agent long-term memory), and more. All with star counts and key features.",
    descriptionZh: "本周GitHub十大热门项目——OpenMontage（AI视频工作室）、Agent-Reach（无需API密钥上网）、codebase-memory-mcp（99% token节省）、Cognee（Agent长期记忆）等。含星数和核心特性。",
    category: "ai-tutorials",
    tags: ["github", "trending", "open-source", "agent", "video", "memory", "tools"],
    difficulty: "beginner",
    toolsMentioned: ["claude", "cursor", "deer-flow"],
    date: "2026-07-01",
  },
  {
    slug: "mastering-ai-workflow-beginner-custom-workbench",
    title: "Mastering AI Workflow: A Beginner-Friendly Guide to Building Your Custom AI Workbench",
    titleZh: "掌握AI工作流：新手友好的自定义AI工作台搭建指南",
    description: "Build a personal AI workbench that boosted productivity by 400% — automate repetitive tasks, create custom Skills, and set up mobile AI office using TRAE Work. Step-by-step from task automation to full workbench.",
    descriptionZh: "搭建提升400%效率的个人AI工作台——用TRAE Work自动化重复任务、创建自定义Skills、搭建移动AI办公。从任务自动化到完整工作台的逐步指南。",
    category: "ai-tutorials",
    tags: ["workflow", "automation", "trae", "skills", "productivity", "beginner"],
    difficulty: "beginner",
    toolsMentioned: ["trae-framework"],
    date: "2026-07-01",
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
  "github-weekly-trending-ai-tools-agents-dominate": {
    content: `<div class="meta-banner">
<p><strong>📅 Published:</strong> July 1, 2026 · <strong>🏷️ Category:</strong> AI Tutorials · <strong>📊 Level:</strong> Beginner</p>
</div>

<p>This week on GitHub, AI tools and Agents are making a splash, with video and memory-related tools seeing rapid growth. Let's dive into the top 10 projects that developers are buzzing about.</p>

<h2>1. OpenMontage — AI Video Production Studio</h2>
<p><strong>+18.0k stars</strong> in a week, totaling 25.6k stars.</p>
<ul>
<li>12 production pipelines for animation, documentary, short film, and subtitle creation</li>
<li>52 tools covering video generation, image creation, TTS, music, and subtitle processing</li>
<li>500+ Agent skills with expert guidance at each stage</li>
<li>Supports real material editing — arguably the most complete open-source video generation system</li>
</ul>

<h2>2. Agent-Reach — No-API-Key Web Browsing for Agents</h2>
<p><strong>+7.7k stars</strong> in a week, totaling 4.37k stars.</p>
<ul>
<li>Supports 10+ platforms (Twitter, CSDN, Xiaohongshu, Reddit, GitHub)</li>
<li>One-click installation: copy a line to your Agent and it auto-configures</li>
<li>Automatic failover: if a platform is blocked, switches to backup without user intervention</li>
</ul>

<h2>3. codebase-memory-mcp — Intelligent Code Knowledge Graph</h2>
<p><strong>+7.7k stars</strong> in a week, totaling 18.0k stars.</p>
<ul>
<li>Millisecond-level queries for 158 programming languages</li>
<li><strong>99% reduction in token consumption</strong> compared to traditional methods</li>
<li>Indexes the 2.8 million-line Linux kernel in 3 minutes, queries under 1 millisecond</li>
<li>Single-file installation with zero dependencies, compatible with 11 assistants including Claude Code and Cursor</li>
</ul>

<h2>4. daily_stock_analysis — LLM-Driven Multi-Market Stock Analysis</h2>
<p><strong>+7.1k stars</strong> in a week, totaling 50.6k stars.</p>
<ul>
<li>Supports A-shares, Hong Kong, US, Japanese, and Korean stocks</li>
<li>Aggregates market data, news, and technical indicators for auto-generated buy/sell dashboards</li>
<li>Sends updates to WeCom, Feishu, or Telegram</li>
<li>Runs on GitHub Actions for zero-cost scheduling</li>
</ul>

<h2>5. Cognee — Long-Term Memory Platform for AI Agents</h2>
<p><strong>+5.5k stars</strong> in a week, totaling 24.1k stars.</p>
<ul>
<li>Helps Agents remember important information across conversations</li>
<li>Supports data import, knowledge graph construction, and semantic search</li>
<li>End-to-end open-source and self-hostable, PostgreSQL as unified backend</li>
<li>Outperforms previous SOTA in BEAM benchmark: 0.79 score in 100k token scenarios</li>
</ul>

<h2>6. Anthropic-Cybersecurity-Skills — 817 Security Skills for Agents</h2>
<p><strong>+5.1k stars</strong> in a week, totaling 22.3k stars.</p>
<ul>
<li>Maps to MITRE ATT&CK, NIST CSF, ATLAS frameworks</li>
<li>Covers 29 security domains: cloud security, threat hunting, incident analysis</li>
<li>Provides expert-level operation manuals for penetration testing, threat hunting, and DFIR</li>
</ul>

<h2>7. ai-website-cloner-template — One-Command Website Cloning</h2>
<p><strong>+4.6k stars</strong> in a week, totaling 22.3k stars.</p>
<ul>
<li>One command: <code>ai-website-cloner &lt;target-url&gt;</code></li>
<li>AI analyzes the target site, extracts design specs, builds sections in parallel, merges into clean Next.js code</li>
<li>Uses TypeScript, Next.js 16, Tailwind CSS v4 — up-to-date technology stack</li>
</ul>

<h2>8. Voicebox — Open-Source AI Voice Studio</h2>
<p><strong>+4.0k stars</strong> in a week, totaling 35.0k stars.</p>
<ul>
<li>7 TTS engines supporting 23 languages</li>
<li>Zero-shot voice cloning and full transcription</li>
<li>Built with Tauri + Rust for local execution, privacy, and security</li>
<li>Supports pitch, reverb, and delay effects switching</li>
</ul>

<h2>9. Penpot — Open-Source Figma Alternative</h2>
<p><strong>+3.3k stars</strong> in a week, totaling 54.2k stars.</p>
<ul>
<li>Supports SVG, CSS, and HTML design with real-time collaboration</li>
<li>Integrates with MCP servers for design-to-code workflow</li>
<li>Runs in browser or self-hosted, written in Clojure</li>
<li>Seamless design handoff and direct usable code export</li>
</ul>

<h2>10. Deer-Flow — ByteDance's Super Agent Framework</h2>
<p><strong>+3.3k stars</strong> in a week, totaling 75.1k stars (highest on the list).</p>
<ul>
<li>LAN graph-driven, supporting sub-Agent sandbox execution</li>
<li>Integrates IM channels like Telegram, Feishu, and WeChat</li>
<li>Breaks down complex tasks for sub-Agents to execute in parallel</li>
<li>Automates tasks from minutes to hours</li>
</ul>

<h2>常见问题</h2>

<h3>Which of these projects is most immediately useful for an AI developer?</h3>
<p>codebase-memory-mcp is the most impactful for daily AI coding work. It indexes your codebase into a knowledge graph and reduces token consumption by 99% — meaning your AI coding assistant can understand your entire project without burning through your context window. It works with Claude Code, Cursor, and 9 other assistants, installs as a single file with zero dependencies, and can index the entire Linux kernel (2.8M lines) in 3 minutes. For anyone doing AI-assisted development on non-trivial codebases, this is a game-changer.</p>

<h3>Are these GitHub trending projects production-ready or just experiments?</h3>
<p>Mixed. Deer-Flow (75.1k stars, ByteDance-backed) and Penpot (54.2k stars) are mature, production-tested projects. daily_stock_analysis (50.6k stars) is actively used by traders. codebase-memory-mcp (18k stars) is being adopted by professional dev teams. On the newer side, Agent-Reach (4.37k stars) and OpenMontage (25.6k stars) are growing fast but still maturing. The star counts are a decent proxy for maturity — projects above 20k stars generally have stable APIs and active maintenance. Below 10k, expect some rough edges and rapid API changes.</p>

<h3>How do I choose which trending projects to actually adopt?</h3>
<p>Three criteria: (1) Does it solve a problem you actually have right now? Don't adopt a tool just because it's trending. (2) Check the issue tracker — look at how many open issues there are and how quickly maintainers respond. A project with 50+ unanswered issues is a red flag. (3) Test with a small, non-critical task first. For codebase-memory-mcp, try it on a side project before pointing it at your production codebase. The best GitHub projects become essential parts of your workflow; the rest are interesting experiments you learn from and move on.</p>

<div class="next-step">
<p><strong>下一篇：</strong> <a href="/en/article/mastering-ai-workflow-beginner-custom-workbench">Mastering AI Workflow: A Beginner-Friendly Guide to Building Your Custom AI Workbench →</a></p>
</div>`,
    contentZh: `<div class="meta-banner">
<p><strong>📅 发布日期：</strong>2026年7月1日 · <strong>🏷️ 分类：</strong>AI教程 · <strong>📊 难度：</strong>初级</p>
</div>

<p>本周GitHub上，AI工具和Agent掀起热潮，视频和记忆相关工具增长迅猛。让我们深入了解开发者热议的十大项目。</p>

<h2>1. OpenMontage — AI视频制作工作室</h2>
<p>一周<strong>+18.0k stars</strong>，总计25.6k stars。</p>
<ul>
<li>12条制作管线：动画、纪录片、短片、字幕创作</li>
<li>52个工具覆盖视频生成、图像创作、TTS、音乐和字幕处理</li>
<li>500+ Agent技能，每阶段有专家指导</li>
<li>支持真实素材编辑——可能是最完整的开源视频生成系统</li>
</ul>

<h2>2. Agent-Reach — Agent免API密钥上网</h2>
<p>一周<strong>+7.7k stars</strong>，总计4.37k stars。</p>
<ul>
<li>支持10+平台（Twitter、CSDN、小红书、Reddit、GitHub）</li>
<li>一键安装：复制一行到Agent，自动配置一切</li>
<li>自动故障切换：平台被屏蔽时自动切换备用方案，无需用户干预</li>
</ul>

<h2>3. codebase-memory-mcp — 智能代码知识图谱</h2>
<p>一周<strong>+7.7k stars</strong>，总计18.0k stars。</p>
<ul>
<li>158种编程语言的毫秒级查询</li>
<li>相比传统方法<strong>减少99% token消耗</strong></li>
<li>3分钟索引280万行Linux内核，查询响应低于1毫秒</li>
<li>单文件安装零依赖，兼容Claude Code、Cursor等11种编程助手</li>
</ul>

<h2>4. daily_stock_analysis — LLM驱动多市场股票分析</h2>
<p>一周<strong>+7.1k stars</strong>，总计50.6k stars。</p>
<ul>
<li>支持A股、港股、美股、日股、韩股</li>
<li>聚合市场数据、新闻和技术指标，自动生成买卖决策仪表盘</li>
<li>发送更新到企业微信、飞书或Telegram</li>
<li>运行在GitHub Actions上零成本调度</li>
</ul>

<h2>5. Cognee — AI Agent长期记忆平台</h2>
<p>一周<strong>+5.5k stars</strong>，总计24.1k stars。</p>
<ul>
<li>帮助Agent跨对话记住重要信息</li>
<li>支持数据导入、知识图谱构建和语义搜索</li>
<li>端到端开源可自托管，PostgreSQL统一后端</li>
<li>BEAM基准测试超越此前SOTA：100k token场景得分0.79</li>
</ul>

<h2>6. Anthropic-Cybersecurity-Skills — 817项Agent安全技能</h2>
<p>一周<strong>+5.1k stars</strong>，总计22.3k stars。</p>
<ul>
<li>映射MITRE ATT&CK、NIST CSF、ATLAS等框架</li>
<li>覆盖29个安全领域：云安全、威胁狩猎、事件分析</li>
<li>提供渗透测试、威胁狩猎和DFIR的专家级操作手册</li>
</ul>

<h2>7. ai-website-cloner-template — 一条命令克隆网站</h2>
<p>一周<strong>+4.6k stars</strong>，总计22.3k stars。</p>
<ul>
<li>一条命令：<code>ai-website-cloner &lt;目标URL&gt;</code></li>
<li>AI自动分析目标网站、提取设计规范、并行构建各部分、合并为干净Next.js代码</li>
<li>使用TypeScript、Next.js 16、Tailwind CSS v4——技术栈最新</li>
</ul>

<h2>8. Voicebox — 开源AI语音工作室</h2>
<p>一周<strong>+4.0k stars</strong>，总计35.0k stars。</p>
<ul>
<li>7个TTS引擎支持23种语言</li>
<li>零样本声音克隆和完整转录</li>
<li>Tauri + Rust构建，本地执行保护隐私安全</li>
<li>支持切换音高、混响和延迟效果</li>
</ul>

<h2>9. Penpot — 开源Figma替代品</h2>
<p>一周<strong>+3.3k stars</strong>，总计54.2k stars。</p>
<ul>
<li>支持SVG、CSS和HTML设计，实时协作</li>
<li>集成MCP服务器实现设计到代码工作流</li>
<li>浏览器运行或自托管，Clojure编写</li>
<li>设计稿无缝交接，直接导出可用代码</li>
</ul>

<h2>10. Deer-Flow — 字节跳动超级Agent框架</h2>
<p>一周<strong>+3.3k stars</strong>，总计75.1k stars（榜单最高）。</p>
<ul>
<li>LAN图驱动，支持子Agent沙箱执行</li>
<li>集成Telegram、飞书、微信等IM渠道</li>
<li>拆解复杂任务由子Agent并行执行</li>
<li>自动化数分钟到数小时的任务</li>
</ul>

<h2>常见问题</h2>

<h3>哪个项目对AI开发者最直接有用？</h3>
<p>codebase-memory-mcp对日常AI编程工作影响最大。它将你的代码库索引为知识图谱，减少99%的token消耗——意味着你的AI编程助手可以理解整个项目而不会耗尽上下文窗口。它兼容Claude Code、Cursor等11种助手，单文件安装零依赖，可在3分钟内索引整个Linux内核（280万行代码）。对于在非平凡代码库上进行AI辅助开发的任何人，这都是改变游戏规则的工具。</p>

<h3>这些GitHub热门项目是生产就绪的还是只是实验？</h3>
<p>混合的。Deer-Flow（75.1k stars，字节跳动支持）和Penpot（54.2k stars）是成熟、经过生产测试的项目。daily_stock_analysis（50.6k stars）被交易者积极使用。codebase-memory-mcp（18k stars）正被专业开发团队采用。较新的方面，Agent-Reach（4.37k stars）和OpenMontage（25.6k stars）增长迅速但仍在成熟中。星数是成熟度的合理代理——超过20k stars的项目通常有稳定的API和活跃维护。低于10k，预计会有一些粗糙边缘和快速API变更。</p>

<h3>如何选择实际采用哪些热门项目？</h3>
<p>三个标准：（1）它解决了你现在实际遇到的问题吗？不要仅仅因为一个工具热门就采用它。（2）检查issue跟踪器——看有多少未解决的issue以及维护者响应速度。50+未回复issue的项目是红旗。（3）先用小型非关键任务测试。对于codebase-memory-mcp，先在副项目上尝试再指向生产代码库。最好的GitHub项目会成为你工作流中不可或缺的部分；其余的是你从中学习然后继续前进的有趣实验。</p>

<div class="next-step">
<p><strong>下一篇：</strong> <a href="/zh/article/mastering-ai-workflow-beginner-custom-workbench">掌握AI工作流：新手友好的自定义AI工作台搭建指南 →</a></p>
</div>`,
  },

  "mastering-ai-workflow-beginner-custom-workbench": {
    content: `<div class="meta-banner">
<p><strong>📅 Published:</strong> July 1, 2026 · <strong>🏷️ Category:</strong> AI Tutorials · <strong>📊 Level:</strong> Beginner · <strong>🛠️ Tools:</strong> TRAE Work</p>
</div>

<p>In the evolving landscape of workplace productivity, leveraging AI to build a customized workflow is no longer a luxury but a necessity. This guide, tailored for beginners, will walk you through the practical steps to create your own AI workbench — just like the one that boosted work efficiency by 400%.</p>

<h2>My AI Workbench: A Glimpse into Customization</h2>

<p>Components of a self-built AI workbench:</p>
<ul>
<li><strong>Topic Management:</strong> Automatically scrapes data from various platforms to identify trending topics</li>
<li><strong>Library:</strong> A web-based system for managing reading lists and notes, with easy retrieval and reading plan formulation</li>
<li><strong>Schedule Management:</strong> A "Delegate to AI" button — one click assigns tasks to AI for automatic execution, with batch processing for multiple tasks</li>
<li><strong>Experience Review Library:</strong> A self-coded writing application for fine-grained content modification</li>
</ul>

<h2>The Right Mindset: Augment, Not Compete</h2>

<p>Forget the anxiety-inducing rhetoric about AI replacing humans. The correct approach is to <strong>use AI to augment yourself</strong>, not compete with it. Just as cars didn't make walking obsolete but expanded our reach, AI should be your tool to achieve more in less time.</p>

<h2>Getting Started with TRAE Work</h2>

<p>For beginners hesitant about technical hurdles, <strong>TRAE Work</strong> is an excellent choice — a leading domestic Agent application that's free to use, accessible on PC, web, and mobile, and integrated with the Feishu ecosystem.</p>

<h2>Step 1: Automate Repetitive Tasks</h2>

<p>The easiest way to start is identifying tasks you repeat weekly and find tedious. Jot them down — these are your candidates for automation.</p>

<h3>Example Automations:</h3>

<p><strong>1. Growth Daily Report:</strong> Previously, checking data across multiple platforms daily was tedious. Now, delegate to TRAE Work:</p>
<blockquote>"Automatically crawl growth data from [platform names] and generate a daily report."</blockquote>

<p><strong>2. Meeting Summary & Action Items:</strong> TRAE Work automatically reviews Feishu meeting notes at night, extracts methodologies, creates a knowledge base, and schedules to-dos:</p>
<blockquote>"Read today's Feishu meeting notes, extract key methodologies, create a knowledge base, and schedule action items."</blockquote>

<p><strong>3. Schedule Automation:</strong> Reminders for key focus areas daily, or auto-generated weekly/monthly reports:</p>
<blockquote>"Remind me of key priorities every morning and generate a weekly summary."</blockquote>

<h2>Step 2: Create Custom Skills</h2>

<p>When tasks have a consistent pattern but aren't identical, turn them into <strong>Skills</strong> — think of them as your personalized AI apps.</p>

<h3>How to Create Skills:</h3>

<ol>
<li><strong>Find Existing Skills:</strong> Browse the TRAE Work community for pre-built skills. If none fit, ask TRAE Work to search GitHub or Reddit for similar functions.</li>
<li><strong>Customize Skills:</strong> Once you find a skill, modify it by describing your needs: <em>"I want this Skill to scrape content from [platforms], filter for posts with at least [X] likes, format the output in [specific style], focus on [specific topics], and send the result to Feishu."</em></li>
</ol>

<h2>Step 3: Build Your AI Workbench</h2>

<p>As you accumulate skills, you'll want a centralized hub — the AI workbench where all automations and skills converge. Tell TRAE Work your requirements for the web page, including features and design. Iterate by communicating about UI adjustments and new features:</p>

<blockquote>"I want to build a web page to manage all my viral content skills. It should display titles, engagement metrics, and allow easy filtering. Let's design the UI and add features like a search bar."</blockquote>

<h2>Step 4: Mobile AI Office</h2>

<p>To truly free yourself from your desk, leverage TRAE Work's mobile capabilities:</p>
<ul>
<li><strong>Sync Across Devices:</strong> Bind your PC, web, and mobile accounts for cloud synchronization</li>
<li><strong>Delegate Tasks on the Go:</strong> Dictate an idea into your phone, and TRAE Work files it into your idea library or adds it to your calendar</li>
<li><strong>Remote Document Handling:</strong> Command TRAE Work via mobile to edit a document on your office computer and send it: <em>"Edit [document name] as per [client's requirements] and send it to [email address]."</em></li>
</ul>

<h2>The Human Touch in an AI-Driven World</h2>

<p>While AI excels at execution and structured thinking, it can't replace <strong>human emotional experiences and real-life experiences</strong>. As you offload tasks to AI, you'll find more time for team collaboration, offline meetups, idea exchanges, and personal relationships. AI handles the "work" and "labor", while you focus on "action" — the unique human elements of creativity, connection, and self-expression.</p>

<p>Start small, automate the repetitive, customize your skills, and build a workbench that grows with you. The future of work is not about competing with AI, but about harnessing it to be more human.</p>

<h2>常见问题</h2>

<h3>What's the difference between TRAE Work and regular Trae (the coding IDE)?</h3>
<p>TRAE Work is an Agent application focused on task automation and workflow orchestration — it's designed for non-developers to automate daily work tasks. Regular Trae (trae-framework) is an AI coding IDE similar to Cursor, focused on code generation and software development. TRAE Work integrates with Feishu, runs on mobile, and handles things like meeting summaries and data scraping. Think of Trae as your AI programmer and TRAE Work as your AI personal assistant. They complement each other but serve different audiences.</p>

<h3>How much time does it take to set up a useful AI workbench?</h3>
<p>Start with one automation (Step 1) — that takes about 30 minutes the first time, 5 minutes once you're familiar. After a week of using that one automation, you'll naturally identify 2-3 more repetitive tasks to automate. A basic workbench with 3-5 automations can be built over a weekend. The full workbench described in this article (topic management, library, schedule, review system) took the author about 2-3 weeks of incremental building. The key is starting small and adding incrementally — don't try to build everything at once.</p>

<h3>Can I build an AI workbench without TRAE Work?</h3>
<p>Yes. The principles apply to any AI automation tool — Claude Code with custom slash commands, Codex with Agent skills, n8n for visual workflows, or even a combination of Zapier + ChatGPT. TRAE Work is recommended because it's free, has mobile support, and integrates with Feishu (popular in Chinese workplaces). If you're outside the Feishu ecosystem, Claude Code + custom scripts or n8n are excellent alternatives. The methodology (identify repetitive tasks → automate → create skills → build workbench) works regardless of the tool.</p>

<div class="next-step">
<p><strong>上一篇：</strong> <a href="/en/article/github-weekly-trending-ai-tools-agents-dominate">GitHub Weekly Trending: AI Tools and Agents Dominate the Chart ←</a></p>
</div>`,
    contentZh: `<div class="meta-banner">
<p><strong>📅 发布日期：</strong>2026年7月1日 · <strong>🏷️ 分类：</strong>AI教程 · <strong>📊 难度：</strong>初级 · <strong>🛠️ 工具：</strong>TRAE Work</p>
</div>

<p>在职场生产力不断演变的格局中，利用AI构建自定义工作流已不再是奢侈品而是必需品。本指南专为初学者量身定制，将带你完成创建自己AI工作台的实操步骤——就像那个将工作效率提升400%的工作台一样。</p>

<h2>我的AI工作台：一窥自定义</h2>

<p>自建AI工作台的组件：</p>
<ul>
<li><strong>选题管理：</strong> 自动从各平台抓取数据，帮你发现热门话题</li>
<li><strong>图书馆：</strong> 基于Web的阅读清单和笔记管理系统，方便检索和制定阅读计划</li>
<li><strong>日程管理：</strong> "委托给AI"按钮——一键将任务分配给AI自动执行，支持多任务打包批处理</li>
<li><strong>心得复盘库：</strong> 自编码的写作应用，实现精细化内容修改</li>
</ul>

<h2>正确心态：增强，而非竞争</h2>

<p>忘记那些引发焦虑的"AI取代人类"论调。正确的方式是<strong>用AI增强自己</strong>，而非与它竞争。正如汽车没有让步行过时而是扩展了我们的活动范围，AI应该是你用更少时间实现更多目标的工具。</p>

<h2>从TRAE Work开始</h2>

<p>对于担心技术门槛的初学者，<strong>TRAE Work</strong>是绝佳选择——领先的国产Agent应用，免费使用，支持PC、网页和移动端，集成飞书生态。</p>

<h2>第1步：自动化重复任务</h2>

<p>最简单的开始方式是识别你每周重复且觉得繁琐的任务。记下来——这些就是你的自动化候选。</p>

<h3>示例自动化：</h3>

<p><strong>1. 增长日报：</strong> 以前每天要跨多个平台查数据。现在委托给TRAE Work：</p>
<blockquote>"自动抓取[平台名称]的增长数据并生成日报。"</blockquote>

<p><strong>2. 会议总结与行动项：</strong> TRAE Work晚上自动审阅飞书会议笔记，提取方法论，创建知识库，安排待办：</p>
<blockquote>"阅读今天的飞书会议笔记，提取关键方法论，创建知识库，安排行动项。"</blockquote>

<p><strong>3. 日程自动化：</strong> 每日提醒关键重点，或自动生成周/月报：</p>
<blockquote>"每天早上提醒我关键优先级，生成周报总结。"</blockquote>

<h2>第2步：创建自定义Skills</h2>

<p>当任务有固定模式但不完全相同时，将它们转化为<strong>Skills</strong>——把它们想象成你的个性化AI应用。</p>

<h3>如何创建Skills：</h3>

<ol>
<li><strong>找现有Skills：</strong> 浏览TRAE Work社区找预建技能。没有合适的，让TRAE Work在GitHub或Reddit搜索类似功能。</li>
<li><strong>自定义Skills：</strong> 找到技能后通过描述需求修改：<em>"我要这个Skill从[平台]抓取内容，筛选至少[X]赞的帖子，按[特定风格]格式化输出，聚焦[特定主题]，并将结果发送到飞书。"</em></li>
</ol>

<h2>第3步：搭建AI工作台</h2>

<p>随着技能积累，你需要一个集中枢纽——AI工作台，所有自动化和技能汇聚于此。告诉TRAE Work你对网页的需求，包括功能和设计。通过沟通迭代UI调整和新功能：</p>

<blockquote>"我想建一个网页管理所有爆款内容技能。应显示标题、互动指标，支持便捷筛选。我们来设计UI，添加搜索栏等功能。"</blockquote>

<h2>第4步：移动AI办公</h2>

<p>要真正摆脱办公桌，利用TRAE Work的移动能力：</p>
<ul>
<li><strong>跨设备同步：</strong> 绑定PC、网页和移动端账号实现云同步</li>
<li><strong>随时随地委托：</strong> 对着手机口述想法，TRAE Work将其归档到想法库或添加到日历</li>
<li><strong>远程文档处理：</strong> 通过手机命令TRAE Work编辑办公电脑上的文档并发送：<em>"按[客户要求]编辑[文档名]并发送到[邮箱]。"</em></li>
</ul>

<h2>AI驱动世界中的人性触感</h2>

<p>虽然AI擅长执行和结构化思维，但它无法替代<strong>人类的情感体验和真实生活经历</strong>。当你把任务交给AI，你会发现更多时间用于团队协作、线下聚会、想法交流和个人关系。AI处理"工作"和"劳动"，你专注"行动"——创造力、连接和自我表达这些独特的人类元素。</p>

<p>从小处开始，自动化重复的，自定义你的技能，构建一个与你一起成长的工作台。工作的未来不是与AI竞争，而是驾驭它变得更人性化。</p>

<h2>常见问题</h2>

<h3>TRAE Work和普通Trae（编程IDE）有什么区别？</h3>
<p>TRAE Work是一个专注于任务自动化和工作流编排的Agent应用——为非开发者自动化日常工作任务而设计。普通Trae（trae-framework）是类似Cursor的AI编程IDE，专注于代码生成和软件开发。TRAE Work集成飞书，可在移动端运行，处理会议总结和数据抓取等事务。把Trae想象成你的AI程序员，TRAE Work是你的AI个人助理。它们互补但服务不同受众。</p>

<h3>搭建一个有用的AI工作台需要多长时间？</h3>
<p>从一项自动化开始（第1步）——第一次约需30分钟，熟悉后5分钟。使用一周后，你自然会识别出2-3个更多重复任务来自动化。一个包含3-5项自动化的基础工作台可以在一个周末内搭建完成。本文描述的完整工作台（选题管理、图书馆、日程、复盘系统）作者花了约2-3周逐步构建。关键是小处开始逐步添加——不要试图一次构建所有东西。</p>

<h3>没有TRAE Work能搭建AI工作台吗？</h3>
<p>可以。这些原则适用于任何AI自动化工具——带自定义斜杠命令的Claude Code、带Agent技能的Codex、用于可视化工作流的n8n，甚至Zapier+ChatGPT的组合。推荐TRAE Work因为它免费、有移动端支持、集成飞书（在中国职场流行）。如果你不在飞书生态中，Claude Code+自定义脚本或n8n是优秀的替代方案。方法论（识别重复任务→自动化→创建技能→搭建工作台）无论使用什么工具都适用。</p>

<div class="next-step">
<p><strong>上一篇：</strong> <a href="/zh/article/github-weekly-trending-ai-tools-agents-dominate">GitHub周趋势：AI工具与Agent霸榜 ←</a></p>
</div>`,
  },

'''

last_brace = content_src.rfind('};')
content_new = content_src[:last_brace] + new_contents + '};'

with open('src/lib/article-content.ts', 'w', encoding='utf-8') as f:
    f.write(content_new)

print('Part 2: 2 article contents added to article-content.ts')

print('\n=== All done! Run build to verify ===')
