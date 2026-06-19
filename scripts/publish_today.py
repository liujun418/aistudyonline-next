import re, os, json

PROJECT = r"C:\Users\jun\aistudyonline-next"

# ============================================================
# PHASE 1: Add 6 new tools to tools.ts
# ============================================================
tools_file = os.path.join(PROJECT, "src", "lib", "tools.ts")
with open(tools_file, "r", encoding="utf-8") as f:
    tools_src = f.read()

# Find where to insert (before last closing bracket of array)
# Insert before the last "];" but actually after the last tool entry
# Find "];" at end of file
last_bracket = tools_src.rfind("];")
assert last_bracket > 0, "Could not find end of tools array"

new_tools = r"""
{
    id: "e2b",
    name: "E2B",
    description: "Cloud sandbox infrastructure for AI agents with secure code execution and file system isolation.",
    descriptionZh: "为AI代理提供安全代码执行和文件系统隔离的云端沙箱基础设施。",
    category: "coding",
    tags: ["sandbox", "ai-agents", "security", "code-execution", "cloud"],
    difficulty: "intermediate",
    url: "https://e2b.dev",
    rating: r(4.6),
    pricing: "Free tier available / Pay-as-you-go",
    useCase: "E2B provides secure cloud sandboxes for AI agents to execute code, manage files, and run commands without risking the host system.",
    icon: "\u{1F6E1}",
    company: "E2B.dev",
    companyZh: "E2B.dev",
    founded: "2023",
    headquarters: "San Francisco, CA",
    descriptionLong: "E2B (E2B.dev) is a cloud infrastructure platform purpose-built for AI agent sandboxing, providing secure, isolated execution environments where AI agents can run code, manage files, browse the web, and interact with system resources without endangering the host machine. Unlike general-purpose containers or VMs, E2B's sandboxes are designed with AI-specific requirements: millisecond-level startup times (critical for agent workflows that spawn many short-lived sessions), built-in file system APIs that agents can call programmatically, environment snapshot/restore capabilities for iterative development, and comprehensive audit logging of every action the agent takes. E2B integrates directly with popular AI frameworks like LangChain, CrewAI, and AutoGen, making it straightforward to add sandboxing to existing agent pipelines. The platform supports multiple runtimes (Python, Node.js, Bash) within each sandbox, and provides SDKs for Python and JavaScript. For teams building autonomous AI agents that need to execute untrusted code, access the internet, or manipulate files — E2B provides the security boundary that turns a risky prototype into a production-ready system. It's particularly valuable for coding agents, research agents that scrape the web, and multi-agent systems where one agent's actions shouldn't compromise others.",
    descriptionLongZh: "E2B（E2B.dev）是专为AI代理沙箱构建的云端基础设施平台，提供安全隔离的执行环境，让AI代理可以运行代码、管理文件、浏览网页和与系统资源交互，而不会危及主机安全。与通用容器或虚拟机不同，E2B的沙箱针对AI特定需求设计：毫秒级启动时间（对产生大量短生命周期会话的代理工作流至关重要）、代理可通过编程调用的内置文件系统API、支持迭代开发的环境快照/恢复能力，以及代理每项操作的全面审计日志。E2B直接与LangChain、CrewAI和AutoGen等主流AI框架集成，可轻松将沙箱添加到现有代理管道中。该平台在每个沙箱内支持多种运行时（Python、Node.js、Bash），并提供Python和JavaScript的SDK。对于构建需要执行不受信任代码、访问互联网或操作文件的自主AI代理的团队，E2B提供了将高风险原型转变为生产就绪系统的安全边界。",
    advantages: ["Millisecond startup", "AI-native APIs", "Full audit logging", "Framework integrations", "Snapshot/restore"],
    advantagesZh: ["毫秒级启动", "AI原生API", "完整审计日志", "框架集成", "快照/恢复"],
    useCases: ["Secure AI code execution", "Multi-agent sandboxing", "Web browsing agents", "Untrusted code testing"],
    useCasesZh: ["安全AI代码执行", "多代理沙箱", "网页浏览代理", "不受信任代码测试"],
    targetAudience: "AI developers building autonomous agents that execute code or interact with external systems.",
    targetAudienceZh: "构建执行代码或与外部系统交互的自主AI代理的开发者。",
    pricingTiers: [{tier: "Free", tierZh: "免费版", price: "$0", features: ["500 sandbox hours/month", "1 concurrent sandbox", "Community support"]}, {tier: "Pro", tierZh: "专业版", price: "$39/month", features: ["2000 sandbox hours", "10 concurrent sandboxes", "Priority support"]}],
    pros: ["Purpose-built for AI agents", "Fast startup times", "Good framework integrations", "Comprehensive logging"],
    prosZh: ["专为AI代理设计", "快速启动", "良好的框架集成", "全面的日志记录"],
    cons: ["Cloud-dependent (no local mode)", "Limited free tier hours", "Pricing scales with usage"],
    consZh: ["依赖云端（无本地模式）", "免费时长有限", "按使用量计费"],
},

{
    id: "firecracker",
    name: "Firecracker",
    description: "AWS open-source microVM monitor for secure, fast, multi-tenant container and function isolation.",
    descriptionZh: "AWS开源的微型虚拟机监视器，用于安全、快速的多租户容器和函数隔离。",
    category: "coding",
    tags: ["microvm", "security", "aws", "open-source", "sandbox"],
    difficulty: "advanced",
    url: "https://firecracker-microvm.github.io",
    rating: r(4.7),
    pricing: "Free (open-source, Apache 2.0)",
    useCase: "Firecracker launches lightweight microVMs in milliseconds for secure multi-tenant workloads like AWS Lambda and Fargate.",
    icon: "\u{1F525}",
    company: "Amazon Web Services",
    companyZh: "亚马逊云科技",
    founded: "2018",
    headquarters: "Seattle, WA",
    descriptionLong: "Firecracker is an open-source Virtual Machine Monitor (VMM) developed by AWS that powers AWS Lambda and Fargate, designed to launch lightweight microVMs in as little as 125ms while providing hardware-level isolation between workloads. Unlike traditional VMs that take seconds to boot and consume significant memory, Firecracker microVMs are purpose-built for serverless and container workloads — they strip away unnecessary devices (no BIOS, no graphics, no USB), use a minimal Linux kernel, and leverage KVM for hardware virtualization. This gives you the security of a VM (each microVM has its own kernel, so a kernel exploit in one can't reach others) with the speed and density of containers. Firecracker supports snapshot/restore for near-instant VM resumption, a RESTful API for VM lifecycle management, and integrates with containerd via the firecracker-containerd runtime. For AI agent sandboxing, Firecracker microVMs are ideal — each agent gets its own isolated environment with its own filesystem, network namespace, and resource limits, making it impossible for a compromised or hallucinating agent to affect other agents or the host. The microVM approach is particularly powerful for multi-tenant AI platforms where different users' agents share the same physical infrastructure.",
    descriptionLongZh: "Firecracker 是 AWS 开发的开源虚拟机监视器（VMM），为 AWS Lambda 和 Fargate 提供动力，设计用于在短短 125 毫秒内启动轻量级微型虚拟机，同时提供工作负载之间的硬件级隔离。与传统虚拟机需要数秒启动并消耗大量内存不同，Firecracker 微型虚拟机专为无服务器和容器工作负载设计——它们剥离了不必要的设备（无 BIOS、无显卡、无 USB），使用最小化 Linux 内核，并利用 KVM 进行硬件虚拟化。这为你提供了虚拟机的安全性（每个微型虚拟机有自己的内核，一个内核漏洞无法影响其他虚拟机）以及容器的速度和密度。Firecracker 支持快照/恢复以实现近乎即时的虚拟机恢复，提供 RESTful API 用于虚拟机生命周期管理，并通过 firecracker-containerd 运行时与 containerd 集成。对于 AI 代理沙箱，Firecracker 微型虚拟机是理想选择——每个代理获得自己的隔离环境，拥有独立的文件系统、网络命名空间和资源限制，使被入侵或产生幻觉的代理无法影响其他代理或主机。",
    advantages: ["125ms startup", "Hardware-level isolation", "AWS production-proven", "Open source", "Minimal attack surface"],
    advantagesZh: ["125ms启动", "硬件级隔离", "AWS生产验证", "开源", "最小攻击面"],
    useCases: ["AI agent sandboxing", "Serverless platforms", "Multi-tenant SaaS", "Secure code execution"],
    useCasesZh: ["AI代理沙箱", "无服务器平台", "多租户SaaS", "安全代码执行"],
    targetAudience: "Platform engineers and security teams building multi-tenant or AI agent infrastructure.",
    targetAudienceZh: "构建多租户或AI代理基础设施的平台工程师和安全团队。",
    pricingTiers: [{tier: "Open Source", tierZh: "开源版", price: "$0", features: ["Full microVM capabilities", "Apache 2.0 license", "Community support"]}],
    pros: ["Production-proven at AWS scale", "Extremely fast boot", "Strong security isolation", "Minimal resource overhead"],
    prosZh: ["AWS规模生产验证", "极快启动", "强安全隔离", "最小资源开销"],
    cons: ["Linux-only (requires KVM)", "Complex setup for beginners", "Limited to x86_64 and ARM64"],
    consZh: ["仅Linux（需KVM）", "初学者设置复杂", "仅限x86_64和ARM64"],
},

{
    id: "autogen",
    name: "AutoGen",
    description: "Microsoft's open-source framework for building multi-agent AI systems with conversational workflows.",
    descriptionZh: "微软开源的多代理AI系统框架，支持对话式工作流。",
    category: "coding",
    tags: ["multi-agent", "microsoft", "framework", "open-source", "python"],
    difficulty: "advanced",
    url: "https://microsoft.github.io/autogen",
    rating: r(4.5),
    pricing: "Free (open-source, MIT)",
    useCase: "AutoGen builds multi-agent systems where specialized AI agents collaborate through structured conversations to solve complex tasks.",
    icon: "\u{1F91D}",
    company: "Microsoft",
    companyZh: "微软",
    founded: "2023",
    headquarters: "Redmond, WA",
    descriptionLong: "AutoGen is Microsoft's open-source framework for building multi-agent AI applications where multiple specialized agents converse, collaborate, and negotiate to accomplish complex tasks. Unlike single-agent architectures, AutoGen enables agent teams where a planner agent breaks down tasks, coder agents implement solutions, critic agents review output, and user proxy agents represent human-in-the-loop oversight. The framework supports flexible conversation patterns — sequential chains, parallel fan-out, nested chats for sub-task delegation — and integrates with any LLM backend (OpenAI, Claude, local models). AutoGen's key innovation is its conversation-driven programming model: rather than hard-coding agent interactions, you define agents with specific roles and let them negotiate solutions through structured dialogue. The framework handles message routing, turn-taking, and error recovery automatically. AutoGen Studio provides a no-code UI for designing and testing agent teams, while the core library supports advanced features like code execution in Docker sandboxes, tool use, RAG integration, and human feedback loops. For developers building complex AI workflows — code generation pipelines, research assistants, automated tutoring systems — AutoGen provides a battle-tested foundation from one of the world's largest AI research organizations.",
    descriptionLongZh: "AutoGen 是微软的开源多代理 AI 应用框架，允许多个专业代理通过对话、协作和协商来完成复杂任务。与单代理架构不同，AutoGen 支持代理团队，其中规划代理分解任务，编码代理实现解决方案，审查代理检查输出，用户代理代表人在环监督。该框架支持灵活的对话模式——顺序链、并行扇出、子任务委托的嵌套对话——并与任何 LLM 后端集成。AutoGen 的关键创新是其对话驱动的编程模型：你不是硬编码代理交互，而是定义具有特定角色的代理，让它们通过结构化对话协商解决方案。框架自动处理消息路由、轮流发言和错误恢复。AutoGen Studio 提供无代码 UI 用于设计和测试代理团队，核心库支持 Docker 沙箱中的代码执行、工具使用、RAG 集成和人工反馈循环。对于构建复杂 AI 工作流的开发者，AutoGen 提供了来自全球最大 AI 研究机构之一的实战验证基础。",
    advantages: ["Multi-agent architecture", "Conversation-driven", "Docker sandbox", "No-code Studio", "Microsoft-backed"],
    advantagesZh: ["多代理架构", "对话驱动", "Docker沙箱", "无代码Studio", "微软支持"],
    useCases: ["Multi-agent code generation", "Research assistants", "Automated tutoring", "Complex workflow automation"],
    useCasesZh: ["多代理代码生成", "研究助手", "自动辅导", "复杂工作流自动化"],
    targetAudience: "AI engineers building complex multi-agent systems with human-in-the-loop workflows.",
    targetAudienceZh: "构建带人在环工作流的复杂多代理系统的AI工程师。",
    pricingTiers: [{tier: "Open Source", tierZh: "开源版", price: "$0", features: ["Full framework", "AutoGen Studio", "Docker integration", "MIT license"]}],
    pros: ["Flexible agent patterns", "Strong community", "Docker sandbox built-in", "Human-in-loop support"],
    prosZh: ["灵活的代理模式", "强大的社区", "内置Docker沙箱", "人在环支持"],
    cons: ["Steep learning curve", "Complex debugging", "Python-only", "Documentation evolving"],
    consZh: ["学习曲线陡峭", "调试复杂", "仅Python", "文档仍在完善"],
},

{
    id: "opentelemetry",
    name: "OpenTelemetry",
    description: "CNCF observability framework for generating, collecting, and exporting telemetry data from applications.",
    descriptionZh: "CNCF可观测性框架，用于生成、收集和导出应用程序的遥测数据。",
    category: "coding",
    tags: ["observability", "tracing", "monitoring", "cncf", "open-source"],
    difficulty: "advanced",
    url: "https://opentelemetry.io",
    rating: r(4.8),
    pricing: "Free (open-source, Apache 2.0)",
    useCase: "OpenTelemetry provides vendor-neutral APIs and SDKs for distributed tracing, metrics, and logging in cloud-native applications.",
    icon: "\u{1F50D}",
    company: "Cloud Native Computing Foundation",
    companyZh: "云原生计算基金会",
    founded: "2019",
    headquarters: "San Francisco, CA",
    descriptionLong: "OpenTelemetry (OTel) is the industry-standard observability framework under the Cloud Native Computing Foundation (CNCF), providing a unified set of APIs, SDKs, and tools for generating, collecting, and exporting telemetry data — traces, metrics, and logs — from applications. Think of it as the universal adapter for observability: instead of instrumenting your code with vendor-specific libraries, you use OpenTelemetry's vendor-neutral APIs once, then export your telemetry data to any backend (Jaeger, Prometheus, Datadog, Grafana, etc.) by changing the exporter configuration. For AI agent systems, OpenTelemetry is invaluable — it lets you trace every agent action across a multi-step workflow, measure token usage and latency at each step, detect anomalies in agent behavior, and create dashboards showing the end-to-end health of your agent pipeline. The framework supports automatic instrumentation for popular libraries (Express, gRPC, HTTP clients, databases) and manual instrumentation for custom business logic. With the rise of AI agents that can run for hours or days unattended, OpenTelemetry provides the observability backbone needed to understand what agents are doing, detect when they go wrong, and debug complex multi-agent interactions in production.",
    descriptionLongZh: "OpenTelemetry（OTel）是云原生计算基金会（CNCF）下的行业标准可观测性框架，提供统一的 API、SDK 和工具集，用于生成、收集和导出应用程序的遥测数据——链路追踪、指标和日志。可以将其视为可观测性的通用适配器：无需使用供应商特定的库来检测代码，只需使用一次 OpenTelemetry 的供应商中立 API，然后通过更改导出器配置将遥测数据发送到任何后端（Jaeger、Prometheus、Datadog、Grafana 等）。对于 AI 代理系统，OpenTelemetry 非常宝贵——它可以追踪多步工作流中每个代理的操作，测量每步的 token 使用量和延迟，检测代理行为的异常，并创建显示代理管道端到端健康状况的仪表板。该框架支持流行库的自动检测和自定义业务逻辑的手动检测。随着能够无人值守运行数小时或数天的 AI 代理的兴起，OpenTelemetry 提供了理解代理行为、检测异常和调试复杂多代理交互所需的可观测性基础。",
    advantages: ["Vendor-neutral standard", "Auto-instrumentation", "CNCF graduated", "Universal exporter", "Rich ecosystem"],
    advantagesZh: ["供应商中立标准", "自动检测", "CNCF毕业项目", "通用导出器", "丰富生态"],
    useCases: ["AI agent monitoring", "Distributed tracing", "Performance optimization", "Production debugging"],
    useCasesZh: ["AI代理监控", "分布式追踪", "性能优化", "生产调试"],
    targetAudience: "Platform engineers and SREs needing vendor-neutral observability for distributed systems.",
    targetAudienceZh: "需要供应商中立可观测性的平台工程师和SRE。",
    pricingTiers: [{tier: "Open Source", tierZh: "开源版", price: "$0", features: ["Full OTel SDK", "Auto-instrumentation", "All exporters", "Apache 2.0"]}],
    pros: ["Industry standard", "Vendor lock-in prevention", "Rich auto-instrumentation", "Massive community"],
    prosZh: ["行业标准", "防止供应商锁定", "丰富的自动检测", "庞大的社区"],
    cons: ["Complex configuration", "Documentation gaps", "Overhead for simple apps"],
    consZh: ["配置复杂", "文档有缺口", "简单应用有开销"],
},

{
    id: "open-policy-agent",
    name: "Open Policy Agent (OPA)",
    description: "CNCF policy engine for unified, context-aware authorization across the cloud-native stack.",
    descriptionZh: "CNCF策略引擎，在整个云原生技术栈中提供统一的上下文感知授权。",
    category: "coding",
    tags: ["policy", "security", "authorization", "cncf", "open-source"],
    difficulty: "advanced",
    url: "https://www.openpolicyagent.org",
    rating: r(4.7),
    pricing: "Free (open-source, Apache 2.0)",
    useCase: "OPA decouples policy decisions from application logic using declarative Rego language for fine-grained access control.",
    icon: "\u{1F6E1}",
    company: "Styra / CNCF",
    companyZh: "Styra / CNCF",
    founded: "2016",
    headquarters: "San Francisco, CA",
    descriptionLong: "Open Policy Agent (OPA) is a CNCF-graduated open-source policy engine that provides unified, context-aware authorization across the entire cloud-native stack. OPA decouples policy decisions from application logic: instead of embedding authorization rules in your code, you write policies in Rego (a declarative, Datalog-inspired language) and OPA evaluates them against real-time data. This separation means policy changes don't require code changes or redeployment. For AI agent systems, OPA is a powerful tool for defining what agents can and cannot do — you can write policies like 'an agent can read files only in /data/agent/', 'an agent can make network requests only to approved domains', or 'an agent must request human approval for any command that modifies production data'. OPA can be deployed as a sidecar container, a library embedded in your Go application, or a standalone service with a REST API. It supports real-time policy updates, decision logging for audit trails, and integration with Kubernetes admission control, Envoy service mesh, and Terraform infrastructure-as-code. For teams building AI agents that interact with sensitive systems, OPA provides the guardrails that turn autonomous agents from a security risk into a controlled, auditable capability.",
    descriptionLongZh: "Open Policy Agent（OPA）是 CNCF 毕业的开源策略引擎，在整个云原生技术栈中提供统一的上下文感知授权。OPA 将策略决策与应用逻辑解耦：你不再将授权规则嵌入代码中，而是用 Rego（一种声明式的类 Datalog 语言）编写策略，OPA 根据实时数据评估它们。这种分离意味着策略变更不需要代码变更或重新部署。对于 AI 代理系统，OPA 是定义代理可以做什么和不能做什么的强大工具——你可以编写诸如'代理只能读取 /data/agent/ 目录中的文件'、'代理只能向已批准的域名发起网络请求'或'代理修改生产数据的任何命令必须请求人工批准'等策略。OPA 可以部署为边车容器、嵌入 Go 应用的库或带 REST API 的独立服务。它支持实时策略更新、审计跟踪的决策日志，以及与 Kubernetes 准入控制、Envoy 服务网格和 Terraform 基础设施即代码的集成。对于构建与敏感系统交互的 AI 代理的团队，OPA 提供了将自主代理从安全风险转变为受控、可审计能力的护栏。",
    advantages: ["Declarative Rego language", "Decoupled from app code", "CNCF graduated", "Real-time policy updates", "Decision audit logs"],
    advantagesZh: ["声明式Rego语言", "与应用代码解耦", "CNCF毕业项目", "实时策略更新", "决策审计日志"],
    useCases: ["AI agent access control", "Kubernetes admission control", "API authorization", "Infrastructure policy"],
    useCasesZh: ["AI代理访问控制", "Kubernetes准入控制", "API授权", "基础设施策略"],
    targetAudience: "Security and platform teams needing fine-grained, decoupled policy enforcement.",
    targetAudienceZh: "需要细粒度解耦策略执行的安全和平台团队。",
    pricingTiers: [{tier: "Open Source", tierZh: "开源版", price: "$0", features: ["Full policy engine", "Rego language", "REST API", "Apache 2.0"]}, {tier: "Styra DAS", tierZh: "Styra DAS", price: "Contact sales", features: ["Centralized management", "Decision logging", "Impact analysis", "Team collaboration"]}],
    pros: ["Industry standard for policy", "Powerful Rego language", "Large ecosystem", "Proven at scale"],
    prosZh: ["行业策略标准", "强大的Rego语言", "庞大的生态", "规模化验证"],
    cons: ["Rego learning curve", "Performance at high throughput", "Limited UI without Styra"],
    consZh: ["Rego学习曲线", "高吞吐性能", "无Styra时UI有限"],
},

{
    id: "docker",
    name: "Docker",
    description: "Industry-standard container platform for packaging, distributing, and running applications in isolated environments.",
    descriptionZh: "行业标准的容器平台，用于在隔离环境中打包、分发和运行应用程序。",
    category: "coding",
    tags: ["container", "devops", "deployment", "isolation"],
    difficulty: "intermediate",
    url: "https://www.docker.com",
    rating: r(4.8),
    pricing: "Free (Docker Desktop Personal) / Business from $24/user/month",
    useCase: "Docker packages applications with their dependencies into portable containers that run consistently across any environment.",
    icon: "\u{1F433}",
    company: "Docker Inc.",
    companyZh: "Docker公司",
    founded: "2013",
    headquarters: "Palo Alto, CA",
    descriptionLong: "Docker is the industry-standard container platform that revolutionized software deployment by packaging applications and their dependencies into lightweight, portable containers that run consistently across any environment — from a developer's laptop to a production Kubernetes cluster. For AI agent development, Docker serves as an essential isolation layer: each agent or agent team can run in its own container with precisely defined dependencies (specific Python versions, system libraries, GPU drivers), ensuring reproducibility and preventing dependency conflicts between agents. Docker Compose enables orchestrating multi-container agent systems where a coding agent, testing agent, and monitoring agent each run in their own environment with defined networking. Docker's image layering and caching make iterative agent development fast, while Docker Hub provides a registry for sharing pre-built agent environments. For production AI agent deployments, Docker containers integrate with Kubernetes for auto-scaling agent workers, provide resource limits (CPU, memory, GPU) to prevent runaway agents from consuming all system resources, and enable blue-green deployments for zero-downtime agent updates. While alternatives like Podman exist, Docker remains the most widely supported container runtime with the largest ecosystem of pre-built images and tooling integrations, making it the default choice for containerizing AI agent workloads.",
    descriptionLongZh: "Docker 是行业标准的容器平台，通过将应用程序及其依赖打包到轻量级、可移植的容器中，彻底改变了软件部署方式——容器在任何环境中都能一致运行，从开发者的笔记本电脑到生产 Kubernetes 集群。对于 AI 代理开发，Docker 是关键的隔离层：每个代理或代理团队可以在自己的容器中运行，具有精确定义的依赖（特定 Python 版本、系统库、GPU 驱动），确保可复现性并防止代理之间的依赖冲突。Docker Compose 支持编排多容器代理系统，其中编码代理、测试代理和监控代理各自在自己的环境中运行，具有定义的网络连接。Docker 的镜像分层和缓存使迭代代理开发变得快速，Docker Hub 提供了共享预构建代理环境的注册表。对于生产级 AI 代理部署，Docker 容器与 Kubernetes 集成以实现代理工作器的自动扩缩容，提供资源限制（CPU、内存、GPU）以防止失控代理消耗所有系统资源，并支持蓝绿部署以实现零停机代理更新。虽然存在 Podman 等替代方案，但 Docker 仍然是最广泛支持的容器运行时，拥有最大的预构建镜像和工具集成生态。",
    advantages: ["Industry standard", "Consistent environments", "Large image ecosystem", "Compose orchestration", "Resource isolation"],
    advantagesZh: ["行业标准", "环境一致性", "庞大的镜像生态", "Compose编排", "资源隔离"],
    useCases: ["AI agent isolation", "Reproducible ML environments", "Microservice deployment", "CI/CD pipelines"],
    useCasesZh: ["AI代理隔离", "可复现ML环境", "微服务部署", "CI/CD管道"],
    targetAudience: "Developers and DevOps engineers needing consistent, isolated application environments.",
    targetAudienceZh: "需要一致、隔离应用环境的开发者和DevOps工程师。",
    pricingTiers: [{tier: "Personal", tierZh: "个人版", price: "$0", features: ["Docker Desktop", "Docker Hub (1 private repo)", "Docker Compose", "Community support"]}, {tier: "Business", tierZh: "商业版", price: "$24/user/month", features: ["Unlimited private repos", "Advanced security", "SSO", "Premium support"]}],
    pros: ["Universal standard", "Massive ecosystem", "Excellent documentation", "Cross-platform"],
    prosZh: ["通用标准", "庞大的生态", "优秀的文档", "跨平台"],
    cons: ["Docker Desktop licensing changes", "Resource overhead on macOS/Windows", "Linux knowledge required"],
    consZh: ["Docker Desktop许可变更", "macOS/Windows资源开销", "需Linux知识"],
},
"""

# Insert new tools before the closing ];
insert_pos = last_bracket
tools_src = tools_src[:insert_pos] + new_tools + "\n];\n"

with open(tools_file, "w", encoding="utf-8") as f:
    f.write(tools_src)

print("Added 6 new tools: E2B, Firecracker, AutoGen, OpenTelemetry, OPA, Docker")

# ============================================================
# PHASE 2: Add articles to articles.ts
# ============================================================
articles_file = os.path.join(PROJECT, "src", "lib", "articles.ts")
with open(articles_file, "r", encoding="utf-8") as f:
    articles_src = f.read()

new_articles = """
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
];"""

# Find last "];" before end
last_arr_end = articles_src.rfind("];")
articles_src = articles_src[:last_arr_end] + new_articles + "\n];\n"

with open(articles_file, "w", encoding="utf-8") as f:
    f.write(articles_src)

print("Added 2 new articles to articles.ts")

# ============================================================
# PHASE 3: Add article content to article-content.ts
# ============================================================
content_file = os.path.join(PROJECT, "src", "lib", "article-content.ts")
with open(content_file, "r", encoding="utf-8") as f:
    content_src = f.read()

# Article 1: AI Agent Sandbox
article1_en = r"""
<div class="article-meta-banner">
<p><strong>Category:</strong> AI Agent Security · <strong>Difficulty:</strong> Intermediate</p>
<p><strong>What you'll learn:</strong> How to sandbox AI agents using microVMs, policy engines, state snapshots, and observability — turning risky autonomous agents into production-ready tools.</p>
</div>

<p>As large language models evolve from mere text generators to autonomous AI Agents capable of interacting with local files, executing code, and making network requests, the need for robust security boundaries has become paramount. This article dives into the <strong>AI Agent Sandbox</strong> — a specialized security infrastructure designed to manage the risks of autonomous AI while enabling practical, productive workflows.</p>

<h2>What is an AI Agent Sandbox?</h2>

<p>An AI Agent Sandbox is not just a virtual machine or Docker container. It's a <strong>comprehensive security layer</strong> tailored for multi-step AI interactions, combining three core capabilities:</p>

<ul>
<li><strong>Lightning-Fast Isolation</strong>: A millisecond-launch environment that physically separates the Agent from the host system.</li>
<li><strong>Dynamic Policy Control</strong>: A system to grant or revoke permissions in real time.</li>
<li><strong>Auditable Traceability</strong>: Full logging and tracing of all Agent actions, tied to session context.</li>
</ul>

<h2>Evolution of Sandboxing for AI Agents</h2>

<p>The concept of sandboxing has evolved over 30+ years, adapting to the needs of AI Agents:</p>

<h3>Historical Isolation Technologies</h3>

<ul>
<li><strong>1990s: Java Applets</strong> — Early sandboxing via permission-based isolation (e.g., restricting file system access).</li>
<li><strong>2000s: Virtual Machines (VMs)</strong> — Heavyweight hardware-level isolation (e.g., VMware), too slow for modern AI workflows.</li>
<li><strong>2010s: Containers (Docker)</strong> — Lightweight namespace isolation, but still vulnerable to escape attacks.</li>
<li><strong>2020s: MicroVMs (Firecracker)</strong> — Combines speed (millisecond startup) with strong isolation, ideal for AI Agents.</li>
</ul>

<h3>The "Naked Deployment" Era (2022–2023)</h3>

<p>Early AI Agent frameworks like <a href="/en/tools/langchain">LangChain</a> and <a href="/en/tools/autogen">AutoGen</a> lacked proper sandboxes. Agents ran code directly on local machines or shared containers, leading to disasters:</p>

<ul>
<li>Accidental system deletion via <code>rm -rf /</code>.</li>
<li>Leakage of API keys and environment variables.</li>
<li>Uncontrolled API request loops (e.g., thousands of redundant calls).</li>
</ul>

<p><em>Example of a risky setup (<strong>never use in production</strong>):</em></p>

<pre><code class="language-python"># Early LangChain code with no sandbox
from langchain.agents import initialize_agent, Tool
from langchain.utilities import BashProcess

bash_tool = Tool(
    name="Bash",
    func=BashProcess().run,
    description="Run bash commands"
)
agent = initialize_agent([bash_tool], llm, agent="zero-shot-react-description")
agent.run("Delete all logs in /var/log")  # High risk!</code></pre>

<h3>Modern Sandboxing (2023–Present)</h3>

<p>Industry and academia now prioritize sandboxing:</p>

<ul>
<li><strong>Academia</strong>: Benchmarks like AgentBench require repeatable, isolated environments.</li>
<li><strong>Industry</strong>: Services like <a href="/en/tools/e2b">E2B</a> provide AI-native sandboxes with cloud isolation.</li>
<li><strong>Open Source</strong>: Frameworks like <a href="/en/tools/langgraph">LangGraph</a> add state snapshots for safe multi-step workflows.</li>
</ul>

<h2>Why Sandboxes Are Essential for AI Agents</h2>

<h3>Permission Escalation & System Breakdown</h3>

<p>Agents can misinterpret commands or be tricked into running malicious code. For example:</p>

<pre><code class="language-bash"># A risky command an Agent might execute
rm -rf /etc  # Deletes critical system configs</code></pre>

<h3>Hallucination-Driven Chaos</h3>

<p>Agents often "hallucinate" non-existent resources (e.g., fake server IPs or SQL tables), leading to failed or dangerous operations.</p>

<h3>Resource Overuse</h3>

<p>Uncontrolled Agent loops can trigger thousands of API requests or CPU-heavy tasks:</p>

<pre><code class="language-python"># A loop that could spiral out of control
while True:
    agent.run("Check inventory")  # Repeats indefinitely</code></pre>

<h3>Compliance Failures</h3>

<p>In regulated industries (finance, healthcare), un-audited Agent actions violate laws like the EU AI Act, leading to massive fines.</p>

<h2>Building a Practical AI Agent Sandbox</h2>

<p>A robust sandbox combines isolation, policy control, and observability. Here's how to implement it:</p>

<h3>Step 1: MicroVM-Level Isolation with Firecracker</h3>

<p>Use microVMs (e.g., <a href="/en/tools/firecracker">Firecracker</a>) to isolate Agents at the hardware level. This prevents container or process escape.</p>

<p><em>Launch a Firecracker microVM for an Agent:</em></p>

<pre><code class="language-bash"># Install Firecracker (Linux only)
curl https://raw.githubusercontent.com/firecracker-microvm/firecracker/main/tools/install.sh | bash

# Start a microVM with an Alpine OS image
firecracker --kernel-path=vmlinux --root-drive-path=alpine-rootfs.ext4</code></pre>

<h3>Step 2: Dynamic Policy Control with OPA</h3>

<p>Use <a href="/en/tools/open-policy-agent">Open Policy Agent (OPA)</a> to enforce fine-grained permissions. Define rules for what an Agent can and cannot do.</p>

<p><em>Example OPA Policy (<code>policy.rego</code>) to restrict file access:</em></p>

<pre><code class="language-rego">package agent.sandbox

# Allow reading files only in /data/agent directory
allow[true] {
    input.action == "read_file"
    startswith(input.path, "/data/agent/")
}

# Deny all other file actions
deny[true] {
    input.action == "read_file"
    not allow
}</code></pre>

<p><em>Enforce the policy with an OPA server:</em></p>

<pre><code class="language-bash">opa run --server policy.rego</code></pre>

<h3>Step 3: State Snapshots for Rollbacks</h3>

<p>Use filesystem snapshots (e.g., Btrfs/ZFS) to roll back changes if an Agent fails:</p>

<pre><code class="language-bash"># Create a snapshot before an Agent runs (Btrfs)
btrfs subvolume snapshot -r /data/agent /data/agent_snapshot_$(date +%s)

# Run the Agent
agent run "Process data"

# Roll back if needed
btrfs subvolume delete /data/agent
btrfs subvolume snapshot /data/agent_snapshot_123456 /data/agent</code></pre>

<h3>Step 4: Full Observability with OpenTelemetry</h3>

<p>Track every Agent action with distributed tracing using <a href="/en/tools/opentelemetry">OpenTelemetry</a>:</p>

<pre><code class="language-python">from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

# Configure Jaeger exporter
resource = Resource(attributes={SERVICE_NAME: "ai-agent-sandbox"})
jaeger_exporter = JaegerExporter(
    agent_host_name="localhost",
    agent_port=6831,
)
provider = TracerProvider(resource=resource)
processor = BatchSpanProcessor(jaeger_exporter)
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

# Create a trace for an Agent action
tracer = trace.get_tracer(__name__)
with tracer.start_as_current_span("agent_task"):
    agent.run("Analyze sales data")</code></pre>

<h2>Future of AI Sandboxes</h2>

<p>Looking ahead, sandboxes will become more adaptive:</p>

<ul>
<li><strong>Self-Evolving Policies</strong>: Use reinforcement learning to update policies based on real-world feedback.</li>
<li><strong>Dynamic Capability Spectrums</strong>: Grant permissions based on real-time risk assessments (e.g., auto-approve low-risk actions, require approval for high-risk ones).</li>
<li><strong>TEE Integration</strong>: Combine with Trusted Execution Environments (e.g., Intel SGX) for ultra-secure workloads.</li>
</ul>

<h2>FAQ</h2>

<h3>Do I really need a sandbox for my AI agent? Can't I just use a Docker container?</h3>
<p>Docker containers provide namespace isolation but share the host kernel — a determined or compromised agent can potentially escape via kernel exploits. For simple, trusted agents running your own code, Docker may be sufficient. But if your agent executes arbitrary code, makes network requests, or handles sensitive data, you need microVM-level isolation (Firecracker) or a cloud sandbox service (E2B). The risk scales with agent autonomy: the more freedom you give an agent, the stronger your sandbox should be.</p>

<h3>What's the difference between E2B and Firecracker for AI agent sandboxing?</h3>
<p>E2B is a managed cloud service — you get AI-native sandboxes via API without managing infrastructure. It's ideal for SaaS products and teams that want sandboxing without ops overhead. Firecracker is the open-source microVM technology — you run and manage it yourself on your own infrastructure. Choose E2B for speed of integration and zero ops; choose Firecracker when you need full control, on-premise deployment, or cost optimization at scale.</p>

<h3>How do I monitor what my AI agents are doing inside the sandbox?</h3>
<p>Use OpenTelemetry for distributed tracing of every agent action, combined with OPA's decision logging for policy-level auditing. Together they give you a complete picture: OpenTelemetry shows what happened (traces, latency, errors), while OPA logs show what was allowed or denied and why. For production systems, ship both to a centralized observability platform like Grafana or Datadog for alerting and dashboards.</p>

<div class="next-step">
<p><strong>Next:</strong> <a href="/article/multi-agent-system-long-task">Building a Practical Multi-Agent System for Unattended Long-Task Execution →</a></p>
</div>"""

article1_zh = r"""
<div class="article-meta-banner">
<p><strong>分类：</strong> AI代理安全 · <strong>难度：</strong> 中级</p>
<p><strong>你将学到：</strong> 如何使用微虚拟机、策略引擎、状态快照和可观测性为AI代理构建沙箱——将危险的自主代理转变为生产就绪的工具。</p>
</div>

<p>随着大语言模型从单纯的文本生成器进化为能够与本地文件交互、执行代码和发起网络请求的自主AI代理，对强大的安全边界的需求变得至关重要。本文深入探讨<strong>AI代理沙箱</strong>——一种专门设计的安全基础设施，旨在管理自主AI的风险，同时支持实用的高效工作流。</p>

<h2>什么是AI代理沙箱？</h2>

<p>AI代理沙箱不仅仅是一个虚拟机或Docker容器。它是为多步AI交互量身定制的<strong>综合安全层</strong>，结合了三种核心能力：</p>

<ul>
<li><strong>闪电般快速的隔离</strong>：毫秒级启动的环境，将代理与主机系统物理分离。</li>
<li><strong>动态策略控制</strong>：实时授予或撤销权限的系统。</li>
<li><strong>可审计的可追溯性</strong>：完整记录和追踪所有代理操作，与会话上下文关联。</li>
</ul>

<h2>AI代理沙箱的演变</h2>

<p>沙箱概念已经发展了30多年，不断适应AI代理的需求：</p>

<h3>历史上的隔离技术</h3>

<ul>
<li><strong>1990年代：Java Applet</strong> — 通过基于权限的隔离实现早期沙箱（如限制文件系统访问）。</li>
<li><strong>2000年代：虚拟机（VM）</strong> — 重量级硬件级隔离（如VMware），对现代AI工作流来说太慢。</li>
<li><strong>2010年代：容器（Docker）</strong> — 轻量级命名空间隔离，但仍易受逃逸攻击。</li>
<li><strong>2020年代：微虚拟机（Firecracker）</strong> — 结合速度（毫秒启动）和强隔离，非常适合AI代理。</li>
</ul>

<h3>"裸奔部署"时代（2022-2023）</h3>

<p>早期的AI代理框架如 <a href="/zh/tools/langchain">LangChain</a> 和 <a href="/zh/tools/autogen">AutoGen</a> 缺乏合适的沙箱。代理直接在本地机器或共享容器上运行代码，导致了灾难：</p>

<ul>
<li>通过 <code>rm -rf /</code> 意外删除系统文件。</li>
<li>API密钥和环境变量泄露。</li>
<li>不受控制的API请求循环（如数千次冗余调用）。</li>
</ul>

<p><em>一个危险的设置示例（<strong>绝不要在生产环境中使用</strong>）：</em></p>

<pre><code class="language-python"># 早期的LangChain代码，没有沙箱
from langchain.agents import initialize_agent, Tool
from langchain.utilities import BashProcess

bash_tool = Tool(
    name="Bash",
    func=BashProcess().run,
    description="Run bash commands"
)
agent = initialize_agent([bash_tool], llm, agent="zero-shot-react-description")
agent.run("Delete all logs in /var/log")  # 高风险！</code></pre>

<h3>现代沙箱技术（2023至今）</h3>

<p>工业界和学术界现在都将沙箱作为优先事项：</p>

<ul>
<li><strong>学术界</strong>：AgentBench等基准测试要求可重复的隔离环境。</li>
<li><strong>工业界</strong>：<a href="/zh/tools/e2b">E2B</a>等服务提供AI原生的云端隔离沙箱。</li>
<li><strong>开源</strong>：<a href="/zh/tools/langgraph">LangGraph</a>等框架为安全的多步工作流添加了状态快照。</li>
</ul>

<h2>为什么沙箱对AI代理至关重要</h2>

<h3>权限提升与系统崩溃</h3>

<p>代理可能误解命令或被诱导运行恶意代码。例如：</p>

<pre><code class="language-bash"># 代理可能执行的危险命令
rm -rf /etc  # 删除关键系统配置</code></pre>

<h3>幻觉驱动的混乱</h3>

<p>代理经常"幻觉"出不存在的资源（如虚假的服务器IP或SQL表），导致失败或危险的操作。</p>

<h3>资源过度消耗</h3>

<p>不受控制的代理循环可能触发数千次API请求或CPU密集型任务：</p>

<pre><code class="language-python"># 可能失控的循环
while True:
    agent.run("Check inventory")  # 无限重复</code></pre>

<h3>合规失败</h3>

<p>在受监管行业（金融、医疗），未经审计的代理操作违反欧盟AI法案等法律，导致巨额罚款。</p>

<h2>构建实用的AI代理沙箱</h2>

<p>一个强大的沙箱结合了隔离、策略控制和可观测性。以下是实现方法：</p>

<h3>第一步：使用Firecracker实现微虚拟机级隔离</h3>

<p>使用微虚拟机（如 <a href="/zh/tools/firecracker">Firecracker</a>）在硬件级别隔离代理。这可以防止容器或进程逃逸。</p>

<p><em>为代理启动Firecracker微虚拟机：</em></p>

<pre><code class="language-bash"># 安装Firecracker（仅Linux）
curl https://raw.githubusercontent.com/firecracker-microvm/firecracker/main/tools/install.sh | bash

# 使用Alpine OS镜像启动微虚拟机
firecracker --kernel-path=vmlinux --root-drive-path=alpine-rootfs.ext4</code></pre>

<h3>第二步：使用OPA实现动态策略控制</h3>

<p>使用 <a href="/zh/tools/open-policy-agent">Open Policy Agent（OPA）</a> 强制执行细粒度权限。定义代理可以和不可以做什么的规则。</p>

<p><em>限制文件访问的OPA策略示例（<code>policy.rego</code>）：</em></p>

<pre><code class="language-rego">package agent.sandbox

# 只允许读取 /data/agent 目录中的文件
allow[true] {
    input.action == "read_file"
    startswith(input.path, "/data/agent/")
}

# 拒绝所有其他文件操作
deny[true] {
    input.action == "read_file"
    not allow
}</code></pre>

<p><em>使用OPA服务器强制执行策略：</em></p>

<pre><code class="language-bash">opa run --server policy.rego</code></pre>

<h3>第三步：状态快照实现回滚</h3>

<p>使用文件系统快照（如Btrfs/ZFS），在代理失败时回滚更改：</p>

<pre><code class="language-bash"># 代理运行前创建快照（Btrfs）
btrfs subvolume snapshot -r /data/agent /data/agent_snapshot_$(date +%s)

# 运行代理
agent run "Process data"

# 需要时回滚
btrfs subvolume delete /data/agent
btrfs subvolume snapshot /data/agent_snapshot_123456 /data/agent</code></pre>

<h3>第四步：使用OpenTelemetry实现全面可观测性</h3>

<p>使用 <a href="/zh/tools/opentelemetry">OpenTelemetry</a> 通过分布式追踪记录每个代理操作：</p>

<pre><code class="language-python">from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

# 配置Jaeger导出器
resource = Resource(attributes={SERVICE_NAME: "ai-agent-sandbox"})
jaeger_exporter = JaegerExporter(
    agent_host_name="localhost",
    agent_port=6831,
)
provider = TracerProvider(resource=resource)
processor = BatchSpanProcessor(jaeger_exporter)
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

# 为代理操作创建追踪
tracer = trace.get_tracer(__name__)
with tracer.start_as_current_span("agent_task"):
    agent.run("Analyze sales data")</code></pre>

<h2>AI沙箱的未来</h2>

<p>展望未来，沙箱将变得更加自适应：</p>

<ul>
<li><strong>自进化策略</strong>：使用强化学习基于真实反馈更新策略。</li>
<li><strong>动态能力范围</strong>：基于实时风险评估授予权限（如自动批准低风险操作，高风险操作需要审批）。</li>
<li><strong>TEE集成</strong>：结合可信执行环境（如Intel SGX）实现超安全工作负载。</li>
</ul>

<h2>常见问题</h2>

<h3>我的AI代理真的需要沙箱吗？不能只用Docker容器吗？</h3>
<p>Docker容器提供命名空间隔离但共享主机内核——一个被入侵的代理可能通过内核漏洞逃逸。对于运行自己代码的简单可信代理，Docker可能足够。但如果你的代理执行任意代码、发起网络请求或处理敏感数据，你需要微虚拟机级隔离（Firecracker）或云端沙箱服务（E2B）。风险随代理自主性增加：你给代理的自由越多，沙箱就应该越强。</p>

<h3>E2B和Firecracker在AI代理沙箱方面有什么区别？</h3>
<p>E2B是托管云服务——你通过API获得AI原生沙箱，无需管理基础设施。它适合SaaS产品和想要沙箱功能但不想承担运维负担的团队。Firecracker是开源微虚拟机技术——你在自己的基础设施上运行和管理它。选择E2B以快速集成和零运维；当你需要完全控制、本地部署或大规模成本优化时选择Firecracker。</p>

<h3>如何监控我的AI代理在沙箱内的行为？</h3>
<p>使用OpenTelemetry对每个代理操作进行分布式追踪，结合OPA的决策日志进行策略级审计。两者结合给你完整的画面：OpenTelemetry显示发生了什么（追踪、延迟、错误），而OPA日志显示什么被允许或拒绝以及原因。对于生产系统，将两者发送到Grafana或Datadog等集中式可观测性平台进行告警和仪表板展示。</p>

<div class="next-step">
<p><strong>下一步：</strong> <a href="/article/multi-agent-system-long-task">构建实用的多代理系统：无人值守长任务执行 →</a></p>
</div>"""

# Article 2: Multi-Agent System
article2_en = r"""
<div class="article-meta-banner">
<p><strong>Category:</strong> AI Agent Architecture · <strong>Difficulty:</strong> Advanced</p>
<p><strong>What you'll learn:</strong> How to build a graph-based multi-agent orchestration system that ran unattended for 4 days, processing 416 tasks and generating 140,000 lines of production code.</p>
</div>

<p>In the realm of AI development, building a multi-agent system that can handle long tasks unattended is a challenging yet rewarding endeavor. This article delves into a practical case where a multi-agent system ran unattended for 4 days, generating 140,000 lines of code. We'll explore the architecture, key techniques, and practical steps to replicate such a system.</p>

<h2>The Challenge of Long-Task Execution in AI</h2>

<p>When dealing with complex, long-running tasks, AI models often suffer from context forgetting. As the task progresses, earlier details get pushed out of the context window, causing the task to deviate. Even models with large context windows only delay this forgetting curve rather than eliminating it.</p>

<p>To address this, the solution is to <strong>break tasks into small chunks, maintain clean context for each chunk, and have agents hand off tasks after completion</strong>.</p>

<h2>Architecture: Graph-Based Orchestration of Agents</h2>

<p>The system uses a graph-based approach to orchestrate multiple agents. Each node in the graph is an agent, and edges represent the transfer of structured data between agents.</p>

<ul>
<li><strong>Node Responsibility</strong>: Each node (agent) is responsible for only one specific task, such as analysis, coding, testing, etc.</li>
<li><strong>Communication</strong>: Agents don't have free-form conversations. They transfer predefined structured data. For example, when a coding agent finishes, it hands off a structured object containing code details, modification logs, and the next step to the testing agent.</li>
</ul>

<p>Here's a simplified example of how the orchestration can be defined in a YAML file (a core configuration file for the system):</p>

<pre><code class="language-yaml">pipeline:
  - name: analyzer
    type: agent
    responsibility: task analysis
    next: [coder]
  - name: coder
    type: agent
    responsibility: code generation
    next: [tester, quality_gate]
  - name: tester
    type: agent
    responsibility: code testing
    next: [reviewer]
  - name: quality_gate
    type: agent
    responsibility: code quality check
    after: tester
    next: [reviewer]
  - name: reviewer
    type: agent
    responsibility: code review
    next: [committer]
  - name: committer
    type: agent
    responsibility: code commit</code></pre>

<h2>Key Components and Their Roles</h2>

<h3>1. Codex: The Orchestrator</h3>

<p><a href="/en/tools/codex">Codex</a> acts as the brain of the system. Its responsibilities include:</p>

<ul>
<li><strong>Task Allocation</strong>: It takes high-level tasks (like an issue or voice command) and generates a structured task draft.</li>
<li><strong>Graph Initiation</strong>: It selects a YAML template based on the task type and initiates the pipeline.</li>
<li><strong>Monitoring and Fallback</strong>: It continuously polls the status of each node, monitors for failures, and can intervene (like stopping or rolling back) when necessary.</li>
</ul>

<h3>2. YAML: The Core Interface</h3>

<p>YAML is not just a configuration file; it's the core interface that defines the entire orchestration logic. It includes:</p>

<ul>
<li><strong>Topology</strong>: Defines the structure of the agent graph (serial, parallel, fan-out, fan-in, etc.).</li>
<li><strong>Agent Definition</strong>: Specifies the role, responsibility, and system prompt of each agent.</li>
<li><strong>Model Profile</strong>: Defines which AI model each agent uses (useful for cost optimization).</li>
<li><strong>Environment</strong>: Specifies the Docker image for each agent (e.g., a coding agent might use a basic worker image, while a frontend testing agent uses an image with Chrome and Puppeteer).</li>
</ul>

<h3>3. Scorecard: The Audit Layer</h3>

<p>To ensure the reliability of the system, a Scorecard layer is introduced. Instead of just trusting an agent's claim of "task completed", Scorecard verifies against real records:</p>

<ul>
<li><strong>Node Handoff Check</strong>: Ensures the handoff format between nodes is correct.</li>
<li><strong>Command Execution Check</strong>: Verifies that test commands have actual outputs.</li>
<li><strong>PR Association Check</strong>: Ensures pull requests are linked to the correct issues.</li>
</ul>

<h2>Practical Implementation Steps</h2>

<h3>1. Set Up the Orchestration Graph</h3>

<p>Define your pipeline in a YAML file as shown earlier. This file should be version-controlled.</p>

<h3>2. Implement Agents</h3>

<p>Each agent should be a standalone module with a clear system prompt. For example, a coder agent's system prompt might look like this:</p>

<pre><code class="language-text">You are a senior software developer specializing in TypeScript.
Your task is to convert Python modules to TypeScript, ensuring
type safety and adherence to the defined API contracts. After
coding, you must generate a structured handoff including code,
modification details, and the next steps.</code></pre>

<h3>3. Deploy the Environment</h3>

<p>Use <a href="/en/tools/docker">Docker</a> to containerize each agent's environment. For a frontend testing agent, the Dockerfile might be:</p>

<pre><code class="language-dockerfile">FROM node:18
RUN npm install -g puppeteer
COPY test-scripts /app/test-scripts
CMD ["node", "/app/test-scripts/run-tests.js"]</code></pre>

<h3>4. Set Up Monitoring with Codex</h3>

<p>Write a Python script for Codex to monitor the pipeline:</p>

<pre><code class="language-python">import requests
import time

def monitor_pipeline(pipeline_id):
    while True:
        response = requests.get(f"http://api.example.com/pipeline/{pipeline_id}/status")
        status = response.json()["status"]
        if status in ["completed", "failed"]:
            break
        print(f"Pipeline status: {status}")
        time.sleep(30)  # Poll every 30 seconds
    print(f"Pipeline finished with status: {status}")

# Initiate the pipeline and get the ID
pipeline_response = requests.post("http://api.example.com/pipeline", json={"task": "TS refactoring"})
pipeline_id = pipeline_response.json()["pipeline_id"]
monitor_pipeline(pipeline_id)</code></pre>

<h2>Performance and Optimization</h2>

<p>In the 4-day unattended run:</p>

<ul>
<li><strong>Task Volume</strong>: 416 tasks were executed, 374 completed successfully.</li>
<li><strong>Code Output</strong>: 140,000 lines of code were generated, with 516 files committed.</li>
<li><strong>Token Usage</strong>: 1.29 billion tokens were consumed, mostly by worker agents.</li>
</ul>

<h3>Optimization Tips</h3>

<ul>
<li><strong>Codex Monitoring Frequency</strong>: Initially, Codex's monitoring was too frequent, leading to high costs. Adjust the polling interval based on task urgency.</li>
<li><strong>Parallel Pipelines</strong>: The initial setup was serial. For better efficiency, design multiple pipelines to run in parallel, each handling a different module.</li>
<li><strong>Environment Isolation</strong>: Use Docker Compose to manage multi-container environments for complex tasks.</li>
</ul>

<h2>FAQ</h2>

<h3>How do you prevent agents from hallucinating during long unattended runs?</h3>
<p>Three techniques work together: (1) <strong>Chunking</strong> — break work into small, verifiable units so each agent has a clean, focused context. (2) <strong>Structured handoffs</strong> — agents pass predefined data structures, not free-text, reducing ambiguity. (3) <strong>Scorecard verification</strong> — every agent output is checked against real records (test outputs, PR links, commit hashes) before the pipeline continues. These three layers mean a hallucination gets caught at the handoff boundary rather than cascading through the entire pipeline.</p>

<h3>What's the minimum team size needed to set up a system like this?</h3>
<p>One experienced developer can set up a basic version in about a week. You need familiarity with YAML for pipeline definitions, Docker for agent environments, and a basic understanding of how to write agent system prompts. The complexity scales with the number of agent types and the variety of tasks you want to handle. Start with a simple 3-agent pipeline (analyzer → coder → reviewer) for a single task type, then expand.</p>

<h3>How do you control costs with 1.29 billion tokens consumed?</h3>
<p>Token costs are dominated by worker agents, not the orchestrator. Key strategies: (1) Use cheaper models for routine tasks (e.g., Haiku for code formatting, Opus only for complex architecture decisions). (2) Adjust Codex's polling interval — polling every 5 seconds vs every 30 seconds makes a big difference over 4 days. (3) Implement early termination — if a coder agent produces output that fails the quality gate twice, stop and escalate rather than retrying indefinitely. (4) Cache and reuse results — if two tasks require the same analysis step, run it once and share the output.</p>

<div class="next-step">
<p><strong>Next:</strong> <a href="/article/ai-agent-sandbox-guide">AI Agent Sandbox: A Practical Guide to Secure Autonomous Action →</a></p>
</div>"""

article2_zh = r"""
<div class="article-meta-banner">
<p><strong>分类：</strong> AI代理架构 · <strong>难度：</strong> 高级</p>
<p><strong>你将学到：</strong> 如何构建基于图的多代理编排系统，该系统无人值守运行4天，处理416个任务，生成14万行生产代码。</p>
</div>

<p>在AI开发领域，构建能够无人值守处理长任务的多代理系统是一项具有挑战性但回报丰厚的努力。本文深入探讨一个实战案例——一个多代理系统无人值守运行了4天，生成了14万行代码。我们将探索其架构、关键技术和复现该系统的实践步骤。</p>

<h2>AI长任务执行的挑战</h2>

<p>处理复杂的长运行任务时，AI模型经常遭受上下文遗忘的困扰。随着任务推进，早期的细节被推出上下文窗口，导致任务偏离。即使拥有大上下文窗口的模型也只是推迟了遗忘曲线，而非消除它。</p>

<p>解决方法是：<strong>将任务分解为小块，为每块保持干净的上下文，并让代理在完成后进行任务交接</strong>。</p>

<h2>架构：基于图的多代理编排</h2>

<p>该系统使用基于图的方法来编排多个代理。图中的每个节点是一个代理，边代表代理之间结构化数据的传输。</p>

<ul>
<li><strong>节点职责</strong>：每个节点（代理）只负责一个特定任务，如分析、编码、测试等。</li>
<li><strong>通信方式</strong>：代理之间没有自由对话。它们传输预定义的结构化数据。例如，当编码代理完成时，它向测试代理交接一个包含代码详情、修改日志和下一步的结构化对象。</li>
</ul>

<p>以下是如何在YAML文件（系统的核心配置文件）中定义编排的简化示例：</p>

<pre><code class="language-yaml">pipeline:
  - name: analyzer
    type: agent
    responsibility: task analysis
    next: [coder]
  - name: coder
    type: agent
    responsibility: code generation
    next: [tester, quality_gate]
  - name: tester
    type: agent
    responsibility: code testing
    next: [reviewer]
  - name: quality_gate
    type: agent
    responsibility: code quality check
    after: tester
    next: [reviewer]
  - name: reviewer
    type: agent
    responsibility: code review
    next: [committer]
  - name: committer
    type: agent
    responsibility: code commit</code></pre>

<h2>关键组件及其角色</h2>

<h3>1. Codex：编排器</h3>

<p><a href="/zh/tools/codex">Codex</a> 充当系统的大脑。其职责包括：</p>

<ul>
<li><strong>任务分配</strong>：接收高层任务（如issue或语音命令）并生成结构化的任务草稿。</li>
<li><strong>图初始化</strong>：根据任务类型选择YAML模板并启动管道。</li>
<li><strong>监控与回退</strong>：持续轮询每个节点的状态，监控失败情况，并在必要时进行干预（如停止或回滚）。</li>
</ul>

<h3>2. YAML：核心接口</h3>

<p>YAML不仅仅是配置文件，它是定义整个编排逻辑的核心接口。包括：</p>

<ul>
<li><strong>拓扑结构</strong>：定义代理图的结构（串行、并行、扇出、扇入等）。</li>
<li><strong>代理定义</strong>：指定每个代理的角色、职责和系统提示。</li>
<li><strong>模型配置</strong>：定义每个代理使用哪个AI模型（用于成本优化）。</li>
<li><strong>环境</strong>：指定每个代理的Docker镜像（如编码代理可能使用基础工作镜像，而前端测试代理使用包含Chrome和Puppeteer的镜像）。</li>
</ul>

<h3>3. Scorecard：审计层</h3>

<p>为确保系统可靠性，引入了Scorecard层。不再仅仅信任代理声称的"任务完成"，Scorecard根据真实记录进行验证：</p>

<ul>
<li><strong>节点交接检查</strong>：确保节点之间的交接格式正确。</li>
<li><strong>命令执行检查</strong>：验证测试命令有实际输出。</li>
<li><strong>PR关联检查</strong>：确保Pull Request关联到正确的Issue。</li>
</ul>

<h2>实践实现步骤</h2>

<h3>1. 设置编排图</h3>

<p>如上所示在YAML文件中定义你的管道。该文件应该进行版本控制。</p>

<h3>2. 实现代理</h3>

<p>每个代理应该是一个独立模块，具有清晰的系统提示。例如，编码代理的系统提示可能如下：</p>

<pre><code class="language-text">你是一位专注于TypeScript的高级软件开发者。
你的任务是将Python模块转换为TypeScript，确保
类型安全并遵循定义的API契约。编码完成后，
你必须生成包含代码、修改详情和下一步的
结构化交接信息。</code></pre>

<h3>3. 部署环境</h3>

<p>使用 <a href="/zh/tools/docker">Docker</a> 容器化每个代理的环境。对于前端测试代理，Dockerfile可能是：</p>

<pre><code class="language-dockerfile">FROM node:18
RUN npm install -g puppeteer
COPY test-scripts /app/test-scripts
CMD ["node", "/app/test-scripts/run-tests.js"]</code></pre>

<h3>4. 使用Codex设置监控</h3>

<p>编写Python脚本让Codex监控管道：</p>

<pre><code class="language-python">import requests
import time

def monitor_pipeline(pipeline_id):
    while True:
        response = requests.get(f"http://api.example.com/pipeline/{pipeline_id}/status")
        status = response.json()["status"]
        if status in ["completed", "failed"]:
            break
        print(f"Pipeline status: {status}")
        time.sleep(30)  # 每30秒轮询一次
    print(f"Pipeline finished with status: {status}")

# 启动管道并获取ID
pipeline_response = requests.post("http://api.example.com/pipeline", json={"task": "TS refactoring"})
pipeline_id = pipeline_response.json()["pipeline_id"]
monitor_pipeline(pipeline_id)</code></pre>

<h2>性能与优化</h2>

<p>在4天的无人值守运行中：</p>

<ul>
<li><strong>任务量</strong>：执行了416个任务，374个成功完成。</li>
<li><strong>代码产出</strong>：生成了14万行代码，提交了516个文件。</li>
<li><strong>Token消耗</strong>：消耗了12.9亿tokens，主要由工作代理使用。</li>
</ul>

<h3>优化技巧</h3>

<ul>
<li><strong>Codex监控频率</strong>：最初Codex的监控过于频繁，导致成本高昂。根据任务紧急程度调整轮询间隔。</li>
<li><strong>并行管道</strong>：初始设置是串行的。为提高效率，设计多个并行运行的管道，每个处理不同的模块。</li>
<li><strong>环境隔离</strong>：使用Docker Compose管理复杂任务的多容器环境。</li>
</ul>

<h2>常见问题</h2>

<h3>如何在长时间无人值守运行中防止代理产生幻觉？</h3>
<p>三种技术协同工作：（1）<strong>分块</strong>——将工作分解为小的、可验证的单元，使每个代理拥有干净、专注的上下文。（2）<strong>结构化交接</strong>——代理传递预定义的数据结构，而非自由文本，减少歧义。（3）<strong>Scorecard验证</strong>——每个代理的输出在管道继续前都根据真实记录（测试输出、PR链接、提交哈希）进行检查。这三层意味着幻觉在交接边界被捕获，而不是级联到整个管道。</p>

<h3>建立这样的系统需要多大的团队？</h3>
<p>一位有经验的开发者可以在一周内搭建基本版本。你需要熟悉YAML用于管道定义，Docker用于代理环境，以及基本的代理系统提示编写能力。复杂度随代理类型数量和你想处理的任务种类而增长。从简单的3代理管道（分析器→编码器→审查器）开始处理单一任务类型，然后逐步扩展。</p>

<h3>如何控制在消耗12.9亿tokens的情况下的成本？</h3>
<p>Token成本主要由工作代理而非编排器产生。关键策略：（1）对常规任务使用更便宜的模型（如用Haiku做代码格式化，只在复杂架构决策时用Opus）。（2）调整Codex的轮询间隔——每5秒轮询vs每30秒轮询在4天内有巨大差异。（3）实施提前终止——如果编码代理的输出两次未通过质量门，停止并升级，而不是无限重试。（4）缓存和复用结果——如果两个任务需要相同的分析步骤，运行一次并共享输出。</p>

<div class="next-step">
<p><strong>下一步：</strong> <a href="/article/ai-agent-sandbox-guide">AI代理沙箱：安全自主行动的实践指南 →</a></p>
</div>"""

# Insert content before the closing "};"
last_content_end = content_src.rfind("};")
assert last_content_end > 0, "Could not find end of articleContents"

new_content = f"""
  // ====== Article: AI Agent Sandbox Guide ======
  "ai-agent-sandbox-guide": {{
    content: `{article1_en}`,
    contentZh: `{article1_zh}`,
  }},

  // ====== Article: Multi-Agent System for Long Tasks ======
  "multi-agent-system-long-task": {{
    content: `{article2_en}`,
    contentZh: `{article2_zh}`,
  }},
}};
"""

content_src = content_src[:last_content_end] + new_content

with open(content_file, "w", encoding="utf-8") as f:
    f.write(content_src)

print("Added 2 articles to article-content.ts")
print("DONE!")
