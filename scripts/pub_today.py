"""
Publish July 9, 2026 — 2 articles + 1 new tool (Seedream 5.0 Pro).
"""
import os

BASE = r"C:\Users\jun\aistudyonline-next"
os.chdir(BASE)

# ===== Part 1: Add 1 new tool to tools.ts =====
with open('src/lib/tools.ts', 'r', encoding='utf-8') as f:
    tools_src = f.read()

new_tools = r"""
  {
    id: "seedream-5-pro",
    name: "Seedream 5.0 Pro",
    nameZh: "Seedream 5.0 Pro",
    description: "ByteDance's flagship AI image generation model on Volcano Engine, delivering 2K resolution with exceptional Chinese text rendering, artistic detail, and commercial design capabilities.",
    descriptionZh: "字节跳动火山引擎旗舰AI图像生成模型，支持2K分辨率，中文文字渲染、艺术细节和商业设计能力出色。",
    category: "image-generation",
    tags: ["image-generation", "china", "bytedance", "design", "commercial", "2k"],
    difficulty: "beginner",
    url: "https://www.volcengine.com/product/seedream",
    rating: 4.5,
    pricing: "Pay per use",
    useCase: "AI image generation — artistic portraits, Chinese text designs, character turnaround sheets, commercial UI mockups, and bookmark/poster designs",
    icon: "🎨",
    company: "ByteDance",
    companyZh: "字节跳动",
    founded: 2012,
    headquarters: "Beijing, China",
    descriptionLong: "Seedream 5.0 Pro is ByteDance's latest flagship AI image generation model, hosted on the Volcano Engine platform. It represents a significant leap in Chinese AI imaging capability, competing directly with global leaders like GPT Image 2 and Nano Banana Pro. Priced at ¥0.3 per 1K image (¥0.6 at 2K resolution), it offers exceptional value for professional-grade output. The model excels in five key areas: (1) Artistic expression — renders fine details like petals, water droplets, and fabric textures at 2K with near-photographic realism; (2) Chinese text rendering — a standout feature where many global models fail, Seedream accurately renders Chinese characters in handwritten, typographic, and decorative styles; (3) Simple prompt interpretation — expands brief prompts into complete commercial designs with professional creative extensions; (4) Professional workflow support — generates character turnaround sheets with consistent front/side/back views for game and animation production; (5) Complex commercial UI — produces cohesive steampunk, fantasy, and modern UI mockups with all required interface elements. Independent testing shows it outperforms Nano Banana Pro in most scenarios and approaches GPT Image 2 in composition quality, with Chinese text handling as its clear differentiator. For Chinese designers, developers, and content creators who need high-quality AI imaging with native Chinese language support, Seedream 5.0 Pro is currently the strongest domestic option.",
    descriptionLongZh: "Seedream 5.0 Pro是字节跳动最新的旗舰AI图像生成模型，部署在火山引擎平台。它代表了中国AI成像能力的重大飞跃，直接与GPT Image 2和Nano Banana Pro等全球领先产品竞争。定价¥0.3/千张（2K分辨率¥0.6/千张），专业级输出性价比极高。模型在五个关键领域表现突出：（1）艺术表现力——2K分辨率下渲染花瓣、水滴、布料纹理等精细细节，接近照片级真实感；（2）中文文字渲染——这是许多全球模型的短板，Seedream准确渲染手写、排版和装饰风格的中文字符；（3）简单提示词理解——将简短提示词扩展为完整的商业设计，添加专业级创意延伸；（4）专业工作流支持——生成前后侧一致的角色三视图，用于游戏和动画制作；（5）复杂商业UI——生成风格统一的蒸汽朋克、奇幻和现代UI界面，包含所有必需元素。独立测试表明它在大多数场景下超越Nano Banana Pro，构图质量接近GPT Image 2，中文文字处理是其核心差异化优势。对于需要高质量AI成像且支持原生中文的中国设计师、开发者和内容创作者，Seedream 5.0 Pro是目前最强的国产选择。",
    advantages: ["Best-in-class Chinese text rendering", "2K resolution with fine detail preservation", "Expands simple prompts into professional designs", "Character turnaround consistency for production workflows", "Competitive pricing at ¥0.3/1K images", "Steampunk and complex UI generation capability"],
    advantagesZh: ["中文文字渲染业界最佳", "2K分辨率精细细节保留", "简单提示词自动扩展为专业设计", "角色三视图一致性适合生产流程", "¥0.3/千张的竞争力定价", "蒸汽朋克和复杂UI生成能力"],
    useCases: ["Artistic portrait and seasonal theme generation", "Handwritten Chinese text designs and bookmarks", "Game character turnaround sheets (front/side/back)", "Commercial mobile game UI mockups", "Traditional Chinese painting style designs"],
    useCasesZh: ["艺术肖像和四季主题生成", "手写中文文字设计和书签", "游戏角色三视图（正/侧/背面）", "商业手游UI界面设计", "传统中国画风格设计"],
    targetAudience: "Chinese designers, game developers, content creators, and anyone who needs AI image generation with accurate Chinese text rendering",
    targetAudienceZh: "中国设计师、游戏开发者、内容创作者，以及需要准确中文文字渲染的AI图像生成用户",
    pricingTiers: [
      {
        tier: "Pay-per-use",
        tierZh: "按量付费",
        price: "¥0.3/1K image (¥0.6 at 2K)",
        features: ["2K max resolution", "All model capabilities", "Volcano Engine API access"],
        featuresZh: ["最高2K分辨率", "全部模型能力", "火山引擎API访问"],
      },
    ],
    pros: ["Exceptional Chinese text accuracy", "2K detail rivals GPT Image 2", "Strong simple-prompt interpretation", "Affordable per-image pricing", "Consistent character turnaround output"],
    prosZh: ["中文文字准确度出色", "2K细节媲美GPT Image 2", "简单提示词理解力强", "按张计费价格实惠", "角色三视图输出一致"],
    cons: ["Initial generation can be slow (up to 2.5 min)", "Occasional Chinese text garbling in complex UIs", "Composition still slightly behind GPT Image 2", "Requires Volcano Engine account"],
    consZh: ["首次生成可能较慢（最长2.5分钟）", "复杂UI中偶有中文乱码", "构图仍略逊GPT Image 2", "需要火山引擎账号"],
    extensions: [],
    skills: ["Artistic portrait generation", "Chinese text rendering", "Character turnaround sheets", "UI/UX mockup generation", "Traditional art style design"],
    scene: "design-video",
  },
"""

last_tool = tools_src.rfind('] as Tool[];')
tools_new = tools_src[:last_tool] + new_tools + '] as Tool[];'

with open('src/lib/tools.ts', 'w', encoding='utf-8') as f:
    f.write(tools_new)

print('Part 1: 1 new tool added to tools.ts (Seedream 5.0 Pro)')

# ===== Part 2: Add 2 article metadata to articles.ts =====
with open('src/lib/articles.ts', 'r', encoding='utf-8') as f:
    articles_src = f.read()

new_articles = r"""  {
    slug: "seedream-5-pro-ai-image-generation-guide",
    title: "Seedream 5.0 Pro: A Comprehensive Practical Guide to China's Leading AI Image Generation Model",
    titleZh: "Seedream 5.0 Pro实战评测：国产顶流AI图像生成模型全指南",
    description: "Hands-on testing of ByteDance's Seedream 5.0 Pro across five scenarios — artistic eye close-ups, Chinese text rendering, bookmark design, character turnaround sheets, and steampunk UI — comparing against GPT Image 2 and Nano Banana Pro.",
    descriptionZh: "字节跳动Seedream 5.0 Pro五大场景实战评测——艺术眼部特写、中文文字渲染、书签设计、角色三视图和蒸汽朋克UI——与GPT Image 2和Nano Banana Pro横向对比。",
    category: "AI Tools",
    tags: ["Seedream", "ByteDance", "Image Generation", "China", "AI Art", "Design", "Review"],
    difficulty: "beginner",
    toolsMentioned: ["Seedream 5.0 Pro", "GPT Image 2", "Nano Banana Pro"],
    date: "2026-07-09",
  },
  {
    slug: "official-tutorial-three-ways-codex-control-computer",
    title: "Official Tutorial: Three Ways Codex Can Control Your Computer for You",
    titleZh: "官方教程：Codex控制电脑的三种方式详解",
    description: "OpenAI's Jason Liu breaks down Codex's three computer control modes — Computer Use (desktop automation), Chrome Extension (browser tasks), and In-App Browser (web dev debugging) — with real-world examples and a decision framework for choosing the right mode.",
    descriptionZh: "OpenAI Jason Liu详解Codex三种电脑控制方式——Computer Use（桌面自动化）、Chrome扩展（浏览器任务）和内置浏览器（网页开发调试）——含真实案例和选型决策框架。",
    category: "AI Tools",
    tags: ["Codex", "OpenAI", "Computer Use", "Automation", "Chrome Extension", "Tutorial"],
    difficulty: "beginner",
    toolsMentioned: ["Codex Agent"],
    date: "2026-07-09",
  },

"""

last_bracket = articles_src.rfind('];')
articles_new = articles_src[:last_bracket] + new_articles + '];'

with open('src/lib/articles.ts', 'w', encoding='utf-8') as f:
    f.write(articles_new)

print('Part 2: 2 new articles added to articles.ts')

# ===== Part 3: Add article content to article-content.ts =====
with open('src/lib/article-content.ts', 'r', encoding='utf-8') as f:
    content_src = f.read()

new_contents = r'''
  "seedream-5-pro-ai-image-generation-guide": {
    content: `<div class="meta-banner">
  <span class="meta-badge">🔧 AI Tools</span>
  <span class="meta-badge">🕒 7 min read</span>
  <span class="meta-badge">📅 Jul 9, 2026</span>
  <span class="meta-badge">🎯 Beginner</span>
</div>

<h2 id="introduction">Introduction</h2>

<p>Seedream 5.0 Pro, the latest breakthrough from China's AI image generation landscape, is making waves as a formidable competitor to top global models like GPT Image 2 and Nano Banana Pro. This guide will walk you through hands-on testing of Seedream 5.0 Pro across five distinct scenarios, using five unique prompt structures to evaluate its real-world performance. All demonstrations are based on practical usage experience, with no commercial affiliations, ensuring you get reliable, actionable insights.</p>

<h2 id="getting-started">Getting Started with Seedream 5.0 Pro</h2>

<p>To begin using Seedream 5.0 Pro, navigate to the Volcano Engine official website and select the model. Key details about its pricing and capabilities include:</p>

<ul>
  <li><strong>Pricing</strong>: ¥0.3 per 1K image, with a maximum supported resolution of 2K (¥0.6 per 2K image).</li>
  <li><strong>Performance Note</strong>: Initial generation times may be slow (up to 2.5 minutes for the first image) due to model rollout and increased parameter size, but this is expected to improve as infrastructure stabilizes.</li>
</ul>

<h2 id="testing">Practical Testing Scenarios</h2>

<h3>1. Artistic Expression: Four Seasons Eye Close-Ups</h3>

<p><strong>Prompt</strong>: Generate a set of four eye close-ups representing the four seasons (spring, summer, autumn, winter). Integrate seasonal elements (cherry blossoms for spring, lotus for summer, maple leaves for autumn, snowflakes for winter) into the iris, eyelashes, and lighting, while maintaining realistic details and a unified artistic style.</p>

<p><strong>Results</strong>: Seedream 5.0 Pro delivered exceptional detail, with fine textures of petals, leaves, and water droplets clearly visible in 2K resolution. The model achieved a level of artistic detail comparable to GPT Image 2, though GPT Image 2 maintained a slight edge in overall composition and visual impact.</p>

<h3>2. Chinese Text and Layout: Handwritten Style Notes</h3>

<p><strong>Prompt</strong>: Use a JSON-structured prompt to generate a handwritten-style note with a large amount of Chinese text. Ensure accurate character rendering, proper layout, and consistent style.</p>

<p><strong>Results</strong>: Seedream 5.0 Pro excelled here, rendering all Chinese characters correctly and maintaining a stable handwritten style. This addresses a common pain point for many AI models that struggle with Chinese text and layout consistency.</p>

<h3>3. Simple Prompt Understanding: Traditional Chinese Bookmark Design</h3>

<p><strong>Prompt</strong>: Generate a series of traditional Chinese painting bookmark designs.</p>

<p><strong>Results</strong>: Seedream 5.0 Pro expanded this simple prompt into a complete commercial design, incorporating traditional elements like plum blossoms, orchids, bamboo, chrysanthemums, flowers, birds, and landscapes, along with material textures, patterns, and craftsmanship details. This demonstrates its ability to interpret basic prompts and add professional-level creative extensions.</p>

<h3>4. Professional Workflow: Character Turnaround Sheet</h3>

<p><strong>Prompt</strong>: Using a reference image of a novel's female lead, generate a character turnaround sheet showing front, side, and back views. Ensure visual consistency across all angles, including hairstyle, clothing, textures, accessories, and weapons.</p>

<p><strong>Results</strong>: The turnaround sheet showed high overall completeness, with consistent details across all views. While there was slight overlap between the headshots and full-body views, the model provided sufficient consistency for character reference in AI video and animation production workflows.</p>

<h3>5. Complex Commercial UI: Steampunk Mobile Game Main Interface</h3>

<p><strong>Prompt</strong>: Generate a complete commercial-level 2D mobile game main interface with a steampunk worldview. Include UI elements like character resource bars, function buttons, event entrances, and ensure visual consistency across all components.</p>

<p><strong>Results</strong>: Seedream 5.0 Pro successfully generated a visually cohesive steampunk interface with all required UI elements. Minor areas for improvement included occasional Chinese text garbling and simplified mechanical weapon details, but the overall result was suitable for game art, UI design, and development reference.</p>

<h2 id="comparison">Model Comparison</h2>

<p>Based on practical testing, Seedream 5.0 Pro outperforms Nano Banana Pro in most scenarios. While it still has room to improve in composition and stability compared to GPT Image 2, it stands as one of the top AI image generation models globally, solidifying its position as a leading Chinese AI innovation.</p>

<h2 id="conclusion">Conclusion</h2>

<p>Seedream 5.0 Pro is a powerful, practical AI image generation model that excels in artistic detail, Chinese text handling, simple prompt interpretation, professional workflow support, and complex commercial UI design. Whether you're a designer, developer, or content creator, it offers valuable capabilities for enhancing your creative workflow.</p>

<h2>常见问题</h2>

<h3>How does Seedream 5.0 Pro compare to Midjourney?</h3>
<p>They serve different strengths. Midjourney excels at artistic composition, atmospheric lighting, and creative interpretation — it's the go-to for concept art and mood-driven pieces. Seedream 5.0 Pro's key differentiator is <strong>Chinese text accuracy</strong> and <strong>commercial workflow support</strong>. If you need a poster with Chinese text, Midjourney will likely mangle the characters. Seedream renders them correctly. For character turnaround sheets (front/side/back views) and UI mockups, Seedream's consistency is production-ready. For pure artistic quality without text, Midjourney still leads. For Chinese commercial design work, Seedream is the better choice.</p>

<h3>Is the ¥0.3 per 1K image pricing competitive?</h3>
<p>Yes, significantly. At ~$0.04 per 1K images (standard resolution) or ~$0.08 per 2K images, Seedream is among the most affordable professional-grade AI image generators. For comparison, Midjourney's standard plan is $10/month for ~200 images ($0.05/image), and DALL-E 3 via API is $0.04-0.12/image depending on resolution. Seedream's per-image cost is 1-2 orders of magnitude lower, making it viable for high-volume production workflows like game asset generation, e-commerce product images, and batch content creation.</p>

<h3>Why is the first generation so slow (2.5 minutes)?</h3>
<p>This is a cold-start issue common with newly deployed large models. The model needs to load into GPU memory on first request. Subsequent generations are typically much faster (30-60 seconds). This should improve as Volcano Engine optimizes their infrastructure and the model graduates from rollout phase to stable production. For batch work, generate images in sequence rather than one at a time — the warm model stays loaded and each subsequent image is faster.</p>

<h3>Can Seedream 5.0 Pro generate English text designs?</h3>
<p>Yes, but Chinese text is its standout feature. English text rendering is competent but not as extensively tested or optimized. For English-heavy designs, GPT Image 2 or DALL-E 3 may produce more polished results. Seedream's sweet spot is bilingual or Chinese-primary designs where you need Chinese characters to look perfect. If your design is English-only, test both Seedream and the alternatives — the results may surprise you, but don't assume English text will be as flawless as Chinese.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Impressed by Seedream? Explore more AI image and design tools:</p>
  <ul>
    <li><a href="/articles/2025-ai-toolkit-practical-guide-every-domain">2025 AI Toolkit: A Practical Guide for Every Domain</a> — discover more AI tools across categories</li>
    <li><a href="/articles/ai-bubble-or-opportunity-guide-ordinary-people">Is AI a Bubble or Opportunity? A Guide for Ordinary People</a> — understand ByteDance's role in the AI landscape</li>
    <li><a href="/articles/top-5-ai-ppt-skills-tested-ranked">Battle of the Best: Top 5 AI PPT Skills Tested and Ranked</a> — if design productivity is your focus</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">🔧 AI 工具</span>
  <span class="meta-badge">🕒 阅读约7分钟</span>
  <span class="meta-badge">📅 2026年7月9日</span>
  <span class="meta-badge">🎯 入门</span>
</div>

<h2 id="introduction">引言</h2>

<p>Seedream 5.0 Pro是中国AI图像生成领域的最新突破，作为GPT Image 2和Nano Banana Pro等全球顶级模型的有力竞争者引起广泛关注。本指南将在五个不同场景下实战测试Seedream 5.0 Pro，用五种独特提示词结构评估其真实表现。所有演示基于实际使用体验，无商业关联，确保你获得可靠、可操作的洞察。</p>

<h2 id="getting-started">快速上手</h2>

<p>使用Seedream 5.0 Pro，导航到火山引擎官网选择该模型。关于定价和能力的关键信息：</p>

<ul>
  <li><strong>定价</strong>：¥0.3/千张，最高支持2K分辨率（2K为¥0.6/千张）。</li>
  <li><strong>性能提示</strong>：由于模型部署和参数规模增大，首次生成可能较慢（最长2.5分钟），随着基础设施稳定预计会改善。</li>
</ul>

<h2 id="testing">实战测试场景</h2>

<h3>1. 艺术表现：四季眼部特写</h3>

<p><strong>提示词</strong>：生成一组四张代表四季的眼部特写。将季节元素（春樱、夏荷、秋枫、冬雪）融入虹膜、睫毛和光影中，保持真实细节和统一艺术风格。</p>

<p><strong>结果</strong>：Seedream 5.0 Pro细节表现出色，2K分辨率下花瓣、叶片和水滴的细腻纹理清晰可见。艺术细节水平媲美GPT Image 2，但GPT Image 2在整体构图和视觉冲击力上仍略占优势。</p>

<h3>2. 中文文字与排版：手写风格笔记</h3>

<p><strong>提示词</strong>：使用JSON结构化提示词生成包含大量中文文字的手写风格笔记。确保文字渲染准确、排版合理、风格一致。</p>

<p><strong>结果</strong>：Seedream 5.0 Pro在此表现卓越，所有中文字符渲染正确，手写风格稳定。这解决了许多AI模型在中文文字和排版一致性上的痛点。</p>

<h3>3. 简单提示词理解：传统中国风书签设计</h3>

<p><strong>提示词</strong>：生成一系列传统中国画书签设计。</p>

<p><strong>结果</strong>：Seedream 5.0 Pro将这个简短提示词扩展为完整的商业设计，融入梅兰竹菊、花鸟山水等传统元素，以及材质纹理、纹样和工艺细节。这展示了它解读基础提示词并添加专业级创意延伸的能力。</p>

<h3>4. 专业工作流：角色三视图</h3>

<p><strong>提示词</strong>：使用小说女主角的参考图，生成正面、侧面和背面的角色三视图。确保各角度视觉一致，包括发型、服装、纹理、配饰和武器。</p>

<p><strong>结果</strong>：三视图整体完成度高，各角度细节一致。虽然头部特写和全身图之间有轻微重叠，但模型为AI视频和动画制作流程提供了足够的一致性参考。</p>

<h3>5. 复杂商业UI：蒸汽朋克手游主界面</h3>

<p><strong>提示词</strong>：生成一张蒸汽朋克世界观的完整商业级2D手游主界面。包含角色资源条、功能按钮、活动入口等UI元素，确保各组件视觉一致。</p>

<p><strong>结果</strong>：Seedream 5.0 Pro成功生成了视觉统一的蒸汽朋克界面，所有UI元素齐全。需要改进的地方包括偶有中文文字乱码和机械武器细节简化，但整体结果适合游戏美术、UI设计和开发参考。</p>

<h2 id="comparison">模型对比</h2>

<p>基于实战测试，Seedream 5.0 Pro在大多数场景下超越Nano Banana Pro。虽然在构图和稳定性上相比GPT Image 2仍有提升空间，但它已是全球顶级AI图像生成模型之一，巩固了其作为中国AI创新领导者的地位。</p>

<h2 id="conclusion">总结</h2>

<p>Seedream 5.0 Pro是一款强大实用的AI图像生成模型，在艺术细节、中文文字处理、简单提示词理解、专业工作流支持和复杂商业UI设计方面表现出色。无论你是设计师、开发者还是内容创作者，它都能为你的创意工作流提供有价值的助力。</p>

<h2>常见问题</h2>

<h3>Seedream 5.0 Pro和Midjourney比怎么样？</h3>
<p>各有所长。Midjourney擅长艺术构图、氛围光影和创意诠释——是概念艺术和情绪驱动作品的首选。Seedream 5.0 Pro的核心差异化是<strong>中文文字准确度</strong>和<strong>商业工作流支持</strong>。如果你需要带中文的海报，Midjourney大概率会把字搞乱。Seedream渲染正确。对于角色三视图和UI设计稿，Seedream的一致性已达到生产级别。纯艺术质量不含文字，Midjourney仍领先。中文商业设计，Seedream是更好的选择。</p>

<h3>¥0.3/千张的定价有竞争力吗？</h3>
<p>是的，非常有竞争力。约$0.04/千张（标准分辨率）或$0.08/千张（2K），Seedream是最实惠的专业级AI图像生成器之一。对比：Midjourney标准方案$10/月约200张（$0.05/张），DALL-E 3 API约$0.04-0.12/张。Seedream的单张成本低1-2个数量级，适合游戏素材生成、电商产品图、批量内容创作等高产量工作流。</p>

<h3>为什么第一次生成那么慢（2.5分钟）？</h3>
<p>这是新部署大模型的冷启动问题。首次请求时模型需要加载到GPU内存。后续生成通常快得多（30-60秒）。随着火山引擎优化基础设施和模型从部署阶段过渡到稳定生产，这应该会改善。批量工作时，连续生成图片比一次一张更高效——模型保持热加载状态，每张后续图片更快。</p>

<h3>Seedream 5.0 Pro能生成英文文字设计吗？</h3>
<p>可以，但中文文字才是它的招牌。英文文字渲染能力不错但测试和优化程度不如中文。对于英文为主的设计，GPT Image 2或DALL-E 3可能产生更精致的结果。Seedream的甜蜜点是双语或以中文为主的设计——你需要中文完美呈现。如果设计纯英文，两种都试试——结果可能让你惊喜，但别假设英文和中文一样完美。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>对Seedream感兴趣？探索更多AI图像和设计工具：</p>
  <ul>
    <li><a href="/articles/2025-ai-toolkit-practical-guide-every-domain">2025 AI工具箱：全领域实用指南</a> — 发现更多跨品类AI工具</li>
    <li><a href="/articles/ai-bubble-or-opportunity-guide-ordinary-people">AI是泡沫还是机遇？普通人应对AI浪潮的生存指南</a> — 了解字节跳动在AI格局中的角色</li>
    <li><a href="/articles/top-5-ai-ppt-skills-tested-ranked">AI PPT技能大比拼：5款工具实测排名与推荐</a> — 如果设计效率是你的关注点</li>
  </ul>
</div>`,
  },

  "official-tutorial-three-ways-codex-control-computer": {
    content: `<div class="meta-banner">
  <span class="meta-badge">🔧 AI Tools</span>
  <span class="meta-badge">🕒 6 min read</span>
  <span class="meta-badge">📅 Jul 9, 2026</span>
  <span class="meta-badge">🎯 Beginner</span>
</div>

<h2 id="introduction">Introduction</h2>

<p>Codex offers three distinct ways to control your computer and automate tasks. Which one is right for you? And what are their capabilities and limitations? Jason Liu, former Meta data scientist and current OpenAI Developer Experience Engineer, recently published a post explaining the use cases, features, and advantages of each method.</p>

<h2 id="computer-use">1. Computer Use</h2>

<p>Computer Use is currently the most powerful and versatile way for an agent to control a computer, and it is the key reason Codex stands out among other agent tools. It can simulate most operations on your computer, whether it's WeChat, Feishu, Excel, or video editing software. As long as the operation involves mouse clicks or keyboard input, it can generally handle it. It is available on both macOS and Windows, and can switch between different applications when a task involves multiple software programs.</p>

<p>Jason Liu shared a real example: once his package was stolen, but Amazon customer service had a 25-minute wait time. He instructed Codex to check the customer service window every five minutes, switch to checking every minute once the customer service representative connected, and then apply for a refund. When Jason returned from his shower, the refund had already been processed. This demonstrates the core strength of Computer Use: it can monitor windows and workflows, taking over tedious but necessary tasks.</p>

<p>However, it has a clear limitation: it is slow. Each step requires understanding the interface, locating the button, and then performing the click or input. This visual loop is time-consuming, so it is not suitable for tasks requiring extreme efficiency. But it is ideal for tasks that have no API, no plugins, and can only be completed through the graphical interface.</p>

<h2 id="chrome-extension">2. Codex Chrome Extension</h2>

<p>The Codex Chrome Extension is designed for tasks that primarily occur in the browser, especially those requiring a logged-in state, such as Feishu Docs, Taobao Merchant Backend, and Bilibili Creator Center. These tools rely on account status, and the extension can directly use your logged-in browser session to operate.</p>

<p>The key difference from Computer Use is that Computer Use simulates clicking buttons on the screen, while the Chrome Extension works directly within the browser workflow. It can read web content and switch between multiple tabs, for example, viewing data, comparing information, and compiling results. As a result, browser tasks using the Chrome Extension are usually faster, more accurate, and more efficient than using Computer Use.</p>

<p>Jason Liu uses it long-term to check private messages, browse news, collect feedback, and save valuable content to local files for easy access later. However, it has more sensitive permissions: since it uses your real logged-in state, websites will treat Codex's clicks, inputs, and submissions as your own actions. You can safely use it for information collection and content drafting, but you should personally confirm actions like sending messages or making payments.</p>

<h2 id="in-app-browser">3. In-App Browser</h2>

<p>The in-app browser is more suitable for developers, especially for web frontend development and local tool debugging. For example, when working on a frontend page, you can have Codex open the local preview address, check for layout issues, button misalignment, or mobile overflow. After reviewing, it can directly modify the code and then reopen the page for verification.</p>

<p>Its most valuable feature is that it connects code writing and result viewing. So the in-app browser is not for logging into websites; it is more like Codex's workspace for web development and interface debugging.</p>

<h2 id="how-to-choose">How to Choose?</h2>

<ul>
  <li>For website tasks requiring a logged-in state: use the <strong>Chrome Extension</strong>.</li>
  <li>For tasks involving desktop software or switching between multiple applications: use <strong>Computer Use</strong>.</li>
  <li>For web development, page preview, and interface debugging: use the <strong>in-app browser</strong>.</li>
</ul>

<p>Jason Liu also emphasized that if a task can be completed using plugins or MCP, you should prioritize using structured tools. For example, reading Feishu Docs or organizing online tables directly with plugins or interfaces is usually more accurate than having Codex simulate clicks in the interface.</p>

<p>In other words, Codex's computer control is not about being as human-like as possible, but about choosing the right entry point. A truly strong agent does not mindlessly click the mouse when given a task; it knows when to call an API, when to use the browser, and when to take over the desktop. This is the most notable change in Codex: it is no longer just a coding tool, but is evolving into a task execution system that revolves around computers, browsers, and local projects.</p>

<h2>常见问题</h2>

<h3>When should I use Computer Use vs. the Chrome Extension?</h3>
<p>The simple rule: if the task lives entirely in a browser tab, use the Chrome Extension. It's faster, more accurate, and uses your real logged-in session. If the task involves desktop apps (WeChat, Excel, video editors) or requires switching between multiple applications, use Computer Use. The Chrome Extension can't touch desktop software, and Computer Use is overkill for single-website tasks. Jason Liu's refund example is a great Computer Use case because it involved monitoring a browser window over time — something the Chrome Extension isn't designed for.</p>

<h3>Is Computer Use safe? Can it accidentally delete files or send messages?</h3>
<p>Codex's permission system gives you control. In "approve for me" mode (recommended), Codex asks for confirmation before any destructive action. For Computer Use specifically, you can see what it's doing on screen in real time. Jason Liu's advice: use it freely for information gathering and content drafting, but personally confirm actions like sending messages, making payments, or deleting files. The Chrome Extension has more sensitive permissions because it uses your real logged-in state — websites see its actions as yours. Treat it like giving a colleague access to your browser: great for research, risky for transactions.</p>

<h3>Can I use all three modes simultaneously?</h3>
<p>Yes, and that's the ideal workflow. A typical development session might look like: use the in-app browser to preview your frontend changes, use Computer Use to test the app in a real browser environment, and use the Chrome Extension to pull reference designs from Feishu Docs or Figma. The modes are complementary, not competing. The skill is knowing which entry point to use for each sub-task — this is what separates casual Codex users from power users.</p>

<h3>Do I need the Chrome Extension if I already have Computer Use?</h3>
<p>Yes, if you do a lot of browser-based work. Computer Use can technically control Chrome, but it does so by visually locating buttons and clicking them — which is slow and error-prone. The Chrome Extension works at the browser level, reading page structure directly and interacting with the DOM. For tasks like "check all my unread Feishu messages and summarize them," the Chrome Extension completes in seconds what might take Computer Use minutes. The extension is free and takes 2 minutes to install — there's no reason not to have both.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Mastered Codex's control modes? Level up your Codex workflow:</p>
  <ul>
    <li><a href="/articles/complete-guide-codex-zero-to-advanced">Complete Guide to Codex: From Zero to Advanced Development Workflow</a> — the full Codex mastery path</li>
    <li><a href="/articles/2026-ai-agent-guide-choose-right-tool-beginners">2026 AI Agent Guide: How to Choose the Right Tool for Beginners</a> — see why Codex ranks #1 among Agents</li>
    <li><a href="/articles/mastering-ai-workflow-beginner-custom-workbench">Mastering AI Workflow: Build Your Custom AI Workbench</a> — integrate Codex into a broader automation system</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">🔧 AI 工具</span>
  <span class="meta-badge">🕒 阅读约6分钟</span>
  <span class="meta-badge">📅 2026年7月9日</span>
  <span class="meta-badge">🎯 入门</span>
</div>

<h2 id="introduction">引言</h2>

<p>Codex提供三种不同的方式来控制你的电脑并自动化任务。哪种适合你？它们的能力和局限是什么？前Meta数据科学家、现OpenAI开发者体验工程师Jason Liu最近发布了一篇文章，详解每种方式的使用场景、特点和优势。</p>

<h2 id="computer-use">1. Computer Use</h2>

<p>Computer Use是目前Agent控制电脑最强大、最通用的方式，也是Codex在众多Agent工具中脱颖而出的关键原因。它可以模拟电脑上的大多数操作，无论是微信、飞书、Excel还是视频剪辑软件。只要操作涉及鼠标点击或键盘输入，它基本都能处理。它在macOS和Windows上均可使用，当任务涉及多个软件时可在不同应用间切换。</p>

<p>Jason Liu分享了一个真实案例：有一次他的快递被偷了，但亚马逊客服有25分钟的等待时间。他让Codex每五分钟检查一次客服窗口，一旦客服接通就改为每分钟检查一次，然后申请退款。等Jason洗完澡回来，退款已经处理完毕。这展示了Computer Use的核心优势：它可以监控窗口和工作流，接管繁琐但必要的任务。</p>

<p>但它有一个明显的局限：速度慢。每一步都需要理解界面、定位按钮，然后执行点击或输入。这个视觉循环很耗时，所以不适合要求极高效率的任务。但它非常适合那些没有API、没有插件、只能通过图形界面完成的任务。</p>

<h2 id="chrome-extension">2. Codex Chrome扩展</h2>

<p>Codex Chrome扩展专为主要发生在浏览器中的任务设计，特别是需要登录状态的任务，如飞书文档、淘宝商家后台、B站创作中心。这些工具依赖账号状态，扩展可以直接使用你已登录的浏览器会话来操作。</p>

<p>与Computer Use的关键区别在于：Computer Use模拟在屏幕上点击按钮，而Chrome扩展直接在浏览器工作流中运行。它可以读取网页内容并在多个标签页之间切换，例如查看数据、对比信息、汇总结果。因此，使用Chrome扩展的浏览器任务通常比Computer Use更快、更准确、更高效。</p>

<p>Jason Liu长期用它来查看私信、浏览新闻、收集反馈，并将有价值的内容保存到本地文件方便后续查阅。但它的权限更敏感：由于使用真实的登录状态，网站会将Codex的点击、输入和提交视为你本人的操作。信息收集和内容草拟可以放心使用，但发送消息或付款等操作应亲自确认。</p>

<h2 id="in-app-browser">3. 内置浏览器</h2>

<p>内置浏览器更适合开发者，特别是网页前端开发和本地工具调试。例如，在做前端页面时，你可以让Codex打开本地预览地址，检查布局问题、按钮错位或移动端溢出。审查后，它可以直接修改代码，然后重新打开页面验证。</p>

<p>它最有价值的功能是将代码编写和结果查看连接起来。所以内置浏览器不是用来登录网站的；它更像是Codex进行网页开发和界面调试的工作区。</p>

<h2 id="how-to-choose">如何选择？</h2>

<ul>
  <li>需要登录状态的网站任务：用<strong>Chrome扩展</strong>。</li>
  <li>涉及桌面软件或多应用切换的任务：用<strong>Computer Use</strong>。</li>
  <li>网页开发、页面预览和界面调试：用<strong>内置浏览器</strong>。</li>
</ul>

<p>Jason Liu还强调，如果任务可以通过插件或MCP完成，应优先使用结构化工具。例如，直接用插件或接口读取飞书文档、整理在线表格，通常比让Codex在界面中模拟点击更准确。</p>

<p>换句话说，Codex的电脑控制不是追求越像人越好，而是选择正确的入口。真正强大的Agent不是接到任务就盲目点击鼠标；它知道什么时候调用API，什么时候用浏览器，什么时候接管桌面。这是Codex最显著的变化：它不再只是一个编码工具，而是正演变成一个围绕电脑、浏览器和本地项目的任务执行系统。</p>

<h2>常见问题</h2>

<h3>什么时候用Computer Use，什么时候用Chrome扩展？</h3>
<p>简单规则：如果任务完全在浏览器标签页中，用Chrome扩展。它更快、更准确，使用真实登录会话。如果任务涉及桌面应用（微信、Excel、视频编辑器）或需要在多个应用间切换，用Computer Use。Chrome扩展碰不到桌面软件，Computer Use对单网站任务又太小题大做。Jason Liu的退款案例是典型的Computer Use场景——涉及长时间监控浏览器窗口，Chrome扩展不是为此设计的。</p>

<h3>Computer Use安全吗？会不会误删文件或发送消息？</h3>
<p>Codex的权限系统让你掌控。在"approve for me"模式下（推荐），Codex在执行任何破坏性操作前都会请求确认。Computer Use具体来说，你可以实时看到屏幕上它在做什么。Jason Liu的建议：信息收集和内容草拟放心用，但发送消息、付款或删除文件等操作亲自确认。Chrome扩展的权限更敏感，因为使用真实登录状态——网站会把它的操作视为你的操作。把它当作让同事访问你的浏览器：研究没问题，交易有风险。</p>

<h3>三种模式能同时使用吗？</h3>
<p>可以，而且这正是理想的工作流。一个典型的开发会话可能是：用内置浏览器预览前端改动，用Computer Use在真实浏览器环境中测试应用，用Chrome扩展从飞书文档或Figma拉取参考设计。三种模式互补而非竞争。关键是知道每个子任务该用哪个入口——这是区分Codex普通用户和高级用户的分水岭。</p>

<h3>有了Computer Use还需要Chrome扩展吗？</h3>
<p>需要，如果你做大量浏览器工作的话。Computer Use技术上也能控制Chrome，但它通过视觉定位按钮然后点击——慢且易出错。Chrome扩展在浏览器层面工作，直接读取页面结构、与DOM交互。像"检查所有未读飞书消息并汇总"这样的任务，Chrome扩展几秒就能完成，Computer Use可能要几分钟。扩展免费，安装只需2分钟——没有理由不两个都装。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>掌握了Codex的控制模式？升级你的Codex工作流：</p>
  <ul>
    <li><a href="/articles/complete-guide-codex-zero-to-advanced">Codex完全指南：从零基础到高级开发工作流</a> — Codex完整掌握路径</li>
    <li><a href="/articles/2026-ai-agent-guide-choose-right-tool-beginners">2026 AI Agent选型指南：新手如何选择最适合的工具</a> — 了解Codex为何排名第一</li>
    <li><a href="/articles/mastering-ai-workflow-beginner-custom-workbench">掌握AI工作流：打造你的专属AI工作台</a> — 将Codex集成到更广泛的自动化系统</li>
  </ul>
</div>`,
  },

'''

last_brace = content_src.rfind('};')
content_new = content_src[:last_brace] + new_contents + '};'

with open('src/lib/article-content.ts', 'w', encoding='utf-8') as f:
    f.write(content_new)

print('Part 3: 2 article contents added to article-content.ts')

print('\n=== All done! Run build to verify ===')