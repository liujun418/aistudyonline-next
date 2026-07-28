"""Publish July 28, 2026 — 1 article, no new tools."""
import os; BASE = r"C:\Users\jun\aistudyonline-next"; os.chdir(BASE)

with open('src/lib/articles.ts', 'r', encoding='utf-8') as f: s = f.read()
a = r"""  {
    slug: "full-practical-guide-ai-comic-drama-production-zero-to-published",
    title: "Full Practical Guide to AI Comic Drama Production: From Zero to Published Video",
    titleZh: "AI漫剧制作完全实战指南：从零到发布视频",
    description: "A complete 4-step AI comic drama production workflow — scene description with AI refinement, text-to-image with style/aspect ratio control, image-to-video with dialogue and voice direction, and post-production editing with sound effects, subtitles, and trimming — plus AI script creation techniques.",
    descriptionZh: "AI漫剧四步完整制作流程——AI润色场景描述、文生图（风格/比例控制）、图生视频（对话/声音指导）和后期剪辑（音效/字幕/裁剪）——含AI剧本创作技巧。",
    category: "AI Tutorials",
    tags: ["AI Comic Drama", "Video Generation", "Content Creation", "Seedance", "Xiaoyunque", "Tutorial"],
    difficulty: "beginner",
    toolsMentioned: ["Seedance 2.0", "Xiaoyunque", "CapCut"],
    date: "2026-07-28",
  },

"""
last = s.rfind('];')
with open('src/lib/articles.ts', 'w', encoding='utf-8') as f: f.write(s[:last] + a + '];')
print('Part 1 done')

with open('src/lib/article-content.ts', 'r', encoding='utf-8') as f: c = f.read()
n = r'''
  "full-practical-guide-ai-comic-drama-production-zero-to-published": {
    content: `<div class="meta-banner">
  <span class="meta-badge">📚 AI Tutorials</span>
  <span class="meta-badge">🕒 6 min read</span>
  <span class="meta-badge">📅 Jul 28, 2026</span>
  <span class="meta-badge">🎯 Beginner</span>
</div>

<h2 id="introduction">Introduction</h2>
<p>AI comic drama is a highly profitable form of animated short drama that allows audiences to unlock episodes by either paying or watching ads. In this guide, we will walk you through the complete process of creating an AI comic drama, from initial scene description to final post-production, using free AI tools.</p>

<h2 id="workflow">Core Production Workflow</h2>
<p>The AI video production process consists of four key steps: Scene Description → Text-to-Image Generation → Image-to-Video Generation → Post-Production Editing.</p>

<h2 id="step-1">Step 1: Scene Description</h2>
<p>Use an AI assistant to help refine your scene description:</p>
<pre><code class="language-text">I will provide you with a scene, please help me refine it into a detailed scene description, do not generate images: a girl standing by a grassland, with long white hair, red eyes, wearing a large white hat and a white dress, looking at the camera.</code></pre>
<p><strong>Key Tips</strong>: Be clear about what you'll provide, specify what you want AI to do, and clearly state what you don't want.</p>

<h2 id="step-2">Step 2: Text-to-Image Generation</h2>
<p>Once you have a refined scene description, generate images:</p>
<pre><code class="language-text">Generate an image for this scene, with a 16:9 aspect ratio, using a flat Japanese anime style.</code></pre>
<p><strong>Key Tips</strong>: Always specify aspect ratio (16:9 for horizontal videos), specify art style, generate multiple and select the best.</p>

<h2 id="step-3">Step 3: Image-to-Video Generation</h2>
<p>After selecting the best image, generate a video:</p>
<pre><code class="language-text">Generate a video from this image, with a 16:9 aspect ratio. The girl says: "I have forgotten my original name, just call me Bai. Do you remember your name?" Her voice is soft, and the wind gently blows her hair.</code></pre>
<p><strong>Key Tips</strong>: Use tools like Xiaoyunque for cost-effective generation, 10 seconds recommended for beginners, let AI freely add details.</p>

<h2 id="step-4">Step 4: Post-Production Editing</h2>
<p>Use Jianying (CapCut) for final editing:</p>
<ol>
  <li><strong>Add Sound Effects</strong>: Match the scene (e.g., wind blowing through grass)</li>
  <li><strong>Adjust Audio Levels</strong>: Balance sound effects with video</li>
  <li><strong>Add Subtitles</strong>: Add dialogue text</li>
  <li><strong>Trim the Video</strong>: Cut to desired length</li>
</ol>

<h2 id="script">Script Creation with AI</h2>
<p>The core of AI script creation is precise prompting — Who, What, How:</p>
<pre><code class="language-text">You are a skilled animation screenwriter specializing in one-minute healing animation series. Please write a one-minute animation core plot around the theme of "companionship", with the protagonist being a cartoon cat.</code></pre>

<h2 id="conclusion">Conclusion</h2>
<p>By following these four steps, you can create a high-quality AI comic drama from scratch. Remember to refine your prompts, experiment with different tools, and iterate on your work to achieve the best results.</p>

<h2>常见问题</h2>

<h3>How is this guide different from the July 20 AI Manhua guide?</h3>
<p>The July 20 guide covered the <strong>production workflow</strong> plus script creation methods, monetization, and model selection. This guide is a <strong>streamlined production-only walkthrough</strong> — it focuses on the exact prompts and steps to go from idea to published video as fast as possible. It adds dialogue/voice direction in the image-to-video step (the July 20 guide didn't cover adding character dialogue to videos) and a simpler script creation template. Read the July 20 guide for the full ecosystem (monetization, model comparison, prompt optimization). Read this one for a quick-start production recipe you can follow today.</h3>

<h3>Which free tools should I use for each step?</h3>
<p>Step 1 (Scene Description): Any free AI chat — Doubao, Kimi, ChatGPT free tier.<br>Step 2 (Text-to-Image): Seedream free tier or Xiaoyunque free daily credits.<br>Step 3 (Image-to-Video): Xiaoyunque (free daily credits, ~5 credits per 10s video).<br>Step 4 (Post-Production): Jianying/CapCut free version (watermark on export, paid version removes it). Total cost for your first episode: $0. The tools mentioned (Xiaoyunque, Jianying) were chosen specifically for their free tiers — you can produce a complete episode without spending anything.</p>

<h3>How long does it take to produce one episode?</h3>
<p>For a beginner following this guide: 2-3 hours for the first episode (includes learning curve). After 3-5 episodes: 30-60 minutes per episode. The bottleneck is usually image generation (waiting for results, selecting the best one) and post-production (sound effects and subtitle timing). The AI generation steps themselves take only 1-2 minutes each. The time goes into creative decisions: which image looks best, what sound effect fits, how to pace the subtitles.</p>

<h3>Can I make money from AI comic dramas?</h3>
<p>Yes, through platforms that support paid unlock or ad revenue models for short dramas. The July 20 AI Manhua guide covers monetization in detail (paid unlock + ad revenue). The key success factors: publish consistently (2-3 episodes/week), build a content library (50+ episodes), and focus on engaging story hooks in the first 3 seconds. Individual episodes earn modest amounts, but cumulative revenue from a large content library can become meaningful. The AI workflow reduces production cost to near-zero, so even modest revenue is profitable.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Created your first episode? Level up your AI content production:</p>
  <ul>
    <li><a href="/articles/ai-manhua-production-full-workflow-script-to-monetization">AI Manhua Production Full Workflow: From Script to Monetization</a> — the complete ecosystem guide</li>
    <li><a href="/articles/how-to-use-douyin-ai-creation-agent-generate-images-videos">How to Use Douyin's AI Creation Agent</a> — another conversational creation tool</li>
    <li><a href="/articles/mastering-ai-image-generation-fix-prompt-issues-avoid-draw-failures">Mastering AI Image Generation: Fix Prompt Issues</a> — improve your image outputs</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">📚 AI 教程</span>
  <span class="meta-badge">🕒 阅读约6分钟</span>
  <span class="meta-badge">📅 2026年7月28日</span>
  <span class="meta-badge">🎯 入门</span>
</div>

<h2 id="introduction">引言</h2>
<p>AI漫剧是一种高收益的动画短剧形式，观众可通过付费或观看广告解锁剧集。本指南将带你走完AI漫剧创作的完整流程——从初始场景描述到最终后期制作，全部使用免费AI工具。</p>

<h2 id="workflow">核心制作流程</h2>
<p>AI视频制作四步走：场景描述 → 文生图 → 图生视频 → 后期剪辑。</p>

<h2 id="step-1">第一步：场景描述</h2>
<p>用AI助手润色场景描述：</p>
<pre><code class="language-text">我会给你一个场景，请帮我润色成详细的场景描述，不要生成图片：一个女孩站在草原旁，白色长发，红色眼眸，戴着白色大帽子穿着白色连衣裙，看着镜头。</code></pre>
<p><strong>关键技巧</strong>：明确提供什么、让AI做什么、不让AI做什么。</p>

<h2 id="step-2">第二步：文生图</h2>
<p>润色后的场景生成图片：</p>
<pre><code class="language-text">为这个场景生成一张图片，16:9比例，使用日式动漫平面风格。</code></pre>
<p><strong>关键技巧</strong>：始终指定比例（横屏视频用16:9）、指定美术风格、生成多张选最优。</p>

<h2 id="step-3">第三步：图生视频</h2>
<p>选好图后生成视频：</p>
<pre><code class="language-text">基于这张图生成16:9比例的视频。女孩说："我忘了自己原来的名字，叫我白就好。你还记得你的名字吗？"声音轻柔，微风轻轻吹动头发。</code></pre>
<p><strong>关键技巧</strong>：用Xiaoyunque等实惠工具、新手推荐10秒、让AI自由添加细节。</p>

<h2 id="step-4">第四步：后期剪辑</h2>
<p>用剪映完成：</p>
<ol>
  <li><strong>添加音效</strong>：匹配场景（如草地配风声）</li>
  <li><strong>调整音量</strong>：平衡音效与视频</li>
  <li><strong>添加字幕</strong>：加入对白文本</li>
  <li><strong>裁剪视频</strong>：切成需要时长</li>
</ol>

<h2 id="script">AI剧本创作</h2>
<p>AI剧本核心是精准提示词——Who/What/How：</p>
<pre><code class="language-text">你是一位擅长一分钟治愈动画系列的动画编剧。请围绕"陪伴"主题创作一分钟动画核心剧情，主角是一只卡通猫。</code></pre>

<h2 id="conclusion">总结</h2>
<p>遵循这四步，你可以从零开始创作高质量AI漫剧。记住不断优化提示词、尝试不同工具、持续迭代，取得最佳效果。</p>

<h2>常见问题</h2>

<h3>本指南和7月20日的AI漫剧指南有什么不同？</h3>
<p>7月20日指南涵盖<strong>制作流程</strong>+剧本创作方法+变现+模型选择。本指南是<strong>精简纯制作指南</strong>——聚焦最快从创意到发布视频的具体提示词和步骤。它在图生视频步骤中增加了对话/声音指导（7月20日指南未涵盖添加角色对话）和更简单的剧本创作模板。读7月20日指南了解完整生态（变现、模型对比、提示词优化）。读本指南获取今天就能用的快速制作配方。</p>

<h3>每步该用哪个免费工具？</h3>
<p>第一步（场景描述）：任何免费AI聊天——豆包、Kimi、ChatGPT免费层。<br>第二步（文生图）：Seedream免费层或Xiaoyunque每日免费积分。<br>第三步（图生视频）：Xiaoyunque（每日免费积分，约5积分/10秒视频）。<br>第四步（后期）：剪映/CapCut免费版（导出带水印，付费版去水印）。第一集总成本：$0。提到的工具（Xiaoyunque、剪映）专为其免费层选择——可以零成本产出完整一集。</p>

<h3>一集制作需要多长时间？</h3>
<p>新手按本指南操作：首集约2-3小时（含学习曲线）。3-5集后：每集30-60分钟。瓶颈通常是文生图（等待结果、选最优）和后期（音效和字幕时机）。AI生成步骤本身每次仅需1-2分钟。时间花在创意决策上：哪张图最好、什么音效合适、字幕如何把握节奏。</p>

<h3>AI漫剧能赚钱吗？</h3>
<p>能，通过支持付费解锁或广告收益模式的短剧平台。7月20日AI漫剧指南详细介绍了变现方式（付费解锁+广告收入）。关键成功要素：持续发布（每周2-3集）、建立内容库（50+集）、聚焦前3秒吸引人的故事钩子。单集收入有限，但大量内容库的累计收益可以变得可观。AI工作流将制作成本降到几乎为零，即使微薄收入也能盈利。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>创作了第一集？升级你的AI内容制作：</p>
  <ul>
    <li><a href="/articles/ai-manhua-production-full-workflow-script-to-monetization">AI漫剧制作全流程：从剧本到变现的完整指南</a> — 完整生态指南</li>
    <li><a href="/articles/how-to-use-douyin-ai-creation-agent-generate-images-videos">抖音AI创作助手：无需复杂提示词也能生成图片和视频</a> — 另一款对话式创作工具</li>
    <li><a href="/articles/mastering-ai-image-generation-fix-prompt-issues-avoid-draw-failures">掌握AI图像生成：修复提示词问题，避免'翻车'</a> — 优化你的图像输出</li>
  </ul>
</div>`,
  },

'''
last = c.rfind('};')
with open('src/lib/article-content.ts', 'w', encoding='utf-8') as f: f.write(c[:last] + n + '};')
print('Part 2 done\n=== Done ===')