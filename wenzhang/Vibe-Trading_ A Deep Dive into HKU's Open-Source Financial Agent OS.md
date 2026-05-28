# Vibe\-Trading: A Deep Dive into HKU\&\#39;s Open\-Source Financial Agent OS



In the realm of financial technology, Hong Kong University’s open\-source project **Vibe\-Trading** has emerged as a game\-changer\. This financial Agent Operating System \(OS\) has garnered over 7,000 stars on GitHub within just a month of its release, showcasing its rapid adoption and potential\. Let’s break down its architecture, functionalities, and practical applications for global financial professionals\.

## What is Vibe\-Trading?

Vibe\-Trading is not a traditional financial tool—it’s a **financial Agent OS**\. Unlike standard software, it operates as an intelligent system where you simply give a command \(e\.g\., “Analyze Moutai’s stock performance”\), and the Agent autonomously determines which tools to use, what code to write, which data to fetch, and how to run backtests\. It’s designed to handle cross\-market analyses, supporting regions like A\-shares, US stocks, and Hong Kong stocks seamlessly\.

## Core Architecture \&amp; Components

### 1\. Multi\-Layered Tool Ecosystem

Vibe\-Trading boasts **30\+ tools** that act as the “hands and feet” of the system\. These tools cover:

- Backtesting engines for different markets\.

- Code execution environments \(sandboxes\)\.

- Knowledge loading modules\.

- Shadow account analysis \(upload real trade records to identify profit/loss patterns\)\.

- Multi\-agent collaboration frameworks\.

To utilize these tools, you can interact with the Agent via a simple prompt\. For example:

```python
# Example prompt to analyze a stock with dual moving averages
prompt = "Analyze Moutai's stock performance over the past 3 years using a dual moving average strategy. Provide backtest results."
```

### 2\. 72\-Skill Knowledge Base

The system includes **72 specialized skills \(Skills\)**—a professional knowledge repository covering:

- Data API integrations\.

- Technical analysis frameworks\.

- Strategy templates\.

- Workflow guides \(e\.g\., backtesting protocols, report writing, team collaboration\)\.

When the Agent detects relevant keywords in your prompt, it automatically taps into these Skills\. For instance, if you ask for a “Moutai stock report,” it will pull from report\-writing and data\-analysis Skills\.

### 3\. 452 Alpha Factors

For quantitative analysts, Vibe\-Trading offers **452 stock selection factors** across four academic systems:

- 101 factors from classic financial theories\.

- 191 factors tailored for A\-shares\.

- 154 factors for HK stocks\.

- 6 factors from cutting\-edge research \(e\.g\., from the Qlip project\)\.

These factors enable robust quantitative modeling\. Here’s a snippet of how you might interact with them:

```python
# Example: Fetch and analyze factors for a stock
factors = vibe_trading.get_factors(stock="Moutai", market="A-shares", categories=["valuation", "momentum"])
analysis = vibe_trading.analyze_factors(factors)
print(analysis.summary)
```

### 4\. 33\-Agent Team Collaboration

Vibe\-Trading operates with a **team of 33 specialized Agents**, mimicking a real\-world investment research department\. When you request an analysis, the system deploys relevant Agents:

- Macro industry chiefs\.

- Technical analysts\.

- Quantitative researchers\.

- Risk management experts\.

For example, analyzing Moutai might involve a macro economist, a liquor industry specialist, and a quant analyst—all working in tandem\.

## How It Works: The Think\-Act\-Observe Loop

Vibe\-Trading follows a **React\-style loop** to deliver results:

1. **Think**: The Agent parses your request and decides on the next steps \(e\.g\., which tools to use, which Agents to involve\)\.

2. **Act**: It executes the plan—writing code, fetching data, running backtests\.

3. **Observe**: It evaluates the results\. If unsatisfied, it loops back to “Think” \(up to 50 iterations\)\.

This loop ensures high\-quality outputs\. For example, testing a dual moving average strategy on Moutai would involve:

```python
# Simplified workflow example
def analyze_stock(stock, strategy):
    agent = VibeTradingAgent()
    plan = agent.think(stock, strategy)
    result = agent.act(plan)
    while not agent.observe(result) and agent.iterations < 50:
        plan = agent.think(stock, strategy, result)
        result = agent.act(plan)
    return result

moutai_result = analyze_stock("Moutai", "dual_moving_average")
print(moutai_result.backtest_metrics)
```

## Practical Use Cases

### 1\. Strategy Development \&amp; Backtesting

With Vibe\-Trading’s **code sandbox**, you can prototype and backtest new strategies without manual coding\. For example:

```python
# Request a new strategy and backtest
prompt = "Create a Python strategy for Moutai using RSI and MACD indicators. Backtest it over the past 3 years and return annual return, max drawdown, and Sharpe ratio."
strategy_result = vibe_trading.execute(prompt)
print(strategy_result.metrics)
```

### 2\. Shadow Account Analysis

Upload your real trade records to identify patterns in your profits and losses:

```python
# Upload trade records and get analysis
trade_data = load_trade_history("my_trades.csv")
shadow_analysis = vibe_trading.analyze_shadow_account(trade_data)
print(shadow_analysis.profit_patterns)
print(shadow_analysis.improvement_recommendations)
```

### 3\. Cross\-Market Research

Analyze stocks across different markets with region\-specific rules:

```python
# Analyze Tencent across HK and US markets
prompt = "Compare Tencent's performance in HK and US markets over the past year. Use fundamental and technical factors."
cross_market_report = vibe_trading.generate_report(prompt)
print(cross_market_report.summary)
```

## Why Vibe\-Trading Stands Out

- **No Configuration Hassle**: Tools and factors are pre\-integrated—simply ask, and the Agent handles the rest\.

- **Continuous Iteration**: The project is actively updated, with new features and markets added regularly\.

- **Comprehensive Knowledge**: The 72\-Skill library and 452 factors cover both mainstream and niche financial analyses\.

## Getting Started

To start using Vibe\-Trading:

1. Clone the repository:

```bash
git clone https://github.com/HKUDS/Vibe-Trading.git
cd Vibe-Trading
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the demo:

```python
from vibe_trading import VibeTradingAgent

agent = VibeTradingAgent()
response = agent.query("Analyze Moutai's stock using a value-investing approach.")
print(response)
```

Vibe\-Trading is revolutionizing how financial professionals conduct research and analysis\. Its agent\-driven architecture, rich toolset, and collaborative framework make it a must\-try for anyone in the global financial sector\.

