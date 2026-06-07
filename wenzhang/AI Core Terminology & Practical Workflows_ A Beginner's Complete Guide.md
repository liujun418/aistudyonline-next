# AI Core Terminology \& Practical Workflows: A Beginner's Complete Guide



If you are new to AI, you may feel confused by endless buzzwords like Token, Context Window, Prompt, RAG, MCP, Agent and Workflow\. These terms are not random jargon\. They record the whole evolution path of AI: from a simple chatbot to a powerful system that handles real\-world work\.

This article explains each concept in plain language, matches **practical operations, commands and code examples**, and helps zero\-based AI learners understand the logic, functions and usage scenarios of these terms step by step\. You can apply all the operations directly to mainstream AI tools such as Claude Code and Codex\.

## 1\. Token \& Context Window: How Much Content Can AI Read at One Time?

### Basic Definition

AI cannot read text like humans\. It splits all input content into small basic units called **Tokens**\. A Chinese phrase or an English word may be divided into multiple tokens\.

**Context Window** refers to the maximum number of tokens an AI model can process and remember in a single session\. It determines three core points:

1. The total volume of content AI can view at once

2. The cost of each AI call \(most platforms charge by tokens\)

3. Why AI forgets early conversation content

When your dialogue, files, prompts and tool outputs exceed the context window limit, the earliest content will be automatically truncated\.

### Practical Operation \& Detection

We can check the token usage and context window status via Claude Code CLI\.

```bash
# Check current session token usage and remaining context window
/cli token stats
```

#### Usage Tips for Beginners

- Do not pile all files and history dialogues into one session\. Split long content into multiple parts\.

- For models with an 8k token limit, keep the total content below 7k to avoid truncation\.

- Long conversations can use the built\-in compression function to save context space\.

## 2\. Prompt \& Prompt Engineering: Let AI Understand Your Tasks Clearly

### Basic Definition

A **Prompt** is the instruction you send to AI\. **Prompt Engineering** is the skill of writing standardized, clear instructions, just like writing a detailed job description for AI\.

Vague prompts lead to empty and useless outputs\. Standard prompts define AI’s role, tasks, background, output format and acceptance rules\.

### Practical Comparison \& Standard Template

❌ Poor vague prompt

```plaintext
Write a work plan for me.
```

✅ Standard prompt for beginners \(copy and use directly\)

```plaintext
You are a professional project manager. Write a 1-week AI learning work plan for absolute beginners.
Requirements:
1. Divide tasks by day;
2. Match simple practice cases for each task;
3. Output in table format;
4. Avoid complex professional terms.
```

#### Common Command in AI Tools

```plaintext
# Load fixed prompt rules for the current project (take Claude Code as an example)
/prompt load ./basic-rule.md
```

## 3\. RAG \(Retrieval Augmented Generation\): Let AI Query External Materials

### Basic Definition

A major flaw of pure prompt: AI can only rely on its training data\. It will make up answers for unfamiliar internal documents, new materials or private files \(AI hallucination\)\.

**RAG** solves this problem\. Its core logic: **Retrieve relevant information from the knowledge base first, then generate answers based on the retrieved content**\.

RAG also involves related concepts:

- **Embedding**: Convert text into digital vectors for semantic matching

- **Vector Database**: Store massive vector data and quickly search similar content

- **Agentic RAG**: Advanced RAG, which actively splits questions, supplements materials and verifies conflicting information

### Practical RAG Deployment Steps \(for Local Files\)

1. Prepare your document \(such as `employee-manual.md`\) and put it in the project folder

2. Run commands to build a local knowledge base and enable RAG

```bash
# Import local documents into RAG knowledge base (Claude Code)
/rag add ./employee-manual.md
# Enable automatic retrieval mode
/rag enable auto
```

3. Ask questions to test the effect

```plaintext
According to the employee manual, how many working days in advance should I apply for annual leave?
```

AI will first retrieve the document content, then give accurate answers instead of guessing\.

## 4\. Tool Calling: Let AI Move from Answering Questions to Performing Actions

### Basic Definition

RAG gives AI the ability to "check materials", while **Tool Calling \(Function Calling\)** gives AI the ability to "operate tools"\. AI is no longer limited to text generation, and can call third\-party tools to complete actual operations\.

Common applicable tools: calendar, code runner, order system, browser tools, database, etc\.

### Simple Python Demo of Tool Calling

This case realizes that AI calls the time query tool:

```python
# Define a simple time query tool
import datetime

def get_current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# AI triggers tool calling according to instructions
user_input = "Tell me the current system time"
if "time" in user_input:
    result = get_current_time()
    print(f"Current time: {result}")
```

### Tool Calling Command in AI Agent

```plaintext
# Call the built-in code running tool to execute the above script
/tool run python ./time-tool.py
```

## 5\. MCP \(Model Context Protocol\): Unified Standard for AI to Connect External Tools

### Basic Definition

When there are more and more tools, each tool requires an independent interface, which leads to high development and maintenance costs\.

**MCP** is a unified connection protocol for AI and external tools, equivalent to the **USB\-C interface in the AI world**\. It unifies the access rules of all tools, including parameter transmission, permission management, result return and security control\.

### Practical MCP Installation \& Connection

Take connecting the web search MCP service as an example:

```bash
# Install Brave Search MCP server
npm install -g @brave-search-mcp-server
# Add MCP tool to Claude Code
claude mcp add brave-search --api-key YOUR_API_KEY
```

After configuration, you only need to send natural language instructions, and AI will automatically call the MCP tool to complete the search\.

## 6\. Context Engineering \& Context Engine: Manage Information Seen by AI

### Basic Definition

**Prompt Engineering** focuses on a single instruction, while **Context Engineering** focuses on the overall information flow\. It reasonably matches dialogue history, user data, document content and tool results for AI\.

Core principle: Do not send excessive information to interfere with AI, nor send too little information to cause misjudgment — provide **exactly the required content**\.

**Context Engine** is the automated system of Context Engineering\. It automatically filters sensitive content, compresses long text and sorts key information\.

### Practical Configuration File Example

Create `context-config.json` in the project folder to limit context rules:

```json
{
  "keep_recent_dialogue": 5,
  "compress_long_text": true,
  "filter_sensitive_data": true,
  "max_token_per_request": 6000
}
```

Load the configuration file in the AI tool:

```plaintext
/context load ./context-config.json
```

## 7\. Skill: Reuse Mature Workflows and Avoid Repeated Teaching

### Basic Definition

A **Skill** is a reusable solidified workflow\. A prompt is a one\-time instruction, while a Skill is a long\-term standard operating procedure \(SOP\)\.

For repetitive work such as writing weekly reports, sorting code and processing forms, you can solidify the whole process into a Skill\. Next time you just call the Skill directly\.

### Create \& Call Custom Skill

1. Create a new Skill for "AI Weekly Report Generation"

```plaintext
Create a new skill named weekly-report. The requirements: sort this week's work content, extract core achievements, list pending problems and next week's plan, and use formal workplace tone.
```

2. Call the existing Skill with one click

```plaintext
Use weekly-report to generate my work weekly report.
```

## 8\. Computer Use: Let AI Operate Computers Like Humans

### Basic Definition

Tool Calling is to call API interfaces, while **Computer Use** is to let AI directly operate the computer: identify the screen, control the mouse and keyboard, complete page clicking, form filling, file uploading and other manual operations\.

It is suitable for old systems and web pages without open APIs, such as internal approval systems, legacy background management pages, etc\.

### Practical Operation \(Combined with Playwright CLI\)

```bash
# Start headed browser for manual simulation operations
playwright-cli open https://your-work-system.com --headed --persistent
# Automatically click the login button
playwright-cli click "text=Login"
# Automatically fill account and password
playwright-cli fill "input[name=username]" "test-user"
playwright-cli fill "input[name=password]" "test-123456"
```

## 9\. Agent: AI Automatically Splits Tasks and Executes Cycles

### Basic Definition

An **Agent** is an autonomous AI execution body\. Different from one\-round dialogue and single tool calling, Agent follows a loop logic: **Make a plan → Perform actions → Observe results → Adjust steps**\.

Given a general goal, Agent will split complex tasks into multiple subtasks, select tools independently and solve problems round by round\. It is widely used in code development, project debugging and data analysis\.

### Agent Core Startup Command \(Claude Code\)

```bash
# Set the overall goal and start automatic cycle execution
/goal Debug the project startup error, check logs and configuration files, fix bugs and ensure the project runs normally. Stop after 15 iterations.
# Enable automatic mode to reduce manual confirmation
/auto on
```

## 10\. Harness Engineering: Make Agent Run Safely and Controllably

### Basic Definition

Powerful Agents have risks such as misdeleting files, modifying production code and leaking data\. **Harness Engineering** is the safety control system for Agents, equivalent to safety belts and brakes\.

It includes permission control, sandbox operation, log tracking, manual approval, rollback mechanism and cost control\.

### Simple Sandbox Restriction Configuration

Create `harness-rule.md` to limit Agent permissions:

```markdown
# Agent Safety Rules
1. Only allow operating files in the ./test folder;
2. Prohibit deleting any files;
3. All code modifications must be reviewed manually before submission;
4. Automatically stop when token consumption exceeds 10000 per hour.
```

Load the rule file:

```plaintext
/harness load ./harness-rule.md
```

## 11\. Workflow \& Workspace Agent: Access Formal Business Processes

### 11\.1 Workflow

**Workflow** connects AI, databases, message notifications, manual approval and timing tasks into a complete business process\. It is responsible for arranging the execution sequence of each step, suitable for long\-link business such as customer consultation, order processing and report statistics\.

### 11\.2 Workspace Agent

- Ordinary Agent: Equivalent to a temporary worker, completing a single task

- **Workspace Agent**: Equivalent to a long\-term on\-site assistant\. It always exists in the team workspace, mastering team documents, personnel division, historical work and permission rules\. It can automatically associate long\-term context to complete work\.

### Simple Workflow Command Example

```plaintext
# Start the customer consultation process workflow
/workflow start customer-service-flow
# View the running status of the workflow
/workflow status
```

## Full Evolution Logic \& Beginner Learning Suggestions

### AI Evolution Main Line

Chatbot \(Prompt\) → Query External Knowledge \(RAG\) → Perform Actions \(Tool Calling \+ MCP\) → Reuse Workflow \(Skill\) → Simulate Manual Operation \(Computer Use\) → Autonomous Task Execution \(Agent\) → Safe Launch \(Harness\) → Access Business Scenarios \(Workflow \+ Workspace Agent\)

### Learning Steps for Zero\-Based Learners

1. Master **Token \& Context Window** first to control usage cost and content volume

2. Practice **Prompt Writing** to improve basic AI output quality

3. Learn **RAG** to solve the problem of private document query

4. Try **Tool Calling \& MCP** to realize simple automated operations

5. Solidify repeated operations into **Skills** to improve efficiency

6. Gradually learn **Agent, Harness and Workflow** to build complex AI systems

All the above commands and code snippets can be directly applied to Claude Code, Codex and other mainstream AI tools\. Start with simple cases and practice step by step, and you can easily master the mainstream AI technologies\.

