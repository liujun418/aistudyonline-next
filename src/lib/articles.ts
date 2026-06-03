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
];
