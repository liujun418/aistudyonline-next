# WorkBuddy L05: Master the 3\-Layer Memory System – Make AI Understand You Better

## Introduction

If you’ve ever found yourself reintroducing yourself to an AI assistant every time you start a new conversation, or having to re\-explain your preferences when switching projects, this tutorial is for you\. WorkBuddy’s 3\-layer memory system is designed to solve these exact problems, allowing AI to truly "remember" you and adapt to your workflow over time\.

## What is the 3\-Layer Memory System?

WorkBuddy’s memory system is structured into three layers, each serving a unique purpose and working together to create a seamless, personalized experience:

1. **Layer 1: Cloud Memory**

    - Automatically learns your habits and preferences over time

    - Generates a personal profile that works across all conversations

    - Requires no manual management

2. **Layer 2: User\-level Local Memory**

    - Stores information you explicitly ask WorkBuddy to remember

    - Example: "Use this design style for this series of projects"

    - Saved in a local file

3. **Layer 3: Workspace Memory**

    - Maintains independent records for each project

    - Automatically adds daily logs after completing substantive work

    - Requires no manual effort from you

These three layers work together, moving from broad to specific, from passive to active, to create a comprehensive memory system\.

## Deep Dive into Each Layer

### Layer 1: Cloud Memory

Cloud memory has two core capabilities:

#### 1\. Auto Profile Generation

- Servers analyze your conversations to automatically summarize your code preferences, work habits, and commonly used tools

- This profile is automatically loaded every time you start a new conversation

- WorkBuddy "recognizes" you without you having to reintroduce yourself

#### 2\. Cross\-Conversation History Search

- When you mention something like "the deployment solution we discussed last week," WorkBuddy uses `conversation_search` to search through all your historical conversations

- It can find the exact discussion, including tools used, configurations, and ports

- You don’t have to re\-explain everything – it finds the information itself

### Layer 2 \& 3: Local Memory

#### Layer 2: User\-level Local Memory

- Stored in the `MEMORY.md` file

- When you explicitly state your requirements, those rules are written to this file

- Applies to all projects and conversations moving forward

#### Layer 3: Workspace Memory

- Stored in the `.workbuddy/memory/` directory within your project folder

- After you complete substantive work, WorkBuddy automatically adds a daily log entry

- Logs include what you did, what solutions you used, and what problems you encountered

- Logs older than 30 days are refined into long\-term project notes

## Memory System \+ Skills \+ Automation: The Complete Workflow

### Skills System

- Memory is the "brain" of WorkBuddy, while the skills system is its "hands"

- Skills are divided into three categories: user\-level, project\-level, and built\-in marketplace

- A skill is a reusable workflow

- Example: If you have the `poster-design-warm-tech` skill installed, simply say "help me create a tech poster" and WorkBuddy automatically loads the skill’s context and generates it according to the preset workflow

- After completing a complex workflow, WorkBuddy can automatically accumulate it as a new skill, getting smarter with use

### Automation System

- Automation is the most "active" form of the memory system

- Supports both recurring tasks and one\-time tasks

- Examples:

    - "Generate a market briefing every morning at 9 AM"

    - "Write a weekly report automatically every Friday at 5 PM"

- Can specify which expert to activate automatically and which third\-party service to connect to

In simple terms:

- Cloud memory is passively learned

- Local memory is static rules

- Workspace memory is post\-work records

- Automation is "pre\-set future memory" that automatically wakes up and executes at specified times

## Practical Operation Guide

### Setting Up Automation Tasks

1. Open WorkBuddy

2. Click "Automation" → "Add Task"

3. Fill in the following:

    - Name

    - Workspace

    - Prompt

    - Connector

    - Execution frequency

Each configuration item corresponds to a piece of memory:

- The prompt is the "memory body" of automation

- The expert and connector determine the context scope

### Key Settings Interfaces

#### 1\. Memory Settings

- The management center for cloud memory

- Here you can toggle automatic profile generation, manage existing memory cards, and import habits from other AI platforms

#### 2\. Conversation Management

- The cost switch for cloud memory

- Automatically disconnects context after long periods of inactivity to save tokens

- With `conversation_search`, disconnecting doesn’t mean forgetting

#### 3\. Personalization

- The rule engine for local memory

- Custom instructions written here are saved to the `MEMORY.md` file

- Applies to all projects with the highest priority

#### 4\. Data Management

- The archive for workspace memory

- Centralized display of shared files, archived tasks, and installed applications for all projects

#### 5\. Workspace

- The write trigger for workspace memory

- Manually save content to `.workbuddy/`

- Works with automatic log addition to form a complete memory loop

## Summary

Good AI assistants aren’t one\-time tools – they remember your every decision and help you accumulate every experience\.

1. **Use Memory Wisely**

    - Say "remember this" to save rules locally

    - Say "the solution we discussed last time" to use cloud memory

    - Let it automatically write logs after completing important work

2. **Accumulate Skills**

    - Complex workflows are automatically accumulated

    - Bug fixes are automatically learned

    - Reusable workflows mean you don’t have to start from scratch every time

3. **Free Your Hands**

    - Set up automation to handle recurring tasks

    - Let WorkBuddy work for you even when you’re not around

This is the WorkBuddy memory system – making AI understand you better, work more efficiently, and become a true partner in your workflow\.

