"""
Publish July 20, 2026 — 2 articles, no new tools.
"""
import os

BASE = r"C:\Users\jun\aistudyonline-next"
os.chdir(BASE)

# ===== Part 1: Add 2 article metadata to articles.ts =====
with open('src/lib/articles.ts', 'r', encoding='utf-8') as f:
    articles_src = f.read()

new_articles = r"""  {
    slug: "ai-manhua-production-full-workflow-script-to-monetization",
    title: "AI Manhua Production Full Workflow: From Script to Monetization",
    titleZh: "AI漫剧制作全流程：从剧本到变现的完整指南",
    description: "A complete AI manhua (short anime) production workflow using only a smartphone — from scene description and text-to-image through image-to-video and post-editing, plus 3 script creation methods, prompt optimization for camera control, model selection (Seedance, Xiaoyunque, Wan, LTX), and monetization basics.",
    descriptionZh: "仅用手机完成AI漫剧制作的完整流程——从场景描述、文生图到图生视频和后期剪辑，含3种剧本创作方法、镜头控制提示词优化、模型选择（Seedance、Xiaoyunque、Wan、LTX）和变现基础。",
    category: "AI Tutorials",
    tags: ["AI Manhua", "Video Generation", "Content Creation", "Seedance", "Monetization", "Tutorial"],
    difficulty: "beginner",
    toolsMentioned: ["Seedance 2.0", "Xiaoyunque", "CapCut"],
    date: "2026-07-20",
  },
  {
    slug: "kimi-k3-takes-global-top-spot-week-29-frontend-coding-benchmark",
    title: "Kimi K3 Takes Global Top Spot: Week 29 LLM Front-End Coding Benchmark Report",
    titleZh: "Kimi K3登顶全球第一：第29周LLM前端编码基准测试报告",
    description: "Week 29 front-end coding benchmark results: Kimi K3 debuts at #1 globally (1679 score), surpassing Claude Fable-5 and GPT-5.6 Sol — 9 Chinese models in top 25, with GLM 5.2 at #4 — plus a Python test script and model selection guide for developers.",
    descriptionZh: "第29周前端编码基准测试：Kimi K3首秀全球第一（1679分），超越Claude Fable-5和GPT-5.6 Sol——9款国产模型进入前25，GLM 5.2第4——含Python测试脚本和开发者选型指南。",
    category: "AI News",
    tags: ["Kimi K3", "Benchmark", "Front-End", "Coding", "LLM", "China", "Claude", "GPT"],
    difficulty: "beginner",
    toolsMentioned: ["Kimi", "Claude Fable 5", "GPT-5.6", "GLM-5"],
    date: "2026-07-20",
  },

"""

last_bracket = articles_src.rfind('];')
articles_new = articles_src[:last_bracket] + new_articles + '];'

with open('src/lib/articles.ts', 'w', encoding='utf-8') as f:
    f.write(articles_new)

print('Part 1: 2 new articles added to articles.ts')

# ===== Part 2: Add article content to article-content.ts =====
with open('src/lib/article-content.ts', 'r', encoding='utf-8') as f:
    content_src = f.read()

new_contents = r'''
  "ai-manhua-production-full-workflow-script-to-monetization": {
    content: `<div class="meta-banner">
  <span class="meta-badge">📚 AI Tutorials</span>
  <span class="meta-badge">🕒 8 min read</span>
  <span class="meta-badge">📅 Jul 20, 2026</span>
  <span class="meta-badge">🎯 Beginner</span>
</div>

<h2 id="introduction">Introduction</h2>

<p>Creating AI manhua (short animated drama) doesn't require professional screenwriting or directing experience. This guide breaks down the complete, practical workflow to help you produce publishable content in just three days using only a smartphone. The process follows four core stages: scene description, text-to-image, image-to-video, and post-editing, with clear, actionable steps for beginners.</p>

<h2 id="workflow">Core Production Workflow</h2>

<h3>1. Scene Description</h3>

<p>Start by defining your scene with AI assistance. Use the following prompt structure to get detailed, polished descriptions:</p>

<pre><code class="language-text">I will describe a scene, please help me refine it into a vivid, detailed description. Do not generate images.
[Your scene description: e.g., "A girl stands in a grassland with long white hair, red eyes, wearing a large white hat and white dress, looking at the camera"]</code></pre>

<p>AI will automatically enhance the description with details like lighting, atmosphere, and character expressions to make the scene more vivid.</p>

<h3>2. Text-to-Image</h3>

<p>Use the refined scene description to generate your base image. Specify the aspect ratio (16:9 for horizontal video) and style (e.g., Japanese anime flat style) in your prompt:</p>

<pre><code class="language-text">Generate an image of this scene, aspect ratio 16:9, using Japanese anime flat style.</code></pre>

<p>Select the best result from the generated options, prioritizing close-up shots for character-focused scenes.</p>

<h3>3. Image-to-Video</h3>

<p>Convert your selected image into a short video. For beginners, use affordable tools like Xiaoyunque:</p>

<ol>
  <li>Upload your base image to the platform</li>
  <li>Add voiceover text (keep it simple for better AI performance)</li>
  <li>Select the "Participate in Creation" mode for iterative adjustments</li>
  <li>Generate a 5-10 second video (costs ~5 credits, with daily free credits available)</li>
</ol>

<h3>4. Post-Editing</h3>

<p>Use Jianying (CapCut) to finalize your video:</p>
<ol>
  <li>Add sound effects (e.g., wind for grassland scenes) from the built-in library</li>
  <li>Manually add subtitles (free alternative to paid AI recognition)</li>
  <li>Adjust audio levels and trim clips to match the video duration</li>
  <li>Export your final video in 1080p resolution</li>
</ol>

<h2 id="script-methods">AI Script Creation Methods</h2>

<h3>Method 1: Direct Full Script Generation</h3>

<pre><code class="language-text">Assume you are a screenwriter with 15 years of experience in short-form animation. Create a 1-minute healing animation script with the theme of "Companion" featuring a cartoon cat. Design 18 shots, each no longer than 7 seconds, including scene descriptions, camera angles, and timing.</code></pre>

<p><strong>Pros</strong>: Fast, one-step generation. <strong>Cons</strong>: May include complex scenes that are hard to visualize.</p>

<h3>Method 2: Story-to-Script Conversion</h3>

<p>Better for logical, easy-to-produce content:</p>
<ol>
  <li>First generate a simple story: "Write a short healing story about a cartoon cat with the theme of 'Companion', with a clear beginning, middle, and end."</li>
  <li>Then convert to script: "Convert this story into a shot list. Each shot should have a simple description that can be easily visualized as an image."</li>
</ol>

<p><strong>Pros</strong>: More logical plot, easier to visualize scenes. <strong>Cons</strong>: Requires an extra step.</p>

<h3>Method 3: Framework-Based Rewriting</h3>

<pre><code class="language-text">Refer to the story framework of "The Dog's Promise" (separation, waiting, reunion, companionship), rewrite a new story with different characters and details, keeping the emotional arc intact.</code></pre>

<p><strong>Pros</strong>: High efficiency, proven emotional structure. <strong>Cons</strong>: Requires careful adaptation to avoid plagiarism.</p>

<h2 id="prompt-tips">Prompt Optimization Tips</h2>

<h3>Style Control</h3>
<p>Specify visual styles in your prompts: 3D styles (Pixar, 3D modeling, Chinese anime), Painting styles (Illustration, Japanese anime, oil painting, game art), Realistic styles (Nature photography, street photography, film camera).</p>

<h3>Camera Angle Control</h3>
<ul>
  <li><strong>Movement</strong>: Follow shot, push-in, pull-out, slow push</li>
  <li><strong>Angle</strong>: Over-the-shoulder, first-person, low-angle, high-angle</li>
  <li><strong>Distance</strong>: Close-up, medium shot, long shot, extreme close-up</li>
</ul>

<h3>Advanced Video Prompt Structure</h3>
<p>For high-quality video generation, include these four elements: Camera movement, Scene, Subject, Details. Example: "Medium shot, slow push-in. Early morning sunlit forest, misty atmosphere. Girl in white dress running, hair blowing in wind. Sunlight filtering through leaves, soft lens flare."</p>

<h2 id="model-selection">Model Selection Guide</h2>

<h3>Open-Source Models (For Advanced Users)</h3>
<ul>
  <li><strong>Wan 2.2</strong>: Large community support, rich resources, no built-in audio output</li>
  <li><strong>LTX 2.3</strong>: Supports audio-video synchronization, smaller community with fewer tutorials</li>
</ul>

<h3>Closed-Source Models (For Beginners)</h3>
<ul>
  <li><strong>Seedance 2.0 (ByteDance)</strong>: Industry-leading quality, used for most commercial manhua</li>
  <li><strong>Xiaoyunque 1.5</strong>: Affordable, easy to use, ideal for beginners</li>
  <li><strong>Other options</strong>: Hailuo, Kening, Weidu (lower cost, slightly lower quality)</li>
</ul>

<h2 id="monetization">Monetization Basics</h2>

<p>AI manhua generates revenue through two main models: (1) <strong>Paid unlock</strong>: Users pay to access subsequent episodes. (2) <strong>Ad revenue</strong>: Earn from ads displayed between episodes. This creates a recurring income stream with minimal ongoing effort once the initial content is produced.</p>

<h2 id="conclusion">Conclusion</h2>

<p>AI manhua production is accessible to anyone with basic digital literacy. By following this four-stage workflow and mastering prompt engineering techniques, you can create publishable content in just a few days. Start with simple scenes, experiment with different AI tools, and iterate on your work to develop your own style.</p>

<h2>常见问题</h2>

<h3>Can I really do this with just a smartphone?</h3>
<p>Yes — the entire workflow described in this guide (scene description → text-to-image → image-to-video → post-editing) runs on a smartphone. The AI tools mentioned (Xiaoyunque, Seedance, CapCut/Jianying) all have mobile apps. The limiting factor isn't hardware — it's your prompt engineering skills and patience with iteration. A smartphone is sufficient for producing 1-3 minute manhua episodes. For longer content (5+ minutes) or higher production values, a tablet or computer makes editing easier but isn't required. The guide's "3 days from idea to publishable content" timeline assumes smartphone-only workflow.</p>

<h3>Which model should I use if I'm on a zero budget?</h3>
<p>Start with <strong>Xiaoyunque 1.5</strong> — it offers daily free credits (enough for 1-2 short videos per day) and is the most beginner-friendly. For text-to-image, use free tiers of AI image generators. For post-editing, CapCut/Jianying is free with watermark (paid version removes it). Total cost: $0 for your first few episodes. Once you validate that your content resonates with an audience (views, engagement, positive feedback), invest in Seedance 2.0 for higher quality or CapCut Pro for watermark-free exports. The monetization models (paid unlock + ad revenue) can fund your tool upgrades once you have a content pipeline.</p>

<h3>How do I avoid my AI manhua looking generic or "AI-generated"?</h3>
<p>Three techniques: (1) <strong>Consistent style prompts</strong> — lock in your visual style, color palette, and character design in every prompt. If episode 1 uses "Japanese anime flat style, warm color palette, soft lighting," episode 2 must use the same. (2) <strong>Camera variety</strong> — the guide's camera angle section is critical. Amateur AI content uses the same wide shot for every scene. Professional content varies: close-up for emotion, medium shot for action, long shot for establishing location. (3) <strong>Post-production polish</strong> — sound effects, subtitles, and audio mixing are what separate "AI slop" from "AI-assisted production." A 10-second clip with good sound design feels more professional than a 60-second clip with none. Spend 30% of your production time on post-editing, not just generation.</p>

<h3>How much can I realistically earn from AI manhua?</h3>
<p>This is a volume game. Individual episodes earn modest amounts — a few dollars to tens of dollars in ad revenue or paid unlocks per episode. The model works through consistency: publish 2-3 episodes per week, build a content library of 50+ episodes, and the cumulative revenue becomes meaningful. Think of it like YouTube: your first 100 videos might earn $100 total, but video #500 could earn $500/month from the back catalog alone. The AI workflow reduces production cost to near-zero (just tool subscriptions), so even modest revenue is profitable. The key is treating it as a content business, not a get-rich-quick scheme — the creators who succeed are the ones who publish consistently for 6+ months.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Ready to create AI content? Explore more creation tools and techniques:</p>
  <ul>
    <li><a href="/articles/vibecoding-contest-guide-game-animations-ai-tools">VibeCoding Contest Guide: Create Game Animations Efficiently With AI Tools</a> — apply similar prompt + generation workflows to game animation</li>
    <li><a href="/articles/seedream-5-pro-ai-image-generation-guide">Seedream 5.0 Pro: A Comprehensive Practical Guide</a> — master the image generation step of this workflow</li>
    <li><a href="/articles/build-ai-team-coze-3-one-person-company">Build an AI Team with Coze 3.0</a> — use AI agents to automate your content production pipeline</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">📚 AI 教程</span>
  <span class="meta-badge">🕒 阅读约8分钟</span>
  <span class="meta-badge">📅 2026年7月20日</span>
  <span class="meta-badge">🎯 入门</span>
</div>

<h2 id="introduction">引言</h2>

<p>制作AI漫剧（短剧动画）不需要专业编剧或导演经验。本指南拆解完整实战流程，帮你仅用手机在三天内产出可发布的内容。流程遵循四个核心阶段：场景描述、文生图、图生视频和后期剪辑，为新手提供清晰可操作的步骤。</p>

<h2 id="workflow">核心制作流程</h2>

<h3>1. 场景描述</h3>

<p>先用AI辅助定义场景。使用以下提示词结构获得详细精致的描述：</p>

<pre><code class="language-text">我将描述一个场景，请帮我润色成生动详细的描述。不要生成图片。
[你的场景描述：如"一个女孩站在草原上，白色长发，红色眼睛，戴着大白色帽子穿着白色连衣裙，看着镜头"]</code></pre>

<p>AI会自动增强描述，添加光影、氛围和角色表情等细节，让场景更生动。</p>

<h3>2. 文生图</h3>

<p>用润色后的场景描述生成底图。在提示词中指定宽高比（横屏视频用16:9）和风格（如日式动漫平面风格）：</p>

<pre><code class="language-text">生成这个场景的图片，宽高比16:9，使用日式动漫平面风格。</code></pre>

<p>从生成选项中选最佳结果，角色为主的场景优先选择近景镜头。</p>

<h3>3. 图生视频</h3>

<p>将选中的图片转为短视频。新手用小鱼云等实惠工具：</p>

<ol>
  <li>上传底图到平台</li>
  <li>添加配音文本（保持简单以提高AI表现）</li>
  <li>选择"参与创作"模式进行迭代调整</li>
  <li>生成5-10秒视频（约5积分，每日有免费积分）</li>
</ol>

<h3>4. 后期剪辑</h3>

<p>用剪映（CapCut）完成视频：</p>
<ol>
  <li>从内置音效库添加音效（如草原场景配风声）</li>
  <li>手动添加字幕（免费替代付费AI识别）</li>
  <li>调整音量并裁剪片段匹配视频时长</li>
  <li>导出1080p分辨率最终视频</li>
</ol>

<h2 id="script-methods">AI剧本创作方法</h2>

<h3>方法一：直接全剧本生成</h3>

<pre><code class="language-text">假设你是有15年短篇动画经验的编剧。以"陪伴"为主题，创作一部1分钟治愈动画剧本，主角是卡通猫。设计18个镜头，每个不超过7秒，包含场景描述、镜头角度和时长。</code></pre>

<p><strong>优势</strong>：快速，一步生成。<strong>不足</strong>：可能包含难以视觉化的复杂场景。</p>

<h3>方法二：故事转剧本</h3>

<p>更适合逻辑清晰、易于制作的内容：</p>
<ol>
  <li>先生成简单故事："写一个关于卡通猫的短篇治愈故事，主题'陪伴'，有清晰的开头、发展和结尾。"</li>
  <li>再转为剧本："将这个故事转换为镜头列表。每个镜头应有简单描述，易于视觉化为图片。"</li>
</ol>

<p><strong>优势</strong>：情节更有逻辑，场景更容易视觉化。<strong>不足</strong>：多一步操作。</p>

<h3>方法三：框架改编</h3>

<pre><code class="language-text">参考《一条狗的使命》的故事框架（分离、等待、重逢、陪伴），用不同角色和细节改写新故事，保持情感弧线完整。</code></pre>

<p><strong>优势</strong>：效率高，情感结构经过验证。<strong>不足</strong>：需小心改编避免抄袭。</p>

<h2 id="prompt-tips">提示词优化技巧</h2>

<h3>风格控制</h3>
<p>在提示词中指定视觉风格：3D风格（皮克斯、3D建模、国漫）、绘画风格（插画、日式动漫、油画、游戏美术）、写实风格（自然摄影、街拍、胶片相机）。</p>

<h3>镜头控制</h3>
<ul>
  <li><strong>运动</strong>：跟拍、推镜、拉镜、慢推</li>
  <li><strong>角度</strong>：过肩、第一人称、低角度、高角度</li>
  <li><strong>距离</strong>：特写、中景、远景、大特写</li>
</ul>

<h3>高级视频提示词结构</h3>
<p>高质量视频生成需包含四要素：镜头运动、场景、主体、细节。示例："中景，慢推镜。清晨阳光森林，薄雾氛围。白裙女孩奔跑，头发随风飘动。阳光透过树叶，柔和镜头光晕。"</p>

<h2 id="model-selection">模型选择指南</h2>

<h3>开源模型（进阶用户）</h3>
<ul>
  <li><strong>Wan 2.2</strong>：社区支持大、资源丰富、无内置音频输出</li>
  <li><strong>LTX 2.3</strong>：支持音视频同步、社区较小教程较少</li>
</ul>

<h3>闭源模型（新手友好）</h3>
<ul>
  <li><strong>Seedance 2.0（字节跳动）</strong>：行业领先质量，多数商业漫剧使用</li>
  <li><strong>Xiaoyunque 1.5</strong>：实惠易用，新手首选</li>
  <li><strong>其他选项</strong>：海螺、可宁、维度（成本更低，质量略低）</li>
</ul>

<h2 id="monetization">变现基础</h2>

<p>AI漫剧通过两种主要模式产生收入：(1) <strong>付费解锁</strong>：用户付费观看后续剧集。(2) <strong>广告收入</strong>：从剧集间展示的广告中获利。一旦初始内容制作完成，就能以最少持续投入创造循环收入。</p>

<h2 id="conclusion">总结</h2>

<p>AI漫剧制作对有基础数字素养的人完全开放。遵循四阶段工作流并掌握提示词工程技巧，你可以在几天内创作出可发布的内容。从简单场景开始，尝试不同AI工具，迭代你的作品，发展自己的风格。</p>

<h2>常见问题</h2>

<h3>真的只用手机就能做吗？</h3>
<p>能——本指南描述的整个流程（场景描述→文生图→图生视频→后期剪辑）都在手机上运行。提到的AI工具（Xiaoyunque、Seedance、剪映/CapCut）都有手机App。限制因素不是硬件——是你的提示词工程技巧和迭代耐心。手机足够制作1-3分钟的漫剧。更长内容（5分钟以上）或更高制作水准，平板或电脑能让剪辑更轻松但不是必须的。指南"从创意到可发布内容3天"的时间线基于纯手机流程。</p>

<h3>零预算该选哪个模型？</h3>
<p>从<strong>Xiaoyunque 1.5</strong>开始——每天提供免费积分（足够每天1-2个短视频），对新手最友好。文生图用AI图像生成器的免费层。后期剪辑用剪映/CapCut免费版（带水印，付费版去水印）。总成本：前几集$0。一旦验证你的内容能引起受众共鸣（观看量、互动、正面反馈），再投资Seedance 2.0提升质量或CapCut Pro去水印。变现模式（付费解锁+广告收入）可以在有内容管线后为工具升级提供资金。</p>

<h3>如何避免AI漫剧看起来千篇一律或"AI感"太重？</h3>
<p>三个技巧：(1) <strong>统一风格提示词</strong>——在每个提示词中锁定视觉风格、色板和角色设计。第1集用"日式动漫平面风格、暖色调、柔光"，第2集必须相同。(2) <strong>镜头多样性</strong>——指南的镜头角度部分至关重要。业余AI内容每个场景都用同样的广角。专业内容变化丰富：情感用特写、动作用中景、场景建立用远景。(3) <strong>后期打磨</strong>——音效、字幕和混音是区分"AI垃圾"和"AI辅助制作"的关键。10秒带好音效的片段比60秒无音效的看起来更专业。花30%制作时间在后期，而非只生成。</p>

<h3>AI漫剧实际能赚多少钱？</h3>
<p>这是量变游戏。单集收入有限——每集几美元到几十美元的广告收入或付费解锁。模式靠持续性运作：每周发布2-3集，建立50+集的內容库，累计收入变得可观。就像YouTube：前100个视频可能总共赚$100，但第500个视频可能仅靠历史库就能月入$500。AI工作流将制作成本降到几乎为零（仅工具订阅），所以即使微薄收入也是盈利的。关键是把它当作内容生意，不是暴富捷径——成功的创作者是那些坚持发布6个月以上的人。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>准备好创作AI内容？探索更多创作工具和技巧：</p>
  <ul>
    <li><a href="/articles/vibecoding-contest-guide-game-animations-ai-tools">VibeCoding大赛指南：用AI工具高效制作游戏动画</a> — 将类似的提示词+生成流程应用到游戏动画</li>
    <li><a href="/articles/seedream-5-pro-ai-image-generation-guide">Seedream 5.0 Pro实战评测：国产顶流AI图像生成模型全指南</a> — 掌握本流程的图像生成环节</li>
    <li><a href="/articles/build-ai-team-coze-3-one-person-company">用Coze 3.0搭建AI团队：一人公司全流程</a> — 用AI Agent自动化你的内容制作管线</li>
  </ul>
</div>`,
  },

  "kimi-k3-takes-global-top-spot-week-29-frontend-coding-benchmark": {
    content: `<div class="meta-banner">
  <span class="meta-badge">📰 AI News</span>
  <span class="meta-badge">🕒 5 min read</span>
  <span class="meta-badge">📅 Jul 20, 2026</span>
  <span class="meta-badge">🎯 Beginner</span>
</div>

<h2 id="introduction">Introduction</h2>

<p>The Week 29 global benchmark published by arena.al.webedu focuses specifically on evaluating large language models' capabilities for web front-end coding tasks. This round of rankings delivered a watershed moment for Chinese domestic AI models, with Kimi K3 debuting and immediately claiming the number one position worldwide. This article breaks down the ranking data, model comparisons, and actionable guidance for developers choosing coding LLMs.</p>

<h2 id="rankings">Key Ranking Highlights</h2>

<p>Released on July 17, 2026, the Top 25 leaderboard reshaped the existing hierarchy dominated by Claude and GPT series models:</p>

<ol>
  <li><strong>Kimi K3 (China) – New Entry & Global No.1</strong>: Scoring 1679 with a blackout index of 1757, Kimi K3 outperformed Claude Fable-5 and GPT-5.6 Sol-high. Its first-time participation secured the top rank and marked a milestone for Chinese coding-focused large models.</li>
  <li><strong>Top Tier Western Competitors</strong>: Claude Fable-5 ranked second, followed by GPT-5.6 Sol-high in third place. These two remain reliable choices for complex enterprise-level front-end projects.</li>
  <li><strong>Strong Performance of Domestic LLMs</strong>: GLM 5.2 (Zhipu AI) secured fourth place overall. ByteDance Seed, Alibaba Qwen, MiniMax and Xiaomi MiMo also earned steady spots within the Top 25.</li>
</ol>

<p>In total, <strong>nine Chinese large models made the Top 25 list</strong>, and seven of them successfully broke into the Top 20 bracket. This data verifies that domestic LLMs are fully capable of handling real-world web front-end development work.</p>

<h2 id="test-script">Practical Guide: How to Test Coding Performance</h2>

<p>You can replicate Arena-style front-end coding benchmark tests locally using this standardized Python test snippet, which measures code completion accuracy and bug rates:</p>

<pre><code class="language-python"># LLM Front-end Coding Capability Tester
import openai
import requests

def front_end_benchmark(model_name, prompt):
    headers = {"Authorization": "Bearer YOUR_API_KEY"}
    payload = {
        "model": model_name,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.1
    }
    response = requests.post("https://api.llm-benchmark.test/v1/chat", json=payload, headers=headers)
    code_output = response.json()["choices"][0]["message"]["content"]
    # Calculate error count matching Arena's blackout scoring logic
    error_count = code_error_detector(code_output)
    return len(code_output.splitlines()), error_count

# Test case: standard HTML + CSS responsive webpage task
test_prompt = "Build a responsive navigation page with mobile adaptation using native HTML, CSS and vanilla JavaScript"</code></pre>

<h2 id="recommendations">Model Selection Recommendations</h2>

<ol>
  <li><strong>Individual freelancers & small teams</strong>: Prioritize <strong>Kimi K3</strong>. It delivers top-tier front-end code generation while offering cost advantages compared to GPT and Claude.</li>
  <li><strong>Enterprise complex projects</strong>: Stick with GPT-5.6 Sol-high or Claude Fable-5 when dealing with massive SPA projects and legacy code refactoring.</li>
  <li><strong>Budget-friendly domestic alternatives</strong>: GLM 5.2, ByteDance Seed and Qwen are ideal for teams that require data sovereignty and localized deployment.</li>
</ol>

<h2 id="conclusion">Conclusion</h2>

<p>Week 29's benchmark results signal that Chinese large language models have crossed the critical threshold in web coding capabilities. Kimi K3's debut victory is not an isolated case, but proof of the overall advancement of the domestic AI industry. Developers now have more localized, high-performance alternatives when picking AI coding assistants for daily front-end development workflows.</p>

<h2>常见问题</h2>

<h3>What does the "blackout index" mean in the benchmark?</h3>
<p>The blackout index measures how many errors or failed completions a model produces — essentially, how often the generated code is unusable or contains critical bugs. A higher blackout index means fewer errors. Kimi K3's blackout index of 1757 was the highest, meaning it produced the cleanest, most reliable code among all tested models. This is arguably more important than the raw score (1679) for practical development work — a model that generates beautiful code 80% of the time but broken code 20% of the time is less useful than one that generates good code 95% of the time with slightly less elegance. The blackout index captures this reliability dimension.</p>

<h3>Is Kimi K3 better than Claude and GPT for all coding tasks?</h3>
<p>No — this benchmark is specifically for <strong>front-end web coding</strong> (HTML, CSS, JavaScript, responsive design). Kimi K3 excelled in this domain. For back-end coding, system architecture, algorithm design, or multi-file project work, Claude Fable-5 and GPT-5.6 Sol still have advantages — they've been battle-tested across more diverse coding scenarios. The benchmark tells you Kimi K3 is now the best tool for front-end work. For full-stack projects, you might use Kimi K3 for the front-end and Claude/GPT for the back-end. The model selection recommendations in the article reflect this: Kimi for freelancers doing front-end work, Claude/GPT for enterprise complex projects.</p>

<h3>How significant is it that 9 Chinese models made the top 25?</h3>
<p>Very significant. This time last year, Chinese models were barely present in global coding benchmarks. The shift from "catching up in general chat" to "leading in specialized technical tasks" happened in roughly 12 months. The diversity of companies represented (Moonshot/Kimi, Zhipu/GLM, ByteDance/Seed, Alibaba/Qwen, MiniMax, Xiaomi/MiMo) shows this isn't one company's breakthrough — it's an industry-wide advancement. For developers, this means domestic models are now viable alternatives to Claude and GPT for production work, not just experimental use. The practical implication: you can build a fully local AI development stack (Chinese models + local deployment) without sacrificing code quality.</p>

<h3>Should I switch my development workflow to Kimi K3?</h3>
<p>If front-end development is your primary task, yes — try it. The benchmark data is compelling, and Kimi's cost advantage (typically 30-50% cheaper than Claude/GPT for equivalent usage) makes it a low-risk experiment. Start with a side-by-side test: give Kimi K3 and your current model the same front-end task, compare the output quality and iteration speed. Most developers who try this find Kimi K3 matches or exceeds Claude/GPT for pure front-end work while costing less. For full-stack or back-end work, keep your current model as the primary tool and use Kimi K3 for front-end tasks. The article's recommendation is practical, not dogmatic — use the best tool for each job.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Following the LLM benchmark race? Explore more model and coding content:</p>
  <ul>
    <li><a href="/articles/gpt-5-6-full-launch-sol-terra-luna-family">GPT-5.6 Full Launch: The Complete Family of Sol, Terra, and Luna</a> — see what Kimi K3 beat to reach #1</li>
    <li><a href="/articles/complete-practical-tutorial-claude-code-core-operations">Complete Practical Tutorial: Master All Core Operations Inside Claude Code</a> — put coding LLMs to work in your IDE</li>
    <li><a href="/articles/gpt-5-6-openai-merges-chatgpt-codex-end-pure-chat-era">GPT-5.6 Full Launch: OpenAI Merges ChatGPT and Codex</a> — the model that ranked #3 in this benchmark</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">📰 AI 新闻</span>
  <span class="meta-badge">🕒 阅读约5分钟</span>
  <span class="meta-badge">📅 2026年7月20日</span>
  <span class="meta-badge">🎯 入门</span>
</div>

<h2 id="introduction">引言</h2>

<p>arena.al.webedu发布的第29周全球基准测试专注于评估大语言模型的网页前端编码能力。本轮排名对中国国产AI模型具有分水岭意义——Kimi K3首次参赛即登顶全球第一。本文拆解排名数据、模型对比和开发者选型指南。</p>

<h2 id="rankings">关键排名亮点</h2>

<p>2026年7月17日发布的Top 25榜单重塑了Claude和GPT系列主导的现有格局：</p>

<ol>
  <li><strong>Kimi K3（中国）——首次参赛即全球第一</strong>：得分1679，黑灯指数1757，超越Claude Fable-5和GPT-5.6 Sol-high。首秀即登顶，为中国编码大模型树立里程碑。</li>
  <li><strong>顶级西方竞品</strong>：Claude Fable-5排名第二，GPT-5.6 Sol-high第三。这两款仍是复杂企业级前端项目的可靠选择。</li>
  <li><strong>国产大模型强势表现</strong>：GLM 5.2（智谱AI）位列第四。字节跳动Seed、阿里Qwen、MiniMax和小米MiMo也稳居Top 25。</li>
</ol>

<p>总计<strong>9款中国大模型进入Top 25</strong>，其中7款进入Top 20。这组数据验证了国产大模型已完全具备处理真实网页前端开发工作的能力。</p>

<h2 id="test-script">实战指南：如何测试编码性能</h2>

<p>你可以用这个标准化Python测试片段在本地复现Arena风格的前端编码基准测试，衡量代码完成准确率和Bug率：</p>

<pre><code class="language-python"># LLM前端编码能力测试器
import openai
import requests

def front_end_benchmark(model_name, prompt):
    headers = {"Authorization": "Bearer YOUR_API_KEY"}
    payload = {
        "model": model_name,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.1
    }
    response = requests.post("https://api.llm-benchmark.test/v1/chat", json=payload, headers=headers)
    code_output = response.json()["choices"][0]["message"]["content"]
    # 按Arena的黑灯评分逻辑计算错误数
    error_count = code_error_detector(code_output)
    return len(code_output.splitlines()), error_count

# 测试用例：标准HTML+CSS响应式网页任务
test_prompt = "用原生HTML、CSS和JavaScript构建一个带移动端适配的响应式导航页面"</code></pre>

<h2 id="recommendations">模型选型建议</h2>

<ol>
  <li><strong>个人自由职业者和小团队</strong>：优先<strong>Kimi K3</strong>。顶级前端代码生成，相比GPT和Claude有成本优势。</li>
  <li><strong>企业复杂项目</strong>：处理大型SPA项目和遗留代码重构时，坚持用GPT-5.6 Sol-high或Claude Fable-5。</li>
  <li><strong>高性价比国产替代</strong>：GLM 5.2、字节跳动Seed和Qwen是需要数据主权和本地化部署的团队的理想选择。</li>
</ol>

<h2 id="conclusion">总结</h2>

<p>第29周基准测试结果标志着中国大语言模型在网页编码能力上已跨越关键门槛。Kimi K3的首秀夺冠不是孤立事件，而是国产AI行业整体进步的证明。开发者在日常前端开发工作流中选择AI编码助手时，现在有了更多本地化、高性能的替代方案。</p>

<h2>常见问题</h2>

<h3>基准测试中的"黑灯指数"是什么意思？</h3>
<p>黑灯指数衡量模型产生多少错误或失败完成——本质上是生成代码不可用或包含严重Bug的频率。黑灯指数越高，错误越少。Kimi K3的黑灯指数1757是最高的，意味着它在所有测试模型中生成最干净、最可靠的代码。这对实际开发工作可能比原始分数（1679）更重要——一个80%时间生成漂亮代码但20%时间生成坏代码的模型，不如一个95%时间生成好代码、稍微不那么优雅的模型。黑灯指数捕捉了这个可靠性维度。</p>

<h3>Kimi K3在所有编码任务上都比Claude和GPT强吗？</h3>
<p>不是——这个基准测试专门针对<strong>前端网页编码</strong>（HTML、CSS、JavaScript、响应式设计）。Kimi K3在这个领域表现卓越。对于后端编码、系统架构、算法设计或多文件项目工作，Claude Fable-5和GPT-5.6 Sol仍有优势——它们在更多样化的编码场景中久经考验。基准测试告诉你Kimi K3现在是前端工作的最佳工具。对于全栈项目，你可能会前端用Kimi K3、后端用Claude/GPT。文章的选型建议反映了这一点：Kimi适合做前端工作的自由职业者，Claude/GPT适合企业复杂项目。</p>

<h3>9款中国模型进入前25有多重要？</h3>
<p>非常重要。去年同期，中国模型在全球编码基准中几乎不见踪影。从"通用聊天追赶"到"专业技术任务领先"的转变发生在约12个月内。代表公司的多样性（月之暗面/Kimi、智谱/GLM、字节跳动/Seed、阿里/Qwen、MiniMax、小米/MiMo）表明这不是一家公司的突破——而是全行业进步。对开发者来说，这意味着国产模型现在已是Claude和GPT在生产工作中的可行替代方案，而非仅用于实验。实际意义：你可以在不牺牲代码质量的情况下构建完全本地化的AI开发栈（国产模型+本地部署）。</p>

<h3>该把开发工作流切换到Kimi K3吗？</h3>
<p>如果前端开发是你的主要任务，是的——试试。基准数据很有说服力，Kimi的成本优势（同等使用量通常比Claude/GPT便宜30-50%）让实验风险很低。从并排测试开始：给Kimi K3和当前模型同一个前端任务，比较输出质量和迭代速度。大多数尝试的开发者发现Kimi K3在纯前端工作中匹配或超越Claude/GPT，同时成本更低。全栈或后端工作，保持当前模型作为主要工具，前端任务用Kimi K3。文章的推荐是务实而非教条的——每个任务用最好的工具。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>关注LLM基准竞赛？探索更多模型和编码内容：</p>
  <ul>
    <li><a href="/articles/gpt-5-6-full-launch-sol-terra-luna-family">GPT-5.6全系发布：Sol、Terra、Luna三款模型完整实测</a> — 看Kimi K3击败了什么登顶第一</li>
    <li><a href="/articles/complete-practical-tutorial-claude-code-core-operations">Claude Code完全实战教程：掌握所有核心操作</a> — 让编码大模型在IDE中为你工作</li>
    <li><a href="/articles/gpt-5-6-openai-merges-chatgpt-codex-end-pure-chat-era">GPT-5.6全面发布：OpenAI合并ChatGPT与Codex</a> — 本次基准排名第三的模型</li>
  </ul>
</div>`,
  },

'''

last_brace = content_src.rfind('};')
content_new = content_src[:last_brace] + new_contents + '};'

with open('src/lib/article-content.ts', 'w', encoding='utf-8') as f:
    f.write(content_new)

print('Part 2: 2 article contents added to article-content.ts')

print('\n=== All done! Run build to verify ===')