# Upgrade Your Obsidian Homepage: Build AI\-Powered Smart Dashboard for Knowledge Workflow

For long\-term Obsidian users, most custom home dashboards rely on basic Markdown combined with DataviewJS plugins\. These simple layouts can display recent notes, daily task lists, reading heatmaps and file catalogs, but they lack compatibility with modern AI coding tools like Claude Code, Codex, custom Skills, RSS data feeds and GitHub open\-source synchronization\. This tutorial shares a complete hands\-on workflow to rebuild your Obsidian homepage into an automated AI hub that connects your knowledge base with all mainstream LLM coding agents\.

## Limitations of Traditional Dataview Homepage Solutions

The classic DataviewJS homepage only focuses on local vault data queries and static page rendering, with obvious drawbacks in current AI work scenarios:

1. Cannot trigger one\-click AI script execution inside the vault

2. No native integration channels to call Claude Code / Codex coding agents

3. Unable to load external dynamic data such as GitHub updates and RSS news

4. Cannot auto\-generate structured notes via LLM based on inbox raw materials

5. Lacks one\-click vault health inspection and knowledge sorting automation

The upgraded AI dashboard fixes all these pain points while retaining your original note query modules\.

## Step 1: Set Up Obsidian Custom Plugin Development Environment

We will build a lightweight custom dashboard plugin to support AI agent docking, which runs independently without conflicting with existing community plugins\.
Open your terminal and execute these commands to initialize the plugin project folder:

```bash
# Create project directory
mkdir obsidian-ai-dashboard
cd obsidian-ai-dashboard
# Initialize npm environment
npm init -y
# Install official Obsidian API dependency
npm install @obsidianmd/obsidian-api typescript
# Add build script dependency
npm install --save-dev esbuild
```

Create a core entry file `main.ts` as the plugin foundation:

```typescript
import { Plugin } from "obsidian";

export default class AIDashboardPlugin extends Plugin {
  async onload() {
    // Register homepage dashboard view
    this.registerView("ai-dashboard-view", (leaf) => {
      return new AIDashboardView(leaf, this);
    });
    // Add sidebar button to open dashboard
    this.addRibbonIcon("dashboard", "Open AI Dashboard", () => {
      this.activateView();
    });
  }

  async activateView() {
    const { workspace } = this.app;
    let leaf = workspace.getLeaf(false);
    await leaf.setViewState({ type: "ai-dashboard-view", active: true });
  }
}

class AIDashboardView extends TextFileView {
  constructor(leaf, plugin) {
    super(leaf);
    this.plugin = plugin;
  }
  getViewType() { return "ai-dashboard-view"; }
  getDisplayText() { return "AI Dashboard Homepage"; }
  async onLoadFile() {}
  async save() {}
}
```

Add build configuration in `package.json` scripts to compile the plugin:

```json
"scripts": {
  "dev": "esbuild main.ts --outfile=main.js --target=es2020 --watch",
  "build": "esbuild main.ts --outfile=main.js --target=es2020 --minify"
}
```

Run compilation command to generate usable plugin files:

```bash
npm run build
```

Copy the generated `main.js` and `manifest.json` to your Obsidian vault’s `.obsidian/plugins/obsidian-ai-dashboard/` folder, then enable the plugin inside Obsidian settings\.

## Step 2: Build Integrated Frontend Panel with Frontend\-Design Skill

Instead of bulky UI frameworks, call the official `frontend-design` Skill from Claude Code to generate lightweight dashboard HTML components\. Send this prompt to Claude Code for page prototype generation:

```text
Create an Obsidian dashboard UI with 4 core sections:
1. Original Dataview module: Recent files, pending tasks, monthly note heatmap
2. AI Agent operation area: Buttons for deep research, code generation, vault sorting
3. External data panel: RSS feed list, GitHub repository update log
4. Inbox processing module: Auto summarize raw markdown via LLM
Use plain HTML + inline CSS, compatible with Obsidian internal view, no external resource requests
```

After the UI code is output, inject it into the `AIDashboardView` rendering function to display the full homepage layout\.

## Step 3: Realize One\-Click AI Agent Calling Function

Add click triggers on dashboard buttons to send tasks to Claude Code or Codex via local API interface\. Sample calling logic snippet:

```typescript
// Trigger deep research task button click event
document.getElementById("btn-deep-research").addEventListener("click", async () => {
  const vaultPath = this.app.vault.getRoot().path;
  const prompt = `Run deep research on all unprocessed inbox files under ${vaultPath}/Inbox, organize structured knowledge notes and save to /Research folder`;
  
  // Send request to local Claude Code service port
  const res = await fetch("http://127.0.0.1:8080/claude-code/run", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ task: prompt })
  });
  const result = await res.json();
  // Pop up completion notification inside Obsidian
  new Notice(`Deep Research finished: ${result.fileCount} notes generated`);
});
```

Start the local Claude Code background service with this terminal command before using the function:

```bash
claude-code serve --port 8080
```

## Step 4: Embed Dynamic External Data Modules

### 4\.1 RSS Real\-Time Feed

Add DataviewJS code block to the dashboard Markdown container to pull subscription news:

```dataviewjs
const RSS = require("rss-parser");
const parser = new RSS();
const feedUrl = "https://example-tech-blog.com/feed.xml";
const feed = await parser.parseURL(feedUrl);
let list = "";
feed.items.slice(0,10).forEach(item => {
  list += `- [${item.title}](${item.link}) | ${item.pubDate}\n`
})
dv.header(3, "Latest Tech RSS");
dv.markdown(list);
```

### 4\.2 GitHub Repository Sync Log

Call GitHub open API to display commit updates of your code repository on the homepage:

```bash
# Terminal test request for GitHub latest commits
curl https://api.github.com/repos/your-name/your-project/commits?per_page=5
```

Wrap the request in the dashboard plugin to auto\-refresh commit logs every hour\.

## Step 5: Auto Vault Maintenance \& Knowledge Sorting

Add a vault inspection button to execute batch sorting scripts through Codex\. Example task prompt:

```text
Scan the entire Obsidian vault:
1. Mark orphan files without internal links
2. Tag untagged notes by content topic via LLM
3. Merge duplicate concept notes
4. Generate vault structure overview report and save as Vault-Overview.md
```

## Final Optimization Suggestions

1. Retain your original Dataview query code to avoid abandoning existing note statistics

2. Limit concurrent AI task quantity to prevent local port service overload

3. Add switch toggles in plugin settings to turn off RSS/GitHub data modules when not needed

4. Bind hotkeys for core dashboard functions via Obsidian hotkey settings panel

## Closing Words

Upgrading your Obsidian homepage from a static note display page to an AI collaborative dashboard connects your personal knowledge library with mainstream LLM coding agents\. All code and commands provided in this article can be directly replicated and modified according to your vault structure, greatly improving the efficiency of note sorting, technical research and AI code development work\.

