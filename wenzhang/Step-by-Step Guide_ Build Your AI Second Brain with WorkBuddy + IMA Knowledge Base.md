# Step\-by\-Step Guide: Build Your AI Second Brain with WorkBuddy \+ IMA Knowledge Base

## Introduction

Many users face a common pain point when using WorkBuddy: it excels at answering general questions but struggles with personalized or company\-specific content\. This tutorial will walk you through integrating WorkBuddy with IMA Knowledge Base to create a "second brain" for your AI assistant, enabling it to access your private documents and provide accurate, context\-aware responses\.

## Three Core Steps to Master IMA Knowledge Base

The process is divided into three simple phases: **Connect, Use, and Update**, which you can implement immediately after reading this guide\.

### Step 1: Connect to IMA Knowledge Base \(Build Your Knowledge Library\)

Think of this step as building a dedicated library for your AI\. You'll store all your notes, documents, and reference materials here, so the AI can retrieve information directly from these files instead of generating generic responses\.

#### 3 Key Operations to Complete the Connection

1. **Authorize the Connection**

    - Click the "\+" button next to the input box in WorkBuddy

    - Select "Connector" and choose "IMA Knowledge Base"

    - Log in with your account to grant WorkBuddy access permissions

2. **Create and Import Resources**

    - Open the IMA Knowledge Base management page

    - Create a new knowledge base \(e\.g\., "WorkBuddy Mastery Guide"\)

    - Upload your basic files \(supports PDF, Word, PPT, Excel, TXT, and other common formats\)

3. **Enable Connector Synchronization**

    - Return to the main WorkBuddy interface

    - Find the IMA Knowledge Base connector in the added connectors list

    - Turn on the synchronization switch to enable real\-time knowledge sharing

### Step 2: Use the Knowledge Base \(One Prefix for Precise Answers\)

Using the integrated system is extremely simple\. Just add the prefix **"Based on IMA Knowledge Base"** to your questions, and WorkBuddy will only retrieve answers from your uploaded materials, significantly reducing hallucinations\.

#### Two Common Usage Scenarios

1. **Question \& Answer Interaction**

    ```Plain Text
    Based on IMA Knowledge Base, answer: [Your specific question]
    ```

    This format ensures the AI provides direct, verifiable answers based on your documents\.

2. **Creative Generation**

    ```Plain Text
    Based on IMA Knowledge Base, help me write a report/article/summary
    ```

    The AI will use factual data from your knowledge base to generate content that fits your business scenario\.

### Step 3: Update the Knowledge Base \(Manual Upload for Continuous Improvement\)

Building a knowledge base isn't a one\-time task—you need to add new content regularly to keep it useful\.

#### 3 Steps to Update Your Knowledge Base

1. **Open the Knowledge Base**

    - Log in to the IMA Knowledge Base management interface

    - Navigate to the target directory where you want to add content

2. **Trigger the Upload**

    - Click the "Upload" button in the toolbar

    - Select local files from your computer \(supports batch uploads\)

3. **Automatic Parsing and Storage**

    - Confirm the selected files

    - The system will automatically identify file formats, extract key information, and complete parsing

    - The new content will be synchronized to the knowledge base in real time

## Advanced Play: Bidirectional Closed\-Loop Workflow

To make your knowledge base even more powerful, you can set up a bidirectional closed\-loop system that automatically saves AI\-generated content back to the knowledge base\.

### Prerequisite

First, configure the IMA Knowledge Base API in the "Connector" module—this is the core switch for bidirectional data flow\.

### Implementation Steps

1. **Get OpenAPI Credentials**

    - Open `https://ima.qq.com/agent-interface` and log in

    - Apply for and obtain two values:

        ```Plain Text
        Client ID
        API Key
        ```

2. **Configure the API**

    - Send the obtained API Key to the IMA skill to complete the configuration

3. **Automatic Closed\-Loop Operation**
After WorkBuddy generates content \(such as meeting minutes, reports, or summaries\), you can directly instruct it:

    ```Plain Text
    Save this content as an IMA note and upload it to the knowledge base
    ```

    The AI will automatically complete the upload, forming a closed loop:
    **Retrieve from Knowledge Base → AI Process \& Generate → Auto\-Save Back to Knowledge Base**

## More Connector Options

In addition to IMA Knowledge Base, WorkBuddy supports seamless integration with multiple platforms:

- **Feishu**: Real\-time synchronization of document messages and multi\-dimensional tables

- **Tencent Docs**: Direct reading and writing of cloud files

- **Lexiang Knowledge Base**: Enterprise internal knowledge linkage

- **Tencent Meeting**: Automatic organization and synchronization of meeting minutes

## Important Reminders

To maintain the accuracy of your knowledge base, follow these best practices:

1. **Clean Up Redundant "Digital Junk"**

    - Regularly delete expired, invalid, or low\-value documents

    - These files not only occupy storage space but also affect the system's response accuracy

2. **Beware of Information Interference**

    - "Noise" in the knowledge base can interfere with the algorithm's judgment logic

    - This may lead to fuzzy search results, incorrect answers, or even unprofessional responses

3. **Maintain a "Pure" Knowledge Base**

    - Keeping the knowledge base "clean and pure" is the key to improving response quality

    - Pure knowledge allows the system to lock in valid information and output professional answers that meet your needs

## Action Recommendations

- Establish a "weekly self\-check \+ monthly review" mechanism

- Each business department should be responsible for cleaning up the content under its jurisdiction

- Set up automatic expiration reminders for key information to ensure the "freshness" and "purity" of the knowledge base from the source

By following this guide, you'll transform WorkBuddy into a truly personalized AI assistant that grows with your knowledge and business needs\. Start building your AI second brain today\!

