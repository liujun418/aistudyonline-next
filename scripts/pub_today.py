"""
Publish June 30, 2026 articles.
New tools: kouzi (ByteDance agent platform), veo-3-1 (Google video model)
"""
import os

BASE = r"C:\Users\jun\aistudyonline-next"
os.chdir(BASE)

# ===== Part 1: Add 2 new tools to tools.ts =====
with open('src/lib/tools.ts', 'r', encoding='utf-8') as f:
    tools_src = f.read()

new_tools = r"""  {
    id: "kouzi",
    name: "Kouzi (Coze)",
    description: "ByteDance's no-code AI agent building platform — assemble LLMs, tools, knowledge bases, and workflows into working AI agents. No coding required.",
    descriptionZh: "字节跳动无代码AI Agent搭建平台——将LLM、工具、知识库和工作流组装成可工作的AI Agent，无需编程。",
    category: "productivity",
    tags: ["agent", "no-code", "workflow", "bot-building", "bytedance"],
    difficulty: "beginner",
    url: "https://www.coze.com",
    rating: r(4.3),
    pricing: "Free tier + Pro",
    useCase: "Build custom AI agents without coding — pick an LLM brain, add internet search and knowledge bases, create SOP workflows, and package everything into an intelligent agent that actually gets things done.",
    icon: "\u{1F9E9}",
    company: "ByteDance",
    companyZh: "字节跳动",
    founded: "2012",
    headquarters: "Beijing, China",
    descriptionLong: "Kouzi (扣子, international version: Coze) is ByteDance's no-code AI agent building platform that lets anyone assemble working AI solutions without programming. Think of it as a 'super factory' for intelligent agents: you pick an LLM as the brain (Doubao, ChatGPT, etc.), add tools and senses (internet search, knowledge bases, image/audio/video generators), create workflows as SOPs, and package everything into an agent that autonomously executes tasks. It supports multi-turn dialogue, tool calling, and workflow orchestration. The platform is particularly popular in China's AI ecosystem, powering chatbots, customer service agents, content creation pipelines, and research assistants. Unlike coding frameworks like LangChain, Kouzi is visual and drag-and-drop — you assemble agents like building blocks. The free tier is generous enough for most individual use cases, with Pro plans for commercial deployment.",
    descriptionLongZh: "扣子（国际版：Coze）是字节跳动的无代码AI Agent搭建平台，让任何人都能无需编程组装可工作的AI解决方案。可以把它想象成智能Agent的'超级工厂'：选一个LLM做大脑（豆包、ChatGPT等），添加工具和感官（互联网搜索、知识库、图像/音频/视频生成器），创建工作流作为SOP，将所有内容打包成一个自主执行任务的Agent。它支持多轮对话、工具调用和工作流编排。该平台在中国AI生态中特别流行，驱动聊天机器人、客服Agent、内容创作管道和研究助手。与LangChain等编码框架不同，扣子是可视化和拖拽式的——你像搭积木一样组装Agent。免费版对大多数个人用例足够慷慨，专业版用于商业部署。",
    advantages: ["No-code visual builder", "ByteDance ecosystem integration", "Rich plugin/tool marketplace", "Workflow orchestration", "Generous free tier"],
    advantagesZh: ["无代码可视化搭建", "字节跳动生态集成", "丰富插件/工具市场", "工作流编排", "慷慨免费额度"],
    useCases: ["Custom AI chatbots", "Customer service agents", "Content creation pipelines", "Research assistants", "Task automation bots"],
    useCasesZh: ["定制AI聊天机器人", "客服Agent", "内容创作管道", "研究助手", "任务自动化机器人"],
    targetAudience: "Non-programmers who want to build AI agents, businesses needing custom AI solutions without development teams, content creators automating workflows, and anyone wanting to experiment with AI agent construction.",
    targetAudienceZh: "想构建AI Agent的非程序员、需要无开发团队定制AI解决方案的企业、自动化工作流的内容创作者、以及任何想实验AI Agent构建的人。",
    pricingTiers: [
      {tier: "Free", tierZh: "免费版", price: "$0", features: ["Basic agent builder", "Limited API calls", "Community plugins"], featuresZh: ["基础Agent搭建", "有限API调用", "社区插件"]},
      {tier: "Pro", tierZh: "专业版", price: "Custom", features: ["Unlimited agents", "Advanced workflows", "Team collaboration", "Commercial deployment"], featuresZh: ["无限Agent", "高级工作流", "团队协作", "商业部署"]}
    ],
    pros: ["Truly no-code", "Visual and intuitive", "ByteDance quality", "Rich ecosystem", "Great for prototyping"],
    prosZh: ["真正无代码", "可视化直观", "字节跳动品质", "丰富生态", "适合原型设计"],
    cons: ["Limited customization vs coding", "ByteDance ecosystem lock-in", "International version differs from Chinese"],
    consZh: ["定制化不如编码灵活", "字节生态锁定", "国际版与国内版有差异"],
    extensions: [],
    skills: [],
    scene: "productivity",
  },
  {
    id: "veo-3-1",
    name: "Veo 3.1",
    description: "Google's top-tier AI video generation model — perfect audio-visual synchronization, natural motion, and high-quality output at ~$1.90 per 5 seconds.",
    descriptionZh: "Google顶级AI视频生成模型——完美声画同步、自然运动、高质量输出，约¥14/5秒。",
    category: "video-generation",
    tags: ["video-generation", "google", "text-to-video", "audio-visual"],
    difficulty: "beginner",
    url: "https://deepmind.google/technologies/veo/",
    rating: r(4.5),
    pricing: "Pay-per-use (~$1.90/5s)",
    useCase: "Veo 3.1 is Google's latest video generation model with perfect audio-visual synchronization — ideal for producing polished marketing videos, social media content, and creative projects with natural motion quality.",
    icon: "\u{1F3AC}",
    company: "Google DeepMind",
    companyZh: "Google DeepMind",
    founded: "2010",
    headquarters: "London, UK",
    descriptionLong: "Veo 3.1 is Google DeepMind's latest and most advanced AI video generation model, representing a significant leap in AI video quality. Its standout feature is perfect audio-visual synchronization — generated videos have sound and picture that match naturally, with motion quality that approaches cinematic standards. Priced at approximately ¥14 ($1.90) per 5 seconds of generated video, it offers competitive pricing for professional-grade output. The model excels at producing polished marketing videos, social media content, and creative projects. It competes directly with ByteDance's Seedance series and OpenAI's Sora. For cost-effective alternatives, Seedance-1.5-Pro offers similar quality at ¥4 per 5 seconds, and the open-source Wan 2.2 provides rich features comparable to closed-source tools. For character-based video production with reference images, KeLing and Vidu are solid alternatives.",
    descriptionLongZh: "Veo 3.1 是 Google DeepMind 最新和最先进的 AI 视频生成模型，代表了 AI 视频质量的重大飞跃。其突出特点是完美的声画同步——生成的视频音画自然匹配，运动质量接近电影级标准。定价约 ¥14（$1.90）/5秒生成视频，为专业级输出提供有竞争力的价格。该模型擅长制作精致的营销视频、社交媒体内容和创意项目。它与字节跳动的 Seedance 系列和 OpenAI 的 Sora 直接竞争。对于性价比替代方案，Seedance-1.5-Pro 以 ¥4/5秒提供相似质量，开源 Wan 2.2 提供与闭源工具媲美的丰富功能。对于带参考图的角色视频制作，可灵和 Vidu 是可靠的替代选择。",
    advantages: ["Perfect audio-visual sync", "Cinematic motion quality", "Google DeepMind R&D", "Competitive pricing"],
    advantagesZh: ["完美声画同步", "电影级运动质量", "Google DeepMind研发", "有竞争力定价"],
    useCases: ["Marketing video production", "Social media content", "Creative filmmaking", "Product demos", "Educational videos"],
    useCasesZh: ["营销视频制作", "社交媒体内容", "创意电影制作", "产品演示", "教育视频"],
    targetAudience: "Video content creators, marketers, filmmakers, and businesses needing high-quality AI-generated video with natural audio-visual synchronization for professional use.",
    targetAudienceZh: "视频内容创作者、营销人员、电影制作人、以及需要高质量AI生成视频（具有自然声画同步）用于专业用途的企业。",
    pricingTiers: [{tier: "Pay-per-use", tierZh: "按量付费", price: "~$1.90/5s", features: ["Full video generation", "Audio-visual sync", "HD output"], featuresZh: ["完整视频生成", "声画同步", "高清输出"]}],
    pros: ["Best-in-class audio-visual sync", "Google quality", "Natural motion", "Competitive per-second cost"],
    prosZh: ["顶级声画同步", "Google品质", "自然运动", "有竞争力每秒成本"],
    cons: ["Pay-per-use only (no free tier)", "Less accessible in China", "Fewer style options than competitors"],
    consZh: ["仅按量付费(无免费版)", "国内访问不便", "风格选项少于竞品"],
    extensions: [],
    skills: [],
    scene: "video",
  },

"""

last_tool = tools_src.rfind('] as Tool[];')
tools_new = tools_src[:last_tool] + new_tools + '] as Tool[];'

with open('src/lib/tools.ts', 'w', encoding='utf-8') as f:
    f.write(tools_new)

print('Part 1: 2 new tools added to tools.ts (kouzi, veo-3-1)')

# ===== Part 2: Add 2 article metadata to articles.ts =====
with open('src/lib/articles.ts', 'r', encoding='utf-8') as f:
    articles_src = f.read()

new_articles = r"""  {
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
  "demystifying-ai-application-layer-3-layers": {
    content: `<div class="meta-banner">
<p><strong>📅 Published:</strong> June 30, 2026 · <strong>🏷️ Category:</strong> AI Basics · <strong>📊 Level:</strong> Beginner · <strong>🛠️ Tools:</strong> ChatGPT, Gemini, DeepSeek, Qwen, Nano Banana Pro, Midjourney, Veo 3.1, Suno, HeyGen, NotebookLM, Kouzi</p>
</div>

<p>Are you only using AI as a chat tool or a more intelligent browser? Do you still struggle to understand what AI large models, intelligent agents, and AI workflows really are? This guide will break down the underlying logic of the AI application layer in the most accessible way, even for complete AI beginners.</p>

<h2>The 3-Layer Pyramid of AI Applications</h2>

<p>To avoid confusion, let's structure all AI products into a 3-layer pyramid:</p>

<ol>
<li><strong>Core Brain (Large Language Models - LLM)</strong></li>
<li><strong>Senses & Limbs (Multimodal Models)</strong></li>
<li><strong>Skeleton & Tools (Internet, Knowledge Bases, Workflows, Intelligent Agents)</strong></li>
</ol>

<p>These three layers determine what AI can actually do for you.</p>

<h2>Layer 1: The Core Brain — Large Language Models (LLM)</h2>

<p>LLMs are the "brain" of AI. Think of them as a professor who knows everything — they can answer any question quickly and have a perfect memory. Popular LLMs include DeepSeek, Doubao, Qwen 3, ChatGPT, and Gemini 3.0.</p>

<h3>Key Capabilities</h3>
<ul>
<li>Process text and logical thinking</li>
<li>Act as a central hub for understanding and generating information</li>
</ul>

<h3>Critical Limitations</h3>
<ol>
<li><strong>Knowledge Limitations:</strong> Time lag — an LLM trained last month won't know what happened this month. Scope — LLMs don't know your personal or company-specific data. Ask Doubao about <em>your</em> next week's work plan, and it will make things up because that data isn't in its training set.</li>
<li><strong>Passive Nature:</strong> LLMs only respond when asked. They won't proactively provide information unless prompted.</li>
</ol>

<h3>Mastering Prompts</h3>
<p>The key to working with LLMs is writing good prompts. A prompt's essence is: <em>Don't let the model guess who you are.</em> Be specific about context, goals, and constraints.</p>

<pre><code class="language-plaintext">You are a career coach. I'm a 28-year-old marketing
specialist with 5 years of experience in digital marketing.
I want to transition into product management. My strengths
are data analysis and user research. Please create a 1-year
career transition plan, including skills to learn and job
search strategies.</code></pre>

<h2>Layer 2: Senses & Limbs — Multimodal Models</h2>

<p>Multimodal models are AI's "senses and limbs" — they let AI see, hear, speak, and create. Think of them as giving the LLM "a painter's hands, a director's eyes, and a singer's voice."</p>

<ul>
<li>Generate images (Nano Banana Pro, Midjourney), videos (Veo 3.1, Sora 2), audio (IndexTTS, Suno), and digital humans (HeyGen)</li>
<li>Enable AI to interact with text, images, audio, and video</li>
</ul>

<p><strong>Limitation:</strong> Multimodal models still inherit the LLM's flaws — no real-time data, no personal/company information access, and they're still passive until instructed.</p>

<h2>Layer 3: Skeleton & Tools</h2>

<p>This layer adds "skeleton and tools" to AI, solving its limitations in real-time data, personalization, and proactivity.</p>

<h3>1. Internet Search Tools</h3>
<p>To fix the LLM's time lag, we give it internet access. When you ask Doubao "What's the news today?" it runs a web search — like "plugging the professor into the internet."</p>

<h3>2. Knowledge Bases</h3>
<p>To add personal/company data, use knowledge bases (NotebookLM, IMA). Upload a contract and ask:</p>

<pre><code class="language-plaintext">Analyze this contract for potential risks, specifically
focusing on payment terms and liability clauses.</code></pre>

<p>The LLM will answer based on <em>your</em> actual data, not made-up information.</p>

<h3>3. Workflows (Standard Operating Procedures)</h3>
<p>Workflows turn AI into a "factory line worker" — they enforce consistent steps to ensure stability. Example: Creating a Viral Article Workflow:</p>
<ol>
<li>Search for hot topics on Toutiao in a specific niche</li>
<li>Extract the title style of the top 3 articles</li>
<li>Imitate that style to write an article that fits your personal brand</li>
</ol>
<p>This turns "unpredictable creativity" into a "reliable assembly line."</p>

<h3>4. Intelligent Agents</h3>
<p>Intelligent agents are like "project managers" — they think independently, plan, and act. Unlike workflows (which follow fixed steps), agents decide <em>which tools to use</em> and <em>which workflows to run.</em></p>

<p>Example: Tell an agent "Help me plan a trip to the Moon." It will: check Moon travel tickets, gather travel guides, compile everything into a document, and send it to you. Agents turn AI from a "chatbot" into a "doer."</p>

<h2>Building AI Solutions with Kouzi (扣子)</h2>

<p><strong>Kouzi (Coze)</strong> is ByteDance's platform that lets you assemble all these layers into a working AI solution — no coding required. Think of it as a "super factory" for building intelligent agents.</p>

<ol>
<li><strong>Choose a Brain (LLM):</strong> Pick an LLM like Doubao or ChatGPT</li>
<li><strong>Add Tools & Senses:</strong> Integrate internet search, knowledge bases, image/audio/video generators</li>
<li><strong>Create Workflows (SOPs):</strong> Define the steps AI should follow</li>
<li><strong>Build an Intelligent Agent:</strong> Package everything into an agent that delivers results</li>
</ol>

<h2>Final Takeaway</h2>

<p>AI applications work in a 3-layer pyramid: Brain (LLM) processes text and logic, Senses/Limbs (Multimodal) adds visual/audio capabilities, Skeleton/Tools adds real-time data, personalization, and proactivity. With tools like Kouzi, you can build practical AI solutions even if you don't know how to code.</p>

<h2>常见问题</h2>

<h3>What's the difference between a workflow and an intelligent agent?</h3>
<p>A workflow follows a fixed, pre-defined sequence of steps — like a factory assembly line. It's predictable and reliable, but inflexible. An intelligent agent decides <em>which</em> steps to take based on the situation — like a project manager who chooses tools and workflows dynamically. Workflows are best for repetitive, well-understood tasks (publishing daily reports, processing standard forms). Agents are best for open-ended tasks where the path isn't known in advance (researching a new topic, planning an event). Kouzi lets you build both and even combine them: use workflows for stable sub-tasks and an agent to orchestrate which workflows to run.</p>

<h3>Do I need coding skills to build AI agents with Kouzi?</h3>
<p>No — that's Kouzi's main value proposition. The platform uses a visual, drag-and-drop interface. You select an LLM from a dropdown, add tools by toggling switches, and create workflows by connecting nodes visually. For most common use cases (chatbots, customer service, content automation), you can build a working agent in under an hour with zero code. That said, for advanced customizations or integrating proprietary APIs, some technical knowledge helps — but it's optional for getting started.</p>

<h3>How do knowledge bases actually work with LLMs?</h3>
<p>Knowledge bases use a technique called RAG (Retrieval-Augmented Generation). When you upload a document, the system splits it into chunks, converts each chunk into a vector embedding, and stores them in a vector database. When you ask a question, the system finds the most relevant chunks and injects them into the LLM's prompt as context. This way, the LLM "reads" your documents in real-time and answers based on them, rather than relying on its training data. This is how NotebookLM can answer questions about a contract you just uploaded, even though that contract was never in the model's training data.</p>

<div class="next-step">
<p><strong>下一篇：</strong> <a href="/en/article/2025-ai-toolkit-practical-guide-every-domain">2025 AI Toolkit: A Practical Guide for Every Domain →</a></p>
</div>`,
    contentZh: `<div class="meta-banner">
<p><strong>📅 发布日期：</strong>2026年6月30日 · <strong>🏷️ 分类：</strong>AI基础 · <strong>📊 难度：</strong>初级 · <strong>🛠️ 工具：</strong>ChatGPT、Gemini、DeepSeek、Qwen、Nano Banana Pro、Midjourney、Veo 3.1、Suno、HeyGen、NotebookLM、扣子</p>
</div>

<p>你是否只把AI当作聊天工具或更智能的浏览器来用？你是否仍然难以理解AI大模型、智能Agent和AI工作流到底是什么？本指南将以最通俗易懂的方式拆解AI应用层的底层逻辑，即使是完全的AI初学者也能看懂。</p>

<h2>AI应用的三层金字塔</h2>

<p>为了避免混淆，我们把所有AI产品结构化为三层金字塔：</p>

<ol>
<li><strong>核心大脑（大语言模型 - LLM）</strong></li>
<li><strong>感官与四肢（多模态模型）</strong></li>
<li><strong>骨架与工具（互联网、知识库、工作流、智能Agent）</strong></li>
</ol>

<p>这三层决定了AI到底能为你做什么。</p>

<h2>第一层：核心大脑——大语言模型（LLM）</h2>

<p>LLM是AI的"大脑"。把它们想象成一个无所不知的教授——能快速回答任何问题，拥有完美记忆。流行的LLM包括DeepSeek、豆包、Qwen 3、ChatGPT和Gemini 3.0。</p>

<h3>核心能力</h3>
<ul>
<li>处理文本和逻辑思维</li>
<li>作为理解和生成信息的中心枢纽</li>
</ul>

<h3>关键局限</h3>
<ol>
<li><strong>知识局限：</strong>时间滞后——上个月训练的LLM不知道这个月发生的事。范围限制——LLM不知道你个人或公司的数据。问豆包<em>你</em>下周的工作计划，它会胡编，因为那些数据不在它的训练集中。</li>
<li><strong>被动性：</strong>LLM只在被问时才回答。它们不会主动提供信息除非被提示。</li>
</ol>

<h3>掌握提示词</h3>
<p>与LLM合作的关键是写好提示词。提示词的精髓是：<em>别让模型猜你是谁。</em>具体说明背景、目标和约束条件。</p>

<pre><code class="language-plaintext">你是一名职业教练。我是一名28岁的营销专员，
有5年数字营销经验。我想转行产品管理。我的优势
是数据分析和用户研究。请制定一份1年职业转型计划，
包括需要学习的技能和求职策略。</code></pre>

<h2>第二层：感官与四肢——多模态模型</h2>

<p>多模态模型是AI的"感官和四肢"——让AI能看、听、说、创作。把它们想象成给LLM装上"画家的手、导演的眼睛和歌手的嗓音"。</p>

<ul>
<li>生成图像（Nano Banana Pro、Midjourney）、视频（Veo 3.1、Sora 2）、音频（IndexTTS、Suno）和数字人（HeyGen）</li>
<li>让AI能与文本、图像、音频和视频交互</li>
</ul>

<p><strong>局限：</strong>多模态模型仍然继承LLM的缺陷——没有实时数据、无法访问个人/公司信息、仍然是直到被指示才行动的被动模式。</p>

<h2>第三层：骨架与工具</h2>

<p>这一层给AI加上"骨架和工具"，解决其在实时数据、个性化和主动性方面的局限。</p>

<h3>1. 互联网搜索工具</h3>
<p>为了解决LLM的时间滞后问题，我们给它接入互联网。当你问豆包"今天有什么新闻？"它会运行网络搜索——就像"把教授接入互联网"。</p>

<h3>2. 知识库</h3>
<p>为了添加个人/公司数据，使用知识库（NotebookLM、IMA）。上传一份合同并提问：</p>

<pre><code class="language-plaintext">分析这份合同的潜在风险，特别关注付款条款和
责任条款。</code></pre>

<p>LLM将基于<em>你的</em>真实数据回答，而非编造的信息。</p>

<h3>3. 工作流（标准操作流程）</h3>
<p>工作流把AI变成"工厂流水线工人"——强制执行一致的步骤来保证稳定性。示例：爆款文章创作工作流：</p>
<ol>
<li>在头条搜索特定领域的热门话题</li>
<li>提取前3篇文章的标题风格</li>
<li>模仿该风格撰写符合你个人品牌的文章</li>
</ol>
<p>这把"不可预测的创意"变成了"可靠的流水线"。</p>

<h3>4. 智能Agent</h3>
<p>智能Agent就像"项目经理"——它们独立思考、规划并行动。与工作流（遵循固定步骤）不同，Agent决定<em>使用哪些工具</em>和<em>运行哪些工作流。</em></p>

<p>示例：告诉Agent"帮我规划一次月球旅行"。它会：查询月球旅行"门票"、收集旅行攻略、将所有内容编成文档发给你。Agent把AI从"聊天机器人"变成了"实干家"。</p>

<h2>用扣子（Coze）构建AI解决方案</h2>

<p><strong>扣子（国际版：Coze）</strong>是字节跳动的平台，让你把所有层次组装成可工作的AI解决方案——无需编程。可以把它想象成构建智能Agent的"超级工厂"。</p>

<ol>
<li><strong>选择大脑（LLM）：</strong> 选一个LLM如豆包或ChatGPT</li>
<li><strong>添加工具与感官：</strong> 集成互联网搜索、知识库、图像/音频/视频生成器</li>
<li><strong>创建工作流（SOP）：</strong> 定义AI应遵循的步骤</li>
<li><strong>构建智能Agent：</strong> 把所有内容打包成一个能交付结果的Agent</li>
</ol>

<h2>最终总结</h2>

<p>AI应用以三层金字塔运作：大脑（LLM）处理文本和逻辑，感官/四肢（多模态）增加视觉/音频能力，骨架/工具增加实时数据、个性化和主动性。有了扣子这样的工具，即使你不会编程也能构建实用的AI解决方案。</p>

<h2>常见问题</h2>

<h3>工作流和智能Agent有什么区别？</h3>
<p>工作流遵循固定的、预定义的步骤序列——像工厂流水线。可预测、可靠，但不灵活。智能Agent根据情况决定<em>采取哪些</em>步骤——像项目经理一样动态选择工具和工作流。工作流最适合重复性、理解清晰的任务（发布日报、处理标准表单）。Agent最适合路径事先未知的开放性任务（研究新课题、策划活动）。扣子让你可以构建两者甚至组合使用：用工作流处理稳定的子任务，用Agent编排运行哪些工作流。</p>

<h3>用扣子构建AI Agent需要编程技能吗？</h3>
<p>不需要——这正是扣子的核心价值主张。平台使用可视化拖拽界面。你从下拉菜单选择LLM，通过开关添加工具，通过可视化连接节点创建工作流。对于大多数常见用例（聊天机器人、客服、内容自动化），你可以在不到一小时内零代码构建一个可工作的Agent。不过，对于高级定制或集成专有API，一些技术知识有帮助——但入门完全不需要。</p>

<h3>知识库实际是如何与LLM配合工作的？</h3>
<p>知识库使用一种叫RAG（检索增强生成）的技术。当你上传文档时，系统将其切分成块，将每块转换成向量嵌入，存储在向量数据库中。当你提问时，系统找到最相关的块并将其注入LLM的提示词中作为上下文。这样LLM就实时"阅读"你的文档并基于它们回答，而不是依赖其训练数据。这就是NotebookLM能够回答关于你刚上传的合同的问题的原因，即使该合同从未在模型训练数据中出现过。</p>

<div class="next-step">
<p><strong>下一篇：</strong> <a href="/zh/article/2025-ai-toolkit-practical-guide-every-domain">2025 AI工具大全：全领域实战选型指南 →</a></p>
</div>`,
  },

  "2025-ai-toolkit-practical-guide-every-domain": {
    content: `<div class="meta-banner">
<p><strong>📅 Published:</strong> June 30, 2026 · <strong>🏷️ Category:</strong> AI Comparisons · <strong>📊 Level:</strong> Beginner · <strong>🛠️ Tools:</strong> Gemini, ChatGPT, Claude, Grok, Qwen, DeepSeek, Nano Banana Pro, Midjourney, Veo 3.1, MiniMax M3, ElevenLabs, Suno, HeyGen, Cursor, Trae, Codex, NotebookLM, Kouzi, Runway</p>
</div>

<p>In 2025, the AI landscape has evolved dramatically, with thousands of new tools hitting the market. Navigating this vast ecosystem can be overwhelming, but this guide breaks down the best AI tools across 9 key domains, helping you save time and money while maximizing productivity.</p>

<h2>1. Text AI Tools</h2>

<ul>
<li><strong>Top Pick: Gemini 3.0 Pro</strong> — ¥140/month, best-in-class long context window and multimodal capabilities. Gemini Flash is free, making it a no-brainer for comprehensive text tasks.</li>
<li><strong>Free Alternative: Doubao</strong> — Incredibly well-rounded, covers a wide range of text needs at zero cost.</li>
<li><strong>Open-Source Option: Qwen</strong> — Unlike DeepSeek (often too large), Qwen offers multiple model sizes (0.5B, 1.5B, 14B, 72B) for different performance needs.</li>
<li><strong>Others:</strong> ChatGPT (versatile, ¥140/month), Grok (great for Twitter scraping and real-time updates), Claude (strong for long texts and document analysis), Kimi and DeepSeek (free, each with unique strengths).</li>
</ul>

<h2>2. Image Generation Tools</h2>

<ul>
<li><strong>Top Pick: Nano Banana Pro</strong> — ¥1 per 2K image via API, easy to use, consistent results, convenient editing with high-quality outputs.</li>
<li><strong>Alternative: Seedream-4.5</strong> — ¥0.25 per 2K image via API, excels in consistency and multi-reference support, great value for money.</li>
<li><strong>Open-Source: Z-image</strong> — Works with just 6GB VRAM, excellent Chinese text understanding and high-quality visuals.</li>
<li><strong>Others:</strong> Midjourney (artistic, ¥70/month), Flux (free and open-source).</li>
</ul>

<h2>3. Video AI Tools</h2>

<ul>
<li><strong>Top Pick: Veo 3.1</strong> — Perfect audio-visual synchronization, natural motion, high-quality output at ~¥14 per 5 seconds.</li>
<li><strong>Alternative: Seedance-1.5-Pro</strong> — ¥4 per 5 seconds, synchronized audio-visuals, detailed performances, high cost-effectiveness.</li>
<li><strong>Open-Source: Wan 2.2</strong> — Rich features and quality comparable to closed-source tools.</li>
<li><strong>Others:</strong> KeLing, Vidu (character-based video with reference images), Conch (motion capture), Runway (excellent editing effects).</li>
</ul>

<h2>4. Audio AI Tools</h2>

<h3>Voiceover</h3>
<ul>
<li><strong>Top Pick: MiniMax</strong> — 36mb/month, easy to use, cost-effective, natural-sounding voices in various tones.</li>
<li><strong>Advanced: ElevenLabs</strong> — 355mb/month (free tier available), superior for foreign language voiceovers.</li>
<li><strong>Open-Source: IndexTTS2</strong> — Free, great for voice cloning and text-to-speech with user-friendly interface.</li>
</ul>

<h3>Music</h3>
<ul>
<li><strong>Top Pick: Suno</strong> — ¥70/month (free tier: 10 songs/day), stunning AI-generated music.</li>
<li><strong>Others:</strong> Udio (segmental fine-tuning), Stable Audio (precise beat matching).</li>
</ul>

<h2>5. Digital Human Tools</h2>

<ul>
<li><strong>Top Pick: HeyGen</strong> — 203mb/month, high-quality digital human videos with natural motions and expressions.</li>
<li><strong>Alternative: InfiniteTalk</strong> — Free and open-source, though requires more setup effort.</li>
<li><strong>Quick Replacement:</strong> For short AI character clips with brief dialogues, use image-to-video tools like Veo 3.1.</li>
</ul>

<h2>6. AI Browsers</h2>

<ul>
<li><strong>Top Picks: Dia, Atlas</strong> — Dia offers comfortable UI, free GPT access, customization, and Agent capabilities. Atlas is strong if you're already invested in ChatGPT.</li>
<li><strong>Alternatives:</strong> Doubao, Kuaike — free domestic AI browsers for basic AI-assisted browsing.</li>
</ul>

<h2>7. Coding AI Tools</h2>

<ul>
<li><strong>Top Pick: Cursor</strong> — Pro ¥140/month, Pro+ ¥420/month, Ultra ¥1400/month. Stable, rapidly updated, integrates Claude Code and Codex seamlessly.</li>
<li><strong>Alternative: Trae</strong> — ¥21 first month, ¥70/month thereafter. Excellent product details, user-friendly for beginners.</li>
<li><strong>Advanced: Claude Code, Codex (GPT5 Series)</strong> — Claude Code (Pro: ¥100/month, Max: ¥700-1400/month) and Codex (Plus: ¥140/month, Pro: ¥210/month) for complex coding. Codex often fixes bugs Claude can't.</li>
<li><strong>Entry-Level: Google AI Studio (Build Mode)</strong> — Free, great for creative coding demos with Gemini.</li>
</ul>

<h2>8. Knowledge Base Tools</h2>

<ul>
<li><strong>Top Pick: NotebookLM</strong> — Free, multi-resource learning powerhouse. Dump large amounts of data to generate audio summaries, mind maps, presentations, infographics, and video summaries.</li>
<li><strong>Alternative: IMA</strong> — 30GB free storage, great for collecting and reading public accounts.</li>
</ul>

<h2>9. Agent Tools</h2>

<ul>
<li><strong>Top Pick: Codex</strong> — ¥140/month, can be used as a general-purpose Agent.</li>
<li><strong>Specialized: Deep Research</strong> — Perfect for in-depth investigations, saves significant research time.</li>
<li><strong>Alternatives: AutoGLM, Kouzi Space</strong> — Both free, AutoGLM is open-source, Kouzi Space offers user-friendly interface.</li>
<li><strong>Workflow: n8n</strong> — Free for local deployment, great for automated workflows (steep learning curve).</li>
</ul>

<h2>Final Thoughts</h2>

<p>The tools listed here are time-tested and can handle 95% of your daily and professional AI needs. For the remaining 5% of specific requirements, use these tools as a base and then conduct targeted searches and learning. Stay updated with the latest developments, and don't hesitate to dive into new tools when they fit your needs.</p>

<h2>常见问题</h2>

<h3>Which single paid AI tool gives the most value for its price?</h3>
<p>Cursor at ¥140/month (Pro plan). For the price of a meal, you get an AI coding assistant that understands your entire project, integrates multiple AI models, and effectively acts as a senior programmer working for you. It's the tool that most directly translates to increased productivity and income for developers. If coding isn't your focus, Gemini 3.0 Pro at the same price point offers the broadest capabilities across research, writing, and analysis — and Gemini Flash is free if budget is tight.</p>

<h3>Are open-source AI tools actually usable for professional work?</h3>
<p>Increasingly, yes. Qwen offers multiple model sizes that can be deployed locally for specific tasks — the 72B version competes with GPT-4 class models on many benchmarks. Wan 2.2 for video and Z-image for image generation deliver quality comparable to closed-source alternatives. The main tradeoffs are: you need technical skills to deploy and maintain them, you need your own hardware (GPUs), and you're responsible for updates and security. For tech-savvy teams with specific requirements, open-source can save thousands per month. For most individuals, the convenience of hosted tools is worth the subscription cost.</p>

<h3>How do I choose between all these tools without getting overwhelmed?</h3>
<p>Start with one category that matters most to your daily work. If you write a lot, pick a text tool. If you create visual content, pick an image tool. Master that one tool before expanding. A practical starter stack: Gemini (free) for research and writing, Nano Banana Pro (free) for images, Cursor (¥140/month) if you code, NotebookLM (free) for knowledge management. That covers 4 major categories for ¥140/month total. Add specialized tools only when you hit the limits of these core tools. The biggest mistake is subscribing to 10 tools on day one and using none of them deeply.</p>

<div class="next-step">
<p><strong>上一篇：</strong> <a href="/en/article/demystifying-ai-application-layer-3-layers">Demystifying AI Application Layer: From Large Language Models to Intelligent Agents in 3 Layers ←</a></p>
</div>`,
    contentZh: `<div class="meta-banner">
<p><strong>📅 发布日期：</strong>2026年6月30日 · <strong>🏷️ 分类：</strong>AI对比 · <strong>📊 难度：</strong>初级 · <strong>🛠️ 工具：</strong>Gemini、ChatGPT、Claude、Grok、Qwen、DeepSeek、Nano Banana Pro、Midjourney、Veo 3.1、MiniMax M3、ElevenLabs、Suno、HeyGen、Cursor、Trae、Codex、NotebookLM、扣子、Runway</p>
</div>

<p>2025年，AI格局发生了巨大变化，数千款新工具涌入市场。在这庞大的生态中导航可能让人不知所措，但本指南拆解了9个关键领域的最佳AI工具，帮你省时省钱同时最大化生产力。</p>

<h2>1. 文本AI工具</h2>

<ul>
<li><strong>首选：Gemini 3.0 Pro</strong>——¥140/月，顶级长上下文窗口和多模态能力。Gemini Flash免费，是综合文本任务的不二之选。</li>
<li><strong>免费替代：豆包</strong>——极其全面，零成本覆盖广泛文本需求。</li>
<li><strong>开源选项：Qwen</strong>——与DeepSeek（通常太大难以部署）不同，Qwen提供多种模型尺寸（0.5B、1.5B、14B、72B），满足不同性能需求。</li>
<li><strong>其他：</strong>ChatGPT（多功能，¥140/月）、Grok（擅长Twitter抓取和实时更新）、Claude（擅长长文本和文档分析）、Kimi和DeepSeek（免费，各有独特优势）。</li>
</ul>

<h2>2. 图像生成工具</h2>

<ul>
<li><strong>首选：Nano Banana Pro</strong>——API ¥1/2K图像，易用、结果一致、便捷编辑、高质量输出。</li>
<li><strong>替代：Seedream-4.5</strong>——API ¥0.25/2K图像，一致性和多参考支持出色，性价比极高。</li>
<li><strong>开源：Z-image</strong>——仅需6GB显存，优秀的中文文本理解和高质量视觉。</li>
<li><strong>其他：</strong>Midjourney（艺术性，¥70/月）、Flux（免费开源）。</li>
</ul>

<h2>3. 视频AI工具</h2>

<ul>
<li><strong>首选：Veo 3.1</strong>——完美声画同步、自然运动、高质量输出，约¥14/5秒。</li>
<li><strong>替代：Seedance-1.5-Pro</strong>——¥4/5秒，同步声画、细腻表演、高性价比。</li>
<li><strong>开源：Wan 2.2</strong>——丰富功能和媲美闭源工具的质量。</li>
<li><strong>其他：</strong>可灵、Vidu（带参考图的角色视频）、海螺（动作捕捉出色）、Runway（编辑效果优秀）。</li>
</ul>

<h2>4. 音频AI工具</h2>

<h3>配音</h3>
<ul>
<li><strong>首选：MiniMax</strong>——36mb/月，易用、性价比高、多种音色自然发音。</li>
<li><strong>高级：ElevenLabs</strong>——355mb/月（有免费版），外语配音更优。</li>
<li><strong>开源：IndexTTS2</strong>——免费，声音克隆和文字转语音出色，界面友好。</li>
</ul>

<h3>音乐</h3>
<ul>
<li><strong>首选：Suno</strong>——¥70/月（免费版：10首/天），惊艳的AI生成音乐。</li>
<li><strong>其他：</strong>Udio（分段精细调整）、Stable Audio（精准节拍匹配）。</li>
</ul>

<h2>5. 数字人工具</h2>

<ul>
<li><strong>首选：HeyGen</strong>——203mb/月，高质量数字人视频，动作表情自然。</li>
<li><strong>替代：InfiniteTalk</strong>——免费开源，但需要更多搭建工作。</li>
<li><strong>快速替代：</strong>短AI角色片段配简短对话，用Veo 3.1等图生视频工具。</li>
</ul>

<h2>6. AI浏览器</h2>

<ul>
<li><strong>首选：Dia、Atlas</strong>——Dia提供舒适UI、免费GPT访问、定制化和Agent能力。Atlas适合已投资ChatGPT的用户。</li>
<li><strong>替代：</strong>豆包、快可——免费国产AI浏览器，满足基础AI辅助浏览。</li>
</ul>

<h2>7. 编程AI工具</h2>

<ul>
<li><strong>首选：Cursor</strong>——Pro ¥140/月、Pro+ ¥420/月、Ultra ¥1400/月。稳定、更新快，无缝集成Claude Code和Codex。</li>
<li><strong>替代：Trae</strong>——首月¥21、后续¥70/月。产品细节优秀，对新手友好。</li>
<li><strong>高级：Claude Code、Codex（GPT5系列）</strong>——Claude Code（Pro: ¥100/月、Max: ¥700-1400/月）和Codex（Plus: ¥140/月、Pro: ¥210/月）处理复杂编码。Codex常修复Claude搞不定的Bug。</li>
<li><strong>入门级：Google AI Studio（Build模式）</strong>——免费，适合用Gemini创建创意编码演示。</li>
</ul>

<h2>8. 知识库工具</h2>

<ul>
<li><strong>首选：NotebookLM</strong>——免费，多资源学习利器。丢入大量数据生成音频摘要、思维导图、演示文档、信息图和视频摘要。</li>
<li><strong>替代：IMA</strong>——30GB免费存储，适合收集和阅读公众号内容。</li>
</ul>

<h2>9. Agent工具</h2>

<ul>
<li><strong>首选：Codex</strong>——¥140/月，可作为通用Agent使用。</li>
<li><strong>专项：Deep Research</strong>——深度调研完美之选，节省大量研究时间。</li>
<li><strong>替代：AutoGLM、扣子空间</strong>——均免费，AutoGLM开源，扣子空间界面友好。</li>
<li><strong>工作流：n8n</strong>——本地部署免费，适合自动化工作流（学习曲线较陡）。</li>
</ul>

<h2>最终总结</h2>

<p>这里列出的工具经过时间检验，可处理你95%的日常和专业AI需求。对于剩余5%的特定需求，以这些工具为基础再进行针对性搜索和学习。保持关注最新发展，当新工具适合你的需求时不要犹豫尝试。</p>

<h2>常见问题</h2>

<h3>哪一款付费AI工具性价比最高？</h3>
<p>Cursor ¥140/月（Pro版）。一顿饭的价格，你获得一个理解你整个项目的AI编程助手，集成多个AI模型，实际上相当于一个为你工作的高级程序员。它是开发者最直接转化为生产力提升和收入增长的工具。如果你不专注编程，同价位的Gemini 3.0 Pro在研究、写作和分析方面提供最广泛的能力——而且预算紧张时Gemini Flash免费。</p>

<h3>开源AI工具真的能用于专业工作吗？</h3>
<p>越来越能。Qwen提供多种可本地部署的模型尺寸用于特定任务——72B版本在许多基准测试中与GPT-4级模型竞争。Wan 2.2做视频和Z-image做图像生成的质量媲美闭源替代品。主要权衡是：你需要技术技能来部署和维护它们，需要自己的硬件（GPU），以及你负责更新和安全。对于有特定需求的技术团队，开源每月可节省数千元。对大多数个人而言，托管工具的便利性值得订阅费用。</p>

<h3>如何在众多工具中选择而不被淹没？</h3>
<p>从对你日常工作最重要的一个类别开始。如果你大量写作，选文本工具。如果你创作视觉内容，选图像工具。在扩展前先精通那一个工具。实用起步方案：Gemini（免费）做研究和写作，Nano Banana Pro（免费）做图像，Cursor（¥140/月）如果你编程，NotebookLM（免费）做知识管理。总共¥140/月覆盖4个主要类别。只在这些核心工具达到极限时才添加专项工具。最大的错误是第一天订阅10个工具却一个都没深入使用。</p>

<div class="next-step">
<p><strong>上一篇：</strong> <a href="/zh/article/demystifying-ai-application-layer-3-layers">拆解AI应用层：从大语言模型到智能Agent的三层金字塔 ←</a></p>
</div>`,
  },

'''

last_brace = content_src.rfind('};')
content_new = content_src[:last_brace] + new_contents + '};'

with open('src/lib/article-content.ts', 'w', encoding='utf-8') as f:
    f.write(content_new)

print('Part 3: 2 article contents added to article-content.ts')

print('\n=== All done! Run build to verify ===')
