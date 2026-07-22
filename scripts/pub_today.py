"""
Publish July 22, 2026 — 1 article, no new tools.
"""
import os

BASE = r"C:\Users\jun\aistudyonline-next"
os.chdir(BASE)

with open('src/lib/articles.ts', 'r', encoding='utf-8') as f:
    articles_src = f.read()

new_articles = r"""  {
    slug: "ai-powered-excel-workflow-4-practical-skills-beginners",
    title: "AI-Powered Excel Workflow: 4 Practical Skills for Beginners",
    titleZh: "AI加持Excel工作流：新手必学的4个实用技能",
    description: "Four essential AI+Excel skills for beginners — defining clear requirements to auto-generate tables, identifying and fixing data quality issues, setting business rules for tiered calculations with VBA macros, and asking the right questions to generate interactive HTML dashboards.",
    descriptionZh: "新手必学的四个AI+Excel核心技能——用清晰需求自动生成表格、识别修复数据质量问题、设定业务规则实现阶梯计算+VBA宏、提出正确问题生成交互式HTML仪表盘。",
    category: "AI Tutorials",
    tags: ["Excel", "AI", "Productivity", "Data Analysis", "Beginner", "Tutorial", "Dashboard"],
    difficulty: "beginner",
    toolsMentioned: ["ChatGPT"],
    date: "2026-07-22",
  },

"""

last_bracket = articles_src.rfind('];')
articles_new = articles_src[:last_bracket] + new_articles + '];'

with open('src/lib/articles.ts', 'w', encoding='utf-8') as f:
    f.write(articles_new)

print('Part 1: 1 article added')

with open('src/lib/article-content.ts', 'r', encoding='utf-8') as f:
    content_src = f.read()

new_contents = r'''
  "ai-powered-excel-workflow-4-practical-skills-beginners": {
    content: `<div class="meta-banner">
  <span class="meta-badge">📚 AI Tutorials</span>
  <span class="meta-badge">🕒 5 min read</span>
  <span class="meta-badge">📅 Jul 22, 2026</span>
  <span class="meta-badge">🎯 Beginner</span>
</div>

<h2 id="introduction">Introduction</h2>

<p>AI has revolutionized spreadsheet creation and data analysis, making these tasks accessible to beginners. This guide presents four core skills to master the full workflow of using AI for Excel tasks, from creating tables to generating interactive dashboards.</p>

<h2 id="skill-1">Skill 1: Define Clear Requirements to Create Tables</h2>

<h3>Core Formula</h3>

<p>To create a table, provide three key pieces of information to AI:</p>

<ol>
  <li>Your industry and job role</li>
  <li>The purpose of the table</li>
  <li>Any special requirements</li>
</ol>

<h3>Example</h3>

<p>If you are a home goods salesperson, you can input:</p>

<pre><code class="language-text">I am a home goods salesperson. Create a professional bilingual (Chinese-English) quotation template with USD exchange rate calculation, complete structure, and built-in formulas.</code></pre>

<p>AI will generate a fully functional quotation template with automatic price calculation and exchange rate adjustment.</p>

<h2 id="skill-2">Skill 2: Identify and Fix Issues in Existing Tables</h2>

<h3>Step 1: Analyze Data Quality</h3>

<p>Upload your existing table and use this prompt:</p>

<pre><code class="language-text">List all columns in the table, sample 5 entries from each column, and perform data quality checks for missing values, incorrect formats, and anomalies.</code></pre>

<h3>Step 2: Repair and Optimize</h3>

<p>After AI identifies issues, request repairs:</p>

<pre><code class="language-text">Fix all identified issues, merge related tables, and generate an interactive HTML dashboard.</code></pre>

<h2 id="skill-3">Skill 3: Define Business Rules for Calculations</h2>

<h3>Key Elements</h3>

<p>When calculating data, specify:</p>

<ol>
  <li>What data you have</li>
  <li>What results you need</li>
  <li>The business rules</li>
</ol>

<h3>Example</h3>

<p>For sales commission calculation:</p>

<pre><code class="language-text">This is monthly sales data. Calculate commission (3% for <50k, 5% for 50k-100k, 8% for >100k, tiered calculation), tax, and net pay.</code></pre>

<p>For repeated calculations, create a VBA macro with:</p>

<pre><code class="language-text">Create a one-click VBA macro for commission calculation based on these rules.</code></pre>

<h2 id="skill-4">Skill 4: Ask the Right Questions for Data Analysis</h2>

<h3>Step 1: Clean Data</h3>

<p>Use the data cleaning method from Skill 2 to prepare your dataset.</p>

<h3>Step 2: Generate Analysis</h3>

<p>Ask AI:</p>

<pre><code class="language-text">What key metrics can be calculated from this data? What valuable questions can it answer?</code></pre>

<p>Then request:</p>

<pre><code class="language-text">Calculate these metrics and create corresponding visualizations.</code></pre>

<h3>Step 3: Create Interactive Dashboard</h3>

<p>For reporting:</p>

<pre><code class="language-text">Generate an interactive HTML dashboard with all analysis results and visualizations.</code></pre>

<h3>Pro Tip</h3>

<p>To prepare for stakeholder questions:</p>

<pre><code class="language-text">Act as the audience for this report. What questions would you ask, and how should I answer them?</code></pre>

<h2 id="conclusion">Conclusion</h2>

<p>Mastering these four skills allows beginners to become proficient in AI-powered spreadsheet work. By clearly communicating requirements, fixing issues, defining rules, and asking the right questions, you can efficiently create, analyze, and present data like a professional.</p>

<h2>常见问题</h2>

<h3>Which AI tool should I use for these Excel workflows?</h3>
<p>Any general-purpose AI works — ChatGPT, Claude, Codex, or WorkBuddy. The prompts in this guide are tool-agnostic. For Skill 1 (table creation) and Skill 2 (data quality analysis), a chat interface with file upload capability is ideal. For Skill 3 (VBA macros), Codex or Claude Code can generate and test the macros directly. For Skill 4 (interactive dashboards), any tool that can generate HTML output works. The key difference: tools with local file access (Codex, Claude Code, WorkBuddy) can read your Excel files directly without requiring manual upload, which is faster for large files or frequent iterations.</p>

<h3>Are AI-generated Excel formulas and VBA macros reliable?</h3>
<p>They're reliable for common patterns (SUMIFS, VLOOKUP, pivot tables, tiered commissions) but should be tested before production use. The guide's approach is designed to catch errors early: Skill 2's data quality check identifies formula errors in existing tables, and Skill 3's business rule definition gives the AI explicit logic rather than leaving it to guess. For VBA macros, always test on a copy of your data first. AI-generated macros handle 80% of common Excel automation needs correctly on the first try. For the remaining 20%, a second prompt with the specific error usually fixes it.</p>

<h3>Can I use these skills with Google Sheets instead of Excel?</h3>
<p>Yes — the prompt patterns are identical. For Google Sheets, replace "VBA macro" with "Google Apps Script" in Skill 3. The data quality analysis (Skill 2) and dashboard generation (Skill 4) work the same way since both platforms export to common formats. One advantage of Google Sheets: the AI-generated HTML dashboard can pull live data from your sheet using the Google Sheets API, creating auto-updating dashboards. For Excel, the dashboard is typically a static HTML export that you regenerate when data changes.</p>

<h3>How much Excel knowledge do I need to use these AI skills effectively?</h3>
<p>You need to understand the <strong>business logic</strong> (what commission structure your company uses, what metrics matter to your boss) but not the <strong>technical implementation</strong> (how to write the formula, how to build the dashboard). The guide's design reflects this: every skill starts with you describing what you want in plain language, and the AI handles the technical execution. The most common failure mode is not describing the business rules clearly enough — "calculate commission" is too vague, while "calculate commission at 3% for sales under 50k, 5% for 50k-100k, and 8% above 100k" gives the AI exactly what it needs. If you can explain the rule to a coworker, you can explain it to the AI.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Mastered AI+Excel? Explore more productivity workflows:</p>
  <ul>
    <li><a href="/articles/chatgpt-codex-10-core-features-beginners-work-efficiency">ChatGPT Codex: 10 Core Features for Beginners to Boost Work Efficiency</a> — more practical AI productivity skills</li>
    <li><a href="/articles/practical-guide-tencent-workbuddy-ai-office-assistant">A Practical Guide to Tencent WorkBuddy: Your All-in-One AI Office Assistant</a> — apply these Excel skills in WorkBuddy</li>
    <li><a href="/articles/workbuddy-10-core-skills-beginner-to-advanced">WorkBuddy: 10 Core Skills to Master from Beginner to Advanced</a> — build on your AI productivity foundation</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">📚 AI 教程</span>
  <span class="meta-badge">🕒 阅读约5分钟</span>
  <span class="meta-badge">📅 2026年7月22日</span>
  <span class="meta-badge">🎯 入门</span>
</div>

<h2 id="introduction">引言</h2>

<p>AI彻底改变了电子表格创建和数据分析的方式，让这些任务对新手也变得简单。本指南介绍四个核心技能，帮你掌握用AI处理Excel任务的完整工作流——从创建表格到生成交互式仪表盘。</p>

<h2 id="skill-1">技能1：用清晰需求创建表格</h2>

<h3>核心公式</h3>

<p>创建表格时，向AI提供三个关键信息：</p>

<ol>
  <li>你的行业和职位</li>
  <li>表格的用途</li>
  <li>特殊需求</li>
</ol>

<h3>示例</h3>

<p>如果你是家居用品销售，输入：</p>

<pre><code class="language-text">我是家居用品销售。创建一份专业的中英文双语报价模板，含美元汇率计算、完整结构和内置公式。</code></pre>

<p>AI会生成一个功能完整的报价模板，包含自动价格计算和汇率调整。</p>

<h2 id="skill-2">技能2：识别并修复已有表格的问题</h2>

<h3>第一步：分析数据质量</h3>

<p>上传已有表格，使用此提示词：</p>

<pre><code class="language-text">列出表格中的所有列，每列抽查5条数据，执行数据质量检查：缺失值、格式错误、异常值。</code></pre>

<h3>第二步：修复与优化</h3>

<p>AI识别问题后，请求修复：</p>

<pre><code class="language-text">修复所有识别出的问题，合并关联表格，生成交互式HTML仪表盘。</code></pre>

<h2 id="skill-3">技能3：定义业务规则进行计算</h2>

<h3>关键要素</h3>

<p>计算数据时，明确说明：</p>

<ol>
  <li>你有什么数据</li>
  <li>你需要什么结果</li>
  <li>业务规则是什么</li>
</ol>

<h3>示例</h3>

<p>销售佣金计算：</p>

<pre><code class="language-text">这是月度销售数据。计算佣金（<5万提3%，5-10万提5%，>10万提8%，阶梯计算）、个税和实发工资。</code></pre>

<p>重复计算用VBA宏：</p>

<pre><code class="language-text">根据这些规则创建一键佣金计算的VBA宏。</code></pre>

<h2 id="skill-4">技能4：提出正确问题做数据分析</h2>

<h3>第一步：清洗数据</h3>

<p>用技能2的数据清洗方法准备好数据集。</p>

<h3>第二步：生成分析</h3>

<p>问AI：</p>

<pre><code class="language-text">这份数据可以算出哪些关键指标？能回答什么有价值的问题？</code></pre>

<p>然后请求：</p>

<pre><code class="language-text">计算这些指标并创建对应的可视化图表。</code></pre>

<h3>第三步：创建交互式仪表盘</h3>

<p>用于汇报：</p>

<pre><code class="language-text">生成包含所有分析结果和可视化的交互式HTML仪表盘。</code></pre>

<h3>进阶技巧</h3>

<p>为应对领导提问做准备：</p>

<pre><code class="language-text">以这份报告的受众视角，你会提出哪些问题？我该如何回答？</code></pre>

<h2 id="conclusion">总结</h2>

<p>掌握这四项技能，新手也能熟练运用AI处理电子表格工作。通过清晰沟通需求、修复问题、定义规则和提出正确问题，你可以像专业人士一样高效地创建、分析和展示数据。</p>

<h2>常见问题</h2>

<h3>这些Excel工作流该用哪个AI工具？</h3>
<p>任何通用AI都行——ChatGPT、Claude、Codex或WorkBuddy。本指南的提示词与工具无关。技能1（表格创建）和技能2（数据质量分析）最好用支持文件上传的聊天界面。技能3（VBA宏），Codex或Claude Code可直接生成并测试宏。技能4（交互式仪表盘），任何能生成HTML输出的工具都行。关键区别：有本地文件访问权限的工具（Codex、Claude Code、WorkBuddy）可直接读取Excel文件无需手动上传，处理大文件或频繁迭代时更快。</p>

<h3>AI生成的Excel公式和VBA宏可靠吗？</h3>
<p>常见模式（SUMIFS、VLOOKUP、数据透视表、阶梯佣金）很可靠，但生产使用前应该测试。本指南的方法旨在及早发现错误：技能2的数据质量检查可在已有表格中识别公式错误，技能3的业务规则定义给AI明确的逻辑而非靠它猜测。VBA宏务必先在数据副本上测试。AI生成的宏首次就能正确处理80%的常见Excel自动化需求。剩下20%，第二个提示词说明具体错误通常就能修复。</p>

<h3>这些技能能用于Google Sheets而非Excel吗？</h3>
<p>可以——提示词模式完全一样。Google Sheets中，技能3的"VBA宏"替换为"Google Apps Script"。数据质量分析（技能2）和仪表盘生成（技能4）工作方式相同，因为两个平台都导出为通用格式。Google Sheets的一个优势：AI生成的HTML仪表盘可以通过Google Sheets API拉取实时数据，创建自动更新的仪表盘。Excel中仪表盘通常是静态HTML导出，数据变化时需要重新生成。</p>

<h3>有效使用这些AI技能需要多少Excel知识？</h3>
<p>你需要理解<strong>业务逻辑</strong>（公司用什么佣金结构、什么指标对老板重要），但不需要懂<strong>技术实现</strong>（怎么写公式、怎么搭仪表盘）。本指南的设计反映了这一点：每个技能都从你用自然语言描述需求开始，AI处理技术执行。最常见失败模式是业务规则描述不够清晰——"算佣金"太模糊，而"销售额5万以下提3%、5-10万提5%、10万以上提8%"给了AI完全所需信息。如果你能给同事讲清楚规则，就能给AI讲清楚。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>掌握了AI+Excel？探索更多生产力工作流：</p>
  <ul>
    <li><a href="/articles/chatgpt-codex-10-core-features-beginners-work-efficiency">ChatGPT Codex：新手必学的10个核心提效功能</a> — 更多实用AI生产力技能</li>
    <li><a href="/articles/practical-guide-tencent-workbuddy-ai-office-assistant">腾讯WorkBuddy实操指南：一站式AI办公助手完全上手</a> — 在WorkBuddy中应用这些Excel技能</li>
    <li><a href="/articles/workbuddy-10-core-skills-beginner-to-advanced">WorkBuddy十大核心技能：从入门到精通</a> — 夯实你的AI生产力基础</li>
  </ul>
</div>`,
  },

'''

last_brace = content_src.rfind('};')
content_new = content_src[:last_brace] + new_contents + '};'

with open('src/lib/article-content.ts', 'w', encoding='utf-8') as f:
    f.write(content_new)

print('Part 2: 1 article content added')
print('\n=== Done ===')