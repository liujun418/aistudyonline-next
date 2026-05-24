# Harness in Practice: Automating Knowledge Explanation Video Creation


In the realm of content creation, especially for technical knowledge explanation videos, achieving automation while ensuring quality and consistency can be challenging\. This article dives into how to leverage Harness and agent technologies to automate the process of turning an article into a polished knowledge video, with practical steps and code snippets\.

## Introduction: Why Harness for Video Creation?

Creating technical knowledge videos often involves tedious steps: scripting, visual design, animation, and audio synchronization\. With Harness, we can orchestrate agents to handle these tasks automatically\. The core advantage lies in **controllability**—unlike AI video generation models, web\-based video creation via Harness allows precise control over elements like font, color, frame duration, and dynamic effects\. This approach is also more stable and cost\-effective than relying on unstable video model “draws”\.

## The Workflow: From Article to Video

The entire process is divided into four stages, with human checkpoints to ensure quality\. Here’s the breakdown:

### 1\. Content Editing: Script and Development Plan

First, convert the technical article into a **conversational script** \(suited for video narration\) and a **development plan** \(outlining visual steps and chapters\)\.

- **Script Transformation**: Rewrite formal technical prose into short, conversational, second\-person sentences\. For example, “The tool aims to provide efficient solutions” becomes “This tool is designed to solve your problem efficiently—let’s see how\.”

- **Development Plan**: Break the script into visual steps and chapters\. Each paragraph in the script maps to a specific screen step, and several steps form a chapter focused on one topic\.

To automate this, use the following command with Claude Code \(or compatible agents\) to invoke the `web\-video\-presentation` skill:

```bash
claude -v  # Ensure Claude Code is installed and configured
claude run --skill web-video-presentation --input "path/to/your/article.md" --task "generate_script_and_outline"
```

### 2\. Human Checkpoint: Validate and Adjust

After generating the script and development plan, the agent pauses for human review\. You need to confirm:

- Whether the script and development plan need revisions\.

- Which visual theme to use \(the skill offers multiple pre\-designed themes\)\.

- How to prepare materials \(e\.g\., images, diagrams\) and whether to develop chapters sequentially or in parallel\.

### 3\. Web Development and Audio Synthesis

Once confirmed, the agent develops web pages for each chapter and handles audio:

- **Web Development**: Each chapter is developed in an isolated folder \(to avoid conflicts\)\. The agent uses HTML, CSS, and JavaScript to create dynamic visual pages\. For example, to set a custom font and color scheme, the agent modifies code snippets like:

    ```css
    :root {
      --primary-font: "Inter", sans-serif;
      --primary-color: #2c3e50;
      --accent-color: #e74c3c;
    }
    ```

- **Audio Synthesis**: If auto\-synthesis is needed, the agent extracts text from the script and uses the MiniMax CLI for TTS \(Text\-to\-Speech\)\. Install and use the MiniMax CLI with:

    ```bash
    # Install MiniMax CLI
    curl -fsSL https://raw.githubusercontent.com/minimax-ai/cli/main/install.sh | bash
    # Synthesize audio
    mmx tts --text "Your script text here" --output "audio.mp3"
    ```

### 4\. Screen Recording: Generate the Final Video

Open the web pages in a browser, play the synthesized audio, and record the screen\. This ensures perfect synchronization between audio and visuals\. To automate playback and recording, use a tool like `ffmpeg` for screen recording with audio:

```bash
ffmpeg -f avfoundation -i "1:0" -f lavfi -i anullsrc -c:v libx264 -c:a aac -t 60 -y output.mp4
```

## Technical Implementation: Harness Components

A robust Harness for this workflow includes six core components:

### 1\. Context Management

To prevent information overload, split content into stage\-specific documents\. For example:

- `script\-style\.md` \(only read during scripting\)\.

- `chapter\-guide\.md` \(only read during web development\)\.

- `audio\-spec\.md` \(only read during audio synthesis\)\.

This ensures the agent always accesses the most relevant information\.

### 2\. State and Memory

Use files like `outline\.md` to store key decisions \(e\.g\., chapter structure, pacing\)\. When developing later chapters, the agent references this file to maintain consistency\. Example `outline\.md` snippet:

```markdown
- Chapter 1: Introduction to Harness
  - Step 1: Explain "What is Harness?" (3s, use animation)
  - Step 2: Core components overview (5s, use diagram)
- Chapter 2: Workflow Orchestration
  - Step 1: Stage breakdown (4s, use timeline)
```

### 3\. Tool System

Leverage basic file operations \(`read\_file`, `write\_file`\) and specialized tools like the MiniMax CLI\. To avoid conflicts in multi\-agent parallel development, each chapter is in an isolated folder with unique CSS prefixes:

```html
<!-- Chapter 1 HTML -->
<div class="chapter-1-container">
  <h1 class="chapter-1-title">Introduction</h1>
</div>

<!-- Chapter 2 HTML -->
<div class="chapter-2-container">
  <h1 class="chapter-2-title">Workflow</h1>
</div>
```

## Practical Setup: Tools and Configuration

To implement this workflow, set up the following tools:

### 1\. Claude Code \(or Compatible Agents\)

Install Claude Code and configure it to use domestic models \(e\.g\., MiniMax\) via `cc\-switch`:

```bash
# Install Claude Code
curl -fsSL https://claude.ai/install.sh | bash
# Install cc-switch
git clone https://github.com/yourusername/cc-switch.git
cd cc-switch && npm install && npm run build
```

Configure `cc\-switch` to route Claude Code to MiniMax by adding your MiniMax API key in the tool’s settings\.

### 2\. MiniMax CLI for Audio Synthesis

As shown earlier, the MiniMax CLI simplifies TTS\. Ensure you have a valid API key from the MiniMax platform\.

### 3\. Skill Installation: `web\-video\-presentation`

Download and install the skill from GitHub:

```bash
git clone https://github.com/ConardLi/garden-skills.git
cd garden-skills/web-video-presentation
# Follow the setup instructions in the README
```

## Conclusion

By leveraging Harness, agents, and web technologies, you can automate the creation of knowledge explanation videos from articles\. This approach offers unmatched control, stability, and efficiency—empowering content creators to focus on storytelling rather than tedious production tasks\. Try it with your own articles and see how Harness transforms your content workflow\!
