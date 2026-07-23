"""
Publish July 23, 2026 — 1 article, no new tools.
(Skipped "2026 Local LLM Benchmark" — duplicate of July 21 article)
"""
import os

BASE = r"C:\Users\jun\aistudyonline-next"
os.chdir(BASE)

with open('src/lib/articles.ts', 'r', encoding='utf-8') as f:
    articles_src = f.read()

new_articles = r"""  {
    slug: "why-99-percent-ai-knowledge-bases-fail-in-practice",
    title: "Why 99% of AI Knowledge Bases Fail in Practice",
    titleZh: "为什么99%的AI知识库在实践中失败：RAG深度解析",
    description: "A deep dive into why most AI knowledge bases fail — covering RAG fundamentals, ingestion pipeline (cleaning, semantic chunking, vectorization), QA pipeline (question understanding, reranking, context assembly), four-layer implementation, hybrid retrieval, and practical lessons from real enterprise projects.",
    descriptionZh: "深度解析AI知识库失败的根源——RAG核心原理、摄入管线（清洗、语义分块、向量化）、问答管线（问题理解、重排序、上下文组装）、四层实施方法、混合检索和企业实战经验。",
    category: "AI Learning",
    tags: ["RAG", "Knowledge Base", "Vector Database", "Enterprise AI", "Chunking", "Embedding", "Engineering"],
    difficulty: "advanced",
    toolsMentioned: [],
    date: "2026-07-23",
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
  "why-99-percent-ai-knowledge-bases-fail-in-practice": {
    content: `<div class="meta-banner">
  <span class="meta-badge">📚 AI Learning</span>
  <span class="meta-badge">🕒 12 min read</span>
  <span class="meta-badge">📅 Jul 23, 2026</span>
  <span class="meta-badge">🎯 Advanced</span>
</div>

<h2 id="introduction">Introduction</h2>

<p>Many people think building an AI knowledge base is as simple as dumping company documents into a vector database and connecting a large language model (LLM). However, this approach often leads to real-world issues: the AI either fails to answer or provides incorrect responses, retrieves the wrong information or treats outdated documents as the latest conclusions, and invents answers even when the company has standard processes. In this article, we will break down the core concepts of AI knowledge bases, the differences between demos and real-world implementations, and how to design a truly usable system.</p>

<h2 id="rag">Understanding RAG: Retrieval-Augmented Generation</h2>

<p>RAG stands for <strong>Retrieval-Augmented Generation</strong>. The key idea is not to make the model "smarter," but to equip it with an external brain that can look up information.</p>

<p>Large language models are good at speaking, reasoning, and summarizing, but they have three inherent limitations:</p>
<ol>
  <li>They don't know the company's internal information</li>
  <li>They don't know the latest updates to documents</li>
  <li>They can generate plausible-sounding answers even when they don't know the facts</li>
</ol>

<p>For example, if you ask the model about the company's refund process, it might make up a reasonable-sounding process. But if you first let it search the knowledge base for the latest refund SOP, customer service scripts, and financial approval rules, then generate an answer based on these materials — that's the core logic of RAG.</p>

<p>RAG essentially has two steps: <strong>retrieval</strong> and <strong>generation</strong>. While this logic sounds simple, the real engineering challenges lie in the middle layer: how to split, store, search, sort, and insert context, and how to determine if the answer is incorrect. These are the factors that determine whether the system works well.</p>

<h2 id="workflows">The Two Core Workflows of a RAG System</h2>

<h3>1. Ingestion Pipeline: Converting Knowledge into Machine-Readable Format</h3>

<p>This workflow converts company knowledge into a format that machines can search. It can handle various document types — product documents, API docs, Feishu pages, Notion pages, customer service tickets, meeting minutes, code READMEs, and database table structures.</p>

<p>However, you can't just throw these documents in as-is. The ingestion process has three key steps:</p>

<ul>
  <li><strong>Cleaning</strong>: Remove meaningless formats, duplicate content, and retain important information such as titles, hierarchy, update time, author, permissions, and business lines.</li>
  <li><strong>Chunking</strong>: This is a critical step. Many knowledge bases fail not because of the model, but because of poor chunking. For example, if you split a complete refund process in the middle — first half about application conditions, second half about approval rules — when a user asks about the refund process, the system might only retrieve the second half, and the AI will lack context. <strong>Best Practice</strong>: Chunk by semantic meaning, not just by word count. A complete small topic should be placed in the same chunk. Chunks should not be too large (reduces retrieval accuracy, wastes tokens) or too small (breaks information into pieces the AI can't assemble).</li>
  <li><strong>Vectorization</strong>: Convert text into numerical coordinates. If two pieces of text have similar meanings, they will be close to each other in this coordinate space. For example, "how to return a laptop when leaving a job" and "equipment recycling process after terminating labor relations" — vector search finds the similarity even though keywords differ. <strong>Note</strong>: Vector search is not universal. It's good at semantic similarity but not at handling version numbers, dates, departments, permissions, product lines, regions, or contract types. In real projects, you need <strong>hybrid retrieval</strong>: vector search for semantic relevance, keyword search for exact matches, and metadata filtering.</li>
</ul>

<h3>2. Question-Answering Pipeline: Understanding and Responding to User Queries</h3>

<p>When a user asks a question, the system should first understand the question, not just search with the user's exact words. In real projects, user questions are often very colloquial. For example, "how to refund for this customer" contains at least several implicit pieces of information: who the customer is, what product they bought, whether the refund period has passed, whether the invoice has been issued, whether it's domestic or international, and whether there are special contract terms.</p>

<p>A mature RAG system doesn't rush to answer. Instead, it first checks if the question is complete. If key information is missing, it should ask follow-up questions. Many AI products fail because they are too eager to show off, generating long answers to vague questions that are full of risks.</p>

<p>After retrieval, you can't just send the top 5 pieces of information to the model. You need to do <strong>reranking</strong>. The first round of retrieval is like casting a net — getting a batch of potentially relevant materials, but some are only superficially relevant. Reranking uses a more refined model to determine which pieces of information are most worth including in the context.</p>

<p><strong>Key Insight</strong>: More information doesn't always mean better results. When you change from top 5 to top 10, the effect may not improve because more information brings more noise. The model can get confused when given conflicting information. RAG is not about retrieving more, but about retrieving more accurately.</p>

<p>The third step is <strong>context assembly</strong>. You can't just dump the information into the model. You need to tell the model: which parts are the user's question, which parts are the retrieved information, which parts are system rules, which information is more recent, and which information has higher priority. It's also best to require the model to cite sources when answering — document titles, update times, and source links. This is not for aesthetics, but to make the answers traceable. The most important indicator of an enterprise AI knowledge base is not how human-like the answers are, but whether the answers can be verified.</p>

<h2 id="implementation">Practical Implementation: How to Launch a RAG Project</h2>

<p>When building an AI knowledge base in a company, don't start with the goal of "building a company-wide brain" — that's too big. The best starting point is to find a scenario that is <strong>high-frequency, low-risk, and has relatively stable information</strong>.</p>

<h3>Recommended Starting Scenarios</h3>
<ol>
  <li><strong>Internal R&D Q&A</strong>: Developers ask questions like how to start a service, where to find API documents, what error codes mean, and how the release process works. These questions have clear information and answers, and it's easy to correct mistakes.</li>
  <li><strong>Customer Service Knowledge Base</strong>: Customer service representatives repeatedly ask about product rules, after-sales processes, script templates, and complaint escalation paths. These scenarios are very suitable for RAG.</li>
  <li><strong>Code Knowledge Base</strong>: This is more difficult because code is not ordinary documents. You can't just chunk by natural language; you need to consider functions, classes, files, modules, and dependencies.</li>
</ol>

<h3>Four-Layer Implementation Approach</h3>
<ol>
  <li><strong>Data Layer</strong>: Where does the knowledge come from? Exclude outdated documents, drafts, and documents with unclear permissions. Merge duplicate content and mark conflicting content.</li>
  <li><strong>Index Layer</strong>: How to make the information searchable. This usually includes vector indexing, keyword indexing, and metadata indexing.</li>
  <li><strong>Reasoning Layer</strong>: How the LLM answers based on retrieved information. The most important rule is not to make the model sound friendly, but to constrain it from making up information. If there's no retrieved information, say "I don't know." If there's conflicting information, point it out first.</li>
  <li><strong>Feedback Layer</strong>: Record whether users find the answers useful, whether they follow up, whether they complain, and whether the answers are incorrect. A knowledge base requires continuous adjustment of chunks, recall, ranking, adding documents, and modifying prompts.</li>
</ol>

<h2 id="misconceptions">Common Misconceptions and Best Practices</h2>

<h3>1. Context Window Size</h3>
<p>Many people think a larger context window is better. While models can support hundreds of thousands of tokens, this is not always optimal. Longer context means higher costs, higher latency, more noise, and diluted model attention. It's better to give the model three pages of precise information than three hundred pages of contracts. The core of context management is <strong>compression and selection</strong>: Immediate Context (current question + recent follow-ups), Retrieval Context (knowledge base results), and Long-Term Memory (user profiles, preferences, permissions).</p>

<h3>2. AI Memory</h3>
<p>Large language models don't truly remember company knowledge. The so-called "memory" in the application layer usually has three implementations: Conversational Memory (short-term), User Memory (preferences, projects, department), and Knowledge Memory (documents, processes, code — best suited for RAG). Knowledge memory should not be hard-coded in prompts or trained into the model, because company knowledge changes. If you train it into the model, the update cost is too high.</p>

<h3>3. Practical Lessons from Real Projects</h3>
<ol>
  <li><strong>Don't pursue full automation at the beginning</strong>: Let AI provide answers first, then sources, then confidence scores, and let humans confirm important questions.</li>
  <li><strong>Must cite sources</strong>: An enterprise knowledge base without source citations can't build trust.</li>
  <li><strong>Handle outdated knowledge</strong>: If both 2024 and 2026 processes are in the knowledge base, the system might retrieve old documents if it doesn't check the update time.</li>
  <li><strong>Permissions must be upfront</strong>: If a user doesn't have permission to view a document, the document should not be retrieved in the first place, not filtered after the AI answers.</li>
  <li><strong>Have an evaluation set</strong>: Collect 50 to 200 high-frequency real questions, each with a standard answer and source. Run the evaluation every time you change chunking, embedding, reranking, or prompts.</li>
</ol>

<h2 id="true-value">The True Value of AI Knowledge Bases</h2>

<p>The true value of an AI knowledge base is not to make employees open fewer documents. It's more like installing a knowledge scheduling system for the company. In the past, knowledge was scattered in Feishu, code repositories, group chats, and meeting minutes. Everyone had to find it based on experience — new employees couldn't find it, old employees were too lazy to explain, and when information changed, everyone might use old answers.</p>

<p>When RAG is done well, the AI becomes an entry point. You can ask business questions, and it knows which documents to check. You can ask technical questions, and it can find relevant code and design descriptions. You can ask about processes, and it can tell you the latest version and the person in charge.</p>

<p>The most important point: <strong>AI knowledge bases don't replace knowledge management; they force companies to redo knowledge management</strong>. If the documents are unclear, the AI will be unclear. If the processes are inconsistent, the AI will be inconsistent. If the permissions are not clean, the AI might leak information. A good team doesn't just deploy a RAG framework — they integrate document management, retrieval systems, LLM reasoning, permission systems, feedback, and evaluation into a single system.</p>

<h2 id="conclusion">Final Thoughts</h2>

<p>Building a practical AI knowledge base is more about engineering than technology. It requires careful consideration of data ingestion, retrieval strategies, context management, and continuous iteration based on feedback. The key is to start small, focus on high-value scenarios, and build trust through traceable, verifiable answers.</p>

<h2>常见问题</h2>

<h3>What's the single biggest reason AI knowledge bases fail?</h3>
<p><strong>Poor chunking strategy.</strong> Most teams use naive chunking — split by 500 tokens, regardless of content. This breaks semantic units in half, so the retrieval system returns fragments that the LLM can't assemble into coherent answers. The fix is surprisingly simple: chunk by semantic boundaries (paragraphs, sections, topics), not by token count. A complete FAQ entry, a full API endpoint description, or an entire process step should stay in one chunk. The second biggest reason is skipping the reranking step — dumping top-K retrieval results directly into the prompt without filtering for relevance. Adding a reranking model (even a simple cross-encoder) typically improves answer quality by 20-30%.</p>

<h3>How is this different from the WorkBuddy+IMA knowledge base guide?</h3>
<p>The WorkBuddy+IMA guide (July 15) is a <strong>hands-on tutorial</strong> for building a personal knowledge base using specific tools. This article is a <strong>conceptual deep dive</strong> into why knowledge bases fail and how to design them correctly — it covers the engineering principles (chunking, reranking, hybrid retrieval, context assembly, evaluation) that apply regardless of which tools you use. Read the WorkBuddy+IMA guide to build your first knowledge base today. Read this article to understand why it works (or doesn't) and how to improve it. They're complementary: the tutorial gives you the recipe; this article explains the food science.</p>

<h3>Do I need a vector database to build a RAG system?</h3>
<p>For prototypes and small-scale projects (hundreds of documents), no — you can use in-memory vector stores (FAISS, Chroma) or even numpy arrays. For production systems with thousands of documents or multiple users, yes — a dedicated vector database (Pinecone, Weaviate, Milvus, Qdrant) provides the performance, filtering, and scalability you need. The article's point about hybrid retrieval (vector + keyword + metadata) is where vector databases become essential: you need to filter by department, date range, and document type simultaneously with semantic search, which in-memory solutions don't handle well at scale.</p>

<h3>How long does it take to build a production-ready RAG system?</h3>
<p>A demo (one document type, basic chunking, no reranking, no evaluation) takes 1-2 days. A production-ready system for a single department (one document type, proper chunking, reranking, source citation, evaluation set) takes 2-4 weeks. A company-wide system with multiple document types, permission layers, hybrid retrieval, feedback loops, and continuous evaluation takes 2-3 months of iterative work. The article's recommendation to start with a high-frequency, low-risk scenario is designed to get you to the 2-4 week milestone quickly — you learn the real engineering challenges on a manageable scope before scaling to the whole company.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Understand RAG theory? Put it into practice:</p>
  <ul>
    <li><a href="/articles/build-personal-ai-knowledge-base-workbuddy-ima-guide">Build Your Personal AI Knowledge Base with WorkBuddy + IMA</a> — hands-on knowledge base tutorial</li>
    <li><a href="/articles/dont-be-intimidated-ai-jargon-practical-guide-concepts">Don't Be Intimidated by AI Jargon: A Practical Guide to AI Concepts</a> — RAG explained in the broader AI concept map</li>
    <li><a href="/articles/understanding-large-language-models-principles-architecture">Understanding Large Language Models: Principles, Architecture, and Practical Usage</a> — understand the LLM that powers the "G" in RAG</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">📚 AI 学习</span>
  <span class="meta-badge">🕒 阅读约12分钟</span>
  <span class="meta-badge">📅 2026年7月23日</span>
  <span class="meta-badge">🎯 高级</span>
</div>

<h2 id="introduction">引言</h2>

<p>很多人以为搭建AI知识库就是把公司文档扔进向量数据库，再接一个大语言模型就完事了。然而这种做法往往导致现实问题：AI要么不回答要么乱回答，检索到错误信息或把过期文档当最新结论，明明公司有标准流程却凭空编造答案。本文将拆解AI知识库的核心概念、Demo与真实落地的区别，以及如何设计一个真正可用的系统。</p>

<h2 id="rag">理解RAG：检索增强生成</h2>

<p>RAG全称<strong>Retrieval-Augmented Generation（检索增强生成）</strong>。核心理念不是让模型"更聪明"，而是给它配一个能查资料的外部大脑。</p>

<p>大语言模型擅长说话、推理和总结，但有三个先天局限：</p>
<ol>
  <li>不知道公司内部信息</li>
  <li>不知道文档最新更新</li>
  <li>不知道事实时也能生成听起来合理的回答</li>
</ol>

<p>举个例子，如果你问模型公司退款流程，它可能编造一个听起来合理的流程。但如果先让它搜索知识库中最新的退款SOP、客服话术和财务审批规则，再基于这些材料生成回答——这就是RAG的核心逻辑。</p>

<p>RAG本质就两步：<strong>检索</strong>和<strong>生成</strong>。逻辑听起来简单，但真正的工程挑战在中间层：怎么切分、怎么存储、怎么搜索、怎么排序、怎么插入上下文、怎么判断回答不对。这些才是决定系统好不好用的关键。</p>

<h2 id="workflows">RAG系统的两大核心工作流</h2>

<h3>1. 摄入管线：把知识变成机器可读格式</h3>

<p>这个工作流把公司知识转化为机器可搜索的格式。可处理各类文档——产品文档、API文档、飞书页面、Notion页面、客服工单、会议纪要、代码README甚至数据库表结构。</p>

<p>但不能原样扔进去。摄入过程有三个关键步骤：</p>

<ul>
  <li><strong>清洗</strong>：去除无意义格式、重复内容，保留标题、层级、更新时间、作者、权限、业务线等重要信息。</li>
  <li><strong>分块</strong>：这是最关键的一步。很多知识库失败不是因为模型，而是因为分块策略差。比如把完整退款流程从中间切开——前半段是申请条件，后半段是审批规则——用户问退款流程时，系统可能只检索到后半段，AI缺乏上下文。<strong>最佳实践</strong>：按语义分块，不是按字数。一个完整的小主题应该放在同一个块里。块不能太大（降低检索精度、浪费token）也不能太小（把信息切碎，AI拼不成完整答案）。</li>
  <li><strong>向量化</strong>：把文本转换成一串数值坐标。如果两段文本意思相近，它们在坐标空间中就近。比如用户问"离职怎么退电脑"，文档写的是"终止劳动关系后的设备回收流程"——向量搜索能找到相似性，虽然关键词不同。<strong>注意</strong>：向量搜索不是万能的。它擅长语义相似，但不擅长处理版本号、日期、部门、权限、产品线、地区、合同类型等精确条件。真实项目中需要<strong>混合检索</strong>：向量搜索做语义相关、关键词搜索做精确匹配、元数据过滤。</li>
</ul>

<h3>2. 问答管线：理解并响应用户查询</h3>

<p>用户提问时，系统应该先理解问题，而不是直接用用户原话搜索。真实项目中用户问题往往很口语化。比如"这个客户怎么退款"至少包含几层隐含信息：客户是谁、买了什么产品、是否过了退款期、是否已开发票、国内还是国际订单、有没有特殊合同条款。</p>

<p>成熟的RAG系统不会急着回答。它首先检查问题是否完整。关键信息缺失时，应该反问。很多AI产品失败就是因为太急于表现，对模糊问题生成长篇大论的回答，充满风险。</p>

<p>检索后不能直接把top 5信息塞给模型。需要做<strong>重排序</strong>。第一轮检索像撒网——捞到一批潜在相关材料，但有些只是表面相关。重排序用更精细的模型判断哪些信息最值得放进上下文。</p>

<p><strong>关键洞察</strong>：信息不是越多越好。从top 5改成top 10，效果可能不升反降，因为更多信息带来更多噪音。模型看到矛盾信息会混淆。RAG不是检索更多，而是检索更准。</p>

<p>第三步是<strong>上下文组装</strong>。不能把信息一股脑倒给模型。需要告诉模型：哪些是用户问题、哪些是检索到的信息、哪些是系统规则、哪些信息更新、哪些信息优先级更高。最好还要求模型回答时注明出处——文档标题、更新时间和来源链接。这不是为了好看，是为了让回答可追溯。企业AI知识库最重要的指标不是回答多像人，而是回答是否可验证。</p>

<h2 id="implementation">实战落地：如何启动RAG项目</h2>

<p>在公司搭建AI知识库，不要一上来就奔着"建一个公司级大脑"——目标太大了。最佳切入点是找一个<strong>高频、低风险、信息相对稳定</strong>的场景。</p>

<h3>推荐起步场景</h3>
<ol>
  <li><strong>内部研发问答</strong>：开发者常问怎么启动服务、API文档在哪、错误码什么意思、发布流程怎么走。这些问题信息清晰、答案明确、改错容易。</li>
  <li><strong>客服知识库</strong>：客服反复问产品规则、售后流程、话术模板、投诉升级路径。这些场景非常适合RAG。</li>
  <li><strong>代码知识库</strong>：难度更大，因为代码不是普通文档。不能按自然语言分块，需要考虑函数、类、文件、模块和依赖关系。</li>
</ol>

<h3>四层实施方法</h3>
<ol>
  <li><strong>数据层</strong>：知识从哪来？排除过期文档、草稿和权限不清的文档。合并重复内容，标注冲突内容。</li>
  <li><strong>索引层</strong>：如何让信息可搜索。通常包括向量索引、关键词索引和元数据索引。</li>
  <li><strong>推理层</strong>：LLM如何基于检索到的信息回答。最重要的规则不是让模型说话好听，而是约束它不能编造信息。没有检索到信息就说"不知道"。有矛盾信息先指出。涉及权限、法律、财务、医疗的高风险问题不要直接下结论。</li>
  <li><strong>反馈层</strong>：记录用户觉得回答有没有用、有没有追问、有没有投诉、回答有没有错。知识库不是搭完就完事了，需要持续调整分块、召回、排序、补充文档、修改提示词。</li>
</ol>

<h2 id="misconceptions">常见误区和最佳实践</h2>

<h3>1. 上下文窗口大小</h3>
<p>很多人以为上下文窗口越大越好。模型确实能支持几十万token，但工程上不是最优解。更长上下文意味着更高成本、更高延迟、更多噪音和稀释的模型注意力。给模型三页精准信息比三百页合同强。上下文管理的核心是<strong>压缩和选择</strong>：即时上下文（当前问题+最近追问）、检索上下文（知识库结果）、长期记忆（用户画像、偏好、权限）。</p>

<h3>2. AI记忆</h3>
<p>大语言模型不会真正记住公司知识。应用层所谓的"记忆"通常有三种实现：对话记忆（短期）、用户记忆（偏好、项目、部门）、知识记忆（文档、流程、代码——最适合RAG）。知识记忆不应硬编码在提示词中或训练进模型，因为公司知识会变。训练进模型更新成本太高，还很难知道模型什么时候在用旧知识。</p>

<h3>3. 真实项目实战经验</h3>
<ol>
  <li><strong>不要一开始追求全自动化</strong>：让AI先给答案，再给来源，再给置信度，重要问题让人确认。</li>
  <li><strong>必须标注来源</strong>：没有来源引用的企业知识库无法建立信任。</li>
  <li><strong>处理过期知识</strong>：如果知识库里同时有2024年和2026年的流程，系统不检查更新时间就可能检索到旧文档。</li>
  <li><strong>权限必须前置</strong>：用户没权限看的文档，从一开始就不该被检索到，而不是AI回答完再过滤。</li>
  <li><strong>要有评估集</strong>：收集50到200个高频真实问题，每题有标准答案和标准来源。每次改分块策略、嵌入模型、重排序模型或提示词，都跑一遍评估。</li>
</ol>

<h2 id="true-value">AI知识库的真正价值</h2>

<p>AI知识库的真正价值不是让员工少打开几个文档。它更像是给公司装了一套知识调度系统。过去知识散落在飞书、代码仓库、群聊和会议纪要里，每个人凭经验找——新人找不到，老人懒得讲，信息变了大家都可能用旧答案。</p>

<p>RAG做好之后，AI变成一个入口。你可以问业务问题，它知道该查哪些文档。你可以问技术问题，它能找到相关代码和设计说明。你可以问流程，它能告诉你最新版本和负责人。</p>

<p>最重要的一点：<strong>AI知识库不是替代知识管理，而是倒逼公司重做知识管理</strong>。文档不清楚，AI就不清楚。流程不一致，AI就不一致。权限不干净，AI就可能泄露信息。好的团队不只是部署一个RAG框架，而是把文档管理、检索系统、LLM推理、权限系统、反馈和评估整合成一个系统。</p>

<h2 id="conclusion">结语</h2>

<p>搭建可用的AI知识库更多是工程问题而非技术问题。需要仔细考虑数据摄入、检索策略、上下文管理，以及基于反馈的持续迭代。关键是从小做起，聚焦高价值场景，通过可追溯、可验证的答案建立信任。</p>

<h2>常见问题</h2>

<h3>AI知识库失败的最大单一原因是什么？</h3>
<p><strong>糟糕的分块策略。</strong>大多数团队用朴素分块——按500 token切，不管内容。这会把语义单元切成两半，检索系统返回碎片，LLM拼不成连贯答案。修复出乎意料地简单：按语义边界分块（段落、章节、主题），不是按token数。一条完整FAQ、一个完整API端点描述、一个完整流程步骤应该留在同一个块里。第二大原因是跳过了重排序步骤——直接把top-K检索结果倒进提示词，不做相关性过滤。加一个重排序模型（哪怕简单的交叉编码器）通常能提升回答质量20-30%。</p>

<h3>这和WorkBuddy+IMA知识库指南有什么不同？</h3>
<p>WorkBuddy+IMA指南（7月15日）是<strong>实操教程</strong>，教你用特定工具搭建个人知识库。本文是<strong>概念深度解析</strong>，讲知识库为什么失败以及如何正确设计——涵盖的工程原则（分块、重排序、混合检索、上下文组装、评估）无论用什么工具都适用。读WorkBuddy+IMA指南今天就能搭第一个知识库。读本文理解它为什么好用（或不好用）以及如何改进。两者互补：教程给你菜谱，本文解释烹饪科学。</p>

<h3>搭建RAG系统需要向量数据库吗？</h3>
<p>原型和小规模项目（几百份文档）不需要——可以用内存向量存储（FAISS、Chroma）甚至numpy数组。生产系统有数千份文档或多用户，需要专用向量数据库（Pinecone、Weaviate、Milvus、Qdrant）提供性能、过滤和扩展能力。本文关于混合检索（向量+关键词+元数据）的观点正是向量数据库变得必不可少的地方：需要同时按部门、日期范围和文档类型过滤加语义搜索，内存方案在规模上处理不好。</p>

<h3>搭建一个生产可用的RAG系统需要多久？</h3>
<p>一个Demo（单一文档类型、基础分块、无重排序、无评估）需要1-2天。单个部门的生产可用系统（单一文档类型、正确分块、重排序、来源引用、评估集）需要2-4周。公司级系统含多种文档类型、权限层、混合检索、反馈闭环和持续评估需要2-3个月迭代。本文建议从高频低风险场景切入正是为了让你快速达到2-4周里程碑——在可控范围内学会真正的工程挑战，再扩展到整个公司。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>理解了RAG理论？付诸实践：</p>
  <ul>
    <li><a href="/articles/build-personal-ai-knowledge-base-workbuddy-ima-guide">WorkBuddy + IMA：搭建个人AI知识库的完整指南</a> — 知识库实操教程</li>
    <li><a href="/articles/dont-be-intimidated-ai-jargon-practical-guide-concepts">别被AI术语吓到：从Token到Workspace Agent的实用指南</a> — 在更广的AI概念地图中理解RAG</li>
    <li><a href="/articles/understanding-large-language-models-principles-architecture">大语言模型深度解读：从Transformer原理到实战应用</a> — 理解驱动RAG中"G"的LLM</li>
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