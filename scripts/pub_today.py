"""
Publish July 26, 2026 — 1 article, no new tools.
"""
import os; BASE = r"C:\Users\jun\aistudyonline-next"; os.chdir(BASE)

with open('src/lib/articles.ts', 'r', encoding='utf-8') as f: articles_src = f.read()
new_articles = r"""  {
    slug: "ai-powered-spreadsheet-creation-future-office-productivity",
    title: "AI-Powered Spreadsheet Creation: The Future of Office Productivity",
    titleZh: "AI驱动电子表格创建：未来办公生产力的革命",
    description: "A practical guide to AI-powered spreadsheet creation — from choosing AI tools and providing profession-specific requirements, to advanced use cases like e-commerce operation tables, expense report processing, and data visualization with interactive charts.",
    descriptionZh: "AI驱动电子表格创建实操指南——从选择AI工具、按职业提供需求，到电商运营表、费用报销处理和数据可视化等进阶场景。",
    category: "AI Use Cases",
    tags: ["AI", "Spreadsheet", "Excel", "Productivity", "Office", "Automation", "Beginner"],
    difficulty: "beginner",
    toolsMentioned: ["Doubao"],
    date: "2026-07-26",
  },

"""
last_bracket = articles_src.rfind('];')
with open('src/lib/articles.ts', 'w', encoding='utf-8') as f: f.write(articles_src[:last_bracket] + new_articles + '];')
print('Part 1: 1 article added')

with open('src/lib/article-content.ts', 'r', encoding='utf-8') as f: content_src = f.read()
new_contents = r'''
  "ai-powered-spreadsheet-creation-future-office-productivity": {
    content: `<div class="meta-banner">
  <span class="meta-badge">💼 AI Use Cases</span>
  <span class="meta-badge">🕒 4 min read</span>
  <span class="meta-badge">📅 Jul 26, 2026</span>
  <span class="meta-badge">🎯 Beginner</span>
</div>

<h2 id="introduction">Introduction</h2>

<p>Creating spreadsheets is a tedious task that often requires hours of manual work, formula memorization, and data verification. However, AI is transforming this process, making it faster, more accurate, and accessible to everyone.</p>

<h2 id="struggle">The Traditional Spreadsheet Struggle</h2>

<p>Traditionally, spreadsheet creation involves hours of copying and pasting data, memorizing complex formulas, manually verifying data entry, and spending excessive time on data organization. These tasks are time-consuming and prone to human error, especially for beginners.</p>

<h2 id="ai-solution">The AI Solution</h2>

<p>AI tools can now handle all these spreadsheet tasks automatically. With just a few simple steps, you can create professional-looking spreadsheets in minutes.</p>

<h3>Step 1: Choose Your AI Tool</h3>
<p>Select an AI assistant with spreadsheet capabilities, such as Doubao.</p>

<h3>Step 2: Access the AI Spreadsheet Feature</h3>
<p>In the chat interface, select the "AI Spreadsheet" option.</p>

<h3>Step 3: Provide Your Requirements</h3>
<p>Enter your profession and the type of spreadsheet you need. For example:</p>
<pre><code class="language-text">I am a company manager, please create an employee roster with data anonymization</code></pre>

<h3>Step 4: Receive Your Spreadsheet</h3>
<p>The AI will generate a complete spreadsheet with all information neatly organized.</p>

<h3>Step 5: Customize with Simple Commands</h3>
<p>If you need to modify the spreadsheet, simply describe your request:</p>
<pre><code class="language-text">Sort the hire date column from oldest to newest</code></pre>

<h2 id="advanced">Advanced Use Cases</h2>

<h3>1. Complex E-commerce Operation Tables</h3>
<p>AI can create detailed operation tables with clear task modules, priority sorting, progress tracking, status indicators, additional team member information sheets, and data dashboards.</p>

<h3>2. Expense Report Processing</h3>
<p>For messy files like company receipts:</p>
<ol>
  <li>Upload all receipt files to the AI</li>
  <li>Provide the command:</li>
</ol>
<pre><code class="language-text">Extract key information from these receipts and create a professional expense report spreadsheet with data classification</code></pre>
<ol start="3">
  <li>The AI will generate an expense summary table, a detailed travel itinerary table, and all data properly organized and anonymized.</li>
</ol>

<h3>3. Data Visualization</h3>
<p>AI can also transform spreadsheet data into interactive charts:</p>
<pre><code class="language-text">Create interactive charts to highlight key data trends</code></pre>

<h2 id="benefits">Benefits of AI Spreadsheet Creation</h2>
<ul>
  <li><strong>Speed</strong>: Create spreadsheets in minutes instead of hours</li>
  <li><strong>Accuracy</strong>: Eliminate human error in data entry</li>
  <li><strong>Accessibility</strong>: No need to memorize complex formulas</li>
  <li><strong>Professional Quality</strong>: Generate polished, well-organized spreadsheets</li>
  <li><strong>Customization</strong>: Easily modify with simple commands</li>
</ul>

<h2 id="conclusion">Conclusion</h2>
<p>AI is revolutionizing spreadsheet creation, making it accessible to everyone regardless of their Excel skills. Whether you're a beginner or an experienced professional, AI tools can help you save time, reduce errors, and create better spreadsheets.</p>

<h2>常见问题</h2>

<h3>Which AI tool is best for spreadsheet creation?</h3>
<p>For Chinese users, <strong>Doubao</strong> (mentioned in this guide) has a built-in AI Spreadsheet feature that's the most accessible — it's free, requires no setup, and the Chinese-language interface is intuitive. <strong>WorkBuddy</strong> has stronger Excel file operation capabilities (direct local file access, batch processing, VBA macro generation). <strong>ChatGPT/Codex</strong> can generate Excel formulas, VBA macros, and HTML dashboards from natural language. For simple table creation, Doubao is fastest. For complex data processing and integration with existing Excel workflows, WorkBuddy or Codex are better choices. The guide's principles (profession + requirements → AI generates) work across all tools.</p>

<h3>How is this different from the July 22 AI Excel Skills article?</h3>
<p>The July 22 article focused on <strong>skills</strong> — specific prompt patterns for data quality analysis, business rule calculations, and dashboard generation. This article focuses on the <strong>workflow</strong> — the end-to-end process of going from a vague need ("I need a spreadsheet") to a finished product. It also covers use cases the previous article didn't: e-commerce operation tables, expense report processing from receipts, and the profession-specific approach (telling AI your role for better context). The two articles are complementary: read this one for the 5-step process, then read the July 22 article for advanced prompt techniques.</p>

<h3>Can AI handle sensitive data in spreadsheets (like employee information)?</h3>
<p>Yes, with caveats. The guide explicitly mentions "data anonymization" in the employee roster example. AI tools can mask or replace sensitive fields (names → Employee IDs, phone numbers → masked digits, salaries → ranges). However, the security of this depends on your tool: <strong>cloud-based tools</strong> (Doubao, ChatGPT) process data on their servers — avoid uploading truly sensitive data. <strong>Local tools</strong> (WorkBuddy, Claude Code, Codex with local mode) process data on your machine — safer for internal documents. For any sensitive data, use the anonymization prompt pattern: "Create a spreadsheet with [purpose] and anonymize all personal information (replace names with IDs, mask contact details, use salary ranges instead of exact figures)."</p>

<h3>What if the AI generates incorrect formulas or data?</h3>
<p>Always verify. The guide's "customize with simple commands" step (Step 5) is designed for quick corrections — if a formula is wrong, describe the expected behavior and the AI will fix it. For complex spreadsheets, use these verification prompts: "Check all formulas in this spreadsheet for errors" and "Verify that the totals in column X match the sum of individual entries." The AI can self-audit if you ask it to. For critical business spreadsheets, always do a manual spot-check of 5-10 data points before sharing. AI-generated spreadsheets are a starting point, not a finished product — the human review step is essential.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Mastered AI spreadsheets? Explore more office productivity:</p>
  <ul>
    <li><a href="/articles/ai-powered-excel-workflow-4-practical-skills-beginners">AI-Powered Excel Workflow: 4 Practical Skills for Beginners</a> — advanced prompt techniques for Excel</li>
    <li><a href="/articles/chatgpt-codex-10-core-features-beginners-work-efficiency">ChatGPT Codex: 10 Core Features for Beginners</a> — more AI office productivity features</li>
    <li><a href="/articles/practical-guide-tencent-workbuddy-ai-office-assistant">A Practical Guide to Tencent WorkBuddy</a> — use WorkBuddy for local spreadsheet automation</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">💼 AI 应用</span>
  <span class="meta-badge">🕒 阅读约4分钟</span>
  <span class="meta-badge">📅 2026年7月26日</span>
  <span class="meta-badge">🎯 入门</span>
</div>

<h2 id="introduction">引言</h2>

<p>创建电子表格是一项繁琐的任务，通常需要数小时的手动工作、公式记忆和数据验证。然而，AI正在改变这一过程，使其更快、更准确、人人可用。</p>

<h2 id="struggle">传统电子表格的困境</h2>
<p>传统电子表格创建涉及数小时的复制粘贴数据、记忆复杂公式、手动验证数据输入和大量时间花在数据整理上。这些任务耗时且容易出错，对新手尤甚。</p>

<h2 id="ai-solution">AI解决方案</h2>
<p>AI工具现在可以自动处理所有这些电子表格任务。只需几个简单步骤，几分钟内就能创建专业外观的电子表格。</p>

<h3>步骤1：选择AI工具</h3>
<p>选择有电子表格能力的AI助手，如豆包。</p>

<h3>步骤2：访问AI电子表格功能</h3>
<p>在聊天界面中选择"AI电子表格"选项。</p>

<h3>步骤3：提供需求</h3>
<p>输入你的职业和需要的电子表格类型。例如：</p>
<pre><code class="language-text">我是一名公司管理者，请创建一份员工花名册并进行数据脱敏</code></pre>

<h3>步骤4：接收电子表格</h3>
<p>AI将生成一份完整电子表格，所有信息排列整齐。</p>

<h3>步骤5：用简单指令自定义</h3>
<p>需要修改时，直接描述需求：</p>
<pre><code class="language-text">将入职日期列从早到晚排序</code></pre>

<h2 id="advanced">进阶场景</h2>

<h3>1. 复杂电商运营表</h3>
<p>AI可创建详细运营表，包含清晰的任务模块、优先级排序、进度跟踪、状态指示器、团队信息附表和数据分析仪表盘。</p>

<h3>2. 费用报销处理</h3>
<p>处理公司收据等杂乱文件：上传所有收据文件→输入指令"从这些收据中提取关键信息，创建专业费用报销电子表格并进行数据分类"→AI生成费用汇总表、详细行程表和所有数据妥善整理并脱敏。</p>

<h3>3. 数据可视化</h3>
<p>AI可将电子表格数据转化为交互式图表："创建交互式图表以突出关键数据趋势"。</p>

<h2 id="benefits">AI电子表格的优势</h2>
<ul>
  <li><strong>速度</strong>：几分钟而非数小时创建电子表格</li>
  <li><strong>准确性</strong>：消除数据录入中的人为错误</li>
  <li><strong>可访问性</strong>：无需记忆复杂公式</li>
  <li><strong>专业质量</strong>：生成精良、组织良好的电子表格</li>
  <li><strong>可定制</strong>：简单指令轻松修改</li>
</ul>

<h2 id="conclusion">总结</h2>
<p>AI正在革新电子表格创建，让每个人——无论Excel水平如何——都能使用。无论你是新手还是资深专业人士，AI工具都能帮你节省时间、减少错误、创建更好的电子表格。</p>

<h2>常见问题</h2>

<h3>创建电子表格用哪个AI工具最好？</h3>
<p>对中国用户，<strong>豆包</strong>（本指南提及）内置AI电子表格功能最易用——免费、无需配置、中文界面直观。<strong>WorkBuddy</strong>有更强的Excel文件操作能力（直接本地文件访问、批量处理、VBA宏生成）。<strong>ChatGPT/Codex</strong>可从自然语言生成Excel公式、VBA宏和HTML仪表盘。简单表格创建豆包最快。复杂数据处理和与现有Excel工作流集成，WorkBuddy或Codex更好。本指南的原则（职业+需求→AI生成）适用于所有工具。</p>

<h3>这和7月22日的AI Excel技能文章有什么区别？</h3>
<p>7月22日文章聚焦<strong>技能</strong>——数据质量分析、业务规则计算和仪表盘生成的具体提示词模式。本文聚焦<strong>工作流</strong>——从模糊需求（"我需要一个电子表格"）到成品端到端的过程。本文还涵盖前文未涉及的场景：电商运营表、从收据处理费用报销、以及基于职业的方法（告诉AI你的角色以获得更好上下文）。两篇文章互补：先读这篇掌握5步流程，再读7月22日文章学习高级提示词技巧。</p>

<h3>AI能处理电子表格中的敏感数据吗（如员工信息）？</h3>
<p>可以，但有条件。指南在员工花名册示例中明确提到"数据脱敏"。AI工具可以遮盖或替换敏感字段（姓名→员工编号、电话号码→打码数字、薪资→区间）。但安全性取决于工具：<strong>云端工具</strong>（豆包、ChatGPT）在服务器上处理数据——避免上传真正敏感数据。<strong>本地工具</strong>（WorkBuddy、Claude Code、Codex本地模式）在电脑上处理数据——内部文档更安全。处理任何敏感数据，使用脱敏提示词模式："创建一份[用途]电子表格，并对所有个人信息进行脱敏处理（将姓名替换为编号、联系方式打码、薪资使用区间而非精确数字）。"</p>

<h3>AI生成了错误公式或数据怎么办？</h3>
<p>始终验证。指南的"用简单指令自定义"步骤（第5步）专为快速纠正设计——如果公式错误，描述预期行为，AI会修复。复杂电子表格用这些验证提示词："检查此电子表格中所有公式是否有错误"和"验证X列的总计是否与单个条目之和匹配"。AI可以自我审计，只要你要求。关键业务电子表格，分享前始终手动抽查5-10个数据点。AI生成的电子表格是起点而非成品——人类审查步骤必不可少。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>掌握了AI电子表格？探索更多办公生产力：</p>
  <ul>
    <li><a href="/articles/ai-powered-excel-workflow-4-practical-skills-beginners">AI加持Excel工作流：新手必学的4个实用技能</a> — Excel高级提示词技巧</li>
    <li><a href="/articles/chatgpt-codex-10-core-features-beginners-work-efficiency">ChatGPT Codex：新手必学的10个核心提效功能</a> — 更多AI办公生产力功能</li>
    <li><a href="/articles/practical-guide-tencent-workbuddy-ai-office-assistant">腾讯WorkBuddy实操指南：一站式AI办公助手完全上手</a> — 用WorkBuddy进行本地电子表格自动化</li>
  </ul>
</div>`,
  },

'''
last_brace = content_src.rfind('};')
with open('src/lib/article-content.ts', 'w', encoding='utf-8') as f: f.write(content_src[:last_brace] + new_contents + '};')
print('Part 2: 1 article content added')
print('\n=== Done ===')