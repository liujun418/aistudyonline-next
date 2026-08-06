# Vibe Coding Practical Guide: AI Development Full Workflow \(Part 1\)

## Introduction: The Common Dilemma in AI Project Initiation

You might have been in this situation: you open AI excitedly, eager to build your own project, but end up sitting there, clueless about the first step\. Your mind is full of ideas, yet you don’t know where to start\. So, you might just say, "Help me build a certain system," throw everything to AI, and then watch helplessly as it writes more and more chaotically, making you increasingly unsure\.

This article is part of the "Vibe Coding" series, focusing on the workflow of AI development from project initiation to before writing code\. The entire series is structured around a development process: project initiation, task breakdown, technology selection, and project architecture\. Each episode is released separately, but when combined, they form a complete workflow\. However, when people watch them piecemeal, they often understand each segment but struggle to string them together when doing a project from scratch\. So, this article will walk you through this process step by step\.

Since there’s a lot to cover, it’s split into two parts\. This part \(Part 1\) focuses on the early preparation phase—how to lay the groundwork and establish rules before writing code\.

## Four Key Steps Before AI Writes Business Logic

Before letting AI handle business functions, there are four crucial steps: **project initiation and feature list**, **technology stack selection**, **project architecture setup**, and **writing an Agent Constitution**\. Only after completing these four steps can you say the groundwork and rules are properly established\. Let’s break them down one by one\.

### Step 1: Project Initiation and Feature List

This is the starting point of the entire process, and it’s also the step many people are tempted to skip\. Project initiation means figuring out what the project is supposed to do\. The feature list involves breaking that down into clear, individual features\. These two steps have been covered in detail in previous articles; if you haven’t seen them, check out the "Project Initiation" and "Project Initiation Supplement" episodes\.

A key reminder: if you skimp on this step, rework is likely later\. Because if you don’t know what you need, AI will be guessing when building the project\.

In essence, when developing with AI, the only thing that changes is the role in development\. Previously, when building a product, the project party had to clarify business requirements with programmers\. Now, AI is your programmer, so you must clarify requirements with AI clearly\. Whether now or before, whether dealing with a professional programmer or AI, ambiguous requirements are always dangerous\.

### Step 2: Technology Stack Selection

Once you’ve decided what the project will do, you need to decide what technologies to use—that’s technology stack selection\. You need to determine the front\-end tech stack, component library, back\-end language, and framework\.

The key here isn’t to pick the most advanced or powerful technologies, but the ones that best suit your project and that AI is most familiar with\. Don’t underestimate this step; it’s very important\. You can’t just decide it casually\. If you choose wrong, problems often surface halfway through, and starting over is very time\-consuming and labor\-intensive\.

For specific selection methods and how to use AI to judge if you’re over\-engineering, check previous articles\. Here, just remember: once the technology stack is decided, don’t waver\. If the front\-end switches from React to Vue overnight, or the back\-end from Python to Go, each waver means rebuilding the previous groundwork\.

### Step 3: Project Architecture Setup

After deciding on the technology stack, the next step is to set up the project architecture\. Whether it’s front\-end or back\-end, before writing business logic, you should first set up a solid and stable project architecture\. It’s like building a skyscraper—you don’t start by decorating a room; you first set up the foundation, framework, and load\-bearing walls\. The project architecture is the framework of your building\.

Note: This step isn’t about having AI write all features like login, orders, and payments right away\. Instead, you first set up a minimal, runnable framework and establish general rules\.

Take the back\-end as an example: first ensure the project can start, configurations can be read, interfaces return consistently, error handling is uniform, and set up logging, database connections, and permission entry points\. The front\-end is similar: decide how to structure directories, how to standardize components, how to unify request handling, and how to manage state\. In short, for both front\-end and back\-end, you first establish a set of rules that every feature will follow\.

For details on how to set this up and judge if the framework is stable, check previous breakdowns for front\-end and back\-end \(there’s even a dedicated episode on back\-end skeleton setup and acceptance\)\. We won’t elaborate here\.

### Step 4: Writing an Agent Constitution

Once the groundwork is laid, you need to establish an "Agent Constitution" for the project\. What is an Agent Constitution? Why can it keep AI in check? This was covered in previous videos; if you haven’t seen it, check those out\. Here’s a brief overview: the Agent Constitution is a set of rules for AI to follow when working on the project—rules that must be adhered to for any feature\.

People often get stuck on two points with this Constitution:

1. How does it actually control AI?

2. Where exactly should it be placed?

Let’s address these:

#### How the Agent Constitution Works

Many people think the Agent Constitution is just a document for their own reference, and once written, it’s left alone\. That’s not true\. The key is that most AI programming tools have a mechanism where if you place the rule file in a specified location, the tool automatically reads it into AI’s context every time it starts a task\. Essentially, before you ask AI to do anything, it “recites” these rules from start to finish\. So, it’s not just for show; it actually influences every decision AI makes\.

#### Where to Place the Agent Constitution

Because it relies on a specific location, the second issue arises: the Constitution must be placed correctly\. If placed correctly, the tool reads it automatically every time; if placed incorrectly, the tool ignores it, making the Constitution useless\. Different development tools require different locations and filenames\. You don’t need to memorize these\. The most reliable way is to ask your AI tool directly:

```Plain Text
Please create an Agent Constitution file in the location that this tool automatically reads.
```

It will place it correctly for you\.

Also, don’t confuse it with the project architecture design document\. The architecture document describes how the project’s code is organized and where directories are placed\. The Agent Constitution defines the behavioral rules AI must follow, such as:

- Must follow the architecture design document\.

- If changing the underlying layer, framework, or adding new dependencies, explain the reason first\.

- Use the framework’s built\-in capabilities instead of writing your own from scratch whenever possible\.

- Self\-inspect after completing each phase\.

#### Why Write It in Step 4?

A useful Constitution must be tailored to your project’s actual situation—your project initiation details, feature list, and technology stack\. These are all finalized in the first three steps, so writing the Constitution now ensures accuracy\.

#### How to Write It

You don’t need to create it from scratch\. I have a general Agent Constitution template that I use for projects\. This template isn’t made up; it’s derived from Codex analyzing all the Constitutions in my projects and summarizing them into a general version\. So, it’s based on real projects, not just a random creation\.

However, don’t just copy this template directly into your project\. Many people do that and think it’s done, but that’s wrong\. My template is general and designed for AI, not for you to read directly\. I’ve left many variable placeholders for AI to fill\.

The correct approach is to give the template to AI and say:

```Plain Text
Please create a project-specific Agent Constitution based on the actual situation of the current project and this general template.
```

The key here is “based on your project’s actual situation”—your project initiation, feature list, and technology stack aren’t in the general template\. AI needs to adapt these general rules to your project’s specific language, framework, and business for the Constitution to be truly effective\.

After customization, glance through it\. If there’s anything you don’t understand, don’t pretend to get it\. Ask AI to explain each rule in plain language\.

## Part 1 Summary

To recap, the four steps in Part 1 are:

1. **Project Initiation and Feature List**: Clarify what to build and break it into individual features\.

2. **Technology Stack Selection**: Choose what’s best for your project and what AI is familiar with, then stick with it\.

3. **Project Architecture Setup**: For both front\-end and back\-end, first set up a runnable framework and establish uniform rules\.

4. **Write an Agent Constitution**: Document the rules AI must follow for all features, ensuring AI reviews them before each task\.

After these four steps, the groundwork and rules are in place\. Remember this rule: once the groundwork is laid, try not to redo it later\. The reasons and costs of redoing it will be covered in Part 2\.

Once the groundwork and rules are set, the next step is to have AI start writing code\. How to break each major phase into detailed sub\-phases and guide AI step by step without it going off track will be covered in Part 2\.

If you haven’t even initiated your project, check out the previous "Project Initiation" episode\. If you want the general Agent Constitution template, leave a comment with "Constitution"\.

