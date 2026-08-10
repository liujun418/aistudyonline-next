export interface Article {
  slug: string;
  title: string;
  titleZh: string;
  description: string;
  descriptionZh: string;
  category: string;
  tags: string[];
  difficulty: "beginner" | "intermediate" | "advanced";
  toolsMentioned: string[];
  date: string;
}

export const articles: Article[] = [

  {
    slug: "claude-code-install-setup",
    title: "Claude Code Installation & Setup: From Zero to Your First AI-Generated Web Page",
    titleZh: "Claude Code安装与配置：从零开始到你的第一个AI网页",
    description:
      "Step-by-step guide to installing Claude Code on Windows, Mac, or Linux — with copyable commands, API key setup, and your first AI-generated project.",
    descriptionZh:
      "在Windows、Mac或Linux上安装Claude Code的逐步指南——包含可复制的命令、API密钥设置和你的第一个AI生成项目。",
    category: "ai-tutorials",
    tags: ["claude-code", "installation", "setup", "command-line", "coding", "beginner"],
    difficulty: "beginner",
    toolsMentioned: ["claude"],
    date: "2026-05-22",
  },

  {
    slug: "llms-in-plain-english",
    title: "I Keep Hearing About 'LLMs' — What They Actually Are in Plain English",
    titleZh: "我总听到“LLM”——它们到底是什么？（通俗版）",
    description:
      "Everyone says 'large language model' like you should know what it means. Here's the actually-simple explanation, with zero technical jargon.",
    descriptionZh:
      "每个人都在说‘大语言模型’，好像你应该知道它是什么意思。这里有一个真正简单的解释，没有任何技术术语。",
    category: "ai-basics",
    tags: ["llm", "explained", "non-technical", "fundamentals"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt", "claude"],
    date: "2026-05-22",
  },

  {
    slug: "ai-hallucinations-explained-with-examples",
    title: "AI Hallucinations Explained: Why ChatGPT Makes Stuff Up (With Real Examples)",
    titleZh: "AI幻觉解释：为什么ChatGPT会编造内容（附真实例子）",
    description:
      "You asked for a recipe and it invented an ingredient that doesn't exist. Here's why AI hallucinates, how to spot it, and what to do when it happens.",
    descriptionZh:
      "你要了一个食谱，它却发明了一个不存在的食材。这是为什么AI会幻觉，如何发现它，以及遇到时该怎么办。",
    category: "ai-basics",
    tags: ["hallucinations", "chatgpt", "accuracy", "beginner"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt", "claude", "perplexity"],
    date: "2026-05-20",
  },

  {
    slug: "how-to-choose-right-ai-tool",
    title: "Which AI Tool Should You Use? A Decision Framework for Beginners",
    titleZh: "你应该使用哪个AI工具？初学者的决策框架",
    description:
      "ChatGPT vs Claude vs Gemini vs Perplexity vs Midjourney — which one do you actually need? A practical decision matrix based on what you're trying to do.",
    descriptionZh:
      "ChatGPT vs Claude vs Gemini vs Perplexity vs Midjourney——你真正需要哪一个？一个基于你的实际需求的实用决策矩阵。",
    category: "ai-basics",
    tags: ["comparison", "tools", "chatgpt", "claude", "gemini", "perplexity", "midjourney", "beginner"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt", "claude", "gemini", "perplexity", "midjourney"],
    date: "2026-05-22",
  },

  {
    slug: "free-vs-paid-ai-tools-worth-it",
    title: "Free vs Paid AI Tools: When It's Actually Worth Paying (and When It's Not)",
    titleZh: "免费vs付费AI工具：何时值得付费（何时不值得）",
    description:
      "ChatGPT Plus is $20/month. Claude Pro is $20/month. Midjourney is $10. Do you need any of them? Here's how to decide, based on what you actually use AI for.",
    descriptionZh:
      "ChatGPT Plus每月0。Claude Pro每月0。Midjourney每月0。你真的需要它们吗？以下是如何基于你对AI的实际使用情况来决定。",
    category: "ai-basics",
    tags: ["pricing", "free-vs-paid", "chatgpt", "value", "guide"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt", "claude", "midjourney", "gemini", "perplexity"],
    date: "2026-05-18",
  },

  {
    slug: "what-is-a-gpu-non-techie",
    title: "What's a GPU and Why Does AI Need It? A Non-Techie Explanation",
    titleZh: "什么是GPU？AI为什么需要它？非技术人员的解释",
    description:
      "NVIDIA is suddenly worth more than Google because of 'AI chips.' Here's what a GPU actually does, why AI needs thousands of them, and why you should care.",
    descriptionZh:
      "NVIDIA突然比Google还值钱了——因为‘AI芯片’。这是GPU实际做的事情，为什么AI需要成千上万个GPU，以及你为什么应该关心。",
    category: "ai-basics",
    tags: ["gpu", "nvidia", "hardware", "explained", "non-technical"],
    difficulty: "beginner",
    toolsMentioned: [],
    date: "2026-05-16",
  },

  {
    slug: "ai-myths-people-still-believe",
    title: "5 AI Myths Your Non-Techie Friends Still Believe (and What's Actually True)",
    titleZh: "你的非技术朋友仍然相信的5个AI迷思（以及真相是什么）",
    description:
      "\"AI is conscious.\" \"AI will take all jobs.\" \"AI knows everything.\" None of these are true. Here's what the reality looks like in 2026.",
    descriptionZh:
      "“AI有意识。”“AI会取代所有工作。”“AI什么都知道。”这些都不是真的。以下是2026年的真实情况。",
    category: "ai-basics",
    tags: ["myths", "misconceptions", "explained", "beginner"],
    difficulty: "beginner",
    toolsMentioned: [],
    date: "2026-05-14",
  },

  {
    slug: "chatgpt-voice-mode-job-interview",
    title: "ChatGPT Fundamentals: Interface, Settings, and Your First 10 Prompts",
    titleZh: "ChatGPT基础：界面、设置和你的前10个提示词",
    description:
      "New to ChatGPT? Here is the complete beginner's guide — account setup, interface tour, settings to configure, and 10 starter prompts to get real value from day one.",
    descriptionZh:
      "ChatGPT新手？这里有完整的初学者指南——账户设置、界面导览、需要配置的设置，以及10个入门提示词让你从第一天就获得真正价值。",
    category: "ai-tutorials",
    tags: ["chatgpt", "beginner", "fundamentals", "prompts", "getting-started"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt"],
    date: "2026-05-22",
  },

  {
    slug: "claude-projects-organize-chats",
    title: "How to Write Prompts That Actually Work: The 5-Point Framework",
    titleZh: "如何写出真正有效的提示词：5点框架",
    description:
      "Vague prompts get mediocre answers. Master the 5-Point Prompt Framework — Role, Context, Task, Format, Constraints — and get dramatically better results from any AI tool.",
    descriptionZh:
      "模糊的提示词只能得到平庸的回答。掌握5点提示框架——角色、上下文、任务、格式、约束——从任何AI工具中获得显著更好的结果。",
    category: "ai-tutorials",
    tags: ["prompts", "prompt-engineering", "framework", "writing", "chatgpt"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt", "claude"],
    date: "2026-05-22",
  },

  {
    slug: "ai-images-that-dont-look-like-ai",
    title: "ChatGPT for Writing: Emails, Reports, and Creative Projects",
    titleZh: "ChatGPT写作：邮件、报告和创意项目",
    description:
      "Move beyond basic prompts. Master AI writing with tone control, outline-first reports, creative techniques, and editing workflows that produce professional-grade content.",
    descriptionZh:
      "超越基础提示词。掌握语气控制、先写大纲的报告、创意技巧和编辑工作流程，产出专业级内容。",
    category: "ai-tutorials",
    tags: ["chatgpt", "writing", "email", "content", "editing"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt"],
    date: "2026-05-22",
  },

  {
    slug: "voice-recording-to-meeting-notes-free",
    title: "ChatGPT for Research and Analysis: Web Search, File Upload, and Data",
    titleZh: "ChatGPT研究与分析：网页搜索、文件上传和数据处理",
    description:
      "ChatGPT is more than a chatbot. Use it for web search, document analysis, data processing with Advanced Data Analysis, and long-form research — all in one place.",
    descriptionZh:
      "ChatGPT不仅仅是聊天机器人。用它进行网页搜索、文档分析、高级数据分析处理和研究——都在一个地方。",
    category: "ai-tutorials",
    tags: ["chatgpt", "research", "file-upload", "data-analysis", "web-search"],
    difficulty: "intermediate",
    toolsMentioned: ["chatgpt"],
    date: "2026-05-22",
  },

  {
    slug: "first-ai-coding-project-no-experience",
    title: "Custom GPTs and Automation: Build Your Own AI Assistant",
    titleZh: "自定义GPT和自动化：构建你自己的AI助手",
    description:
      "Create custom versions of ChatGPT for your specific needs. Learn to build, configure with knowledge files, and share GPTs — no coding required.",
    descriptionZh:
      "为你的特定需求创建ChatGPT的自定义版本。学习构建、配置知识文件并分享GPT——无需编程。",
    category: "ai-tutorials",
    tags: ["chatgpt", "custom-gpts", "automation", "gpt-store", "no-code"],
    difficulty: "intermediate",
    toolsMentioned: ["chatgpt"],
    date: "2026-05-22",
  },

  {
    slug: "etsy-seller-ai-product-descriptions",
    title: "AI for Business Communication: Emails, Proposals, and Client Outreach",
    titleZh: "AI商务沟通：邮件、提案和客户拓展",
    description:
      "Professional communication takes hours each day. Use AI to draft emails, proposals, pitches, and product descriptions faster while maintaining your professional tone.",
    descriptionZh:
      "专业沟通每天需要数小时。使用AI更快地起草邮件、提案和产品描述，同时保持专业语气。",
    category: "ai-use-cases",
    tags: ["business", "communication", "email", "proposals", "productivity"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt", "claude"],
    date: "2026-05-22",
  },

  {
    slug: "ai-wedding-planning-free-tools",
    title: "AI for Project Planning and Organization: From Timelines to Budgets",
    titleZh: "AI项目规划与组织：从时间线到预算",
    description:
      "AI excels at structured planning. Use it for timelines, budgets, task breakdowns, decision matrices, and status reports — whether for work projects or personal events.",
    descriptionZh:
      "AI擅长结构化规划。用它来做时间线、预算、任务分解、决策矩阵和状态报告——无论是工作项目还是个人事务。",
    category: "ai-use-cases",
    tags: ["planning", "project-management", "timeline", "budget", "productivity"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt", "claude"],
    date: "2026-05-22",
  },

  {
    slug: "ai-travel-itinerary-real-prompts",
    title: "AI for Research and Report Writing: Find, Analyze, and Summarize",
    titleZh: "AI研究与报告写作：查找、分析和总结",
    description:
      "Accelerate your research workflow with AI. Plan your approach, analyze sources, interpret data, and write reports — with prompting techniques that produce reliable results.",
    descriptionZh:
      "用AI加速你的研究流程。规划方法、分析来源、解释数据并撰写报告——使用产生可靠结果的提示技巧。",
    category: "ai-use-cases",
    tags: ["research", "report-writing", "analysis", "productivity", "data"],
    difficulty: "intermediate",
    toolsMentioned: ["chatgpt", "perplexity"],
    date: "2026-05-22",
  },

  {
    slug: "learn-english-with-ai-free-speaking-practice",
    title: "AI for Learning and Skill Development: Language, Tech, and More",
    titleZh: "AI学习与技能发展：语言、技术等",
    description:
      "AI is the most powerful self-education tool ever created. Use it for language practice with voice mode, interview prep, concept learning, and certification study.",
    descriptionZh:
      "AI是有史以来最强大的自学工具。用它进行语音模式语言练习、面试准备、概念学习和认证考试学习。",
    category: "ai-use-cases",
    tags: ["learning", "education", "language", "skills", "voice-mode"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt", "claude"],
    date: "2026-05-22",
  },

  {
    slug: "ai-for-parents-quiet-moments",
    title: "AI for Parents: 7 Ways to Use ChatGPT When You Have 10 Minutes of Quiet",
    titleZh: "AI家长指南：当你有10分钟安静时间时的7种ChatGPT用法",
    description:
      "Kids are finally asleep. You've got 10 minutes. Here are 7 actually-useful things to do with AI — meal plan the week, draft a permission slip, plan a birthday party.",
    descriptionZh:
      "孩子终于睡着了。你有10分钟时间。以下是7件用AI做的实用事情——规划一周菜单、起草请假条、计划生日派对。",
    category: "ai-use-cases",
    tags: ["parents", "busy-lifestyle", "quick-tips", "practical", "life-hacks"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt", "claude"],
    date: "2026-05-12",
  },

  {
    slug: "free-ai-image-generators-same-prompt-test",
    title: "Midjourney Basics: Getting Started with AI Image Creation",
    titleZh: "Midjourney基础：AI图像创作入门",
    description:
      "Midjourney produces the highest-quality AI images, but it requires Discord. Here is how to set up, write your first /imagine prompt, and master essential parameters.",
    descriptionZh:
      "Midjourney能生成最高质量的AI图像，但需要Discord。以下是如何设置、编写你的第一个/imagine提示词以及掌握关键参数。",
    category: "ai-comparisons",
    tags: ["midjourney", "image-generation", "tutorial", "discord", "beginner"],
    difficulty: "beginner",
    toolsMentioned: ["midjourney"],
    date: "2026-05-22",
  },

  {
    slug: "chatgpt-free-vs-plus-2026-what-you-get",
    title: "ChatGPT Free vs Plus in 2026: What You Actually Get Without Paying",
    titleZh: "2026年ChatGPT免费版vs Plus版：你不付费实际能获得什么",
    description:
      "OpenAI keeps changing what's free and what's not. Here's the updated 2026 breakdown: image generation limits, message caps, GPT-5 access, and which paid features are now free.",
    descriptionZh:
      "OpenAI不断改变免费和付费的边界。这里是2026年最新解析：图像生成限制、消息上限、GPT-5访问权限，以及哪些付费功能现在免费了。",
    category: "ai-comparisons",
    tags: ["chatgpt", "free-vs-paid", "pricing", "2026", "updated"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt"],
    date: "2026-05-17",
  },

  {
    slug: "notebooklm-vs-perplexity-research",
    title: "NotebookLM vs Perplexity: Which Is Better for Researching a Topic From Scratch?",
    titleZh: "NotebookLM vs Perplexity：从零研究一个主题哪个更好？",
    description:
      "Both claim to help you research, but they work completely differently. I used both to research the same topic and compared notes — here's which one actually saved me time.",
    descriptionZh:
      "两者都声称能帮助你研究，但它们的工作方式完全不同。我用两者研究了同一个主题并对比了结果——这是哪个真正节省了我的时间。",
    category: "ai-comparisons",
    tags: ["notebooklm", "perplexity", "research", "productivity", "side-by-side"],
    difficulty: "intermediate",
    toolsMentioned: ["perplexity"],
    date: "2026-05-15",
  },

  {
    slug: "claude-vs-chatgpt-writing-blind-test",
    title: "Claude's Writing Style vs ChatGPT: We Asked 10 People Which Sounds More Human",
    titleZh: "Claude vs ChatGPT写作风格：我们问了10个人哪个听起来更像人",
    description:
      "We generated the same content with both AIs, removed the labels, and asked 10 regular people to pick which version they preferred. The results weren't even close.",
    descriptionZh:
      "我们用两个AI生成了相同的内容，去掉标签，问了10个普通人他们更喜欢哪个版本。结果差距很大。",
    category: "ai-comparisons",
    tags: ["claude", "chatgpt", "writing", "blind-test", "real-people"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt", "claude"],
    date: "2026-05-13",
  },

  {
    slug: "cursor-vs-copilot-complete-beginner",
    title: "Cursor vs GitHub Copilot for a Complete Beginner: Which One Is Less Confusing?",
    titleZh: "Cursor vs GitHub Copilot：对于完全初学者哪个不那么令人困惑？",
    description:
      "You've never coded before. Both tools promise AI-powered coding, but one has a much gentler learning curve. Here's what each looks like on day one — no experience assumed.",
    descriptionZh:
      "你从未编过程。两个工具都承诺AI辅助编程，但一个的学习曲线要平缓得多。以下是每个工具在第一天看起来的样子——无需任何编程经验。",
    category: "ai-comparisons",
    tags: ["cursor", "copilot", "coding", "beginner", "learning-curve"],
    difficulty: "beginner",
    toolsMentioned: ["cursor", "github-copilot"],
    date: "2026-05-11",
  },

  {
    slug: "gpt5-for-regular-users",
    title: "GPT-5: What's Actually New and What It Means for Regular Users (Not Developers)",
    titleZh: "GPT-5：真正的新功能以及对普通用户意味着什么（非开发者）",
    description:
      "Every GPT-5 article is written for developers. This one isn't. Here's what's actually changed for normal people: better writing, fewer mistakes, and one feature you'll actually use daily.",
    descriptionZh:
      "每篇关于GPT-5的文章都是写给开发者看的。这一篇不是。以下是真正为普通人改变的事情：更好的写作、更少的错误，以及一个你每天都会使用的功能。",
    category: "ai-news",
    tags: ["gpt5", "openai", "update", "for-beginners", "whats-new"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt"],
    date: "2026-05-21",
  },

  {
    slug: "open-source-ai-models-run-on-laptop",
    title: "Open Source AI Models in 2026: Which Ones You Can Actually Run on Your Laptop",
    titleZh: "2026年开源AI模型：哪些可以在你的笔记本上运行",
    description:
      "\"Open source AI\" sounds great until you realize most models need a $10,000 GPU. Here are 4 open models that actually run on a normal laptop — and what they're good for.",
    descriptionZh:
      "“开源AI”听起来很棒，直到你意识到大多数模型需要一台价值0,000的GPU。这里有4个真正能在普通笔记本上运行的开源模型——以及它们适合做什么。",
    category: "ai-news",
    tags: ["open-source", "local-ai", "laptop", "free", "models"],
    difficulty: "intermediate",
    toolsMentioned: ["deepseek"],
    date: "2026-05-19",
  },

  {
    slug: "eu-ai-act-plain-english",
    title: "EU AI Act in Plain English: What It Means for the Tools You Use Every Day",
    titleZh: "通俗解释欧盟AI法案：对你日常使用的工具意味着什么",
    description:
      "The EU just passed rules that affect every AI tool you use. No legalese — here's what's banned, what requires a label, and how it changes ChatGPT, Midjourney, and the rest.",
    descriptionZh:
      "欧盟刚刚通过了影响你使用的每个AI工具的法规。没有法律术语——这是被禁止的内容、需要标注的内容，以及它如何改变ChatGPT、Midjourney等。",
    category: "ai-news",
    tags: ["eu-ai-act", "regulation", "explained", "plain-english", "policy"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt", "midjourney", "claude"],
    date: "2026-05-17",
  },

  {
    slug: "ai-jobs-that-didnt-exist-3-years-ago",
    title: "AI Jobs That Didn't Exist 3 Years Ago (and How Much They Pay)",
    titleZh: "3年前不存在的AI工作（及其薪资水平）",
    description:
      "\"Prompt engineer\" isn't the only one. There's AI safety officer, AI content editor, AI workflow consultant. Here's what these jobs actually do, what they pay, and how to get started.",
    descriptionZh:
      "“提示工程师”不是唯一的新工作。还有AI安全官、AI内容编辑、AI工作流顾问。以下是这些工作实际做什么、薪资水平以及如何入门。",
    category: "ai-news",
    tags: ["jobs", "career", "salary", "new-roles", "trends"],
    difficulty: "beginner",
    toolsMentioned: [],
    date: "2026-05-15",
  },

  {
    slug: "apple-intelligence-6-months-later",
    title: "Apple Intelligence 6 Months Later: Which Features Actually Made It to Your iPhone",
    titleZh: "Apple Intelligence六个月后：哪些功能真正到了你的iPhone上",
    description:
      "Apple announced a lot at WWDC. Half of it shipped late, some of it still says 'coming soon.' Here's what's actually working on your iPhone right now — and what's still vaporware.",
    descriptionZh:
      "Apple在WWDC上宣布了很多。一半推迟发布，有些仍然显示“即将推出”。以下是你的iPhone上现在真正能用的——以及哪些仍然是空头支票。",
    category: "ai-news",
    tags: ["apple", "intelligence", "iphone", "ios", "features"],
    difficulty: "beginner",
    toolsMentioned: [],
    date: "2026-05-13",
  },

  {
    slug: "google-io-2026-93-ai-agents",
    title: "Google I/O 2026: 93 AI Agents Built an OS in 12 Hours — Here's What It Means",
    titleZh: "Google I/O 2026：93个AI代理12小时协作构建操作系统——这意味着什么",
    description:
      "At Google I/O 2026, 93 AI agents collaborated autonomously to build a working OS from scratch. Here's what happened, why it matters, and how it changes the AI landscape.",
    descriptionZh:
      "在Google I/O 2026上，93个AI代理自主协作，从零构建了一个可运行的操作系统。发生了什么、为什么重要、以及它如何改变AI格局。",
    category: "ai-news",
    tags: ["google-io", "ai-agents", "gemini", "google", "collaboration", "2026"],
    difficulty: "beginner",
    toolsMentioned: ["gemini"],
    date: "2026-05-22",
  },

  {
    slug: "claude-code-mcp-configuration",
    title: "Configure MCP Servers in Claude Code: File Access, APIs, and Databases",
    titleZh: "在Claude Code中配置MCP服务器：文件访问、API和数据库",
    description:
      "Extend Claude Code's capabilities with MCP (Model Context Protocol) servers. Learn to configure file system access, API integration, and database connections.",
    descriptionZh:
      "用MCP（模型上下文协议）服务器扩展Claude Code的能力。了解如何配置文件系统访问、API集成和数据库连接。",
    category: "ai-tutorials",
    tags: ["claude-code", "mcp", "configuration", "servers", "tools"],
    difficulty: "intermediate",
    toolsMentioned: ["claude"],
    date: "2026-05-22",
  },

  {
    slug: "claude-code-in-action",
    title: "Claude Code in Action: Build a Real Project from Scratch",
    titleZh: "Claude Code实战：从零构建一个真实项目",
    description:
      "Watch Claude Code build a complete web application from a single prompt. See the full workflow — planning, coding, debugging, and deployment.",
    descriptionZh:
      "观察Claude Code从一个提示词构建完整的Web应用程序。看完整工作流程——规划、编码、调试和部署。",
    category: "ai-tutorials",
    tags: ["claude-code", "project", "web-development", "workflow"],
    difficulty: "intermediate",
    toolsMentioned: ["claude"],
    date: "2026-05-22",
  },

  {
    slug: "claude-code-advanced",
    title: "Advanced Claude Code: Custom Slash Commands, Hooks, and CI/CD Integration",
    titleZh: "高级Claude Code：自定义Slash命令、Hooks和CI/CD集成",
    description:
      "Take Claude Code to production. Build custom slash commands, pre-commit hooks for code quality, and integrate with your CI/CD pipeline.",
    descriptionZh:
      "将Claude Code用于生产环境。构建自定义Slash命令、代码质量的pre-commit hooks，以及与CI/CD管道的集成。",
    category: "ai-tutorials",
    tags: ["claude-code", "advanced", "hooks", "ci-cd", "custom-commands"],
    difficulty: "advanced",
    toolsMentioned: ["claude"],
    date: "2026-05-22",
  },

  {
    slug: "claude-code-top-7-skills",
    title: "Claude Code's Top 7 Skills: A Complete Guide to the Most Powerful Extensions",
    titleZh: "Claude Code 七大技能：最强扩展完整指南",
    description:
      "Explore the 7 must-install skills for Claude Code — from document processing and frontend design to skill creation and debugging — that transform it into a truly proficient AI teammate.",
    descriptionZh:
      "探索Claude Code的7个必装技能——从文档处理、前端设计到技能创建和调试——将其转变为真正娴熟的AI队友。",
    category: "ai-tutorials",
    tags: ["claude-code", "skills", "extensions", "productivity", "coding"],
    difficulty: "intermediate",
    toolsMentioned: ["claude", "cursor"],
    date: "2026-05-22",
  },

  {
    slug: "ai-image-dalle-firefly",
    title: "DALL-E vs Firefly vs Midjourney: Which AI Image Generator Should You Use?",
    titleZh: "DALL-E vs Firefly vs Midjourney：你应该使用哪个AI图像生成器？",
    description:
      "Compare the three leading AI image generators head-to-head. See real outputs, pricing, and use cases to decide which one fits your workflow.",
    descriptionZh:
      "让三大AI图像生成器正面交锋。看实际输出、价格和使用场景，决定哪个适合你的工作流程。",
    category: "ai-tutorials",
    tags: ["ai-image", "dalle3", "adobe-firefly", "midjourney", "comparison"],
    difficulty: "beginner",
    toolsMentioned: ["dalle3", "midjourney", "adobe-firefly"],
    date: "2026-05-22",
  },

  {
    slug: "ai-image-prompt-guide",
    title: "The Ultimate AI Image Prompt Guide: Techniques That Actually Work",
    titleZh: "终极AI图像提示指南：真正有效的技巧",
    description:
      "Go beyond 'a cat in space.' Learn professional prompt techniques — style references, lighting specs, composition rules, and negative prompts that deliver stunning results.",
    descriptionZh:
      "超越“太空中的猫”。学习专业提示技巧——风格参考、灯光规格、构图规则和负面提示——产出惊艳效果。",
    category: "ai-tutorials",
    tags: ["ai-image", "prompts", "prompt-engineering", "techniques", "guide"],
    difficulty: "intermediate",
    toolsMentioned: ["dalle3", "midjourney", "adobe-firefly", "stable-diffusion"],
    date: "2026-05-22",
  },

  {
    slug: "ai-image-commercial-licensing",
    title: "AI Image Copyright and Commercial Licensing: What You Can and Can't Sell",
    titleZh: "AI图像版权和商业许可：你可以卖什么，不能卖什么",
    description:
      "Navigate the legal landscape of AI-generated images. Understand copyright rules, commercial licenses, and platform-specific terms for DALL-E, Firefly, and Midjourney.",
    descriptionZh:
      "了解AI生成图像的法律环境。理解版权规则、商业许可和DALL-E、Firefly、Midjourney的平台特定条款。",
    category: "ai-tutorials",
    tags: ["ai-image", "copyright", "licensing", "commercial", "legal"],
    difficulty: "beginner",
    toolsMentioned: ["dalle3", "midjourney", "adobe-firefly"],
    date: "2026-05-22",
  },

  {
    slug: "12-core-ai-concepts-guide",
    title: "Master 12 Core Concepts of AI Large Models in One Guide",
    titleZh: "一篇文章掌握AI大模型12个核心概念",
    description:
      "From model parameters and context windows to RAG and embodied intelligence — this guide breaks down 12 essential AI concepts in plain language with real-world examples.",
    descriptionZh:
      "从模型参数、上下文窗口到RAG和具身智能——本文用通俗语言和真实例子解释12个AI必备概念。",
    category: "ai-basics",
    tags: ["llm", "concepts", "parameters", "token", "rag", "agent", "quantization", "guide"],
    difficulty: "beginner",
    toolsMentioned: ["deepseek", "chatgpt", "claude"],
    date: "2026-05-22",
  },

  {
    slug: "openclaw-demystified-20-lines",
    title: "Unveiling OpenClaw: Demystify the AI Tool in 20 Lines of Code",
    titleZh: "揭开OpenClaw面纱：20行代码讲透这个AI工具",
    description:
      "OpenClaw (aka Lobster) isn't magic — it's an agent loop + LLM + prompt instructions. Here's exactly how it works, with code you can run yourself.",
    descriptionZh:
      "OpenClaw（又名Lobster）不是魔法——它是代理循环+LLM+提示指令的组合。这里用可运行的代码精确解释其工作原理。",
    category: "ai-tutorials",
    tags: ["openclaw", "agent", "llm", "automation", "tutorial", "open-source"],
    difficulty: "intermediate",
    toolsMentioned: ["openclaw", "openrouter", "claude", "chatgpt"],
    date: "2026-05-22",
  },

  {
    slug: "llm-service-packages-review-2026",
    title: "LLM Service Packages Review: From Premium to Disappointing",
    titleZh: "LLM服务套餐评测：从物超所值到令人失望",
    description:
      "A critical comparison of domestic and international LLM service packages — analyzing pricing, features, and hidden pitfalls of OpenAI, Anthropic, Google, and domestic providers.",
    descriptionZh:
      "国内外LLM服务套餐的深度对比评测——分析OpenAI、Anthropic、Google及国内厂商的定价、功能和隐藏陷阱。",
    category: "ai-comparisons",
    tags: ["llm", "pricing", "comparison", "openai", "anthropic", "google"],
    difficulty: "intermediate",
    toolsMentioned: ["chatgpt", "claude", "gemini", "deepseek"],
    date: "2026-05-22",
  },

  {
    slug: "claude-code-browser-automation",
    title: "Efficient Browser Control with Claude Code: Minimize Token Consumption",
    titleZh: "用Claude Code高效操控浏览器：最小化Token消耗",
    description:
      "Learn how to control web browsers through Claude Code with token-saving strategies — page navigation, data capture, screenshots, and cross-page workflows.",
    descriptionZh:
      "学习如何通过Claude Code操控浏览器并节省Token——页面导航、数据抓取、截图和跨页面工作流。",
    category: "ai-tutorials",
    tags: ["claude-code", "browser", "automation", "token-optimization", "productivity"],
    difficulty: "intermediate",
    toolsMentioned: ["claude"],
    date: "2026-05-22",
  },

  {
    slug: "5-ai-tools-one-person-overseas-business",
    title: "5 AI Tools to Build Your One-Person Overseas Business: Let Claude Code Work for You While You Sleep",
    titleZh: "5款AI工具打造你的单人海外业务：让Claude Code在你睡觉时为你工作",
    description:
      "Discover 5 powerful AI tools — Deer-Flow, Prompt Optimizer, Agents, Ruflo, and Letta — that together form a complete one-person AI company for overseas entrepreneurs.",
    descriptionZh:
      "发现5款强大的AI工具——Deer-Flow、Prompt Optimizer、Agents、Ruflo和Letta——它们共同构成一个完整的单人AI公司，助力海外创业者。",
    category: "ai-use-cases",
    tags: ["ai-tools", "overseas-business", "one-person-company", "automation", "productivity"],
    difficulty: "beginner",
    toolsMentioned: ["deer-flow", "prompt-optimizer", "openagents", "ruflo", "letta", "claude"],
    date: "2026-05-23",
  },

  {
    slug: "git-github-beginners-guide",
    title: "Git & GitHub Beginner's Guide: Core Concepts & Operation",
    titleZh: "Git与GitHub初学者指南：核心概念与操作",
    description:
      "A complete beginner guide to Git and GitHub covering core concepts, workflow, essential commands, branch management, and common troubleshooting tips.",
    descriptionZh:
      "Git和GitHub的完整初学者指南，涵盖核心概念、工作流程、基本命令、分支管理和常见故障排除技巧。",
    category: "ai-tutorials",
    tags: ["git", "github", "version-control", "beginner", "tutorial"],
    difficulty: "beginner",
    toolsMentioned: ["claude"],
    date: "2026-05-23",
  },

  {
    slug: "openai-strategic-counterattack-openclaw-codex",
    title: "OpenAI's Strategic Counterattack: How OpenClaw Integration and Codex Innovations Are Reshaping the AI Developer Landscape",
    titleZh: "OpenAI的战略反击：OpenClaw集成与Codex创新如何重塑AI开发者格局",
    description:
      "An in-depth analysis of OpenAI's latest moves — OpenClaw integration, Codex pixel pet, autonomous iteration, and one-click migration — reshaping the AI developer tools market.",
    descriptionZh:
      "深入分析OpenAI的最新举措——OpenClaw集成、Codex像素宠物、自主迭代和一键迁移——重塑AI开发者工具市场。",
    category: "ai-news",
    tags: ["openai", "openclaw", "codex", "strategy", "developer-tools"],
    difficulty: "intermediate",
    toolsMentioned: ["openclaw", "chatgpt", "claude"],
    date: "2026-05-23",
  },

  {
    slug: "agent-skill-harness-explained",
    title: "Practical Explanation of Agent, Skill and Harness in Modern AI Development",
    titleZh: "现代AI开发中Agent、Skill和Harness的实用解释",
    description:
      "A detailed breakdown of three core AI automation concepts — Agent, Skill, and Harness — with definitions, operational logic, and practical Python code examples.",
    descriptionZh:
      "详细解析三个核心AI自动化概念——Agent、Skill和Harness——包括定义、操作逻辑和实际Python代码示例。",
    category: "ai-basics",
    tags: ["agent", "skill", "harness", "ai-automation", "python"],
    difficulty: "intermediate",
    toolsMentioned: ["claude"],
    date: "2026-05-23",
  },

  {
    slug: "5-ai-html-hacks-overseas-websites",
    title: "Unlock Hidden Potentials: 5 Practical AI+HTML Hacks for Overseas Websites",
    titleZh: "解锁隐藏潜力：面向海外网站的5个实用AI+HTML技巧",
    description:
      "5 actionable AI+HTML use cases for overseas websites — real-time language localization, dynamic content personalization, FAQ chatbot, AI email templates, and smart form validation.",
    descriptionZh:
      "面向海外网站的5个实用的AI+HTML用例——实时语言本地化、动态内容个性化、FAQ聊天机器人、AI邮件模板和智能表单验证。",
    category: "ai-use-cases",
    tags: ["ai-html", "overseas-websites", "localization", "chatbot", "form-validation"],
    difficulty: "intermediate",
    toolsMentioned: ["chatgpt", "claude"],
    date: "2026-05-23",
  },

  {
		slug: "alexander-wang-meta-ai-superintelligence",
		title: "Alexander Wang's Meta AI Superintelligence: A New Era for Overseas Businesses",
		titleZh: "Alexander Wang的Meta AI超级智能：海外业务的新纪元",
		description:
			"Alexander Wang returns to lead Meta's AI division after a $14B deal. Here's what Muse Spark, MSL, and Meta's superintelligence strategy mean for overseas businesses.",
		descriptionZh:
			"Alexander Wang以140亿美元交易回归领导Meta AI部门。Muse Spark、MSL和Meta的超级智能战略对海外业务意味着什么。",
		category: "ai-news",
		tags: ["meta", "alexander-wang", "superintelligence", "muse-spark", "msl", "overseas-business"],
		difficulty: "beginner",
		toolsMentioned: [],
		date: "2026-05-24",
	},

  {
		slug: "ai-workforce-virtual-employees",
		title: "From Tool Development to AI Workforce: Why Programmers Are Building Virtual AI Employees",
		titleZh: "从工具开发到AI劳动力：为什么程序员正在构建虚拟AI员工",
		description:
			"Programmers are shifting from building utility tools to creating AI employees that handle business tasks autonomously. Learn the architecture, deployment, and practical use cases.",
		descriptionZh:
			"程序员正从构建实用工具转向创建能自主处理业务任务的AI员工。了解架构、部署和实际用例。",
		category: "ai-use-cases",
		tags: ["ai-employees", "virtual-staff", "automation", "overseas-business", "workforce"],
		difficulty: "intermediate",
		toolsMentioned: ["claude"],
		date: "2026-05-24",
	},

  {
		slug: "free-ai-knowledge-base-tool-tutorial",
		title: "Practical Tutorial on Powerful Free AI Knowledge Base Tool",
		titleZh: "强大的免费AI知识库工具实用教程",
		description:
			"A step-by-step guide to building your own private AI knowledge base for free. Learn document management, intelligent retrieval, and practical applications for overseas business.",
		descriptionZh:
			"构建你自己的免费私有AI知识库的分步指南。了解文档管理、智能检索和海外业务的实际应用。",
		category: "ai-tutorials",
		tags: ["knowledge-base", "document-management", "ai-search", "tutorial", "free-tool"],
		difficulty: "beginner",
		toolsMentioned: [],
		date: "2026-05-24",
	},

  {
		slug: "6-must-have-openclaw-skills",
		title: "6 Must-Have Base Skills for OpenClaw to Boost Your AI Productivity",
		titleZh: "OpenClaw必备的6个基础技能，提升你的AI生产力",
		description:
			"Discover the 6 most practical OpenClaw skills for AI productivity: browser automation, web search, self-improvement, skill discovery, security auditing, and email management.",
		descriptionZh:
			"发现OpenClaw中最实用的6个提升AI生产力的技能：浏览器自动化、网络搜索、自我进化、技能发现、安全审计和邮件管理。",
		category: "ai-tutorials",
		tags: ["openclaw", "skills", "automation", "productivity", "browser", "search", "email"],
		difficulty: "intermediate",
		toolsMentioned: ["openclaw"],
		date: "2026-05-24",
	},

  {
		slug: "top-10-claude-code-commands",
		title: "Top 10 Claude Code Commands: Boost Your AI Productivity",
		titleZh: "Top 10 Claude Code命令：提升你的AI生产力",
		description:
			"Master the 10 most practical Claude Code commands for automated coding, project initialization, context management, insights, and plugin installation.",
		descriptionZh:
			"掌握10个最实用的Claude Code命令，涵盖自动化编码、项目初始化、上下文管理、洞察分析和插件安装。",
		category: "ai-tutorials",
		tags: ["claude-code", "commands", "automation", "productivity", "terminal", "cli"],
		difficulty: "beginner",
		toolsMentioned: ["claude"],
		date: "2026-05-24",
	},

  {
		slug: "deerflow-multi-agent-tool",
		title: "DeerFlow: The Open-Source Parallel Multi-Agent Tool for Efficient Task Execution",
		titleZh: "DeerFlow：高效任务执行的开源并行多智能体工具",
		description:
			"DeerFlow is an open-source parallel multi-agent framework that splits tasks into sub-tasks and runs them simultaneously. Learn architecture, features, and practical use cases.",
		descriptionZh:
			"DeerFlow是一个开源并行多智能体框架，将任务拆分为子任务并同时运行。了解架构、特性和实际用例。",
		category: "ai-tools",
		tags: ["deerflow", "multi-agent", "parallel", "open-source", "automation", "productivity"],
		difficulty: "intermediate",
		toolsMentioned: ["deer-flow", "claude"],
		date: "2026-05-24",
	},

  {
		slug: "12-claude-code-terminal-commands",
		title: "12 Essential Claude Code Terminal Commands to Boost Efficiency and Avoid Pitfalls",
		titleZh: "12个必备Claude Code终端命令：提升效率、避免陷阱",
		description:
			"Discover 12 practical Claude Code terminal commands across three tiers — from beginner essentials like /init and /help to advanced power-user tricks like /exclude and /reload — that boost your AI coding efficiency and prevent common mistakes.",
		descriptionZh:
			"探索12个实用的Claude Code终端命令，分为三个等级——从/init和/help等初学者必备命令到/exclude和/reload等高级技巧——提升你的AI编码效率，避免常见错误。",
		category: "ai-tutorials",
		tags: ["claude-code", "terminal-commands", "cli", "productivity", "beginner"],
		difficulty: "beginner",
		toolsMentioned: ["claude"],
		date: "2026-05-24",
	},

  {
		slug: "claude-code-overseas-business-guide",
		title: "Claude Code: A Comprehensive Guide to Boosting Productivity for Overseas Businesses",
		titleZh: "Claude Code：助力海外业务提升效率的全面指南",
		description:
			"A complete guide to using Claude Code for overseas businesses — covering installation, model configuration, modes of operation, essential commands, hooks, and practical automation use cases for global entrepreneurs.",
		descriptionZh:
			"一份面向海外业务的Claude Code完整使用指南——涵盖安装、模型配置、操作模式、基本命令、钩子和面向全球创业者的实用自动化用例。",
		category: "ai-use-cases",
		tags: ["claude-code", "overseas-business", "productivity", "automation", "cli"],
		difficulty: "beginner",
		toolsMentioned: ["claude"],
		date: "2026-05-24",
	},

  {
		slug: "harness-automating-video-creation",
		title: "Harness in Practice: Automating Knowledge Explanation Video Creation",
		titleZh: "Harness实战：自动化知识讲解视频创作",
		description:
			"Learn how to leverage Harness and agent technologies to automate the creation of technical knowledge explanation videos — from script writing and visual design to audio synthesis and screen recording.",
		descriptionZh:
			"学习如何利用Harness和代理技术自动化创建技术知识讲解视频——从脚本编写、视觉设计到音频合成和屏幕录制。",
		category: "ai-use-cases",
		tags: ["harness", "video-creation", "automation", "agents", "content-creation"],
		difficulty: "intermediate",
		toolsMentioned: ["claude"],
		date: "2026-05-24",
	},

  {
		slug: "oh-my-claudecode-omc-guide",
		title: "Unlock Ultimate AI Coding Efficiency with Oh-My-ClaudeCode (OMC)",
		titleZh: "用Oh-My-ClaudeCode（OMC）解锁终极AI编码效率",
		description:
			"Discover Oh-My-ClaudeCode (OMC), the super-enhancement plugin that turns Claude Code into a full AI development team — with 32 specialized agents, three core modes, and smart model routing for token savings.",
		descriptionZh:
			"了解Oh-My-ClaudeCode（OMC），这个超级增强插件将Claude Code转变为完整的AI开发团队——拥有32个专业代理、三种核心模式和智能模型路由以节省Token。",
		category: "ai-tutorials",
		tags: ["claude-code", "omc", "oh-my-claudecode", "plugin", "agents", "productivity"],
		difficulty: "intermediate",
		toolsMentioned: ["claude"],
		date: "2026-05-24",
	},

  {
			slug: "claude-code-self-coding-revolution",
			title: "AI Era Dawns: Claude Code's Self-Coding Revolution and Practical Guide to Leveraging Actionable AI Agents",
			titleZh: "AI时代来临：Claude Code的自我编程革命与AI Agent实战指南",
			description:
				"Claude Code now writes 100% of its own code. Learn how to leverage actionable AI agents for task automation, travel planning, and business workflow optimization.",
			descriptionZh:
				"Claude Code现在能100%自主编写代码。了解如何利用可操作的AI代理进行任务自动化、旅行规划和业务流程优化。",
			category: "ai-tutorials",
			tags: ["claude-code", "ai-agents", "automation", "prompt-engineering", "productivity"],
			difficulty: "intermediate",
			toolsMentioned: ["claude"],
			date: "2026-05-25",
		},

  {
			slug: "gpt-claude-grok-gemini-comparison",
			title: "Choosing the Right AI Giant: GPT, Claude, Grok, or Gemini for Your Needs",
			titleZh: "选择合适的AI巨头：GPT、Claude、Grok还是Gemini？",
			description:
				"A practical comparison of GPT, Claude, Grok, and Gemini — strengths, weaknesses, and who should use each. Make an informed decision for academic research, coding, or content creation.",
			descriptionZh:
				"GPT、Claude、Grok和Gemini的实用对比——优势、劣势和各自适合人群。为学术研究、编程或内容创作做出明智选择。",
			category: "ai-comparisons",
			tags: ["gpt", "claude", "grok", "gemini", "comparison", "ai-models"],
			difficulty: "beginner",
			toolsMentioned: ["chatgpt", "claude", "gemini"],
			date: "2026-05-25",
		},

  {
			slug: "codex-agent-desktop-jarvis",
			title: "Codex Agent: Your Desktop Jarvis for Effortless Task Automation",
			titleZh: "Codex Agent：你的桌面贾维斯，轻松实现任务自动化",
			description:
				"OpenAI Codex's new agent update turns your desktop into a Jarvis-like assistant. Learn to command apps with natural language, automate workflows, and boost overseas business productivity.",
			descriptionZh:
				"OpenAI Codex的新代理更新将你的桌面变成贾维斯式助手。学习用自然语言命令应用、自动化工作流，提升海外业务生产力。",
			category: "ai-tools",
			tags: ["codex", "openai", "automation", "desktop", "ai-agent", "productivity"],
			difficulty: "beginner",
			toolsMentioned: ["chatgpt", "claude"],
			date: "2026-05-25",
		},

  {
			slug: "google-5-skill-design-patterns",
			title: "Google's 5 Skill Design Patterns for Stable Agent Output: A Practical Guide for Overseas Web Development",
			titleZh: "Google的5个技能设计模式：稳定AI Agent输出的实用指南",
			description:
				"Learn Google's five Skill design patterns — Tool Wrapper, Generator, Reviewer, Inversion, and Pipeline — for stable, high-quality AI agent output in overseas web development.",
			descriptionZh:
				"学习Google的五个技能设计模式——Tool Wrapper、Generator、Reviewer、Inversion和Pipeline——在海外Web开发中实现稳定高质量的AI Agent输出。",
			category: "ai-tutorials",
			tags: ["google", "skill-patterns", "ai-agents", "overseas-web", "tutorial", "design-patterns"],
			difficulty: "intermediate",
			toolsMentioned: ["gemini"],
			date: "2026-05-25",
		},

  {
		slug: "beyond-llms-ai-fundamentals",
		title: "Beyond Large Language Models: Mastering AI Fundamental Knowledge for Overseas Developers",
		titleZh: "超越大语言模型：海外开发者必须掌握的AI基础知识",
		description: "Most developers equate AI with LLMs, leading to wasted tokens and high costs. This guide breaks down AI core concepts, token calculation, and practical optimization strategies.",
		descriptionZh: "大多数开发者将AI等同于大语言模型，导致token浪费和高成本。本文详解AI核心概念、token计算和实用优化策略。",
		category: "ai-basics",
		tags: ["llm", "token", "ai-fundamentals", "embedding", "multimodal", "agent", "optimization"],
		difficulty: "beginner",
		toolsMentioned: ["chatgpt", "claude", "gemini"],
		date: "2026-05-26",
	},

  {
		slug: "choosing-right-ai-tool-comparison",
		title: "Choosing the Right AI Tool: GPT, Claude, Grok, and Gemini for Your Needs",
		titleZh: "选择合适的AI工具：GPT、Claude、Grok和Gemini对比",
		description: "GPT, Claude, Grok, and Gemini each excel in different areas. This head-to-head comparison breaks down strengths, weaknesses, and ideal use cases for each.",
		descriptionZh: "GPT、Claude、Grok和Gemini各有所长。这篇正面比较分析每个模型的优势、劣势和最佳使用场景。",
		category: "ai-comparisons",
		tags: ["gpt", "claude", "grok", "gemini", "comparison", "ai-models"],
		difficulty: "beginner",
		toolsMentioned: ["chatgpt", "claude", "gemini", "grok"],
		date: "2026-05-26",
	},

  {
		slug: "claude-code-final-config-guide",
		title: "Claude Code: Final Configuration Guide for Overseas Users (Beginner-Friendly)",
		titleZh: "Claude Code：海外用户最终配置指南（新手友好）",
		description: "Step-by-step guide to configuring API proxies for Claude Code using CC Switch — including Yunwu, ClaudeCN, and Silicone Flow setup.",
		descriptionZh: "使用CC Switch为Claude Code配置API代理的分步指南——包括云坞、ClaudeCN和Silicone Flow的设置方法。",
		category: "ai-tutorials",
		tags: ["claude-code", "configuration", "api-proxy", "cc-switch", "overseas"],
		difficulty: "beginner",
		toolsMentioned: ["claude"],
		date: "2026-05-26",
	},

  {
		slug: "cut-openclaw-costs-10x",
		title: "Cut OpenClaw Operating Costs by 10 Times: 4 Practical Strategies",
		titleZh: "将OpenClaw运营成本降低10倍：4个实用策略",
		description: "4 actionable strategies to slash OpenClaw running costs — local model switching, task concurrency limits, cache reuse, and off-peak scheduling with executable commands.",
		descriptionZh: "4个切实可行的策略将OpenClaw运行成本降低10倍——本地模型切换、任务并发限制、缓存复用和闲时调度，含可执行命令。",
		category: "ai-tutorials",
		tags: ["openclaw", "cost-optimization", "local-model", "cache", "concurrency"],
		difficulty: "intermediate",
		toolsMentioned: ["openclaw"],
		date: "2026-05-26",
	},

  {
		slug: "ecc-claude-code-setup-guide",
		title: "Stop Misconfiguring Claude Code: ECC's Zero-Pitfall Setup Guide for Overseas Projects",
		titleZh: "别再错误配置Claude Code：ECC零陷阱设置指南",
		description: "ECC's latest update eliminates common Claude Code configuration pitfalls. Learn zero-pitfall deployment with encrypted key storage, region-optimized endpoints, and sandbox execution.",
		descriptionZh: "ECC最新更新消除了常见的Claude Code配置陷阱。学习加密密钥存储、区域优化端点和沙箱执行的零陷阱部署。",
		category: "ai-tutorials",
		tags: ["claude-code", "ecc", "configuration", "overseas", "sandbox", "security"],
		difficulty: "beginner",
		toolsMentioned: ["claude"],
		date: "2026-05-26",
	},

  {
		slug: "ditching-mcp-for-cli",
		title: "Why More Developers Are Ditching MCP for CLI in AI Agent Development",
		titleZh: "为什么越来越多开发者在AI Agent开发中用CLI取代MCP",
		description: "MCP was hailed as the universal agent interface, but developers are increasingly turning to CLI for token efficiency and execution speed. Industry leaders like Perplexity and Y Combinator have embraced CLI tools.",
		descriptionZh: "MCP曾被誉为人机交互的通用接口，但越来越多的开发者转向CLI以提高token效率和执行速度。Perplexity和Y Combinator等行业领导者已拥抱CLI工具。",
		category: "ai-news",
		tags: ["mcp", "cli", "agent", "token-efficiency", "tool-comparison"],
		difficulty: "intermediate",
		toolsMentioned: ["claude", "chatgpt"],
		date: "2026-05-26",
	},

  {
			slug: "google-gemini-3-5-leak",
			title: "Google Gemini 3.5 Leak: A Game-Changer for Overseas AI Strategies with Practical Insights",
			titleZh: "Google Gemini 3.5泄露：海外AI战略的游戏规则改变者与实用洞察",
			description:
				"A massive leak reveals Google's Gemini 3.5 family with multimodal Pro, cost-efficient Flash, and 24/7 Spark agent with practical strategies for overseas businesses and developers.",
			descriptionZh:
				"大规模泄露揭示Google Gemini 3.5系列：多模态Pro、高性价比Flash和全天候Spark Agent——附带面向海外企业和开发者的实用策略。",
			category: "ai-news",
			tags: ["gemini", "google", "ai-news", "multimodal", "overseas-business"],
			difficulty: "beginner",
			toolsMentioned: ["gemini"],
			date: "2026-05-26",
		},

  {
			slug: "openai-codex-openclaw-revolution",
			title: "OpenAI's Codex and OpenClaw: Revolutionizing AI Development",
			titleZh: "OpenAI的Codex与OpenClaw：革命性的AI开发工具",
			description:
				"OpenAI integrates OpenClaw with ChatGPT Plus and upgrades Codex with pixel-art pets, autonomous iteration, and one-click migration reshaping the AI developer experience.",
			descriptionZh:
				"OpenAI将OpenClaw与ChatGPT Plus深度整合，并升级Codex：像素宠物、自主迭代和一键迁移——重塑AI开发者体验。",
			category: "ai-news",
			tags: ["openai", "codex", "openclaw", "ai-development", "automation"],
			difficulty: "intermediate",
			toolsMentioned: ["chatgpt", "openclaw", "codex-agent"],
			date: "2026-05-26",
		},

  {
    slug: "claude-code-vs-codex-automation",
    title: "AI-Powered Computer Automation: Claude Code vs. Codex - Which Path to Choose for Practical Use?",
    titleZh: "AI驱动电脑自动化：Claude Code vs Codex - 实际使用该选哪个？",
    description: "Compare Claude Code and Codex head-to-head — their vision-based vs structured-data approaches, speed, cost, accuracy, and when to use each for AI computer automation.",
    descriptionZh: "正面比较Claude Code和Codex——基于视觉 vs 基于结构化数据的技术路径、速度、成本、准确性，以及AI电脑自动化场景下的选择策略。",
    category: "ai-comparisons",
    tags: ["claude-code", "codex", "computer-use", "automation", "comparison"],
    difficulty: "intermediate",
    toolsMentioned: ["claude", "codex-agent"],
    date: "2026-05-27",
  },

  {
    slug: "ai-money-making-system-one-day",
    title: "Build Your Money-Making System in One Day: Stop Trading Time for Money Alone",
    titleZh: "一天搭建你的赚钱系统：别再单独用时间换钱",
    description: "A practical step-by-step guide to building an AI-powered money-making system in just one day — from identifying paid needs to launching your first product.",
    descriptionZh: "一个实用的分步指南，教你一天内搭建AI驱动的赚钱系统——从识别付费需求到发布你的第一个产品。",
    category: "ai-use-cases",
    tags: ["money-making", "ai-business", "passive-income", "product-creation", "beginner"],
    difficulty: "beginner",
    toolsMentioned: ["claude", "chatgpt"],
    date: "2026-05-27",
  },

  {
    slug: "claude-code-6-hidden-powers",
    title: "Claude Code: 6 Hidden Powers to Transform It From Chatbot to Your AI Development Partner",
    titleZh: "Claude Code：6个隐藏力量，将其从聊天机器人转变为你的AI开发伙伴",
    description: "Discover 6 hidden features of Claude Code — /init, Plan Mode, /compact, custom slash commands, subagents, and hooks — that turn it into a long-term AI development partner for overseas projects.",
    descriptionZh: "发现Claude Code的6个隐藏功能——/init、Plan Mode、/compact、自定义Slash命令、子代理和钩子——将其转变为海外项目的长期AI开发伙伴。",
    category: "ai-tutorials",
    tags: ["claude-code", "hidden-powers", "init", "plan-mode", "hooks", "overseas"],
    difficulty: "intermediate",
    toolsMentioned: ["claude"],
    date: "2026-05-27",
  },

  {
    slug: "karpathy-ai-training-scale-method",
    title: "Karpathy's Viral Twitter Method: Scale AI Training with 1.6K Samples for Overseas Projects",
    titleZh: "Karpathy的病毒式Twitter方法：用1600个样本实现海外项目AI训练规模化",
    description: "Andrej Karpathy's cost-efficient AI training method uses just 1,600 curated samples. Learn step-by-step implementation, from dataset curation to model deployment for overseas projects.",
    descriptionZh: "Andrej Karpathy的高性价比AI训练方法仅需1600个精心挑选的样本。学习从数据集筛选到模型部署的分步实现，适用于海外项目。",
    category: "ai-news",
    tags: ["karpathy", "ai-training", "small-data", "fine-tuning", "overseas"],
    difficulty: "intermediate",
    toolsMentioned: ["chatgpt", "claude"],
    date: "2026-05-27",
  },

  {
    slug: "google-gemini-3-5-upgrade-guide",
    title: "Google Accelerates Upgrade to Gemini 3.5: Full New Features & Practical Deployment Guide",
    titleZh: "Google加速升级Gemini 3.5：全新功能与实战部署指南",
    description: "Google's Gemini 3.5 brings Ultra and Flash variants, enhanced multimodal capabilities, and lower API costs. Complete deployment guide with code examples for overseas businesses.",
    descriptionZh: "Google Gemini 3.5带来Ultra和Flash双版本、增强的多模态能力与更低API成本。包含代码示例的完整部署指南，面向海外业务。",
    category: "ai-news",
    tags: ["gemini", "google", "multimodal", "api", "deployment", "overseas"],
    difficulty: "beginner",
    toolsMentioned: ["gemini"],
    date: "2026-05-27",
  },

  {
    slug: "6-ai-tools-dominating-github",
    title: "6 AI Tools Dominating GitHub to Take Over Your Workflow",
    titleZh: "统治GitHub的6大AI工具：接管你的工作流",
    description:
      "Six groundbreaking AI tools are dominating GitHub — Karpathy Skills, CodeGraph, Understand Anything, Presenton, NVIDIA LongLive, and Claude Plugins. Learn how to leverage them for overseas development projects.",
    descriptionZh:
      "六个开创性的AI工具正在GitHub上主导趋势——Karpathy Skills、CodeGraph、Understand Anything、Presenton、NVIDIA LongLive和Claude Plugins。了解如何将它们用于海外开发项目。",
    category: "ai-tools",
    tags: ["ai-tools", "github", "workflow-automation", "karpathy", "codegraph", "overseas-development"],
    difficulty: "beginner",
    toolsMentioned: ["claude", "karpathy-skills", "codegraph", "presenton", "nvidia-longlive"],
    date: "2026-05-28",
  },

  {
    slug: "ai-document-replication-one-click",
    title: "AI-Powered Document Replication: One-Click Duplicate Any File for Overseas Use Cases",
    titleZh: "AI文档复制：一键复制任何文件用于海外业务场景",
    description:
      "Replicate professional documents — contracts, marketing brochures, or industry reports — for overseas markets using AI. A step-by-step guide with Python code for structure parsing and style emulation.",
    descriptionZh:
      "使用AI为海外市场复制专业文档——合同、营销手册或行业报告。包含使用Python进行结构解析和风格模拟的分步指南。",
    category: "ai-use-cases",
    tags: ["document-replication", "document-automation", "overseas-business", "ai-tutorial", "content-creation"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt", "claude"],
    date: "2026-05-28",
  },

  {
    slug: "mastering-hermes-agent-7-levels",
    title: "Mastering Hermes Agent: A Practical Guide to 7 Levels of Configuration for Powerful AI Automation",
    titleZh: "掌握Hermes Agent：7级配置实现强大AI自动化的实用指南",
    description:
      "Transform Hermes Agent from a basic chatbot into a robust backend system. A practical guide covering 7 configuration levels — VPS deployment, Discord, Kanban, holographic memory, and MCP server.",
    descriptionZh:
      "将Hermes Agent从基本聊天机器人转变为强大的后端系统。涵盖7级配置的实用指南——VPS部署、Discord、看板、全息记忆和MCP服务器。",
    category: "ai-tutorials",
    tags: ["hermes-agent", "ai-agent", "automation", "vps", "discord", "mcp", "ai-tutorial"],
    difficulty: "intermediate",
    toolsMentioned: ["hermes-agent", "openrouter"],
    date: "2026-05-28",
  },

  {
    slug: "vibe-trading-hku-financial-agent",
    title: "Vibe-Trading: A Deep Dive into HKU's Open-Source Financial Agent OS",
    titleZh: "Vibe-Trading深度解析：港大开源金融代理操作系统",
    description:
      "HKU's Vibe-Trading is a financial Agent OS with 30+ tools, 72 skills, 452 alpha factors, and a 33-agent team. Deep dive into its architecture, Think-Act-Observe loop, and practical applications.",
    descriptionZh:
      "港大的Vibe-Trading是一个拥有30+工具、72项技能、452个Alpha因子和33代理团队的金融代理操作系统。深入解析其架构、Think-Act-Observe循环和实际应用。",
    category: "ai-news",
    tags: ["vibe-trading", "hku", "financial-agent", "open-source", "trading", "ai-agent"],
    difficulty: "intermediate",
    toolsMentioned: ["vibe-trading"],
    date: "2026-05-28",
  },

  {
    slug: "hermes-agent-vs-openclaw-comparison",
    title: "A Practical Comparison: Hermes Agent vs OpenClaw in AI Task Execution and Self-Evolution",
    titleZh: "Hermes Agent vs OpenClaw实用对比：AI任务执行与自我进化",
    description:
      "An 8-round practical test comparing Hermes Agent and OpenClaw on speed, token efficiency, user preference learning, and self-evolution capabilities. See which AI agent comes out ahead.",
    descriptionZh:
      "通过8轮实战测试对比Hermes Agent和OpenClaw在速度、Token效率、用户偏好学习和自我进化方面的表现。看清哪款AI代理更胜一筹。",
    category: "ai-comparisons",
    tags: ["hermes-agent", "openclaw", "ai-comparison", "ai-agents", "self-evolution", "task-automation"],
    difficulty: "intermediate",
    toolsMentioned: ["hermes-agent", "openclaw"],
    date: "2026-05-29",
  },

  {
    slug: "codegraph-local-semantic-code-intelligence",
    title: "CodeGraph: Supercharge AI Coding Agents with Local Semantic Code Intelligence",
    titleZh: "CodeGraph：用本地语义代码智能为AI编程代理加速",
    description:
      "CodeGraph is an open-source semantic code knowledge graph that reduces AI tool calls by up to 70% and token usage by 35%. Learn how to integrate it with Claude Code, Cursor, and more.",
    descriptionZh:
      "CodeGraph是一个开源语义代码知识图谱，可将AI工具调用减少70%，Token使用量降低35%。了解如何将其与Claude Code、Cursor等集成。",
    category: "ai-tools",
    tags: ["codegraph", "semantic-code", "ai-coding", "claude-code", "cursor", "knowledge-graph"],
    difficulty: "intermediate",
    toolsMentioned: ["codegraph", "claude", "cursor"],
    date: "2026-05-29",
  },

  {
    slug: "ditch-rag-llm-wiki-future",
    title: "Ditch RAG: LLM Wiki Is the Future of Personal Knowledge Bases for Global Users",
    titleZh: "放弃RAG：LLM Wiki是面向全球用户的个人知识库的未来",
    description:
      "LLM Wiki outperforms RAG for global knowledge management with lower latency, reduced token waste, and contextual linking. A step-by-step guide to building your own LLM Wiki for overseas use cases.",
    descriptionZh:
      "LLM Wiki在延迟更低、Token浪费更少和上下文关联方面优于RAG。面向海外用例的LLM Wiki构建分步指南。",
    category: "ai-news",
    tags: ["llm-wiki", "rag", "knowledge-base", "overseas", "semantic-search", "personal-knowledge"],
    difficulty: "intermediate",
    toolsMentioned: ["chatgpt", "claude"],
    date: "2026-05-29",
  },

  {
    slug: "hermes-agent-8-features-smb",
    title: "Hermes Agent: 8 Game-Changing Features in One Week for SMBs and Solopreneurs",
    titleZh: "Hermes Agent：一周内为中小企业和个人创业者推出的8个革命性功能",
    description:
      "Hermes Agent's latest update brings 8 new features including Computer Use, background task processing, and long-term memory upgrades. Practical guide for SMBs and solopreneurs.",
    descriptionZh:
      "Hermes Agent最新更新带来8个新功能，包括电脑使用、后台任务处理和长期记忆升级。面向中小企业和个人创业者的实用指南。",
    category: "ai-tools",
    tags: ["hermes-agent", "ai-agent", "smb", "solopreneur", "automation", "computer-use"],
    difficulty: "beginner",
    toolsMentioned: ["hermes-agent"],
    date: "2026-05-29",
  },

  {
    slug: "ultimate-ai-coding-apps-minutes",
    title: "Ultimate AI Coding Guide: Build Your Own Global Apps Within Minutes",
    titleZh: "终极AI编码指南：几分钟内构建你的全球应用",
    description:
      "A comprehensive guide to AI-driven application development using modern AI tools. Learn to initialize, code, debug, and deploy global apps from scratch with zero professional coding experience.",
    descriptionZh:
      "使用现代AI工具进行AI驱动应用开发的全面指南。学习从零初始化、编码、调试和部署全球应用，无需专业编程经验。",
    category: "ai-tutorials",
    tags: ["ai-coding", "app-development", "vite", "react", "vercel", "overseas", "beginner"],
    difficulty: "beginner",
    toolsMentioned: ["claude", "cursor", "chatgpt"],
    date: "2026-05-29",
  },

  {
    slug: "codex-obsidian-knowledge-base",
    title: "Build Super Powerful Personal Knowledge Base: Combine Codex AI with Obsidian Full Practical Guide",
    titleZh: "构建超强个人知识库：Codex AI与Obsidian完整实战指南",
    description: "Learn how to combine Codex AI with Obsidian to build a private, offline, high-performance knowledge management system.",
    descriptionZh: "学习如何将Codex AI与Obsidian结合，构建私有高性能的知识管理系统。",
    category: "ai-tutorials",
    tags: ["codex", "obsidian", "knowledge-base", "note-taking", "local-ai", "beginner"],
    difficulty: "beginner",
    toolsMentioned: ["codex-agent", "chatgpt"],
    date: "2026-05-30",
  },

  {
    slug: "claude-code-essential-three-tools",
    title: "Claude Code Essential Setup: The Must-Have Three Tools for Global Developers (Beginner's Guide)",
    titleZh: "Claude Code必备设置：全球开发者三大工具（初学者指南）",
    description: "Before running Claude Code, you need Node.js, Git, and a terminal enhancement tool.",
    descriptionZh: "在运行Claude Code之前需安装Node.js、Git和终端增强工具。",
    category: "ai-tutorials",
    tags: ["claude-code", "nodejs", "git", "setup", "terminal", "beginner"],
    difficulty: "beginner",
    toolsMentioned: ["claude"],
    date: "2026-05-30",
  },

  {
    slug: "mastering-claude-code-cli",
    title: "Mastering Claude Code CLI: A Practical Guide for Overseas Developers",
    titleZh: "掌握Claude Code CLI：海外开发者实用指南",
    description: "Master Claude Code CLI for overseas development.",
    descriptionZh: "掌握面向海外开发的Claude Code CLI。",
    category: "ai-tutorials",
    tags: ["claude-code", "cli", "terminal", "overseas", "productivity", "intermediate"],
    difficulty: "intermediate",
    toolsMentioned: ["claude"],
    date: "2026-05-30",
  },

  {
    slug: "token-business-101-beginners",
    title: "Token Business 101: How Beginners Start from Zero for Global Markets",
    titleZh: "Token经济入门：初学者从零进军全球市场",
    description: "A complete beginner's guide to launching a token business for global markets.",
    descriptionZh: "面向全球市场启动Token业务的完整初学者指南。",
    category: "ai-use-cases",
    tags: ["token", "crypto", "blockchain", "business", "overseas", "beginner"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt", "claude"],
    date: "2026-05-30",
  },

  {
    slug: "5-must-have-claude-code-skills",
    title: "5 Must-Have Claude Code Skills for Developers: Boost Your AI Coding Efficiency Globally",
    titleZh: "开发者必备的5个Claude Code技能：提升你的AI编码效率",
    description: "Discover 5 powerful Claude Code skills that transform your development workflow for global projects.",
    descriptionZh: "发现5个强大的Claude Code技能，为你的全球项目开发流程带来变革。",
    category: "ai-tutorials",
    tags: ["claude-code", "skills", "productivity", "cli", "coding", "developer-tools"],
    difficulty: "intermediate",
    toolsMentioned: ["claude"],
    date: "2026-05-31",
  },

  {
    slug: "claude-opus-4-8-redefining-ai",
    title: "Claude Opus 4.8: Redefining AI Engineering and Software Development Paradigms",
    titleZh: "Claude Opus 4.8：重新定义AI工程与软件开发范式",
    description: "Claude Opus 4.8 achieves two groundbreaking 0 percent milestones in reliability and introduces Dynamic Workflows.",
    descriptionZh: "Claude Opus 4.8实现了两个开创性的0百分比可靠性里程碑，并引入了动态工作流。",
    category: "ai-news",
    tags: ["claude", "opus-4-8", "anthropic", "ai-model", "software-engineering"],
    difficulty: "beginner",
    toolsMentioned: ["claude"],
    date: "2026-05-31",
  },

  {
    slug: "hermes-agent-beginner-guide-ep1",
    title: "Hermes Agent Full Beginner Guide Episode 1: Ditch Complex Settings and Master Practical Local AI Deployment",
    titleZh: "Hermes Agent新手完全指南第一集：摒弃复杂设置，掌握实用本地AI部署",
    description: "A practical beginner guide to Hermes Agent focusing on core usable functions for local AI deployment.",
    descriptionZh: "实用的Hermes Agent新手指南，专注于本地AI部署的核心功能。",
    category: "ai-tutorials",
    tags: ["hermes-agent", "beginner", "local-ai", "deployment", "ai-agent", "tutorial"],
    difficulty: "beginner",
    toolsMentioned: ["hermes-agent"],
    date: "2026-05-31",
  },

  {
    slug: "multi-agent-collaboration-architecture",
    title: "Multi-Agent Collaboration Architecture: The Ultimate Version QandA Tool",
    titleZh: "多智能体协作架构：终极版问答工具",
    description: "Multi-agent collaboration architecture outperforms traditional QandA tools for global teams.",
    descriptionZh: "多智能体协作架构以并行处理和多语言适应性超越传统问答工具。",
    category: "ai-tutorials",
    tags: ["multi-agent", "collaboration", "qa-tool", "ai-agent", "architecture"],
    difficulty: "intermediate",
    toolsMentioned: ["claude", "chatgpt"],
    date: "2026-05-31",
  },
  {
    slug: "codegraph-17x-coding-efficiency",
    title: "CodeGraph: The Tool That Boosts Coding Efficiency by 17x for Global Developers",
    titleZh: "CodeGraph：将全球开发者编码效率提升17倍的工具",
    description: "CodeGraph is an open-source code knowledge graph tool that reduces AI tool calls by 17x. Learn deployment, integration with Claude Code, and practical use cases for overseas projects.",
    descriptionZh: "CodeGraph是一个开源代码知识图谱工具，可将AI工具调用次数减少17倍。了解部署方法、与Claude Code的集成以及海外项目实用案例。",
    category: "ai-tools",
    tags: ["codegraph", "knowledge-graph", "ai-coding", "open-source", "productivity"],
    difficulty: "beginner",
    toolsMentioned: ["codegraph"],
    date: "2026-06-01",
  },

  {
    slug: "deepseek-v4-cost-effective",
    title: "DeepSeek V4: The Cost-Effective King of AI Models for Developers",
    titleZh: "DeepSeek V4：开发者性价比最高的AI模型",
    description: "DeepSeek V4 offers 1.6 trillion parameters, MoE architecture, and 1M token context at 7x cheaper than Claude and 40x cheaper than GPT-5.5 Pro. Complete deployment guide with OpenCode.",
    descriptionZh: "DeepSeek V4拥有1.6万亿参数、MoE架构和100万token上下文窗口，比Claude便宜7倍，比GPT-5.5 Pro便宜40倍。包含使用OpenCode的完整部署指南。",
    category: "ai-news",
    tags: ["deepseek", "ai-model", "open-source", "cost-effective", "moE", "coding"],
    difficulty: "beginner",
    toolsMentioned: ["deepseek"],
    date: "2026-06-01",
  },

  {
    slug: "mastering-ai-agents-entrepreneurs",
    title: "Mastering AI Agents: A Practical Guide for Overseas Entrepreneurs",
    titleZh: "掌握AI Agent：面向海外创业者的实用指南",
    description: "Learn the difference between LLM workflows and AI Agents, the 5 pillars of building an Agent, the ReAct framework, and practical tips for leveraging AI Agents in overseas businesses.",
    descriptionZh: "了解LLM工作流与AI Agent的区别、构建Agent的五大支柱、ReAct框架以及在海外业务中利用AI Agent的实用技巧。",
    category: "ai-use-cases",
    tags: ["ai-agents", "llm-workflow", "react-framework", "overseas-business", "automation", "entrepreneurs"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt", "claude", "openclaw"],
    date: "2026-06-01",
  },

  {
    slug: "six-advanced-claude-code-skills",
    title: "Six Advanced Claude Code Skills: Master AI Coding From Beginner To Expert In 90 Seconds",
    titleZh: "六个高级Claude Code技能：从新手到AI编程高手只需90秒",
    description: "Master 6 advanced Claude Code skills for overseas development: project scanning, code standardization, multilingual comments, module splitting, deployment config, and technical documentation.",
    descriptionZh: "掌握6个高级Claude Code技能，适用于海外开发：项目扫描、代码标准化、多语言注释、模块拆分、部署配置和技术文档生成。",
    category: "ai-tutorials",
    tags: ["claude-code", "advanced-skills", "coding", "productivity", "overseas-development", "cli"],
    difficulty: "intermediate",
    toolsMentioned: ["claude"],
    date: "2026-06-01",
  },

  {
    slug: "why-claude-code-overseas-website",
    title: "Why Claude Code is a Must-Have Tool for Overseas Website Owners",
    titleZh: "为什么Claude Code是海外网站拥有者的必备工具",
    description: "Discover how Claude Code helps overseas website owners with deployment, open-source software management, custom tool development, content creation, and project execution automation.",
    descriptionZh: "了解Claude Code如何帮助海外网站拥有者进行部署、开源软件管理、自定义工具开发、内容创作和项目执行自动化。",
    category: "ai-use-cases",
    tags: ["claude-code", "overseas-website", "automation", "deployment", "content-creation", "productivity"],
    difficulty: "beginner",
    toolsMentioned: ["claude"],
    date: "2026-06-01",
  },


  {
    slug: "8-game-changing-claude-code-skills",
    title: "8 Game-Changing Skills of Claude Code to Transform You into an All-Round Creative Team",
    titleZh: "8个改变游戏规则的Claude Code技能，将你转变为全能创意团队",
    description: "Discover 8 powerful Claude Code skills — content strategy, frontend design, SVG logo, animation, DOCX, PPTX, XLSX, and PDF — that transform you into an all-round creative team.",
    descriptionZh: "发现8个强大的Claude Code技能——内容策略、前端设计、SVG标志、动画、DOCX、PPTX、XLSX和PDF——将你转变为全能的创意团队。",
    category: "ai-tutorials",
    tags: ["claude-code", "skills", "creative-team", "productivity", "cli"],
    difficulty: "intermediate",
    toolsMentioned: ["claude"],
    date: "2026-06-02",
  },

  {
    slug: "github-repositories-guide-developers",
    title: "Complete Practical Guide to Using GitHub Repositories for Global Independent Developers",
    titleZh: "全球独立开发者GitHub仓库完整实战指南",
    description: "A complete hands-on guide to using GitHub repositories for global independent developers — covering installation, common commands, branch management, remote sync, and practical tips.",
    descriptionZh: "面向全球独立开发者的GitHub仓库完整实战指南——涵盖安装、常用命令、分支管理、远程同步和实用技巧。",
    category: "ai-tutorials",
    tags: ["git", "github", "version-control", "branching", "collaboration", "overseas"],
    difficulty: "beginner",
    toolsMentioned: ["claude"],
    date: "2026-06-02",
  },

  {
    slug: "hooks-ai-workflow-gatekeeper",
    title: "Hooks: The Gatekeeper for AI Workflows to Ensure Rule Compliance",
    titleZh: "Hooks：AI工作流的守门人，确保规则执行",
    description: "Learn how Hooks act as enforceable checkpoints in AI workflows to ensure rule compliance — from session start to task completion, with practical implementation methods.",
    descriptionZh: "了解Hooks如何作为AI工作流中的强制检查点来确保规则遵守——从会话开始到任务完成，包含实用实现方法。",
    category: "ai-tutorials",
    tags: ["hooks", "ai-workflow", "compliance", "automation", "claude-code"],
    difficulty: "intermediate",
    toolsMentioned: ["claude"],
    date: "2026-06-02",
  },

  {
    slug: "llm-stable-json-output-guide",
    title: "How to Ensure Large Language Models Stably Output JSON: A Practical Guide for Developers",
    titleZh: "如何确保大语言模型稳定输出JSON：开发者实用指南",
    description: "A practical guide with 4 layers of strategies — prompt engineering, native LLM capabilities, token constraints, and fallback mechanisms — to ensure stable JSON output from LLMs.",
    descriptionZh: "4层策略的实用指南——提示工程、原生LLM能力、Token约束和回退机制——确保LLM稳定输出JSON。",
    category: "ai-tutorials",
    tags: ["llm", "json", "prompt-engineering", "function-calling", "structured-output", "developer-guide"],
    difficulty: "intermediate",
    toolsMentioned: ["chatgpt", "claude", "deepseek"],
    date: "2026-06-02",
  },


  {
    slug: "codegraph-open-source-knowledge-graphs",
    title: "CodeGraph: Open-Source Tool to Supercharge AI Coding Agents with Knowledge Graphs",
    titleZh: "CodeGraph：用知识图谱为AI编程代理加速的开源工具",
    description: "CodeGraph is an open-source project with 28.5k GitHub stars that creates a structured knowledge graph of your codebase, reducing AI tool calls by 17x and cutting costs by 35%.",
    descriptionZh: "CodeGraph是一个拥有28.5k GitHub星标的开源项目，为你的代码库创建结构化知识图谱，将AI工具调用减少17倍，成本降低35%。",
    category: "ai-tools",
    tags: ["codegraph", "knowledge-graph", "ai-coding", "open-source", "claude-code"],
    difficulty: "intermediate",
    toolsMentioned: ["codegraph", "claude"],
    date: "2026-06-03",
  },

  {
    slug: "agent-skill-hit-rate",
    title: "How to Ensure Agent Skill Hit Rate When Skills Are Overwhelming",
    titleZh: "当技能数量过多时，如何确保代理技能命中率",
    description: "As your AI Agent's skill set grows, accuracy plummets. Learn 4 practical strategies — optimized descriptions, skill trees, negative samples, and recall-rerank — to maintain high hit rates.",
    descriptionZh: "随着AI Agent技能集的增长，命中率会急剧下降。学习4个实用策略——优化描述、技能树、负样本和召回重排序——来保持高命中率。",
    category: "ai-tutorials",
    tags: ["ai-agent", "skills", "routing", "prompt-engineering", "rag"],
    difficulty: "intermediate",
    toolsMentioned: ["claude"],
    date: "2026-06-03",
  },

  {
    slug: "connect-deepseek-to-claude-code",
    title: "Step-by-Step Guide: Connect DeepSeek LLM to Claude Code for Cost-Effective Local & Cloud Development",
    titleZh: "分步指南：将DeepSeek LLM连接到Claude Code，实现高性价比的本地与云端开发",
    description: "A production-ready guide to integrating DeepSeek into Claude Code. Covers API key setup, bridge script building, parameter tuning, and verification testing for overseas developers.",
    descriptionZh: "将DeepSeek集成到Claude Code的生产级指南。涵盖API密钥设置、桥接脚本构建、参数调优和验证测试，面向海外开发者。",
    category: "ai-tutorials",
    tags: ["deepseek", "claude-code", "api-integration", "cost-optimization", "overseas-development"],
    difficulty: "intermediate",
    toolsMentioned: ["claude", "deepseek"],
    date: "2026-06-03",
  },

  {
    slug: "claude-code-9-skill-framework",
    title: "Unlock Team Potential with Claude Code's 9-Skill Framework for AI-Driven Development",
    titleZh: "用Claude Code的9技能框架释放团队潜力，实现AI驱动开发",
    description: "Claude Code team engineer Thariq's 9-skill framework maps the entire development lifecycle — awareness, production, validation, and delivery. Learn to turn tacit knowledge into reusable assets.",
    descriptionZh: "Claude Code团队工程师Thariq的9技能框架覆盖整个开发生命周期——认知、生产、验证和交付。学习将隐性知识转化为可复用的资产。",
    category: "ai-tutorials",
    tags: ["claude-code", "skills", "framework", "team-productivity", "ai-development", "devops"],
    difficulty: "intermediate",
    toolsMentioned: ["claude"],
    date: "2026-06-03",
  },

  {
    slug: "design-md-trae-framework-guide",
    title: "Elevate AI Design Aesthetics with DESIGN.md: A Practical Guide for TRAE Framework",
    titleZh: "用DESIGN.md提升AI设计美学：TRAE框架实战指南",
    description:
      "Learn how to use DESIGN.md and the frontend-design skill to transform AI-generated interfaces from generic to polished with the TRAE framework.",
    descriptionZh:
      "学习如何使用DESIGN.md和前端设计技能，借助TRAE框架将AI生成的界面从千篇一律转变为精致专业。",
    category: "ai-tutorials",
    tags: ["design", "trae", "design-md", "frontend-design", "ai-design", "tutorial"],
    difficulty: "intermediate",
    toolsMentioned: ["claude", "cursor", "trae-framework", "design-md"],
    date: "2026-06-04",
  },

  {
    slug: "free-access-codex-hermes-guide",
    title: "Free Access to Codex, Hermes, and More: A Practical Guide for Overseas Users",
    titleZh: "免费使用Codex、Hermes等AI工具：海外用户实用指南",
    description:
      "A practical guide to accessing Codex, Hermes, and more AI tools for free using the Agnes API. Step-by-step setup for overseas website owners.",
    descriptionZh:
      "使用Agnes API免费访问Codex、Hermes等AI工具的实用指南。面向海外网站拥有者的分步设置教程。",
    category: "ai-tutorials",
    tags: ["codex", "hermes", "agnes", "free-ai", "api", "overseas"],
    difficulty: "beginner",
    toolsMentioned: ["codex-agent", "hermes-agent"],
    date: "2026-06-04",
  },

  {
    slug: "mastering-cc-switch-ai-coding",
    title: "Mastering CC Switch: The Ultimate Tool for Managing AI Coding Tools",
    titleZh: "掌握CC Switch：管理AI编程工具的终极利器",
    description:
      "A complete guide to CC Switch, the cross-platform desktop app for managing multiple AI coding tools like Claude Code, Codex, and Gemini CLI.",
    descriptionZh:
      "CC Switch完整指南，这是一款跨平台桌面应用，用于统一管理Claude Code、Codex和Gemini CLI等多个AI编程工具。",
    category: "ai-tools",
    tags: ["cc-switch", "ai-coding", "tool-management", "claude-code", "codex", "gemini"],
    difficulty: "beginner",
    toolsMentioned: ["claude", "cc-switch"],
    date: "2026-06-04",
  },

  {
    slug: "vibecoding-workflow-110k-stars",
    title: "Vibecoding Workflow: The 110K Star Open-Source Tool for AI-Powered Coding",
    titleZh: "Vibecoding工作流：11万星标的AI编程开源工具",
    description:
      "Explore Vibecoding, the 110K+ GitHub star open-source workflow with 28 agents, 125 skills, and 60 commands for supercharging AI-powered development.",
    descriptionZh:
      "探索Vibecoding——拥有11万+GitHub星标的开源AI编程工作流，包含28个代理、125项技能和60个命令，为AI驱动开发加速。",
    category: "ai-tools",
    tags: ["vibecoding", "open-source", "ai-coding", "agents", "skills", "workflow"],
    difficulty: "beginner",
    toolsMentioned: ["claude", "vibecoding"],
    date: "2026-06-04",
  },
  {
    slug: "6-trending-github-ai-projects-beginners",
    title: "6 Trending GitHub AI Projects for Absolute Beginners: Easy Local Setup Tutorial",
    titleZh: "6个最热GitHub AI项目：绝对新手也能轻松本地部署",
    description:
      "Six hot open-source AI tools from GitHub trending list, with simplified installation steps for beginners with zero coding background to run on regular laptops.",
    descriptionZh:
      "精选GitHub热门趋势榜上的6个开源AI工具，为零编程基础的新手提供简化安装步骤，普通笔记本就能跑。",
    category: "ai-tutorials",
    tags: ["github", "open-source", "local-setup", "beginner", "tutorial", "ai-trending"],
    difficulty: "beginner",
    toolsMentioned: ["claude"],
    date: "2026-06-05",
  },

  {
    slug: "mastering-claude-design-presentations",
    title: "Mastering Claude Design for AI Beginners: Create Interactive, Editable Presentations Easily",
    titleZh: "掌握Claude Design：AI新手也能轻松制作交互式可编辑演示文稿",
    description:
      "Step-by-step guide to Claude Design — create professional, interactive presentations with AI prompts. No coding or design skills needed.",
    descriptionZh:
      "Claude Design分步指南——用AI提示词创建专业的交互式演示文稿，无需编程或设计技能。",
    category: "ai-tutorials",
    tags: ["claude-design", "presentation", "ai-tools", "design", "beginner", "tutorial"],
    difficulty: "beginner",
    toolsMentioned: ["claude", "claude-design"],
    date: "2026-06-05",
  },

  {
    slug: "vibe-coding-build-with-ai",
    title: "Vibe Coding: Build Software by Talking to AI – A Practical Guide for Beginners",
    titleZh: "Vibe Coding：和AI聊天就能开发软件——新手实战指南",
    description:
      "Learn Vibe Coding — build applications by communicating your ideas to AI. Practical steps from setup to deployment for absolute beginners.",
    descriptionZh:
      "学习Vibe Coding——通过向AI表达想法来构建应用程序。从零开始到部署的实战步骤。",
    category: "ai-tutorials",
    tags: ["vibe-coding", "ai-coding", "claude-code", "cursor", "beginner", "software-development"],
    difficulty: "beginner",
    toolsMentioned: ["claude", "cursor", "chatgpt", "vibecoding"],
    date: "2026-06-05",
  },


  {
    slug: "google-gemma-4-12b-local-deployment",
    title: "Google's Gemma 4 12B: Revolutionizing AI with Local Deployment on 16GB Laptops",
    titleZh: "Google Gemma 4 12B：在16GB笔记本上本地部署的AI革命",
    description:
      "Google DeepMind's Gemma 4 12B runs offline on a 16GB RAM laptop. Learn how this open-source multimodal model transforms overseas AI projects with local deployment, cost savings, and privacy compliance.",
    descriptionZh:
      "Google DeepMind的Gemma 4 12B可在16GB内存笔记本上离线运行。了解这款开源多模态模型如何通过本地部署、成本节省和隐私合规来改变海外AI项目。",
    category: "ai-news",
    tags: ["gemma", "google", "local-ai", "open-source", "multimodal", "offshore"],
    difficulty: "beginner",
    toolsMentioned: ["gemini", "gemma"],
    date: "2026-06-05",
  },

  {
    slug: "enhance-claude-code-customizations",
    title: "Enhance Your Claude Code Experience with Practical Tools and Customizations",
    titleZh: "用实用工具和自定义增强你的Claude Code体验",
    description:
      "Extend Claude Code with MCP tools for web search, webpage parsing, and image recognition, plus customize the HUD plugin for Coding Plan monitoring.",
    descriptionZh:
      "用MCP工具扩展Claude Code实现网页搜索、页面解析和图像识别，以及自定义HUD插件监控Coding Plan使用情况。",
    category: "ai-tutorials",
    tags: ["claude-code", "mcp", "customization", "tools", "productivity"],
    difficulty: "intermediate",
    toolsMentioned: ["claude"],
    date: "2026-06-06",
  },

  {
    slug: "claude-code-automate-while-sleep",
    title: "How to Let Claude Code Automate Tasks While You Sleep: A Practical Guide to Boosting Productivity",
    titleZh: "如何在睡眠中让Claude Code自动完成任务：提升生产力的实用指南",
    description:
      "Master Claude Code's /goal, /loop, /batch, /simplify, /debug, and /doctor commands to automate development tasks autonomously.",
    descriptionZh:
      "掌握Claude Code的/goal、/loop、/batch、/simplify、/debug和/doctor命令，自主自动化开发任务。",
    category: "ai-use-cases",
    tags: ["claude-code", "automation", "productivity", "autonomous", "commands"],
    difficulty: "beginner",
    toolsMentioned: ["claude"],
    date: "2026-06-06",
  },

  {
    slug: "claude-code-zero-to-hero-beginners",
    title: "Claude Code Zero-to-Hero: A 9-Minute Practical Guide for Beginners",
    titleZh: "Claude Code从零到精通：9分钟初学者实战指南",
    description:
      "Learn Claude Code from zero in 9 minutes — write, debug, and automate code using natural language. A beginner-friendly guide with hands-on Python examples.",
    descriptionZh:
      "9分钟从零学会Claude Code——用自然语言写代码、调试和自动化。包含动手Python示例的初学者友好指南。",
    category: "ai-tutorials",
    tags: ["claude-code", "beginner", "python", "debugging", "automation", "command-line"],
    difficulty: "beginner",
    toolsMentioned: ["claude"],
    date: "2026-06-12",
  },

  {
    slug: "vibe-coding-ai-beginners-step-by-step",
    title: "Vibe Coding for AI Beginners: Build Software by Talking to AI (Step-by-Step Guide)",
    titleZh: "Vibe Coding AI 入门：通过和 AI 对话构建软件（一步步指南）",
    description:
      "Learn Vibe Coding step by step — build functional software by talking to AI. Zero coding experience required. Complete guide from setup to deployment.",
    descriptionZh:
      "一步步学习 Vibe Coding——通过和 AI 对话来构建功能性软件。无需任何编程经验。从环境搭建到部署的完整指南。",
    category: "ai-tutorials",
    tags: ["vibe-coding", "ai-coding", "claude-code", "cursor", "beginner", "software-development"],
    difficulty: "beginner",
    toolsMentioned: ["claude", "cursor", "chatgpt", "vibecoding"],
    date: "2026-06-06",
  },


  {
    slug: "ai-core-terminology-workflows-beginners",
    title: "AI Core Terminology & Practical Workflows: A Beginner's Complete Guide",
    titleZh: "AI核心术语与实用工作流程：初学者完整指南",
    description: "Master essential AI concepts: Token, Context Window, Prompt, RAG, MCP, Agent, Workflow and more -- with practical commands and code examples for Claude Code.",
    descriptionZh: "掌握核心AI概念：Token、上下文窗口、提示词、RAG、MCP、Agent、工作流等——附带Claude Code实用命令和代码示例。",
    category: "ai-basics",
    tags: ["ai-basics", "terminology", "beginner-guide", "llm", "rag", "mcp", "agent", "workflow"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt", "claude", "gemini"],
    date: "2026-06-07",
  },
  {
    slug: "github-10k-star-thinking-styles",
    title: "GitHub 10K Star Open-Source Gem: Embodying Top Minds Thinking Styles",
    titleZh: "GitHub万星开源项目：体现顶尖思维风格的全能工具",
    description: "Discover the 10K-star GitHub project that embodies thinking styles of top minds like Karpathy. Practical guide for AI developers and overseas entrepreneurs.",
    descriptionZh: "探索这个万星GitHub项目，它体现了Karpathy等顶尖人才的思维风格。",
    category: "ai-tools",
    tags: ["github","open-source","thinking-styles","ai-agents","productivity"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt","claude"],
    date: "2026-06-08",
  },
  {
    slug: "professional-era-ai-skills-workflows",
    title: "The Professional Era of AI Skills: Master GitHub Trending Skill Workflows",
    titleZh: "AI技能的专业时代：掌握GitHub热门技能工作流",
    description: "Learn how to leverage trending GitHub skill workflows for practical AI development.",
    descriptionZh: "学习如何利用GitHub热门技能工作流进行实用AI开发。",
    category: "ai-tutorials",
    tags: ["skills","workflows","github","claude-code","productivity","ai-development"],
    difficulty: "intermediate",
    toolsMentioned: ["claude"],
    date: "2026-06-08",
  },
  {
    slug: "token-aggregation-distribution-ai-trend",
    title: "Token Aggregation and Distribution: An Inevitable Trend in the AI Industry",
    titleZh: "Token聚合与分发：AI行业的必然趋势",
    description: "Why token aggregation and distribution is reshaping the AI industry.",
    descriptionZh: "为什么token聚合与分发正在重塑AI行业。",
    category: "ai-news",
    tags: ["token","aggregation","ai-industry","trend","business-model"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt","claude"],
    date: "2026-06-08",
  },
  {
    slug: "workflows-master-claude-design",
    title: "Master Claude Design Workflows: Interactive and Editable AI Design Guide",
    titleZh: "掌握Claude Design工作流：交互式可编辑AI设计指南",
    description: "A practical guide to Claude Design workflows for interactive AI-powered presentations.",
    descriptionZh: "Claude Design工作流实用指南，创建交互式AI驱动演示。",
    category: "ai-tutorials",
    tags: ["claude-design","workflows","interactive","presentations","ai-design"],
    difficulty: "intermediate",
    toolsMentioned: ["claude","claude-design"],
    date: "2026-06-08",
  },

  {
    slug: "anthropic-harness-dynamic-workflows",
    title: "Anthropic Harness Dynamic Workflows: Full Practical Guide for Claude Code Developers",
    titleZh: "Anthropic Harness动态工作流：Claude Code开发者完整实战指南",
    description: "Master Anthropic's Dynamic Workflow Harness for Claude Code -- parallel sub-agents, breakpoint resume, autonomous task orchestration, and practical startup commands.",
    descriptionZh: "掌握Anthropic为Claude Code推出的动态工作流Harness系统——并行子代理、断点续传、自主任务编排及实用启动命令。",
    category: "ai-tutorials",
    tags: ["claude-code", "dynamic-workflow", "harness", "multi-agent", "automation"],
    difficulty: "intermediate",
    toolsMentioned: ["claude"],
    date: "2026-06-07",
  },
  {
    slug: "2026-guide-personal-knowledge-base",
    title: "2026 Guide: Is There a Standard Answer for Personal Knowledge Bases?",
    titleZh: "2026年指南：个人知识库有标准答案吗？",
    description: "Practical implementation and optimization guide for AI-powered personal knowledge bases. Compare RAG, LLM Wiki, and hybrid approaches.",
    descriptionZh: "AI驱动的个人知识库实用实施与优化指南。对比RAG、LLM Wiki和混合方案。",
    category: "ai-tutorials",
    tags: ["knowledge-base","rag","llm-wiki","personal-ai","2026"],
    difficulty: "intermediate",
    toolsMentioned: ["chatgpt","claude"],
    date: "2026-06-08",
  },
  {
    slug: "hermes-profiles-multi-agent-team",
    title: "Hermes Profiles: Building a True Multi-Agent AI Team for Enhanced Productivity",
    titleZh: "Hermes Profiles：构建真正的多代理AI团队提升生产力",
    description: "Learn how Hermes Profiles enables true multi-agent AI collaboration. Build specialized AI teams for complex workflows.",
    descriptionZh: "了解Hermes Profiles如何实现真正的多代理AI协作。为复杂工作流构建专业化AI团队。",
    category: "ai-tools",
    tags: ["hermes","multi-agent","profiles","ai-team","productivity"],
    difficulty: "intermediate",
    toolsMentioned: ["hermes-agent"],
    date: "2026-06-08",
  },
  {
    slug: "write-effective-agents-md-codex",
    title: "The First Step to Making Codex Understand You: Write Effective AGENTS.md Files",
    titleZh: "让Codex理解你的第一步：编写有效的AGENTS.md文件",
    description: "Master the art of writing AGENTS.md files for Codex. Configure your AI coding agent with project context, rules, and preferences.",
    descriptionZh: "掌握为Codex编写AGENTS.md文件的技巧。用项目上下文、规则和偏好配置你的AI编程代理。",
    category: "ai-tutorials",
    tags: ["codex","agents-md","configuration","ai-coding","beginner"],
    difficulty: "beginner",
    toolsMentioned: ["codex-agent","claude"],
    date: "2026-06-08",
  },

  {
    slug: "cli-skill-browser-ai-automation",
    title: "CLI + Skill: A Browser AI Automation Framework to Bid Farewell to Repetitive Tasks",
    titleZh: "CLI + Skill：告别重复任务的浏览器AI自动化框架",
    description: "Learn how CLI tools and custom skills create a token-efficient browser automation framework -- with Playwright CLI, 0-token workflows, and practical examples.",
    descriptionZh: "学习如何使用CLI工具和自定义技能构建高效的浏览器自动化框架——包含Playwright CLI、零Token工作流和实战示例。",
    category: "ai-use-cases",
    tags: ["cli", "skill", "browser-automation", "playwright", "token-efficiency"],
    difficulty: "intermediate",
    toolsMentioned: ["claude"],
    date: "2026-06-07",
  },

  {
    slug: "agency-agents-chinese-version-100k",
    title: "Unleash the Power of AI Agents with the Chinese Version of agency-agents: Outperforming the Original with 100K+ Stars",
    titleZh: "用中文版agency-agents释放AI代理的力量：10万+Star超越原版",
    description: "Explore agency-agents open-source project with 215 expert AI roles, 17 integrated tools, and China-specific features that outperforms the original with 100K+ stars.",
    descriptionZh: "探索拥有215个AI专家角色、17个集成工具和中国专属功能的开源项目agency-agents，以10万+Star超越原版。",
    category: "ai-tools",
    tags: ["agency-agents", "ai-agents", "open-source", "github", "chinese-localization"],
    difficulty: "beginner",
    toolsMentioned: ["claude"],
    date: "2026-06-07",
  },

  {
    slug: "mastering-ai-programming-agents-2026",
    title: "Mastering AI Programming Agents: A Practical Guide to 6 Leading Tools in 2026",
    titleZh: "掌握AI编程代理：2026年六大领先工具实战指南",
    description:
      "Six AI programming agents are reshaping how developers write code in 2026. Compare Claude Code, Cursor, GitHub Copilot, Codex Agent, OpenClaw, and LangChain — with use cases, code examples, and selection criteria for overseas projects.",
    descriptionZh:
      "六款AI编程代理正在重塑2026年的开发方式。对比Claude Code、Cursor、GitHub Copilot、Codex Agent、OpenClaw和LangChain——包含实际用例、代码示例和海外项目选择标准。",
    category: "ai-tutorials",
    tags: ["ai-programming", "ai-agents", "claude-code", "cursor", "copilot", "codex", "openclaw", "langchain", "overseas-development"],
    difficulty: "intermediate",
    toolsMentioned: ["claude", "cursor", "github-copilot", "codex-agent", "openclaw", "langchain"],
    date: "2026-06-10",
  },

  {
    slug: "mastering-multi-agent-collaboration-patterns",
    title: "Mastering Multi-Agent Collaboration: A Practical Guide to 5 Core Patterns with Hands-On Code",
    titleZh: "掌握多智能体协作：5种核心模式与手把手代码实战",
    description:
      "Master five multi-agent collaboration patterns — Supervisor, Hierarchical, Swarm, Sequential Chain, and Network — with working code examples using LangGraph and AutoGen. Learn A2A protocol, MCP integration, and security best practices.",
    descriptionZh:
      "掌握五种多智能体协作模式——Supervisor、Hierarchical、Swarm、Sequential Chain和Network——附LangGraph和AutoGen的可运行代码示例。学习A2A协议、MCP集成和安全最佳实践。",
    category: "ai-tutorials",
    tags: ["multi-agent", "collaboration", "langgraph", "autogen", "ai-agents", "patterns", "overseas-development"],
    difficulty: "intermediate",
    toolsMentioned: ["langchain", "claude"],
    date: "2026-06-10",
  },
  {
    slug: "4-ai-memory-solutions-comparison",
    title: "4 Leading AI Memory Solutions: A Practical Guide to Choosing the Right One for Your Needs",
    titleZh: "四大AI记忆方案对比：选择最适合你的持久上下文方案",
    description:
      "Compare 4 leading AI memory solutions — Gbrain, Microsoft GraphRAG, Graphify, and Karpathy's LLM Wiki — with a 5-dimension comparison and practical selection guide for your specific use case.",
    descriptionZh:
      "对比4款领先的AI记忆方案——Gbrain、Microsoft GraphRAG、Graphify和Karpathy的LLM Wiki——附带5维对比和实用选择指南，帮你找到最适合的方案。",
    category: "ai-comparisons",
    tags: ["ai-memory", "gbrain", "graphrag", "graphify", "llm-wiki", "knowledge-base", "comparison"],
    difficulty: "intermediate",
    toolsMentioned: ["gbrain", "graphrag", "graphify", "llm-wiki", "lightrag"],
    date: "2026-06-11",
  },
  {
    slug: "ai-browser-automation-6-routes",
    title: "Exploring AI Browser Automation: 6 Technical Routes, Architecture, and Practical Selection",
    titleZh: "探索AI浏览器自动化：6条技术路线、架构与实用选择",
    description:
      "Browser automation tools fall into 6 core technical routes — CDP direct control, accessibility tree, screenshot recognition, cloud browsers, anti-detection browsing, and AI-native automation. Explore each route with practical tools and code examples.",
    descriptionZh:
      "浏览器自动化工具可归为6大核心技术路线——CDP直接控制、无障碍树交互、截图识别、云浏览器、反检测浏览和AI原生自动化。探索每条路线及实用工具和代码示例。",
    category: "ai-tutorials",
    tags: ["browser-automation", "playwright", "puppeteer", "cdp", "web-scraping", "ai-native", "overseas"],
    difficulty: "intermediate",
    toolsMentioned: ["playwright", "puppeteer", "stagehand", "camoufox", "scrapingbee", "browserbase", "browserless", "bug0"],
    date: "2026-06-11",
  },
  {
    slug: "skillclaw-ai-agents-self-evolving",
    title: "SkillClaw: Empowering AI Agents with Self-Evolving, Shareable Skills",
    titleZh: "SkillClaw：用自我进化的可共享技能赋能AI代理",
    description:
      "Alibaba's open-source SkillClaw enables AI agents to automatically refine, deduplicate, and share skills. Explore its architecture, two evolution engines, and practical setup guide for autonomous skill management.",
    descriptionZh:
      "阿里巴巴开源的SkillClaw让AI代理自动优化、去重和共享技能。探索其架构、两种进化引擎和自主技能管理的实际部署指南。",
    category: "ai-tools",
    tags: ["skillclaw", "self-evolving", "ai-agents", "open-source", "skills", "autonomous-learning"],
    difficulty: "intermediate",
    toolsMentioned: ["skillclaw"],
    date: "2026-06-11",
  },
  {
    slug: "huawei-ascend-deepseek-v4-breakthrough",
    title: "China's AI Breakthrough: How Huawei Ascend and DeepSeek V4 Redefine AI Computing Without NVIDIA",
    titleZh: "中国AI突破：华为昇腾与DeepSeek V4如何在没有NVIDIA的情况下重新定义AI计算",
    description:
      "China's collaboration between Huawei Ascend 950 chips and DeepSeek V4 LLM marks a new era of domestic AI computing, achieving 1/7 the cost of international alternatives.",
    descriptionZh:
      "华为昇腾950芯片与DeepSeek V4大语言模型的合作标志着国产AI计算的新纪元，成本仅为国际替代方案的七分之一。",
    category: "ai-news",
    tags: ["deepseek", "huawei", "ascend", "china-ai", "nvidia-free", "domestic-computing", "ai-chip"],
    difficulty: "beginner",
    toolsMentioned: ["deepseek"],
    date: "2026-06-12",
  },

  {
    slug: "large-cap-investment-dashboard-claude-code",
    title: "Build a Large-Cap Investment Research Dashboard with Claude Code: A Step-by-Step Guide",
    titleZh: "用Claude Code构建大盘投资研究仪表盘：分步指南",
    description:
      "Build a fully functional investment research dashboard with Claude Code in minutes. Pull real-time stock data, calculate financial metrics, and visualize trends for large-cap stocks.",
    descriptionZh:
      "用Claude Code在几分钟内构建一个功能完整的投资研究仪表盘。获取实时股票数据、计算财务指标并可视化大盘股趋势。",
    category: "ai-use-cases",
    tags: ["claude-code", "investment", "dashboard", "stock-market", "streamlit", "financial-analysis", "data-visualization"],
    difficulty: "intermediate",
    toolsMentioned: ["claude"],
    date: "2026-06-12",
  },
  {
    slug: "ai-wechat-mini-programs-guide",
    title: "A Practical Guide to Launching AI-Powered WeChat Mini Programs: Navigating Tools, Categories, and Compliance",
    titleZh: "AI驱动微信小程序上线实战指南：工具选择、类目选择与合规备案",
    description:
      "A comprehensive guide to launching AI-powered WeChat Mini Programs, covering essential tools, category selection, code upload, user authentication, ICP filing, and common pitfalls.",
    descriptionZh:
      "一份全面的AI驱动微信小程序上线指南，涵盖必备工具选择、类目选择、代码上传、用户认证、ICP备案和常见陷阱。",
    category: "ai-use-cases",
    tags: ["wechat", "mini-program", "ai-development", "compliance", "tutorial"],
    difficulty: "intermediate",
    toolsMentioned: [],
    date: "2026-06-14",
  },
  {
    slug: "claude-code-vs-codex-architecture",
    title: "Claude Code vs. Codex: Architecture Differences & Practical Selection Guide",
    titleZh: "Claude Code vs Codex：架构差异与实用选择指南",
    description:
      "A deep dive into the architectural differences between Claude Code and Codex — context-centric vs task-oriented harness designs — with practical comparison across 5 key workflows.",
    descriptionZh:
      "深入解析Claude Code与Codex的架构差异——上下文中心vs任务导向的Harness设计理念——通过5个关键工作流的实用对比。",
    category: "ai-comparisons",
    tags: ["claude-code", "codex", "architecture", "comparison", "harness", "ai-coding"],
    difficulty: "intermediate",
    toolsMentioned: ["claude", "codex-agent"],
    date: "2026-06-14",
  },
  {
    slug: "codex-8-new-features-this-month",
    title: "Codex: 8 New Game-Changing Features This Month for Developers",
    titleZh: "Codex：本月面向开发者的8个革命性新功能",
    description:
      "Codex transforms from a terminal AI coding tool into a versatile digital coworker with 8 groundbreaking features including Computer Use, browser comment commands, automations, and GPT-5.5.",
    descriptionZh:
      "Codex从终端AI编码工具转变为全能型数字同事，带来8个革命性功能，包括电脑操控、浏览器评论命令、自动化任务和GPT-5.5。",
    category: "ai-news",
    tags: ["codex", "openai", "gpt-5.5", "automation", "computer-use", "new-features"],
    difficulty: "beginner",
    toolsMentioned: ["codex-agent"],
    date: "2026-06-14",
  },
  {
    slug: "hermes-official-desktop-app-guide",
    title: "Hermes Official Desktop App: Beginner Setup & Common Pitfall Avoidance Guide",
    titleZh: "Hermes官方桌面应用：新手安装配置与常见避坑指南",
    description: "A practical guide to installing, configuring, and using the Hermes Official Desktop App. Covers pre-installation checks, environment preparation, core operations, and solutions to common pitfalls that beginners face.",
    descriptionZh: "一份实用的Hermes官方桌面应用安装、配置和使用指南。涵盖安装前检查、环境准备、核心操作以及新手常见问题的解决方案。",
    category: "ai-tools",
    tags: ["hermes-agent", "desktop-app", "installation", "beginner", "setup", "ai-agent", "configuration"],
    difficulty: "beginner",
    toolsMentioned: ["hermes-agent"],
    date: "2026-06-14",
  },

  {
    slug: "glm-5-vs-kimi-2-code-comparison",
    title: "GLM 5.2 vs. Kimi 2.7 Code: A Practical Comparison of Domestic AI Coding Models",
    titleZh: "GLM 5.2 vs Kimi 2.7 Code：国产AI编程模型实战对比",
    description:
      "A comprehensive, practical comparison of GLM 5.2 and Kimi 2.7 Code through frontend and backend testing scenarios — animation rendering, full-stack e-commerce development, and performance metrics across 6 domestic AI models.",
    descriptionZh:
      "通过前端和后端测试场景对 GLM 5.2 和 Kimi 2.7 Code 进行全面实战对比——动画渲染、全栈电商开发以及6款国产AI模型的性能指标。",
    category: "ai-comparisons",
    tags: ["glm-5", "kimi-2", "ai-comparison", "coding", "domestic-ai", "frontend", "backend"],
    difficulty: "intermediate",
    toolsMentioned: ["glm-5", "kimi-2", "deepseek"],
    date: "2026-06-14",
  },

  {
    slug: "ai-agent-sandbox-guide",
    title: "AI Agent Sandbox: A Practical Guide to Secure Autonomous Action",
    titleZh: "AI Agent沙箱：安全自主行动的实践指南",
    description:
      "A comprehensive guide to AI Agent sandboxing covering microVM isolation, dynamic policy control with OPA, state snapshots, and OpenTelemetry observability — everything you need to deploy autonomous AI agents safely.",
    descriptionZh:
      "AI Agent沙箱完整实践指南，涵盖微虚拟机隔离、OPA动态策略控制、状态快照和OpenTelemetry可观测性——安全部署自主AI代理所需的全部知识。",
    category: "ai-tutorials",
    tags: ["ai-agent", "sandbox", "security", "firecracker", "opa", "opentelemetry", "e2b"],
    difficulty: "intermediate",
    toolsMentioned: ["e2b", "firecracker", "langchain", "langgraph", "autogen", "opentelemetry", "open-policy-agent"],
    date: "2026-06-15",
  },

  {
    slug: "multi-agent-system-long-task",
    title: "Building a Practical Multi-Agent System for Unattended Long-Task Execution",
    titleZh: "构建实用的多代理系统：无人值守长任务执行",
    description:
      "A practical case study of building a multi-agent system that ran unattended for 4 days, generating 140K lines of code — covering graph-based orchestration, YAML pipelines, Scorecard auditing, and Docker-based agent isolation.",
    descriptionZh:
      "构建多代理系统无人运行4天、生成14万行代码的实战案例——涵盖图编排、YAML管道、Scorecard审计和Docker代理隔离。",
    category: "ai-tutorials",
    tags: ["multi-agent", "orchestration", "codex", "docker", "automation", "yaml", "pipeline"],
    difficulty: "advanced",
    toolsMentioned: ["codex", "docker", "puppeteer"],
    date: "2026-06-15",
  },

  {
    slug: "harness-engineering-guide",
    title: "Harness Engineering: Empowering AI to Deliver Complete Projects with Practical Implementation",
    titleZh: "Harness工程：赋能AI交付完整项目的实战指南",
    description: "A comprehensive guide to Harness Engineering — the systematic approach to structuring AI development with context architecture, task orchestration, feedback mechanisms, and architectural guardrails for reliable end-to-end project delivery.",
    descriptionZh: "Harness工程完整指南——通过上下文架构、任务编排、反馈机制和架构护栏构建可靠的AI开发体系，实现端到端项目交付。",
    category: "ai-tutorials",
    tags: ["harness-engineering", "ai-development", "context-architecture", "task-orchestration", "codex", "workflow"],
    difficulty: "intermediate",
    toolsMentioned: ["codex", "cursor", "puppeteer", "husky"],
    date: "2026-06-16",
  },
  {
    slug: "small-models-2026-opportunity",
    title: "Seize the 2026 AI Opportunity: Small Models Are the Gateway for Ordinary People",
    titleZh: "抓住2026年AI机遇：小模型是普通人的入场券",
    description: "How fine-tuning small open-source models (1B-4B parameters) with tools like Unsloth and Qwen on Google Colab can outperform giant models at a fraction of the cost — practical roadmap with code examples.",
    descriptionZh: "如何使用Unsloth和Qwen在Google Colab上微调小型开源模型（1B-4B参数），以极低成本超越巨型模型——含代码示例的实操路线图。",
    category: "ai-tutorials",
    tags: ["small-models", "fine-tuning", "unsloth", "qwen", "google-colab", "lora"],
    difficulty: "beginner",
    toolsMentioned: ["unsloth", "qwen", "google-colab", "codex", "deepseek"],
    date: "2026-06-16",
  },


  {
    slug: "mastering-app-dev-with-codex",
    title: "Mastering App Development with Codex: A Step-by-Step Guide from Zero to App Store Launch",
    titleZh: "用Codex掌握应用开发：从零到App Store上架的逐步指南",
    description: "A hands-on tutorial building an AI nail art try-on app with Codex — covering Superpower for planning, Expo/React Native for frontend, Supabase for backend, and TestFlight deployment to the App Store.",
    descriptionZh: "用Codex构建AI美甲试戴应用的实操教程——涵盖Superpower规划、Expo/React Native前端、Supabase后端和TestFlight上架App Store。",
    category: "ai-tutorials",
    tags: ["codex", "app-development", "expo", "react-native", "supabase", "ios", "mobile"],
    difficulty: "intermediate",
    toolsMentioned: ["codex", "superpower", "expo", "react-native", "supabase", "openai"],
    date: "2026-06-17",
  },
  {
    slug: "claude-code-free-unlimited-guide",
    title: "How to Use Claude Code for Free (Unlimited Access): A Step-by-Step Practical Guide",
    titleZh: "如何免费使用Claude Code（无限制访问）：逐步实操指南",
    description: "A complete guide to using Claude Code completely free with no limits — covering web interface, VS Code integration, batch processing, multi-file projects, and common pitfalls with code examples.",
    descriptionZh: "完全免费无限制使用Claude Code的完整指南——涵盖Web界面、VS Code集成、批量处理、多文件项目和常见陷阱，含代码示例。",
    category: "ai-tutorials",
    tags: ["claude-code", "free", "vscode", "coding-assistant", "debugging", "beginner"],
    difficulty: "beginner",
    toolsMentioned: ["claude", "vscode"],
    date: "2026-06-17",
  },

  {
    slug: "open-source-claude-design-local-deploy",
    title: "Open-Source Claude Design Local Deployment Guide: Free Self-Hosted AI UI Design Tool",
    titleZh: "开源Claude Design本地部署指南：免费自托管AI UI设计工具",
    description: "A complete guide to deploying the open-source Claude Design locally on your PC for unlimited, free AI-powered UI design generation — covering environment setup, model configuration, and common pitfalls.",
    descriptionZh: "在本地PC上部署开源Claude Design的完整指南——实现无限免费AI界面设计生成，涵盖环境配置、模型对接和常见问题解决。",
    category: "ai-tutorials",
    tags: ["claude-design", "self-hosted", "open-source", "ollama", "deployment", "beginner"],
    difficulty: "beginner",
    toolsMentioned: ["ollama", "claude-design"],
    date: "2026-06-18",
  },
  {
    slug: "one-claude-code-two-roles",
    title: "One Claude Code, Two Roles: Code Writing and Reviewing Without Codex",
    titleZh: "一个Claude Code，两种角色：无需Codex也能写代码和审代码",
    description: "Learn how to use a single Claude Code model to both write and review code by leveraging isolated contexts and a dedicated code-review agent — no Codex required.",
    descriptionZh: "学习如何通过隔离上下文和专用代码审查代理，用一个Claude Code模型同时完成代码编写和审查——无需Codex。",
    category: "ai-tutorials",
    tags: ["claude-code", "code-review", "agent", "productivity", "workflow"],
    difficulty: "intermediate",
    toolsMentioned: ["claude", "codex"],
    date: "2026-06-18",
  },

  {
    slug: "codex-domestic-ai-models",
    title: "How to Use Codex with Domestic AI Models: A Practical Guide for Everyone",
    titleZh: "Codex搭配国产AI模型使用指南：人人都能用的实操教程",
    description: "Step-by-step guide to configuring Codex with domestic AI models like DeepSeek V4 and Mimo v2.5 using CC Switch — no ChatGPT account or special network setup needed.",
    descriptionZh: "通过CC Switch配置Codex使用DeepSeek V4等国产AI模型的逐步教程——无需ChatGPT账号或特殊网络环境。",
    category: "ai-tutorials",
    tags: ["codex", "deepseek", "cc-switch", "coding", "api", "beginner"],
    difficulty: "beginner",
    toolsMentioned: ["codex", "cc-switch", "deepseek"],
    date: "2026-06-19",
  },
  {
    slug: "long-running-ai-coding-glm-claude",
    title: "Mastering Long-Running AI Coding Tasks with GLM 5.2 and Claude Code",
    titleZh: "用GLM 5.2和Claude Code驾驭长时间AI编程任务",
    description: "A practical case study on running 13-hour AI coding sessions with GLM 5.2's million-token context and Claude Code's goal command for large-scale project porting.",
    descriptionZh: "实战案例：利用GLM 5.2的百万Token上下文和Claude Code的goal命令，运行13小时AI编码任务完成大型项目迁移。",
    category: "ai-tutorials",
    tags: ["glm-5", "claude-code", "long-context", "coding", "workflow", "advanced"],
    difficulty: "advanced",
    toolsMentioned: ["claude", "codex"],
    date: "2026-06-19",
  },

  {
    slug: "claude-dynamic-workflows",
    title: "Claude Dynamic Workflows: Transform One AI into a Team of 100 for Explosive Productivity",
    titleZh: "Claude动态工作流：把一个AI变成百人团队，效率爆炸提升",
    description: "Learn how Claude's Dynamic Workflows feature turns a solo AI assistant into a project manager that orchestrates hundreds of sub-agents in parallel — 10x efficiency for research, writing, and coding.",
    descriptionZh: "了解Claude动态工作流如何将单人AI助手变成能并行调度数百个子代理的项目经理——研究、写作、编码效率提升10倍。",
    category: "ai-tutorials",
    tags: ["claude", "workflow", "productivity", "agent", "parallel"],
    difficulty: "intermediate",
    toolsMentioned: ["claude"],
    date: "2026-06-20",
  },
  {
    slug: "codex-complete-guide-domestic",
    title: "Codex Complete Guide for Domestic Users: Full Installation + Official Plugins Setup (Step-by-Step)",
    titleZh: "Codex国内用户完整指南：安装+官方插件配置全流程（手把手）",
    description: "A spoon-feeding guide for Chinese developers to install Codex with domestic AI models, activate all 8+ official plugins, and troubleshoot common issues — no VPN needed.",
    descriptionZh: "面向国内开发者的手把手教程：用国产AI模型安装Codex、激活全部8+官方插件、解决常见问题——无需VPN。",
    category: "ai-tutorials",
    tags: ["codex", "deepseek", "coding", "plugins", "domestic", "beginner"],
    difficulty: "beginner",
    toolsMentioned: ["codex", "deepseek"],
    date: "2026-06-20",
  },

  {
    slug: "6-practical-claude-code-plugins",
    title: "6 Practical Claude Code Plugins for Boosting Productivity in Real Projects",
    titleZh: "6个实用的Claude Code插件：真实项目中提升效率",
    description: "Discover 6 underrated yet highly practical Claude Code plugins — Grill Me, Codex, Graphify, Claude Obsidian, NotebookLM CLI, and Impeccable — that solve real development problems from planning to frontend polish.",
    descriptionZh: "发现6个被低估但极其实用的Claude Code插件——Grill Me、Codex、Graphify、Claude Obsidian、NotebookLM CLI和Impeccable——从规划到前端美化解决真实开发问题。",
    category: "ai-tutorials",
    tags: ["claude-code", "plugins", "productivity", "code-review", "graphify"],
    difficulty: "intermediate",
    toolsMentioned: ["claude", "codex", "graphify"],
    date: "2026-06-21",
  },
  {
    slug: "demystifying-ai-engineering-function-calling-skills-mcp",
    title: "Demystifying AI Engineering: Function Calling, Skills, and MCP",
    titleZh: "揭秘AI工程：Function Calling、Skills和MCP的层次架构",
    description: "A clear breakdown of the three core AI engineering concepts — Function Calling (microscopic action layer), Skills (mesoscopic module layer), and MCP (macroscopic integration layer) — with practical code examples.",
    descriptionZh: "清晰拆解AI工程三大核心概念——Function Calling（微观动作层）、Skills（中观模块层）和MCP（宏观集成层）——附实战代码示例。",
    category: "ai-basics",
    tags: ["function-calling", "skills", "mcp", "ai-engineering", "architecture"],
    difficulty: "intermediate",
    toolsMentioned: [],
    date: "2026-06-21",
  },

  {
    slug: "codex-superpowers-transform-coding",
    title: "Codex Superpowers: Transform Your AI Coding from Random to Engineering-Grade",
    titleZh: "Codex超能力：将AI编码从随机输出升级为工程级别",
    description: "A 210k-star open-source tool transforms Codex (and Claude Code, Gemini CLI, Cursor, Copilot) from a code-slinging machine into a disciplined software engineer with requirements gathering, TDD, and sub-agent driven development.",
    descriptionZh: "一个21万Star的开源工具将Codex（及Claude Code、Gemini CLI、Cursor、Copilot）从代码机器转变为遵循需求澄清→实现规划→TDD→子代理开发的 disciplined 软件工程师。",
    category: "ai-tutorials",
    tags: ["codex", "tdd", "sub-agents", "requirements", "code-review", "engineering"],
    difficulty: "intermediate",
    toolsMentioned: ["codex-agent", "claude", "cursor", "github-copilot"],
    date: "2026-06-22",
  },
  {
    slug: "upgrade-obsidian-ai-dashboard",
    title: "Upgrade Your Obsidian Homepage: Build AI-Powered Smart Dashboard for Knowledge Workflow",
    titleZh: "升级Obsidian首页：构建AI驱动智能仪表盘赋能知识工作流",
    description: "Replace your static DataviewJS Obsidian homepage with an AI-powered dashboard that connects Claude Code, Codex, RSS feeds, and GitHub — with one-click deep research, auto-tagging, and vault health inspection.",
    descriptionZh: "用AI驱动的仪表盘取代静态DataviewJS Obsidian首页，连接Claude Code、Codex、RSS源和GitHub——实现一键深度研究、自动标签和知识库健康检查。",
    category: "ai-tutorials",
    tags: ["obsidian", "dashboard", "claude-code", "codex", "plugin", "knowledge-base"],
    difficulty: "advanced",
    toolsMentioned: ["claude", "codex-agent"],
    date: "2026-06-22",
  },

  {
    slug: "minimax-m3-flagship-multimodal-agent",
    title: "MiniMax M3: The Flagship AI Model Merging Coding, Multimodality, and Agent Capabilities",
    titleZh: "MiniMax M3：融合编程、多模态和Agent能力的旗舰AI模型",
    description: "Hands-on benchmark of MiniMax M3 — the first open-source model combining native multimodality, million-token context, and agent capabilities — tested across 5 scenarios including 3D maze, pocket watch animation, keyframe extraction, and custom computer-use agents.",
    descriptionZh: "MiniMax M3实操评测——首个融合原生多模态、百万token上下文和Agent能力的开源模型——5大场景实测：3D迷宫、怀表拆解动画、关键帧提取、自定义Computer-Use Agent。",
    category: "ai-comparisons",
    tags: ["minimax", "multimodal", "agent", "threejs", "computer-use", "benchmark", "chinese-model"],
    difficulty: "intermediate",
    toolsMentioned: ["minimax-m3", "claude", "deepseek"],
    date: "2026-06-23",
  },
  {
    slug: "github-vibe-coding-backend-workflow",
    title: "GitHub as the Core Backend for Vibe Coding: Full Setup & Collaborative AI Development Workflow",
    titleZh: "GitHub作为Vibe Coding核心后端：完整配置与协作AI开发工作流",
    description: "Complete guide to integrating GitHub as Vibe Coding's backend — PAT setup, repo binding, version-controlled AI code iteration, community template imports, and GitHub Actions CI/CD for auto-deploying AI-generated code.",
    descriptionZh: "将GitHub集成为Vibe Coding后端的完整指南——PAT配置、仓库绑定、版本控制AI代码迭代、社区模板导入、GitHub Actions CI/CD自动部署AI生成代码。",
    category: "ai-tutorials",
    tags: ["github", "vibe-coding", "ci-cd", "version-control", "collaboration", "workflow"],
    difficulty: "beginner",
    toolsMentioned: ["vibecoding", "github-copilot"],
    date: "2026-06-23",
  },

  {
    slug: "mastering-ai-agent-tool-orchestration-meta-tools",
    title: "Mastering AI Agent Tool Orchestration: The Power of Meta-Tools in Modern Workflows",
    titleZh: "掌握AI Agent工具编排：Meta-Tools在现代工作流中的力量",
    description: "How meta-tools like web-tools-guide dominate AI skill marketplaces by solving tool orchestration — with a practical 4-step framework for primary tool selection, fallback mechanisms, user transparency, and bilingual trigger coverage, achieving 10x cost reduction.",
    descriptionZh: "Meta-Tools如web-tools-guide如何通过解决工具编排问题主导AI技能市场——包含主工具选择、降级机制、用户透明度和双语触发覆盖的4步实操框架，实现10倍成本降低。",
    category: "ai-tutorials",
    tags: ["agent", "tool-orchestration", "meta-tools", "workflow", "cost-optimization", "fallback"],
    difficulty: "intermediate",
    toolsMentioned: [],
    date: "2026-06-24",
  },
  {
    slug: "effective-multi-agent-collaboration-4-structures",
    title: "Effective Multi-Agent Collaboration: 4 Practical Structures Beyond Just Scaling Agents",
    titleZh: "高效多Agent协作：超越简单堆量的4种实用结构",
    description: "Stop just adding more agents — learn 4 proven collaboration structures (Orchestrator-Workers, Pipeline, Parallelization, Evaluator-Optimizer) with actionable code examples in Python, and when to use multi-agent vs single-agent approaches.",
    descriptionZh: "停止简单添加更多Agent——学习4种经过验证的协作结构（Orchestrator-Workers、Pipeline、Parallelization、Evaluator-Optimizer），附可操作的Python代码示例，以及何时使用多Agent vs 单Agent的决策指南。",
    category: "ai-tutorials",
    tags: ["multi-agent", "collaboration", "orchestrator", "pipeline", "parallelization", "evaluator-optimizer"],
    difficulty: "intermediate",
    toolsMentioned: ["claude", "minimax-m3"],
    date: "2026-06-24",
  },

  {
    slug: "codex-autocad-redraw-dwg-one-sentence",
    title: "Codex + AutoCAD: Redraw Complex DWG with Just One Sentence",
    titleZh: "Codex+AutoCAD：一句话重绘复杂DWG图纸",
    description: "How Codex integrates with AutoCAD's COM interface to automatically analyze layers, redraw complex DWG files, and perform quality inspection — all from a single command, reducing hours of manual CAD work to 90 seconds.",
    descriptionZh: "Codex如何通过AutoCAD COM接口自动分析图层、重绘复杂DWG文件并执行质量检查——只需一条命令，将数小时手动CAD工作缩减到90秒。",
    category: "ai-tutorials",
    tags: ["codex", "autocad", "dwg", "cad", "automation", "skill"],
    difficulty: "intermediate",
    toolsMentioned: ["codex-agent"],
    date: "2026-06-25",
  },
  {
    slug: "glm-5-2-coding-prowess-deep-dive",
    title: "GLM-5.2: A Deep Dive into Its Coding Prowess and Practical Insights",
    titleZh: "GLM-5.2：深度解析其编程实力与实战洞察",
    description: "Rigorous benchmark of GLM-5.2 vs GPT-5.5 and Claude Opus 4.8 across authentication migration and web full-stack projects — plus sentiment analysis of 6,690 community comments revealing why developers both love and hate it.",
    descriptionZh: "GLM-5.2 vs GPT-5.5和Claude Opus 4.8的严格基准测试——认证迁移和Web全栈两大实战项目+6,690条社区评论情感分析，揭示开发者爱恨交织的原因。",
    category: "ai-comparisons",
    tags: ["glm", "zhipu", "coding-benchmark", "backend", "security", "chinese-model"],
    difficulty: "intermediate",
    toolsMentioned: ["glm-5-2"],
    date: "2026-06-25",
  },

  {
    slug: "build-stable-data-storage-large-ai-projects-claude-code",
    title: "Build Stable Long-Term Data Storage for Large AI Projects With Claude Code",
    titleZh: "用Claude Code为大型AI项目构建稳定的长期数据存储",
    description: "A complete Node.js data persistence system for Claude Code agent tasks — auto-classification, timestamp naming, version snapshots with auto-cleanup, crash fault recovery, and one-click rollback to any historical state.",
    descriptionZh: "为Claude Code Agent任务构建完整的Node.js数据持久化系统——自动分类、时间戳命名、版本快照自动清理、崩溃故障恢复、一键回滚到任意历史状态。",
    category: "ai-tutorials",
    tags: ["claude-code", "data-storage", "nodejs", "persistence", "snapshot", "fault-recovery"],
    difficulty: "intermediate",
    toolsMentioned: ["claude"],
    date: "2026-06-26",
  },
  {
    slug: "claude-code-workflow-orchestrating-agent-teams",
    title: "Claude Code Workflow: From Writing Code to Orchestrating Agent Teams",
    titleZh: "Claude Code Workflow：从写代码到编排Agent团队",
    description: "Claude Code's major update — Workflow transforms solo coding into agent team orchestration with JavaScript scripts, 5-stage deep-research pipeline, budget control, and verifiable multi-agent coordination at scale.",
    descriptionZh: "Claude Code重大更新——Workflow将单人编码转变为Agent团队编排，JavaScript脚本驱动、5阶段深度研究流水线、预算控制、可验证的大规模多Agent协调。",
    category: "ai-news",
    tags: ["claude-code", "workflow", "agent-orchestration", "deep-research", "multi-agent", "anthropic"],
    difficulty: "beginner",
    toolsMentioned: ["claude"],
    date: "2026-06-26",
  },

  {
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

  {
    slug: "ai-infrastructure-revolution-bubble-computing-power",
    title: "AI Infrastructure: Revolution or Bubble? A Deep Dive into the Computing Power Ecosystem",
    titleZh: "AI基础设施：革命还是泡沫？算力生态深度解析",
    description: "A deep dive into the AI computing power ecosystem — from Nvidia DGX H100 servers, switches and optical modules, to liquid cooling and NVL72 cabinets. Understand the full supply chain behind the $690B AI infrastructure boom.",
    descriptionZh: "深度解析AI算力生态系统——从Nvidia DGX H100服务器、交换机和光模块，到液冷和NVL72机柜。理解6900亿美元AI基础设施热潮背后的完整供应链。",
    category: "ai-tutorials",
    tags: ["infrastructure", "nvidia", "hardware", "computing-power", "data-center", "supply-chain"],
    difficulty: "intermediate",
    toolsMentioned: [],
    date: "2026-06-28",
  },
  {
    slug: "codex-website-dev-zero-basis-tutorial",
    title: "Codex Website Development: Zero-Basis Practical Tutorial and Deployment Guide",
    titleZh: "Codex网站开发：零基础实战教程与部署指南",
    description: "Build a complete cat-themed website from scratch using Codex — two building methods (personalized and quick creative), image generation, animation effects, and one-click Vercel deployment. No coding experience required.",
    descriptionZh: "用Codex从零构建完整猫咪主题网站——两种搭建方法（个性化定制和快速创意）、图片生成、动画特效、一键Vercel部署。无需编程经验。",
    category: "ai-tutorials",
    tags: ["codex", "web-development", "website", "vercel", "beginner", "tutorial"],
    difficulty: "beginner",
    toolsMentioned: ["codex-agent", "vercel"],
    date: "2026-06-28",
  },

  {
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

  {
    slug: "demystifying-ai-application-layer-3-layers",
    title: "Demystifying AI Application Layer: From Large Language Models to Intelligent Agents in 3 Layers",
    titleZh: "拆解AI应用层：从大语言模型到智能Agent的三层金字塔",
    description: "A beginner-friendly guide to the 3-layer AI pyramid — LLM (brain), Multimodal (senses), Tools & Agents (skeleton) — plus how to build your own AI agent with Kouzi (Coze), no coding required.",
    descriptionZh: "面向初学者的三层AI金字塔指南——LLM（大脑）、多模态（感官）、工具与Agent（骨架）——附扣子无代码搭建AI Agent实战。",
    category: "ai-basics",
    tags: ["llm", "multimodal", "agent", "kouzi", "beginner", "pyramid", "workflow"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt", "gemini", "deepseek", "qwen", "nano-banana-pro", "midjourney", "veo-3-1", "suno", "heygen", "notebooklm", "kouzi"],
    date: "2026-06-30",
  },
  {
    slug: "2025-ai-toolkit-practical-guide-every-domain",
    title: "2025 AI Toolkit: A Practical Guide for Every Domain",
    titleZh: "2025 AI工具大全：全领域实战选型指南",
    description: "A comprehensive toolkit guide across 9 domains — text, image, video, audio, digital humans, browsers, coding, knowledge bases, and agents — with top picks, free alternatives, and open-source options for each category.",
    descriptionZh: "覆盖9大领域的全面工具选型指南——文本、图像、视频、音频、数字人、浏览器、编程、知识库和Agent——每类含首选推荐、免费替代和开源选项。",
    category: "ai-comparisons",
    tags: ["tools", "roundup", "comparison", "guide", "2025", "free"],
    difficulty: "beginner",
    toolsMentioned: ["gemini", "chatgpt", "claude", "grok", "qwen", "deepseek", "nano-banana-pro", "midjourney", "veo-3-1", "minimax-m3", "elevenlabs", "suno", "heygen", "cursor", "trae-framework", "codex-agent", "notebooklm", "kouzi", "runway"],
    date: "2026-06-30",
  },

  {
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

  {
    slug: "dont-be-intimidated-ai-jargon-practical-guide-concepts",
    title: "Don't Be Intimidated by AI Jargon: A Practical Guide to AI Concepts from ChatGPT to Workspace Agent",
    titleZh: "别被AI术语吓倒：从ChatGPT到Workspace Agent的AI概念实战指南",
    description: "A complete journey through 12 AI concepts — Token, Prompt Engineering, RAG, Tool Calling, MCP, Context Engineering, Skill, Computer Use, Agent, Harness Engineering, Workflow, and Workspace Agent — with code snippets and actionable tips for each.",
    descriptionZh: "12个AI概念的完整之旅——Token、提示词工程、RAG、工具调用、MCP、上下文工程、Skill、计算机使用、Agent、Harness工程、工作流和Workspace Agent——每个概念含代码示例和实操建议。",
    category: "ai-basics",
    tags: ["concepts", "beginner", "rag", "agent", "mcp", "workflow", "prompt-engineering", "guide"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt", "langchain", "n8n", "pinecone"],
    date: "2026-07-02",
  },

  {
    slug: "understanding-large-language-models-principles-architecture",
    title: "Understanding Large Language Models: Principles, Architecture, and Practical Usage",
    titleZh: "大语言模型深度解读：从Transformer原理到实战应用",
    description: "A comprehensive guide breaking down LLM core principles, Transformer architecture with PyTorch implementation, common limitations (hallucinations, context decay, math errors), and practical tips for choosing and using models effectively in real-world tasks.",
    descriptionZh: "从Transformer架构原理到PyTorch代码实现，全面解读大语言模型的核心机制、常见局限（幻觉、上下文衰减、数学错误）以及实际使用中的模型选择与提示技巧。",
    category: "ai-learning",
    tags: ["LLM", "Transformer", "PyTorch", "AI Architecture", "Prompt Engineering", "Deep Learning"],
    difficulty: "intermediate",
    toolsMentioned: ["PyTorch"],
    date: "2026-07-03",
  },
  {
    slug: "complete-guide-codex-zero-to-advanced",
    title: "Complete Guide to Codex: From Zero to Advanced Development Workflow",
    titleZh: "Codex完全指南：从零基础到高级开发工作流",
    description: "A step-by-step walkthrough of OpenAI Codex from installation and project setup through Git version control, agent.md configuration, Electron refactoring, plugins & skills, and mobile control — covering the complete development workflow for beginners and advanced users alike.",
    descriptionZh: "从安装配置、项目创建到Git版本控制、agent.md跨项目规则、Electron重构、插件与技能扩展、移动端控制，全方位覆盖Codex开发工作流的每一步操作。",
    category: "ai-tools",
    tags: ["Codex", "OpenAI", "AI Development", "CLI", "Git", "Electron", "Automation"],
    difficulty: "beginner",
    toolsMentioned: ["Codex Agent", "Electron"],
    date: "2026-07-03",
  },

  {
    slug: "ai-bubble-or-opportunity-guide-ordinary-people",
    title: "Is AI a Bubble or Opportunity? A Guide for Ordinary People to Navigate the AI Wave",
    titleZh: "AI是泡沫还是机遇？普通人应对AI浪潮的生存指南",
    description: "Using the 'survivor model' from the 2000 internet bubble (Foundation/Platform/Application layers), this guide maps today's AI landscape and presents three actionable opportunities for ordinary people — career enhancement, side hustles, and frontier innovation — ranked by risk level.",
    descriptionZh: "用2000年互联网泡沫的'幸存者模型'（基础层/平台层/应用层）映射当今AI格局，并按风险等级为普通人梳理三条可行路径——职业增强、副业创业和前沿创新。",
    category: "ai-news",
    tags: ["AI Bubble", "Investment", "Career", "AI Strategy", "Side Hustle", "Technology Trends"],
    difficulty: "beginner",
    toolsMentioned: ["ChatGPT", "Claude", "Midjourney"],
    date: "2026-07-04",
  },
  {
    slug: "top-5-ai-ppt-skills-tested-ranked",
    title: "Battle of the Best: Top 5 AI PPT Skills Tested and Ranked",
    titleZh: "AI PPT技能大比拼：5款工具实测排名与推荐",
    description: "A hands-on comparison of five popular AI PPT generation skills — PPT Master, Banana Slides, Frontend Slides, HTML PPT, and Guizang PPT — tested with the same prompt and ranked by Codex for content quality, design, and functionality.",
    descriptionZh: "用同一提示词实测5款热门AI PPT生成技能——PPT Master、Banana Slides、Frontend Slides、HTML PPT和Guizang PPT Skill，由Codex从内容质量、设计和功能三个维度综合排名。",
    category: "ai-tools",
    tags: ["PPT", "AI Presentation", "Productivity", "Codex Skills", "Comparison", "Tools Review"],
    difficulty: "beginner",
    toolsMentioned: ["Codex Agent"],
    date: "2026-07-04",
  },

  {
    slug: "2026-ai-agent-guide-choose-right-tool-beginners",
    title: "2026 AI Agent Guide: How to Choose the Right Tool for Beginners",
    titleZh: "2026 AI Agent选型指南：新手如何选择最适合的工具",
    description: "A ranked comparison of five mainstream AI Agent tools — Codex, Claude Code, OpenClaw, Hermes Agent, and TRAE — with pros, cons, and best-use recommendations to help beginners pick the right tool for their workflow.",
    descriptionZh: "五款主流AI Agent工具横向排名对比——Codex、Claude Code、OpenClaw、Hermes Agent和TRAE——含优缺点和最佳场景推荐，帮新手选出最适合自己工作流的工具。",
    category: "ai-tools",
    tags: ["AI Agent", "Codex", "Claude Code", "OpenClaw", "Tools Comparison", "Beginner Guide"],
    difficulty: "beginner",
    toolsMentioned: ["Codex Agent", "Claude Code", "OpenClaw", "Hermes Agent", "TRAE Framework"],
    date: "2026-07-05",
  },
  {
    slug: "tencent-workbuddy-ai-office-workbench",
    title: "Tencent WorkBuddy: The Ultimate AI Office Workbench for Everyday Work",
    titleZh: "腾讯WorkBuddy：日常办公的终极AI工作台深度评测",
    description: "A comprehensive review of Tencent WorkBuddy — a full-scenario AI office workbench featuring three working modes, multi-agent parallel execution, 20+ built-in skills, pre-configured expert teams, and mobile control via WeChat/QQ/Feishu.",
    descriptionZh: "腾讯WorkBuddy全面评测——全场景AI办公工作台，三种工作模式、多Agent并行执行、20+内置技能、预配置专家团队、微信/QQ/飞书移动端控制。",
    category: "ai-tools",
    tags: ["Tencent", "WorkBuddy", "AI Office", "Productivity", "AI Agent", "China"],
    difficulty: "beginner",
    toolsMentioned: ["Tencent WorkBuddy"],
    date: "2026-07-05",
  },

  {
    slug: "complete-practical-tutorial-claude-code-core-operations",
    title: "Complete Practical Tutorial: Master All Core Operations Inside Claude Code",
    titleZh: "Claude Code完全实战教程：掌握所有核心操作",
    description: "A hands-on tutorial covering every core Claude Code operation — from CLI installation and project import to file analysis, batch refactoring, automatic debugging, claude.md rules, Git integration, Plan Mode, and permission controls — with executable commands for every step.",
    descriptionZh: "从CLI安装、项目导入到文件分析、批量重构、自动调试、claude.md规则、Git联动、Plan模式和权限控制，每一步都有可执行命令，覆盖Claude Code全部核心操作。",
    category: "ai-tutorials",
    tags: ["Claude Code", "CLI", "Tutorial", "Coding", "Debugging", "Refactoring", "Git"],
    difficulty: "intermediate",
    toolsMentioned: ["Claude Code"],
    date: "2026-07-07",
  },
  {
    slug: "7-mainstream-agent-architectures-beginner-enterprise-guide",
    title: "7 Mainstream Agent Architectures: From Beginner to Enterprise-Grade Guide",
    titleZh: "7大主流Agent架构：从入门到企业级完整指南",
    description: "A systematic breakdown of 7 Agent architectures — Single Agent, ReAct, Plan & Execute, Multi-Agent, Router+Skill, Blackboard, and Graph/Workflow — with pros, cons, best-use cases, and a recommended evolution path from beginner to enterprise.",
    descriptionZh: "系统拆解7种Agent架构——单Agent、ReAct、Plan & Execute、多Agent、Router+Skill、黑板架构和Graph/Workflow——含优缺点、最佳场景和从入门到企业级的推荐演进路径。",
    category: "ai-learning",
    tags: ["AI Agent", "Architecture", "ReAct", "Multi-Agent", "Workflow", "LangGraph", "Enterprise"],
    difficulty: "intermediate",
    toolsMentioned: ["LangGraph", "n8n"],
    date: "2026-07-07",
  },

  {
    slug: "practical-guide-tencent-workbuddy-ai-office-assistant",
    title: "A Practical Guide to Tencent WorkBuddy: Your All-in-One AI Office Assistant",
    titleZh: "腾讯WorkBuddy实操指南：一站式AI办公助手完全上手",
    description: "A hands-on guide to Tencent WorkBuddy covering installation, interface overview, and 6 practical use cases with specific prompt examples — document generation, data analysis, PPT creation, weekly reports, code development, and design — plus Expert Teams and Skill Library.",
    descriptionZh: "腾讯WorkBuddy上手实操指南，覆盖安装配置、界面概览和6大实战场景（文档生成、数据分析、PPT制作、周报、代码开发、设计创意），每个场景含具体提示词示例，附专家团队和技能库使用说明。",
    category: "ai-tools",
    tags: ["Tencent", "WorkBuddy", "AI Office", "Productivity", "Practical Guide", "China"],
    difficulty: "beginner",
    toolsMentioned: ["Tencent WorkBuddy"],
    date: "2026-07-08",
  },

  {
    slug: "seedream-5-pro-ai-image-generation-guide",
    title: "Seedream 5.0 Pro: A Comprehensive Practical Guide to China's Leading AI Image Generation Model",
    titleZh: "Seedream 5.0 Pro实战评测：国产顶流AI图像生成模型全指南",
    description: "Hands-on testing of ByteDance's Seedream 5.0 Pro across five scenarios — artistic eye close-ups, Chinese text rendering, bookmark design, character turnaround sheets, and steampunk UI — comparing against GPT Image 2 and Nano Banana Pro.",
    descriptionZh: "字节跳动Seedream 5.0 Pro五大场景实战评测——艺术眼部特写、中文文字渲染、书签设计、角色三视图和蒸汽朋克UI——与GPT Image 2和Nano Banana Pro横向对比。",
    category: "ai-tools",
    tags: ["Seedream", "ByteDance", "Image Generation", "China", "AI Art", "Design", "Review"],
    difficulty: "beginner",
    toolsMentioned: ["Seedream 5.0 Pro", "GPT Image 2", "Nano Banana Pro"],
    date: "2026-07-09",
  },
  {
    slug: "official-tutorial-three-ways-codex-control-computer",
    title: "Official Tutorial: Three Ways Codex Can Control Your Computer for You",
    titleZh: "官方教程：Codex控制电脑的三种方式详解",
    description: "OpenAI's Jason Liu breaks down Codex's three computer control modes — Computer Use (desktop automation), Chrome Extension (browser tasks), and In-App Browser (web dev debugging) — with real-world examples and a decision framework for choosing the right mode.",
    descriptionZh: "OpenAI Jason Liu详解Codex三种电脑控制方式——Computer Use（桌面自动化）、Chrome扩展（浏览器任务）和内置浏览器（网页开发调试）——含真实案例和选型决策框架。",
    category: "ai-tools",
    tags: ["Codex", "OpenAI", "Computer Use", "Automation", "Chrome Extension", "Tutorial"],
    difficulty: "beginner",
    toolsMentioned: ["Codex Agent"],
    date: "2026-07-09",
  },

  {
    slug: "workbuddy-3-layer-memory-system-make-ai-understand-you",
    title: "WorkBuddy L05: Master the 3-Layer Memory System – Make AI Understand You Better",
    titleZh: "WorkBuddy L05：掌握三层记忆系统，让AI越来越懂你",
    description: "A deep dive into WorkBuddy's 3-layer memory architecture — Cloud Memory (auto profile + cross-conversation search), User-level Local Memory (MEMORY.md), and Workspace Memory (auto daily logs) — plus how Memory integrates with Skills and Automation to create a self-improving AI assistant.",
    descriptionZh: "深度解析WorkBuddy三层记忆架构——云端记忆（自动画像+跨对话搜索）、用户级本地记忆（MEMORY.md）和工作区记忆（自动日志）——以及记忆如何与技能和自动化系统联动，打造越用越聪明的AI助手。",
    category: "ai-tutorials",
    tags: ["WorkBuddy", "Memory", "Automation", "Skills", "Productivity", "AI Assistant"],
    difficulty: "beginner",
    toolsMentioned: ["Tencent WorkBuddy"],
    date: "2026-07-10",
  },
  {
    slug: "codex-zero-basics-tutorial-part-2-hands-on-guide",
    title: "Codex Zero-Basics Tutorial Part 2: Hands-On Guide to Using Codex for AI Beginners",
    titleZh: "Codex零基础教程（下）：AI新手实操完全指南",
    description: "A beginner-friendly Codex hands-on tutorial covering installation (Windows/Mac), project setup, file organization with real café example, Plan Mode for complex tasks, Pet feature, and dashboard creation — zero technical knowledge required.",
    descriptionZh: "Codex新手实操教程，覆盖安装（Windows/Mac）、项目设置、咖啡馆文件整理实战案例、Plan Mode复杂任务模式、Pet宠物功能和Dashboard创建——完全零技术门槛。",
    category: "ai-tutorials",
    tags: ["Codex", "OpenAI", "Tutorial", "Beginner", "Hands-on", "Plan Mode", "Automation"],
    difficulty: "beginner",
    toolsMentioned: ["Codex Agent"],
    date: "2026-07-10",
  },

  {
    slug: "chatgpt-codex-10-core-features-beginners-work-efficiency",
    title: "ChatGPT Codex: 10 Core Features for Beginners to Boost Work Efficiency",
    titleZh: "ChatGPT Codex：新手必学的10个核心提效功能",
    description: "A practical guide to ChatGPT Codex's 10 most useful features — batch file renaming, data analysis with charts, doc-to-web conversion, local file memory, scheduled automation, plugin ecosystem, PPT creation, system cleanup, hand-drawn flowcharts, and article formatting — each with example commands.",
    descriptionZh: "ChatGPT Codex十大实用功能实操指南——批量文件重命名、数据图表分析、文档转网页、本地文件记忆、定时自动化、插件生态、PPT制作、系统清理、手绘流程图和文章格式化，每个功能含示例指令。",
    category: "ai-tools",
    tags: ["ChatGPT", "Codex", "Productivity", "Automation", "Beginner", "Tutorial"],
    difficulty: "beginner",
    toolsMentioned: ["ChatGPT", "Codex Agent"],
    date: "2026-07-11",
  },
  {
    slug: "lightweight-ai-transformation-traditional-business-workbuddy-cordys-crm",
    title: "Lightweight AI Transformation for Traditional Business Systems: WorkBuddy + Cordys CRM Skills",
    titleZh: "传统业务系统轻量级AI改造方案：WorkBuddy + Cordys CRM技能实战",
    description: "A practical enterprise AI transformation blueprint using a three-layer architecture — WorkBuddy (AI entry), Business Skills (capability encapsulation), and Existing Systems (Cordys CRM) — with detailed Skill file anatomy, import process, and web/mobile demonstrations.",
    descriptionZh: "企业AI改造实战方案：三层架构——WorkBuddy（AI入口）+ 业务技能（能力封装）+ 现有系统（Cordys CRM），含Skill文件逐项拆解、导入流程和网页/移动端实操演示。",
    category: "ai-use-cases",
    tags: ["WorkBuddy", "Enterprise", "CRM", "Skills", "Digital Transformation", "Business"],
    difficulty: "intermediate",
    toolsMentioned: ["Tencent WorkBuddy"],
    date: "2026-07-11",
  },

  {
    slug: "vibecoding-contest-guide-game-animations-ai-tools",
    title: "VibeCoding Contest Guide: Create Game Animations Efficiently With AI Tools",
    titleZh: "VibeCoding大赛指南：用AI工具高效制作游戏动画",
    description: "A complete AI game animation workflow — from sprite sheet generation with structured prompts, to animation control code for Godot (GDScript) and Unity (C#), motion fine-tuning, easing functions, and advanced cutscene sequencing — zero art or coding foundation required.",
    descriptionZh: "AI游戏动画完整工作流——从精灵表生成的结构化提示词，到Godot（GDScript）和Unity（C#）的动画控制代码，动作微调、缓动函数和高级过场动画编排——零美术和编程基础也能上手。",
    category: "ai-tutorials",
    tags: ["VibeCoding", "Game Development", "Animation", "Godot", "Unity", "Sprite Sheet", "Tutorial"],
    difficulty: "intermediate",
    toolsMentioned: ["Claude Code", "Godot", "Unity"],
    date: "2026-07-13",
  },
  {
    slug: "claude-code-game-studios-game-development-easier",
    title: "Make Game Development Easier with Claude Code Game Studios",
    titleZh: "Claude Code Game Studios：让独立游戏开发从未如此简单",
    description: "An introduction to Claude Code Game Studios — an open-source project that transforms a single Claude Code session into a complete game studio with 49 AI agents, 73 skills, 12 hooks, and a hierarchical studio structure (Directors → Department Heads → Experts) for solo game development.",
    descriptionZh: "Claude Code Game Studios开源项目介绍——将单个Claude Code会话转变为完整游戏工作室，含49个AI Agent、73个技能、12个钩子和层级化工作室架构（总监→部门主管→专家），实现单人全流程游戏开发。",
    category: "ai-tools",
    tags: ["Claude Code", "Game Development", "Open Source", "AI Agent", "Studio", "Indie Dev"],
    difficulty: "beginner",
    toolsMentioned: ["Claude Code"],
    date: "2026-07-13",
  },

  {
    slug: "gpt-5-6-full-launch-sol-terra-luna-family",
    title: "GPT-5.6 Full Launch: The Complete Family of Sol, Terra, and Luna",
    titleZh: "GPT-5.6全系发布：Sol、Terra、Luna三款模型完整实测",
    description: "Hands-on testing of OpenAI's GPT-5.6 model family — Sol building a 3D FPS game with Three.js in 1.5 hours, Terra generating a 3D voxel rocket in 35 minutes, and Luna producing a 47-page annual report from 26K records — with model selection guidance for different task types.",
    descriptionZh: "OpenAI GPT-5.6三款模型完整实测——Sol用Three.js 1.5小时构建3D FPS游戏、Terra 35分钟生成3D体素火箭、Luna从2.6万条记录生成47页年报——含不同任务类型的模型选择指南。",
    category: "ai-news",
    tags: ["GPT-5.6", "OpenAI", "Sol", "Terra", "Luna", "Model Comparison", "Benchmark"],
    difficulty: "beginner",
    toolsMentioned: ["ChatGPT", "Codex Agent"],
    date: "2026-07-14",
  },
  {
    slug: "gpt-5-6-openai-merges-chatgpt-codex-end-pure-chat-era",
    title: "GPT-5.6 Full Launch: OpenAI Merges ChatGPT and Codex, Ending the Pure Chat Era",
    titleZh: "GPT-5.6全面发布：OpenAI合并ChatGPT与Codex，纯聊天时代终结",
    description: "OpenAI's landmark GPT-5.6 launch merges ChatGPT and Codex into 'ChatGPT Work', featuring Sol (flagship), Terra (balanced), and Luna (lightweight) — with coding benchmarks beating Claude Fable 5, cybersecurity testing, and UX improvements for 1 billion weekly users.",
    descriptionZh: "OpenAI里程碑式发布：ChatGPT与Codex合并为'ChatGPT Work'，推出Sol（旗舰）、Terra（均衡）、Luna（轻量）三款模型——编码基准超越Claude Fable 5、网络安全实测、面向10亿周活用户的UX升级。",
    category: "ai-news",
    tags: ["GPT-5.6", "OpenAI", "ChatGPT", "Codex", "Sol", "AI News", "Merger"],
    difficulty: "beginner",
    toolsMentioned: ["ChatGPT", "Codex Agent", "Claude Fable 5"],
    date: "2026-07-14",
  },

  {
    slug: "build-personal-ai-knowledge-base-workbuddy-ima-guide",
    title: "Build Your Personal AI Knowledge Base with WorkBuddy + IMA: A Step-by-Step Guide",
    titleZh: "WorkBuddy + IMA：搭建个人AI知识库的完整指南",
    description: "A step-by-step guide to building a personal AI knowledge base using WorkBuddy (AI agent) + IMA Knowledge Base (storage) — tailored for Chinese users as an alternative to Codex+Obsidian, covering installation, connection, content management, and advanced prompts.",
    descriptionZh: "用WorkBuddy（AI Agent）+ IMA知识库（存储）搭建个人AI知识库的完整步骤指南——面向国内用户的Codex+Obsidian替代方案，覆盖安装、连接、内容管理和高级提示词。",
    category: "ai-tutorials",
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
    category: "ai-tutorials",
    tags: ["WorkBuddy", "Skills", "Productivity", "Prompt Engineering", "Automation", "Tutorial"],
    difficulty: "beginner",
    toolsMentioned: ["Tencent WorkBuddy"],
    date: "2026-07-15",
  },

  {
    slug: "ai-powered-quantitative-trading-quantdinger-guide",
    title: "AI-Powered Quantitative Trading Made Accessible: A Practical Guide to QuantDinger",
    titleZh: "AI量化交易入门：QuantDinger实战指南",
    description: "A practical guide to QuantDinger — an open-source AI-powered quantitative trading platform featuring automatic strategy optimization, multi-market coverage (A-shares, US stocks, crypto, futures, forex), deterministic backtesting, self-hosted Docker deployment, and MCP integration with AI coding tools.",
    descriptionZh: "QuantDinger开源AI量化交易平台实战指南——自动策略优化、多市场覆盖（A股/美股/加密货币/期货/外汇）、确定性回测、Docker自托管部署和MCP集成AI编码工具。",
    category: "ai-tools",
    tags: ["QuantDinger", "Quantitative Trading", "Finance", "Open Source", "Docker", "Python", "AI"],
    difficulty: "advanced",
    toolsMentioned: ["QuantDinger", "Claude Code", "Cursor"],
    date: "2026-07-16",
  },

  {
    slug: "how-to-use-codex-quantitative-strategy-research-backtesting",
    title: "How to Use Codex for Quantitative Strategy Research and Backtesting",
    titleZh: "用Codex做量化策略研究与回测：完整教程",
    description: "A step-by-step tutorial on using Codex with khQuant CLI for quantitative strategy research — covering installation, configuration testing, data download, batch golden-cross strategy optimization, and backtest report generation.",
    descriptionZh: "用Codex配合khQuant命令行工具进行量化策略研究的完整教程——覆盖安装、配置测试、数据下载、批量金叉策略优化和回测报告生成。",
    category: "ai-tutorials",
    tags: ["Codex", "Quantitative Trading", "khQuant", "Backtesting", "Strategy Research", "Finance"],
    difficulty: "intermediate",
    toolsMentioned: ["Codex Agent"],
    date: "2026-07-18",
  },
  {
    slug: "how-to-build-personal-ai-quant-trading-system-2026",
    title: "How to Build a Personal AI Quant Trading System in 2026",
    titleZh: "2026个人AI量化交易系统搭建全指南",
    description: "A comprehensive guide to building a personal AI quant trading system — from understanding how large quant firms profit versus individual trader advantages, to choosing holaOS as the agent framework, training AI with 6 core skills, implementing event-driven strategies with multi-model validation (Claude + GLM-5), and cost breakdown (~$400/month).",
    descriptionZh: "搭建个人AI量化交易系统的完整指南——从理解大机构盈利模式与个人优势，到选择holaOS作为Agent框架、训练AI六大核心能力、实施事件驱动策略+多模型验证（Claude+GLM-5），含成本分析（约$400/月）。",
    category: "ai-tutorials",
    tags: ["Quantitative Trading", "AI Agent", "holaOS", "Event-Driven", "Finance", "Claude", "GLM-5"],
    difficulty: "advanced",
    toolsMentioned: ["Claude Code", "GLM-5"],
    date: "2026-07-18",
  },

  {
    slug: "build-ai-team-coze-3-one-person-company",
    title: "8-Minute Guide: Build an AI Team with Coze 3.0 – Complete a Project from Idea to Launch as a One-Person Company",
    titleZh: "8分钟学会用Coze 3.0搭建AI团队：一人公司从创意到上线全流程",
    description: "A step-by-step tutorial on building a multi-agent AI team in Coze 3.0 — Product Manager, Designer, Development Planner (Claude Code), Development Executor (Codex CLI), and Video Producer (Seedance) — to build an anti-procrastination app from scratch, including PRD, UI design, coding, and promotional video generation.",
    descriptionZh: "在Coze 3.0中搭建多Agent AI团队的完整教程——产品经理、设计师、开发规划（Claude Code）、开发执行（Codex CLI）和视频制作（Seedance）——从零构建反拖延App，含PRD、UI设计、编码和宣传视频全流程。",
    category: "ai-tutorials",
    tags: ["Coze", "AI Agent", "Multi-Agent", "No-Code", "Productivity", "Tutorial", "One-Person Company"],
    difficulty: "beginner",
    toolsMentioned: ["Coze", "Claude Code", "Codex Agent"],
    date: "2026-07-19",
  },

  {
    slug: "ai-manhua-production-full-workflow-script-to-monetization",
    title: "AI Manhua Production Full Workflow: From Script to Monetization",
    titleZh: "AI漫剧制作全流程：从剧本到变现的完整指南",
    description: "A complete AI manhua (short anime) production workflow using only a smartphone — from scene description and text-to-image through image-to-video and post-editing, plus 3 script creation methods, prompt optimization for camera control, model selection (Seedance, Xiaoyunque, Wan, LTX), and monetization basics.",
    descriptionZh: "仅用手机完成AI漫剧制作的完整流程——从场景描述、文生图到图生视频和后期剪辑，含3种剧本创作方法、镜头控制提示词优化、模型选择（Seedance、Xiaoyunque、Wan、LTX）和变现基础。",
    category: "ai-tutorials",
    tags: ["AI Manhua", "Video Generation", "Content Creation", "Seedance", "Monetization", "Tutorial"],
    difficulty: "beginner",
    toolsMentioned: ["Seedance 2.0", "Xiaoyunque", "CapCut"],
    date: "2026-07-20",
  },
  {
    slug: "kimi-k3-takes-global-top-spot-week-29-frontend-coding-benchmark",
    title: "Kimi K3 Takes Global Top Spot: Week 29 LLM Front-End Coding Benchmark Report",
    titleZh: "Kimi K3登顶全球第一：第29周LLM前端编码基准测试报告",
    description: "Week 29 front-end coding benchmark results: Kimi K3 debuts at #1 globally (1679 score), surpassing Claude Fable-5 and GPT-5.6 Sol — 9 Chinese models in top 25, with GLM 5.2 at #4 — plus a Python test script and model selection guide for developers.",
    descriptionZh: "第29周前端编码基准测试：Kimi K3首秀全球第一（1679分），超越Claude Fable-5和GPT-5.6 Sol——9款国产模型进入前25，GLM 5.2第4——含Python测试脚本和开发者选型指南。",
    category: "ai-news",
    tags: ["Kimi K3", "Benchmark", "Front-End", "Coding", "LLM", "China", "Claude", "GPT"],
    difficulty: "beginner",
    toolsMentioned: ["Kimi", "Claude Fable 5", "GPT-5.6", "GLM-5"],
    date: "2026-07-20",
  },

  {
    slug: "2026-local-llm-benchmark-13-open-source-models-4000-hardware-guide",
    title: "2026 Local Large Language Model Benchmark: 13 Open-Source Models, $4000 Budget Hardware Local Deployment Guide",
    titleZh: "2026本地大模型横评：13款开源模型+$4000硬件部署全指南",
    description: "A 30-day, $4,185 hardware deep dive testing 13 open-source LLMs (Qwen3.6, Gemma 4, Ornith 1.0) for local deployment — covering quantization, MTP, Dense vs MoE, OCR, long-context reasoning, full-stack coding, speed benchmarks, and llama.cpp deployment with GGUF.",
    descriptionZh: "30天$4185硬件深度评测13款开源大模型（Qwen3.6、Gemma 4、Ornith 1.0）本地部署——覆盖量化、MTP、Dense vs MoE、OCR、长上下文推理、全栈编码、速度基准和llama.cpp GGUF部署。",
    category: "ai-learning",
    tags: ["LLM", "Local Deployment", "Open Source", "Benchmark", "Hardware", "Qwen", "Gemma", "Quantization"],
    difficulty: "advanced",
    toolsMentioned: ["Qwen", "Gemma", "DeepSeek"],
    date: "2026-07-21",
  },

  {
    slug: "ai-powered-excel-workflow-4-practical-skills-beginners",
    title: "AI-Powered Excel Workflow: 4 Practical Skills for Beginners",
    titleZh: "AI加持Excel工作流：新手必学的4个实用技能",
    description: "Four essential AI+Excel skills for beginners — defining clear requirements to auto-generate tables, identifying and fixing data quality issues, setting business rules for tiered calculations with VBA macros, and asking the right questions to generate interactive HTML dashboards.",
    descriptionZh: "新手必学的四个AI+Excel核心技能——用清晰需求自动生成表格、识别修复数据质量问题、设定业务规则实现阶梯计算+VBA宏、提出正确问题生成交互式HTML仪表盘。",
    category: "ai-tutorials",
    tags: ["Excel", "AI", "Productivity", "Data Analysis", "Beginner", "Tutorial", "Dashboard"],
    difficulty: "beginner",
    toolsMentioned: ["ChatGPT"],
    date: "2026-07-22",
  },

  {
    slug: "why-99-percent-ai-knowledge-bases-fail-in-practice",
    title: "Why 99% of AI Knowledge Bases Fail in Practice",
    titleZh: "为什么99%的AI知识库在实践中失败：RAG深度解析",
    description: "A deep dive into why most AI knowledge bases fail — covering RAG fundamentals, ingestion pipeline (cleaning, semantic chunking, vectorization), QA pipeline (question understanding, reranking, context assembly), four-layer implementation, hybrid retrieval, and practical lessons from real enterprise projects.",
    descriptionZh: "深度解析AI知识库失败的根源——RAG核心原理、摄入管线（清洗、语义分块、向量化）、问答管线（问题理解、重排序、上下文组装）、四层实施方法、混合检索和企业实战经验。",
    category: "ai-learning",
    tags: ["RAG", "Knowledge Base", "Vector Database", "Enterprise AI", "Chunking", "Embedding", "Engineering"],
    difficulty: "advanced",
    toolsMentioned: [],
    date: "2026-07-23",
  },

  {
    slug: "6-popular-ai-agent-tools-reviewed-chinese-beginners-2026",
    title: "6 Popular AI‑Agent Tools Reviewed: Which One Should Chinese Beginners Pick in 2026",
    titleZh: "2026年6款主流AI Agent工具横评：中国新手该选哪个？",
    description: "A practical ranking of 6 AI Agent tools for Chinese beginners — Codex (5/5), WorkBuddy (4/5), Trae & Z-Code (3.5/5), Claude Code (2.5/5), OpenClaw/Hermes (2/5) — with setup steps, pros/cons, and a decision guide based on network/payment accessibility.",
    descriptionZh: "面向中国新手的6款AI Agent工具实用排名——Codex(5/5)、WorkBuddy(4/5)、Trae和Z-Code(3.5/5)、Claude Code(2.5/5)、OpenClaw/Hermes(2/5)——含安装步骤、优缺点和基于网络/支付条件的选型决策指南。",
    category: "ai-tools",
    tags: ["AI Agent", "Tools Comparison", "Codex", "WorkBuddy", "Claude Code", "China", "Beginner"],
    difficulty: "beginner",
    toolsMentioned: ["Codex Agent", "Tencent WorkBuddy", "Claude Code", "TRAE Framework", "Z-Code"],
    date: "2026-07-24",
  },
  {
    slug: "master-ai-driven-development-openspec-practical-guide-beginners",
    title: "Master AI-Driven Development with OpenSpec: A Practical Guide for Beginners",
    titleZh: "用OpenSpec掌握AI驱动开发：新手实操指南",
    description: "A beginner-friendly guide to OpenSpec — a lightweight specification-driven development (SDD) framework that structures AI coding projects through a 4-step workflow (Explore → Generate Docs → Develop → Archive), comparing it with Spec-Kit and Superpowers for different project scales.",
    descriptionZh: "OpenSpec新手实操指南——轻量级规格驱动开发（SDD）框架，通过4步工作流（需求探索→文档生成→开发→归档）结构化AI编码项目，与Spec-Kit和Superpowers的横向对比。",
    category: "ai-tools",
    tags: ["OpenSpec", "SDD", "Specification-Driven Development", "AI Coding", "Framework", "Tutorial"],
    difficulty: "beginner",
    toolsMentioned: ["OpenSpec"],
    date: "2026-07-24",
  },

  {
    slug: "mastering-ai-image-generation-fix-prompt-issues-avoid-draw-failures",
    title: "Mastering AI Image Generation: How to Fix Prompt Issues and Avoid 'Draw Failures'",
    titleZh: "掌握AI图像生成：修复提示词问题，避免'翻车'",
    description: "A deep dive into common AI image generation failures — 'prompt pollution' (keyword association traps), the 'visual compensation' bug, and camera control workarounds — with practical fixes like word substitution, reverse-trap techniques, and direct visual element description.",
    descriptionZh: "深度解析AI图像生成常见失败——'提示词污染'（关键词关联陷阱）、'视觉补偿'Bug和相机控制技巧——含词汇替换、反向陷阱利用和直接视觉元素描述等实用修复方法。",
    category: "ai-tutorials",
    tags: ["AI Image Generation", "Prompt Engineering", "Midjourney", "DALL-E", "Tutorial", "Tips"],
    difficulty: "intermediate",
    toolsMentioned: ["Midjourney", "DALL-E"],
    date: "2026-07-25",
  },

  {
    slug: "ai-powered-spreadsheet-creation-future-office-productivity",
    title: "AI-Powered Spreadsheet Creation: The Future of Office Productivity",
    titleZh: "AI驱动电子表格创建：未来办公生产力的革命",
    description: "A practical guide to AI-powered spreadsheet creation — from choosing AI tools and providing profession-specific requirements, to advanced use cases like e-commerce operation tables, expense report processing, and data visualization with interactive charts.",
    descriptionZh: "AI驱动电子表格创建实操指南——从选择AI工具、按职业提供需求，到电商运营表、费用报销处理和数据可视化等进阶场景。",
    category: "ai-use-cases",
    tags: ["AI", "Spreadsheet", "Excel", "Productivity", "Office", "Automation", "Beginner"],
    difficulty: "beginner",
    toolsMentioned: ["Doubao"],
    date: "2026-07-26",
  },

  {
    slug: "how-to-use-douyin-ai-creation-agent-generate-images-videos",
    title: "How to Use Douyin's AI Creation Agent to Generate Images and Videos Without Complex Prompts",
    titleZh: "抖音AI创作助手：无需复杂提示词也能生成图片和视频",
    description: "A beginner-friendly guide to Douyin's AI Creation Agent powered by Seedream 5.0 Pro and Seedance 2.0 — conversational image and video generation without complex prompts, featuring reference photo upload, iterative refinement, trend-based creation, and one-click remixing of existing AI videos.",
    descriptionZh: "抖音AI创作助手新手指南——搭载Seedream 5.0 Pro和Seedance 2.0，对话式图片和视频生成无需复杂提示词，支持参考照片上传、迭代优化、趋势创作和AI视频一键再创作。",
    category: "ai-tools",
    tags: ["Douyin", "AI Creation", "Seedream", "Seedance", "Image Generation", "Video Generation", "Beginner"],
    difficulty: "beginner",
    toolsMentioned: ["Seedream 5.0 Pro", "Seedance 2.0"],
    date: "2026-07-27",
  },

  {
    slug: "full-practical-guide-ai-comic-drama-production-zero-to-published",
    title: "Full Practical Guide to AI Comic Drama Production: From Zero to Published Video",
    titleZh: "AI漫剧制作完全实战指南：从零到发布视频",
    description: "A complete 4-step AI comic drama production workflow — scene description with AI refinement, text-to-image with style/aspect ratio control, image-to-video with dialogue and voice direction, and post-production editing with sound effects, subtitles, and trimming — plus AI script creation techniques.",
    descriptionZh: "AI漫剧四步完整制作流程——AI润色场景描述、文生图（风格/比例控制）、图生视频（对话/声音指导）和后期剪辑（音效/字幕/裁剪）——含AI剧本创作技巧。",
    category: "ai-tutorials",
    tags: ["AI Comic Drama", "Video Generation", "Content Creation", "Seedance", "Xiaoyunque", "Tutorial"],
    difficulty: "beginner",
    toolsMentioned: ["Seedance 2.0", "Xiaoyunque", "CapCut"],
    date: "2026-07-28",
  },

  {
    slug: "correct-way-to-collaborate-with-ai-practical-guide",
    title: "The Correct Way to Collaborate with AI: A Practical Guide",
    titleZh: "与AI正确协作的方式：一份实用指南",
    description: "A practical guide to effective AI collaboration using a 3-step framework — Put It Forward (start with real tasks, not tutorials), Explain It Clearly (break vague feelings into specific parameters), and Keep Asking (build a two-way question loop) — embracing 'learning by doing' over 'learn first, use later.'",
    descriptionZh: "高效AI协作三步框架实操指南——提出来（从真实任务开始而非教程）、说清楚（将模糊感觉拆解为具体参数）、持续追问（构建双向问答循环）——拥抱'做中学'而非'先学后用'。",
    category: "ai-learning",
    tags: ["AI Collaboration", "Prompt Engineering", "Learning by Doing", "Productivity", "Beginner", "Guide"],
    difficulty: "beginner",
    toolsMentioned: [],
    date: "2026-07-29",
  },

  {
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

  {
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

  {
    slug: "deepseek-v4-flash-official-release-practical-guide",
    title: "DeepSeek V4 Flash Official Release: A Practical Guide to the Game-Changing AI Model",
    titleZh: "DeepSeek V4 Flash正式发布：改变游戏规则的AI模型实战指南",
    description: "DeepSeek V4 Flash official launch breakdown — 82.7 Terminal-Bench (global 2nd), 36-107x cheaper than GPT-5.6 Sol at $0.14/M input tokens, 284B MoE architecture with 13B active per token, 1M native context, plus Python API setup, agent task execution, and cost optimization tips.",
    descriptionZh: "DeepSeek V4 Flash正式发布深度解析——Terminal-Bench 82.7分（全球第2），比GPT-5.6 Sol便宜36-107倍（$0.14/M输入token），284B MoE架构仅13B/token激活，原生1M上下文，含Python API配置、Agent任务执行和成本优化技巧。",
    category: "ai-news",
    tags: ["DeepSeek", "DeepSeek V4", "MoE", "API", "Benchmark", "Cost Efficiency", "Tutorial"],
    difficulty: "intermediate",
    toolsMentioned: ["DeepSeek"],
    date: "2026-08-01",
  },

  {
    slug: "how-to-build-high-end-ai-personal-workbench-zero-code-workbuddy",
    title: "How to Build a High-End AI Personal Workbench with Zero Code",
    titleZh: "零代码搭建高端AI个人工作台：WorkBuddy完整教程",
    description: "A step-by-step guide to building a custom AI personal workbench in WorkBuddy with zero code — using /finesse-brief (requirement organization) and /finesse-ui (high-end UI generation) Skills, covering pet daily record workbench, AI workbench, and life management workbench examples.",
    descriptionZh: "用WorkBuddy零代码搭建自定义AI个人工作台——使用/finesse-brief（需求整理）和/finesse-ui（高端UI生成）两个技能，含宠物日常记录、AI工作台、生活管理三个实战案例。",
    category: "ai-tutorials",
    tags: ["WorkBuddy", "No-Code", "Workbench", "Personal Dashboard", "Productivity", "UI Design"],
    difficulty: "beginner",
    toolsMentioned: ["Tencent WorkBuddy"],
    date: "2026-08-03",
  },

  {
    slug: "how-feishu-redefined-ai-work-100-to-20000-system-in-minutes",
    title: "How Feishu Redefined AI Work: $100 → $20,000 System in Minutes",
    titleZh: "飞书重新定义AI工作：100元→2万元系统几分钟搞定",
    description: "Feishu's three groundbreaking AI features — one-click personal AI Agent (Little Lobster), Feishu Miaoda generating $20K business systems for $100 in natural language, and Multidimensional Table Agent with auto table/dashboard/permission generation — plus the OpenClaw open-source plugin for multi-model integration.",
    descriptionZh: "飞书三大AI突破——一键创建个人AI Agent（小龙虾）、飞书妙搭用自然语言100元生成2万元业务系统、多维表格AI Agent自动生成表格/仪表盘/权限——含OpenClaw开源插件多模型集成。",
    category: "ai-news",
    tags: ["Feishu", "Lark", "AI Agent", "Miaoda", "OpenClaw", "Productivity", "China"],
    difficulty: "beginner",
    toolsMentioned: ["OpenClaw"],
    date: "2026-08-04",
  },

  {
    slug: "complete-guide-ai-industry-chain-from-energy-to-robots",
    title: "A Complete Guide to the AI Industry Chain: From Energy to Smart Robots",
    titleZh: "AI产业链完整指南：从能源到智能机器人",
    description: "A bottom-up overview of the AI industry chain — energy (solar/wind/nuclear), chips (ASML lithography, semiconductor manufacturing), PCB & MLCC, large models (training pipeline), and smart robots — plus investment, career, and skill-building opportunities in each layer.",
    descriptionZh: "从底层到顶层的AI产业链全景——能源（光伏/风电/核电）、芯片（ASML光刻、半导体制造）、PCB和MLCC、大模型（训练流程）、智能机器人——每层的投资、职业和技能机会。",
    category: "ai-learning",
    tags: ["AI Industry", "Chips", "Semiconductor", "Energy", "Robots", "Large Models", "Career"],
    difficulty: "beginner",
    toolsMentioned: ["DeepSeek", "TensorFlow"],
    date: "2026-08-05",
  },

  {
    slug: "build-your-first-personal-app-with-ai-even-without-coding-experience",
    title: "Build Your First Personal App with AI Even Without Coding Experience",
    titleZh: "零代码经验也能用AI搭建你的第一个个人应用",
    description: "A complete hands-on tutorial for building a personal work-and-life management app with AI — from prompt writing, PRD drafting, and Git archiving to secondary development and interface beautification. Zero programming experience required.",
    descriptionZh: "从零开始用AI搭建个人工作生活管理应用的完整教程——涵盖提示词编写、PRD文档、Git归档、二次开发和界面美化。无需编程经验。",
    category: "ai-tutorials",
    tags: ["AI App Development", "No Code", "Personal App", "AI Agent", "Prompt Engineering", "Git", "Beginner"],
    difficulty: "beginner",
    toolsMentioned: ["Doubao", "Trae", "Kimi", "Tongyi", "Cursor", "Claude", "Codex"],
    date: "2026-08-06",
  },

  {
    slug: "master-seedance-2-5-zero-basics-guide-commercial-grade-ai-video-creation",
    title: "Master Seedance 2.5: Zero-Basics Guide to Commercial-Grade AI Video Creation",
    titleZh: "掌握Seedance 2.5：零基础商业级AI视频创作指南",
    description: "A hands-on guide to ByteDance's Seedance 2.5 video model — direct 30-second commercial video generation, smart editing, style replication, multi-language localization, and cost control strategies. Zero-basics to professional in one workflow.",
    descriptionZh: "字节跳动Seedance 2.5视频模型的实战指南——30秒直出商业视频、智能剪辑、风格复刻、多语言本地化和成本控制策略。零基础到专业一步到位。",
    category: "ai-tools",
    tags: ["Seedance", "ByteDance", "Video Generation", "AI Video", "Content Creation", "Commercial", "Prompt Engineering"],
    difficulty: "beginner",
    toolsMentioned: ["Seedance 2.5"],
    date: "2026-08-07",
  },

  {
    slug: "deepseek-v4-flash-vs-gpt-5-6-luna-codex-integration-benchmark",
    title: "DeepSeek V4 Flash vs GPT-5.6 Luna: Full Codex Integration Guide & 10-Round Capability Benchmark",
    titleZh: "DeepSeek V4 Flash vs GPT-5.6 Luna：Codex完整接入指南与10轮能力实测",
    description: "Step-by-step guide to integrating DeepSeek V4 Flash into Codex — with one-click setup scripts for macOS and Windows, pitfall fixes, and a 10-round head-to-head benchmark vs GPT-5.6 Luna covering writing, coding, visualization, and data analysis.",
    descriptionZh: "DeepSeek V4 Flash接入Codex的完整指南——含macOS和Windows一键配置脚本、兼容性坑修复，以及与GPT-5.6 Luna的10轮实战对决，覆盖写作、编程、可视化和数据分析。",
    category: "ai-tutorials",
    tags: ["DeepSeek", "GPT-5.6", "Codex", "Benchmark", "Model Comparison", "Integration", "Coding"],
    difficulty: "intermediate",
    toolsMentioned: ["DeepSeek V4 Flash", "Codex Agent", "GPT-5.6 Luna"],
    date: "2026-08-08",
  },

  {
    slug: "codex-skill-bundle-4-skills-professional-websites-one-prompt",
    title: "Codex Skill Bundle: 4 Skills to Build Professional Websites in One Prompt",
    titleZh: "Codex技能包：4个技能让一条提示词生成专业网站",
    description: "Install four skills into Codex to generate professional websites in a single prompt — Taste Skill for design aesthetics, GSAP for smooth animations, Ponytail for clean minimal code, and Playwright MCP for automated testing.",
    descriptionZh: "为Codex安装四个技能，一条提示词生成专业网站——Taste Skill解决设计美学、GSAP实现流畅动画、Ponytail保证代码极简、Playwright MCP自动测试。",
    category: "ai-tutorials",
    tags: ["Codex", "Skills", "Web Development", "Frontend", "GSAP", "Playwright", "Testing"],
    difficulty: "beginner",
    toolsMentioned: ["Codex Agent", "Playwright"],
    date: "2026-08-10",
  },

];