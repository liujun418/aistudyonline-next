# Complete Guide to Codex: From Zero to Advanced Development Workflow

## Introduction

Codex is OpenAI's core AI development tool, designed to assist with coding, debugging, testing, and even computer control\. This guide will walk you through the complete workflow of using Codex, from installation to advanced features like plugins, skills, and mobile control\.

## 1\. Installation and Initial Setup

### 1\.1 Download and Install Codex

- Visit the official Codex website and download the installation package\.

- On macOS, drag the Codex app to the Applications folder to complete installation\.

### 1\.2 Login Options

- **ChatGPT Account Login**: Choose from ChatGPT's subscription plans \(Free, Go, Plus, Pro\)\. Plus \($20/month\) is recommended for balanced token limits\.

- **API Key Login**: Use an OpenAI API key \(requires a foreign credit card, less cost\-effective than subscriptions\)\.

### 1\.3 Initial Configuration

- Select your job role when prompted\.

- Skip the "Import Cloud Code" step for now\.

- You can set up Codex Mobile later \(we'll cover this in Section 8\)\.

## 2\. Basic Project Development Workflow

### 2\.1 Create a Project

- Create a local folder \(e\.g\., "Mark Note"\) to store your project files\.

- In Codex, click "Work on a Project" → "Use an Existing Folder" and select your project folder\.

### 2\.2 First Project: Build a Markdown Note App

- Input your requirement:

    ```Plain Text
    Build a note-taking app with HTML, with two columns: left for note list, right for note content. Include basic CRUD operations and local storage.
    ```

- Codex will generate code and ask for permission to start a local server\. Choose "Yes" to allow it\.

### 2\.3 Preview and Iterate

- Click "Open in" to preview the app in a browser\.

- Use the "Annotation" feature to select areas of the UI and request changes:

    ```Plain Text
    Remove the two sample notes at the top of the left column.
    ```

### 2\.4 Debugging

- If the "Add Note" button doesn't work, Codex will diagnose the issue \(often due to preview environment restrictions\)\.

- Test the app in an independent browser to confirm functionality\.

## 3\. Advanced Configuration and Security

### 3\.1 Permission Modes

- **Default Permissions**: Codex will prompt for approval before executing risky operations\.

- **Auto\-Review**: A security agent automatically approves safe operations and blocks risky ones \(recommended for balance of safety and efficiency\)\.

- **Full Access**: No prompts, but use with caution \(risk of data loss\)\.

### 3\.2 Model Settings

- **Model Selection**: Choose from GPT\-5\.5, GPT\-5\.4, etc\., based on task complexity\.

- **Thinking Depth**: Adjust from Low to Extra High \(higher depth = better code quality but slower speed\)\.

- **Speed Mode**: Enable "Fast" mode for 1\.5x faster generation \(consumes more tokens\)\.

## 4\. Version Control with Git

### 4\.1 Initialize Git Repository

- Press `Command+J` to open the terminal in Codex\.

- Run these commands:

    ```bash
    git init
    git add .
    git commit -m "first commit"
    ```

### 4\.2 Commit Changes

- Use Codex's built\-in Git interface:

    - Click the "Changes" icon → "Unstaged" to view modified files\.

    - Click "Commit", enter a message \(e\.g\., "Change theme to blue"\), and click "Continue"\.

### 4\.3 Rollback with Fork

- Use the "Fork" feature to roll back conversations and code:

    - **Fork into Local**: Creates a new conversation but keeps the current code \(use Git to roll back code manually\)\.

    - **Fork into New Worktree**: Creates a new conversation and a separate project folder \(no code rollback, but isolates changes\)\.

## 5\. Cross\-Project Configuration with `agent.md`

### 5\.1 Create `agent.md`

- In your project folder, create a file named `agent.md`\.

- Add rules like:

    ```markdown
    - After every code change, run `git commit` with a descriptive message.
    - Use React + TypeScript for all new components.
    - Follow the project's color scheme (blue theme).
    ```

### 5\.2 Test the Configuration

- Create a new conversation and ask Codex to add a feature \(e\.g\., "Add a dark/light mode toggle"\)\.

- Check the Git log to confirm Codex automatically committed the changes\.

## 6\. Project Refactoring and Advanced Features

### 6\.1 Refactor to Electron Desktop App

- Use "Plan Mode" to let Codex create a refactoring plan:

    ```Plain Text
    Refactor this web app to an Electron desktop app using React + TypeScript. Ensure all features work correctly.
    ```

- Review the plan and click "Yes, implement this plan"\.

### 6\.2 Add Markdown Support

- Ask Codex to add Markdown editing and preview modes:

    ```Plain Text
    Add Markdown support: a "Edit" mode for writing with syntax highlighting, and a "Preview" mode for rendering.
    ```

## 7\. Extend Capabilities with Plugins and Skills

### 7\.1 Install Plugins

- Click "Plugins" in the sidebar to browse available plugins:

    - **Chrome**: Control the Chrome browser to scrape data or interact with web pages\.

    - **Computer Use**: Control your computer's desktop apps \(e\.g\., calendar, files\)\.

    - **Presentations**: Generate PowerPoint presentations\.

### 7\.2 Use Skills

- **Image Generation**: Use the "Image Gen" skill to generate images based on screenshots:

    ```Plain Text
    Generate a promotional poster for this note app, using the provided screenshots.
    ```

- **Custom Skills**: Create your own skills \(e\.g\., a code review skill\) to automate repetitive tasks\.

### 7\.3 Automations

- Set up automated tasks \(e\.g\., daily code review\):

    - Click "Automations" → "Add Automation"\.

    - Define the task: "Check the project code for issues daily at 9 AM"\.

    - Select "Local" as the execution environment and save\.

## 8\. Mobile Control with Codex Mobile

### 8\.1 Set Up Codex Mobile

- Click "Codex Mobile" in the sidebar\.

- Allow mobile control and scan the QR code with your phone to connect\.

### 8\.2 Control Your Computer from Mobile

- Use the "Computer Use" plugin on your phone to control desktop apps:

    ```Plain Text
    Delete the calendar event "Discuss Mark Note design" on May 28.
    ```

## Conclusion

Codex is a powerful tool that can streamline your development workflow from start to finish\. By following this guide, you can leverage its features to build projects efficiently, automate tasks, and extend its capabilities with plugins and skills\. Experiment with different configurations and find the workflow that best suits your needs\.

