# DeepSeek Harness: Complete Beginner's Guide

# DeepSeek Harness: Complete Beginner's Guide

## Introduction

DeepSeek Harness is a powerful AI agent framework that allows you to create, run, and manage plugins with a unique "write on the spot, run on the spot, no restart needed" workflow\. This guide will walk you through installation, configuration, and creating your first plugin\.

## Prerequisites

Before you begin, ensure you have Node\.js 22\+ installed on your system\. Verify your installation with:

```bash
node -v
```

## Installation

There are two installation methods:

### 1\. Quick Try \(Temporary Use\)

For one\-time testing, use the npx command:

```bash
npx @deepseek-ai/dsh web
```

This will start Harness temporarily and open it in your browser at `http://127.0.0.1:3030`\.

### 2\. Permanent Installation \(Recommended\)

For long\-term use, install it globally:

```bash
npm install -g @deepseek-ai/dsh
```

After installation, start Harness with:

```bash
dsh web
```

## Advanced Installation Options

### Headless Mode \(For Servers\)

To run Harness on a server without a GUI, use headless mode:

```bash
# Set your API key first
export DEEPSEEK_API_KEY=your_api_key

# Run a task in headless mode
dsh --profile headless "your task description"
```

### Source Code Build \(For Developers\)

If you want to modify the source code:

```bash
# Clone the repository
git clone https://github.com/deepseek-ai/deepseek-harness.git
cd deepseek-harness

# Install dependencies
pnpm install

# Build the project
pnpm run build

# Run the web interface
pnpm run web

# Or run in headless mode
pnpm dsh --profile headless "your task"
```

## Configuration

### Setting Up Your API Key

1. Open the Harness settings panel

2. Navigate to the "Model" section

3. Enter your DeepSeek API key

4. Save the configuration

Your API key will be stored in a secure credentials file with 0600 permissions, ensuring other users cannot access it\.

### Adding Model Providers

Harness supports multiple model providers, not just DeepSeek\. To add a new provider:

1. Go to Settings \> Model Providers

2. Click "Add Provider"

3. Enter the provider details and API key

4. Save the configuration

## Working Modes

Harness offers four working modes:

### 1\. Standard Mode

- Full\-featured agent

- Supports files, terminals, browsers, and skills

- 90% of your work will be done in this mode

### 2\. Minimal Mode

- Only two tools: terminal and file editor

- Shortest prompts

- Used for benchmarking and testing

### 3\. PTC Mode

- Optimized for token efficiency

- Combines multiple operations into a single script

- Suitable for advanced users concerned about cost

### 4\. Creative Mode

- Adds additional tools for plugin development

- Allows reading and modifying runtime state

- Used for writing and testing plugins on the fly

## Permission Levels

Harness provides three permission levels to control file access:

1. **Read Only**: Safest option, no file modifications allowed

2. **Workspace Write** \(Default\): Only modifies files in your specified workspace directory

3. **Full Access**: Complete system access \(use with caution\)

## Plugin Management

### Finding Plugins

Browse thousands of community plugins on GitHub by searching for the "dsh plugin" tag\.

### Installing Plugins

Install plugins using the command line:

```bash
dsh plugin --profile demo add ./path/to/plugin
```

Or let Harness install plugins for you through the chat interface\.

### Important Notes

- The v0\.1 ecosystem is still young, so some plugins may be untested

- Always check the plugin documentation before installation

- Uninstalling plugins is clean and reversible

## Creating Your First Plugin

Harness's unique "write on the spot" workflow allows you to create and test plugins in real\-time:

1. Switch to Creative Mode

2. Describe your plugin idea in natural language

3. Harness will generate the plugin code

4. Test the plugin immediately without restarting

5. Refine and iterate as needed

For permanent plugins, follow the official development workflow to package and distribute your plugin\.

## Conclusion

DeepSeek Harness provides a unique and powerful platform for AI agent development\. With its intuitive interface, flexible plugin system, and innovative "write on the spot" workflow, it's an excellent choice for both beginners and experienced developers\.

Start with the standard mode to get familiar with the interface, then explore the advanced features and plugin development capabilities as you become more comfortable\.

