# Build a Karpathy\-Style AI Knowledge Base: A 2\-Minute Setup with Just 3 Folders

Karpathy’s recent tweet about his AI\-powered personal knowledge base went viral, garnering 44K saves and millions of views in just two days\. The key insight? He leverages AI to organize scattered notes and articles into a searchable system—no Notion or Obsidian needed, just a simple folder structure and a text file\. Here’s how to build your own, with practical steps you can implement today\.

## The 3\-Folder Structure: Super Simple, Fully Flat

This system can be set up in two minutes, with each folder serving a distinct purpose:

- **raw/**: A drop zone for all your unorganized raw materials—articles, screenshots, notes, etc\. Just dump everything here without worrying about organization\.

- **wiki/**: The AI\-curated knowledge base\. This is where AI writes organized content after processing raw materials\. Never edit this folder manually\.

- **outputs/**: Stores AI\-generated answers, reports, and analysis results\.

To create these folders, run the following commands in your terminal:

```bash
mkdir my-knowledge-base
cd my-knowledge-base
mkdir raw wiki outputs
```

## The Schema File: Your AI’s Instruction Manual

A schema file is crucial to guide AI on how to structure and manage your knowledge base\. Create a `CLAUDE.md` file in the root directory with rules like:

```markdown
# What This Is
A personal knowledge base about [your topic].

# How to Organize
- raw/: Raw materials, never modify.
- wiki/: AI-maintained organized content.
- outputs/: Generated reports and answers.

# Wiki Rules
- One .md file per topic.
- Link related topics using [[topic-name]] format.
- Maintain INDEX.md to list all main topics.
```

Karpathy emphasizes that this schema is “super simple”—just a text file telling AI the rules\. It directly impacts the quality of the AI\-curated wiki, so don’t skip this step\.

## Launch AI Processing with One Command

With the folders and schema ready, open Claude Code and issue this prompt:

> “Read all content in raw/\. Follow the rules in \[CLAUDE\.md\]\(CLAUDE\.md\) to compile a wiki in wiki/\. First create \[INDEX\.md\]\(INDEX\.md\), then create a \.md file for each main topic\. Link related topics\. Summarize each section\.”
> 
> 

Then let AI run—no need to monitor it\. Once complete, you’ll get a `wiki` folder with topic\-organized articles and an `INDEX.md` for easy navigation\.

## Accelerate Content Collection with agent\-browser

To supercharge raw material collection, use `agent-browser`—a tool that lets AI control a real Chrome browser to scrape web content\. It handles JavaScript\-rendered pages, login\-required content, and infinitely scrolling pages, while saving 82% more tokens than tools like Playwright MCP\.

Install and use it with these commands:

```bash
npm install -g @vercel/agent-browser
agent-browser install
# Example usage
agent-browser open https://some-article.com
agent-browser get text "article"  # Saves text directly to raw/
```

## Start Using Your Knowledge Base Today

Karpathy’s knowledge base has 44K saves, but the real value comes from actually building and using it\. With three folders, one schema file, and an AI tool, you can have your own system up and running in a weekend\. Pick a topic you’re eager to master, dump your existing articles and notes into `raw/`, and let AI do the rest\.


