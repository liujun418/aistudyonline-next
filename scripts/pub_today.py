"""
Publish July 14, 2026 — 2 articles, no new tools.
"""
import os

BASE = r"C:\Users\jun\aistudyonline-next"
os.chdir(BASE)

# ===== Part 1: Add 2 article metadata to articles.ts =====
with open('src/lib/articles.ts', 'r', encoding='utf-8') as f:
    articles_src = f.read()

new_articles = r"""  {
    slug: "gpt-5-6-full-launch-sol-terra-luna-family",
    title: "GPT-5.6 Full Launch: The Complete Family of Sol, Terra, and Luna",
    titleZh: "GPT-5.6全系发布：Sol、Terra、Luna三款模型完整实测",
    description: "Hands-on testing of OpenAI's GPT-5.6 model family — Sol building a 3D FPS game with Three.js in 1.5 hours, Terra generating a 3D voxel rocket in 35 minutes, and Luna producing a 47-page annual report from 26K records — with model selection guidance for different task types.",
    descriptionZh: "OpenAI GPT-5.6三款模型完整实测——Sol用Three.js 1.5小时构建3D FPS游戏、Terra 35分钟生成3D体素火箭、Luna从2.6万条记录生成47页年报——含不同任务类型的模型选择指南。",
    category: "AI News",
    tags: ["GPT-5.6", "OpenAI", "Sol", "Terra", "Luna", "Model Comparison", "Benchmark"],
    difficulty: "beginner",
    toolsMentioned: ["ChatGPT", "Codex Agent"],
    date: "2026-07-14",
  },
  {
    slug: "gpt-5-6-openai-merges-chatgpt-codex-end-pure-chat-era",
    title: "GPT-5.6 Full Launch: OpenAI Merges ChatGPT and Codex, Ending the Pure Chat Era",
    titleZh: "GPT-5.6全面发布：OpenAI合并ChatGPT与Codex，纯聊天时代终结",
    description: "OpenAI's landmark GPT-5.6 launch merges ChatGPT and Codex into 'ChatGPT Work', featuring Sol (flagship), Terra (balanced), and Luna (lightweight) — with coding benchmarks beating Claude Fable 5, cybersecurity testing, and UX improvements for 1 billion weekly users.",
    descriptionZh: "OpenAI里程碑式发布：ChatGPT与Codex合并为'ChatGPT Work'，推出Sol（旗舰）、Terra（均衡）、Luna（轻量）三款模型——编码基准超越Claude Fable 5、网络安全实测、面向10亿周活用户的UX升级。",
    category: "AI News",
    tags: ["GPT-5.6", "OpenAI", "ChatGPT", "Codex", "Sol", "AI News", "Merger"],
    difficulty: "beginner",
    toolsMentioned: ["ChatGPT", "Codex Agent", "Claude Fable 5"],
    date: "2026-07-14",
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
  "gpt-5-6-full-launch-sol-terra-luna-family": {
    content: `<div class="meta-banner">
  <span class="meta-badge">📰 AI News</span>
  <span class="meta-badge">🕒 6 min read</span>
  <span class="meta-badge">📅 Jul 14, 2026</span>
  <span class="meta-badge">🎯 Beginner</span>
</div>

<h2 id="introduction">Introduction</h2>

<p>OpenAI has officially released the full GPT-5.6 family: Sol, Terra, and Luna, putting the entire model lineup directly on the desktop. Users can now choose models based on task complexity, cost, and speed, similar to selecting coffee cup sizes. Sol is designed for heavy-duty tasks, Terra for balanced daily work, and Luna for lightweight, cost-effective operations.</p>

<h2 id="sol">Sol: The Flagship Model</h2>

<p>Sol is the most powerful model in the lineup, prompting competitors to activate emergency response measures. Anthropic even delayed Fable 5's experience by a week and reset all user quotas, highlighting the intense competition in the AI space.</p>

<h3>Practical Testing: Building a 3D FPS Game</h3>

<p>We tested Sol's capabilities by creating a fully functional first-person shooter game using Three.js. The task required complete game mechanics, including movement, ammunition, health, enemy AI, and real GLB 3D models for assets.</p>

<h4>Prompt Example</h4>

<pre><code class="language-text">Use Next.js + TypeScript + react-three-fiber + Three.js to create a playable first-person FPS game demo. The game should feature complete movement, ammunition, health, enemy AI, and real GLB 3D models for core assets.</code></pre>

<h4>Results</h4>

<p>Sol successfully generated the entire game in 1.5 hours, including:</p>
<ul>
  <li>Three game concept designs</li>
  <li>Free 3D asset sourcing from open-source communities</li>
  <li>Code generation for missing assets</li>
  <li>Full integration of all components</li>
</ul>

<p>The game features smooth movement, shooting mechanics, enemy AI, and terminal destruction objectives, with only minor bugs that do not affect gameplay.</p>

<h2 id="terra">Terra: The Balanced Model</h2>

<p>Terra is priced at half the cost of GPT-5.5 and offers balanced performance for daily tasks.</p>

<h3>Practical Testing: 3D Voxel Rocket</h3>

<p>We tested Terra by generating a 3D voxel rocket. The model completed the task in 35 minutes, with improved rocket design and UI compared to GPT-5.5. However, the physics engine still needs improvement, as the rocket tilts immediately after launch.</p>

<h2 id="luna">Luna: The Lightweight Model</h2>

<p>Luna is the most cost-effective model, designed for lightweight tasks.</p>

<h3>Practical Testing: Annual Report Generation</h3>

<p>We tested Luna by generating an annual report from a large Excel dataset. The model completed the task in 49 minutes, producing a 47-page report with comprehensive data analysis, including:</p>

<ul>
  <li>13 worksheets and 26,712 transaction records</li>
  <li>Year-over-year and month-over-month comparisons</li>
  <li>Half-year and full-year summaries</li>
  <li>Second-half predictions</li>
  <li>Data integrity checks</li>
</ul>

<p>The report had only minor issues, such as a Chinese garble, but overall was faster and more detailed than manual creation.</p>

<h2 id="conclusion">Conclusion</h2>

<p>GPT-5.6 offers a model for every need:</p>

<ul>
  <li><strong>Sol</strong>: Best for heavy tasks, but high cost</li>
  <li><strong>Terra</strong>: Balanced performance for daily use</li>
  <li><strong>Luna</strong>: Cost-effective for lightweight tasks</li>
</ul>

<p>Users can now choose the model that best fits their requirements, making GPT-5.6 a versatile solution for a wide range of applications.</p>

<h2>常见问题</h2>

<h3>Which GPT-5.6 model should I use for my daily work?</h3>
<p>For most daily tasks, <strong>Terra</strong> is the sweet spot. It matches GPT-5.5's performance at half the cost, which means you get the same quality you're used to while spending less. Use Sol when you need maximum capability: complex coding projects, multi-file refactors, research requiring deep reasoning, or agentic workflows that span many steps. Use Luna for high-volume, simple tasks: summarizing documents, formatting data, drafting emails, or generating basic reports. The cost difference is significant — Luna can handle 5-10x more tasks than Sol for the same token budget.</p>

<h3>How does Sol's 1.5-hour FPS game build compare to what a human developer could do?</h3>
<p>A human developer building the same FPS game from scratch — with movement, shooting, enemy AI, 3D asset sourcing, and full integration — would typically take 3-5 days. Sol's 1.5 hours includes generating three concept designs, sourcing free 3D assets, writing all the code, and integrating everything. The result had minor bugs but was fully playable. This represents roughly a 16-27x speedup. The caveat: the game is a demo, not a polished product. A human would spend additional time on polish, balance, and edge cases. But for prototyping and proof-of-concept, Sol's speed is transformative.</p>

<h3>Is Luna actually useful, or is it too weak for real work?</h3>
<p>Luna's 47-page annual report from 26,712 records proves it's not just a toy. The key is using Luna for the right tasks. It excels at data processing, report generation, summarization, and formatting — tasks where the bottleneck is volume, not reasoning depth. For creative writing, complex coding, or strategic analysis, use Terra or Sol. For routine tasks that would take you hours of manual work, Luna is surprisingly capable and dramatically cheaper. The Chinese garble issue in the test is a minor concern for Chinese-language users, but it's the kind of edge case that improves with each model iteration.</p>

<h3>Will Terra eventually replace GPT-5.5 entirely?</h3>
<p>OpenAI hasn't announced deprecation plans, but Terra's positioning — same performance at half the cost — makes GPT-5.5's continued relevance questionable. In practice, there's no reason to use GPT-5.5 over Terra for new projects. The only reason to keep using GPT-5.5 is if you have existing prompts or workflows that are finely tuned to it and haven't been tested on Terra yet. Given the cost savings, it's worth migrating those workflows sooner rather than later.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Understand the GPT-5.6 family? See the bigger picture:</p>
  <ul>
    <li><a href="/articles/gpt-5-6-openai-merges-chatgpt-codex-end-pure-chat-era">GPT-5.6 Full Launch: OpenAI Merges ChatGPT and Codex</a> — the merger story and coding benchmarks</li>
    <li><a href="/articles/2026-ai-agent-guide-choose-right-tool-beginners">2026 AI Agent Guide: How to Choose the Right Tool for Beginners</a> — see how GPT-5.6's models fit into the Agent landscape</li>
    <li><a href="/articles/understanding-large-language-models-principles-architecture">Understanding Large Language Models: Principles, Architecture, and Practical Usage</a> — understand the technology behind models like Sol</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">📰 AI 新闻</span>
  <span class="meta-badge">🕒 阅读约6分钟</span>
  <span class="meta-badge">📅 2026年7月14日</span>
  <span class="meta-badge">🎯 入门</span>
</div>

<h2 id="introduction">引言</h2>

<p>OpenAI正式发布了完整的GPT-5.6家族：Sol、Terra和Luna，将整个模型阵容直接带到桌面端。用户现在可以根据任务复杂度、成本和速度选择模型，就像选择咖啡杯大小。Sol专为重型任务设计，Terra适合均衡的日常工作，Luna用于轻量、高性价比操作。</p>

<h2 id="sol">Sol：旗舰模型</h2>

<p>Sol是系列中最强大的模型，促使竞争对手启动紧急响应措施。Anthropic甚至将Fable 5的体验推迟了一周并重置了所有用户配额，凸显了AI领域的激烈竞争。</p>

<h3>实战测试：构建3D FPS游戏</h3>

<p>我们通过使用Three.js创建完整的第一人称射击游戏来测试Sol的能力。任务要求包含完整的游戏机制：移动、弹药、生命值、敌人AI和真实GLB 3D模型素材。</p>

<h4>提示词示例</h4>

<pre><code class="language-text">使用Next.js + TypeScript + react-three-fiber + Three.js创建一个可玩的第一人称FPS游戏Demo。游戏应包含完整的移动、弹药、生命值、敌人AI系统，核心素材使用真实GLB 3D模型。</code></pre>

<h4>结果</h4>

<p>Sol在1.5小时内成功生成了整个游戏，包括：</p>
<ul>
  <li>三套游戏概念设计</li>
  <li>从开源社区获取免费3D素材</li>
  <li>为缺失素材生成代码</li>
  <li>所有组件的完整集成</li>
</ul>

<p>游戏具有流畅的移动、射击机制、敌人AI和终端摧毁目标，仅有不影响游戏性的小Bug。</p>

<h2 id="terra">Terra：均衡模型</h2>

<p>Terra的价格是GPT-5.5的一半，为日常任务提供均衡性能。</p>

<h3>实战测试：3D体素火箭</h3>

<p>我们通过生成3D体素火箭来测试Terra。模型在35分钟内完成任务，火箭设计和UI相比GPT-5.5有所改进。但物理引擎仍需改进，火箭发射后立即倾斜。</p>

<h2 id="luna">Luna：轻量模型</h2>

<p>Luna是性价比最高的模型，为轻量任务设计。</p>

<h3>实战测试：年报生成</h3>

<p>我们通过从大型Excel数据集生成年报来测试Luna。模型在49分钟内完成任务，生成了一份47页的报告，包含全面数据分析：</p>

<ul>
  <li>13个工作表和26,712条交易记录</li>
  <li>同比和环比对比</li>
  <li>半年和全年汇总</li>
  <li>下半年预测</li>
  <li>数据完整性检查</li>
</ul>

<p>报告仅有小问题，如一处中文乱码，但整体比手动创建更快、更详细。</p>

<h2 id="conclusion">总结</h2>

<p>GPT-5.6为每种需求提供了模型：</p>

<ul>
  <li><strong>Sol</strong>：最适合重型任务，但成本较高</li>
  <li><strong>Terra</strong>：日常使用的均衡性能</li>
  <li><strong>Luna</strong>：轻量任务的高性价比之选</li>
</ul>

<p>用户现在可以选择最适合自己需求的模型，使GPT-5.6成为覆盖广泛应用的通用解决方案。</p>

<h2>常见问题</h2>

<h3>日常办公该选哪个GPT-5.6模型？</h3>
<p>对大多数日常任务，<strong>Terra</strong>是最佳选择。它以一半的价格匹配GPT-5.5的性能，意味着你获得同样质量的同时花更少。需要最强能力时用Sol：复杂编码项目、多文件重构、需要深度推理的研究、或跨多步骤的Agent工作流。高容量简单任务用Luna：文档摘要、数据格式化、邮件起草、基础报告生成。成本差异显著——同样token预算下Luna能处理5-10倍于Sol的任务量。</p>

<h3>Sol 1.5小时构建FPS游戏和人类开发者比如何？</h3>
<p>人类开发者从零构建同样的FPS游戏——包含移动、射击、敌人AI、3D素材获取和完整集成——通常需要3-5天。Sol的1.5小时包括生成三套概念设计、获取免费3D素材、编写所有代码和集成所有内容。结果有小Bug但完全可玩。这大约代表了16-27倍的加速。注意事项：游戏是Demo，不是成品。人类会花额外时间打磨、平衡和边缘情况处理。但对原型验证和概念证明，Sol的速度是革命性的。</p>

<h3>Luna真的有用吗，还是太弱了做不了实际工作？</h3>
<p>Luna从26,712条记录生成47页年报证明了它不只是玩具。关键是用Luna做正确的任务。它擅长数据处理、报告生成、摘要和格式化——这些任务的瓶颈是量而非推理深度。创意写作、复杂编码或战略分析用Terra或Sol。对于需要你数小时手动工作的常规任务，Luna的能力出人意料且成本极低。测试中的中文乱码问题对中文用户是小困扰，但这是每次模型迭代都会改善的边缘情况。</p>

<h3>Terra最终会完全取代GPT-5.5吗？</h3>
<p>OpenAI未公布淘汰计划，但Terra的定位——同样性能、一半价格——让GPT-5.5的持续存在变得可疑。实际使用中，新项目没有理由用GPT-5.5而非Terra。继续使用GPT-5.5的唯一理由是已有针对它精细调优且未在Terra上测试过的提示词或工作流。考虑到成本节省，尽早迁移这些工作流是明智的。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>了解了GPT-5.6家族？看清全局：</p>
  <ul>
    <li><a href="/articles/gpt-5-6-openai-merges-chatgpt-codex-end-pure-chat-era">GPT-5.6全面发布：OpenAI合并ChatGPT与Codex</a> — 合并故事与编码基准测试</li>
    <li><a href="/articles/2026-ai-agent-guide-choose-right-tool-beginners">2026 AI Agent选型指南：新手如何选择最适合的工具</a> — 了解GPT-5.6模型在Agent格局中的位置</li>
    <li><a href="/articles/understanding-large-language-models-principles-architecture">大语言模型深度解读：从Transformer原理到实战应用</a> — 理解Sol等模型背后的技术</li>
  </ul>
</div>`,
  },

  "gpt-5-6-openai-merges-chatgpt-codex-end-pure-chat-era": {
    content: `<div class="meta-banner">
  <span class="meta-badge">📰 AI News</span>
  <span class="meta-badge">🕒 5 min read</span>
  <span class="meta-badge">📅 Jul 14, 2026</span>
  <span class="meta-badge">🎯 Beginner</span>
</div>

<h2 id="introduction">Introduction</h2>

<p>OpenAI has officially merged ChatGPT and Codex, and the highly anticipated GPT-5.6 series is now live. The once-central chat box in ChatGPT has been replaced by a Codex-style workspace, marking the end of the pure chat era and the beginning of a new AI age.</p>

<h2 id="three-models">The Three Models of GPT-5.6</h2>

<p>The GPT-5.6 series includes three models:</p>

<ul>
  <li><strong>Sol</strong>: The new flagship model, designed for complex reasoning, coding, research, and long-horizon agentic work.</li>
  <li><strong>Terra</strong>: A balanced model for efficient everyday work, with performance comparable to GPT-5.5 at a lower cost.</li>
  <li><strong>Luna</strong>: The fastest and most cost-efficient model, ideal for high-volume tasks.</li>
</ul>

<p>All three models are available to all ChatGPT subscription plans, making advanced AI capabilities accessible to every member.</p>

<h2 id="sol-details">GPT-5.6 Sol: The All-Rounder Model</h2>

<p>After five hours of intensive use, GPT-5.6 Sol stands out as the most well-rounded model available today. It offers low pricing, strong planning capabilities, exceptional code execution, extremely low hallucination rates, and high accuracy. While its front-end aesthetics and content creation still have room for improvement, it outperforms previous models in these areas.</p>

<h3>Key Performance Highlights</h3>

<ul>
  <li><strong>Coding</strong>: GPT-5.6 Sol scores 80 on the Artificial Analysis Coding Agent Index, surpassing Claude Fable 5's 77.2 by 2.8 points.</li>
  <li><strong>Efficiency</strong>: It reduces output token latency by more than half and lowers costs by one-third compared to other leading models.</li>
  <li><strong>Cybersecurity</strong>: GPT-5.6 Sol achieves results comparable to Claude Fable 5 on the ExploitBench cybersecurity evaluation at a fraction of the cost.</li>
</ul>

<h2 id="cybersecurity">Real-World Application: Cybersecurity</h2>

<p>For an AI news website under frequent DDoS attacks, GPT-5.6 Sol proved invaluable. When using Claude Fable 5 for security tasks, it was often restricted due to security keywords. GPT-5.6 Sol, however, identified and fixed multiple security vulnerabilities in just 21 minutes using its Ultra Fast mode, with minimal token consumption.</p>

<h2 id="ux-improvements">User Experience Improvements</h2>

<p>GPT-5.6 Sol also shows significant improvements in front-end aesthetics. For example, visualizing data for Typhoon Bavi produced results far better than what GPT-5.5 could produce, though still not quite at the level of Claude's best outputs.</p>

<h2 id="merger">The ChatGPT and Codex Merge</h2>

<p>OpenAI has transformed ChatGPT into ChatGPT Work, making it easier for the 1 billion weekly active ChatGPT users to transition to Codex's capabilities. Users can now switch between Work and Codex modes in the top-left corner, with the original chat mode now located in the sidebar.</p>

<h2 id="conclusion">Conclusion</h2>

<p>GPT-5.6 represents a significant leap forward in AI capabilities, offering powerful, cost-effective solutions for coding, cybersecurity, and everyday work. The merge of ChatGPT and Codex, along with the new model lineup, marks the beginning of the agentic AI era, providing users with more powerful and versatile tools to tackle complex tasks.</p>

<h2>常见问题</h2>

<h3>What does the ChatGPT-Codex merger mean for existing ChatGPT users?</h3>
<p>ChatGPT is now called "ChatGPT Work" — the familiar chat interface still exists in the sidebar, but the default view is now a Codex-style workspace. This means every ChatGPT user now has access to agent capabilities (file operations, code execution, browser control) without installing a separate app. The transition is designed to be gradual: you can still use pure chat mode for simple questions, but the workspace is there when you need the AI to actually do things rather than just talk about them. For 1 billion weekly active users, this is the biggest interface change since ChatGPT launched.</p>

<h3>How significant is Sol beating Claude Fable 5 on coding benchmarks?</h3>
<p>Very. Claude Fable 5 was the undisputed coding champion, and Sol's 80 vs. 77.2 on the Coding Agent Index is a meaningful gap — not just a statistical tie. More importantly, Sol achieves this while reducing latency by 50%+ and cost by one-third. This combination — better quality, faster speed, lower cost — is rare in AI benchmarks. The cybersecurity results are equally notable: matching Claude's security analysis quality at a fraction of the cost makes Sol the practical choice for security-sensitive development work. The one area where Claude still leads is front-end aesthetics and creative output quality.</p>

<h3>Should I switch from Claude to GPT-5.6 Sol?</h3>
<p>It depends on your primary use case. For <strong>coding and agentic workflows</strong>, Sol is now the stronger choice — better benchmarks, lower cost, faster output. For <strong>front-end design and creative content</strong>, Claude still produces more polished results. For <strong>security-sensitive work</strong>, Sol's ability to handle security tasks without triggering keyword restrictions (unlike Claude) is a practical advantage. The smart approach: use both. Sol for heavy coding, agent tasks, and security work. Claude for design, creative writing, and when you need the most polished final output. The cost difference means you can use Sol for 80% of tasks and Claude for the 20% where it excels.</p>

<h3>Is Luna worth using, or is it just a stripped-down model?</h3>
<p>Luna is purpose-built for high-volume, low-complexity tasks. It's not "stripped down" — it's optimized for a different workload. For tasks like summarizing 100 customer emails, formatting a dataset, or generating routine reports, Luna is actually the better choice than Sol or Terra because it's faster and cheaper while being perfectly adequate for the task. The companion article (GPT-5.6 Family practical testing) shows Luna generating a 47-page report from 26K records — that's real work, not a toy. The key is task matching: don't use Luna for complex reasoning, don't use Sol for simple data processing.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Understand the GPT-5.6 launch? See the models in action:</p>
  <ul>
    <li><a href="/articles/gpt-5-6-full-launch-sol-terra-luna-family">GPT-5.6 Full Launch: The Complete Family of Sol, Terra, and Luna</a> — hands-on testing of all three models</li>
    <li><a href="/articles/chatgpt-codex-10-core-features-beginners-work-efficiency">ChatGPT Codex: 10 Core Features for Beginners to Boost Work Efficiency</a> — put the new ChatGPT Work to use</li>
    <li><a href="/articles/2026-ai-agent-guide-choose-right-tool-beginners">2026 AI Agent Guide: How to Choose the Right Tool for Beginners</a> — see how GPT-5.6 changes the Agent landscape</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">📰 AI 新闻</span>
  <span class="meta-badge">🕒 阅读约5分钟</span>
  <span class="meta-badge">📅 2026年7月14日</span>
  <span class="meta-badge">🎯 入门</span>
</div>

<h2 id="introduction">引言</h2>

<p>OpenAI正式合并了ChatGPT和Codex，备受期待的GPT-5.6系列现已上线。ChatGPT中原先居中的聊天框被Codex风格的工作区取代，标志着纯聊天时代的终结和新AI时代的开启。</p>

<h2 id="three-models">GPT-5.6的三款模型</h2>

<p>GPT-5.6系列包含三款模型：</p>

<ul>
  <li><strong>Sol</strong>：新旗舰模型，专为复杂推理、编码、研究和长周期Agent工作设计。</li>
  <li><strong>Terra</strong>：均衡模型，高效处理日常工作，性能媲美GPT-5.5但成本更低。</li>
  <li><strong>Luna</strong>：最快、最高效的模型，适合高容量任务。</li>
</ul>

<p>三款模型面向所有ChatGPT订阅方案开放，让每位会员都能使用先进的AI能力。</p>

<h2 id="sol-details">GPT-5.6 Sol：全能模型</h2>

<p>经过五小时高强度使用，GPT-5.6 Sol是当今最全面的模型。它提供低价格、强规划能力、卓越的代码执行、极低的幻觉率和高准确率。虽然前端美学和内容创作仍有提升空间，但在这些方面已超越前代模型。</p>

<h3>关键性能亮点</h3>

<ul>
  <li><strong>编码</strong>：GPT-5.6 Sol在Artificial Analysis编码Agent指数上得分80，超越Claude Fable 5的77.2分，领先2.8分。</li>
  <li><strong>效率</strong>：输出token延迟降低过半，成本相比其他领先模型降低三分之一。</li>
  <li><strong>网络安全</strong>：GPT-5.6 Sol在ExploitBench网络安全评估中取得与Claude Fable 5相当的成绩，成本仅为零头。</li>
</ul>

<h2 id="cybersecurity">实战应用：网络安全</h2>

<p>对于一家频繁遭受DDoS攻击的AI新闻网站，GPT-5.6 Sol证明了其价值。使用Claude Fable 5处理安全任务时，常因安全关键词被限制。而GPT-5.6 Sol使用Ultra Fast模式，仅用21分钟就识别并修复了多个安全漏洞，token消耗极少。</p>

<h2 id="ux-improvements">用户体验改进</h2>

<p>GPT-5.6 Sol在前端美学方面也有显著提升。例如，可视化台风巴威数据的结果远超GPT-5.5的水平，虽然仍不及Claude的最佳输出。</p>

<h2 id="merger">ChatGPT与Codex合并</h2>

<p>OpenAI将ChatGPT转型为ChatGPT Work，让10亿周活跃ChatGPT用户更容易过渡到Codex的能力。用户现在可以在左上角切换Work和Codex模式，原聊天模式位于侧边栏中。</p>

<h2 id="conclusion">总结</h2>

<p>GPT-5.6代表了AI能力的重大飞跃，为编码、网络安全和日常工作提供了强大且高性价比的解决方案。ChatGPT与Codex的合并以及新模型阵容，标志着Agent AI时代的开启，为用户提供了更强大、更多元的工具来应对复杂任务。</p>

<h2>常见问题</h2>

<h3>ChatGPT-Codex合并对现有ChatGPT用户意味着什么？</h3>
<p>ChatGPT现在叫"ChatGPT Work"——熟悉的聊天界面仍在侧边栏中，但默认视图变为Codex风格的工作区。这意味着每个ChatGPT用户现在都能使用Agent能力（文件操作、代码执行、浏览器控制），无需安装单独应用。过渡设计为渐进式：简单问题仍可用纯聊天模式，但需要AI真正做事而不只是谈论时，工作区就在那里。对10亿周活跃用户来说，这是ChatGPT上线以来最大的界面变革。</p>

<h3>Sol在编码基准上击败Claude Fable 5有多重要？</h3>
<p>非常重要。Claude Fable 5曾是无可争议的编码冠军，Sol的80 vs. 77.2分差距有意义——不是统计平局。更重要的是，Sol在实现这一点的同时将延迟降低50%+、成本降低三分之一。这种组合——更好质量、更快速度、更低成本——在AI基准测试中很少见。网络安全结果同样值得关注：以零头成本匹配Claude的安全分析质量，使Sol成为安全敏感开发工作的务实选择。Claude仍领先的领域是前端美学和创意输出质量。</p>

<h3>该从Claude切换到GPT-5.6 Sol吗？</h3>
<p>取决于你的主要使用场景。<strong>编码和Agent工作流</strong>方面，Sol现在是更强选择——更好的基准、更低的成本、更快的输出。<strong>前端设计和创意内容</strong>方面，Claude仍产出更精致的结果。<strong>安全敏感工作</strong>方面，Sol能在不触发关键词限制的情况下处理安全任务（与Claude不同）是实际优势。聪明做法：两者都用。Sol处理重型编码、Agent任务和安全工作。Claude处理设计、创意写作和需要最精致最终输出的场景。成本差异意味着你可以用Sol处理80%的任务，Claude处理它擅长的20%。</p>

<h3>Luna值得用吗，还是只是一个阉割版模型？</h3>
<p>Luna专为高容量低复杂度任务设计。它不是"阉割版"——它是为不同工作负载优化的。对于总结100封客户邮件、格式化数据集或生成常规报告等任务，Luna实际上比Sol或Terra更合适，因为它更快更便宜，同时完全胜任这些任务。配套文章（GPT-5.6家族实测）展示了Luna从2.6万条记录生成47页报告——这是真正的工作，不是玩具。关键是任务匹配：不要用Luna做复杂推理，也不要用Sol做简单数据处理。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>了解了GPT-5.6发布？看模型实战表现：</p>
  <ul>
    <li><a href="/articles/gpt-5-6-full-launch-sol-terra-luna-family">GPT-5.6全系发布：Sol、Terra、Luna三款模型完整实测</a> — 三款模型实战测试</li>
    <li><a href="/articles/chatgpt-codex-10-core-features-beginners-work-efficiency">ChatGPT Codex：新手必学的10个核心提效功能</a> — 把新的ChatGPT Work用起来</li>
    <li><a href="/articles/2026-ai-agent-guide-choose-right-tool-beginners">2026 AI Agent选型指南：新手如何选择最适合的工具</a> — 了解GPT-5.6如何改变Agent格局</li>
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