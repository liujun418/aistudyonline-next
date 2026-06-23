"""
Publish June 23, 2026 articles.
1 new tool: MiniMax M3 (Chinese flagship model with coding+multimodal+agent capabilities)
"""

import os

BASE = r"C:\Users\jun\aistudyonline-next"
os.chdir(BASE)

# ===== Part 1: Add 1 new tool to tools.ts =====
with open('src/lib/tools.ts', 'r', encoding='utf-8') as f:
    tools_src = f.read()

new_tool = r"""  {
    id: "minimax-m3",
    name: "MiniMax M3",
    description: "Flagship Chinese AI model integrating coding, native multimodality, agent capabilities, and million-token context.",
    descriptionZh: "中国旗舰AI模型，融合编程、原生多模态、Agent能力和百万token上下文。",
    category: "chatbots",
    tags: ["multimodal", "coding", "agent", "chinese-model", "open-source"],
    difficulty: "intermediate",
    url: "https://www.minimax.io",
    rating: r(4.5),
    pricing: "Free tier + Paid API",
    useCase: "MiniMax M3 is the first open-source model to combine native multimodality with agent capabilities. It excels at complex 3D coding tasks (Three.js), HTML animation, keyframe extraction, and building custom computer-use agents.",
    icon: "\u{1F30D}",
    company: "MiniMax",
    companyZh: "MiniMax",
    founded: "2021",
    headquarters: "Shanghai, China",
    descriptionLong: "MiniMax M3 is a flagship Chinese AI model that uniquely combines three core capabilities: robust Agent and coding skills, native multimodal understanding (text+vision trained jointly, no external alignment layers), and million-token context handling. It is the first open-source model to integrate all three. In practical benchmarks, M3 matches or exceeds GPT-5.5 on 3D graphics tasks (Three.js maze, pocket watch animation), outperforms Claude Opus 4.8 on keyframe extraction and HTML knowledge graph animation, and successfully builds custom computer-use agents with PyAutoGUI. M3's native multimodality means it learns from text-visual mixed data directly, resulting in precise cross-modal understanding without the information loss typical of vision-encoder-bolted-on architectures. For Agent workflows, M3 can be packaged as a reusable Skill in OpenCode and deployed via MiniMax Code, a desktop client supporting Computer-Use functionality even operable via mobile devices. The API is competitively priced against DeepSeek V4 and GPT-5.5.",
    descriptionLongZh: "MiniMax M3 是一款中国旗舰AI模型，独特地融合了三大核心能力：强大的Agent和编码技能、原生多模态理解（文本+视觉联合训练，无外部对齐层）、以及百万token上下文处理。它是首个集成这三者的开源模型。在实际基准测试中，M3在3D图形任务（Three.js迷宫、怀表动画）上匹敌或超越GPT-5.5，在关键帧提取和HTML知识图谱动画上超越Claude Opus 4.8，并成功用PyAutoGUI构建自定义计算机使用Agent。M3的原生多模态意味着它直接从文本-视觉混合数据中学习，实现精准的跨模态理解，避免了外挂视觉编码器架构常见的信息损失。对于Agent工作流，M3可被包装为OpenCode中的可复用Skill，并通过MiniMax Code桌面客户端部署，支持Computer-Use功能甚至可通过移动设备操作。API定价与DeepSeek V4和GPT-5.5竞争。",
    advantages: ["Native multimodal (no bolt-on encoder)", "Million-token context", "Open-source", "Strong 3D coding & Agent", "Mobile-ready desktop client"],
    advantagesZh: ["原生多模态(非外挂编码器)", "百万token上下文", "开源", "强大的3D编码和Agent", "支持移动端的桌面客户端"],
    useCases: ["3D visualization & animation", "Computer-use agents", "Keyframe extraction", "Multimodal content production", "Vibe coding with zero-code"],
    useCasesZh: ["3D可视化与动画", "计算机使用Agent", "关键帧提取", "多模态内容生产", "零代码Vibe Coding"],
    targetAudience: "Developers and teams building multimodal AI applications, agent enthusiasts, and content creators exploring AI-driven automation.",
    targetAudienceZh: "构建多模态AI应用的开发者和团队、Agent爱好者、以及探索AI驱动自动化的内容创作者。",
    pricingTiers: [
      {tier: "Free", tierZh: "免费版", price: "$0", features: ["Limited API calls", "Web chat access"], featuresZh: ["有限API调用", "Web聊天访问"]},
      {tier: "API", tierZh: "API版", price: "Pay-per-token", features: ["Full model access", "Multimodal inputs", "Million-token context"], featuresZh: ["完整模型访问", "多模态输入", "百万token上下文"]}
    ],
    pros: ["Native multimodal quality", "Competitive with GPT-5.5 on 3D", "Open-source availability", "Computer-use ready"],
    prosZh: ["原生多模态质量", "3D任务匹敌GPT-5.5", "开源可用", "内置Computer-Use"],
    cons: ["Smaller ecosystem than GPT/Claude", "English docs less comprehensive", "Newer model with less community"],
    consZh: ["生态小于GPT/Claude", "英文文档不够全面", "较新模型社区较小"],
    extensions: [
      {name: "MiniMax Code", description: "Desktop client with Computer-Use, domestic Codex alternative", descriptionZh: "桌面客户端支持Computer-Use，国产Codex替代品", url: "https://www.minimax.io/code"},
      {name: "OpenCode Integration", description: "Package M3 as reusable Skill in OpenCode Agent framework", descriptionZh: "在OpenCode Agent框架中打包M3为可复用Skill"}
    ],
    skills: [],
    scene: "development",
  },

"""

last_tool = tools_src.rfind('] as Tool[];')
tools_new = tools_src[:last_tool] + new_tool + '] as Tool[];'

with open('src/lib/tools.ts', 'w', encoding='utf-8') as f:
    f.write(tools_new)

print('Part 1: MiniMax M3 tool added to tools.ts')

# ===== Part 2: Add 2 article metadata to articles.ts =====
with open('src/lib/articles.ts', 'r', encoding='utf-8') as f:
    articles_src = f.read()

new_articles = r"""  {
    slug: "minimax-m3-flagship-multimodal-agent",
    title: "MiniMax M3: The Flagship AI Model Merging Coding, Multimodality, and Agent Capabilities",
    titleZh: "MiniMax M3：融合编程、多模态和Agent能力的旗舰AI模型",
    description: "Hands-on benchmark of MiniMax M3 — the first open-source model combining native multimodality, million-token context, and agent capabilities — tested across 5 scenarios including 3D maze, pocket watch animation, keyframe extraction, and custom computer-use agents.",
    descriptionZh: "MiniMax M3实操评测——首个融合原生多模态、百万token上下文和Agent能力的开源模型——5大场景实测：3D迷宫、怀表拆解动画、关键帧提取、自定义Computer-Use Agent。",
    category: "ai-comparisons",
    tags: ["minimax", "multimodal", "agent", "threejs", "computer-use", "benchmark", "chinese-model"],
    difficulty: "intermediate",
    toolsMentioned: ["minimax-m3", "claude", "deepseek"],
    date: "2026-06-23",
  },
  {
    slug: "github-vibe-coding-backend-workflow",
    title: "GitHub as the Core Backend for Vibe Coding: Full Setup & Collaborative AI Development Workflow",
    titleZh: "GitHub作为Vibe Coding核心后端：完整配置与协作AI开发工作流",
    description: "Complete guide to integrating GitHub as Vibe Coding's backend — PAT setup, repo binding, version-controlled AI code iteration, community template imports, and GitHub Actions CI/CD for auto-deploying AI-generated code.",
    descriptionZh: "将GitHub集成为Vibe Coding后端的完整指南——PAT配置、仓库绑定、版本控制AI代码迭代、社区模板导入、GitHub Actions CI/CD自动部署AI生成代码。",
    category: "ai-tutorials",
    tags: ["github", "vibe-coding", "ci-cd", "version-control", "collaboration", "workflow"],
    difficulty: "beginner",
    toolsMentioned: ["vibecoding", "github-copilot"],
    date: "2026-06-23",
  },

"""

last_bracket = articles_src.rfind('];')
articles_new = articles_src[:last_bracket] + new_articles + '];'

with open('src/lib/articles.ts', 'w', encoding='utf-8') as f:
    f.write(articles_new)

print('Part 2: 2 new articles added to articles.ts')

# ===== Part 3: Add 2 article contents to article-content.ts =====
with open('src/lib/article-content.ts', 'r', encoding='utf-8') as f:
    content_src = f.read()

new_contents = r'''
  "minimax-m3-flagship-multimodal-agent": {
    content: `<div class="meta-banner">
<p><strong>📅 Published:</strong> June 23, 2026 · <strong>🏷️ Category:</strong> AI Comparisons · <strong>📊 Level:</strong> Intermediate · <strong>🛠️ Tools:</strong> MiniMax M3, Claude, DeepSeek, OpenCode</p>
</div>

<p>A truly powerful flagship AI model needs three core capabilities: robust Agent and coding skills, native multimodal understanding, and million-token context handling. MiniMax M3 is the first open-source model to integrate these three "puzzle pieces", revolutionizing how we approach AI-driven workflows — especially when combining multimodality with Agent capabilities to enable AI to actively participate in content production and complex task automation. This article dives into practical tests across five high-difficulty scenarios.</p>

<h2>Test Environment Setup for Fair Comparisons</h2>

<p>To ensure fairness, all models are integrated into the same Agent framework, <strong>OpenCode</strong>, with separate working directories for each. Domestic models (MiniMax M3, DeepSeek V4 Pro, etc.) are connected via official subscriptions, while overseas models (Claude Sonnet 4.6, GPT 5.5, etc.) use OpenRouter.</p>

<h2>Scenario 1: 3D Maze Navigation with Three.js</h2>

<p>This test evaluates maze generation, physics simulation, spatial reasoning, and camera control using Three.js:</p>

<pre><code class="language-text">Create a 3D maze with a moving ball using Three.js. All code in one HTML file. The maze must be complex and interactive (drag/scroll to adjust view).</code></pre>

<ul>
<li><strong>Claude Sonnet 4.6:</strong> Fails due to insufficient context in both OpenCode and Claude Code.</li>
<li><strong>Claude Opus 4.8:</strong> Visually decent but has reversed left/right key controls.</li>
<li><strong>LMA 5.1:</strong> The ball gets stuck immediately.</li>
<li><strong>K2.6:</strong> Physics issues — erratic ball movement and excessive bouncing.</li>
<li><strong>DeepSeek V4 Pro:</strong> Slow movement and confused key controls.</li>
<li><strong>MiniMax M3 (Best Among Domestic Models):</strong> Clean scene, proper controls, and camera adjustments. Minor issue: reversed keys when the camera rotates 90°.</li>
<li><strong>GPT 5.5 (Overall Best):</strong> No major flaws, smooth interaction.</li>
</ul>

<h2>Scenario 2: 3D Pocket Watch Disassembly Animation</h2>

<p>This tests the model's ability to create complex 3D models and animations:</p>

<ul>
<li><strong>GPT 5.5 & MiniMax M3:</strong> Top performers with aesthetically pleasing dials and smooth disassembly animations, resembling professional product demos.</li>
<li><strong>DeepSeek V4 Pro:</strong> Solid performance among domestic models.</li>
<li><strong>Claude Series:</strong> Severe failures — Sonnet 4.6 produces an unrecognizable shape, and Opus 4.8 has reversed needle directions.</li>
</ul>

<h2>Scenario 3: HTML Animation for Step-by-Step Knowledge Graphs</h2>

<p>Convert an infographic into a step-by-step HTML animation to sync with video explanations:</p>

<pre><code class="language-text">Split the infographic into sections, mask them, and reveal each section sequentially as per the narration. Output an HTML PPT.</code></pre>

<ul>
<li><strong>Q 3.6 Plus:</strong> Fails to mask; redraws the image in HTML poorly.</li>
<li><strong>K2.6:</strong> Fixed mask positions with illogical reveal order.</li>
<li><strong>Claude Opus 4.8 & GPT 5.5:</strong> Masks are too noticeable, distracting viewers.</li>
<li><strong>MiniMax M3 & Claude Sonnet 4.6:</strong> Use background-matching masks. MiniMax M3's region division is the most logical, delivering the best result.</li>
</ul>

<h2>Scenario 4: Keyframe Extraction from Animated Videos</h2>

<p>Extract precise keyframes from a fast-paced animation (each keyframe window is only 0.1 seconds):</p>

<ul>
<li><strong>Q 3.6 Plus:</strong> Insufficient and inaccurately timed screenshots.</li>
<li><strong>K2.6, Claude Sonnet 4.6, Claude Opus 4.8:</strong> Decent completion but with minor motion blur.</li>
<li><strong>MiniMax M3 & GPT 5.5 (Top Performers):</strong> MiniMax M3 uses a two-step process — rough screenshotting to locate key moments, then fine-grained sampling to pick the perfect frame. Results are sharp with no blur. GPT 5.5 generates a frame gallery first, then selects the best frame.</li>
</ul>

<h2>Scenario 5: Building a Custom Computer-Use Agent</h2>

<p>Create an Agent to control the computer via PyAutoGUI and MSS:</p>

<pre><code class="language-text">Build an Agent with mss and pyautogui to control the computer. It should take a task, screenshot, think, act, and repeat until completion.</code></pre>

<p>MiniMax M3 generates the Agent code. Testing the task "Open Chrome and search for MiniMax M3's latest model features": M3 opens Chrome, locates the search bar, inputs the query, expands "More Results" for deeper info, and outputs a precise summary — all without unnecessary actions.</p>

<p>We then package this Agent as a <strong>reusable Skill</strong> in OpenCode. Testing "Upload this project to GitHub via VS Code": the Agent completes the process step-by-step, successfully uploading the project.</p>

<p>Alternatively, use MiniMax's desktop client, <strong>MiniMax Code</strong> (a domestic alternative to Codex), which natively supports Computer-Use functionality — even operable via mobile devices.</p>

<h2>Why MiniMax M3 Stands Out</h2>

<ul>
<li><strong>Coding & Agent Abilities:</strong> Handles complex programming tasks and automates workflows.</li>
<li><strong>Native Multimodality:</strong> Learns from text-visual mixed data natively (no reliance on external encoding/alignment layers), ensuring precise cross-modal understanding.</li>
<li><strong>Million-Token Context:</strong> Maintains coherence over extremely long inputs.</li>
</ul>

<p>It's ideal for teams building multimodal automated workflows, Agent enthusiasts, and content creators exploring AI-driven "vibe coding" with zero-code experience.</p>

<h2>常见问题</h2>

<h3>How does MiniMax M3's native multimodality differ from GPT-4o or Gemini?</h3>
<p>Most multimodal models bolt a vision encoder onto a text LLM and align them through training. MiniMax M3 is trained on text-visual mixed data from the start — there's no separate encoder to align. This means less information loss when reasoning across modalities. In practice, M3 excels at tasks requiring precise spatial understanding (like the pocket watch animation where gear positions must be exact), while bolt-on architectures sometimes misalign visual and textual reasoning.</p>

<h3>Can MiniMax M3 replace Claude Code or Codex for coding tasks?</h3>
<p>For 3D graphics, animation, and multimodal coding tasks, M3 is genuinely competitive — often beating Claude Opus 4.8. For pure backend logic or text-only coding, GPT-5.5 and Claude Opus 4.8 still hold an edge. The best strategy is using M3 for multimodal-heavy tasks and your preferred coding model for everything else. M3's strength is the multimodal+agent combo, not raw text coding.</p>

<h3>Is MiniMax Code a full Codex replacement?</h3>
<p>MiniMax Code is positioned as a domestic Codex alternative with native Computer-Use support. It can control your desktop, browse the web, and execute tasks — all operable from mobile. While its plugin ecosystem is smaller than Codex's, the core Computer-Use functionality is production-ready and uniquely accessible via mobile.</p>

<div class="next-step">
<p><strong>下一篇：</strong> <a href="/en/article/github-vibe-coding-backend-workflow">GitHub as the Core Backend for Vibe Coding: Full Setup & Collaborative AI Workflow →</a></p>
</div>`,
    contentZh: `<div class="meta-banner">
<p><strong>📅 发布日期：</strong>2026年6月23日 · <strong>🏷️ 分类：</strong>AI对比 · <strong>📊 难度：</strong>中级 · <strong>🛠️ 工具：</strong>MiniMax M3、Claude、DeepSeek、OpenCode</p>
</div>

<p>一款真正强大的旗舰AI模型需要三大核心能力：强大的Agent和编码技能、原生多模态理解、以及百万token上下文处理。MiniMax M3是首个将这三块"拼图"整合在一起的开源模型，彻底改变了我们处理AI驱动工作流的方式——尤其是将多模态与Agent能力结合，让AI主动参与内容生产和复杂任务自动化。本文深入实测五大高难度场景。</p>

<h2>公平对比的测试环境搭建</h2>

<p>为确保公平，所有模型集成到同一Agent框架<strong>OpenCode</strong>中，各模型使用独立工作目录。国内模型（MiniMax M3、DeepSeek V4 Pro等）通过官方订阅连接，海外模型（Claude Sonnet 4.6、GPT 5.5等）使用OpenRouter。</p>

<h2>场景1：Three.js 3D迷宫导航</h2>

<p>此测试评估使用Three.js的迷宫生成、物理模拟、空间推理和相机控制：</p>

<pre><code class="language-text">使用Three.js创建一个带移动球的3D迷宫。所有代码在一个HTML文件中。迷宫必须复杂且可交互（拖拽/滚轮调整视角）。</code></pre>

<ul>
<li><strong>Claude Sonnet 4.6：</strong>因上下文不足在OpenCode和Claude Code中均失败。</li>
<li><strong>Claude Opus 4.8：</strong>视觉效果尚可但左右键控制反转。</li>
<li><strong>LMA 5.1：</strong>球立即卡住。</li>
<li><strong>K2.6：</strong>物理问题——球运动不稳定、过度弹跳。</li>
<li><strong>DeepSeek V4 Pro：</strong>移动缓慢、按键控制混乱。</li>
<li><strong>MiniMax M3（国产最佳）：</strong>场景清晰、控制正确、相机调整正常。小问题：相机旋转90°后按键反转。</li>
<li><strong>GPT 5.5（全场最佳）：</strong>无明显缺陷，交互流畅。</li>
</ul>

<h2>场景2：3D怀表拆解动画</h2>

<p>测试模型创建复杂3D模型和动画的能力：</p>

<ul>
<li><strong>GPT 5.5 & MiniMax M3：</strong>表现最佳，表盘美观、拆解动画流畅，类似专业产品演示。</li>
<li><strong>DeepSeek V4 Pro：</strong>国产品牌中表现扎实。</li>
<li><strong>Claude系列：</strong>严重失败——Sonnet 4.6生成不可辨认的形状，Opus 4.8指针方向反转。</li>
</ul>

<h2>场景3：分步知识图谱HTML动画</h2>

<p>将信息图转换为分步HTML动画，与视频解说同步：</p>

<pre><code class="language-text">将信息图分割为多个区域，遮罩后按解说顺序逐步展示。输出HTML PPT。</code></pre>

<ul>
<li><strong>Q 3.6 Plus：</strong>无法遮罩；用HTML重绘图片效果差。</li>
<li><strong>K2.6：</strong>固定遮罩位置，展示顺序不合理。</li>
<li><strong>Claude Opus 4.8 & GPT 5.5：</strong>遮罩过于明显，分散注意力。</li>
<li><strong>MiniMax M3 & Claude Sonnet 4.6：</strong>使用背景匹配遮罩。MiniMax M3的区域划分最合理，效果最佳。</li>
</ul>

<h2>场景4：动画视频关键帧提取</h2>

<p>从快节奏动画中提取精确关键帧（每个关键帧窗口仅0.1秒）：</p>

<ul>
<li><strong>Q 3.6 Plus：</strong>截图数量不足且时间不准确。</li>
<li><strong>K2.6、Claude Sonnet 4.6、Claude Opus 4.8：</strong>完成度尚可但截图有轻微运动模糊。</li>
<li><strong>MiniMax M3 & GPT 5.5（最佳表现）：</strong>MiniMax M3采用两步流程——粗略截图定位关键时刻，然后细粒度采样选出完美帧。结果清晰无模糊。GPT 5.5先生成帧图库再选最佳帧。</li>
</ul>

<h2>场景5：构建自定义Computer-Use Agent</h2>

<p>创建通过PyAutoGUI和MSS控制电脑的Agent：</p>

<pre><code class="language-text">用mss和pyautogui构建一个Agent控制电脑。它应接受任务、截图、思考、行动、循环直到完成。</code></pre>

<p>MiniMax M3生成Agent代码。测试任务"打开Chrome搜索MiniMax M3最新模型特性"：M3打开Chrome、定位搜索栏、输入查询、展开"更多结果"获取深度信息、输出精准摘要——全程无多余动作。</p>

<p>随后将此Agent打包为OpenCode中的<strong>可复用Skill</strong>。测试"通过VS Code将项目上传GitHub"：Agent逐步完成流程，成功上传项目。</p>

<p>或者使用MiniMax桌面客户端<strong>MiniMax Code</strong>（国产Codex替代品），原生支持Computer-Use功能——甚至可通过手机操作。</p>

<h2>MiniMax M3为何出众</h2>

<ul>
<li><strong>编码与Agent能力：</strong>处理复杂编程任务并自动化工作流。</li>
<li><strong>原生多模态：</strong>从文本-视觉混合数据中原生学习（不依赖外部编码/对齐层），确保精准的跨模态理解。</li>
<li><strong>百万Token上下文：</strong>在超长输入上保持连贯性。</li>
</ul>

<p>适合构建多模态自动化工作流的团队、Agent爱好者、以及探索AI驱动"Vibe Coding"零代码体验的内容创作者。</p>

<h2>常见问题</h2>

<h3>MiniMax M3的原生多模态与GPT-4o或Gemini有何不同？</h3>
<p>大多数多模态模型是将视觉编码器外挂到文本LLM上通过训练对齐。MiniMax M3从一开始就用文本-视觉混合数据训练——没有独立编码器需要对齐。这意味着跨模态推理时信息损失更少。实践中，M3在需要精确空间理解的任务上表现优异（如怀表动画中齿轮位置必须精确），而外挂架构有时会错配视觉和文本推理。</p>

<h3>MiniMax M3能替代Claude Code或Codex做编码任务吗？</h3>
<p>在3D图形、动画和多模态编码任务上，M3真正有竞争力——经常击败Claude Opus 4.8。纯后端逻辑或纯文本编码方面，GPT 5.5和Claude Opus 4.8仍占优势。最佳策略是用M3处理多模态密集型任务，其他任务用你偏好的编码模型。M3的强项是多模态+Agent组合，而非纯文本编码。</p>

<h3>MiniMax Code是Codex的完整替代品吗？</h3>
<p>MiniMax Code定位为国产Codex替代品，原生支持Computer-Use。它能控制桌面、浏览网页、执行任务——全部可从手机操作。虽然插件生态小于Codex，但核心Computer-Use功能已可生产使用，且独特的移动端可操作性是其亮点。</p>

<div class="next-step">
<p><strong>下一篇：</strong> <a href="/zh/article/github-vibe-coding-backend-workflow">GitHub作为Vibe Coding核心后端：完整配置与协作AI开发工作流 →</a></p>
</div>`,
  },

  "github-vibe-coding-backend-workflow": {
    content: `<div class="meta-banner">
<p><strong>📅 Published:</strong> June 23, 2026 · <strong>🏷️ Category:</strong> AI Tutorials · <strong>📊 Level:</strong> Beginner · <strong>🛠️ Tools:</strong> Vibe Coding, GitHub, GitHub Actions</p>
</div>

<p>Vibe Coding has rapidly evolved from a standalone local AI coding tool into a community-driven development framework, with GitHub officially becoming its primary backend storage and collaboration hub. Many beginner developers only use Vibe Coding for local script generation but ignore GitHub integration, which locks them out of version rollback, team co-development, community template sharing, and automated cloud execution. This practical guide walks you through linking Vibe Coding with GitHub repositories, configuring access credentials, syncing project snapshots, and leveraging community open-source templates to boost development efficiency.</p>

<h2>Why GitHub Is Mandatory for Professional Vibe Coding Workflows</h2>

<p>Local-only Vibe Coding usage carries obvious limitations for long-term projects: local file corruption, lost AI generation history, inability to revert bad AI code iterations, and no way to reuse public community workflow templates. GitHub integration resolves these pain points:</p>

<ol>
<li>Persistent storage for all AI-generated code iterations with full commit history</li>
<li>One-click rollback to stable versions when Vibe Coding outputs broken logic</li>
<li>Import ready-made community Vibe Coding task templates (API scaffolding, frontend boilerplate, test suites)</li>
<li>Collaborative editing where multiple AI agents or human developers modify the same project</li>
<li>Trigger automated builds via GitHub Actions after Vibe Coding completes code writing</li>
</ol>

<h2>Step 1: Prepare GitHub Personal Access Token</h2>

<p>Vibe Coding requires a PAT (Personal Access Token) to read/write repository content securely; password login is no longer supported by GitHub's API rules.</p>

<ol>
<li>Navigate to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)</li>
<li>Create a new token with these permission scopes: <code>repo</code>, <code>workflow</code>, <code>gist</code></li>
<li>Set an expiration date matching your project cycle, generate the token, and copy it immediately (GitHub only displays it once)</li>
</ol>

<p>Store the token locally in your Vibe Coding config file:</p>

<pre><code class="language-json">// vibe-coding-config.json
{
  "github_auth": {
    "username": "your-github-username",
    "personal_access_token": "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "default_branch": "main"
  }
}</code></pre>

<h2>Step 2: Initialize Vibe Coding Project and Bind Remote GitHub Repository</h2>

<h3>2.1 Local Project Initialization</h3>

<pre><code class="language-bash">mkdir vibe-coding-ai-project
cd vibe-coding-ai-project
git init</code></pre>

<h3>2.2 Create Empty Remote Repo & Link Origin</h3>

<p>Create a new public/private repository on GitHub without initializing README or LICENSE files, then link the remote address locally:</p>

<pre><code class="language-bash">git remote add origin https://github.com/your-github-username/vibe-coding-ai-project.git</code></pre>

<h3>2.3 Connect Repository Inside Vibe Coding Client</h3>

<p>Launch the Vibe Coding desktop client, open Settings → Cloud Sync → GitHub Sync, paste your PAT and select the bound repository. Enable auto-sync to push code once AI generation finishes.</p>

<h2>Step 3: Standard Workflow — AI Code Generation + GitHub Version Control</h2>

<p>This standardized workflow ensures every piece of AI-generated code is tracked and reversible:</p>

<ol>
<li>Submit development requirements to Vibe Coding (e.g., build a Node.js file upload API with error handling)</li>
<li>After Vibe Coding outputs complete functional code, verify local runtime:</li>
</ol>

<pre><code class="language-bash"># Test Node.js project generated by Vibe Coding
npm install
node server.js</code></pre>

<ol start="3">
<li>Stage, commit and push qualified code with descriptive commit messages:</li>
</ol>

<pre><code class="language-bash">git add .
git commit -m "VibeCoding Iter 1: Complete file upload API with validation middleware"
git push origin main</code></pre>

<ol start="4">
<li>If AI code contains critical bugs, roll back to the last stable commit:</li>
</ol>

<pre><code class="language-bash"># Terminal rollback command for faulty AI commits
git reset --hard HEAD~1
git push origin main --force-with-lease</code></pre>

<h2>Step 4: Import Community Open-Source Vibe Coding Templates</h2>

<p>The biggest benefit of GitHub as Vibe Coding's backend is access to thousands of community-contributed pre-built templates.</p>

<ol>
<li>Search GitHub with keyword <code>vibe-coding-template</code> to filter high-star official and community repositories</li>
<li>Clone the template repository locally and import it directly into Vibe Coding:</li>
</ol>

<pre><code class="language-bash">git clone https://github.com/community-author/vibe-coding-react-starter.git
cd vibe-coding-react-starter</code></pre>

<ol start="3">
<li>Reload the project in Vibe Coding; the pre-configured prompt rules, build scripts and lint settings will load automatically, eliminating repetitive foundational configuration work.</li>
</ol>

<h2>Step 5: Automate Post-Generation Deployment with GitHub Actions</h2>

<p>Configure a simple CI/CD workflow to auto-test and deploy code right after Vibe Coding pushes new commits:</p>

<pre><code class="language-yaml">name: Vibe Coding Auto Deploy
on: push
  branches: [ main ]
jobs:
  build-and-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 20
      - name: Install Dependencies & Test AI Code
        run: |
          npm install
          npm run test
      - name: Deploy if tests pass
        run: echo "Vibe Coding project deployed successfully"</code></pre>

<p>Once saved and pushed, every new Vibe Coding code submission triggers automated testing to prevent unqualified code from going live.</p>

<h2>Critical Best Practices & Risk Avoidance</h2>

<ol>
<li><strong>Never hardcode GitHub PAT</strong> directly inside AI-generated source files; always store tokens in local private config files added to <code>.gitignore</code>:</li>
</ol>

<pre><code class="language-gitignore"># .gitignore mandatory entry
vibe-coding-config.json
.env</code></pre>

<ol start="2">
<li><strong>Separate experimental AI branches</strong> from the main production branch: test risky Vibe Coding prompts on <code>dev</code> branch before merging</li>
<li><strong>Limit PAT permissions</strong> to only required scopes to reduce security risks if credentials leak</li>
<li><strong>Label each commit</strong> with iteration numbers to distinguish different Vibe Coding prompt outputs for easy tracing</li>
</ol>

<h2>常见问题</h2>

<h3>Can I use Vibe Coding with GitHub without a paid plan?</h3>
<p>Yes. GitHub's free tier includes unlimited public/private repositories, 2,000 GitHub Actions minutes/month, and full API access — more than enough for individual Vibe Coding workflows. You only need a paid plan if you exceed the free tier's CI/CD minutes or need advanced features like protected branches and required reviewers.</p>

<h3>What happens if Vibe Coding generates broken code — can I recover?</h3>
<p>That's exactly why GitHub integration matters. Every AI generation iteration is a Git commit. If the latest output breaks your project, simply run <code>git reset --hard HEAD~1</code> to instantly revert to the last working version. Without GitHub, you'd have no undo mechanism beyond manual file restoration.</p>

<h3>How do I collaborate with teammates using Vibe Coding + GitHub?</h3>
<p>Each teammate clones the same GitHub repository, connects it to their Vibe Coding client, and works on separate branches. Use pull requests to review AI-generated code before merging into main. This is identical to standard Git collaboration — the only difference is that some commits are authored by AI rather than humans.</p>

<div class="next-step">
<p><strong>Previous:</strong> <a href="/en/article/minimax-m3-flagship-multimodal-agent">MiniMax M3: The Flagship AI Model Merging Coding, Multimodality, and Agent Capabilities ←</a></p>
</div>`,
    contentZh: `<div class="meta-banner">
<p><strong>📅 发布日期：</strong>2026年6月23日 · <strong>🏷️ 分类：</strong>AI教程 · <strong>📊 难度：</strong>初级 · <strong>🛠️ 工具：</strong>Vibe Coding、GitHub、GitHub Actions</p>
</div>

<p>Vibe Coding已从独立的本地AI编码工具迅速演变为社区驱动的开发框架，GitHub正式成为其主要后端存储和协作中心。许多初学者开发者只用Vibe Coding做本地脚本生成，却忽略了GitHub集成，导致无法版本回滚、团队协作、社区模板共享和自动化云端执行。本实操指南带你完成Vibe Coding与GitHub仓库的连接、配置访问凭证、同步项目快照、并利用社区开源模板提升开发效率。</p>

<h2>为什么GitHub是专业Vibe Coding工作流的必需品</h2>

<p>纯本地使用Vibe Coding对长期项目有明显局限：本地文件损坏、AI生成历史丢失、无法回退AI的错误代码迭代、无法复用公共社区工作流模板。GitHub集成解决了这些痛点：</p>

<ol>
<li>所有AI生成代码迭代的持久存储及完整提交历史</li>
<li>Vibe Coding输出错误逻辑时一键回滚到稳定版本</li>
<li>导入现成的社区Vibe Coding任务模板（API脚手架、前端样板、测试套件）</li>
<li>多个AI代理或人类开发者协同编辑同一项目</li>
<li>Vibe Coding完成代码编写后通过GitHub Actions触发自动化构建</li>
</ol>

<h2>步骤1：准备GitHub Personal Access Token</h2>

<p>Vibe Coding需要PAT（Personal Access Token）安全读写仓库内容；GitHub API规则已不再支持密码登录。</p>

<ol>
<li>导航到GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)</li>
<li>创建新Token并启用权限范围：<code>repo</code>、<code>workflow</code>、<code>gist</code></li>
<li>设置与项目周期匹配的过期时间，生成Token并立即复制（GitHub仅显示一次）</li>
</ol>

<p>将Token存储在本地Vibe Coding配置文件中：</p>

<pre><code class="language-json">// vibe-coding-config.json
{
  "github_auth": {
    "username": "your-github-username",
    "personal_access_token": "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "default_branch": "main"
  }
}</code></pre>

<h2>步骤2：初始化Vibe Coding项目并绑定远程GitHub仓库</h2>

<h3>2.1 本地项目初始化</h3>

<pre><code class="language-bash">mkdir vibe-coding-ai-project
cd vibe-coding-ai-project
git init</code></pre>

<h3>2.2 创建空远程仓库并关联</h3>

<p>在GitHub上创建新仓库（不初始化README或LICENSE），然后本地关联远程地址：</p>

<pre><code class="language-bash">git remote add origin https://github.com/your-github-username/vibe-coding-ai-project.git</code></pre>

<h3>2.3 在Vibe Coding客户端内连接仓库</h3>

<p>启动Vibe Coding桌面客户端，打开Settings → Cloud Sync → GitHub Sync，粘贴PAT并选择绑定的仓库。启用自动同步，AI生成完成后自动推送代码。</p>

<h2>步骤3：标准工作流——AI代码生成+GitHub版本控制</h2>

<p>此标准化工作流确保每段AI生成的代码都被追踪且可逆：</p>

<ol>
<li>向Vibe Coding提交开发需求（如构建带错误处理的Node.js文件上传API）</li>
<li>Vibe Coding输出完整功能代码后，本地验证运行：</li>
</ol>

<pre><code class="language-bash"># 测试Vibe Coding生成的Node.js项目
npm install
node server.js</code></pre>

<ol start="3">
<li>暂存、提交并推送合格代码，附带描述性提交信息：</li>
</ol>

<pre><code class="language-bash">git add .
git commit -m "VibeCoding Iter 1: 完成带验证中间件的文件上传API"
git push origin main</code></pre>

<ol start="4">
<li>如果AI代码有严重Bug，直接在Vibe Coding的GitHub面板回滚到上次稳定提交：</li>
</ol>

<pre><code class="language-bash"># 终端回滚错误AI提交
git reset --hard HEAD~1
git push origin main --force-with-lease</code></pre>

<h2>步骤4：从GitHub导入社区开源Vibe Coding模板</h2>

<p>GitHub作为Vibe Coding后端最大的好处是能访问数千个社区贡献的预构建模板。</p>

<ol>
<li>在GitHub搜索关键词<code>vibe-coding-template</code>筛选高星官方和社区仓库</li>
<li>克隆模板仓库到本地并直接导入Vibe Coding：</li>
</ol>

<pre><code class="language-bash">git clone https://github.com/community-author/vibe-coding-react-starter.git
cd vibe-coding-react-starter</code></pre>

<ol start="3">
<li>在Vibe Coding中重新加载项目；预配置的提示规则、构建脚本和lint设置将自动加载，省去重复的基础配置工作。</li>
</ol>

<h2>步骤5：用GitHub Actions自动化部署AI生成代码</h2>

<p>配置简单CI/CD工作流，在Vibe Coding推送新提交后自动测试和部署代码：</p>

<pre><code class="language-yaml">name: Vibe Coding自动部署
on: push
  branches: [ main ]
jobs:
  build-and-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: 安装Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 20
      - name: 安装依赖并测试AI代码
        run: |
          npm install
          npm run test
      - name: 测试通过则部署
        run: echo "Vibe Coding项目部署成功"</code></pre>

<p>保存并推送后，每次Vibe Coding新代码提交都会触发自动化测试，防止不合格代码上线。</p>

<h2>关键最佳实践与风险规避</h2>

<ol>
<li><strong>绝不在AI生成的源文件中硬编码GitHub PAT</strong>；始终将Token存储在添加到<code>.gitignore</code>的本地私有配置文件中：</li>
</ol>

<pre><code class="language-gitignore"># .gitignore必加条目
vibe-coding-config.json
.env</code></pre>

<ol start="2">
<li><strong>将实验性AI分支与主生产分支分离</strong>：在<code>dev</code>分支上测试高风险的Vibe Coding提示，再合并</li>
<li><strong>限制PAT权限</strong>仅必要范围，降低凭证泄露时的安全风险</li>
<li><strong>每次提交标注迭代编号</strong>，区分不同Vibe Coding提示输出，便于追溯</li>
</ol>

<h2>常见问题</h2>

<h3>Vibe Coding配合GitHub需要付费吗？</h3>
<p>不需要。GitHub免费版包含无限公开/私有仓库、每月2,000分钟GitHub Actions、完整API访问——对个人Vibe Coding工作流绰绰有余。只有超出免费CI/CD分钟数或需要受保护分支、必须审阅者等高级功能时才需付费。</p>

<h3>Vibe Coding生成错误代码怎么办——能恢复吗？</h3>
<p>这正是GitHub集成的意义所在。每次AI生成迭代都是一个Git提交。如果最新输出破坏了项目，只需<code>git reset --hard HEAD~1</code>即刻回滚到上一个可用版本。没有GitHub，除了手动恢复文件外没有撤销机制。</p>

<h3>如何与团队成员用Vibe Coding+GitHub协作？</h3>
<p>每个成员克隆同一个GitHub仓库，连接到自己的Vibe Coding客户端，在各自分支上工作。用Pull Request审查AI生成代码后再合并到main。这与标准Git协作完全相同——唯一区别是部分提交由AI而非人类创作。</p>

<div class="next-step">
<p><strong>上一篇：</strong> <a href="/zh/article/minimax-m3-flagship-multimodal-agent">MiniMax M3：融合编程、多模态和Agent能力的旗舰AI模型 ←</a></p>
</div>`,
  },

'''

last_brace = content_src.rfind('};')
content_new = content_src[:last_brace] + new_contents + '};'

with open('src/lib/article-content.ts', 'w', encoding='utf-8') as f:
    f.write(content_new)

print('Part 3: 2 article contents added to article-content.ts')

print('\n=== All done! Run build to verify ===')
