"""Publish Aug 26, 2026 — 1 article (Auto-Evolving AI Knowledge Base), no new tools."""
import os

BASE = r"C:\Users\jun\aistudyonline-next"
os.chdir(BASE)

SLUG = "build-auto-evolving-ai-knowledge-base-hands-on-tutorial"

# ---------------------------------------------------------------------------
# Part 1: articles.ts
# ---------------------------------------------------------------------------
a = r"""  {
    slug: "build-auto-evolving-ai-knowledge-base-hands-on-tutorial",
    title: "Hands-On Tutorial: Build an Auto-Evolving AI Knowledge Base",
    titleZh: "实操教程：搭建自动进化的AI知识库",
    description: "Build an auto-evolving AI knowledge base that collects, filters, and structures new information on its own. Master the closed-loop workflow — folder-trigger collection, JSON knowledge-sorting agent, API write-back with duplicate skip, and scheduled self-optimization — so your knowledge base grows without manual file uploading.",
    descriptionZh: "搭建能自动收集、筛选、结构化新信息的自动进化AI知识库。掌握闭环工作流——文件夹触发器收集、JSON知识整理Agent、API写回去重、定时自我优化——让知识库无需手动上传文件也能自我成长。",
    category: "ai-tutorials",
    tags: ["Knowledge Base", "AI Agent", "Automation", "RAG", "Self-Evolving", "Closed Loop", "Workflow", "Tutorial"],
    difficulty: "beginner",
    toolsMentioned: [],
    date: "2026-08-26",
  },
"""
with open("src/lib/articles.ts", encoding="utf-8") as f:
    s = f.read()
last = s.rfind("];")
assert last != -1, "articles.ts: ]; marker not found"
s2 = s[:last] + a + s[last:]
with open("src/lib/articles.ts", "w", encoding="utf-8", newline="\n") as f:
    f.write(s2)
print("articles.ts updated")

# ---------------------------------------------------------------------------
# Part 2: article-content.ts
# ---------------------------------------------------------------------------
content = r"""  "build-auto-evolving-ai-knowledge-base-hands-on-tutorial": {
    content: `<div class="meta-banner">
  <span class="meta-badge">📚 AI Tutorials</span>
  <span class="meta-badge">🕒 8 min read</span>
  <span class="meta-badge">📅 Aug 26, 2026</span>
  <span class="meta-badge">🎯 Beginner</span>
</div>

<h2 id="introduction">Introduction</h2>

<p>Ordinary AI knowledge bases require you to manually upload files one by one. Once materials are updated, you have to re-upload and re-parse everything. This repetitive work is exhausting. In this tutorial, we will build an <strong>auto-evolving AI knowledge base</strong> — a system that automatically collects new information, sorts out content, adds knowledge entries, and optimizes itself without constant manual file uploading. Even AI-generated outputs can feed back into the knowledge base, forming a self-growing closed-loop system. This guide is made for AI beginners; you can copy-paste the prompts and configurations directly to practice.</p>

<h2 id="core-logic">Core Logic of an Auto-Evolving Knowledge Base</h2>

<p>The auto-evolving knowledge base runs on a simple closed-loop workflow:</p>

<blockquote>
  <p>Collect new information → Filter valid content → Re-organize knowledge entries → Write into knowledge base → AI uses knowledge to generate output → Feed new output back into knowledge base</p>
</blockquote>

<p>Instead of humans doing all the import work, the AI agent takes charge of information collection, filtering, and updating. Your job is to set rules and review key results.</p>

<h2 id="preparation">Preparation Work</h2>

<p>You need an AI Agent platform that supports knowledge bases plus custom skill triggers. Prerequisites:</p>

<ol>
  <li>Create an empty knowledge base as your main storage library.</li>
  <li>Enable the custom agent skill and workflow trigger function.</li>
  <li>Get your knowledge base API credentials: <code>API-Endpoint</code> and <code>Access-Key</code>.</li>
</ol>

<blockquote>
  <p>Store your credential variables safely. Never hard-print raw keys in chat windows.</p>
</blockquote>

<pre><code class="language-text">API-Endpoint = "your-knowledge-base-api-url"
Access-Key = "your-access-key-here"</code></pre>

<h2 id="step-1-collection">Step 1: Configure the Information Collection Source</h2>

<p>Set where your knowledge base obtains new raw materials. Common sources include a local monitoring folder, web page crawling, chat-session output, meeting transcripts, and note-software synchronization.</p>

<p>Take local folder monitoring as a practical example:</p>

<ol>
  <li>Create a dedicated local folder for incoming materials.</li>
  <li>Turn on the folder-monitoring trigger inside your agent workflow.</li>
  <li>Set the trigger rule: when new files (<code>.pdf</code>, <code>.txt</code>, <code>.md</code>, <code>.docx</code>) appear in this folder, start the auto-evolution workflow automatically.</li>
</ol>

<blockquote>
  <p>You do not need to manually open the knowledge base and click upload. Just drop new documents into this folder, and the whole process kicks off.</p>
</blockquote>

<h2 id="step-2-filtering-agent">Step 2: Build the Filtering &amp; Knowledge-Sorting Agent Prompt</h2>

<p>This is the most critical part. The agent reads raw files, throws away junk content, extracts valuable points, and restructures standardized knowledge entries. Paste this prompt block directly into your agent system:</p>

<pre><code class="language-text">You are the knowledge sorting agent for the auto-evolving knowledge base.
Task rules:
1. Read input raw document content. Remove redundant ads, repeated paragraphs, and meaningless noise text.
2. Split long content into independent knowledge entries. Each entry contains: Title, Tags, Core-Content, Source-Reference.
3. Tags should be concise keywords for later retrieval. Do not make tags too long.
4. Do not fabricate facts. All content must come from the original input material.
5. Output format must strictly follow the JSON structure below, no extra explanatory chat text.

Output JSON format:
{
  "knowledge_list": [
    {
      "title": "knowledge entry title",
      "tags": ["tag1","tag2"],
      "core_content": "condensed core information",
      "source_reference": "file name or web source"
    }
  ]
}</code></pre>

<p>After parsing finishes, the agent outputs structured JSON knowledge entries, ready to be written into the knowledge base via API.</p>

<h2 id="step-3-api-write">Step 3: Automatically Write Entries via API Call</h2>

<p>Configure the agent API-call node to push the JSON knowledge list into your knowledge base. Sample request payload template:</p>

<pre><code class="language-json">{
  "knowledge_items": {{knowledge_list}},
  "overwrite_strategy": "skip_duplicate",
  "auto_create_tag": true
}</code></pre>

<ul>
  <li><strong>overwrite_strategy: skip_duplicate</strong> — if the same title and source already exist in the library, skip the import to avoid duplicate knowledge pollution.</li>
  <li><strong>auto_create_tag</strong> — automatically generate tag categories inside the knowledge base.</li>
</ul>

<blockquote>
  <p>Important setting: turn on duplicate detection. Without this switch, repeated similar entries will pile up and reduce AI answer quality.</p>
</blockquote>

<h2 id="step-4-closed-loop">Step 4: Realize Closed-Loop Evolution — Feed AI Output Back</h2>

<p>This step differentiates an auto-evolving knowledge base from a regular static one. Every time your AI finishes answering questions or generates reports/summaries, trigger a secondary workflow.</p>

<p>Trigger instruction you send to the agent:</p>

<pre><code class="language-text">Treat this AI-generated reply as new source material. Run the knowledge-sorting agent prompt, extract valid knowledge points, filter out useless conversational filler content, and write qualified new knowledge entries back to the auto-evolving knowledge base. Skip vague conclusions without factual support.</code></pre>

<p>Workflow logic:</p>

<p><strong>User question → Knowledge base provides reference → AI generates answer → Agent extracts new knowledge points → Append into knowledge base</strong></p>

<p>Now your knowledge base continuously absorbs both external documents and internal AI-produced insights.</p>

<h2 id="step-5-self-optimization">Step 5: Add a Regular Self-Optimization Task</h2>

<p>Set a scheduled cron trigger for a weekly knowledge-base maintenance task. Run this prompt periodically:</p>

<pre><code class="language-text">You are the knowledge-base maintenance agent.
Read existing entries in the current knowledge base:
1. Merge highly duplicated knowledge entries.
2. Mark outdated information and tag it as "obsolete". Do not directly delete for traceability.
3. Supplement cross-reference links between related knowledge entries.
4. Output the optimized updated knowledge list, and call the API to apply changes.</code></pre>

<p>This scheduled job keeps your knowledge base clean, prevents information bloat, and maintains query response accuracy.</p>

<h2 id="practical-tips">Practical Usage Tips</h2>

<ol>
  <li><strong>Watch your input quality</strong>: don't throw messy, unfiltered files into the monitoring folder. The filtering agent can handle noise, but too much garbage input will lower final knowledge quality.</li>
  <li><strong>Keep duplicate-skip always enabled</strong>: mass duplicates will break retrieval performance.</li>
  <li><strong>Enable human review for critical knowledge</strong>: new entries will wait for your manual confirmation before being written into the base.</li>
  <li><strong>Monitor growth speed</strong>: if entries expand extremely fast, check whether your filtering rules are too loose.</li>
</ol>

<h2 id="troubleshooting">Common Troubleshooting</h2>

<h3>New files are dropped into the folder, but no new knowledge appears</h3>
<p>Check the trigger status, verify the API Access-Key validity, and confirm the file format is supported.</p>

<h3>Knowledge entries are too long and messy after auto-parsing</h3>
<p>Adjust the sorting-agent prompt and strengthen the requirements for the condensed core-content field.</p>

<h3>AI-generated low-quality nonsense is written into the knowledge library</h3>
<p>Add a stricter rule to the prompt: reject entries without factual support, and turn on human review mode.</p>

<h2 id="conclusion">Final Summary</h2>

<p>A traditional knowledge base is static storage. An auto-evolving AI knowledge base builds a self-reinforcing loop: automatic collection, intelligent filtering, structured parsing, scheduled maintenance, and feeding AI output back to expand your knowledge inventory.</p>

<p>You don't need complex development work. By configuring trigger rules, a sorting-agent prompt, and an API writing node, beginners can deploy this system. Start with small-scale test files first, tune the filtering rules, then expand to full-scale use.</p>

<h2>常见问题</h2>

<h3>Do I need to write code to build this system?</h3>
<p>No. The whole system is driven by configuration and prompts: trigger rules (folder monitoring), a knowledge-sorting agent prompt, and an API-write node with a paste-ready JSON payload. The only "API" work is replacing two credential placeholders and one template field. If your platform supports knowledge-base connectors (like WorkBuddy + IMA Knowledge Base), you can often skip the API entirely.</p>

<h3>Which platforms can I use to build an auto-evolving knowledge base?</h3>
<p>Any AI Agent platform that supports knowledge bases plus custom skill or workflow triggers. Popular choices include WorkBuddy with IMA Knowledge Base, agent frameworks with built-in KB APIs, and RAG platforms with scheduled jobs. The pattern is platform-agnostic — what matters is that your platform exposes three things: a collection trigger, an agent-prompt slot, and a way to write entries programmatically.</p>

<h3>How do I prevent the knowledge base from being polluted with low-quality content?</h3>
<p>Use three layers of protection: (1) keep duplicate detection on so repeated entries never pile up; (2) strengthen the sorting-agent prompt — demand condensed core-content, require factual grounding, and reject vague conclusions; (3) turn on the human-review switch for critical business knowledge so new entries wait for your confirmation before being written.</p>

<h3>What's the difference between this and a static knowledge base?</h3>
<p>A static knowledge base only answers from files you manually upload and re-upload. An auto-evolving knowledge base closes the loop: it collects new materials by trigger, filters and structures them into entries automatically, and even feeds AI-generated output back in — then runs scheduled maintenance to merge duplicates and mark obsolete content. It grows and cleans itself, which is the entire point.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Want to go deeper with AI knowledge bases? Keep exploring:</p>
  <ul>
    <li><a href="/article/build-personal-ai-knowledge-base-workbuddy-ima-guide">Build Your Personal AI Knowledge Base with WorkBuddy + IMA: A Step-by-Step Guide</a> — set up a concrete WorkBuddy + IMA knowledge base first</li>
    <li><a href="/article/build-ai-second-brain-workbuddy-ima-knowledge-base">Step-by-Step Guide: Build Your AI Second Brain with WorkBuddy + IMA Knowledge Base</a> — add the bidirectional closed loop to your knowledge system</li>
    <li><a href="/article/why-99-percent-ai-knowledge-bases-fail-in-practice">Why 99% of AI Knowledge Bases Fail in Practice</a> — avoid the common RAG pitfalls that kill knowledge-base quality</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">📚 AI 教程</span>
  <span class="meta-badge">🕒 阅读约8分钟</span>
  <span class="meta-badge">📅 2026年8月26日</span>
  <span class="meta-badge">🎯 入门</span>
</div>

<h2 id="introduction">引言</h2>

<p>普通的AI知识库需要你一个一个手动上传文件。一旦资料更新，又要重新上传、重新解析，重复劳动让人疲惫。本教程中，我们将搭建一个<strong>自动进化的AI知识库</strong>——它能自动收集新信息、梳理内容、添加知识条目并自我优化，无需频繁手动上传文件。甚至AI生成的输出也能反馈回知识库，形成自我成长的闭环系统。本指南面向AI初学者，提示词和配置都可以直接复制粘贴练习。</p>

<h2 id="core-logic">自进化知识库的核心逻辑</h2>

<p>自进化知识库运行在一个简单的闭环工作流之上：</p>

<blockquote>
  <p>收集新信息 → 筛选有效内容 → 重新组织知识条目 → 写入知识库 → AI使用知识生成输出 → 新输出反馈回知识库</p>
</blockquote>

<p>导入工作不再由人类完成，而是由AI Agent负责信息收集、筛选和更新。你的工作只是设定规则并审核关键结果。</p>

<h2 id="preparation">准备工作</h2>

<p>你需要一个支持知识库+自定义技能触发的AI Agent平台。前置条件：</p>

<ol>
  <li>创建一个空知识库作为你的主存储库。</li>
  <li>开启自定义Agent技能和工作流触发功能。</li>
  <li>获取你的知识库API凭证：<code>API-Endpoint</code> 和 <code>Access-Key</code>。</li>
</ol>

<blockquote>
  <p>请安全保存你的凭证变量。切勿在聊天窗口中明文打印原始密钥。</p>
</blockquote>

<pre><code class="language-text">API-Endpoint = "你的知识库API地址"
Access-Key = "你的访问密钥"</code></pre>

<h2 id="step-1-collection">第一步：配置信息收集源</h2>

<p>设定知识库获取新原料的渠道。常见来源包括：本地监控文件夹、网页爬取、会话输出、会议转写、笔记软件同步。</p>

<p>以本地文件夹监控为例：</p>

<ol>
  <li>创建一个专门的本地文件夹存放待入库材料。</li>
  <li>在Agent工作流中开启文件夹监控触发器。</li>
  <li>设置触发规则：当该文件夹出现新文件（<code>.pdf</code>、<code>.txt</code>、<code>.md</code>、<code>.docx</code>）时，自动启动自进化工作流。</li>
</ol>

<blockquote>
  <p>你无需手动打开知识库点击上传。只要把新文档丢进这个文件夹，整个流程就会自动启动。</p>
</blockquote>

<h2 id="step-2-filtering-agent">第二步：构建筛选与知识整理Agent提示词</h2>

<p>这是最关键的一步。Agent会读取原始文件、丢弃垃圾内容、提取有价值要点，并重构为标准化的知识条目。把这段提示词直接粘贴进你的Agent系统：</p>

<pre><code class="language-text">你是自进化知识库的知识整理Agent。
任务规则：
1. 读取输入的原始文档内容，删除冗余广告、重复段落和无意义的噪音文本。
2. 将长内容拆分为独立的知识条目。每个条目包含：标题、标签、核心内容、来源引用。
3. 标签应使用简洁关键词，便于后续检索，不要太长。
4. 不得编造事实。所有内容必须来自原始输入材料。
5. 输出格式必须严格遵循下方JSON结构，不要附带额外解释性聊天文本。

输出JSON格式：
{
  "knowledge_list": [
    {
      "title": "知识条目标题",
      "tags": ["标签1","标签2"],
      "core_content": "凝练的核心信息",
      "source_reference": "文件名或网页来源"
    }
  ]
}</code></pre>

<p>解析完成后，Agent输出结构化的JSON知识条目，即可通过API写入知识库。</p>

<h2 id="step-3-api-write">第三步：通过API调用自动写入条目</h2>

<p>配置Agent的API调用节点，把JSON知识列表推入知识库。请求负载模板示例：</p>

<pre><code class="language-json">{
  "knowledge_items": {{knowledge_list}},
  "overwrite_strategy": "skip_duplicate",
  "auto_create_tag": true
}</code></pre>

<ul>
  <li><strong>overwrite_strategy: skip_duplicate</strong>——如果库中已存在相同标题与来源，则跳过导入，避免重复知识污染。</li>
  <li><strong>auto_create_tag</strong>——在知识库内自动生成标签分类。</li>
</ul>

<blockquote>
  <p>重要设置：务必开启去重检测。没有这个开关，相似的重复条目会不断堆积，拉低AI回答质量。</p>
</blockquote>

<h2 id="step-4-closed-loop">第四步：实现闭环进化——将AI输出反馈回知识库</h2>

<p>这一步是自进化知识库与普通静态知识库的本质区别。每次AI完成问题回答或生成报告/总结后，触发一个次级工作流。</p>

<p>发给Agent的触发指令：</p>

<pre><code class="language-text">把这段AI生成的回复当作新的源材料。运行知识整理Agent提示词，提取有效的知识要点，过滤掉无用的对话填充内容，把合格的新知识条目写回自进化知识库。跳过没有事实依据的模糊结论。</code></pre>

<p>工作流逻辑：</p>

<p><strong>用户提问 → 知识库提供参考 → AI生成答案 → Agent从答案中提取新知识点 → 追加进知识库</strong></p>

<p>现在，你的知识库能持续吸收外部文档和内部AI产出的洞见。</p>

<h2 id="step-5-self-optimization">第五步：添加定期自我优化任务</h2>

<p>设置定时cron触发，执行每周的知识库维护任务。定期运行这段提示词：</p>

<pre><code class="language-text">你是知识库维护Agent。
读取当前知识库中的现有条目：
1. 合并高度重复的知识条目。
2. 标记过期信息并打上"obsolete"标签，为了可追溯性不要直接删除。
3. 为相关条目之间补充交叉引用链接。
4. 输出优化后的知识列表，并调用API应用变更。</code></pre>

<p>这个定时任务能让知识库保持整洁、防止信息膨胀，并维持查询回答的准确性。</p>

<h2 id="practical-tips">实用使用技巧</h2>

<ol>
  <li><strong>把好输入关</strong>：不要往监控文件夹里丢杂乱未过滤的文件。筛选Agent能处理噪音，但太多垃圾输入会拉低最终的知识质量。</li>
  <li><strong>始终开启去重跳过</strong>：海量重复会破坏检索性能。</li>
  <li><strong>关键业务知识开启人工审核</strong>：新条目会等待你手动确认后才写入知识库。</li>
  <li><strong>监控知识增长速度</strong>：如果条目膨胀极快，检查筛选规则是否过于宽松。</li>
</ol>

<h2 id="troubleshooting">常见问题排查</h2>

<h3>文件已丢入文件夹，但没有新知识出现</h3>
<p>检查触发状态、验证API Access-Key是否有效、确认文件格式受支持。</p>

<h3>自动解析后知识条目过长且杂乱</h3>
<p>调整整理Agent提示词，强化对core-content核心内容字段凝练程度的要求。</p>

<h3>AI生成的低质量废话被写进了知识库</h3>
<p>在提示词中增加更严格的规则：拒绝没有事实依据的条目；开启人工审核模式。</p>

<h2 id="conclusion">总结</h2>

<p>传统知识库是静态存储。自动进化的AI知识库则构建了一条自我强化的闭环：自动收集、智能筛选、结构化解析、定时维护，以及把AI输出反馈回来扩充知识库存。</p>

<p>你不需要复杂的开发工作。通过配置触发规则、整理Agent提示词和API写入节点，初学者就能部署这套系统。先用小规模测试文件起步，调好筛选规则，再扩展到全量使用。</p>

<h2>常见问题</h2>

<h3>搭建这套系统需要写代码吗？</h3>
<p>不需要。整个系统由配置和提示词驱动：触发规则（文件夹监控）、知识整理Agent提示词、以及带现成JSON负载的API写入节点。所谓的"API"工作只是替换两个凭证占位符和一个模板字段。如果你的平台支持知识库连接器（如WorkBuddy + IMA知识库），甚至可以完全跳过API。</p>

<h3>可以用哪些平台搭建自进化知识库？</h3>
<p>任何支持知识库+自定义技能或工作流触发的AI Agent平台都可以。常见选择包括：WorkBuddy + IMA知识库、内置KB API的Agent框架、支持定时任务的RAG平台。这套模式与平台无关——关键在于你的平台要能暴露三样东西：收集触发器、Agent提示词槽位、程序化写入条目的途径。</p>

<h3>如何防止低质量内容污染知识库？</h3>
<p>用三层防护：(1) 始终开启去重检测，让重复条目无法堆积；(2) 强化整理Agent提示词——要求凝练的核心内容、强制事实依据、拒绝模糊结论；(3) 对关键业务知识开启人工审核开关，让新条目先等待你的确认再写入。</p>

<h3>它和静态知识库有什么区别？</h3>
<p>静态知识库只能回答你手动上传并反复更新的文件。自进化知识库则打通了闭环：通过触发器自动收集新材料、自动筛选并结构化知识条目、甚至把AI生成的输出反馈回库——再运行定时维护去重和标记过期内容。它会自我成长和自我清理，这正是它的核心价值。</p>

<div class="next-step">
  <h3>📖 继续学习</h3>
  <p>想深入了解AI知识库？继续探索：</p>
  <ul>
    <li><a href="/article/build-personal-ai-knowledge-base-workbuddy-ima-guide">用WorkBuddy + IMA搭建个人AI知识库：完整步骤指南</a> — 先搭好一个具体的WorkBuddy + IMA知识库</li>
    <li><a href="/article/build-ai-second-brain-workbuddy-ima-knowledge-base">分步指南：用WorkBuddy + IMA知识库打造你的AI第二大脑</a> — 为你的知识系统加上双向闭环</li>
    <li><a href="/article/why-99-percent-ai-knowledge-bases-fail-in-practice">为什么99%的AI知识库在实践中失败</a> — 避开拖垮知识库质量的常见RAG陷阱</li>
  </ul>
</div>`,
  },
"""
with open("src/lib/article-content.ts", encoding="utf-8") as f:
    s = f.read()
last = s.rfind("};")
assert last != -1, "article-content.ts: }; marker not found"
s2 = s[:last] + content + s[last:]
with open("src/lib/article-content.ts", "w", encoding="utf-8", newline="\n") as f:
    f.write(s2)
print("article-content.ts updated")
print("Done. Article:", SLUG)
