# Mastering Claude Code CLI: A Practical Guide for Overseas Developers

If you\&\#39;re an overseas developer looking to leverage AI for coding efficiency, Claude Code is a powerful tool worth mastering\. This guide breaks down its practical usage, focusing on the CLI version, to help you build applications seamlessly\.

## Understanding Claude Code Versions

Claude Code comes in two versions:

- **CLI \(Command\-Line Interface\)**: Ideal for developers who prioritize efficiency and resource\-friendliness\. It integrates easily with third\-party tools and is perfect for automated workflows\.

- **Desktop GUI**: Suited for those who prefer visual interfaces, offering code comparison and task planning panels\.

For most developers, the CLI version is recommended due to its speed, low resource usage, and flexibility in integrating with tools like Git and Node\.js\.

## Environment Setup

To get started, you’ll need:

- **Node\.js**

- **Git**

For Windows users, you can install Claude Code via the following command:

```bash
winget install Anthropic.ClaudeCode
```

If you encounter network issues, be patient—the installation will complete eventually\.

## Launching Claude Code

To start Claude Code:

1. Right\-click in any folder and select \&\#34;Open in Terminal\&\#34;\.

2. In the terminal, type:

    ```bash
    claude
    ```

This opens the Claude Code interface, ready for your commands\.

## Project Organization Best Practices

When working on projects, follow these steps:

1. Create a project folder with **English\-only names** \(e\.g\., `test\-project`\)\. This avoids errors since most programming tools are designed for English\.

2. Navigate to the folder and open the terminal there\. Launching Claude Code from within the project folder ensures it focuses on your project’s context\.

## Core Modes and Commands

Claude Code operates in three key modes, switchable via `Shift \+ Tab`:

- **Default Mode**: Prompts for confirmation at each step \(stable but slower\)\.

- **Auto Mode**: Executes commands automatically \(fast but less control\)\.

- **Plan Mode**: Generates detailed project plans without executing code \(great for planning\)\.

### Recommended Workflow:

1. Use **Plan Mode** to outline your project structure\.

2. Switch to **Auto Mode** to implement the plan\.

When executing sensitive commands, Claude Code will prompt you with three options:

- Approve once\.

- Approve and authorize for future actions\.

- Reject\.

## Managing Conversations and Context

- **Resume Conversations**: Use the `/resume` command to access past chat histories:

    ```bash
    /resume
    ```

- **Undo Actions**: Double\-press `ESC` to revert to the state before the last action \(a handy \&\#34;undo\&\#34; feature\)\.

- **Optimize Context**:

    - Use `/compact` to summarize and compress context\.

    - Use `/clear` to reset the context entirely\.
    Maintaining context under 50% usage ensures optimal performance\.

## Advanced Features

To truly master Claude Code, explore these advanced features:

- **Skills**: A standardized guide for AI to perform tasks more reliably\.

- **MCP \(Modular Capability Protocol\)**: An extension protocol to access external tools and services beyond the local environment\.

- **Hooks**: An automation trigger system for seamless development workflows\.

For in\-depth learning, check out the open\-source repository [claude\-howto](https://github.com/yourusername/claude-howto) on GitHub, a comprehensive resource with 29\.8K stars\.

With these practical steps and commands, you’re ready to harness Claude Code CLI for your overseas development projects\. Happy coding\!

