"""Publish Aug 7, 2026 — 1 article + 1 new tool (Seedance 2.5)."""
import os; BASE = r"C:\Users\jun\aistudyonline-next"; os.chdir(BASE)

with open('src/lib/articles.ts', 'r', encoding='utf-8') as f: s = f.read()
a = r"""  {
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

"""
last = s.rfind('];')
with open('src/lib/articles.ts', 'w', encoding='utf-8') as f: f.write(s[:last] + a + '];')
print('Part 1 done')

with open('src/lib/article-content.ts', 'r', encoding='utf-8') as f: c = f.read()
n = r'''
  "master-seedance-2-5-zero-basics-guide-commercial-grade-ai-video-creation": {
    content: `<div class="meta-banner">
  <span class="meta-badge">🔧 AI Tools</span>
  <span class="meta-badge">🕒 8 min read</span>
  <span class="meta-badge">📅 Aug 7, 2026</span>
  <span class="meta-badge">🎯 Beginner</span>
</div>

<h2 id="introduction">Introduction</h2>
<p>Seedance 2.5 is not just a parameter upgrade — it represents a paradigm shift where AI can now directly generate fully commercial-ready video content in one go. This hands-on guide distills real-world testing insights and practical workflows, enabling beginners to transform into professional AI creators by mastering prompt writing, multi-scenario application, and cost control.</p>

<h2 id="advantages">Core Advantages of Seedance 2.5</h2>
<ul>
  <li><strong>Direct Long-Form Video Generation</strong>: Supports single-shot generation up to 30 seconds, with an extended mode for maximum 3-minute clips, eliminating the need for manual splicing</li>
  <li><strong>Ultra-Realistic Visual Quality</strong>: Significantly reduces the "AI rendering texture" of version 2.0, achieving near-photorealistic skin details and natural motion capture effects</li>
  <li><strong>Multi-Functional Workflow</strong>: Covers full-cycle video production from raw material generation, targeted editing to style replication</li>
  <li><strong>Highly Flexible Reference System</strong>: Accepts up to 50 reference materials for complex style fusion and content customization</li>
</ul>

<h2 id="workflow1">Core Workflow 1: Direct Commercial Video Generation</h2>

<h3>Universal Prompt Framework</h3>
<p>Construct prompts using the four-dimensional structure for stable professional output:</p>
<ol>
  <li><strong>Subject</strong>: Clear product positioning and core selling points</li>
  <li><strong>Style</strong>: Visual language and tone requirements</li>
  <li><strong>Timeline</strong>: Scene-by-scene action descriptions</li>
  <li><strong>Constraints</strong>: Negative prompts to avoid defects</li>
</ol>

<h4>Example: Keyboard Commercial Prompt</h4>
<pre><code class="language-plaintext">[Subject]
Produce a 30-second 16:9 cinematic video for ALTO KEYS K98M mechanical keyboard. Highlight features: translucent purple housing, hot-swappable switches, PBT keycaps, wireless connectivity. Target audience: tech enthusiasts and office professionals.

[Style]
Japanese minimalist tech aesthetic, soft backlighting, close-up texture shots, dynamic keyboard typing animations, smooth transition effects.

[Timeline]
0-5s: Low-angle shot of keyboard on desk, fingers pressing keys to show feedback
5-12s: Exploded view of keyboard structure (switch, keycap, PCB board)
12-20s: Wireless connectivity demonstration, multi-device switching
20-30s: Hero shot with product logo and tagline "Elevate Your Typing Experience"

[Constraints]
Avoid over-saturated colors, maintain realistic lighting, no floating text overlays except final logo</code></pre>

<h3>Skill-Based Prompt Templates</h3>
<p>Pre-built skill templates simplify complex prompts into one-click generation. Access the public repository for ready-to-use templates:</p>
<pre><code class="language-bash"># Seedance 2.5 prompt template repository
git clone https://github.com/HuangBaiAI/seed-2.5-prompt</code></pre>
<p>Copy templates directly for scenarios including product commercials, short films, and animation production.</p>

<h2 id="workflow2">Core Workflow 2: Precise Video Editing</h2>

<h3>Smart Editing Mode</h3>
<ol>
  <li>Upload the original video to the platform</li>
  <li>Select "Smart Editing" mode in the interface</li>
  <li>Mark target areas with red boxes and input modification prompts</li>
  <li>Generate edited video with one click</li>
</ol>

<h4>Example: Special Effect Generation</h4>
<p>Input prompt:</p>
<pre><code class="language-plaintext">Add a "point-and-shoot" effect where clicking any position in the video triggers a corresponding animation effect</code></pre>
<p>The system automatically identifies key frames and generates seamless transitions.</p>

<h3>Local Editing Features</h3>
<ul>
  <li><strong>Background Replacement</strong>: Swap static backgrounds with dynamic scenes while preserving subject integrity</li>
  <li><strong>Object Removal</strong>: Eliminate unwanted elements (pedestrians, clutter) with AI inpainting</li>
  <li><strong>Style Transfer</strong>: Convert ordinary footage into cinematic quality (e.g., turn a desk toy video into a 3D animation battle scene)</li>
</ul>

<h2 id="workflow3">Core Workflow 3: Video Replication & Style Matching</h2>

<h3>Agent Mode for Style Replication</h3>
<ol>
  <li>Upload the reference video with desired effects</li>
  <li>Select "Agent Mode" in the generation interface</li>
  <li>Input reverse-engineering prompt to extract style elements</li>
  <li>Upload new subject material and generate matching content</li>
</ol>

<h4>Example: Phone Commercial Replication</h4>
<p>Input reverse prompt:</p>
<pre><code class="language-plaintext">Extract the mechanical assembly transition effects, color grading, and camera movement patterns from the reference video. Apply these styles to generate a new video featuring the latest smartphone model</code></pre>

<h3>Element Replacement Workflow</h3>
<ol>
  <li>Select "Smart Editing" mode</li>
  <li>Upload original video and replacement elements</li>
  <li>Input prompt for seamless integration:</li>
</ol>
<pre><code class="language-plaintext">Replace the human subject in the original video with the new character while maintaining all motion, lighting, and background consistency</code></pre>

<h2 id="scenarios">Advanced Application Scenarios</h2>

<h3>1. Commercial Product Videos</h3>
<p>Generate TVC-level content for electronics, cosmetics, and consumer goods. The keyboard commercial example demonstrates that even 30-second professional videos can be produced in minutes.</p>

<h3>2. Short Film & Animation</h3>
<p>Create narrative content with complex character interactions and scene transitions. The cooking short film example shows Seedance 2.5's improved motion capture and scene continuity capabilities.</p>

<h3>3. Cross-Border Video Localization</h3>
<p>Use multi-language voiceover feature to generate videos with synchronized lip movements in English, Japanese, French, and other languages, ideal for e-commerce product localization.</p>

<h3>4. UI/UX Animation</h3>
<p>Produce high-quality interface animations for software demos and product onboarding videos. The UI interaction example shows how to generate complex button animations and transition effects.</p>

<h2 id="cost">Cost Control Strategy</h2>
<ul>
  <li><strong>Pricing Model</strong>: 260 points/second for 720P resolution (approximately $0.37/second)</li>
  <li><strong>Cost Optimization</strong>:
    <ol>
      <li>Use version 2.0 for simple content (140 points/second)</li>
      <li>Batch generate short clips and splice manually</li>
      <li>Reuse skill templates to reduce prompt iteration time</li>
    </ol>
  </li>
  <li><strong>ROI Analysis</strong>: Compared to traditional TVC production costs ($10,000-$100,000), Seedance 2.5 delivers equivalent results at 1% of the cost</li>
</ul>

<h2 id="best-practices">Final Best Practices</h2>
<ol>
  <li><strong>Start with Templates</strong>: Use pre-built skill templates before creating custom prompts</li>
  <li><strong>Iterate Gradually</strong>: Generate 10-second clips first, then extend to full length</li>
  <li><strong>Reference System</strong>: Combine 3-5 reference materials for complex style fusion</li>
  <li><strong>Negative Prompts</strong>: Always include constraints to avoid common AI defects</li>
  <li><strong>Cost Tracking</strong>: Monitor point usage and optimize generation parameters</li>
</ol>

<h2 id="conclusion">Final Takeaway</h2>
<p>With Seedance 2.5, the barrier to professional video production has been fundamentally lowered. Even without programming or design experience, you can create commercial-grade content that once required large production teams. The future of video creation is no longer limited by technical skills — only by imagination.</p>

<h2>常见问题</h2>

<h3>How does Seedance 2.5 compare to other AI video models like Sora and Veo?</h3>
<p>Seedance 2.5's key differentiator is direct long-form generation — a single 30-second clip with an extended mode up to 3 minutes, eliminating the manual splicing that other models require. Its video quality now rivals global leaders: it significantly reduces the "AI rendering texture" visible in earlier versions, achieving near-photorealistic skin detail and natural motion capture. On cost, it is far more accessible for Chinese creators than Sora (which has limited availability and higher pricing). Compared to Veo 3.1 at ~$1.90 per 5 seconds, Seedance 2.5 at ~$0.37/second (roughly $1.85 per 5 seconds) is comparable, but with the advantage of native access in China, multi-language lip-sync voiceover, and an up-to-50-reference-material system that competitors don't match. For commercial product videos, Seedance 2.5 is currently the strongest domestic option.</p>

<h3>What is the four-dimensional prompt framework and why does it matter?</h3>
<p>The framework structures every commercial prompt into four sections: <strong>Subject</strong> (product positioning + selling points), <strong>Style</strong> (visual language and tone), <strong>Timeline</strong> (scene-by-scene action descriptions, usually in 5-second blocks), and <strong>Constraints</strong> (negative prompts to avoid defects like oversaturated colors or floating text). This matters because video generation models are extremely sensitive to prompt structure — a single paragraph prompt produces unpredictable results, while the four-dimensional structure gives the model explicit staging instructions (what to show, in what style, in what order, and what to avoid). The tutorial's keyboard commercial example produces a complete 30-second TVC from one structured prompt, something a free-form prompt cannot achieve.</p>

<h3>How can beginners control costs when using Seedance 2.5?</h3>
<p>Three practical strategies: (1) <strong>Use version 2.0 for simple content</strong> — at 140 points/second it costs roughly half of 2.5's 260 points/second, so reserve 2.5 for hero shots and complex scenes; (2) <strong>Batch and splice</strong> — generate multiple 5-10 second clips and join them manually instead of one long expensive generation; (3) <strong>Reuse skill templates</strong> — the public prompt repository (github.com/HuangBaiAI/seed-2.5-prompt) eliminates paid prompt-iteration time. For a typical 30-second 720P commercial, expect roughly 7,800 points (~$11) in direct generation cost — versus $10,000-$100,000 for a traditional TVC production, that's roughly 1% of the cost for comparable output.</p>

<h3>Can Seedance 2.5 really replace a professional video production team?</h3>
<p>For most commercial use cases, yes — with the right workflow. The tutorial demonstrates three core workflows that cover the full production cycle: <strong>Direct generation</strong> (30-second TVC from a structured prompt), <strong>Smart editing</strong> (background replacement, object removal, style transfer on existing footage), and <strong>Style replication</strong> (Agent Mode extracts the style of a reference video and applies it to new content). Where a human team is still needed: complex narrative scripts with consistent characters across long videos, fine audio design beyond lip-synced voiceover, and brand-specific creative direction. The practical approach is using Seedance 2.5 for the 80% of production work (visual generation, editing, localization) while humans focus on the creative 20% (concept, script, brand voice).</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Mastered AI video generation? Build on these related skills:</p>
  <ul>
    <li><a href="/articles/seedream-5-pro-ai-image-generation-guide">Seedream 5.0 Pro: A Comprehensive Practical Guide to China's Leading AI Image Generation Model</a> — pair video with ByteDance's flagship image model for full creative workflows</li>
    <li><a href="/articles/full-practical-guide-ai-comic-drama-production-zero-to-published">Full Practical Guide to AI Comic Drama Production: From Zero to Published Video</a> — apply AI video workflows to short-drama and comic content production</li>
    <li><a href="/articles/mastering-ai-image-generation-fix-prompt-issues-avoid-draw-failures">Mastering AI Image Generation: How to Fix Prompt Issues and Avoid Draw Failures</a> — sharpen prompt skills that transfer directly to video generation</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">🔧 AI工具</span>
  <span class="meta-badge">🕒 阅读约8分钟</span>
  <span class="meta-badge">📅 2026年8月7日</span>
  <span class="meta-badge">🎯 入门</span>
</div>

<h2 id="introduction">引言</h2>
<p>Seedance 2.5不仅是参数升级——它代表一种范式转变：AI现在可以直接一次性生成完全商业级的视频内容。本实战指南提炼真实测试洞察和实用工作流，通过掌握提示词编写、多场景应用和成本控制，让初学者快速成长为专业AI创作者。</p>

<h2 id="advantages">Seedance 2.5核心优势</h2>
<ul>
  <li><strong>直接生成长视频</strong>：支持单次生成最长30秒，扩展模式可达3分钟短片，无需手动拼接</li>
  <li><strong>超真实视觉质量</strong>：大幅降低2.0版本的"AI渲染质感"，实现接近照片级的皮肤细节和自然动作捕捉效果</li>
  <li><strong>多功能工作流</strong>：覆盖从素材生成、定向剪辑到风格复刻的全周期视频制作</li>
  <li><strong>高度灵活参考系统</strong>：支持多达50个参考素材，实现复杂风格融合和内容定制</li>
</ul>

<h2 id="workflow1">核心工作流一：直接生成商业视频</h2>

<h3>通用提示词框架</h3>
<p>使用四维结构构建提示词，确保稳定的专业输出：</p>
<ol>
  <li><strong>主体</strong>：明确产品定位和核心卖点</li>
  <li><strong>风格</strong>：视觉语言和基调要求</li>
  <li><strong>时间线</strong>：逐场景的动作描述</li>
  <li><strong>约束</strong>：避免缺陷的负面提示词</li>
</ol>

<h4>示例：键盘商业广告提示词</h4>
<pre><code class="language-plaintext">[主体]
为ALTO KEYS K98M机械键盘制作30秒16:9电影级视频。突出卖点：半透明紫色外壳、热插拔轴体、PBT键帽、无线连接。目标受众：科技爱好者和办公专业人士。

[风格]
日式极简科技美学，柔和背光，特写质感镜头，动态打字动画，平滑转场效果。

[时间线]
0-5秒：低角度拍摄桌面键盘，手指按压展示反馈
5-12秒：键盘结构分解图（轴体、键帽、PCB板）
12-20秒：无线连接演示，多设备切换
20-30秒：主镜头带产品logo和标语"Elevate Your Typing Experience"

[约束]
避免过度饱和色彩，保持真实光照，除最终logo外不出现漂浮文字叠加</code></pre>

<h3>技能型提示词模板</h3>
<p>预置技能模板将复杂提示词简化为一键生成。访问公共仓库获取即用模板：</p>
<pre><code class="language-bash"># Seedance 2.5提示词模板仓库
git clone https://github.com/HuangBaiAI/seed-2.5-prompt</code></pre>
<p>可直接复制产品广告、短片、动画制作等场景的模板。</p>

<h2 id="workflow2">核心工作流二：精准视频剪辑</h2>

<h3>智能剪辑模式</h3>
<ol>
  <li>将原始视频上传到平台</li>
  <li>在界面中选择"智能剪辑"模式</li>
  <li>用红框标记目标区域并输入修改提示词</li>
  <li>一键生成剪辑后的视频</li>
</ol>

<h4>示例：特效生成</h4>
<p>输入提示词：</p>
<pre><code class="language-plaintext">添加"点击即射"效果：点击视频任意位置触发对应的动画效果</code></pre>
<p>系统自动识别关键帧并生成无缝转场。</p>

<h3>局部剪辑功能</h3>
<ul>
  <li><strong>背景替换</strong>：在保持主体完整的情况下，将静态背景替换为动态场景</li>
  <li><strong>物体移除</strong>：通过AI修补消除不需要的元素（行人、杂物）</li>
  <li><strong>风格迁移</strong>：将普通素材转换为电影级质感（例如将桌面玩具视频变成3D动画战斗场景）</li>
</ul>

<h2 id="workflow3">核心工作流三：视频复刻与风格匹配</h2>

<h3>Agent模式风格复刻</h3>
<ol>
  <li>上传具有所需效果的参考视频</li>
  <li>在生成界面中选择"Agent模式"</li>
  <li>输入逆向工程提示词提取风格元素</li>
  <li>上传新主体素材并生成匹配内容</li>
</ol>

<h4>示例：手机广告复刻</h4>
<p>输入逆向提示词：</p>
<pre><code class="language-plaintext">提取参考视频中的机械组装转场效果、色彩分级和镜头运动模式。将这些风格应用到新视频，展示最新款智能手机</code></pre>

<h3>元素替换工作流</h3>
<ol>
  <li>选择"智能剪辑"模式</li>
  <li>上传原始视频和替换元素</li>
  <li>输入无缝集成提示词：</li>
</ol>
<pre><code class="language-plaintext">将原始视频中的人物主体替换为新角色，同时保持所有运动、光照和背景的一致性</code></pre>

<h2 id="scenarios">高级应用场景</h2>

<h3>1. 商业产品视频</h3>
<p>为电子产品、化妆品和消费品生成TVC级内容。键盘商业广告示例表明，即使30秒的专业视频也可以在几分钟内制作完成。</p>

<h3>2. 短片与动画</h3>
<p>创作具有复杂角色互动和场景转换的叙事内容。烹饪短片示例展示了Seedance 2.5改进的动作捕捉和场景连续性能力。</p>

<h3>3. 跨境视频本地化</h3>
<p>利用多语言配音功能生成英语、日语、法语等语言的同步唇形视频，非常适合电商产品本地化。</p>

<h3>4. UI/UX动画</h3>
<p>为软件演示和产品引导视频制作高质量界面动画。UI交互示例展示了如何生成复杂的按钮动画和转场效果。</p>

<h2 id="cost">成本控制策略</h2>
<ul>
  <li><strong>定价模型</strong>：720P分辨率260积分/秒（约$0.37/秒）</li>
  <li><strong>成本优化</strong>：
    <ol>
      <li>简单内容使用2.0版本（140积分/秒）</li>
      <li>批量生成短视频段并手动拼接</li>
      <li>复用技能模板减少提示词迭代时间</li>
    </ol>
  </li>
  <li><strong>ROI分析</strong>：与传统TVC制作成本（$10,000-$100,000）相比，Seedance 2.5以1%的成本实现同等效果</li>
</ul>

<h2 id="best-practices">最佳实践</h2>
<ol>
  <li><strong>从模板开始</strong>：创建自定义提示词前先使用预置技能模板</li>
  <li><strong>逐步迭代</strong>：先生成10秒片段，再扩展到完整长度</li>
  <li><strong>参考系统</strong>：复杂风格融合时组合3-5个参考素材</li>
  <li><strong>负面提示词</strong>：始终包含约束条件以避免常见AI缺陷</li>
  <li><strong>成本跟踪</strong>：监控积分使用并优化生成参数</li>
</ol>

<h2 id="conclusion">总结</h2>
<p>借助Seedance 2.5，专业视频制作的门槛已从根本上降低。即使没有编程或设计经验，你也可以创建曾经需要大型制作团队才能完成的商业级内容。视频创作的未来不再受技术技能限制——只受想象力的限制。</p>

<h2>常见问题</h2>

<h3>Seedance 2.5与Sora、Veo等其他AI视频模型相比如何？</h3>
<p>Seedance 2.5的关键差异化优势是直接生成长视频——单次30秒片段，扩展模式最长3分钟，无需其他模型所需的手动拼接。视频质量已与全球领先者媲美：大幅减少了早期版本中明显的"AI渲染质感"，实现接近照片级的皮肤细节和自然动作捕捉。在成本上，相比Sora（可用性受限、定价更高），它对中国创作者更友好。与Veo 3.1约$1.90/5秒相比，Seedance 2.5约$0.37/秒（约$1.85/5秒）价格相当，但优势在于国内原生访问、多语言唇形同步配音，以及竞争对手无法匹敌的多达50个参考素材系统。对于商业产品视频，Seedance 2.5是目前最强的国产选择。</p>

<h3>什么是四维提示词框架？为什么它很重要？</h3>
<p>该框架将每个商业提示词组织为四个部分：<strong>主体</strong>（产品定位+卖点）、<strong>风格</strong>（视觉语言和基调）、<strong>时间线</strong>（逐场景动作描述，通常以5秒为块）、<strong>约束</strong>（避免过饱和色彩或漂浮文字等缺陷的负面提示词）。这很重要，因为视频生成模型对提示词结构极其敏感——单一段落提示词会产生不可预测的结果，而四维结构为模型提供了明确的分镜指令（展示什么、什么风格、什么顺序、避免什么）。教程中的键盘商业广告示例通过一个结构化提示词即可生成完整的30秒TVC，这是自由格式提示词无法做到的。</p>

<h3>初学者如何控制使用Seedance 2.5的成本？</h3>
<p>三个实用策略：(1)<strong>简单内容使用2.0版本</strong>——140积分/秒的成本约为2.5版本260积分/秒的一半，因此将2.5保留给主镜头和复杂场景；(2)<strong>批量生成再拼接</strong>——生成多个5-10秒片段手动拼接，避免一次长时间的高成本生成；(3)<strong>复用技能模板</strong>——公共提示词仓库（github.com/HuangBaiAI/seed-2.5-prompt）消除了付费的提示词迭代时间。一个典型的30秒720P商业视频，直接生成成本约为7,800积分（约$11）——相比传统TVC制作的$10,000-$100,000，这只是约1%的成本。</p>

<h3>Seedance 2.5真的能取代专业视频制作团队吗？</h3>
<p>对于大多数商业用例，可以——但需要正确的工作流。教程演示了三个覆盖完整制作周期的核心工作流：<strong>直接生成</strong>（从结构化提示词生成30秒TVC）、<strong>智能剪辑</strong>（对现有素材进行背景替换、物体移除、风格迁移）、<strong>风格复刻</strong>（Agent模式提取参考视频的风格并应用到新内容）。仍需要人类团队的部分：跨长视频保持角色一致性的复杂叙事脚本、唇形同步配音之外的精细音频设计，以及品牌专属的创意方向。实用做法是用Seedance 2.5完成80%的制作工作（视觉生成、剪辑、本地化），人类专注于创意20%（概念、脚本、品牌声音）。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>掌握了AI视频生成？基于这些相关技能继续提升：</p>
  <ul>
    <li><a href="/articles/seedream-5-pro-ai-image-generation-guide">Seedream 5.0 Pro实战评测：国产顶流AI图像生成模型全指南</a> — 将视频与字节跳动旗舰图像模型配对，打造完整创意工作流</li>
    <li><a href="/articles/full-practical-guide-ai-comic-drama-production-zero-to-published">AI漫剧制作全流程实战：从零到发布成片</a> — 将AI视频工作流应用于短剧和漫剧内容制作</li>
    <li><a href="/articles/mastering-ai-image-generation-fix-prompt-issues-avoid-draw-failures">掌握AI图像生成：如何修复提示词问题避免"画崩"</a> — 打磨可直接迁移到视频生成的提示词技能</li>
  </ul>
</div>`,
  },

'''
last = c.rfind('};')
with open('src/lib/article-content.ts', 'w', encoding='utf-8') as f: f.write(c[:last] + n + '};')
print('Part 2 done')

with open('src/lib/tools.ts', 'r', encoding='utf-8') as f: t = f.read()
tool = r'''
  {
    id: "seedance-2-5",
    name: "Seedance 2.5",
    nameZh: "Seedance 2.5",
    description: "ByteDance's flagship AI video generation model — direct 30-second commercial-grade clips, ultra-realistic visuals, smart editing, style replication, and up to 50 reference materials.",
    descriptionZh: "字节跳动旗舰AI视频生成模型——30秒直出商业级视频、超真实画质、智能剪辑、风格复刻，支持多达50个参考素材。",
    category: "video-generation",
    tags: ["video-generation", "bytedance", "china", "text-to-video", "commercial", "ai-video"],
    difficulty: "beginner",
    url: "https://www.volcengine.com/product/seedance",
    rating: r(4.6),
    pricing: "Pay per use (260 points/sec at 720P, ~$0.37/sec)",
    useCase: "Commercial-grade AI video generation — product commercials, short films, style replication, smart editing, and multi-language lip-synced localization",
    icon: "\u{1F3AC}",
    company: "ByteDance",
    companyZh: "字节跳动",
    founded: 2012,
    headquarters: "Beijing, China",
    descriptionLong: "Seedance 2.5 is ByteDance's latest flagship AI video generation model on the Volcano Engine platform, representing a paradigm shift where AI can directly generate fully commercial-ready video content in one go. Its standout feature is direct long-form generation — single-shot clips up to 30 seconds, with an extended mode reaching 3 minutes, eliminating the manual splicing required by competitors. Visual quality is dramatically improved over version 2.0, reducing the 'AI rendering texture' to achieve near-photorealistic skin detail and natural motion capture. It accepts up to 50 reference materials for complex style fusion. The platform covers the full video production cycle: direct generation via a four-dimensional prompt framework (subject, style, timeline, constraints), smart editing (background replacement, object removal, style transfer on existing footage), and Agent Mode for style replication from reference videos. Multi-language voiceover generates synchronized lip movements in English, Japanese, French and more for e-commerce localization. Priced at 260 points/second for 720P (approximately $0.37/second), it delivers TVC-level results at roughly 1% of traditional production costs. It competes directly with Google's Veo 3.1 and OpenAI's Sora, and is the strongest domestic option for Chinese commercial video creators.",
    descriptionLongZh: "Seedance 2.5是字节跳动在火山引擎平台上的最新旗舰AI视频生成模型，代表了AI直接一次性生成完全商业级视频内容的范式转变。其突出特点是直接生成长视频——单次片段最长30秒，扩展模式可达3分钟，消除了竞争对手所需的手动拼接。视觉质量相比2.0版本大幅提升，减少"AI渲染质感"，实现接近照片级的皮肤细节和自然动作捕捉。支持多达50个参考素材进行复杂风格融合。平台覆盖完整视频制作周期：通过四维提示词框架（主体、风格、时间线、约束）直接生成、智能剪辑（背景替换、物体移除、风格迁移）、以及从参考视频提取风格的Agent模式复刻。多语言配音生成英语、日语、法语等的同步唇形动作，适合电商本地化。定价720P分辨率260积分/秒（约$0.37/秒），以传统制作成本约1%的价格交付TVC级效果。它直接与Google的Veo 3.1和OpenAI的Sora竞争，是中国商业视频创作者最强的国产选择。",
    advantages: ["Direct 30-second generation with 3-minute extended mode", "Near-photorealistic visual quality", "Up to 50 reference materials for style fusion", "Smart editing: background replacement, object removal, style transfer", "Agent Mode for video style replication", "Multi-language lip-synced voiceover for localization"],
    advantagesZh: ["30秒直出+3分钟扩展模式", "接近照片级的视觉质量", "多达50个参考素材风格融合", "智能剪辑：背景替换、物体移除、风格迁移", "Agent模式视频风格复刻", "多语言唇形同步配音本地化"],
    useCases: ["Commercial product videos (TVC-level)", "Short films and animation", "Cross-border e-commerce video localization", "UI/UX interface animations", "Social media content at scale"],
    useCasesZh: ["商业产品视频（TVC级）", "短片与动画", "跨境电商视频本地化", "UI/UX界面动画", "规模化社交媒体内容"],
    targetAudience: "Chinese video creators, marketers, e-commerce sellers, and businesses who need commercial-grade AI video generation without a professional production team",
    targetAudienceZh: "中国视频创作者、营销人员、电商卖家和需要商业级AI视频生成但无专业制作团队的企业",
    pricingTiers: [
      {
        tier: "Pay-per-use",
        tierZh: "按量付费",
        price: "260 points/sec at 720P (~$0.37/sec)",
        features: ["30-second direct generation", "3-minute extended mode", "Smart editing tools", "Up to 50 reference materials", "Multi-language voiceover"],
        featuresZh: ["30秒直出生成", "3分钟扩展模式", "智能剪辑工具", "多达50个参考素材", "多语言配音"],
      },
    ],
    pros: ["Best-in-class long-form generation", "Near-photorealistic quality", "Native access in China", "Strong cost efficiency vs traditional TVC", "Rich editing and replication workflow"],
    prosZh: ["顶级长视频生成", "接近照片级画质", "国内原生访问", "相比传统TVC极强性价比", "丰富的剪辑和复刻工作流"],
    cons: ["No free tier", "720P cap at standard pricing (4K costs more)", "Chinese interface focus", "Prompt quality heavily affects output"],
    consZh: ["无免费版", "标准定价720P上限（4K更贵）", "界面以中文为主", "提示词质量严重影响输出"],
    extensions: [],
    skills: ["Text-to-video generation", "Smart video editing", "Style replication", "Background replacement", "Object removal", "Multi-language localization"],
    scene: "video",
  },

'''
last_t = t.rfind('] as Tool[];')
with open('src/lib/tools.ts', 'w', encoding='utf-8') as f: f.write(t[:last_t] + tool + '] as Tool[];')
print('Part 3 done\n=== Done ===')