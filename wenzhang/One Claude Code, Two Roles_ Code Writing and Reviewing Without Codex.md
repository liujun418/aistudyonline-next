# One Claude Code, Two Roles: Code Writing and Reviewing Without Codex



In the world of AI\-assisted coding, many developers think you need two models like Claude Code and Codex to handle writing and reviewing\. But what if you only have Claude Code? This guide shows you how to use a single Claude Code model to both write and review code by leveraging isolated contexts, with practical steps and code examples\.

## Why One Model Can Do Both: Isolated Contexts Matter

The key isn’t having a second model; it’s having a **second clean context**\. When a model reviews its own code in the same conversation, it’s biased by its original implementation\. A separate context, however, acts like a fresh pair of eyes—one that hasn’t seen the coding process and only focuses on the code itself\.

For example, if you ask Claude Code to review its own code in the same chat, it might miss issues like:

- Memory leaks in idempotent keys that aren’t cleaned up\.

- Race conditions in high\-concurrency order systems\.

A separate review agent in its own context catches these because it’s not influenced by how the code was written\.

## Setting Up a Code\-Review Agent in Claude Code

To create a dedicated review agent, you need a configuration file\. Here’s how to do it:

### Step 1: Create the Agent Configuration File

In your project’s `.claude/agents/` directory, create a file named `code-reviewer.md`\. This file has two parts: frontmatter \(configuration\) and a prompt \(instructions for the reviewer\)\.

```markdown
---
name: code-reviewer
description: Review code changes for issues.
tools: Read, Grep, Glob, Bash
model: inherit
---
# Code Review Guidelines
01. Focus only on identifying issues, not fixing them. List problems clearly.
02. Check for memory leaks, especially in idempotent implementations.
03. Verify concurrency safety for high-traffic features.
04. Ensure code follows best practices (readability, maintainability).
05. Use `git diff` to understand changes and review only the modified parts.
06. Report issues without suggesting code changes—leave fixes to the main conversation.
```

### Step 2: Understand the Configuration

- **`name`**: Identifies the agent \(e\.g\., `code-reviewer`\)\.

- **`description`**: Tells the main Claude Code when to use this agent\.

- **`tools`**: Limits the agent to read\-only tools \(`Read`, `Grep`, `Glob`\) and `git diff` \(via Bash\) to analyze changes\. No write/edit tools to prevent it from fixing code directly\.

- **`model: inherit`**: Uses the same model as the main conversation \(so you don’t need Codex\)\.

## How to Use the Review Agent in Practice

Once set up, using the agent is straightforward:

1. **Write Code in the Main Conversation**:
Ask Claude Code to write code, e\.g\., "Implement an idempotent order API to prevent duplicate orders\."

2. **Trigger the Review Agent**:
After the code is written, request a review: "Use `code-reviewer` to check the recent idempotent order API changes\."

3. **Analyze the Feedback**:
The review agent will generate a list of issues\. For example, it might point out:

    - "Idempotent keys are not cleaned up, leading to memory bloat\."

    - "Race condition in concurrent order requests\."

4. **Fix Issues in the Main Conversation**:
Go back to the main chat and address the issues, then repeat the review process for high\-risk changes\.

## When to Use the Review Agent \(and When to Skip\)

Not all changes need a full review\. Use this **risk\-based checklist** to decide:

- **High\-Risk Changes \(Use the Review Agent\)**:

    - Authentication/authorization logic\.

    - Financial transactions \(e\.g\., payment systems\)\.

    - Data deletion features\.

    - High\-concurrency features \(e\.g\., order processing\)\.

- **Low\-Risk Changes \(Skip the Review\)**:

    - UI text or style tweaks\.

    - Documentation updates\.

    - Small refactors with no business logic changes\.

## Beyond Claude Code: Applying This to Codex

This approach isn’t limited to Claude Code\. If you use Codex, you can create a similar review agent in `.codex/agents/reviewer.md` with the same structure\. Codex even has a built\-in `/review` command for one\-click reviews, working the same way as Claude Code’s `code-reviewer`\.

## Conclusion

You don’t need two models to write and review code\. With a single model like Claude Code \(or Codex\) and isolated contexts, you can catch critical issues that self\-reviews miss\. Use the configuration and workflow above to implement this in your projects, and rely on the risk checklist to decide when a review is necessary\. This method saves you from hidden bugs and ensures your AI\-written code is robust\.
