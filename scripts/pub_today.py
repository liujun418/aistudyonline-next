"""
Publish July 2, 2026 article.
No new tools - mentions dev frameworks (LangChain, Pinecone, LangGraph, etc.) already covered or not standalone AI tools.
"""
import os

BASE = r"C:\Users\jun\aistudyonline-next"
os.chdir(BASE)

# ===== Part 1: Add 1 article metadata to articles.ts =====
with open('src/lib/articles.ts', 'r', encoding='utf-8') as f:
    articles_src = f.read()

new_articles = r"""  {
    slug: "dont-be-intimidated-ai-jargon-practical-guide-concepts",
    title: "Don't Be Intimidated by AI Jargon: A Practical Guide to AI Concepts from ChatGPT to Workspace Agent",
    titleZh: "别被AI术语吓倒：从ChatGPT到Workspace Agent的AI概念实战指南",
    description: "A complete journey through 12 AI concepts — Token, Prompt Engineering, RAG, Tool Calling, MCP, Context Engineering, Skill, Computer Use, Agent, Harness Engineering, Workflow, and Workspace Agent — with code snippets and actionable tips for each.",
    descriptionZh: "12个AI概念的完整之旅——Token、提示词工程、RAG、工具调用、MCP、上下文工程、Skill、计算机使用、Agent、Harness工程、工作流和Workspace Agent——每个概念含代码示例和实操建议。",
    category: "ai-basics",
    tags: ["concepts", "beginner", "rag", "agent", "mcp", "workflow", "prompt-engineering", "guide"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt", "langchain", "n8n", "pinecone"],
    date: "2026-07-02",
  },

"""

last_bracket = articles_src.rfind('];')
articles_new = articles_src[:last_bracket] + new_articles + '];'

with open('src/lib/articles.ts', 'w', encoding='utf-8') as f:
    f.write(articles_new)

print('Part 1: 1 new article added to articles.ts')

# ===== Part 2: Add article content to article-content.ts =====
with open('src/lib/article-content.ts', 'r', encoding='utf-8') as f:
    content_src = f.read()

new_contents = r'''
  "dont-be-intimidated-ai-jargon-practical-guide-concepts": {
    content: `<div class="meta-banner">
<p><strong>📅 Published:</strong> July 2, 2026 · <strong>🏷️ Category:</strong> AI Basics · <strong>📊 Level:</strong> Beginner</p>
</div>

<p>The AI landscape is rife with jargon — Prompt, RAG, Agent, MCP, Workflow, and more. But these aren't just buzzwords; they represent a clear evolution of AI from a "chat tool" to a "real-world work system." Let's break down this journey with practical explanations and actionable insights.</p>

<h2>Chapter 1: Token & Context Window — How Much Can AI "See" at Once?</h2>

<p>When you interact with AI tools like ChatGPT, you might think it processes text like a human. In reality, AI breaks down input into tiny units called <strong>Tokens</strong>. For example, "I love artificial intelligence" might be split into tokens like <em>I, love, art, if, icial, intelligence</em> (varies by model).</p>

<p>Tokens matter for three key reasons:</p>
<ol>
<li><strong>Context Limit:</strong> AI models have a maximum token capacity. This includes your query, conversation history, system prompts, document content, and tool responses. Exceeding it means earlier content gets "pushed out" — like a desk that can only hold 10 papers. This limit is called the <strong>Context Window</strong>.</li>
<li><strong>Cost:</strong> Many AI services charge by token.</li>
<li><strong>Memory:</strong> AI "forgets" earlier content when the context window overflows.</li>
</ol>

<h2>Chapter 2: Prompt Engineering — How to Make AI Understand Your Task</h2>

<p>Early AI users were excited by "type a query, get an answer." But they quickly realized <em>how</em> you ask matters:</p>
<ul>
<li>Vague: <em>"Help me write a product plan."</em> → generic, useless output</li>
<li>Detailed: <em>"You are a senior product manager. Write a product plan for an AI tool targeted at developers. Include target users, core pain points, feature modules, business model, and go-to-market strategy. Output in a table."</em> → structured, relevant results</li>
</ul>

<p>A good prompt includes: <strong>Role</strong> (who AI should act as), <strong>Task</strong> (clear goal), <strong>Context</strong> (background), <strong>Format</strong> (output structure), <strong>Constraints</strong> (what to avoid), and <strong>Examples</strong> (desired output).</p>

<h2>Chapter 3: RAG (Retrieval-Augmented Generation) — How AI Finds External Information</h2>

<p>AI can't know what it hasn't been trained on — like your company's internal docs or yesterday's news. <strong>RAG</strong> solves this by having AI "search first, then answer."</p>

<p>The RAG process:</p>
<ol>
<li><strong>Ingest Data:</strong> Add documents to a Knowledge Base</li>
<li><strong>Embed Text:</strong> Convert text into numerical vectors (Embeddings) for semantic similarity</li>
<li><strong>Retrieve:</strong> When you ask, the system retrieves relevant chunks from the Vector Database</li>
<li><strong>Generate:</strong> AI answers based on the retrieved information</li>
</ol>

<p>Example: Ask <em>"How many days in advance do I need to apply for leave?"</em> RAG searches the employee handbook, retrieves the policy, and answers with citations.</p>

<pre><code class="language-python">from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
import pinecone

pinecone.init(api_key="your-api-key", environment="your-environment")
index = pinecone.Index("your-index-name")

embeddings = OpenAIEmbeddings()
vector_store = Pinecone.from_texts(
    texts=["Your company policy text here..."],
    embedding=embeddings,
    index_name="your-index-name"
)

query = "How to apply for leave?"
docs = vector_store.similarity_search(query)
print(docs[0].page_content)</code></pre>

<h2>Chapter 4: Tool Calling — How AI Takes Action Beyond Text</h2>

<p>While RAG lets AI access information, <strong>Tool Calling</strong> (Function Calling) lets AI <em>act</em> — checking real-time data, executing code, or interacting with apps.</p>

<ul>
<li>Ask: <em>"What's my order status?"</em> → AI calls your e-commerce API → <em>"Order #12345: Shipped."</em></li>
<li>Ask: <em>"Run this Python code: print(2+2)"</em> → AI executes → <em>"4"</em></li>
</ul>

<p>Define your tool's schema in JSON with name and parameters, then instruct AI to use it when needed.</p>

<h2>Chapter 5: MCP (Model-Component Protocol) — How AI Connects to Tools Uniformly</h2>

<p>As you add more tools, connecting them becomes chaotic — each has its own interface. <strong>MCP</strong> is a standard protocol for AI to connect to external tools, like USB-C for electronics. It standardizes how tools expose capabilities, how AI discovers and calls them, and how parameters, returns, and security are handled.</p>

<h2>Chapter 6: Context Engineering — What Information Should AI See?</h2>

<p>Beyond writing good prompts, you need to manage the <em>flow of information</em> AI receives — this is <strong>Context Engineering</strong>. For an AI customer support agent, context might include: purchase history, past support tickets, current order status, and refund policies. Too little context → wrong answers; too much → confusion. Use tools like LlamaIndex to automate context assembly.</p>

<h2>Chapter 7: Skill — How AI Reuses Proven Workflows</h2>

<p><strong>Skill</strong> is turning repetitive tasks into reusable AI workflows. Instead of explaining "how to write a weekly report" every time, save the instructions as a Skill:</p>
<ol>
<li>Retrieve completed tasks from project management tool</li>
<li>Extract key achievements and risks</li>
<li>Format into a template</li>
<li>Adjust tone to match company standards</li>
</ol>
<p>Use tools like Dify or Microsoft Copilot Studio to create and deploy Skills.</p>

<h2>Chapter 8: Computer Use — How AI Operates Like a Human on Desktop/Web</h2>

<p>Not all systems have APIs. <strong>Computer Use</strong> lets AI interact with software and web pages like a human — clicking buttons, filling forms, navigating UIs. Example: automating expense report submission without an API — AI opens the portal, logs in, fills the form, attaches receipt, submits.</p>

<h2>Chapter 9: Agent — How AI Autonomously Completes Complex Tasks</h2>

<p>An <strong>Agent</strong> is AI that can plan, act, and adapt to complete a goal. Unlike a chatbot (responds to queries) or tool-calling AI (single actions), an Agent can:</p>
<ol>
<li><strong>Plan:</strong> Break a goal into steps</li>
<li><strong>Act:</strong> Call tools, use Skills, interact with computers</li>
<li><strong>Reflect:</strong> Adjust plans based on results</li>
</ol>

<p>Example: A coding Agent fixing a bug — identifies bug from error → retrieves code file → modifies code → runs tests → if tests fail, repeats.</p>

<pre><code class="language-python">from langchain.agents import AgentType, initialize_agent, load_tools

tools = load_tools(["serpapi", "llm-math"], llm=your_llm)
agent = initialize_agent(
    tools, your_llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)
agent.run("What's the weather in Tokyo? Then calculate how many days until summer solstice.")</code></pre>

<h2>Chapter 10: Harness Engineering — How to Deploy Agents Safely</h2>

<p>Agents are powerful but risky — they might delete files, write bad code, or access sensitive data. <strong>Harness Engineering</strong> provides safeguards: <strong>Sandboxing</strong> (restrict access to test branches, not production), <strong>Approval Flows</strong> (human sign-off for critical actions), and <strong>Logging & Auditing</strong> (track every action). Start with a sandbox — have the Agent push to a staging branch first, requiring human merge to main.</p>

<h2>Chapter 11: Workflow — How to Orchestrate AI and Tools into Processes</h2>

<p>Real-world work is a series of steps. <strong>Workflow</strong> tools (n8n, Zapier, LangGraph) string together AI actions, tool calls, and human approvals into automated processes. Example: "New Customer Inquiry → AI Generates Response → Human Approves → Send Email → Log in CRM."</p>

<pre><code class="language-python">from langgraph.graph import StateGraph, START

graph = StateGraph()

def generate_response(state):
    return {"response": your_llm.generate(state["inquiry"])}

def human_approve(state):
    return {"approved": input("Approve? (y/n)") == "y"}

def send_email(state):
    return {"email_sent": True}

graph.add_node("generate", generate_response)
graph.add_node("approve", human_approve)
graph.add_node("send", send_email)
graph.add_edge(START, "generate")
graph.add_edge("generate", "approve")
graph.add_edge("approve", "send", cond=lambda s: s["approved"])

app = graph.compile()
result = app.invoke({"inquiry": "I'm interested in your product."})</code></pre>

<h2>Chapter 12: Workspace Agent — How AI Becomes a Team Member</h2>

<p>A <strong>Workspace Agent</strong> lives in your team's work environment, understanding long-term context: team projects, document locations, customer histories, and role-based permissions. Example: automatically drafts weekly reports by pulling completed tasks from project management, identifying risks from meetings, summarizing code commits, and formatting for approval. Use tools like CrewAI to manage agent roles and workflows within the workspace.</p>

<h2>Conclusion: AI Jargon Is a Map, Not a Maze</h2>

<p>Each term — from Token to Workspace Agent — solves a specific problem in making AI useful for real work. Instead of getting lost in jargon, focus on <em>what problem each concept solves</em> and <em>how you can apply it</em>. Start small: use Prompt Engineering for better outputs, add RAG for external knowledge, then Tool Calling for actions, and build from there. Before you know it, you'll be navigating the AI landscape with confidence.</p>

<h2>常见问题</h2>

<h3>What's the most important concept for a beginner to master first?</h3>
<p>Prompt Engineering. It's the foundation everything else builds on — even RAG, Agents, and Workflows ultimately depend on giving AI clear instructions. Master the Role-Task-Context-Format-Constraints-Examples framework first. Once you can consistently get quality outputs from a simple chat interface, the other concepts (RAG, Tool Calling, Agents) become natural extensions rather than confusing abstractions. Most beginners try to jump straight to building Agents without solid prompt skills, and the result is frustration when the Agent does unpredictable things.</p>

<h3>How are RAG, Tool Calling, and Agents different from each other?</h3>
<p>Think of them as escalating levels of AI capability: <strong>RAG</strong> lets AI <em>read</em> external information (search docs, retrieve facts). <strong>Tool Calling</strong> lets AI <em>act</em> (call APIs, run code, send emails). <strong>Agents</strong> combine both plus planning — they decide <em>when</em> to read, <em>when</em> to act, and <em>how</em> to adjust when things go wrong. A chatbot with RAG can answer "What's our refund policy?" An AI with Tool Calling can process "Refund order #12345." An Agent can handle "A customer is unhappy about a late delivery — figure out what happened and make it right."</p>

<h3>Do I need to know how to code to use these AI concepts?</h3>
<p>Not for the concepts themselves — you can use Prompt Engineering, Skills (via no-code tools like Dify), and basic Workflows (via Zapier or n8n's visual editor) without coding. RAG and Tool Calling become easier with some coding knowledge but have no-code alternatives (NotebookLM for RAG, Kouzi for tool-based agents). Computer Use and Harness Engineering are more code-heavy. The chapters in this guide are ordered roughly from least to most technical — start from Chapter 1 and go as far as your comfort level allows. Each chapter builds on the previous ones, so even if you stop at Chapter 7, you'll have a solid practical foundation.</p>

<div class="next-step">
<p><strong>上一篇：</strong> <a href="/en/article/mastering-ai-workflow-beginner-custom-workbench">Mastering AI Workflow: A Beginner-Friendly Guide to Building Your Custom AI Workbench ←</a></p>
</div>`,
    contentZh: `<div class="meta-banner">
<p><strong>📅 发布日期：</strong>2026年7月2日 · <strong>🏷️ 分类：</strong>AI基础 · <strong>📊 难度：</strong>初级</p>
</div>

<p>AI领域充斥着术语——Prompt、RAG、Agent、MCP、Workflow等等。但它们不只是流行词；它们代表了AI从"聊天工具"到"实际工作系统"的清晰演变。让我们用实操解释和可执行的洞察来拆解这段旅程。</p>

<h2>第1章：Token与上下文窗口——AI一次能"看到"多少？</h2>

<p>当你与ChatGPT等AI工具交互时，你可能以为它像人类一样处理文本。实际上，AI将输入分解为称为<strong>Token</strong>的微小单元。例如"I love artificial intelligence"可能被分割为<em>I, love, art, if, icial, intelligence</em>（不同模型分割方式不同）。</p>

<p>Token重要的三个原因：</p>
<ol>
<li><strong>上下文限制：</strong>AI模型有最大token容量。包括你的查询、对话历史、系统提示、文档内容和工具响应。超出限制意味着更早的内容被"推出"——像一张只能放10张纸的桌子，新纸把旧纸推下去。这个限制叫<strong>上下文窗口</strong>。</li>
<li><strong>成本：</strong>许多AI服务按token收费。</li>
<li><strong>记忆：</strong>上下文窗口溢出时AI"忘记"更早的内容。</li>
</ol>

<h2>第2章：提示词工程——如何让AI理解你的任务</h2>

<p>早期AI用户对"输入问题，得到答案"感到兴奋。但很快发现<em>如何</em>提问很重要：</p>
<ul>
<li>模糊：<em>"帮我写产品方案。"</em>→ 通用、无用的输出</li>
<li>详细：<em>"你是一名高级产品经理。为面向开发者的AI工具写产品方案。包含目标用户、核心痛点、功能模块、商业模式和上市策略。用表格输出。"</em>→ 结构化、相关的结果</li>
</ul>

<p>好的提示词包含：<strong>角色</strong>（AI应扮演谁）、<strong>任务</strong>（明确目标）、<strong>背景</strong>（上下文信息）、<strong>格式</strong>（输出结构）、<strong>约束</strong>（避免什么）和<strong>示例</strong>（期望输出）。</p>

<h2>第3章：RAG（检索增强生成）——AI如何查找和使用外部信息</h2>

<p>AI不知道没被训练过的内容——比如你公司的内部文档或昨天的新闻。<strong>RAG</strong>通过让AI"先搜索，再回答"来解决这个问题。</p>

<p>RAG流程：</p>
<ol>
<li><strong>摄入数据：</strong>将文档添加到知识库</li>
<li><strong>文本嵌入：</strong>将文本转换为数值向量（Embeddings）以判断语义相似度</li>
<li><strong>检索：</strong>当你提问时，系统从向量数据库中检索相关片段</li>
<li><strong>生成：</strong>AI基于检索到的信息回答</li>
</ol>

<p>示例：问<em>"请假需要提前几天申请？"</em>RAG搜索员工手册，检索相关政策，然后带引用回答。</p>

<pre><code class="language-python">from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
import pinecone

pinecone.init(api_key="your-api-key", environment="your-environment")
index = pinecone.Index("your-index-name")

embeddings = OpenAIEmbeddings()
vector_store = Pinecone.from_texts(
    texts=["你的公司政策文本..."],
    embedding=embeddings,
    index_name="your-index-name"
)

query = "如何申请请假？"
docs = vector_store.similarity_search(query)
print(docs[0].page_content)</code></pre>

<h2>第4章：工具调用——AI如何在文本之外采取行动</h2>

<p>RAG让AI获取信息，<strong>工具调用</strong>（Function Calling）让AI<em>行动</em>——查询实时数据、执行代码或与应用交互。</p>

<ul>
<li>问：<em>"我的订单状态是什么？"</em>→ AI调用电商API → <em>"订单#12345：已发货。"</em></li>
<li>问：<em>"运行这段Python代码：print(2+2)"</em>→ AI执行 → <em>"4"</em></li>
</ul>

<p>用JSON定义工具Schema（名称和参数），然后在提示词中指示AI在需要时使用该工具。</p>

<h2>第5章：MCP（模型组件协议）——AI如何统一连接工具</h2>

<p>随着工具增多，连接变得混乱——每个工具有自己的接口。<strong>MCP</strong>是AI连接外部工具的标准协议，就像电子设备的USB-C。它标准化了工具如何暴露能力、AI如何发现和调用工具、以及参数、返回值和安全的处理方式。</p>

<h2>第6章：上下文工程——AI应该看到什么信息？</h2>

<p>除了写好提示词，你还需要管理AI接收的<em>信息流</em>——这就是<strong>上下文工程</strong>。对于AI客服Agent，上下文可能包括：购买历史、过往工单、当前订单状态和退款政策。上下文太少→错误答案；太多→混乱。使用LlamaIndex等工具自动化上下文组装。</p>

<h2>第7章：Skill——AI如何复用经过验证的工作流</h2>

<p><strong>Skill</strong>是将重复任务转化为可复用AI工作流。不用每次都解释"如何写周报"，将指令保存为Skill：</p>
<ol>
<li>从项目管理工具获取已完成任务</li>
<li>提取关键成就和风险</li>
<li>格式化为模板</li>
<li>调整语气匹配公司标准</li>
</ol>
<p>使用Dify或Microsoft Copilot Studio等工具创建和部署Skills。</p>

<h2>第8章：Computer Use——AI如何像人类一样操作桌面/网页</h2>

<p>不是所有系统都有API。<strong>Computer Use</strong>让AI像人类一样与软件和网页交互——点击按钮、填写表单、导航UI。示例：无需API自动提交报销单——AI打开报销门户、登录、填写金额、附上收据、提交表单。</p>

<h2>第9章：Agent——AI如何自主完成复杂任务</h2>

<p><strong>Agent</strong>是能规划、行动和适应以完成目标的AI。与聊天机器人（响应查询）或工具调用AI（单次操作）不同，Agent能：</p>
<ol>
<li><strong>规划：</strong>将目标分解为步骤</li>
<li><strong>行动：</strong>调用工具、使用Skills、与计算机交互</li>
<li><strong>反思：</strong>根据结果调整计划</li>
</ol>

<p>示例：编程Agent修复Bug——从错误信息识别Bug→获取代码文件→修改代码→运行测试→测试失败则重复。</p>

<pre><code class="language-python">from langchain.agents import AgentType, initialize_agent, load_tools

tools = load_tools(["serpapi", "llm-math"], llm=your_llm)
agent = initialize_agent(
    tools, your_llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)
agent.run("东京天气如何？然后计算距离夏至还有多少天。")</code></pre>

<h2>第10章：Harness工程——如何安全部署Agent</h2>

<p>Agent强大但有风险——可能删除文件、写出糟糕代码或访问敏感数据。<strong>Harness工程</strong>提供安全保障：<strong>沙箱</strong>（限制Agent只修改测试分支而非生产代码）、<strong>审批流程</strong>（关键操作需人类签字）和<strong>日志审计</strong>（追踪Agent每项操作）。从沙箱开始——让Agent先推送到staging分支，由人类合并到main。</p>

<h2>第11章：Workflow——如何将AI和工具编排为流程</h2>

<p>实际工作是系列步骤。<strong>Workflow</strong>工具（n8n、Zapier、LangGraph）将AI操作、工具调用和人类审批串联成自动化流程。示例："新客户咨询→AI生成回复→人类审批→发送邮件→记录到CRM。"</p>

<pre><code class="language-python">from langgraph.graph import StateGraph, START

graph = StateGraph()

def generate_response(state):
    return {"response": your_llm.generate(state["inquiry"])}

def human_approve(state):
    return {"approved": input("批准？(y/n)") == "y"}

def send_email(state):
    return {"email_sent": True}

graph.add_node("generate", generate_response)
graph.add_node("approve", human_approve)
graph.add_node("send", send_email)
graph.add_edge(START, "generate")
graph.add_edge("generate", "approve")
graph.add_edge("approve", "send", cond=lambda s: s["approved"])

app = graph.compile()
result = app.invoke({"inquiry": "我对你们的产品感兴趣。"})</code></pre>

<h2>第12章：Workspace Agent——AI如何成为团队成员</h2>

<p><strong>Workspace Agent</strong>存在于团队工作环境中，理解长期上下文：团队项目和任务、文档位置、客户历史、基于角色的权限。示例：自动起草周报——从项目管理工具拉取已完成任务、从会议中识别风险、总结代码提交、格式化后送审。使用CrewAI等工具管理工作空间内的Agent角色和工作流。</p>

<h2>结语：AI术语是地图，不是迷宫</h2>

<p>每个术语——从Token到Workspace Agent——解决了让AI对实际工作有用的特定问题。不要迷失在术语中，专注<em>每个概念解决什么问题</em>和<em>你如何应用它</em>。从小处开始：用提示词工程获得更好的输出，然后添加RAG获取外部知识，接着工具调用执行操作，逐步构建。不知不觉中，你将自信地在AI领域中导航。</p>

<h2>常见问题</h2>

<h3>初学者最应该先掌握哪个概念？</h3>
<p>提示词工程。它是所有其他概念的基础——甚至RAG、Agent和工作流最终都依赖于给AI清晰的指令。先掌握角色-任务-背景-格式-约束-示例框架。一旦你能从简单的聊天界面持续获得高质量输出，其他概念（RAG、工具调用、Agent）就成为自然的扩展而非令人困惑的抽象。大多数初学者试图直接跳到构建Agent而没有扎实的提示词技能，结果是Agent做不可预测的事情时感到沮丧。</p>

<h3>RAG、工具调用和Agent之间有什么区别？</h3>
<p>将它们想象成AI能力的逐步升级：<strong>RAG</strong>让AI<em>读取</em>外部信息（搜索文档、检索事实）。<strong>工具调用</strong>让AI<em>行动</em>（调用API、运行代码、发送邮件）。<strong>Agent</strong>结合两者再加上规划——它们决定<em>何时</em>读取、<em>何时</em>行动以及<em>如何</em>在出错时调整。带RAG的聊天机器人能回答"退款政策是什么？"带工具调用的AI能处理"退款订单#12345。"Agent能处理"客户因延迟交付不满——弄清楚发生了什么并妥善解决。"</p>

<h3>使用这些AI概念需要会编程吗？</h3>
<p>概念本身不需要——你可以无需编码使用提示词工程、Skills（通过Dify等无代码工具）和基础工作流（通过Zapier或n8n的可视化编辑器）。RAG和工具调用有一些编码知识会更容易但有无代码替代方案（NotebookLM做RAG，扣子做基于工具的Agent）。Computer Use和Harness工程更偏代码。本指南的章节大致按技术性从低到高排列——从第1章开始，根据你的舒适程度尽可能深入。每章都以前面章节为基础，所以即使停在第7章，你也会有一个扎实的实践基础。</p>

<div class="next-step">
<p><strong>上一篇：</strong> <a href="/zh/article/mastering-ai-workflow-beginner-custom-workbench">掌握AI工作流：新手友好的自定义AI工作台搭建指南 ←</a></p>
</div>`,
  },

'''

last_brace = content_src.rfind('};')
content_new = content_src[:last_brace] + new_contents + '};'

with open('src/lib/article-content.ts', 'w', encoding='utf-8') as f:
    f.write(content_new)

print('Part 2: 1 article content added to article-content.ts')

print('\n=== All done! Run build to verify ===')
