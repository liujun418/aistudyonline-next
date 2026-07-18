"""
Publish July 18, 2026 — 2 articles, no new tools.
(Skipped July 17 — no articles in wenzhang with that date.)
"""
import os

BASE = r"C:\Users\jun\aistudyonline-next"
os.chdir(BASE)

# ===== Part 1: Add 2 article metadata to articles.ts =====
with open('src/lib/articles.ts', 'r', encoding='utf-8') as f:
    articles_src = f.read()

new_articles = r"""  {
    slug: "how-to-use-codex-quantitative-strategy-research-backtesting",
    title: "How to Use Codex for Quantitative Strategy Research and Backtesting",
    titleZh: "用Codex做量化策略研究与回测：完整教程",
    description: "A step-by-step tutorial on using Codex with khQuant CLI for quantitative strategy research — covering installation, configuration testing, data download, batch golden-cross strategy optimization, and backtest report generation.",
    descriptionZh: "用Codex配合khQuant命令行工具进行量化策略研究的完整教程——覆盖安装、配置测试、数据下载、批量金叉策略优化和回测报告生成。",
    category: "AI Tutorials",
    tags: ["Codex", "Quantitative Trading", "khQuant", "Backtesting", "Strategy Research", "Finance"],
    difficulty: "intermediate",
    toolsMentioned: ["Codex Agent"],
    date: "2026-07-18",
  },
  {
    slug: "how-to-build-personal-ai-quant-trading-system-2026",
    title: "How to Build a Personal AI Quant Trading System in 2026",
    titleZh: "2026个人AI量化交易系统搭建全指南",
    description: "A comprehensive guide to building a personal AI quant trading system — from understanding how large quant firms profit versus individual trader advantages, to choosing holaOS as the agent framework, training AI with 6 core skills, implementing event-driven strategies with multi-model validation (Claude + GLM-5), and cost breakdown (~$400/month).",
    descriptionZh: "搭建个人AI量化交易系统的完整指南——从理解大机构盈利模式与个人优势，到选择holaOS作为Agent框架、训练AI六大核心能力、实施事件驱动策略+多模型验证（Claude+GLM-5），含成本分析（约$400/月）。",
    category: "AI Tutorials",
    tags: ["Quantitative Trading", "AI Agent", "holaOS", "Event-Driven", "Finance", "Claude", "GLM-5"],
    difficulty: "advanced",
    toolsMentioned: ["Claude Code", "GLM-5"],
    date: "2026-07-18",
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
  "how-to-use-codex-quantitative-strategy-research-backtesting": {
    content: `<div class="meta-banner">
  <span class="meta-badge">📚 AI Tutorials</span>
  <span class="meta-badge">🕒 5 min read</span>
  <span class="meta-badge">📅 Jul 18, 2026</span>
  <span class="meta-badge">🎯 Intermediate</span>
</div>

<h2 id="introduction">Introduction</h2>

<p>This guide demonstrates how to use Codex to conduct quantitative strategy research and backtesting, covering the complete process from installation to validation. We will use Codex as the primary tool, with khQuant as the underlying command-line quantitative research tool.</p>

<h2 id="install">1. Install Codex</h2>

<p>First, complete the installation of Codex. There are multiple installation methods available online, including official subscription and mirror sites. It is recommended to use the official subscription if possible.</p>

<h2 id="verify">2. Verify khQuant Installation</h2>

<p>Before proceeding, confirm that you have installed the V3 version of khQuant on your local machine.</p>

<h2 id="test">3. Test Configuration with Codex</h2>

<p>Ask Codex to check your configuration and run built-in test cases:</p>

<pre><code class="language-text">On this computer, I have installed the khQuant CLI command set and corresponding skills. Please help me check if the configuration is complete, run the built-in examples using the CLI, and generate a backtest report for me.</code></pre>

<p>After the execution is complete, you will see the backtest report, which includes key metrics such as:</p>

<ul>
  <li>Profit and Loss (PnL)</li>
  <li>Drawdown (DD)</li>
  <li>Transaction statistics (TRD)</li>
</ul>

<h2 id="download">4. Download Data via Codex</h2>

<p>You can also use Codex to command khQuant to download and manage data. For example, to download the daily data of the Shanghai 50 Index for the past 5 years, including unadjusted, forward-adjusted, and backward-adjusted versions:</p>

<pre><code class="language-text">Help me download the daily data of the Shanghai 50 Index for the past 5 years, including unadjusted, forward-adjusted, and backward-adjusted data.</code></pre>

<p>After the download is complete, you can ask Codex to summarize the downloaded data:</p>

<pre><code class="language-text">Please summarize the data I just downloaded.</code></pre>

<h2 id="gui">5. Check Data in khQuant GUI</h2>

<p>You can also open the graphical interface of khQuant and find the database management module to view the downloaded data.</p>

<h2 id="batch">6. Batch Strategy Research</h2>

<p>You can use Codex to conduct batch research on strategy parameters. For example, to study the golden cross and death cross strategy for a specific stock, and find the optimal long-term and short-term moving average parameters:</p>

<pre><code class="language-text">I want to study the golden cross and death cross strategy for a specific stock, but I need to find the optimal long-term and short-term moving average parameters. Please help me call the khQuant skill to generate batch golden cross and death cross strategies, conduct batch backtests, and find the optimal parameters for the past year.</code></pre>

<p>After the automatic strategy writing and backtesting are completed, you will obtain the results of the batch strategy research.</p>

<h2 id="conclusion">Conclusion</h2>

<p>The above is an introductory tutorial on how to use Codex to call khQuant for configuration and strategy research. Once you master this process, you can submit any strategy ideas to the large model for implementation and validation. Note: This tutorial uses Codex as the demonstration example. If you are using Claude Code or other powerful agents, you can also use similar methods to call the toolchain to complete the research.</p>

<h2>常见问题</h2>

<h3>Can I use Claude Code instead of Codex for this workflow?</h3>
<p>Yes. The article notes this explicitly. The key is the toolchain (khQuant CLI + Skills), not the specific agent. Claude Code's harness engineering is arguably better suited for this type of multi-step research workflow — it handles long-running tasks, state recovery, and batch operations more robustly. The prompts in this guide work with any agent that can execute CLI commands. If you're using Claude Code, the workflow is identical: install khQuant, configure the skills, and use the same prompts. The batch strategy research section (golden cross optimization) benefits most from Claude Code's stronger planning and multi-step execution.</p>

<h3>What is khQuant and where do I get it?</h3>
<p>khQuant is a command-line quantitative research tool that provides data download, backtesting, and strategy analysis capabilities. It's the "engine" that Codex controls — Codex handles the natural language interface and orchestration, while khQuant does the actual financial computation. The article assumes you have khQuant V3 installed. Check the original video by Mr. Kanhai (credited at the end of the article) for khQuant installation and setup instructions. The toolchain pattern (AI agent + CLI quant tool) is more important than the specific tools — you can substitute khQuant with any CLI-compatible quant library.</p>

<h3>What's a golden cross strategy and why batch-test it?</h3>
<p>A golden cross occurs when a short-term moving average (e.g., 50-day) crosses above a long-term moving average (e.g., 200-day) — traditionally a bullish signal. A death cross is the opposite (bearish). The problem: which moving average periods work best? 50/200 is the classic pair, but for a specific stock, 20/100 or 30/150 might perform better. Batch testing means the AI generates and backtests dozens of parameter combinations (short MA from 5 to 60, long MA from 20 to 250) to find the optimal pair for your specific stock and timeframe. This is exactly the kind of tedious optimization work that AI agents excel at — what would take a human days of manual testing takes Codex minutes.</p>

<h3>Do I need to know quantitative finance to use this workflow?</h3>
<p>You need to understand the <strong>concepts</strong> (moving averages, golden/death crosses, backtesting, PnL, drawdown) but not the implementation details. The AI handles the coding and parameter optimization. Think of it like driving a car: you need to know where you're going and the basic rules of the road, but you don't need to be a mechanic. Start with simple strategies (single indicator, single stock) to build intuition, then gradually increase complexity. The biggest risk is not understanding what the backtest results actually mean — a 90% win rate with 1 trade is meaningless, while a 55% win rate with 1,000 trades is statistically significant. Learn to read backtest reports critically before deploying real money.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Mastered Codex quant workflow? Go deeper into AI+finance:</p>
  <ul>
    <li><a href="/articles/ai-powered-quantitative-trading-quantdinger-guide">AI-Powered Quantitative Trading Made Accessible: A Practical Guide to QuantDinger</a> — another AI quant platform for comparison</li>
    <li><a href="/articles/how-to-build-personal-ai-quant-trading-system-2026">How to Build a Personal AI Quant Trading System in 2026</a> — the full system architecture guide</li>
    <li><a href="/articles/complete-guide-codex-zero-to-advanced">Complete Guide to Codex: From Zero to Advanced Development Workflow</a> — master the AI agent used in this tutorial</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">📚 AI 教程</span>
  <span class="meta-badge">🕒 阅读约5分钟</span>
  <span class="meta-badge">📅 2026年7月18日</span>
  <span class="meta-badge">🎯 中级</span>
</div>

<h2 id="introduction">引言</h2>

<p>本指南演示如何使用Codex进行量化策略研究和回测，覆盖从安装到验证的完整流程。我们将使用Codex作为主要工具，khQuant作为底层命令行量化研究工具。</p>

<h2 id="install">1. 安装Codex</h2>

<p>首先完成Codex的安装。网上有多种安装方式，包括官方订阅和镜像站点。建议尽量使用官方订阅。</p>

<h2 id="verify">2. 验证khQuant安装</h2>

<p>继续之前，确认你已在本地安装了V3版本的khQuant。</p>

<h2 id="test">3. 用Codex测试配置</h2>

<p>让Codex检查配置并运行内置测试用例：</p>

<pre><code class="language-text">这台电脑上我已经安装了khQuant的CLI命令集和相应技能。请帮我检查配置是否完整，使用CLI运行内置示例，并为我生成回测报告。</code></pre>

<p>执行完成后，你将看到回测报告，包含关键指标：</p>

<ul>
  <li>盈亏（PnL）</li>
  <li>回撤（DD）</li>
  <li>交易统计（TRD）</li>
</ul>

<h2 id="download">4. 通过Codex下载数据</h2>

<p>你也可以用Codex命令khQuant下载和管理数据。例如，下载上证50指数近5年的日线数据，包含未复权、前复权和后复权版本：</p>

<pre><code class="language-text">帮我下载上证50指数近5年的日线数据，包含未复权、前复权和后复权数据。</code></pre>

<p>下载完成后，可以让Codex汇总下载的数据：</p>

<pre><code class="language-text">请汇总我刚下载的数据。</code></pre>

<h2 id="gui">5. 在khQuant GUI中查看数据</h2>

<p>你也可以打开khQuant的图形界面，找到数据库管理模块查看下载的数据。</p>

<h2 id="batch">6. 批量策略研究</h2>

<p>你可以用Codex对策略参数进行批量研究。例如，研究某只股票的金叉死叉策略，找出最优的长期和短期均线参数：</p>

<pre><code class="language-text">我想研究某只股票的金叉死叉策略，但需要找到最优的长短期均线参数。请帮我调用khQuant技能生成批量金叉死叉策略，进行批量回测，找出近一年的最优参数。</code></pre>

<p>自动策略编写和回测完成后，你将获得批量策略研究的结果。</p>

<h2 id="conclusion">总结</h2>

<p>以上是用Codex调用khQuant进行配置和策略研究的入门教程。掌握这个流程后，你可以将任何策略想法提交给大模型来实现和验证。注意：本教程以Codex为演示示例。如果你使用Claude Code或其他强大的Agent，也可以用类似方法调用工具链完成研究。</p>

<h2>常见问题</h2>

<h3>能用Claude Code替代Codex做这个工作流吗？</h3>
<p>可以。文章明确提到这一点。关键是工具链（khQuant CLI + Skills），不是特定Agent。Claude Code的Harness工程能力可能更适合这类多步骤研究工作流——它更稳健地处理长时间运行任务、状态恢复和批量操作。本指南中的提示词适用于任何能执行CLI命令的Agent。如果使用Claude Code，流程完全相同：安装khQuant、配置技能、使用相同的提示词。批量策略研究部分（金叉优化）最能受益于Claude Code更强的规划和多步执行能力。</p>

<h3>khQuant是什么？在哪获取？</h3>
<p>khQuant是一个命令行量化研究工具，提供数据下载、回测和策略分析功能。它是Codex控制的"引擎"——Codex处理自然语言界面和编排，khQuant做实际的金融计算。文章假设你已安装khQuant V3。查看文章末尾注明的原作者Kanhai先生的视频获取安装和设置说明。工具链模式（AI Agent + CLI量化工具）比具体工具更重要——你可以用任何CLI兼容的量化库替换khQuant。</p>

<h3>什么是金叉策略，为什么要批量测试？</h3>
<p>金叉指短期均线（如50日）上穿长期均线（如200日）——传统上被视为看涨信号。死叉则相反（看跌）。问题在于：哪些均线周期效果最好？50/200是经典配对，但对特定股票，20/100或30/150可能表现更好。批量测试意味着AI生成并回测几十种参数组合（短期MA从5到60，长期MA从20到250），找到你特定股票和时间框架的最优配对。这正是AI Agent擅长的繁琐优化工作——人类需要数天手动测试的工作，Codex在几分钟内完成。</h3>

<h3>使用这个工作流需要懂量化金融吗？</h3>
<p>你需要理解<strong>概念</strong>（均线、金叉/死叉、回测、盈亏、回撤），但不需要懂实现细节。AI处理编码和参数优化。就像开车：你需要知道去哪和基本交通规则，但不需要是机械师。从简单策略开始（单一指标、单只股票）建立直觉，然后逐步增加复杂度。最大风险是不理解回测结果的实际含义——1笔交易90%胜率毫无意义，1000笔交易55%胜率在统计上显著。实盘之前学会批判性地阅读回测报告。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>掌握了Codex量化工作流？深入了解AI+金融：</p>
  <ul>
    <li><a href="/articles/ai-powered-quantitative-trading-quantdinger-guide">AI量化交易入门：QuantDinger实战指南</a> — 另一个AI量化平台对比</li>
    <li><a href="/articles/how-to-build-personal-ai-quant-trading-system-2026">2026个人AI量化交易系统搭建全指南</a> — 完整系统架构指南</li>
    <li><a href="/articles/complete-guide-codex-zero-to-advanced">Codex完全指南：从零基础到高级开发工作流</a> — 掌握本教程使用的AI Agent</li>
  </ul>
</div>`,
  },

  "how-to-build-personal-ai-quant-trading-system-2026": {
    content: `<div class="meta-banner">
  <span class="meta-badge">📚 AI Tutorials</span>
  <span class="meta-badge">🕒 10 min read</span>
  <span class="meta-badge">📅 Jul 18, 2026</span>
  <span class="meta-badge">🎯 Advanced</span>
</div>

<h2 id="introduction">Introduction</h2>

<p>If you have your own quantitative trading system and still lose money, there's no excuse — you're simply not good enough. As a college sophomore, I aim to be the first to deliver real results and teach you how to build AI-driven quantitative strategies. In this guide, I'll break down quantitative trading in 10 minutes, focusing on practical implementation for beginners.</p>

<p><strong>Important Disclaimer</strong>: This guide does not constitute investment advice. The trading ideas are for demonstrating technical paths only. Anyone reaching out to you unsolicited is a scammer — please stay vigilant.</p>

<h2 id="big-quant">1. How Large Quant Firms Profit</h2>

<h3>1.1 The Core Strategy of Big Quant Firms</h3>

<p><strong>Example: High-Frequency Trading (HFT)</strong></p>
<ul>
  <li>Firms like HF Quant use AI-powered hedge fund strategies.</li>
  <li>They process massive data with neural networks and analyze financial/economic behavior using NLP.</li>
  <li>Instead of predicting single stock movements, they rank thousands of stocks simultaneously.</li>
  <li>If a model predicts Stock A has a higher probability of outperforming and Stock B a lower probability, the portfolio increases A's weight and decreases B's weight.</li>
  <li>Over thousands of trades, statistical advantage ensures profitability — flipping a coin 10,000 times approaches 50%; quant firms profit by identifying which side has 51%.</li>
</ul>

<h3>1.2 The Formula</h3>
<p><strong>Strategy</strong>: Minimal probability advantage × Extremely high trading frequency. Example: 51% win rate, 100,000 trades per day.</p>

<h3>1.3 Barriers to Entry</h3>
<ol>
  <li>Capital volume + Computational power</li>
  <li>Model speed + Execution system</li>
  <li>Data access + Scale</li>
</ol>

<h2 id="individual">2. Opportunities for Individual Traders</h2>

<p>You can't beat big firms on speed, computing power, or data — but you can win on <strong>information understanding</strong> and <strong>flexibility</strong>.</p>

<h3>Your Competitive Advantage</h3>
<ul>
  <li><strong>Big Quant</strong>: Industrial money-making machine (small advantage × high frequency)</li>
  <li><strong>You + AI</strong>: Flexible small hunter (big advantage × low frequency)</li>
  <li><strong>Key Insight</strong>: Big quant firms are slow and clumsy — you can target opportunities they miss.</li>
</ul>

<h3>The Common Mistake to Avoid</h3>
<ul>
  <li><strong>Myth</strong>: "Low-frequency trading + certainty"</li>
  <li><strong>Reality</strong>: There is no certainty in quantitative trading — only probability advantage. If AI predicts a 70% probability of a positive event, a single trade may still fail. The goal is to increase the win rate, not guarantee success.</li>
</ul>

<h2 id="2026">3. 2026: The Year of Personal AI Quant Trading</h2>

<p>In 2026, personal quantitative trading has advanced significantly. You can now achieve what was once only possible for institutions: news monitoring, announcement interpretation, sentiment analysis, order book structure analysis, and technical analysis.</p>

<h2 id="framework">4. Choosing the Right AI Agent Framework</h2>

<p>For financial quantitative trading, you need a system with 24/7 stability, concurrency processing, state recovery, and black-box monitoring.</p>

<h3>4.1 The Best Framework: holaOS</h3>

<ul>
  <li>System-level sandbox designed for long-term work</li>
  <li>Harness mechanism for state persistence and breakpoint resumption</li>
  <li>Multi-app concurrency and full desktop view</li>
  <li>Native advanced routing for task distribution and model allocation</li>
</ul>

<p><strong>Installation</strong>:</p>
<pre><code class="language-bash">curl -fsSL https://raw.githubusercontent.com/holaboss-ai/holaOS/refs/heads/main/scripts/install.sh | bash -s -- --launch</code></pre>

<h3>4.2 Framework Comparison</h3>

<table>
  <tr><th>Feature</th><th>holaOS</th><th>OpenClaw</th><th>Hermes Agent</th></tr>
  <tr><td>24/7 Stability</td><td>Excellent</td><td>Poor (prone to crashes)</td><td>Moderate</td></tr>
  <tr><td>Concurrency</td><td>Multi-app sandbox</td><td>Chaotic execution</td><td>Dialogue-oriented</td></tr>
  <tr><td>State Recovery</td><td>Native support</td><td>No mechanism</td><td>Memory-based (fragile)</td></tr>
  <tr><td>Visualization</td><td>Holaboss dashboard</td><td>No unified view</td><td>No unified view</td></tr>
</table>

<h2 id="training">5. Training Your AI Quant Trader</h2>

<p>A competent AI quant trader needs 6 core skills:</p>

<ol>
  <li><strong>Data Layer</strong>: Access K-line data — fetching historical price data</li>
  <li><strong>Backtesting Layer</strong>: Test strategies against historical data</li>
  <li><strong>News Monitoring Layer</strong>: Track news, key figure dynamics, and macro data</li>
  <li><strong>Decision Layer</strong>: Generate structured trading recommendations</li>
  <li><strong>Risk Control Layer</strong>: Multi-model validation, information verification, and position control</li>
  <li><strong>Execution Layer</strong>: Connect to trading APIs for order execution</li>
</ol>

<h2 id="implementation">6. Practical Implementation: Event-Driven Strategy</h2>

<h3>6.1 Setup</h3>
<ul>
  <li><strong>Initial Capital</strong>: $500</li>
  <li><strong>Strategy</strong>: Spot trading (lowest risk)</li>
  <li><strong>Timeframe</strong>: 1+ month</li>
  <li><strong>Asset</strong>: 24/7 tradable (e.g., cryptocurrency)</li>
</ul>

<h3>6.2 Event-Driven Logic</h3>
<ul>
  <li>Check US-Iran dynamics every 5 minutes</li>
  <li>If Iran threatens to close Strait of Hormuz → Sell</li>
  <li>If US-Iran peace talks announced → Buy</li>
  <li>If talks stall → Adjust positions automatically</li>
</ul>

<h3>6.3 Multi-Model Validation</h3>
<ul>
  <li>GLM-5 handles daily tasks</li>
  <li>Claude performs full analysis when GLM-5 confirms a trade</li>
  <li>Only execute when both models agree</li>
</ul>

<h2 id="cost">7. Cost of Personal AI Quant Trading</h2>

<ul>
  <li>GLM-5: $40/month</li>
  <li>Claude API: ~$100/month</li>
  <li>24/7 MacBook: ~$30/month in electricity</li>
  <li>API Interfaces: ~$200/month</li>
  <li><strong>Total</strong>: ~$400/month (varies with strategy complexity)</li>
</ul>

<h2 id="conclusion">Conclusion</h2>

<p>In 2026, personal AI quantitative trading is no longer a dream — it's a practical reality. By leveraging holaOS, event-driven strategies, and multi-model validation, you can compete with big quant firms on flexibility and information understanding. The goal isn't to get rich quick — it's to build a sustainable, profitable system that works for you.</p>

<p><strong>Key Takeaways</strong>: Big Quant = small advantage × high frequency. You + AI = big advantage × low frequency. Success factor = clearer information understanding, not faster AI. Start small, focus on quality signals, validate rigorously with multi-model backtesting, and never risk more than you can afford to lose.</p>

<h2>常见问题</h2>

<h3>Is $400/month really the minimum cost for personal AI quant trading?</h3>
<p>No — $400/month is the cost for the specific setup described in this guide (Claude + GLM-5 + paid APIs + 24/7 MacBook). You can start much cheaper. A minimal setup: use a single model (GLM-5 at $40/month or Claude at $20/month for the API tier), run it on your existing computer during hours you're not using it (no extra electricity cost), use free data sources (Yahoo Finance, Alpha Vantage free tier), and trade manually based on AI signals instead of full API automation. That brings the cost to $20-40/month. The $400 figure represents a fully automated, always-on, multi-model system — it's the target, not the starting point.</p>

<h3>Why holaOS instead of just using Claude Code or Codex directly?</h3>
<p>Claude Code and Codex are designed for interactive development work — they excel when you're actively collaborating with them. Quantitative trading needs the opposite: unattended 24/7 operation, automatic crash recovery, and concurrent multi-task execution. holaOS is purpose-built for this "set and forget" agent workload. Its harness mechanism means if your bot crashes at 3am due to a network blip, it restarts and resumes from where it left off. Claude Code would just stop and wait for you to wake up. For research and strategy development, use Claude Code or Codex. For live trading deployment, use holaOS (or similar long-running agent frameworks).</p>

<h3>How reliable is multi-model validation for trading decisions?</h3>
<p>Multi-model validation (Claude + GLM-5 in this guide) reduces but doesn't eliminate bad trades. Think of it as requiring two independent analysts to agree before executing. It catches cases where one model hallucinates a signal or misinterprets news. The trade-off: you'll miss some profitable trades (when one model correctly identifies an opportunity but the other disagrees) but avoid more bad ones. The guide's results — "barely passing" returns — reflect this conservative approach. For higher returns, you'd loosen the agreement threshold (execute if either model says yes) but accept more risk. There's no free lunch.</p>

<h3>Can I apply this event-driven strategy to traditional stocks instead of crypto?</h3>
<p>Yes, but with modifications. The event-driven logic (monitor news → trigger trades) works for any asset class. For A-shares: monitor policy announcements, earnings reports, and industry regulations instead of geopolitical events. For US stocks: monitor Fed decisions, earnings calls, and SEC filings. The main difference is market hours — stocks trade 6.5 hours/day, 5 days/week, so you don't need true 24/7 monitoring. This actually makes stocks easier for beginners: you can run the AI during market hours only, reducing complexity and cost. The multi-model validation pattern (GLM-5 for daily screening, Claude for final decision) transfers directly.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Ready to build your quant system? Start with these foundations:</p>
  <ul>
    <li><a href="/articles/how-to-use-codex-quantitative-strategy-research-backtesting">How to Use Codex for Quantitative Strategy Research and Backtesting</a> — hands-on strategy research workflow</li>
    <li><a href="/articles/ai-powered-quantitative-trading-quantdinger-guide">AI-Powered Quantitative Trading Made Accessible: QuantDinger Guide</a> — another AI quant platform for your toolkit</li>
    <li><a href="/articles/2026-ai-agent-guide-choose-right-tool-beginners">2026 AI Agent Guide: How to Choose the Right Tool for Beginners</a> — compare agent frameworks for your quant system</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">📚 AI 教程</span>
  <span class="meta-badge">🕒 阅读约10分钟</span>
  <span class="meta-badge">📅 2026年7月18日</span>
  <span class="meta-badge">🎯 高级</span>
</div>

<h2 id="introduction">引言</h2>

<p>如果你有自己的量化交易系统还在亏钱，没有借口——就是水平不够。作为一个大二学生，我的目标是最先交付真实成果，教你如何构建AI驱动的量化策略。本指南10分钟拆解量化交易，聚焦初学者的实战落地。</p>

<p><strong>重要声明</strong>：本指南不构成投资建议。交易思路仅用于演示技术路径。任何主动联系你的人都是骗子——请保持警惕。</p>

<h2 id="big-quant">1. 大机构如何盈利</h2>

<h3>1.1 大机构的核心策略</h3>

<p><strong>示例：高频交易（HFT）</strong></p>
<ul>
  <li>HF Quant等公司使用AI驱动的对冲基金策略。</li>
  <li>用神经网络处理海量数据，用NLP分析金融/经济行为。</li>
  <li>不预测单只股票走势，而是同时对数千只股票排序。</li>
  <li>模型预测A股跑赢概率高、B股概率低，组合就加A减B。</li>
  <li>数千次交易后，统计优势确保盈利——抛硬币10000次趋近50%；量化机构靠识别哪面有51%的概率盈利。</li>
</ul>

<h3>1.2 公式</h3>
<p><strong>策略</strong>：极小概率优势 × 极高交易频率。示例：51%胜率，每天10万笔交易。</p>

<h3>1.3 进入壁垒</h3>
<ol>
  <li>资金量 + 算力</li>
  <li>模型速度 + 执行系统</li>
  <li>数据获取 + 规模</li>
</ol>

<h2 id="individual">2. 个人交易者的机会</h2>

<p>你在速度、算力和数据上打不过大机构——但你可以在<strong>信息理解</strong>和<strong>灵活性</strong>上取胜。</p>

<h3>你的竞争优势</h3>
<ul>
  <li><strong>大机构</strong>：工业级赚钱机器（小优势 × 高频）</li>
  <li><strong>你 + AI</strong>：灵活的小猎手（大优势 × 低频）</li>
  <li><strong>核心洞察</strong>：大机构又慢又笨——你可以瞄准它们错过的机会。</li>
</ul>

<h3>需要避免的常见错误</h3>
<ul>
  <li><strong>迷思</strong>："低频交易 + 确定性"</li>
  <li><strong>现实</strong>：量化交易中没有确定性——只有概率优势。AI预测70%概率的利好事件，单笔交易仍可能失败。目标是提高胜率，而非保证成功。</li>
</ul>

<h2 id="2026">3. 2026：个人AI量化交易元年</h2>

<p>2026年，个人量化交易已大幅进步。你现在可以实现过去只有机构才能做到的事：新闻监控、公告解读、情绪分析、订单簿结构分析和技术分析。</p>

<h2 id="framework">4. 选择合适的AI Agent框架</h2>

<p>金融量化交易需要具备：24/7稳定性、并发处理、状态恢复和黑盒监控的系统。</p>

<h3>4.1 最佳框架：holaOS</h3>

<ul>
  <li>为长期工作设计的系统级沙箱</li>
  <li>Harness机制支持状态持久化和断点续传</li>
  <li>多应用并发和全桌面视图</li>
  <li>原生高级路由支持任务分发和模型分配</li>
</ul>

<p><strong>安装</strong>：</p>
<pre><code class="language-bash">curl -fsSL https://raw.githubusercontent.com/holaboss-ai/holaOS/refs/heads/main/scripts/install.sh | bash -s -- --launch</code></pre>

<h3>4.2 框架对比</h3>

<table>
  <tr><th>特性</th><th>holaOS</th><th>OpenClaw</th><th>Hermes Agent</th></tr>
  <tr><td>24/7稳定性</td><td>优秀</td><td>差（容易崩溃）</td><td>中等</td></tr>
  <tr><td>并发处理</td><td>多应用沙箱</td><td>混乱执行</td><td>对话导向</td></tr>
  <tr><td>状态恢复</td><td>原生支持</td><td>无机制</td><td>基于记忆（脆弱）</td></tr>
  <tr><td>可视化</td><td>Holaboss仪表盘</td><td>无统一视图</td><td>无统一视图</td></tr>
</table>

<h2 id="training">5. 训练你的AI量化交易员</h2>

<p>一个合格的AI量化交易员需要6项核心能力：</p>

<ol>
  <li><strong>数据层</strong>：获取K线数据</li>
  <li><strong>回测层</strong>：对历史数据测试策略</li>
  <li><strong>新闻监控层</strong>：追踪新闻、关键人物动态和宏观数据</li>
  <li><strong>决策层</strong>：生成结构化交易建议</li>
  <li><strong>风控层</strong>：多模型验证、信息核实和仓位控制</li>
  <li><strong>执行层</strong>：连接交易API下单</li>
</ol>

<h2 id="implementation">6. 实战落地：事件驱动策略</h2>

<h3>6.1 设置</h3>
<ul>
  <li><strong>初始资金</strong>：$500</li>
  <li><strong>策略</strong>：现货交易（风险最低）</li>
  <li><strong>时间框架</strong>：1个月以上</li>
  <li><strong>资产</strong>：24/7可交易（如加密货币）</li>
</ul>

<h3>6.2 事件驱动逻辑</h3>
<ul>
  <li>每5分钟检查美伊动态</li>
  <li>伊朗威胁关闭霍尔木兹海峡 → 卖出</li>
  <li>美伊和谈公布 → 买入</li>
  <li>谈判停滞 → 自动调整仓位</li>
</ul>

<h3>6.3 多模型验证</h3>
<ul>
  <li>GLM-5处理日常任务</li>
  <li>GLM-5确认交易后Claude进行完整分析</li>
  <li>两模型一致才执行</li>
</ul>

<h2 id="cost">7. 个人AI量化交易成本</h2>

<ul>
  <li>GLM-5：$40/月</li>
  <li>Claude API：约$100/月</li>
  <li>24/7 MacBook：约$30/月电费</li>
  <li>API接口：约$200/月</li>
  <li><strong>合计</strong>：约$400/月（随策略复杂度变化）</li>
</ul>

<h2 id="conclusion">总结</h2>

<p>2026年，个人AI量化交易不再是梦想——而是切实可行的现实。通过holaOS、事件驱动策略和多模型验证，你可以在灵活性和信息理解上与大机构竞争。目标不是一夜暴富——而是构建一个可持续盈利的系统为你工作。</p>

<p><strong>核心要点</strong>：大机构 = 小优势 × 高频。你 + AI = 大优势 × 低频。成功要素 = 更清晰的信息理解，而非更快的AI。从小开始，聚焦高质量信号，用多模型回测严格验证，永远不要冒超过你能承受的损失。</p>

<h2>常见问题</h2>

<h3>$400/月真的是个人AI量化交易的最低成本吗？</h3>
<p>不是——$400/月是本指南描述特定配置的成本（Claude + GLM-5 + 付费API + 24/7 MacBook）。你可以起步便宜得多。最小配置：使用单一模型（GLM-5 $40/月或Claude API层$20/月），在你不用电脑的时间段运行（无额外电费），使用免费数据源（Yahoo Finance、Alpha Venture免费层），基于AI信号手动交易而非全API自动化。这样成本降到$20-40/月。$400是代表全自动、始终在线、多模型系统的目标配置，不是起点。</p>

<h3>为什么选holaOS而不是直接用Claude Code或Codex？</h3>
<p>Claude Code和Codex为互动开发工作设计——在主动协作时表现出色。量化交易需要相反的：无人值守24/7运行、自动崩溃恢复和并发多任务执行。holaOS专为这种"设置后不管"的Agent工作负载设计。它的Harness机制意味着如果机器人在凌晨3点因网络波动崩溃，它会自动重启并从断点继续。Claude Code只会停下来等你起床。研究和策略开发用Claude Code或Codex。实盘交易部署用holaOS（或类似的长期运行Agent框架）。</p>

<h3>多模型验证对交易决策有多可靠？</h3>
<p>多模型验证（本指南中的Claude + GLM-5）能减少但不能消除坏交易。把它理解为需要两个独立分析师在交易前达成一致。它能捕捉一个模型幻觉信号或误读新闻的情况。代价：你会错过一些盈利交易（一个模型正确识别机会但另一个不同意），但能避免更多坏交易。指南的结果——"勉强及格"的收益率——反映了这种保守策略。要更高收益，可以放宽一致性门槛（任一模型说Yes就执行），但接受更大风险。没有免费午餐。</p>

<h3>这个事件驱动策略能用于传统股票而非加密货币吗？</h3>
<p>可以，但需调整。事件驱动逻辑（监控新闻→触发交易）适用于任何资产类别。A股：监控政策公告、财报和行业监管而非地缘事件。美股：监控美联储决策、财报电话和SEC文件。主要区别是交易时间——股票每天交易6.5小时、每周5天，所以不需要真正的24/7监控。这实际上让股票对新手更友好：只在交易时段运行AI，降低复杂度和成本。多模型验证模式（GLM-5日常筛选、Claude最终决策）直接适用。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>准备好搭建你的量化系统？从这些基础开始：</p>
  <ul>
    <li><a href="/articles/how-to-use-codex-quantitative-strategy-research-backtesting">用Codex做量化策略研究与回测：完整教程</a> — 实战策略研究工作流</li>
    <li><a href="/articles/ai-powered-quantitative-trading-quantdinger-guide">AI量化交易入门：QuantDinger实战指南</a> — 工具箱中的另一个AI量化平台</li>
    <li><a href="/articles/2026-ai-agent-guide-choose-right-tool-beginners">2026 AI Agent选型指南：新手如何选择最适合的工具</a> — 为你的量化系统对比Agent框架</li>
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