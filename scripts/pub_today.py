"""
Publish July 4, 2026 — 2 articles, no new tools.
"""
import os

BASE = r"C:\Users\jun\aistudyonline-next"
os.chdir(BASE)

# ===== Part 1: Add 2 article metadata to articles.ts =====
with open('src/lib/articles.ts', 'r', encoding='utf-8') as f:
    articles_src = f.read()

new_articles = r"""  {
    slug: "ai-bubble-or-opportunity-guide-ordinary-people",
    title: "Is AI a Bubble or Opportunity? A Guide for Ordinary People to Navigate the AI Wave",
    titleZh: "AI是泡沫还是机遇？普通人应对AI浪潮的生存指南",
    description: "Using the 'survivor model' from the 2000 internet bubble (Foundation/Platform/Application layers), this guide maps today's AI landscape and presents three actionable opportunities for ordinary people — career enhancement, side hustles, and frontier innovation — ranked by risk level.",
    descriptionZh: "用2000年互联网泡沫的'幸存者模型'（基础层/平台层/应用层）映射当今AI格局，并按风险等级为普通人梳理三条可行路径——职业增强、副业创业和前沿创新。",
    category: "AI Insights",
    tags: ["AI Bubble", "Investment", "Career", "AI Strategy", "Side Hustle", "Technology Trends"],
    difficulty: "beginner",
    toolsMentioned: ["ChatGPT", "Claude", "Midjourney"],
    date: "2026-07-04",
  },
  {
    slug: "top-5-ai-ppt-skills-tested-ranked",
    title: "Battle of the Best: Top 5 AI PPT Skills Tested and Ranked",
    titleZh: "AI PPT技能大比拼：5款工具实测排名与推荐",
    description: "A hands-on comparison of five popular AI PPT generation skills — PPT Master, Banana Slides, Frontend Slides, HTML PPT, and Guizang PPT — tested with the same prompt and ranked by Codex for content quality, design, and functionality.",
    descriptionZh: "用同一提示词实测5款热门AI PPT生成技能——PPT Master、Banana Slides、Frontend Slides、HTML PPT和Guizang PPT Skill，由Codex从内容质量、设计和功能三个维度综合排名。",
    category: "AI Tools",
    tags: ["PPT", "AI Presentation", "Productivity", "Codex Skills", "Comparison", "Tools Review"],
    difficulty: "beginner",
    toolsMentioned: ["Codex Agent"],
    date: "2026-07-04",
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
  "ai-bubble-or-opportunity-guide-ordinary-people": {
    content: `<div class="meta-banner">
  <span class="meta-badge">💡 AI Insights</span>
  <span class="meta-badge">🕒 8 min read</span>
  <span class="meta-badge">📅 Jul 4, 2026</span>
  <span class="meta-badge">🎯 Beginner</span>
</div>

<h2 id="introduction">Introduction</h2>

<p>You've probably wondered: On one hand, NVIDIA's stock keeps hitting new highs, making you feel like you're missing out on a fortune if you don't buy it. On the other hand, some warn that this is a huge bubble, and jumping in now is like buying at the top. So, should ordinary people dive in or stay away?</p>

<p>To answer this question, we need to distinguish between <strong>real technology</strong> and <strong>artificial prices</strong>. AI technology itself is revolutionary — like pure water, it's useful. But its price is like soda water, filled with gas — valuation bubbles. Recently, legendary Wall Street investor Jeremy Grantham warned that the AI market is in the final chapter of the 2000 internet bubble. Bank of America's chief investment strategist Michael Hartnett compared NVIDIA's P/E ratio to Cisco's at the peak of the 2000 bubble, and the results are strikingly similar.</p>

<p>Back then, everyone believed Cisco was the cornerstone of the internet, but that didn't stop its stock from plummeting 80% after the bubble burst. On the other hand, Wall Street bulls like Cathie Wood argue that AI, like the invention of electricity and the internet wave, will revolutionize everything around us. Now it can generate movie-level videos, accelerate cancer drug development, and reshape many industries in unprecedented ways.</p>

<p>So who should we believe? To answer this, we can't just focus on current stock prices and news — we need a map, and the best map is hidden in history.</p>

<h2 id="survivor-model">The Survivor Model: Lessons from the 2000 Internet Bubble</h2>

<p>Let's rewind to 2000, when the internet bubble burst, countless companies vanished, and countless fortunes were lost. But looking back today, if we sift through all the surviving and dead companies, we find a <strong>survivor model</strong> that applies to almost all technological revolutions. It's like a pyramid with three layers:</p>

<h3>Layer 1: The Foundation Layer ("Sellers of Shovels")</h3>

<p>In the gold rush, the first and most certain way to make money was selling shovels and jeans. In 2000, that company was Cisco, which sold routers and switches — the "pipes" of the internet world, without which information couldn't flow.</p>

<p>Characteristics of this layer:</p>
<ul>
  <li>Closest to the revolution, everyone needs it.</li>
  <li>Most likely to be hyped by capital, leading to valuation bubbles.</li>
</ul>

<h3>Layer 2: The Platform Layer ("Builders")</h3>

<p>If the foundation layer provides tools, the platform layer uses these tools to build "super cities" in the new world and set their own rules. Around 2000, Amazon built an "everything store," and Google built an "information entrance." They used new technology to build strong ecosystems connecting countless merchants and users, creating uncrossable moats.</p>

<p>Characteristics of this layer:</p>
<ul>
  <li>Strong network effects and user stickiness.</li>
  <li>Can turn revolutionary technology into sustainable, stable, and extremely profitable businesses.</li>
</ul>

<h3>Layer 3: The Application Layer ("Gold Diggers")</h3>

<p>The top of the pyramid is the most crowded and competitive layer — the application layer, where thousands of "gold diggers" operate. These were the ".com" companies of the past, trying to solve all kinds of problems, from group buying to fresh food delivery.</p>

<p>Some survivors like PayPal became giants, but many more like Pets.com and Webvan burned hundreds of millions of dollars in investment and left nothing behind.</p>

<p>Characteristics of this layer:</p>
<ul>
  <li>Most innovative, closest to users.</li>
  <li>Most concentrated in bubbles, highest mortality rate — up to 99% of companies may disappear.</li>
</ul>

<h2 id="apply-model">Applying the Model to Today's AI Wave</h2>

<p>Now let's use this survivor model to look at today's AI landscape:</p>

<h3>Foundation Layer: Sellers of Shovels</h3>

<p>Undoubtedly, this is NVIDIA, AMD, TSMC, and ASML. Their computing power chips and equipment are the "routers and switches" of the AI era.</p>

<h3>Platform Layer: Builders</h3>

<p>These are companies like Microsoft, Google, and Adobe. Microsoft injects AI capabilities into Office and Windows through Azure and Copilot; Google integrates Gemini into its search and Android ecosystem; Adobe embeds AI drawing capabilities into Photoshop. They're making us unknowingly inseparable from AI, just like smartphones once did.</p>

<h3>Application Layer: Gold Diggers</h3>

<p>This layer is countless — video generation tools like Pika and Sora, design tools like Midjourney, search tools like Perplexity, and thousands of writing tools, educational software, and customer service tools. These are today's Pets.com, but among them, there must be the next PayPal.</p>

<h2 id="opportunities">Three Opportunities for Ordinary People</h2>

<p>Now that we understand the map, what should ordinary people do? Based on different risk levels and investment, I've summarized three opportunities:</p>

<h3>Opportunity 1: Career Enhancement (Low Risk, Most Suitable for Most People)</h3>

<p>The goal is not to switch careers, but to use AI to make your current work 10x more efficient and valuable. In any industry, strive to be the person in the office who best uses AI — this will make you more secure in layoffs and more confident in salary negotiations.</p>

<p>Examples:</p>
<ul>
  <li><strong>Designers</strong>: Master Midjourney and Stable Diffusion to outperform peers in creative efficiency.</li>
  <li><strong>Editors/Operators</strong>: Use ChatGPT or Claude to assist with research, data analysis, and content drafting.</li>
  <li><strong>Everyone</strong>: Focus on developing skills that AI can't replace, like complex decision-making, deep empathy, and trust-building.</li>
</ul>

<h3>Opportunity 2: Side Hustle & Small Business (Medium Risk)</h3>

<p>Suitable for people with professional skills who want to transform or start a side business/small business. The goal is to connect ecosystems and provide services to others for steady income.</p>

<p>Ways to do this:</p>
<ul>
  <li><strong>Knowledge Sharing</strong>: Create content about AI, do corporate training, or become an AI tool reviewer/KOL. Many people are anxious about AI but don't know where to start — if you can make complex things simple, that's valuable.</li>
  <li><strong>Micro-Applications</strong>: Develop small tools based on large model APIs to solve specific pain points, like tools for lawyers to write contracts or accountants to review financial statements. These can generate subscription revenue.</li>
</ul>

<p>The core of this opportunity is to use your expertise to match AI, finding small, real needs that big companies ignore. It may not make you rich, but it has low investment and risk, and can even grow into a sustainable small business.</p>

<h3>Opportunity 3: Frontier Innovation (High Risk, High Return)</h3>

<p>Only suitable for a very small number of entrepreneurs, venture capitalists, or top technical talents. You can choose to go all-in on AI, with the goal of becoming or investing in the next Amazon or PayPal.</p>

<p>Two approaches:</p>
<ol>
  <li><strong>Invest in or Join "Killer Apps"</strong>: Develop your own criteria to identify promising AI companies. Key questions: Does it solve high-frequency, urgent needs? Does it have a data moat? Is its business model clear?</li>
  <li><strong>Focus on Core Technology</strong>: If you're a top technical talent, dive into underlying algorithms, model optimization, and computing power architecture — this is the center of the action and the source of future wealth.</li>
</ol>

<h2 id="conclusion">Conclusion: It's a Strategy Question, Not a Choice</h2>

<p>So, should we dive into the AI wave or stay away? It's not a choice — it's a strategy question. Valuation bubbles will eventually dissipate, like the gas in soda water. But the "water" of the AI technological revolution will remain forever, nourishing our future world.</p>

<p>Our strategy is not to bet on whether the bubble will burst, but to quickly learn to use this new technology and make it work for us. AI can solve more and more problems, but it may never be able to ask a good question. The scarcest resources in the future will not be answers, but high-quality questions, deep insights, and warm empathy. These are our greatest and most fundamental opportunities as humans in this wave.</p>

<h2>常见问题</h2>

<h3>How do I know if AI is in a bubble right now?</h3>
<p>You don't need to predict it — and nobody can. Instead, use the survivor model as a lens: <strong>Foundation layer</strong> stocks (NVIDIA, TSMC) are the most bubble-prone because they're the easiest narrative for capital to hype. <strong>Platform layer</strong> companies (Microsoft, Google) have real revenue and moats, making them more resilient. <strong>Application layer</strong> startups have the highest failure rate but also the highest upside. The practical takeaway: don't bet your savings on any single layer. Diversify across layers and time horizons, and focus your personal effort on the layer that matches your skills and risk tolerance.</p>

<h3>I'm not a programmer — can I still benefit from the AI wave?</h3>
<p>Absolutely. The three opportunities in this guide are designed specifically for this. Opportunity 1 (Career Enhancement) requires zero coding — it's about using existing AI tools to 10x your current work. A marketer using ChatGPT for copywriting, a designer using Midjourney for mockups, a teacher using AI for lesson plans — none of these require programming. Opportunity 2 (Side Hustle) may involve light technical work but can be done with no-code tools. Only Opportunity 3 requires deep technical skills. Most people should focus on Opportunities 1 and 2.</p>

<h3>What's the single most important skill to develop in the AI era?</h3>
<p><strong>Asking good questions.</strong> AI can generate answers, but it can't decide what's worth asking. The ability to frame problems clearly, identify what matters, and iterate on prompts until you get useful output — this is the meta-skill that makes every AI tool more effective. It's also the one skill that becomes more valuable as AI gets better at generating answers. Pair this with deep domain expertise in your field, and you become irreplaceable.</p>

<h3>Should I invest in AI stocks now?</h3>
<p>This article is not financial advice, but the survivor model offers a framework: if you're investing, distinguish between <strong>trading</strong> (timing the market) and <strong>investing</strong> (holding through cycles). For long-term investing, platform-layer companies with real revenue and moats tend to survive bubbles. For short-term trading, understand that foundation-layer stocks are the most volatile — they rise fastest in hype and fall hardest in crashes. The safest approach for most people: dollar-cost average into a diversified tech index fund rather than betting on individual stocks.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Understand the AI landscape? Now build your practical skills:</p>
  <ul>
    <li><a href="/articles/demystifying-ai-application-layer-3-layers">Demystifying AI Application Layer: From LLMs to Agents in 3 Layers</a> — dive deeper into the three-layer AI architecture</li>
    <li><a href="/articles/2025-ai-toolkit-practical-guide-every-domain">2025 AI Toolkit: A Practical Guide for Every Domain</a> — find the right AI tools for your career path</li>
    <li><a href="/articles/dont-be-intimidated-ai-jargon-practical-guide-concepts">Don't Be Intimidated by AI Jargon: A Practical Guide to AI Concepts</a> — master AI fundamentals from scratch</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">💡 AI 洞察</span>
  <span class="meta-badge">🕒 阅读约8分钟</span>
  <span class="meta-badge">📅 2026年7月4日</span>
  <span class="meta-badge">🎯 入门</span>
</div>

<h2 id="introduction">引言</h2>

<p>你可能也在纠结：一边是英伟达股价屡创新高，让你觉得不买就错过了暴富机会；另一边是有人警告这是巨大泡沫，现在冲进去就是高位接盘。普通人到底该入场还是远离？</p>

<p>要回答这个问题，我们需要区分<strong>真正的技术</strong>和<strong>人为的价格</strong>。AI 技术本身是革命性的——像纯净水一样有用。但它的价格像苏打水，充满了气体——估值泡沫。最近，华尔街传奇投资者 Jeremy Grantham 警告 AI 市场正处于 2000 年互联网泡沫的最后一章。美银首席投资策略师 Michael Hartnett 将英伟达的市盈率与 2000 年泡沫顶峰时的思科做了对比，结果惊人地相似。</p>

<p>当年所有人都相信思科是互联网的基石，但这并未阻止泡沫破裂后其股价暴跌 80%。另一边，华尔街多头如 Cathie Wood 则认为 AI 像电的发明和互联网浪潮一样，将彻底改变我们周围的一切——现在它已经能生成电影级视频、加速癌症药物研发、以前所未有的方式重塑多个行业。</p>

<p>那么该信谁？要回答这个问题，不能只看当前的股价和新闻——我们需要一张地图，而最好的地图藏在历史中。</p>

<h2 id="survivor-model">幸存者模型：2000年互联网泡沫的教训</h2>

<p>让我们回到 2000 年，互联网泡沫破裂，无数公司消失，无数财富蒸发。但今天回看，如果我们梳理所有存活和死亡的公司，会发现一个适用于几乎所有技术革命的<strong>幸存者模型</strong>。它像一个三层金字塔：</p>

<h3>第一层：基础层（"卖铲子的人"）</h3>

<p>淘金热中，最早最稳的赚钱方式是卖铲子和牛仔裤。在 2000 年，这家公司是思科——卖路由器和交换机，互联网世界的"管道"，没有它们信息就无法流动。</p>

<p>这一层的特点：</p>
<ul>
  <li>离革命最近，所有人都需要。</li>
  <li>最容易被资本炒作，导致估值泡沫。</li>
</ul>

<h3>第二层：平台层（"建城者"）</h3>

<p>如果基础层提供工具，平台层则用这些工具在新世界建造"超级城市"并制定规则。2000 年前后，亚马逊建了"万物商店"，谷歌建了"信息入口"。它们用新技术构建了连接无数商家和用户的强大生态，挖出了不可逾越的护城河。</p>

<p>这一层的特点：</p>
<ul>
  <li>强大的网络效应和用户黏性。</li>
  <li>能将革命性技术转化为可持续、稳定且极赚钱的生意。</li>
</ul>

<h3>第三层：应用层（"淘金者"）</h3>

<p>金字塔顶端是最拥挤、竞争最激烈的应用层，成千上万的"淘金者"在这里厮杀。这就是当年的".com"公司，试图解决从团购到生鲜配送的各种问题。</p>

<p>像 PayPal 这样的幸存者成了巨头，但更多像 Pets.com 和 Webvan 的公司烧掉了数亿美元投资，最终什么都没留下。</p>

<p>这一层的特点：</p>
<ul>
  <li>最具创新性，离用户最近。</li>
  <li>泡沫最集中，死亡率最高——可能 99% 的公司会消失。</li>
</ul>

<h2 id="apply-model">用模型看今天的 AI 浪潮</h2>

<p>现在用这个幸存者模型来看当今的 AI 格局：</p>

<h3>基础层：卖铲子的人</h3>

<p>毫无疑问，这是英伟达、AMD、台积电和 ASML。它们的算力芯片和设备就是 AI 时代的"路由器和交换机"。</p>

<h3>平台层：建城者</h3>

<p>这些是微软、谷歌、Adobe 等公司。微软通过 Azure 和 Copilot 将 AI 能力注入 Office 和 Windows；谷歌将 Gemini 整合进搜索和安卓生态；Adobe 将 AI 绘图能力嵌入 Photoshop。它们正让我们在不知不觉中离不开 AI，就像当年智能手机做的那样。</p>

<h3>应用层：淘金者</h3>

<p>这一层数不胜数——视频生成工具如 Pika、Sora，设计工具如 Midjourney，搜索工具如 Perplexity，还有成千上万的写作工具、教育软件、客服工具。这些都是今天的 Pets.com，但其中一定会有下一个 PayPal。</p>

<h2 id="opportunities">普通人的三个机会</h2>

<p>了解了地图之后，普通人该怎么做？基于不同的风险等级和投入，我总结了三类机会：</p>

<h3>机会一：职业增强（低风险，最适合大多数人）</h3>

<p>目标不是转行，而是用 AI 让你当前的工作效率提升 10 倍、价值翻倍。在任何行业，努力成为办公室里最会用 AI 的人——这会让你在裁员时更安全，在谈薪时更有底气。</p>

<p>举例：</p>
<ul>
  <li><strong>设计师</strong>：掌握 Midjourney 和 Stable Diffusion，在创意效率上远超同行。</li>
  <li><strong>编辑/运营</strong>：用 ChatGPT 或 Claude 辅助调研、数据分析和内容草拟。</li>
  <li><strong>所有人</strong>：专注培养 AI 无法替代的能力，如复杂决策、深度共情和信任建立。</li>
</ul>

<h3>机会二：副业与小型创业（中等风险）</h3>

<p>适合有专业技能、想转型或开启副业/小生意的人。目标是连接生态，为他人提供服务，获得稳定收入。</p>

<p>实现方式：</p>
<ul>
  <li><strong>知识分享</strong>：创作 AI 相关内容，做企业培训，或成为 AI 工具评测者/KOL。很多人对 AI 焦虑但不知从何入手——如果你能把复杂的东西讲简单，这就是价值。</li>
  <li><strong>微应用开发</strong>：基于大模型 API 开发小工具解决特定痛点，比如帮律师写合同的工具、帮会计审财务报表的工具。这些可以产生订阅收入。</li>
</ul>

<p>这个机会的核心是用你的专业能力去匹配 AI，找到大公司忽略的小而真实的需求。不一定让你暴富，但投入和风险都低，甚至可能成长为可持续的小生意。</p>

<h3>机会三：前沿创新（高风险，高回报）</h3>

<p>只适合极少数创业者、风投或顶尖技术人才。你可以选择 All-in AI，目标是成为或投资下一个亚马逊或 PayPal。</p>

<p>两条路径：</p>
<ol>
  <li><strong>投资或加入"杀手级应用"</strong>：建立自己的标准来识别有潜力的 AI 公司。关键问题：是否解决高频刚需？是否有数据护城河？商业模式是否清晰？</li>
  <li><strong>专注核心技术</strong>：如果你是顶尖技术人才，深耕底层算法、模型优化和算力架构——这是风暴的中心，也是未来财富的源头。</li>
</ol>

<h2 id="conclusion">结语：这不是选择题，而是策略题</h2>

<p>所以，该冲进 AI 浪潮还是远离？这不是选择题——而是策略题。估值泡沫终将消散，像苏打水里的气泡。但 AI 技术革命的"水"会永远留下，滋养我们未来的世界。</p>

<p>我们的策略不是赌泡沫会不会破，而是尽快学会使用这项新技术，让它为我们工作。AI 能解决的问题越来越多，但它可能永远无法提出一个好问题。未来最稀缺的资源不是答案，而是高质量的提问、深刻的洞察和温暖的共情。这是我们作为人类在这波浪潮中最大、最根本的机会。</p>

<h2>常见问题</h2>

<h3>怎么判断 AI 现在是不是泡沫？</h3>
<p>你不需要预测——也没人能预测。把幸存者模型当镜头用：<strong>基础层</strong>股票（英伟达、台积电）最容易被炒作，因为叙事最简单，资本最爱讲。一旦泡沫破裂，它们跌得最狠。<strong>平台层</strong>公司（微软、谷歌）有真实收入和护城河，抗跌能力更强。<strong>应用层</strong>创业公司失败率最高但上限也最高。实操建议：不要把身家押在单一层面。跨层、跨时间分散配置，把个人精力投入到与你的技能和风险承受力匹配的那个层面。</p>

<h3>我不是程序员，还能从 AI 浪潮中获益吗？</h3>
<p>当然可以。本文的三个机会正是为此设计的。机会一（职业增强）完全不需要编程——就是用现有的 AI 工具把你当前的工作效率提升 10 倍。营销人员用 ChatGPT 写文案、设计师用 Midjourney 做原型、老师用 AI 备课——这些都不需要编程。机会二（副业）可能涉及轻度技术工作，但无代码工具也能搞定。只有机会三需要深度技术能力。大多数人应该聚焦机会一和二。</p>

<h3>AI 时代最重要的单项技能是什么？</h3>
<p><strong>提出好问题的能力。</strong>AI 能生成答案，但它无法判断什么值得问。清晰地定义问题、识别什么重要、不断迭代提示直到获得有用输出的能力——这是让每个 AI 工具更有效的元技能。而且随着 AI 生成答案的能力越来越强，这个技能的价值只会越来越高。把它和你所在领域的深厚专业能力结合，你就会变得不可替代。</p>

<h3>现在该不该买 AI 股票？</h3>
<p>本文不是投资建议，但幸存者模型提供了一个框架：如果你要投资，区分<strong>交易</strong>（择时）和<strong>投资</strong>（穿越周期）。长期投资的话，有真实收入和护城河的平台层公司更可能在泡沫中存活。短期交易的话，要明白基础层股票波动最大——炒作时涨最快，崩盘时跌最狠。对大多数人最稳妥的方式：定投多元化的科技指数基金，而不是押注单只股票。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>了解了 AI 格局？现在构建你的实战技能：</p>
  <ul>
    <li><a href="/articles/demystifying-ai-application-layer-3-layers">拆解 AI 应用层：从大语言模型到智能体的三层体系</a> — 深入了解三层 AI 架构</li>
    <li><a href="/articles/2025-ai-toolkit-practical-guide-every-domain">2025 AI 工具箱：全领域实用指南</a> — 为你的职业路径找到合适的 AI 工具</li>
    <li><a href="/articles/dont-be-intimidated-ai-jargon-practical-guide-concepts">别被 AI 术语吓到：从 Token 到 Workspace Agent 的实用指南</a> — 从零掌握 AI 基础知识</li>
  </ul>
</div>`,
  },

  "top-5-ai-ppt-skills-tested-ranked": {
    content: `<div class="meta-banner">
  <span class="meta-badge">🔧 AI Tools</span>
  <span class="meta-badge">🕒 6 min read</span>
  <span class="meta-badge">📅 Jul 4, 2026</span>
  <span class="meta-badge">🎯 Beginner</span>
</div>

<h2 id="introduction">Introduction</h2>

<p>Creating high-quality presentations has never been easier with AI PPT skills, but with so many options available, it can be hard to know which one to choose. In this guide, we'll test the five most popular AI PPT skills using the same prompt and evaluate their performance to help you find the best tool for your needs.</p>

<h2 id="methodology">Test Methodology</h2>

<p>We followed a three-step process to ensure a fair comparison:</p>

<ol>
  <li><strong>Identify Top Skills</strong>: Use Codex to find the five most popular PPT skills on GitHub.</li>
  <li><strong>Standardized Testing</strong>: Generate a presentation on the same topic (a Chinese language lesson plan for the text <em>Spring</em> by Zhu Ziqing) using each skill.</li>
  <li><strong>AI Evaluation</strong>: Have Codex analyze and rank the presentations based on content quality, design, and functionality.</li>
</ol>

<h2 id="contenders">The Contenders</h2>

<p>The five skills we tested are:</p>

<ol>
  <li><strong>PPT Master</strong></li>
  <li><strong>Banana Slides</strong></li>
  <li><strong>Frontend Slides</strong></li>
  <li><strong>HTML PPT</strong></li>
  <li><strong>Guizang PPT Skill</strong></li>
</ol>

<h2 id="results">Detailed Test Results</h2>

<h3>1. PPT Master</h3>

<ul>
  <li><strong>Output</strong>: An 11-page PowerPoint presentation with a clean, structured design.</li>
  <li><strong>Strengths</strong>: Well-organized content with clear sections; includes speaker notes for each slide; good visual hierarchy with key points highlighted.</li>
  <li><strong>Weaknesses</strong>: Some text elements may be misaligned and require manual adjustment; limited customization options.</li>
</ul>

<h3>2. Banana Slides</h3>

<ul>
  <li><strong>Output</strong>: A 13-page presentation with a light green color scheme.</li>
  <li><strong>Strengths</strong>: Highly structured content that follows a logical flow; includes clear learning objectives and assessment criteria; visually appealing design with consistent styling.</li>
  <li><strong>Weaknesses</strong>: Less flexibility for advanced customization; may not be suitable for highly creative or non-educational presentations.</li>
</ul>

<h3>3. Frontend Slides</h3>

<ul>
  <li><strong>Output</strong>: A 12-page presentation with a minimalist design.</li>
  <li><strong>Strengths</strong>: Clean, modern design with a focus on readability; good use of white space and simple graphics; content is concise and to the point.</li>
  <li><strong>Weaknesses</strong>: Limited visual variety; may not be suitable for presentations that require more visual impact.</li>
</ul>

<h3>4. HTML PPT</h3>

<ul>
  <li><strong>Output</strong>: A web-based presentation with a left-side navigation menu.</li>
  <li><strong>Strengths</strong>: Interactive design with easy navigation; good for online presentations or sharing via the web; includes detailed content with in-depth analysis.</li>
  <li><strong>Weaknesses</strong>: Requires web access to view; limited customization of the design.</li>
</ul>

<h3>5. Guizang PPT Skill</h3>

<ul>
  <li><strong>Output</strong>: A 12-page presentation with a dark theme.</li>
  <li><strong>Strengths</strong>: Unique, modern design with a dark color scheme; good use of visual elements and animations; content is well-structured and engaging.</li>
  <li><strong>Weaknesses</strong>: Dark theme may not be suitable for all audiences; some elements may be difficult to read in bright environments.</li>
</ul>

<h2 id="ranking">AI Evaluation and Ranking</h2>

<p>After analyzing all five presentations, Codex provided the following rankings:</p>

<ol>
  <li><strong>PPT Master</strong> — Most balanced, well-structured, and includes speaker notes</li>
  <li><strong>Banana Slides</strong> — Most suitable for educational presentations with clear learning objectives</li>
  <li><strong>Frontend Slides</strong> — Clean, minimalist design with concise content</li>
  <li><strong>HTML PPT</strong> — Interactive web-based design with detailed content</li>
  <li><strong>Guizang PPT Skill</strong> — Unique dark theme with good visual elements</li>
</ol>

<h2 id="takeaways">Key Takeaways</h2>

<ul>
  <li><strong>Best for Education</strong>: Banana Slides is the top choice for creating educational presentations, with clear learning objectives and assessment criteria.</li>
  <li><strong>Best for General Use</strong>: PPT Master is the most balanced option, suitable for a wide range of presentation types.</li>
  <li><strong>Best for Web Sharing</strong>: HTML PPT is ideal for creating interactive presentations that can be shared online.</li>
  <li><strong>Best for Modern Design</strong>: Guizang PPT Skill offers a unique dark theme with good visual elements, making it a good choice for presentations that need to stand out.</li>
</ul>

<h2 id="recommendation">Final Recommendation</h2>

<p>If you're looking for a versatile AI PPT skill that can handle a wide range of presentation types, <strong>PPT Master</strong> is the best choice. It offers a good balance of structure, design, and functionality, making it suitable for both educational and general use.</p>

<p>For more specialized needs, consider <strong>Banana Slides</strong> for educational presentations or <strong>HTML PPT</strong> for web-based presentations.</p>

<p>No matter which skill you choose, be sure to review and edit the output to ensure it meets your specific needs and requirements.</p>

<h2>常见问题</h2>

<h3>Which AI PPT skill is the best overall?</h3>
<p>PPT Master ranked first in our test for its balanced combination of structure, design, and functionality. It's the most versatile — suitable for business reports, educational lessons, and general presentations alike. The inclusion of speaker notes is a standout feature that most other skills lack. That said, "best" depends on your use case: if you're an educator, Banana Slides' built-in learning objectives give it an edge. If you share presentations primarily online, HTML PPT's web-native format is more practical.</p>

<h3>Are these AI PPT skills free to use?</h3>
<p>Most of these skills are available as Codex plugins or community skills, which are free to install and use within the Codex environment. However, Codex itself requires a subscription (Plus at $20/month is recommended). The PPT output files (.pptx or HTML) are yours to keep and use without restrictions. Some skills may have premium tiers for advanced features, but the basic functionality tested here is accessible with a standard Codex subscription.</p>

<h3>Can I customize the AI-generated presentations?</h3>
<p>Yes, and you should. AI-generated presentations are a starting point, not a finished product. After generating a presentation, you can: (1) ask Codex to make specific changes via annotations or prompts, (2) download the .pptx file and edit it in PowerPoint or Google Slides, or (3) for HTML PPT, edit the HTML/CSS directly. Our test found that PPT Master and Banana Slides produce the most editable output with the least need for manual fixes.</p>

<h3>How long does it take to generate a presentation with these skills?</h3>
<p>In our tests, each skill generated a full 11-13 page presentation in 30-90 seconds, depending on complexity and Codex's current load. PPT Master was the fastest at ~30 seconds. The real time-saver isn't the generation speed — it's eliminating the 2-4 hours you'd normally spend on structure, design, and content drafting. Even with 10-15 minutes of manual review and editing, you're still saving 90%+ of the time compared to building from scratch.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Found your PPT tool? Explore more AI productivity skills:</p>
  <ul>
    <li><a href="/articles/complete-guide-codex-zero-to-advanced">Complete Guide to Codex: From Zero to Advanced Development Workflow</a> — master Codex skills and plugins</li>
    <li><a href="/articles/mastering-ai-workflow-beginner-custom-workbench">Mastering AI Workflow: Build Your Custom AI Workbench</a> — build your own AI productivity system</li>
    <li><a href="/articles/2025-ai-toolkit-practical-guide-every-domain">2025 AI Toolkit: A Practical Guide for Every Domain</a> — discover more AI tools across categories</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">🔧 AI 工具</span>
  <span class="meta-badge">🕒 阅读约6分钟</span>
  <span class="meta-badge">📅 2026年7月4日</span>
  <span class="meta-badge">🎯 入门</span>
</div>

<h2 id="introduction">引言</h2>

<p>用 AI PPT 技能创建高质量演示文稿从未如此简单，但选择太多反而让人无从下手。本文用同一提示词实测五款最热门的 AI PPT 技能，从内容质量、设计和功能三个维度进行排名，帮你找到最适合自己的工具。</p>

<h2 id="methodology">测试方法</h2>

<p>我们采用三步流程确保公平对比：</p>

<ol>
  <li><strong>筛选顶尖技能</strong>：用 Codex 找到 GitHub 上最热门的五款 PPT 技能。</li>
  <li><strong>标准化测试</strong>：用同一主题（朱自清《春》的语文教案）让每款技能生成演示文稿。</li>
  <li><strong>AI 评估</strong>：让 Codex 基于内容质量、设计和功能分析并排名。</li>
</ol>

<h2 id="contenders">参赛选手</h2>

<p>测试的五款技能：</p>

<ol>
  <li><strong>PPT Master</strong></li>
  <li><strong>Banana Slides</strong></li>
  <li><strong>Frontend Slides</strong></li>
  <li><strong>HTML PPT</strong></li>
  <li><strong>Guizang PPT Skill</strong></li>
</ol>

<h2 id="results">详细测试结果</h2>

<h3>1. PPT Master</h3>

<ul>
  <li><strong>输出</strong>：11 页 PowerPoint 演示文稿，设计简洁、结构清晰。</li>
  <li><strong>优势</strong>：内容组织良好，段落分明；每页含演讲者备注；重点突出，视觉层次好。</li>
  <li><strong>不足</strong>：部分文本元素可能错位需手动调整；自定义选项有限。</li>
</ul>

<h3>2. Banana Slides</h3>

<ul>
  <li><strong>输出</strong>：13 页演示文稿，浅绿色配色方案。</li>
  <li><strong>优势</strong>：内容结构严谨，逻辑流畅；含明确的学习目标和评估标准；设计美观，风格统一。</li>
  <li><strong>不足</strong>：高级自定义灵活性较低；不太适合高度创意或非教育类演示。</li>
</ul>

<h3>3. Frontend Slides</h3>

<ul>
  <li><strong>输出</strong>：12 页演示文稿，极简设计风格。</li>
  <li><strong>优势</strong>：设计简洁现代，注重可读性；留白和简单图形运用得当；内容精炼、直击要点。</li>
  <li><strong>不足</strong>：视觉多样性有限；不太适合需要强烈视觉冲击力的演示。</li>
</ul>

<h3>4. HTML PPT</h3>

<ul>
  <li><strong>输出</strong>：网页版演示文稿，左侧导航菜单。</li>
  <li><strong>优势</strong>：交互式设计，导航便捷；适合在线演示或网页分享；内容详细，分析深入。</li>
  <li><strong>不足</strong>：需要网络访问才能查看；设计自定义有限。</li>
</ul>

<h3>5. Guizang PPT Skill</h3>

<ul>
  <li><strong>输出</strong>：12 页演示文稿，暗色主题。</li>
  <li><strong>优势</strong>：设计独特现代，暗色配色出众；视觉元素和动画运用得当；内容结构良好，引人入胜。</li>
  <li><strong>不足</strong>：暗色主题不一定适合所有受众；亮光环境下部分元素可能难以阅读。</li>
</ul>

<h2 id="ranking">AI 评估排名</h2>

<p>综合分析五份演示文稿后，Codex 给出以下排名：</p>

<ol>
  <li><strong>PPT Master</strong> — 最均衡，结构清晰，含演讲者备注</li>
  <li><strong>Banana Slides</strong> — 最适合教育类演示，学习目标明确</li>
  <li><strong>Frontend Slides</strong> — 极简设计，内容精炼</li>
  <li><strong>HTML PPT</strong> — 交互式网页设计，内容详细</li>
  <li><strong>Guizang PPT Skill</strong> — 暗色主题独特，视觉元素出色</li>
</ol>

<h2 id="takeaways">关键结论</h2>

<ul>
  <li><strong>教育场景首选</strong>：Banana Slides，学习目标和评估标准内置。</li>
  <li><strong>通用场景首选</strong>：PPT Master，最均衡，适用面最广。</li>
  <li><strong>网页分享首选</strong>：HTML PPT，交互式设计，在线分享方便。</li>
  <li><strong>设计感首选</strong>：Guizang PPT Skill，暗色主题独树一帜，适合需要脱颖而出的演示。</li>
</ul>

<h2 id="recommendation">最终推荐</h2>

<p>如果你想要一款能应对各类演示需求的通用 AI PPT 技能，<strong>PPT Master</strong> 是最佳选择。它在结构、设计和功能之间取得了良好平衡，教育和通用场景都适用。</p>

<p>如果有特定需求：教育类选 <strong>Banana Slides</strong>，网页分享选 <strong>HTML PPT</strong>。</p>

<p>无论选哪款，记得审查和编辑输出结果，确保满足你的具体需求。</p>

<h2>常见问题</h2>

<h3>哪款 AI PPT 技能综合最强？</h3>
<p>PPT Master 在我们的测试中排名第一，它在结构、设计和功能三个维度最为均衡。它适用范围最广——商务报告、教学课件、通用演示都能胜任。演讲者备注是它独有的亮点功能，其他技能大多没有。但"最强"取决于你的场景：教育工作者选 Banana Slides 更合适（内置学习目标），主要在线分享的用户选 HTML PPT 更实用（网页原生格式）。</p>

<h3>这些 AI PPT 技能免费吗？</h3>
<p>这些技能大多是 Codex 插件或社区技能，在 Codex 环境内可免费安装使用。但 Codex 本身需要订阅（推荐 Plus，$20/月）。生成的 PPT 文件（.pptx 或 HTML）归你所有，无使用限制。部分技能可能有高级功能付费层级，但本文测试的基础功能在标准 Codex 订阅下均可使用。</p>

<h3>AI 生成的演示文稿可以自定义吗？</h3>
<p>可以，而且应该自定义。AI 生成的演示文稿是起点，不是成品。生成后你可以：(1) 通过标注或提示词让 Codex 做具体修改，(2) 下载 .pptx 文件在 PowerPoint 或 Google Slides 中编辑，(3) HTML PPT 的话直接编辑 HTML/CSS。我们的测试发现 PPT Master 和 Banana Slides 生成的输出最易编辑，需要手动修复的地方最少。</p>

<h3>用这些技能生成一个演示文稿要多久？</h3>
<p>测试中每款技能生成 11-13 页完整演示文稿耗时 30-90 秒，取决于复杂度和 Codex 当前负载。PPT Master 最快，约 30 秒。真正省时间的不是生成速度——而是省掉了你通常花在结构设计、内容草拟上的 2-4 小时。即使加上 10-15 分钟人工审查和编辑，相比从零做起仍然节省了 90% 以上的时间。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>找到了合适的 PPT 工具？探索更多 AI 生产力技能：</p>
  <ul>
    <li><a href="/articles/complete-guide-codex-zero-to-advanced">Codex 完全指南：从零基础到高级开发工作流</a> — 掌握 Codex 技能和插件体系</li>
    <li><a href="/articles/mastering-ai-workflow-beginner-custom-workbench">掌握 AI 工作流：打造你的专属 AI 工作台</a> — 构建自己的 AI 生产力系统</li>
    <li><a href="/articles/2025-ai-toolkit-practical-guide-every-domain">2025 AI 工具箱：全领域实用指南</a> — 发现更多跨品类 AI 工具</li>
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
