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
  // ====== Sample: Claude Code (Path: Claude Code 编程入门, Part 1/4) ======
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

  // ====== AI Basics (5) ======
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

  // ====== AI Tutorials (5) ======
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

  // ====== AI Use Cases (5) ======
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

  // ====== AI Comparisons (5) ======
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

  // ====== AI News (5) ======
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

  // ====== AI News (6/6: Google I/O 2026) ======
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

  // ====== Claude Code Path (Part 2/4) ======
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

  // ====== Claude Code Path (Part 3/4) ======
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

  // ====== Claude Code Path (Part 4/4) ======
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

  // ====== Claude Code Companion: Top 7 Skills Guide ======
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

  // ====== AI Image Generation Path (Part 2/4) ======
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

  // ====== AI Image Generation Path (Part 3/4) ======
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

  // ====== AI Image Generation Path (Part 4/4) ======
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

  // ====== AI Basics: 12 Core Concepts ======
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

  // ====== AI Tutorials: OpenClaw Demystified ======
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

  // ====== AI Comparisons: LLM Service Packages Review ======
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

  // ====== Claude Code Companion: Browser Control ======
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

  // ====== Article: 5 AI Tools to Build Your One-Person Overseas Business ======
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

  // ====== Article: Git & GitHub Beginner's Guide ======
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

  // ====== Article: OpenAI's Strategic Counterattack ======
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

  // ====== Article: Practical Explanation of Agent, Skill and Harness ======
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

  // ====== Article: Unlock Hidden Potentials: 5 AI+HTML Hacks ======
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

	// ====== Article: Alexander Wang's Meta AI Superintelligence ======
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

	// ====== Article: AI Workforce ======
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

	// ====== Article: Free AI Knowledge Base Tool ======
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

	// ====== Article: 6 Must-Have OpenClaw Skills ======
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

	// ====== Article: Top 10 Claude Code Commands ======
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

	// ====== Article: DeerFlow Multi-Agent ======
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

	// ====== Article: 12 Essential Claude Code Terminal Commands ======
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

	// ====== Article: Claude Code Overseas Business Guide ======
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

	// ====== Article: Harness Automating Video Creation ======
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

	// ====== Article: Oh-My-ClaudeCode (OMC) Guide ======
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

];