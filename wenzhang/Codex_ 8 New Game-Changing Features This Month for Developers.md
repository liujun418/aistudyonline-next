# Codex: 8 New Game\-Changing Features This Month for Developers



For a long time, Codex was seen as a secondary choice compared to tools like Claude Code—just a terminal\-based AI for writing code\. But with its latest updates, Codex has transformed into a **versatile digital coworker** capable of cross\-app tasks, long\-term automations, and even interactive UI manipulations\. Let’s dive into its 8 groundbreaking features with practical examples\.

## 1\. Computer Use: Beyond the Terminal, Into Desktop Apps

Codex now breaks free from terminal limitations—it can **interact with your entire desktop**\. Authorize it, and it gains the ability to view your screen, click UI elements, and type with its own cursor\.

### Practical Example: Figma to Tailwind Workflow

Suppose you need to extract color values from a Figma design and add them to your Tailwind config\. Codex handles this end\-to\-end:

```plaintext
Task: Extract color values from the Figma file "UI Kit.fig" and write them into tailwind.config.js.
```

Codex will:

1. Open Figma, locate the design file\.

2. Screenshot the color palette section, identify hex codes via OCR\.

3. Generate and save the Tailwind config:

```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: '#165DFF',
        secondary: '#36BFFA',
        // ... other colors extracted from Figma
      },
    },
  },
}
```

*Note:* This requires granting Codex full computer access, so use it with caution\.

## 2\. In\-Browser Comment Commands: Talk to Web Pages Directly

Codex introduces a **browser\-based comment system** to manipulate web DOM—no API knowledge needed\.

### Practical Example: Tweak a Local Web Page

1. Open a local HTML preview \(e\.g\., a landing page\)\.

2. Select a button element and add a comment:
`This button’s CTA is too subtle. Make it a prominent primary action with a blue background and rounded corners.`

3. Codex automatically updates the element’s CSS:

```html
<!-- Before -->
<button class="px-4 py-2 border">Submit</button>

<!-- After -->
<button class="px-6 py-3 bg-blue-600 text-white rounded-lg">Submit</button>
```

This works like Google Docs comments but for web UIs—intuitive for both developers and non\-technical users\.

## 3\. Automations: Long\-Term Task Management

Codex’s *Automations* let you set up **scheduled, recurring tasks** that run across days or weeks\.

### Practical Example: Open\-Source Issue Monitoring

```plaintext
Automation Task: Daily check for new performance-related issues in the "react" GitHub repo. For each issue, summarize the problem, reproduction steps, and potential fixes. Store results in a "react-performance-issues.md" file.
```

Codex will:

- Run daily at your specified time\.

- Use GitHub’s API to fetch new issues\.

- Generate a structured report:

```markdown
# React Performance Issues - [Date]
## Issue #1234: Excessive Re-renders in Hooks
- **Problem**: Users report lag when using `useState` with large arrays.
- **Reproduction**: ...
- **Fix Suggestion**: Implement memoization with `useMemo`...
```

## 4\. Pets: Interactive Status Indicators

Codex’s *Pets* are **virtual companions** that float on your screen, showing real\-time task status\.

### How to Use:

- Summon a pet with `/slash pet` \(choose from 8 built\-in options like cats, robots, or create custom ones with `/slash hatch`\)\.

- The pet’s animations indicate what Codex is doing:

    - Sitting idle: Waiting for your input\.

    - Typing animation: Processing a request\.

    - Celebration dance: Task completed\.

Example custom pet prompt:

```plaintext
/slash hatch Create a pixel-art dog that wags its tail when Codex is running a task.
```

## 5\. Mobile Remote Control \(ChatGPT App Integration\)

Codex now integrates with the **ChatGPT mobile app**, letting you remote\-control tasks on your Mac from anywhere\.

### Practical Workflow:

1. Start a long\-running task on your Mac \(e\.g\., a batch data processing script\)\.

2. Leave your desk—open ChatGPT on your phone\.

3. Check task progress, approve intermediate steps, or view diffs:

```plaintext
Ask Codex: "Show me the latest diff for the data processing script."
```

Codex will send a summary or screenshot to your phone\.

## 6\. 90\+ New Plugins: One\-Click Integrations

Codex now supports **90\+ plugins** for tools like:

- *Atlassian Rovo*: Jira issue management\.

- *CircleCI*: CI/CD pipelines\.

- *CodeRabbit*: Code review automation\.

- *Microsoft Suite*: Excel, Word, and PowerPoint integrations\.

### Example: CodeRabbit Integration

```plaintext
Task: Use CodeRabbit to review the PR #123 in my GitHub repo. Highlight security issues and performance bottlenecks.
```

Codex will generate a detailed review:

```markdown
# PR #123 Review - CodeRabbit
## Security Issue: Hardcoded API Key
- File: `src/api.js`
- Line 10: `const API_KEY = "secret-123";`
- Fix: Move to environment variables.

## Performance Bottleneck: Unoptimized Loop
- File: `src/utils.js`
- Line 25: Nested loop with O(n²) complexity.
- Fix: Replace with a hash map for O(n) performance.
```

## 7\. GPT\-5\.5: Faster, Cheaper, and More Powerful

Under the hood, Codex now runs on **GPT\-5\.5**, which is:

- **Faster**: Optimized for NVIDIA GB200/GB300 NVL72 hardware\.

- **Cheaper**: Uses fewer tokens for the same tasks compared to previous models\.

- **More Capable**: Excels at long\-term tasks and complex logic\.

### Cost Comparison Example

For a task that used 1,000 tokens with GPT\-4, GPT\-5\.5 might use only 700 tokens—reducing costs by 30%\.

## 8\. Skill Synergy: Codex \+ Claude Code

Many developers now use **Codex and Claude Code together**:

- *Codex* for fast, daily coding \(keystrokes, UI tweaks, and long tasks\)\.

- *Claude Code* for high\-stakes work \(critical commits, code reviews, and complex refactoring\)\.

Example Workflow:

1. Use Codex to draft a new feature’s UI components quickly\.

2. Switch to Claude Code to refactor the component for performance and add unit tests\.

3. Use Codex’s Automations to monitor the feature’s GitHub issues post\-deployment\.

## Conclusion: Codex as Your Digital Coworker

Codex has evolved from a “coding 备胎” to a **full\-fledged digital coworker**—one that interacts with your desktop, manages long\-term tasks, and even keeps you company with virtual pets\. Whether you’re automating workflows, tweaking UIs, or collaborating remotely, Codex’s new features make it an indispensable tool for modern developers\.


