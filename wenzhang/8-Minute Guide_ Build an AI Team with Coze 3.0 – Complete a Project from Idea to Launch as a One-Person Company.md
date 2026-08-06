# 8\-Minute Guide: Build an AI Team with Coze 3\.0 – Complete a Project from Idea to Launch as a One\-Person Company

This tutorial shows you how to build a fully functional AI agent team to complete an entire project from idea to launch using Coze 3\.0\. The example project is an anti\-procrastination app called *Time Blocks*, designed to break large tasks into small, actionable 10–30 minute chunks\.

## What You'll Learn

- How to build an AI agent team in Coze 3\.0

- How to assign roles like product manager, designer, developer, and video producer to different AI agents

- How to use skill packs to give agents professional capabilities

- How to run a full project workflow: requirement definition → design → development → video production

- How to manage and iterate on your project using AI collaboration

## Prerequisites

- A Coze 3\.0 account

- Basic understanding of AI agents and workflow automation

- No coding experience required \(though familiarity with tools like Claude Code or Codex CLI is helpful\)

## Step 1: Create a New Project in Coze

1. Open Coze 3\.0 and click the **\+** button in the top\-left corner

2. Select **New Project**

3. Enter the project name: `Time Blocks`

4. Click **Create Project**

## Step 2: Build Your AI Agent Team

You'll create agents for different roles in your project\.

### Create a Product Manager Agent

1. Click the **\+** button again and select **New Agent**

2. Choose **Cloud Agent**

3. Select **Coze Agent** as the base model

4. Name it `Product Manager`

5. Click **Create and Deploy**

6. In the agent settings, select a model \(e\.g\., GPT\-4o, Claude 3\)

7. Go to the **Skill Store** and add the **Product Operations Skill Pack**

8. This skill pack includes:

    - Product strategy and positioning

    - User research and pain point analysis

    - PRD \(Product Requirements Document\) generation

    - User flow design

### Create a Designer Agent

1. Click **\+** → **New Agent** → **Cloud Agent**

2. Name it `Designer`

3. Choose a model suitable for design tasks

4. Add the **UI/UX Design Skill Pack** from the Skill Store

5. This skill pack includes:

    - Wireframing and prototyping

    - Visual design principles

    - Design system creation

    - Handoff documentation for developers

### Create Developer Agents

You'll create two developer agents:

- **Development Planner**: Uses Claude Code to create a detailed development plan

- **Development Executor**: Uses Codex CLI to write the actual code

1. Click **\+** → **New Agent** → **Local Agent**

2. Select **Claude Code** and name it `Development Planner`

3. Click **Create**

4. Repeat the process to create `Development Executor` using **Codex CLI**

### Create a Video Producer Agent

1. Click **\+** → **New Agent** → **Cloud Agent**

2. Name it `Video Producer`

3. Choose a model with strong video generation capabilities

4. Add the **Video Production Skill Pack**

5. This skill pack includes:

    - Script writing

    - Storyboarding

    - Video generation using Seedance

    - Editing and post\-production

## Step 3: Add Agents to Your Project

1. Go to your `Time Blocks` project

2. Click **Project Settings** in the top\-right corner

3. Under **Agent Management**, click **Add**

4. Select all the agents you created:

    - Product Manager

    - Designer

    - Development Planner

    - Development Executor

    - Video Producer

5. Click **Save**

## Step 4: Run the Project Workflow

### 4\.1 Define Requirements with the Product Manager

1. In the project chat, tag the Product Manager agent:

    ```Plain Text
    @ProductManager
    ```

2. Send the following prompt:

    ```Plain Text
    I want to build an anti-procrastination app called "Time Blocks". The app should help users break large, overwhelming tasks into small, 10-30 minute time blocks.
    
    Please:
    1. Define the product positioning
    2. Identify target users and their pain points
    3. Outline core features
    4. Create a user flow
    5. Write a PRD for the designer and developer agents
    
    Use the Product Operations Skill Pack to help you.
    ```

3. The Product Manager will generate a complete PRD document\.

### 4\.2 Design the UI with the Designer

1. Tag the Designer agent:

    ```Plain Text
    @Designer
    ```

2. Send the following prompt:

    ```Plain Text
    Based on the PRD from the Product Manager, design the UI for the Time Blocks app.
    
    Requirements:
    - Single-page layout
    - Visual style: clean, minimal, with a focus on time blocks
    - Include a time board where users can drag and drop time blocks
    - Provide handoff documentation for the developer agents
    
    Use the UI/UX Design Skill Pack to help you.
    ```

3. The Designer will generate:

    - Wireframes

    - Visual design mockups

    - Handoff documentation with CSS styles and component specs

### 4\.3 Create a Development Plan with the Development Planner

1. Tag the Development Planner agent:

    ```Plain Text
    @DevelopmentPlanner
    ```

2. Send the following prompt:

    ```Plain Text
    Based on the PRD and design documents, create a detailed development plan for the Time Blocks app.
    
    Include:
    - Technology stack
    - File structure
    - Development phases
    - Implementation details for each feature
    - Timeline estimates
    
    Use Claude Code to help you.
    ```

3. The Development Planner will generate a comprehensive development plan\.

### 4\.4 Write Code with the Development Executor

1. Tag the Development Executor agent:

    ```Plain Text
    @DevelopmentExecutor
    ```

2. Send the following prompt:

    ```Plain Text
    Based on the development plan, write the code for the Time Blocks app.
    
    Requirements:
    - Use HTML, CSS, and JavaScript
    - Implement the time block drag-and-drop functionality
    - Include a timer for each time block
    - Make the app responsive
    
    Use Codex CLI to help you.
    ```

3. The Development Executor will write the code and create the app\.

### 4\.5 Generate a Promotional Video with the Video Producer

1. Tag the Video Producer agent:

    ```Plain Text
    @VideoProducer
    ```

2. Send the following prompt:

    ```Plain Text
    Create a 60-second promotional video for the Time Blocks app.
    
    Requirements:
    - Script: Explain how the app helps users overcome procrastination
    - Visuals: Show the app in action, with time blocks being dragged and dropped
    - Music: Upbeat and motivating
    - Style: Clean and modern
    
    Use the Video Production Skill Pack and Seedance to generate the video.
    ```

3. The Video Producer will generate a complete promotional video\.

## Step 5: Test and Iterate

1. Test the app to make sure it works correctly

2. If you find issues, tag the relevant agent and ask them to fix it:

    ```Plain Text
    @DevelopmentExecutor
    The time block drag-and-drop functionality is not working correctly. Please fix it.
    ```

3. Iterate until the app is perfect

## Step 6: Deploy the App

1. Once the app is working correctly, deploy it to a hosting service like Vercel or Netlify

2. Share the promotional video on social media to promote the app

## Conclusion

Congratulations\! You've just built a complete AI agent team and used it to create a full project from idea to launch\. This workflow can be applied to any type of project, from app development to content creation to marketing\.

Coze 3\.0 makes it easy to build and manage AI agent teams, allowing you to focus on the big picture while the AI agents handle the details\. With the right skill packs, you can give your AI agents the professional capabilities they need to complete complex tasks\.

## Next Steps

- Try building a different project with your AI agent team

- Experiment with different skill packs to see what capabilities you can add to your agents

- Share your projects with the Coze community to get feedback and inspiration

---

**Note**: Some features mentioned in this tutorial, like multiple local agent access and faster video generation, require the Coze 3\.0 Pro plan\. The free plan includes basic agent collaboration and standard video generation\.

