"""Publish Aug 4, 2026 — 1 article, no new tools."""
import os; BASE = r"C:\Users\jun\aistudyonline-next"; os.chdir(BASE)

with open('src/lib/articles.ts', 'r', encoding='utf-8') as f: s = f.read()
a = r"""  {
    slug: "how-feishu-redefined-ai-work-100-to-20000-system-in-minutes",
    title: "How Feishu Redefined AI Work: $100 → $20,000 System in Minutes",
    titleZh: "飞书重新定义AI工作：100元→2万元系统几分钟搞定",
    description: "Feishu's three groundbreaking AI features — one-click personal AI Agent (Little Lobster), Feishu Miaoda generating $20K business systems for $100 in natural language, and Multidimensional Table Agent with auto table/dashboard/permission generation — plus the OpenClaw open-source plugin for multi-model integration.",
    descriptionZh: "飞书三大AI突破——一键创建个人AI Agent（小龙虾）、飞书妙搭用自然语言100元生成2万元业务系统、多维表格AI Agent自动生成表格/仪表盘/权限——含OpenClaw开源插件多模型集成。",
    category: "ai-news",
    tags: ["Feishu", "Lark", "AI Agent", "Miaoda", "OpenClaw", "Productivity", "China"],
    difficulty: "beginner",
    toolsMentioned: ["OpenClaw"],
    date: "2026-08-04",
  },

"""
last = s.rfind('];')
with open('src/lib/articles.ts', 'w', encoding='utf-8') as f: f.write(s[:last] + a + '];')
print('Part 1 done')

with open('src/lib/article-content.ts', 'r', encoding='utf-8') as f: c = f.read()
n = r'''
  "how-feishu-redefined-ai-work-100-to-20000-system-in-minutes": {
    content: `<div class="meta-banner">
  <span class="meta-badge">📰 AI News</span>
  <span class="meta-badge">🕒 5 min read</span>
  <span class="meta-badge">📅 Aug 4, 2026</span>
  <span class="meta-badge">🎯 Beginner</span>
</div>

<h2 id="introduction">Introduction</h2>
<p>If you've ever struggled to set up an AI assistant, spend weeks developing business systems, or manually build data tables, Feishu's latest launch is about to change everything. In a recent conference, Feishu introduced three groundbreaking features that lowered the barrier for AI-driven work to near zero.</p>

<h2 id="first">The First Breakthrough: Your Personal AI Agent in One Click</h2>
<p>Gone are the days of endless tutorials, environment configurations, and API adjustments. With Feishu's new feature, you can get your own AI agent — dubbed "Little Lobster" — with a single click.</p>
<h3>What It Does:</h3>
<ul>
  <li><strong>Context-Aware</strong>: Lives in your Feishu contacts list, understands your work context, proactively follows up on tasks.</li>
  <li><strong>Permission-Aligned</strong>: Same access rights as you, ensuring data security while automating workflows.</li>
  <li><strong>Task Execution</strong>: From summarizing reports to generating PPTs, delivers results directly without manual intervention.</li>
</ul>
<h3>How to Set Up:</h3>
<ol>
  <li>Open Feishu and navigate to the AI agent section.</li>
  <li>Click "Create My Agent" and follow the on-screen prompts.</li>
  <li>Customize its name and preferences (e.g., "Litian's Ally").</li>
</ol>

<h2 id="second">The Second Breakthrough: Feishu Miaoda — $100 for a $20,000 System</h2>
<p>Feishu Miaoda is a game-changer for businesses. In a live demo, a user spent just over 100 yuan on token fees and generated a system application worth 20,000 yuan using natural language.</p>
<h3>How It Works:</h3>
<ol>
  <li><strong>Natural Language Input</strong>: Describe your business needs in plain Chinese (e.g., "I need a sales performance tracking system").</li>
  <li><strong>AI Understanding</strong>: The AI analyzes your requirements, clarifies ambiguities, and generates a detailed requirements document.</li>
  <li><strong>System Generation</strong>: Within minutes, it creates a fully functional system with tables, dashboards, and permissions.</li>
</ol>
<h3>Example Workflow:</h3>
<p>User: "Help me build a weekly sales report system that automatically pulls data from our CRM and generates visualizations." → AI: "I'll create a table for sales data, a dashboard with weekly trends, and set up access permissions." → Result: A complete system ready in under 10 minutes.</p>

<h2 id="third">The Third Breakthrough: Multidimensional Table Agent</h2>
<p>Manually building data tables, dragging dashboards, and configuring permissions is a thing of the past. Feishu's Multidimensional Table Agent automates all these tasks.</p>
<h3>Key Features:</h3>
<ul>
  <li><strong>Requirement-Based Creation</strong>: Describe your data needs, and the agent generates tables, dashboards, and questionnaires automatically.</li>
  <li><strong>Permission Automation</strong>: Configures access rights based on your team structure.</li>
  <li><strong>End-to-End Workflow</strong>: From idea to implementation, entire process is AI-driven.</li>
</ul>

<h2 id="openclaw">The Game-Changer: OpenClaw Open Source Plugin</h2>
<p>Feishu also open-sourced the official OpenClaw plugin, which allows AI agents to operate Feishu documents, multidimensional tables, and calendars with user-level permissions. This integration means you can use any major AI model (e.g., Volcano Engine, MiniMax, Coze) directly within Feishu — no platform switching required.</p>

<h2 id="conclusion">The Future of Work: Tools That Learn You</h2>
<p>Feishu's vision: "Previously, you learned how to use tools; now, tools learn you." If you're still struggling to set up AI tools, stop wasting time. With Feishu's new features, you can get a personal AI agent in one click, build business systems for $100 that used to cost $20,000, and automate data management with the Multidimensional Table Agent.</p>

<h2>常见问题</h2>

<h3>How is Feishu's AI Agent different from WorkBuddy or Coze?</h3>
<p>Feishu's AI Agent is <strong>embedded in your work communication platform</strong> — it's a contact in your Feishu address book, not a separate app. This means it has direct access to your Feishu documents, calendars, and team chat history. WorkBuddy is a standalone desktop agent. Coze is a multi-agent orchestration platform. Feishu's advantage is <strong>context proximity</strong>: your AI agent knows what your team discussed in chat, what documents were shared, and what meetings you had — because it's part of the same platform. The trade-off is that it's Feishu-specific (you must be a Feishu user). Many professionals use Feishu for communication, WorkBuddy for desktop automation, and Coze for complex multi-agent workflows — they're complementary.</p>

<h3>Is Feishu Miaoda really $100 for a $20,000 system?</h3>
<p>The $100 (¥100) refers to the API token cost during the live demo — the actual compute cost of generating the system. The "$20,000 system" refers to what a traditional development agency would charge to build the same application from scratch (custom tables, dashboards, permissions, workflow logic). The value gap comes from AI eliminating the <strong>labor cost</strong> of development. The generated system is not a toy — it's a fully functional Feishu application with proper data models, user permissions, and automation. However, complex business logic, custom integrations, and enterprise-specific workflows may still require manual configuration. Miaoda is a rapid prototyping and deployment tool, not a replacement for complex software engineering.</p>

<h3>Can I use my own AI model with Feishu's features?</h3>
<p>Yes — the OpenClaw open-source plugin enables multi-model integration. You can connect Volcano Engine, MiniMax, Coze, or any model that supports the OpenClaw plugin protocol. This means you're not locked into a single AI provider. The plugin handles the Feishu API integration (documents, tables, calendars), and your chosen model powers the AI logic. The permission system ensures the model only accesses what you're authorized to see. For teams with specific model preferences or compliance requirements, this flexibility is critical.</p>

<h3>Do I need to be a developer to use these features?</h3>
<p>No — the entire design philosophy is zero-code. The AI Agent (Little Lobster) is one-click setup. Miaoda uses natural language — you describe what you need in plain Chinese. The Multidimensional Table Agent works by typing requirements into a text field. The only CLI commands in this article are optional (checking OpenClaw version, managing automation) and not required for normal use. If you can describe what you need in a sentence, you can use these features. Feishu's target audience for these launches is business users, not developers.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Interested in AI-powered business platforms? Explore more:</p>
  <ul>
    <li><a href="/articles/lightweight-ai-transformation-traditional-business-workbuddy-cordys-crm">Lightweight AI Transformation for Traditional Business Systems</a> — another approach to AI-powered business systems</li>
    <li><a href="/articles/build-ai-team-coze-3-one-person-company">Build an AI Team with Coze 3.0: One-Person Company Guide</a> — compare Feishu with Coze's multi-agent approach</li>
    <li><a href="/articles/tencent-workbuddy-ai-office-workbench">Tencent WorkBuddy: The Ultimate AI Office Workbench</a> — the desktop-centric alternative to Feishu's embedded approach</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">📰 AI 新闻</span>
  <span class="meta-badge">🕒 阅读约5分钟</span>
  <span class="meta-badge">📅 2026年8月4日</span>
  <span class="meta-badge">🎯 入门</span>
</div>

<h2 id="introduction">引言</h2>
<p>如果你曾挣扎于设置AI助手、花数周开发业务系统或手动搭建数据表格，飞书的最新发布将改变一切。在最近的发布会上，飞书推出三项突破性功能，将AI驱动工作的门槛降到接近零。</p>

<h2 id="first">第一项突破：一键创建个人AI Agent</h2>
<p>无尽教程、环境配置和API调整的日子一去不复返。飞书新功能让你一键获得自己的AI Agent——名为"小"。小龙虾"。</p>
<h3>功能：</h3>
<ul>
  <li><strong>上下文感知</strong>：存在于飞书通讯录中，理解你的工作上下文，主动跟进任务。</li>
  <li><strong>权限对齐</strong>：与你拥有相同权限，保障数据安全的同时自动化工作流。</li>
  <li><strong>任务执行</strong>：从总结报告到生成PPT，直接交付结果无需人工干预。</li>
</ul>
<h3>设置：</h3>
<ol>
  <li>打开飞书进入AI Agent部分。</li>
  <li>点击"创建我的Agent"按提示操作。</li>
  <li>自定义名称和偏好。</li>
</ol>

<h2 id="second">第二项突破：飞书妙搭——100元生成2万元系统</h2>
<p>飞书妙搭是企业的游戏改变者。现场演示中，用户仅用100多元token费用就生成了一个价值2万元的系统应用。</p>
<h3>工作原理：</h3>
<ol>
  <li><strong>自然语言输入</strong>：用中文描述业务需求（如"我需要一个销售业绩跟踪系统"）。</li>
  <li><strong>AI理解</strong>：AI分析需求、澄清歧义、生成详细需求文档。</li>
  <li><strong>系统生成</strong>：几分钟内创建含表格、仪表盘和权限的完整功能系统。</li>
</ol>

<h2 id="third">第三项突破：多维表格AI Agent</h2>
<p>手动搭建数据表格、拖拽仪表盘和配置权限已成为过去。飞书多维表格AI Agent自动完成所有这些任务。</p>
<h3>关键特性：</h3>
<ul>
  <li><strong>基于需求创建</strong>：描述数据需求，Agent自动生成表格、仪表盘和问卷。</li>
  <li><strong>权限自动化</strong>：基于团队结构配置访问权限。</li>
  <li><strong>端到端工作流</strong>：从创意到实施全流程AI驱动。</li>
</ul>

<h2 id="openclaw">OpenClaw开源插件</h2>
<p>飞书同时开源了官方OpenClaw插件，允许AI Agent以用户级权限操作飞书文档、多维表格和日历。可集成任意主流AI模型（火山引擎、MiniMax、扣子等），无需切换平台。</p>

<h2 id="conclusion">未来工作：工具学习你</h2>
<p>飞书愿景："以前你学习如何使用工具，现在工具学习你。"一键创建个人AI Agent，100元搭建以往2万元的业务系统，多维表格AI Agent自动化数据管理。</p>

<h2>常见问题</h2>

<h3>飞书AI Agent和WorkBuddy或扣子有什么不同？</h3>
<p>飞书AI Agent<strong>嵌入在你的工作沟通平台中</strong>——它是飞书通讯录中的一个联系人，而非独立App。这意味着它可直接访问你的飞书文档、日历和团队聊天记录。WorkBuddy是独立桌面Agent。扣子是多Agent编排平台。飞书的优势是<strong>上下文接近性</strong>：你的AI Agent知道团队在聊什么、分享了什么文档、开了什么会——因为它在同一平台中。代价是仅限飞书用户。很多专业人士飞书用于沟通、WorkBuddy用于桌面自动化、扣子用于复杂多Agent工作流——三者互补。</p>

<h3>飞书妙搭真的100元生成2万元系统？</h3>
<p>100元（¥100）指现场演示中的API token成本——生成系统的实际计算费用。"2万元系统"指传统开发公司从零构建同样应用（自定义表格、仪表盘、权限、工作流逻辑）的收费。价值差距来自AI消除了<strong>开发人力成本</strong>。生成系统不是玩具——是功能完整的飞书应用，含数据模型、用户权限和自动化。但复杂业务逻辑、自定义集成和企业特定工作流仍需手动配置。妙搭是快速原型和部署工具，非复杂软件工程的替代品。</p>

<h3>能用自己偏好的AI模型配合飞书功能吗？</h3>
<p>可以——OpenClaw开源插件支持多模型集成。可连接火山引擎、MiniMax、扣子或任何支持OpenClaw插件协议的模型。不锁定单一AI供应商。插件处理飞书API集成（文档、表格、日历），你选择的模型驱动AI逻辑。权限系统确保模型仅访问你授权的内容。对有特定模型偏好或合规要求的团队，这种灵活性至关重要。</p>

<h3>需要是开发者才能用这些功能吗？</h3>
<p>不需要——整个设计理念是无代码。AI Agent（小龙虾）一键设置。妙搭用自然语言——用中文描述需求。多维表格AI Agent在文本框中输入需求即可。本文中的CLI命令是可选的，正常使用无需。如果你能用一句话描述需求，就能用这些功能。飞书这些发布的目标受众是业务用户，而非开发者。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>对AI驱动业务平台感兴趣？探索更多：</p>
  <ul>
    <li><a href="/articles/lightweight-ai-transformation-traditional-business-workbuddy-cordys-crm">传统业务系统轻量级AI改造方案</a> — 另一种AI驱动业务系统方案</li>
    <li><a href="/articles/build-ai-team-coze-3-one-person-company">用Coze 3.0搭建AI团队：一人公司全流程</a> — 对比飞书与扣子的多Agent方案</li>
    <li><a href="/articles/tencent-workbuddy-ai-office-workbench">腾讯WorkBuddy：日常办公的终极AI工作台</a> — 桌面端替代飞书嵌入方式</li>
  </ul>
</div>`,
  },

'''
last = c.rfind('};')
with open('src/lib/article-content.ts', 'w', encoding='utf-8') as f: f.write(c[:last] + n + '};')
print('Part 2 done\n=== Done ===')