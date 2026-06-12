# Build a Large\-Cap Investment Research Dashboard with Claude Code: A Step\-by\-Step Guide



Investment research requires aggregating, analyzing, and visualizing financial data efficiently—especially for large\-cap stocks\. With Claude Code, you can build a fully functional investment research dashboard in minutes, even with minimal coding experience\. This guide walks you through creating a dashboard that pulls real\-time stock data, calculates key financial metrics, and visualizes trends—perfect for tracking large\-cap companies \(market cap ≥ $10B\)\.

## Why Claude Code for Investment Dashboards?

- **Natural Language to Code**: Explain financial logic in plain English \(e\.g\., "Calculate P/E ratio"\) without complex syntax\.

- **Data Integration Expertise**: Seamlessly connects to financial APIs \(Yahoo Finance, Alpha Vantage\) with pre\-built code snippets\.

- **Real\-Time Debugging**: Fixes data parsing, visualization, and metric calculation errors on the fly\.

- **Customization Flexibility**: Tweak charts, metrics, and data sources with simple prompts—no need to rewrite entire code blocks\.

## Prerequisites

- A free Anthropic account \(sign up at [anthropic\.com](https://anthropic.com)\)\.

- VS Code with the [Claude Code extension](https://marketplace.visualstudio.com/items?itemName=Anthropic.claude-code) \(install via Marketplace\)\.

- Basic understanding of financial metrics \(P/E ratio, market cap, revenue growth\) is helpful but not required\.

- API key for Alpha Vantage \(free tier available at [alpha\-vantage\.co](https://www.alphavantage.co/)—needed for real\-time stock data\)\.

## Step 1: Set Up the Project \(5 Minutes\)

1. Open VS Code, create a new folder `investment_dashboard` and a file `dashboard.py`\.

2. Activate Claude Code \(Ctrl\+Shift\+P → "Claude Code: Open Assistant"\)\.

3. Install required libraries by asking Claude Code:

    ```plaintext
    List the Python libraries needed for a stock research dashboard (data fetching, visualization, metrics) and provide the pip install command.
    ```

4. Run the generated install command in VS Code Terminal:

    ```bash
    pip install yfinance alpha_vantage pandas matplotlib streamlit
    ```

    - `yfinance`: Free stock data from Yahoo Finance \(fallback if Alpha Vantage limits are hit\)\.

    - `alpha_vantage`: Real\-time financial data \(earnings, cash flow\)\.

    - `pandas`: Data cleaning and analysis\.

    - `matplotlib`: Basic charts\.

    - `streamlit`: Builds interactive web dashboards \(no frontend coding needed\)\.

## Step 2: Fetch Real\-Time Large\-Cap Stock Data \(10 Minutes\)

We’ll pull data for 3 large\-cap stocks \(Apple, Microsoft, Amazon\) using Alpha Vantage and yfinance\. Ask Claude Code:

```plaintext
Write Python code to:
1. Fetch real-time stock prices, market cap, P/E ratio, and revenue growth for AAPL, MSFT, AMZN using Alpha Vantage (use my API key: YOUR_API_KEY).
2. Fall back to yfinance if Alpha Vantage rate limits are exceeded.
3. Store data in a pandas DataFrame with columns: Ticker, Price, Market_Cap, PE_Ratio, Revenue_Growth.
```

### Generated Code \(Customize with Your API Key\)

```python
import pandas as pd
import yfinance as yf
from alpha_vantage.fundamentaldata import FundamentalData

# Replace with your Alpha Vantage API key
API_KEY = "YOUR_API_KEY"
fd = FundamentalData(key=API_KEY, output_format='pandas')

def fetch_large_cap_data(tickers):
    data = []
    for ticker in tickers:
        try:
            # Fetch Alpha Vantage data (income statement for revenue growth, overview for market cap/PE)
            income_stmt, _ = fd.get_income_statement_annual(ticker)
            overview, _ = fd.get_company_overview(ticker)
            
            # Extract metrics (latest data = first row)
            latest_revenue = income_stmt.loc['totalRevenue'].iloc[0]
            prev_revenue = income_stmt.loc['totalRevenue'].iloc[1]
            revenue_growth = ((latest_revenue - prev_revenue) / prev_revenue) * 100
            
            price = float(overview['LatestStockPrice'][0])
            market_cap = float(overview['MarketCapitalization'][0])
            pe_ratio = float(overview['PERatio'][0])
            
            data.append({
                'Ticker': ticker,
                'Price': round(price, 2),
                'Market_Cap': round(market_cap / 1e9, 2),  # Convert to billions
                'PE_Ratio': round(pe_ratio, 2),
                'Revenue_Growth': round(revenue_growth, 2)
            })
        except Exception as e:
            # Fallback to yfinance if Alpha Vantage fails/rate-limited
            print(f"Alpha Vantage error for {ticker}—using yfinance: {e}")
            stock = yf.Ticker(ticker)
            info = stock.info
            data.append({
                'Ticker': ticker,
                'Price': round(info.get('currentPrice', 0), 2),
                'Market_Cap': round(info.get('marketCap', 0) / 1e9, 2),
                'PE_Ratio': round(info.get('trailingPE', 0), 2),
                'Revenue_Growth': round(info.get('revenueGrowth', 0) * 100, 2)
            })
    return pd.DataFrame(data)

# Fetch data for large-cap stocks
large_cap_tickers = ["AAPL", "MSFT", "AMZN"]
df = fetch_large_cap_data(large_cap_tickers)
print("Large-Cap Stock Data:")
print(df)
```

### Test the Data Fetch

Run the code—you’ll see a DataFrame with key metrics for the 3 stocks\. If you hit Alpha Vantage’s free tier limit \(5 requests/minute\), yfinance will automatically take over\.

## Step 3: Build an Interactive Dashboard with Streamlit \(15 Minutes\)

Streamlit turns Python scripts into web apps with zero frontend code\. Ask Claude Code:

```plaintext
Use Streamlit to build an interactive dashboard for the large-cap stock DataFrame:
1. Add a title "Large-Cap Investment Research Dashboard".
2. Display the DataFrame as a table with sorting.
3. Add 3 charts:
   - Line chart: Stock prices over the last 30 days (use yfinance for historical data).
   - Bar chart: Revenue growth by ticker.
   - Scatter plot: P/E ratio vs. Market Cap (color-code by ticker).
4. Add a sidebar to select tickers (allow multiple selection).
```

### Generated Dashboard Code

```python
import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

# Set page config
st.set_page_config(page_title="Large-Cap Investment Dashboard", layout="wide")

# Title and sidebar
st.title("📊 Large-Cap Investment Research Dashboard")
st.sidebar.header("Select Tickers")
selected_tickers = st.sidebar.multiselect(
    "Choose large-cap stocks",
    options=large_cap_tickers,
    default=large_cap_tickers
)

# Filter DataFrame by selected tickers
filtered_df = df[df['Ticker'].isin(selected_tickers)]

# Display data table
st.subheader("Key Financial Metrics")
st.dataframe(filtered_df, use_container_width=True)

# 1. Line chart: 30-day stock prices
st.subheader("30-Day Stock Price Trend")
historical_data = yf.download(selected_tickers, period="30d", progress=False)['Close']
st.line_chart(historical_data, use_container_width=True)

# 2. Bar chart: Revenue growth
st.subheader("Revenue Growth (%)")
plt.figure(figsize=(10, 5))
bars = plt.bar(filtered_df['Ticker'], filtered_df['Revenue_Growth'], color=['#1f77b4', '#ff7f0e', '#2ca02c'])
plt.xlabel("Ticker")
plt.ylabel("Revenue Growth (%)")
plt.title("Large-Cap Revenue Growth")
st.pyplot(plt)

# 3. Scatter plot: P/E Ratio vs. Market Cap
st.subheader("P/E Ratio vs. Market Cap (Billion $)")
plt.figure(figsize=(10, 5))
for ticker in selected_tickers:
    ticker_data = filtered_df[filtered_df['Ticker'] == ticker]
    plt.scatter(
        ticker_data['Market_Cap'],
        ticker_data['PE_Ratio'],
        label=ticker,
        s=100  # Marker size
    )
plt.xlabel("Market Cap (Billion $)")
plt.ylabel("P/E Ratio")
plt.title("Valuation vs. Size")
plt.legend()
st.pyplot(plt)
```

### Run the Dashboard

Add this code to `dashboard.py` and run it with:

```bash
streamlit run dashboard.py
```

A browser window will open with your interactive dashboard—you can sort metrics, select tickers, and zoom into charts\.

## Step 4: Add Advanced Features \(10 Minutes\)

Enhance the dashboard with Claude Code’s help\. Try these prompts:

### Prompt 1: Add Dividend Yield

```plaintext
Update the data fetch function to include dividend yield (using Alpha Vantage/yfinance) and add it to the DataFrame and dashboard table.
```

### Prompt 2: Compare to S\&P 500

```plaintext
Add a line to the price trend chart showing the S&P 500 (^GSPC) over the same 30-day period for benchmarking.
```

### Prompt 3: Add Valuation Score

```plaintext
Calculate a "Valuation Score" (1-10) for each stock:
- PE Ratio < 20: +3 points
- Revenue Growth > 10%: +3 points
- Dividend Yield > 2%: +2 points
- Market Cap < $500B: +2 points
Add the score to the DataFrame and a bar chart to the dashboard.
```

### Example of Updated Valuation Score Code

Claude Code will generate this function—add it after fetching the DataFrame:

```python
def calculate_valuation_score(row):
    score = 0
    # PE Ratio < 20
    if row['PE_Ratio'] > 0 and row['PE_Ratio'] < 20:
        score += 3
    # Revenue Growth > 10%
    if row['Revenue_Growth'] > 10:
        score += 3
    # Dividend Yield > 2% (add dividend_yield to row first)
    if row.get('Dividend_Yield', 0) > 2:
        score += 2
    # Market Cap < $500B
    if row['Market_Cap'] < 500:
        score += 2
    return min(score, 10)  # Cap at 10

# Add score to DataFrame
filtered_df['Valuation_Score'] = filtered_df.apply(calculate_valuation_score, axis=1)

# Add to dashboard
st.subheader("Valuation Score (1-10)")
st.bar_chart(filtered_df.set_index('Ticker')['Valuation_Score'], use_container_width=True)
```

## Step 5: Deploy the Dashboard \(5 Minutes\)

Share your dashboard with teammates or clients using Streamlit Community Cloud:

1. Push your code to a GitHub repository \(create a new repo, add `dashboard.py` and a `requirements.txt` file\)\.

2. The `requirements.txt` should list all libraries:

    ```Plain Text
    yfinance
    alpha_vantage
    pandas
    matplotlib
    streamlit
    ```

3. Go to [share\.streamlit\.io](https://share.streamlit.io/), sign in with GitHub, and click "New app"\.

4. Select your repo, branch, and `dashboard.py` file—click "Deploy"\.

5. Your dashboard is now live \(e\.g\., `https://your-username-investment-dashboard.streamlit.app`\)\.

## Pro Tips for Claude Code Dashboard Development

1. **Be Specific About Metrics**: Instead of "add financial data", say "add free cash flow margin and debt\-to\-equity ratio"\.

2. **Iterate Quickly**: If a chart looks messy, ask "Make the bar chart horizontal and sort by revenue growth descending"\.

3. **Handle Edge Cases**: Prompt "Add error handling for missing data \(e\.g\., if PE ratio is NaN, show 'N/A' in the table\)"\.

4. **Customize Design**: Ask "Change the dashboard theme to dark mode and use brand colors \(blue, green, orange\) for charts"\.

## Common Use Cases for Investors

- **Large\-Cap Screening**: Filter stocks by valuation score, revenue growth, or dividend yield\.

- **Benchmarking**: Compare individual stocks to the S\&P 500 or industry peers\.

- **Real\-Time Monitoring**: Refresh data with a button \(add `st.button("Refresh Data")` to the dashboard\)\.

- **Reporting**: Export the DataFrame to CSV/Excel with `st.download_button`\.

## Conclusion

With Claude Code, building a professional investment research dashboard doesn’t require advanced coding skills—just plain English prompts and a clear vision of your metrics\. This dashboard gives you real\-time insights into large\-cap stocks, helping you make data\-driven investment decisions\. Start by testing with 3\-5 stocks, then expand to include industry peers, sector data, or custom metrics \(e\.g\., ESG scores\)\.

Need me to help you add a specific feature to the dashboard \(e\.g\., ESG data integration, technical indicators like RSI, or email alerts for price changes\)?

