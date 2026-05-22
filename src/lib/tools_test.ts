export interface Tool {
  id: string;
  name: string;
  description: string;
  descriptionZh: string;
  category: "chatbots" | "image-generation" | "video-generation" | "writing" | "coding" | "productivity" | "audio" | "learning" | "industry" | "art" | "design" | "video" | "code" | "data" | "marketing" | "search" | "chat" | "education" | "support";
  tags: string[];
  difficulty: "beginner" | "intermediate" | "advanced";
  url: string;
  rating: number;
  pricing: string;
  useCase: string;
  icon: string;

  // Company info
  company: string;
  companyZh: string;
  founded: string;
  headquarters: string;

  // Detailed description (250-400 chars)
  descriptionLong: string;
  descriptionLongZh: string;

  // Advantages (3-5)
  advantages: string[];
  advantagesZh: string[];

  // Use Cases (3-5)
  useCases: string[];
  useCasesZh: string[];

  // Target audience
  targetAudience: string;
  targetAudienceZh: string;

  // Pricing tiers
  pricingTiers: { tier: string; tierZh: string; price: string; features: string[]; featuresZh: string[] }[];

  // Extensions / plugins
  extensions: { name: string; description: string; descriptionZh: string; url?: string }[];

  // Related skills
  skills: string[];

  // Pros and Cons
  pros: string[];
  prosZh: string[];
  cons: string[];
  consZh: string[];
  scene: "content-creation" | "design-video" | "office-productivity" | "development" | "marketing" | "free-open-source";
  affiliateUrl?: string;
  hasAffiliate?: boolean;
}

export const toolCategories = [
  "chatbots",
  "image-generation",
  "video-generation",
  "writing",
  "coding",
  "productivity",
  "audio",
  "learning",
  "industry",
  "art",
  "design",
  "video",
  "code",
  "data",
  "marketing",
  "search",
  "chat",
  "education",
  "support",
] as const;

export type ToolCategory = (typeof toolCategories)[number];

export const toolDifficulties = ["beginner", "intermediate", "advanced"] as const;
export type ToolDifficulty = (typeof toolDifficulties)[number];

export const toolDifficultyLabels: Record<ToolDifficulty, { en: string; zh: string }> = {
  beginner: { en: "Beginner", zh: "入门" },
  intermediate: { en: "Intermediate", zh: "中级" },
  advanced: { en: "Advanced", zh: "高级" },
};

export const toolCategoryLabels: Record<ToolCategory, { en: string; zh: string }> = {
  chatbots: { en: "Chatbots", zh: "聊天机器人" },
  "image-generation": { en: "Image Gen", zh: "图像生成" },
  "video-generation": { en: "Video Gen", zh: "视频生成" },
  writing: { en: "Writing", zh: "写作" },
  coding: { en: "Coding", zh: "编程" },
  productivity: { en: "Productivity", zh: "效率" },
  audio: { en: "Audio", zh: "音频" },
  learning: { en: "Learning", zh: "学习" },
  industry: { en: "Industry", zh: "行业" },
  art: { en: "Art", zh: "艺术" },
  design: { en: "Design", zh: "设计" },
  video: { en: "Video", zh: "视频" },
  code: { en: "Code", zh: "代码" },
  data: { en: "Data", zh: "数据" },
  marketing: { en: "Marketing", zh: "营销" },
  search: { en: "Search", zh: "搜索" },
  chat: { en: "Chat", zh: "聊天" },
  education: { en: "Education", zh: "教育" },
  support: { en: "Support", zh: "客户支持" },
};

function r(n: number): number {
  return Math.min(5, Math.max(1, Math.round(n)));
}


export const toolScenes = [
  "content-creation",
  "design-video",
  "office-productivity",
  "development",
  "marketing",
  "free-open-source",
] as const;

export type ToolScene = (typeof toolScenes)[number];

export const toolSceneLabels: Record<ToolScene, { en: string; zh: string }> = {
  "content-creation": { en: "Content Creation", zh: "内容创作" },
  "design-video": { en: "Design & Video", zh: "设计与视频" },
  "office-productivity": { en: "Office & Productivity", zh: "办公效率" },
  development: { en: "Development", zh: "开发" },
  marketing: { en: "Marketing", zh: "营销" },
  "free-open-source": { en: "Free & Open Source", zh: "免费开源" },
};


export const tools = [

  {
    id: "chatgpt",
    name: "ChatGPT",
    description: "The most popular AI assistant for conversation, writing, coding, and problem-solving.",
  descriptionZh: "最受欢迎的AI助手，适用于对话、写作、编程和问题解决。",
    category: "chatbots",
    tags: ["conversation", "writing", "coding", "analysis"],
    difficulty: "beginner",
    url: "https://chat.openai.com",
    rating: r(4.7),
    pricing: "Free / $20/mo Plus",
    useCase: "ChatGPT handles general Q&A, content drafting, code generation, and brainstorming. Use it as your daily AI copilot for almost any text-based task.",
    icon: "\u{1F916}",
  company: "OpenAI",
  companyZh: "OpenAI",
  founded: "2015",  headquarters: "San Francisco, CA",  
  descriptionLong: "ChatGPT is OpenAI's flagship conversational AI model that has transformed how millions interact with artificial intelligence. Based on GPT-4o and GPT-5, it handles text, images, audio, and code in one unified interface. With web browsing, file uploads, advanced data analysis, custom GPTs, and voice conversations, it serves as a versatile productivity tool.",
  descriptionLongZh: "ChatGPT是OpenAI的旗舰对话式AI模型，基于GPT-4o和GPT-5构建，在统一界面中处理文本、图像、音频和代码，支持网页浏览、文件上传和高级数据分析。",
  advantages: [
            "Unified multimodal interface for text, images, audio, and code",
            "Extensive plugin ecosystem with custom GPTs and GPT Store",
            "Advanced data analysis with Python execution and file processing"
          ],
  advantagesZh: [
            "统一多模态界面，支持文本、图像、音频和代码",
            "丰富的插件生态系统，含自定义GPTs和GPT商店",
            "高级数据分析，支持Python执行"
          ],
  useCases: [
            "Draft professional emails, reports, and proposals in minutes",
            "Analyze datasets using natural language instead of SQL",
            "Generate and debug code across multiple languages",
            "Create lesson plans and study guides"
          ],
  useCasesZh: [
            "快速起草专业邮件、报告和提案",
            "用自然语言分析数据，无需SQL",
            "跨语言代码生成和调试",
            "创建课程计划和学xi指南"
          ],
  targetAudience: "Anyone who needs an AI assistant -- students, professionals, writers, developers, and creators.",
  targetAudienceZh: "任何需要AI助手的人——学生、专业人士、写作者和开发者。",
  pricingTiers: [
      {
        tier: "Free",
          tierZh: "免费版",
        price: "$0",
        features: [
          "GPT-4o mini access",
          "Limited GPT-5 messages",
          "Basic file uploads"
        ],
        featuresZh: [
          "GPT-4o mini访问权限",
          "GPT-5消息有限额度",
          "基础文件上传",
        ],
      },
      {
        tier: "Plus",
          tierZh: "Plus版",
        price: "$20/mo",
        features: [
          "Unlimited GPT-5",
          "Advanced data analysis",
          "DALL-E 3",
          "Custom GPTs"
        ],
        featuresZh: [
          "GPT-5无限使用",
          "高级数据分析",
          "DALL-E 3图像生成",
          "自定义GPTs",
        ],
      },
      {
        tier: "Pro",
          tierZh: "专业版",
        price: "$200/mo",
        features: [
          "Unlimited GPT-5 Turbo",
          "Priority access",
          "Extended context"
        ],
        featuresZh: [
          "GPT-5 Turbo无限使用",
          "优先访问",
          "扩展上下文",
        ],
      }
    ],  
  extensions: [
        {
          name: "ChatGPT for Chrome",
          description: "Official browser extension",
          descriptionZh: "官方浏览器扩展程序",
          url: "https://chrome.google.com/webstore"
        },
        {
          name: "ChatGPT Desktop",
          description: "Native apps for Windows and macOS",
          descriptionZh: "Windows和macOS桌面应用",
        }
      ],  
  scene: "content-creation",
  affiliateUrl: "https://chat.openai.com/affiliate",
  hasAffiliate: true,
  skills: [
            "prompt engineering",
            "content creation",
            "data analysis",
            "code generation",
            "conversational AI"
          ],  
  pros: [
            "Free tier with GPT-4o mini and basic features",
            "Massive ecosystem of custom GPTs",
            "Multimodal in a single interface"
          ],
  prosZh: [
            "免费版包含GPT-4o mini",
            "海量自定义GPTs生态系统",
            "单一界面的多模态能力"
          ],
  cons: [
            "Free tier has limited GPT-5 messages",
            "Can give confidently incorrect answers",
            "No native offline mode"
          ],
  consZh: [
            "免费版GPT-5消息有限额度",
            "可能自信地给出错误答案",
            "无原生离线模式"
          ],
  },

  {
    id: "claude",
    name: "Claude",
    description: "Anthropic's AI assistant focused on safety, long-form reasoning, and detailed analysis.",
  descriptionZh: "Anthropic的AI助手，注重安全性、长文本推理和详细分析。",
    category: "chatbots",
    tags: ["reasoning", "analysis", "writing", "safety"],
    difficulty: "beginner",
    url: "https://claude.ai",
    rating: r(4.6),
    pricing: "Free / $20/mo Pro",
    useCase: "Claude excels at long document analysis, detailed writing tasks, and thoughtful reasoning. Great for research, editing, and complex problem-solving.",
    icon: "\u{1F9E0}",
  company: "Anthropic",
  companyZh: "Anthropic",
  founded: "2021",  headquarters: "San Francisco, CA",  
  descriptionLong: "Claude is Anthropic's AI assistant built on advanced language models with emphasis on safety and long-form reasoning. With a 200K+ token context window, Claude excels at processing entire books, research papers, and complex codebases. Known for nuanced writing and thoughtful analysis, it is favored by writers, researchers, and professionals.",
  descriptionLongZh: "Claude是Anthropic的AI助手，强调安全性和长文本推理能力。拥有超过20万令牌的上下文窗口，擅长处理整本书籍、研究论文和复杂代码库。",
  advantages: [
            "200K+ token context window for large documents",
            "Nuanced writing style producing quality prose",
            "Strong safety with Constitutional AI",
            "Excellent at complex instructions"
          ],
  advantagesZh: [
            "20万+令牌上下文窗口，可处理大型文档",
            "细腻的写作风格，生成优质文章",
            "宪法AI确保强大的安全性",
            "擅长处理复杂指令"
          ],
  useCases: [
            "Analyze 100+ page research papers and legal docs",
            "Edit long-form content like novels and reports",
            "Debug complex codebases step by step",
            "Conduct literature reviews with citations",
            "Generate detailed business reports"
          ],
  useCasesZh: [
            "分析100页以上的研究论文和法律文档",
            "编辑长篇幅内容，如小说和报告",
            "逐步调试复杂代码库",
            "带引用的文献综述"
          ],
  targetAudience: "Professionals needing detailed AI assistance -- writers, researchers, lawyers, developers, analysts.",
  targetAudienceZh: "需要详细AI辅助的专业人士——写作者、研究人员、律师、开发者和分析师。",
  pricingTiers: [
      {
        tier: "Free",
          tierZh: "免费版",
        price: "$0",
        features: [
          "Claude 4 Sonnet",
          "Limited daily messages",
          "Basic uploads"
        ],
        featuresZh: [
          "Claude 4 Sonnet模型",
          "每日消息限制",
          "基础文件上传",
        ],
      },
      {
        tier: "Pro",
          tierZh: "专业版",
        price: "$20/mo",
        features: [
          "Unlimited Claude 4 Sonnet",
          "Claude 4 Opus",
          "Projects"
        ],
        featuresZh: [
          "Claude 4 Sonnet无限使用",
          "Claude 4 Opus模型",
          "项目管理",
        ],
      },
      {
        tier: "Team",
          tierZh: "团队版",
        price: "$30/user/mo",
        features: [
          "All Pro features",
          "Higher limits",
          "Shared workspaces"
        ],
        featuresZh: [
          "所有专业版功能",
          "更高使用额度",
          "共享工作区",
        ],
      }
    ],  
  extensions: [
        {
          name: "Claude Code CLI",
          description: "Command-line coding assistant",
          descriptionZh: "命令行编码助手",
        },
        {
          name: "Claude API",
          description: "Enterprise API with SSO",
          descriptionZh: "企业级API，支持单点登录",
        }
      ],  
  scene: "content-creation",
  skills: [
            "prompt engineering",
            "document analysis",
            "creative writing",
            "code review",
            "research"
          ],  
  pros: [
            "Massive context window for entire books",
            "Superior writing quality",
            "Strong safety without sacrificing capability",
            "Detailed structured responses"
          ],
  prosZh: [
            "超大上下文窗口，可处理整本书籍",
            "卓越的写作质量",
            "不牺牲能力的安全性",
            "详细的结构化响应"
          ],
  cons: [
            "Strict daily limits on free tier",
            "No image generation",
            "Slower on complex tasks",
            "Limited integrations"
          ],
  consZh: [
            "免费版每日使用限制严格",
            "不支持图像生成",
            "复杂任务处理较慢",
            "集成有限"
          ],
  },

  {
    id: "gemini",
    name: "Google Gemini",
    description: "Google's multimodal AI model with deep Google ecosystem integration.",
  descriptionZh: "谷歌的多模态AI模型，深度集成谷歌生态系统。",
    category: "chatbots",
    tags: ["multimodal", "google", "reasoning", "search"],
    difficulty: "beginner",
    url: "https://gemini.google.com",
    rating: r(4.5),
    pricing: "Free / $19.99/mo Advanced",
    useCase: "Gemini's multimodal capabilities let you upload images, audio, and video for analysis. It integrates with Google apps like Gmail, Docs, and Drive.",
    icon: "\u{1F31F}",
  company: "Google DeepMind",
  companyZh: "谷歌DeepMind",
  founded: "2023",  headquarters: "Mountain View, CA",  
  descriptionLong: "Gemini is Google's natively multimodal AI model family built by Google DeepMind. It processes text, images, audio, video, and code simultaneously. Deeply integrated with Gmail, Docs, Drive, and Search, Gemini offers unique advantages for Google ecosystem users with real-time search access and workspace integration.",
  descriptionLongZh: "Gemini是谷歌DeepMind构建的原生多模态AI模型家族，可同时处理文本、图像、音频、视频和代码。深度集成Gmail、文档、云端硬盘和搜索。",
  advantages: [
            "Native multimodal processing of text/images/audio/video",
            "Deep Google Workspace integration",
            "Real-time Google Search access",
            "Generous free tier"
          ],
  advantagesZh: [
            "原生多模态处理",
            "深度集成谷歌工作区",
            "实时谷歌搜索",
            "慷慨的免费版本"
          ],
  useCases: [
            "Upload video for AI content analysis",
            "Plan trips with Google Maps integration",
            "Analyze Sheets data with natural language",
            "Draft Gmail emails with context"
          ],
  useCasesZh: [
            "上传视频进行AI内容分析",
            "集成谷歌地图规划旅行",
            "用自然语言分析表格数据",
            "在Gmail中撰写上下文相关的邮件"
          ],
  targetAudience: "Google users who want AI in their workflow -- Gmail, Workspace, and Android users.",
  targetAudienceZh: "希望AI融入工作流程的谷歌用户——Gmail、工作区和Android用户。",
  pricingTiers: [
      {
        tier: "Free",
          tierZh: "免费版",
        price: "$0",
        features: [
          "Gemini 2.0 Flash",
          "Google Search",
          "File uploads"
        ],
        featuresZh: [
          "Gemini 2.0 Flash模型",
          "谷歌搜索",
          "文件上传",
        ],
      },
      {
        tier: "Advanced",
          tierZh: "高级版",
        price: "$19.99/mo",
        features: [
          "Gemini 2.0 Pro",
          "1TB Drive storage",
          "Workspace integration"
        ],
        featuresZh: [
          "Gemini 2.0 Pro模型",
          "1TB云盘存储",
          "工作区集成",
        ],
      }
    ],  
  extensions: [
        {
          name: "Gemini for Workspace",
          description: "AI across Gmail, Docs, Sheets",
          descriptionZh: "Gmail、文档和表格的AI功能",
        },
        {
          name: "Gemini Mobile",
          description: "Android/iOS app with voice",
          descriptionZh: "支持语音的Android/iOS应用",
        }
      ],  
  scene: "office-productivity",
  skills: [
            "multimodal AI",
            "Google Workspace",
            "data analysis",
            "video analysis",
            "search"
          ],  
  pros: [
            "Natively multimodal without separate tools",
            "Seamless Google integration",
            "Generous free tier",
            "Real-time search"
          ],
  prosZh: [
            "原生多模态，无需额外工具",
            "与谷歌应用无缝集成",
            "慷慨的免费版本",
            "实时搜索能力"
          ],
  cons: [
            "Weaker creative writing vs Claude/ChatGPT",
            "Privacy concerns with Google",
            "Advanced tier less competitive"
          ],
  consZh: [
            "创意写作能力较弱",
            "隐私问题",
            "高级版竞争力不足"
          ],
  },

  {
    id: "deepseek",
    name: "DeepSeek",
    description: "Open-source LLM with strong reasoning capabilities and competitive performance.",
  descriptionZh: "开源LLM，具有强大的推理能力和有竞争力的性能。",
    category: "chatbots",
    tags: ["reasoning", "open-source", "coding", "analysis"],
    difficulty: "intermediate",
    url: "https://chat.deepseek.com",
    rating: r(4.4),
    pricing: "Free",
    useCase: "DeepSeek offers strong reasoning and coding capabilities at no cost. Its open-source nature allows self-hosting and customization.",
    icon: "\u{1F50D}",
  company: "DeepSeek",
  companyZh: "深度求索",
  founded: "2023",  headquarters: "Hangzhou, China",  
  descriptionLong: "DeepSeek is a Chinese AI company known for powerful open-source language models. DeepSeek-R1 and V3 deliver performance comparable to leading proprietary models at a fraction of the cost. Strong in mathematics, coding, and logical reasoning, it is a favorite in the open-source community for transparency and impressive benchmarks.",
  descriptionLongZh: "深度求索是一家中国AI公司，以强大的开源语言模型闻名。DeepSeek-R1和V3的性能可与领先的专有模型媲美，而成本仅为其一小部分。",
  advantages: [
            "Fully open-source for self-hosting",
            "Exceptional reasoning and math",
            "Cost-effective API pricing",
            "Strong coding performance"
          ],
  advantagesZh: [
            "完全开源",
            "卓越的推理和数学能力",
            "经济高效的API",
            "强大的编程性能"
          ],
  useCases: [
            "Self-host LLM on your infrastructure",
            "Solve complex math problems",
            "Build custom AI apps with open weights",
            "Code generation and debugging"
          ],
  useCasesZh: [
            "在自己的基础设施上自行托管LLM",
            "解决复杂数学问题",
            "使用开放权重构建自定义AI应用",
            "代码生成和调试"
          ],
  targetAudience: "Developers and organizations wanting powerful AI with full control over deployment and privacy.",
  targetAudienceZh: "希望在部署和隐私方面拥有完全控制的开发者和组织。",
  pricingTiers: [
      {
        tier: "Free Chat",
          tierZh: "免费聊天版",
        price: "$0",
        features: [
          "Unlimited DeepSeek chat",
          "DeepSeek-R1",
          "File uploads"
        ],
        featuresZh: [
          "DeepSeek无限聊天",
          "DeepSeek-R1模型",
          "文件上传",
        ],
      },
      {
        tier: "API",
          tierZh: "API版",
        price: "From $0.14/M tokens",
        features: [
          "R1 and V3 API",
          "Rate limits",
          "Fine-tuning"
        ],
        featuresZh: [
          "R1和V3 API",
          "速率限制",
          "模型微调",
        ],
      }
    ],  
  extensions: [
        {
          name: "DeepSeek API",
          description: "REST API for app integration",
          descriptionZh: "用于应用集成的REST API",
        },
        {
          name: "Ollama Support",
          description: "Run locally via Ollama",
          descriptionZh: "通过Ollama本地运行",
        }
      ],  
  scene: "free-open-source",
  skills: [
            "open-source AI",
            "self-hosting",
            "mathematical reasoning",
            "API integration",
            "fine-tuning"
          ],  
  pros: [
            "Free web chat with no limits",
            "Open-source for self-hosting",
            "Excellent performance-to-cost",
            "Strong reasoning ability"
          ],
  prosZh: [
            "免费网页聊天，无使用限制",
            "开源，可自行托管",
            "卓越的性价比",
            "强大的推理能力"
          ],
  cons: [
            "Inconsistent server availability",
            "Less refined conversation ability",
            "Documentation in Chinese",
            "Limited enterprise support"
          ],
  consZh: [
            "服务器可用性不稳定",
            "对话能力不够精细",
            "文档为中文",
            "企业支持有限"
          ],
  },

  {
    id: "perplexity",
    name: "Perplexity AI",
    description: "AI-powered search engine that provides answers with real-time citations.",
  descriptionZh: "AI驱动的搜索引擎，提供带实时引用的答案。",
    category: "chatbots",
    tags: ["search", "research", "citations", "real-time"],
    difficulty: "beginner",
    url: "https://www.perplexity.ai",
    rating: r(4.5),
    pricing: "Free / $20/mo Pro",
    useCase: "Perplexity is an AI search engine that answers questions with cited sources. Perfect for research, fact-checking, and staying updated.",
    icon: "\u{1F4A1}",
  company: "Perplexity AI",
  companyZh: "Perplexity AI",
  founded: "2022",  headquarters: "San Francisco, CA",  
  descriptionLong: "Perplexity AI combines LLMs with real-time web search to deliver answers with inline citations. Unlike traditional search, it synthesizes multiple sources into coherent answers with references. Supports file uploads, image recognition, and pro features. Its focus on source transparency makes it a favorite for researchers and students.",
  descriptionLongZh: "Perplexity AI结合LLM与实时网络搜索，提供带有内联引用的答案。综合多个来源形成带有参考文献的连贯答案。",
  advantages: [
            "Answers with real-time citations",
            "Synthesizes multiple sources",
            "File upload analysis",
            "Adjustable focus modes"
          ],
  advantagesZh: [
            "带实时引用的答案",
            "综合多个来源",
            "文件分析能力",
            "可调节的聚焦模式"
          ],
  useCases: [
            "Research with cited sources",
            "Fact-check with real-time search",
            "Analyze uploaded documents",
            "Curated news summaries"
          ],
  useCasesZh: [
            "带引用来源的研究",
            "实时搜索进行事实核查",
            "分析上传的文档",
            "精选新闻摘要"
          ],
  targetAudience: "Researchers, students, and journalists needing accurate cited information quickly.",
  targetAudienceZh: "需要快速获取准确引用信息的研究人员、学生和记者。",
  pricingTiers: [
      {
        tier: "Free",
          tierZh: "免费版",
        price: "$0",
        features: [
          "Standard search",
          "Limited Pro searches",
          "File uploads"
        ],
        featuresZh: [
          "标准搜索",
          "专业搜索有限额度",
          "文件上传",
        ],
      },
      {
        tier: "Pro",
          tierZh: "专业版",
        price: "$20/mo",
        features: [
          "Unlimited Pro",
          "Unlimited file analysis",
          "API access"
        ],
        featuresZh: [
          "专业搜索无限使用",
          "文件分析无限使用",
          "API访问权限",
        ],
      }
    ],  
  extensions: [
        {
          name: "Perplexity Browser Extension",
          description: "Search anywhere on the web",
          descriptionZh: "在网页任意位置搜索",
        },
        {
          name: "Perplexity Mobile",
          description: "iOS and Android apps",
          descriptionZh: "iOS和Android应用",
        }
      ],  
  scene: "office-productivity",
  skills: [
            "research",
            "fact-checking",
            "information synthesis",
            "source evaluation",
            "academic writing"
          ],  
  pros: [
            "Cited answers with sources",
            "Excellent for fact-checking",
            "Generous free tier",
            "File analysis capability"
          ],
  prosZh: [
            "带来源引用的答案",
            "非常适合事实核查",
            "慷慨的免费版本",
            "文件分析能力"
          ],
  cons: [
            "Limited creative writing",
            "Pro plan expensive",
            "Quality depends on web search",
            "Weak for coding"
          ],
  consZh: [
            "创意写作能力有限",
            "Pro版价格较高",
            "质量依赖网络搜索",
            "编程能力较弱"
          ],
  },

  {
    id: "midjourney",
    name: "Midjourney",
    description: "Leading AI image generator known for artistic quality and stylistic versatility.",
  descriptionZh: "领先的AI图像生成器，以艺术质量和风格多样性闻名。",
    category: "image-generation",
    tags: ["art", "design", "creative", "high-quality"],
    difficulty: "intermediate",
    url: "https://www.midjourney.com",
    rating: r(4.8),
    pricing: "$10/mo starting",
    useCase: "Midjourney produces stunning artistic images from text prompts. Best for concept art, illustrations, branding visuals, and creative projects.",
    icon: "\u{1F3A8}",
  company: "Midjourney Inc.",
  companyZh: "Midjourney",
  founded: "2021",  headquarters: "San Francisco, CA",  
  descriptionLong: "Midjourney is the highest-quality AI image generation platform, known for its distinctive artistic style. Operating through Discord and web, it excels at concept art, illustrations, and character designs. Its advanced parameter system allows fine-grained control over style, composition, and lighting, making it the go-to for professional artists.",
  descriptionLongZh: "Midjourney是最高质量的AI图像生成平台，以其独特的艺术风格著称。通过Discord和网页运行，擅长概念艺术、插图和角色设计。",
  advantages: [
            "Highest artistic quality",
            "Advanced parameter control",
            "Strong community references",
            "Regular model updates"
          ],
  advantagesZh: [
            "最高艺术质量",
            "高级参数控制",
            "强大的社区参考",
            "定期模型更新"
          ],
  useCases: [
            "Concept art for games and films",
            "Brand visuals and marketing",
            "Book illustrations",
            "Product visualizations",
            "Creative prototyping"
          ],
  useCasesZh: [
            "游戏和电影概念艺术",
            "品牌视觉和营销",
            "书籍插图",
            "产品可视化"
          ],
  targetAudience: "Artists, designers, and creative professionals needing high-quality AI visuals.",
  targetAudienceZh: "需要高质量AI视觉内容的艺术家、设计师和创意专业人士。",
  pricingTiers: [
      {
        tier: "Basic",
          tierZh: "基础版",
        price: "$10/mo",
        features: [
          "3.3 hrs/month GPU",
          "Commercial license"
        ],
        featuresZh: ["每月3.3小时GPU时长", "商业使用授权"],
      },
      {
        tier: "Standard",
          tierZh: "标准版",
        price: "$30/mo",
        features: [
          "15 hrs/month GPU",
          "Stealth mode"
        ],
        featuresZh: ["每月15小时GPU时长", "隐身模式"],
      },
      {
        tier: "Pro",
          tierZh: "专业版",
        price: "$60/mo",
        features: [
          "30 hrs/month GPU",
          "Priority queue"
        ],
        featuresZh: ["每月30小时GPU时长", "优先队列"],
      }
    ],  
  extensions: [
        {
          name: "Midjourney Discord Bot",
          description: "Primary interface via Discord",
          descriptionZh: "通过Discord使用的主要界面",
        },
        {
          name: "Midjourney Web",
          description: "Web editor and gallery",
          descriptionZh: "网页编辑器和作品集",
        }
      ],  
  scene: "design-video",
  affiliateUrl: "https://www.midjourney.com/affiliate",
  hasAffiliate: true,
  skills: [
            "prompt engineering",
            "art direction",
            "visual design",
            "composition",
            "color theory"
          ],  
  pros: [
            "Best image quality available",
            "Fine parameter control",
            "Strong community",
            "Regular updates"
          ],
  prosZh: [
            "最佳图像质量",
            "精细的参数控制",
            "强大的社区",
            "定期模型更新"
          ],
  cons: [
            "Requires Discord",
            "Steep learning curve",
            "No free tier",
            "Limited vs SD with LoRAs"
          ],
  consZh: [
            "需要使用Discord",
            "学习曲线陡峭",
            "无免费版本",
            "相比SD的LoRA支持有限"
          ],
  },

  {
    id: "dalle3",
    name: "DALL-E 3",
    description: "OpenAI's image generator integrated into ChatGPT with strong prompt adherence.",
  descriptionZh: "OpenAI的图像生成器，集成在ChatGPT中，指令跟随能力强。",
    category: "image-generation",
    tags: ["openai", "chatgpt", "design", "realistic"],
    difficulty: "beginner",
    url: "https://openai.com/dall-e-3",
    rating: r(4.6),
    pricing: "Included with ChatGPT Plus",
    useCase: "DALL-E 3 generates images directly within ChatGPT. Great for quick visual ideas, social media graphics, and prototyping designs.",
    icon: "\u{1F5BC}️",
  company: "OpenAI",
  companyZh: "OpenAI",
  founded: "2015",  headquarters: "San Francisco, CA",  
  descriptionLong: "DALL-E 3 is OpenAI's latest image generation model, integrated into ChatGPT. It excels at following complex prompts with high accuracy, generating detailed images from text. Working within ChatGPT allows iterative refinement through natural conversation. Best for quick visual ideation and integrated workflows.",
  descriptionLongZh: "DALL-E 3是OpenAI最新的图像生成模型，集成在ChatGPT中。擅长高精度地跟随复杂提示词生成详细图像。",
  advantages: [
            "Integrated into ChatGPT",
            "Excellent prompt adherence",
            "Natural conversation refinement",
            "Included with ChatGPT Plus"
          ],
  advantagesZh: [
            "集成在ChatGPT中",
            "出色的提示词跟随能力",
            "通过对话自然优化",
            "包含在ChatGPT Plus中"
          ],
  useCases: [
            "Social media graphics",
            "Blog illustrations",
            "Design concept prototyping",
            "Marketing visuals"
          ],
  useCasesZh: [
            "社交媒体图像",
            "博客插图",
            "设计概念原型",
            "营销视觉"
          ],
  targetAudience: "ChatGPT users wanting integrated image generation without leaving the chat.",
  targetAudienceZh: "希望在不离开聊天的情况下集成图像生成的ChatGPT用户。",
  pricingTiers: [
      {
        tier: "ChatGPT Free",
          tierZh: "ChatGPT免费版",
        price: "$0",
        features: [
          "Limited DALL-E 3",
          "Basic resolution"
        ],
        featuresZh: ["DALL-E 3有限使用", "基础分辨率"],
      },
      {
        tier: "ChatGPT Plus",
          tierZh: "ChatGPT Plus版",
        price: "$20/mo",
        features: [
          "Unlimited DALL-E 3",
          "HD resolution"
        ],
        featuresZh: ["DALL-E 3无限使用", "高清分辨率"],
      }
    ],  
  extensions: [
        {
          name: "Built into ChatGPT",
          description: "Access via ChatGPT interface",
          descriptionZh: "通过ChatGPT界面访问",
        }
      ],  
  scene: "design-video",
  skills: [
            "prompt engineering",
            "creative visualization",
            "design ideation",
            "image prompting"
          ],  
  pros: [
            "Seamless ChatGPT integration",
            "Excellent prompt following",
            "Fast iteration and refinement"
          ],
  prosZh: [
            "与ChatGPT无缝集成",
            "出色的指令跟随能力",
            "快速迭代和优化"
          ],
  cons: [
            "Requires ChatGPT subscription",
            "Less artistic than Midjourney",
            "Not standalone tool"
          ],
  consZh: [
            "需要ChatGPT订阅",
            "艺术性不如Midjourney",
            "非独立工具"
          ],
  },

  {
    id: "stable-diffusion",
    name: "Stable Diffusion",
    description: "Open-source image generation model with full local control and customization.",
  descriptionZh: "开源图像生成模型，支持本地控制和完全自定义。",
    category: "image-generation",
    tags: ["open-source", "local", "customizable", "free"],
    difficulty: "advanced",
    url: "https://stability.ai",
    rating: r(4.4),
    pricing: "Free (open-source)",
    useCase: "Stable Diffusion runs locally on your hardware with full control. Ideal for developers, researchers, and anyone needing uncensored or customized generation.",
    icon: "\u{26A1}",
  company: "Stability AI",
  companyZh: "Stability AI",
  founded: "2020",  headquarters: "London, UK",  
  descriptionLong: "Stable Diffusion is a powerful open-source image generation model running locally on your hardware. Developed by Stability AI, it offers complete control with extensive community support, custom models (LoRAs, Checkpoints), and fine-tuning. Provides unlimited free generation, full privacy, and deep customization through its open ecosystem.",
  descriptionLongZh: "Stable Diffusion是一个强大的开源图像生成模型，可在本地硬件上运行。提供完全控制权，拥有广泛的社区支持、自定义模型和微调能力。",
  advantages: [
            "Local execution with full privacy",
            "Free and open-source",
            "Extensive community models",
            "Full customization via fine-tuning"
          ],
  advantagesZh: [
            "本地运行，完全隐私保护",
            "免费开源",
            "广泛的社区模型",
            "通过微调实现完全自定义"
          ],
  useCases: [
            "Unlimited image generation",
            "Custom model fine-tuning",
            "Sensitive content processing",
            "Advanced techniques (ControlNet)",
            "AI image app building"
          ],
  useCasesZh: [
            "无限图像生成",
            "自定义模型微调",
            "本地处理敏感内容",
            "高级技术（ControlNet等）"
          ],
  targetAudience: "Developers and power users wanting complete control over AI image generation with no restrictions.",
  targetAudienceZh: "希望完全控制AI图像生成且无限制的开发者和高级用户。",
  pricingTiers: [
      {
        tier: "Self-hosted",
          tierZh: "自托管版",
        price: "$0",
        features: [
          "Unlimited generation",
          "Full privacy",
          "All models"
        ],
        featuresZh: [
          "无限生成",
          "完全隐私保护",
          "所有模型",
        ],
      },
      {
        tier: "API",
          tierZh: "API版",
        price: "Pay-as-you-go",
        features: [
          "Cloud hosted",
          "API access",
          "No GPU needed"
        ],
        featuresZh: [
          "云端托管",
          "API访问权限",
          "无需GPU",
        ],
      }
    ],  
  extensions: [
        {
          name: "Automatic1111 WebUI",
          description: "Most popular SD interface",
          descriptionZh: "最流行的Stable Diffusion界面",
        },
        {
          name: "ComfyUI",
          description: "Node-based workflow interface",
          descriptionZh: "基于节点的可视化工作流界面",
        }
      ],  
  scene: "free-open-source",
  skills: [
            "model fine-tuning",
            "LoRA training",
            "prompt engineering",
            "ControlNet",
            "image processing"
          ],  
  pros: [
            "Free with unlimited generation",
            "Full privacy local execution",
            "Extensive community ecosystem",
            "Deep customization"
          ],
  prosZh: [
            "免费无限生成",
            "完全本地隐私保护",
            "广泛的社区生态系统",
            "深度自定义"
          ],
  cons: [
            "Requires powerful GPU",
            "Steep learning curve",
            "Complex setup",
            "No official mobile app"
          ],
  consZh: [
            "需要强大的GPU",
            "学习曲线陡峭",
            "安装配置复杂",
            "无官方移动应用"
          ],
  },

  {
    id: "adobe-firefly",
    name: "Adobe Firefly",
    description: "Adobe's generative AI suite integrated with Creative Cloud for professional design.",
  descriptionZh: "Adobe的生成式AI套件，集成Creative Cloud，用于专业设计。",
    category: "image-generation",
    tags: ["adobe", "design", "professional", "integration"],
    difficulty: "intermediate",
    url: "https://www.adobe.com/products/firefly.html",
    rating: r(4.3),
    pricing: "Free tier / Creative Cloud subscription",
    useCase: "Firefly integrates AI image generation into Adobe's design tools. Best for designers who already use Photoshop, Illustrator, or Express.",
    icon: "\u{1F525}",
  company: "Adobe Inc.",
  companyZh: "Adobe（奥多比）",
  founded: "1982",  headquarters: "San Jose, CA",  
  descriptionLong: "Adobe Firefly is Adobe's generative AI family integrated into Creative Cloud. It enables designers to generate images, apply effects, and extend compositions using natural language. Commercially safe with licensed training data and enterprise-grade features, Firefly is ideal for professional design workflows in Photoshop, Illustrator, and Express.",
  descriptionLongZh: "Adobe Firefly是Adobe的生成式AI家族，集成在Creative Cloud中。设计师可通过自然语言生成图像、应用效果和扩展构图。",
  advantages: [
            "Deep Creative Cloud integration",
            "Commercially safe training",
            "Generative Fill for photo editing",
            "Enterprise-grade security"
          ],
  advantagesZh: [
            "深度集成Creative Cloud",
            "商业安全的训练数据",
            "生成式填充",
            "企业级安全"
          ],
  useCases: [
            "Generative Fill in Photoshop",
            "Social media graphics in Express",
            "AI text effects",
            "Image extension",
            "Brand asset variations"
          ],
  useCasesZh: [
            "Photoshop中的生成式填充",
            "Express中的社交媒体图像",
            "AI文字效果",
            "图像扩展"
          ],
  targetAudience: "Professional designers using Creative Cloud who want integrated AI capabilities.",
  targetAudienceZh: "使用Creative Cloud并希望集成AI能力的专业设计师。",
  pricingTiers: [
      {
        tier: "Free",
          tierZh: "免费版",
        price: "$0",
        features: [
          "25 credits/month",
          "Basic features",
          "Express access"
        ],
        featuresZh: [
          "每月25积分",
          "基础功能",
          "Express访问权限",
        ],
      },
      {
        tier: "Premium",
          tierZh: "高级版",
        price: "$4.99/mo",
        features: [
          "100 credits/month",
          "Full features",
          "Commercial use"
        ],
        featuresZh: [
          "每月100积分",
          "全部功能",
          "商业使用授权",
        ],
      }
    ],  
  extensions: [
        {
          name: "Adobe Photoshop",
          description: "Generative Fill built in",
          descriptionZh: "内置生成式填充功能",
        },
        {
          name: "Adobe Express",
          description: "Quick AI design tool",
          descriptionZh: "快速AI设计工具",
        }
      ],  
  scene: "design-video",
  skills: [
            "photo editing",
            "graphic design",
            "brand design",
            "creative direction",
            "commercial art"
          ],  
  pros: [
            "Seamless Creative Cloud integration",
            "Commercially safe",
            "Best-in-class Generative Fill",
            "Enterprise ready"
          ],
  prosZh: [
            "与Creative Cloud无缝集成",
            "商业使用安全",
            "卓越的生成式填充",
            "企业级就绪"
          ],
  cons: [
            "Requires CC subscription",
            "Limited free credits",
            "Less artistic freedom",
            "Adobe ecosystem only"
          ],
  consZh: [
            "需要CC订阅",
            "免费积分有限",
            "艺术自由度较低",
            "仅限Adobe生态系统"
          ],
  },

  {
    id: "leonardo-ai",
    name: "Leonardo AI",
    description: "AI image generation platform with fine-tuned models for games, characters, and assets.",
  descriptionZh: "AI图像生成平台，为游戏、角色和资产提供微调模型。",
    category: "image-generation",
    tags: ["gaming", "assets", "characters", "models"],
    difficulty: "intermediate",
    url: "https://leonardo.ai",
    rating: r(4.4),
    pricing: "Free tier / from $10/mo",
    useCase: "Leonardo AI offers specialized models for game assets, character design, and environment art. Great for indie game developers and content creators.",
    icon: "\u{1F58C}️",
  company: "Leonardo AI",
  companyZh: "Leonardo AI",
  founded: "2022",  headquarters: "Sydney, Australia",  
  descriptionLong: "Leonardo AI is a specialized image generation platform for game assets, character design, and environment art. It offers fine-tuned models for different art styles from realistic to anime. Features include AI canvas for in-painting, real-time generation, and dataset creation tools. Popular among indie game developers and content creators.",
  descriptionLongZh: "Leonardo AI是一个针对游戏资产、角色设计和环境艺术的专业图像生成平台。提供针对不同艺术风格微调的模型。",
  advantages: [
            "Specialized game asset models",
            "AI canvas for in-painting",
            "Real-time generation",
            "Community model sharing"
          ],
  advantagesZh: [
            "专业游戏资产模型",
            "AI画布用于内绘",
            "实时生成",
            "社区模型共享"
          ],
  useCases: [
            "Game character design",
            "Environment texture creation",
            "Marketing game visuals",
            "Concept art pipeline",
            "Custom model training"
          ],
  useCasesZh: [
            "游戏角色设计",
            "环境纹理创建",
            "营销视觉",
            "概念艺术"
          ],
  targetAudience: "Game developers, indie creators, and digital artists needing specialized AI for game assets.",
  targetAudienceZh: "需要专业AI生成游戏资产的游戏开发者、独立创作者和数字艺术家。",
  pricingTiers: [
      {
        tier: "Free",
          tierZh: "免费版",
        price: "$0",
        features: [
          "150 tokens/day",
          "Standard models"
        ],
        featuresZh: ["每日150点数", "标准模型"],
      },
      {
        tier: "Starter",
          tierZh: "入门版",
        price: "$10/mo",
        features: [
          "2500 tokens/month",
          "Faster generation"
        ],
        featuresZh: ["每月2500点数", "更快的生成速度"],
      },
      {
        tier: "Pro",
          tierZh: "专业版",
        price: "$24/mo",
        features: [
          "8000 tokens/month",
          "API access"
        ],
        featuresZh: ["每月8000点数", "API访问权限"],
      }
    ],  
  extensions: [
        {
          name: "Leonardo Web App",
          description: "Full web-based creation platform",
          descriptionZh: "基于网页的完整创作平台",
        }
      ],  
  scene: "design-video",
  skills: [
            "game art",
            "character design",
            "environment art",
            "texture creation",
            "concept art"
          ],  
  pros: [
            "Specialized for game assets",
            "Generous free tier",
            "Real-time generation",
            "Custom model training"
          ],
  prosZh: [
            "专为游戏资产优化",
            "慷慨的免费版本",
            "实时生成",
            "自定义模型训练"
          ],
  cons: [
            "Token limits on usage",
            "Inconsistent quality",
            "Less photorealistic output",
            "Smaller community"
          ],
  consZh: [
            "点数使用限制",
            "质量不稳定",
            "输出不够照片级真实",
            "社区规模较小"
          ],
  },

  {
    id: "runway",
    name: "Runway",
    description: "Professional AI video generation and editing platform with advanced motion control.",
  descriptionZh: "专业AI视频生成和编辑平台，具有高级运动控制。",
    category: "video-generation",
    tags: ["video", "editing", "motion", "professional"],
    difficulty: "intermediate",
    url: "https://runwayml.com",
    rating: r(4.5),
    pricing: "Free tier / from $15/mo",
    useCase: "Runway generates and edits video using AI. Use it for creating short films, social media clips, and professional video content with text prompts.",
    icon: "\u{1F3AC}",
  company: "Runway ML",
  companyZh: "Runway ML",
  founded: "2018",  headquarters: "New York, NY",  
  descriptionLong: "Runway is a professional AI video generation and editing platform with advanced motion control. It offers text-to-video, image-to-video, and video-to-video generation along with powerful editing tools like in-painting, motion tracking, and green screen removal. Used by filmmakers, content creators, and studios for rapid video production.",
  descriptionLongZh: "Runway是一个专业的AI视频生成和编辑平台。提供文本转视频、图像转视频以及内绘、运动跟踪等高级编辑工具。",
  advantages: [
            "Advanced motion control",
            "Multiple generation modes",
            "Professional editing tools",
            "Real-time collaboration"
          ],
  advantagesZh: [
            "高级运动控制",
            "多种生成模式",
            "专业编辑工具",
            "实时协作"
          ],
  useCases: [
            "Short film and video creation",
            "Social media video content",
            "Video background removal",
            "Motion tracking and editing",
            "AI video effects"
          ],
  useCasesZh: [
            "短片和视频创作",
            "社交媒体视频内容",
            "视频背景移除",
            "AI视频特效"
          ],
  targetAudience: "Video creators, filmmakers, and content producers who want AI-powered video generation and editing.",
  targetAudienceZh: "需要AI驱动的视频生成和编辑的视频创作者、电影制作人和内容制作人。",
  pricingTiers: [
      {
        tier: "Free",
          tierZh: "免费版",
        price: "$0",
        features: [
          "Limited generations",
          "720p export"
        ],
        featuresZh: ["有限生成次数", "720p导出"],
      },
      {
        tier: "Pro",
          tierZh: "专业版",
        price: "$15/mo",
        features: [
          "Unlimited generations",
          "4K export",
          "Green screen"
        ],
        featuresZh: [
          "无限生成",
          "4K导出",
          "绿幕功能",
        ],
      },
      {
        tier: "Team",
          tierZh: "团队版",
        price: "$30/mo",
        features: [
          "All Pro",
          "Collaboration",
          "Priority support"
        ],
        featuresZh: [
          "所有专业版功能",
          "团队协作",
          "优先支持",
        ],
      }
    ],  
  extensions: [
        {
          name: "Runway Browser",
          description: "Web-based editing platform",
          descriptionZh: "基于网页的编辑平台",
        }
      ],  
  scene: "design-video",
  skills: [
            "video editing",
            "motion graphics",
            "content creation",
            "visual effects",
            "storyboarding"
          ],  
  pros: [
            "Multiple video generation modes",
            "Professional editing tools",
            "Real-time collaboration",
            "Regular feature updates"
          ],
  prosZh: [
            "多种生成模式",
            "专业编辑工具",
            "实时协作",
            "定期功能更新"
          ],
  cons: [
            "Expensive pro plans",
            "Learning curve for advanced features",
            "Generation quality varies",
            "Limited free tier"
          ],
  consZh: [
            "专业版价格较高",
            "学习曲线陡峭",
            "质量不稳定",
            "免费版功能有限"
          ],
  },

  {
    id: "pika",
    name: "Pika",
    description: "Easy-to-use AI video generator focused on quick, high-quality video creation.",
  descriptionZh: "易于使用的AI视频生成器，专注于快速创建高质量视频。",
    category: "video-generation",
    tags: ["video", "quick", "social-media", "easy"],
    difficulty: "beginner",
    url: "https://pika.art",
    rating: r(4.3),
    pricing: "Free tier / from $10/mo",
    useCase: "Pika makes AI video generation accessible to everyone. Great for creating short video clips, animations, and social media content from text prompts.",
    icon: "\u{1F3A5}",
  company: "Pika Labs",
  companyZh: "Pika Labs",
  founded: "2023",  headquarters: "San Francisco, CA",  
  descriptionLong: "Pika is an easy-to-use AI video generator focused on quick, high-quality video creation from text and image prompts. It excels at short-form content with features like video in-painting, style transfer, and motion control. Designed for accessibility, Pika makes AI video generation available to everyone without technical expertise.",
  descriptionLongZh: "Pika是一个易于使用的AI视频生成器，可从文本和图像提示快速创建高质量视频。无需技术专业知识即可使用。",
  advantages: [
            "Easy to use interface",
            "Quick video generation",
            "Text and image prompts",
            "Video in-painting"
          ],
  advantagesZh: [
            "易于使用的界面",
            "快速生成",
            "支持文本和图像提示",
            "视频内绘"
          ],
  useCases: [
            "Short social media clips",
            "Animated marketing content",
            "Creative video effects",
            "Quick video prototyping"
          ],
  useCasesZh: [
            "社交媒体短视频",
            "动画营销内容",
            "创意视频特效",
            "快速视频原型"
          ],
  targetAudience: "Social media creators and marketers who want easy AI video generation without technical skills.",
  targetAudienceZh: "希望无需技术技能即可轻松生成AI视频的社交媒体创作者和营销人员。",
  pricingTiers: [
      {
        tier: "Free",
          tierZh: "免费版",
        price: "$0",
        features: [
          "Limited generations",
          "Standard quality"
        ],
        featuresZh: ["有限生成次数", "标准质量"],
      },
      {
        tier: "Pro",
          tierZh: "专业版",
        price: "$10/mo",
        features: [
          "More generations",
          "HD quality",
          "Faster queue"
        ],
        featuresZh: [
          "更多生成次数",
          "高清质量",
          "更快的处理队列",
        ],
      }
    ],  
  extensions: [
        {
          name: "Pika Web App",
          description: "Browser-based video generation",
          descriptionZh: "基于浏览器的视频生成",
        }
      ],  
  scene: "design-video",
  skills: [
            "video creation",
            "social media content",
            "creative effects",
            "animation"
          ],  
  pros: [
            "Very easy to use",
            "Fast generation speed",
            "Good for social media",
            "Free tier available"
          ],
  prosZh: [
            "非常易于使用",
            "快速生成",
            "适合社交媒体",
            "提供免费版本"
          ],
  cons: [
            "Limited video length",
            "Less control over output",
            "Lower quality than Runway",
            "Fewer features"
          ],
  consZh: [
            "视频时长有限",
            "对输出控制较少",
            "质量不如Runway",
            "功能较少"
          ],
  },

  {
    id: "heygen",
    name: "HeyGen",
    description: "AI video platform for creating talking avatars and professional presentations.",
  descriptionZh: "AI视频平台，用于创建会说话的虚拟形象和专业演示。",
    category: "video-generation",
    tags: ["avatars", "presentation", "talking", "business"],
    difficulty: "intermediate",
    url: "https://www.heygen.com",
    rating: r(4.4),
    pricing: "Free tier / from $29/mo",
    useCase: "HeyGen creates talking-head videos from text or scripts using realistic avatars. Perfect for training videos, marketing content, and global communications.",
    icon: "\u{1F3AD}",
  company: "HeyGen",
  companyZh: "HeyGen",
  founded: "2020",  headquarters: "Los Angeles, CA",  
  descriptionLong: "HeyGen is an AI video platform for creating talking avatars and professional presentations. It generates realistic talking-head videos from text or scripts using digital avatars. Features include multi-language support, custom avatar creation, and template-based video production. Popular for training videos, marketing content, and corporate communications.",
  descriptionLongZh: "HeyGen是一个AI视频平台，用于创建会说话的虚拟形象。通过数字虚拟形象从文本生成逼真的口播视频，支持多语言。",
  advantages: [
            "Realistic talking avatars",
            "Multi-language support",
            "Custom avatar creation",
            "Template library"
          ],
  advantagesZh: [
            "逼真的说话虚拟形象",
            "多语言支持",
            "自定义虚拟形象创建",
            "模板库"
          ],
  useCases: [
            "Training and educational videos",
            "Marketing video content",
            "Corporate communications",
            "Multi-language content",
            "Social media avatars"
          ],
  useCasesZh: [
            "培训和教育视频",
            "营销视频内容",
            "企业沟通",
            "多语言内容"
          ],
  targetAudience: "Businesses and content creators who need professional talking-head videos at scale.",
  targetAudienceZh: "需要规模化制作专业口播视频的企业和内容创作者。",
  pricingTiers: [
      {
        tier: "Free",
          tierZh: "免费版",
        price: "$0",
        features: [
          "1 min video",
          "Watermark",
          "Basic avatars"
        ],
        featuresZh: [
          "1分钟视频",
          "包含水印",
          "基础虚拟形象",
        ],
      },
      {
        tier: "Creator",
          tierZh: "创作者版",
        price: "$29/mo",
        features: [
          "10 mins/month",
          "No watermark",
          "HD export"
        ],
        featuresZh: [
          "每月10分钟",
          "无水印",
          "高清导出",
        ],
      },
      {
        tier: "Business",
          tierZh: "商务版",
        price: "$89/mo",
        features: [
          "30 mins/month",
          "Custom avatars",
          "Priority support"
        ],
        featuresZh: [
          "每月30分钟",
          "自定义虚拟形象",
          "优先支持",
        ],
      }
    ],  
  extensions: [
        {
          name: "HeyGen Web",
          description: "Browser-based video creation platform",
          descriptionZh: "基于浏览器的视频创作平台",
        }
      ],  
  scene: "design-video",
  skills: [
            "video production",
            "avatar creation",
            "voiceover",
            "multi-language content",
            "corporate training"
          ],  
  pros: [
            "Realistic avatar quality",
            "Multi-language support",
            "Fast video production",
            "Professional templates"
          ],
  prosZh: [
            "逼真的虚拟形象质量",
            "多语言支持",
            "快速视频制作",
            "专业模板"
          ],
  cons: [
            "Expensive compared to alternatives",
            "Avatars can feel uncanny",
            "Limited creative control",
            "Watermark on free tier"
          ],
  consZh: [
            "相比替代方案价格较高",
            "虚拟形象可能显得不自然",
            "创意控制有限",
            "免费版有水印"
          ],
  },

  {
    id: "jasper",
    name: "Jasper AI",
    description: "AI writing assistant built for marketing teams and content creators.",
  descriptionZh: "为营销团队和内容创作者设计的AI写作助手。",
    category: "writing",
    tags: ["marketing", "content", "copywriting", "brand"],
    difficulty: "beginner",
    url: "https://www.jasper.ai",
    rating: r(4.3),
    pricing: "from $49/mo",
    useCase: "Jasper specializes in marketing copy, blog posts, and brand content. It uses brand voice customization to produce consistent on-brand writing.",
    icon: "\u{270D}️",
  company: "Jasper AI",
  companyZh: "Jasper AI",
  founded: "2021",  headquarters: "Austin, TX",  
  descriptionLong: "Jasper is an AI writing assistant built for marketing teams and content creators. It specializes in creating brand-aligned copy, blog posts, social media content, and ad copy. With brand voice customization, SEO tools, and team collaboration features, Jasper helps businesses produce consistent on-brand content at scale.",
  descriptionLongZh: "Jasper是一款面向营销团队和内容创作者的AI写作助手。专注于创建品牌对齐的文案、博客文章和社交媒体内容。",
  advantages: [
            "Brand voice customization",
            "SEO-optimized content",
            "Team collaboration",
            "Template library"
          ],
  advantagesZh: [
            "品牌语气自定义",
            "SEO优化内容",
            "团队协作",
            "模板库"
          ],
  useCases: [
            "Marketing copy and ads",
            "Blog post writing",
            "Social media content",
            "Email campaigns",
            "Product descriptions"
          ],
  useCasesZh: [
            "营销文案",
            "博客文章写作",
            "社交媒体内容",
            "邮件营销"
          ],
  targetAudience: "Marketing teams and content creators who need consistent brand-aligned copy at scale.",
  targetAudienceZh: "需要规模化创建一致品牌文案的营销团队和内容创作者。",
  pricingTiers: [
      {
        tier: "Creator",
          tierZh: "创作者版",
        price: "$49/mo",
        features: [
          "1 user",
          "50+ templates",
          "SEO mode"
        ],
        featuresZh: [
          "1个用户",
          "50多个模板",
          "SEO模式",
        ],
      },
      {
        tier: "Pro",
          tierZh: "专业版",
        price: "$69/mo",
        features: [
          "3 users",
          "Brand voice",
          "Custom templates"
        ],
        featuresZh: [
          "3个用户",
          "品牌语气",
          "自定义模板",
        ],
      }
    ],  
  extensions: [
        {
          name: "Jasper Chrome Extension",
          description: "Write anywhere on the web",
          descriptionZh: "在网页任意位置写作",
        }
      ],  
  scene: "marketing",
  affiliateUrl: "https://www.jasper.ai/affiliate",
  hasAffiliate: true,
  skills: [
            "copywriting",
            "content marketing",
            "SEO writing",
            "brand voice",
            "email marketing"
          ],  
  pros: [
            "Brand voice consistency",
            "SEO integration",
            "Team features",
            "Good template variety"
          ],
  prosZh: [
            "品牌语气一致性",
            "SEO集成",
            "团队功能",
            "模板种类丰富"
          ],
  cons: [
            "Expensive for individuals",
            "Output can feel templated",
            "Better alternatives for free",
            "Overkill for simple tasks"
          ],
  consZh: [
            "个人用户价格较高",
            "输出可能显得模板化",
            "有更好的免费替代方案",
            "简单任务过于复杂"
          ],
  },

  {
    id: "copy-ai",
    name: "Copy.ai",
    description: "AI copywriting tool for sales, marketing, and social media content.",
  descriptionZh: "AI文案写作工具，用于销售、营销和社交媒体内容。",
    category: "writing",
    tags: ["copywriting", "sales", "marketing", "social-media"],
    difficulty: "beginner",
    url: "https://www.copy.ai",
    rating: r(4.2),
    pricing: "Free tier / from $36/mo",
    useCase: "Copy.ai generates sales copy, email campaigns, and social media posts quickly. Ideal for marketers who need批量 content fast without sacrificing quality.",
    icon: "\u{1F4DD}",
  company: "Copy.ai",
  companyZh: "Copy.ai",
  founded: "2020",  headquarters: "San Francisco, CA",  
  descriptionLong: "Copy.ai is an AI copywriting tool for sales, marketing, and social media content. It generates sales copy, email campaigns, blog content, and social media posts quickly. With workflow automation features and a user-friendly interface, it helps marketers produce bulk content efficiently without sacrificing quality.",
  descriptionLongZh: "Copy.ai是一款面向销售、营销和社交媒体的AI文案写作工具。可快速生成销售文案、邮件营销、博客内容和社交媒体帖子。",
  advantages: [
            "Quick content generation",
            "Workflow automation",
            "Multi-platform support",
            "User-friendly interface"
          ],
  advantagesZh: [
            "快速生成",
            "工作流自动化",
            "多平台支持",
            "用户友好界面"
          ],
  useCases: [
            "Sales copy generation",
            "Email campaign writing",
            "Social media posts",
            "Blog content",
            "Product descriptions"
          ],
  useCasesZh: [
            "销售文案生成",
            "邮件营销",
            "社交媒体帖子",
            "博客内容"
          ],
  targetAudience: "Marketers and sales professionals who need fast content generation for multiple platforms.",
  targetAudienceZh: "需要为多个平台快速生成内容的营销和销售专业人士。",
  pricingTiers: [
      {
        tier: "Free",
          tierZh: "免费版",
        price: "$0",
        features: [
          "2000 words/month",
          "1 user",
          "Basic templates"
        ],
        featuresZh: [
          "每月2000词",
          "1个用户",
          "基础模板",
        ],
      },
      {
        tier: "Pro",
          tierZh: "专业版",
        price: "$36/mo",
        features: [
          "Unlimited words",
          "5 users",
          "Workflows"
        ],
        featuresZh: [
          "无限字数",
          "5个用户",
          "工作流自动化",
        ],
      }
    ],  
  extensions: [
        {
          name: "Copy.ai Chrome Extension",
          description: "Write anywhere",
          descriptionZh: "随处写作",
        }
      ],  
  scene: "marketing",
  skills: [
            "copywriting",
            "email marketing",
            "social media",
            "content automation",
            "sales writing"
          ],  
  pros: [
            "Fast content generation",
            "Workflow automations",
            "Good free tier",
            "Easy to use"
          ],
  prosZh: [
            "快速生成",
            "工作流自动化",
            "良好的免费版本",
            "易于使用"
          ],
  cons: [
            "Output needs editing",
            "Less brand voice control",
            "Generic templates",
            "Limited long-form"
          ],
  consZh: [
            "输出需要编辑",
            "对输出控制较少",
            "模板较为通用",
            "长文生成能力有限"
          ],
  },

  {
    id: "notion-ai",
    name: "Notion AI",
    description: "AI-powered writing and knowledge management integrated into Notion workspaces.",
  descriptionZh: "AI驱动的写作和知识管理，集成在Notion工作区中。",
    category: "productivity",
    tags: ["notes", "knowledge", "writing", "organization"],
    difficulty: "beginner",
    url: "https://www.notion.so/product/ai",
    rating: r(4.5),
    pricing: "$10/mo add-on to Notion plan",
    useCase: "Notion AI assists with drafting, summarizing, and editing inside your Notion workspace. Use it for meeting notes, project docs, and knowledge base articles.",
    icon: "\u{1F4CB}",
  company: "Notion Labs",
  companyZh: "Notion Labs",
  founded: "2013",  headquarters: "San Francisco, CA",  
  descriptionLong: "Notion AI brings AI-powered writing and knowledge management directly into your Notion workspace. It assists with drafting, summarizing, editing, and brainstorming inside your existing docs and databases. Seamlessly integrated, it can translate, fix spelling, generate action items from meeting notes, and help organize your knowledge base without switching tools.",
  descriptionLongZh: "Notion AI将AI驱动的写作和知识管理带入Notion工作区。辅助起草、总结、编辑，无需切换工具即可完成多项任务。",
  advantages: [
            "Integrated into Notion workspace",
            "AI writing and editing",
            "Knowledge management",
            "Meeting notes automation"
          ],
  advantagesZh: [
            "集成在Notion中",
            "AI写作和编辑",
            "知识管理",
            "会议记录自动化"
          ],
  useCases: [
            "Meeting notes summarization",
            "Doc drafting and editing",
            "Knowledge base Q&A",
            "Project planning",
            "Content translation"
          ],
  useCasesZh: [
            "会议记录总结",
            "文档起草和编辑",
            "知识库问答",
            "项目规划"
          ],
  targetAudience: "Existing Notion users who want AI assistance integrated into their workspace without switching tools.",
  targetAudienceZh: "希望在不切换工具的情况下将AI助手集成到工作区的现有Notion用户。",
  pricingTiers: [
      {
        tier: "Add-on",
          tierZh: "附加功能版",
        price: "$10/mo",
        features: [
          "Per member",
          "AI writing",
          "Auto-fill databases"
        ],
        featuresZh: [
          "按成员计费",
          "AI写作",
          "自动填充数据库",
        ],
      }
    ],  
  extensions: [
        {
          name: "Notion AI Built-in",
          description: "Available in all Notion workspaces",
          descriptionZh: "所有Notion工作区可用",
        }
      ],  
  scene: "office-productivity",
  affiliateUrl: "https://www.notion.so/product/ai?ref=affiliate",
  hasAffiliate: true,
  skills: [
            "knowledge management",
            "note-taking",
            "project management",
            "writing",
            "documentation"
          ],  
  pros: [
            "Deep Notion integration",
            "Useful for summarization",
            "Q&A over knowledge base",
            "Non-disruptive workflow"
          ],
  prosZh: [
            "深度Notion集成",
            "总结功能实用",
            "知识库问答",
            "不干扰现有工作流"
          ],
  cons: [
            "Requires Notion subscription",
            "Add-on cost",
            "Less powerful than dedicated AI",
            "Notion dependency"
          ],
  consZh: [
            "需要Notion订阅",
            "附加功能需付费",
            "不如专用AI工具强大",
            "依赖Notion平台"
          ],
  },

  {
    id: "grammarly",
    name: "Grammarly",
    description: "AI writing assistant for grammar checking, style improvement, and tone adjustment.",
  descriptionZh: "AI写作助手，用于语法检查、风格改进和语气调整。",
    category: "writing",
    tags: ["grammar", "writing", "editing", "style"],
    difficulty: "beginner",
    url: "https://www.grammarly.com",
    rating: r(4.6),
    pricing: "Free / $12/mo Premium",
    useCase: "Grammarly checks grammar, clarity, engagement, and delivery across emails, documents, and web forms. Essential for professional and error-free writing.",
    icon: "\u{2705}",
  company: "Grammarly",
  companyZh: "Grammarly",
  founded: "2009",  headquarters: "San Francisco, CA",  
  descriptionLong: "Grammarly is an AI writing assistant for grammar checking, style improvement, and tone adjustment. It works across emails, documents, and web forms with features including real-time grammar correction, plagiarism detection, tone detection, and style suggestions. Used by millions for professional and error-free writing across all platforms.",
  descriptionLongZh: "Grammarly是一款AI写作助手，用于语法检查、风格改进和语气调整。可跨邮件、文档和网页表单使用，提供实时语法纠正和查重功能。",
  advantages: [
            "Real-time grammar checking everywhere",
            "Tone detection and adjustment",
            "Plagiarism detection",
            "Style and clarity suggestions"
          ],
  advantagesZh: [
            "实时语法检查",
            "语气检测",
            "查重检测",
            "风格建议"
          ],
  useCases: [
            "Professional email writing",
            "Academic essay editing",
            "Business document polish",
            "Social media posts",
            "Creative writing refinement"
          ],
  useCasesZh: [
            "专业邮件写作",
            "学术论文编辑",
            "商业文档润色",
            "社交媒体帖子"
          ],
  targetAudience: "Anyone who writes professionally -- students, professionals, writers, and non-native speakers wanting error-free writing.",
  targetAudienceZh: "任何需要专业写作的人——学生、专业人士、写作者和非母语者。",
  pricingTiers: [
      {
        tier: "Free",
          tierZh: "免费版",
        price: "$0",
        features: [
          "Basic grammar",
          "Spelling",
          "Punctuation"
        ],
        featuresZh: [
          "基础语法检查",
          "拼写检查",
          "标点检查",
        ],
      },
      {
        tier: "Premium",
          tierZh: "高级版",
        price: "$12/mo",
        features: [
          "Full grammar",
          "Tone detection",
          "Plagiarism"
        ],
        featuresZh: [
          "完整语法检查",
          "语气检测",
          "查重功能",
        ],
      },
      {
        tier: "Business",
          tierZh: "商务版",
        price: "$15/user/mo",
        features: [
          "All Premium",
          "Style guide",
          "Analytics"
        ],
        featuresZh: [
          "所有高级版功能",
          "风格指南",
          "数据分析",
        ],
      }
    ],  
  extensions: [
        {
          name: "Grammarly for Chrome",
          description: "Browser extension for all sites",
          descriptionZh: "支持所有网站的浏览器扩展",
        },
        {
          name: "Grammarly Desktop",
          description: "Windows and Mac app",
          descriptionZh: "Windows和Mac应用",
        }
      ],  
  scene: "content-creation",
  skills: [
            "grammar",
            "writing",
            "editing",
            "proofreading",
            "style"
          ],  
  pros: [
            "Works everywhere via extension",
            "Excellent grammar detection",
            "Tone analysis helpful",
            "Generous free tier"
          ],
  prosZh: [
            "通过扩展随处可用",
            "语法检测出色",
            "语气分析实用",
            "良好的免费版本"
          ],
  cons: [
            "Premium expensive",
            "Privacy concerns with content",
            "Over-zealous suggestions",
            "Can slow down browsers"
          ],
  consZh: [
            "高级版价格较高",
            "隐私问题",
            "建议有时过于激进",
            "可能拖慢浏览器"
          ],
  },

  {
    id: "cursor",
    name: "Cursor",
    description: "AI-first code editor built on VS Code with deep AI integration for faster development.",
  descriptionZh: "基于VS Code的AI优先代码编辑器，深度集成AI以加速开发。",
    category: "coding",
    tags: ["ide", "code-generation", "vs-code", "productivity"],
    difficulty: "intermediate",
    url: "https://cursor.sh",
    rating: r(4.7),
    pricing: "Free / $20/mo Pro",
    useCase: "Cursor is an AI-native code editor that understands your codebase. It offers autocomplete, inline editing, and chat-based code generation.",
    icon: "\u{1F4BB}",
  company: "Anysphere",
  companyZh: "Anysphere",
  founded: "2022",  headquarters: "San Francisco, CA",  
  descriptionLong: "Cursor is an AI-first code editor built on VS Code with deep AI integration. It offers AI-powered autocomplete, inline editing, multi-file editing, and chat-based code generation that understands your entire codebase. With features like AI context awareness and agent mode, Cursor dramatically accelerates development speed.",
  descriptionLongZh: "Cursor是一个基于VS Code的AI优先代码编辑器。提供AI驱动的自动补全、内联编辑和基于聊天的代码生成，能理解你的整个代码库。",
  advantages: [
            "VS Code compatible",
            "AI understands full codebase",
            "Multi-file editing",
            "Agent mode for complex tasks"
          ],
  advantagesZh: [
            "兼容VS Code",
            "AI理解整个代码库",
            "多文件编辑",
            "代理模式"
          ],
  useCases: [
            "Full-stack web development",
            "Code refactoring across files",
            "Bug fixing with AI",
            "Learning new codebases",
            "Rapid prototyping"
          ],
  useCasesZh: [
            "全栈Web开发",
            "跨文件代码重构",
            "AI辅助Bug修复",
            "学xi新的代码库"
          ],
  targetAudience: "Developers who want AI deeply integrated into their code editor for faster development.",
  targetAudienceZh: "希望AI深度集成到代码编辑器中以加速开发的开发者。",
  pricingTiers: [
      {
        tier: "Free",
          tierZh: "免费版",
        price: "$0",
        features: [
          "200 AI completions",
          "Basic chat"
        ],
        featuresZh: ["200次AI补全", "基础聊天"],
      },
      {
        tier: "Pro",
          tierZh: "专业版",
        price: "$20/mo",
        features: [
          "Unlimited AI",
          "Agent mode",
          "Multi-file edit"
        ],
        featuresZh: [
          "AI无限使用",
          "代理模式",
          "多文件编辑",
        ],
      }
    ],  
  extensions: [
        {
          name: "Cursor Editor",
          description: "Standalone VS Code fork with AI",
          descriptionZh: "集成AI的独立VS Code分支",
        }
      ],  
  scene: "development",
  skills: [
            "software development",
            "code refactoring",
            "debugging",
            "full-stack",
            "pair programming"
          ],  
  pros: [
            "Deep VS Code integration",
            "Codebase-aware AI",
            "Excellent autocomplete",
            "Agent mode powerful"
          ],
  prosZh: [
            "深度VS Code集成",
            "AI感知整个代码库",
            "出色的自动补全",
            "代理模式 potente"
          ],
  cons: [
            "Requires subscription for full features",
            "Can be resource heavy",
            "Still maturing",
            "Pro plan expensive"
          ],
  consZh: [
            "完整功能需要订阅",
            "资源占用较高",
            "仍在不断完善中",
            "Pro版价格较高"
          ],
  },

  {
    id: "github-copilot",
    name: "GitHub Copilot",
    description: "AI pair programmer from GitHub that suggests code in real-time across popular IDEs.",
  descriptionZh: "GitHub的AI配对编程器，在主流IDE中实时建议代码。",
    category: "coding",
    tags: ["code-generation", "ide", "github", "pair-programming"],
    difficulty: "intermediate",
    url: "https://github.com/features/copilot",
    rating: r(4.6),
    pricing: "Free / $10/mo Individual",
    useCase: "Copilot provides real-time code suggestions as you type. It integrates with VS Code, JetBrains, and Neovim for seamless AI-assisted development.",
    icon: "\u{1F91D}",
  company: "GitHub (Microsoft)",
  companyZh: "GitHub（微软）",
  founded: "2008",  headquarters: "San Francisco, CA",  
  descriptionLong: "GitHub Copilot is an AI pair programmer from GitHub that suggests code in real-time across popular IDEs including VS Code, JetBrains, and Neovim. Powered by OpenAI's Codex models, it offers context-aware code completions, chat-based coding help, and pull request summaries. Copilot has become the standard for AI-assisted development.",
  descriptionLongZh: "GitHub Copilot是一个AI配对编程器，在VS Code、JetBrains和Neovim等主流IDE中实时建议代码。由OpenAI的Codex模型驱动。",
  advantages: [
            "Integrated in major IDEs",
            "Context-aware suggestions",
            "Chat-based coding help",
            "PR summary generation"
          ],
  advantagesZh: [
            "集成在主流IDE中",
            "上下文感知的建议",
            "基于聊天的帮助",
            "PR摘要生成"
          ],
  useCases: [
            "Real-time code completion",
            "Chat-based code generation",
            "Pull request descriptions",
            "Code explanation",
            "Test generation"
          ],
  useCasesZh: [
            "实时代码补全",
            "基于聊天的代码生成",
            "拉取请求描述",
            "代码解释"
          ],
  targetAudience: "Developers using VS Code, JetBrains, or Neovim who want AI code suggestions in their existing IDE.",
  targetAudienceZh: "使用VS Code、JetBrains或Neovim并希望在现有IDE中获得AI代码建议的开发者。",
  pricingTiers: [
      {
        tier: "Free",
          tierZh: "免费版",
        price: "$0",
        features: [
          "2000 completions/month",
          "Code chat"
        ],
        featuresZh: ["每月2000次补全", "代码聊天"],
      },
      {
        tier: "Individual",
          tierZh: "个人版",
        price: "$10/mo",
        features: [
          "Unlimited",
          "Multi-file",
          "PR summaries"
        ],
        featuresZh: [
          "无限使用",
          "多文件支持",
          "PR摘要生成",
        ],
      }
    ],  
  extensions: [
        {
          name: "Copilot for VS Code",
          description: "VS Code extension",
          descriptionZh: "VS Code扩展",
        },
        {
          name: "Copilot for JetBrains",
          description: "JetBrains IDE plugin",
          descriptionZh: "JetBrains IDE插件",
        }
      ],  
  scene: "development",
  skills: [
            "software development",
            "code completion",
            "pair programming",
            "debugging",
            "code review"
          ],  
  pros: [
            "Works in existing IDEs",
            "Context-aware completions",
            "Good for boilerplate",
            "Free for students"
          ],
  prosZh: [
            "在现有IDE中工作",
            "上下文感知补全",
            "适合样板代码",
            "学生免费"
          ],
  cons: [
            "Less powerful than Cursor agent",
            "Can suggest insecure code",
            "Limited multi-file context",
            "Pro plan needed"
          ],
  consZh: [
            "不如Cursor代理模式强大",
            "可能建议不安全代码",
            "多文件上下文有限",
            "需要Pro计划"
          ],
  },

  {
    id: "replit-ai",
    name: "Replit AI",
    description: "Browser-based IDE with built-in AI agent that can build and deploy apps from prompts.",
  descriptionZh: "基于浏览器的IDE，内置AI代理，可从提示构建和部署应用。",
    category: "coding",
    tags: ["ide", "deploy", "no-setup", "agent"],
    difficulty: "beginner",
    url: "https://replit.com",
    rating: r(4.3),
    pricing: "Free / $20/mo Pro",
    useCase: "Replit AI can generate entire applications from a prompt, run them in the browser, and deploy them. Great for prototyping and learning to code.",
    icon: "\u{1F527}",
  company: "Replit",
  companyZh: "Replit",
  founded: "2016",  headquarters: "San Francisco, CA",  
  descriptionLong: "Replit AI is a browser-based IDE with a built-in AI agent that can build and deploy applications from natural language prompts. It requires zero setup -- just describe what you want and the AI agent creates, runs, and deploys the app. Perfect for beginners learning to code, rapid prototyping, and building MVPs without local development setup.",
  descriptionLongZh: "Replit AI是一个基于浏览器的IDE，内置AI代理，可根据自然语言提示构建和部署应用。零设置，适合初学者和快速原型开发。",
  advantages: [
            "Zero setup browser IDE",
            "AI builds entire apps",
            "Instant deployment",
            "Collaboration built-in"
          ],
  advantagesZh: [
            "零设置浏览器IDE",
            "AI构建完整应用",
            "即时部署",
            "内置协作功能"
          ],
  useCases: [
            "Rapid app prototyping",
            "Learning to code interactively",
            "Building MVPs quickly",
            "Collaborative development",
            "Deploying side projects"
          ],
  useCasesZh: [
            "快速应用原型开发",
            "交互式学编程",
            "快速构建MVP",
            "协作开发"
          ],
  targetAudience: "Beginners learning to code and developers who want rapid prototyping without local setup.",
  targetAudienceZh: "学习编程的初学者和希望无需本地设置即可快速原型开发的开发者。",
  pricingTiers: [
      {
        tier: "Free",
          tierZh: "免费版",
        price: "$0",
        features: [
          "Limited compute",
          "AI agent access",
          "Public projects"
        ],
        featuresZh: [
          "有限计算资源",
          "AI代理访问",
          "公开项目",
        ],
      },
      {
        tier: "Pro",
          tierZh: "专业版",
        price: "$20/mo",
        features: [
          "Unlimited compute",
          "Private projects",
          "Faster AI"
        ],
        featuresZh: [
          "无限计算资源",
          "私有项目",
          "更快的AI响应",
        ],
      }
    ],  
  extensions: [
        {
          name: "Replit Browser",
          description: "Web-based IDE and deployment",
          descriptionZh: "基于网页的IDE和部署平台",
        }
      ],  
  scene: "development",
  skills: [
            "full-stack",
            "rapid prototyping",
            "web development",
            "deployment",
            "collaborative coding"
          ],  
  pros: [
            "Zero setup required",
            "AI builds full apps",
            "Built-in deployment",
            "Great for learning"
          ],
  prosZh: [
            "零设置，无需配置",
            "AI构建完整应用",
            "内置部署功能",
            "非常适合学习"
          ],
  cons: [
            "Limited for complex apps",
            "Free tier computing limits",
            "Requires internet",
            "Less control than local"
          ],
  consZh: [
            "复杂应用能力有限",
            "计算资源限制",
            "需要联网",
            "对输出控制较少 que local"
          ],
  },

  {
    id: "gamma",
    name: "Gamma",
    description: "AI-powered presentation tool that creates slides, documents, and web pages from text.",
  descriptionZh: "AI驱动的演示工具，可从文本创建幻灯片、文档和网页。",
    category: "productivity",
    tags: ["presentation", "slides", "design", "documents"],
    difficulty: "beginner",
    url: "https://gamma.app",
    rating: r(4.5),
    pricing: "Free tier / from $10/mo",
    useCase: "Gamma generates beautiful presentations, documents, and web pages from a simple text prompt. Perfect for students, educators, and business professionals.",
    icon: "\u{1F4CA}",
  company: "Gamma",
  companyZh: "Gamma",
  founded: "2020",  headquarters: "San Francisco, CA",  
  descriptionLong: "Gamma is an AI-powered presentation tool that creates slides, documents, and web pages from text prompts. It generates beautifully designed content with smart layouts, images, and consistent themes automatically. Unlike traditional presentation tools, Gamma handles the design so users focus on content. Perfect for students, educators, and professionals.",
  descriptionLongZh: "Gamma是一个AI驱动的演示工具，可从文本提示创建幻灯片、文档和网页。自动生成设计精美的内容，用户只需专注于内容。",
  advantages: [
            "AI generates complete presentations",
            "Smart auto-layout",
            "Web pages and docs too",
            "Beautiful design templates"
          ],
  advantagesZh: [
            "AI生成完整演示文稿",
            "智能自动布局",
            "也支持网页和文档",
            "精美的设计模板"
          ],
  useCases: [
            "Business presentations",
            "Educational slide decks",
            "Project proposals",
            "Web page creation",
            "Pitch decks"
          ],
  useCasesZh: [
            "商业演示",
            "教育幻灯片",
            "项目提案",
            "网页创建"
          ],
  targetAudience: "Students, educators, and professionals who want AI-generated presentations and documents quickly.",
  targetAudienceZh: "希望快速获得AI生成演示文稿和文档的学生、教育工作者和专业人士。",
  pricingTiers: [
      {
        tier: "Free",
          tierZh: "免费版",
        price: "$0",
        features: [
          "Limited AI credits",
          "Basic templates"
        ],
        featuresZh: ["有限AI额度", "基础模板"],
      },
      {
        tier: "Pro",
          tierZh: "专业版",
        price: "$10/mo",
        features: [
          "Unlimited AI",
          "All templates",
          "Export options"
        ],
        featuresZh: [
          "AI无限使用",
          "所有模板",
          "导出选项",
        ],
      }
    ],  
  extensions: [
        {
          name: "Gamma Web App",
          description: "Browser-based creation tool",
          descriptionZh: "基于浏览器的创作工具",
        }
      ],  
  scene: "office-productivity",
  skills: [
            "presentation design",
            "content creation",
            "visual storytelling",
            "document design"
          ],  
  pros: [
            "Fast presentation creation",
            "Beautiful auto-design",
            "Multi-format output",
            "Easy to use"
          ],
  prosZh: [
            "快速创建",
            "自动设计精美",
            "多格式输出",
            "易于使用"
          ],
  cons: [
            "Limited customization",
            "Less control than PowerPoint",
            "AI designs not always perfect",
            "Subscription needed"
          ],
  consZh: [
            "自定义有限",
            "对输出控制较少 que PowerPoint",
            "AI设计不一定完美",
            "需要订阅"
          ],
  },

  {
    id: "beautiful-ai",
    name: "Beautiful.ai",
    description: "AI presentation tool with smart templates that auto-layout your content beautifully.",
  descriptionZh: "AI演示工具，智能模板自动排版你的内容。",
    category: "productivity",
    tags: ["presentation", "design", "templates", "business"],
    difficulty: "beginner",
    url: "https://www.beautiful.ai",
    rating: r(4.2),
    pricing: "from $12/mo",
    useCase: "Beautiful.ai's smart slides auto-arrange your content into professional layouts. Best for business presentations where design consistency matters.",
    icon: "✨",
  company: "Beautiful.ai",
  companyZh: "Beautiful.ai",
  founded: "2015",  headquarters: "San Francisco, CA",  
  descriptionLong: "Beautiful.ai is an AI presentation tool with smart templates that auto-layout your content. As you add content, the AI automatically arranges it into professional designs with consistent spacing, alignment, and styling. It enforces design rules so presentations always look polished without manual formatting. Best for business presentations needing design consistency.",
  descriptionLongZh: "Beautiful.ai是一款AI演示工具，智能模板自动将你的内容排版成专业设计。AI自动处理间距、对齐和样式一致性。",
  advantages: [
            "Smart auto-layout technology",
            "Design consistency enforcement",
            "Professional templates",
            "Team collaboration"
          ],
  advantagesZh: [
            "智能自动排版",
            "设计一致性",
            "专业模板",
            "团队协作"
          ],
  useCases: [
            "Business presentations",
            "Sales decks",
            "Investor pitches",
            "Team reports",
            "Brand presentations"
          ],
  useCasesZh: [
            "商业演示",
            "销售演示",
            "投资人路演",
            "团队报告"
          ],
  targetAudience: "Business professionals who need consistent, professional presentations without design skills.",
  targetAudienceZh: "需要一致专业演示文稿但无设计技能的商业专业人士。",
  pricingTiers: [
      {
        tier: "Pro",
          tierZh: "专业版",
        price: "$12/mo",
        features: [
          "Unlimited presentations",
          "All templates",
          "Export"
        ],
        featuresZh: [
          "无限演示文稿",
          "所有模板",
          "导出功能",
        ],
      },
      {
        tier: "Team",
          tierZh: "团队版",
        price: "$40/user/mo",
        features: [
          "All Pro",
          "Team library",
          "Brand control"
        ],
        featuresZh: [
          "所有专业版功能",
          "团队资源库",
          "品牌控制",
        ],
      }
    ],  
  extensions: [
        {
          name: "Beautiful.ai Web",
          description: "Browser-based presentation tool",
          descriptionZh: "基于浏览器的演示文稿工具",
        }
      ],  
  scene: "office-productivity",
  skills: [
            "presentation design",
            "business communication",
            "visual storytelling",
            "brand consistency"
          ],  
  pros: [
            "Auto-layout saves time",
            "Design consistency",
            "Professional output",
            "Good for teams"
          ],
  prosZh: [
            "智能自动布局",
            "设计一致性",
            "专业输出",
            "适合团队使用"
          ],
  cons: [
            "Less creative freedom",
            "Expensive for individuals",
            "Limited templates",
            "AI can be restrictive"
          ],
  consZh: [
            "创意自由度较低",
            "个人用户价格较高",
            "模板有限",
            "AI限制较多"
          ],
  },

  {
    id: "canva-ai",
    name: "Canva AI",
    description: "All-in-one design platform with AI features for generating images, copy, and layouts.",
  descriptionZh: "一体化设计平台，具有AI功能，可生成图像、文案和布局。",
    category: "productivity",
    tags: ["design", "templates", "social-media", "all-in-one"],
    difficulty: "beginner",
    url: "https://www.canva.com",
    rating: r(4.7),
    pricing: "Free / $12.99/mo Pro",
    useCase: "Canva AI includes Magic Design, Magic Write文案生成, and AI image generation. Ideal for non-designers creating social media graphics, flyers, and presentations.",
    icon: "\u{1F3AF}",
  company: "Canva",
  companyZh: "Canva（可画）",
  founded: "2013",  headquarters: "Sydney, Australia",  
  descriptionLong: "Canva AI brings AI-powered design features into the popular Canva platform. Features include Magic Design (generates complete templates from descriptions), Magic Write文案生成 (AI copy generation), AI image generation, background removal, and smart resize. Canva AI makes professional design accessible to non-designers with an all-in-one platform for social media, presentations, and print.",
  descriptionLongZh: "Canva AI将AI驱动的设计功能带入Canva平台。包含Magic Design、Magic Write文案生成、AI图像生成、背景移除和智能调整大小。",
  advantages: [
            "All-in-one design platform",
            "Magic Design from text",
            "Magic Write文案生成 copy generation",
            "AI image generation",
            "Background removal"
          ],
  advantagesZh: [
            "一体化设计平台",
            "Magic Design从文本生成",
            "Magic Write文案生成",
            "AI图像生成",
            "视频背景移除"
          ],
  useCases: [
            "Social media graphics",
            "Presentation design",
            "Marketing materials",
            "Video creation",
            "Brand kits"
          ],
  useCasesZh: [
            "社交媒体图像",
            "演示文稿设计",
            "营销物料",
            "视频创作"
          ],
  targetAudience: "Non-designers and social media managers who want easy professional design with AI assistance.",
  targetAudienceZh: "希望借助AI轻松实现专业设计的非设计师和社交媒体管理者。",
  pricingTiers: [
      {
        tier: "Free",
          tierZh: "免费版",
        price: "$0",
        features: [
          "Limited AI",
          "250K+ templates",
          "1GB storage"
        ],
        featuresZh: [
          "AI功能有限",
          "超过25万个模板",
          "1GB存储空间",
        ],
      },
      {
        tier: "Pro",
          tierZh: "专业版",
        price: "$12.99/mo",
        features: [
          "Unlimited AI",
          "100M+ assets",
          "Brand kits"
        ],
        featuresZh: [
          "AI无限使用",
          "超过1亿素材",
          "品牌工具包",
        ],
      }
    ],  
  extensions: [
        {
          name: "Canva Web App",
          description: "Full browser-based design platform",
          descriptionZh: "完整的基于浏览器的设计平台",
        },
        {
          name: "Canva Desktop",
          description: "Windows and Mac app",
          descriptionZh: "Windows和Mac应用",
        }
      ],  
  scene: "design-video",
  skills: [
            "graphic design",
            "social media",
            "brand design",
            "content creation",
            "visual marketing"
          ],  
  pros: [
            "All-in-one design",
            "Magic Design is powerful",
            "Huge template library",
            "Team collaboration"
          ],
  prosZh: [
            "一体化设计",
            "Magic Design功能强大",
            "海量模板库",
            "团队协作"
          ],
  cons: [
            "Pro subscription needed for AI",
            "Can feel overwhelming",
            "Export limited without Pro",
            "Brand control limited on Free"
          ],
  consZh: [
            "AI功能需要Pro订阅",
            "功能繁多可能让人不知所措",
            "导出功能在免费版受限",
            "免费版品牌控制有限"
          ],
  },

  {
    id: "elevenlabs",
    name: "ElevenLabs",
    description: "Industry-leading AI voice synthesis with realistic, expressive speech generation.",
  descriptionZh: "业界领先的AI语音合成，生成逼真且富有表现力的语音。",
    category: "audio",
    tags: ["voice", "tts", "audiobooks", "realistic"],
    difficulty: "beginner",
    url: "https://elevenlabs.io",
    rating: r(4.7),
    pricing: "Free tier / from $5/mo",
    useCase: "ElevenLabs generates ultra-realistic speech from text, supports voice cloning, and multi-language narration. Perfect for audiobooks, videos, and voiceovers.",
    icon: "\u{1F399}️",
  company: "ElevenLabs",
  companyZh: "ElevenLabs",
  founded: "2022",  headquarters: "New York, NY",  
  descriptionLong: "ElevenLabs is the industry-leading AI voice synthesis platform known for ultra-realistic, expressive speech generation. It offers text-to-speech, voice cloning, voice library, and multi-language narration in 29+ languages. With features like voice design, emotion control, and API access, ElevenLabs is used for audiobooks, videos, voiceovers, and content creation.",
  descriptionLongZh: "ElevenLabs是业界领先的AI语音合成平台，以超逼真、富有表现力的语音生成闻名。提供文本转语音和语音克隆功能。",
  advantages: [
            "Ultra-realistic voice quality",
            "Voice cloning technology",
            "29+ language support",
            "Emotion and tone control"
          ],
  advantagesZh: [
            "超逼真的语音质量",
            "语音克隆",
            "支持29+种语言",
            "情感和语气控制"
          ],
  useCases: [
            "Audiobook narration",
            "Video voiceovers",
            "Content creator voice",
            "Language learning audio",
            "Accessibility solutions"
          ],
  useCasesZh: [
            "有声书旁白",
            "视频配音",
            "内容创作者语音",
            "语言学xi音频"
          ],
  targetAudience: "Content creators, publishers, and developers needing realistic AI voice generation for audio content.",
  targetAudienceZh: "需要为音频内容生成逼真AI语音的内容创作者、出版商和开发者。",
  pricingTiers: [
      {
        tier: "Free",
          tierZh: "免费版",
        price: "$0",
        features: [
          "10K chars/month",
          "Standard voices"
        ],
        featuresZh: ["每月1万字符", "标准语音"],
      },
      {
        tier: "Starter",
          tierZh: "入门版",
        price: "$5/mo",
        features: [
          "30K chars/month",
          "Voice cloning"
        ],
        featuresZh: ["每月3万字符", "语音克隆"],
      },
      {
        tier: "Creator",
          tierZh: "创作者版",
        price: "$22/mo",
        features: [
          "100K chars/month",
          "API access"
        ],
        featuresZh: ["每月10万字符", "API访问权限"],
      }
    ],  
  extensions: [
        {
          name: "ElevenLabs Web",
          description: "Browser-based TTS platform",
          descriptionZh: "基于浏览器的语音合成平台",
        }
      ],  
  scene: "content-creation",
  skills: [
            "voice synthesis",
            "audio production",
            "voice cloning",
            "TTS",
            "audiobook production"
          ],  
  pros: [
            "Most realistic AI voices",
            "Excellent voice cloning",
            "Multi-language support",
            "Good API"
          ],
  prosZh: [
            "最逼真的AI语音",
            "出色的语音克隆",
            "多语言支持",
            "良好的API"
          ],
  cons: [
            "Expensive for high usage",
            "Voice cloning ethical concerns",
            "Free tier limited",
            "Long processing for long text"
          ],
  consZh: [
            "高使用量费用较高",
            "语音克隆伦理问题",
            "免费版功能有限",
            "长文本处理较慢"
          ],
  },

  {
    id: "suno",
    name: "Suno",
    description: "AI music generation that creates original songs with lyrics from text prompts.",
  descriptionZh: "AI音乐生成，从文本提示创建带歌词的原创歌曲。",
    category: "audio",
    tags: ["music", "song", "creative", "audio"],
    difficulty: "beginner",
    url: "https://suno.com",
    rating: r(4.5),
    pricing: "Free tier / from $10/mo",
    useCase: "Suno creates original songs with vocals and instruments from text descriptions. Great for content creators, musicians, and anyone exploring AI music.",
    icon: "\u{1F3B5}",
  company: "Suno",
  companyZh: "Suno",
  founded: "2022",  headquarters: "Cambridge, MA",  
  descriptionLong: "Suno is an AI music generation platform that creates original songs with vocals and instruments from text prompts. It can generate complete songs in various genres including pop, rock, hip-hop, electronic, and classical. Users provide lyrics or let Suno generate them, choose a style, and the AI produces a complete musical composition. Great for content creators and music exploration.",
  descriptionLongZh: "Suno是一个AI音乐生成平台，从文本提示创建带有歌声和乐器的原创歌曲。支持流行、摇滚、嘻哈等多种风格。",
  advantages: [
            "Complete song generation",
            "Multiple genres supported",
            "Lyrics generation included",
            "Fast creation process"
          ],
  advantagesZh: [
            "完整歌曲生成",
            "多种音乐风格",
            "包含歌词生成",
            "创作速度快"
          ],
  useCases: [
            "Background music creation",
            "Content creator intro songs",
            "Music exploration",
            "Creative inspiration",
            "Personal enjoyment"
          ],
  useCasesZh: [
            "背景音乐创作",
            "内容创作者的开场曲",
            "音乐探索",
            "创意灵感"
          ],
  targetAudience: "Content creators, musicians exploring AI, and anyone wanting original AI-generated music.",
  targetAudienceZh: "内容创作者、探索AI的音乐人以及任何想要AI生成原创音乐的人。",
  pricingTiers: [
      {
        tier: "Free",
          tierZh: "免费版",
        price: "$0",
        features: [
          "5 songs/day",
          "Basic quality"
        ],
        featuresZh: ["每天5首", "基础质量"],
      },
      {
        tier: "Pro",
          tierZh: "专业版",
        price: "$10/mo",
        features: [
          "500 songs/month",
          "Full quality",
          "Commercial use"
        ],
        featuresZh: [
          "每月500首",
          "完整质量",
          "商业使用授权",
        ],
      }
    ],  
  extensions: [
        {
          name: "Suno Web",
          description: "Browser-based music generation",
          descriptionZh: "基于浏览器的音乐生成",
        }
      ],  
  scene: "content-creation",
  skills: [
            "music production",
            "songwriting",
            "creative AI",
            "audio production"
          ],  
  pros: [
            "Generates complete songs",
            "Multiple genres",
            "Easy to use",
            "Good quality output"
          ],
  prosZh: [
            "生成完整歌曲",
            "多种音乐风格",
            "易于使用",
            "输出质量不错"
          ],
  cons: [
            "Limited control over details",
            "Not for professional music",
            "Similar sounding songs",
            "Free tier limitations"
          ],
  consZh: [
            "细节控制有限",
            "不适合专业音乐制作",
            "歌曲听感相似",
            "免费版功能限制"
          ],
  },

  {
    id: "murf-ai",
    name: "Murf AI",
    description: "AI voiceover platform with natural-sounding voices for professional content creation.",
  descriptionZh: "AI配音平台，提供自然声音，用于专业内容创作。",
    category: "audio",
    tags: ["voiceover", "tts", "professional", "narration"],
    difficulty: "beginner",
    url: "https://murf.ai",
    rating: r(4.3),
    pricing: "Free tier / from $19/mo",
    useCase: "Murf AI turns text into voiceovers for videos, e-learning, and presentations. It offers a wide range of natural voices with pitch and emphasis control.",
    icon: "\u{1F3A4}",
  company: "Murf AI",
  companyZh: "Murf AI",
  founded: "2020",  headquarters: "Boston, MA",  
  descriptionLong: "Murf AI is a voiceover platform with natural-sounding AI voices for professional content creation. It offers 120+ voices across 20+ languages with features like pitch control, emphasis adjustment, and pause insertion. Murf is widely used for e-learning, presentations, advertising, and corporate videos with a user-friendly editor.",
  descriptionLongZh: "Murf AI是一个AI配音平台，提供自然听感的AI语音。提供120多种声音、20多种语言，支持音调控制和强调调整。",
  advantages: [
            "120+ natural voices",
            "20+ languages",
            "Pitch and emphasis control",
            "User-friendly editor"
          ],
  advantagesZh: [
            "120多种自然声音",
            "20多种语言",
            "音调和强调控制",
            "用户友好的编辑器"
          ],
  useCases: [
            "E-learning narration",
            "Voiceover for videos",
            "Corporate training",
            "Podcast creation",
            "Advertising audio"
          ],
  useCasesZh: [
            "在线教育旁白",
            "视频配音",
            "企业培训",
            "播客创作"
          ],
  targetAudience: "Content creators, educators, and businesses needing professional voiceovers without hiring voice actors.",
  targetAudienceZh: "需要专业配音但又不想聘请配音演员的内容创作者、教育工作者和企业。",
  pricingTiers: [
      {
        tier: "Free",
          tierZh: "免费版",
        price: "$0",
        features: [
          "10 mins voice",
          "Limited voices"
        ],
        featuresZh: ["10分钟语音", "有限语音选择"],
      },
      {
        tier: "Basic",
          tierZh: "基础版",
        price: "$19/mo",
        features: [
          "24 hours/year",
          "All voices",
          "Commercial use"
        ],
        featuresZh: [
          "每年24小时",
          "所有语音",
          "商业使用授权",
        ],
      }
    ],  
  extensions: [
        {
          name: "Murf Web",
          description: "Browser-based voiceover studio",
          descriptionZh: "基于浏览器的配音工作室",
        }
      ],  
  scene: "content-creation",
  skills: [
            "voiceover",
            "audio production",
            "e-learning",
            "narration",
            "corporate training"
          ],  
  pros: [
            "Many voice options",
            "Natural sounding",
            "Good editing controls",
            "Multi-language"
          ],
  prosZh: [
            "多种声音选择",
            "声音自然",
            "编辑控制良好",
            "多语言支持"
          ],
  cons: [
            "Can be robotic at times",
            "Expensive for full features",
            "Limited free tier",
            "Voice quality varies"
          ],
  consZh: [
            "部分声音仍显机械",
            "完整功能价格较高",
            "免费版功能有限",
            "质量不稳定"
          ],
  },

  {
    id: "deeplearning-ai",
    name: "DeepLearning.AI",
    description: "World-class AI education platform offering courses from Andrew Ng and industry experts.",
  descriptionZh: "世界级的AI教育平台，提供吴恩达和行业专家的课程。",
    category: "learning",
    tags: ["courses", "education", "deep-learning", "certificate"],
    difficulty: "intermediate",
    url: "https://www.deeplearning.ai",
    rating: r(4.8),
    pricing: "Free / from $49/mo",
    useCase: "DeepLearning.AI offers structured AI courses from beginner to advanced. Andrew Ng's courses are the gold standard for learning machine learning and AI fundamentals.",
    icon: "\u{1F4DA}",
  company: "DeepLearning.AI",
  companyZh: "DeepLearning.AI",
  founded: "2017",  headquarters: "Palo Alto, CA",  
  descriptionLong: "DeepLearning.AI offers world-class AI education founded by Andrew Ng, one of the most influential figures in machine learning. It provides structured courses from beginner to advanced levels including the famous Deep Learning Specialization, Generative AI for Everyone, and more. Courses feature video lectures, quizzes, and hands-on projects. The gold standard for learning AI fundamentals.",
  descriptionLongZh: "DeepLearning.AI提供由吴恩达创办的世界级AI教育。提供从初级到高级的结构化课程，包含视频讲座、测验和动手项目。",
  advantages: [
            "Taught by Andrew Ng",
            "Structured learning paths",
            "Hands-on projects",
            "Industry-recognized certificates"
          ],
  advantagesZh: [
            "由吴恩达授课",
            "结构化的学习路径",
            "动手项目",
            "行业认可的证书"
          ],
  useCases: [
            "Starting AI learning journey",
            "Deep learning mastery",
            "Generative AI skills",
            "Career transition to AI",
            "ML fundamentals"
          ],
  useCasesZh: [
            "开启AI学xi之旅",
            "掌握深度学习",
            "生成式AI技能",
            "转型AI职业"
          ],
  targetAudience: "Anyone wanting to learn AI from scratch -- beginners to experienced developers seeking structured courses.",
  targetAudienceZh: "任何想从零学习AI的人——从初学者到寻求结构化课程的有经验开发者。",
  pricingTiers: [
      {
        tier: "Audit",
          tierZh: "旁听版",
        price: "$0",
        features: [
          "Video access",
          "Limited exercises"
        ],
        featuresZh: ["视频课程访问", "有限练习"],
      },
      {
        tier: "Coursera",
          tierZh: "Coursera版",
        price: "From $49/mo",
        features: [
          "Full courses",
          "Projects",
          "Certificate"
        ],
        featuresZh: [
          "完整课程",
          "项目管理",
          "结业证书",
        ],
      }
    ],  
  extensions: [
        {
          name: "DeepLearning.AI Website",
          description: "Course platform and community",
          descriptionZh: "课程平台和社区",
        }
      ],  
  scene: "free-open-source",
  skills: [
            "machine learning",
            "deep learning",
            "generative AI",
            "neural networks",
            "AI fundamentals"
          ],  
  pros: [
            "World-class instruction",
            "Structured curriculum",
            "Hands-on projects",
            "Certificate value"
          ],
  prosZh: [
            "世界级教学",
            "结构化课程",
            "动手项目",
            "证书有含金量"
          ],
  cons: [
            "Can be expensive",
            "Courses take time",
            "More academic focus",
            "Some content dated"
          ],
  consZh: [
            "费用可能较高",
            "课程耗时较长",
            "偏学术导向",
            "部分内容有些过时"
          ],
  },

  {
    id: "fast-ai",
    name: "fast.ai",
    description: "Practical deep learning education with a top-down teaching approach for developers.",
  descriptionZh: "实用的深度学习教育，采用自上而下的教学方法。",
    category: "learning",
    tags: ["courses", "practical", "free", "deep-learning"],
    difficulty: "intermediate",
    url: "https://www.fast.ai",
    rating: r(4.6),
    pricing: "Free",
    useCase: "fast.ai teaches deep learning using a practical, code-first approach. Their free courses let you build production models quickly without heavy math prerequisites.",
    icon: "\u{1F3C3}",
  company: "fast.ai",
  companyZh: "fast.ai",
  founded: "2016",  headquarters: "San Francisco, CA",  
  descriptionLong: "fast.ai provides practical deep learning education with a unique top-down teaching approach. Their famous Practical Deep Learning for Coders course teaches you to build production-ready models from lesson one without requiring heavy math prerequisites. All courses are free and focus on getting results quickly. The fast.ai library abstracts complexity while maintaining flexibility.",
  descriptionLongZh: "fast.ai提供实用的深度学习教育，采用自上而下的方法。从第一课就开始教授构建可投入生产的模型，无需大量数学先修知识。",
  advantages: [
            "Free high-quality courses",
            "Top-down practical approach",
            "Build production models early",
            "Active community"
          ],
  advantagesZh: [
            "免费高质量课程",
            "实用方法，从实践入手",
            "早期就能构建生产级模型",
            "活跃社区"
          ],
  useCases: [
            "Learning deep learning practically",
            "Building production ML models",
            "AI research exploration",
            "Teaching DL concepts"
          ],
  useCasesZh: [
            "实用学深度学习",
            "构建生产级ML模型",
            "AI研究探索",
            "教授深度学习概念"
          ],
  targetAudience: "Developers wanting to learn deep learning with a practical code-first approach.",
  targetAudienceZh: "希望通过实用的代码优先方法学习深度学习的开发者。",
  pricingTiers: [
      {
        tier: "All Courses",
          tierZh: "全部课程版",
        price: "$0",
        features: [
          "All course materials",
          "Forum access",
          "Book included"
        ],
        featuresZh: [
          "所有课程资料",
          "论坛访问权限",
          "包含教材",
        ],
      }
    ],  
  extensions: [
        {
          name: "fast.ai Forums",
          description: "Community discussion platform",
          descriptionZh: "社区讨论平台",
        }
      ],  
  scene: "free-open-source",
  skills: [
            "deep learning",
            "practical ML",
            "neural networks",
            "model deployment",
            "AI development"
          ],  
  pros: [
            "Completely free",
            "Practical approach",
            "Build real models quickly",
            "Great for coders"
          ],
  prosZh: [
            "完全免费",
            "实用方法，从实践入手",
            "快速构建真实模型",
            "非常适合程序员"
          ],
  cons: [
            "Not for absolute beginners",
            "Less theoretical depth",
            "Python focused only",
            "Self-paced no certification"
          ],
  consZh: [
            "不适合完全零基础初学者",
            "理论深度较少",
            "仅限Python",
            "无认证证书"
          ],
  },

  {
    id: "langchain",
    name: "LangChain",
    description: "Framework for building LLM-powered applications with composable chains and agents.",
  descriptionZh: "用可组合的链和代理构建LLM驱动应用的框架。",
    category: "coding",
    tags: ["framework", "llm", "agents", "python"],
    difficulty: "advanced",
    url: "https://www.langchain.com",
    rating: r(4.5),
    pricing: "Free (open-source) / LangSmith paid",
    useCase: "LangChain builds applications on top of LLMs. Use it to create chatbots, RAG systems, AI agents, and automated workflows with chain composition.",
    icon: "\u{26D3}️",
  company: "LangChain Inc.",
  companyZh: "LangChain",
  founded: "2022",  headquarters: "San Francisco, CA",  
  descriptionLong: "LangChain is a framework for building LLM-powered applications with composable chains and agents. It provides tools for prompt management, memory, retrieval-augmented generation (RAG), tool calling, and multi-agent systems. With LangSmith for debugging and LangGraph for stateful agents, it has become the standard framework for production LLM applications.",
  descriptionLongZh: "LangChain是一个用可组合链和代理构建LLM驱动应用的框架。已成为生产级LLM应用的标准框架，提供RAG、代理系统等工具。",
  advantages: [
            "Standard LLM framework",
            "RAG support built-in",
            "Multi-agent orchestration",
            "LangSmith debugging"
          ],
  advantagesZh: [
            "标准LLM框架",
            "内置RAG支持",
            "多代理编排",
            "LangSmith调试"
          ],
  useCases: [
            "Building RAG applications",
            "Creating AI chatbots",
            "Multi-agent systems",
            "Document Q&A systems",
            "Workflow automation"
          ],
  useCasesZh: [
            "构建RAG应用",
            "创建AI聊天机器人",
            "多代理系统",
            "文档问答"
          ],
  targetAudience: "Developers building production LLM applications who need a structured framework for chains and agents.",
  targetAudienceZh: "构建生产级LLM应用的开发者，需要一个结构化的链和代理框架。",
  pricingTiers: [
      {
        tier: "Open Source",
          tierZh: "开源版",
        price: "$0",
        features: [
          "All framework features",
          "Self-hosted"
        ],
        featuresZh: ["所有框架功能", "自行托管"],
      },
      {
        tier: "LangSmith",
          tierZh: "LangSmith版",
        price: "Pay-as-you-go",
        features: [
          "Debugging",
          "Monitoring",
          "Evaluation"
        ],
        featuresZh: [
          "调试功能",
          "监控功能",
          "评估功能",
        ],
      }
    ],  
  extensions: [
        {
          name: "LangChain Python",
          description: "Python framework package",
          descriptionZh: "Python框架包",
        },
        {
          name: "LangChain JS",
          description: "JavaScript/TypeScript framework",
          descriptionZh: "JavaScript/TypeScript框架",
        }
      ],  
  scene: "development",
  skills: [
            "LLM development",
            "RAG systems",
            "agent development",
            "Python",
            "prompt engineering"
          ],  
  pros: [
            "Industry standard framework",
            "Excellent RAG support",
            "Active development",
            "Strong community"
          ],
  prosZh: [
            "行业标准框架",
            "RAG支持出色",
            "积极开发中",
            "强大的社区"
          ],
  cons: [
            "Fast-changing API",
            "Can be complex",
            "Overkill for simple apps",
            "Documentation can lag"
          ],
  consZh: [
            "API变化快",
            "可能过于复杂",
            "简单应用大材小用",
            "文档更新滞后"
          ],
  },

  {
    id: "huggingface",
    name: "Hugging Face",
    description: "Leading platform for open-source AI models, datasets, and collaborative ML development.",
  descriptionZh: "开源AI模型、数据集和协作ML开发的领先平台。",
    category: "industry",
    tags: ["models", "open-source", "community", "mlops"],
    difficulty: "advanced",
    url: "https://huggingface.co",
    rating: r(4.7),
    pricing: "Free / paid inference and storage",
    useCase: "Hugging Face is the GitHub of AI. Access thousands of pre-trained models, datasets, and Spaces apps. Essential for ML engineers and AI researchers.",
    icon: "\u{1F917}",
  company: "Hugging Face",
  companyZh: "Hugging Face",
  founded: "2016",  headquarters: "New York, NY",  
  descriptionLong: "Hugging Face is the leading platform for open-source AI models, datasets, and collaborative ML development. Often called the GitHub of AI, it hosts 500K+ models, 15万+数据集, and Spaces apps. The Transformers library provides a unified API for thousands of models. Essential for ML engineers and AI researchers for model discovery, sharing, and deployment.",
  descriptionLongZh: "Hugging Face是开源AI模型、数据集和协作ML开发的领先平台。托管50万+模型、15万+数据集和Spaces应用，是ML工程师的必备工具。",
  advantages: [
            "500K+ open-source models",
            "15万+数据集",
            "Spaces for demo apps",
            "Transformers library"
          ],
  advantagesZh: [
            "50万+开源模型",
            "15万+数据集",
            "Spaces演示应用",
            "Transformers库"
          ],
  useCases: [
            "Model discovery and download",
            "Fine-tuning open models",
            "Dataset sharing",
            "ML research collaboration",
            "Deploying model demos"
          ],
  useCasesZh: [
            "模型发现和下载",
            "微调开放模型",
            "数据集共享",
            "ML研究协作",
            "部署模型演示"
          ],
  targetAudience: "ML engineers, AI researchers, and developers who work with open-source AI models and datasets.",
  targetAudienceZh: "使用开源AI模型和数据集的ML工程师、AI研究人员和开发者。",
  pricingTiers: [
      {
        tier: "Free",
          tierZh: "免费版",
        price: "$0",
        features: [
          "Public models",
          "Datasets",
          "Limited Spaces"
        ],
        featuresZh: [
          "公开模型",
          "数据集访问",
          "有限Spaces额度",
        ],
      },
      {
        tier: "Pro",
          tierZh: "专业版",
        price: "$9/mo",
        features: [
          "Private repos",
          "More Spaces",
          "Inference API"
        ],
        featuresZh: [
          "私有仓库",
          "更多Spaces额度",
          "推理API",
        ],
      }
    ],  
  extensions: [
        {
          name: "Hugging Face Hub",
          description: "Web platform and APIs",
          descriptionZh: "网页平台和API",
        }
      ],  
  scene: "free-open-source",
  skills: [
            "machine learning",
            "model deployment",
            "NLP",
            "model fine-tuning",
            "MLOps"
          ],  
  pros: [
            "Huge model repository",
            "Strong community",
            "Transformers industry standard",
            "Spaces for demos"
          ],
  prosZh: [
            "海量模型仓库",
            "强大的社区",
            "Transformers行业标准",
            "Spaces演示应用"
          ],
  cons: [
            "Can be overwhelming",
            "Pro features cost money",
            "Model quality varies",
            "Dependency on platform"
          ],
  consZh: [
            "功能繁多可能让人不知所措",
            "Pro功能需要付费",
            "模型质量参差不齐",
            "依赖平台"
          ],
  },
  // ====== Content Creation (8) ======
  {
    id: "writesonic",
    name: "Writesonic",
    description: "AI writing assistant for marketing content, blog posts, and SEO-optimized copy.",
    descriptionZh: "AI写作助手，用于营销内容、博客文章和SEO优化文案。",
    category: "writing",
    tags: ["writing", "marketing", "SEO", "content"],
    difficulty: "beginner",
    url: "https://writesonic.com",
    rating: 4,
    pricing: "Free tier / from $19/mo",
    useCase: "Writesonic generates SEO-optimized blog posts, landing pages, and ad copy with built-in keyword research.",
    icon: "\u270F\uFE0F",
    company: "Writesonic",
    companyZh: "Writesonic",
    founded: "2020",
    headquarters: "San Francisco, CA",
    descriptionLong: "Writesonic is an AI writing assistant focused on marketing content creation with built-in SEO tools. It generates blog posts, landing pages, ad copy, and email campaigns. Features include AI article writer with up-to-date facts, SEO optimization, and brand voice customization. Popular among content marketers and small businesses.",
    descriptionLongZh: "Writesonic是一款AI写作助手，专注于营销内容创作，内置SEO工具。可生成博客文章、落地页、广告文案和邮件营销内容。",
    advantages: ["Built-in SEO optimization", "AI article writer with real-time facts", "Brand voice customization", "Multi-language support"],
    advantagesZh: ["内置SEO优化", "支持实时信息的AI文章撰写", "品牌语气定制", "多语言支持"],
    useCases: ["Blog post writing with SEO", "Landing page copy", "Facebook and Google ads", "Email marketing campaigns", "Product descriptions"],
    useCasesZh: ["SEO博客文章写作", "落地页文案", "广告文案", "邮件营销", "产品描述"],
    targetAudience: "Content marketers and small business owners needing SEO-optimized copy at scale.",
    targetAudienceZh: "需要大规模SEO优化文案的内容营销人员和小企业主。",
    pricingTiers: [
      { tier: "Free", tierZh: "免费版", price: "$0", features: ["10,000 words/month", "Basic templates"], featuresZh: ["每月1万字", "基础模板"] },
    ],
    extensions: [{ name: "Writesonic Chrome Extension", description: "Write anywhere on the web", descriptionZh: "在网页任意位置写作" }],
    skills: ["copywriting", "SEO writing", "content marketing", "email marketing", "landing pages"],
    pros: ["SEO-focused writing", "Good for long-form content", "Real-time fact checking", "Affordable pricing"],
    prosZh: ["专注于SEO写作", "适合长内容", "实时事实核查", "价格实惠"],
    cons: ["Output can be generic", "Less creative than Jasper", "Free tier limited", "SEO features beta"],
    consZh: ["内容可能较通用", "创意不如Jasper", "免费版限制多", "SEO功能尚在测试"],
    scene: "content-creation",
  },
  {
    id: "rytr",
    name: "Rytr",
    description: "Affordable AI writing assistant with a wide range of use cases and tones.",
    descriptionZh: "价格实惠的AI写作助手，支持多种用例和语气。",
    category: "writing",
    tags: ["writing", "affordable", "templates", "copywriting"],
    difficulty: "beginner",
    url: "https://rytr.me",
    rating: 4,
    pricing: "Free tier / from $9/mo",
    useCase: "Rytr is a budget-friendly AI writer for emails, blogs, social media, and copywriting with 40+ use case templates.",
    icon: "\u270D\uFE0F",
    company: "Rytr",
    companyZh: "Rytr",
    founded: "2021",
    headquarters: "London, UK",
    descriptionLong: "Rytr is an affordable AI writing assistant offering 40+ use case templates and 30+ tones. It generates copy for emails, blogs, social media, SEO content, and more. With built-in plagiarism checking and integration support, it is a strong budget option for solo creators and small teams.",
    descriptionLongZh: "Rytr是一款价格实惠的AI写作助手，提供40多种用例模板和30多种语气。适合个人创作者和小团队。",
    advantages: ["Very affordable pricing", "40+ use case templates", "30+ tones to choose from", "Built-in plagiarism checker"],
    advantagesZh: ["价格非常实惠", "40多种用例模板", "30多种语气可选", "内置查重功能"],
    useCases: ["Email writing", "Blog content", "Social media posts", "SEO copy", "Product descriptions"],
    useCasesZh: ["邮件写作", "博客内容", "社交媒体帖子", "SEO文案", "产品描述"],
    targetAudience: "Budget-conscious solo creators and small teams needing versatile AI writing.",
    targetAudienceZh: "预算有限的个人创作者和小团队，需要多功能AI写作。",
    pricingTiers: [
      { tier: "Free", tierZh: "免费版", price: "$0", features: ["5,000 chars/month", "40+ templates"], featuresZh: ["每月5000字符", "40多个模板"] },
    ],
    extensions: [{ name: "Rytr Web App", description: "Browser-based writing tool", descriptionZh: "基于浏览器的写作工具" }],
    skills: ["copywriting", "content creation", "email writing", "social media"],
    pros: ["Very affordable", "Good template variety", "Easy to use", "Plagiarism checker included"],
    prosZh: ["价格实惠", "模板种类丰富", "易于使用", "包含查重功能"],
    cons: ["Limited long-form quality", "Less advanced features", "Output can feel templated", "No team features"],
    consZh: ["长文质量有限", "高级功能较少", "内容可能模板化", "无团队功能"],
    scene: "content-creation",
  },
  {
    id: "quillbot",
    name: "QuillBot",
    description: "AI paraphrasing and writing tool that helps rephrase sentences and improve writing.",
    descriptionZh: "AI改写和写作工具，帮助改写句子和改进写作。",
    category: "writing",
    tags: ["paraphrasing", "writing", "grammar", "summarization"],
    difficulty: "beginner",
    url: "https://quillbot.com",
    rating: 4,
    pricing: "Free / $9.95/mo Premium",
    useCase: "QuillBot paraphrases sentences, summarizes articles, checks grammar, and helps improve writing clarity.",
    icon: "\uD83D\uDCDD",
    company: "QuillBot",
    companyZh: "QuillBot",
    founded: "2017",
    headquarters: "Chicago, IL",
    descriptionLong: "QuillBot is an AI paraphrasing and writing tool that helps rephrase sentences, summarize articles, and improve writing clarity. It offers 7+ paraphrasing modes from standard to creative, a grammar checker, summarizer, and citation generator. Widely used by students, researchers, and professionals for rewriting and polishing content.",
    descriptionLongZh: "QuillBot是一款AI改写和写作工具，可改写句子、总结文章、改进写作清晰度。广泛应用于学生、研究人员和专业人士。",
    advantages: ["7+ paraphrasing modes", "Grammar checker included", "Article summarizer", "Citation generator"],
    advantagesZh: ["7种以上改写模式", "包含语法检查", "文章摘要工具", "引文生成器"],
    useCases: ["Paraphrasing academic text", "Summarizing long articles", "Grammar and style checking", "Academic citation generation", "Essay rewriting"],
    useCasesZh: ["学术文本改写", "长文章摘要", "语法和风格检查", "学术引文生成", "论文改写"],
    targetAudience: "Students, researchers, and professionals who need to paraphrase, summarize, and polish written content.",
    targetAudienceZh: "需要改写、总结和润色书面内容的学生、研究人员和专业人士。",
    pricingTiers: [
      { tier: "Free", tierZh: "免费版", price: "$0", features: ["Limited paraphrasing", "2 modes", "Basic summary"], featuresZh: ["有限改写次数", "2种模式", "基础摘要"] },
    ],
    extensions: [{ name: "QuillBot Chrome Extension", description: "Paraphrase anywhere on the web", descriptionZh: "在网页任意位置改写" }],
    skills: ["paraphrasing", "academic writing", "editing", "summarization", "grammar"],
    pros: ["Excellent paraphrasing quality", "Useful summarizer", "Generous free tier", "Multiple modes"],
    prosZh: ["改写质量优秀", "摘要功能实用", "慷慨的免费套餐", "多种模式"],
    cons: ["Not for original writing", "Premium needed for best features", "Can change meaning", "Limited creativity"],
    consZh: ["不适合原创写作", "最佳功能需付费", "可能改变原意", "创意有限"],
    scene: "content-creation",
  },
  {
    id: "wordtune",
    name: "Wordtune",
    description: "AI writing companion that rephrases sentences and helps express ideas more clearly.",
    descriptionZh: "AI写作伴侣，可改写句子，帮助更清晰地表达想法。",
    category: "writing",
    tags: ["writing", "paraphrasing", "editing", "productivity"],
    difficulty: "beginner",
    url: "https://www.wordtune.com",
    rating: 4,
    pricing: "Free / $9.99/mo Premium",
    useCase: "Wordtune rephrases sentences in multiple ways, adjusts tone, and helps you write more confidently.",
    icon: "\uD83D\uDCDD",
    company: "AI21 Labs",
    companyZh: "AI21 Labs",
    founded: "2017",
    headquarters: "Tel Aviv, Israel",
    descriptionLong: "Wordtune is an AI writing companion from AI21 Labs that rephrases sentences in multiple ways to help users express ideas more clearly. It offers tone adjustment, sentence expansion/shortening, and translation features. Integrates as a browser extension across the web and as a desktop app, making it available anywhere you write.",
    descriptionLongZh: "Wordtune是AI21 Labs推出的AI写作伴侣，能以多种方式改写句子，帮助用户更清晰地表达想法。集成浏览器扩展和桌面应用。",
    advantages: ["Multiple rephrase options per sentence", "Tone adjustment (casual/professional)", "Sentence expansion and shortening", "Cross-platform browser extension"],
    advantagesZh: ["每句多种改写选项", "语气调整（随意/专业）", "句子扩写和缩写", "跨平台浏览器扩展"],
    useCases: ["Professional email rewriting", "Academic text refinement", "Social media copy", "Creative writing variation", "Translation-assisted writing"],
    useCasesZh: ["专业邮件改写", "学术文本精炼", "社交媒体文案", "创意写作变体", "翻译辅助写作"],
    targetAudience: "Writers and professionals who want to improve sentence-level clarity and express ideas more effectively.",
    targetAudienceZh: "希望在句子层面提高清晰度和表达效果的写作者和专业人士。",
    pricingTiers: [
      { tier: "Free", tierZh: "免费版", price: "$0", features: ["10 rephrases/day", "Basic modes"], featuresZh: ["每天10次改写", "基础模式"] },
    ],
    extensions: [{ name: "Wordtune Chrome Extension", description: "Write better across the web", descriptionZh: "在网页各处写出更好的文章" }],
    skills: ["editing", "paraphrasing", "writing refinement", "professional writing", "creative writing"],
    pros: ["Excellent sentence-level suggestions", "Natural rephrasing", "Works everywhere via extension", "Tone options useful"],
    prosZh: ["句子级建议出色", "改写自然", "扩展随处可用", "语气选项实用"],
    cons: ["Daily limits on free", "Premium expensive for value", "Only sentence level", "No long-form generation"],
    consZh: ["免费版每日限制", "付费版性价比一般", "仅限句子级别", "不支持长文生成"],
    scene: "content-creation",
  },
  {
    id: "copysmith",
    name: "CopySmith",
    description: "AI copywriting platform for e-commerce product descriptions and marketing copy.",
    descriptionZh: "AI文案写作平台，专注于电商产品描述和营销文案。",
    category: "writing",
    tags: ["ecommerce", "copywriting", "product-descriptions", "marketing"],
    difficulty: "beginner",
    url: "https://copysmith.ai",
    rating: 3,
    pricing: "From $19/mo",
    useCase: "CopySmith specializes in generating product descriptions and e-commerce copy at scale for online stores.",
    icon: "\uD83D\uDCE6",
    company: "CopySmith",
    companyZh: "CopySmith",
    founded: "2020",
    headquarters: "San Francisco, CA",
    descriptionLong: "CopySmith is an AI copywriting platform specializing in e-commerce product descriptions, marketing copy, and content creation at scale. It offers bulk generation for product listings, Amazon-optimized descriptions, and integration with e-commerce platforms like Shopify. Popular among online retailers and dropshippers.",
    descriptionLongZh: "CopySmith是一款AI文案平台，专注于电商产品描述和营销文案的批量生成。支持Shopify等电商平台集成。",
    advantages: ["E-commerce focused", "Bulk product description generation", "Shopify integration", "Amazon-optimized copy"],
    advantagesZh: ["专注电商", "批量产品描述生成", "Shopify集成", "亚马逊优化文案"],
    useCases: ["Product description writing", "Amazon listing optimization", "E-commerce SEO copy", "Bulk catalog writing", "Marketing emails"],
    useCasesZh: ["产品描述写作", "亚马逊Listing优化", "电商SEO文案", "批量目录编写", "营销邮件"],
    targetAudience: "E-commerce businesses and dropshippers who need bulk product descriptions and marketing copy.",
    targetAudienceZh: "需要批量产品描述和营销文案的电商企业和代发货商。",
    pricingTiers: [
      { tier: "Starter", tierZh: "入门版", price: "$19/mo", features: ["20,000 words/mo", "Basic features"], featuresZh: ["每月2万字", "基础功能"] },
    ],
    extensions: [{ name: "CopySmith Shopify App", description: "Direct Shopify integration", descriptionZh: "Shopify直接集成" }],
    skills: ["e-commerce copywriting", "product descriptions", "Amazon SEO", "Shopify", "bulk content"],
    pros: ["Great for e-commerce", "Bulk generation saves time", "Shopify integration", "Good template library"],
    prosZh: ["适合电商", "批量生成省时", "Shopify集成", "模板库丰富"],
    cons: ["Not for general writing", "More expensive than alternatives", "Output needs editing", "Limited creative work"],
    consZh: ["不适合通用写作", "比替代品贵", "输出需编辑", "创意有限"],
    scene: "marketing",
  },
  {
    id: "anyword",
    name: "Anyword",
    description: "AI copywriting platform with predictive performance scoring for marketing copy.",
    descriptionZh: "AI文案平台，为营销文案提供预测性效果评分。",
    category: "writing",
    tags: ["copywriting", "analytics", "marketing", "performance"],
    difficulty: "intermediate",
    url: "https://anyword.com",
    rating: 4,
    pricing: "From $49/mo",
    useCase: "Anyword generates and scores marketing copy by predicted performance, helping optimize conversion rates.",
    icon: "\uD83D\uDCCA",
    company: "Anyword",
    companyZh: "Anyword",
    founded: "2021",
    headquarters: "New York, NY",
    descriptionLong: "Anyword is an AI copywriting platform with predictive performance scoring. It generates marketing copy and scores each variation by predicted conversion rate, engagement, and readability. Supports ads, emails, landing pages, and social media with data-driven optimization. Popular among performance marketers.",
    descriptionLongZh: "Anyword是一款AI文案平台，具有预测性效果评分功能。可生成营销文案并按预测转化率、参与度和可读性评分。",
    advantages: ["Predictive performance scoring", "Data-driven optimization", "Multiple channel support", "A/B copy testing"],
    advantagesZh: ["预测性效果评分", "数据驱动优化", "多平台支持", "A/B文案测试"],
    useCases: ["Ad copy optimization", "Email subject line scoring", "Landing page copy", "Social media ads", "Conversion optimization"],
    useCasesZh: ["广告文案优化", "邮件主题行评分", "落地页文案", "社交媒体广告", "转化率优化"],
    targetAudience: "Performance marketers and growth teams who want data-driven copywriting with conversion optimization.",
    targetAudienceZh: "追求数据驱动文案和转化率优化的效果营销人员和增长团队。",
    pricingTiers: [
      { tier: "Starter", tierZh: "入门版", price: "$49/mo", features: ["5,000 AI words/mo", "Basic scoring"], featuresZh: ["每月5000AI词", "基础评分"] },
    ],
    extensions: [{ name: "Anyword Chrome Extension", description: "Score copy anywhere", descriptionZh: "随处评估文案效果" }],
    skills: ["copywriting", "conversion optimization", "A/B testing", "marketing analytics", "ad copy"],
    pros: ["Unique scoring feature", "Data-driven approach", "Good for ads", "Optimization insights"],
    prosZh: ["独特的评分功能", "数据驱动方法", "适合广告", "优化洞察"],
    cons: ["Expensive", "Overkill for simple copy", "Scoring not always accurate", "Less creative flexibility"],
    consZh: ["价格较高", "简单文案过大材小用", "评分不一定准确", "创意灵活性较低"],
    scene: "marketing",
  },
  {
    id: "sudowrite",
    name: "Sudowrite",
    description: "AI writing tool designed specifically for creative and fiction writers.",
    descriptionZh: "专为创意和小说作家设计的AI写作工具。",
    category: "writing",
    tags: ["creative-writing", "fiction", "storytelling", "novel"],
    difficulty: "intermediate",
    url: "https://www.sudowrite.com",
    rating: 4,
    pricing: "From $19/mo",
    useCase: "Sudowrite helps fiction writers brainstorm plots, develop characters, rewrite passages, and overcome writer's block.",
    icon: "\uD83D\uDCD6",
    company: "Sudowrite",
    companyZh: "Sudowrite",
    founded: "2020",
    headquarters: "San Francisco, CA",
    descriptionLong: "Sudowrite is an AI writing tool designed specifically for creative and fiction writers. It helps with story outlining, character development, world-building, rewriting passages, and overcoming writer's block. Features include beat sheets, story engine for generating variations, and descriptive writing expansion. Loved by novelists and screenwriters.",
    descriptionLongZh: "Sudowrite是一款专为创意和小说作家设计的AI写作工具。帮助故事大纲、角色发展、段落改写和克服写作障碍。",
    advantages: ["Fiction-focused AI", "Story outlining tools", "Character development", "Descriptive writing expansion"],
    advantagesZh: ["专注小说创作", "故事大纲工具", "角色发展", "描写性写作扩展"],
    useCases: ["Novel writing and outlining", "Character development", "Scene rewriting", "Overcoming writer's block", "World-building"],
    useCasesZh: ["小说写作和大纲", "角色发展", "场景改写", "克服写作障碍", "世界观构建"],
    targetAudience: "Novelists, fiction writers, and screenwriters who want AI assistance for creative writing.",
    targetAudienceZh: "小说家、虚构作家和编剧，希望AI辅助创意写作。",
    pricingTiers: [
      { tier: "Pro", tierZh: "专业版", price: "$19/mo", features: ["Unlimited words", "All features"], featuresZh: ["无限字数", "All features"] },
    ],
    extensions: [{ name: "Sudowrite Web App", description: "Browser-based writing studio", descriptionZh: "基于浏览器的写作工作室" }],
    skills: ["creative writing", "fiction", "storytelling", "character design", "world-building"],
    pros: ["Excellent for fiction", "Unique story tools", "Good rewriting features", "Inspirational for writers"],
    prosZh: ["适合小说创作", "独特的故事工具", "改写功能好", "激发作家灵感"],
    cons: ["Not for business writing", "Expensive for casual use", "Learning curve for features", "AI suggestions can be generic"],
    consZh: ["不适合商务写作", "随意使用较贵", "功能有学习曲线", "AI建议可能过于泛泛"],
    scene: "content-creation",
  },

  // ====== Design & Video (8) ======
  {
    id: "remove-bg",
    name: "Remove.bg",
    description: "AI-powered background removal tool that works in seconds with impressive accuracy.",
    descriptionZh: "AI驱动的背景移除工具，几秒钟内完成，精准度令人印象深刻。",
    category: "image-generation",
    tags: ["background-removal", "photo-editing", "design", "quick"],
    difficulty: "beginner",
    url: "https://www.remove.bg",
    rating: 4,
    pricing: "Free / from $9/mo",
    useCase: "Remove.bg instantly removes image backgrounds with AI. Perfect for e-commerce photos, profile pictures, and design assets.",
    icon: "\uD83D\uDCF7",
    company: "Kaleido",
    companyZh: "Kaleido",
    founded: "2018",
    headquarters: "Berlin, Germany",
    descriptionLong: "Remove.bg is an AI-powered background removal tool that processes images in seconds with impressive accuracy. It handles complex edges like hair and fur well. Offers API access for automation, batch processing for bulk work, and integration with design tools like Photoshop and Canva. Essential for e-commerce, real estate, and graphic design workflows.",
    descriptionLongZh: "Remove.bg是一款AI背景移除工具，几秒内处理图像，对复杂边缘（如头发、毛发）处理效果出色。",
    advantages: ["Fast AI background removal", "Handles complex edges well", "API for automation", "Batch processing"],
    advantagesZh: ["快速AI背景移除", "复杂边缘处理出色", "API支持自动化", "批量处理"],
    useCases: ["E-commerce product photos", "Profile picture cleanup", "Real estate photo editing", "Design asset preparation", "Social media visuals"],
    useCasesZh: ["电商产品照片", "头像清理", "房产照片编辑", "设计素材准备", "社交媒体视觉"],
    targetAudience: "E-commerce sellers, designers, and photographers needing quick background removal.",
    targetAudienceZh: "需要快速背景移除的电商卖家、设计师和摄影师。",
    pricingTiers: [
      { tier: "Free", tierZh: "免费版", price: "$0", features: ["Standard resolution", "Preview quality"], featuresZh: ["标准分辨率", "预览质量"] },
    ],
    extensions: [
      { name: "Remove.bg Photoshop Plugin", description: "Background removal in Photoshop", descriptionZh: "在Photoshop中移除背景" },
      { name: "Remove.bg API", description: "Automated background removal", descriptionZh: "自动化背景移除" },
    ],
    skills: ["photo editing", "background removal", "e-commerce photos", "image processing"],
    pros: ["Fast and accurate", "Easy to use", "API available", "Works on complex edges"],
    prosZh: ["快速精准", "易于使用", "提供API", "复杂边缘也可处理"],
    cons: ["Free has limited resolution", "Expensive for high volume", "Less control than manual", "Privacy concerns with uploaded images"],
    consZh: ["免费版分辨率有限", "大量使用时较贵", "不如手动控制灵活", "上传图片有隐私顾虑"],
    scene: "design-video",
  },
  {
    id: "clipdrop",
    name: "ClipDrop",
    description: "AI design toolkit for image cleanup, relighting, and background replacement.",
    descriptionZh: "AI设计工具包，用于图像清理、重新照明和背景替换。",
    category: "image-generation",
    tags: ["design", "cleanup", "relighting", "tools"],
    difficulty: "beginner",
    url: "https://clipdrop.co",
    rating: 4,
    pricing: "Free tier / from $9/mo",
    useCase: "ClipDrop offers AI-powered image cleaning, relighting, background removal, and text-to-image generation in one toolkit.",
    icon: "\uD83D\uDD8C\uFE0F",
    company: "ClipDrop (Init ML)",
    companyZh: "ClipDrop（Init ML）",
    founded: "2021",
    headquarters: "Paris, France",
    descriptionLong: "ClipDrop is an AI design toolkit by Init ML that offers image cleanup, relighting, background removal, text-to-image generation, and object removal. The apps work via web and mobile with a focus on quick, one-click fixes. Integrates with popular design tools via API and plugins. Useful for designers and content creators who need fast image adjustments.",
    descriptionLongZh: "ClipDrop是Init ML推出的AI设计工具包，提供图像清理、重新照明、背景移除和文字生成图像等功能。",
    advantages: ["Multiple AI tools in one", "One-click image fixes", "Mobile and web apps", "API integration"],
    advantagesZh: ["多种AI工具合一", "一键图像修复", "移动和网页应用", "API集成"],
    useCases: ["Product photo cleanup", "Image relighting", "Object removal", "Background replacement", "Quick design mockups"],
    useCasesZh: ["产品照片清理", "图像重新照明", "物体移除", "背景替换", "快速设计原型"],
    targetAudience: "Designers and content creators who need quick AI-powered image fixes without complex software.",
    targetAudienceZh: "需要快速AI图像修复的设计师和内容创作者。",
    pricingTiers: [
      { tier: "Free", tierZh: "免费版", price: "$0", features: ["Basic tools", "Standard quality"], featuresZh: ["基础工具", "标准质量"] },
    ],
    extensions: [{ name: "ClipDrop Web App", description: "Browser-based design toolkit", descriptionZh: "基于浏览器的设计工具包" }],
    skills: ["photo editing", "image cleanup", "design tools", "background removal", "object removal"],
    pros: ["Versatile tool collection", "One-click simplicity", "Good quality output", "Mobile app available"],
    prosZh: ["工具集多功能", "一键操作简单", "输出质量好", "提供移动应用"],
    cons: ["Individual tools limited", "Pro needed for quality", "Some features beta", "Less powerful than dedicated tools"],
    consZh: ["单个工具功能有限", "高质量需Pro版", "部分功能测试中", "不如专业工具强大"],
    scene: "design-video",
  },
  {
    id: "capcut",
    name: "CapCut",
    description: "Free all-in-one video editing app with AI features for creators.",
    descriptionZh: "免费的全能视频编辑应用，为创作者提供AI功能。",
    category: "video-generation",
    tags: ["video-editing", "free", "social-media", "mobile"],
    difficulty: "beginner",
    url: "https://capcut.com",
    rating: 4,
    pricing: "Free / Pro $7.99/mo",
    useCase: "CapCut is a free video editor with AI auto-captions, text-to-speech, effects, and templates for social media content.",
    icon: "\uD83C\uDFA5",
    company: "ByteDance",
    companyZh: "字节跳动",
    founded: "2020",
    headquarters: "Beijing, China",
    descriptionLong: "CapCut is a free all-in-one video editing app developed by ByteDance with powerful AI features. It offers auto-captions, text-to-speech, motion tracking, keyframe animation, and extensive template library. Widely used for TikTok and social media content creation. The Pro tier adds advanced effects, higher exports, and cloud storage.",
    descriptionLongZh: "CapCut是字节跳动开发的免费全能视频编辑应用，具有强大的AI功能。提供自动字幕、文字转语音、运动跟踪和丰富的模板库。",
    advantages: ["Completely free core features", "AI auto-captions", "Extensive template library", "Desktop and mobile"],
    advantagesZh: ["核心功能完全免费", "AI自动字幕", "海量模板库", "支持桌面和移动端"],
    useCases: ["TikTok video creation", "Social media shorts", "YouTube content", "Video captions", "Quick video editing"],
    useCasesZh: ["抖音视频创作", "社交媒体短视频", "YouTube内容", "视频字幕", "快速视频编辑"],
    targetAudience: "Social media creators and anyone needing a free, powerful video editor for short-form content.",
    targetAudienceZh: "社交媒体创作者和任何需要免费、强大视频编辑器制作短视频的人。",
    pricingTiers: [
      { tier: "Free", tierZh: "免费版", price: "$0", features: ["Basic editing", "Auto-captions", "Templates"], featuresZh: ["基础编辑", "自动字幕", "模板"] },
    ],
    extensions: [
      { name: "CapCut Desktop", description: "Windows and Mac app", descriptionZh: "Windows和Mac应用" },
      { name: "CapCut Mobile", description: "iOS and Android app", descriptionZh: "iOS和Android应用" },
    ],
    skills: ["video editing", "social media content", "captions", "short-form video", "motion graphics"],
    pros: ["Free with powerful features", "AI captions excellent", "Easy to use", "Great for TikTok"],
    prosZh: ["免费功能强大", "AI字幕出色", "易于使用", "适合抖音短视频"],
    cons: ["ByteDance privacy concerns", "Pro features limited on free", "Desktop app less polished", "Watermark on some exports"],
    consZh: ["字节跳动隐私顾虑", "免费版Pro功能有限", "桌面端不够精致", "部分导出有水印"],
    scene: "design-video",
  },
  {
    id: "descript",
    name: "Descript",
    description: "AI-powered video and audio editor that works like a document editor.",
    descriptionZh: "AI驱动的视频和音频编辑器，像编辑文档一样编辑媒体。",
    category: "video-generation",
    tags: ["video-editing", "audio", "transcription", "podcast"],
    difficulty: "intermediate",
    url: "https://www.descript.com",
    rating: 4,
    pricing: "Free tier / from $24/mo",
    useCase: "Descript edits video and audio by editing the transcript. Remove filler words, add captions, and record voiceovers.",
    icon: "\uD83C\uDF99\uFE0F",
    company: "Descript",
    companyZh: "Descript",
    founded: "2017",
    headquarters: "San Francisco, CA",
    descriptionLong: "Descript is an AI-powered video and audio editor that works like a document editor. It transcribes your media, allowing you to edit by editing text. Features include filler word removal, AI voice cloning (Overdub), screen recording, caption generation, and multi-track editing. Revolutionary for podcasters and content creators who dislike traditional video editing.",
    descriptionLongZh: "Descript是一款AI视频和音频编辑器，像编辑文档一样编辑媒体。自动转录音视频，通过编辑文字来编辑媒体内容。",
    advantages: ["Edit media by editing text", "AI filler word removal", "Voice cloning (Overdub)", "Auto-caption generation"],
    advantagesZh: ["通过编辑文字来编辑媒体", "AI去除填充词", "语音克隆", "自动生成字幕"],
    useCases: ["Podcast editing", "Screen recording voiceovers", "Video captioning", "Remote interview editing", "Filler word removal"],
    useCasesZh: ["播客编辑", "屏幕录制配音", "视频字幕", "远程采访编辑", "去除填充词"],
    targetAudience: "Podcasters, content creators, and anyone who wants a simpler way to edit video and audio.",
    targetAudienceZh: "播客制作者、内容创作者，以及希望简化音视频编辑的人。",
    pricingTiers: [
      { tier: "Free", tierZh: "免费版", price: "$0", features: ["1 hour transcription", "Basic editing"], featuresZh: ["1小时转录", "基础编辑"] },
    ],
    extensions: [{ name: "Descript Desktop", description: "Windows and Mac app", descriptionZh: "Windows和Mac应用" }],
    skills: ["video editing", "audio editing", "podcasting", "transcription", "screen recording"],
    pros: ["Innovative text-based editing", "AI features powerful", "Great for podcasters", "Saves editing time"],
    prosZh: ["创新的文本编辑方式", "AI功能强大", "适合播客制作者", "节省编辑时间"],
    cons: ["Expensive for full features", "Not for complex video", "Voice cloning ethical concerns", "Requires internet"],
    consZh: ["全功能价格较高", "不适合复杂视频", "语音克隆伦理问题", "需要联网"],
    scene: "design-video",
  },
  {
    id: "synthesia",
    name: "Synthesia",
    description: "AI video generation platform for creating professional videos with AI avatars.",
    descriptionZh: "AI视频生成平台，使用AI虚拟形象创建专业视频。",
    category: "video-generation",
    tags: ["avatars", "presentation", "training", "professional"],
    difficulty: "intermediate",
    url: "https://www.synthesia.io",
    rating: 4,
    pricing: "From $29/mo",
    useCase: "Synthesia creates professional videos with AI avatars from text scripts. Ideal for training, marketing, and corporate comms.",
    icon: "\uD83C\uDFAD",
    company: "Synthesia",
    companyZh: "Synthesia",
    founded: "2017",
    headquarters: "London, UK",
    descriptionLong: "Synthesia is an AI video generation platform that creates professional videos with realistic AI avatars from text scripts. It offers 140+ AI avatar options, 120+ languages, and custom avatar creation. Used for training videos, product demos, marketing content, and corporate communications without filming. Enterprise-grade security and template library included.",
    descriptionLongZh: "Synthesia是AI视频生成平台，通过文字脚本创建逼真的AI虚拟形象视频。支持140+虚拟形象、120+语言。",
    advantages: ["140+ AI avatars", "120+ languages", "No filming required", "Template library"],
    advantagesZh: ["140多种AI虚拟形象", "120多种语言", "无需拍摄", "模板库"],
    useCases: ["Training videos", "Product demos", "Marketing content", "Corporate communications", "Multi-language content"],
    useCasesZh: ["培训视频", "产品演示", "营销内容", "企业沟通", "多语言内容"],
    targetAudience: "Businesses and content teams who need professional video content without filming or voice actors.",
    targetAudienceZh: "需要专业视频内容但无需拍摄或配音演员的企业和内容团队。",
    pricingTiers: [
      { tier: "Starter", tierZh: "入门版", price: "$29/mo", features: ["10 mins video", "Standard avatars"], featuresZh: ["10分钟视频", "标准虚拟形象"] },
    ],
    extensions: [{ name: "Synthesia Web App", description: "Browser-based video creation platform", descriptionZh: "基于浏览器的视频创作平台" }],
    skills: ["video production", "AI avatars", "corporate training", "multi-language content", "presentation"],
    pros: ["Professional avatar quality", "Multi-language support", "No filming needed", "Fast production"],
    prosZh: ["虚拟形象专业", "多语言支持", "无需拍摄", "制作快速"],
    cons: ["Expensive starting price", "Avatars can feel stiff", "Limited creative control", "Not for artistic video"],
    consZh: ["起价较高", "虚拟形象可能显僵硬", "创意控制有限", "不适合艺术性视频"],
    scene: "design-video",
  },
  {
    id: "invideo",
    name: "InVideo",
    description: "AI-powered video creation platform with templates for marketing and social media.",
    descriptionZh: "AI驱动的视频创作平台，提供营销和社交媒体模板。",
    category: "video-generation",
    tags: ["video", "templates", "marketing", "social-media"],
    difficulty: "beginner",
    url: "https://invideo.io",
    rating: 4,
    pricing: "Free tier / from $20/mo",
    useCase: "InVideo creates videos from text prompts with AI, offering 5000+ templates for social media, ads, and marketing.",
    icon: "\uD83C\uDFAC",
    company: "InVideo",
    companyZh: "InVideo",
    founded: "2017",
    headquarters: "San Francisco, CA",
    descriptionLong: "InVideo is an AI-powered video creation platform offering 5000+ templates for marketing and social media. It generates videos from text prompts with AI, provides stock media library, voiceovers, and team collaboration. The AI text-to-video feature creates complete videos from blog posts or articles. Popular among marketers and small businesses.",
    descriptionLongZh: "InVideo是一款AI视频创作平台，提供5000+模板，通过AI从文字提示生成视频。配备素材库、配音和团队协作功能。",
    advantages: ["5000+ customizable templates", "AI text-to-video", "Stock media library", "Team collaboration"],
    advantagesZh: ["5000+可定制模板", "AI文字转视频", "素材库", "团队协作"],
    useCases: ["Social media video ads", "YouTube intros", "Marketing videos", "Product promos", "Blog-to-video conversion"],
    useCasesZh: ["社交媒体视频广告", "YouTube片头", "营销视频", "产品推广", "博客转视频"],
    targetAudience: "Marketers and small business owners who want professional videos without video editing skills.",
    targetAudienceZh: "希望制作专业视频但无视频编辑技能的营销人员和小企业主。",
    pricingTiers: [
      { tier: "Free", tierZh: "免费版", price: "$0", features: ["Watermarked", "Limited templates"], featuresZh: ["含带水印", "有限模板"] },
    ],
    extensions: [{ name: "InVideo Web App", description: "Browser-based video creation", descriptionZh: "基于浏览器的视频创作" }],
    skills: ["video creation", "marketing video", "social media video", "template design", "content repurposing"],
    pros: ["Huge template library", "AI text-to-video works well", "Good for beginners", "Large stock media library"],
    prosZh: ["海量模板库", "AI文字转视频效果好", "适合初学者", "素材库丰富"],
    cons: ["Free exports watermarked", "Templates can look generic", "AI video quality varies", "Pro needed for full features"],
    consZh: ["免费版导出带水印", "模板可能显通用", "AI视频质量不稳定", "全功能需Pro版"],
    scene: "design-video",
  },
  {
    id: "pixlr",
    name: "Pixlr",
    description: "Free browser-based photo editor with AI-powered design tools and filters.",
    descriptionZh: "免费的基于浏览器的照片编辑器，具有AI驱动的设计工具和滤镜。",
    category: "image-generation",
    tags: ["photo-editing", "free", "browser", "design"],
    difficulty: "beginner",
    url: "https://pixlr.com",
    rating: 4,
    pricing: "Free / Premium from $1.99/mo",
    useCase: "Pixlr offers professional photo editing in the browser for free. AI tools include background removal, effect generation, and smart filters.",
    icon: "\uD83D\uDDBC\uFE0F",
    company: "Pixlr (Canva subsidiary)",
    companyZh: "Pixlr（Canva子公司）",
    founded: "2008",
    headquarters: "Stockholm, Sweden",
    descriptionLong: "Pixlr is a free browser-based photo editor with AI-powered design tools. It offers multiple editors including Pixlr X (quick) and Pixlr E (advanced). AI features include background removal, generative fill, AI effects, and smart filters. Completely free with optional premium for advanced features. No download needed, works entirely in browser.",
    descriptionLongZh: "Pixlr是一款免费的基于浏览器的照片编辑器，具有AI设计工具。提供快速版和专业版两种编辑器，完全免费使用。",
    advantages: ["Free in-browser editing", "AI background removal", "Generative fill AI", "No download needed"],
    advantagesZh: ["免费浏览器编辑", "AI背景移除", "AI生成填充", "无需下载"],
    useCases: ["Quick photo editing", "Social media graphics", "Background removal", "Photo retouching", "Collage creation"],
    useCasesZh: ["快速照片编辑", "社交媒体图形", "背景移除", "照片修饰", "拼贴创作"],
    targetAudience: "Anyone who needs free, quick photo editing without installing software.",
    targetAudienceZh: "任何需要免费、快速照片编辑又不想安装软件的人。",
    pricingTiers: [
      { tier: "Free", tierZh: "免费版", price: "$0", features: ["Basic editors", "AI tools limited"], featuresZh: ["基础编辑器", "AI工具有限"] },
    ],
    extensions: [{ name: "Pixlr Web App", description: "Browser-based photo editor", descriptionZh: "基于浏览器的照片编辑器" }],
    skills: ["photo editing", "graphic design", "image retouching", "collage", "social media graphics"],
    pros: ["Free for core features", "Works in browser", "AI tools included", "Low price for premium"],
    prosZh: ["核心功能免费", "浏览器运行", "包含AI工具", "高级版价格低廉"],
    cons: ["Not as powerful as Photoshop", "Ads on free version", "Requires internet", "AI features limited on free"],
    consZh: ["不如Photoshop强大", "免费版有广告", "需要联网", "免费版AI功能有限"],
    scene: "design-video",
  },

  // ====== Office Productivity (8) ======
  {
    id: "microsoft-copilot",
    name: "Microsoft Copilot",
    description: "AI assistant integrated across Microsoft 365 apps for work productivity.",
    descriptionZh: "集成在Microsoft 365应用中的AI助手，提升工作效率。",
    category: "productivity",
    tags: ["microsoft", "office", "productivity", "enterprise"],
    difficulty: "beginner",
    url: "https://copilot.microsoft.com",
    rating: 4,
    pricing: "Free / from $30/user/mo",
    useCase: "Microsoft Copilot assists with writing, analysis, and task automation across Word, Excel, Teams, and Outlook.",
    icon: "\uD83D\uDCBB",
    company: "Microsoft",
    companyZh: "微软",
    founded: "1975",
    headquarters: "Redmond, WA",
    descriptionLong: "Microsoft Copilot is an AI assistant integrated across Microsoft 365. It helps draft documents in Word, analyze data in Excel, summarize meetings in Teams, manage emails in Outlook, and create presentations in PowerPoint. Copilot Studio allows custom agent creation. Available as a free web version and premium integrated version for enterprise subscribers.",
    descriptionLongZh: "Microsoft Copilot是集成在Microsoft 365中的AI助手。帮助在Word中起草文档、Excel中分析数据、Teams中总结会议等。",
    advantages: ["Deep Microsoft 365 integration", "Data analysis in Excel", "Meeting summaries in Teams", "Copilot Studio for custom agents"],
    advantagesZh: ["深度Microsoft 365集成", "Excel数据分析", "Teams会议总结", "Copilot Studio自定义代理"],
    useCases: ["Drafting documents in Word", "Analyzing spreadsheets", "Summarizing Teams meetings", "Managing Outlook emails", "PowerPoint slide creation"],
    useCasesZh: ["Word文档起草", "电子表格分析", "Teams会议总结", "Outlook邮件管理", "PPT幻灯片创建"],
    targetAudience: "Microsoft 365 users who want AI assistance integrated into their existing work apps.",
    targetAudienceZh: "希望AI助手集成到现有工作应用中的Microsoft 365用户。",
    pricingTiers: [
      { tier: "Free", tierZh: "免费版", price: "$0", features: ["Web copilot", "Limited daily chats"], featuresZh: ["网页版Copilot", "每日聊天次数限制"] },
    ],
    extensions: [
      { name: "Copilot in Word", description: "AI writing assistant in Word", descriptionZh: "Word中的AI写作助手" },
      { name: "Copilot in Excel", description: "AI data analysis in Excel", descriptionZh: "Excel中的AI数据分析" },
    ],
    skills: ["office productivity", "document drafting", "data analysis", "meeting management", "email management"],
    pros: ["Deep Office integration", "Excel analysis powerful", "Teams summaries useful", "Enterprise ready"],
    prosZh: ["深度Office集成", "Excel分析强大", "Teams总结实用", "适合企业"],
    cons: ["Expensive per user", "Requires M365 subscription", "Limited free version", "Not standalone tool"],
    consZh: ["按用户价格较高", "需要M365订阅", "免费版功能有限", "非独立工具"],
    scene: "office-productivity",
  },
  {
    id: "otter-ai",
    name: "Otter.ai",
    description: "AI meeting assistant that records, transcribes, and summarizes meetings in real-time.",
    descriptionZh: "AI会议助手，实时录制、转录和总结会议内容。",
    category: "productivity",
    tags: ["meetings", "transcription", "notes", "collaboration"],
    difficulty: "beginner",
    url: "https://otter.ai",
    rating: 4,
    pricing: "Free / $16.99/mo Pro",
    useCase: "Otter.ai joins your meetings, transcribes everything in real-time, and generates summaries with action items.",
    icon: "\uD83D\uDCEB",
    company: "Otter.ai",
    companyZh: "Otter.ai",
    founded: "2016",
    headquarters: "Mountain View, CA",
    descriptionLong: "Otter.ai is an AI meeting assistant that records, transcribes, and summarizes meetings in real-time. It integrates with Zoom, Google Meet, and Microsoft Teams. Automatically captures slides, identifies speakers, generates action items, and creates searchable transcripts. Used by sales teams, journalists, and professionals who want to focus on conversations instead of note-taking.",
    descriptionLongZh: "Otter.ai是一款AI会议助手，实时录制、转录和总结会议。集成Zoom、Google Meet和Microsoft Teams。",
    advantages: ["Real-time meeting transcription", "Automatic speaker identification", "Meeting summary with action items", "Integrates with major video platforms"],
    advantagesZh: ["实时会议转录", "自动识别发言人", "会议总结和行动项", "集成主流视频平台"],
    useCases: ["Sales call transcription", "Team meeting notes", "Interview recording", "Lecture transcription", "Action item tracking"],
    useCasesZh: ["销售电话转录", "团队会议记录", "采访录音整理", "讲座转录", "行动项追踪"],
    targetAudience: "Professionals who attend many meetings and want automated notes without manual transcription.",
    targetAudienceZh: "参加大量会议、希望自动做记录的专业人士。",
    pricingTiers: [
      { tier: "Free", tierZh: "免费版", price: "$0", features: ["300 mins/month", "Basic transcription"], featuresZh: ["每月300分钟", "基础转录"] },
    ],
    extensions: [
      { name: "Otter for Zoom", description: "Zoom integration", descriptionZh: "Zoom集成" },
      { name: "Otter for Google Meet", description: "Google Meet integration", descriptionZh: "Google Meet集成" },
    ],
    skills: ["meeting notes", "transcription", "sales productivity", "interview recording", "collaboration"],
    pros: ["Excellent transcription accuracy", "Real-time during meetings", "Speaker identification", "Searchable transcripts"],
    prosZh: ["转录精度优秀", "会议中实时转录", "发言人识别", "可搜索的转录"],
    cons: ["Free limited minutes", "Pro expensive for individuals", "Only English well supported", "Can miss technical terms"],
    consZh: ["免费版分钟数有限", "个人Pro版较贵", "仅英语支持良好", "可能遗漏技术术语"],
    scene: "office-productivity",
  },
  {
    id: "fireflies-ai",
    name: "Fireflies.ai",
    description: "AI meeting assistant that records, transcribes, and analyzes conversations across platforms.",
    descriptionZh: "AI会议助手，跨平台录制、转录和分析对话。",
    category: "productivity",
    tags: ["meetings", "transcription", "analytics", "sales"],
    difficulty: "beginner",
    url: "https://fireflies.ai",
    rating: 4,
    pricing: "Free tier / from $10/mo",
    useCase: "Fireflies.ai records and transcribes meetings from Zoom, Teams, and Google Meet with searchable transcripts and analytics.",
    icon: "\uD83D\uDD25",
    company: "Fireflies.ai",
    companyZh: "Fireflies.ai",
    founded: "2019",
    headquarters: "San Francisco, CA",
    descriptionLong: "Fireflies.ai is an AI meeting assistant that records, transcribes, and analyzes meetings across Zoom, Teams, and Google Meet. It features searchable transcripts, automated meeting notes, sentiment analysis, action item tracking, and CRM integration. Includes AI-powered search across all past conversations. Popular with sales and recruiting teams for conversation intelligence.",
    descriptionLongZh: "Fireflies.ai是一款AI会议助手，跨Zoom、Teams和Google Meet录制、转录和分析会议。支持可搜索的转录和CRM集成。",
    advantages: ["Multi-platform meeting support", "Searchable transcript library", "Sentiment analysis", "CRM integration"],
    advantagesZh: ["多平台会议支持", "可搜索的转录库", "情感分析", "CRM集成"],
    useCases: ["Sales call analysis", "Meeting documentation", "Conversation intelligence", "Recruiting interviews", "Team collaboration"],
    useCasesZh: ["销售电话分析", "会议文档化", "对话智能分析", "招聘面试", "团队协作"],
    targetAudience: "Sales teams, recruiters, and managers who want conversation intelligence from their meetings.",
    targetAudienceZh: "希望从会议中获得对话智能的销售团队、招聘人员和管理者。",
    pricingTiers: [
      { tier: "Free", tierZh: "免费版", price: "$0", features: ["Limited transcription", "Public meetings"], featuresZh: ["有限转录", "公开会议"] },
    ],
    extensions: [
      { name: "Fireflies for Zoom", description: "Zoom bot", descriptionZh: "Zoom机器人" },
      { name: "Fireflies for Salesforce", description: "Salesforce integration", descriptionZh: "Salesforce集成" },
    ],
    skills: ["meeting transcription", "sales analytics", "conversation intelligence", "CRM workflows", "recruiting"],
    pros: ["Works with multiple platforms", "Strong search", "CRM integration useful", "Good analytics"],
    prosZh: ["支持多个平台", "搜索功能强大", "CRM集成实用", "分析功能好"],
    cons: ["Free tier limited", "Bot joins meeting (privacy)", "Accuracy varies by speaker", "Can miss context"],
    consZh: ["免费版功能有限", "机器人加入会议（隐私问题）", "准确性因发言者而异", "可能遗漏上下文"],
    scene: "office-productivity",
  },
  {
    id: "slides-ai",
    name: "SlidesAI",
    description: "AI presentation tool that creates slides from text in Google Slides.",
    descriptionZh: "AI演示工具，从文本在Google Slides中创建幻灯片。",
    category: "productivity",
    tags: ["presentation", "google-slides", "productivity", "ai"],
    difficulty: "beginner",
    url: "https://www.slidesai.io",
    rating: 4,
    pricing: "Free tier / from $10/mo",
    useCase: "SlidesAI creates professional presentations from text in Google Slides. Just type your content and AI designs the slides.",
    icon: "\uD83D\uDCCA",
    company: "SlidesAI",
    companyZh: "SlidesAI",
    founded: "2022",
    headquarters: "Prague, Czech Republic",
    descriptionLong: "SlidesAI is an AI presentation tool that creates professional slides from text directly in Google Slides. It offers multiple design themes, auto-layout, image suggestions, and formatting. No need to switch between apps -- works as a Google Slides add-on. Popular among educators, students, and business professionals for quick presentation creation.",
    descriptionLongZh: "SlidesAI是一款AI演示工具，直接在Google Slides中从文本创建专业幻灯片。支持多种设计主题和自动排版。",
    advantages: ["Works inside Google Slides", "Auto-layout from text", "Multiple design themes", "Fast presentation creation"],
    advantagesZh: ["在Google Slides内工作", "从文本自动排版", "多种设计主题", "快速创建演示文稿"],
    useCases: ["Quick presentation creation", "Educational slide decks", "Business proposals", "Lesson planning", "Conference talks"],
    useCasesZh: ["快速创建演示文稿", "教育幻灯片", "商业提案", "课程计划", "会议演讲"],
    targetAudience: "Google Slides users who want AI-powered presentation creation without leaving their workflow.",
    targetAudienceZh: "希望不离开工作流即可AI创建演示文稿的Google Slides用户。",
    pricingTiers: [
      { tier: "Free", tierZh: "免费版", price: "$0", features: ["Limited slides", "Basic themes"], featuresZh: ["有限幻灯片数", "基础主题"] },
    ],
    extensions: [{ name: "SlidesAI Google Workspace", description: "Google Slides add-on", descriptionZh: "Google Slides插件" }],
    skills: ["presentation design", "Google Slides", "content formatting", "visual design", "educational content"],
    pros: ["Google Slides integration", "Quick slide creation", "Clean designs", "Free tier usable"],
    prosZh: ["Google Slides集成", "快速创建幻灯片", "设计简洁", "免费版可用"],
    cons: ["Requires Google Slides", "Limited customization", "Themes can feel generic", "Less control than manual"],
    consZh: ["需要Google Slides", "自定义有限", "主题可能显通用", "不如手动灵活"],
    scene: "office-productivity",
  },
  {
    id: "tome",
    name: "Tome",
    description: "AI storytelling and presentation tool for creating narrative-driven content.",
    descriptionZh: "AI叙事和演示工具，用于创建故事驱动的内容。",
    category: "productivity",
    tags: ["presentation", "storytelling", "narrative", "design"],
    difficulty: "beginner",
    url: "https://tome.app",
    rating: 4,
    pricing: "Free tier / from $16/mo",
    useCase: "Tome creates narrative-driven presentations and documents with AI. It combines slides, video, and web content seamlessly.",
    icon: "\uD83D\uDCD6",
    company: "Tome",
    companyZh: "Tome",
    founded: "2020",
    headquarters: "San Francisco, CA",
    descriptionLong: "Tome is an AI storytelling and presentation tool for creating narrative-driven content. Unlike traditional slide tools, Tome combines slides, video, web embeds, and interactive content in a single canvas. AI generates complete presentations from prompts, with smart layouts and image suggestions. Used by product teams, educators, and storytellers.",
    descriptionLongZh: "Tome是一款AI叙事和演示工具，创建故事驱动的内容。不同于传统幻灯片工具，它在单一画布中融合幻灯片、视频和网页嵌入。",
    advantages: ["Narrative-focused design", "Multi-format canvas", "AI generation from prompts", "Embed web and video"],
    advantagesZh: ["以叙事为中心的设计", "多格式画布", "从提示生成内容", "嵌入网页和视频"],
    useCases: ["Product storytelling", "Pitch decks", "Educational content", "Portfolio presentations", "Project proposals"],
    useCasesZh: ["产品故事讲述", "融资路演", "教育内容", "作品集展示", "项目提案"],
    targetAudience: "Product managers, educators, and storytellers who want narrative-rich, multi-format presentations.",
    targetAudienceZh: "想要叙事丰富、多格式演示的产品经理、教育工作者和故事讲述者。",
    pricingTiers: [
      { tier: "Free", tierZh: "免费版", price: "$0", features: ["Limited presentations", "Basic AI"], featuresZh: ["有限演示文稿", "基础AI功能"] },
    ],
    extensions: [{ name: "Tome Web App", description: "Browser-based storytelling tool", descriptionZh: "基于浏览器的故事讲述工具" }],
    skills: ["presentation design", "storytelling", "visual communication", "product pitches", "educational content"],
    pros: ["Unique narrative format", "Multi-format canvas", "Good AI generation", "Great for pitches"],
    prosZh: ["独特的叙事格式", "多格式画布", "AI生成好", "适合路演"],
    cons: ["Not for data-heavy decks", "Expensive for individuals", "Limited export options", "Still maturing platform"],
    consZh: ["不适合数据密集的演示", "个人版较贵", "导出选项有限", "平台仍在完善"],
    scene: "office-productivity",
  },
  {
    id: "llamaindex",
    name: "LlamaIndex",
    description: "Data framework for building LLM applications with custom data ingestion and retrieval.",
    descriptionZh: "用于构建LLM应用的数据框架，支持自定义数据接入和检索。",
    category: "coding",
    tags: ["data-framework", "rag", "llm", "python"],
    difficulty: "advanced",
    url: "https://www.llamaindex.ai",
    rating: 4,
    pricing: "Free (open-source)",
    useCase: "LlamaIndex connects LLMs to your custom data sources. Build RAG systems, data agents, and knowledge assistants.",
    icon: "\uD83E\uDD99",
    company: "LlamaIndex",
    companyZh: "LlamaIndex",
    founded: "2023",
    headquarters: "San Francisco, CA",
    descriptionLong: "LlamaIndex is a data framework for building LLM applications with custom data ingestion and retrieval. It simplifies connecting LLMs to your data sources (PDFs, databases, APIs, websites) for RAG (retrieval-augmented generation). Features include data connectors, indexing strategies, query engines, and agent tools. Essential for production RAG systems.",
    descriptionLongZh: "LlamaIndex是一个用于构建LLM应用的数据框架，简化了将LLM连接到自定义数据源的过程。适用于生产级RAG系统。",
    advantages: ["Simple data ingestion", "Multiple indexing strategies", "RAG optimization", "Agent integration"],
    advantagesZh: ["简单的数据接入", "多种索引策略", "RAG优化", "代理集成"],
    useCases: ["RAG system building", "Document Q&A", "Data agent creation", "Knowledge base construction", "Enterprise search"],
    useCasesZh: ["RAG系统构建", "文档问答", "数据代理创建", "知识库构建", "企业搜索"],
    targetAudience: "Developers building RAG systems and data-intensive LLM applications who need structured data frameworks.",
    targetAudienceZh: "构建RAG系统和数据密集型LLM应用的开发者，需要结构化数据框架。",
    pricingTiers: [
      { tier: "Open Source", tierZh: "开源版", price: "$0", features: ["All framework features", "Self-hosted"], featuresZh: ["所有框架功能", "自行托管"] },
    ],
    extensions: [
      { name: "LlamaIndex Python", description: "Python framework package", descriptionZh: "Python框架包" },
      { name: "LlamaIndex TS", description: "TypeScript framework", descriptionZh: "TypeScript框架" },
    ],
    skills: ["RAG systems", "data engineering", "LLM development", "Python", "information retrieval"],
    pros: ["Excellent RAG support", "Flexible data connectors", "Active development", "Strong documentation"],
    prosZh: ["RAG支持出色", "灵活的数据连接器", "积极开发", "文档完善"],
    cons: ["Python heavy", "Learning curve", "Fast-changing API", "Debugging can be complex"],
    consZh: ["偏重Python", "学习曲线", "API变化快", "调试可能复杂"],
    scene: "development",
  },

  // ====== Development (8) ======
  {
    id: "tabnine",
    name: "Tabnine",
    description: "AI code completion tool that runs locally for privacy and supports multiple IDEs.",
    descriptionZh: "本地运行的AI代码补全工具，注重隐私，支持多种IDE。",
    category: "coding",
    tags: ["code-completion", "privacy", "local", "ide"],
    difficulty: "intermediate",
    url: "https://www.tabnine.com",
    rating: 4,
    pricing: "Free / $12/mo Pro",
    useCase: "Tabnine provides AI code completions that run on your local machine, keeping code private while boosting productivity.",
    icon: "\uD83D\uDD12",
    company: "Tabnine (Codota)",
    companyZh: "Tabnine（Codota）",
    founded: "2013",
    headquarters: "Tel Aviv, Israel",
    descriptionLong: "Tabnine is an AI code completion tool that runs locally for privacy and supports multiple IDEs including VS Code, JetBrains, and Vim. It offers whole-line and full-function completions based on your codebase context. The key differentiator is privacy -- models run on your machine, so code never leaves your environment. Pro tier offers team models trained on your codebase.",
    descriptionLongZh: "Tabnine是一款本地运行的AI代码补全工具，注重隐私，支持多种IDE。代码永远不会离开你的环境。",
    advantages: ["Local execution for privacy", "Multi-IDE support", "Codebase-aware completions", "No data sent to cloud"],
    advantagesZh: ["本地执行保护隐私", "多IDE支持", "代码库感知的补全", "数据不上云"],
    useCases: ["Privacy-sensitive coding", "Offline development", "Enterprise code completion", "Multi-language projects", "Team code consistency"],
    useCasesZh: ["隐私敏感编码", "离线开发", "企业代码补全", "多语言项目", "团队代码一致性"],
    targetAudience: "Developers and enterprises who need AI code completion with strong privacy guarantees.",
    targetAudienceZh: "需要AI代码补全且有强隐私保证的开发者及企业。",
    pricingTiers: [
      { tier: "Basic", tierZh: "基础版", price: "$0", features: ["Local completions", "Limited suggestions"], featuresZh: ["本地补全", "有限建议"] },
    ],
    extensions: [
      { name: "Tabnine for VS Code", description: "VS Code extension", descriptionZh: "VS Code扩展" },
      { name: "Tabnine for JetBrains", description: "JetBrains plugin", descriptionZh: "JetBrains插件" },
    ],
    skills: ["code completion", "software development", "privacy", "IDE usage", "multi-language development"],
    pros: ["Strong privacy", "Offline capable", "Works in many IDEs", "No data sharing"],
    prosZh: ["隐私保护强", "可离线使用", "支持多种IDE", "不分享数据"],
    cons: ["Less powerful than cloud AI", "Free tier limited", "Slower on large codebases", "Setup more complex"],
    consZh: ["不如云端AI强大", "免费版功能有限", "大代码库上较慢", "设置较复杂"],
    scene: "development",
  },
  {
    id: "codeium",
    name: "Codeium",
    description: "Free AI code completion and chat tool for developers, supporting 70+ languages.",
    descriptionZh: "面向开发者的免费AI代码补全和聊天工具，支持70多种语言。",
    category: "coding",
    tags: ["code-completion", "free", "chat", "multi-language"],
    difficulty: "intermediate",
    url: "https://codeium.com",
    rating: 4,
    pricing: "Free / $15/mo Pro",
    useCase: "Codeium offers free AI code completion and chat for developers with support for 70+ languages and 40+ IDEs.",
    icon: "\uD83D\uDCA1",
    company: "Codeium (Exafunction)",
    companyZh: "Codeium（Exafunction）",
    founded: "2022",
    headquarters: "Mountain View, CA",
    descriptionLong: "Codeium is a free AI code completion and chat tool for developers, supporting 70+ languages and 40+ IDEs. It offers fast code completions, AI chat for code questions, and code search across your codebase. Generous free tier with unlimited completions differentiates it from competitors. Pro tier adds priority support and higher limits.",
    descriptionLongZh: "Codeium是一款免费AI代码补全和聊天工具，支持70多种语言和40多种IDE。免费套餐慷慨，补全次数无限制。",
    advantages: ["Generous free tier", "70+ language support", "40+ IDE integrations", "AI chat for coding"],
    advantagesZh: ["慷慨的免费套餐", "支持70+语言", "40+IDE集成", "AI编程聊天"],
    useCases: ["Free code completion", "AI chat about code", "Multi-language development", "Codebase search", "Learning new languages"],
    useCasesZh: ["免费代码补全", "AI代码聊天", "多语言开发", "代码库搜索", "学习新语言"],
    targetAudience: "Developers who want free, fast AI code completion across many languages and IDEs.",
    targetAudienceZh: "希望跨多种语言和IDE获得免费、快速AI代码补全的开发者。",
    pricingTiers: [
      { tier: "Free", tierZh: "免费版", price: "$0", features: ["Unlimited completions", "AI chat"], featuresZh: ["Unlimited completions", "AI chat"] },
    ],
    extensions: [
      { name: "Codeium for VS Code", description: "VS Code extension", descriptionZh: "VS Code扩展" },
      { name: "Codeium for JetBrains", description: "JetBrains plugin", descriptionZh: "JetBrains插件" },
    ],
    skills: ["code completion", "software development", "AI chat", "multi-language", "productivity"],
    pros: ["Free with unlimited completions", "Good quality suggestions", "Fast responses", "Support for many IDEs"],
    prosZh: ["免费无限补全", "建议质量好", "响应快速", "支持众多IDE"],
    cons: ["Cloud-based (privacy concern)", "Less accurate on niche code", "Pro expensive vs free tier", "Brand less known"],
    consZh: ["基于云端（隐私考量）", "小众代码准确度较低", "Pro版价格对比免费版差距大", "品牌知名度较低"],
    scene: "development",
  },
  {
    id: "sourcegraph-cody",
    name: "Sourcegraph Cody",
    description: "AI coding assistant that understands your entire codebase for context-aware help.",
    descriptionZh: "理解整个代码库的AI编程助手，提供上下文感知的帮助。",
    category: "coding",
    tags: ["code-search", "context", "codebase", "enterprise"],
    difficulty: "intermediate",
    url: "https://sourcegraph.com/cody",
    rating: 4,
    pricing: "Free / $9/mo Pro",
    useCase: "Cody answers coding questions using your entire codebase as context. It understands project structure, dependencies, and conventions.",
    icon: "\uD83D\uDC0D",
    company: "Sourcegraph",
    companyZh: "Sourcegraph",
    founded: "2013",
    headquarters: "San Francisco, CA",
    descriptionLong: "Sourcegraph Cody is an AI coding assistant that understands your entire codebase. It uses Sourcegraph's code intelligence to provide context-aware answers, autocompletions, and code generation. Unlike tools limited to current file context, Cody understands your project structure, dependencies, and coding patterns. Excellent for onboarding to new codebases and large-scale refactoring.",
    descriptionLongZh: "Sourcegraph Cody是理解整个代码库的AI编程助手。使用Sourcegraph的代码智能提供上下文感知的答案和代码生成。",
    advantages: ["Full codebase context", "Code intelligence powered", "Project-aware answers", "Great for codebase onboarding"],
    advantagesZh: ["完整代码库上下文", "代码智能驱动", "项目感知的答案", "适合代码库入职"],
    useCases: ["New codebase onboarding", "Large-scale refactoring", "Code review assistance", "Bug investigation", "Dependency understanding"],
    useCasesZh: ["新代码库入职", "大规模重构", "代码审查辅助", "Bug调查", "依赖理解"],
    targetAudience: "Developers working with large codebases who need AI assistance with full project context.",
    targetAudienceZh: "处理大型代码库、需要完整项目上下文的AI辅助的开发者。",
    pricingTiers: [
      { tier: "Free", tierZh: "免费版", price: "$0", features: ["Limited requests", "Basic context"], featuresZh: ["有限请求", "基础上下文"] },
    ],
    extensions: [
      { name: "Cody for VS Code", description: "VS Code extension", descriptionZh: "VS Code扩展" },
      { name: "Cody for JetBrains", description: "JetBrains plugin", descriptionZh: "JetBrains插件" },
    ],
    skills: ["codebase understanding", "code search", "refactoring", "code review", "debugging"],
    pros: ["Understands full codebase", "Excellent for large projects", "Context-aware answers", "Good onboarding tool"],
    prosZh: ["理解完整代码库", "非常适合大型项目", "上下文感知的答案", "好的入职工具"],
    cons: ["Requires Sourcegraph setup", "Free tier limited", "Heavier than simple completions", "Pro features need subscription"],
    consZh: ["需要Sourcegraph设置", "免费版功能有限", "比简单补全更重", "Pro功能需订阅"],
    scene: "development",
  },
  {
    id: "warp",
    name: "Warp",
    description: "Modern AI-powered terminal with smart autocomplete and command generation.",
    descriptionZh: "现代化的AI驱动终端，具有智能自动补全和命令生成功能。",
    category: "coding",
    tags: ["terminal", "productivity", "ai", "command-line"],
    difficulty: "intermediate",
    url: "https://www.warp.dev",
    rating: 4,
    pricing: "Free / $12/mo Pro",
    useCase: "Warp is a Rust-based terminal with AI command search, smart autocomplete, and workflow automation.",
    icon: "\uD83D\uDCA8",
    company: "Warp",
    companyZh: "Warp",
    founded: "2020",
    headquarters: "New York, NY",
    descriptionLong: "Warp is a modern AI-powered terminal built in Rust with GPU-accelerated rendering. It features AI command search (type intent, get the command), smart autocomplete, workflow editor, and team sharing for commands. Unlike traditional terminals, Warp is editable like a text editor with mouse support, split panes, and persistent history. Available for macOS and Linux.",
    descriptionLongZh: "Warp是一个用Rust构建的现代化AI驱动终端，具有GPU加速渲染。支持AI命令搜索、智能自动补全和工作流编辑器。",
    advantages: ["AI command search", "Smart autocomplete", "GPU-accelerated rendering", "Workflow editor"],
    advantagesZh: ["AI命令搜索", "智能自动补全", "GPU加速渲染", "工作流编辑器"],
    useCases: ["Daily terminal use", "Complex command construction", "DevOps workflows", "Team command sharing", "Learning command line"],
    useCasesZh: ["日常终端使用", "复杂命令构建", "DevOps工作流", "团队命令共享", "学习命令行"],
    targetAudience: "Developers and DevOps professionals who spend significant time in the terminal.",
    targetAudienceZh: "经常在终端中工作的开发者和DevOps专业人士。",
    pricingTiers: [
      { tier: "Free", tierZh: "免费版", price: "$0", features: ["AI search limited", "Basic features"], featuresZh: ["AI搜索有限", "基础功能"] },
    ],
    extensions: [{ name: "Warp Desktop", description: "Native terminal app for macOS/Linux", descriptionZh: "macOS/Linux原生终端应用" }],
    skills: ["terminal usage", "command line", "DevOps", "developer productivity", "scripting"],
    pros: ["Beautiful modern UI", "AI command search helpful", "Fast GPU rendering", "Smart autocomplete"],
    prosZh: ["美观的现代UI", "AI命令搜索实用", "GPU渲染快速", "智能自动补全"],
    cons: ["macOS/Linux only (no Windows)", "Pro features behind paywall", "Can be resource heavy", "Learning new terminal paradigm"],
    consZh: ["仅支持macOS/Linux（无Windows）", "Pro功能需付费", "可能占用资源较多", "需要学习新的终端范式"],
    scene: "development",
  },
  {
    id: "replit-ghostwriter",
    name: "Replit Ghostwriter",
    description: "AI coding assistant built into the Replit browser IDE with real-time suggestions.",
    descriptionZh: "内置于Replit浏览器IDE的AI编程助手，提供实时建议。",
    category: "coding",
    tags: ["ide", "browser", "real-time", "learning"],
    difficulty: "beginner",
    url: "https://replit.com/ghostwriter",
    rating: 4,
    pricing: "Free / $20/mo Pro",
    useCase: "Ghostwriter provides real-time code suggestions, chat, and debugging within Replit's browser IDE.",
    icon: "\uD83D\uDC7B",
    company: "Replit",
    companyZh: "Replit",
    founded: "2016",
    headquarters: "San Francisco, CA",
    descriptionLong: "Replit Ghostwriter is an AI coding assistant built into the Replit browser IDE. It offers real-time code suggestions, AI chat for coding help, and debug assistance. Unlike other coding AI tools, Ghostwriter works entirely in the browser with no setup required. Particularly useful for beginners learning to code and collaborative coding in Replit's multi-player mode.",
    descriptionLongZh: "Replit Ghostwriter是内置于Replit浏览器IDE的AI编程助手。提供实时代码建议、AI聊天和调试辅助，完全在浏览器中工作。",
    advantages: ["Built into Replit IDE", "No setup required", "Real-time suggestions", "Great for learning"],
    advantagesZh: ["内置于Replit IDE", "无需设置", "实时建议", "适合学习"],
    useCases: ["Learning to code", "Browser-based development", "Collaborative coding", "Rapid prototyping", "Coding interviews"],
    useCasesZh: ["学习编程", "基于浏览器的开发", "协作编程", "快速原型", "编程面试"],
    targetAudience: "Beginner coders and anyone using Replit for browser-based development with AI assistance.",
    targetAudienceZh: "初学者编程者和任何在Replit上使用浏览器开发且需要AI辅助的人。",
    pricingTiers: [
      { tier: "Free", tierZh: "免费版", price: "$0", features: ["Limited suggestions", "Basic chat"], featuresZh: ["有限建议", "基础聊天"] },
    ],
    extensions: [{ name: "Replit Browser IDE", description: "Browser-based development environment", descriptionZh: "基于浏览器的开发环境" }],
    skills: ["web development", "learning to code", "browser IDE", "collaborative coding", "prototyping"],
    pros: ["No setup needed", "Beginner friendly", "Built-in deployment", "Collaborative features"],
    prosZh: ["无需设置", "新手友好", "内置部署", "协作功能"],
    cons: ["Limited to Replit platform", "Pro needed for full features", "Browser performance limits", "Less powerful than local IDEs"],
    consZh: ["限于Replit平台", "全功能需Pro版", "浏览器性能限制", "不如本地IDE强大"],
    scene: "development",
  },
  {
    id: "mintlify",
    name: "Mintlify",
    description: "AI-powered documentation platform that makes writing and maintaining docs easier.",
    descriptionZh: "AI驱动的文档平台，让编写和维护文档更轻松。",
    category: "coding",
    tags: ["documentation", "writing", "developer-tools", "api"],
    difficulty: "intermediate",
    url: "https://mintlify.com",
    rating: 4,
    pricing: "Free / from $150/mo",
    useCase: "Mintlify creates beautiful developer documentation with AI-powered search, writing assistance, and auto-generated API references.",
    icon: "\uD83D\uDCD6",
    company: "Mintlify",
    companyZh: "Mintlify",
    founded: "2021",
    headquarters: "San Francisco, CA",
    descriptionLong: "Mintlify is an AI-powered documentation platform for creating beautiful developer docs. It offers AI writing assistance, auto-generated API references from code, intelligent search, and analytics. Docs are written in markdown and Mintlify handles the design. Popular among startups and developer tools companies who want professional docs without a dedicated docs team.",
    descriptionLongZh: "Mintlify是一款AI驱动的文档平台，用于创建美观的开发者文档。支持AI写作辅助、自动生成API参考和智能搜索。",
    advantages: ["Beautiful default design", "AI writing assistance", "Auto API reference generation", "Intelligent search"],
    advantagesZh: ["美观的默认设计", "AI写作辅助", "自动API参考生成", "智能搜索"],
    useCases: ["Developer documentation", "API reference docs", "Knowledge base", "Product documentation", "Onboarding guides"],
    useCasesZh: ["开发者文档", "API参考文档", "知识库", "产品文档", "入门指南"],
    targetAudience: "Startups, developer tool companies, and tech teams who need professional documentation without a dedicated team.",
    targetAudienceZh: "需要专业文档但没有专门文档团队的初创公司、开发者工具公司和技术团队。",
    pricingTiers: [
      { tier: "Free", tierZh: "免费版", price: "$0", features: ["Public docs", "Basic features"], featuresZh: ["公开文档", "基础功能"] },
    ],
    extensions: [{ name: "Mintlify Web Platform", description: "Hosted documentation platform", descriptionZh: "托管的文档平台" }],
    skills: ["technical writing", "API documentation", "developer relations", "knowledge management", "product documentation"],
    pros: ["Beautiful output", "Easy to set up", "Great search", "Auto API refs"],
    prosZh: ["输出美观", "易于设置", "搜索功能好", "自动API引用"],
    cons: ["Pro pricing steep", "Limited customization", "Best for public docs", "Still maturing platform"],
    consZh: ["Pro版价格较高", "自定义有限", "最适合公开文档", "平台仍在完善"],
    scene: "development",
  },
  {
    id: "pieces",
    name: "Pieces",
    description: "AI developer productivity tool that captures, saves, and enriches code snippets.",
    descriptionZh: "AI开发者生产力工具，捕获、保存和丰富代码片段。",
    category: "coding",
    tags: ["snippets", "productivity", "knowledge", "workflow"],
    difficulty: "beginner",
    url: "https://pieces.app",
    rating: 4,
    pricing: "Free / $20/mo Pro",
    useCase: "Pieces captures code snippets automatically, enriches them with context, and makes them searchable with AI.",
    icon: "\uD83E\uDDE0",
    company: "Pieces",
    companyZh: "Pieces",
    founded: "2021",
    headquarters: "Cincinnati, OH",
    descriptionLong: "Pieces is an AI developer productivity tool that automatically captures code snippets, enriches them with context (screenshots, links, tags), and makes them searchable. It integrates with the browser and IDEs to capture and recall snippets without leaving your workflow. AI provides related information and documentation for saved snippets. On-device AI ensures privacy.",
    descriptionLongZh: "Pieces是一款AI开发者生产力工具，自动捕获代码片段，用上下文丰富它们，并使用AI使其可搜索。设备端AI确保隐私。",
    advantages: ["Automatic snippet capture", "AI enrichment and search", "IDE and browser integration", "On-device AI for privacy"],
    advantagesZh: ["自动捕获代码片段", "AI丰富和搜索", "IDE和浏览器集成", "设备端AI保护隐私"],
    useCases: ["Code snippet management", "Personal knowledge base", "Code reuse", "Learning and reference", "Context preservation"],
    useCasesZh: ["代码片段管理", "个人知识库", "代码复用", "学习和参考", "上下文保存"],
    targetAudience: "Developers who want to build a personal knowledge base of code snippets with AI-powered recall.",
    targetAudienceZh: "希望构建AI驱动的个人代码片段知识库的开发者。",
    pricingTiers: [
      { tier: "Free", tierZh: "免费版", price: "$0", features: ["Basic capture", "Limited storage"], featuresZh: ["基础捕获", "有限存储"] },
    ],
    extensions: [
      { name: "Pieces Desktop", description: "Desktop app for snippet management", descriptionZh: "代码片段管理桌面应用" },
      { name: "Pieces for VS Code", description: "VS Code extension", descriptionZh: "VS Code扩展" },
    ],
    skills: ["code organization", "knowledge management", "developer productivity", "snippet management", "workflow optimization"],
    pros: ["Automatic capture", "AI enrichment useful", "Works across tools", "Privacy focused"],
    prosZh: ["自动捕获", "AI丰富实用", "跨工具工作", "注重隐私"],
    cons: ["Free storage limited", "Pro needed for team", "Desktop app required", "Can be distracting"],
    consZh: ["免费版存储有限", "团队功能需Pro版", "需要桌面应用", "可能让人分心"],
    scene: "development",
  },
  {
    id: "phind",
    name: "Phind",
    description: "AI search engine for developers that answers technical questions with up-to-date information.",
    descriptionZh: "面向开发者的AI搜索引擎，用最新信息回答技术问题。",
    category: "coding",
    tags: ["search", "developer", "technical", "up-to-date"],
    difficulty: "beginner",
    url: "https://www.phind.com",
    rating: 4,
    pricing: "Free / $20/mo Pro",
    useCase: "Phind searches the web and generates answers for programming questions with code examples and source citations.",
    icon: "\uD83D\uDD0D",
    company: "Phind",
    companyZh: "Phind",
    founded: "2022",
    headquarters: "San Francisco, CA",
    descriptionLong: "Phind is an AI search engine built for developers that answers technical questions with up-to-date information. Unlike general search, Phind understands code context, can search the web in real-time, and provides answers with citations to source documentation and repositories. It features multi-step reasoning for complex questions and supports code snippet generation. Popular among developers for quick technical answers.",
    descriptionLongZh: "Phind是为开发者构建的AI搜索引擎，用最新信息回答技术问题。理解代码上下文，提供带引用的答案。",
    advantages: ["Code-aware search", "Real-time web information", "Source citations included", "Multi-step reasoning"],
    advantagesZh: ["感知代码的搜索", "实时网络信息", "包含来源引用", "多步推理"],
    useCases: ["Technical Q&A", "Code debugging help", "Documentation search", "Best practices research", "Library comparison"],
    useCasesZh: ["技术问答", "代码调试帮助", "文档搜索", "最佳实践研究", "库对比"],
    targetAudience: "Developers who need quick, accurate technical answers with up-to-date information and source citations.",
    targetAudienceZh: "需要快速准确的技术答案和最新信息及来源引用的开发者。",
    pricingTiers: [
      { tier: "Free", tierZh: "免费版", price: "$0", features: ["Limited searches", "Basic models"], featuresZh: ["有限搜索", "基础模型"] },
    ],
    extensions: [{ name: "Phind Web App", description: "Browser-based AI search", descriptionZh: "基于浏览器的AI搜索" }],
    skills: ["technical research", "debugging", "code search", "problem solving", "developer tools"],
    pros: ["Accurate technical answers", "Up-to-date information", "Code examples included", "Citations for verification"],
    prosZh: ["技术答案准确", "信息最新", "包含代码示例", "可验证的引用来源"],
    cons: ["Developer-focused only", "Free tier limited", "Less useful for non-code queries", "Pro expensive for casual use"],
    consZh: ["仅面向开发者", "免费版功能有限", "非代码查询用处不大", "随意使用Pro版较贵"],
    scene: "development",
  },

  // ====== Marketing (5) ======
  {
    id: "surferseo",
    name: "SurferSEO",
    description: "AI-powered SEO tool for content optimization, keyword research, and SERP analysis.",
    descriptionZh: "AI驱动的SEO工具，用于内容优化、关键词研究和SERP分析。",
    category: "productivity",
    tags: ["SEO", "content-optimization", "keyword-research", "marketing"],
    difficulty: "intermediate",
    url: "https://surferseo.com",
    rating: 4,
    pricing: "From $69/mo",
    useCase: "SurferSEO analyzes top-ranking pages and provides AI recommendations to optimize content for search engines.",
    icon: "\uD83C\uDF0A",
    company: "SurferSEO",
    companyZh: "SurferSEO",
    founded: "2018",
    headquarters: "Wroclaw, Poland",
    descriptionLong: "SurferSEO is an AI-powered SEO tool that optimizes content for search engines. It analyzes top-ranking pages to create data-driven content guidelines, recommends keyword usage, structure, and word count. Features include content editor with real-time optimization scoring, keyword research, and SERP analyzer. Integrates with Google Docs and WordPress. Essential for content teams focused on organic growth.",
    descriptionLongZh: "SurferSEO是一款AI驱动的SEO工具，通过分析排名靠前的页面来优化搜索内容。提供实时优化评分的内容编辑器。",
    advantages: ["Data-driven content guidelines", "Real-time optimization scoring", "SERP analysis", "Google Docs integration"],
    advantagesZh: ["数据驱动的内容指南", "实时优化评分", "SERP分析", "Google Docs集成"],
    useCases: ["Blog post optimization", "Keyword research", "Content strategy", "Competitor SERP analysis", "SEO content briefs"],
    useCasesZh: ["博客文章优化", "关键词研究", "内容策略", "竞争对手SERP分析", "SEO内容简报"],
    targetAudience: "SEO professionals and content teams who want data-driven optimization for organic search performance.",
    targetAudienceZh: "追求数据驱动优化的SEO专业人员和内容团队。",
    pricingTiers: [
      { tier: "Essential", tierZh: "基础版", price: "$69/mo", features: ["60 articles", "Basic analysis"], featuresZh: ["60篇文章", "基础分析"] },
    ],
    extensions: [
      { name: "Surfer SEO Chrome Extension", description: "SERP analyzer", descriptionZh: "SERP分析器" },
      { name: "Surfer Google Docs Add-on", description: "Content editor in Google Docs", descriptionZh: "Google Docs中的内容编辑器" },
    ],
    skills: ["SEO", "content optimization", "keyword research", "content strategy", "organic marketing"],
    pros: ["Data-driven suggestions", "Real-time content scoring", "SERP analysis valuable", "Integration ecosystem"],
    prosZh: ["数据驱动建议", "实时内容评分", "SERP分析有价值", "集成生态系统"],
    cons: ["Expensive starting price", "Overkill for small sites", "Can encourage keyword stuffing", "Learning curve"],
    consZh: ["起价较高", "小网站太大材小用", "可能鼓励关键词堆砌", "有学习曲线"],
    scene: "marketing",
  },
  {
    id: "frase-io",
    name: "Frase.io",
    description: "AI content optimization and research platform for SEO-driven content creation.",
    descriptionZh: "AI内容优化和研究平台，用于SEO驱动的内容创作。",
    category: "productivity",
    tags: ["SEO", "content", "research", "optimization"],
    difficulty: "intermediate",
    url: "https://www.frase.io",
    rating: 4,
    pricing: "From $14.99/mo",
    useCase: "Frase.io researches top SERP results and generates AI content briefs with optimized outlines and questions to answer.",
    icon: "\uD83D\uDD0D",
    company: "Frase.io",
    companyZh: "Frase.io",
    founded: "2018",
    headquarters: "Austin, TX",
    descriptionLong: "Frase.io is an AI content optimization platform for SEO-driven content creation. It researches top SERP results to generate content briefs with optimized outlines, relevant questions to answer, and keyword recommendations. Includes an AI writer that generates content based on briefs, content scoring, and optimization suggestions. More affordable than SurferSEO with similar core features.",
    descriptionLongZh: "Frase.io是AI内容优化平台，研究SERP结果以生成内容简报。比SurferSEO更实惠，核心功能类似。",
    advantages: ["SERP-driven content briefs", "AI content generation", "Question research from search", "More affordable than alternatives"],
    advantagesZh: ["SERP驱动的内容简报", "AI内容生成", "从搜索中提取问题", "比替代品更实惠"],
    useCases: ["Content brief generation", "SEO blog writing", "Topic research", "Content optimization", "Question-based content"],
    useCasesZh: ["内容简报生成", "SEO博客写作", "主题研究", "内容优化", "基于问题的内容"],
    targetAudience: "Content marketers and SEO professionals who want affordable AI-driven content optimization.",
    targetAudienceZh: "想要价格实惠的AI驱动内容优化的内容营销人员和SEO专业人士。",
    pricingTiers: [
      { tier: "Individual", tierZh: "个人版", price: "$14.99/mo", features: ["1 user", "30 articles/mo"], featuresZh: ["1个用户", "每月30篇文章"] },
    ],
    extensions: [
      { name: "Frase Chrome Extension", description: "SERP research tool", descriptionZh: "SERP研究工具" },
      { name: "Frase WordPress Plugin", description: "WordPress integration", descriptionZh: "WordPress集成" },
    ],
    skills: ["SEO", "content strategy", "topic research", "content writing", "keyword optimization"],
    pros: ["Affordable pricing", "Good SERP research", "AI content briefs useful", "Integrated writing tool"],
    prosZh: ["价格实惠", "SERP研究好", "AI内容简报实用", "集成写作工具"],
    cons: ["AI writing quality varies", "Less comprehensive than Surfer", "Limited customization", "Interface can be clunky"],
    consZh: ["AI写作质量不稳定", "不如Surfer全面", "自定义有限", "界面可能不够流畅"],
    scene: "marketing",
  },
  {
    id: "marketmuse",
    name: "MarketMuse",
    description: "Enterprise AI content planning and optimization platform for data-driven content strategy.",
    descriptionZh: "企业级AI内容规划和优化平台，用于数据驱动的内容策略。",
    category: "productivity",
    tags: ["enterprise", "content-strategy", "AI", "optimization"],
    difficulty: "advanced",
    url: "https://www.marketmuse.com",
    rating: 4,
    pricing: "Custom pricing",
    useCase: "MarketMuse uses AI to analyze content gaps, plan topics, and optimize existing content for authority and coverage.",
    icon: "\uD83C\uDFAF",
    company: "MarketMuse",
    companyZh: "MarketMuse",
    founded: "2014",
    headquarters: "Boston, MA",
    descriptionLong: "MarketMuse is an enterprise AI content planning and optimization platform. It analyzes your content against competitors to identify gaps, prioritize topics by potential impact, and optimize existing pages for authority. Features include content inventory audit, topic modeling, content brief generation, and optimization scoring. Used by enterprise content teams for strategic content planning at scale.",
    descriptionLongZh: "MarketMuse是企业级AI内容规划和优化平台。分析内容与竞争对手的差距，确定主题优先级，优化现有页面。",
    advantages: ["Content gap analysis", "Topic modeling and prioritization", "Enterprise-scale planning", "Authority scoring"],
    advantagesZh: ["内容差距分析", "主题建模和优先级排序", "企业级规划", "权威性评分"],
    useCases: ["Content strategy planning", "Competitive gap analysis", "Content inventory audit", "Topic cluster development", "Enterprise content optimization"],
    useCasesZh: ["内容策略规划", "竞争差距分析", "内容库存审计", "主题集群开发", "企业内容优化"],
    targetAudience: "Enterprise content teams and marketing departments who need data-driven content strategy at scale.",
    targetAudienceZh: "需要数据驱动内容策略的企业内容团队和营销部门。",
    pricingTiers: [
      { tier: "Enterprise", tierZh: "企业版", price: "Custom", features: ["Full platform", "Custom analysis", "Dedicated support"], featuresZh: ["完整平台", "自定义分析", "专属支持"] },
      ],
    extensions: [{ name: "MarketMuse Web Platform", description: "Enterprise content optimization", descriptionZh: "企业级内容优化" }],
    skills: ["content strategy", "SEO", "competitive analysis", "content planning", "topic modeling"],
    pros: ["Deep content analysis", "Strategic planning focus", "Enterprise grade", "Comprehensive audits"],
    prosZh: ["深度内容分析", "战略规划焦点", "企业级", "全面的审计"],
    cons: ["Expensive enterprise pricing", "Overkill for small teams", "Steep learning curve", "Implementation takes time"],
    consZh: ["企业定价昂贵", "小团队过大", "学习曲线陡峭", "实施需要时间"],
    scene: "marketing",
  },
  {
    id: "hubspot-ai",
    name: "HubSpot AI",
    description: "AI features integrated across HubSpot's CRM, marketing, sales, and service platforms.",
    descriptionZh: "集成在HubSpot的CRM、营销、销售和服务平台中的AI功能。",
    category: "productivity",
    tags: ["crm", "marketing", "sales", "automation"],
    difficulty: "intermediate",
    url: "https://www.hubspot.com/ai",
    rating: 4,
    pricing: "Free / from $50/mo",
    useCase: "HubSpot AI generates content, analyzes data, predicts deal outcomes, and automates workflows within HubSpot.",
    icon: "\uD83D\uDEE0\uFE0F",
    company: "HubSpot",
    companyZh: "HubSpot",
    founded: "2006",
    headquarters: "Cambridge, MA",
    descriptionLong: "HubSpot AI brings AI capabilities across HubSpot's CRM platform. Features include AI content assistant for emails and landing pages, predictive lead scoring, deal forecasting, chat assistant for customer service, and content remix for repurposing. Integrated directly into HubSpot workflows without needing separate AI tools. Popular among businesses already using HubSpot.",
    descriptionLongZh: "HubSpot AI将AI能力带到HubSpot CRM平台的各个方面。包括AI内容助手、预测性线索评分、交易预测等。",
    advantages: ["Integrated into HubSpot CRM", "AI content generation", "Predictive lead scoring", "Automated workflows"],
    advantagesZh: ["集成在HubSpot CRM中", "AI内容生成", "预测性线索评分", "自动化工作流"],
    useCases: ["Marketing content creation", "Sales email personalization", "Customer service chatbots", "Lead scoring automation", "Content repurposing"],
    useCasesZh: ["营销内容创作", "销售邮件个性化", "客服聊天机器人", "线索评分自动化", "内容再利用"],
    targetAudience: "HubSpot users who want AI capabilities integrated into their existing CRM and marketing workflows.",
    targetAudienceZh: "希望AI能力集成到现有CRM和营销工作流中的HubSpot用户。",
    pricingTiers: [
      { tier: "Free", tierZh: "免费版", price: "$0", features: ["Basic AI tools", "Limited content"], featuresZh: ["基础AI工具", "有限内容"] },
    ],
    extensions: [
      { name: "HubSpot Content Hub", description: "AI content platform", descriptionZh: "AI内容平台" },
      { name: "HubSpot Sales Hub", description: "Sales AI features", descriptionZh: "销售AI功能" },
    ],
    skills: ["CRM", "marketing automation", "sales enablement", "content marketing", "customer service"],
    pros: ["Deep HubSpot integration", "All-in-one platform", "Good for existing users", "Scalable"],
    prosZh: ["深度HubSpot集成", "一体化平台", "适合现有用户", "可扩展"],
    cons: ["Requires HubSpot subscription", "Can be expensive", "AI features limited without Pro", "Best for HubSpot ecosystem"],
    consZh: ["需要HubSpot订阅", "可能价格较高", "无Pro版AI功能有限", "最适合HubSpot生态系统"],
    scene: "marketing",
  },
  {
    id: "manychat",
    name: "ManyChat",
    description: "AI-powered chatbot platform for marketing automation on Messenger, Instagram, and WhatsApp.",
    descriptionZh: "AI驱动的聊天机器人平台，用于Messenger、Instagram和WhatsApp的营销自动化。",
    category: "productivity",
    tags: ["chatbot", "marketing", "automation", "social-media"],
    difficulty: "beginner",
    url: "https://manychat.com",
    rating: 4,
    pricing: "Free / from $15/mo",
    useCase: "ManyChat builds AI chatbots for Messenger, Instagram, and WhatsApp to automate marketing, sales, and support.",
    icon: "\uD83D\uDCAC",
    company: "ManyChat",
    companyZh: "ManyChat",
    founded: "2015",
    headquarters: "San Francisco, CA",
    descriptionLong: "ManyChat is an AI-powered chatbot platform for marketing automation on Messenger, Instagram, and WhatsApp. It offers visual flow builder, AI responses, broadcasting, and integration with 80+ tools including Shopify, Mailchimp, and HubSpot. Used for lead generation, customer support, and e-commerce automation. Beginner-friendly with drag-and-drop interface.",
    descriptionLongZh: "ManyChat是AI驱动的聊天机器人平台，用于Messenger、Instagram和WhatsApp的营销自动化。提供可视化流程构建器和AI回复。",
    advantages: ["Multi-platform chatbot support", "Visual flow builder", "AI-powered responses", "80+ tool integrations"],
    advantagesZh: ["多平台聊天机器人支持", "可视化流程构建器", "AI驱动的回复", "80+工具集成"],
    useCases: ["Lead generation automation", "Customer support chatbots", "E-commerce order updates", "Social media marketing", "FAQ automation"],
    useCasesZh: ["线索生成自动化", "客服聊天机器人", "电商订单更新", "社交媒体营销", "FAQ自动化"],
    targetAudience: "Marketers and business owners who want automated chatbot marketing on social messaging platforms.",
    targetAudienceZh: "希望在社交消息平台上实现聊天机器人自动化营销的营销人员和企业主。",
    pricingTiers: [
      { tier: "Free", tierZh: "免费版", price: "$0", features: ["1,000 contacts", "Basic features"], featuresZh: ["1000个联系人", "基础功能"] },
    ],
    extensions: [
      { name: "ManyChat for Messenger", description: "Facebook Messenger integration", descriptionZh: "Facebook Messenger集成" },
      { name: "ManyChat for Instagram", description: "Instagram DM integration", descriptionZh: "Instagram私信集成" },
    ],
    skills: ["chatbot marketing", "social media automation", "lead generation", "customer service", "e-commerce"],
    pros: ["Easy to set up", "Multi-platform", "Visual builder intuitive", "Good integrations"],
    prosZh: ["易于设置", "多平台", "可视化构建直观", "集成丰富"],
    cons: ["Free tier contacts limited", "Advanced features cost", "Platform rules change risk", "AI features limited on free"],
    consZh: ["免费版联系人限制", "高级功能需付费", "平台规则变化风险", "免费版AI功能有限"],
    scene: "marketing",
  },

  // ====== Free & Open Source (5) ======
  {
    id: "ollama",
    name: "Ollama",
    description: "Run open-source LLMs locally on your machine with a simple command-line interface.",
    descriptionZh: "在本地机器上运行开源LLM，配有简单的命令行界面。",
    category: "coding",
    tags: ["open-source", "local", "llm", "privacy"],
    difficulty: "intermediate",
    url: "https://ollama.ai",
    rating: 4,
    pricing: "Free (open-source)",
    useCase: "Ollama lets you download and run LLMs like Llama 3, Mistral, and Phi-3 on your own computer with one command.",
    icon: "\uD83E\uDD16",
    company: "Ollama",
    companyZh: "Ollama",
    founded: "2023",
    headquarters: "San Francisco, CA",
    descriptionLong: "Ollama is a free open-source tool that lets you run LLMs locally on your machine with a simple CLI. It supports Llama 3, Mistral, Phi-3, Gemma, Qwen, and 100+ other models. Download models with one command, run them via CLI or API, and integrate with apps. Completely free, private (everything runs locally), and no data leaves your computer. Essential for privacy-conscious AI users.",
    descriptionLongZh: "Ollama是一款免费开源工具，让你在本地机器上轻松运行LLM。支持Llama 3、Mistral、Phi-3等100多种模型。完全免费、保护隐私。",
    advantages: ["100% free and open-source", "100+ models available", "Runs completely locally", "Simple one-command setup"],
    advantagesZh: ["100%免费开源", "100多种模型", "完全本地运行", "一键安装使用"],
    useCases: ["Running LLMs privately", "Offline AI usage", "Model experimentation", "Local RAG systems", "Privacy-sensitive applications"],
    useCasesZh: ["私有运行LLM", "离线AI使用", "模型实验", "本地RAG系统", "隐私敏感应用"],
    targetAudience: "Privacy-conscious users, developers, and AI enthusiasts who want to run LLMs locally for free.",
    targetAudienceZh: "注重隐私的用户、开发者和AI爱好者，希望免费本地运行LLM。",
    pricingTiers: [
      { tier: "Open Source", tierZh: "开源版", price: "$0", features: ["All models", "Local only", "CLI + API"], featuresZh: ["所有模型", "仅本地运行", "命令行和API"] },
      ],
    extensions: [
      { name: "Ollama CLI", description: "Command-line tool", descriptionZh: "命令行工具" },
      { name: "Ollama Python Library", description: "Python API client", descriptionZh: "Python API客户端" },
    ],
    skills: ["local AI", "LLM deployment", "self-hosting", "privacy", "open-source tools"],
    pros: ["Completely free", "Full privacy", "Easy to use", "Large model library"],
    prosZh: ["完全免费", "完全隐私", "易于使用", "大量模型"],
    cons: ["Requires decent hardware", "Limited to smaller models", "No GUI by default", "Setup requires technical knowledge"],
    consZh: ["需要一定硬件配置", "限于较小模型", "默认无图形界面", "设置需技术知识"],
    scene: "free-open-source",
  },
  {
    id: "lm-studio",
    name: "LM Studio",
    description: "Desktop app for running and experimenting with local LLMs with a user-friendly GUI.",
    descriptionZh: "用于运行和实验本地LLM的桌面应用，配有用户友好的图形界面。",
    category: "learning",
    tags: ["local", "gui", "llm", "experiment"],
    difficulty: "intermediate",
    url: "https://lmstudio.ai",
    rating: 4,
    pricing: "Free (open-source)",
    useCase: "LM Studio provides a GUI for downloading, running, and experimenting with local LLMs on your computer.",
    icon: "\uD83D\uDDC2\uFE0F",
    company: "LM Studio",
    companyZh: "LM Studio",
    founded: "2023",
    headquarters: "San Francisco, CA",
    descriptionLong: "LM Studio is a free desktop app for running and experimenting with local LLMs. Unlike Ollama's CLI, LM Studio provides a polished GUI for model discovery, download, and inference. It supports models from Hugging Face, offers in-app chat, local API server, and model configuration (context length, GPU offloading). Available for Windows, Mac, and Linux. Best for users who prefer GUI over command line.",
    descriptionLongZh: "LM Studio是一款免费桌面应用，用于运行和实验本地LLM。提供精美的图形界面，不像Ollama只有命令行。支持Windows、Mac和Linux。",
    advantages: ["User-friendly GUI", "Built-in model browser", "Local API server", "GPU acceleration support"],
    advantagesZh: ["友好的图形界面", "内置模型浏览器", "本地API服务器", "GPU加速支持"],
    useCases: ["Local LLM experimentation", "Offline AI chat", "Model testing and evaluation", "Local API development", "Privacy-sensitive AI use"],
    useCasesZh: ["本地LLM实验", "离线AI聊天", "模型测试评估", "本地API开发", "隐私敏感AI使用"],
    targetAudience: "AI enthusiasts and developers who prefer a GUI for running local LLMs without command-line complexity.",
    targetAudienceZh: "喜欢用图形界面运行本地LLM而不想处理命令行的AI爱好者和开发者。",
    pricingTiers: [
      { tier: "Open Source", tierZh: "开源版", price: "$0", features: ["All features", "Local only", "GUI + API"], featuresZh: ["All features", "仅本地运行", "图形界面和API"] },
      ],
    extensions: [{ name: "LM Studio Desktop", description: "Desktop app for Windows/Mac/Linux", descriptionZh: "Windows/Mac/Linux桌面应用" }],
    skills: ["local AI", "LLM experimentation", "model evaluation", "self-hosting", "GUI tools"],
    pros: ["Beautiful GUI", "Free and open-source", "Easy model management", "Built-in chat"],
    prosZh: ["精美图形界面", "免费开源", "模型管理方便", "内置聊天"],
    cons: ["Requires decent hardware", "Limited to consumer GPUs", "Smaller model selection than Ollama", "Still in active development"],
    consZh: ["需要一定硬件", "限于消费级GPU", "模型选择少于Ollama", "仍在积极开发中"],
    scene: "free-open-source",
  },
  {
    id: "gpt4all",
    name: "GPT4All",
    description: "Free local AI assistant that runs on consumer hardware without internet or GPU.",
    descriptionZh: "在消费级硬件上运行的免费本地AI助手，无需联网或GPU。",
    category: "learning",
    tags: ["local", "free", "no-gpu", "privacy"],
    difficulty: "beginner",
    url: "https://gpt4all.io",
    rating: 4,
    pricing: "Free (open-source)",
    useCase: "GPT4All runs AI models locally on your CPU without needing internet or a GPU. Download and chat privately.",
    icon: "\uD83D\uDCA1",
    company: "Nomic AI",
    companyZh: "Nomic AI",
    founded: "2022",
    headquarters: "New York, NY",
    descriptionLong: "GPT4All is a free open-source local AI assistant that runs on consumer hardware without internet or a dedicated GPU. It runs entirely on CPU and is optimized for low-resource environments. The desktop app provides a chat interface with model download manager. Supports RAG with local documents and privacy-first offline operation. Best entry point for users new to local AI.",
    descriptionLongZh: "GPT4All是在消费级硬件上运行的免费开源本地AI助手，无需联网或GPU。完全在CPU上运行，是本地AI的最佳入门选择。",
    advantages: ["No GPU required", "Works offline completely", "CPU-only operation", "Private and local"],
    advantagesZh: ["无需GPU", "完全离线运行", "仅CPU运行", "隐私且本地"],
    useCases: ["Offline AI chat", "Privacy-sensitive conversations", "Document Q&A locally", "Learning about AI", "Basic task assistance"],
    useCasesZh: ["离线AI聊天", "隐私敏感对话", "本地文档问答", "了解AI", "基本任务辅助"],
    targetAudience: "Anyone who wants a free, private AI assistant that runs on their existing computer without special hardware.",
    targetAudienceZh: "任何想要免费、隐私的AI助手且无需特殊硬件的人。",
    pricingTiers: [
      { tier: "Open Source", tierZh: "开源版", price: "$0", features: ["All features", "Local CPU", "Offline"], featuresZh: ["All features", "本地CPU运行", "离线运行"] },
      ],
    extensions: [{ name: "GPT4All Desktop", description: "Desktop chat application", descriptionZh: "桌面聊天应用" }],
    skills: ["local AI", "offline AI", "privacy", "CPU inference", "document RAG"],
    pros: ["Works on any computer", "Completely free", "No GPU needed", "Private and offline"],
    prosZh: ["任何电脑可用", "完全免费", "无需GPU", "隐私离线"],
    cons: ["Slower than GPU models", "Limited to smaller models", "Less capable than cloud AI", "Basic chat interface"],
    consZh: ["比GPU模型慢", "限于较小模型", "不如云端AI强大", "聊天界面简单"],
    scene: "free-open-source",
  },
  {
    id: "open-interpreter",
    name: "Open Interpreter",
    description: "Open-source alternative to ChatGPT Code Interpreter that runs locally on your computer.",
    descriptionZh: "ChatGPT Code Interpreter的开源替代方案，在本地运行。",
    category: "coding",
    tags: ["open-source", "code-execution", "local", "automation"],
    difficulty: "advanced",
    url: "https://openinterpreter.com",
    rating: 4,
    pricing: "Free (open-source)",
    useCase: "Open Interpreter lets LLMs run code (Python, JavaScript, shell) locally to accomplish tasks on your computer.",
    icon: "\uD83D\uDCA1",
    company: "Open Interpreter (Community)",
    companyZh: "Open Interpreter（社区）",
    founded: "2023",
    headquarters: "Open Source",
    descriptionLong: "Open Interpreter is an open-source alternative to ChatGPT Code Interpreter that runs locally. It gives LLMs the ability to run code (Python, JavaScript, shell, etc.) on your computer to accomplish tasks like data analysis, file manipulation, web research, and system automation. Unlike ChatGPT's cloud-based version, Open Interpreter runs completely locally with full access to your system.",
    descriptionLongZh: "Open Interpreter是ChatGPT Code Interpreter的开源替代方案，在本地运行。允许LLM在你的电脑上执行代码完成各种任务。",
    advantages: ["Full local code execution", "Open-source and free", "Unlimited capabilities", "System-level access"],
    advantagesZh: ["完整本地代码执行", "开源免费", "能力无限制", "系统级访问"],
    useCases: ["Local data analysis", "File system automation", "Web scraping locally", "Custom script generation", "System administration"],
    useCasesZh: ["本地数据分析", "文件系统自动化", "本地网页爬取", "自定义脚本生成", "系统管理"],
    targetAudience: "Power users and developers who want local, unrestricted AI-powered code execution and system automation.",
    targetAudienceZh: "希望本地、无限制的AI驱动代码执行和系统自动化的高级用户和开发者。",
    pricingTiers: [
      { tier: "Open Source", tierZh: "开源版", price: "$0", features: ["All features", "Local only", "Self-hosted"], featuresZh: ["All features", "仅本地运行", "自行托管"] },
      ],
    extensions: [{ name: "Open Interpreter CLI", description: "Command-line tool", descriptionZh: "命令行工具" }],
    skills: ["automation", "code execution", "data analysis", "system administration", "Python"],
    pros: ["Completely free", "Unlimited capability", "Full system access", "Active community"],
    prosZh: ["完全免费", "能力无限制", "完整系统访问", "活跃社区"],
    cons: ["Powerful = dangerous", "Requires technical skill", "Can break things", "Setup complexity"],
    consZh: ["强大=有风险", "需要技术技能", "可能损坏系统", "设置复杂"],
    scene: "free-open-source",
  },
  {
    id: "librechat",
    name: "LibreChat",
    description: "Open-source chat platform that connects to multiple AI models in one interface.",
    descriptionZh: "开源聊天平台，在一个界面中连接多种AI模型。",
    category: "chatbots",
    tags: ["open-source", "multi-model", "chat", "self-hosted"],
    difficulty: "intermediate",
    url: "https://librechat.com",
    rating: 4,
    pricing: "Free (open-source)",
    useCase: "LibreChat provides a unified chat interface for OpenAI, Anthropic, Google, and local models -- all in one place.",
    icon: "\uD83D\uDCE2",
    company: "LibreChat (Community)",
    companyZh: "LibreChat（社区）",
    founded: "2023",
    headquarters: "Open Source",
    descriptionLong: "LibreChat is an open-source chat platform that connects to multiple AI model providers in one interface. It supports OpenAI (GPT-4o, GPT-5), Anthropic (Claude), Google (Gemini), and local models via Ollama. Features include conversation branching, custom presets, multi-model responses, plugins, and file uploads. Self-hosted for privacy and data control. Used extensively by developers and AI enthusiasts.",
    descriptionLongZh: "LibreChat是开源聊天平台，在一个界面中连接多个AI模型提供商。支持OpenAI、Anthropic、Google和本地模型。可自行托管的聊天界面。",
    advantages: ["Multi-provider support", "Self-hosted privacy", "Conversation branching", "Custom presets"],
    advantagesZh: ["多提供商支持", "自托管隐私", "对话分支", "自定义预设"],
    useCases: ["Using multiple AI models", "Model comparison testing", "Private AI chat", "Custom AI workflows", "Team AI tools"],
    useCasesZh: ["使用多个AI模型", "模型对比测试", "私有AI聊天", "自定义AI工作流", "团队AI工具"],
    targetAudience: "AI enthusiasts and developers who want a single, self-hosted interface for multiple AI models with privacy.",
    targetAudienceZh: "想要一个可自托管的单一界面来使用多种AI模型并保护隐私的AI爱好者和开发者。",
    pricingTiers: [
      { tier: "Open Source", tierZh: "开源版", price: "$0", features: ["All features", "Self-hosted", "Multi-provider"], featuresZh: ["All features", "自行托管", "多提供商支持"] },
      ],
    extensions: [{ name: "LibreChat Web App", description: "Self-hosted chat platform", descriptionZh: "自托管聊天平台" }],
    skills: ["multi-model AI", "self-hosting", "chat interfaces", "AI comparison", "privacy"],
    pros: ["Multi-model in one UI", "Self-hosted privacy", "Free and open-source", "Active development"],
    prosZh: ["多模型统一界面", "自托管隐私", "免费开源", "积极开发"],
    cons: ["Requires self-hosting", "Setup can be complex", "API keys needed for providers", "UI less polished than ChatGPT"],
    consZh: ["需要自行托管", "设置可能复杂", "需要各提供商API密钥", "界面不如ChatGPT精致"],
    scene: "free-open-source",
  },

  {
    id: "ideogram",
    name: "Ideogram",
    description: "AI image generation tool with exceptional text rendering and logo design capabilities.",
    descriptionZh: "AI图像生成工具，具有出色的文字渲染和标志设计能力。",
    category: "image-generation",
    tags: ["image-generation", "logo", "typography", "design", "text-rendering"],
    difficulty: "beginner",
    url: "https://ideogram.ai",
    rating: 4,
    pricing: "Free tier / from $20/mo",
    useCase: "Ideogram generates images with accurate text rendering, making it ideal for logos, posters, and branded visuals.",
    icon: "\uD83C\uDFA8",
    company: "Ideogram AI",
    companyZh: "Ideogram AI",
    founded: "2022",
    headquarters: "Toronto, Canada",
    descriptionLong: "Ideogram is an AI image generation tool that excels at rendering text within images -- a known weakness of other AI image models. It produces high-quality logos, posters, social media graphics, and branded visuals with accurate typography. Features include magic prompt for prompt optimization, image upscaling, and style presets. Popular among designers and marketers for text-heavy visual content.",
    descriptionLongZh: "Ideogram是一款AI图像生成工具，擅长在图像中渲染文字。可生成高质量标志、海报和品牌视觉内容。",
    advantages: ["Best-in-class text rendering in images", "Logo and typography focus", "Magic prompt optimization", "Style presets and upscaling"],
    advantagesZh: ["图像中文字渲染行业领先", "专注标志和字体设计", "智能提示优化", "风格预设和放大"],
    useCases: ["Logo design and branding", "Poster and flyer creation", "Social media graphics with text", "Product mockups with labels", "Presentation visuals"],
    useCasesZh: ["标志设计和品牌推广", "海报和传单制作", "带文字的社交媒体图形", "带标签的产品样机", "演示文稿视觉"],
    targetAudience: "Designers, marketers, and brand managers who need AI-generated images with accurate text rendering.",
    targetAudienceZh: "需要AI生成图像且文字渲染准确的设计师、营销人员和品牌经理。",
    pricingTiers: [
      { tier: "Free", tierZh: "免费版", price: "$0", features: ["Limited generations", "Basic features"], featuresZh: ["有限生成次数", "基础功能"] },
    ],
    extensions: [{ name: "Ideogram Web App", description: "Browser-based image generation", descriptionZh: "基于浏览器的图像生成" }],
    skills: ["image generation", "logo design", "typography", "graphic design", "branding"],
    pros: ["Best text rendering in AI images", "Great for logos", "Easy to use", "High quality output"],
    prosZh: ["AI图像中文字渲染最佳", "非常适合标志设计", "易于使用", "输出质量高"],
    cons: ["Less versatile than Midjourney", "Smaller community", "Free tier limited", "Fewer style options"],
    consZh: ["不如Midjourney多功能", "社区较小", "免费版有限", "风格选项较少"],
    scene: "design-video",
  },
  {
    id: "podcastle",
    name: "Podcastle",
    description: "AI-powered podcast creation platform with recording, editing, and publishing tools.",
    descriptionZh: "AI驱动的播客创作平台，包含录制、编辑和发布工具。",
    category: "audio",
    tags: ["podcasting", "audio", "recording", "editing"],
    difficulty: "beginner",
    url: "https://podcastle.ai",
    rating: 4,
    pricing: "Free tier / from $11.99/mo",
    useCase: "Podcastle provides AI-powered recording, editing, and publishing tools for podcasters of all levels.",
    icon: "\uD83C\uDF99\uFE0F",
    company: "Podcastle",
    companyZh: "Podcastle",
    founded: "2020",
    headquarters: "Yerevan, Armenia",
    descriptionLong: "Podcastle is an AI-powered podcast creation platform offering recording, editing, and publishing in one place. Features include Magic Dust for one-click audio cleanup, silence removal, background noise reduction, AI voice cloning, remote guest recording with separate tracks, and direct publishing to major platforms. The Revoice feature lets you fix mistakes by typing instead of re-recording. Good for solo podcasters and production teams.",
    descriptionLongZh: "Podcastle是一款AI驱动的播客创作平台，集录制、编辑和发布于一体。支持一键音频清理、远程嘉宾录制和AI语音克隆。",
    advantages: ["All-in-one podcast platform", "Magic Dust one-click audio cleanup", "Remote guest recording", "AI voice cloning (Revoice)"],
    advantagesZh: ["一站式播客平台", "一键音频清理", "远程嘉宾录制", "AI语音克隆"],
    useCases: ["Podcast recording and editing", "Remote interview production", "Audio cleanup and enhancement", "AI voiceover creation", "Multi-track podcast production"],
    useCasesZh: ["播客录制和编辑", "远程采访制作", "音频清理和增强", "AI配音创作", "多轨播客制作"],
    targetAudience: "Podcasters and audio content creators who want an all-in-one platform for recording, editing, and publishing.",
    targetAudienceZh: "想要一站式录制、编辑和发布平台的播客制作者和音频内容创作者。",
    pricingTiers: [
      { tier: "Free", tierZh: "免费版", price: "$0", features: ["Basic recording", "Audio cleanup"], featuresZh: ["基础录制", "音频清理"] },
    ],
    extensions: [{ name: "Podcastle Web App", description: "Browser-based podcast studio", descriptionZh: "基于浏览器的播客工作室" }],
    skills: ["podcasting", "audio editing", "audio production", "voice recording", "content creation"],
    pros: ["All-in-one platform", "Magic Dust cleanup impressive", "Remote recording good quality", "Revoice saves re-recording"],
    prosZh: ["一站式平台", "音频清理效果出色", "远程录制质量好", "Revoice免去重新录制"],
    cons: ["Free tier limited", "Advanced editing less powerful", "Revoice quality varies", "Newer platform"],
    consZh: ["免费版限制多", "高级编辑不如专业DAW", "语音克隆质量不一", "较新的平台"],
    scene: "content-creation",
  },
] as Tool[];