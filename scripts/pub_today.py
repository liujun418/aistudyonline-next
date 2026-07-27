"""
Publish July 27, 2026 — 1 article, no new tools.
"""
import os; BASE = r"C:\Users\jun\aistudyonline-next"; os.chdir(BASE)

with open('src/lib/articles.ts', 'r', encoding='utf-8') as f: s = f.read()
a = r"""  {
    slug: "how-to-use-douyin-ai-creation-agent-generate-images-videos",
    title: "How to Use Douyin's AI Creation Agent to Generate Images and Videos Without Complex Prompts",
    titleZh: "抖音AI创作助手：无需复杂提示词也能生成图片和视频",
    description: "A beginner-friendly guide to Douyin's AI Creation Agent powered by Seedream 5.0 Pro and Seedance 2.0 — conversational image and video generation without complex prompts, featuring reference photo upload, iterative refinement, trend-based creation, and one-click remixing of existing AI videos.",
    descriptionZh: "抖音AI创作助手新手指南——搭载Seedream 5.0 Pro和Seedance 2.0，对话式图片和视频生成无需复杂提示词，支持参考照片上传、迭代优化、趋势创作和AI视频一键再创作。",
    category: "AI Tools",
    tags: ["Douyin", "AI Creation", "Seedream", "Seedance", "Image Generation", "Video Generation", "Beginner"],
    difficulty: "beginner",
    toolsMentioned: ["Seedream 5.0 Pro", "Seedance 2.0"],
    date: "2026-07-27",
  },

"""
last = s.rfind('];')
with open('src/lib/articles.ts', 'w', encoding='utf-8') as f: f.write(s[:last] + a + '];')
print('Part 1 done')

with open('src/lib/article-content.ts', 'r', encoding='utf-8') as f: c = f.read()
n = r'''
  "how-to-use-douyin-ai-creation-agent-generate-images-videos": {
    content: `<div class="meta-banner">
  <span class="meta-badge">🔧 AI Tools</span>
  <span class="meta-badge">🕒 4 min read</span>
  <span class="meta-badge">📅 Jul 27, 2026</span>
  <span class="meta-badge">🎯 Beginner</span>
</div>

<h2 id="introduction">Introduction</h2>

<p>If you've ever struggled with AI content creation — failing to get the results you want, feeling lost on where to start, or getting stuck on prompt engineering, model selection, and complicated settings — Douyin's newly upgraded AI Creation Agent is here to solve these problems. This conversational creation tool eliminates the need for complex parameters, allowing you to generate content simply by describing your ideas like chatting. It can help you brainstorm directions, generate images, create videos, and even iterate on existing results.</p>

<h2 id="access">How to Access the Tool</h2>

<p>The entry point is located in the "+" button at the bottom of the Douyin app:</p>
<ol>
  <li>Tap the "+" icon</li>
  <li>Select "AI Creation"</li>
  <li>Upload a reference photo of a person</li>
  <li>Enter your specific requirements directly in the chat box</li>
</ol>

<h2 id="image-example">Step-by-Step Image Generation Example</h2>

<p>Let's say you want to create a 3:4 vertical AI tech cover:</p>
<ol>
  <li>Upload your reference photo</li>
  <li>Enter the following prompt:</li>
</ol>
<pre><code class="language-text">Generate a 3:4 vertical AI tech cover, referencing the uploaded person photo</code></pre>
<ol start="3">
  <li>If you're not satisfied with the first version's character proportion and background effect, simply continue the conversation with:</li>
</ol>
<pre><code class="language-text">Enlarge the character by about 20% and replace the background with a bright and clean AI video creation studio</code></pre>
<ol start="4">
  <li>The tool will quickly adjust the result based on your feedback.</li>
</ol>

<h2 id="technology">Underlying Technology</h2>

<p>The AI Creation Agent is powered by ByteDance's Seedream model series:</p>
<ul>
  <li><strong>Seedream 5.0 Pro</strong>: Handles character restoration, image composition, and static details for high-quality image generation</li>
  <li><strong>Seedance 2.0</strong>: Drives video generation with smooth shot transitions and stable character consistency</li>
</ul>

<h2 id="video-workflow">Video Generation Workflow</h2>

<p>To create a dynamic tech opening video using your adjusted cover as a reference:</p>
<ol>
  <li>Use your final cover image as input</li>
  <li>Enter the prompt:</li>
</ol>
<pre><code class="language-text">Generate a dynamic tech opening video based on this reference image</code></pre>
<ol start="3">
  <li>The tool will use Seedance 2.0 to generate a video with coherent shot transitions and consistent character appearance.</li>
</ol>

<h2 id="additional">Additional Features</h2>

<h3>Trend-Based Creation</h3>
<p>The tool can recommend popular creation trends based on your needs. You can directly enter an interesting trend for secondary creation, turning it into a starting point for your own content rather than just a template.</p>

<h3>One-Click Creation from Other Videos</h3>
<p>When you encounter a video with an "AI Creation" anchor: tap the anchor → enter creation mode → keep the core effect of the original video → replace with your own materials and theme → complete a new creation.</p>

<h2 id="conclusion">Why This Tool Is Great for Beginners</h2>
<p>For those new to AI creation, this tool lowers the barriers of prompt engineering and operational complexity. It turns vague ideas into tangible content faster, making AI creation accessible to everyone.</p>

<h2>常见问题</h2>

<h3>How is Douyin AI Creation Agent different from Seedream or Seedance directly?</h3>
<p>The AI Creation Agent is a <strong>consumer-facing product</strong> built on top of Seedream 5.0 Pro and Seedance 2.0. It abstracts away all the technical complexity — no API keys, no parameter tuning, no prompt engineering. When you use Seedream directly (covered in our July 9 guide), you're working with the raw model: JSON-structured prompts, resolution settings, style parameters. The Douyin Agent is the "iPhone version" — conversational, forgiving, designed for creators who want results without learning the underlying technology. For professional workflows (character turnaround sheets, commercial UI design), use Seedream directly. For quick social media content, use the Douyin Agent.</p>

<h3>Can I use this tool without a Chinese phone number?</h3>
<p>No — the AI Creation Agent is built into the Douyin app, which requires a Chinese phone number for registration. This is a domestic Chinese product. International users interested in Seedream/Seedance technology should use the Volcano Engine API directly (covered in our Seedream 5.0 Pro guide) rather than the Douyin consumer app. The underlying models are the same; the access method differs.</p>

<h3>Does the iterative refinement actually work well?</h3>
<p>Yes, and this is the Agent's standout feature. Traditional AI image generation forces you to rewrite the entire prompt for each iteration — change one detail, and everything else might shift. The Douyin Agent's conversational approach maintains context: "enlarge the character 20%" only affects character size, leaving background, lighting, and composition intact. This works well for 2-3 iterations. Beyond that, the model's context degrades and you're better off starting fresh. For best results, nail the composition in your first prompt, then use iterations only for detail adjustments — not major redesigns.</p>

<h3>Can I use the generated images and videos commercially?</h3>
<p>Douyin's terms of service govern commercial usage. Generally, content created with the AI Creation Agent can be posted on Douyin and used for personal/social media purposes. Commercial use (advertisements, product promotions, monetized content) may have additional restrictions or require attribution. The underlying models (Seedream/Seedance via Volcano Engine API) have clearer commercial terms — if you need guaranteed commercial rights, use the API directly rather than the consumer app. Always check the latest terms before using AI-generated content in paid campaigns.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Enjoyed AI creation? Explore the underlying models and more creation workflows:</p>
  <ul>
    <li><a href="/articles/seedream-5-pro-ai-image-generation-guide">Seedream 5.0 Pro: A Comprehensive Practical Guide</a> — master the model powering this tool</li>
    <li><a href="/articles/ai-manhua-production-full-workflow-script-to-monetization">AI Manhua Production Full Workflow: From Script to Monetization</a> — apply AI creation to video content</li>
    <li><a href="/articles/mastering-ai-image-generation-fix-prompt-issues-avoid-draw-failures">Mastering AI Image Generation: Fix Prompt Issues</a> — improve your results even further</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">🔧 AI 工具</span>
  <span class="meta-badge">🕒 阅读约4分钟</span>
  <span class="meta-badge">📅 2026年7月27日</span>
  <span class="meta-badge">🎯 入门</span>
</div>

<h2 id="introduction">引言</h2>

<p>如果你曾在AI内容创作中挣扎——得不到想要的结果、不知从何开始、或卡在提示词工程、模型选择和复杂设置上——抖音新升级的AI创作助手正是为解决这些问题而来。这款对话式创作工具无需复杂参数，像聊天一样描述想法即可生成内容。它能帮你头脑风暴方向、生成图片、制作视频，甚至对已有结果进行迭代优化。</p>

<h2 id="access">如何访问</h2>
<p>入口在抖音App底部"+"按钮：点击"+"→选择"AI创作"→上传人物参考照→在聊天框直接输入具体需求。</p>

<h2 id="image-example">图片生成示例</h2>
<p>创建3:4竖版AI科技封面：</p>
<ol>
  <li>上传参考照片</li>
  <li>输入：</li>
</ol>
<pre><code class="language-text">生成3:4竖版AI科技封面，参考上传的人物照片</code></pre>
<ol start="3">
  <li>不满意第一版人物比例和背景效果？继续对话：</li>
</ol>
<pre><code class="language-text">将人物放大20%左右，背景换成明亮干净的AI视频制作工作室</code></pre>
<ol start="4">
  <li>工具会根据反馈快速调整结果。</li>
</ol>

<h2 id="technology">底层技术</h2>
<p>AI创作助手由字节跳动Seedream模型系列驱动：<strong>Seedream 5.0 Pro</strong>处理人物还原、图像构图和静态细节；<strong>Seedance 2.0</strong>驱动视频生成，镜头过渡流畅、人物一致性稳定。</p>

<h2 id="video-workflow">视频生成流程</h2>
<p>用调整后的封面作为参考创建动态科技开场视频：使用最终封面图→输入"基于此参考图生成动态科技开场视频"→工具用Seedance 2.0生成镜头连贯、人物一致的视频。</p>

<h2 id="additional">附加功能</h2>

<h3>趋势创作</h3>
<p>工具可根据需求推荐热门创作趋势。可直接输入有趣趋势进行二次创作，将其转化为创作起点而非只是模板。</p>

<h3>一键再创作</h3>
<p>遇到带"AI创作"锚点的视频：点击锚点→进入创作模式→保留原视频核心效果→替换为自己的素材和主题→完成新创作。</p>

<h2 id="conclusion">为什么适合新手</h2>
<p>对于AI创作新手，这个工具降低了提示词工程和操作复杂度的门槛，将模糊想法更快转化为可感知的内容，让人人都能用AI创作。</p>

<h2>常见问题</h2>

<h3>抖音AI创作助手和直接用Seedream/Seedance有什么区别？</h3>
<p>AI创作助手是建立在Seedream 5.0 Pro和Seedance 2.0之上的<strong>消费级产品</strong>。它抽象了所有技术复杂性——无需API密钥、无需参数调优、无需提示词工程。直接用Seedream（参见7月9日指南）是用原始模型：JSON结构化提示词、分辨率设置、风格参数。抖音助手是"iPhone版"——对话式、容错性强，为想要结果而非学习底层技术的创作者设计。专业工作流（角色三视图、商业UI设计）直接用Seedream。快速社交媒体内容用抖音助手。</p>

<h3>没有中国手机号能用吗？</h3>
<p>不能——AI创作助手内置在抖音App中，需中国手机号注册。这是国产产品。对Seedream/Seedance技术感兴趣的国际用户应直接用火山引擎API（参见Seedream 5.0 Pro指南），而非抖音消费App。底层模型相同，访问方式不同。</p>

<h3>迭代优化真的有效吗？</h3>
<p>有效，这是助手的突出特性。传统AI图像生成每次迭代都需重写整个提示词——改一个细节，其他可能全变。抖音助手的对话方式保持上下文："把人物放大20%"只影响人物大小，背景、光影、构图保持不变。2-3次迭代效果最好。超过后模型上下文衰减，最好重新开始。最佳实践：首次提示词搞定构图，迭代仅用于细节调整——不做大改。</p>

<h3>生成的图片和视频能商用吗？</h3>
<p>抖音服务条款约束商业使用。一般来说，用AI创作助手生成的内容可在抖音发布和用于个人/社交媒体目的。商业用途（广告、产品推广、盈利内容）可能有额外限制或需要署名。底层模型（Seedream/Seedance通过火山引擎API）有更清晰的商业条款——如需保障商业使用权，直接用API而非消费App。付费广告中使用AI生成内容前始终查看最新条款。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>喜欢AI创作？探索底层模型和更多创作工作流：</p>
  <ul>
    <li><a href="/articles/seedream-5-pro-ai-image-generation-guide">Seedream 5.0 Pro实战评测：国产顶流AI图像生成模型全指南</a> — 掌握驱动本工具的模型</li>
    <li><a href="/articles/ai-manhua-production-full-workflow-script-to-monetization">AI漫剧制作全流程：从剧本到变现的完整指南</a> — 将AI创作应用到视频内容</li>
    <li><a href="/articles/mastering-ai-image-generation-fix-prompt-issues-avoid-draw-failures">掌握AI图像生成：修复提示词问题，避免'翻车'</a> — 进一步优化你的创作结果</li>
  </ul>
</div>`,
  },

'''
last = c.rfind('};')
with open('src/lib/article-content.ts', 'w', encoding='utf-8') as f: f.write(c[:last] + n + '};')
print('Part 2 done')
print('=== Done ===')