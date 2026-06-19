# Mastering Long\-Running AI Coding Tasks with GLM 5\.2 and Claude Code

In the realm of AI\-assisted software development, running large\-scale projects over extended periods has long been a challenge\. However, with the advent of models like Zhiyuan's GLM 5\.2 and tools like Claude Code, it's now feasible to automate complex tasks for hours, even with massive codebases\. This article dives into a practical case study where we leveraged these technologies to port the 400,000\-line TypeScript project OpenClaw to Python, showcasing the power of long\-context AI models and structured task management\.

## Unleashing the Power of GLM 5\.2 and Claude Code

GLM 5\.2, recently released by Zhiyuan, stands out with its **million\-token context window** and optimized attention mechanisms, making it capable of handling large\-scale, long\-duration tasks\. Paired with Claude Code’s `goal` command for looped execution, we have a robust setup for end\-to\-end AI\-driven development\.

### Why This Matters

Most AI models struggle with "lost in the middle" issues when context windows overflow\. GLM 5\.2’s architectural improvements minimize this, ensuring it stays on track even after 13\+ hours of continuous operation—critical for projects like OpenClaw, which has 10\+ core modules and 400,000\+ lines of code\.

## Step 1: Project Analysis and Task Breakdown

Before diving into code, we need to dissect the project and define clear tasks\.

### Reading and Analyzing the Codebase

First, clone the OpenClaw repository and use Claude Code’s agent capabilities to map the architecture:

```bash
git clone --depth 1 <OpenClaw-repo-url>
cd python-openclaw
```

Then, use a prompt to trigger multi\-agent analysis \(leveraging Claude Code’s `Superpowers`\):

```text
Analyze all .ts files in the 'ts-reference/' directory. 
1. Map import dependencies and draw a call graph.
2. Identify core modules (utils, agents, plugins, etc.).
3. Document the dependency hierarchy from bottom to top.
4. List each module’s responsibilities and file count.
```

This generates a structured report outlining the project’s architecture, like:

- **Layer 1 \(Utils\):** `utils/shared-types` \(214 files\) – pure utility functions\.

- **Layer 2 \(Infrastructure\):** `logging`, `infra`, `terminal` \(273 files\) – logging, environment management, and terminal rendering\.

- **Layer 3 \(Agent Core\):** `agents`, `auto-reply`, `context-engine` \(529 files\) – core AI agent logic\.

### Breaking Down Tasks

With the architecture mapped, we split the project into granular tasks using another prompt \(relying on Claude Code’s `writing-plans` skill\):

```text
For each module in docs/specs/, break down into function-level tasks.
- Each task must include:
  - A clear requirement (e.g., "Implement compaction for message summarization").
  - At least 3 test cases (e.g., `test_empty_messages_returns_empty_string`).
  - A validation method (e.g., "Run `pytest` and ensure 100% coverage").
- Generate a progress.json file to track task status.
```

This yields a list of **443 tasks**, each with precise 验收 criteria \(acceptance criteria\)\. For example, a task for the `agents` module might look like:

```text
## Task 154: Compaction for Message Summarization
- **Requirement:** Implement `summarize_messages(messages, model)` to generate a summary of chat history.
- **Test Cases:**
  1. `test_summarize_single_message_returns_text`
  2. `test_empty_messages_returns_empty_string`
  3. `test_fallback_truncation_when_model_fails`
- **Validation:** Run `pytest --cov=agents` and ensure coverage ≥ 90%.
```

## Step 2: Long\-Running Execution with `goal` Command

Claude Code’s `goal` command enables looped execution, where the model fetches tasks from `progress.json`, executes them, and updates status iteratively\.

### The `goal` Command Setup

Use this compressed prompt \(to avoid formatting errors\) and set `bypass permissions on` to skip redundant confirmations:

```text
/goal Iterate over all tasks in docs/plans until python check_progress.py returns 0. 
- Read progress.json to get the first pending task.
- Execute all test cases defined in the task (at least 3).
- If tests fail (RED), stop and mark as failed.
- If tests pass (GREEN), run `ruff check` and `ruff format --check`; fix any issues.
- Commit changes with `git commit --task=N`.
- Update progress.json (done, completed+1, rounds+1).
- Stop if `check_progress.py` returns 0; else, continue.
```

Execute it in Claude Code with:

```text
/bypass permissions on
/goal <prompt-text>
```

### What Happens During Execution

The model runs for 13\+ hours, handling:

- **Code Generation:** Writing Python equivalents for TypeScript modules\.

- **Testing:** Automatically running `pytest` and linting with `ruff`\.

- **Version Control:** Committing changes for each task\.

- **Progress Tracking:** Updating `progress.json` to reflect completed tasks\.

## Step 3: Validation and Iteration

Post\-execution, validate the output and refine as needed\.

### Testing the Python Port

The Python version of OpenClaw \(dubbed "Lobster Chat"\) should replicate core features:

- **Web Chat:** A functional chat interface \(test by visiting `http://localhost:8080`\)\.

- **Skill Execution:** Run pre\-installed skills like image generation:

    ```text
    Generate a photo of a woman in a forest, photorealistic style.
    ```

- **Tool Usage:** Fetch web content and save to local files:

    ```text
    Download the GLM-5.1 technical document from <url> and save as GLM-5.1.md.
    ```

### Iterating on Feedback

If issues arise \(e\.g\., repetitive task execution\), simply prompt the model to fix it:

```text
The agent is repeating historical tasks. Fix the loop to avoid duplication.
```

GLM 5\.2’s improved instruction\-following ensures most fixes are implemented in one go\.

## Key Takeaways and Limitations

- **Strengths:** GLM 5\.2 excels at long\-context tasks, making it viable for enterprise\-grade projects \(e\.g\., legacy code refactoring, cross\-module API development\)\.

- **Limitations:** As a text\-only model, it struggles with UI/UX aesthetics and cannot process image\-based feedback\.

- **Future Outlook:** A multi\-modal version of GLM would address these gaps, enabling even more versatile AI\-driven development\.

By combining GLM 5\.2’s context capabilities with Claude Code’s workflow tools, we’ve demonstrated that AI can now handle end\-to\-end development of large\-scale projects\. This isn’t just a technical demo—it’s a glimpse into the future of software engineering, where AI takes the reins on grunt work, freeing developers to focus on innovation\.

