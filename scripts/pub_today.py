"""Publish Aug 13, 2026 — 1 article, no new tools."""
import os; BASE = r"C:\Users\jun\aistudyonline-next"; os.chdir(BASE)

with open('src/lib/articles.ts', 'r', encoding='utf-8') as f: s = f.read()
a = r"""  {
    slug: "deepseek-v4-pro-0813-real-world-testing-two-ai-development-projects",
    title: "DeepSeek V4 Pro 0813 Real-World Testing: Two Practical AI Development Projects",
    titleZh: "DeepSeek V4 Pro 0813实战测试：两个实用AI开发项目",
    description: "Hands-on testing of DeepSeek V4 Pro 0813 with two real projects — a 6-style personal blog built in 25 minutes and a runnable 3D racing game in 40 minutes — showing delivery capability beyond benchmark scores.",
    descriptionZh: "用两个真实项目实测DeepSeek V4 Pro 0813——25分钟搭建6风格个人博客、40分钟生成可运行的3D赛车游戏，展示超越基准分数的真实交付能力。",
    category: "ai-news",
    tags: ["DeepSeek", "DeepSeek V4 Pro", "AI Model", "Real-World Testing", "Coding", "Blog", "3D Game"],
    difficulty: "beginner",
    toolsMentioned: ["DeepSeek"],
    date: "2026-08-13",
  },

"""
last = s.rfind('];')
with open('src/lib/articles.ts', 'w', encoding='utf-8') as f: f.write(s[:last] + a + '];')
print('Part 1 done')

with open('src/lib/article-content.ts', 'r', encoding='utf-8') as f: c = f.read()
n = r'''
  "deepseek-v4-pro-0813-real-world-testing-two-ai-development-projects": {
    content: `<div class="meta-banner">
  <span class="meta-badge">📰 AI News</span>
  <span class="meta-badge">🕒 6 min read</span>
  <span class="meta-badge">📅 Aug 13, 2026</span>
  <span class="meta-badge">🎯 Beginner</span>
</div>

<h2 id="introduction">Introduction</h2>
<p>DeepSeek has officially released the V4 Pro 0813 model. Instead of just focusing on parameters and benchmark scores, we will test its real programming capabilities with two practical projects.</p>

<h2 id="core-info">Core Information of the New Model</h2>
<ul>
  <li><strong>Maximum Output</strong>: 384K</li>
  <li><strong>Thinking Mode</strong>: Supports both thinking and non-thinking modes, with thinking mode enabled by default</li>
  <li><strong>Pricing</strong>: Approximately 3 times that of V4 Flash</li>
  <li><strong>Benchmark Scores</strong>: The scores on the left side of the benchmark table are estimated scores, while the scores on the right side are accurate scores. The scores of V4 Pro 0813 are higher than those of V4 Flash 0731, but not exceeding Fable 5.</li>
</ul>

<h2 id="project-1">Project 1: Develop a Personal Blog with 6 Styles</h2>

<h3>The Prompt</h3>
<pre><code class="language-text">Help me design and develop a modern personal blog website, providing 6 switchable visual styles:
- Minimalist black and white
- Tech future
- Warm retro
- Clear deep color
- Other styles you think are suitable

The website should include:
- Home page
- Article list
- Article details
- About us
- Contact information

Each style should have obvious differences in color, font and layout, and support both computer and mobile terminals. Add style switching buttons, light and dark modes and smooth transition animations.
Please use real example content and pictures, the interface is simple and designed, and finally deliver a complete project that can run directly.</code></pre>

<h3>The Result</h3>
<ul>
  <li><strong>Completion Time</strong>: 25 minutes</li>
  <li><strong>Deliverables</strong>: A blog website with 6 visual styles, each supporting light and dark modes, equivalent to 12 display effects</li>
  <li><strong>Functional Modules</strong>: Home page, article list, article details, about us, contact information and theme switching functions are all implemented</li>
  <li><strong>Technical Indicators</strong>: No barrier 100, best practice 100, SEO 100, performance 72</li>
</ul>

<h2 id="project-2">Project 2: Generate a Runnable 3D Racing Game</h2>

<h3>The Prompt</h3>
<pre><code class="language-text">Help me develop a runnable 3D racing game, including:
- Car control
- Track
- Opponent vehicles
- Timing ranking
- Collision effect
- Restart function

The picture should have a sense of speed, support keyboard control and computer browser operation, and finally deliver a complete runnable project.</code></pre>

<h3>The Result</h3>
<ul>
  <li><strong>Completion Time</strong>: 40 minutes</li>
  <li><strong>Deliverables</strong>: A 3D racing game that can be run directly, including README documentation</li>
  <li><strong>Functional Modules</strong>: Car control, track, opponent vehicles, timing ranking, collision, drift, sound effect and restart functions are all implemented</li>
  <li><strong>Game Experience</strong>: The game can be run directly, but the visual effects such as the car model, mountains and clouds are not very realistic. The speed display is very real, and the wind effect is simulated when the car is running.</li>
</ul>

<h2 id="conclusion">Conclusion</h2>
<p>DeepSeek V4 Pro has a good project completion, but whether the price of nearly 3 times is worth it depends on whether you pay more attention to delivery capability or cost performance.</p>
<p>We will continue to test new models with the same set of real project acceptance methods in the future, not just looking at benchmarks, but directly seeing if it can deliver the project.</p>

<h2>常见问题</h2>

<h3>What is DeepSeek V4 Pro 0813, and how is it different from V4 Flash?</h3>
<p>V4 Pro 0813 is the newest DeepSeek release, positioned above V4 Flash in capability. It supports a 384K maximum output, has thinking mode enabled by default (with a non-thinking option), and costs roughly 3 times as much as V4 Flash. In benchmark scores it lands between V4 Flash 0731 and the top-tier Fable 5 — stronger than Flash but not the absolute ceiling. The real difference shows up in delivery: it handled both projects in this test — a 6-style blog in 25 minutes and a 3D racing game in 40 minutes — with solid functional completeness, which is the practical advantage Pro brings over Flash for full-project tasks.</p>

<h3>Are these test projects actually runnable, or just mockups?</h3>
<p>Both are fully runnable deliverables. The blog is a complete website with 6 switchable visual styles, each supporting light and dark modes for 12 total display effects, covering home, article list, article details, about, and contact pages with theme switching — scoring 100 on accessibility, best practices, and SEO. The 3D racing game runs directly in the browser with keyboard control, car physics, track, opponent vehicles, timing ranking, collisions, drifting, sound effects, and restart, plus README documentation. The visual polish of the game (car model, mountains, clouds) is noted as the weakest point, but everything works as delivered.</p>

<h3>Is the ~3x price of V4 Pro worth paying over V4 Flash?</h3>
<p>It depends on what you value. If you're optimizing for cost on high-volume or repetitive tasks, V4 Flash remains the better value. If you're building complete projects — a whole website or a full game from a single prompt — V4 Pro 0813 delivered both here without hand-holding, which is where the premium pays off. The practical guidance from this test: match the model to the task. Use Pro when delivery speed and completeness matter; use Flash when cost per token dominates your decision.</p>

<h3>Should beginners use V4 Pro 0813?</h3>
<p>Yes, for the reason this article demonstrates: you can write a plain-language prompt in natural language and get a complete, runnable project back without deep coding knowledge. The blog prompt in this test was a simple feature list, and the game prompt was six bullet points. That's an approachable entry point for beginners who want real output rather than studying theory. The main caveat is cost — at 3x Flash pricing, beginners iterating a lot may want to prototype on Flash first and reserve Pro for final project generation.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Want to put DeepSeek to work? Continue with these guides:</p>
  <ul>
    <li><a href="/article/deepseek-v4-flash-official-release-practical-guide">DeepSeek V4 Flash Official Release: A Practical Guide to the Game-Changing AI Model</a> — the full breakdown of DeepSeek's cost-efficient flagship release</li>
    <li><a href="/article/deepseek-v4-flash-vs-gpt-5-6-luna-codex-integration-benchmark">DeepSeek V4 Flash vs GPT-5.6 Luna: Codex Integration & 10-Round Benchmark</a> — a head-to-head capability test of DeepSeek against OpenAI's top model</li>
    <li><a href="/article/deepseek-v4-cost-effective">DeepSeek V4: The Cost-Effective King of AI Models for Developers</a> — why DeepSeek became developers' default choice for cost-effective coding</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">📰 AI新闻</span>
  <span class="meta-badge">🕒 阅读约6分钟</span>
  <span class="meta-badge">📅 2026年8月13日</span>
  <span class="meta-badge">🎯 入门</span>
</div>

<h2 id="introduction">引言</h2>
<p>DeepSeek已正式发布V4 Pro 0813模型。我们不再只盯着参数和基准分数，而是用两个真实项目测试它的实际编程能力。</p>

<h2 id="core-info">新模型核心信息</h2>
<ul>
  <li><strong>最大输出</strong>：384K</li>
  <li><strong>思考模式</strong>：支持思考与非思考模式，默认启用思考模式</li>
  <li><strong>定价</strong>：约为V4 Flash的3倍</li>
  <li><strong>基准分数</strong>：基准表左侧为预估分，右侧为准确分。V4 Pro 0813的分数高于V4 Flash 0731，但未超过Fable 5。</li>
</ul>

<h2 id="project-1">项目1：开发一个6种样式的个人博客</h2>

<h3>提示词</h3>
<pre><code class="language-text">帮我设计并开发一个现代个人博客网站，提供6种可切换的视觉风格：
- 极简黑白
- 科技未来
- 温暖复古
- 清晰深色
- 你认为合适的其他风格

网站应包括：
- 首页
- 文章列表
- 文章详情
- 关于我们
- 联系方式

每种风格在颜色、字体和布局上应有明显差异，并支持电脑和移动端。添加风格切换按钮、明暗模式和流畅的过渡动画。
请使用真实的示例内容和图片，界面简洁有设计感，最终交付一个可以直接运行的项目。</code></pre>

<h3>测试结果</h3>
<ul>
  <li><strong>完成时间</strong>：25分钟</li>
  <li><strong>交付物</strong>：一个拥有6种视觉风格的博客网站，每种风格都支持明暗模式，相当于12种显示效果</li>
  <li><strong>功能模块</strong>：首页、文章列表、文章详情、关于我们、联系方式和主题切换功能全部实现</li>
  <li><strong>技术指标</strong>：无障碍100、最佳实践100、SEO 100、性能72</li>
</ul>

<h2 id="project-2">项目2：生成一个可运行的3D赛车游戏</h2>

<h3>提示词</h3>
<pre><code class="language-text">帮我开发一个可运行的3D赛车游戏，包括：
- 赛车控制
- 赛道
- 对手车辆
- 计时排名
- 碰撞效果
- 重新开始功能

画面要有速度感，支持键盘控制和电脑浏览器运行，最终交付一个完整可运行的项目。</code></pre>

<h3>测试结果</h3>
<ul>
  <li><strong>完成时间</strong>：40分钟</li>
  <li><strong>交付物</strong>：一个可直接运行的3D赛车游戏，含README文档</li>
  <li><strong>功能模块</strong>：赛车控制、赛道、对手车辆、计时排名、碰撞、漂移、音效和重新开始功能全部实现</li>
  <li><strong>游戏体验</strong>：游戏可直接运行，但赛车模型、山体和云朵等视觉效果不够逼真。速度显示非常真实，赛车行驶时模拟了风声效果。</li>
</ul>

<h2 id="conclusion">结语</h2>
<p>DeepSeek V4 Pro的项目完成度不错，但接近3倍的价格是否值得，取决于你更看重交付能力还是性价比。</p>
<p>未来我们将继续用同一套真实项目验收方法测试新模型，不只是看基准分数，而是直接看它能否交付项目。</p>

<h2>常见问题</h2>

<h3>什么是DeepSeek V4 Pro 0813？它和V4 Flash有什么不同？</h3>
<p>V4 Pro 0813是DeepSeek的最新发布，定位在V4 Flash之上。它支持384K最大输出，默认启用思考模式（可切换非思考模式），价格约为V4 Flash的3倍。基准分数介于V4 Flash 0731和顶级模型Fable 5之间——比Flash强，但不是绝对上限。真正的差异体现在交付能力上：它在本次测试中完成了两个项目——25分钟做完6风格博客、40分钟做出3D赛车游戏——功能完整度很高，这正是Pro在整项目任务中相对于Flash的实际优势。</p>

<h3>这些测试项目真的能运行吗，还是只是演示稿？</h3>
<p>两个都是可运行的完整交付物。博客是完整的网站，拥有6种可切换的视觉风格，每种都支持明暗模式，共12种显示效果，覆盖首页、文章列表、文章详情、关于和联系页面，并带主题切换——无障碍、最佳实践和SEO都拿到100分。3D赛车游戏可直接在浏览器运行，支持键盘控制、赛车物理、赛道、对手车辆、计时排名、碰撞、漂移、音效和重新开始，并附README文档。游戏在视觉精致度上（赛车模型、山体、云朵）被指为最弱环节，但一切功能都按交付可用。</p>

<h3>V4 Pro约3倍的价格相对于V4 Flash值得吗？</h3>
<p>取决于你看重什么。如果你在做高频或重复性任务时追求成本最优，V4 Flash仍然是更好的选择。如果你要构建完整项目——从一个提示词做出整个网站或完整游戏——V4 Pro 0813在本次测试中无需干预就交付了这两者，这正是溢价物有所值之处。本次测试的实用建议：按任务匹配模型。交付速度和完整性重要时用Pro；每Token成本主导决策时用Flash。</p>

<h3>初学者应该使用V4 Pro 0813吗？</h3>
<p>应该，原因正是本文演示的：你可以用自然语言写一个提示词，无需深厚的编程知识就能拿回完整可运行的项目。本次测试中的博客提示词就是一个简单的功能清单，游戏提示词只有六个要点。这对想获得真实产出而非研究理论的初学者来说是很好的切入点。主要的注意事项是成本——在3倍Flash价格下，频繁迭代的初学者可以先用Flash做原型，把Pro留给最终项目生成。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>想让DeepSeek帮你干活？继续阅读这些指南：</p>
  <ul>
    <li><a href="/article/deepseek-v4-flash-official-release-practical-guide">DeepSeek V4 Flash正式发布：变革性AI模型实用指南</a> — DeepSeek高性价比旗舰发布的完整解读</li>
    <li><a href="/article/deepseek-v4-flash-vs-gpt-5-6-luna-codex-integration-benchmark">DeepSeek V4 Flash vs GPT-5.6 Luna：Codex接入与10轮实测</a> — DeepSeek与OpenAI顶级模型的正面能力对决</li>
    <li><a href="/article/deepseek-v4-cost-effective">DeepSeek V4：开发者性价比之王AI模型</a> — 为什么DeepSeek成为开发者高性价比编程的默认选择</li>
  </ul>
</div>`,
  },

'''
last = c.rfind('};')
with open('src/lib/article-content.ts', 'w', encoding='utf-8') as f: f.write(c[:last] + n + '};')
print('Part 2 done\n=== Done ===')
