# Mastering CC Switch: The Ultimate Tool for Managing AI Coding Tools

As an AI developer, juggling multiple AI coding tools like Claude Code, Codex, and Gemini CLI can be a hassle, especially when switching between them and managing configurations\. Enter **CC Switch**—a cross\-platform desktop application \(supporting Mac, Linux, and Windows\) designed to unify the management of these tools\. In this guide, we’ll walk through its features and how to use it effectively\.

## What is CC Switch?

CC Switch acts as a central hub for AI coding tools\. It eliminates the need to manually edit configuration files \(like `settings.json` for Claude Code, `agent.toml` for Codex, and `.env` for Gemini CLI\) when switching AI providers\. With CC Switch, you can:

- Switch between AI providers with a single click\.

- Manage Skills, system prompts, conversation history, and MCP services globally\.

- Track usage costs across different AI tools to identify the most cost\-effective options\.

## Getting Started with CC Switch

### Step 1: Download and Install

1. Visit the [CC Switch official website](https://example.com/cc-switch-download) \(replace with actual URL\)\.

2. Select the version corresponding to your operating system \(Windows, Mac, or Linux\)\.

3. Run the installer and follow the on\-screen instructions\. Once installed, launch CC Switch\.

### Step 2: Initial Setup

When you first open CC Switch, you’ll see the main interface\. Here’s what you need to do first:

- **Skip Claude Code Initial Setup**: Click the settings icon in the top\-left corner\. Scroll down to the “General” section and enable the “Skip Claude Code Initial Setup” option\. This skips the Anthropic login prompt when using Claude Code, a common fix for network issues when starting out\.

## Configuring AI Providers

To add and switch between AI providers:

1. Click the `+` icon in the top\-right corner of CC Switch\.

2. Choose an AI provider from the preset list \(e\.g\., Kimi for Coding\)\.

3. **Configure API Keys and Models**:

    - For example, with Kimi for Coding:

        - Go to the Kimi Code console and create a new API key\.

        - Paste the API key into CC Switch’s configuration field\.

        - In the advanced options, set the model \(e\.g\., Kimi 2\.5\) and enable features like 1M context window\.

4. Click “Add” to save the configuration\. You’ll now see the new provider in the list\. To switch, simply click “Enable” next to the provider\.

## Managing Skills

Skills are reusable tools that can be used across multiple AI coding tools\. Here’s how to manage them:

1. Click the wrench icon in the top\-right corner to open the Skills Manager\.

2. **Import Existing Skills**: Click “Import Existing” to scan your system for installed skills\.

3. **Install New Skills**:

    - Use the search bar to find skills \(switch the search type to `skill.sh` for better results\)\.

    - For example, search for “subtitle” to find skills related to subtitle extraction\.

    - Click “Install” to add a skill\. You can also install skills from ZIP files by clicking “Install from ZIP”\.

4. **Update Skills**: Click “Check for Updates” to update installed skills to their latest versions\.

## System Prompt Management

CC Switch lets you manage system prompts across all AI tools:

1. Click the text icon in the top\-right corner to open Prompt Management\.

2. **Add a Prompt**:

    - Click “Add Prompt” and name it \(e\.g\., “Frontend Project”\)\.

    - Paste your system prompt into the content field and save\.

3. **Switch Prompts**: Use the toggle switch next to a prompt to apply it across all AI tools\. This automatically updates the corresponding configuration files \(like `claude.md` for Claude Code, `agent.md` for Codex\)\.

## Conversation History Management

To manage and restore conversations:

1. Click the history icon in the top\-right corner\.

2. **Search and Filter**: Use the search bar to find specific conversations\.

3. **Restore Conversations**: Copy the command provided by CC Switch and paste it into your terminal to restore a conversation in tools like Claude Code\.

4. **Delete Conversations**: Select conversations and click “Delete” to remove them from your system\.

## MCP Service Management

MCP \(Model Control Protocol\) services extend the functionality of AI tools\. To manage them:

1. Click the MCP icon in the top\-right corner\.

2. **Add an MCP Service**:

    - Choose a preset MCP service \(e\.g\., `fetch` for web requests\) or create a custom one\.

    - Configure the service details, including API keys and execution commands\.

    - Apply the MCP service to your desired AI tools\.

3. **Test the MCP Service**: In Claude Code, use the `MCP` command to test the service \(e\.g\., `MCP fetch https://example.com` to fetch a web page\)\.

## Tracking Usage Costs

To track how much you’re spending on each AI tool:

1. Go to Settings \> Usage Statistics\.

2. **View Metrics**: See token usage, request counts, and costs for tools like Claude Code, Codex, and Gemini\.

3. **Cost Comparison**: Use the cost breakdown to identify which tool is the most affordable\. You can also set cost multipliers for proxy services\.

## Conclusion

CC Switch is a game\-changer for AI developers, simplifying the management of multiple AI coding tools\. By centralizing configuration, skills, prompts, and usage tracking, it saves time and reduces errors\. Whether you’re switching between AI providers, managing skills, or keeping an eye on costs, CC Switch has you covered\. Try it today and streamline your AI development workflow\!
