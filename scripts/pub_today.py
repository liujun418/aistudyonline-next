"""
Publish July 25, 2026 — 1 article, no new tools.
"""
import os

BASE = r"C:\Users\jun\aistudyonline-next"
os.chdir(BASE)

with open('src/lib/articles.ts', 'r', encoding='utf-8') as f:
    articles_src = f.read()

new_articles = r"""  {
    slug: "mastering-ai-image-generation-fix-prompt-issues-avoid-draw-failures",
    title: "Mastering AI Image Generation: How to Fix Prompt Issues and Avoid 'Draw Failures'",
    titleZh: "掌握AI图像生成：修复提示词问题，避免'翻车'",
    description: "A deep dive into common AI image generation failures — 'prompt pollution' (keyword association traps), the 'visual compensation' bug, and camera control workarounds — with practical fixes like word substitution, reverse-trap techniques, and direct visual element description.",
    descriptionZh: "深度解析AI图像生成常见失败——'提示词污染'（关键词关联陷阱）、'视觉补偿'Bug和相机控制技巧——含词汇替换、反向陷阱利用和直接视觉元素描述等实用修复方法。",
    category: "AI Tutorials",
    tags: ["AI Image Generation", "Prompt Engineering", "Midjourney", "DALL-E", "Tutorial", "Tips"],
    difficulty: "intermediate",
    toolsMentioned: ["Midjourney", "DALL-E"],
    date: "2026-07-25",
  },

"""

last_bracket = articles_src.rfind('];')
articles_new = articles_src[:last_bracket] + new_articles + '];'

with open('src/lib/articles.ts', 'w', encoding='utf-8') as f:
    f.write(articles_new)

print('Part 1: 1 article added')

with open('src/lib/article-content.ts', 'r', encoding='utf-8') as f:
    content_src = f.read()

new_contents = r'''
  "mastering-ai-image-generation-fix-prompt-issues-avoid-draw-failures": {
    content: `<div class="meta-banner">
  <span class="meta-badge">📚 AI Tutorials</span>
  <span class="meta-badge">🕒 5 min read</span>
  <span class="meta-badge">📅 Jul 25, 2026</span>
  <span class="meta-badge">🎯 Intermediate</span>
</div>

<h2 id="introduction">Introduction</h2>

<p>When you use AI to generate images like "a boy playing games on a phone", you might get strange results — like the boy holding the phone backward, just so the game screen is visible. Even though AI can create sci-fi blockbusters, it struggles with simple scenes like this. This article will break down why this happens and give you practical tips to fix it.</p>

<h2 id="prompt-pollution">Why Does This Happen? The "Prompt Pollution" Problem</h2>

<p>The real issue lies in your prompt. AI has a "keyword association trap" (or "prompt pollution"): when you mention a word, even a negated one, AI automatically fills in related stereotypes.</p>

<p>For example:</p>
<ul>
  <li>If you say "generate a person wearing a nurse cap", AI will not only add the cap but also a nurse uniform and a hospital background.</li>
  <li>Even if you say "generate a person not wearing a nurse cap", AI still puts them in a hospital.</li>
  <li>"Not wearing a safety helmet" → AI places the person at a construction site.</li>
  <li>"Not wearing a Christmas hat" → AI creates a Christmas scene.</li>
  <li>"Not wearing a chef hat" → AI shows a kitchen scene.</li>
</ul>

<p>The word "game" in your prompt becomes a "pollutant". AI prioritizes showing the game scene, even making the boy hold the phone backward to display the screen.</p>

<h2 id="fix-pollution">How to Fix It: Avoid the "Pollutant" Word</h2>

<p>The solution is simple: play a word game. Instead of "a boy playing games on the subway", rephrase it to "a boy sitting on the subway, holding the phone horizontally with both hands". By removing the "game" pollutant, the problem is solved.</p>

<h2 id="reverse-trap">Advanced Tip: Reverse the Trap</h2>

<p>You can even use this trap to your advantage. For example, when generating "a boy editing photos on a computer":</p>
<ul>
  <li>If you say "a boy looking at the front of the monitor", AI flips the screen so you (not the boy) can see it.</li>
  <li>Instead, say "a boy looking at the back of the monitor". This "ungrammatical" sentence for humans makes AI generate the correct image.</li>
</ul>

<p>Another example: Instead of "a man with eight-pack abs", use "a man with broad shoulders and narrow waist". This avoids the "abs" pollutant and still creates a fit look.</p>

<h2 id="visual-compensation">The "Visual Compensation" Bug</h2>

<p>Another issue is the "visual compensation" bug. AI lacks a perfect world model and can't understand abstract actions like "facing away" or "looking at". It compensates by drawing concrete visual elements:</p>
<ul>
  <li>"Facing away" → AI draws the back, backpack, and helmet.</li>
  <li>"Looking at" → AI draws the eyes, visor, and front face.</li>
</ul>

<p>When both "facing away" and "looking at" are in the prompt, AI compromises by showing a side view.</p>

<h2 id="fix-visual">How to Fix It: Describe Visual Elements Directly</h2>

<p>To generate an astronaut facing away from the camera and looking at Earth, avoid ambiguous words. Instead of "an astronaut standing on the moon, facing away from the camera, looking at Earth", use "an astronaut standing on the moon, facing away from the camera, with a planet Earth floating in the distant space". This describes the visual elements (the astronaut's back and Earth) instead of abstract actions.</p>

<h2 id="camera-control">Advanced: Control the Camera</h2>

<p>You can use visual compensation to control the camera:</p>
<ul>
  <li>To <strong>zoom in</strong> on an astronaut floating in space, describe details like "worn metal buckles, flashing indicator lights on the chest control panel, clear nylon woven texture on the arms". AI will focus on these details, effectively zooming in.</li>
  <li>For a <strong>close-up</strong>, describe the astronaut's face: "clear eyes through the visor, complex iris texture in the pupils, fine hairs on both sides of the nose".</li>
  <li>To change the <strong>shooting angle</strong>, describe elements from that angle. For a top-down view, say "the round top of the helmet, the shoulder contour visible from above, the top connector of the oxygen cylinder".</li>
</ul>

<h2 id="final-tips">Final Tips</h2>

<p>When generating images, avoid the mistake of first building the entire space and then placing the camera. Instead, describe what you can see in the scene. This will greatly reduce your chance of "drawing failures".</p>

<h2>常见问题</h2>

<h3>Why does AI add things I explicitly told it NOT to include?</h3>
<p>This is the "negation paradox" in prompt engineering. AI models don't process negation the way humans do — when you say "no hat", the model activates the concept of "hat" first, then tries to suppress it. The activation is stronger than the suppression, so hat-related elements (hairstyles, head accessories, sometimes even the hat itself) leak through. The fix: never use negation in image prompts. Instead of "a person without glasses", say "a person with clear, unobstructed eyes". Instead of "no background clutter", say "minimalist white background, empty space". This is the single most impactful habit change for better AI image generation.</p>

<h3>Does this advice apply to all AI image generators (Midjourney, DALL-E, Stable Diffusion)?</h3>
<p>Yes — the prompt pollution and visual compensation behaviors are universal across all major image generation models. They stem from how these models are trained (text-image pairs), not from any specific model's architecture. Midjourney is slightly more resilient to pollution because of its stronger aesthetic training, but it still exhibits the same patterns. DALL-E 3 is more literal and benefits most from the "describe visual elements directly" technique. Stable Diffusion is the most sensitive to prompt pollution and benefits most from the "avoid pollutant words" technique. The camera control trick (describing details to force zoom) works across all three.</p>

<h3>How do I know if my prompt has a "pollutant" word?</h3>
<p>Ask yourself: "If I remove this word, do I still convey the same visual?" If yes, the word is likely a pollutant. "A boy playing games" → "A boy holding a phone horizontally with both hands" — the visual is the same, but the pollutant "game" is gone. The test: generate both versions and compare. If the second version is more accurate, you found a pollutant. Common pollutants to watch for: action verbs (playing, eating, working), abstract roles (doctor, teacher, gamer), and emotional states (happy, sad, angry). Replace them with visual descriptions: what the person is physically doing, what they're wearing, what their expression looks like, what's in the environment.</p>

<h3>Can I use these techniques for video generation too?</h3>
<p>Yes — the same principles apply to AI video generation (Sora, Seedance, Runway, etc.) with one additional consideration: motion. For video prompts, you need to describe both the visual elements (using the techniques in this article) AND the motion. Example: instead of "a person walking happily", use "a person walking forward at a steady pace, arms swinging gently, hair bouncing with each step, slight smile on the face, bright sunlight casting moving shadows". The motion description replaces the abstract "happily" without introducing a pollutant word. The camera control trick (describing details to control framing) works for video too, but you'll also want to specify camera movement explicitly: "slow push-in, handheld style, slight vertical bounce".</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Mastered prompt fixes? Level up your AI image generation skills:</p>
  <ul>
    <li><a href="/articles/seedream-5-pro-ai-image-generation-guide">Seedream 5.0 Pro: A Comprehensive Practical Guide</a> — apply these prompt techniques to a specific model</li>
    <li><a href="/articles/ai-manhua-production-full-workflow-script-to-monetization">AI Manhua Production Full Workflow: From Script to Monetization</a> — use these skills in a complete production pipeline</li>
    <li><a href="/articles/dont-be-intimidated-ai-jargon-practical-guide-concepts">Don't Be Intimidated by AI Jargon: A Practical Guide to AI Concepts</a> — master prompt engineering fundamentals</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">📚 AI 教程</span>
  <span class="meta-badge">🕒 阅读约5分钟</span>
  <span class="meta-badge">📅 2026年7月25日</span>
  <span class="meta-badge">🎯 中级</span>
</div>

<h2 id="introduction">引言</h2>

<p>用AI生成"男孩在手机上玩游戏"时，你可能得到奇怪的结果——比如男孩把手机拿反了，只为了让游戏画面可见。即使AI能创作科幻大片，却在简单场景上翻车。本文拆解为什么发生这种情况，并给出实用修复技巧。</p>

<h2 id="prompt-pollution">为什么会这样？"提示词污染"问题</h2>

<p>真正的问题在于你的提示词。AI有一个"关键词关联陷阱"（或称"提示词污染"）：当你提到一个词，即使是否定的，AI也会自动填充相关的刻板印象。</p>

<p>例如：</p>
<ul>
  <li>说"生成一个戴护士帽的人"，AI不仅加帽子，还会加护士服和医院背景。</li>
  <li>即使说"生成一个不戴护士帽的人"，AI仍把人放在医院里。</li>
  <li>"不戴安全帽"→AI把人放在建筑工地。</li>
  <li>"不戴圣诞帽"→AI创造圣诞场景。</li>
  <li>"不戴厨师帽"→AI展示厨房场景。</li>
</ul>

<p>提示词中的"游戏"一词成为"污染物"。AI优先展示游戏画面，甚至让男孩反拿手机来显示屏幕。</p>

<h2 id="fix-pollution">如何修复：避开"污染物"词汇</h2>

<p>解决方案很简单：玩弄文字游戏。不写"男孩在地铁上玩游戏"，改写为"男孩坐在地铁上，双手横握手机"。去除"游戏"这个污染物，问题解决。</p>

<h2 id="reverse-trap">进阶技巧：反向利用陷阱</h2>

<p>你甚至可以利用这个陷阱。例如生成"男孩在电脑上编辑照片"：</p>
<ul>
  <li>说"男孩看着显示器正面"，AI翻转屏幕让你（而非男孩）能看到。</li>
  <li>改为"男孩看着显示器背面"。对人类来说这句话"不合语法"，却让AI生成正确的画面。</li>
</ul>

<p>另一个例子：不写"有八块腹肌的男人"，写"宽肩窄腰的男人"。避开"腹肌"污染物，仍创造健美的外观。</p>

<h2 id="visual-compensation">"视觉补偿"Bug</h2>

<p>另一个问题是"视觉补偿"Bug。AI缺乏完美的世界模型，无法理解"背对"或"看着"等抽象动作。它通过绘制具体视觉元素来补偿：</p>
<ul>
  <li>"背对"→AI画出背部、背包和头盔。</li>
  <li>"看着"→AI画出眼睛、面罩和正面脸部。</li>
</ul>

<p>当提示词中同时有"背对"和"看着"，AI妥协展示侧面视图。</p>

<h2 id="fix-visual">如何修复：直接描述视觉元素</h2>

<p>生成背对镜头看着地球的宇航员，避免模糊词汇。不写"宇航员站在月球上，背对镜头，看着地球"，写"宇航员站在月球上，背对镜头，远处太空飘浮着一颗蓝色星球"。这描述的是视觉元素（宇航员背影和地球）而非抽象动作。</p>

<h2 id="camera-control">进阶：控制镜头</h2>

<p>可以用视觉补偿来控制镜头：</p>
<ul>
  <li><strong>拉近</strong>太空漂浮宇航员：描述细节如"磨损的金属扣环、胸前控制面板闪烁的指示灯、手臂上清晰的尼龙编织纹理"。AI聚焦这些细节，相当于拉近镜头。</li>
  <li><strong>特写</strong>：描述宇航员面部"透过面罩清晰可见的眼睛，瞳孔中复杂的虹膜纹理，鼻梁两侧的细密绒毛"。</li>
  <li><strong>改变拍摄角度</strong>：从目标角度描述元素。俯视视角说"头盔圆顶、俯视可见的肩部轮廓、氧气瓶顶部连接器"。</li>
</ul>

<h2 id="final-tips">最后建议</h2>

<p>生成图片时，避免先构建整个空间再放置镜头的错误。改为描述场景中你能看到什么。这将大大降低"翻车"概率。</p>

<h2>常见问题</h2>

<h3>为什么AI会添加我明确说不要的东西？</h3>
<p>这是提示词工程中的"否定悖论"。AI模型不按人类方式处理否定——当你说"不要帽子"，模型先激活"帽子"概念，然后试图抑制它。激活强于抑制，所以帽子相关元素（发型、头饰，有时甚至是帽子本身）会泄露出来。修复方法：永远不在图像提示词中使用否定。不写"不戴眼镜的人"，写"眼睛清晰无遮挡的人"。不写"不要背景杂乱"，写"极简白色背景，空旷空间"。这是提升AI图像生成质量最具影响力的习惯改变。</p>

<h3>这些建议适用于所有AI图像生成器吗（Midjourney、DALL-E、Stable Diffusion）？</h3>
<p>适用——提示词污染和视觉补偿行为在所有主流图像生成模型中都存在。它们源于这些模型的训练方式（文本-图像对），而非任何特定模型架构。Midjourney因更强的美学训练对污染略有抵抗力，但仍表现出相同模式。DALL-E 3更字面化，从"直接描述视觉元素"技巧中获益最多。Stable Diffusion对提示词污染最敏感，从"避开污染物词汇"技巧中获益最多。镜头控制技巧（描述细节强制拉近）三者通用。</p>

<h3>怎么判断提示词中是否有"污染物"词汇？</h3>
<p>问自己："如果去掉这个词，我还能传达同样的视觉吗？"如果能，这个词很可能就是污染物。"男孩玩游戏"→"男孩双手横握手机"——视觉相同，但污染物"游戏"消失了。测试方法：两个版本都生成并对比。如果第二版更准确，你找到了污染物。常见的污染物包括：动作动词（玩、吃、工作）、抽象角色（医生、老师、游戏玩家）和情绪状态（开心、悲伤、愤怒）。用视觉描述替换它们：人在具体做什么、穿什么、表情是什么样、环境中有什么。</p>

<h3>这些技巧也能用于视频生成吗？</h3>
<p>可以——相同原则适用于AI视频生成（Sora、Seedance、Runway等），只需额外考虑运动。视频提示词需要同时描述视觉元素（使用本文技巧）和运动。示例：不写"一个人开心地走路"，写"一个人稳步向前走，手臂轻轻摆动，头发随步伐弹跳，脸上带着浅浅微笑，明亮阳光投下移动的阴影"。运动描述替换了抽象的"开心"，没有引入污染物词汇。镜头控制技巧（描述细节控制构图）对视频同样有效，但还需明确指定镜头运动："慢推镜，手持风格，轻微垂直晃动"。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>掌握了提示词修复？提升AI图像生成技能：</p>
  <ul>
    <li><a href="/articles/seedream-5-pro-ai-image-generation-guide">Seedream 5.0 Pro实战评测：国产顶流AI图像生成模型全指南</a> — 将提示词技巧应用到具体模型</li>
    <li><a href="/articles/ai-manhua-production-full-workflow-script-to-monetization">AI漫剧制作全流程：从剧本到变现的完整指南</a> — 在完整制作管线中使用这些技能</li>
    <li><a href="/articles/dont-be-intimidated-ai-jargon-practical-guide-concepts">别被AI术语吓倒：从ChatGPT到Workspace Agent的AI概念实战指南</a> — 掌握提示词工程基础</li>
  </ul>
</div>`,
  },

'''

last_brace = content_src.rfind('};')
content_new = content_src[:last_brace] + new_contents + '};'

with open('src/lib/article-content.ts', 'w', encoding='utf-8') as f:
    f.write(content_new)

print('Part 2: 1 article content added')
print('\n=== Done ===')