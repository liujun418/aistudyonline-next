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
];
