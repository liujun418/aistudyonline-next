"""Publish Aug 5, 2026 — 1 article, no new tools."""
import os; BASE = r"C:\Users\jun\aistudyonline-next"; os.chdir(BASE)

with open('src/lib/articles.ts', 'r', encoding='utf-8') as f: s = f.read()
a = r"""  {
    slug: "complete-guide-ai-industry-chain-from-energy-to-robots",
    title: "A Complete Guide to the AI Industry Chain: From Energy to Smart Robots",
    titleZh: "AI产业链完整指南：从能源到智能机器人",
    description: "A bottom-up overview of the AI industry chain — energy (solar/wind/nuclear), chips (ASML lithography, semiconductor manufacturing), PCB & MLCC, large models (training pipeline), and smart robots — plus investment, career, and skill-building opportunities in each layer.",
    descriptionZh: "从底层到顶层的AI产业链全景——能源（光伏/风电/核电）、芯片（ASML光刻、半导体制造）、PCB和MLCC、大模型（训练流程）、智能机器人——每层的投资、职业和技能机会。",
    category: "ai-learning",
    tags: ["AI Industry", "Chips", "Semiconductor", "Energy", "Robots", "Large Models", "Career"],
    difficulty: "beginner",
    toolsMentioned: ["DeepSeek", "TensorFlow"],
    date: "2026-08-05",
  },

"""
last = s.rfind('];')
with open('src/lib/articles.ts', 'w', encoding='utf-8') as f: f.write(s[:last] + a + '];')
print('Part 1 done')

with open('src/lib/article-content.ts', 'r', encoding='utf-8') as f: c = f.read()
n = r'''
  "complete-guide-ai-industry-chain-from-energy-to-robots": {
    content: `<div class="meta-banner">
  <span class="meta-badge">📚 AI Learning</span>
  <span class="meta-badge">🕒 6 min read</span>
  <span class="meta-badge">📅 Aug 5, 2026</span>
  <span class="meta-badge">🎯 Beginner</span>
</div>

<h2 id="introduction">Introduction</h2>
<p>If you've ever wondered how AI works from the ground up, this guide breaks down the entire AI industry chain in simple, practical terms. From raw materials to smart robots, you'll learn how each part connects — and how you can find opportunities in this trillion-dollar sector.</p>

<h2 id="energy">1. Energy: The Foundation of AI</h2>
<p>AI systems need massive amounts of electricity to operate. "The end of AI is electricity; the end of electricity is energy." <strong>New Energy</strong> (solar, wind, nuclear) and <strong>Fossil Fuels</strong> both play roles in powering AI infrastructure.</p>

<h2 id="chips">2. Chips: The Brain of AI</h2>
<p>Chips are the "brain" of AI systems. How chips are made: raw sand (quartz) → purified to 11-nines silicon → melted into ingot → cut into wafers → etched with nanoscale circuits via ASML EUV lithography.</p>
<pre><code class="language-bash"># Example: Check chip manufacturing equipment
lithography_machine --status</code></pre>

<h2 id="pcb">3. PCB & MLCC: The Body of AI</h2>
<ul>
  <li><strong>PCB (Printed Circuit Board)</strong>: The "skeleton" connecting chips and components.</li>
  <li><strong>MLCC (Multi-Layer Ceramic Capacitor)</strong>: A "micro power bank" stabilizing voltage during AI operations.</li>
</ul>

<h2 id="large-models">4. Large Models: The Knowledge of AI</h2>
<p>Large models (e.g., DeepSeek, Doubao) are the "knowledge base" of AI. They learn from massive data through: Data Collection → Data Processing (cleaned/labeled by "data processing workers") → Training (learning patterns to generate responses).</p>
<pre><code class="language-python"># Example: Train a simple AI model
model = train_model(data="cleaned_data.csv", epochs=100)</code></pre>

<h2 id="robots">5. Smart Robots: The Body of AI</h2>
<p>Smart robots (robot dogs, humanoid robots) are the "physical body" of AI, allowing interaction with the real world. Current applications: tourism (performances), industry (manufacturing, logistics). Future opportunities: service robots (healthcare, education, customer service), industrial robots (assembly, maintenance).</p>

<h2 id="opportunities">How to Find Opportunities</h2>
<h3>Invest in Key Nodes</h3>
<ul>
  <li><strong>Energy</strong>: New energy companies (solar, wind, nuclear)</li>
  <li><strong>Chips</strong>: Semiconductor manufacturers (TSMC, Intel)</li>
  <li><strong>Data Processing</strong>: Companies that clean and label data</li>
</ul>
<h3>Work in the AI Industry</h3>
<ul>
  <li><strong>Data Processing Workers</strong>: Clean and label data for AI models</li>
  <li><strong>Robot Engineers</strong>: Design and program smart robots</li>
  <li><strong>AI Trainers</strong>: Train large models to improve performance</li>
</ul>
<h3>Learn AI Skills</h3>
<ul>
  <li><strong>Programming</strong>: Python and TensorFlow to build AI models</li>
  <li><strong>Data Analysis</strong>: SQL and Excel to analyze AI data</li>
  <li><strong>Robotics</strong>: Arduino and ROS to build smart robots</li>
</ul>
<pre><code class="language-bash"># Install Python for AI development
sudo apt install python3
pip install tensorflow pandas</code></pre>

<h2 id="conclusion">Final Takeaway</h2>
<p>The AI industry chain is a trillion-dollar opportunity. Whether you're an investor, a worker, or a learner, there's a place for you in this sector. The key is to find your niche and stay ahead of the curve.</p>

<h2>常见问题</h2>

<h3>Which layer of the AI industry chain has the highest barrier to entry?</h3>
<p><strong>Chip manufacturing</strong> has the highest barrier by far. It requires ASML's EUV lithography machines (billions of dollars each, years of lead time, export controls), 11-nines silicon purification, and multi-billion-dollar fabrication plants. Only a handful of companies globally (TSMC, Samsung, Intel) can produce cutting-edge AI chips. By contrast, the large model layer has lower barriers in terms of capital — training a model like DeepSeek V4 costs millions, not billions — but requires rare AI research talent. The lowest barrier: data processing (cleaning and labeling data) and AI application development, which individuals and small teams can enter with modest investment.</p>

<h3>How does the energy layer affect AI development?</h3>
<p>Energy is becoming the binding constraint. A single GPT-5.6 training run consumes as much electricity as a small city. As AI inference scales to billions of daily users, the energy cost of running AI (not just training it) now exceeds training costs for most companies. This is driving: (1) nuclear power partnerships — tech giants are signing direct agreements with nuclear plants, (2) location strategy — data centers moving to regions with cheap renewable energy, (3) efficiency innovation — models like DeepSeek V4 Flash that deliver comparable performance at 1/36th the cost, which translates to 1/36th the energy. The energy layer isn't just about powering AI — it's shaping which AI architectures are economically viable.</p>

<h3>What skills should I learn to enter the AI industry chain?</h3>
<p>It depends on which layer you target. The guide gives three paths: <strong>Programming</strong> (Python, TensorFlow) for model development and AI engineering — the most versatile path, applicable to large models, robotics, and data processing. <strong>Data Analysis</strong> (SQL, Excel) for data processing and business intelligence — lower barrier, high demand, but more competition. <strong>Robotics</strong> (Arduino, ROS) for hardware-related roles — higher barrier (requires electronics knowledge), but less competition. The common foundation across all three: Python, basic statistics, and the ability to work with large datasets. The "AI Trainers" role (training and fine-tuning models) is the fastest-growing new job category in the chain — no single degree maps to it yet, making it accessible to self-taught learners with practical experience.</p>

<h3>Is the AI industry chain a bubble, or a real opportunity?</h3>
<p>Both — and the distinction matters for your strategy. The <strong>valuation layer</strong> (publicly traded AI companies) exhibits bubble characteristics: high P/E ratios, speculative narratives, and the expectation that "AI will change everything." The <strong>infrastructure layer</strong> (energy, chips, data centers) is real and growing — data center construction is at an all-time high, chip orders are backlogged for years, and energy demand from AI is measurable on national grids. The <strong>application layer</strong> (AI tools, agents, robots) is where real value is being created for end users, but where 99% of startups will fail. The guide's recommendation: invest in infrastructure (energy, chips), work in applications (where the jobs are), and learn skills that are transferable across layers (Python, data analysis, prompt engineering). The July 4 "AI Bubble or Opportunity" article covers this in more depth with the 2000 internet bubble survivor model.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Understand the big picture? Dive deeper into each layer:</p>
  <ul>
    <li><a href="/articles/ai-bubble-or-opportunity-guide-ordinary-people">Is AI a Bubble or Opportunity? A Guide for Ordinary People</a> — the survivor model for navigating the AI industry</li>
    <li><a href="/articles/understanding-large-language-models-principles-architecture">Understanding Large Language Models: Principles, Architecture, and Practical Usage</a> — understand the large model layer</li>
    <li><a href="/articles/2026-local-llm-benchmark-13-open-source-models-4000-hardware-guide">2026 Local LLM Benchmark: 13 Open-Source Models, $4K Hardware Guide</a> — dive into the hardware/infrastructure layer</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">📚 AI 学习</span>
  <span class="meta-badge">🕒 阅读约6分钟</span>
  <span class="meta-badge">📅 2026年8月5日</span>
  <span class="meta-badge">🎯 入门</span>
</div>

<h2 id="introduction">引言</h2>
<p>如果你曾好奇AI如何从底层到顶层运作，本指南以通俗易懂的方式拆解整个AI产业链。从原材料到智能机器人，你了解每个环节如何连接——以及如何在这个万亿级市场找到机会。</p>

<h2 id="energy">1. 能源：AI的基础</h2>
<p>AI系统运行需要大量电力。"AI的尽头是电力，电力的尽头是能源。"<strong>新能源</strong>（光伏、风电、核电）和<strong>化石能源</strong>都在为AI基础设施提供动力。</p>

<h2 id="chips">2. 芯片：AI的大脑</h2>
<p>芯片制造流程：石英砂→提纯至11个9的硅→熔铸成硅锭→切割成晶圆→ASML EUV光刻机蚀刻纳米级电路。</p>

<h2 id="pcb">3. PCB和MLCC：AI的身体</h2>
<ul>
  <li><strong>PCB（印刷电路板）</strong>：连接芯片和组件的"骨架"。</li>
  <li><strong>MLCC（多层陶瓷电容）</strong>：AI运行时稳定电压的"微型充电宝"。</li>
</ul>

<h2 id="large-models">4. 大模型：AI的知识</h2>
<p>大模型（如DeepSeek、豆包）是AI的"知识库"。数据采集→数据处理（"数据标注员"清洗标注）→训练（学习模式并生成回复）。</p>

<h2 id="robots">5. 智能机器人：AI的身体</h2>
<p>智能机器人（机器狗、人形机器人）是AI的"物理身体"，让AI与现实世界交互。当前应用：旅游（表演）、工业（制造、物流）。未来机会：服务机器人（医疗、教育、客服）、工业机器人（组装、维护）。</p>

<h2 id="opportunities">如何找到机会</h2>
<h3>投资关键节点</h3>
<ul>
  <li><strong>能源</strong>：新能源公司（光伏、风电、核电）</li>
  <li><strong>芯片</strong>：半导体制造商（台积电、英特尔）</li>
  <li><strong>数据处理</strong>：数据清洗标注公司</li>
</ul>
<h3>在AI行业工作</h3>
<ul>
  <li><strong>数据标注员</strong>：清洗标注AI训练数据</li>
  <li><strong>机器人工程师</strong>：设计和编程智能机器人</li>
  <li><strong>AI训练师</strong>：训练大模型提升性能</li>
</ul>
<h3>学AI技能</h3>
<ul>
  <li><strong>编程</strong>：Python和TensorFlow构建AI模型</li>
  <li><strong>数据分析</strong>：SQL和Excel分析AI数据</li>
  <li><strong>机器人</strong>：Arduino和ROS构建智能机器人</li>
</ul>

<h2 id="conclusion">总结</h2>
<p>AI产业链是万亿级机遇。无论你是投资者、从业者还是学习者，都能在这个领域找到位置。关键是找到你的细分领域并保持领先。</p>

<h2>常见问题</h2>

<h3>AI产业链哪一层门槛最高？</h3>
<p><strong>芯片制造</strong>门槛最高。需要ASML的EUV光刻机（每台数十亿美元、数年交货期、出口管制），11个9的硅提纯，以及数十亿美元的晶圆厂。全球仅台积电、三星、英特尔等少数公司能生产顶尖AI芯片。相比之下，大模型层资本门槛较低——训练DeepSeek V4需要数百万而非数十亿——但需要稀缺的AI研究人才。门槛最低：数据处理（清洗标注数据）和AI应用开发，个人和小团队投入适中即可进入。</p>

<h3>能源层如何影响AI发展？</h3>
<p>能源正成为约束条件。单次GPT-5.6训练耗电相当于一个小城市。AI推理扩展到数十亿日活用户后，运行AI的能源成本（不仅训练）已超过大多数公司的训练成本。这推动：(1)核电合作——科技巨头直接与核电站签署协议，(2)选址策略——数据中心迁往可再生能源廉价地区，(3)效率创新——DeepSeek V4 Flash等模型以1/36成本提供相当性能，这意味着1/36的能耗。能源层不仅关乎供电——它在塑造哪些AI架构经济上可行。</p>

<h3>进入AI产业链该学什么技能？</h3>
<p>取决于目标层。指南给出三条路径：<strong>编程</strong>（Python、TensorFlow）面向模型开发和AI工程——最通用的路径，适用于大模型、机器人和数据处理。<strong>数据分析</strong>（SQL、Excel）面向数据处理和商业智能——门槛低、需求大、但竞争也更激烈。<strong>机器人</strong>（Arduino、ROS）面向硬件相关岗位——门槛较高（需电子知识），但竞争较少。三者共同基础：Python、基础统计学、处理大规模数据集的能力。"AI训练师"角色（训练和微调模型）是链条中增长最快的新职业——尚无对应学位，自学者有实际经验即可入门。</p>

<h3>AI产业链是泡沫还是真实机遇？</h3>
<p>两者兼有——区别对你的策略至关重要。<strong>估值层</strong>（上市AI公司）呈现泡沫特征：高市盈率、投机叙事、"AI会改变一切"的预期。<strong>基础设施层</strong>（能源、芯片、数据中心）真实且增长——数据中心建设历史新高，芯片订单积压数年，AI的能源需求可在国家电网层面测量。<strong>应用层</strong>（AI工具、Agent、机器人）正在为终端用户创造真实价值，但99%的创业公司会失败。指南建议：投资基础设施（能源、芯片），在应用层工作（工作机会所在），学习跨层可迁移的技能（Python、数据分析、提示词工程）。7月4日"AI是泡沫还是机遇"文章用2000年互联网泡沫幸存者模型对此有更深入分析。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>理解了全局？深入每一层：</p>
  <ul>
    <li><a href="/articles/ai-bubble-or-opportunity-guide-ordinary-people">AI是泡沫还是机遇？普通人应对AI浪潮的生存指南</a> — 驾驭AI产业的幸存者模型</li>
    <li><a href="/articles/understanding-large-language-models-principles-architecture">大语言模型深度解读：从Transformer原理到实战应用</a> — 理解大模型层</li>
    <li><a href="/articles/2026-local-llm-benchmark-13-open-source-models-4000-hardware-guide">2026本地大模型横评：13款开源模型+$4000硬件部署全指南</a> — 深入硬件/基础设施层</li>
  </ul>
</div>`,
  },

'''
last = c.rfind('};')
with open('src/lib/article-content.ts', 'w', encoding='utf-8') as f: f.write(c[:last] + n + '};')
print('Part 2 done\n=== Done ===')