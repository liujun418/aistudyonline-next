"""Publish Aug 10, 2026 — 1 article, no new tools."""
import os; BASE = r"C:\Users\jun\aistudyonline-next"; os.chdir(BASE)

with open('src/lib/articles.ts', 'r', encoding='utf-8') as f: s = f.read()
a = r"""  {
    slug: "codex-skill-bundle-4-skills-professional-websites-one-prompt",
    title: "Codex Skill Bundle: 4 Skills to Build Professional Websites in One Prompt",
    titleZh: "Codex技能包：4个技能让一条提示词生成专业网站",
    description: "Install four skills into Codex to generate professional websites in a single prompt — Taste Skill for design aesthetics, GSAP for smooth animations, Ponytail for clean minimal code, and Playwright MCP for automated testing.",
    descriptionZh: "为Codex安装四个技能，一条提示词生成专业网站——Taste Skill解决设计美学、GSAP实现流畅动画、Ponytail保证代码极简、Playwright MCP自动测试。",
    category: "ai-tutorials",
    tags: ["Codex", "Skills", "Web Development", "Frontend", "GSAP", "Playwright", "Testing"],
    difficulty: "beginner",
    toolsMentioned: ["Codex Agent", "Playwright"],
    date: "2026-08-10",
  },

"""
last = s.rfind('];')
with open('src/lib/articles.ts', 'w', encoding='utf-8') as f: f.write(s[:last] + a + '];')
print('Part 1 done')

with open('src/lib/article-content.ts', 'r', encoding='utf-8') as f: c = f.read()
n = r'''
  "codex-skill-bundle-4-skills-professional-websites-one-prompt": {
    content: `<div class="meta-banner">
  <span class="meta-badge">📖 AI Tutorials</span>
  <span class="meta-badge">🕒 7 min read</span>
  <span class="meta-badge">📅 Aug 10, 2026</span>
  <span class="meta-badge">🎯 Beginner</span>
</div>

<h2 id="introduction">Introduction</h2>
<p>If you've ever wondered why some Codex users can generate a polished, professional website with a single prompt — while your AI keeps spitting out generic blue buttons on white backgrounds — the answer is simple: they've pre-installed four critical skills into Codex. These four skills form a complete, end-to-end web development workflow that eliminates common AI frontend flaws, improves animation quality, enforces clean code, and adds automated testing.</p>

<h2 id="taste">1. Taste Skill: Fix AI Design Aesthetics</h2>

<h3>What it does</h3>
<p>Taste Skill is an anti-slop frontend framework that trains AI to produce professional design output. It constrains AI's layout decisions, ensuring proper spacing, color harmony, and clear visual hierarchy. This removes the generic "AI-generated" look from your pages.</p>

<h3>How to install</h3>
<pre><code class="language-bash"># Install the full skill bundle
npx skills add Leonxlnx/taste-skill -a codex

# Or install only the core frontend design skill
npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"</code></pre>

<h3>How to use</h3>
<p>Once installed, Codex will automatically apply Taste Skill guidelines when generating UI. You can also explicitly reference it in your prompt:</p>
<blockquote>"Use Taste Skill principles to design a SaaS landing page with balanced whitespace and modern typography."</blockquote>

<h3>What you'll get</h3>
<ul>
  <li>Professional layout with intentional spacing</li>
  <li>Cohesive color palettes</li>
  <li>Clear visual hierarchy</li>
  <li>No generic AI-generated look</li>
</ul>

<h2 id="gsap">2. GSAP Skill: Professional Web Animations</h2>

<h3>What it does</h3>
<p>GSAP Skill teaches Codex to create smooth, professional animations instead of the stiff, robotic movements typical of AI-generated code. It handles scroll-triggered animations, timeline-based element entrance effects, and complex motion sequences.</p>

<h3>How to install</h3>
<pre><code class="language-bash"># Clone the repository
git clone https://github.com/Microck/gsap-skills.git ~/gsap-skills

# Copy skills to Codex directory
mkdir -p ~/.config/opencode/skills
rsync -a --delete ~/gsap-skills/skills/ ~/.config/opencode/skills/

# Optional: Copy the gsap command
mkdir -p ~/.config/opencode/command
cp ~/gsap-skills/command/gsap.md ~/.config/opencode/command/</code></pre>

<h3>How to use</h3>
<p>Ask Codex to use GSAP for animations:</p>
<blockquote>"Add scroll-triggered animations to this page using GSAP Skill. Make the elements stagger in with smooth easing."</blockquote>

<h3>What you'll get</h3>
<ul>
  <li>Smooth scroll-triggered animations</li>
  <li>Professional timeline sequences</li>
  <li>Staggered element entrance effects</li>
  <li>No stiff, robotic animations</li>
</ul>

<h2 id="ponytail">3. Ponytail: Enforce Clean, Minimal Code</h2>

<h3>What it does</h3>
<p>Ponytail makes your AI agent think like the laziest senior developer in the room. It encourages code reuse, minimalism, and engineering best practices — so you get the same functionality with less, cleaner code.</p>

<h3>How to install</h3>
<pre><code class="language-bash"># Add the marketplace
codex plugin marketplace add DietrichGebert/ponytail

# Install the plugin
codex</code></pre>
<p>Then in Codex:</p>
<ol>
  <li>Open <code>/plugins</code></li>
  <li>Select Ponytail and install</li>
  <li>Open <code>/hooks</code></li>
  <li>Trust both lifecycle hooks</li>
  <li>Restart Codex</li>
</ol>

<h3>How to use</h3>
<p>Ponytail works automatically once installed. You can also explicitly reference it:</p>
<blockquote>"Use Ponytail principles to refactor this code. Prioritize reuse and minimalism."</blockquote>

<h3>What you'll get</h3>
<ul>
  <li>54% less code (per project benchmarks)</li>
  <li>Better code reuse</li>
  <li>More maintainable architecture</li>
  <li>Same functionality with fewer lines</li>
</ul>

<h2 id="playwright">4. Playwright MCP: Automated Web Testing</h2>

<h3>What it does</h3>
<p>Playwright MCP teaches Codex to test the websites it generates. It can automatically open browsers, simulate clicks, take screenshots, check for issues, and fix problems — all without manual intervention.</p>

<h3>How to install</h3>
<pre><code class="language-bash"># Add to Codex config
codex mcp add playwright npx -y @playwright/mcp@latest

# Verify installation
codex mcp list</code></pre>
<p>Or manually edit <code>~/.codex/config.toml</code>:</p>
<pre><code class="language-toml">[mcp_servers.playwright]
command = "npx"
args = ["-y", "@playwright/mcp@latest"]</code></pre>

<h3>How to use</h3>
<p>Ask Codex to test your website:</p>
<blockquote>"Use Playwright MCP to test this website. Check for broken links, responsive design issues, and console errors."</blockquote>

<h3>What you'll get</h3>
<ul>
  <li>Automated browser testing</li>
  <li>Screenshot verification</li>
  <li>Click simulation</li>
  <li>Automatic bug fixing</li>
  <li>Regression testing</li>
</ul>

<h2 id="workflow">The Complete Workflow</h2>
<p>When used together, these four skills create a full web development pipeline:</p>
<ol>
  <li><strong>Taste Skill</strong> ensures the design looks professional</li>
  <li><strong>GSAP Skill</strong> adds smooth, polished animations</li>
  <li><strong>Ponytail</strong> keeps the code clean and minimal</li>
  <li><strong>Playwright MCP</strong> tests and fixes issues automatically</li>
</ol>
<p>This is why some Codex users can generate a complete, high-quality website in one prompt — they've given their AI the right tools to do the job properly.</p>

<h2 id="conclusion">Final Takeaway</h2>
<p>Install these four skills today and transform your Codex from a basic code generator into a professional web development assistant.</p>

<h2>常见问题</h2>

<h3>Do I need all four skills, or can I install them individually?</h3>
<p>You can install any subset depending on your goals. Each skill solves one distinct problem: Taste Skill fixes the generic AI design look, GSAP replaces stiff robotic animations with professional motion, Ponytail cuts code volume by up to 54%, and Playwright MCP adds automated browser testing. If you're building landing pages or client-facing sites, Taste + GSAP gives the biggest visible improvement fastest. If you're maintaining a larger codebase, Ponytail + Playwright MCP matter more for quality and reliability. For the full "one prompt → professional website" experience described in this article, install all four — they complement each other and together cover the complete build → animate → refactor → test pipeline.</p>

<h3>Are these skills compatible with other AI coding tools besides Codex?</h3>
<p>Partially. Taste Skill and GSAP Skill are skill-package based and work with any agent that supports the standard skills format (the install commands show the Codex / OpenCode variants, but the same packages can be adapted to Claude Code, Cursor, and other skill-capable agents). Ponytail is distributed as a Codex-specific plugin marketplace, so it requires Codex or OpenCode's plugin system. Playwright MCP uses the standard MCP protocol — because MCP is an open standard, the same <code>@playwright/mcp</code> server can be wired into Codex, Claude Code, and other MCP-compatible agents via their config files. If you switch agents often, the skill packages and MCP servers are the most portable; the Codex plugin is the most locked-in.</p>

<h3>Will adding these skills slow down my Codex workflow?</h3>
<p>Negligibly. The skills are lightweight instruction sets and hooks — they add guidance and lifecycle checks, not heavy processing. The main perceived difference is that generated websites look dramatically better and need fewer manual fix rounds, which usually makes the overall workflow <em>faster</em> despite the one-time installation cost of a few minutes. Ponytail's hooks run during code generation to enforce minimalism, and Playwright MCP runs tests on demand (or when you ask), not continuously. The only real overhead is the initial install (about 5-10 minutes for all four) and the occasional test run, which is far cheaper than manually debugging broken layouts or silently shipping buggy code.</p>

<h3>Do I still need to know web development basics to use these skills effectively?</h3>
<p>No, and that's the point. The skills are designed for prompt-driven workflows: you describe what you want ("a SaaS landing page with balanced whitespace"), and Codex applies the skill rules. You don't need to write CSS, GSAP timelines, or Playwright scripts yourself. However, knowing a little helps you write better prompts and verify results — for example, understanding the difference between scroll-triggered animations and timeline-based entrances lets you describe motion more precisely, and being able to read console errors lets you confirm Playwright MCP's fixes. As a rule of thumb: zero coding skills to start, basic HTML/CSS familiarity to get consistently great results, and that's it.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Equipped Codex for professional sites? Continue building with these guides:</p>
  <ul>
    <li><a href="/articles/codex-website-dev-zero-basis-tutorial">Codex Website Development: Zero-Basis Practical Tutorial and Deployment Guide</a> — the full workflow from coding to deploying a site with Codex</li>
    <li><a href="/articles/master-ai-driven-development-openspec-practical-guide-beginners">Master AI-Driven Development with OpenSpec: A Practical Guide for Beginners</a> — structure complex AI coding projects with spec-driven workflows</li>
    <li><a href="/articles/complete-guide-codex-zero-to-advanced">Complete Guide to Codex: From Zero to Advanced Development Workflow</a> — master every Codex capability, from basics to advanced workflows</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">📖 AI教程</span>
  <span class="meta-badge">🕒 阅读约7分钟</span>
  <span class="meta-badge">📅 2026年8月10日</span>
  <span class="meta-badge">🎯 入门</span>
</div>

<h2 id="introduction">引言</h2>
<p>如果你曾疑惑为什么有些Codex用户能用一个提示词就生成精致的专业网站——而你的AI却总是吐出白底蓝按钮的通用页面——答案很简单：他们给Codex预装了四个关键技能。这四个技能构成了完整的端到端网页开发工作流，消除常见的AI前端缺陷、提升动画质量、强制代码整洁，并增加自动化测试。</p>

<h2 id="taste">1. Taste Skill：修复AI设计美学</h2>

<h3>它的作用</h3>
<p>Taste Skill是一个反"劣质模板"前端框架，训练AI产出专业设计输出。它约束AI的布局决策，确保合理的间距、和谐的色彩和清晰的视觉层级。它从你的页面中消除通用的"AI生成"外观。</p>

<h3>如何安装</h3>
<pre><code class="language-bash"># 安装完整技能包
npx skills add Leonxlnx/taste-skill -a codex

# 或只安装核心前端设计技能
npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"</code></pre>

<h3>如何使用</h3>
<p>安装后，Codex生成UI时会自动应用Taste Skill准则。你也可以在提示词中显式引用它：</p>
<blockquote>"使用Taste Skill原则设计一个SaaS落地页，注重留白平衡和现代排版。"</blockquote>

<h3>你将获得</h3>
<ul>
  <li>有意识间距的专业布局</li>
  <li>协调的色彩方案</li>
  <li>清晰的视觉层级</li>
  <li>不再有通用AI生成外观</li>
</ul>

<h2 id="gsap">2. GSAP Skill：专业Web动画</h2>

<h3>它的作用</h3>
<p>GSAP Skill教Codex创建流畅、专业的动画，而不是AI生成代码中典型的僵硬机械运动。它处理滚动触发动画、基于时间线的元素入场效果和复杂运动序列。</p>

<h3>如何安装</h3>
<pre><code class="language-bash"># 克隆仓库
git clone https://github.com/Microck/gsap-skills.git ~/gsap-skills

# 复制技能到Codex目录
mkdir -p ~/.config/opencode/skills
rsync -a --delete ~/gsap-skills/skills/ ~/.config/opencode/skills/

# 可选：复制gsap命令
mkdir -p ~/.config/opencode/command
cp ~/gsap-skills/command/gsap.md ~/.config/opencode/command/</code></pre>

<h3>如何使用</h3>
<p>让Codex使用GSAP制作动画：</p>
<blockquote>"使用GSAP Skill给这个页面添加滚动触发动画。让元素以平滑缓动交错入场。"</blockquote>

<h3>你将获得</h3>
<ul>
  <li>流畅的滚动触发动画</li>
  <li>专业的时间线序列</li>
  <li>交错的元素入场效果</li>
  <li>不再有僵硬机械动画</li>
</ul>

<h2 id="ponytail">3. Ponytail：强制极简整洁代码</h2>

<h3>它的作用</h3>
<p>Ponytail让你的AI代理像团队里最懒的资深开发者一样思考。它鼓励代码复用、极简主义和工程最佳实践——让你用更少、更整洁的代码实现同样的功能。</p>

<h3>如何安装</h3>
<pre><code class="language-bash"># 添加市场
codex plugin marketplace add DietrichGebert/ponytail

# 安装插件
codex</code></pre>
<p>然后在Codex中：</p>
<ol>
  <li>打开<code>/plugins</code></li>
  <li>选择Ponytail并安装</li>
  <li>打开<code>/hooks</code></li>
  <li>信任两个生命周期钩子</li>
  <li>重启Codex</li>
</ol>

<h3>如何使用</h3>
<p>Ponytail安装后自动生效。你也可以显式引用它：</p>
<blockquote>"使用Ponytail原则重构这段代码。优先考虑复用和极简。"</blockquote>

<h3>你将获得</h3>
<ul>
  <li>减少54%的代码量（按项目基准测试）</li>
  <li>更好的代码复用</li>
  <li>更易维护的架构</li>
  <li>更少的行数实现同样的功能</li>
</ul>

<h2 id="playwright">4. Playwright MCP：自动化Web测试</h2>

<h3>它的作用</h3>
<p>Playwright MCP教Codex测试它生成的网站。它可以自动打开浏览器、模拟点击、截图、检查问题并修复缺陷——全程无需人工干预。</p>

<h3>如何安装</h3>
<pre><code class="language-bash"># 添加到Codex配置
codex mcp add playwright npx -y @playwright/mcp@latest

# 验证安装
codex mcp list</code></pre>
<p>或手动编辑<code>~/.codex/config.toml</code>：</p>
<pre><code class="language-toml">[mcp_servers.playwright]
command = "npx"
args = ["-y", "@playwright/mcp@latest"]</code></pre>

<h3>如何使用</h3>
<p>让Codex测试你的网站：</p>
<blockquote>"使用Playwright MCP测试这个网站。检查死链、响应式设计问题和控制台错误。"</blockquote>

<h3>你将获得</h3>
<ul>
  <li>自动化浏览器测试</li>
  <li>截图验证</li>
  <li>点击模拟</li>
  <li>自动修复Bug</li>
  <li>回归测试</li>
</ul>

<h2 id="workflow">完整工作流</h2>
<p>当这四个技能组合使用时，它们构成了完整的网页开发流水线：</p>
<ol>
  <li><strong>Taste Skill</strong>确保设计看起来专业</li>
  <li><strong>GSAP Skill</strong>添加流畅精致的动画</li>
  <li><strong>Ponytail</strong>保持代码整洁极简</li>
  <li><strong>Playwright MCP</strong>自动测试并修复问题</li>
</ol>
<p>这就是为什么有些Codex用户能用一个提示词生成完整的高质量网站——他们给了AI正确完成工作的工具。</p>

<h2 id="conclusion">总结</h2>
<p>今天就安装这四个技能，把你的Codex从基础代码生成器变成专业网页开发助手。</p>

<h2>常见问题</h2>

<h3>我需要全部四个技能，还是可以单独安装？</h3>
<p>你可以根据目标安装任意子集。每个技能解决一个不同的问题：Taste Skill修复通用AI设计外观，GSAP把僵硬机械的动画替换为专业运动效果，Ponytail减少高达54%的代码量，Playwright MCP增加自动化浏览器测试。如果你在构建落地页或面向客户的网站，Taste + GSAP能最快带来最明显的视觉提升。如果你在维护较大代码库，Ponytail + Playwright MCP对质量和可靠性更重要。要获得本文描述的完整"一条提示词→专业网站"体验，请安装全部四个——它们互补，共同覆盖构建→动画→重构→测试的完整流水线。</p>

<h3>这些技能除了Codex还能用于其他AI编码工具吗？</h3>
<p>部分可以。Taste Skill和GSAP Skill基于技能包格式，适用于任何支持标准技能格式的Agent（安装命令显示的是Codex/OpenCode变体，但相同技能包可适配Claude Code、Cursor等其他支持技能的Agent）。Ponytail以Codex专用插件市场分发，需要Codex或OpenCode的插件系统。Playwright MCP使用标准MCP协议——因为MCP是开放标准，同一个<code>@playwright/mcp</code>服务器可以通过配置文件接入Codex、Claude Code和其他兼容MCP的Agent。如果你经常切换Agent，技能包和MCP服务器最便携；Codex插件绑定最深。</p>

<h3>添加这些技能会拖慢我的Codex工作流吗？</h3>
<p>几乎不会。技能是轻量的指令集和钩子——它们增加的是指导和生命周期检查，不是重型处理。主要感知差异是生成的网站外观明显更好、需要的人工修复轮次更少，这通常让整体工作流<em>更快</em>，尽管一次性安装只需几分钟。Ponytail的钩子在代码生成期间运行以强制极简，Playwright MCP按需（或应你要求）运行测试，不是持续运行。唯一的真实开销是初始安装（四个约5-10分钟）和偶尔的测试运行，远比自己手动调试坏掉的布局或静默上线带Bug的代码便宜。</p>

<h3>我仍然需要了解Web开发基础知识才能有效使用这些技能吗？</h3>
<p>不需要，这正是重点。技能是为提示词驱动的工作流设计的：你描述想要的东西（"一个注重留白平衡的SaaS落地页"），Codex应用技能规则。你不需要自己写CSS、GSAP时间线或Playwright脚本。然而，了解一点有助于你写出更好的提示词并验证结果——例如，理解滚动触发动画和时间线入场之间的区别能让你更精确地描述运动，能够阅读控制台错误可以让你确认Playwright MCP的修复。经验法则：零编码技能即可开始，了解基本HTML/CSS能持续获得出色结果，仅此而已。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>为专业网站配齐了Codex技能？继续用这些指南构建：</p>
  <ul>
    <li><a href="/articles/codex-website-dev-zero-basis-tutorial">Codex网站开发：零基础实战教程与部署指南</a> — 从编码到部署网站的完整工作流</li>
    <li><a href="/articles/master-ai-driven-development-openspec-practical-guide-beginners">用OpenSpec掌握AI驱动开发：新手实操指南</a> — 用规范驱动的工作流结构化复杂AI编码项目</li>
    <li><a href="/articles/complete-guide-codex-zero-to-advanced">Codex完全指南：从零基础到高级开发工作流</a> — 掌握Codex每项能力，从基础到高级工作流</li>
  </ul>
</div>`,
  },

'''
last = c.rfind('};')
with open('src/lib/article-content.ts', 'w', encoding='utf-8') as f: f.write(c[:last] + n + '};')
print('Part 2 done\n=== Done ===')