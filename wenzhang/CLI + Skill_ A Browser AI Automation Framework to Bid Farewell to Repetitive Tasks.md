# CLI \+ Skill: A Browser AI Automation Framework to Bid Farewell to Repetitive Tasks



In the realm of automation, the combination of CLI \(Command\-Line Interface\) tools and custom skills is revolutionizing how we handle browser\-based tasks\. This framework empowers AI to automate browser operations, taking over mechanical and repetitive work while being incredibly token\-efficient—even allowing for **0\-token automation workflows** that don’t require AI involvement at all\. Let’s dive into how this works, with practical steps and code examples\.

## 1\. Core Components and Advantages

### Key Tools

- **Agent Frameworks**: Claude Code or Codex \(for AI\-driven task orchestration\)\.

- **Browser Automation Tool**: Playwright CLI \(a new open\-source tool from Microsoft in early 2026, designed for efficient browser control\)\.

- **Skills**: Custom scripts or workflows that encapsulate repeatable processes, reducing token usage and streamlining AI interactions\.

### Why This Framework Stands Out

- **Token Efficiency**: Playwright CLI reduces token consumption by up to 4x compared to traditional Playwright MCP methods\. It fetches web content on\-demand \(e\.g\., webpage snapshots or screenshots are stored locally, not sent to AI unless needed\)\.

- **0\-Token Workflows**: Many tasks can be automated with fixed scripts, eliminating AI token costs entirely\.

- **No Browser Expertise Needed**: You can automate tasks using natural language—no deep knowledge of browser internals is required\.

## 2\. Setup and Basic Usage

### Step 1: Install Dependencies

First, ensure you have **Node\.js** installed\. Visit the [Node\.js official website](https://nodejs.org/) to download and install the version matching your operating system\.

Next, install Playwright CLI via npm \(Node Package Manager\):

```bash
npm install -g @playwright/cli
```

Also, make sure **Google Chrome** \(or Microsoft Edge\) is installed on your machine for browser automation\.

### Step 2: Playwright CLI Basics

Playwright CLI supports two browser modes:

- **Headed Mode** \(`--headed`\): Visible browser window \(great for debugging\)\.

- **Headless Mode** \(default\): Invisible, background browser \(saves memory for batch tasks\)\.

To open a webpage in headed mode \(e\.g\., Google\):

```bash
playwright-cli open google.com --headed
```

When you run this command, Playwright CLI outputs a concise webpage summary \(not the entire DOM\) and a snapshot file path\. AI can fetch the full DOM from this snapshot only if needed, minimizing token usage\.

For taking a screenshot:

```bash
playwright-cli screenshot
```

This saves a PNG image locally, and AI decides whether to process it—no need to send image data to AI directly\.

To retain login states \(e\.g\., cookies\) across sessions, use the `--persistent` flag:

```bash
playwright-cli open google.com --headed --persistent
```

## 3\. Integrating with AI Agents \(Claude Code \& Codex\)

AI agents like Claude Code or Codex need “skills” to understand how to use Playwright CLI\. Here’s how to set this up:

### Step 1: Create a Project and Install Skills

1. Create a project folder and open a terminal in that directory\.

2. Install the Playwright CLI skills:

    ```bash
    playwright-cli install --skill
    ```

### Step 2: Connect to Claude Code

Launch Claude Code and check available skills:

```plaintext
What skills do you have?
```

Claude Code should list `playwright-cli` as a skill, confirming integration\.

### Step 3: Connect to Codex

Rename the skills folder from `.claude` to `.codex` in your project directory\. Then, in Codex, run:

```plaintext
/skills
```

Codex will list `playwright-cli`, showing it’s ready for use\.

## 4\. Practical Examples

### Example 1: Scrape E\-Commerce Reviews \(0\-Token Workflow\)

Let’s extract the first 100 reviews from a Tmall product page and save them as a CSV file\.

#### Step 1: Let AI Explore and Refine \(First Run\)

Ask Codex to handle the task with natural language:

```plaintext
Use playwright-cli --headed --persistent to open this Tmall product page, scrape the first 100 reviews, and save them to a CSV file.
```

Codex will experiment with Playwright CLI commands, which might involve some trial and error\. Once successful, it will output a CSV file with the reviews\.

#### Step 2: Save the Workflow as a Skill

To optimize future runs, turn this process into a reusable skill\. Prompt Codex:

```plaintext
Create a new skill called "save-tmall-reviews" that encapsulates opening the product page, scraping reviews, and saving to CSV. Include all steps and fixes for any issues encountered.
```

Codex will generate a skill file that you can store in your project\.

#### Step 3: Run with the Skill \(Reduced Token Usage\)

Now, re\-run the task using the skill:

```plaintext
Use the "save-tmall-reviews" skill to scrape reviews for this Tmall product.
```

With the skill’s guidance, Codex completes the task with \~5% of the original token usage\.

#### Step 4: Convert to a 0\-Token Script

For fully automated, token\-free execution, ask Codex to write a fixed script\. Prompt:

```plaintext
Write a PowerShell script that combines all Playwright CLI commands to scrape Tmall reviews and save them to CSV. Include delays to ensure reliability.
```

Codex will generate a script like this \(simplified example\):

```powershell
# Open the product page
playwright-cli open "https://detail.tmall.com/..." --headed --persistent

# Wait for the page to load
playwright-cli wait-for-selector "text=查看全部评价" --timeout 5000

# Click to view all reviews
playwright-cli click "text=查看全部评价"

# Extract reviews and save as CSV
playwright-cli eval "() => { /* JavaScript to extract reviews */ }" | ConvertTo-Csv | Out-File "reviews.csv"
```

Run this script directly in PowerShell—no AI involvement, no tokens used\.

### Example 2: Automate Article Publishing on Platform X

Publishing Markdown articles on Platform X is tedious \(formatting issues, image uploads\)\. Let’s automate it\.

#### Step 1: Prepare the Article \(Markdown to HTML\)

First, convert the Markdown article to HTML and download images locally\. Use this Python script \(generated by Codex\):

```python
import requests
import re
import os
from bs4 import BeautifulSoup
import pandoc

# Download images from the Markdown article and reformat to local paths
def download_images_and_convert(md_path, img_dir="images", html_output="article.html"):
    # Create image directory
    os.makedirs(img_dir, exist_ok=True)
    
    # Read Markdown content
    with open(md_path, "r", encoding="utf-8") as f:
        md_content = f.read()
    
    # Extract and download images
    img_links = re.findall(r"!\[.*?\]\((.*?)\)", md_content)
    for i, img_link in enumerate(img_links):
        img_name = f"00{i+1}.png"
        img_path = os.path.join(img_dir, img_name)
        response = requests.get(img_link)
        with open(img_path, "wb") as f:
            f.write(response.content)
        # Replace remote image link with local path
        md_content = md_content.replace(img_link, img_path)
    
    # Convert Markdown to HTML with pandoc
    html_content = pandoc.convert_text(md_content, to="html", format="md")
    
    # Ensure each image is in its own paragraph
    html_content = re.sub(r"<img(.*?)>", r"<p><img\1></p>", html_content)
    
    # Save HTML
    with open(html_output, "w", encoding="utf-8") as f:
        f.write(html_content)

if __name__ == "__main__":
    download_images_and_convert("article.md")
```

#### Step 2: Automate Publishing with Playwright CLI

Prompt Codex to automate the publishing workflow:

```plaintext
Use playwright-cli --headed --persistent to open Platform X, create a new article, paste the HTML content, and replace image placeholders with the local images in the "images" folder. Ensure images are uploaded in order.
```

Codex will generate Playwright CLI commands to:

1. Open Platform X and create a draft\.

2. Paste the HTML content\.

3. Locate image placeholders and replace them with local images via copy\-paste\.

#### Step 3: Save as a Reusable Skill

Finally, save this workflow as a skill for future use:

```plaintext
Create a skill called "publish-to-platform-x" that includes downloading images, converting to HTML, and automating the publishing process on Platform X.
```

### Example 3: Automated Testing for Web Apps

For a self\-developed web app \(e\.g\., a resume optimization tool\), use Playwright CLI to run automated tests\.

#### Step 1: Generate Test Cases with AI

Prompt Codex to analyze your app’s code and create test cases:

```plaintext
Read the code of my resume optimization web app, then write a Chinese test document outlining the main flow (register → login → upload resume → get AI suggestions). Then, use playwright-cli to execute these tests.
```

Codex will produce a test document like this \(simplified\):

```markdown
# Test Cases for Resume Optimization App
## 1. Registration
- Step 1: Open the app’s registration page.
- Step 2: Enter a test email and password.
- Step 3: Submit and verify successful registration.

## 2. Login
- Step 1: Navigate to the login page.
- Step 2: Enter the registered email and password.
- Step 3: Verify successful login and redirection to the dashboard.

## 3. Resume Upload and AI Suggestions
- Step 1: Click "Upload Resume" and select a test resume file.
- Step 2: Wait for AI analysis and suggestions to load.
- Step 3: Verify the suggestions appear correctly.
```

#### Step 2: Execute Tests with Playwright CLI

Codex will generate Playwright CLI commands to run these tests:

```bash
# Open the registration page
playwright-cli open "http://localhost:5000/register" --headed --persistent

# Fill registration form
playwright-cli fill "input[name='email']" "test@example.com"
playwright-cli fill "input[name='password']" "testpass123"
playwright-cli click "text=Register"

# Login after registration
playwright-cli open "http://localhost:5000/login" --headed --persistent
playwright-cli fill "input[name='email']" "test@example.com"
playwright-cli fill "input[name='password']" "testpass123"
playwright-cli click "text=Login"

# Upload resume and test AI suggestions
playwright-cli set-input-files "input[type='file']" "test_resume.pdf"
playwright-cli click "text=Upload & Analyze"
playwright-cli wait-for-selector "div.ai-suggestions" --timeout 10000
```

## 5\. Workflow Summary

To implement this framework effectively, follow these steps:

1. **Prepare**: Install Node\.js, Playwright CLI, and Chrome\.

2. **Integrate with AI Agents**: Install skills for Claude Code or Codex\.

3. **Task Execution**: Let AI explore and complete a complex task using Playwright CLI\.

4. **Refine with Skills**: Ask AI to summarize the workflow into a reusable skill\.

5. **Optimize**: Re\-run the task with the skill to reduce token usage by up to 10x\.

6. **0\-Token Automation**: For fixed workflows, ask AI to write a standalone script and run it directly\.

This CLI \+ Skill framework is a game\-changer for browser automation, offering efficiency, cost savings, and simplicity\. Whether you’re scraping data, publishing content, or testing apps, it empowers you to automate repetitive tasks with minimal effort\.

