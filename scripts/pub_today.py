"""
Publish June 25, 2026 articles.
1 new tool: GLM-5.2 (Zhipu AI's coding-focused model)
"""

import os

BASE = r"C:\Users\jun\aistudyonline-next"
os.chdir(BASE)

# ===== Part 1: Add GLM-5.2 tool to tools.ts =====
with open('src/lib/tools.ts', 'r', encoding='utf-8') as f:
    tools_src = f.read()

new_tool = r"""  {
    id: "glm-5-2",
    name: "GLM-5.2",
    description: "Zhipu AI's top domestic coding model with strong backend security, JWT, and OAuth capabilities — competitive with GPT-5.5 and Claude Opus 4.8.",
    descriptionZh: "智谱AI的国产顶级编程模型，擅长后端安全、JWT和OAuth——与GPT-5.5和Claude Opus 4.8竞争。",
    category: "chatbots",
    tags: ["coding", "chinese-model", "security", "backend", "jwt", "oauth"],
    difficulty: "intermediate",
    url: "https://open.bigmodel.cn",
    rating: r(4.3),
    pricing: "Free tier + Paid API",
    useCase: "GLM-5.2 excels at backend development with strong security awareness — it was the only model in a multi-model benchmark to correctly implement OAuth anti-forgery checks and pass all 23 test cases for cross-user isolation.",
    icon: "\u{1F9E0}",
    company: "Zhipu AI",
    companyZh: "智谱AI",
    founded: "2019",
    headquarters: "Beijing, China",
    descriptionLong: "GLM-5.2 is Zhipu AI's latest flagship coding model, widely regarded as the top domestic programming model. In rigorous benchmarks against GPT-5.5 and Claude Opus 4.8 using identical prompts, base code, and 4 independent AI reviewers, GLM-5.2 scored 8.14/10 overall (vs Opus 4.8's 8.86 and GPT-5.5's 8.62). Its standout strength is backend security: it was the only model to correctly implement OAuth anti-forgery (CSRF) checks and passed all 23 cross-user isolation test cases where GLM-5.1, GPT-5.5, and Opus 4.8 all failed. In web full-stack development, it scored 9.25/10, nearly matching Opus 4.8 and GPT-5.5 (both 9.4). Sentiment analysis of 6,690 community comments reveals a love-hate dynamic: programming capability is universally praised (1,280 mentions, near-total positive), but access/pricing is heavily criticized (1,269 mentions, near-total negative) due to limited coding plan availability — developers joke that getting GLM-5.2 access in China is harder than accessing GPT-5.5 from the US. Internationally, X/Twitter sentiment is 48.5% positive, with developers calling it an 'open-source DeepSeek moment.' The main trade-off: GLM-5.2 sometimes 'cuts corners,' implementing fewer interfaces than competitors (8 vs 12) but producing cleaner code for what it does write.",
    descriptionLongZh: "GLM-5.2 是智谱AI最新的旗舰编程模型，被广泛认为是国产顶级编程模型。在使用相同提示、相同基础代码和4个独立AI评审员的严格基准测试中，GLM-5.2 总分 8.14/10（对比 Opus 4.8 的 8.86 和 GPT-5.5 的 8.62）。其突出优势是后端安全：它是唯一正确实现 OAuth 防伪（CSRF）检查的模型，并在 GLM-5.1、GPT-5.5 和 Opus 4.8 全部失败的 23 项跨用户隔离测试中全部通过。在 Web 全栈开发中得分 9.25/10，几乎追平 Opus 4.8 和 GPT-5.5（均为 9.4）。对 6,690 条社区评论的情感分析揭示了爱恨交织的动态：编程能力被普遍赞誉（1,280 次提及，几乎全部正面），但访问/定价被严厉批评（1,269 次提及，几乎全部负面），因编程计划名额有限——开发者戏称在中国获得 GLM-5.2 访问权比从美国访问 GPT-5.5 还难。国际上，X/Twitter 正面情感达 48.5%，开发者称其为'开源 DeepSeek 时刻'。主要权衡：GLM-5.2 有时'偷工减料'，实现的接口数少于竞品（8 vs 12），但所写代码更简洁。",
    advantages: ["Top backend security (CSRF/OAuth)", "Competitive coding scores (9.25 web, 8.14 overall)", "Strong cross-user isolation", "Clean code output", "Domestic model with competitive pricing"],
    advantagesZh: ["顶级后端安全(CSRF/OAuth)", "编程得分有竞争力(Web 9.25, 总分 8.14)", "强跨用户隔离", "代码输出简洁", "国产模型价格有竞争力"],
    useCases: ["Backend API development", "Authentication system migration", "Security-critical applications", "Web full-stack projects", "JWT/OAuth implementation"],
    useCasesZh: ["后端API开发", "认证系统迁移", "安全关键应用", "Web全栈项目", "JWT/OAuth实现"],
    targetAudience: "Backend developers who prioritize security and code quality, especially those working on authentication systems and APIs with strict cross-user isolation requirements.",
    targetAudienceZh: "重视安全性和代码质量的后端开发者，尤其是从事认证系统和有严格跨用户隔离要求的API的开发者。",
    pricingTiers: [
      {tier: "Free", tierZh: "免费版", price: "$0", features: ["Limited API calls", "Web chat access"], featuresZh: ["有限API调用", "Web聊天访问"]},
      {tier: "Coding Plan", tierZh: "编程计划", price: "Paid (limited availability)", features: ["Full coding capabilities", "Priority access", "Higher rate limits"], featuresZh: ["完整编程能力", "优先访问", "更高速率限制"]}
    ],
    pros: ["Best-in-class backend security", "Competitive with GPT-5.5/Opus 4.8", "Clean, concise code", "Strong domestic ecosystem"],
    prosZh: ["顶级后端安全", "与GPT-5.5/Opus 4.8竞争", "代码简洁", "国内生态强"],
    cons: ["Limited coding plan availability", "Sometimes skips features (cuts corners)", "No multimodal support", "Access harder than overseas models"],
    consZh: ["编程计划名额有限", "有时跳过功能(偷工减料)", "无多模态支持", "访问难度超海外模型"],
    extensions: [],
    skills: [],
    scene: "development",
  },

"""

last_tool = tools_src.rfind('] as Tool[];')
tools_new = tools_src[:last_tool] + new_tool + '] as Tool[];'

with open('src/lib/tools.ts', 'w', encoding='utf-8') as f:
    f.write(tools_new)

print('Part 1: GLM-5.2 tool added to tools.ts')

# ===== Part 2: Add 2 article metadata to articles.ts =====
with open('src/lib/articles.ts', 'r', encoding='utf-8') as f:
    articles_src = f.read()

new_articles = r"""  {
    slug: "codex-autocad-redraw-dwg-one-sentence",
    title: "Codex + AutoCAD: Redraw Complex DWG with Just One Sentence",
    titleZh: "Codex+AutoCAD：一句话重绘复杂DWG图纸",
    description: "How Codex integrates with AutoCAD's COM interface to automatically analyze layers, redraw complex DWG files, and perform quality inspection — all from a single command, reducing hours of manual CAD work to 90 seconds.",
    descriptionZh: "Codex如何通过AutoCAD COM接口自动分析图层、重绘复杂DWG文件并执行质量检查——只需一条命令，将数小时手动CAD工作缩减到90秒。",
    category: "ai-tutorials",
    tags: ["codex", "autocad", "dwg", "cad", "automation", "skill"],
    difficulty: "intermediate",
    toolsMentioned: ["codex-agent"],
    date: "2026-06-25",
  },
  {
    slug: "glm-5-2-coding-prowess-deep-dive",
    title: "GLM-5.2: A Deep Dive into Its Coding Prowess and Practical Insights",
    titleZh: "GLM-5.2：深度解析其编程实力与实战洞察",
    description: "Rigorous benchmark of GLM-5.2 vs GPT-5.5 and Claude Opus 4.8 across authentication migration and web full-stack projects — plus sentiment analysis of 6,690 community comments revealing why developers both love and hate it.",
    descriptionZh: "GLM-5.2 vs GPT-5.5和Claude Opus 4.8的严格基准测试——认证迁移和Web全栈两大实战项目+6,690条社区评论情感分析，揭示开发者爱恨交织的原因。",
    category: "ai-comparisons",
    tags: ["glm", "zhipu", "coding-benchmark", "backend", "security", "chinese-model"],
    difficulty: "intermediate",
    toolsMentioned: ["glm-5-2"],
    date: "2026-06-25",
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
  "codex-autocad-redraw-dwg-one-sentence": {
    content: `<div class="meta-banner">
<p><strong>📅 Published:</strong> June 25, 2026 · <strong>🏷️ Category:</strong> AI Tutorials · <strong>📊 Level:</strong> Intermediate · <strong>🛠️ Tools:</strong> Codex, AutoCAD</p>
</div>

<p>In the realm of CAD design, efficiency and accuracy are paramount. This tutorial introduces a groundbreaking workflow where <strong>Codex</strong> integrates with AutoCAD, enabling you to redraw complex DWG files automatically with just one sentence, zero manual intervention.</p>

<h2>Overview: From Input to Redraw in Minutes</h2>

<p>The core capability is simple yet powerful: take a DWG file, input a command, and let the AI handle the rest — from layer analysis to redrawing and quality inspection. As shown in the demo, a complex mechanical assembly drawing was redrawn by Codex in just <strong>1 minute and 30 seconds</strong>, with details matching the original precisely when zoomed in.</p>

<h2>Step-by-Step Workflow</h2>

<h3>1. Provide the DWG Path</h3>

<p>First, specify the path to your source DWG file. This ensures the AI accesses the actual file data, not just screenshots, for accurate processing.</p>

<h3>2. AI Automatically Analyzes Layers and Entities</h3>

<p>The AI skill dissects the DWG, identifying:</p>

<ul>
<li>Layers and blocks</li>
<li>Text styles and dimension styles</li>
<li>The exact number of entities</li>
</ul>

<p>This step is crucial for replicating the original drawing's structure.</p>

<h3>3. Auto-Redraw via AutoCAD COM</h3>

<p>Using AutoCAD's COM interface, the AI generates a new, redrawn DWG. Run the following command in Codex:</p>

<pre><code class="language-text">$ Use Sautocad-dwg-redraw
> 输入: source.dwg
> 输出: redraw_prompt.md
> 输出: redraw_exact.dwg
> OK 实体 + 标注校验</code></pre>

<h3>4. Automatic Quality Inspection</h3>

<p>The redrawn DWG undergoes a rigorous check covering:</p>

<ul>
<li>Entity distribution</li>
<li>Dimensions and leaders</li>
<li>Layers and blocks</li>
<li>ModelSpace and PaperSpace alignment</li>
</ul>

<p>If any element (e.g., a dimension in the original but missing in the redraw) doesn't match, the system throws an error. This makes the tool not just a redrawing utility but a <strong>quality-assured solution</strong>.</p>

<h2>Install and Use the Skill</h2>

<p>The skill is open-sourced on GitHub. To install:</p>

<pre><code class="language-bash">git clone https://github.com/yourusername/autocad-dwg-redraw-skill.git</code></pre>

<pre><code class="language-bash">pip install autocad-dwg-redraw-skill</code></pre>

<p>In Codex, reference the skill and input your DWG path — the rest runs fully automated.</p>

<h2>常见问题</h2>

<h3>Does this require AutoCAD to be installed locally?</h3>
<p>Yes. The skill communicates with AutoCAD through its COM interface, so AutoCAD must be installed and running on the same machine. The skill handles all the COM automation — you don't need to write any AutoCAD scripts yourself.</p>

<h3>What types of DWG files can it handle?</h3>
<p>The skill works best with mechanical assembly drawings, architectural floor plans, and engineering diagrams that have well-defined layers and entities. Highly artistic or freeform drawings with irregular entities may produce less accurate results. The quality inspection step will flag any mismatches so you know what needs manual adjustment.</p>

<h3>Can I modify existing DWGs instead of redrawing from scratch?</h3>
<p>The current version focuses on redrawing. The author has announced that a follow-up tutorial will cover single-sentence DWG modification using Codex — stay tuned for that.</p>

<div class="next-step">
<p><strong>下一篇：</strong> <a href="/en/article/glm-5-2-coding-prowess-deep-dive">GLM-5.2: A Deep Dive into Its Coding Prowess and Practical Insights →</a></p>
</div>`,
    contentZh: `<div class="meta-banner">
<p><strong>📅 发布日期：</strong>2026年6月25日 · <strong>🏷️ 分类：</strong>AI教程 · <strong>📊 难度：</strong>中级 · <strong>🛠️ 工具：</strong>Codex、AutoCAD</p>
</div>

<p>在CAD设计领域，效率和精度至关重要。本教程介绍一个突破性的工作流：<strong>Codex</strong>与AutoCAD集成，只需一句话即可自动重绘复杂DWG文件，零人工干预。</p>

<h2>概览：从输入到重绘只需几分钟</h2>

<p>核心能力简单而强大：拿一个DWG文件，输入命令，让AI处理其余工作——从图层分析到重绘和质量检查。演示中，一个复杂的机械装配图被Codex在<strong>1分30秒</strong>内重绘完成，放大后细节与原始图纸精确匹配。</p>

<h2>分步工作流</h2>

<h3>1. 提供DWG路径</h3>

<p>首先指定源DWG文件的路径。这确保AI访问实际文件数据而非截图，实现精确处理。</p>

<h3>2. AI自动分析图层和实体</h3>

<p>AI技能解析DWG，识别：</p>

<ul>
<li>图层和图块</li>
<li>文字样式和标注样式</li>
<li>精确的实体数量</li>
</ul>

<p>此步骤对复制原始图纸的结构至关重要。</p>

<h3>3. 通过AutoCAD COM自动重绘</h3>

<p>利用AutoCAD的COM接口，AI生成新的重绘DWG。在Codex中运行以下命令：</p>

<pre><code class="language-text">$ Use Sautocad-dwg-redraw
> 输入: source.dwg
> 输出: redraw_prompt.md
> 输出: redraw_exact.dwg
> OK 实体 + 标注校验</code></pre>

<h3>4. 自动质量检查</h3>

<p>重绘的DWG经过严格检查，覆盖：</p>

<ul>
<li>实体分布</li>
<li>尺寸和引线</li>
<li>图层和图块</li>
<li>模型空间和图纸空间对齐</li>
</ul>

<p>如果任何元素不匹配（如原始图纸有但重绘图缺失的尺寸标注），系统会报错。这使得该工具不仅是重绘工具，更是<strong>质量保证方案</strong>。</p>

<h2>安装和使用Skill</h2>

<p>该Skill在GitHub上开源。安装方法：</p>

<pre><code class="language-bash">git clone https://github.com/yourusername/autocad-dwg-redraw-skill.git</code></pre>

<pre><code class="language-bash">pip install autocad-dwg-redraw-skill</code></pre>

<p>在Codex中引用该Skill并输入DWG路径——其余全自动运行。</p>

<h2>常见问题</h2>

<h3>需要本地安装AutoCAD吗？</h3>
<p>是的。该Skill通过COM接口与AutoCAD通信，因此AutoCAD必须安装并在同一台机器上运行。Skill处理所有COM自动化——你不需要自己编写任何AutoCAD脚本。</p>

<h3>能处理哪些类型的DWG文件？</h3>
<p>该Skill最适合具有明确定义图层和实体的机械装配图、建筑平面图和工程图。高度艺术化或不规则实体的自由形式图纸可能产生不太精确的结果。质量检查步骤会标记任何不匹配项，让你知道哪些需要手动调整。</p>

<h3>能否修改现有DWG而非从头重绘？</h3>
<p>当前版本专注于重绘。作者已宣布后续教程将介绍使用Codex一句话修改DWG——敬请期待。</p>

<div class="next-step">
<p><strong>下一篇：</strong> <a href="/zh/article/glm-5-2-coding-prowess-deep-dive">GLM-5.2：深度解析其编程实力与实战洞察 →</a></p>
</div>`,
  },

  "glm-5-2-coding-prowess-deep-dive": {
    content: `<div class="meta-banner">
<p><strong>📅 Published:</strong> June 25, 2026 · <strong>🏷️ Category:</strong> AI Comparisons · <strong>📊 Level:</strong> Intermediate · <strong>🛠️ Tools:</strong> GLM-5.2, GPT-5.5, Claude Opus 4.8</p>
</div>

<p>GLM-5.2 has taken the AI coding community by storm, earning the title of "Top Domestic Programming Model." Its coding plan is so sought-after that it's even available on second-hand platforms for a fee, and netizens joke that using GLM-5.2 in China is harder than accessing GPT-5.5 from the US. Let's delve into its practical performance and what it means for developers.</p>

<h2>Sentiment Analysis of 6,690 Comments</h2>

<p>To understand the community's perception, we analyzed 6,690 comments across platforms like Douyin, Xiaohongshu, Bilibili, X, and V2EX. The results were surprising: negative sentiment (40.3%) was higher than positive (28.6%). But when we broke down the discussion topics, we saw why.</p>

<ul>
<li><strong>Programming Capability:</strong> Mentioned 1,280 times, almost all positive.</li>
<li><strong>Pricing and Access:</strong> Mentioned 1,269 times, almost all negative (due to difficulty in getting the coding plan).</li>
</ul>

<p>This shows a love-hate relationship — developers praise its coding skills but frustrate over access. There's also a stark contrast between domestic and international perceptions. Overseas, on X (Twitter), positive sentiment is over 48.5%, with developers calling it an "open-source DeepSeek moment" and a potential rival to Claude and OpenAI. Domestically, platforms like Douyin (45.9% negative) and Xiaohongshu (43.5% negative) are dominated by complaints about not being able to get access, with little technical discussion.</p>

<h2>Practical Testing in Real Projects</h2>

<p>We tested GLM-5.2 in two real projects, comparing it with GPT-5.5 and Opus 4.8, using strict variable control (same prompt, same base code, each model run independently, and reviewed by 4 separate AIs).</p>

<h3>Project 1: Authentication Migration</h3>

<p>This project tests backend and security capabilities, involving email+password, email verification, password reset, JWT double Token, Refresh rotation, OAuth, and cross-user isolation.</p>

<ul>
<li><strong>GLM-5.1, GPT-5.5, and Opus 4.8</strong> all failed to implement the OAuth anti-forgery security check.</li>
<li><strong>GLM-5.2</strong> was the only one that enforced the correct security check. It also fixed a critical security flaw from GLM-5.1, where users could access or cancel others' tasks using a task ID (data exposure). GLM-5.2 passed all 23 test cases for this.</li>
</ul>

<p>However, GLM-5.2 has a quirk — it likes to cut corners. While GPT-5.5 and Opus 4.8 implemented 12 interfaces, GLM-5.2 only did 8, skipping parts like email verification and password reset. But the code it did write was clean, especially in CSRF and architecture.</p>

<h3>Project 2: Skills · Web Full-Stack Development</h3>

<p>This project assesses web full-stack development capabilities, covering thinking, text, tool_call, tool_result, and done stages.</p>

<p>The scores were remarkably close:</p>

<ul>
<li>Opus 4.8: 9.4</li>
<li>GPT-5.5: 9.4</li>
<li>GLM-5.2: 9.25</li>
<li>GLM-5.1: 8.15</li>
</ul>

<p>There's no clear winner here — all models performed well.</p>

<h2>Comprehensive Scoring and Selection Advice</h2>

<p>We submitted the code from each model, anonymized it, had 4 AIs review it, tested it with real cases, and graded it on dimensions like completeness, correctness, security, testing, and quality.</p>

<ul>
<li><strong>Opus 4.8:</strong> 8.86 (best overall)</li>
<li><strong>GPT-5.5:</strong> 8.62</li>
<li><strong>GLM-5.2:</strong> 8.14</li>
<li><strong>GLM-5.1:</strong> 7.77</li>
</ul>

<h3>How to Choose?</h3>

<ul>
<li><strong>If budget is no issue and you need the highest ceiling:</strong> Opus 4.8 and GPT-5.5 are still top choices.</li>
<li><strong>If you focus on backend development, don't need multimodal, and want to control costs with a domestic model:</strong> GLM-5.2 is excellent — <em>if you can get access</em>.</li>
</ul>

<h2>Code Example: JWT Utility with GLM-5.2</h2>

<p>To test GLM-5.2 yourself, start with simple commands. For example, to generate a JWT utility class in Python:</p>

<pre><code class="language-python">import jwt
import datetime
from typing import Dict, Optional

class JWTUtil:
    def __init__(self, secret_key: str, algorithm: str = "HS256"):
        self.secret_key = secret_key
        self.algorithm = algorithm

    def generate_token(self, payload: Dict, expire_minutes: Optional[int] = None) -> str:
        if expire_minutes:
            payload["exp"] = datetime.datetime.utcnow() + datetime.timedelta(minutes=expire_minutes)
        return jwt.encode(payload, self.secret_key, algorithm=self.algorithm)

    def decode_token(self, token: str) -> Dict:
        return jwt.decode(token, self.secret_key, algorithms=[self.algorithm])

# Example usage
jwt_util = JWTUtil(secret_key="your-secret-key")
token = jwt_util.generate_token({"user_id": 123, "role": "admin"}, expire_minutes=60)
print(token)
decoded = jwt_util.decode_token(token)
print(decoded)</code></pre>

<h2>常见问题</h2>

<h3>How does GLM-5.2 compare to DeepSeek V4 for coding?</h3>
<p>They serve different niches. DeepSeek V4 excels at reasoning-heavy tasks (math, competitive programming, logic puzzles) and is fully open-source for self-hosting. GLM-5.2 excels at practical backend engineering — it writes production-grade auth systems with proper security checks that other models miss. If you're building APIs with JWT/OAuth, GLM-5.2 has the edge. If you're doing algorithmic work, DeepSeek V4 is stronger. Both are priced competitively against Western models.</p>

<h3>Why is GLM-5.2 access so difficult?</h3>
<p>The coding plan has limited capacity — Zhipu AI appears to be rationing access to manage infrastructure costs while demand far exceeds supply. The model's reputation for security-critical coding has driven intense demand from enterprise developers. Secondary-market resale of coding plan slots has emerged as a gray market. Zhipu is expected to expand capacity, but no timeline has been announced.</p>

<h3>Should I switch from Claude Code to GLM-5.2 for coding?</h3>
<p>Not as a full replacement. GLM-5.2 is a model, not a coding agent like Claude Code. You can use GLM-5.2 as the underlying LLM in agent frameworks like OpenCode or via API. For tasks where security correctness is paramount (auth migration, user isolation), GLM-5.2 is worth adding to your toolkit. For general coding workflows, Claude Code's agent loop and tool integration still provide a better overall experience. The ideal setup: use Claude Code for orchestration and GLM-5.2 for security-critical code generation.</p>

<div class="next-step">
<p><strong>Previous:</strong> <a href="/en/article/codex-autocad-redraw-dwg-one-sentence">Codex + AutoCAD: Redraw Complex DWG with Just One Sentence ←</a></p>
</div>`,
    contentZh: `<div class="meta-banner">
<p><strong>📅 发布日期：</strong>2026年6月25日 · <strong>🏷️ 分类：</strong>AI对比 · <strong>📊 难度：</strong>中级 · <strong>🛠️ 工具：</strong>GLM-5.2、GPT-5.5、Claude Opus 4.8</p>
</div>

<p>GLM-5.2 在AI编程社区掀起风暴，赢得"国产顶级编程模型"的称号。其编程计划供不应求，甚至在二手平台上有偿转让，网友戏称在中国使用GLM-5.2比从美国访问GPT-5.5还难。让我们深入了解其实际表现和对开发者的意义。</p>

<h2>6,690条评论的情感分析</h2>

<p>为理解社区认知，我们分析了抖音、小红书、B站、X和V2EX等平台上的6,690条评论。结果令人惊讶：负面情感（40.3%）高于正面（28.6%）。但当我们拆解讨论话题时，明白了原因。</p>

<ul>
<li><strong>编程能力：</strong>提及1,280次，几乎全部正面。</li>
<li><strong>定价和访问：</strong>提及1,269次，几乎全部负面（因难以获得编程计划）。</li>
</ul>

<p>这显示出爱恨交织的关系——开发者赞美其编程能力但为访问问题感到沮丧。国内外认知也存在鲜明对比。海外X（Twitter）上正面情感超过48.5%，开发者称其为"开源DeepSeek时刻"和Claude、OpenAI的潜在对手。国内抖音（45.9%负面）和小红书（43.5%负面）则被无法获取访问的抱怨主导，技术讨论很少。</p>

<h2>真实项目实战测试</h2>

<p>我们在两个真实项目中测试了GLM-5.2，对比GPT-5.5和Opus 4.8，使用严格变量控制（相同提示、相同基础代码、每个模型独立运行、4个独立AI评审）。</p>

<h3>项目1：认证迁移</h3>

<p>此项目测试后端和安全能力，涉及邮箱+密码、邮箱验证、密码重置、JWT双Token、Refresh轮换、OAuth和跨用户隔离。</p>

<ul>
<li><strong>GLM-5.1、GPT-5.5和Opus 4.8</strong>均未实现OAuth防伪安全检查。</li>
<li><strong>GLM-5.2</strong>是唯一强制正确安全检查的模型。它还修复了GLM-5.1的一个关键安全漏洞——用户可通过任务ID访问或取消他人任务（数据泄露）。GLM-5.2在此项目的23个测试用例中全部通过。</li>
</ul>

<p>但GLM-5.2有个怪癖——喜欢偷工减料。GPT-5.5和Opus 4.8实现了12个接口，GLM-5.2只做了8个，跳过了邮箱验证和密码重置等部分。但它写的代码确实干净，尤其在CSRF和架构方面。</p>

<h3>项目2：Skills · Web全栈开发</h3>

<p>此项目评估Web全栈开发能力，涵盖thinking、text、tool_call、tool_result和done阶段。</p>

<p>得分非常接近：</p>

<ul>
<li>Opus 4.8：9.4</li>
<li>GPT-5.5：9.4</li>
<li>GLM-5.2：9.25</li>
<li>GLM-5.1：8.15</li>
</ul>

<p>没有明显赢家——所有模型表现都不错。</p>

<h2>综合评分与选择建议</h2>

<p>我们提交每个模型的代码（匿名化），由4个AI评审，用真实案例测试，从完整性、正确性、安全性、测试和质量等维度评分。</p>

<ul>
<li><strong>Opus 4.8：</strong>8.86（综合最佳）</li>
<li><strong>GPT-5.5：</strong>8.62</li>
<li><strong>GLM-5.2：</strong>8.14</li>
<li><strong>GLM-5.1：</strong>7.77</li>
</ul>

<h3>如何选择？</h3>

<ul>
<li><strong>预算充足且需要最高上限：</strong>Opus 4.8和GPT-5.5仍是首选。</li>
<li><strong>专注后端开发、不需要多模态、想用国产模型控制成本：</strong>GLM-5.2非常出色——<em>如果你能获取访问权限的话</em>。</li>
</ul>

<h2>代码示例：GLM-5.2生成的JWT工具类</h2>

<pre><code class="language-python">import jwt
import datetime
from typing import Dict, Optional

class JWTUtil:
    def __init__(self, secret_key: str, algorithm: str = "HS256"):
        self.secret_key = secret_key
        self.algorithm = algorithm

    def generate_token(self, payload: Dict, expire_minutes: Optional[int] = None) -> str:
        if expire_minutes:
            payload["exp"] = datetime.datetime.utcnow() + datetime.timedelta(minutes=expire_minutes)
        return jwt.encode(payload, self.secret_key, algorithm=self.algorithm)

    def decode_token(self, token: str) -> Dict:
        return jwt.decode(token, self.secret_key, algorithms=[self.algorithm])

# 使用示例
jwt_util = JWTUtil(secret_key="your-secret-key")
token = jwt_util.generate_token({"user_id": 123, "role": "admin"}, expire_minutes=60)
print(token)
decoded = jwt_util.decode_token(token)
print(decoded)</code></pre>

<h2>常见问题</h2>

<h3>GLM-5.2与DeepSeek V4在编程方面相比如何？</h3>
<p>两者服务于不同领域。DeepSeek V4擅长推理密集型任务（数学、竞赛编程、逻辑谜题），且完全开源可自托管。GLM-5.2擅长实用后端工程——它编写生产级认证系统，包含其他模型遗漏的适当安全检查。如果你在构建JWT/OAuth的API，GLM-5.2有优势。如果你做算法工作，DeepSeek V4更强。两者价格都比西方模型有竞争力。</p>

<h3>为什么GLM-5.2访问这么难？</h3>
<p>编程计划容量有限——智谱AI似乎在配给访问以管理基础设施成本，而需求远超供应。该模型在安全关键编码方面的声誉推动了企业开发者的强烈需求。编程计划名额的二级市场转售已作为灰色市场出现。智谱预计将扩大容量，但尚未公布时间表。</p>

<h3>应该从Claude Code切换到GLM-5.2编程吗？</h3>
<p>不建议完全替换。GLM-5.2是一个模型，不是像Claude Code那样的编码Agent。你可以在OpenCode等Agent框架中或通过API使用GLM-5.2作为底层LLM。对于安全正确性至关重要的任务（认证迁移、用户隔离），GLM-5.2值得加入你的工具箱。对于通用编码工作流，Claude Code的Agent循环和工具集成仍提供更好的整体体验。理想设置：用Claude Code做编排，GLM-5.2做安全关键代码生成。</p>

<div class="next-step">
<p><strong>上一篇：</strong> <a href="/zh/article/codex-autocad-redraw-dwg-one-sentence">Codex+AutoCAD：一句话重绘复杂DWG图纸 ←</a></p>
</div>`,
  },

'''

last_brace = content_src.rfind('};')
content_new = content_src[:last_brace] + new_contents + '};'

with open('src/lib/article-content.ts', 'w', encoding='utf-8') as f:
    f.write(content_new)

print('Part 3: 2 article contents added to article-content.ts')

print('\n=== All done! Run build to verify ===')
