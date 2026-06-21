# Codex Complete Guide for Domestic Users: Full Installation \+ Official Plugins Setup \(Step\-by\-Step\)



For developers in China, accessing and using Codex effectively—with all official plugins—has long been a challenge due to network restrictions and configuration hurdles\. This beginner\-friendly, "spoon\-feeding" guide breaks down the entire process from installation to plugin activation, ensuring even non\-technical users can leverage Codex’s full capabilities without complex setups\.

## Core Advantages of This Domestic\-Friendly Setup

- **No Special Network Required**: Works with regular domestic internet \(no VPN needed\)\.

- **Full Official Plugins Access**: Activate all 8\+ official Codex plugins \(e\.g\., Browser, Terminal, File Manager\)\.

- **Stable Connection**: Uses domestic API gateways to avoid latency or disconnections\.

- **Zero Coding Experience Needed**: Follow copy\-paste commands and visual steps\.

## Prerequisites \(3 Things You Need\)

1. A Windows 10/11 or macOS 12\+ computer \(64\-bit, 8GB\+ RAM recommended\)\.

2. A free [DeepSeek/Ernie Bot API key](https://platform.deepseek.com/) \(domestic AI model alternative to GPT\)\.

3. 10 minutes of time \(the entire process is streamlined to under 10 minutes\)\.

## Step 1: Download Codex Client \(Domestic Mirror\)

The official Codex download may be inaccessible in China—use this trusted domestic mirror:

1. Visit the [Codex China Mirror](https://codex-mirror-cn.oss-cn-beijing.aliyuncs.com/) \(Alibaba Cloud\-hosted, safe to use\)\.

2. Select the version for your OS:

    - Windows: Download `Codex-Setup-1.8.2.exe` \(58MB\)\.

    - macOS: Download `Codex-1.8.2.dmg` \(62MB\)\.

3. Install the client by double\-clicking the file—no custom settings needed \(just click "Next" → "Install" → "Finish"\)\.

## Step 2: Configure Domestic AI Model Connection \(No ChatGPT Required\)

Codex defaults to ChatGPT, but we’ll connect it to a domestic model \(DeepSeek\) for stable access:

1. Open Codex after installation\. Click "Settings" \(gear icon\) in the bottom\-left corner\.

2. Select "Model Configuration" → "Custom API"\.

3. Fill in the fields with the following details \(copy\-paste directly\):

    ```plaintext
    API Provider: DeepSeek
    API Base URL: https://api.deepseek.com/v1
    API Key: [Paste your DeepSeek API key here]
    Model: deepseek-chat
    ```

4. Click "Test Connection"—a green "Connected Successfully" message means it’s working\.

5. Click "Save" to apply the settings\.

### How to Get a DeepSeek API Key \(30\-Second Tutorial\)

1. Go to [DeepSeek Open Platform](https://platform.deepseek.com/) and sign up with your phone number \(domestic number supported\)\.

2. After logging in, click "API Keys" → "Create New Key"\.

3. Name the key \(e\.g\., "Codex Usage"\) and click "Generate"—copy the key immediately \(it won’t be shown again\)\.

## Step 3: Install All Official Codex Plugins \(One\-Click Activation\)

Codex’s power lies in its plugins—here’s how to install and enable all official ones:

1. In Codex, click "Plugins" \(puzzle icon\) in the left sidebar\.

2. Click "Install Official Plugins" → select "All Plugins" \(or check individual ones you need\):

    - **Browser**: Web search and page scraping\.

    - **Terminal**: Run shell commands \(Windows/macOS/Linux\)\.

    - **File Manager**: Read/write local files\.

    - **Code Interpreter**: Execute Python/R code\.

    - **PDF Reader**: Analyze PDF documents\.

    - **Image Generator**: Create images from text\.

    - **Excel Processor**: Edit and analyze Excel files\.

    - **Git Integration**: Manage Git repositories\.

3. Click "Install"—wait 20 seconds for all plugins to download \(no additional setup needed\)\.

### Verify Plugin Activation

Run this test prompt in Codex to confirm plugins work:

```plaintext
Use the Browser plugin to search for "2024 top Python frameworks", then use the File Manager plugin to save the results to a text file named "python-frameworks-2024.txt" on my desktop.
```

Codex will automatically:

1. Launch the built\-in browser to run the search\.

2. Extract key information from the results\.

3. Create and save the file to your desktop\.

## Step 4: Practical Use Cases \(With Copy\-Paste Prompts\)

Here are 3 common scenarios to start using Codex with plugins effectively:

### 1\. Automate File Organization \(File Manager Plugin\)

Prompt:

```plaintext
Use the File Manager plugin to organize my "Downloads" folder:
1. Create subfolders: "Documents", "Images", "Videos", "Others".
2. Move all .pdf/.docx/.txt files to "Documents".
3. Move all .jpg/.png/.gif files to "Images".
4. Move all .mp4/.mov files to "Videos".
5. Move remaining files to "Others".
6. Generate a summary of how many files were moved to each folder.
```

### 2\. Run Code Snippets \(Code Interpreter Plugin\)

Prompt:

```plaintext
Use the Code Interpreter plugin to:
1. Calculate the sum of the first 100 prime numbers.
2. Generate a bar chart showing the distribution of these primes.
3. Save the chart as "prime-numbers-chart.png" on my desktop.
4. Output the final sum and the file path.
```

Codex will execute the Python code automatically:

```python
import numpy as np
import matplotlib.pyplot as plt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

primes = []
num = 2
while len(primes) < 100:
    if is_prime(num):
        primes.append(num)
    num += 1

# Generate chart
plt.bar(range(1, 101), primes, color='skyblue')
plt.title('Distribution of First 100 Prime Numbers')
plt.xlabel('Prime Number Rank')
plt.ylabel('Prime Number Value')
plt.savefig('/Users/[Your Username]/Desktop/prime-numbers-chart.png')
plt.close()

print(f"Sum of first 100 primes: {sum(primes)}")
print("Chart saved to desktop as 'prime-numbers-chart.png'")
```

### 3\. Analyze PDF Data \(PDF Reader Plugin\)

Prompt:

```plaintext
Use the PDF Reader plugin to:
1. Open the file "sales-report-2024.pdf" from my Documents folder.
2. Extract all numerical sales data (revenue, units sold) from the first 5 pages.
3. Calculate the total revenue and average units sold per month.
4. Save the analysis as "sales-analysis-2024.txt" in the same folder.
```

## Step 5: Troubleshooting Common Issues \(Domestic Users\)

### Issue 1: Plugin Installation Fails

Fix:

```plaintext
1. Close Codex completely.
2. Open Command Prompt (Windows) or Terminal (macOS) and run:
# Windows
cd C:\Program Files\Codex
codex --repair-plugins

# macOS
cd /Applications/Codex.app/Contents/MacOS
./Codex --repair-plugins
3. Restart Codex and retry installing plugins.
```

### Issue 2: API Connection Error

Fix:

- Ensure your API key is not expired \(DeepSeek keys are valid for 90 days\)\.

- Check if your internet connection is stable \(switch to Wi\-Fi if on mobile data\)\.

- Re\-enter the API Base URL: `https://api.deepseek.com/v1` \(no typos\)\.

### Issue 3: Terminal Plugin Not Working \(Windows\)

Fix:

1. Open Codex → "Plugins" → "Terminal" → "Settings"\.

2. Select "Use PowerShell" \(default is Command Prompt\)\.

3. Click "Save" and retry running commands\.

## Conclusion

With this guide, domestic users can now access Codex’s full functionality—including all official plugins—without network barriers\. The key is using a domestic AI model \(like DeepSeek\) as the backend and leveraging the trusted Chinese mirror for installation\. Whether you’re automating file tasks, running code, or analyzing documents, Codex becomes a powerful assistant with minimal setup\.

Start with the practical use cases above, and explore more plugin combinations to fit your workflow\. If you encounter any other issues, leave a comment or refer to Codex’s domestic support forum for real\-time help\.