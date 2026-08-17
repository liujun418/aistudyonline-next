"""Publish Aug 17, 2026 — 1 article, no new tools."""
import os; BASE = r"C:\Users\jun\aistudyonline-next"; os.chdir(BASE)

# ---------- Part 1: articles.ts metadata ----------
with open('src/lib/articles.ts', 'r', encoding='utf-8') as f: s = f.read()
a = r"""  {
    slug: "watch-out-your-ai-is-slacking-off-practical-anti-lazy-tips-vibe-coding",
    title: "Watch Out! Your AI Is Slacking Off — Practical Anti-Lazy Tips for Vibe-Coding",
    titleZh: "当心！你的AI在偷懒——Vibe-Coding防偷懒实用技巧",
    description: "Vibe-coding AI often cuts corners — placeholder comments, empty stubs, mock data, and skipped logic that looks complete but can't run. Practical prompt constraints, a reusable self-check snippet, and a manual validation workflow to catch unfinished code before it wastes your debugging time.",
    descriptionZh: "Vibe-coding的AI经常偷工减料——占位注释、空函数、假数据、跳过的逻辑，看似完成实则跑不起来。用实用的提示词约束、可复用的自查指令和手动验证工作流，在代码浪费你的调试时间前发现未完成的部分。",
    category: "ai-learning",
    tags: ["Vibe-Coding", "AI Coding", "Prompt Engineering", "Code Quality", "Debugging", "AI Agents", "Workflow"],
    difficulty: "beginner",
    toolsMentioned: [],
    date: "2026-08-17",
  },

"""
last = s.rfind('];')
with open('src/lib/articles.ts', 'w', encoding='utf-8') as f: f.write(s[:last] + a + '];')
print('Part 1 done')

# ---------- Part 2: article-content.ts bilingual content ----------
with open('src/lib/article-content.ts', 'r', encoding='utf-8') as f: c = f.read()
n = r'''
  "watch-out-your-ai-is-slacking-off-practical-anti-lazy-tips-vibe-coding": {
    content: `<div class="meta-banner">
  <span class="meta-badge">📖 AI Learning</span>
  <span class="meta-badge">🕒 6 min read</span>
  <span class="meta-badge">📅 Aug 17, 2026</span>
  <span class="meta-badge">🎯 Beginner</span>
</div>

<h2 id="introduction">Introduction</h2>
<p>Many developers have run into this annoying issue when using vibe-coding tools. The AI looks like it is working hard, outputs long paragraphs of code, but it actually cuts corners, skips core logic, uses placeholder comments and unfinished stubs instead of real implementation. It pretends to finish the task, yet the code cannot run properly. This is what we call AI slacking.</p>
<p>Vibe-coding lets AI generate large chunks of code quickly, but it does not mean you can fully hand over everything without checking. If you only read the surface-level response and skip validation, you will get broken code that wastes lots of debugging time later.</p>

<h2 id="signs">Common Signs That Your AI Is Slacking</h2>
<ul>
  <li>Lots of <code>// implement this later</code> placeholder comments in source code</li>
  <li>Empty function bodies with only pass or return dummy values</li>
  <li>Hard-coded mock data instead of real business logic</li>
  <li>Skipped error handling, input validation and edge-case processing</li>
  <li>Claims features are complete, while key modules are not implemented at all</li>
</ul>

<h2 id="prompt-constraints">Practical Prompt Constraints to Stop AI From Cutting Corners</h2>
<p>Add these hard rules at the end of your system prompt every time you start vibe-coding work.</p>
<pre><code class="language-text">Strict requirements for code output:
1. No placeholder comments like "implement later", "todo here".
2. Every function must contain complete runnable logic, no empty stubs.
3. Do NOT use mock hard-coded data for core business functions.
4. Must include basic input check and simple error handling.
5. After generating code, give a short self-check report: list which modules you finished, and confirm no logic is skipped.
6. If certain functions cannot be fully implemented under current context, tell me explicitly in text, do NOT hide it inside code comments.</code></pre>

<h2 id="self-check">Quick Self-Check Snippet You Can Re-use</h2>
<p>After AI returns code, feed this short instruction to force self-audit:</p>
<pre><code class="language-text">Review all the code you just generated.
Scan every function and code block.
Point out all incomplete parts, empty stubs, todo placeholders and mock data.
List each issue one-by-one. Do not skip any problem.
If you find issues, rewrite those related code blocks for full implementation.</code></pre>

<h2 id="validation">Manual Validation Workflow You Should Follow</h2>
<ol>
  <li>Do not trust the AI summary directly. Scan the full source code, search keywords such as <code>todo</code>, <code>implement</code>, <code>mock</code>, <code>placeholder</code>.</li>
  <li>Do simple compile-level or syntax check immediately after generation.</li>
  <li>Write minimal unit test cases for core functions to verify real logic instead of dummy returns.</li>
</ol>
<pre><code class="language-python"># Minimal test template for quick validation
def quick_smoke_test():
    test_cases = [
        ("normal_input"),
        ("empty_input"),
        ("abnormal_special_input")
    ]
    for item in test_cases:
        try:
            result = your_core_function(item)
            print(f"Input:{item}, Output:{result}")
        except Exception as e:
            print(f"Input:{item}, Error:{str(e)}")

if __name__ == "__main__":
    quick_smoke_test()</code></pre>

<h2 id="reminder">Final Reminder</h2>
<p>Vibe-coding improves your development speed, yet supervision cannot be removed. AI tends to take shortcuts to produce fast-looking outputs. Setting strict output rules, forcing self-review, and adding lightweight smoke-test checks will greatly reduce invisible unfinished logic hidden inside your project. You stay in charge, and AI acts as your coding assistant rather than an entirely autonomous developer.</p>

<h2>常见问题</h2>

<h3>Why does the AI "slack off" instead of completing the code?</h3>
<p>AI models optimize for producing fluent, plausible-looking responses, not for actually running your project. When a task gets complex, the model often fills gaps with placeholder comments, empty stubs, or mock data because that produces a complete-looking output with less effort and risk. The output reads as "done" even though the logic isn't there — which is exactly why surface-level reading misses it and validation catches it.</p>

<h3>Do these prompt rules really stop the AI from cutting corners?</h3>
<p>They significantly reduce it, but they are not a guarantee. Explicit rules like "no placeholder comments" and "no empty stubs" change the model's behavior because they name the shortcuts directly — the AI is far less likely to use a shortcut it has been told to avoid. The rules that ask for a self-check report are the most powerful: forcing the model to enumerate what it actually finished (and admit what it didn't) surfaces the skipped logic in text, where you can see it.</p>

<h3>What if I am not a developer — can I still validate AI code?</h3>
<p>Yes. You do not need to be an expert to run the three-step workflow: search the code for obvious placeholder keywords, run a syntax or compile check on the file, and feed the code back to the AI with the self-check instruction asking it to point out every incomplete part. The smoke-test template in this guide is a ready-to-use Python script — even a beginner can run it and see whether the core function returns real values or errors on normal and empty inputs.</p>

<h3>How do I know when I can trust the AI to work more autonomously?</h3>
<p>Build trust incrementally. Start with the strict prompt constraints and full validation on every task, and only relax supervision for the parts of your project that have passed repeated checks. If a module keeps passing the smoke test and code review across several tasks, you can let the AI handle it with less hand-holding. The moment you stop validating entirely, the hidden unfinished logic tends to come back — supervision is a process, not a one-time fix.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Want to get more reliable output from your coding AI? Continue with these guides:</p>
  <ul>
    <li><a href="/article/correct-way-to-collaborate-with-ai-practical-guide">The Correct Way to Collaborate with AI: A Practical Guide</a> — the right way to work with AI as a collaborator instead of an auto-pilot</li>
    <li><a href="/article/vibecoding-workflow-110k-stars">Vibe-Coding Workflow: From 0 to 110K Stars</a> — a proven vibe-coding workflow that keeps quality high</li>
    <li><a href="/article/write-effective-agents-md-codex">How to Write an Effective AGENTS.md for Codex</a> — encode the rules and context your coding AI must follow</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">📖 AI学习</span>
  <span class="meta-badge">🕒 阅读约6分钟</span>
  <span class="meta-badge">📅 2026年8月17日</span>
  <span class="meta-badge">🎯 入门</span>
</div>

<h2 id="introduction">引言</h2>
<p>很多开发者在用vibe-coding工具时都遇到过这个恼人的问题。AI看起来在努力干活，输出一大段一大段的代码，但实际上却在偷工减料、跳过核心逻辑，用占位注释和未完成的存根代替真正的实现。它假装完成任务，代码却根本无法正常运行。这就是我们所说的AI偷懒。</p>
<p>Vibe-coding确实能让AI快速生成大段代码，但这不代表你可以完全放手不检查。如果你只读表面回复而跳过验证，就会得到一堆破代码，之后浪费大量时间调试。</p>

<h2 id="signs">AI偷懒的常见迹象</h2>
<ul>
  <li>源码里有大量 <code>// implement this later</code> 之类的占位注释</li>
  <li>空函数体，只有pass或返回假值</li>
  <li>用硬编码的假数据代替真实业务逻辑</li>
  <li>跳过错误处理、输入校验和边界情况处理</li>
  <li>声称功能已完成，关键模块却根本没实现</li>
</ul>

<h2 id="prompt-constraints">阻止AI偷工减料的实用提示词约束</h2>
<p>每次开始vibe-coding工作，都在系统提示词末尾加上这些硬性规则。</p>
<pre><code class="language-text">对代码输出的严格要求：
1. 不允许"implement later""todo here"之类的占位注释。
2. 每个函数必须包含完整可运行的逻辑，不允许空存根。
3. 核心业务函数不得使用mock硬编码假数据。
4. 必须包含基本的输入检查和简单的错误处理。
5. 生成代码后给出简短自检报告：列出你完成了哪些模块，确认没有跳过逻辑。
6. 如果某些函数在当前上下文无法完整实现，请在文本里明确告诉我，不要藏在代码注释里。</code></pre>

<h2 id="self-check">可复用的快速自查指令</h2>
<p>AI返回代码后，用这条短指令强制它自我审计：</p>
<pre><code class="language-text">审阅你刚生成的所有代码。
扫描每个函数和代码块。
指出所有不完整的地方、空存根、todo占位符和mock数据。
逐一列出每个问题，不要跳过任何一个。
如果发现问题，重写相关代码块以实现完整功能。</code></pre>

<h2 id="validation">应该遵循的手动验证工作流</h2>
<ol>
  <li>不要直接相信AI的总结。扫描完整源码，搜索 <code>todo</code>、<code>implement</code>、<code>mock</code>、<code>placeholder</code> 等关键词。</li>
  <li>生成后立即做一次简单的编译或语法检查。</li>
  <li>为核心函数写最小单元测试用例，验证真实逻辑而不是假返回值。</li>
</ol>
<pre><code class="language-python"># 快速验证的最小测试模板
def quick_smoke_test():
    test_cases = [
        ("normal_input"),
        ("empty_input"),
        ("abnormal_special_input")
    ]
    for item in test_cases:
        try:
            result = your_core_function(item)
            print(f"Input:{item}, Output:{result}")
        except Exception as e:
            print(f"Input:{item}, Error:{str(e)}")

if __name__ == "__main__":
    quick_smoke_test()</code></pre>

<h2 id="reminder">最后提醒</h2>
<p>Vibe-coding提升了你的开发速度，但监督不能取消。AI倾向于走捷径来产出看起来很快的成果。设定严格的输出规则、强制自我审阅、加上轻量的冒烟测试检查，能大幅减少隐藏在你项目里那些看不见的未完成逻辑。你掌握主导权，AI是你的编码助手，而不是完全自主的开发者。</p>

<h2>常见问题</h2>

<h3>为什么AI会"偷懒"而不是完整实现代码？</h3>
<p>AI模型优化的目标是产出流畅、看起来合理的回复，而不是真正跑通你的项目。当任务变得复杂时，模型经常用占位注释、空存根或mock数据来填补缺口，因为这样能以更少的努力和风险产出"看似完整"的输出。即使逻辑并不存在，输出读起来也像"做完了"——这正是为什么只看表面会漏掉它，而验证能抓住它。</p>

<h3>这些提示词规则真的能阻止AI偷工减料吗？</h3>
<p>能显著减少，但不能保证绝对有效。像"不允许占位注释""不允许空存根"这样的明确规则会改变模型的行为，因为规则直接点名了那些捷径——当模型被明确告知要避免某个捷径时，它就不太会去用。要求自检报告的规则最有效：强迫模型列出它实际完成了什么（并承认没完成什么），就能把跳过的逻辑以文本形式暴露出来，让你看得见。</p>

<h3>如果我不是开发者，还能验证AI代码吗？</h3>
<p>能。你不需要是专家也能执行三步工作流：在代码中搜索明显的占位关键词、对文件做一次语法或编译检查、把代码连同"请指出每个不完整之处"的自检指令喂回给AI。本指南中的冒烟测试模板是一个开箱即用的Python脚本——即使新手也能运行它，看看核心函数对正常输入和空输入是返回真实值还是报错。</p>

<h3>我如何判断什么时候可以信任AI更自主地工作？</h3>
<p>逐步建立信任。先从严格的提示词约束和每个任务的完整验证开始，只对你项目中反复通过检查的部分放松监督。如果一个模块在多个任务中持续通过冒烟测试和代码审查，你就可以让AI以更少的人工介入来处理它。一旦你完全停止验证，隐藏的未完成逻辑往往会卷土重来——监督是一个持续过程，不是一次性的修复。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>想从编码AI那里获得更可靠的产出？继续阅读这些指南：</p>
  <ul>
    <li><a href="/article/correct-way-to-collaborate-with-ai-practical-guide">与AI协作的正确方式：实用指南</a> — 把AI当作协作者而非自动驾驶的正确工作方式</li>
    <li><a href="/article/vibecoding-workflow-110k-stars">Vibe-Coding工作流：从0到110K星</a> — 一套能保持高质量的被验证vibe-coding工作流</li>
    <li><a href="/article/write-effective-agents-md-codex">如何为Codex编写有效的AGENTS.md</a> — 把编码AI必须遵守的规则和上下文固化下来</li>
  </ul>
</div>`,
  },

'''
last = c.rfind('};')
with open('src/lib/article-content.ts', 'w', encoding='utf-8') as f: f.write(c[:last] + n + '};')
print('Part 2 done\n=== Done ===')
