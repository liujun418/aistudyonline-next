"""
Publish July 16, 2026 — 1 article + 1 new tool (QuantDinger).
"""
import os

BASE = r"C:\Users\jun\aistudyonline-next"
os.chdir(BASE)

# ===== Part 1: Add 1 new tool to tools.ts =====
with open('src/lib/tools.ts', 'r', encoding='utf-8') as f:
    tools_src = f.read()

new_tools = r"""
  {
    id: "quantdinger",
    name: "QuantDinger",
    nameZh: "QuantDinger",
    description: "Open-source AI-powered quantitative trading platform with automatic strategy optimization, multi-market coverage (A-shares, US stocks, crypto, futures, forex), deterministic backtesting, and self-hosted Docker deployment.",
    descriptionZh: "开源AI量化交易平台，支持自动策略优化、多市场覆盖（A股、美股、加密货币、期货、外汇）、确定性回测和Docker自托管部署。",
    category: "industry",
    tags: ["quantitative-trading", "finance", "open-source", "ai", "docker", "python", "trading-bot"],
    difficulty: "advanced",
    url: "https://github.com/brokermr810/QuantDinger",
    rating: 4.4,
    pricing: "Free",
    useCase: "AI-powered quantitative trading — automatic strategy generation, backtesting, and live trading across multiple markets with self-hosted data security",
    icon: "📈",
    company: "Open Source",
    companyZh: "开源项目",
    founded: 2025,
    headquarters: "Open Source",
    descriptionLong: "QuantDinger is an open-source AI-powered quantitative trading platform that democratizes algorithmic trading by making advanced strategies accessible to everyone. It supports trading across multiple asset classes including A-shares, US stocks, futures, cryptocurrencies, and forex, with 24/7 market scanning and real-time push notifications. The platform's standout feature is its AI-driven strategy development pipeline: it can automatically generate trading strategy code, run backtests, analyze equity curves and risk metrics, and call large language models to iteratively refine strategy parameters. Users can write Python-native strategies using DataFrame-based IndicatorStrategy or event-driven ScriptStrategy patterns, with AI assisting in code drafting while users retain full ownership. The deterministic backtesting engine models commissions and slippage, generates trade-by-trade analytics and equity curves, and pins every backtest run to a code hash and configuration snapshot for perfect reproducibility. Pre-built trading bots (Grid, Martingale, Trend Following, DCA) are execution-aware and restart-resilient. The entire platform is self-hosted via a one-line Docker Compose command that brings up Flask API, PostgreSQL 16, Redis, and Nginx — all data stays on your infrastructure. An optional MCP package enables integration with AI coding tools like Cursor and Claude Code. For anyone looking to combine AI with quantitative trading while maintaining complete data sovereignty, QuantDinger is the most accessible open-source option.",
    descriptionLongZh: "QuantDinger是一个开源AI量化交易平台，通过让高级策略人人可用，实现了算法交易的民主化。它支持A股、美股、期货、加密货币和外汇等多资产类别的交易，具备24/7市场扫描和实时推送通知。平台的核心亮点是AI驱动的策略开发流程：自动生成交易策略代码、运行回测、分析权益曲线和风险指标，并调用大语言模型迭代优化策略参数。用户可使用基于DataFrame的IndicatorStrategy或事件驱动的ScriptStrategy模式编写Python原生策略，AI辅助起草代码，用户保留完整所有权。确定性回测引擎建模佣金和滑点，生成逐笔交易分析和权益曲线，每次回测运行都绑定到代码哈希和配置快照，确保完美可复现。预置交易机器人（网格、马丁格尔、趋势跟踪、定投）具备执行感知和重启恢复能力。整个平台通过一行Docker Compose命令自托管部署，启动Flask API、PostgreSQL 16、Redis和Nginx——所有数据留在你的基础设施上。可选MCP包支持与Cursor和Claude Code等AI编码工具集成。对于想在保持数据主权的同时将AI与量化交易结合的人，QuantDinger是最易用的开源选择。",
    advantages: ["AI auto-generates and optimizes trading strategies", "Multi-market: A-shares, US stocks, crypto, futures, forex", "Deterministic backtesting with perfect reproducibility", "Self-hosted Docker deployment — data never leaves your machine", "Pre-built trading bots (Grid, Martingale, Trend Following, DCA)", "MCP integration with Cursor and Claude Code"],
    advantagesZh: ["AI自动生成和优化交易策略", "多市场覆盖：A股、美股、加密货币、期货、外汇", "确定性回测，完美可复现", "Docker自托管部署——数据不离开电脑", "预置交易机器人（网格、马丁格尔、趋势跟踪、定投）", "MCP集成Cursor和Claude Code"],
    useCases: ["Automated multi-market quantitative trading", "AI-assisted strategy backtesting and optimization", "Self-hosted algorithmic trading with data sovereignty", "Learning quantitative trading with AI guidance", "Integrating trading bots with AI coding assistants via MCP"],
    useCasesZh: ["自动化多市场量化交易", "AI辅助策略回测和优化", "自托管算法交易保障数据主权", "在AI指导下学习量化交易", "通过MCP将交易机器人与AI编码助手集成"],
    targetAudience: "Quantitative traders, finance professionals, algo-trading enthusiasts, and developers interested in combining AI with financial markets",
    targetAudienceZh: "量化交易者、金融专业人士、算法交易爱好者，以及对AI与金融市场结合感兴趣的开发者",
    pricingTiers: [
      {
        tier: "Free",
        tierZh: "免费",
        price: "Free",
        features: ["Full platform access", "All trading bots", "AI strategy optimization", "Self-hosted deployment", "Multi-market support"],
        featuresZh: ["完整平台访问", "全部交易机器人", "AI策略优化", "自托管部署", "多市场支持"],
      },
    ],
    pros: ["Completely free and open-source", "AI strategy generation saves hours of manual coding", "Self-hosted — no third-party access to your trading data", "One-line Docker deployment", "Pre-built bots work out of the box", "MCP integration with AI coding tools"],
    prosZh: ["完全免费开源", "AI策略生成节省数小时手动编码", "自托管——第三方无法访问交易数据", "一行Docker命令部署", "预置机器人开箱即用", "MCP集成AI编码工具"],
    cons: ["Requires Docker and basic command-line comfort", "Advanced strategies still need Python knowledge", "Self-hosted means you manage infrastructure", "Community support rather than enterprise SLA"],
    consZh: ["需要Docker和基本命令行操作", "高级策略仍需Python知识", "自托管意味着自己管理基础设施", "社区支持而非企业SLA"],
    extensions: [],
    skills: ["Strategy backtesting", "AI strategy optimization", "Live trading bot deployment", "Multi-market scanning", "Equity curve analysis"],
    scene: "development",
  },
"""

last_tool = tools_src.rfind('] as Tool[];')
tools_new = tools_src[:last_tool] + new_tools + '] as Tool[];'

with open('src/lib/tools.ts', 'w', encoding='utf-8') as f:
    f.write(tools_new)

print('Part 1: 1 new tool added to tools.ts (QuantDinger)')

# ===== Part 2: Add 1 article metadata to articles.ts =====
with open('src/lib/articles.ts', 'r', encoding='utf-8') as f:
    articles_src = f.read()

new_articles = r"""  {
    slug: "ai-powered-quantitative-trading-quantdinger-guide",
    title: "AI-Powered Quantitative Trading Made Accessible: A Practical Guide to QuantDinger",
    titleZh: "AI量化交易入门：QuantDinger实战指南",
    description: "A practical guide to QuantDinger — an open-source AI-powered quantitative trading platform featuring automatic strategy optimization, multi-market coverage (A-shares, US stocks, crypto, futures, forex), deterministic backtesting, self-hosted Docker deployment, and MCP integration with AI coding tools.",
    descriptionZh: "QuantDinger开源AI量化交易平台实战指南——自动策略优化、多市场覆盖（A股/美股/加密货币/期货/外汇）、确定性回测、Docker自托管部署和MCP集成AI编码工具。",
    category: "AI Tools",
    tags: ["QuantDinger", "Quantitative Trading", "Finance", "Open Source", "Docker", "Python", "AI"],
    difficulty: "advanced",
    toolsMentioned: ["QuantDinger", "Claude Code", "Cursor"],
    date: "2026-07-16",
  },

"""

last_bracket = articles_src.rfind('];')
articles_new = articles_src[:last_bracket] + new_articles + '];'

with open('src/lib/articles.ts', 'w', encoding='utf-8') as f:
    f.write(articles_new)

print('Part 2: 1 new article added to articles.ts')

# ===== Part 3: Add article content to article-content.ts =====
with open('src/lib/article-content.ts', 'r', encoding='utf-8') as f:
    content_src = f.read()

new_contents = r'''
  "ai-powered-quantitative-trading-quantdinger-guide": {
    content: `<div class="meta-banner">
  <span class="meta-badge">🔧 AI Tools</span>
  <span class="meta-badge">🕒 7 min read</span>
  <span class="meta-badge">📅 Jul 16, 2026</span>
  <span class="meta-badge">🎯 Advanced</span>
</div>

<h2 id="introduction">Introduction</h2>

<p>Quantitative trading has long been seen as a complex, high-barrier field reserved for financial professionals. But the open-source project <strong>QuantDinger</strong> is changing that, bringing AI-driven quantitative trading within reach of everyone. This tool not only supports automatic strategy optimization and one-click deployment but also runs entirely on your local machine, ensuring data security while delivering powerful features for both beginners and experienced traders.</p>

<h2 id="core-features">Core Features of QuantDinger</h2>

<h3>1. Universal Market Coverage</h3>

<p>QuantDinger supports trading across multiple asset classes, including A-shares, US stocks, futures, cryptocurrencies, and forex. It continuously scans markets 24/7 to capture opportunities, with real-time key signal push notifications to your mobile device, ensuring you never miss a market movement.</p>

<h3>2. AI-Driven Strategy Development</h3>

<p>One of QuantDinger's most impressive capabilities is its AI-powered strategy workflow:</p>

<ul>
  <li><strong>Automatic Strategy Generation</strong>: It can automatically write strategy code and run backtests</li>
  <li><strong>Intelligent Optimization</strong>: The system analyzes equity curves and risk metrics, calls large language models to refine parameters, and continuously improves strategy stability</li>
  <li><strong>Python-Native Strategies</strong>: Write DataFrame-based <code>IndicatorStrategy</code> or event-driven <code>ScriptStrategy</code>, with AI assisting in drafting code while you retain full ownership of your strategies</li>
</ul>

<h3>3. Deterministic Backtesting Engine</h3>

<p>The platform supports commission and slippage modeling, trade-by-trade analytics, and equity curve generation. Every backtest run is pinned to a code hash and configuration snapshot, ensuring perfect reproducibility of results.</p>

<h3>4. Autonomous Trading Bots</h3>

<p>QuantDinger comes with pre-built strategies like Grid, Martingale, Trend Following, and DCA out of the box. These bots are execution-aware, restart-resilient, and support both signal and fully live execution modes.</p>

<h3>5. Self-Hosted Architecture</h3>

<p>All components run locally on your computer, with a one-line Docker Compose command that brings up the entire stack including Flask API, PostgreSQL 16, Redis, and Nginx. Your API keys, strategies, AI history, and trade data never leave your infrastructure, ensuring complete data security.</p>

<h2 id="deployment">Practical Deployment Guide</h2>

<h3>Prerequisites</h3>
<ul>
  <li>Docker Desktop installed on your computer</li>
  <li>Stable internet connection to access GitHub and Docker Hub</li>
</ul>

<h3>Step 1: Install QuantDinger</h3>

<p>Run the following command in your terminal to install QuantDinger:</p>

<pre><code class="language-bash">curl -fsSL https://raw.githubusercontent.com/brokermr810/QuantDinger/main/install.sh | bash</code></pre>

<h3>Step 2: Configure Environment Variables</h3>

<p>Navigate to the QuantDinger directory and set up your environment variables:</p>

<pre><code class="language-bash">cd ~/quantdinger/backend_api_python
cp env.example .env
./scripts/generate-secret-key.sh</code></pre>

<p>Paste the generated <code>SECRET_KEY</code> into the <code>.env</code> file, and add your exchange API keys and broker credentials as needed.</p>

<h3>Step 3: Start the Platform</h3>

<p>Launch all services with Docker Compose:</p>

<pre><code class="language-bash">cd ~/quantdinger
docker compose up -d</code></pre>

<p>The web UI will be available at <code>http://localhost:8888</code> within about 60 seconds.</p>

<h3>Step 4: Install MCP Package (Optional)</h3>

<p>If you want to integrate QuantDinger with AI clients like Cursor or Claude Code, install the MCP package:</p>

<pre><code class="language-bash">pip install quantdinger-mcp</code></pre>

<h2 id="first-strategy">Getting Started with Your First Strategy</h2>

<h3>Creating a Strategy</h3>
<ol>
  <li>Open the QuantDinger web interface at <code>http://localhost:8888</code></li>
  <li>Navigate to the Strategy Development section</li>
  <li>Choose between <code>IndicatorStrategy</code> (for technical indicator-based strategies) or <code>ScriptStrategy</code> (for event-driven logic)</li>
  <li>Use the AI assistant to help draft your strategy code, or write it manually</li>
</ol>

<h3>Running a Backtest</h3>
<ol>
  <li>Select your strategy and choose a historical data range</li>
  <li>Configure backtest parameters including initial capital, commission rates, and slippage</li>
  <li>Run the backtest to see performance metrics including equity curve, win rate, and risk-adjusted returns</li>
</ol>

<h3>Deploying to Live Trading</h3>
<ol>
  <li>After validating your strategy with backtesting, navigate to the Trading Bots section</li>
  <li>Select your strategy and configure live trading parameters</li>
  <li>Enable the bot to start automated trading, with real-time monitoring available through the web interface or mobile app</li>
</ol>

<h2 id="conclusion">Conclusion</h2>

<p>QuantDinger democratizes quantitative trading by making advanced AI-driven strategies accessible to everyone. With its self-hosted architecture, automatic strategy optimization, and support for multiple markets, it's an excellent tool for anyone looking to get started with quantitative trading or enhance their existing trading workflow. The platform's one-click deployment and user-friendly interface mean you can be up and running with your first strategy in minutes, not days.</p>

<p>Whether you're a complete beginner or an experienced trader, QuantDinger provides the tools you need to develop, test, and deploy quantitative strategies with confidence.</p>

<h2>常见问题</h2>

<h3>Do I need to know Python to use QuantDinger?</h3>
<p>For basic usage — running pre-built bots (Grid, Martingale, Trend Following, DCA) — no Python knowledge is needed. You configure them through the web UI. For custom strategies, yes, you'll need basic Python. However, QuantDinger's AI assistant significantly lowers the barrier: you describe your strategy in plain language, and the AI drafts the Python code. You review and approve it. This means you can create custom strategies with minimal Python knowledge as long as you understand the trading logic. The learning curve is: pre-built bots (zero code) → AI-assisted custom strategies (basic Python reading ability) → fully manual strategies (Python proficiency).</p>

<h3>Is it safe to run trading bots on my own machine?</h3>
<p>Self-hosting is actually more secure than cloud-based alternatives for one reason: your API keys and trading data never leave your computer. With cloud quant platforms, you're trusting a third party with access to your brokerage accounts. QuantDinger's architecture means everything runs locally — the Docker containers are isolated, and no data is sent to external servers. The trade-off is that you're responsible for uptime. If your computer goes offline, your bots stop. For serious traders, running QuantDinger on a dedicated machine or low-cost VPS (which still counts as self-hosted) solves this. Never share your <code>.env</code> file or <code>SECRET_KEY</code> with anyone.</p>

<h3>How does AI strategy optimization actually work?</h3>
<p>QuantDinger's AI optimization follows a loop: (1) you define a strategy with initial parameters (e.g., "buy when RSI < 30, sell when RSI > 70"), (2) the backtesting engine runs it against historical data and generates an equity curve, win rate, Sharpe ratio, and max drawdown, (3) the AI analyzes these metrics and suggests parameter adjustments (e.g., "RSI < 30 gives too few signals — try RSI < 35 and add a volume filter"), (4) the modified strategy is backtested again, (5) the loop continues until the AI converges on optimal parameters or you stop it. This is what used to take human quants days of manual tuning — the AI does it in minutes. The key insight: the AI isn't inventing strategies from scratch; it's optimizing parameters within a strategy framework you define.</p>

<h3>Can I use QuantDinger with my existing brokerage account?</h3>
<p>QuantDinger connects to exchanges and brokers via API keys. It supports major crypto exchanges (Binance, OKX, etc.) and Chinese brokers for A-shares. For US stocks and futures, you'll need a broker that provides API access (Interactive Brokers, Alpaca, etc.). The setup process is: register for API access on your broker's platform → copy the API key and secret → paste them into QuantDinger's <code>.env</code> file → restart the platform. Always use read-only API keys for testing and enable trading permissions only after you've validated your strategy with paper trading. Most brokers let you create separate API keys with different permission levels.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Interested in AI + finance? Explore related content:</p>
  <ul>
    <li><a href="/articles/ai-bubble-or-opportunity-guide-ordinary-people">Is AI a Bubble or Opportunity? A Guide for Ordinary People</a> — understand the financial side of the AI revolution</li>
    <li><a href="/articles/complete-practical-tutorial-claude-code-core-operations">Complete Practical Tutorial: Master All Core Operations Inside Claude Code</a> — use Claude Code with QuantDinger's MCP integration</li>
    <li><a href="/articles/2025-ai-toolkit-practical-guide-every-domain">2025 AI Toolkit: A Practical Guide for Every Domain</a> — discover more AI tools across industries</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">🔧 AI 工具</span>
  <span class="meta-badge">🕒 阅读约7分钟</span>
  <span class="meta-badge">📅 2026年7月16日</span>
  <span class="meta-badge">🎯 高级</span>
</div>

<h2 id="introduction">引言</h2>

<p>量化交易长期以来被视为金融专业人士专属的高门槛领域。但开源项目<strong>QuantDinger</strong>正在改变这一局面，让AI驱动的量化交易触手可及。这个工具不仅支持自动策略优化和一键部署，还完全在本地运行，保障数据安全的同时为新手和资深交易者提供强大功能。</p>

<h2 id="core-features">QuantDinger核心功能</h2>

<h3>1. 全市场覆盖</h3>

<p>QuantDinger支持跨多资产类别的交易，包括A股、美股、期货、加密货币和外汇。24/7持续扫描市场捕捉机会，实时关键信号推送通知到手机，确保你不会错过任何市场动向。</p>

<h3>2. AI驱动策略开发</h3>

<p>QuantDinger最令人印象深刻的能力是其AI策略工作流：</p>

<ul>
  <li><strong>自动策略生成</strong>：自动编写策略代码并运行回测</li>
  <li><strong>智能优化</strong>：系统分析权益曲线和风险指标，调用大语言模型优化参数，持续提升策略稳定性</li>
  <li><strong>Python原生策略</strong>：编写基于DataFrame的<code>IndicatorStrategy</code>或事件驱动的<code>ScriptStrategy</code>，AI辅助起草代码，你保留策略完整所有权</li>
</ul>

<h3>3. 确定性回测引擎</h3>

<p>平台支持佣金和滑点建模、逐笔交易分析和权益曲线生成。每次回测运行都绑定到代码哈希和配置快照，确保结果的完美可复现性。</p>

<h3>4. 自主交易机器人</h3>

<p>QuantDinger开箱即用预置网格、马丁格尔、趋势跟踪和定投等策略。这些机器人具备执行感知和重启恢复能力，支持信号和完全实盘两种执行模式。</p>

<h3>5. 自托管架构</h3>

<p>所有组件在本地运行，一行Docker Compose命令启动完整技术栈，包括Flask API、PostgreSQL 16、Redis和Nginx。你的API密钥、策略、AI历史和交易数据绝不离开你的基础设施，确保数据完整安全。</p>

<h2 id="deployment">实战部署指南</h2>

<h3>前置条件</h3>
<ul>
  <li>电脑上安装Docker Desktop</li>
  <li>稳定的网络连接访问GitHub和Docker Hub</li>
</ul>

<h3>第一步：安装QuantDinger</h3>

<p>在终端运行以下命令安装QuantDinger：</p>

<pre><code class="language-bash">curl -fsSL https://raw.githubusercontent.com/brokermr810/QuantDinger/main/install.sh | bash</code></pre>

<h3>第二步：配置环境变量</h3>

<p>导航到QuantDinger目录并设置环境变量：</p>

<pre><code class="language-bash">cd ~/quantdinger/backend_api_python
cp env.example .env
./scripts/generate-secret-key.sh</code></pre>

<p>将生成的<code>SECRET_KEY</code>粘贴到<code>.env</code>文件中，按需添加交易所API密钥和券商凭证。</p>

<h3>第三步：启动平台</h3>

<p>用Docker Compose启动所有服务：</p>

<pre><code class="language-bash">cd ~/quantdinger
docker compose up -d</code></pre>

<p>约60秒后Web界面在<code>http://localhost:8888</code>可用。</p>

<h3>第四步：安装MCP包（可选）</h3>

<p>如需将QuantDinger与Cursor或Claude Code等AI客户端集成，安装MCP包：</p>

<pre><code class="language-bash">pip install quantdinger-mcp</code></pre>

<h2 id="first-strategy">首个策略快速上手</h2>

<h3>创建策略</h3>
<ol>
  <li>打开QuantDinger Web界面<code>http://localhost:8888</code></li>
  <li>导航到策略开发部分</li>
  <li>选择<code>IndicatorStrategy</code>（基于技术指标）或<code>ScriptStrategy</code>（事件驱动逻辑）</li>
  <li>使用AI助手起草策略代码，或手动编写</li>
</ol>

<h3>运行回测</h3>
<ol>
  <li>选择策略和历史数据范围</li>
  <li>配置回测参数：初始资金、佣金率、滑点</li>
  <li>运行回测查看性能指标：权益曲线、胜率、风险调整收益</li>
</ol>

<h3>部署实盘交易</h3>
<ol>
  <li>回测验证策略后，导航到交易机器人部分</li>
  <li>选择策略并配置实盘交易参数</li>
  <li>启动机器人开始自动交易，通过Web界面或手机App实时监控</li>
</ol>

<h2 id="conclusion">总结</h2>

<p>QuantDinger通过让高级AI驱动策略人人可用，实现了量化交易的民主化。自托管架构、自动策略优化和多市场支持，使其成为任何想入门量化交易或增强现有交易工作流的人的绝佳工具。平台的一键部署和用户友好界面意味着你可以在几分钟内启动首个策略，而非数天。</p>

<p>无论你是完全的新手还是经验丰富的交易者，QuantDinger都提供了你自信开发、测试和部署量化策略所需的工具。</p>

<h2>常见问题</h2>

<h3>使用QuantDinger需要懂Python吗？</h3>
<p>基础使用——运行预置机器人（网格、马丁格尔、趋势跟踪、定投）——不需要Python知识。通过Web界面配置即可。自定义策略需要基础Python。但QuantDinger的AI助手显著降低了门槛：你用自然语言描述策略，AI起草Python代码。你审查并批准。这意味着只要理解交易逻辑，用最少的Python知识就能创建自定义策略。学习曲线：预置机器人（零代码）→ AI辅助自定义策略（基础Python阅读能力）→ 完全手动策略（Python熟练）。</p>

<h3>在自己电脑上运行交易机器人安全吗？</h3>
<p>自托管实际上比云端方案更安全，原因只有一个：你的API密钥和交易数据绝不离开电脑。云端量化平台需要你信任第三方访问你的券商账户。QuantDinger的架构意味着一切在本地运行——Docker容器隔离，没有数据发送到外部服务器。代价是你需要负责正常运行时间。如果电脑离线，机器人停止。对严肃交易者，在专用机器或低成本VPS上运行QuantDinger（仍算自托管）可以解决这个问题。永远不要与任何人分享你的<code>.env</code>文件或<code>SECRET_KEY</code>。</p>

<h3>AI策略优化具体是怎么工作的？</h3>
<p>QuantDinger的AI优化遵循一个循环：(1) 你定义策略及初始参数（如"RSI<30买入，RSI>70卖出"），(2) 回测引擎对历史数据运行并生成权益曲线、胜率、夏普比率和最大回撤，(3) AI分析这些指标并建议参数调整（如"RSI<30信号太少——试试RSI<35并加成交量过滤器"），(4) 修改后的策略再次回测，(5) 循环持续直到AI收敛到最优参数或你停止。这以前是人类量化分析师需要数天手动调参的工作——AI在几分钟内完成。关键洞察：AI不是从零发明策略；它是在你定义的策略框架内优化参数。</p>

<h3>能用QuantDinger连接我现有的券商账户吗？</h3>
<p>QuantDinger通过API密钥连接交易所和券商。支持主流加密货币交易所（Binance、OKX等）和A股国内券商。美股和期货需要提供API访问的券商（Interactive Brokers、Alpaca等）。设置流程：在券商平台注册API访问→复制API密钥和密钥→粘贴到QuantDinger的<code>.env</code>文件→重启平台。测试时始终使用只读API密钥，仅在纸交易验证策略后再启用交易权限。大多数券商允许创建不同权限级别的独立API密钥。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>对AI+金融感兴趣？探索相关内容：</p>
  <ul>
    <li><a href="/articles/ai-bubble-or-opportunity-guide-ordinary-people">AI是泡沫还是机遇？普通人应对AI浪潮的生存指南</a> — 理解AI革命的金融面</li>
    <li><a href="/articles/complete-practical-tutorial-claude-code-core-operations">Claude Code完全实战教程：掌握所有核心操作</a> — 用Claude Code配合QuantDinger的MCP集成</li>
    <li><a href="/articles/2025-ai-toolkit-practical-guide-every-domain">2025 AI工具箱：全领域实用指南</a> — 发现更多跨行业AI工具</li>
  </ul>
</div>`,
  },

'''

last_brace = content_src.rfind('};')
content_new = content_src[:last_brace] + new_contents + '};'

with open('src/lib/article-content.ts', 'w', encoding='utf-8') as f:
    f.write(content_new)

print('Part 3: 1 article content added to article-content.ts')

print('\n=== All done! Run build to verify ===')