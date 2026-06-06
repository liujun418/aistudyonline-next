# Enhance Your Claude Code Experience with Practical Tools and Customizations

If you've been struggling with Claude Code's limitations like no web search, image recognition issues, or webpage parsing troubles, this guide is for you\. We’ll explore practical tools and customizations to supercharge your Claude Code usage, with step\-by\-step 实操 \(hands\-on\) instructions\.

## Unlock Core Capabilities with MCP

MCP, short for Model Context Protocol, acts as a bridge between AI and external software, enabling features like web search, webpage parsing, and image recognition\. Here are three essential open\-source MCP tools from GitHub:

### 1\. brave\-search\-mcp\-server for Web Search

To enable web search in Claude Code, **brave\-search\-mcp\-server** is a top choice\. It boasts an independent search index and AI\-friendly data output\.

- **Step 1: Get a Brave Search API Key**
Obtain your API key \(for free tier details, consult Gemini or Brave’s official docs\)\.

- **Step 2: Install via Terminal**
Run the following command \(replace `YOUR_API_KEY` with your actual key\):

    ```powershell
    claude mcp add brave-search --api-key YOUR_API_KEY --npm -y @brave-search-mcp-server
    ```

- **Usage**: Simply prompt Claude Code with "帮我搜一下 XXXX" \(Help me search for XXXX\), and it will automatically invoke the brave\-search tool\.

### 2\. server\-fetch for Webpage Parsing

**server\-fetch** filters out clutter from webpages, extracting only core code and text for AI analysis\.

- **Installation Command**:

    ```powershell
    claude mcp add fetch --npm -y @modelcontextprotocol/server-fetch
    ```

- **Usage**: Share a webpage link with Claude Code, e\.g\., "按这个链接里的开源项目说明，帮我搭个环境" \(Help me set up the environment according to the open\-source project instructions in this link\), and it will efficiently parse the page\.

### 3\. Screenshot MCP for Image Recognition

**Screenshot MCP** lets Claude Code capture your screen or specific windows to identify bugs or analyze visual content\.

- **Installation Command**:

    ```powershell
    claude mcp add screenshot --npm -y mcp-screenshot-service
    ```

- **Usage**: When facing a broken program, just say "看下我现在的屏幕，帮我找 bug 出在哪" \(Look at my current screen and help me find where the bug is\), and it will automatically capture and analyze the screen\.

## Customize the Claude HUD Plugin for Coding Plan Monitoring

If you use a domestic Coding Plan and find the default Claude HUD plugin doesn’t support it, you can customize it with Claude Code\.

### Step 1: Analyze the Plugin and Mechanism

- Claude Code’s CLI offers high flexibility, and the plugin is open\-source, making modification feasible\.

- Notice that the mechanism of Claude’s subscription and domestic Coding Plan \(5\-hour and weekly limits\) is similar, so we can replace the data source\.

### Step 2: Implement the Customization

1. **Search for Coding Plan Data Access Methods**
Ask Claude Code: "Use brave\-search to find how to get data for my coding plan"\.

2. **Replace Data in the Plugin Code**
Instruct Claude Code to write a script to replace the Claude subscription data section in the plugin with your Coding Plan data\. Use the command below as a reference \(adjust based on your actual plugin structure\):

    ```javascript
    // Sample script snippet to replace data source
    function fetchCodingPlanData() {
      // Your logic to fetch Coding Plan data
      return {
        contextUsage: "2%",
        hourlyUsage: "4h 21m",
        weeklyUsage: "3d 19h"
      };
    }
    // Replace the original Claude data fetching function
    ```

3. **Set Auto\-Refresh**
Configure the plugin to refresh every 5 minutes to ensure real\-time data\.

## Conclusion

By leveraging MCP tools and customizing plugins, you can transform Claude Code into a more powerful, tailored AI tool\. Remember, the key to mastering AI tools lies in understanding their principles and getting hands\-on\. Explore more MCP tools on GitHub and keep experimenting to unlock even more potential\!

