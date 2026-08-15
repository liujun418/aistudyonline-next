"""Publish Aug 15, 2026 — 1 article + 1 new tool (TraeWork)."""
import os; BASE = r"C:\Users\jun\aistudyonline-next"; os.chdir(BASE)

# ---------- Part 1: articles.ts metadata ----------
with open('src/lib/articles.ts', 'r', encoding='utf-8') as f: s = f.read()
a = r"""  {
    slug: "mastering-ai-powered-content-creation-complete-traework-workflow-tutorial",
    title: "Mastering AI-Powered Content Creation: A Complete TraeWork Workflow Tutorial",
    titleZh: "掌握AI内容创作：TraeWork完整工作流教程",
    description: "A complete step-by-step TraeWork workflow for AI content creation — from research and ranking in Work mode, syncing to Feishu, visual design in Design mode, interactive demos in Code mode, and Seedream AI covers, to weekly automated monitoring.",
    descriptionZh: "用TraeWork完成AI内容创作的完整分步工作流——从Work模式研究筛选、飞书文档同步、Design模式视觉设计、Code模式交互演示、Seedream AI封面，到每周自动化监控的全流程教程。",
    category: "ai-tutorials",
    tags: ["TraeWork", "AI Content Creation", "Workflow", "Feishu", "Seedream", "GitHub", "Automation"],
    difficulty: "beginner",
    toolsMentioned: ["TraeWork"],
    date: "2026-08-15",
  },

"""
last = s.rfind('];')
with open('src/lib/articles.ts', 'w', encoding='utf-8') as f: f.write(s[:last] + a + '];')
print('Part 1 done')

# ---------- Part 2: article-content.ts bilingual content ----------
with open('src/lib/article-content.ts', 'r', encoding='utf-8') as f: c = f.read()
n = r'''
  "mastering-ai-powered-content-creation-complete-traework-workflow-tutorial": {
    content: `<div class="meta-banner">
  <span class="meta-badge">📖 AI Tutorial</span>
  <span class="meta-badge">🕒 8 min read</span>
  <span class="meta-badge">📅 Aug 15, 2026</span>
  <span class="meta-badge">🎯 Beginner</span>
</div>

<h2 id="introduction">Introduction</h2>
<p>Creating high-quality AI content doesn't have to be complicated. With TraeWork, you can handle the entire process from research to final production in a single platform. This guide walks you through every step, using the example of creating a video about "5 Worth-Recommending AI Open Source Projects."</p>

<h2 id="step-1">Step 1: Project Planning & Research in Work Mode</h2>
<p>The process starts with the Work mode, designed for professional office tasks like research and analysis.</p>
<ol>
  <li><strong>Enter Work Mode</strong>: Click the "Work" tab in the top-left corner.</li>
  <li><strong>Define Your Goal</strong>: Input your task clearly. For our example, use this prompt:</li>
</ol>
<pre><code class="language-text">I want to create a video titled "5 Worth-Recommending AI Open Source Projects."
Please research recent AI open source projects on GitHub Trending, focusing on projects that have emerged recently or have been active in the past 90 days.
Summarize 20-30 candidate projects, including project name, GitHub link, category, core use case, star count, latest update, release date, project activity, key highlights, known issues, and information sources.</code></pre>
<ol start="3">
  <li><strong>Wait for Results</strong>: TraeWork will use its research and data processing skills to search the web, read project files, and compile a detailed list of candidates.</li>
</ol>

<h2 id="step-2">Step 2: Project Ranking & Selection</h2>
<p>Once you have the candidate list, use Work mode again to rank the projects:</p>
<ol>
  <li><strong>Submit Ranking Request</strong>: Use this prompt to evaluate the candidates:</li>
</ol>
<pre><code class="language-text">Please rank these 20 candidate projects based on practical value, project activity, innovation, audience appeal, video presentation effectiveness, and project uniqueness.
Include scores for each dimension, an overall ranking, recommendations, and main risks.</code></pre>
<ol start="2">
  <li><strong>Select Final Projects</strong>: From the ranked list, choose the top 5 projects that best fit your video theme.</li>
</ol>

<h2 id="step-3">Step 3: Sync to Feishu Document</h2>
<p>TraeWork integrates with Feishu to keep your work organized:</p>
<ol>
  <li><strong>Open Plugin Market</strong>: Click "Plugin Market" in the left sidebar.</li>
  <li><strong>Add Feishu Plugin</strong>: Find and add the Feishu plugin.</li>
  <li><strong>Sync Data</strong>: In the chat box, click the Feishu icon and use this prompt:</li>
</ol>
<pre><code class="language-text">Please verify the final 5 projects, organize their core functions, recommendations, use cases, limitations, and official sources, and create a clear video outline in a new Feishu document.</code></pre>

<h2 id="step-4">Step 4: Visual Design in Design Mode</h2>
<p>Now move to Design mode to create visual assets for your video:</p>
<ol>
  <li><strong>Enter Design Mode</strong>: Click the "Design" tab.</li>
  <li><strong>Generate Visual Concepts</strong>: Use this prompt to create design options:</li>
</ol>
<pre><code class="language-text">Read the Feishu document with the video outline and 5 project details.
Design a unified visual system for the video "5 Worth-Recommending AI Open Source Projects."
The 5 projects and their themes are:
- Agent Reach: Agent Networking
- Reasonix: AI Programming
- SkillSpector: Agent Security
- Headroom: Context Compression
- DeepTutor: AI Education
Provide 3 distinct visual directions, including:
1. Video main cover
2. Introduction cards for the 5 projects
3. Video section pages
Visual requirements:
- Rich colors
- Large, clear title text (no compression)
- Reserve space for the host in the bottom-left of the main cover
- Consistent style with unique elements for each project
- Main cover text: "5 GitHub AI Open Source Projects"</code></pre>
<ol start="3">
  <li><strong>Choose Design</strong>: Select your preferred design direction and have TraeWork add the design specifications to your Feishu document.</li>
</ol>

<h2 id="step-5">Step 5: Create Interactive Video Materials in Code Mode</h2>
<p>Use Code mode to generate dynamic video materials:</p>
<ol>
  <li><strong>Enter Code Mode</strong>: Click the "Code" tab.</li>
  <li><strong>Generate Interactive Demo</strong>: Use this prompt to create your video materials:</li>
</ol>
<pre><code class="language-text">Read the Feishu project document.
Based on the confirmed video outline, 5 project details, and design specifications, create an interactive web demo suitable for screen recording.
The pages should include:
- Opening overview page
- Pages for each of the 5 projects
- Summary page
Requirements:
- Follow the design specifications for fonts, colors, and layout
- Support mouse clicks and keyboard navigation between sections
- Animate titles, project cards, and key information in sequence
- Clean, professional animations without excessive effects
- All text and visual elements must be accurate
- Page resolution: 1920x1080</code></pre>
<ol start="3">
  <li><strong>Use the Output</strong>: The generated HTML demo maintains your design style and includes all the information from your research, ready for screen recording.</li>
</ol>

<h2 id="step-6">Step 6: Generate Video Cover with Seedream AI</h2>
<p>Create eye-catching video covers using the Seedream AI image generation feature:</p>
<ol>
  <li><strong>Access Seedream</strong>: Go to the Plugin Market, click "Skills," search for "seed," and add the Seedream image generation skill.</li>
  <li><strong>Generate Covers</strong>: Use this prompt (you can also upload a reference photo):</li>
</ol>
<pre><code class="language-text">Generate 3-4 video covers for the topic "5 Worth-Recommending GitHub AI Open Source Projects."
Requirements:
1. Character consistency: Ensure the person in the image has the same face, glasses, hairstyle, clothing, and age.
2. Host expression: Expressive body language, hand gestures, wide-angle shot, close-up.
3. Main title: Large, bold, high-contrast text (6-10 characters, title takes up ~40% of the visual width).
4. Visual focus: One main focus point (face/main title/foreground elements/comparison cards), other elements serve it.
5. Information hierarchy: Clear sections (original/edited image, main title, scene, poster/thumbnail, foreground elements, host information, background, negative space).
6. Color scheme: Black, white, yellow, red with small red/blue accents. High contrast, strong visual impact.
7. Restrictions: No messy code, logos, watermarks, extra text, distorted characters, empty background, or randomly floating elements.</code></pre>
<ol start="3">
  <li><strong>Finalize</strong>: Select the best cover, make minor text adjustments if needed, and you're ready to record your video.</li>
</ol>

<h2 id="step-7">Step 7: Automate Future Tasks</h2>
<p>To stay updated on new AI projects without manual work:</p>
<ol>
  <li><strong>Create Automation Task</strong>: Click "Automation" in the left sidebar.</li>
  <li><strong>Configure Task</strong>: Create a new task with these settings:</li>
</ol>
<ul>
  <li>Task name: "Weekly GitHub AI Open Source Project Monitoring"</li>
  <li>Schedule: Weekly at 08:00</li>
  <li>Task description:</li>
</ul>
<pre><code class="language-text">Research new or trending AI open source projects on GitHub from the past week.
Focus on practical value, innovation, activity, audience appeal, and video presentation effectiveness.
Exclude projects that haven't been updated recently or have no practical application.
Finally, select the 10 most noteworthy projects and rank them.</code></pre>
<ol start="3">
  <li><strong>Activate</strong>: Save and activate the automation task to automatically track new AI projects.</li>
</ol>

<h2 id="conclusion">Conclusion</h2>
<p>TraeWork streamlines the entire AI content creation process, from initial research to final production. By following this workflow, you can efficiently create high-quality AI content that's both informative and visually appealing. The platform's integrated modes and AI capabilities make it accessible even for those without advanced technical skills, allowing you to focus on creating valuable content for your audience.</p>

<h2>常见问题</h2>

<h3>What is TraeWork, and who is it for?</h3>
<p>TraeWork is an all-in-one AI content creation platform that covers the full pipeline — research, project ranking, document syncing, visual design, interactive demos, and cover generation. It's built for content creators, YouTubers, and marketers who want to produce polished videos without juggling multiple tools. The workflow in this tutorial walks from researching GitHub Trending projects to recording a finished "top 5" video, all within one interface and its plugin ecosystem (Feishu, Seedream, and more).</p>

<h3>Do I need design or coding skills to use this workflow?</h3>
<p>No. The workflow is intentionally accessible to non-technical users. Design mode generates visual directions from a plain-language prompt, and Code mode produces the interactive HTML demo you screen-record — you don't write the code yourself. What you do provide is clear input: a well-defined research prompt, a design brief, and final choices on ranking, style, and covers. TraeWork handles the execution in each step.</p>

<h3>How does the Feishu integration help the process?</h3>
<p>Feishu documents act as the shared workspace between steps. Research results, the ranked shortlist, the video outline, design specifications, and project details all live in Feishu documents that TraeWork reads and writes as you move between modes. This keeps the information consistent — the Design and Code modes both read from the same document, so the visual style and the demo match the outline you confirmed in Step 3, instead of each step starting from scratch.</p>

<h3>Can TraeWork really automate the research for recurring content?</h3>
<p>Yes, and that's the point of Step 7. The Automation feature lets you schedule a recurring task — the example runs weekly at 08:00 and returns the 10 most noteworthy new AI open source projects, ranked by practical value, innovation, activity, and video appeal. This turns what used to be manual weekly research into a hands-off pipeline, so you always have fresh source material for your next video without doing the searching yourself.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Want to streamline more of your content workflow? Continue with these guides:</p>
  <ul>
    <li><a href="/article/how-to-create-professional-ai-videos-flova-ai-complete-practical-guide">How to Create Professional AI Videos with Flova.ai: A Complete Practical Guide</a> — an alternative all-in-one AI video production workflow</li>
    <li><a href="/article/master-seedance-2-5-zero-basics-guide-commercial-grade-ai-video-creation">Master Seedance 2.5: Zero-Basics Guide to Commercial-Grade AI Video Creation</a> — the Seedance 2.5 model behind AI video generation</li>
    <li><a href="/article/how-feishu-redefined-ai-work-100-to-20000-system-in-minutes">How Feishu Redefined AI Work: $100 → $20,000 System in Minutes</a> — how Feishu-based AI workflows scale content operations</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">📖 AI教程</span>
  <span class="meta-badge">🕒 阅读约8分钟</span>
  <span class="meta-badge">📅 2026年8月15日</span>
  <span class="meta-badge">🎯 入门</span>
</div>

<h2 id="introduction">引言</h2>
<p>制作高质量的AI内容并不复杂。使用TraeWork，你可以在一个平台内完成从调研到成片的全流程。本指南以制作"5个值得推荐的AI开源项目"视频为例，带你走完每一步。</p>

<h2 id="step-1">第一步：Work模式下的项目规划与研究</h2>
<p>流程从Work模式开始，它专为研究和分析这类专业办公任务而设计。</p>
<ol>
  <li><strong>进入Work模式</strong>：点击左上角的"Work"标签。</li>
  <li><strong>定义目标</strong>：清晰输入你的任务。以本例来说，使用这个提示词：</li>
</ol>
<pre><code class="language-text">我想制作一个名为"5个值得推荐的AI开源项目"的视频。
请在GitHub Trending上研究近期的AI开源项目，重点关注近期涌现或过去90天内活跃的项目。
汇总20-30个候选项目，包括项目名称、GitHub链接、分类、核心用途、星标数、最近更新、发布日期、项目活跃度、亮点、已知问题以及信息来源。</code></pre>
<ol start="3">
  <li><strong>等待结果</strong>：TraeWork会利用其研究和数据处理技能，搜索网页、阅读项目文件，并整理出详细的候选列表。</li>
</ol>

<h2 id="step-2">第二步：项目排名与筛选</h2>
<p>拿到候选列表后，再次使用Work模式对项目进行排名：</p>
<ol>
  <li><strong>提交排名请求</strong>：使用这个提示词评估候选项目：</li>
</ol>
<pre><code class="language-text">请根据实用价值、项目活跃度、创新性、观众吸引力、视频呈现效果和项目独特性，对这20个候选项目进行排名。
包括各维度评分、综合排名、推荐建议和主要风险。</code></pre>
<ol start="2">
  <li><strong>选定最终项目</strong>：从排名结果中，选出最契合视频主题的前5个项目。</li>
</ol>

<h2 id="step-3">第三步：同步到飞书文档</h2>
<p>TraeWork与飞书集成，让你的工作井然有序：</p>
<ol>
  <li><strong>打开插件市场</strong>：点击左侧边栏的"插件市场"。</li>
  <li><strong>添加飞书插件</strong>：找到并添加飞书插件。</li>
  <li><strong>同步数据</strong>：在对话框点击飞书图标，使用这个提示词：</li>
</ol>
<pre><code class="language-text">请核实最终选定的5个项目，整理其核心功能、推荐理由、使用场景、局限性和官方来源，并在新的飞书文档中创建清晰的视频大纲。</code></pre>

<h2 id="step-4">第四步：Design模式下的视觉设计</h2>
<p>接下来进入Design模式，为你的视频创建视觉素材：</p>
<ol>
  <li><strong>进入Design模式</strong>：点击"Design"标签。</li>
  <li><strong>生成视觉方案</strong>：使用这个提示词创建设计选项：</li>
</ol>
<pre><code class="language-text">阅读包含视频大纲和5个项目详情的飞书文档。
为"5个值得推荐的AI开源项目"视频设计一套统一的视觉系统。
这5个项目及其主题是：
- Agent Reach：Agent网络
- Reasonix：AI编程
- SkillSpector：Agent安全
- Headroom：上下文压缩
- DeepTutor：AI教育
提供3个不同的视觉方向，包括：
1. 视频主封面
2. 5个项目的介绍卡片
3. 视频分段页面
视觉要求：
- 色彩丰富
- 标题文字大而清晰（不要压缩）
- 主封面左下角为主播预留空间
- 风格统一但每个项目有独特元素
- 主封面文字："5个GitHub AI开源项目"</code></pre>
<ol start="3">
  <li><strong>选定设计</strong>：选择你偏好的设计方向，让TraeWork把设计规范写入你的飞书文档。</li>
</ol>

<h2 id="step-5">第五步：Code模式下制作交互式视频素材</h2>
<p>使用Code模式生成动态视频素材：</p>
<ol>
  <li><strong>进入Code模式</strong>：点击"Code"标签。</li>
  <li><strong>生成交互式演示</strong>：使用这个提示词创建视频素材：</li>
</ol>
<pre><code class="language-text">阅读飞书项目文档。
根据已确认的视频大纲、5个项目详情和设计规范，创建一个适合录屏的交互式网页演示。
页面应包括：
- 开场总览页
- 5个项目各自的页面
- 总结页
要求：
- 遵循设计规范中的字体、颜色和布局
- 支持鼠标点击和键盘在章节间导航
- 标题、项目卡片和关键信息依次动画呈现
- 动画干净专业，不要过度特效
- 所有文字和视觉元素必须准确
- 页面分辨率：1920x1080</code></pre>
<ol start="3">
  <li><strong>使用成果</strong>：生成的HTML演示保持了你的设计风格，并包含研究中的所有信息，可直接用于录屏。</li>
</ol>

<h2 id="step-6">第六步：用Seedream AI生成视频封面</h2>
<p>使用Seedream AI图像生成功能打造吸睛的视频封面：</p>
<ol>
  <li><strong>打开Seedream</strong>：进入插件市场，点击"技能"，搜索"seed"，添加Seedream图像生成技能。</li>
  <li><strong>生成封面</strong>：使用这个提示词（也可以上传参考图）：</li>
</ol>
<pre><code class="language-text">为"5个值得推荐的GitHub AI开源项目"生成3-4个视频封面。
要求：
1. 角色一致性：确保画面中的人物拥有相同的脸型、眼镜、发型、服装和年龄。
2. 主播表情：表情丰富的肢体语言、手势、广角镜头、近景。
3. 主标题：大号、粗体、高对比度文字（6-10个字，标题约占视觉宽度的40%）。
4. 视觉焦点：一个主要焦点（人脸/主标题/前景元素/对比卡片），其他元素为其服务。
5. 信息层级：清晰的区块（原图/编辑图、主标题、场景、海报/缩略图、前景元素、主播信息、背景、留白）。
6. 配色：黑、白、黄、红，点缀小面积红/蓝。高对比、强视觉冲击。
7. 限制：不要杂乱的代码、logo、水印、多余文字、变形字符、空白背景或随意漂浮的元素。</code></pre>
<ol start="3">
  <li><strong>定稿</strong>：选出最佳封面，必要时微调文字，就可以开始录制视频了。</li>
</ol>

<h2 id="step-7">第七步：自动化未来任务</h2>
<p>无需手动操作也能持续跟进新的AI项目：</p>
<ol>
  <li><strong>创建自动化任务</strong>：点击左侧边栏的"自动化"。</li>
  <li><strong>配置任务</strong>：创建新任务并设置以下参数：</li>
</ol>
<ul>
  <li>任务名称："每周GitHub AI开源项目监控"</li>
  <li>执行计划：每周08:00</li>
  <li>任务描述：</li>
</ul>
<pre><code class="language-text">研究过去一周GitHub上新增或热门的AI开源项目。
重点关注实用价值、创新性、活跃度、观众吸引力和视频呈现效果。
排除近期未更新或没有实际应用的项目。
最后选出10个最值得关注的项目并排名。</code></pre>
<ol start="3">
  <li><strong>激活</strong>：保存并激活自动化任务，即可自动跟踪新的AI项目。</li>
</ol>

<h2 id="conclusion">结语</h2>
<p>TraeWork精简了整个AI内容创作流程，从前期调研到最终成片。遵循这个工作流，你可以高效制作兼具信息量与视觉吸引力的优质AI内容。平台集成化的模式和AI能力，让即使没有高级技术技能的人也能轻松上手，让你专注于为观众创造有价值的内容。</p>

<h2>常见问题</h2>

<h3>什么是TraeWork？它适合谁使用？</h3>
<p>TraeWork是一站式AI内容创作平台，覆盖从研究、项目排名、文档同步、视觉设计、交互式演示到封面生成的完整流程。它面向内容创作者、视频博主和营销人员，让他们无需在多个工具之间切换就能产出精良视频。本教程演示的工作流，就是在同一个界面及其插件生态（飞书、Seedream等）中，从调研GitHub Trending项目到录制完成一部"TOP 5"视频。</p>

<h3>使用这个工作流需要设计或编程技能吗？</h3>
<p>不需要。这个工作流对非技术用户很友好。Design模式从自然语言提示词生成视觉方向，Code模式产出可供录屏的交互式HTML演示——你不需要自己写代码。你需要提供的是清晰的输入：定义明确的研究提示词、设计简报，以及排名、风格和封面上的最终选择。TraeWork负责每一步的执行。</p>

<h3>飞书集成如何帮助整个流程？</h3>
<p>飞书文档是各步骤之间的共享工作空间。研究结果、排名候选、视频大纲、设计规范和项目详情都存放在飞书文档中，TraeWork在各模式之间切换时会读取和写入这些文档。这保证了信息的一致性——Design模式和Code模式都读取同一份文档，因此视觉风格和演示与你第三步确认的大纲保持一致，而不是每个步骤都从头开始。</p>

<h3>TraeWork真的能自动完成周期性内容的研究吗？</h3>
<p>能，这正是第七步的意义。自动化功能让你设置周期性任务——示例中每周08:00运行，返回按实用价值、创新性、活跃度和视频吸引力排名的最值得关注的10个新AI开源项目。这把你原本每周手动进行的研究变成了一条无人值守的流水线，让你总能有新鲜的素材源来做下一条视频，而无需自己搜索。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>想让内容工作流更高效？继续阅读这些指南：</p>
  <ul>
    <li><a href="/article/how-to-create-professional-ai-videos-flova-ai-complete-practical-guide">如何使用Flova.ai制作专业AI视频：完整实战指南</a> — 另一种一站式AI视频制作工作流</li>
    <li><a href="/article/master-seedance-2-5-zero-basics-guide-commercial-grade-ai-video-creation">掌握Seedance 2.5：零基础商业级AI视频创作指南</a> — 驱动AI视频生成的Seedance 2.5模型</li>
    <li><a href="/article/how-feishu-redefined-ai-work-100-to-20000-system-in-minutes">飞书如何重塑AI办公：$100到$20,000的分钟级系统</a> — 基于飞书的AI工作流如何规模化内容运营</li>
  </ul>
</div>`,
  },

'''
last = c.rfind('};')
with open('src/lib/article-content.ts', 'w', encoding='utf-8') as f: f.write(c[:last] + n + '};')
print('Part 2 done')

# ---------- Part 3: tools.ts new tool ----------
with open('src/lib/tools.ts', 'r', encoding='utf-8') as f: t = f.read()
tool = r'''  {
    id: "traework",
    name: "TraeWork",
    nameZh: "TraeWork",
    description: "An all-in-one AI content creation platform — research, project ranking, Feishu document syncing, visual design, interactive demos, and AI covers in one workflow, with recurring automation tasks.",
    descriptionZh: "一站式AI内容创作平台——研究、项目排名、飞书文档同步、视觉设计、交互式演示和AI封面于一个工作流，支持周期性自动化任务。",
    category: "writing",
    tags: ["content-creation", "ai-agent", "workflow", "feishu", "seedream", "video", "automation"],
    difficulty: "beginner",
    url: "https://www.trae.ai",
    rating: r(4.5),
    pricing: "Free tier with premium plans",
    useCase: "End-to-end AI content creation — from research and ranking to design, interactive demos, covers, and automated weekly monitoring",
    icon: "\u{1F3AC}",
    company: "Trae",
    companyZh: "Trae",
    founded: 2024,
    headquarters: "Shenzhen, China",
    descriptionLong: "TraeWork is an all-in-one AI content creation platform that compresses the entire production pipeline into one workflow. Instead of hopping between a research tool, a ranking sheet, a design app, and a code editor, creators work in four integrated modes. Work mode handles research and analysis — for example, scanning GitHub Trending to compile a candidate list of AI open source projects with structured metadata. Design mode generates unified visual systems (covers, project cards, section pages) from plain-language prompts. Code mode produces interactive HTML demos ready for screen recording, following the design specifications. A Feishu plugin keeps every step in sync: research results, the ranked shortlist, the video outline, and design specs all live in Feishu documents that the modes read and write. For covers, TraeWork integrates Seedream AI image generation with prompts for character consistency, title hierarchy, and color schemes. The Automation feature schedules recurring research tasks — the tutorial's example runs weekly at 08:00 and returns the 10 most noteworthy new AI open source projects, ranked. The platform is designed for creators without advanced technical skills: you provide clear prompts and choices, TraeWork handles execution.",
    descriptionLongZh: "TraeWork是一站式AI内容创作平台，把整个制作流程压缩进一个工作流。创作者不再需要在研究工具、排名表格、设计应用和代码编辑器之间来回切换，而是在四个集成模式中完成。Work模式负责研究和分析——例如扫描GitHub Trending，整理带结构化元数据的AI开源项目候选列表。Design模式从自然语言提示词生成统一的视觉系统（封面、项目卡片、分段页面）。Code模式根据设计规范产出可供录屏的交互式HTML演示。飞书插件让每一步保持同步：研究结果、排名候选、视频大纲和设计规范都存放在飞书文档中，各模式读取和写入这些文档。封面方面，TraeWork集成Seedream AI图像生成，支持角色一致性、标题层级和配色等提示词。自动化功能可安排周期性研究任务——教程示例每周08:00运行，返回按排名的最值得关注的10个新AI开源项目。该平台面向没有高级技术技能的创作者设计：你提供清晰的提示词和选择，TraeWork负责执行。",
    advantages: ["Four integrated modes: Work, Design, Code, Automation", "Feishu document syncing keeps every step consistent", "Seedream AI covers with character consistency", "Interactive HTML demos ready for screen recording", "Recurring automation tasks for fresh research", "Accessible to creators without technical skills"],
    advantagesZh: ["四个集成模式：Work、Design、Code、自动化", "飞书文档同步让每一步保持一致", "Seedream AI封面支持角色一致性", "交互式HTML演示可直接录屏", "周期性自动化任务持续产出新研究", "非技术创作者也能轻松上手"],
    useCases: ["YouTube video production from research to cover", "Weekly AI open source project monitoring", "Visual design systems for content series", "Screen-recordable interactive web demos", "Feishu-based content operations"],
    useCasesZh: ["从研究到封面的YouTube视频制作", "每周AI开源项目监控", "内容系列的视觉设计系统", "可录屏的交互式网页演示", "基于飞书的内容运营"],
    targetAudience: "Content creators, YouTubers, and marketers who want a single platform for the full AI content production pipeline",
    targetAudienceZh: "希望在单一平台完成AI内容制作全流程的内容创作者、视频博主和营销人员",
    pricingTiers: [
      {
        tier: "Free",
        tierZh: "免费版",
        price: "Free tier",
        features: ["Work research mode", "Feishu integration", "Basic design and code modes", "Seedream covers"],
        featuresZh: ["Work研究模式", "飞书集成", "基础设计和代码模式", "Seedream封面"],
      },
      {
        tier: "Premium",
        tierZh: "高级版",
        price: "Premium plans",
        features: ["Automation tasks", "Advanced design options", "Priority processing"],
        featuresZh: ["自动化任务", "高级设计选项", "优先处理"],
      },
    ],
    pros: ["Full pipeline in one platform", "Feishu keeps workflow consistent", "Automation handles recurring research", "Accessible for non-technical creators"],
    prosZh: ["一个平台完成全流程", "飞书保证工作流一致", "自动化处理周期性研究", "非技术创作者也能上手"],
    cons: ["Newer platform with a shorter track record", "Heavy reliance on Feishu for workflow consistency", "Best covers depend on Seedream prompt quality"],
    consZh: ["较新的平台，历史记录较短", "工作流一致性高度依赖飞书", "最佳封面依赖Seedream提示词质量"],
    extensions: [],
    skills: ["Content research", "Project ranking", "Visual design", "Interactive demo generation", "Cover generation", "Recurring automation"],
    scene: "content-creation",
  },

'''
last_tool = t.rfind('] as Tool[];')
with open('src/lib/tools.ts', 'w', encoding='utf-8') as f: f.write(t[:last_tool] + tool + '] as Tool[];')
print('Part 3 done\n=== Done ===')
