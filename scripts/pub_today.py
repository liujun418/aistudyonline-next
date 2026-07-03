"""
Publish July 3, 2026 — 2 articles, no new tools.
"""
import os

BASE = r"C:\Users\jun\aistudyonline-next"
os.chdir(BASE)

# ===== Part 1: Add 2 article metadata to articles.ts =====
with open('src/lib/articles.ts', 'r', encoding='utf-8') as f:
    articles_src = f.read()

new_articles = r"""  {
    slug: "understanding-large-language-models-principles-architecture",
    title: "Understanding Large Language Models: Principles, Architecture, and Practical Usage",
    titleZh: "大语言模型深度解读：从Transformer原理到实战应用",
    description: "A comprehensive guide breaking down LLM core principles, Transformer architecture with PyTorch implementation, common limitations (hallucinations, context decay, math errors), and practical tips for choosing and using models effectively in real-world tasks.",
    descriptionZh: "从Transformer架构原理到PyTorch代码实现，全面解读大语言模型的核心机制、常见局限（幻觉、上下文衰减、数学错误）以及实际使用中的模型选择与提示技巧。",
    category: "AI Learning",
    tags: ["LLM", "Transformer", "PyTorch", "AI Architecture", "Prompt Engineering", "Deep Learning"],
    difficulty: "Intermediate",
    toolsMentioned: ["PyTorch"],
    date: "2026-07-03",
  },
  {
    slug: "complete-guide-codex-zero-to-advanced",
    title: "Complete Guide to Codex: From Zero to Advanced Development Workflow",
    titleZh: "Codex完全指南：从零基础到高级开发工作流",
    description: "A step-by-step walkthrough of OpenAI Codex from installation and project setup through Git version control, agent.md configuration, Electron refactoring, plugins & skills, and mobile control — covering the complete development workflow for beginners and advanced users alike.",
    descriptionZh: "从安装配置、项目创建到Git版本控制、agent.md跨项目规则、Electron重构、插件与技能扩展、移动端控制，全方位覆盖Codex开发工作流的每一步操作。",
    category: "AI Tools",
    tags: ["Codex", "OpenAI", "AI Development", "CLI", "Git", "Electron", "Automation"],
    difficulty: "Beginner",
    toolsMentioned: ["Codex Agent", "Electron"],
    date: "2026-07-03",
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
  "understanding-large-language-models-principles-architecture": {
    content: `<div class="meta-banner">
  <span class="meta-badge">📚 AI Learning</span>
  <span class="meta-badge">🕒 10 min read</span>
  <span class="meta-badge">📅 Jul 3, 2026</span>
  <span class="meta-badge">🎯 Intermediate</span>
</div>

<h2 id="introduction">Introduction</h2>

<p>This guide will break down the core principles and architecture of large language models (LLMs) in an accessible way, with practical insights to help you use them more effectively. We'll start with the foundational technology behind LLMs—Transformer—and move through its components, limitations, and real-world applications.</p>

<h2 id="what-is-transformer">1. What is Transformer?</h2>

<p>Transformer is a neural network architecture introduced by Google in the 2017 paper <em>Attention Is All You Need</em>. Initially designed for machine translation, it revolutionized natural language processing (NLP) by replacing traditional RNN/CNN structures with self-attention mechanisms.</p>

<h3>Key Advantages of Transformer</h3>

<ul>
  <li><strong>Parallel Processing</strong>: Unlike RNNs, which process data sequentially, Transformer can handle all input tokens simultaneously, drastically improving speed.</li>
  <li><strong>Long-Range Dependencies</strong>: Self-attention allows the model to directly connect any two tokens in the input, avoiding the information loss that plagues RNNs for long sequences.</li>
  <li><strong>Better Performance</strong>: It achieves state-of-the-art results in both speed and quality for NLP tasks.</li>
</ul>

<h2 id="transformer-architecture">2. Transformer Architecture</h2>

<p>Transformer consists of two main components: <strong>Encoder</strong> and <strong>Decoder</strong>.</p>

<h3>Encoder</h3>

<p>The encoder processes input sequences (e.g., text) and converts them into intermediate representations that capture semantic meaning. Key steps include:</p>

<ol>
  <li><strong>Input Embeddings</strong>: Convert tokens into numerical vectors.</li>
  <li><strong>Positional Encodings</strong>: Add position information to embeddings to preserve word order.</li>
  <li><strong>Multi-Head Attention</strong>: Allow the model to focus on different parts of the input simultaneously.</li>
  <li><strong>Feed-Forward Network</strong>: Apply non-linear transformations to extract features.</li>
  <li><strong>Residual Connections & Layer Normalization</strong>: Stabilize training and improve performance.</li>
</ol>

<h3>Decoder</h3>

<p>The decoder generates output sequences (e.g., translations or text) using the encoder's outputs. It adds:</p>

<ol>
  <li><strong>Masked Multi-Head Attention</strong>: Prevent the model from looking at future tokens during generation.</li>
  <li><strong>Linear & Softmax Layers</strong>: Convert decoder outputs into probability distributions over the vocabulary.</li>
</ol>

<h2 id="practical-implementation">3. Practical Implementation: Building a Simple LLM</h2>

<p>You can implement a basic Transformer-based LLM using PyTorch. Here's a simplified example:</p>

<pre><code class="language-python">import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

# Simplified Transformer Decoder Layer
class TransformerDecoderLayer(nn.Module):
    def __init__(self, d_model, nhead, dim_feedforward=2048, dropout=0.1):
        super().__init__()
        self.self_attn = nn.MultiheadAttention(d_model, nhead, dropout=dropout)
        self.linear1 = nn.Linear(d_model, dim_feedforward)
        self.dropout = nn.Dropout(dropout)
        self.linear2 = nn.Linear(dim_feedforward, d_model)
        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)
        self.dropout1 = nn.Dropout(dropout)
        self.dropout2 = nn.Dropout(dropout)

    def forward(self, tgt, tgt_mask=None):
        tgt2 = self.self_attn(tgt, tgt, tgt, attn_mask=tgt_mask)[0]
        tgt = tgt + self.dropout1(tgt2)
        tgt = self.norm1(tgt)
        tgt2 = self.linear2(self.dropout(torch.relu(self.linear1(tgt))))
        tgt = tgt + self.dropout2(tgt2)
        tgt = self.norm2(tgt)
        return tgt

# Simplified Transformer Decoder
class TransformerDecoder(nn.Module):
    def __init__(self, vocab_size, d_model, nhead, num_layers, dim_feedforward=2048, dropout=0.1):
        super().__init__()
        self.d_model = d_model
        self.embedding = nn.Embedding(vocab_size, d_model)
        self.pos_encoding = nn.Parameter(torch.zeros(1, 1000, d_model))
        self.layers = nn.ModuleList([
            TransformerDecoderLayer(d_model, nhead, dim_feedforward, dropout)
            for _ in range(num_layers)
        ])
        self.linear = nn.Linear(d_model, vocab_size)

    def forward(self, tgt, tgt_mask=None):
        tgt = self.embedding(tgt) + self.pos_encoding[:, :tgt.size(1), :]
        for layer in self.layers:
            tgt = layer(tgt, tgt_mask)
        output = self.linear(tgt)
        return output

# Example usage
vocab_size = 10000
d_model = 512
nhead = 8
num_layers = 6

model = TransformerDecoder(vocab_size, d_model, nhead, num_layers)
input_seq = torch.randint(0, vocab_size, (1, 10))
output = model(input_seq)
print(output.shape)  # Expected: (1, 10, vocab_size)</code></pre>

<h2 id="llm-limitations">4. Understanding LLM Limitations</h2>

<p>LLMs have key limitations that affect their performance:</p>

<ul>
  <li><strong>Token-Based Billing</strong>: LLMs charge by tokens (subunits of text). More tokens mean higher cost and longer processing time.</li>
  <li><strong>Mathematical Inaccuracy</strong>: LLMs predict next tokens based on patterns, not actual calculation, so they often fail at complex math.</li>
  <li><strong>Hallucinations</strong>: They generate plausible but false information because they don't "know" facts—they just predict patterns.</li>
  <li><strong>Context Decay</strong>: Over long conversations, early details may be forgotten as new content dominates the model's attention.</li>
  <li><strong>Knowledge Gaps</strong>: LLMs have broad but shallow knowledge, often struggling with niche or highly technical details.</li>
</ul>

<h2 id="practical-tips">5. Practical Tips for Using LLMs Effectively</h2>

<h3>1. Understand LLM Capabilities and Limitations</h3>

<ul>
  <li>LLMs excel at text generation, content creation, and pattern recognition.</li>
  <li>They struggle with complex math, factual accuracy, and long-term memory.</li>
  <li>Be aware of token limits and context windows.</li>
</ul>

<h3>2. Set Clear Goals and Tasks</h3>

<ul>
  <li>Define your objective clearly (e.g., "Write a 500-word blog post about AI ethics" instead of "Write something about AI").</li>
  <li>Provide context and constraints to guide the model.</li>
</ul>

<h3>3. Choose the Right Model</h3>

<ul>
  <li>Prefer models trained on your specific domain (e.g., medical models for healthcare tasks).</li>
  <li>Larger models with more parameters generally perform better but cost more.</li>
</ul>

<h3>4. Master Prompt Engineering</h3>

<ul>
  <li>Use short, clear, and specific instructions.</li>
  <li>Provide examples to guide the model (e.g., "Write a product description like this example: [example text]").</li>
  <li>Break complex tasks into smaller steps.</li>
</ul>

<h3>5. Leverage Other Tools</h3>

<ul>
  <li>Use APIs to integrate LLMs with other tools (e.g., databases, spreadsheets).</li>
  <li>Adjust parameters like <code>temperature</code> (controls randomness) to fine-tune outputs.</li>
  <li>Explore advanced techniques like Retrieval-Augmented Generation (RAG) to add external knowledge.</li>
</ul>

<h2 id="conclusion">Conclusion</h2>

<p>Transformer is the backbone of modern LLMs, enabling parallel processing and long-range context understanding. While LLMs have limitations, understanding their architecture and behavior allows you to use them more effectively. By following the practical tips in this guide, you can leverage LLMs to boost productivity and solve real-world problems.</p>

<h2>常见问题</h2>

<h3>What's the core difference between Transformer and RNN?</h3>
<p>RNN processes tokens one by one sequentially — no parallel computation, and early information gets lost in long sequences. Transformer uses self-attention to process all tokens at once, letting each token directly connect with any other token regardless of distance. This enables parallel training and eliminates the long-range dependency problem. In practice, this means Transformer models train faster and understand context better, especially for documents longer than a few paragraphs.</p>

<h3>Why do LLMs hallucinate?</h3>
<p>LLMs are probability prediction engines — they predict the next most likely token based on patterns in training data, not by querying a fact database. When training data coverage is thin or inconsistent on a topic, the model generates plausible-sounding but factually wrong content. This is an architectural limitation, not a bug. RAG (Retrieval-Augmented Generation) is currently the most effective mitigation: it gives the model a "cheat sheet" of verified facts before it generates an answer.</p>

<h3>Which model should I start with for learning LLMs?</h3>
<p>Start with GPT-4o or Claude Sonnet — both have free tiers and excellent instruction-following. If you want to understand the internals, implement a simplified Transformer decoder in PyTorch (like the code in Section 3). Work through Embedding → Attention → LayerNorm → Feed-Forward step by step. The PyTorch implementation is about 50 lines and teaches you more than reading 10 papers.</p>

<h3>How do tokens affect cost and usage?</h3>
<p>Most APIs charge per token, typically $0.002–$0.06 per 1K tokens depending on the model. Both input and output count toward your total. A practical tip: summarize long documents before feeding them to the model — this can cut token usage by 80%+ while preserving the key information the model needs. OpenAI provides a free online Tokenizer tool to estimate token counts before making API calls.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Now that you understand LLM architecture, put it into practice:</p>
  <ul>
    <li><a href="/articles/demystifying-ai-application-layer-3-layers">Demystifying AI Application Layer: From LLMs to Agents in 3 Layers</a> — see where LLMs fit in the AI stack</li>
    <li><a href="/articles/dont-be-intimidated-ai-jargon-practical-guide-concepts">Don't Be Intimidated by AI Jargon: A Practical Guide to AI Concepts</a> — master the full AI concept map from Token to Workspace Agent</li>
    <li><a href="/articles/mastering-ai-workflow-beginner-custom-workbench">Mastering AI Workflow: Build Your Custom AI Workbench</a> — apply LLMs in a real productivity workflow</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">📚 AI 学习</span>
  <span class="meta-badge">🕒 阅读约10分钟</span>
  <span class="meta-badge">📅 2026年7月3日</span>
  <span class="meta-badge">🎯 中级</span>
</div>

<h2 id="introduction">引言</h2>

<p>本文将以通俗易懂的方式拆解大语言模型（LLM）的核心原理和架构，并提供实用建议帮你更高效地使用它们。我们从 LLM 的底层技术——Transformer 出发，逐步讲解其组件、局限性和实际应用。</p>

<h2 id="what-is-transformer">1. 什么是 Transformer？</h2>

<p>Transformer 是 Google 在 2017 年论文《Attention Is All You Need》中提出的神经网络架构。它最初用于机器翻译，通过自注意力机制替代传统的 RNN/CNN 结构，彻底改变了自然语言处理（NLP）领域。</p>

<h3>Transformer 的核心优势</h3>

<ul>
  <li><strong>并行处理</strong>：与 RNN 的串行处理不同，Transformer 可同时处理所有输入 token，速度大幅提升。</li>
  <li><strong>长距离依赖</strong>：自注意力机制让模型能直接连接输入中任意两个 token，避免 RNN 在长序列中的信息丢失问题。</li>
  <li><strong>性能领先</strong>：在 NLP 任务的速度和质量上都达到最优水平。</li>
</ul>

<h2 id="transformer-architecture">2. Transformer 架构</h2>

<p>Transformer 由两个主要组件构成：<strong>编码器（Encoder）</strong>和<strong>解码器（Decoder）</strong>。</p>

<h3>编码器</h3>

<p>编码器处理输入序列（如文本），将其转换为捕捉语义的中间表示。关键步骤包括：</p>

<ol>
  <li><strong>输入嵌入（Input Embeddings）</strong>：将 token 转换为数值向量。</li>
  <li><strong>位置编码（Positional Encodings）</strong>：为嵌入添加位置信息，保留词序。</li>
  <li><strong>多头注意力（Multi-Head Attention）</strong>：让模型同时关注输入的不同部分。</li>
  <li><strong>前馈网络（Feed-Forward Network）</strong>：应用非线性变换提取特征。</li>
  <li><strong>残差连接与层归一化</strong>：稳定训练过程，提升性能。</li>
</ol>

<h3>解码器</h3>

<p>解码器利用编码器的输出生成目标序列（如翻译结果或文本）。它额外包含：</p>

<ol>
  <li><strong>掩码多头注意力（Masked Multi-Head Attention）</strong>：防止模型在生成时"偷看"未来的 token。</li>
  <li><strong>线性层与 Softmax 层</strong>：将解码器输出转换为词汇表上的概率分布。</li>
</ol>

<h2 id="practical-implementation">3. 实战：用 PyTorch 构建简化版 LLM</h2>

<p>你可以用 PyTorch 实现一个基础的 Transformer 解码器。以下是简化版代码：</p>

<pre><code class="language-python">import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

# 简化版 Transformer 解码器层
class TransformerDecoderLayer(nn.Module):
    def __init__(self, d_model, nhead, dim_feedforward=2048, dropout=0.1):
        super().__init__()
        self.self_attn = nn.MultiheadAttention(d_model, nhead, dropout=dropout)
        self.linear1 = nn.Linear(d_model, dim_feedforward)
        self.dropout = nn.Dropout(dropout)
        self.linear2 = nn.Linear(dim_feedforward, d_model)
        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)
        self.dropout1 = nn.Dropout(dropout)
        self.dropout2 = nn.Dropout(dropout)

    def forward(self, tgt, tgt_mask=None):
        tgt2 = self.self_attn(tgt, tgt, tgt, attn_mask=tgt_mask)[0]
        tgt = tgt + self.dropout1(tgt2)
        tgt = self.norm1(tgt)
        tgt2 = self.linear2(self.dropout(torch.relu(self.linear1(tgt))))
        tgt = tgt + self.dropout2(tgt2)
        tgt = self.norm2(tgt)
        return tgt

# 简化版 Transformer 解码器
class TransformerDecoder(nn.Module):
    def __init__(self, vocab_size, d_model, nhead, num_layers, dim_feedforward=2048, dropout=0.1):
        super().__init__()
        self.d_model = d_model
        self.embedding = nn.Embedding(vocab_size, d_model)
        self.pos_encoding = nn.Parameter(torch.zeros(1, 1000, d_model))
        self.layers = nn.ModuleList([
            TransformerDecoderLayer(d_model, nhead, dim_feedforward, dropout)
            for _ in range(num_layers)
        ])
        self.linear = nn.Linear(d_model, vocab_size)

    def forward(self, tgt, tgt_mask=None):
        tgt = self.embedding(tgt) + self.pos_encoding[:, :tgt.size(1), :]
        for layer in self.layers:
            tgt = layer(tgt, tgt_mask)
        output = self.linear(tgt)
        return output

# 使用示例
vocab_size = 10000
d_model = 512
nhead = 8
num_layers = 6

model = TransformerDecoder(vocab_size, d_model, nhead, num_layers)
input_seq = torch.randint(0, vocab_size, (1, 10))
output = model(input_seq)
print(output.shape)  # 预期输出: (1, 10, vocab_size)</code></pre>

<h2 id="llm-limitations">4. 理解 LLM 的局限性</h2>

<p>LLM 有以下关键局限影响其表现：</p>

<ul>
  <li><strong>按 Token 计费</strong>：LLM 按 token（文本子单元）收费。token 越多，成本越高，处理时间越长。</li>
  <li><strong>数学不准确</strong>：LLM 基于模式预测下一个 token，而非实际计算，因此复杂数学容易出错。</li>
  <li><strong>幻觉（Hallucination）</strong>：模型生成看似合理但虚假的内容，因为它不"知道"事实——只是预测模式。</li>
  <li><strong>上下文衰减</strong>：在长对话中，早期细节可能被遗忘，因为新内容占据了模型的注意力。</li>
  <li><strong>知识盲区</strong>：LLM 知识面广但深度不足，在细分领域或高度技术性的细节上经常力不从心。</li>
</ul>

<h2 id="practical-tips">5. 高效使用 LLM 的实用技巧</h2>

<h3>1. 理解 LLM 的能力和局限</h3>

<ul>
  <li>LLM 擅长文本生成、内容创作和模式识别。</li>
  <li>在复杂数学、事实准确性和长期记忆方面存在短板。</li>
  <li>注意 token 限制和上下文窗口大小。</li>
</ul>

<h3>2. 设定清晰的目标和任务</h3>

<ul>
  <li>明确定义目标（如"写一篇 500 字关于 AI 伦理的博客"而非"写点关于 AI 的东西"）。</li>
  <li>提供上下文和约束条件来引导模型。</li>
</ul>

<h3>3. 选择合适的模型</h3>

<ul>
  <li>优先选择在特定领域训练的模型（如医疗模型用于医疗任务）。</li>
  <li>参数量更大的模型通常表现更好，但成本更高。</li>
</ul>

<h3>4. 掌握提示词工程</h3>

<ul>
  <li>使用简短、清晰、具体的指令。</li>
  <li>提供示例引导模型（如"参考这个例子写产品描述：[示例文本]"）。</li>
  <li>将复杂任务拆分为小步骤。</li>
</ul>

<h3>5. 善用其他工具</h3>

<ul>
  <li>通过 API 将 LLM 与数据库、电子表格等工具集成。</li>
  <li>调整参数如 <code>temperature</code>（控制随机性）来优化输出。</li>
  <li>探索高级技术如检索增强生成（RAG）来补充外部知识。</li>
</ul>

<h2 id="conclusion">总结</h2>

<p>Transformer 是现代 LLM 的基石，它实现了并行处理和长距离上下文理解。尽管 LLM 有局限性，理解其架构和行为能让你更高效地使用它们。遵循本文的实用建议，你可以利用 LLM 提升生产力，解决实际问题。</p>

<h2>常见问题</h2>

<h3>Transformer 和 RNN 的核心区别是什么？</h3>
<p>RNN 按顺序逐个处理 token，无法并行计算，且长序列容易丢失早期信息。Transformer 通过自注意力机制（Self-Attention）一次性处理所有 token，每个 token 可以直接与序列中任意位置的 token 建立联系，因此支持并行计算且不受距离限制。实际效果是 Transformer 模型训练更快、上下文理解更好，尤其是对于超过几段的长文档。</p>

<h3>为什么 LLM 会"幻觉"（Hallucination）？</h3>
<p>LLM 本质上是一个概率预测模型——它根据训练数据中的模式预测下一个最可能的 token，而不是"查询事实数据库"。当模型遇到训练数据覆盖不足或不一致的知识点时，它会生成看似合理但实际错误的内容。这是架构层面的固有限制，不是 bug。RAG（检索增强生成）是目前最有效的缓解方案：在生成回答前先给模型一份经过验证的"小抄"。</p>

<h3>我应该从哪个模型开始学习 LLM？</h3>
<p>建议从 GPT-4o 或 Claude Sonnet 开始，两者都有免费额度且指令遵循能力强。如果目标是学习底层原理，用 PyTorch 从简化版 Transformer 解码器开始实现（如本文第3节代码），逐步理解 Embedding → Attention → LayerNorm → Feed-Forward。约50行 PyTorch 代码教你的比读10篇论文还多。</p>

<h3>Token 数量如何影响成本和使用？</h3>
<p>大多数 API 按 token 计费，通常每 1000 token 约 $0.002–$0.06（取决于模型）。输入和输出都计入 token 总数。实用技巧：长文档先用摘要压缩再送入模型——可以削减 80% 以上 token 消耗，同时保留模型所需的关键信息。OpenAI 提供免费在线 Tokenizer 工具，可以在调用 API 前预估 token 数。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>理解了 LLM 架构之后，将其付诸实践：</p>
  <ul>
    <li><a href="/articles/demystifying-ai-application-layer-3-layers">拆解 AI 应用层：从大语言模型到智能体的三层体系</a> — 了解 LLM 在 AI 技术栈中的位置</li>
    <li><a href="/articles/dont-be-intimidated-ai-jargon-practical-guide-concepts">别被 AI 术语吓到：从 Token 到 Workspace Agent 的实用指南</a> — 掌握完整的 AI 概念地图</li>
    <li><a href="/articles/mastering-ai-workflow-beginner-custom-workbench">掌握 AI 工作流：打造你的专属 AI 工作台</a> — 将 LLM 应用于实际生产力工作流</li>
  </ul>
</div>`,
  },

  "complete-guide-codex-zero-to-advanced": {
    content: `<div class="meta-banner">
  <span class="meta-badge">🔧 AI Tools</span>
  <span class="meta-badge">🕒 12 min read</span>
  <span class="meta-badge">📅 Jul 3, 2026</span>
  <span class="meta-badge">🎯 Beginner</span>
</div>

<h2 id="introduction">Introduction</h2>

<p>Codex is OpenAI's core AI development tool, designed to assist with coding, debugging, testing, and even computer control. This guide will walk you through the complete workflow of using Codex, from installation to advanced features like plugins, skills, and mobile control.</p>

<h2 id="installation">1. Installation and Initial Setup</h2>

<h3>1.1 Download and Install Codex</h3>

<ul>
  <li>Visit the official Codex website and download the installation package.</li>
  <li>On macOS, drag the Codex app to the Applications folder to complete installation.</li>
</ul>

<h3>1.2 Login Options</h3>

<ul>
  <li><strong>ChatGPT Account Login</strong>: Choose from ChatGPT's subscription plans (Free, Go, Plus, Pro). Plus ($20/month) is recommended for balanced token limits.</li>
  <li><strong>API Key Login</strong>: Use an OpenAI API key (requires a foreign credit card, less cost-effective than subscriptions).</li>
</ul>

<h3>1.3 Initial Configuration</h3>

<ul>
  <li>Select your job role when prompted.</li>
  <li>Skip the "Import Cloud Code" step for now.</li>
  <li>You can set up Codex Mobile later (we'll cover this in Section 8).</li>
</ul>

<h2 id="basic-workflow">2. Basic Project Development Workflow</h2>

<h3>2.1 Create a Project</h3>

<ul>
  <li>Create a local folder (e.g., "Mark Note") to store your project files.</li>
  <li>In Codex, click "Work on a Project" → "Use an Existing Folder" and select your project folder.</li>
</ul>

<h3>2.2 First Project: Build a Markdown Note App</h3>

<ul>
  <li>Input your requirement:</li>
</ul>

<pre><code class="language-text">Build a note-taking app with HTML, with two columns: left for note list, right for note content. Include basic CRUD operations and local storage.</code></pre>

<ul>
  <li>Codex will generate code and ask for permission to start a local server. Choose "Yes" to allow it.</li>
</ul>

<h3>2.3 Preview and Iterate</h3>

<ul>
  <li>Click "Open in" to preview the app in a browser.</li>
  <li>Use the "Annotation" feature to select areas of the UI and request changes:</li>
</ul>

<pre><code class="language-text">Remove the two sample notes at the top of the left column.</code></pre>

<h3>2.4 Debugging</h3>

<ul>
  <li>If the "Add Note" button doesn't work, Codex will diagnose the issue (often due to preview environment restrictions).</li>
  <li>Test the app in an independent browser to confirm functionality.</li>
</ul>

<h2 id="advanced-config">3. Advanced Configuration and Security</h2>

<h3>3.1 Permission Modes</h3>

<ul>
  <li><strong>Default Permissions</strong>: Codex will prompt for approval before executing risky operations.</li>
  <li><strong>Auto-Review</strong>: A security agent automatically approves safe operations and blocks risky ones (recommended for balance of safety and efficiency).</li>
  <li><strong>Full Access</strong>: No prompts, but use with caution (risk of data loss).</li>
</ul>

<h3>3.2 Model Settings</h3>

<ul>
  <li><strong>Model Selection</strong>: Choose from GPT-5.5, GPT-5.4, etc., based on task complexity.</li>
  <li><strong>Thinking Depth</strong>: Adjust from Low to Extra High (higher depth = better code quality but slower speed).</li>
  <li><strong>Speed Mode</strong>: Enable "Fast" mode for 1.5x faster generation (consumes more tokens).</li>
</ul>

<h2 id="git">4. Version Control with Git</h2>

<h3>4.1 Initialize Git Repository</h3>

<ul>
  <li>Press <code>Command+J</code> to open the terminal in Codex.</li>
  <li>Run these commands:</li>
</ul>

<pre><code class="language-bash">git init
git add .
git commit -m "first commit"</code></pre>

<h3>4.2 Commit Changes</h3>

<ul>
  <li>Use Codex's built-in Git interface:</li>
  <ul>
    <li>Click the "Changes" icon → "Unstaged" to view modified files.</li>
    <li>Click "Commit", enter a message (e.g., "Change theme to blue"), and click "Continue".</li>
  </ul>
</ul>

<h3>4.3 Rollback with Fork</h3>

<ul>
  <li>Use the "Fork" feature to roll back conversations and code:</li>
  <ul>
    <li><strong>Fork into Local</strong>: Creates a new conversation but keeps the current code (use Git to roll back code manually).</li>
    <li><strong>Fork into New Worktree</strong>: Creates a new conversation and a separate project folder (no code rollback, but isolates changes).</li>
  </ul>
</ul>

<h2 id="agent-md">5. Cross-Project Configuration with agent.md</h2>

<h3>5.1 Create agent.md</h3>

<ul>
  <li>In your project folder, create a file named <code>agent.md</code>.</li>
  <li>Add rules like:</li>
</ul>

<pre><code class="language-markdown">- After every code change, run git commit with a descriptive message.
- Use React + TypeScript for all new components.
- Follow the project's color scheme (blue theme).</code></pre>

<h3>5.2 Test the Configuration</h3>

<ul>
  <li>Create a new conversation and ask Codex to add a feature (e.g., "Add a dark/light mode toggle").</li>
  <li>Check the Git log to confirm Codex automatically committed the changes.</li>
</ul>

<h2 id="refactoring">6. Project Refactoring and Advanced Features</h2>

<h3>6.1 Refactor to Electron Desktop App</h3>

<ul>
  <li>Use "Plan Mode" to let Codex create a refactoring plan:</li>
</ul>

<pre><code class="language-text">Refactor this web app to an Electron desktop app using React + TypeScript. Ensure all features work correctly.</code></pre>

<ul>
  <li>Review the plan and click "Yes, implement this plan".</li>
</ul>

<h3>6.2 Add Markdown Support</h3>

<ul>
  <li>Ask Codex to add Markdown editing and preview modes:</li>
</ul>

<pre><code class="language-text">Add Markdown support: an "Edit" mode for writing with syntax highlighting, and a "Preview" mode for rendering.</code></pre>

<h2 id="plugins-skills">7. Extend Capabilities with Plugins and Skills</h2>

<h3>7.1 Install Plugins</h3>

<ul>
  <li>Click "Plugins" in the sidebar to browse available plugins:</li>
  <ul>
    <li><strong>Chrome</strong>: Control the Chrome browser to scrape data or interact with web pages.</li>
    <li><strong>Computer Use</strong>: Control your computer's desktop apps (e.g., calendar, files).</li>
    <li><strong>Presentations</strong>: Generate PowerPoint presentations.</li>
  </ul>
</ul>

<h3>7.2 Use Skills</h3>

<ul>
  <li><strong>Image Generation</strong>: Use the "Image Gen" skill to generate images based on screenshots:</li>
</ul>

<pre><code class="language-text">Generate a promotional poster for this note app, using the provided screenshots.</code></pre>

<ul>
  <li><strong>Custom Skills</strong>: Create your own skills (e.g., a code review skill) to automate repetitive tasks.</li>
</ul>

<h3>7.3 Automations</h3>

<ul>
  <li>Set up automated tasks (e.g., daily code review):</li>
  <ul>
    <li>Click "Automations" → "Add Automation".</li>
    <li>Define the task: "Check the project code for issues daily at 9 AM".</li>
    <li>Select "Local" as the execution environment and save.</li>
  </ul>
</ul>

<h2 id="mobile">8. Mobile Control with Codex Mobile</h2>

<h3>8.1 Set Up Codex Mobile</h3>

<ul>
  <li>Click "Codex Mobile" in the sidebar.</li>
  <li>Allow mobile control and scan the QR code with your phone to connect.</li>
</ul>

<h3>8.2 Control Your Computer from Mobile</h3>

<ul>
  <li>Use the "Computer Use" plugin on your phone to control desktop apps:</li>
</ul>

<pre><code class="language-text">Delete the calendar event "Discuss Mark Note design" on May 28.</code></pre>

<h2 id="conclusion">Conclusion</h2>

<p>Codex is a powerful tool that can streamline your development workflow from start to finish. By following this guide, you can leverage its features to build projects efficiently, automate tasks, and extend its capabilities with plugins and skills. Experiment with different configurations and find the workflow that best suits your needs.</p>

<h2>常见问题</h2>

<h3>What's the difference between Codex and VS Code Copilot?</h3>
<p>Codex is OpenAI's standalone desktop app that goes beyond code assistance — it can control your entire desktop: open browsers, manage files, run terminal commands, generate presentations, and more. Copilot is GitHub's editor plugin focused on code completion and chat. Think of Codex as an "AI operator" vs. Copilot as a "code assistant." If you need help writing code, Copilot is enough. If you want AI to handle multi-app workflows (code → test → deploy → document), Codex is the better fit.</p>

<h3>Which Codex subscription should I choose?</h3>
<p>Plus ($20/month) is the sweet spot for individual developers — enough token limits for daily coding without breaking the bank. Free tier has very limited tokens and is mainly for trying the tool. Pro ($200/month) is for heavy users who treat Codex as their primary development environment. API Key login requires a foreign credit card and pay-per-use pricing, which is less cost-effective than subscriptions for regular use.</p>

<h3>Does agent.md have to be in the project root?</h3>
<p>Yes. Codex automatically reads <code>agent.md</code> (or <code>CLAUDE.md</code>) from the project root as system instructions. You can define coding conventions, Git habits, tech stack preferences, and project-specific rules there. Codex follows these rules in every conversation within that project. This is one of Codex's most powerful features — consistent behavior across sessions without repeating instructions.</p>

<h3>How do I choose between the two Fork options?</h3>
<p><strong>Fork into Local</strong>: The conversation rolls back but the code stays as-is. Use this when you went down the wrong path in discussion but want to keep the current code state. You'll need to manually <code>git reset</code> if you want to roll back code too. <strong>Fork into New Worktree</strong>: Creates a completely separate working directory. The original project is untouched. Use this when you want to explore an alternative approach without risking your current progress — it's like a "what if" branch for the entire project state.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Mastered Codex? Level up your AI development workflow:</p>
  <ul>
    <li><a href="/articles/vibe-coding-practical-guide-ai-dev-workflow-part1">Vibe Coding Practical Guide: AI Development Full Workflow (Part 1)</a> — dive into the vibe coding methodology</li>
    <li><a href="/articles/mastering-ai-workflow-beginner-custom-workbench">Mastering AI Workflow: Build Your Custom AI Workbench</a> — build a centralized AI productivity hub</li>
    <li><a href="/articles/codex-website-dev-zero-basis-tutorial">Codex Website Development: Zero-Basis Practical Tutorial</a> — build complete websites with Codex from scratch</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">🔧 AI 工具</span>
  <span class="meta-badge">🕒 阅读约12分钟</span>
  <span class="meta-badge">📅 2026年7月3日</span>
  <span class="meta-badge">🎯 入门</span>
</div>

<h2 id="introduction">引言</h2>

<p>Codex 是 OpenAI 的核心 AI 开发工具，能辅助编码、调试、测试，甚至控制电脑。本指南将带你走完 Codex 的完整使用流程——从安装到插件、技能、移动端控制等高级功能。</p>

<h2 id="installation">1. 安装与初始设置</h2>

<h3>1.1 下载安装 Codex</h3>

<ul>
  <li>访问 Codex 官网下载安装包。</li>
  <li>macOS 用户将 Codex 拖入 Applications 文件夹即可完成安装。</li>
</ul>

<h3>1.2 登录方式</h3>

<ul>
  <li><strong>ChatGPT 账号登录</strong>：可选 Free、Go、Plus、Pro 套餐。推荐 Plus（$20/月），token 额度适中。</li>
  <li><strong>API Key 登录</strong>：使用 OpenAI API 密钥（需境外信用卡，性价比不如订阅）。</li>
</ul>

<h3>1.3 初始配置</h3>

<ul>
  <li>按提示选择你的职位角色。</li>
  <li>暂时跳过"导入云端代码"步骤。</li>
  <li>Codex Mobile 可以稍后设置（详见第 8 节）。</li>
</ul>

<h2 id="basic-workflow">2. 基础项目开发流程</h2>

<h3>2.1 创建项目</h3>

<ul>
  <li>创建本地文件夹（如"Mark Note"）存放项目文件。</li>
  <li>在 Codex 中点击"Work on a Project" → "Use an Existing Folder"，选择你的项目文件夹。</li>
</ul>

<h3>2.2 第一个项目：构建 Markdown 笔记应用</h3>

<ul>
  <li>输入你的需求：</li>
</ul>

<pre><code class="language-text">用 HTML 构建一个笔记应用，左右两栏：左侧笔记列表，右侧笔记内容。包含基本的增删改查和本地存储功能。</code></pre>

<ul>
  <li>Codex 会生成代码并请求启动本地服务器的权限。选择"Yes"允许。</li>
</ul>

<h3>2.3 预览与迭代</h3>

<ul>
  <li>点击"Open in"在浏览器中预览应用。</li>
  <li>使用"Annotation"功能选中 UI 区域并请求修改：</li>
</ul>

<pre><code class="language-text">删除左侧栏顶部的两个示例笔记。</code></pre>

<h3>2.4 调试</h3>

<ul>
  <li>如果"添加笔记"按钮不工作，Codex 会诊断问题（通常是预览环境限制导致）。</li>
  <li>在独立浏览器中测试应用以确认功能正常。</li>
</ul>

<h2 id="advanced-config">3. 高级配置与安全</h2>

<h3>3.1 权限模式</h3>

<ul>
  <li><strong>默认权限</strong>：执行高风险操作前 Codex 会请求确认。</li>
  <li><strong>自动审查</strong>：安全代理自动批准安全操作、阻止危险操作（推荐，兼顾安全与效率）。</li>
  <li><strong>完全访问</strong>：无提示，但需谨慎使用（有数据丢失风险）。</li>
</ul>

<h3>3.2 模型设置</h3>

<ul>
  <li><strong>模型选择</strong>：根据任务复杂度选择 GPT-5.5、GPT-5.4 等。</li>
  <li><strong>思考深度</strong>：从 Low 到 Extra High 可调（深度越高，代码质量越好但速度越慢）。</li>
  <li><strong>速度模式</strong>：启用"Fast"模式可提速 1.5 倍（消耗更多 token）。</li>
</ul>

<h2 id="git">4. Git 版本控制</h2>

<h3>4.1 初始化 Git 仓库</h3>

<ul>
  <li>按 <code>Command+J</code> 在 Codex 中打开终端。</li>
  <li>运行以下命令：</li>
</ul>

<pre><code class="language-bash">git init
git add .
git commit -m "first commit"</code></pre>

<h3>4.2 提交更改</h3>

<ul>
  <li>使用 Codex 内置的 Git 界面：</li>
  <ul>
    <li>点击"Changes"图标 → "Unstaged"查看修改文件。</li>
    <li>点击"Commit"，输入提交信息（如"Change theme to blue"），点击"Continue"。</li>
  </ul>
</ul>

<h3>4.3 用 Fork 回滚</h3>

<ul>
  <li>使用"Fork"功能回滚对话和代码：</li>
  <ul>
    <li><strong>Fork into Local</strong>：创建新对话但保留当前代码（需手动 git reset 回滚代码）。</li>
    <li><strong>Fork into New Worktree</strong>：创建新对话和独立项目文件夹（不回滚代码，但隔离更改）。</li>
  </ul>
</ul>

<h2 id="agent-md">5. 跨项目配置：agent.md</h2>

<h3>5.1 创建 agent.md</h3>

<ul>
  <li>在项目文件夹中创建名为 <code>agent.md</code> 的文件。</li>
  <li>添加规则，例如：</li>
</ul>

<pre><code class="language-markdown">- 每次代码变更后用描述性信息执行 git commit。
- 所有新组件使用 React + TypeScript。
- 遵循项目的蓝色主题配色方案。</code></pre>

<h3>5.2 测试配置</h3>

<ul>
  <li>创建新对话，让 Codex 添加功能（如"添加深色/浅色模式切换"）。</li>
  <li>检查 Git 日志确认 Codex 自动提交了更改。</li>
</ul>

<h2 id="refactoring">6. 项目重构与高级功能</h2>

<h3>6.1 重构为 Electron 桌面应用</h3>

<ul>
  <li>使用"Plan Mode"让 Codex 创建重构方案：</li>
</ul>

<pre><code class="language-text">将此 Web 应用重构为 Electron 桌面应用，使用 React + TypeScript。确保所有功能正常工作。</code></pre>

<ul>
  <li>审查方案后点击"Yes, implement this plan"。</li>
</ul>

<h3>6.2 添加 Markdown 支持</h3>

<ul>
  <li>让 Codex 添加 Markdown 编辑和预览模式：</li>
</ul>

<pre><code class="language-text">添加 Markdown 支持："编辑"模式支持语法高亮编写，"预览"模式用于渲染。</code></pre>

<h2 id="plugins-skills">7. 插件与技能扩展</h2>

<h3>7.1 安装插件</h3>

<ul>
  <li>点击侧边栏"Plugins"浏览可用插件：</li>
  <ul>
    <li><strong>Chrome</strong>：控制 Chrome 浏览器抓取数据或与网页交互。</li>
    <li><strong>Computer Use</strong>：控制电脑桌面应用（如日历、文件）。</li>
    <li><strong>Presentations</strong>：生成 PowerPoint 演示文稿。</li>
  </ul>
</ul>

<h3>7.2 使用技能（Skills）</h3>

<ul>
  <li><strong>图片生成</strong>：使用"Image Gen"技能基于截图生成图片：</li>
</ul>

<pre><code class="language-text">用提供的截图为这个笔记应用生成宣传海报。</code></pre>

<ul>
  <li><strong>自定义技能</strong>：创建自己的技能（如代码审查技能）来自动化重复任务。</li>
</ul>

<h3>7.3 自动化任务</h3>

<ul>
  <li>设置自动化任务（如每日代码审查）：</li>
  <ul>
    <li>点击"Automations" → "Add Automation"。</li>
    <li>定义任务："每天早上 9 点检查项目代码问题"。</li>
    <li>选择"Local"作为执行环境并保存。</li>
  </ul>
</ul>

<h2 id="mobile">8. 移动端控制：Codex Mobile</h2>

<h3>8.1 设置 Codex Mobile</h3>

<ul>
  <li>点击侧边栏"Codex Mobile"。</li>
  <li>允许移动端控制，用手机扫描二维码连接。</li>
</ul>

<h3>8.2 从手机控制电脑</h3>

<ul>
  <li>在手机上使用"Computer Use"插件控制桌面应用：</li>
</ul>

<pre><code class="language-text">删除 5 月 28 日"讨论 Mark Note 设计"的日历事件。</code></pre>

<h2 id="conclusion">总结</h2>

<p>Codex 是一款强大的工具，能从头到尾优化你的开发工作流。通过本指南，你可以高效地构建项目、自动化任务、通过插件和技能扩展能力。尝试不同配置，找到最适合你的工作流。</p>

<h2>常见问题</h2>

<h3>Codex 和 VS Code Copilot 有什么区别？</h3>
<p>Codex 是 OpenAI 的独立桌面应用，不仅能辅助编码，还能控制整个桌面环境——打开浏览器、操作文件管理器、运行终端命令、生成 PPT 等。Copilot 是 GitHub 的编辑器插件，专注代码补全和聊天。Codex 的定位更接近"AI 操作员"而非单纯的"代码助手"。如果只需要写代码辅助，Copilot 足够；如果希望 AI 处理跨应用工作流（编码→测试→部署→文档），Codex 更合适。</p>

<h3>Codex 的订阅方案怎么选？</h3>
<p>Plus（$20/月）是个人开发者的最佳选择——token 额度足够日常编码，价格合理。Free 版 token 极少，主要供试用。Pro 版（$200/月）适合将 Codex 作为主力开发环境的重度用户。API Key 方式需境外信用卡且按量付费，经常使用的话性价比不如订阅。</p>

<h3>agent.md 文件必须放在项目根目录吗？</h3>
<p>是的，Codex 会自动读取项目根目录下的 <code>agent.md</code>（或 <code>CLAUDE.md</code>）作为系统指令。你可以在里面定义代码规范、Git 提交习惯、技术栈偏好和项目特定规则。Codex 在该项目的每次对话中都会遵守这些规则——这是 Codex 最强大的功能之一：跨会话保持一致行为，无需重复说明。</p>

<h3>Fork 功能的两个选项怎么选？</h3>
<p><strong>Fork into Local</strong>：对话回滚但代码保持不变。适合"讨论方向跑偏了但代码没问题"的情况。如需同时回滚代码，需手动 <code>git reset</code>。<strong>Fork into New Worktree</strong>：创建完全独立的工作目录，原项目不受任何影响。适合"想试试另一个方向但不影响当前进度"——相当于给整个项目状态开一个"假设"分支。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>掌握了 Codex？升级你的 AI 开发工作流：</p>
  <ul>
    <li><a href="/articles/vibe-coding-practical-guide-ai-dev-workflow-part1">Vibe Coding 实战指南：AI 开发完整工作流（上篇）</a> — 深入了解 Vibe Coding 方法论</li>
    <li><a href="/articles/mastering-ai-workflow-beginner-custom-workbench">掌握 AI 工作流：打造你的专属 AI 工作台</a> — 构建集中式 AI 生产力中心</li>
    <li><a href="/articles/codex-website-dev-zero-basis-tutorial">Codex 网站开发：零基础实战教程与部署指南</a> — 用 Codex 从零构建完整网站</li>
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
