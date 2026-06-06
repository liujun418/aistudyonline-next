# How to Let Claude Code Automate Tasks While You Sleep: A Practical Guide to Boosting Productivity

As developers, we often find ourselves stuck in a repetitive cycle when using AI coding assistants like Claude Code—constantly prompting, reviewing, and prompting again\. This not only drains our energy but also limits the efficiency of AI\. However, by leveraging specific commands, we can transform Claude Code into a self\-sufficient worker that completes tasks autonomously, even while we sleep\. Here’s a practical breakdown of the key commands and how to use them effectively\.

## 1\. /goal: Define Completion Criteria and Let It Run

The `/goal` command is the cornerstone of autonomous task execution\. Instead of micromanaging each iteration, you define clear completion conditions, and Claude Code will keep working until those conditions are met\.

- **How It Works**: When you use `/goal`, you specify concrete success metrics \(e\.g\., “All tests in `/test/auth` must pass” or “The login page renders without errors”\)\. A built\-in evaluator \(powered by Haiku\) then checks after each iteration if the goal is achieved\.

- **Best Practices**:

    - **Be Specific**: Avoid vague goals like “Fix the bug\.” Instead, write something like:

        ```Plain Text
        /goal Ensure all tests in /test/auth pass, npm test exits with code 0, and no other test files are modified.
        ```

    - **Use Safeguards**: You can set limits like maximum iterations or timeouts:

        ```Plain Text
        /goal Complete the user dashboard with all CRUD operations working. Stop after 20 iterations or 30 minutes.
        ```

    - **Check Status or Cancel**: Use `/goal` to check progress or `/goal clear` to cancel the task\.

To fully leverage `/goal`, combine it with a clear spec \(including objectives, acceptance criteria, and boundaries\), then enable Auto Mode to reduce tool confirmation prompts\. This lets you step away while Claude Code works\.

## 2\. /loop: Monitor Status at Intervals

When you need to track ongoing processes \(e\.g\., deployment status, long\-running builds\), `/loop` is invaluable\. It periodically checks the state so you don’t have to\.

- **Usage Scenarios**:

    - Check deployment status every 5 minutes:

        ```Plain Text
        /loop 5m Check if the production deployment is live and returns a 200 OK.
        ```

    - Let Claude Code dynamically adjust the interval \(shorter when near completion, longer when idle\):

        ```Plain Text
        /loop Check the progress of the data migration job.
        ```

    - Run maintenance checks using default instructions \(from `.claude/loop.md`\):

        ```Plain Text
        /loop
        ```

- **Limitations**: `/loop` isn’t a 24/7 background service\. It works within the current session and consumes tokens even when there’s no change\. For event\-driven needs \(e\.g\., code review comments\), use event\-driven notifications instead\.

## 3\. /batch: Split Large Tasks Into Manageable Units

For big projects \(e\.g\., migrating a codebase to a new framework\), `/batch` splits the work into 5–30 independent units, each handled by a background subagent\.

- **Workflow**:

    1. Provide a high\-level change description:

        ```Plain Text
        /batch Migrate the entire codebase from React Class Components to Function Components with Hooks.
        ```

    2. Review and confirm the split plan\. Ensure boundaries, dependencies, and file scopes are clear to avoid conflicting changes\.

    3. Each subagent works in its own Git worktree, and changes are merged into a single pull request\.

- **Critical Note**: The success of `/batch` depends on proper splitting\. Always review the plan thoroughly before approval\.

## 4\. /simplify: Refine and Clean Up After Changes

After implementing a feature or fix, `/simplify` optimizes the code by reusing helpers, simplifying logic, and fixing security issues\.

- **How to Use**: Run it after a change:

    ```Plain Text
    /simplify Review the recently added payment processing module for code simplicity and security.
    ```

- **Version Consideration**: Since v2\.1\.154, `/simplify` focuses less on correctness bugs \(use `/code-review` for that\)\. Treat it as a pre\-commit cleanup tool, and always verify with tests, linters, and manual reviews\.

## 5\. /debug and /doctor: Troubleshoot Issues

When Claude Code malfunctions \(e\.g\., hooks not triggering, tools not loading\), use these commands:

- **/debug**: Diagnose issues within Claude Code’s workflow\. It provides structured logs to identify problems like uninvoked skills or deprecated API suggestions:

    ```Plain Text
    /debug Investigate why the database connection hook isn’t triggering.
    ```

- **/doctor**: Fix environment, installation, or configuration issues\. Run it first if Claude Code fails to start:

    ```Plain Text
    /doctor Check and fix the local development environment setup.
    ```

## Putting It All Together

The key to autonomous AI coding is clear goal definition\. By using `/goal` with precise specs, complementing it with `/loop` for status tracking, `/batch` for large tasks, `/simplify` for refinement, and `/debug`/`/doctor` for troubleshooting, you can turn Claude Code into a reliable teammate that works while you rest\. Remember, the AI is only as good as the instructions you give—so define your endpoints clearly, and let it handle the rest\.
