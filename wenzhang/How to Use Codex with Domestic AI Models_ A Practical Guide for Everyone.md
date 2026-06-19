# How to Use Codex with Domestic AI Models: A Practical Guide for Everyone

In the realm of AI\-assisted coding, Codex has emerged as a powerful tool, but its reliance on the ChatGPT model can be a barrier for many due to cost and access issues\. This guide will walk you through how to use Codex with domestic AI models like DeepSeek V4, making it accessible without a ChatGPT account, phone number verification, or special network configurations\.

## Understanding Codex and Its Ecosystem

Codex is an **Agent product** designed to assist with coding tasks\. It’s often used alongside tools like **CC Switch**, which allows you to swap out its underlying model\. By default, Codex uses the ChatGPT model, but we can replace this "brain" with domestic alternatives like DeepSeek V4 or Mimo v2\.5 for better accessibility and cost\-effectiveness\.

### Why Choose Domestic Models?

- **DeepSeek V4**: Highly recommended online, with excellent overall performance\. However, it doesn’t support multimodal inputs \(e\.g\., image uploads\)\.

- **Mimo v2\.5**: Supports multimodal inputs and offers a great user experience\.

## Step 1: Download and Install Codex

1. Visit the [Codex official website](https://openai.com/terms/codex) and download the appropriate version for your operating system \(Windows or macOS\)\. The tool is free to download\.

## Step 2: Install CC Switch

CC Switch is a tool that lets you switch Codex’s underlying model\.

1. Go to the [CC Switch GitHub page](https://github.com/12301230/cc-switch/releases)\.

2. Scroll down to find the installation package:

    - For macOS, download the file ending with `.dmg`\.

    - For Windows, download the file ending with `.msi`\.

3. If unsure which version to install, ask DeepSeek:

    ```text
    Which version of CC Switch should I install for my [your OS] system?
    ```

## Step 3: Obtain an API Key from DeepSeek

An **API Key** is like an access credential that allows Codex to communicate with the DeepSeek model\.

1. Visit the [DeepSeek Open Platform](https://platform.deepseek.com/)\.

2. Click on "API Keys" in the left menu\.

3. Create a new API Key, give it a name for easy recall, and copy the generated key\. Keep it secure, as it’s your personal access credential\.

## Step 4: Configure CC Switch

1. Open CC Switch and click on the third icon \(OpenAI icon\) at the top\.

2. Click the "\+" button on the right to add a model\. Select "DeepSeek" \(or your chosen domestic model\)\.

3. Paste the DeepSeek API Key into the designated field\. Ensure the toggle for model integration is enabled, then click "Add"\.

## Step 5: Test the Setup

1. Fully exit Codex and restart it\.

2. In Codex, click on "Settings" in the bottom left corner\. You should see that you’re logged in via the API Key, and the model should show "DeepSeek"\.

3. Send a test message, e\.g\.,:

    ```text
    Hello, what can you help me with?
    ```

    A normal response indicates success\.

## Conclusion

By following these steps, you can now use Codex with the DeepSeek model, leveraging its powerful coding capabilities without the need for a ChatGPT account or complex configurations\. This setup is practical, cost\-effective, and accessible to anyone\. If you encounter any issues during installation, feel free to ask for help\. Stay tuned for more tips on using Codex and CC Switch\!

