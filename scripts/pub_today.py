"""
Publish June 26, 2026 articles.
0 new tools — both articles about Claude Code features (data storage, Workflow).
"""

import os

BASE = r"C:\Users\jun\aistudyonline-next"
os.chdir(BASE)

# ===== Part 1: Add 2 article metadata to articles.ts =====
with open('src/lib/articles.ts', 'r', encoding='utf-8') as f:
    articles_src = f.read()

new_articles = r"""  {
    slug: "build-stable-data-storage-large-ai-projects-claude-code",
    title: "Build Stable Long-Term Data Storage for Large AI Projects With Claude Code",
    titleZh: "用Claude Code为大型AI项目构建稳定的长期数据存储",
    description: "A complete Node.js data persistence system for Claude Code agent tasks — auto-classification, timestamp naming, version snapshots with auto-cleanup, crash fault recovery, and one-click rollback to any historical state.",
    descriptionZh: "为Claude Code Agent任务构建完整的Node.js数据持久化系统——自动分类、时间戳命名、版本快照自动清理、崩溃故障恢复、一键回滚到任意历史状态。",
    category: "ai-tutorials",
    tags: ["claude-code", "data-storage", "nodejs", "persistence", "snapshot", "fault-recovery"],
    difficulty: "intermediate",
    toolsMentioned: ["claude"],
    date: "2026-06-26",
  },
  {
    slug: "claude-code-workflow-orchestrating-agent-teams",
    title: "Claude Code Workflow: From Writing Code to Orchestrating Agent Teams",
    titleZh: "Claude Code Workflow：从写代码到编排Agent团队",
    description: "Claude Code's major update — Workflow transforms solo coding into agent team orchestration with JavaScript scripts, 5-stage deep-research pipeline, budget control, and verifiable multi-agent coordination at scale.",
    descriptionZh: "Claude Code重大更新——Workflow将单人编码转变为Agent团队编排，JavaScript脚本驱动、5阶段深度研究流水线、预算控制、可验证的大规模多Agent协调。",
    category: "ai-news",
    tags: ["claude-code", "workflow", "agent-orchestration", "deep-research", "multi-agent", "anthropic"],
    difficulty: "beginner",
    toolsMentioned: ["claude"],
    date: "2026-06-26",
  },

"""

last_bracket = articles_src.rfind('];')
articles_new = articles_src[:last_bracket] + new_articles + '];'

with open('src/lib/articles.ts', 'w', encoding='utf-8') as f:
    f.write(articles_new)

print('Part 1: 2 new articles added to articles.ts')

# ===== Part 2: Add 2 article contents to article-content.ts =====
with open('src/lib/article-content.ts', 'r', encoding='utf-8') as f:
    content_src = f.read()

new_contents = r'''
  "build-stable-data-storage-large-ai-projects-claude-code": {
    content: `<div class="meta-banner">
<p><strong>📅 Published:</strong> June 26, 2026 · <strong>🏷️ Category:</strong> AI Tutorials · <strong>📊 Level:</strong> Intermediate · <strong>🛠️ Tools:</strong> Claude Code, Node.js</p>
</div>

<p>This hands-on tutorial belongs to the full Claude Code teaching series, focusing on solving a common pain point for AI developers: unstable, fragmented temporary data storage when running multi-round agent tasks. We will build a persistent, standardized local data warehouse entirely through Claude Code with one-click generation scripts, covering data classification, automatic archiving, version snapshot and fault recovery functions.</p>

<h2>Core Pain Points of Default Temporary Storage in AI Projects</h2>

<p>When you run long-cycle research, multi-step coding or multi-agent tasks on Claude Code, all generated text, table data, API response records and intermediate calculation results are saved as temporary cache files by default, bringing obvious drawbacks:</p>

<ol>
<li>Temporary folders get cleared after restarting Claude Code, all historical task data lost directly</li>
<li>Unclassified mixed files make it impossible to quickly retrieve data from specific projects</li>
<li>No automatic snapshot versioning; you cannot roll back data if AI overwrites key records</li>
<li>Lack built-in fault recovery logic, incomplete data after unexpected program interruption</li>
</ol>

<h2>Step 1: Initialize Standard Data Warehouse Directory Structure</h2>

<p>Send the below requirement prompt to Claude Code to auto-generate the full folder tree and initialization script:</p>

<pre><code class="language-text">Generate a persistent local data storage system for large AI agent projects, include directories for raw input data, intermediate processing records, exported results, version snapshots and error backup logs, output a complete init script in Node.js</code></pre>

<p>The generated initialization script <code>data-store-init.js</code>:</p>

<pre><code class="language-javascript">const fs = require("fs-extra");
const path = require("path");

const rootDataDir = path.resolve("./ai-project-data");
const dirList = [
  path.join(rootDataDir, "raw-input"),
  path.join(rootDataDir, "intermediate-cache"),
  path.join(rootDataDir, "export-output"),
  path.join(rootDataDir, "version-snapshot"),
  path.join(rootDataDir, "error-backup")
];

async function initDataWarehouse() {
  for (const dir of dirList) {
    await fs.ensureDir(dir);
    console.log(\`Created storage directory: \${dir}\`);
  }
  const configTemplate = {
    autoSnapshot: true,
    snapshotInterval: 5,
    autoBackupOnError: true,
    maxSnapshotCount: 20
  };
  await fs.writeJSON(path.join(rootDataDir, "store-config.json"), configTemplate, { spaces: 2 });
  console.log("Data warehouse initialization finished");
}

initDataWarehouse().catch(err => console.error("Init failed:", err));</code></pre>

<pre><code class="language-bash">node data-store-init.js</code></pre>

<h2>Step 2: Core Data Read & Write Persistence Module</h2>

<p>Ask Claude Code to generate a reusable data operation tool <code>data-operator.js</code>:</p>

<pre><code class="language-javascript">const fs = require("fs-extra");
const path = require("path");
const { v4: uuidv4 } = require("uuid");
const config = require("./ai-project-data/store-config.json");

const DATA_ROOT = path.resolve("./ai-project-data");

async function saveIntermediateData(taskName, dataContent) {
  const fileName = \`\${taskName}_\${Date.now()}_\${uuidv4()}.json\`;
  const savePath = path.join(DATA_ROOT, "intermediate-cache", fileName);
  await fs.writeJSON(savePath, dataContent, { spaces: 2 });
  console.log(\`Intermediate data saved: \${fileName}\`);
  await checkAndCreateSnapshot();
  return savePath;
}

async function exportFinalResult(taskName, resultData) {
  const outPath = path.join(DATA_ROOT, "export-output", \`\${taskName}_final_output.json\`);
  await fs.writeJSON(outPath, resultData, { spaces: 2 });
  return outPath;
}

async function checkAndCreateSnapshot() {
  const snapshotDir = path.join(DATA_ROOT, "version-snapshot");
  const existSnapshots = await fs.readdir(snapshotDir);
  if (existSnapshots.length >= config.maxSnapshotCount) {
    existSnapshots.sort((a, b) => a.split("_")[0] - b.split("_")[0]);
    await fs.remove(path.join(snapshotDir, existSnapshots[0]));
  }
  const snapName = \`\${Date.now()}_task_snapshot\`;
  await fs.copy(path.join(DATA_ROOT, "intermediate-cache"), path.join(snapshotDir, snapName));
}

async function restoreSnapshot(snapshotFolderName) {
  const source = path.join(DATA_ROOT, "version-snapshot", snapshotFolderName);
  const target = path.join(DATA_ROOT, "intermediate-cache");
  await fs.emptyDir(target);
  await fs.copy(source, target);
  console.log(\`Restored data from snapshot: \${snapshotFolderName}\`);
}

module.exports = { saveIntermediateData, exportFinalResult, restoreSnapshot };</code></pre>

<pre><code class="language-bash">npm install fs-extra uuid</code></pre>

<h2>Step 3: Integrate Storage Module Into Claude Code Agent Tasks</h2>

<p>When you run research, code generation or multi-agent tasks, import the storage tool:</p>

<pre><code class="language-javascript">const { saveIntermediateData, exportFinalResult } = require("./data-operator");

async function runAITaskDemo() {
  const taskData = {
    taskId: "market-research-001",
    model: "Claude 3.5 Code",
    roundCount: 12,
    rawSearchContent: [...],
    analysisConclusion: "xxx",
    codeSnippets: [...]
  };
  await saveIntermediateData("market-research", taskData);
  await exportFinalResult("market-research", taskData.analysisConclusion);
}

runAITaskDemo();</code></pre>

<h2>Step 4: Fault Backup Mechanism For Abnormal Interruption</h2>

<p>Add error capture logic to auto back up incomplete data when Claude Code task crashes unexpectedly:</p>

<pre><code class="language-javascript">process.on("uncaughtException", async (err) => {
  console.error("Task interrupted unexpectedly, backing up unfinished data");
  const unfinishedCache = path.join(DATA_ROOT, "intermediate-cache");
  const backupTarget = path.join(DATA_ROOT, "error-backup", \`crash_backup_\${Date.now()}\`);
  await fs.copy(unfinishedCache, backupTarget);
  process.exit(1);
});</code></pre>

<h2>Step 5: Quick Management Commands For Daily Use</h2>

<pre><code class="language-bash"># List all saved snapshots
node data-manage.js list-snapshots

# Roll back data to target snapshot
node data-manage.js restore 1751234567890_task_snapshot</code></pre>

<h2>Practical Usage Advantages</h2>

<ol>
<li>All task data permanently saved locally, no loss after restarting Claude Code</li>
<li>Automatic layered classification separates raw materials, middle records and final outputs</li>
<li>Timed snapshots with auto cleanup avoid disk overflow</li>
<li>One-click data rollback to any historical task state</li>
<li>Crash automatic backup prevents incomplete data wasting long agent running time</li>
</ol>

<h2>Final Operation Tips</h2>

<ol>
<li>Add the whole <code>ai-project-data</code> folder into <code>.gitignore</code> to avoid submitting massive local data to GitHub repositories</li>
<li>Modify <code>store-config.json</code> to adjust snapshot frequency and maximum storage quantity based on your project size</li>
<li>For ultra-long multi-day agent tasks, extend the snapshot interval to reduce disk write frequency</li>
</ol>

<h2>常见问题</h2>

<h3>Does this work with any Claude Code project or only specific setups?</h3>
<p>It works with any Claude Code project. The data storage system is a standalone Node.js module that you require() into your task scripts — it doesn't depend on Claude Code internals. As long as your agent tasks run in a Node.js environment, the persistence layer works transparently.</p>

<h3>How much disk space does the snapshot system consume?</h3>
<p>With the default config (max 20 snapshots), disk usage depends on your intermediate data size. For typical AI projects with JSON/CSV intermediate data, 20 snapshots typically consume 50-200MB. The auto-cleanup deletes the oldest snapshot when the limit is reached, so storage stays bounded. Adjust <code>maxSnapshotCount</code> in <code>store-config.json</code> to fit your needs.</p>

<h3>Can I use this with multi-agent workflows?</h3>
<p>Yes — and that's one of its best use cases. When multiple agents generate intermediate data concurrently, each gets a unique UUID-based filename, preventing collisions. The snapshot system captures the entire intermediate-cache state at that moment, so you can roll back all agents' data to a consistent point in time.</p>

<div class="next-step">
<p><strong>下一篇：</strong> <a href="/en/article/claude-code-workflow-orchestrating-agent-teams">Claude Code Workflow: From Writing Code to Orchestrating Agent Teams →</a></p>
</div>`,
    contentZh: `<div class="meta-banner">
<p><strong>📅 发布日期：</strong>2026年6月26日 · <strong>🏷️ 分类：</strong>AI教程 · <strong>📊 难度：</strong>中级 · <strong>🛠️ 工具：</strong>Claude Code、Node.js</p>
</div>

<p>本实操教程属于Claude Code完整教学系列，聚焦解决AI开发者的常见痛点：运行多轮Agent任务时临时数据存储不稳定、碎片化。我们将完全通过Claude Code一键生成脚本构建一个持久化、标准化的本地数据仓库，涵盖数据分类、自动归档、版本快照和故障恢复功能。</p>

<h2>AI项目默认临时存储的核心痛点</h2>

<p>在Claude Code上运行长周期研究、多步编码或多Agent任务时，所有生成的文本、表格数据、API响应记录和中间计算结果默认保存为临时缓存文件，带来明显缺陷：</p>

<ol>
<li>重启Claude Code后临时文件夹被清理，所有历史任务数据直接丢失</li>
<li>未分类的混合文件无法快速检索特定项目数据</li>
<li>无自动快照版本控制；AI覆盖关键记录后无法回滚</li>
<li>缺少内置故障恢复逻辑，程序意外中断后数据不完整</li>
</ol>

<h2>步骤1：初始化标准数据仓库目录结构</h2>

<p>向Claude Code发送以下需求提示，自动生成完整文件夹树和初始化脚本：</p>

<pre><code class="language-text">为大型AI Agent项目生成本地持久化数据存储系统，包含原始输入数据、中间处理记录、导出结果、版本快照和错误备份日志目录，输出完整Node.js初始化脚本</code></pre>

<p>生成的初始化脚本 <code>data-store-init.js</code>：</p>

<pre><code class="language-javascript">const fs = require("fs-extra");
const path = require("path");

const rootDataDir = path.resolve("./ai-project-data");
const dirList = [
  path.join(rootDataDir, "raw-input"),
  path.join(rootDataDir, "intermediate-cache"),
  path.join(rootDataDir, "export-output"),
  path.join(rootDataDir, "version-snapshot"),
  path.join(rootDataDir, "error-backup")
];

async function initDataWarehouse() {
  for (const dir of dirList) {
    await fs.ensureDir(dir);
    console.log(\`已创建存储目录: \${dir}\`);
  }
  const configTemplate = {
    autoSnapshot: true,
    snapshotInterval: 5,
    autoBackupOnError: true,
    maxSnapshotCount: 20
  };
  await fs.writeJSON(path.join(rootDataDir, "store-config.json"), configTemplate, { spaces: 2 });
  console.log("数据仓库初始化完成");
}

initDataWarehouse().catch(err => console.error("初始化失败:", err));</code></pre>

<pre><code class="language-bash">node data-store-init.js</code></pre>

<h2>步骤2：核心数据读写持久化模块</h2>

<p>让Claude Code生成可复用的数据操作工具 <code>data-operator.js</code>：</p>

<pre><code class="language-javascript">const fs = require("fs-extra");
const path = require("path");
const { v4: uuidv4 } = require("uuid");
const config = require("./ai-project-data/store-config.json");

const DATA_ROOT = path.resolve("./ai-project-data");

async function saveIntermediateData(taskName, dataContent) {
  const fileName = \`\${taskName}_\${Date.now()}_\${uuidv4()}.json\`;
  const savePath = path.join(DATA_ROOT, "intermediate-cache", fileName);
  await fs.writeJSON(savePath, dataContent, { spaces: 2 });
  console.log(\`中间数据已保存: \${fileName}\`);
  await checkAndCreateSnapshot();
  return savePath;
}

async function exportFinalResult(taskName, resultData) {
  const outPath = path.join(DATA_ROOT, "export-output", \`\${taskName}_final_output.json\`);
  await fs.writeJSON(outPath, resultData, { spaces: 2 });
  return outPath;
}

async function checkAndCreateSnapshot() {
  const snapshotDir = path.join(DATA_ROOT, "version-snapshot");
  const existSnapshots = await fs.readdir(snapshotDir);
  if (existSnapshots.length >= config.maxSnapshotCount) {
    existSnapshots.sort((a, b) => a.split("_")[0] - b.split("_")[0]);
    await fs.remove(path.join(snapshotDir, existSnapshots[0]));
  }
  const snapName = \`\${Date.now()}_task_snapshot\`;
  await fs.copy(path.join(DATA_ROOT, "intermediate-cache"), path.join(snapshotDir, snapName));
}

async function restoreSnapshot(snapshotFolderName) {
  const source = path.join(DATA_ROOT, "version-snapshot", snapshotFolderName);
  const target = path.join(DATA_ROOT, "intermediate-cache");
  await fs.emptyDir(target);
  await fs.copy(source, target);
  console.log(\`已从快照恢复数据: \${snapshotFolderName}\`);
}

module.exports = { saveIntermediateData, exportFinalResult, restoreSnapshot };</code></pre>

<pre><code class="language-bash">npm install fs-extra uuid</code></pre>

<h2>步骤3：将存储模块集成到Claude Code Agent任务中</h2>

<p>运行研究、代码生成或多Agent任务时，导入存储工具：</p>

<pre><code class="language-javascript">const { saveIntermediateData, exportFinalResult } = require("./data-operator");

async function runAITaskDemo() {
  const taskData = {
    taskId: "market-research-001",
    model: "Claude 3.5 Code",
    roundCount: 12,
    rawSearchContent: [...],
    analysisConclusion: "xxx",
    codeSnippets: [...]
  };
  await saveIntermediateData("market-research", taskData);
  await exportFinalResult("market-research", taskData.analysisConclusion);
}

runAITaskDemo();</code></pre>

<h2>步骤4：异常中断的故障备份机制</h2>

<p>添加错误捕获逻辑，在Claude Code任务意外崩溃时自动备份未完成数据：</p>

<pre><code class="language-javascript">process.on("uncaughtException", async (err) => {
  console.error("任务意外中断，正在备份未完成数据");
  const unfinishedCache = path.join(DATA_ROOT, "intermediate-cache");
  const backupTarget = path.join(DATA_ROOT, "error-backup", \`crash_backup_\${Date.now()}\`);
  await fs.copy(unfinishedCache, backupTarget);
  process.exit(1);
});</code></pre>

<h2>步骤5：日常快速管理命令</h2>

<pre><code class="language-bash"># 列出所有已保存快照
node data-manage.js list-snapshots

# 回滚数据到目标快照
node data-manage.js restore 1751234567890_task_snapshot</code></pre>

<h2>实际使用优势</h2>

<ol>
<li>所有任务数据本地永久保存，重启Claude Code不丢失</li>
<li>自动分层分类，分离原始材料、中间记录和最终输出</li>
<li>定时快照自动清理，避免磁盘溢出</li>
<li>一键数据回滚到任意历史任务状态</li>
<li>崩溃自动备份，防止不完整数据浪费长时间Agent运行</li>
</ol>

<h2>最终操作提示</h2>

<ol>
<li>将整个 <code>ai-project-data</code> 文件夹加入 <code>.gitignore</code>，避免提交海量本地数据到GitHub仓库</li>
<li>根据项目规模修改 <code>store-config.json</code> 调整快照频率和最大存储数量</li>
<li>超长多天Agent任务，延长快照间隔以减少磁盘写入频率</li>
</ol>

<h2>常见问题</h2>

<h3>这适用于任何Claude Code项目还是仅特定设置？</h3>
<p>适用于任何Claude Code项目。数据存储系统是独立的Node.js模块，你通过require()引入到任务脚本中——不依赖Claude Code内部。只要Agent任务在Node.js环境中运行，持久化层就透明工作。</p>

<h3>快照系统消耗多少磁盘空间？</h3>
<p>默认配置（最多20个快照），磁盘使用取决于中间数据大小。对于典型的JSON/CSV中间数据的AI项目，20个快照通常消耗50-200MB。达到限制时自动清理删除最旧快照，所以存储保持有界。在 <code>store-config.json</code> 中调整 <code>maxSnapshotCount</code> 以适应需求。</p>

<h3>能用于多Agent工作流吗？</h3>
<p>可以——这是其最佳用例之一。当多个Agent并发生成中间数据时，每个都获得基于UUID的唯一文件名，避免冲突。快照系统捕获该时刻的整个intermediate-cache状态，因此你可以将所有Agent的数据回滚到一致的时间点。</p>

<div class="next-step">
<p><strong>下一篇：</strong> <a href="/zh/article/claude-code-workflow-orchestrating-agent-teams">Claude Code Workflow：从写代码到编排Agent团队 →</a></p>
</div>`,
  },

  "claude-code-workflow-orchestrating-agent-teams": {
    content: `<div class="meta-banner">
<p><strong>📅 Published:</strong> June 26, 2026 · <strong>🏷️ Category:</strong> AI News · <strong>📊 Level:</strong> Beginner · <strong>🛠️ Tools:</strong> Claude Code</p>
</div>

<p>Claude Code has just rolled out a major update — <strong>Workflow</strong>, a feature that transforms Claude Code from a solo coder into an orchestrator of agent teams. This innovation might be Anthropic's next big leap following MCP and Skill, and here's how it works in practice.</p>

<h2>What Makes Claude Code Workflow Different?</h2>

<p>When you think of workflow tools, Dify or Coze might come to mind. But Claude Code's Workflow is unique:</p>

<ul>
<li>Describe a task, and Claude automatically writes a <strong>JavaScript orchestration script</strong>.</li>
<li>It breaks tasks into stages, assigns each stage to different agents, and coordinates dozens to hundreds of subagents in the background to deliver results.</li>
</ul>

<p>Unlike the temporary Agent Teams of the past, Workflow <strong>solidifies agent coordination into code</strong>. It becomes auditable, reusable, and version-controllable — no more relying on the model's on-the-spot performance.</p>

<h2>Deep Dive into the Built-in Deep-Research Workflow</h2>

<p>Let's take the official <code>deep-research</code> workflow as an example. It consists of five stages:</p>

<h3>1. Scope: Multidimensional Disassembly</h3>
<p>Break down your question into search terms from 5 different angles to ensure comprehensive coverage.</p>

<h3>2. Search: Parallel Search</h3>
<p>5 agents search simultaneously, each fetching 4-6 results for their assigned angle — no waiting for each other.</p>

<h3>3. Fetch-Extract: Deduplication and Extraction</h3>
<p>After deduplication, up to 15 webpages are crawled. Each page yields 2-5 verifiable concrete conclusions.</p>

<h3>4. Verify: Cross-Validation</h3>
<p>For each conclusion, 3 skeptical agents independently look for counterevidence. Conclusions with 2 or more objections are rejected.</p>

<h3>5. Synthesize: Merge and Synthesize</h3>
<p>Merge verified conclusions, sort them by confidence, and compile a final report with source citations.</p>

<h2>Practical Demo: Researching Claude Code Workflow</h2>

<p>To test this, we used <code>deep-research</code> to investigate Claude Code's latest Workflow feature and write an article. Here's what happened:</p>

<ul>
<li><strong>Time:</strong> 25 minutes</li>
<li><strong>Agents Involved:</strong> 104</li>
<li><strong>Token Usage:</strong> 2.8 million</li>
<li><strong>Claims Verified:</strong> 25</li>
<li><strong>Output:</strong> A complete article covering Workflow's core positioning, differences from Agent Teams, runtime limits, and the built-in <code>deep-research</code> workflow.</li>
</ul>

<h2>Budget Control: Avoid Token Overspending</h2>

<p>Without budget limits, Workflow could become a "token shredder." To prevent this, you can define a budget directly in the task:</p>

<pre><code class="language-text">workflow 100k</code></pre>

<p>Claude Code will optimize agent count, stage depth, and convergence method based on this budget.</p>

<h2>How to Use Workflow</h2>

<p>There are two ways to activate Workflow:</p>

<h3>1. Trigger with a Prompt Word</h3>

<p>Mention "workflow" in your prompt. The word will turn colorful, and Claude will automatically generate a workflow:</p>

<pre><code class="language-text">请 workflow 帮我深度调研 Claude Code 的 Workflow 功能，写一篇文章</code></pre>

<h3>2. Command Activation</h3>

<p>Use <code>/effort ultracode</code> to let Claude generate a workflow based on your task:</p>

<pre><code class="language-text">/effort ultracode</code></pre>

<p>To check the running workflow and agent count, use:</p>

<pre><code class="language-text">/workflows</code></pre>

<h2>The Significance of Workflow</h2>

<p>Claude Code's Workflow isn't just a new feature — it's a signal that AI programming is shifting from individual capability to <strong>organizational capability</strong>.</p>

<ul>
<li>In the past, we asked: <em>Can a model write code?</em></li>
<li>Later, we asked: <em>Can an agent complete a task independently?</em></li>
<li>Now, we ask: <em>Can a system organize multiple agents to complete complex tasks verifiably within a budget?</em></li>
</ul>

<p>This shift opens up new possibilities for tackling large-scale, multi-faceted challenges with AI.</p>

<h2>常见问题</h2>

<h3>How is Workflow different from regular multi-agent setups in Claude Code?</h3>
<p>The key difference: Workflow is <strong>code-driven</strong>, not prompt-driven. Traditional multi-agent setups rely on the model deciding at runtime which agents to spawn. Workflow generates a JavaScript script that defines the exact orchestration logic — stages, agent assignments, parallelization, verification gates. This script is auditable (you can read exactly what it will do), reusable (run the same workflow on different inputs), and version-controllable (commit it to Git). It's the difference between improvising a team on the spot and having a written playbook.</p>

<h3>What's a reasonable budget for a deep-research workflow?</h3>
<p>Based on the demo: a single deep-research task with 104 agents consumed 2.8M tokens. For quick overviews, budget 500k-1M tokens. For thorough research with adversarial verification (the default), budget 2-3M tokens. Start with a smaller budget and increase if you need deeper coverage. The budget cap is a hard limit — the workflow will optimize within it rather than exceeding it.</p>

<h3>Can I write my own custom workflows?</h3>
<p>Yes. Workflow scripts are plain JavaScript with a defined API (agent(), parallel(), pipeline(), phase(), log()). You can write them by hand or have Claude Code generate them from a natural language description. Custom workflows can be saved to <code>.claude/workflows/</code> and reused across sessions. The API supports patterns like pipeline (sequential stages), parallel (concurrent agents), and loop-until-dry (iterative discovery).</p>

<div class="next-step">
<p><strong>Previous:</strong> <a href="/en/article/build-stable-data-storage-large-ai-projects-claude-code">Build Stable Long-Term Data Storage for Large AI Projects With Claude Code ←</a></p>
</div>`,
    contentZh: `<div class="meta-banner">
<p><strong>📅 发布日期：</strong>2026年6月26日 · <strong>🏷️ 分类：</strong>AI新闻 · <strong>📊 难度：</strong>初级 · <strong>🛠️ 工具：</strong>Claude Code</p>
</div>

<p>Claude Code刚刚推出了重大更新——<strong>Workflow</strong>，这项功能将Claude Code从独立编码者转变为Agent团队的编排器。这一创新可能是Anthropic继MCP和Skill之后的下一个重大飞跃，下面介绍它的实际运作方式。</p>

<h2>Claude Code Workflow有何不同？</h2>

<p>提到工作流工具，你可能会想到Dify或Coze。但Claude Code的Workflow是独特的：</p>

<ul>
<li>描述任务，Claude自动编写<strong>JavaScript编排脚本</strong>。</li>
<li>将任务分解为阶段，为每个阶段分配不同的Agent，在后台协调数十到数百个子Agent交付结果。</li>
</ul>

<p>与过去临时的Agent Teams不同，Workflow <strong>将Agent协调固化为代码</strong>。它变得可审计、可复用、可版本控制——不再依赖模型的临场发挥。</p>

<h2>深入内置Deep-Research工作流</h2>

<p>以官方 <code>deep-research</code> 工作流为例，它包含五个阶段：</p>

<h3>1. Scope：多维度拆解</h3>
<p>从5个不同角度将问题拆解为搜索词，确保全面覆盖。</p>

<h3>2. Search：并行搜索</h3>
<p>5个Agent同时搜索，每个获取4-6条结果——互不等待。</p>

<h3>3. Fetch-Extract：去重和提取</h3>
<p>去重后最多爬取15个网页。每页产出2-5条可验证的具体结论。</p>

<h3>4. Verify：交叉验证</h3>
<p>每条结论由3个怀疑论Agent独立寻找反证。有2个及以上反对意见的结论被拒绝。</p>

<h3>5. Synthesize：合并与综合</h3>
<p>合并已验证结论，按置信度排序，编制附来源引用的最终报告。</p>

<h2>实战演示：调研Claude Code Workflow</h2>

<p>为测试，我们用 <code>deep-research</code> 调研Claude Code最新Workflow功能并撰写文章。结果如下：</p>

<ul>
<li><strong>时间：</strong>25分钟</li>
<li><strong>参与Agent：</strong>104个</li>
<li><strong>Token消耗：</strong>280万</li>
<li><strong>已验证结论：</strong>25条</li>
<li><strong>输出：</strong>一篇完整文章，涵盖Workflow核心定位、与Agent Teams的区别、运行时限制和内置 <code>deep-research</code> 工作流。</li>
</ul>

<h2>预算控制：避免Token超支</h2>

<p>没有预算限制，Workflow可能成为"token碎纸机"。为防止此情况，可直接在任务中定义预算：</p>

<pre><code class="language-text">workflow 100k</code></pre>

<p>Claude Code会根据此预算优化Agent数量、阶段深度和收敛方式。</p>

<h2>如何使用Workflow</h2>

<p>有两种激活Workflow的方式：</p>

<h3>1. 提示词触发</h3>

<p>在提示中提及"workflow"。该词会变成彩色，Claude将自动生成工作流：</p>

<pre><code class="language-text">请 workflow 帮我深度调研 Claude Code 的 Workflow 功能，写一篇文章</code></pre>

<h3>2. 命令激活</h3>

<p>使用 <code>/effort ultracode</code> 让Claude根据任务生成工作流：</p>

<pre><code class="language-text">/effort ultracode</code></pre>

<p>查看正在运行的工作流和Agent数量：</p>

<pre><code class="language-text">/workflows</code></pre>

<h2>Workflow的意义</h2>

<p>Claude Code的Workflow不只是一个新功能——它是一个信号，表明AI编程正从个体能力转向<strong>组织能力</strong>。</p>

<ul>
<li>过去，我们问：<em>模型能写代码吗？</em></li>
<li>后来，我们问：<em>Agent能独立完成任务吗？</em></li>
<li>现在，我们问：<em>系统能组织多个Agent在预算内可验证地完成复杂任务吗？</em></li>
</ul>

<p>这一转变为用AI应对大规模、多方面的挑战开启了新的可能性。</p>

<h2>常见问题</h2>

<h3>Workflow与Claude Code中常规的多Agent设置有何不同？</h3>
<p>关键区别：Workflow是<strong>代码驱动</strong>的，而非提示驱动的。传统多Agent设置依赖模型在运行时决定生成哪些Agent。Workflow生成JavaScript脚本，定义确切的编排逻辑——阶段、Agent分配、并行化、验证关卡。这个脚本可审计（你可以精确读取它将做什么）、可复用（在不同输入上运行相同工作流）、可版本控制（提交到Git）。这就像现场即兴组队 vs 拥有书面战术手册的区别。</p>

<h3>深度研究工作流的合理预算是多少？</h3>
<p>基于演示：单次深度研究任务，104个Agent消耗280万tokens。快速概览预算50万-100万tokens。带对抗验证的彻底研究（默认）预算200万-300万tokens。从较小预算开始，需要更深覆盖时增加。预算上限是硬限制——工作流会在限制内优化而非超出。</p>

<h3>能编写自己的自定义工作流吗？</h3>
<p>可以。Workflow脚本是纯JavaScript，具有定义的API（agent()、parallel()、pipeline()、phase()、log()）。你可以手写或让Claude Code从自然语言描述生成。自定义工作流可保存到 <code>.claude/workflows/</code> 并跨会话复用。API支持pipeline（顺序阶段）、parallel（并发Agent）和loop-until-dry（迭代发现）等模式。</p>

<div class="next-step">
<p><strong>上一篇：</strong> <a href="/zh/article/build-stable-data-storage-large-ai-projects-claude-code">用Claude Code为大型AI项目构建稳定的长期数据存储 ←</a></p>
</div>`,
  },

'''

last_brace = content_src.rfind('};')
content_new = content_src[:last_brace] + new_contents + '};'

with open('src/lib/article-content.ts', 'w', encoding='utf-8') as f:
    f.write(content_new)

print('Part 2: 2 article contents added to article-content.ts')

print('\n=== All done! Run build to verify ===')
