# Anthropic Harness Dynamic Workflows — Full Practical Guide for Claude Code Developers



Anthropic officially released the brand\-new **Dynamic Workflow Harness** system for Claude Code, completely upgrading large\-scale multi\-agent task orchestration\. Unlike rigid fixed pipelines, this dynamic harness lets Claude autonomously plan, split tasks, run parallel sub\-agents, verify results and resume interrupted long jobs, perfectly solving complex cross\-file engineering tasks that single\-pass AI cannot handle\.

## Core Architecture \& Advantages

- Claude automatically generates executable orchestration scripts, storing task logic outside the context window instead of relying on limited token context\.

- Supports **tens to hundreds of parallel subagents** in one session, suitable for massive codebase debugging, full\-project migration, multi\-round security audits and long\-duration research tasks\.

- Built\-in result verification mechanism: independent review agents check outputs before final delivery, greatly reducing errors\.

- Breakpoint resume: long\-running tasks can pause and continue without restarting, stable for hours or even days of continuous operation\.

- Compatible with Claude Code CLI, desktop app, VS Code extension, Claude API, Amazon Bedrock, Vertex AI and Microsoft Foundry\.

## Access \& Permission Rules

- Max \& Team plans: Dynamic Workflows enabled by default\.

- Enterprise plans: Requires administrator manual activation\.

- Pro users: Need to turn on the feature manually in settings\.

- Important reminder: Dynamic workflows consume far more tokens than normal sessions; large\-scale Opus tasks may sharply increase usage costs\.

## Practical Startup Commands \& Operations

### Enable UltraCode High\-Efficiency Mode

```bash
/effort xhigh
```

Switch Claude to maximum computing power mode, matching complex dynamic workflow execution\.

### Start Custom Dynamic Workflow Directly

```plaintext
Create dynamic harness workflow to scan all bugs across backend service files, run parallel audits and output fixed solutions
```

### Bind Workflow with Auto Goal Loop

Combine `/goal` and `/loop` for unattended automatic operation overnight:

```bash
/goal Finish full legacy code migration, pass all unit tests, stop after 30 iterations
/loop Check migration progress every 10 minutes, report abnormal node status
```

### View Running Workflow Status

```bash
/workflow status
```

### Stop Ongoing Dynamic Task

```bash
/workflow clear
```

## Best Use Cases \& Avoid Scenarios

✅ Ideal scenarios

- Cross\-hundreds\-of\-files legacy code reconstruction

- Full\-codebase vulnerability detection \& repair

- Large\-scale multi\-module joint debugging

- Multi\-round adversarial review of technical schemes

❌ Not recommended

- Simple single\-file code writing \& modification

- Short daily prompt queries

- Low\-complexity routine tasks \(will waste massive tokens unnecessarily\)

## Practical Usage Tips

1. Always turn on Auto Mode to reduce manual confirmation prompts\.

2. Start with small\-scoped tasks first to test token consumption rules\.

3. Use lightweight Sonnet for routine subtasks, switch Opus only for core complex links\.

4. Combine custom Skills to further cut redundant token overhead\.
