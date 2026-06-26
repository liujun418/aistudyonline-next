# Claude Code Workflow: From Writing Code to Orchestrating Agent Teams

Claude Code has just rolled out a major update—**Workflow**, a feature that transforms Claude Code from a solo coder into an orchestrator of agent teams\. This innovation might be Anthropic’s next big leap following MCP and Skill, and here’s how it works in practice\.

## What Makes Claude Code Workflow Different?

When you think of workflow tools, Dify or Coze might come to mind\. But Claude Code’s Workflow is unique:

- Describe a task, and Claude automatically writes a **JavaScript orchestration script**\.

- It breaks tasks into stages, assigns each stage to different agents, and coordinates dozens to hundreds of subagents in the background to deliver results\. This significantly boosts the feasibility of complex tasks\.

Unlike the temporary Agent Teams of the past, Workflow **solidifies agent coordination into code**\. It becomes auditable, reusable, and version\-controllable—no more relying on the model’s on\-the\-spot performance\.

## Deep Dive into the Built\-in Deep\-Research Workflow

Let’s take the official `deep-research` workflow as an example\. It consists of five stages:

### 1\. Scope: Multidimensional Disassembly

Break down your question into search terms from 5 different angles to ensure comprehensive coverage\.

### 2\. Search: Parallel Search

5 agents search simultaneously, each fetching 4–6 results for their assigned angle—no waiting for each other\.

### 3\. Fetch\-Extract: Deduplication and Extraction

After deduplication, up to 15 webpages are crawled\. Each page yields 2–5 verifiable concrete conclusions\.

### 4\. Verify: Cross\-Validation

For each conclusion, 3 skeptical agents independently look for counterevidence\. Conclusions with 2 or more objections are rejected\.

### 5\. Synthesize: Merge and Synthesize

Merge verified conclusions, sort them by confidence, and compile a final report with source citations\.

## Practical Demo: Researching Claude Code Workflow

To test this, we used `deep-research` to investigate Claude Code’s latest Workflow feature and write an article\. Here’s what happened:

- **Time**: 25 minutes

- **Agents Involved**: 104

- **Token Usage**: 2\.8 million

- **Claims Verified**: 25

- **Output**: A complete article covering Workflow’s core positioning, differences from Agent Teams, runtime limits, and the built\-in `deep-research` workflow\.

## Budget Control: Avoid Token Overspending

Without budget limits, Workflow could become a “token shredder\.” To prevent this, you can define a budget directly in the task:

```Plain Text
workflow 100k
```

Claude Code will optimize agent count, stage depth, and convergence method based on this budget\.

## How to Use Workflow

There are two ways to activate Workflow:

### 1\. Trigger with a Prompt Word

Mention “workflow” in your prompt\. The word will turn colorful, and Claude will automatically generate a workflow\.

```Plain Text
请 workflow 帮我深度调研 Claude Code 的 Workflow 功能，写一篇文章
```

### 2\. Command Activation

Use `/effort ultracode` to let Claude generate a workflow based on your task:

```Plain Text
/effort ultracode
```

To check the running workflow and agent count, use:

```Plain Text
/workflows
```

## The Significance of Workflow

Claude Code’s Workflow isn’t just a new feature—it’s a signal that AI programming is shifting from individual capability to **organizational capability**\.

- In the past, we asked: *Can a model write code?*

- Later, we asked: *Can an agent complete a task independently?*

- Now, we ask: *Can a system organize multiple agents to complete complex tasks verifiably within a budget?*

This shift opens up new possibilities for tackling large\-scale, multi\-faceted challenges with AI\.

