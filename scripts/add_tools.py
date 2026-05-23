import re

tools_path = r"C:\Users\jun\aistudyonline-next\src\lib\tools.ts"

with open(tools_path, 'r', encoding='utf-8') as f:
    content = f.read()

tool_entries = r"""
{
    id: "deer-flow",
    name: "Deer-Flow",
    description: "AI-powered research assistant that autonomously gathers web data, analyzes trends, and generates comprehensive reports from plain-language commands.",
    descriptionZh: "AI驱动的研究助手，可自主收集网络数据、分析趋势并根据自然语言指令生成综合报告。",
    category: "productivity",
    tags: ["research", "data", "web-scraping", "report", "automation"],
    difficulty: "beginner",
    url: "https://github.com/openclaw/DeerFlow",
    rating: r(4.6),
    pricing: "Free (open source)",
    useCase: "Deer-Flow is an AI-powered research assistant that autonomously gathers web data and generates comprehensive reports from plain-language commands.",
    icon: "\u{1F98C}",
    company: "OpenClaw",
    companyZh: "OpenClaw",
    founded: "2025",
    headquarters: "Community",
    descriptionLong: "Deer-Flow is an AI-powered research assistant that transforms how you gather market intelligence. Simply describe what you need in plain language, and Deer-Flow autonomously scours the web, collects relevant data, analyzes trends, and generates comprehensive reports. With 65,800+ GitHub stars, it is one of the most popular open-source research automation tools available. Whether you need competitive analysis, market trend reports, or customer insights, Deer-Flow handles the entire research pipeline end-to-end — search, gather, analyze, and present — letting you focus on strategic decisions rather than manual data collection.",
    descriptionLongZh: "Deer-Flow是一款AI驱动的研究助手，改变您收集市场情报的方式。只需用自然语言描述需求，Deer-Flow就会自主搜索网络、收集相关数据、分析趋势并生成综合报告。拥有65,800+ GitHub星标，是最受欢迎的开源研究自动化工具之一。无论您需要竞争分析、市场趋势报告还是客户洞察，Deer-Flow都能端到端处理整个研究流程——搜索、收集、分析和呈现——让您专注于战略决策而非手动数据收集。",
    targetAudience: "Entrepreneurs, marketers, and researchers who need automated market intelligence and data gathering without manual effort.",
    targetAudienceZh: "需要自动市场情报和数据收集的企业家、营销人员和研究人员。",
    scene: "office-productivity",
    advantages: [
      "Autonomous web research",
      "Comprehensive report generation",
      "Trend analysis",
      "Open source and free",
      "Plain-language commands"
    ],
    advantagesZh: [
      "自主网络研究",
      "综合报告生成",
      "趋势分析",
      "开源免费",
      "自然语言指令"
    ],
    useCases: [
      "Market research and competitive analysis",
      "Trend monitoring and reporting",
      "Customer insight gathering",
      "Industry news aggregation",
      "Data-driven strategy planning"
    ],
    useCasesZh: [
      "市场研究与竞争分析",
      "趋势监控与报告",
      "客户洞察收集",
      "行业新闻聚合",
      "数据驱动战略规划"
    ],
    skills: [
      "research",
      "web scraping",
      "data analysis",
      "reporting",
      "automation"
    ],
    pros: [
      "Fully autonomous research pipeline",
      "High-quality comprehensive reports",
      "Massive community (65K+ stars)",
      "Completely free and open-source",
      "Saves hours of manual research"
    ],
    prosZh: [
      "全自动研究流程",
      "高质量综合报告",
      "庞大社区（65K+星标）",
      "完全免费开源",
      "节省数小时手动研究时间"
    ],
    cons: [
      "Requires API keys for LLM backend",
      "Report quality depends on source data",
      "No built-in data visualization",
      "Setup requires basic technical knowledge"
    ],
    consZh: [
      "需要LLM后端的API密钥",
      "报告质量取决于源数据",
      "无内置数据可视化",
      "设置需要基本技术知识"
    ],
    pricingTiers: [
      {
        tier: "Free",
        tierZh: "免费版",
        price: "$0",
        features: ["All features", "Open-source", "Self-hosted"],
        featuresZh: ["全部功能", "开源", "自托管"],
      },
    ],
    extensions: [
      {
        name: "DeerFlow GitHub",
        description: "Official open-source repository",
        descriptionZh: "官方开源仓库",
      },
    ],
  },

{
    id: "prompt-optimizer",
    name: "Prompt Optimizer",
    description: "Translates plain-language requests into detailed, professional AI prompts. Bridge the gap between what you mean and what AI understands.",
    descriptionZh: "将自然语言请求转化为详细专业的AI提示词。弥合你所想与AI所理解之间的差距。",
    category: "writing",
    tags: ["prompt-engineering", "writing", "ai-optimization", "productivity", "creative"],
    difficulty: "beginner",
    url: "https://github.com/openclaw/PromptOptimizer",
    rating: r(4.4),
    pricing: "Free (open source)",
    useCase: "Prompt Optimizer translates plain-language requests into detailed, professional AI prompts for better results from any AI tool.",
    icon: "\u{1F3AF}",
    company: "OpenClaw",
    companyZh: "OpenClaw",
    founded: "2025",
    headquarters: "Community",
    descriptionLong: "Prompt Optimizer bridges the gap between what you mean and what AI understands. Instead of struggling to craft the perfect prompt, simply describe what you want in plain language — and Prompt Optimizer transforms it into a structured, professional-grade AI instruction. With 28,300+ GitHub stars, it helps users get dramatically better results from ChatGPT, Claude, Gemini, and other AI tools. Features include automatic context enrichment, format optimization, role assignment, constraint injection, and multi-turn conversation structuring — all from a single plain-language sentence.",
    descriptionLongZh: "Prompt Optimizer弥合了你所想与AI所理解之间的差距。无需绞尽脑汁编写完美提示词，只需用自然语言描述需求——Prompt Optimizer会将其转化为结构化、专业级的AI指令。拥有28,300+ GitHub星标，帮助用户从ChatGPT、Claude、Gemini等AI工具中获得显著更好的结果。功能包括自动上下文丰富、格式优化、角色分配、约束注入和多轮对话结构化——全部来自一句自然语言。",
    targetAudience: "Content creators, marketers, and anyone who wants better results from AI tools without learning prompt engineering.",
    targetAudienceZh: "内容创作者、营销人员以及任何希望在不学习提示工程的情况下从AI工具获得更好结果的用户。",
    scene: "content-creation",
    advantages: [
      "Plain-language to professional prompts",
      "28K+ GitHub stars",
      "Works with any AI tool",
      "Automatic context enrichment",
      "Beginner-friendly"
    ],
    advantagesZh: [
      "自然语言转专业提示词",
      "28K+ GitHub星标",
      "兼容任何AI工具",
      "自动上下文丰富",
      "初学者友好"
    ],
    useCases: [
      "Content creation and copywriting",
      "Marketing campaign generation",
      "Technical documentation writing",
      "Creative writing and storytelling",
      "Business communication drafting"
    ],
    useCasesZh: [
      "内容创作与文案写作",
      "营销活动生成",
      "技术文档编写",
      "创意写作与故事叙述",
      "商务沟通起草"
    ],
    skills: [
      "prompt engineering",
      "writing",
      "optimization",
      "AI communication",
      "content creation"
    ],
    pros: [
      "Eliminates prompt guesswork",
      "Consistent high-quality outputs",
      "Works across all major AI platforms",
      "Active open-source community",
      "Low learning curve"
    ],
    prosZh: [
      "消除提示词试错",
      "一致的输出质量",
      "兼容所有主流AI平台",
      "活跃的开源社区",
      "低学习曲线"
    ],
    cons: [
      "Requires API key for LLM backend",
      "Output quality varies by target model",
      "No offline mode",
      "Limited customization of output formats"
    ],
    consZh: [
      "需要LLM后端的API密钥",
      "输出质量因目标模型而异",
      "无离线模式",
      "输出格式定制有限"
    ],
    pricingTiers: [
      {
        tier: "Free",
        tierZh: "免费版",
        price: "$0",
        features: ["All features", "Open-source", "Self-hosted"],
        featuresZh: ["全部功能", "开源", "自托管"],
      },
    ],
    extensions: [
      {
        name: "PromptOptimizer GitHub",
        description: "Official open-source repository",
        descriptionZh: "官方开源仓库",
      },
    ],
  },

{
    id: "openagents",
    name: "Agents",
    description: "A team of 80+ specialized AI agents for SEO, frontend, data analysis, marketing, and more. Deploy virtual employees for every business function.",
    descriptionZh: "由80多个专业AI代理组成的团队，涵盖SEO、前端、数据分析、营销等领域。为每个业务功能部署虚拟员工。",
    category: "coding",
    tags: ["agents", "automation", "seo", "frontend", "data-analysis", "marketing"],
    difficulty: "intermediate",
    url: "https://github.com/openclaw/agents",
    rating: r(4.5),
    pricing: "Free (open source)",
    useCase: "Agents provides 80+ specialized AI agents for SEO, frontend development, data analysis, marketing, and more - deploy virtual employees for every business function.",
    icon: "\u{1F916}",
    company: "OpenClaw",
    companyZh: "OpenClaw",
    founded: "2025",
    headquarters: "Community",
    descriptionLong: "Agents is an open-source platform that provides a team of 80+ specialized AI agents, each trained for specific business functions. From SEO optimization and frontend development to data analysis and marketing campaigns, you can deploy virtual AI employees that work autonomously on your projects. With 34,900+ GitHub stars, it is one of the most comprehensive multi-agent systems available. Each agent specializes in its domain - SEO experts analyze and optimize websites, frontend engineers fix bugs and build features, data analysts process user behavior, and marketing experts plan campaigns - all working together under your direction.",
    descriptionLongZh: "Agents是一个开源平台，提供由80多个专业AI代理组成的团队，每个代理针对特定业务功能进行训练。从SEO优化和前端开发到数据分析和营销活动，您可以部署自主工作的虚拟AI员工。拥有34,900+ GitHub星标，是最全面的多代理系统之一。每个代理专注于其领域——SEO专家分析和优化网站、前端工程师修复bug和构建功能、数据分析师处理用户行为、营销专家规划活动——都在您的指导下协同工作。",
    targetAudience: "Developers and business owners who want to automate multiple business functions with specialized AI agents.",
    targetAudienceZh: "希望通过专业AI代理自动化多个业务功能的开发者和企业主。",
    scene: "development",
    advantages: [
      "80+ specialized AI agents",
      "Multi-domain coverage",
      "Autonomous task execution",
      "Open source and free",
      "Collaborative agent ecosystem"
    ],
    advantagesZh: [
      "80多个专业AI代理",
      "多领域覆盖",
      "自主任务执行",
      "开源免费",
      "协作代理生态系统"
    ],
    useCases: [
      "SEO audit and optimization",
      "Frontend development and bug fixing",
      "Data analysis and reporting",
      "Marketing campaign planning",
      "Content strategy and creation"
    ],
    useCasesZh: [
      "SEO审计和优化",
      "前端开发和bug修复",
      "数据分析和报告",
      "营销活动规划",
      "内容策略与创建"
    ],
    skills: [
      "multi-agent",
      "automation",
      "SEO",
      "development",
      "marketing"
    ],
    pros: [
      "Massive agent variety (80+)",
      "Covers virtually all business functions",
      "Autonomous and collaborative",
      "Active 34K+ star community",
      "No per-agent licensing fees"
    ],
    prosZh: [
      "海量代理种类（80+）",
      "覆盖几乎所有业务功能",
      "自主协作",
      "活跃的34K+星标社区",
      "无按代理许可费"
    ],
    cons: [
      "Requires technical setup",
      "Agent quality varies by domain",
      "Resource-intensive for many agents",
      "Needs LLM API keys"
    ],
    consZh: [
      "需要技术设置",
      "代理质量因领域而异",
      "多代理时资源消耗大",
      "需要LLM API密钥"
    ],
    pricingTiers: [
      {
        tier: "Free",
        tierZh: "免费版",
        price: "$0",
        features: ["All agents", "Open-source", "Self-hosted"],
        featuresZh: ["全部代理", "开源", "自托管"],
      },
    ],
    extensions: [
      {
        name: "Agents GitHub",
        description: "Official open-source repository",
        descriptionZh: "官方开源仓库",
      },
    ],
  },

{
    id: "ruflo",
    name: "Ruflo (formerly Claude-Flow)",
    description: "AI project manager that breaks down complex projects into tasks, assigns them to specialized AI agents, and ensures automatic quality checks.",
    descriptionZh: "AI项目经理，将复杂项目分解为任务，分配给专业AI代理，并确保自动质量检查。",
    category: "productivity",
    tags: ["project-management", "automation", "workflow", "task-management", "productivity"],
    difficulty: "intermediate",
    url: "https://github.com/openclaw/ruflo",
    rating: r(4.5),
    pricing: "Free (open source)",
    useCase: "Ruflo is an AI project manager that breaks down complex projects into tasks, assigns them to specialized AI agents, and ensures automatic quality checks.",
    icon: "\u{1F4CB}",
    company: "OpenClaw",
    companyZh: "OpenClaw",
    founded: "2025",
    headquarters: "Community",
    descriptionLong: "Ruflo (formerly known as Claude-Flow, with 45,720+ stars) is an AI-powered project management system that acts as your virtual general manager. It takes complex projects, breaks them down into manageable tasks, assigns each task to the most suitable AI agent from your team, and ensures automatic quality verification at every step. Whether launching a new product line, building a website, or running a marketing campaign, Ruflo handles the entire project lifecycle - planning, delegation, execution tracking, and quality assurance - letting you focus on high-level strategy while AI manages the execution.",
    descriptionLongZh: "Ruflo（原名Claude-Flow，拥有45,720+星标）是一个AI驱动的项目管理系统，充当您的虚拟总经理。它接收复杂项目，分解为可管理的任务，将每个任务分配给团队中最合适的AI代理，并确保每个步骤的自动质量验证。无论启动新产品线、构建网站还是进行营销活动，Ruflo处理整个项目生命周期——规划、委派、执行跟踪和质量保证——让您专注于高层战略，AI负责执行。",
    targetAudience: "Project managers, entrepreneurs, and teams who want AI-driven project planning, delegation, and quality control.",
    targetAudienceZh: "需要AI驱动项目规划、委派和质量控制的项目经理、企业家和团队。",
    scene: "office-productivity",
    advantages: [
      "Automated project breakdown",
      "Intelligent task assignment",
      "Automatic quality checks",
      "End-to-end project lifecycle",
      "45K+ GitHub stars"
    ],
    advantagesZh: [
      "自动化项目分解",
      "智能任务分配",
      "自动质量检查",
      "端到端项目生命周期",
      "45K+ GitHub星标"
    ],
    useCases: [
      "Product launch project management",
      "Website development coordination",
      "Marketing campaign execution",
      "Content pipeline management",
      "Cross-team task orchestration"
    ],
    useCasesZh: [
      "产品发布项目管理",
      "网站开发协调",
      "营销活动执行",
      "内容管线管理",
      "跨团队任务编排"
    ],
    skills: [
      "project management",
      "task assignment",
      "workflow automation",
      "quality assurance",
      "team coordination"
    ],
    pros: [
      "Full project lifecycle automation",
      "Intelligent agent-task matching",
      "Built-in quality verification",
      "Active 45K+ star community",
      "Reduces management overhead"
    ],
    prosZh: [
      "全项目生命周期自动化",
      "智能代理-任务匹配",
      "内置质量验证",
      "活跃的45K+星标社区",
      "减少管理开销"
    ],
    cons: [
      "Requires compatible AI agents",
      "Complex initial setup",
      "Best with existing agent ecosystem",
      "Dependent on LLM availability"
    ],
    consZh: [
      "需要兼容的AI代理",
      "初始设置复杂",
      "在现有代理生态系统中效果最佳",
      "依赖LLM可用性"
    ],
    pricingTiers: [
      {
        tier: "Free",
        tierZh: "免费版",
        price: "$0",
        features: ["All features", "Open-source", "Self-hosted"],
        featuresZh: ["全部功能", "开源", "自托管"],
      },
    ],
    extensions: [
      {
        name: "Ruflo GitHub",
        description: "Official open-source repository",
        descriptionZh: "官方开源仓库",
      },
    ],
  },

{
    id: "letta",
    name: "Letta",
    description: "An evolving AI memory system that learns your preferences, tone, and workflow patterns. Maintains context across long-running projects.",
    descriptionZh: "一个不断进化的AI记忆系统，学习您的偏好、语气和工作流程模式。在长期项目中保持上下文。",
    category: "productivity",
    tags: ["memory", "context", "personalization", "workflow", "ai-brain"],
    difficulty: "intermediate",
    url: "https://letta.ai",
    rating: r(4.4),
    pricing: "Free / paid tiers",
    useCase: "Letta is an evolving AI memory system that learns your preferences, tone, and workflow patterns, maintaining context across long-running projects.",
    icon: "\u{1F9E0}",
    company: "Letta AI",
    companyZh: "Letta AI",
    founded: "2024",
    headquarters: "San Francisco, CA",
    descriptionLong: "Letta is an evolving AI memory system that changes how AI interacts with you over time. Unlike stateless AI tools that treat every conversation as fresh, Letta learns your preferences, writing tone, workflow patterns, and recurring requirements - and maintains that knowledge across sessions. With 22,490+ stars, it is the leading solution for persistent AI memory. It remembers your brand voice guidelines, preferred email structures, coding conventions, and even subtle stylistic choices. Start a new project and Letta already knows how you like things done, eliminating repetitive explanation and ensuring consistency across all AI interactions.",
    descriptionLongZh: "Letta是一个不断进化的AI记忆系统，改变AI随时间与您互动的方式。与将每次对话视为全新的无状态AI工具不同，Letta学习您的偏好、写作语气、工作流程模式和重复需求——并在不同会话间保持这些知识。拥有22,490+星标，是持久化AI记忆的领先解决方案。它记住您的品牌声音指南、偏好的邮件结构、编码约定，甚至微妙的风格选择。启动新项目时，Letta已经知道您喜欢如何工作，消除重复解释并确保所有AI交互的一致性。",
    targetAudience: "Professionals and teams who want AI that remembers their preferences and maintains context across long-running projects.",
    targetAudienceZh: "希望在长期项目中让AI记住其偏好并保持上下文的专业人士和团队。",
    scene: "office-productivity",
    advantages: [
      "Persistent memory across sessions",
      "Learns preferences over time",
      "Consistent output quality",
      "Reduces repetitive instructions",
      "22K+ GitHub stars"
    ],
    advantagesZh: [
      "跨会话持久记忆",
      "随时间学习偏好",
      "一致的输出质量",
      "减少重复指令",
      "22K+ GitHub星标"
    ],
    useCases: [
      "Long-term content creation projects",
      "Brand voice consistency management",
      "Personal AI assistant with memory",
      "Team knowledge base building",
      "Workflow pattern optimization"
    ],
    useCasesZh: [
      "长期内容创作项目",
      "品牌声音一致性管理",
      "带记忆的个人AI助手",
      "团队知识库建设",
      "工作流程模式优化"
    ],
    skills: [
      "memory",
      "personalization",
      "context",
      "consistency",
      "workflow learning"
    ],
    pros: [
      "Genuinely persistent AI memory",
      "Improves over time with use",
      "Excellent for long-running projects",
      "Active community development",
      "Reduces repetitive work significantly"
    ],
    prosZh: [
      "真正的持久AI记忆",
      "随着使用不断改进",
      "非常适合长期项目",
      "活跃的社区开发",
      "显著减少重复工作"
    ],
    cons: [
      "Privacy concerns with stored data",
      "Memory can reinforce bad patterns",
      "Requires ongoing API usage",
      "Learning curve for setup"
    ],
    consZh: [
      "存储数据的隐私问题",
      "记忆可能强化不良模式",
      "需要持续API使用",
      "设置需要学习成本"
    ],
    pricingTiers: [
      {
        tier: "Free",
        tierZh: "免费版",
        price: "$0",
        features: ["Basic memory features", "Limited sessions", "Open-source core"],
        featuresZh: ["基础记忆功能", "有限会话", "开源核心"],
      },
      {
        tier: "Pro",
        tierZh: "专业版",
        price: "From $20/mo",
        features: ["Full memory system", "Unlimited sessions", "Priority support", "Team features"],
        featuresZh: ["完整记忆系统", "无限会话", "优先支持", "团队功能"],
      },
    ],
    extensions: [
      {
        name: "Letta Website",
        description: "Official website",
        descriptionZh: "官方网站",
        url: "https://letta.ai",
      },
    ],
  },
"""

# Find the closing of _tools2: "  },\n] as Tool[];"
insert_before = "  },\n] as Tool[];"
last_idx = content.rfind(insert_before)
if last_idx >= 0:
    new_content = content[:last_idx] + "  }," + tool_entries + "]" + content[last_idx + len(insert_before):]
    with open(tools_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully added 5 new tools to tools.ts")
else:
    print("ERROR: Could not find insertion point")
    # Debug
    end_section = content[-300:]
    print("End section:")
    print(repr(end_section))
