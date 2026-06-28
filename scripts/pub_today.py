"""
Publish June 28, 2026 articles.
No new tools - both articles reference existing tools (Nvidia/Intel are hardware, Codex/Vercel already in tools.ts)
"""
import os

BASE = r"C:\Users\jun\aistudyonline-next"
os.chdir(BASE)

# ===== Part 1: Add 2 article metadata to articles.ts =====
with open('src/lib/articles.ts', 'r', encoding='utf-8') as f:
    articles_src = f.read()

new_articles = r"""  {
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

"""

last_bracket = articles_src.rfind('];')
articles_new = articles_src[:last_bracket] + new_articles + '];'

with open('src/lib/articles.ts', 'w', encoding='utf-8') as f:
    f.write(articles_new)

print('Part 1: 2 new articles added to articles.ts')

# ===== Part 2: Add 2 article contents to article-content.ts =====
with open('src/lib/article-content.ts', 'r', encoding='utf-8') as f:
    content_src = f.read()

new_contents = r'''
  "ai-infrastructure-revolution-bubble-computing-power": {
    content: `<div class="meta-banner">
<p><strong>📅 Published:</strong> June 28, 2026 · <strong>🏷️ Category:</strong> AI Tutorials · <strong>📊 Level:</strong> Intermediate</p>
</div>

<p>Is AI infrastructure a bubble or a revolution? With planned investments like the $500 billion Star Gate Project and North American tech giants' combined capex reaching $690 billion in 2026, the AI computing power gold rush shows no signs of slowing. Nvidia's revenue surged from 186 billion yuan in early 2023 to 1.49 trillion yuan by early 2026 — a nearly 8x increase. Let's dissect the full supply chain: chips, PCBs, optical modules, switches, cooling, and power systems.</p>

<h2>The Core Components of AI Computing Power</h2>

<h3>1. Computing Hardware: Nvidia DGX H100 AI Server</h3>

<p>A standard <strong>Nvidia DGX H100 AI server</strong> (worth over 2 million RMB) is a marvel of engineering:</p>

<ul>
<li>8 <strong>Nvidia H100 GPU chips</strong>, each surrounded by 6 SK Hynix HBM high-bandwidth memory chips using TSMC's top-tier packaging</li>
<li>4 Nvidia NVSwitch chips enabling zero-latency communication between GPUs</li>
<li>2 Intel Xeon CPUs, 2TB of system memory, and PCIe data lines for data scheduling</li>
<li>High-speed network cards with optical modules for data transmission</li>
<li>All components mounted on a high-performance PCB</li>
</ul>

<pre><code class="language-plaintext"># Key Components of Nvidia DGX H100
- GPUs: 8 x Nvidia H100
- Memory: 6 x SK Hynix HBM per GPU
- Switches: 4 x Nvidia NVSwitch
- CPUs: 2 x Intel Xeon
- System Memory: 2TB
- Network: High-speed NICs with optical modules
- Carrier: High-performance PCB</code></pre>

<h3>2. Network Equipment: Switches and Optical Modules</h3>

<p>To ensure efficient collaboration among hundreds of thousands of GPUs, network equipment is crucial:</p>

<ul>
<li><strong>Leaf Switches (Cabinet-Level):</strong> Distribution centers collecting data from the same or adjacent cabinets, using multi-mode (light blue) and single-mode (yellow) optical fibers via optical modules.</li>
<li><strong>Spine Switches (Independent-Level):</strong> Aggregate hundreds of leaf switches, connecting countless cabinets into a massive computing cluster.</li>
</ul>

<h3>3. Cooling and Space: Liquid Cooling</h3>

<p>Traditional air cooling limits server density. Liquid cooling, as seen in Elon Musk's XAI data center, solves this: it removes air-cooling systems, reducing server thickness by half. A single cabinet can now hold 8 servers (64 H100 chips), doubling density and cutting costs for cloud vendors.</p>

<h2>The Evolution to NVL72: A Paradigm Shift</h2>

<p>Nvidia's latest <strong>GB300 NVL72 cabinet</strong> (mass-produced May 2025) represents a radical redesign:</p>

<ul>
<li><strong>Compute Trays:</strong> Each contains Nvidia Grace CPUs, Blackwell GPUs, DPUs (security and scheduling), and ConnectX network cards — all Nvidia-owned hardware.</li>
<li><strong>NVLink Spine Backplane:</strong> A 70-pound copper interconnection system connecting 72 GPUs into a single virtual super GPU, eliminating optical modules inside the cabinet.</li>
<li><strong>Switch Trays:</strong> 9 trays with NVLink switch chips enable seamless communication.</li>
</ul>

<p>This design pushes Scale-Up (physical memory sharing) to 72 GPUs, reducing latency and increasing bandwidth to 130TB/s.</p>

<h2>Supply Chain Reconstruction and Competitive Landscape</h2>

<p><strong>Nvidia's Dominance:</strong> It has evolved from a GPU supplier to a system-level infrastructure provider. Cloud vendors must adopt its entire ecosystem — networks, CPUs, GPUs, and cabinet standards. Secondary suppliers risk obsolescence if they can't keep pace.</p>

<h2>Practical Insights for Investors and Builders</h2>

<p>Identify "shovel sellers" in this ecosystem:</p>

<ul>
<li><strong>Chips and Servers:</strong> Nvidia (GPUs, DPUs), Intel/AMD (CPUs), TSMC (packaging)</li>
<li><strong>Network Equipment:</strong> Cisco, Broadcom (switches), Huawei, ZTE (optical modules)</li>
<li><strong>Cooling and Power:</strong> Companies specializing in liquid cooling and high-power supply systems</li>
</ul>

<p>AI infrastructure is not a bubble but a necessary investment for the next tech revolution. Understanding each component's role and dynamics helps you navigate this landscape and seize opportunities.</p>

<h2>常见问题</h2>

<h3>Is the AI infrastructure boom a bubble like the dot-com era?</h3>
<p>The comparison is natural but the dynamics differ. Dot-com was fueled by speculation on future profits; AI infrastructure is backed by real, measurable demand — large models with trillion-level parameters need massive compute for both training and inference. Training one model can require 100,000 GPUs running for 3 months. Revenue at companies across the supply chain (switches, optical modules, storage chips, PCBs) has all grown significantly. The risk isn't a bubble popping — it's overcapacity if model efficiency improvements reduce compute demand faster than new applications increase it.</p>

<h3>Why is Nvidia so dominant in AI infrastructure?</h3>
<p>Nvidia's CUDA ecosystem created a massive software moat — most AI frameworks (PyTorch, TensorFlow) are optimized for CUDA first. Their NVLink and NVSwitch technologies enable GPU-to-GPU communication that competitors can't match. With NVL72, they've moved from selling GPUs to selling entire cabinets where every component (CPU, GPU, DPU, NIC, switch) is Nvidia-designed. Cloud providers effectively must adopt the full Nvidia stack. Competitors like AMD and Intel are closing the hardware gap but remain years behind on the software ecosystem.</p>

<h3>What does this mean for AI developers and startups?</h3>
<p>Compute costs will likely continue falling per unit of performance, even as total spending rises. The NVL72 architecture reduces per-GPU costs through density improvements. For developers, the key takeaway is that AI model training and inference will get cheaper over time — plan your product roadmaps accordingly. For startups building AI infrastructure tools, the opportunity is in the gaps Nvidia doesn't cover: specialized inference hardware, edge computing, and software that makes heterogeneous compute (mixing GPU brands) practical.</p>

<div class="next-step">
<p><strong>下一篇：</strong> <a href="/en/article/codex-website-dev-zero-basis-tutorial">Codex Website Development: Zero-Basis Practical Tutorial and Deployment Guide →</a></p>
</div>`,
    contentZh: `<div class="meta-banner">
<p><strong>📅 发布日期：</strong>2026年6月28日 · <strong>🏷️ 分类：</strong>AI教程 · <strong>📊 难度：</strong>中级</p>
</div>

<p>AI基础设施是泡沫还是革命？星门计划5000亿美元投资、北美五大科技巨头2026年资本支出预计达6900亿美元——AI算力淘金热毫无降温迹象。Nvidia营收从2023年初的1860亿元飙升至2026年初的1.49万亿元，增长近8倍。让我们拆解完整供应链：芯片、PCB、光模块、交换机、散热和电源系统。</p>

<h2>AI算力基础设施的核心组件</h2>

<h3>1. 算力硬件：Nvidia DGX H100 AI服务器</h3>

<p>一台标准 <strong>Nvidia DGX H100 AI服务器</strong>（价值超200万元）是工程奇迹：</p>

<ul>
<li>8颗 <strong>Nvidia H100 GPU芯片</strong>，每颗周围环绕6颗SK海力士HBM高带宽内存芯片，采用台积电顶级封装技术</li>
<li>4颗Nvidia NVSwitch芯片实现GPU间零延迟通信</li>
<li>2颗Intel Xeon CPU、2TB系统内存、PCIe数据线负责数据调度</li>
<li>带光模块的高速网卡负责数据传输</li>
<li>所有组件安装在高性能PCB基板上</li>
</ul>

<pre><code class="language-plaintext"># Nvidia DGX H100 关键组件
- GPU：8 x Nvidia H100
- 内存：每GPU 6 x SK海力士HBM
- 交换机芯片：4 x Nvidia NVSwitch
- CPU：2 x Intel Xeon
- 系统内存：2TB
- 网络：带光模块的高速网卡
- 基板：高性能PCB</code></pre>

<h3>2. 网络设备：交换机和光模块</h3>

<p>确保数十万GPU高效协作，网络设备至关重要：</p>

<ul>
<li><strong>Leaf交换机（机柜级）：</strong> 充当分配中心，收集同一或相邻机柜的数据，通过光模块连接多模（浅蓝）和单模（黄色）光纤。</li>
<li><strong>Spine交换机（独立级）：</strong> 汇聚数百台Leaf交换机，将无数机柜连接成庞大算力集群。</li>
</ul>

<h3>3. 散热与空间：液冷</h3>

<p>传统风冷限制服务器密度。Elon Musk的XAI数据中心采用的液冷方案解决了这个问题：移除风冷系统，服务器厚度减半。单个机柜现在可容纳8台服务器（64颗H100芯片），密度翻倍，为云厂商降低成本。</p>

<h2>NVL72进化：范式转变</h2>

<p>Nvidia最新的 <strong>GB300 NVL72机柜</strong>（2025年5月量产）是彻底重构：</p>

<ul>
<li><strong>计算托盘：</strong> 每个包含Nvidia Grace CPU、Blackwell GPU、DPU（安全调度）和ConnectX网卡——全部Nvidia自有硬件。</li>
<li><strong>NVLink Spine背板：</strong> 70磅铜互联系统将72颗GPU连接成单个虚拟超级GPU，机柜内不再需要光模块。</li>
<li><strong>交换托盘：</strong> 9个托盘搭载NVLink交换芯片实现无缝通信。</li>
</ul>

<p>该设计将Scale-Up（物理内存共享）推向72颗GPU，降低延迟、带宽提升至130TB/s。</p>

<h2>供应链重构与竞争格局</h2>

<p><strong>Nvidia的统治力：</strong> 已从GPU供应商进化为系统级基础设施提供商。云厂商必须采用其完整生态——网络、CPU、GPU和机柜标准。次级供应商跟不上技术就可能被淘汰。</p>

<h2>投资者和建设者的实操洞察</h2>

<p>识别这个生态系统中的"卖铲人"：</p>

<ul>
<li><strong>芯片与服务器：</strong> Nvidia（GPU、DPU）、Intel/AMD（CPU）、台积电（封装）</li>
<li><strong>网络设备：</strong> Cisco、Broadcom（交换机）、华为、中兴（光模块）</li>
<li><strong>散热与电源：</strong> 专注液冷和大功率供电系统的公司</li>
</ul>

<p>AI基础设施不是泡沫，而是下一次科技革命的必要投资。理解每个组件的角色和动态，帮助你在这一格局中把握机遇。</p>

<h2>常见问题</h2>

<h3>AI基础设施热潮像互联网泡沫吗？</h3>
<p>这个比较很自然但动态不同。互联网泡沫由对未来利润的投机驱动；AI基础设施有真实、可衡量的需求支撑——万亿参数大模型的训练和推理都需要海量算力。训练一个模型可能需要10万GPU运行3个月。供应链各环节公司（交换机、光模块、存储芯片、PCB）的营收都显著增长。风险不是泡沫破裂——而是如果模型效率提升降低算力需求的速度超过新应用增加需求的速度，可能出现产能过剩。</p>

<h3>为什么Nvidia在AI基础设施中如此主导？</h3>
<p>Nvidia的CUDA生态创造了巨大的软件护城河——大多数AI框架（PyTorch、TensorFlow）优先为CUDA优化。NVLink和NVSwitch技术实现了竞争对手无法匹敌的GPU间通信。通过NVL72，他们已从卖GPU转向卖整机柜，每个组件（CPU、GPU、DPU、网卡、交换机）都是Nvidia设计。云厂商实际上必须采用完整Nvidia方案。AMD和Intel等竞争对手正在缩小硬件差距，但在软件生态上仍落后数年。</p>

<h3>这对AI开发者和创业公司意味着什么？</h3>
<p>算力单位性能成本可能持续下降，即使总支出在上升。NVL72架构通过密度提升降低了单GPU成本。对开发者来说，关键启示是AI模型训练和推理会随时间变得更便宜——据此规划产品路线图。对构建AI基础设施工具的创业公司，机会在Nvidia未覆盖的领域：专用推理硬件、边缘计算、以及让异构计算（混合GPU品牌）变得实用的软件。</p>

<div class="next-step">
<p><strong>下一篇：</strong> <a href="/zh/article/codex-website-dev-zero-basis-tutorial">Codex网站开发：零基础实战教程与部署指南 →</a></p>
</div>`,
  },

  "codex-website-dev-zero-basis-tutorial": {
    content: `<div class="meta-banner">
<p><strong>📅 Published:</strong> June 28, 2026 · <strong>🏷️ Category:</strong> AI Tutorials · <strong>📊 Level:</strong> Beginner · <strong>🛠️ Tools:</strong> Codex, Vercel</p>
</div>

<p>Gone are the days when building a website required mastering programming, code, and UI design — filled with confusing technical jargon. With <strong>Codex</strong>, you can overcome technical limitations. Just tell it your needs like a boss, and it will build the website step by step for you. In this tutorial, I'll show you how to build a stunning cat-themed website from scratch with zero coding experience, covering two building methods and one-click deployment.</p>

<h2>Method 1: Pure Personalized Building</h2>

<h3>Step 1: Define the Website Framework</h3>

<p>Start by outlining your website's structure, sections, and overall style directly in Codex:</p>

<blockquote>"I want to build a cat website. It should include sections like a cat's profile, daily diary, photo gallery, growth timeline, and favorite recipes. The style should be warm and whimsical."</blockquote>

<p>You can also upload a document with detailed requirements. Once you send your request, Codex works in the background — the basic structure and blocks are laid out, though it may lack some ideal elements. That's normal: Codex has just created the skeleton.</p>

<h3>Step 2: Refine Details</h3>

<p>Keep submitting modification requests to polish details:</p>

<ol>
<li>Open the website preview in Codex</li>
<li>Click the plus sign in the top right corner</li>
<li>Select the area to modify and add a comment: <em>"Change the font color of the 'Cat's Diary' section to a soft orange and increase the image spacing."</em></li>
</ol>

<h3>Step 3: Enhance with Images and Sections</h3>

<p>To add new sections like a photo gallery or favorite recipes, describe them to Codex:</p>

<blockquote>"Add a photo gallery section with images of the cat napping, eating, and playing. The layout should be a grid with hover effects."</blockquote>

<p>If you don't have images, use Codex's built-in <strong>Image 2</strong> feature:</p>

<pre><code class="language-plaintext">@image2 [Orange Cat] Orange cat running in garden, sunny, oil painting style
@image2 [Orange Cat] Orange cat drinking coffee in cafe, warm scene, illustration style</code></pre>

<h3>Step 4: Add Visual Effects and Animations</h3>

<p>To make your website more dynamic, describe effects to Codex. For inspiration, browse resources like <strong>React Bits</strong> for backgrounds, text animations, and border effects. Copy code for an effect you like and tell Codex:</p>

<blockquote>"Apply this glowing text animation to the 'Cat's Motto' section. The color should be light purple."</blockquote>

<p>Codex will implement it — for example, text animation mimicking a cat's gentle movement, and background texture following the mouse cursor.</p>

<h2>Method 2: Quick Creative Building</h2>

<p>For a faster setup using pre-existing design references:</p>

<ol>
<li>Find headings and landing page designs online (e.g., from design platforms)</li>
<li>Copy the prompt of a design you like</li>
<li>Paste it into Codex combined with your own content:</li>
</ol>

<blockquote>"Use this landing page layout for a cat website. Replace the content with my cat's details: name 'Mikan', age 3, breed 'American Shorthair Tabby'."</blockquote>

<h2>Deploying Your Website Online</h2>

<p>Your website initially runs only on your local computer. To make it accessible to others, deploy to <strong>Vercel</strong>:</p>

<ol>
<li>Install the Vercel plugin in Codex</li>
<li>Log in to your Vercel account to authorize</li>
<li>In the Codex chat, mention the Vercel plugin: <em>"@Vercel deploy this cat website online"</em></li>
</ol>

<p>Codex will deploy your site and provide a public URL like <code>https://your-cat-website.vercel.app</code> — anyone can access it anytime.</p>

<h2>Conclusion</h2>

<p>Building a website with Codex is straightforward and requires no technical background. Whether you choose personalized customization or quick creative building, you'll gain a sense of accomplishment. In this AI-driven era, let Codex be your tool to bring ideas to life. Try it out and unleash your creativity!</p>

<h2>常见问题</h2>

<h3>Do I need to know HTML/CSS to use Codex for website building?</h3>
<p>No — that's the whole point. Codex handles all the coding. You describe what you want in natural language, and it generates the code. That said, having basic HTML/CSS knowledge helps you give more precise instructions and understand what's happening. But it's absolutely not required. Many complete beginners have built and deployed their first website with Codex in under an hour.</p>

<h3>What's the difference between Method 1 (personalized) and Method 2 (quick creative)?</h3>
<p>Method 1 gives you full creative control — you describe every section from scratch, refine iteratively, and end up with a unique design. It takes longer but produces more original results. Method 2 uses pre-existing design templates as starting points, which is faster but may result in a less distinctive look. For a portfolio or personal brand site, go with Method 1. For a quick prototype or temporary page, Method 2 works great.</p>

<h3>Can I use other deployment platforms besides Vercel?</h3>
<p>Yes. While Vercel is the most integrated option (Codex has a built-in Vercel plugin), you can also deploy to Netlify, GitHub Pages, Alibaba Cloud, Tencent Cloud, or any static hosting service. The key difference is convenience: Vercel deployment is one command through the plugin, while other platforms may require you to export the code first and configure deployment manually. For beginners, Vercel is strongly recommended as the path of least resistance.</p>

<div class="next-step">
<p><strong>上一篇：</strong> <a href="/en/article/ai-infrastructure-revolution-bubble-computing-power">AI Infrastructure: Revolution or Bubble? A Deep Dive into the Computing Power Ecosystem ←</a></p>
</div>`,
    contentZh: `<div class="meta-banner">
<p><strong>📅 发布日期：</strong>2026年6月28日 · <strong>🏷️ 分类：</strong>AI教程 · <strong>📊 难度：</strong>初级 · <strong>🛠️ 工具：</strong>Codex、Vercel</p>
</div>

<p>建网站需要掌握编程、代码和UI设计的时代已经过去了——充满令人困惑的技术术语。有了 <strong>Codex</strong>，你可以突破技术限制。像老板一样告诉它你的需求，它会一步步为你建网站。本教程展示如何用零编程经验从零构建惊艳的猫咪主题网站，涵盖两种搭建方法和一键部署。</p>

<h2>方法1：纯个性化搭建</h2>

<h3>第1步：定义网站框架</h3>

<p>直接在Codex中描述网站结构、板块和整体风格：</p>

<blockquote>"我想建一个猫咪网站。应该包含猫咪简介、日常日记、照片画廊、成长时间线和最爱食谱等板块。风格温暖奇幻。"</blockquote>

<p>也可以上传详细需求文档。发出请求后Codex在后台工作——基本结构和板块已布局，但可能缺少一些理想元素。这很正常：Codex刚创建了骨架。</p>

<h3>第2步：细化细节</h3>

<p>持续提交修改请求打磨细节：</p>

<ol>
<li>在Codex中打开网站预览</li>
<li>点击右上角加号</li>
<li>选择要修改的区域添加注释：<em>"把'猫咪日记'板块的字体颜色改成柔和的橙色，增加图片间距。"</em></li>
</ol>

<h3>第3步：用图片和板块增强</h3>

<p>要添加照片画廊或最爱食谱等新板块，向Codex描述：</p>

<blockquote>"添加照片画廊板块，包含猫咪打盹、吃饭和玩耍的图片。布局为带悬停效果的网格。"</blockquote>

<p>如果没有图片，使用Codex内置的 <strong>Image 2</strong> 功能生成：</p>

<pre><code class="language-plaintext">@image2 [橘猫] 橘猫在花园里奔跑，阳光明媚，油画风格
@image2 [橘猫] 橘猫在咖啡馆里喝咖啡，温馨场景，插画风格</code></pre>

<h3>第4步：添加视觉效果和动画</h3>

<p>让网站更生动，向Codex描述想要的效果。如需灵感，浏览 <strong>React Bits</strong> 等资源获取背景、文字动画和边框效果。复制喜欢的效果代码告诉Codex：</p>

<blockquote>"把这个发光文字动画应用到'猫咪格言'板块。颜色用淡紫色。"</blockquote>

<p>Codex会实现——例如文字动画模仿猫咪轻柔的动作，背景纹理跟随鼠标光标。</p>

<h2>方法2：快速创意搭建</h2>

<p>使用现有设计参考更快搭建：</p>

<ol>
<li>在网上找标题和落地页设计（如设计平台）</li>
<li>复制喜欢的设计提示词</li>
<li>粘贴到Codex并结合自己的内容：</li>
</ol>

<blockquote>"用这个落地页布局做猫咪网站。替换内容为我的猫的详情：名字'蜜柑'，3岁，品种'美短虎斑'。"</blockquote>

<h2>将网站部署上线</h2>

<p>网站最初只在本地运行。要让别人访问，部署到 <strong>Vercel</strong>：</p>

<ol>
<li>在Codex中安装Vercel插件</li>
<li>登录Vercel账号授权</li>
<li>在Codex聊天中@Vercel插件：<em>"@Vercel 部署这个猫咪网站上线"</em></li>
</ol>

<p>Codex会部署网站并提供公开URL如 <code>https://your-cat-website.vercel.app</code>——任何人都能随时访问。</p>

<h2>总结</h2>

<p>用Codex建网站简单直接，不需要技术背景。无论选择个性化定制还是快速创意搭建，都会获得成就感。在这个AI驱动的时代，让Codex成为你实现创意的工具。试试看，释放你的创造力！</p>

<h2>常见问题</h2>

<h3>用Codex建网站需要懂HTML/CSS吗？</h3>
<p>不需要——这正是Codex的意义所在。Codex处理所有编码。你用自然语言描述需求，它生成代码。不过，有基础HTML/CSS知识能帮你给出更精准的指令和理解发生了什么。但绝对不是必需的。许多完全零基础的新手在一小时内用Codex搭建并部署了他们的第一个网站。</p>

<h3>方法1（个性化）和方法2（快速创意）有什么区别？</h3>
<p>方法1给你完全创意控制——你从零描述每个板块，迭代打磨，最终得到独特设计。耗时更长但产出更原创。方法2使用现有设计模板作为起点，更快但可能导致外观不够独特。做作品集或个人品牌网站用方法1。快速原型或临时页面方法2效果很好。</p>

<h3>除了Vercel还能用其他部署平台吗？</h3>
<p>可以。虽然Vercel是集成度最高的选项（Codex有内置Vercel插件），你也可以部署到Netlify、GitHub Pages、阿里云、腾讯云或任何静态托管服务。关键区别是便利性：Vercel部署通过插件一条命令完成，其他平台可能需要先导出代码再手动配置部署。对初学者强烈推荐Vercel作为阻力最小的路径。</p>

<div class="next-step">
<p><strong>上一篇：</strong> <a href="/zh/article/ai-infrastructure-revolution-bubble-computing-power">AI基础设施：革命还是泡沫？算力生态深度解析 ←</a></p>
</div>`,
  },

'''

last_brace = content_src.rfind('};')
content_new = content_src[:last_brace] + new_contents + '};'

with open('src/lib/article-content.ts', 'w', encoding='utf-8') as f:
    f.write(content_new)

print('Part 2: 2 article contents added to article-content.ts')

print('\n=== All done! Run build to verify ===')
