# Claude Code: Final Configuration Guide for Overseas Users \(Beginner\-Friendly\)

Claude Code is a powerful AI tool, and this final guide will walk you through configuring API 中转站 \(API proxies\) like Yunwu, ClaudeCN, and Silicone Flow using CC Switch, enabling you to fully leverage Claude Code for your overseas projects\.

## Core Configuration Elements

To set up any API proxy, you need three key elements:

- **API Link**: The official URL of the proxy service\.

- **API Key**: The authentication key for the service\.

- **Model Name**: The specific AI model you want to use \(e\.g\., `claude\-sonnet\-4`, `gemini\-3\-pro\-preview`\)\.

## Step 1: Configure Yunwu API Proxy

Yunwu is an overseas model proxy\. Here’s how to set it up in CC Switch:

1. Open CC Switch and click the \&\#34;\+\&\#34; icon in the top\-right corner\.

2. Select \&\#34;Custom Configuration\&\#34; since Yunwu isn’t in the built\-in list\.

3. Fill in the details:

    - **Provider Name**: Yunwu \(or any name you prefer for easy recall\)\.

    - **API Link**: Paste Yunwu’s official URL\.

    - **API Key**: Retrieve your API key from Yunwu’s dashboard and paste it\.

    - **Model Name**: Choose a model from Yunwu’s model library \(e\.g\., `gemini\-3\-pro\-preview`\), copy its name, and paste it in the model field\.

4. Click \&\#34;Add\&\#34; to save\. The proxy is enabled by default\. If not, click \&\#34;Enable\&\#34;\.

To verify, open your terminal and run:

```bash
claude
/status
```

This command will show you the currently active proxy and model\.

## Step 2: Configure ClaudeCN API Proxy

ClaudeCN is another useful proxy\. The configuration steps are similar to Yunwu:

1. In CC Switch, add a new custom configuration\.

    - **Provider Name**: ClaudeCN \(or your chosen name\)\.

    - **API Link**: Paste ClaudeCN’s official URL\.

    - **API Key**: Get the key from ClaudeCN’s key management section and paste it\.

    - **Model Name**: Select a model from ClaudeCN’s list \(e\.g\., `claude\-opus\-4`\), copy its name, and paste it\.

2. Click \&\#34;Add\&\#34; and enable it if needed\.

To switch models later, click \&\#34;Edit\&\#34; on the ClaudeCN configuration in CC Switch and update the model name\.

## Step 3: Configure Silicone Flow API Proxy

Silicone Flow is a built\-in option in CC Switch, making it simpler:

1. In CC Switch, click \&\#34;\+\&\#34; and select Silicone Flow from the built\-in providers\.

2. Only fill in the **API Key** \(retrieve it from Silicone Flow’s dashboard\)\.

3. The API link and provider name are pre\-filled\.

4. Choose a model from Silicone Flow’s offerings and click \&\#34;Add\&\#34;\.

## Verify and Use

After setting up any proxy, use the terminal command to check the status:

```bash
claude
/status
```

You’ll see which proxy and model are active\. Now, you can start interacting with Claude Code, asking it to help with coding, content creation, or other tasks for your overseas projects\.

With these configurations, you’ve unlocked the full potential of Claude Code\. It’s now ready to assist you in various AI\-driven tasks, ensuring efficiency and accuracy for your overseas business needs\.

