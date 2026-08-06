# How to Use Codex for Quantitative Strategy Research and Backtesting

## Introduction

This guide demonstrates how to use Codex to conduct quantitative strategy research and backtesting, covering the complete process from installation to validation\. We will use Codex as the primary tool, with khQuant as the underlying command\-line quantitative research tool\.

## 1\. Install Codex

First, complete the installation of Codex\. There are multiple installation methods available online, including:

- Official subscription

- Mirror sites

It is recommended to use the official subscription if possible\.

## 2\. Verify khQuant Installation

Before proceeding, confirm that you have installed the V3 version of khQuant on your local machine\.

## 3\. Test Configuration with Codex

Ask Codex to check your configuration and run built\-in test cases:

```Plain Text
"On this computer, I have installed the khQuant CLI command set and corresponding skills. Please help me check if the configuration is complete, run the built-in examples using the CLI, and generate a backtest report for me."
```

After the execution is complete, you will see the backtest report, which includes key metrics such as:

- Profit and Loss \(PnL\)

- Drawdown \(DD\)

- Transaction statistics \(TRD\)

## 4\. Download Data via Codex

You can also use Codex to command khQuant to download and manage data\. For example, to download the daily data of the Shanghai 50 Index for the past 5 years, including unadjusted, forward\-adjusted, and backward\-adjusted versions:

```Plain Text
"Help me download the daily data of the Shanghai 50 Index for the past 5 years, including unadjusted, forward-adjusted, and backward-adjusted data."
```

After the download is complete, you can ask Codex to summarize the downloaded data:

```Plain Text
"Please summarize the data I just downloaded."
```

## 5\. Check Data in khQuant GUI

You can also open the graphical interface of khQuant and find the database management module to view the downloaded data\.

## 6\. Batch Strategy Research

You can use Codex to conduct batch research on strategy parameters\. For example, to study the golden cross and death cross strategy for a specific stock, and find the optimal long\-term and short\-term moving average parameters:

```Plain Text
"I want to study the golden cross and death cross strategy for a specific stock, but I need to find the optimal long-term and short-term moving average parameters. Please help me call the khQuant skill to generate batch golden cross and death cross strategies, conduct batch backtests, and find the optimal parameters for the past year."
```

After the automatic strategy writing and backtesting are completed, you will obtain the results of the batch strategy research\.

## 7\. Conclusion

The above is an introductory tutorial on how to use Codex to call khQuant for configuration and strategy research\. Once you master this process, you can submit any strategy ideas to the large model for implementation and validation\.

Note: This video uses Codex as the demonstration example\. If you are using Claude Code or other powerful agents, you can also use similar methods to call the toolchain to complete the research\.

---

*This content is adapted from the original video by Mr\. Kanhai\. For more quantitative research tools and ideas, please follow the original author\.*

