# -*- coding: utf-8 -*-
"""Publish Oct 14, 2026 — Top 5 AI Video Creation Tools. Adds 5 new tools."""
import io, os

BASE = r"C:\Users\jun\aistudyonline-next"
os.chdir(BASE)

# ---------- 1. articles.ts ----------
f = r"src\lib\articles.ts"
s = io.open(f, encoding="utf-8").read()

a = r"""  {
    slug: "top-5-ai-video-creation-tools-streamline-workflow",
    title: "Top 5 AI Video Creation Tools to Streamline Your Workflow",
    titleZh: "Top 5 AI视频创作工具：让工作流真正跑起来",
    description: "AI video creation has reached production-grade maturity. This guide ranks the top 5 AI video tools that automate the entire pipeline from script to final cut — waoowaoo (industrial-grade film production), Toonflow (infinite canvas + agent visual creation), Open-Generative-AI (unrestricted open-source video engine), diffusers (full-modal diffusion infrastructure), and OpenMontage (agent auto-editing with music) — covering key features, install commands, and the best use case for each.",
    descriptionZh: "AI视频创作已进入工业化成熟期。本指南盘点 5 款能从脚本一路自动到成片的AI视频工具——waoowaoo（工业级影视制作）、Toonflow（无限画布+代理可视化创作）、Open-Generative-AI（无限制开源视频引擎）、diffusers（全模态扩散模型基础设施）、OpenMontage（带音乐的代理自动剪辑）——逐一说明关键特性、安装命令与最佳使用场景。",
    category: "ai-tutorials",
    tags: ["AI Video", "Video Creation", "Open Source", "Agent", "Diffusion Models", "Editing", "Top Tools"],
    difficulty: "intermediate",
    toolsMentioned: ["waoowaoo", "toonflow", "open-generative-ai", "diffusers", "openmontage"],
    date: "2026-10-14",
  },
  """
pos = s.rfind("];")
assert pos > 0
s2 = s[:pos] + a + s[pos:]
io.open(f, "w", encoding="utf-8", newline="\n").write(s2)
print("articles.ts entries:", s2.count('slug: "'))

# ---------- 2. article-content.ts ----------
f = r"src\lib\article-content.ts"
s = io.open(f, encoding="utf-8").read()

content = r"""  "top-5-ai-video-creation-tools-streamline-workflow": {
    content: `<div class="meta-banner">
  <span class="meta-badge">📚 AI Tutorials</span>
  <span class="meta-badge">🕒 9 min read</span>
  <span class="meta-badge">📅 Oct 14, 2026</span>
  <span class="meta-badge">🎯 Intermediate</span>
</div>

<h2 id="introduction">Introduction</h2>

<p>The AI video creation industry has fully entered a production-grade era, with tools that can automate the entire process from script to final video. This guide breaks down the top 5 AI video tools that can help you reduce production barriers and boost efficiency.</p>

<h2 id="ranking">The Top 5, Ranked by Production Coverage</h2>
<p>These five tools were selected because each one covers a distinct stage or layer of the AI video pipeline — from full industrial production to component-level infrastructure. The order below runs from end-to-end coverage at #5 to foundational infrastructure at #1, so you can pick where you want to enter the stack.</p>

<h3>5. waoowaoo: Industrial-Grade AI Film Production</h3>
<p>waoowaoo is an industrial-grade AI tool that automates the entire film production workflow. It uses AI agents to orchestrate the process, turning scripts into finished videos with a single workflow.</p>
<ul>
  <li><strong>Full-process automation</strong>: AI script analysis, character and scene generation, storyboard creation, and video compositing.</li>
  <li><strong>Multi-role voice synthesis</strong>: AI-generated voiceovers for multiple characters.</li>
  <li><strong>Bilingual support</strong>: Chinese/English interface with one-click switching.</li>
  <li><strong>Local deployment</strong>: run via Docker Compose for full control over your workflow.</li>
</ul>
<pre><code class="language-bash"># Clone the repository
git clone https://github.com/waooAI/waoowaoo.git
cd waoowaoo

# Start the service with Docker Compose
docker compose up -d</code></pre>
<p><strong>Best for</strong>: short drama production from novel text, comic-style video creation, and rapid prototyping of video concepts.</p>

<h3>4. Toonflow: Infinite Canvas + Agent Visual Creation</h3>
<p>Toonflow is an open-source AI creation tool that combines an infinite canvas with agent-driven visual workflows. It supports intelligent storyboarding for both images and videos, giving creators maximum creative freedom.</p>
<ul>
  <li><strong>Infinite canvas</strong>: drag-and-drop interface for visual storyboarding.</li>
  <li><strong>Agent collaboration</strong>: multiple AI agents work together to handle different production stages.</li>
  <li><strong>Cross-platform support</strong>: available for both Windows and macOS.</li>
  <li><strong>Character consistency</strong>: AI ensures characters stay on-model across all scenes.</li>
</ul>
<pre><code class="language-bash"># Download the latest release
wget https://github.com/HBAI-Ltd/Toonflow-app/releases/latest/download/Toonflow-1.0.0.dmg

# Install and run
open Toonflow-1.0.0.dmg</code></pre>
<p><strong>Best for</strong>: webtoon and comic creation, animated short film production, and visual storyboarding for any video project.</p>

<h3>3. Open-Generative-AI: Unrestricted Open-Source Video Engine</h3>
<p>Open-Generative-AI is an open-source video engine that provides an alternative to commercial video platforms. It offers unrestricted generation capabilities without platform content censorship.</p>
<ul>
  <li><strong>Unrestricted generation</strong>: no content filters or platform restrictions.</li>
  <li><strong>600+ models</strong>: supports popular models like Flux, Midjourney, Kling, and Sora.</li>
  <li><strong>Self-hosted</strong>: run locally for full control over your content.</li>
  <li><strong>MIT licensed</strong>: free for commercial use.</li>
</ul>
<pre><code class="language-bash"># Clone the repository
git clone https://github.com/Anil-matcha/Open-Generative-AI.git
cd Open-Generative-AI

# Install dependencies
npm install

# Start the server
npm start</code></pre>
<p><strong>Best for</strong>: unrestricted video generation, an alternative to commercial video platforms, and custom video engine development.</p>

<h3>2. diffusers: Full-Modal Diffusion Model Infrastructure</h3>
<p>diffusers is a full-modal diffusion model infrastructure that serves as the foundation for many AI generation capabilities. It supports images, videos, and audio across all modalities.</p>
<ul>
  <li><strong>Full-modal support</strong>: images, videos, audio, and even 3D structures.</li>
  <li><strong>Latest model access</strong>: get access to the latest diffusion models as soon as they are released.</li>
  <li><strong>Modular design</strong>: mix and match components to build custom generation systems.</li>
  <li><strong>Production-ready</strong>: used by leading AI companies for their generation pipelines.</li>
</ul>
<pre><code class="language-python"># Install the library
pip install diffusers accelerate transformers

# Generate an image
from diffusers import DiffusionPipeline
pipeline = DiffusionPipeline.from_pretrained("black-forest-labs/FLUX.1-schnell")
image = pipeline("A cat holding a sign that says hello world").images[0]
image.save("cat.png")</code></pre>
<p><strong>Best for</strong>: foundation for custom AI generation tools, research and development of new diffusion models, and production-grade AI generation pipelines.</p>

<h3>1. OpenMontage: Agent Auto-Editing with Music</h3>
<p>OpenMontage is an AI tool that automates video editing and music composition, turning raw footage into finished videos with a single workflow.</p>
<ul>
  <li><strong>Agent-driven workflow</strong>: AI agents handle research, scriptwriting, storyboarding, and editing.</li>
  <li><strong>Automatic music composition</strong>: AI generates background music that matches your video.</li>
  <li><strong>Full-process automation</strong>: from raw footage to final video in one workflow.</li>
  <li><strong>Production-grade output</strong>: professional-quality videos ready for distribution.</li>
</ul>
<pre><code class="language-bash"># Install via npm
npm install -g openmontage

# Start the service
openmontage start</code></pre>
<p><strong>Best for</strong>: automated video editing, music composition for videos, and rapid video production for social media.</p>

<h2 id="conclusion">Conclusion</h2>
<p>These 5 AI video tools represent the cutting edge of AI video creation. Whether you are a professional filmmaker or a content creator, these tools can help you streamline your workflow, reduce production barriers, and create high-quality videos faster than ever before.</p>
<p>All of these tools are open-source, so you can customize them to fit your specific needs. Start with one that fits your use case, and experiment with the others to find the perfect tool for your workflow.</p>

<h2>常见问题</h2>

<h3>Which of the 5 tools is the best starting point for a beginner?</h3>
<p>If you want the simplest path from script to finished video, start with <strong>OpenMontage</strong> — its one-line npm install and agent-driven editing handle the entire pipeline. If your focus is on visual storyboarding, <strong>Toonflow</strong>'s drag-and-drop infinite canvas is the gentlest learning curve.</p>

<h3>Are these AI video tools free to use?</h3>
<p>All five are open-source. <strong>Open-Generative-AI</strong> and <strong>diffusers</strong> are MIT-licensed and free for commercial use. <strong>waoowaoo</strong>, <strong>Toonflow</strong>, and <strong>OpenMontage</strong> are also open-source, so you can self-host and customize them freely.</p>

<h3>Do I need a powerful GPU to run these tools?</h3>
<p>It depends. <strong>diffusers</strong> is the most compute-hungry since it runs diffusion inference locally — a recent GPU is recommended. <strong>Open-Generative-AI</strong> and <strong>waoowaoo</strong> run via Node.js and Docker respectively, and can rely on hosted models for many generation tasks. <strong>Toonflow</strong> and <strong>OpenMontage</strong> are the lightest to get started with.</p>

<h3>Can I use these tools together in one workflow?</h3>
<p>Yes. A practical pipeline: <strong>waoowaoo</strong> or <strong>OpenMontage</strong> for script and storyboard, <strong>Toonflow</strong> for visual layout, <strong>diffusers</strong> for the underlying image/video generation models, and <strong>Open-Generative-AI</strong> as the unconstrained generation engine. Each tool covers a different layer of the same stack.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Want a deeper, hands-on dive into specific video tools? Explore:</p>
  <ul>
    <li><a href="/article/how-to-create-professional-ai-videos-flova-ai-complete-practical-guide">How to Create Professional AI Videos with Flova.ai: A Complete Practical Guide</a> — a polished, end-to-end walkthrough for visual production</li>
    <li><a href="/article/master-seedance-2-5-zero-basics-guide-commercial-grade-ai-video-creation">Master Seedance 2.5: Zero-Basics Guide to Commercial-Grade AI Video Creation</a> — generate commercial-grade footage from scratch</li>
    <li><a href="/article/rewriting-content-creation-workflow-ai-driven-video-production">Rewriting the Content Creation Workflow: A Practical Guide to AI-Driven Video Production</a> — the broader methodology behind an AI-driven video pipeline</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">📚 AI 教程</span>
  <span class="meta-badge">🕒 阅读约9分钟</span>
  <span class="meta-badge">📅 2026年10月14日</span>
  <span class="meta-badge">🎯 进阶</span>
</div>

<h2 id="introduction">引言</h2>

<p>AI视频创作行业已完全进入工业化成熟期，出现了一批能把从脚本到成片的整个流程自动化的工具。本指南拆解 Top 5 款 AI 视频工具，帮你降低制作门槛、提升效率。</p>

<h2 id="ranking">Top 5 工具，按覆盖度排序</h2>
<p>这 5 款工具入选是因为它们各自覆盖了AI视频流水线中不同层级——从端到端工业化制作到组件级基础设施。下面从最广覆盖的 #5 到最底层基础设施的 #1 排列，方便你选择进入栈的哪一层。</p>

<h3>5. waoowaoo：工业级 AI 影视制作</h3>
<p>waoowaoo 是一款工业级 AI 工具，能自动化整个影视制作流程。它用 AI 代理编排整个过程，把脚本一次性变成成片。</p>
<ul>
  <li><strong>全流程自动化</strong>：AI 脚本分析、角色与场景生成、分镜制作与视频合成。</li>
  <li><strong>多角色语音合成</strong>：为多个角色生成 AI 配音。</li>
  <li><strong>双语支持</strong>：中英双语界面，一键切换。</li>
  <li><strong>本地部署</strong>：通过 Docker Compose 启动，完全掌控工作流。</li>
</ul>
<pre><code class="language-bash"># 克隆仓库
git clone https://github.com/waooAI/waoowaoo.git
cd waoowaoo

# 用 Docker Compose 启动服务
docker compose up -d</code></pre>
<p><strong>最佳场景</strong>：从小说文本做短剧、漫画风格视频制作、视频概念快速原型。</p>

<h3>4. Toonflow：无限画布 + 代理可视化创作</h3>
<p>Toonflow 是一款开源 AI 创作工具，把无限画布和代理驱动的可视化工作流结合在一起。它支持图像与视频的智能分镜，让创作者拥有最大的创作自由度。</p>
<ul>
  <li><strong>无限画布</strong>：拖拽式的可视化分镜界面。</li>
  <li><strong>代理协作</strong>：多个 AI 代理协同处理不同制作阶段。</li>
  <li><strong>跨平台</strong>：支持 Windows 和 macOS。</li>
  <li><strong>角色一致性</strong>：AI 保证所有场景的角色不走样。</li>
</ul>
<pre><code class="language-bash"># 下载最新发行版
wget https://github.com/HBAI-Ltd/Toonflow-app/releases/latest/download/Toonflow-1.0.0.dmg

# 安装并启动
open Toonflow-1.0.0.dmg</code></pre>
<p><strong>最佳场景</strong>：网漫与漫画创作、动画短片制作、任意视频项目的可视化分镜。</p>

<h3>3. Open-Generative-AI：无限制开源视频引擎</h3>
<p>Open-Generative-AI 是一款开源视频引擎，提供给商业视频平台的替代选择。它提供无限制的生成能力，不受平台内容审查约束。</p>
<ul>
  <li><strong>无限制生成</strong>：没有内容过滤或平台限制。</li>
  <li><strong>600+ 模型</strong>：支持 Flux、Midjourney、Kling、Sora 等主流模型。</li>
  <li><strong>自托管</strong>：本地运行，完全掌控内容。</li>
  <li><strong>MIT 协议</strong>：允许商业使用。</li>
</ul>
<pre><code class="language-bash"># 克隆仓库
git clone https://github.com/Anil-matcha/Open-Generative-AI.git
cd Open-Generative-AI

# 安装依赖
npm install

# 启动服务
npm start</code></pre>
<p><strong>最佳场景</strong>：无限制视频生成、商业视频平台的替代方案、自定义视频引擎开发。</p>

<h3>2. diffusers：全模态扩散模型基础设施</h3>
<p>diffusers 是全模态扩散模型基础设施，是许多 AI 生成能力的地基。它支持图像、视频、音频等多个模态。</p>
<ul>
  <li><strong>全模态支持</strong>：图像、视频、音频，甚至 3D 结构。</li>
  <li><strong>最新模型</strong>：第一手拿到最新发布的扩散模型。</li>
  <li><strong>模块化设计</strong>：自由拼装组件，构建自定义生成系统。</li>
  <li><strong>生产就绪</strong>：被头部 AI 公司用于生成流水线。</li>
</ul>
<pre><code class="language-python"># 安装库
pip install diffusers accelerate transformers

# 生成一张图
from diffusers import DiffusionPipeline
pipeline = DiffusionPipeline.from_pretrained("black-forest-labs/FLUX.1-schnell")
image = pipeline("A cat holding a sign that says hello world").images[0]
image.save("cat.png")</code></pre>
<p><strong>最佳场景</strong>：自定义 AI 生成工具的底座、新型扩散模型研发、生产级 AI 生成流水线。</p>

<h3>1. OpenMontage：带音乐的代理自动剪辑</h3>
<p>OpenMontage 是一款 AI 工具，能自动完成视频剪辑和音乐合成，把原始素材一次性变成成片。</p>
<ul>
  <li><strong>代理驱动工作流</strong>：AI 代理处理调研、脚本、分镜和剪辑。</li>
  <li><strong>自动音乐创作</strong>：AI 生成与视频匹配的背景音乐。</li>
  <li><strong>全流程自动化</strong>：一条流水线，从素材到成片。</li>
  <li><strong>生产级输出</strong>：可直接发布的专业级视频。</li>
</ul>
<pre><code class="language-bash"># 通过 npm 安装
npm install -g openmontage

# 启动服务
openmontage start</code></pre>
<p><strong>最佳场景</strong>：自动视频剪辑、视频音乐创作、社交媒体快速视频制作。</p>

<h2 id="conclusion">结论</h2>
<p>这 5 款 AI 视频工具代表了 AI 视频创作的最前沿。无论你是专业影视创作者还是普通内容创作者，它们都能帮你简化工作流、降低制作门槛、比以往任何时候都更快地产出高质量视频。</p>
<p>它们全部是开源的，你可以按需定制。先从最适合自己用例的那一款开始，再尝试其他几款，找到契合你工作流的那一把“瑞士军刀”。</p>

<h2>常见问题</h2>

<h3>5 款工具里哪一款最适合新手起步？</h3>
<p>如果你想要最简单的“脚本到成片”路径，从 <strong>OpenMontage</strong> 开始——一行 npm install 加上代理驱动的剪辑就能跑通整条流水线。如果你更关注可视化分镜，<strong>Toonflow</strong> 的拖拽无限画布学习曲线最低。</p>

<h3>这些 AI 视频工具是免费的吗？</h3>
<p>5 款全部开源。<strong>Open-Generative-AI</strong> 和 <strong>diffusers</strong> 是 MIT 协议，可商用。<strong>waoowaoo</strong>、<strong>Toonflow</strong> 和 <strong>OpenMontage</strong> 同样开源，可以自托管和自由定制。</p>

<h3>运行这些工具需要强力 GPU 吗？</h3>
<p>看场景。<strong>diffusers</strong> 在本地跑扩散推理最吃算力，建议有一张较新的 GPU。<strong>Open-Generative-AI</strong> 和 <strong>waoowaoo</strong> 分别基于 Node.js 和 Docker 跑，许多生成任务可走托管模型。<strong>Toonflow</strong> 和 <strong>OpenMontage</strong> 起步最轻。</p>

<h3>这几款工具能在同一条流水线里组合使用吗？</h3>
<p>可以。一条实用的组合：用 <strong>waoowaoo</strong> 或 <strong>OpenMontage</strong> 做脚本与分镜，<strong>Toonflow</strong> 负责画面布局，<strong>diffusers</strong> 提供底层图像/视频生成模型，<strong>Open-Generative-AI</strong> 作为无限制的生成引擎。每一款覆盖栈里的不同层。</p>

<div class="next-step">
  <h3>📖 继续学习</h3>
  <p>想针对具体工具做更深入的实操？继续探索：</p>
  <ul>
    <li><a href="/article/how-to-create-professional-ai-videos-flova-ai-complete-practical-guide">用Flova.ai创建专业AI视频：完整实操指南</a> — 视觉制作的完整端到端走查</li>
    <li><a href="/article/master-seedance-2-5-zero-basics-guide-commercial-grade-ai-video-creation">掌握Seedance 2.5：零基础商业级AI视频创作指南</a> — 从零生成商业级素材</li>
    <li><a href="/article/rewriting-content-creation-workflow-ai-driven-video-production">重塑内容创作工作流：AI驱动视频制作实用指南</a> — AI 驱动视频流水线背后的方法论</li>
  </ul>
</div>`,
  },
  """
pos = s.rfind("};")
assert pos > 0
s2 = s[:pos] + content + s[pos:]
io.open(f, "w", encoding="utf-8", newline="\n").write(s2)
print("article-content.ts entries:", s2.count('content: `'))

# ---------- 3. tools.ts: add 5 new tools ----------
f = r"src\lib\tools.ts"
s = io.open(f, encoding="utf-8").read()

tools_block = r"""  {
    id: "waoowaoo",
    name: "waoowaoo",
    nameZh: "waoowaoo",
    description: "An industrial-grade AI tool that automates the entire film production workflow — AI agents orchestrate script analysis, character/scene generation, storyboard creation, and video compositing, with a Docker Compose deployment for full local control.",
    descriptionZh: "工业化级AI工具，自动化整个影视制作流程——AI代理编排脚本分析、角色与场景生成、分镜制作与视频合成，支持Docker Compose本地部署，完全掌控工作流。",
    category: "video",
    tags: ["waoowaoo", "ai-video", "film", "agent", "open-source", "docker", "bilingual"],
    difficulty: "intermediate",
    url: "https://github.com/waooAI/waoowaoo",
    rating: r(4.5),
    pricing: "Free (open source)",
    useCase: "Industrial-grade AI film production — short drama from novel text, comic-style videos, and rapid concept prototyping",
    icon: "\u{1F3AC}",
    company: "waooAI",
    companyZh: "waooAI",
    founded: 2026,
    headquarters: "Open Source",
    descriptionLong: "waoowaoo is an industrial-grade AI tool hosted on GitHub at waooAI/waoowaoo. It uses AI agents to orchestrate the entire film production pipeline, turning scripts into finished videos with a single workflow. The system handles script analysis, character and scene generation, storyboard creation, and final video compositing, plus multi-role voice synthesis so different characters get distinct AI-generated voiceovers. It ships with a Chinese/English interface and one-click switching, and runs locally via Docker Compose for full control over the production environment. waoowaoo is best suited for short drama production adapted from novel text, comic-style video creation, and rapid prototyping of video concepts where the entire pipeline can be exercised end-to-end without juggling multiple tools.",
    descriptionLongZh: "waoowaoo是托管在GitHub（waooAI/waoowaoo）的工业化级AI工具。它用AI代理编排整个影视制作流水线，一条工作流把脚本变成成片。系统覆盖脚本分析、角色与场景生成、分镜制作和最终视频合成，并内置多角色语音合成，让不同角色拥有各自不同的AI配音。出厂即带中英双语界面，一键切换；通过Docker Compose本地部署，完整掌控生产环境。waoowaoo最适合改编小说文本做短剧、漫画风格视频制作，以及从概念到成片的快速原型——一条流水线跑通整个端到端流程，无需在多个工具之间来回切换。",
    advantages: ["Full-process automation from script to video", "Multi-role AI voice synthesis", "Bilingual Chinese/English interface", "Docker Compose for self-hosted control", "Industrial-grade orchestration with AI agents"],
    advantagesZh: ["从脚本到视频的全流程自动化", "多角色AI语音合成", "中英双语界面", "Docker Compose自托管可控", "AI代理的工业化级编排"],
    useCases: ["Short drama production from novel text", "Comic-style video creation", "Rapid prototyping of video concepts", "End-to-end automated film pipeline"],
    useCasesZh: ["从小说文本做短剧", "漫画风格视频制作", "视频概念快速原型", "端到端自动影视流水线"],
    targetAudience: "Filmmakers, drama studios, and content teams who want an industrial-grade AI pipeline that runs end-to-end from script to finished video on their own infrastructure.",
    targetAudienceZh: "希望在自有基础设施上一条流水线跑通从脚本到成片的影视从业者、剧集工作室与内容团队。",
    pricingTiers: [
      {
        tier: "Free",
        tierZh: "免费版",
        price: "Free (open source)",
        features: ["Full-process automation", "Multi-role voice synthesis", "Bilingual UI", "Docker Compose self-host"],
        featuresZh: ["全流程自动化", "多角色语音合成", "中英双语界面", "Docker Compose自托管"],
      },
    ],
    pros: ["End-to-end pipeline in a single tool", "Open-source and self-hostable", "Bilingual UI lowers the entry barrier"],
    prosZh: ["单条流水线跑通端到端", "开源可自托管", "中英双语界面降低使用门槛"],
    cons: ["Requires Docker for deployment", "Newer ecosystem and community", "Less mature than commercial video platforms"],
    consZh: ["需 Docker 部署", "生态与社区较新", "成熟度低于商业视频平台"],
    extensions: [],
    skills: ["Film production", "Script analysis", "Storyboarding", "Video compositing", "AI orchestration"],
    scene: "video-creation",
  },
  {
    id: "toonflow",
    name: "Toonflow",
    nameZh: "Toonflow",
    description: "An open-source AI creation tool that pairs an infinite canvas with agent-driven visual workflows — intelligent storyboarding for images and videos, with cross-platform support and AI-enforced character consistency across scenes.",
    descriptionZh: "开源AI创作工具，把无限画布与代理驱动的可视化工作流结合——为图像与视频做智能分镜，跨平台支持，AI强制保证角色在所有场景中保持一致。",
    category: "video",
    tags: ["toonflow", "ai-video", "storyboard", "agent", "open-source", "canvas", "comic"],
    difficulty: "beginner",
    url: "https://github.com/HBAI-Ltd/Toonflow-app",
    rating: r(4.4),
    pricing: "Free (open source)",
    useCase: "Visual storyboarding for webtoons, comic creation, and animated short films on an infinite drag-and-drop canvas",
    icon: "\u{1F4D0}",
    company: "HBAI Ltd",
    companyZh: "HBAI",
    founded: 2026,
    headquarters: "Open Source",
    descriptionLong: "Toonflow is an open-source AI creation tool hosted at github.com/HBAI-Ltd/Toonflow-app. It pairs an infinite drag-and-drop canvas with agent-driven visual workflows, supporting intelligent storyboarding for both images and videos. Multiple AI agents collaborate to handle different production stages, and the platform enforces character consistency so the same character stays on-model across every scene. Toonflow ships a cross-platform client for Windows and macOS and is best suited for webtoon and comic creation, animated short film production, and visual storyboarding for any video project where layout and continuity matter more than one-click generation.",
    descriptionLongZh: "Toonflow是托管在github.com/HBAI-Ltd/Toonflow-app的开源AI创作工具。它把无限拖拽式画布与代理驱动的可视化工作流结合在一起，为图像和视频提供智能分镜。多个AI代理协同处理不同制作阶段，平台强制保持角色一致性，让同一个角色在所有场景中都不走样。Toonflow提供Windows与macOS的跨平台客户端，最适合网漫与漫画创作、动画短片制作，以及任何把布局与连续性看得比“一键生成”更重的视频项目的可视化分镜。",
    advantages: ["Infinite drag-and-drop canvas for storyboarding", "Multiple collaborating AI agents", "Cross-platform Windows + macOS client", "AI-enforced character consistency across scenes", "Open-source and free to use"],
    advantagesZh: ["无限拖拽式分镜画布", "多个AI代理协同", "Windows + macOS跨平台客户端", "AI强制保持角色一致性", "开源免费"],
    useCases: ["Webtoon and comic creation", "Animated short film production", "Visual storyboarding for video projects", "Multi-agent visual pipelines"],
    useCasesZh: ["网漫与漫画创作", "动画短片制作", "视频项目的可视化分镜", "多代理可视化流水线"],
    targetAudience: "Comic creators, storyboard artists, and animation teams who want an open-source infinite canvas paired with multi-agent AI for visual storyboarding.",
    targetAudienceZh: "希望在无限画布上由多代理AI辅助完成分镜的漫画创作者、分镜师与动画团队。",
    pricingTiers: [
      {
        tier: "Free",
        tierZh: "免费版",
        price: "Free (open source)",
        features: ["Infinite canvas", "Multi-agent storyboarding", "Windows + macOS client", "Character consistency"],
        featuresZh: ["无限画布", "多代理分镜", "Windows + macOS客户端", "角色一致性"],
      },
    ],
    pros: ["Gentlest learning curve among the 5", "True infinite canvas for layout-heavy projects", "Open-source with cross-platform client"],
    prosZh: ["5款工具中学习曲线最低", "真正无限画布，适合布局密集型项目", "开源且跨平台"],
    cons: ["Less suited for one-click video generation", "Newer ecosystem and community", "Limited to storyboard/visual stage"],
    consZh: ["不太适合一键视频生成", "生态与社区较新", "主要服务分镜与可视化阶段"],
    extensions: [],
    skills: ["Storyboarding", "Infinite canvas", "Multi-agent collaboration", "Character consistency", "Visual layout"],
    scene: "video-creation",
  },
  {
    id: "open-generative-ai",
    name: "Open-Generative-AI",
    nameZh: "Open-Generative-AI",
    description: "An open-source video engine (MIT-licensed) that bundles 600+ models including Flux, Midjourney, Kling, and Sora for unrestricted self-hosted video generation — a commercial-platform alternative with no content censorship.",
    descriptionZh: "开源视频引擎（MIT协议），内置Flux、Midjourney、Kling、Sora等600+模型，支持本地自托管无限制视频生成——无内容审查的商业平台替代方案。",
    category: "video",
    tags: ["open-generative-ai", "ai-video", "open-source", "mit", "self-hosted", "unrestricted", "multi-model"],
    difficulty: "intermediate",
    url: "https://github.com/Anil-matcha/Open-Generative-AI",
    rating: r(4.5),
    pricing: "Free (open source, MIT license)",
    useCase: "Self-hosted, unrestricted video generation across 600+ models — a commercial-platform alternative for teams that need full content control",
    icon: "\u{1F310}",
    company: "Anil-matcha",
    companyZh: "Anil-matcha",
    founded: 2026,
    headquarters: "Open Source",
    descriptionLong: "Open-Generative-AI is an open-source video engine hosted at github.com/Anil-matcha/Open-Generative-AI and released under the MIT license. It bundles 600+ popular models — including Flux, Midjourney, Kling, and Sora — behind a single self-hostable interface, and offers unrestricted generation with no content filters or platform restrictions. The project is best understood as a commercial-platform alternative: teams that need full control over their generation pipeline and content, or that operate in regions or industries where commercial platforms impose limits, can run the engine locally and integrate the models that fit their use case. Being Node.js-based, it integrates easily into existing web stacks and custom video engines.",
    descriptionLongZh: "Open-Generative-AI是托管在github.com/Anil-matcha/Open-Generative-AI的开源视频引擎，采用MIT协议发布。它把600+主流模型——包括Flux、Midjourney、Kling和Sora——整合在一个可自托管的界面下，提供无内容过滤、无平台限制的无限制生成能力。这个项目最准确的定位是商业平台的替代方案：需要完全掌控生成流水线和内容的团队，或在商业平台施加限制的地区/行业工作的团队，可以本地运行引擎并按需接入模型。引擎基于Node.js构建，能轻松集成进现有的Web技术栈和自定义视频引擎。",
    advantages: ["MIT-licensed, free for commercial use", "600+ models including Flux, Midjourney, Kling, Sora", "Unrestricted generation — no platform content filters", "Self-hosted for full content and data control", "Node.js-based for easy integration"],
    advantagesZh: ["MIT协议，可商用", "600+模型，包括Flux、Midjourney、Kling、Sora", "无内容审查的无限制生成", "本地自托管，完全掌控内容与数据", "Node.js技术栈，易于集成"],
    useCases: ["Unrestricted video generation", "Alternative to commercial video platforms", "Custom video engine development", "Self-hosted multi-model generation"],
    useCasesZh: ["无限制视频生成", "商业视频平台的替代方案", "自定义视频引擎开发", "本地自托管多模型生成"],
    targetAudience: "Teams and developers who need an unrestricted, self-hostable video engine with access to 600+ models and full content control.",
    targetAudienceZh: "需要无限制、可自托管、能调用600+模型且完全掌控内容的团队与开发者。",
    pricingTiers: [
      {
        tier: "Free",
        tierZh: "免费版",
        price: "Free (open source, MIT license)",
        features: ["600+ models", "Unrestricted generation", "Self-hosted", "Commercial use allowed"],
        featuresZh: ["600+模型", "无限制生成", "可自托管", "允许商业使用"],
      },
    ],
    pros: ["MIT license, free for commercial use", "Largest model bundle in this list", "True self-hosting and content control"],
    prosZh: ["MIT协议，可商用", "5款中模型最全", "真正自托管，完整掌控内容"],
    cons: ["No first-party UI polish compared to commercial platforms", "You operate and maintain the infrastructure", "Node.js stack required"],
    consZh: ["相对商业平台UI打磨度一般", "需自行运维基础设施", "需要Node.js技术栈"],
    extensions: [],
    skills: ["Video generation", "Multi-model orchestration", "Self-hosting", "Unrestricted content", "MIT licensing"],
    scene: "video-creation",
  },
  {
    id: "diffusers",
    name: "diffusers",
    nameZh: "diffusers",
    description: "The de facto full-modal diffusion model library — production-ready infrastructure for images, video, audio, and 3D, used by leading AI companies to build custom generation pipelines with first access to the latest diffusion models.",
    descriptionZh: "事实标准的全模态扩散模型库——生产就绪的基础设施，覆盖图像、视频、音频乃至3D，是头部AI公司构建自定义生成流水线的底座，第一手拿到最新扩散模型。",
    category: "ai-development",
    tags: ["diffusers", "diffusion", "image", "video", "audio", "3d", "open-source", "python", "huggingface"],
    difficulty: "intermediate",
    url: "https://github.com/huggingface/diffusers",
    rating: r(4.8),
    pricing: "Free (open source, Apache 2.0)",
    useCase: "Build custom AI generation pipelines for images, video, audio, and 3D with the de facto diffusion library",
    icon: "\u{1F4E6}",
    company: "Hugging Face",
    companyZh: "Hugging Face",
    founded: 2022,
    headquarters: "Paris, France",
    descriptionLong: "diffusers is the de facto full-modal diffusion model library maintained by Hugging Face at github.com/huggingface/diffusers. It is the foundation layer used by leading AI companies to build production-grade generation pipelines for images, video, audio, and even 3D structures. The library gives first access to the latest diffusion models as they are released, and its modular design lets teams mix and match components — pipelines, schedulers, models — to build custom generation systems. A simple example: install diffusers with accelerate and transformers, load a Flux checkpoint via DiffusionPipeline.from_pretrained, and start generating images in a few lines of Python. diffusers is the right pick when you need a battle-tested, model-agnostic diffusion layer underneath your own tools, services, or research.",
    descriptionLongZh: "diffusers是由Hugging Face维护的事实标准全模态扩散模型库，托管在github.com/huggingface/diffusers。它是头部AI公司用来构建生产级图像、视频、音频乃至3D结构生成流水线的底座。库本身第一时间跟进最新发布的扩散模型，模块化设计让团队能自由拼装组件——pipeline、scheduler、模型——构建自己的生成系统。举个最简单的例子：pip安装diffusers、accelerate、transformers，通过DiffusionPipeline.from_pretrained加载一个Flux检查点，几行Python代码就能开始生成图像。diffusers是当你需要一个经过实战检验、与模型无关的扩散层垫在自己工具、服务或研究下面时的首选。",
    advantages: ["Full-modal: image, video, audio, 3D", "First access to the latest diffusion models", "Modular pipelines, schedulers, and models", "Used by leading AI companies in production", "Apache 2.0, free for commercial use"],
    advantagesZh: ["全模态：图像、视频、音频、3D", "第一时间拿到最新扩散模型", "模块化pipeline、scheduler与模型", "头部AI公司的生产级底座", "Apache 2.0协议，可商用"],
    useCases: ["Foundation for custom AI generation tools", "Research and development of new diffusion models", "Production-grade AI generation pipelines", "Image, video, audio, and 3D generation"],
    useCasesZh: ["自定义AI生成工具的底座", "新型扩散模型研发", "生产级AI生成流水线", "图像、视频、音频、3D生成"],
    targetAudience: "Developers, ML researchers, and AI companies that need a production-grade, model-agnostic diffusion layer for custom generation systems.",
    targetAudienceZh: "需要为自定义生成系统提供生产级、与模型无关的扩散层的开发者、ML研究员与AI公司。",
    pricingTiers: [
      {
        tier: "Free",
        tierZh: "免费版",
        price: "Free (open source, Apache 2.0)",
        features: ["Full-modal diffusion library", "Latest model access", "Modular pipelines", "Commercial use allowed"],
        featuresZh: ["全模态扩散库", "最新模型接入", "模块化pipeline", "允许商业使用"],
      },
    ],
    pros: ["Battle-tested by major AI companies", "Largest diffusion model ecosystem", "Apache 2.0, free for commercial use"],
    prosZh: ["头部AI公司实战检验", "最大的扩散模型生态", "Apache 2.0，可商用"],
    cons: ["Requires ML expertise to use effectively", "Compute-intensive — strong GPU recommended", "Python-only"],
    consZh: ["需要机器学习背景才能用好", "算力密集，建议有强力GPU", "仅Python"],
    extensions: [],
    skills: ["Diffusion models", "Image generation", "Video generation", "Audio generation", "3D generation", "Pipeline orchestration"],
    scene: "development",
  },
  {
    id: "openmontage",
    name: "OpenMontage",
    nameZh: "OpenMontage",
    description: "An AI tool that automates video editing and music composition end-to-end — agent-driven research, scriptwriting, storyboarding, and editing plus AI-generated background music that matches your video, ready for distribution.",
    descriptionZh: "自动化视频剪辑与音乐合成的AI工具——代理驱动的调研、脚本、分镜、剪辑，以及能匹配视频画面的AI自动背景音乐生成，可直接发布。",
    category: "video",
    tags: ["openmontage", "ai-video", "editing", "music", "agent", "open-source", "npm"],
    difficulty: "beginner",
    url: "https://www.npmjs.com/package/openmontage",
    rating: r(4.4),
    pricing: "Free (open source)",
    useCase: "Automated video editing and music composition for social-media creators who want one pipeline from raw footage to finished video",
    icon: "\u{1F3B5}",
    company: "OpenMontage",
    companyZh: "OpenMontage",
    founded: 2026,
    headquarters: "Open Source",
    descriptionLong: "OpenMontage is an AI tool, distributed via npm as openmontage, that automates video editing and music composition from end to end. AI agents handle research, scriptwriting, storyboarding, and editing, while a separate module generates background music that matches the visual mood and pacing of the video. The full workflow runs from raw footage to finished, distribution-ready video in a single pipeline. Installation is one npm command: npm install -g openmontage, then openmontage start. OpenMontage is the easiest entry point in this list for content creators who want to automate short-form, social-media-style videos without juggling multiple tools.",
    descriptionLongZh: "OpenMontage是一款通过npm分发的AI工具（包名openmontage），端到端自动化视频剪辑和音乐合成。AI代理负责调研、脚本、分镜和剪辑，独立模块则生成与画面情绪和节奏匹配的背景音乐。整个工作流从素材到可发布的成片在一条流水线内完成。安装只需一条npm命令：npm install -g openmontage，然后openmontage start。OpenMontage是这份清单中，对想要自动化短内容/社媒视频的创作者最友好的入门工具——无需在多款工具之间切换。",
    advantages: ["One-line npm install", "Agent-driven editing + automatic music composition", "End-to-end pipeline from footage to finished video", "Production-grade output ready for distribution", "Open-source and free to use"],
    advantagesZh: ["一行npm安装", "代理驱动剪辑 + 自动音乐合成", "从素材到成片的端到端流水线", "生产级输出，可直接发布", "开源免费"],
    useCases: ["Automated video editing", "Music composition for videos", "Rapid social-media video production", "Agent-driven short-form content"],
    useCasesZh: ["自动视频剪辑", "视频音乐创作", "社媒快速视频制作", "代理驱动的短视频内容"],
    targetAudience: "Content creators and social-media teams who want the simplest path from raw footage to a finished, ready-to-publish video with matching music.",
    targetAudienceZh: "希望用最简单的方式从素材走到可发布成片，并自带匹配音乐的内容创作者与社媒团队。",
    pricingTiers: [
      {
        tier: "Free",
        tierZh: "免费版",
        price: "Free (open source)",
        features: ["One-line install via npm", "Agent-driven editing", "AI music composition", "Full-process automation"],
        featuresZh: ["npm一行安装", "代理驱动剪辑", "AI音乐合成", "全流程自动化"],
      },
    ],
    pros: ["Simplest install among the 5", "Auto-generates music that matches the video", "Best fit for short-form social content"],
    prosZh: ["5款中安装最简单", "自动生成匹配视频的音乐", "最适合短视频与社媒内容"],
    cons: ["Less control over granular editing", "Newer ecosystem and community", "Node.js stack required"],
    consZh: ["细粒度剪辑控制有限", "生态与社区较新", "需要Node.js技术栈"],
    extensions: [],
    skills: ["Video editing", "Music composition", "Agent orchestration", "Storyboarding", "Scriptwriting"],
    scene: "video-creation",
  },
  """
pos = s.rfind("] as Tool[];")
assert pos > 0
s2 = s[:pos] + tools_block + s[pos:]
io.open(f, "w", encoding="utf-8", newline="\n").write(s2)
print("tools.ts entries:", s2.count('id: "'))
print("DONE")
