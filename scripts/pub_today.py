"""
Publish July 13, 2026 — 2 articles, no new tools.
"""
import os

BASE = r"C:\Users\jun\aistudyonline-next"
os.chdir(BASE)

# ===== Part 1: Add 2 article metadata to articles.ts =====
with open('src/lib/articles.ts', 'r', encoding='utf-8') as f:
    articles_src = f.read()

new_articles = r"""  {
    slug: "vibecoding-contest-guide-game-animations-ai-tools",
    title: "VibeCoding Contest Guide: Create Game Animations Efficiently With AI Tools",
    titleZh: "VibeCoding大赛指南：用AI工具高效制作游戏动画",
    description: "A complete AI game animation workflow — from sprite sheet generation with structured prompts, to animation control code for Godot (GDScript) and Unity (C#), motion fine-tuning, easing functions, and advanced cutscene sequencing — zero art or coding foundation required.",
    descriptionZh: "AI游戏动画完整工作流——从精灵表生成的结构化提示词，到Godot（GDScript）和Unity（C#）的动画控制代码，动作微调、缓动函数和高级过场动画编排——零美术和编程基础也能上手。",
    category: "AI Tutorials",
    tags: ["VibeCoding", "Game Development", "Animation", "Godot", "Unity", "Sprite Sheet", "Tutorial"],
    difficulty: "intermediate",
    toolsMentioned: ["Claude Code", "Godot", "Unity"],
    date: "2026-07-13",
  },
  {
    slug: "claude-code-game-studios-game-development-easier",
    title: "Make Game Development Easier with Claude Code Game Studios",
    titleZh: "Claude Code Game Studios：让独立游戏开发从未如此简单",
    description: "An introduction to Claude Code Game Studios — an open-source project that transforms a single Claude Code session into a complete game studio with 49 AI agents, 73 skills, 12 hooks, and a hierarchical studio structure (Directors → Department Heads → Experts) for solo game development.",
    descriptionZh: "Claude Code Game Studios开源项目介绍——将单个Claude Code会话转变为完整游戏工作室，含49个AI Agent、73个技能、12个钩子和层级化工作室架构（总监→部门主管→专家），实现单人全流程游戏开发。",
    category: "AI Tools",
    tags: ["Claude Code", "Game Development", "Open Source", "AI Agent", "Studio", "Indie Dev"],
    difficulty: "beginner",
    toolsMentioned: ["Claude Code"],
    date: "2026-07-13",
  },

"""

last_bracket = articles_src.rfind('];')
articles_new = articles_src[:last_bracket] + new_articles + '];'

with open('src/lib/articles.ts', 'w', encoding='utf-8') as f:
    f.write(articles_new)

print('Part 1: 2 new articles added to articles.ts')

# ===== Part 2: Add article content to article-content.ts =====
with open('src/lib/article-content.ts', 'r', encoding='utf-8') as f:
    content_src = f.read()

new_contents = r'''
  "vibecoding-contest-guide-game-animations-ai-tools": {
    content: `<div class="meta-banner">
  <span class="meta-badge">📚 AI Tutorials</span>
  <span class="meta-badge">🕒 8 min read</span>
  <span class="meta-badge">📅 Jul 13, 2026</span>
  <span class="meta-badge">🎯 Intermediate</span>
</div>

<h2 id="introduction">Introduction</h2>

<p>VibeCoding competition focuses on lightweight AI game animation production. Even creators with zero art foundation can finish complete character animations, scene motion effects and cutscene sequences by combining AI drawing models, code generation assistants and animation editing tools. This article sorts out the full practical workflow, covering tool matching, prompt writing, motion code generation and preview debugging steps.</p>

<h2 id="tool-stack">Core Tool Stack For AI Game Animation</h2>

<p>The complete workflow relies on three core modules, which can be used independently or combined:</p>

<ol>
  <li>AI image generation model: Output sprite sheets, character keyframe frames</li>
  <li>Code AI assistant: Generate animation control logic for Unity / Godot</li>
  <li>Lightweight animation editor: Adjust frame rate, motion easing and collision sync</li>
</ol>

<h2 id="step-1">Step 1: Generate Game Animation Sprite Sheets With Image AI</h2>

<p>Sprite sheets are the foundation of 2D game animations. Use structured prompts to get unified style keyframes.</p>

<h3>Practical Prompt Template</h3>

<pre><code class="language-text">2D pixel game character sprite sheet, 8 frames walk cycle, consistent character proportion, transparent background, single horizontal row layout, clean pixel lines, no extra decorative elements, game asset standard, 32x32 pixel per frame</code></pre>

<h3>Operation Tips</h3>

<ul>
  <li>Lock character color palette in prompt to avoid inconsistent tones between frames</li>
  <li>Add "no text, no watermark" to eliminate invalid elements</li>
  <li>Export output as PNG with alpha channel for engine direct import</li>
</ul>

<h2 id="step-2">Step 2: Generate Animation Control Code Via VibeCoding</h2>

<p>After obtaining sprite resources, send asset information to AI coding assistant to generate reusable animation scripts, compatible with mainstream game engines.</p>

<h3>Sample Request Command For Godot Engine</h3>

<pre><code class="language-text">Write a 2D sprite animation script for Godot 4. Read the walk cycle sprite sheet with 8 frames, frame duration 0.12s, add idle transition logic, add flip horizontal function for left-right movement, comment all core logic for modification.</code></pre>

<h3>Generated Standard Code Block (Godot GDScript)</h3>

<pre><code class="language-gdscript">extends Sprite2D

@export var sprite_sheet: Texture2D
@export var frame_count: int = 8
@export var frame_duration: float = 0.12

var current_frame: int = 0
var animation_timer: float = 0.0

func _process(delta: float) -> void:
    animation_timer += delta
    if animation_timer >= frame_duration:
        current_frame = (current_frame + 1) % frame_count
        animation_timer = 0.0
        update_sprite_frame()

func update_sprite_frame() -> void:
    var frame_width = sprite_sheet.get_width() / frame_count
    region_rect = Rect2(current_frame * frame_width, 0, frame_width, sprite_sheet.get_height())

func flip_sprite(is_left: bool) -> void:
    flip_h = is_left</code></pre>

<h3>Sample Request Command For Unity C#</h3>

<pre><code class="language-text">Create C# animation script for Unity 2D SpriteRenderer, implement 6-frame jump animation, control animation playback state via boolean variables, separate idle and jump motion branches.</code></pre>

<h2 id="step-3">Step 3: Motion Fine-Tuning & Real-Time Preview</h2>

<ol>
  <li>Import sprite sheet and script into game engine</li>
  <li>Adjust frame duration to modify motion smoothness: fast attack uses 0.06s per frame, slow walk uses 0.15s per frame</li>
  <li>Add easing logic via AI secondary code generation if motion looks stiff</li>
</ol>

<h3>Easing Function Request Example</h3>

<pre><code class="language-text">Add ease-out slowdown logic to the walk animation script, decelerate frame switching when character stops moving</code></pre>

<h2 id="step-4">Step 4: Advanced Cutscene Animation Workflow</h2>

<p>For story cutscenes with multi-character linkage:</p>

<ol>
  <li>Generate independent sprite sheets for each actor</li>
  <li>Let AI generate timeline scheduling code to sync multiple animation layers</li>
  <li>Add camera shake, fade-in/fade-out auxiliary animation effects via one-line prompt</li>
</ol>

<pre><code class="language-text">Add camera shake animation code triggered when character takes damage, shake intensity fades out in 0.3 seconds</code></pre>

<h2 id="pitfalls">Common Pitfalls & Fix Solutions</h2>

<ol>
  <li><strong>Frame style inconsistency</strong>: Append "unified light source, fixed color palette" to generation prompt</li>
  <li><strong>Animation jitter</strong>: Increase frame count or lower frame duration value in script</li>
  <li><strong>Sprite display offset</strong>: Add coordinate correction code block through AI supplementary generation</li>
  <li><strong>Large file lag</strong>: Add prompt limit "max canvas size 512*128, compressed pixel assets"</li>
</ol>

<h2 id="conclusion">Conclusion</h2>

<p>VibeCoding's AI game animation workflow greatly lowers the threshold for independent game developers. You do not need professional animation drawing skills or solid coding foundation. By standardizing prompt templates and one-click code generation commands, you can rapidly produce usable game motion assets and control scripts. This set of processes fits both small indie pixel games and lightweight casual game projects, greatly shortening animation development cycles.</p>

<h2>常见问题</h2>

<h3>Do I really need zero art skills to create game animations with this workflow?</h3>
<p>Yes — for 2D pixel art and simple sprite animations. The AI image generator handles the actual drawing. Your job is writing good prompts (the article provides templates) and making judgment calls on the output. You do need an <strong>eye for consistency</strong> — checking that frames match in style, proportions, and color palette. The article's "locked color palette" and "no text, no watermark" tips are specifically designed to catch AI generation quirks before they become problems. For complex 3D animations or highly stylized art, you'll still benefit from art direction experience, but the asset generation itself requires no drawing.</p>

<h3>Which game engine should I use — Godot or Unity — for this workflow?</h3>
<p>Both work, but <strong>Godot</strong> has a slight edge for this specific AI-assisted workflow. Godot's GDScript is simpler and more readable than C#, which means AI-generated code is more likely to work correctly on the first try. Godot is also free, open-source, and has a lighter footprint — ideal for indie and solo developers. Unity has a larger asset store and more tutorials, but the C# boilerplate can trip up AI code generation. If you're new to both, start with Godot. If you're already comfortable with Unity, the article includes C# prompt templates that work fine.</p>

<h3>How do I handle animations that need to respond to player input (like attack combos)?</h3>
<p>Extend the script with state machine logic. The base walk cycle script in the article uses a simple frame loop. For input-driven animations, ask the AI to add: (1) an animation state enum (Idle, Walk, Attack, Jump), (2) input detection that switches states, (3) transition rules between states. Example prompt: "Add a state machine to the animation script with Idle, Walk, Attack, and Jump states. Attack triggers on key press and returns to Idle after animation completes. Jump transitions to Fall when velocity becomes negative." The AI can generate the full state machine — you just describe the behavior.</p>

<h3>What's the biggest time-saver in this workflow?</h3>
<p>The <strong>sprite sheet prompt template</strong>. Without it, you'd spend hours iterating on prompts to get consistent frames. With it, the first generation is usually usable. The second biggest is the code generation — writing animation scripts manually for Godot or Unity typically takes 30-60 minutes per character. The AI generates working code in under a minute. Combined, these two steps turn what used to be a day of work per character into about 15 minutes of prompting and 15 minutes of fine-tuning.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Ready to build your game? Continue your game dev journey:</p>
  <ul>
    <li><a href="/articles/claude-code-game-studios-game-development-easier">Make Game Development Easier with Claude Code Game Studios</a> — turn Claude Code into a full game studio with 49 agents</li>
    <li><a href="/articles/vibe-coding-practical-guide-ai-dev-workflow-part1">Vibe Coding Practical Guide: AI Development Full Workflow (Part 1)</a> — the methodology behind AI-assisted development</li>
    <li><a href="/articles/complete-practical-tutorial-claude-code-core-operations">Complete Practical Tutorial: Master All Core Operations Inside Claude Code</a> — the AI coding tool that powers this workflow</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">📚 AI 教程</span>
  <span class="meta-badge">🕒 阅读约8分钟</span>
  <span class="meta-badge">📅 2026年7月13日</span>
  <span class="meta-badge">🎯 中级</span>
</div>

<h2 id="introduction">引言</h2>

<p>VibeCoding大赛聚焦轻量级AI游戏动画制作。即使零美术基础的创作者，通过组合AI绘图模型、代码生成助手和动画编辑工具，也能完成完整的角色动画、场景动效和过场动画序列。本文梳理了完整实战流程，涵盖工具搭配、提示词编写、动作代码生成和预览调试步骤。</p>

<h2 id="tool-stack">AI游戏动画核心工具栈</h2>

<p>完整工作流依赖三个核心模块，可独立使用也可组合：</p>

<ol>
  <li>AI图像生成模型：输出精灵表、角色关键帧帧</li>
  <li>代码AI助手：生成Unity/Godot动画控制逻辑</li>
  <li>轻量动画编辑器：调整帧率、运动缓动和碰撞同步</li>
</ol>

<h2 id="step-1">第一步：用图像AI生成游戏动画精灵表</h2>

<p>精灵表是2D游戏动画的基础。使用结构化提示词获取风格统一的关键帧。</p>

<h3>实战提示词模板</h3>

<pre><code class="language-text">2D像素游戏角色精灵表，8帧行走循环，角色比例一致，透明背景，单行水平排列，干净像素线条，无额外装饰元素，游戏素材标准，每帧32x32像素</code></pre>

<h3>操作技巧</h3>

<ul>
  <li>在提示词中锁定角色色板，避免帧间色调不一致</li>
  <li>添加"无文字、无水印"消除无效元素</li>
  <li>导出含Alpha通道的PNG格式供引擎直接导入</li>
</ul>

<h2 id="step-2">第二步：通过VibeCoding生成动画控制代码</h2>

<p>获取精灵资源后，将素材信息发送给AI编程助手，生成可复用的动画脚本，兼容主流游戏引擎。</p>

<h3>Godot引擎请求示例</h3>

<pre><code class="language-text">为Godot 4编写2D精灵动画脚本。读取8帧行走循环精灵表，帧持续时间0.12秒，添加空闲过渡逻辑，添加左右移动的水平翻转功能，为核心逻辑添加注释以便修改。</code></pre>

<h3>生成的标准代码块（Godot GDScript）</h3>

<pre><code class="language-gdscript">extends Sprite2D

@export var sprite_sheet: Texture2D
@export var frame_count: int = 8
@export var frame_duration: float = 0.12

var current_frame: int = 0
var animation_timer: float = 0.0

func _process(delta: float) -> void:
    animation_timer += delta
    if animation_timer >= frame_duration:
        current_frame = (current_frame + 1) % frame_count
        animation_timer = 0.0
        update_sprite_frame()

func update_sprite_frame() -> void:
    var frame_width = sprite_sheet.get_width() / frame_count
    region_rect = Rect2(current_frame * frame_width, 0, frame_width, sprite_sheet.get_height())

func flip_sprite(is_left: bool) -> void:
    flip_h = is_left</code></pre>

<h3>Unity C#请求示例</h3>

<pre><code class="language-text">为Unity 2D SpriteRenderer创建C#动画脚本，实现6帧跳跃动画，通过布尔变量控制动画播放状态，分离空闲和跳跃动作分支。</code></pre>

<h2 id="step-3">第三步：动作微调与实时预览</h2>

<ol>
  <li>将精灵表和脚本导入游戏引擎</li>
  <li>调整帧持续时间修改动作流畅度：快速攻击用0.06秒/帧，慢速行走用0.15秒/帧</li>
  <li>动作僵硬时通过AI二次代码生成添加缓动逻辑</li>
</ol>

<h3>缓动函数请求示例</h3>

<pre><code class="language-text">为行走动画脚本添加缓出减速逻辑，角色停止移动时帧切换逐渐减速</code></pre>

<h2 id="step-4">第四步：高级过场动画工作流</h2>

<p>多角色联动的剧情过场动画：</p>

<ol>
  <li>为每个角色生成独立的精灵表</li>
  <li>让AI生成时间轴调度代码同步多个动画层</li>
  <li>通过一行提示词添加镜头抖动、淡入淡出等辅助动画效果</li>
</ol>

<pre><code class="language-text">添加角色受伤时触发的镜头抖动动画代码，抖动强度在0.3秒内衰减</code></pre>

<h2 id="pitfalls">常见坑与修复方案</h2>

<ol>
  <li><strong>帧风格不一致</strong>：在生成提示词后追加"统一光源、固定色板"</li>
  <li><strong>动画抖动</strong>：增加帧数或降低脚本中帧持续时间值</li>
  <li><strong>精灵显示偏移</strong>：通过AI补充生成坐标修正代码块</li>
  <li><strong>大文件卡顿</strong>：添加提示词限制"画布最大512*128，压缩像素素材"</li>
</ol>

<h2 id="conclusion">总结</h2>

<p>VibeCoding的AI游戏动画工作流大大降低了独立游戏开发者的门槛。你不需要专业动画绘制技能或扎实编程基础。通过标准化提示词模板和一键代码生成命令，可以快速产出可用的游戏动作素材和控制脚本。这套流程既适合小型独立像素游戏，也适合轻量休闲游戏项目，大幅缩短动画开发周期。</p>

<h2>常见问题</h2>

<h3>真的零美术基础就能用这个工作流做游戏动画？</h3>
<p>是的——对2D像素艺术和简单精灵动画来说。AI图像生成器处理实际绘画。你的工作是写好提示词（文章提供了模板）并对输出做出判断。你确实需要<strong>对一致性有眼光</strong>——检查帧之间风格、比例和色板是否匹配。文章中的"锁定色板"和"无文字无水印"技巧正是为了在AI生成问题成为麻烦之前抓住它们。对于复杂3D动画或高度风格化艺术，有美术指导经验仍然有益，但素材生成本身不需要绘画。</p>

<h3>该用哪个游戏引擎——Godot还是Unity？</h3>
<p>两者都行，但<strong>Godot</strong>在这个特定AI辅助工作流中略占优势。Godot的GDScript比C#更简单、更易读，这意味着AI生成的代码更可能一次就正确运行。Godot还免费、开源、轻量——非常适合独立和单人开发者。Unity有更大的资源商店和更多教程，但C#的样板代码可能让AI代码生成出错。如果你两个都没用过，从Godot开始。如果已经熟悉Unity，文章包含了效果不错的C#提示词模板。</p>

<h3>如何处理需要响应玩家输入的动画（如连击）？</h3>
<p>用状态机逻辑扩展脚本。文章中的基础行走循环脚本使用简单的帧循环。对于输入驱动的动画，让AI添加：(1) 动画状态枚举（Idle、Walk、Attack、Jump），(2) 切换状态的输入检测，(3) 状态间的过渡规则。示例提示词："为动画脚本添加状态机，包含Idle、Walk、Attack、Jump状态。按键触发Attack，动画完成后返回Idle。速度为负时Jump过渡到Fall。"AI可以生成完整状态机——你只需描述行为。</p>

<h3>这个工作流最大的省时点是什么？</h3>
<p><strong>精灵表提示词模板</strong>。没有它，你可能要花数小时迭代提示词才能获得一致帧。有了它，第一次生成通常就能用。第二大省时点是代码生成——手动为Godot或Unity编写动画脚本通常每个角色需要30-60分钟。AI在不到一分钟内生成可运行代码。两者结合，以前每个角色一天的工作量变成约15分钟提示词+15分钟微调。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>准备好做游戏了？继续你的游戏开发之旅：</p>
  <ul>
    <li><a href="/articles/claude-code-game-studios-game-development-easier">Claude Code Game Studios：让独立游戏开发从未如此简单</a> — 将Claude Code变成49个Agent的完整游戏工作室</li>
    <li><a href="/articles/vibe-coding-practical-guide-ai-dev-workflow-part1">Vibe Coding实战指南：AI开发完整工作流（上篇）</a> — AI辅助开发背后的方法论</li>
    <li><a href="/articles/complete-practical-tutorial-claude-code-core-operations">Claude Code完全实战教程：掌握所有核心操作</a> — 驱动这个工作流的AI编码工具</li>
  </ul>
</div>`,
  },

  "claude-code-game-studios-game-development-easier": {
    content: `<div class="meta-banner">
  <span class="meta-badge">🔧 AI Tools</span>
  <span class="meta-badge">🕒 5 min read</span>
  <span class="meta-badge">📅 Jul 13, 2026</span>
  <span class="meta-badge">🎯 Beginner</span>
</div>

<h2 id="introduction">Introduction</h2>

<p>Developing games alone has never been simpler. The <strong>Claude Code Game Studios</strong> project transforms a single Claude Code session into a complete game development studio. It features 49 intelligent agents, 73 skills, and a collaborative AI team to support your entire game creation workflow.</p>

<h2 id="what-is">What is Claude Code Game Studios?</h2>

<p>This open-source project turns Claude Code into a full game development studio, with:</p>

<ul>
  <li>49 AI agents</li>
  <li>72 workflow skills</li>
  <li>A complete coordination system that mirrors the hierarchical structure of a real studio</li>
</ul>

<h3>Core Components</h3>

<table>
  <tr><th>Category</th><th>Count</th><th>Description</th></tr>
  <tr><td><strong>Agents</strong></td><td>49</td><td>Professional intelligent agents covering design, programming, art, audio, narrative, quality assurance, and production.</td></tr>
  <tr><td><strong>Skills</strong></td><td>73</td><td>Slash commands for each workflow stage, including: /start, /design-system, /create-epics, /create-stories, /dev-story, /story-done</td></tr>
  <tr><td><strong>Hooks</strong></td><td>12</td><td>Automated validation for commits, pushes, asset changes, session lifecycle, agent audit tracking, and gap detection.</td></tr>
  <tr><td><strong>Rules</strong></td><td>11</td><td>Enforce domain coding standards when editing gameplay, engines, AI, UI, or network code.</td></tr>
  <tr><td><strong>Templates</strong></td><td>41</td><td>Document templates for GDD, UX specifications, ADR, iteration plans, HUD design, and accessibility design.</td></tr>
</table>

<h2 id="why-it-matters">Why It Matters</h2>

<p>While AI-powered game development is powerful, a single chat session lacks structure. Without a framework, you might hardcode magic numbers, skip design documentation, write messy code, or miss design reviews. No one will ask if your work aligns with the game's vision.</p>

<p>Claude Code Game Studios solves this by giving your AI session a real studio structure. Instead of a generic assistant, you get 49 professional agents organized in a studio hierarchy:</p>

<ul>
  <li><strong>Directors</strong> safeguard the vision</li>
  <li><strong>Department heads</strong> manage their domains</li>
  <li><strong>Experts</strong> execute specific tasks</li>
</ul>

<p>Each agent has clear responsibilities, promotion paths, and quality control points. You still make every decision, but you have a team that asks the right questions, catches errors early, and keeps your project organized from brainstorming to release.</p>

<h2 id="how-it-works">How It Works</h2>

<h3>Intelligent Agent Coordination</h3>

<p>Agents follow a structured delegation model:</p>

<ol>
  <li><strong>Vertical Delegation</strong>: Directors assign tasks to department heads, who then assign tasks to expert agents.</li>
  <li><strong>Horizontal Negotiation</strong>: Agents at the same level can negotiate with each other, but cannot make binding cross-domain decisions.</li>
  <li><strong>Conflict Resolution</strong>: Disagreements are escalated to a shared leader (e.g., creative-director for design, technical-director for technical issues).</li>
  <li><strong>Change Propagation</strong>: Cross-department changes are coordinated by the producer.</li>
  <li><strong>Domain Boundaries</strong>: Agents will not modify files outside their explicitly authorized domain.</li>
</ol>

<h3>Collaboration, Not Autonomy</h3>

<p>Every agent follows a strict collaboration protocol:</p>

<ol>
  <li><strong>Ask</strong>: Agents will ask questions before proposing solutions.</li>
  <li><strong>Present Options</strong>: Agents will present 2-4 options with pros and cons.</li>
  <li><strong>You Decide</strong>: Final decision-making authority always remains with you.</li>
  <li><strong>Draft</strong>: Agents will draft solutions for your review.</li>
  <li><strong>Approval</strong>: No files will be written without your explicit approval.</li>
</ol>

<h2 id="conclusion">Conclusion</h2>

<p>In the past, game development required a full team of planners, programmers, artists, musicians, and testers. Now, you only need to share your game idea with Claude Code, and it will help you build your game step by step. Claude Code Game Studios makes solo game development more accessible than ever, with the structure and support of a professional studio at your fingertips.</p>

<h2>常见问题</h2>

<h3>How is this different from just asking Claude Code to help me make a game?</h3>
<p>Without Game Studios, Claude Code is a general-purpose assistant — it can write code, but it won't proactively ask about your game design document, remind you to update the HUD spec when you change the UI, or flag that your new mechanic conflicts with the established art style. Game Studios adds <strong>process</strong>. The 49 agents act as built-in quality gates: the Creative Director ensures consistency with the vision, the Technical Director catches architectural issues, and the Producer tracks progress. It's the difference between having one smart assistant and having an entire studio's institutional knowledge embedded in your workflow.</p>

<h3>Do I need to configure all 49 agents manually?</h3>
<p>No. The project is designed to work out of the box. The 49 agents, 73 skills, 12 hooks, 11 rules, and 41 templates are pre-configured. You clone the repository, open it in Claude Code, and the studio structure is ready. The slash commands (/start, /design-system, /create-epics, etc.) are the primary interface — you trigger workflows, and the appropriate agents activate automatically. Over time, you can customize agents, add your own skills, and adjust rules to match your project's specific needs, but zero configuration is required to get started.</p>

<h3>Is this only for 2D games or does it support 3D?</h3>
<p>Claude Code Game Studios is engine-agnostic and dimension-agnostic. The agents, skills, and templates are designed around game development <strong>processes</strong> — design documentation, task breakdown, code review, asset management, testing — not specific technologies. Whether you're building a 2D pixel platformer in Godot, a 3D RPG in Unity, or a text-based narrative game, the studio structure works the same way. The domain-specific rules (gameplay, engines, AI, UI, network) apply regardless of your tech stack.</p>

<h3>Can I use this for a team project, or is it solo-only?</h3>
<p>It's designed for solo developers but works for small teams too. In a team setting, the agents serve as a shared process layer — everyone on the team interacts with the same studio structure, ensuring consistent documentation, code standards, and review workflows. The producer agent becomes particularly valuable for teams, tracking cross-member dependencies and flagging integration risks. The caveat: Claude Code sessions are per-user, so each team member runs their own instance. For larger teams, you'd want to supplement with a shared project management tool for the human coordination layer.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Excited about AI game development? Dive deeper:</p>
  <ul>
    <li><a href="/articles/vibecoding-contest-guide-game-animations-ai-tools">VibeCoding Contest Guide: Create Game Animations Efficiently With AI Tools</a> — the hands-on animation workflow companion</li>
    <li><a href="/articles/complete-practical-tutorial-claude-code-core-operations">Complete Practical Tutorial: Master All Core Operations Inside Claude Code</a> — master the foundation this project builds on</li>
    <li><a href="/articles/7-mainstream-agent-architectures-beginner-enterprise-guide">7 Mainstream Agent Architectures: From Beginner to Enterprise-Grade</a> — understand the Multi-Agent architecture behind Game Studios</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">🔧 AI 工具</span>
  <span class="meta-badge">🕒 阅读约5分钟</span>
  <span class="meta-badge">📅 2026年7月13日</span>
  <span class="meta-badge">🎯 入门</span>
</div>

<h2 id="introduction">引言</h2>

<p>独自开发游戏从未如此简单。<strong>Claude Code Game Studios</strong>项目将单个Claude Code会话转变为一个完整的游戏开发工作室。它拥有49个智能Agent、73个技能和一个协作AI团队，支持你的整个游戏创作工作流。</p>

<h2 id="what-is">什么是Claude Code Game Studios？</h2>

<p>这个开源项目将Claude Code变成完整的游戏开发工作室：</p>

<ul>
  <li>49个AI Agent</li>
  <li>72个工作流技能</li>
  <li>镜像真实工作室层级结构的完整协调系统</li>
</ul>

<h3>核心组件</h3>

<table>
  <tr><th>类别</th><th>数量</th><th>描述</th></tr>
  <tr><td><strong>Agent</strong></td><td>49</td><td>覆盖设计、编程、美术、音频、叙事、质量保证和制作的专业智能Agent。</td></tr>
  <tr><td><strong>技能</strong></td><td>73</td><td>每个工作流阶段的斜杠命令，包括：/start、/design-system、/create-epics、/create-stories、/dev-story、/story-done</td></tr>
  <tr><td><strong>钩子</strong></td><td>12</td><td>提交、推送、资源变更、会话生命周期、Agent审计追踪和缺口检测的自动验证。</td></tr>
  <tr><td><strong>规则</strong></td><td>11</td><td>编辑玩法、引擎、AI、UI或网络代码时强制执行领域编码标准。</td></tr>
  <tr><td><strong>模板</strong></td><td>41</td><td>GDD、UX规范、ADR、迭代计划、HUD设计和无障碍设计的文档模板。</td></tr>
</table>

<h2 id="why-it-matters">为什么重要</h2>

<p>虽然AI驱动的游戏开发很强大，但单个聊天会话缺乏结构。没有框架，你可能硬编码魔法数字、跳过设计文档、写出混乱代码或遗漏设计评审。没有人会问你的工作是否符合游戏愿景。</p>

<p>Claude Code Game Studios通过为你的AI会话赋予真实工作室结构来解决这个问题。你得到的不是一个通用助手，而是按工作室层级组织的49个专业Agent：</p>

<ul>
  <li><strong>总监</strong>守护愿景</li>
  <li><strong>部门主管</strong>管理各自领域</li>
  <li><strong>专家</strong>执行具体任务</li>
</ul>

<p>每个Agent有清晰的职责、晋升路径和质量控制点。你仍然做每个决策，但你有一个团队会问正确的问题、及早发现错误、从头脑风暴到发布始终保持项目有序。</p>

<h2 id="how-it-works">工作原理</h2>

<h3>智能Agent协调</h3>

<p>Agent遵循结构化的委托模型：</p>

<ol>
  <li><strong>垂直委托</strong>：总监分配任务给部门主管，部门主管再分配给专家Agent。</li>
  <li><strong>水平协商</strong>：同级Agent可互相协商，但不能做出有约束力的跨领域决策。</li>
  <li><strong>冲突解决</strong>：分歧升级到共同领导（设计问题由创意总监，技术问题由技术总监）。</li>
  <li><strong>变更传播</strong>：跨部门变更由制作人协调。</li>
  <li><strong>领域边界</strong>：Agent不会修改其明确授权范围之外的文件。</li>
</ol>

<h3>协作而非自主</h3>

<p>每个Agent遵循严格的协作协议：</p>

<ol>
  <li><strong>提问</strong>：Agent在提出方案前会先提问。</li>
  <li><strong>提供选项</strong>：Agent会提供2-4个选项及优缺点。</li>
  <li><strong>你决定</strong>：最终决策权始终在你手中。</li>
  <li><strong>起草</strong>：Agent起草方案供你审阅。</li>
  <li><strong>批准</strong>：未经你明确批准，不会写入任何文件。</li>
</ol>

<h2 id="conclusion">总结</h2>

<p>过去，游戏开发需要策划、程序员、美术、音乐和测试组成的完整团队。现在，你只需将游戏想法告诉Claude Code，它会一步步帮你构建游戏。Claude Code Game Studios让单人游戏开发比以往任何时候都更容易，专业工作室的结构和支持触手可及。</p>

<h2>常见问题</h2>

<h3>这和直接让Claude Code帮我做游戏有什么不同？</h3>
<p>没有Game Studios，Claude Code是通用助手——它能写代码，但不会主动询问你的游戏设计文档、在你修改UI时提醒更新HUD规范、或标记你的新机制与既定美术风格冲突。Game Studios添加了<strong>流程</strong>。49个Agent充当内置质量关卡：创意总监确保与愿景一致，技术总监捕捉架构问题，制作人追踪进度。这就像拥有一个聪明助手和拥有整个工作室的制度化知识嵌入工作流之间的区别。</p>

<h3>需要手动配置全部49个Agent吗？</h3>
<p>不需要。项目设计为开箱即用。49个Agent、73个技能、12个钩子、11条规则和41个模板已预配置。克隆仓库，在Claude Code中打开，工作室结构就绪。斜杠命令（/start、/design-system、/create-epics等）是主要接口——你触发工作流，相应的Agent自动激活。随时间推移，你可以自定义Agent、添加自己的技能、调整规则以匹配项目特定需求，但上手零配置。</p>

<h3>只支持2D游戏还是也支持3D？</h3>
<p>Claude Code Game Studios与引擎无关，与维度无关。Agent、技能和模板围绕游戏开发<strong>流程</strong>设计——设计文档、任务拆解、代码审查、资产管理、测试——而非特定技术。无论你在Godot做2D像素平台游戏、在Unity做3D RPG，还是做文字叙事游戏，工作室结构都同样适用。领域特定规则（玩法、引擎、AI、UI、网络）无论技术栈如何都适用。</p>

<h3>能给团队项目用吗，还是只能单人？</h3>
<p>为单人开发者设计，但也适用于小团队。在团队环境中，Agent充当共享流程层——团队中每个人都与同一工作室结构交互，确保一致的文档、代码标准和评审流程。制作人Agent对团队特别有价值，追踪跨成员依赖和标记集成风险。注意事项：Claude Code会话是每用户独立的，所以每个团队成员运行自己的实例。对于更大团队，需要补充共享项目管理工具来管理人协调层。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>对AI游戏开发感兴趣？深入探索：</p>
  <ul>
    <li><a href="/articles/vibecoding-contest-guide-game-animations-ai-tools">VibeCoding大赛指南：用AI工具高效制作游戏动画</a> — 实战动画工作流配套篇</li>
    <li><a href="/articles/complete-practical-tutorial-claude-code-core-operations">Claude Code完全实战教程：掌握所有核心操作</a> — 掌握本项目构建的基础</li>
    <li><a href="/articles/7-mainstream-agent-architectures-beginner-enterprise-guide">7大主流Agent架构：从入门到企业级完整指南</a> — 理解Game Studios背后的多Agent架构</li>
  </ul>
</div>`,
  },

'''

last_brace = content_src.rfind('};')
content_new = content_src[:last_brace] + new_contents + '};'

with open('src/lib/article-content.ts', 'w', encoding='utf-8') as f:
    f.write(content_new)

print('Part 2: 2 article contents added to article-content.ts')

print('\n=== All done! Run build to verify ===')