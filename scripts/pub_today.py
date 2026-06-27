"""
Publish June 27, 2026 articles.
New tools: agent-browser, notebooklm, genspark, nano-banana-pro (Seedance skipped - ByteDance video model, covered by existing tools)
"""

import os

BASE = r"C:\Users\jun\aistudyonline-next"
os.chdir(BASE)

# ===== Part 1: Add 4 new tools to tools.ts =====
with open('src/lib/tools.ts', 'r', encoding='utf-8') as f:
    tools_src = f.read()

new_tools = r"""  {
    id: "agent-browser",
    name: "Agent Browser",
    description: "AI-controlled Chrome browser for web scraping with 82% token savings vs Playwright MCP — handles JS-rendered pages, login content, and infinite scroll.",
    descriptionZh: "AI控制的Chrome浏览器网页抓取工具，比Playwright MCP节省82% token——处理JS渲染页面、需登录内容和无限滚动。",
    category: "productivity",
    tags: ["web-scraping", "browser-automation", "chrome", "data-collection"],
    difficulty: "beginner",
    url: "https://www.npmjs.com/package/@vercel/agent-browser",
    rating: r(4.2),
    pricing: "Free (open-source)",
    useCase: "Collect web content for AI knowledge bases — scrape articles, documentation, and dynamic pages directly into raw/ folders for AI processing.",
    icon: "\u{1F310}",
    company: "Vercel",
    companyZh: "Vercel",
    founded: "2015",
    headquarters: "San Francisco, CA",
    descriptionLong: "Agent Browser is a lightweight CLI tool from Vercel that lets AI agents control a real Chrome browser to scrape web content. Unlike headless browser approaches like Playwright MCP, Agent Browser is optimized for AI-to-browser communication, saving 82% more tokens by sending only the relevant extracted text rather than full DOM snapshots. It handles JavaScript-rendered pages, login-required content, and infinitely scrolling pages — scenarios where simple HTTP fetch fails. For AI knowledge base workflows (like Karpathy's 3-folder system), it automates raw material collection by scraping articles directly into the raw/ folder. Install globally with npm, run 'agent-browser install' to set up Chrome, then use commands like 'agent-browser get text \"article\"' to extract clean content.",
    descriptionLongZh: "Agent Browser 是 Vercel 的轻量级 CLI 工具，让 AI Agent 控制真实 Chrome 浏览器抓取网页内容。与 Playwright MCP 等无头浏览器方案不同，Agent Browser 针对 AI 到浏览器的通信进行了优化，通过仅发送提取的相关文本而非完整 DOM 快照来节省 82% 的 token。它处理 JavaScript 渲染页面、需登录内容和无限滚动页面——这些是简单 HTTP fetch 失败的场景。对于 AI 知识库工作流（如 Karpathy 的 3 文件夹系统），它通过直接抓取文章到 raw/ 文件夹来自动化原始材料收集。通过 npm 全局安装，运行 'agent-browser install' 设置 Chrome，然后使用 'agent-browser get text \"article\"' 等命令提取干净内容。",
    advantages: ["82% token savings vs Playwright", "Handles JS-rendered pages", "Login-required content support", "Infinite scroll handling", "Simple CLI interface"],
    advantagesZh: ["比Playwright节省82% token", "处理JS渲染页面", "支持需登录内容", "无限滚动处理", "简单CLI接口"],
    useCases: ["AI knowledge base raw material collection", "Web scraping for research", "Content extraction from dynamic sites", "Automated documentation archiving"],
    useCasesZh: ["AI知识库原始材料收集", "研究用网页抓取", "动态网站内容提取", "自动化文档归档"],
    targetAudience: "AI developers building knowledge bases, researchers collecting web content, and anyone automating web scraping for AI pipelines.",
    targetAudienceZh: "构建知识库的AI开发者、收集网页内容的研究人员、以及为AI管道自动化网页抓取的任何人。",
    pricingTiers: [{tier: "Free", tierZh: "免费版", price: "$0", features: ["Full functionality", "Open-source", "npm package"], featuresZh: ["完整功能", "开源", "npm包"]}],
    pros: ["Extremely token-efficient", "Simple setup", "Handles complex pages", "Free and open-source"],
    prosZh: ["极高的token效率", "简单设置", "处理复杂页面", "免费开源"],
    cons: ["Requires Chrome installed", "Slower than HTTP fetch for simple pages", "Newer tool, smaller community"],
    consZh: ["需要安装Chrome", "简单页面比HTTP fetch慢", "较新工具社区较小"],
    extensions: [],
    skills: [],
    scene: "productivity",
  },
  {
    id: "notebooklm",
    name: "NotebookLM",
    description: "Google's AI knowledge base — upload PDFs, web pages, YouTube videos, and audio to get summaries, answers, and even AI-generated podcasts. Completely free.",
    descriptionZh: "Google的AI知识库——上传PDF、网页、YouTube视频和音频获取摘要、答案甚至AI生成播客。完全免费。",
    category: "productivity",
    tags: ["knowledge-base", "research", "podcast", "summarization", "google"],
    difficulty: "beginner",
    url: "https://notebooklm.google.com",
    rating: r(4.7),
    pricing: "Free",
    useCase: "NotebookLM is the strongest AI knowledge base product — throw in any document and it auto-generates summaries, answers questions, and even creates podcast-style audio discussions from your materials.",
    icon: "\u{1F4DA}",
    company: "Google",
    companyZh: "Google",
    founded: "1998",
    headquarters: "Mountain View, CA",
    descriptionLong: "NotebookLM is Google's AI-powered research and knowledge base tool that has become the undisputed leader in its category. You can upload PDFs, web pages, YouTube videos, and audio files — it automatically generates summaries, answers questions grounded in your sources, and creates remarkably natural podcast-style audio discussions where two AI hosts debate and discuss your materials. The podcast feature is particularly groundbreaking: it turns dry documents into engaging conversational content that's often more interesting than real podcasts. Users report 100x efficiency gains for research tasks. It's completely free, making it accessible to everyone. For Chinese users, Tencent's IMA Knowledge Base offers a domestic alternative with better Chinese language handling and WeChat mini-program integration. NotebookLM excels at research synthesis, meeting note analysis, and turning scattered materials into structured knowledge.",
    descriptionLongZh: "NotebookLM 是 Google 的 AI 驱动研究和知识库工具，已成为该品类无可争议的领导者。你可以上传 PDF、网页、YouTube 视频和音频文件——它自动生成摘要、基于来源回答问题，并创建非常自然的播客风格音频讨论，两个 AI 主持人辩论和讨论你的材料。播客功能尤其具有突破性：它将枯燥文档转化为引人入胜的对话内容，通常比真实播客更有趣。用户报告研究任务效率提升 100 倍。完全免费，人人可用。对于中文用户，腾讯的 IMA 知识库提供国内替代方案，具有更好的中文处理和微信小程序集成。NotebookLM 擅长研究综合、会议笔记分析和将零散材料转化为结构化知识。",
    advantages: ["Completely free", "AI podcast generation", "Multi-format input (PDF, web, YouTube, audio)", "Source-grounded answers", "Google ecosystem integration"],
    advantagesZh: ["完全免费", "AI播客生成", "多格式输入(PDF/网页/YouTube/音频)", "基于来源的回答", "Google生态集成"],
    useCases: ["Research synthesis", "Meeting note analysis", "Study material organization", "Content repurposing into podcasts"],
    useCasesZh: ["研究综合", "会议笔记分析", "学习材料整理", "内容转为播客"],
    targetAudience: "Researchers, students, content creators, and anyone who needs to organize and digest large amounts of information from diverse sources.",
    targetAudienceZh: "研究人员、学生、内容创作者、以及任何需要组织和消化大量多源信息的人。",
    pricingTiers: [{tier: "Free", tierZh: "免费版", price: "$0", features: ["Unlimited notebooks", "All input formats", "Podcast generation", "Source-grounded Q&A"], featuresZh: ["无限笔记本", "所有输入格式", "播客生成", "基于来源的问答"]}],
    pros: ["Best-in-class knowledge base", "Free with no limits", "Unique podcast feature", "Google-quality AI"],
    prosZh: ["顶级知识库", "免费无限制", "独特的播客功能", "Google品质AI"],
    cons: ["Requires Google account", "No API for automation", "Limited customization"],
    consZh: ["需要Google账号", "无API自动化", "定制化有限"],
    extensions: [],
    skills: [],
    scene: "productivity",
  },
  {
    id: "genspark",
    name: "Genspark",
    description: "General-purpose AI Agent that handles multi-step tasks — meeting minutes, fact-checking, research PPTs — by decomposing and executing complex workflows autonomously.",
    descriptionZh: "通用AI Agent处理多步骤任务——会议纪要、事实核查、研究PPT——通过自主分解和执行复杂工作流。",
    category: "productivity",
    tags: ["agent", "automation", "research", "fact-checking", "meeting-minutes"],
    difficulty: "beginner",
    url: "https://www.genspark.ai",
    rating: r(4.3),
    pricing: "Free tier + Pro",
    useCase: "Genspark autonomously researches topics, fact-checks claims, generates meeting minutes with action items, and creates research presentations — handling multi-step tasks end-to-end.",
    icon: "\u{1F916}",
    company: "Genspark",
    companyZh: "Genspark",
    founded: "2023",
    headquarters: "Palo Alto, CA",
    descriptionLong: "Genspark is currently the strongest general-purpose AI Agent product, having evolved from concept to truly usable tool. Unlike simple chatbots, Genspark autonomously handles multi-step tasks: it can generate meeting minutes with automatic key point extraction and action item tracking, perform fact-checking to verify information authenticity and solve AI hallucination problems, and decompose complex tasks into sub-steps for sequential execution. For example, asking it to 'research the top 10 most profitable overseas companies in 2025 and create a research PPT' — it automatically searches, compares, organizes, and produces the deliverable, reportedly 10x faster than manual work. Genspark's AI calling capability is its standout feature: it doesn't just answer questions, it gets things done. The alternative is Manus, which pioneered the AI Agent track but has more expensive pricing. For users wanting autonomous task completion rather than just conversation, Genspark represents the current state of the art.",
    descriptionLongZh: "Genspark 是目前最强的通用 AI Agent 产品，已从概念进化为真正可用的工具。与简单聊天机器人不同，Genspark 自主处理多步骤任务：它可以生成会议纪要并自动提取关键点和行动项跟踪，执行事实核查验证信息真实性并解决 AI 幻觉问题，以及将复杂任务分解为子步骤顺序执行。例如，让它'调研 2025 年海外最赚钱的 10 家公司并制作研究 PPT'——它自动搜索、比较、整理并产出成果，据报道比手动工作快 10 倍。Genspark 的 AI 调用能力是其突出特点：它不只是回答问题，而是把事情做成。替代方案是 Manus，作为 AI Agent 赛道的先驱，效果也不错但定价更贵。对于想要自主完成任务而非仅仅对话的用户，Genspark 代表了当前最先进水平。",
    advantages: ["Autonomous multi-step execution", "Built-in fact-checking", "Meeting minutes with action items", "Research-to-PPT workflow", "10x faster than manual research"],
    advantagesZh: ["自主多步骤执行", "内置事实核查", "带行动项的会议纪要", "研究到PPT工作流", "比手动研究快10倍"],
    useCases: ["Automated research reports", "Meeting minutes & summaries", "Fact-checking & verification", "Presentation generation"],
    useCasesZh: ["自动化研究报告", "会议纪要与摘要", "事实核查与验证", "演示文稿生成"],
    targetAudience: "Professionals who spend significant time on research, meeting documentation, and content verification — consultants, analysts, project managers, and content creators.",
    targetAudienceZh: "在研究、会议文档和内容验证上花费大量时间的专业人士——顾问、分析师、项目经理和内容创作者。",
    pricingTiers: [
      {tier: "Free", tierZh: "免费版", price: "$0", features: ["Basic agent tasks", "Limited queries"], featuresZh: ["基础Agent任务", "有限查询"]},
      {tier: "Pro", tierZh: "专业版", price: "$20/month", features: ["Unlimited tasks", "Priority processing", "Advanced fact-checking"], featuresZh: ["无限任务", "优先处理", "高级事实核查"]}
    ],
    pros: ["Truly autonomous agent", "Excellent research output", "Built-in hallucination guard", "Competitive pricing"],
    prosZh: ["真正自主的Agent", "优秀的研究输出", "内置幻觉防护", "有竞争力定价"],
    cons: ["Newer product, evolving rapidly", "Occasional task decomposition errors", "Less suitable for creative tasks"],
    consZh: ["较新产品快速迭代", "偶有任务分解错误", "不适合创意任务"],
    extensions: [],
    skills: [],
    scene: "productivity",
  },
  {
    id: "nano-banana-pro",
    name: "Nano Banana Pro",
    description: "Google's top-ranked AI image generator with precise inpainting — change backgrounds, clothing colors, or specific regions while keeping everything else intact.",
    descriptionZh: "Google顶级AI图像生成器，精准局部编辑——换背景、改衣服颜色或修改指定区域，其他部分保持不变。",
    category: "image-generation",
    tags: ["image-generation", "inpainting", "google", "editing", "design"],
    difficulty: "beginner",
    url: "https://deepmind.google/technologies/nano-banana/",
    rating: r(4.6),
    pricing: "Free (with Google account)",
    useCase: "Nano Banana Pro tops AI image generation rankings with quality rivaling MidJourney plus precise 'point-and-edit' inpainting that MidJourney can't match — upload a photo and modify only what you specify.",
    icon: "\u{1F3A8}",
    company: "Google DeepMind",
    companyZh: "Google DeepMind",
    founded: "2010",
    headquarters: "London, UK",
    descriptionLong: "Nano Banana Pro is Google DeepMind's image generation model that immediately topped various AI image generation rankings upon launch in 2025. Its image quality rivals MidJourney, but its killer feature is precise inpainting: upload a photo, specify an area to change (background, clothing color, object), and it modifies only that region while keeping everything else virtually identical. This 'voice-controlled editing' capability is something many AI image tools including MidJourney cannot do reliably. Many designers have canceled their MidJourney subscriptions after trying Nano Banana Pro. It's free with a Google account, making it the most accessible high-quality AI image tool. Alternatives include ByteDance's Jiemeng/Doubao (high cost-performance) and the open-source Flux model (runs on 6GB VRAM locally). For anyone doing visual content creation, Nano Banana Pro represents the current state of the art in accessible, precise AI image generation and editing.",
    descriptionLongZh: "Nano Banana Pro 是 Google DeepMind 的图像生成模型，2025年一推出就立即登顶各类 AI 图像生成排行榜。其画质媲美 MidJourney，但杀手级功能是精准局部重绘：上传照片，指定要修改的区域（背景、衣服颜色、物体），它只修改该区域而其他部分几乎完全不变。这种'语音控制编辑'能力是包括 MidJourney 在内的许多 AI 图像工具无法可靠做到的。许多设计师在试用 Nano Banana Pro 后取消了 MidJourney 订阅。Google 账号免费使用，使其成为最容易获取的高质量 AI 图像工具。替代方案包括字节跳动的即梦/豆包（高性价比）和开源 Flux 模型（6GB 显存本地运行）。对于任何做视觉内容创作的人，Nano Banana Pro 代表了可访问、精准 AI 图像生成和编辑的当前最高水平。",
    advantages: ["Free with Google account", "Quality rivals MidJourney", "Precise inpainting/editing", "Point-and-modify interface", "Google ecosystem integration"],
    advantagesZh: ["Google账号免费", "画质媲美MidJourney", "精准局部编辑", "点击即改界面", "Google生态集成"],
    useCases: ["Photo editing & retouching", "Product image variations", "Background replacement", "Design prototyping", "Social media content"],
    useCasesZh: ["照片编辑与修图", "产品图片变体", "背景替换", "设计原型", "社交媒体内容"],
    targetAudience: "Designers, content creators, marketers, and anyone who needs high-quality AI image generation with precise editing control — especially those tired of MidJourney's subscription costs.",
    targetAudienceZh: "设计师、内容创作者、营销人员、以及任何需要高质量 AI 图像生成和精准编辑控制的人——尤其是厌倦 MidJourney 订阅费用的用户。",
    pricingTiers: [{tier: "Free", tierZh: "免费版", price: "$0", features: ["Full image generation", "Inpainting/editing", "Google account access"], featuresZh: ["完整图像生成", "局部编辑", "Google账号访问"]}],
    pros: ["Free and accessible", "Best-in-class inpainting", "Google DeepMind quality", "No subscription needed"],
    prosZh: ["免费易用", "顶级局部编辑", "Google DeepMind品质", "无需订阅"],
    cons: ["Requires Google account", "Less stylized than MidJourney", "Limited API access"],
    consZh: ["需要Google账号", "风格化不如MidJourney", "API访问有限"],
    extensions: [],
    skills: [],
    scene: "design",
  },

"""

last_tool = tools_src.rfind('] as Tool[];')
tools_new = tools_src[:last_tool] + new_tools + '] as Tool[];'

with open('src/lib/tools.ts', 'w', encoding='utf-8') as f:
    f.write(tools_new)

print('Part 1: 4 new tools added to tools.ts (agent-browser, notebooklm, genspark, nano-banana-pro)')

# ===== Part 2: Add 2 article metadata to articles.ts =====
with open('src/lib/articles.ts', 'r', encoding='utf-8') as f:
    articles_src = f.read()

new_articles = r"""  {
    slug: "karpathy-ai-knowledge-base-3-folders",
    title: "Build a Karpathy-Style AI Knowledge Base: A 2-Minute Setup with Just 3 Folders",
    titleZh: "构建Karpathy风格的AI知识库：3个文件夹2分钟搭建",
    description: "Replicate Karpathy's viral 44K-save AI knowledge base system — raw/, wiki/, outputs/ folder structure + CLAUDE.md schema + agent-browser for automated content collection, all running on Claude Code.",
    descriptionZh: "复刻Karpathy爆火44K收藏的AI知识库系统——raw/wiki/outputs三文件夹+CLAUDE.md Schema+agent-browser自动内容收集，全部运行在Claude Code上。",
    category: "ai-tutorials",
    tags: ["knowledge-base", "karpathy", "claude-code", "agent-browser", "wiki", "productivity"],
    difficulty: "beginner",
    toolsMentioned: ["claude", "agent-browser"],
    date: "2026-06-27",
  },
  {
    slug: "best-ai-tools-2026-free-powerful-practical",
    title: "The Best AI Tools of 2026: Free, Powerful, and Practical",
    titleZh: "2026年最佳AI工具：免费、强大、实用",
    description: "A comprehensive guide covering 12 scenarios — from deep research (Gemini 3.1 Pro), writing (Claude Opus 4.6), coding (Cursor/Claude Code/Codex), image gen (Nano Banana Pro), video (Seedance 2.0), to AI agents (Genspark) — with free alternatives for every category.",
    descriptionZh: "覆盖12个场景的全面指南——从深度研究(Gemini 3.1 Pro)、写作(Claude Opus 4.6)、编程(Cursor/Claude Code/Codex)、图像生成(Nano Banana Pro)、视频(Seedance 2.0)到AI Agent(Genspark)——每个类别都有免费替代方案。",
    category: "ai-comparisons",
    tags: ["tools", "roundup", "2026", "free", "comparison", "guide"],
    difficulty: "beginner",
    toolsMentioned: ["gemini", "claude", "chatgpt", "cursor", "codex-agent", "notebooklm", "genspark", "nano-banana-pro", "elevenlabs", "heygen"],
    date: "2026-06-27",
  },

"""

last_bracket = articles_src.rfind('];')
articles_new = articles_src[:last_bracket] + new_articles + '];'

with open('src/lib/articles.ts', 'w', encoding='utf-8') as f:
    f.write(articles_new)

print('Part 2: 2 new articles added to articles.ts')

# ===== Part 3: Add 2 article contents to article-content.ts =====
with open('src/lib/article-content.ts', 'r', encoding='utf-8') as f:
    content_src = f.read()

new_contents = r'''
  "karpathy-ai-knowledge-base-3-folders": {
    content: `<div class="meta-banner">
<p><strong>📅 Published:</strong> June 27, 2026 · <strong>🏷️ Category:</strong> AI Tutorials · <strong>📊 Level:</strong> Beginner · <strong>🛠️ Tools:</strong> Claude Code, Agent Browser</p>
</div>

<p>Karpathy's recent tweet about his AI-powered personal knowledge base went viral, garnering 44K saves and millions of views in just two days. The key insight? He leverages AI to organize scattered notes and articles into a searchable system — no Notion or Obsidian needed, just a simple folder structure and a text file. Here's how to build your own, with practical steps you can implement today.</p>

<h2>The 3-Folder Structure: Super Simple, Fully Flat</h2>

<p>This system can be set up in two minutes, with each folder serving a distinct purpose:</p>

<ul>
<li><strong>raw/</strong>: A drop zone for all your unorganized raw materials — articles, screenshots, notes, etc. Just dump everything here without worrying about organization.</li>
<li><strong>wiki/</strong>: The AI-curated knowledge base. This is where AI writes organized content after processing raw materials. Never edit this folder manually.</li>
<li><strong>outputs/</strong>: Stores AI-generated answers, reports, and analysis results.</li>
</ul>

<pre><code class="language-bash">mkdir my-knowledge-base
cd my-knowledge-base
mkdir raw wiki outputs</code></pre>

<h2>The Schema File: Your AI's Instruction Manual</h2>

<p>A schema file is crucial to guide AI on how to structure and manage your knowledge base. Create a <code>CLAUDE.md</code> file in the root directory with rules like:</p>

<pre><code class="language-markdown"># What This Is
A personal knowledge base about [your topic].

# How to Organize
- raw/: Raw materials, never modify.
- wiki/: AI-maintained organized content.
- outputs/: Generated reports and answers.

# Wiki Rules
- One .md file per topic.
- Link related topics using [[topic-name]] format.
- Maintain INDEX.md to list all main topics.</code></pre>

<p>Karpathy emphasizes that this schema is "super simple" — just a text file telling AI the rules. It directly impacts the quality of the AI-curated wiki, so don't skip this step.</p>

<h2>Launch AI Processing with One Command</h2>

<p>With the folders and schema ready, open Claude Code and issue this prompt:</p>

<blockquote>"Read all content in raw/. Follow the rules in CLAUDE.md to compile a wiki in wiki/. First create INDEX.md, then create a .md file for each main topic. Link related topics. Summarize each section."</blockquote>

<p>Then let AI run — no need to monitor it. Once complete, you'll get a <code>wiki</code> folder with topic-organized articles and an <code>INDEX.md</code> for easy navigation.</p>

<h2>Accelerate Content Collection with agent-browser</h2>

<p>To supercharge raw material collection, use <code>agent-browser</code> — a tool that lets AI control a real Chrome browser to scrape web content. It handles JavaScript-rendered pages, login-required content, and infinitely scrolling pages, while saving 82% more tokens than tools like Playwright MCP.</p>

<pre><code class="language-bash">npm install -g @vercel/agent-browser
agent-browser install
# Example usage
agent-browser open https://some-article.com
agent-browser get text "article"  # Saves text directly to raw/</code></pre>

<h2>Start Using Your Knowledge Base Today</h2>

<p>Karpathy's knowledge base has 44K saves, but the real value comes from actually building and using it. With three folders, one schema file, and an AI tool, you can have your own system up and running in a weekend. Pick a topic you're eager to master, dump your existing articles and notes into <code>raw/</code>, and let AI do the rest.</p>

<h2>常见问题</h2>

<h3>Do I need Claude Code specifically, or can I use any AI tool?</h3>
<p>The system works with any AI coding agent that can read files and write to disk — Claude Code, Codex, Cursor, or even ChatGPT with file access. Claude Code is recommended because its agent loop naturally handles the multi-step process of reading raw files, organizing content, and writing wiki articles without manual intervention. The CLAUDE.md schema file is named for Claude Code but the concept works universally — just adapt the filename to your tool's convention (AGENTS.md for Codex, .cursorrules for Cursor).</p>

<h3>How is this different from using Notion or Obsidian?</h3>
<p>Karpathy's system is intentionally simpler: plain Markdown files in folders, no proprietary formats, no vendor lock-in. You own your data as files on disk. The AI does the organizing work that you'd normally do manually in Notion — tagging, linking, summarizing. It's a <em>build</em> system for knowledge: dump raw materials in, get organized wiki out. Notion and Obsidian are great tools, but they require you to do the organizing. This system lets AI handle that.</p>

<h3>What happens if the AI makes mistakes in the wiki?</h3>
<p>The wiki/ folder is AI-maintained — never edit it manually. If you find errors, fix the source material in raw/ (or add corrective notes) and re-run the AI processing. The system is designed to be regenerative: you can delete the entire wiki/ folder and rebuild it from raw/ at any time. Think of raw/ as your source of truth and wiki/ as a compiled output.</p>

<div class="next-step">
<p><strong>下一篇：</strong> <a href="/en/article/best-ai-tools-2026-free-powerful-practical">The Best AI Tools of 2026: Free, Powerful, and Practical →</a></p>
</div>`,
    contentZh: `<div class="meta-banner">
<p><strong>📅 发布日期：</strong>2026年6月27日 · <strong>🏷️ 分类：</strong>AI教程 · <strong>📊 难度：</strong>初级 · <strong>🛠️ 工具：</strong>Claude Code、Agent Browser</p>
</div>

<p>Karpathy最近关于他AI驱动的个人知识库的推文爆火，两天内获得44K收藏和数百万浏览。关键洞察？他利用AI将零散的笔记和文章组织成可搜索的系统——不需要Notion或Obsidian，只需简单的文件夹结构和文本文件。下面介绍如何构建你自己的，附今天就能实施的实操步骤。</p>

<h2>3文件夹结构：超级简单，完全扁平</h2>

<p>这个系统可以在两分钟内搭建完成，每个文件夹有不同的用途：</p>

<ul>
<li><strong>raw/</strong>：所有未整理原始材料的投放区——文章、截图、笔记等。只管往这里扔，不用担心整理。</li>
<li><strong>wiki/</strong>：AI策划的知识库。AI处理原始材料后在这里写入有组织的内容。永远不要手动编辑这个文件夹。</li>
<li><strong>outputs/</strong>：存储AI生成的答案、报告和分析结果。</li>
</ul>

<pre><code class="language-bash">mkdir my-knowledge-base
cd my-knowledge-base
mkdir raw wiki outputs</code></pre>

<h2>Schema文件：AI的说明书</h2>

<p>Schema文件至关重要，指导AI如何构建和管理你的知识库。在根目录创建 <code>CLAUDE.md</code> 文件：</p>

<pre><code class="language-markdown"># 这是什么
关于[你的主题]的个人知识库。

# 如何组织
- raw/：原始材料，永不修改。
- wiki/：AI维护的有组织内容。
- outputs/：生成的报告和答案。

# Wiki规则
- 每个主题一个.md文件。
- 使用[[主题名]]格式链接相关主题。
- 维护INDEX.md列出所有主要主题。</code></pre>

<p>Karpathy强调这个Schema"超级简单"——只是一个告诉AI规则的文本文件。它直接影响AI策划Wiki的质量，不要跳过这一步。</p>

<h2>一条命令启动AI处理</h2>

<p>文件夹和Schema就绪后，打开Claude Code发出这个提示：</p>

<blockquote>"读取raw/中的所有内容。按照CLAUDE.md中的规则在wiki/中编译Wiki。先创建INDEX.md，然后为每个主要主题创建.md文件。链接相关主题。总结每个部分。"</blockquote>

<p>然后让AI运行——无需监控。完成后，你将得到一个包含按主题组织的文章和便于导航的 <code>INDEX.md</code> 的 <code>wiki</code> 文件夹。</p>

<h2>用agent-browser加速内容收集</h2>

<p>要加速原始材料收集，使用 <code>agent-browser</code>——一个让AI控制真实Chrome浏览器抓取网页内容的工具。它处理JavaScript渲染页面、需登录内容和无限滚动页面，比Playwright MCP等工具节省82%的token。</p>

<pre><code class="language-bash">npm install -g @vercel/agent-browser
agent-browser install
# 使用示例
agent-browser open https://some-article.com
agent-browser get text "article"  # 直接将文本保存到raw/</code></pre>

<h2>今天就开始使用你的知识库</h2>

<p>Karpathy的知识库有44K收藏，但真正的价值来自实际构建和使用它。三个文件夹、一个Schema文件和一个AI工具，你可以在一个周末内搭建并运行自己的系统。选择一个你渴望掌握的主题，把现有的文章和笔记丢进 <code>raw/</code>，让AI完成剩下的工作。</p>

<h2>常见问题</h2>

<h3>必须用Claude Code吗，还是可以用任何AI工具？</h3>
<p>这个系统适用于任何能读取文件和写入磁盘的AI编码代理——Claude Code、Codex、Cursor，甚至带文件访问的ChatGPT。推荐Claude Code是因为它的Agent循环自然处理读取原始文件、组织内容和编写Wiki文章的多步骤过程，无需人工干预。CLAUDE.md Schema文件是为Claude Code命名的，但概念通用——只需将文件名适配到你工具的约定（Codex用AGENTS.md，Cursor用.cursorrules）。</p>

<h3>这与使用Notion或Obsidian有何不同？</h3>
<p>Karpathy的系统刻意更简单：文件夹中的纯Markdown文件，无专有格式，无供应商锁定。你的数据以磁盘文件形式归你所有。AI做你通常在Notion中手动做的组织工作——打标签、链接、总结。这是一个知识的<em>构建</em>系统：投入原始材料，产出有组织的Wiki。Notion和Obsidian是很好的工具，但它们需要你来做组织工作。这个系统让AI处理那部分。</p>

<h3>如果AI在Wiki中犯了错误怎么办？</h3>
<p>wiki/文件夹由AI维护——永远不要手动编辑它。如果发现错误，修复raw/中的源材料（或添加纠正说明）并重新运行AI处理。系统设计为可再生：你可以随时删除整个wiki/文件夹并从raw/重建。把raw/当作你的真相来源，wiki/当作编译输出。</p>

<div class="next-step">
<p><strong>下一篇：</strong> <a href="/zh/article/best-ai-tools-2026-free-powerful-practical">2026年最佳AI工具：免费、强大、实用 →</a></p>
</div>`,
  },

  "best-ai-tools-2026-free-powerful-practical": {
    content: `<div class="meta-banner">
<p><strong>📅 Published:</strong> June 27, 2026 · <strong>🏷️ Category:</strong> AI Comparisons · <strong>📊 Level:</strong> Beginner · <strong>🛠️ Tools:</strong> Gemini, Claude, ChatGPT, Cursor, Codex, NotebookLM, Genspark, Nano Banana Pro</p>
</div>

<p>In 2025, I and many friends in the AI circle spent over $10,000 testing more than 200 AI tools. Finally, we have painstakingly compiled this most detailed ultimate guide to AI tools. Over the past year, the AI circle has been fiercely competitive — many of the magic tools I recommended last year have been surpassed. So in 2026, I will clarify the truly worthwhile AI tools for you according to different scenarios.</p>

<h2>Scene 1: In-Depth Research — Gemini 3.1 Pro</h2>

<p><strong>Gemini 3.1 Pro</strong> is the king of deep research. Its Deep Research feature automatically searches, organizes, and analyzes information, generating complete reports with citations. For example, a financial analysis of AI industry investments in 2025 — it automatically searched 200+ reports and compiled a 30,000-word report in 5 minutes. Context window: 1,000,000 tokens (equivalent to 20 books). Gemini 3.0 is almost completely free.</p>

<h2>Scene 2: Long-Form Writing — Claude 4.6 Opus</h2>

<p><strong>Claude 4.6 Opus</strong> writes the most "un-AI-like" text in terms of fluency, logic, and emotional expression. For a 10,000-word palace drama novel opening, the character shaping and writing style were indistinguishable from human writing. $20/month — worth it for those who make a living from writing.</p>

<h2>Scene 3: Daily Assistant — ChatGPT</h2>

<p><strong>ChatGPT</strong> with GPT-5.4 offers the most comprehensive capabilities with memory that remembers your previous conversations. $20/month. Free alternatives: Doubao, Tongyi Qianwen, DeepSeek.</p>

<h2>Scene 4: AI Image Generation — Nano Banana Pro</h2>

<p><strong>Nano Banana Pro</strong> from Google DeepMind tops all AI image generation rankings. Quality rivals MidJourney, but its killer feature is precise inpainting: upload a photo, specify what to change, and it modifies only that region. Many designers canceled MidJourney after trying it. Free with Google account. Alternatives: Jiemeng/Doubao (ByteDance, high cost-performance), Flux (open-source, runs on 6GB VRAM).</p>

<h2>Scene 5: AI Video — Seedance 2.0</h2>

<p><strong>Seedance 2.0</strong> from ByteDance is the world's strongest AI video model — synchronized sound and picture, movie-level quality, physical laws that can be confused with reality. Alternatives: Conch (natural movement, ~$4-5 per 5-second video), Keling (good consistency for series with fixed characters).</p>

<h2>Scene 6: AI Programming — Cursor / Claude Code / Codex</h2>

<p>The AI programming field has formed a three-giant pattern:</p>

<ul>
<li><strong>Cursor:</strong> No.1 for beginners — understands entire projects through dialogue, like a senior programmer working for you. $20/month.</li>
<li><strong>Claude Code:</strong> More aggressive automation, ideal for medium-to-large projects.</li>
<li><strong>Codex:</strong> OpenAI's terminal — often solves bugs Claude can't. Many veterans use all three: Cursor for daily, Claude Code for projects, Codex for tough bugs.</li>
</ul>

<p>Dark horse: Google's <strong>Antigravity</strong> with large free quota. Domestic: <strong>Trae</strong> ($3 first month, then $10).</p>

<h2>Scene 7: AI Knowledge Base — NotebookLM</h2>

<p><strong>NotebookLM</strong> from Google is the strongest AI knowledge base, bar none. Upload PDFs, web pages, YouTube videos, and audio — it auto-generates summaries, answers questions, and creates remarkably natural AI podcast discussions. Users report 100x efficiency gains. Completely free. Domestic alternative: Tencent's <strong>IMA Knowledge Base</strong> (better Chinese handling, WeChat mini-program integration, team collaboration).</p>

<h2>Scene 8: AI Audio — ElevenLabs</h2>

<p><strong>ElevenLabs</strong> is the ceiling of AI audio — timbre naturalness has reached the level where it can't be distinguished from human speech. Supports voice cloning from a 1-minute recording. ~$35 for one hour of audio. Alternative: Minimax Audio (lots of free quota, dubbing + voice cloning).</p>

<h2>Scene 9: AI Video Editing — Jianying / ChatCut</h2>

<p><strong>Jianying</strong> is no longer just editing software — it's an AI editing family bucket: AI digital humans, AI subtitles, auto video production, one-click background change, AI copy rewriting. Extremely beginner-friendly. <strong>ChatCut</strong> edits videos through natural language chat.</p>

<h2>Scene 10: AI Digital Humans — HeyGen</h2>

<p><strong>HeyGen</strong> remains the best choice for digital human videos — natural effects, multi-language lip sync. Price dropped to $24/month. Ideal for training videos, marketing content, and product introductions on TikTok/Douyin.</p>

<h2>Scene 11: AI Browser — Atlas / Dia / Comet / Sider</h2>

<p><strong>Atlas</strong> from OpenAI directly calls GPT capabilities — browse, summarize, and answer questions in one go. Alternatives: <strong>Dia</strong> or <strong>Comet</strong> (unique UI, free versions). Don't want to switch browsers? Install <strong>Sider</strong> plugin to add AI to Chrome.</p>

<h2>Scene 12: AI Agent — Genspark</h2>

<p><strong>Genspark</strong> is the strongest general-purpose AI Agent — it doesn't just answer questions, it gets things done. Meeting minutes with action items, fact-checking against hallucinations, multi-step task decomposition. Example: "Research the top 10 most profitable overseas companies in 2025 and create a PPT" — 10x faster than manual work. Alternative: <strong>Manus</strong> (pioneer but more expensive).</p>

<h2>The Four Ecosystem Camps of 2026</h2>

<ul>
<li><strong>Google ecosystem:</strong> Gemini, Nano Banana, NotebookLM — most free</li>
<li><strong>OpenAI ecosystem:</strong> ChatGPT 5.4, Atlas, Codex — ChatGPT Pro covers many scenarios</li>
<li><strong>ByteDance ecosystem:</strong> Doubao, Jianying, Jiemeng, Trae — free or ultra-low cost</li>
<li><strong>Alibaba ecosystem:</strong> Open-source LLMs + video models (Tongyi Wanxiang) — zero cost for self-hosters</li>
</ul>

<p><strong>Recommendation:</strong> If budget allows, dual Google + OpenAI support. Budget-limited? ByteDance family bucket. Want extreme savings? Alibaba open-source package.</p>

<h2>常见问题</h2>

<h3>Which single tool gives the most value for $0?</h3>
<p>NotebookLM. It's completely free, has no usage limits, and the productivity gain for research and learning is genuinely 100x for certain tasks. The AI podcast feature alone is worth trying — it turns any document into an engaging audio discussion. For coding, Cursor's free tier is also excellent for beginners.</p>

<h3>Is it worth paying $20/month for multiple AI subscriptions?</h3>
<p>It depends on your use case. For professionals who write daily (Claude Opus), code daily (Cursor), or do heavy research (Gemini), one $20/month subscription easily pays for itself in time savings. But the Google ecosystem (Gemini + Nano Banana + NotebookLM) covers research, images, and knowledge management for free — start there, then add paid tools for specific needs.</p>

<h3>Are domestic Chinese AI tools catching up to Western ones?</h3>
<p>In specific categories, yes. GLM-5.2 is competitive with GPT-5.5 on backend security coding. MiniMax M3 matches GPT-5.5 on 3D and multimodal tasks. ByteDance's Seedance 2.0 leads AI video globally. For general-purpose chat and reasoning, GPT-5.5 and Claude Opus 4.8 still hold an edge, but the gap is narrowing fast — especially considering domestic tools are often free or much cheaper.</p>

<div class="next-step">
<p><strong>Previous:</strong> <a href="/en/article/karpathy-ai-knowledge-base-3-folders">Build a Karpathy-Style AI Knowledge Base: A 2-Minute Setup with Just 3 Folders ←</a></p>
</div>`,
    contentZh: `<div class="meta-banner">
<p><strong>📅 发布日期：</strong>2026年6月27日 · <strong>🏷️ 分类：</strong>AI对比 · <strong>📊 难度：</strong>初级 · <strong>🛠️ 工具：</strong>Gemini、Claude、ChatGPT、Cursor、Codex、NotebookLM、Genspark、Nano Banana Pro</p>
</div>

<p>2025年，我和AI圈的很多朋友花了超过1万美元测试了200多款AI工具。终于，我们精心整理了这份最详细的AI工具终极指南。过去一年AI圈竞争激烈——我去年推荐的许多神器已被新工具超越。所以在2026年，我将根据不同场景为你明确真正值得的AI神器。</p>

<h2>场景1：深度研究——Gemini 3.1 Pro</h2>

<p><strong>Gemini 3.1 Pro</strong> 是深度研究之王。其Deep Research功能自动帮你搜索、整理和分析信息，生成带引用的完整报告。例如，做2025年AI行业投资财务分析——它自动搜索200+份报告，5分钟编出3万字报告。上下文窗口100万tokens（相当于一次读20本书）。Gemini 3.0几乎完全免费。</p>

<h2>场景2：长文写作——Claude 4.6 Opus</h2>

<p><strong>Claude 4.6 Opus</strong> 写出的文字在流畅度、逻辑和情感表达上最"不像AI"。一篇万字宫廷小说开头，人物塑造和文风完全不像AI写的。$20/月——对靠写作为生的人绝对值得。</p>

<h2>场景3：日常助手——ChatGPT</h2>

<p><strong>ChatGPT</strong> 搭载GPT-5.4，能力最全面，记忆功能记住你之前聊过的内容。$20/月。免费替代：豆包、通义千问、DeepSeek。</p>

<h2>场景4：AI图像生成——Nano Banana Pro</h2>

<p><strong>Nano Banana Pro</strong> 来自Google DeepMind，登顶各类AI图像生成排行榜。画质媲美MidJourney，但杀手级功能是精准局部编辑：上传照片指定修改区域，只改那里其他不变。许多设计师试用后取消了MidJourney订阅。Google账号免费。替代：即梦/豆包（字节跳动，高性价比）、Flux（开源，6GB显存本地运行）。</p>

<h2>场景5：AI视频——Seedance 2.0</h2>

<p><strong>Seedance 2.0</strong> 来自字节跳动，全球最强AI视频模型——声画同步、电影级画质、物理规律可与真实混淆。替代：海螺（动作自然，~$4-5/5秒视频）、可灵（一致性好，适合固定角色系列内容）。</p>

<h2>场景6：AI编程——Cursor / Claude Code / Codex</h2>

<p>AI编程领域已形成三巨头格局：</p>

<ul>
<li><strong>Cursor：</strong> 新手首选——通过对话理解整个项目，像高级程序员为你工作。$20/月。</li>
<li><strong>Claude Code：</strong> 自动化更激进，适合中大型项目。</li>
<li><strong>Codex：</strong> OpenAI的终端——常能解决Claude搞不定的Bug。老手三件套：Cursor日常、Claude Code项目、Codex啃硬骨头。</li>
</ul>

<p>黑马：Google <strong>Antigravity</strong>（大量免费额度）。国内：<strong>Trae</strong>（首月$3，后续$10）。</p>

<h2>场景7：AI知识库——NotebookLM</h2>

<p><strong>NotebookLM</strong> 来自Google，最强AI知识库，没有之一。上传PDF、网页、YouTube视频和音频——自动生成摘要、回答问题、创建非常自然的AI播客讨论。用户报告效率提升100倍。完全免费。国内替代：腾讯<strong>IMA知识库</strong>（中文处理更好、微信小程序集成、支持团队协作）。</p>

<h2>场景8：AI音频——ElevenLabs</h2>

<p><strong>ElevenLabs</strong> 是AI音频天花板——音色自然度已达到听不出是AI的水平。支持1分钟录音克隆任何人声音。约$35生成一小时音频。替代：Minimax Audio（大量免费额度，配音+声音克隆）。</p>

<h2>场景9：AI视频剪辑——剪映 / ChatCut</h2>

<p><strong>剪映</strong> 已不只是传统剪辑软件——AI剪辑全家桶：AI数字人、AI字幕、AI自动视频制作、一键换背景、AI文案改写。对新手极其友好。<strong>ChatCut</strong> 通过自然语言聊天剪辑视频。</p>

<h2>场景10：AI数字人——HeyGen</h2>

<p><strong>HeyGen</strong> 仍是数字人视频最佳选择——效果自然、支持多语言唇形同步。价格降至$24/月。适合TikTok/抖音培训视频、营销内容和产品介绍。</p>

<h2>场景11：AI浏览器——Atlas / Dia / Comet / Sider</h2>

<p><strong>Atlas</strong> 来自OpenAI，直接调用GPT能力——浏览、总结、问答一气呵成。替代：<strong>Dia</strong>或<strong>Comet</strong>（独特UI，有免费版）。不想换浏览器？安装<strong>Sider</strong>插件给Chrome加AI。</p>

<h2>场景12：AI Agent——Genspark</h2>

<p><strong>Genspark</strong> 是最强通用AI Agent——不只会回答问题，而是真正帮你把事情做成。会议纪要带行动项、事实核查防幻觉、多步骤任务分解。示例："调研2025年海外最赚钱的10家公司并制作PPT"——比手动快10倍。替代：<strong>Manus</strong>（先驱但更贵）。</p>

<h2>2026年四大生态阵营</h2>

<ul>
<li><strong>Google生态：</strong>Gemini、Nano Banana、NotebookLM——大多免费</li>
<li><strong>OpenAI生态：</strong>ChatGPT 5.4、Atlas、Codex——ChatGPT Pro覆盖多场景</li>
<li><strong>字节生态：</strong>豆包、剪映、即梦、Trae——免费或超低价</li>
<li><strong>阿里生态：</strong>开源大模型+视频模型（通义万相）——自部署零成本</li>
</ul>

<p><strong>建议：</strong>预算充足双持Google+OpenAI。预算有限字节全家桶。极致省钱阿里开源包。</p>

<h2>常见问题</h2>

<h3>哪款工具零成本价值最高？</h3>
<p>NotebookLM。完全免费、无使用限制，研究和学习的生产力提升对某些任务确实达100倍。单是AI播客功能就值得一试——它把任何文档变成引人入胜的音频讨论。编程方面，Cursor免费版对初学者也很优秀。</p>

<h3>值得每月花$20订阅多个AI吗？</h3>
<p>取决于你的用例。对于每天写作（Claude Opus）、每天编码（Cursor）或做深度研究（Gemini）的专业人士，一个月$20的订阅在时间节省上轻松回本。但Google生态（Gemini+Nano Banana+NotebookLM）免费覆盖研究、图像和知识管理——从那里开始，再按需添加付费工具。</p>

<h3>国产AI工具赶上西方了吗？</h3>
<p>在特定类别，是的。GLM-5.2在后端安全编码上与GPT-5.5有竞争力。MiniMax M3在3D和多模态任务上匹敌GPT-5.5。字节的Seedance 2.0在全球AI视频领域领先。通用聊天和推理方面，GPT-5.5和Claude Opus 4.8仍占优势，但差距正在快速缩小——尤其考虑到国产工具通常免费或便宜得多。</p>

<div class="next-step">
<p><strong>上一篇：</strong> <a href="/zh/article/karpathy-ai-knowledge-base-3-folders">构建Karpathy风格的AI知识库：3个文件夹2分钟搭建 ←</a></p>
</div>`,
  },

'''

last_brace = content_src.rfind('};')
content_new = content_src[:last_brace] + new_contents + '};'

with open('src/lib/article-content.ts', 'w', encoding='utf-8') as f:
    f.write(content_new)

print('Part 3: 2 article contents added to article-content.ts')

print('\n=== All done! Run build to verify ===')
