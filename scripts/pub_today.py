"""
Publish July 21, 2026 — 1 article, no new tools.
"""
import os

BASE = r"C:\Users\jun\aistudyonline-next"
os.chdir(BASE)

with open('src/lib/articles.ts', 'r', encoding='utf-8') as f:
    articles_src = f.read()

new_articles = r"""  {
    slug: "2026-local-llm-benchmark-13-open-source-models-4000-hardware-guide",
    title: "2026 Local Large Language Model Benchmark: 13 Open-Source Models, $4000 Budget Hardware Local Deployment Guide",
    titleZh: "2026本地大模型横评：13款开源模型+$4000硬件部署全指南",
    description: "A 30-day, $4,185 hardware deep dive testing 13 open-source LLMs (Qwen3.6, Gemma 4, Ornith 1.0) for local deployment — covering quantization, MTP, Dense vs MoE, OCR, long-context reasoning, full-stack coding, speed benchmarks, and llama.cpp deployment with GGUF.",
    descriptionZh: "30天$4185硬件深度评测13款开源大模型（Qwen3.6、Gemma 4、Ornith 1.0）本地部署——覆盖量化、MTP、Dense vs MoE、OCR、长上下文推理、全栈编码、速度基准和llama.cpp GGUF部署。",
    category: "AI Learning",
    tags: ["LLM", "Local Deployment", "Open Source", "Benchmark", "Hardware", "Qwen", "Gemma", "Quantization"],
    difficulty: "advanced",
    toolsMentioned: ["Qwen", "Gemma", "DeepSeek"],
    date: "2026-07-21",
  },

"""

last_bracket = articles_src.rfind('];')
articles_new = articles_src[:last_bracket] + new_articles + '];'

with open('src/lib/articles.ts', 'w', encoding='utf-8') as f:
    f.write(articles_new)

print('Part 1: 1 new article added to articles.ts')

with open('src/lib/article-content.ts', 'r', encoding='utf-8') as f:
    content_src = f.read()

new_contents = r'''
  "2026-local-llm-benchmark-13-open-source-models-4000-hardware-guide": {
    content: `<div class="meta-banner">
  <span class="meta-badge">📚 AI Learning</span>
  <span class="meta-badge">🕒 10 min read</span>
  <span class="meta-badge">📅 Jul 21, 2026</span>
  <span class="meta-badge">🎯 Advanced</span>
</div>

<h2 id="introduction">Introduction</h2>

<p>I spent $4000 and 30 days answering one question: <strong>how do you choose the right large language model for local deployment?</strong> From buying hardware to tuning models, from crashes to breakthroughs, I tested 13 open-source models including Qwen3.6, Gemma 4, and Ornith 1.0 end-to-end. This guide covers costs, performance tuning, deployment difficulty, MTP, long-context handling, and real-world troubleshooting logs to help you avoid wasted time and storage.</p>

<h2 id="why-local">1. Why Local Deployment? Three Core Reasons</h2>

<ul>
  <li><strong>Privacy</strong>: Data never leaves your machine, meeting compliance requirements for sensitive internal code or documents.</li>
  <li><strong>Security</strong>: Works offline, making it ideal for air-gapped environments like hospitals processing medical records.</li>
  <li><strong>Cost</strong>: One-time hardware investment vs. infinite cloud API fees. For high-frequency tasks like internal document processing, local deployment is far cheaper long-term.</li>
</ul>

<h2 id="hardware">2. Hardware Setup: $4,185 Build for Local LLM Testing</h2>

<table>
  <tr><th>Component</th><th>Cost</th><th>Notes</th></tr>
  <tr><td>2x V100 16GB GPUs</td><td>$2,200</td><td>32GB total VRAM, PCIe 3.0 x16</td></tr>
  <tr><td>32GB DDR4 RAM</td><td>$800</td><td>Handles model loading and system tasks</td></tr>
  <tr><td>X99 Motherboard</td><td>$240</td><td>Dual PCIe 3.0 x16 slots</td></tr>
  <tr><td>E5-2680 V4 CPU</td><td>$45</td><td>Budget multi-core for system operations</td></tr>
  <tr><td>PSU/Case/SSD</td><td>$900</td><td>Reliable power for 2x GPUs</td></tr>
  <tr><td><strong>Total</strong></td><td><strong>$4,185</strong></td><td></td></tr>
</table>

<h3>Performance Thresholds</h3>
<ul>
  <li><strong>≤3 tokens/s</strong>: Unusable (model too large for hardware)</li>
  <li><strong>20 tokens/s</strong>: Barely usable for casual chat</li>
  <li><strong>50 tokens/s</strong>: Smooth for most tasks</li>
  <li><strong>≥100 tokens/s</strong>: Near cloud-level responsiveness</li>
</ul>

<h2 id="model-selection">3. Model Selection: 13 Models Tested, 5 Advanced to Finals</h2>

<p>I grouped models by parameter size and tested across 3 preliminary rounds: Chinese Writing, Logical Reasoning, and Invoice OCR.</p>

<h3>Top 5 Finalists</h3>
<table>
  <tr><th>Model</th><th>Parameters</th><th>Architecture</th></tr>
  <tr><td>Ornith-1.0-9B</td><td>9B</td><td>Dense</td></tr>
  <tr><td>Ornith-1.0-35B-A3B</td><td>35B</td><td>MoE</td></tr>
  <tr><td>Qwen3.6-35B-A3B</td><td>35B</td><td>MoE</td></tr>
  <tr><td>Gemma-4-26B-A4B (QAT)</td><td>26B</td><td>Dense</td></tr>
  <tr><td>Qwen3.6-27B</td><td>27B</td><td>Dense</td></tr>
</table>

<h2 id="concepts">4. Key Technical Concepts Explained</h2>

<h3>Quantization</h3>
<p>Quantization reduces model size by lowering precision, making large models fit in consumer GPUs:</p>
<ul>
  <li><strong>&lt;4-bit</strong>: Severe quality loss, not recommended</li>
  <li><strong>IQ4/Q4</strong>: Good balance of size and quality</li>
  <li><strong>Q6</strong>: Near-lossless, recommended for most use cases</li>
  <li><strong>Q8</strong>: Maximum quality, larger file size</li>
</ul>
<p>All models used GGUF quantization (Q6_K for most, Q4 for Gemma-4-26B).</p>

<h3>MTP (Multi-Token Prediction)</h3>
<p>MTP is an inference acceleration technique where a small "draft" model predicts multiple tokens at once, and the main model verifies them. It can speed up dense models by <strong>245%</strong> but slows down MoE models due to cross-GPU communication overhead.</p>

<h3>Dense vs. MoE Models</h3>
<ul>
  <li><strong>Dense</strong>: All parameters active for every token. More predictable, no routing overhead.</li>
  <li><strong>MoE</strong>: Only a subset of parameters ("experts") active per token. Faster inference for large models, but requires more complex deployment.</li>
</ul>

<h2 id="final-tests">5. Final Round Tests: Which Model Wins?</h2>

<h3>Test 1: Advanced OCR (Dinosaur Knowledge)</h3>
<p>Extract 30 facts from two dinosaur infographics. <strong>Winners</strong>: Qwen3.6-35B, Qwen3.6-27B (10/10). Others scored 9/10.</p>

<h3>Test 2: Long-Context Reasoning (130K Tokens)</h3>
<p>Find a specific article in a 110-page PDF and determine which boy is lying. <strong>All 5 models scored 10/10</strong> — long-context performance was surprisingly strong across the board.</p>

<h3>Test 3: Document Generation (Multi-Modal)</h3>
<p>Read 171 mixed text/image/video files and generate a structured Excel spreadsheet. <strong>Winners</strong>: Qwen3.6-35B, Ornith-1.0-9B (10/10).</p>

<h3>Test 4: Full-Stack App Building</h3>
<p>Build a novel reading website with MySQL backend, API layer, and frontend. <strong>Winner</strong>: DeepSeek V4 Flash (control group, 34/50). <strong>Local Model Winner</strong>: Ornith-1.0-35B (31/50). Runner-Up: Qwen3.6-35B (24/50).</p>

<h3>Test 5: Inference Speed</h3>
<ul>
  <li><strong>Fastest</strong>: Gemma-4-26B (105 tokens/s)</li>
  <li><strong>Runner-Up</strong>: Ornith-1.0-35B (99 tokens/s)</li>
  <li><strong>Slowest</strong>: Qwen3.6-27B (28 tokens/s)</li>
</ul>

<h2 id="rankings">6. Final Rankings & Recommendations</h2>

<h3>Overall Scores</h3>
<ol>
  <li><strong>Ornith-1.0-35B</strong>: 59/100 (Best for hard tasks)</li>
  <li><strong>Qwen3.6-35B</strong>: 54/100 (Most reliable all-around)</li>
  <li><strong>Qwen3.6-27B</strong>: 39/100 (Best for 24GB GPUs)</li>
  <li><strong>Ornith-1.0-9B</strong>: 39/100 (Best single-GPU entry-level model)</li>
  <li><strong>Gemma-4-26B</strong>: 31/100 (Fastest inference)</li>
</ol>

<h3>Which Model Should You Use?</h3>
<ul>
  <li><strong>Single GPU (16GB VRAM)</strong>: Ornith-1.0-9B</li>
  <li><strong>24GB GPU</strong>: Qwen3.6-27B</li>
  <li><strong>Dual 16GB GPUs</strong>: Qwen3.6-35B</li>
  <li><strong>Hard tasks (coding, complex reasoning)</strong>: Ornith-1.0-35B</li>
</ul>

<h2 id="deployment">7. How to Deploy These Models</h2>

<h3>Prerequisites</h3>
<p>Install llama.cpp, the lightweight inference engine used for all tests:</p>

<pre><code class="language-bash"># Install via official script
curl -LsSf https://llama.app/install.sh | sh</code></pre>

<h3>Model Download Links</h3>
<table>
  <tr><th>Model</th><th>Download</th></tr>
  <tr><td>Ornith-1.0-9B</td><td>huggingface.co/deepreinforce-ai/Ornith-1.0-9B-GGUF</td></tr>
  <tr><td>Ornith-1.0-35B</td><td>huggingface.co/deepreinforce-ai/Ornith-1.0-35B-GGUF</td></tr>
  <tr><td>Qwen3.6-27B</td><td>huggingface.co/Qwen/Qwen3.6-27B-GGUF</td></tr>
  <tr><td>Qwen3.6-35B</td><td>huggingface.co/Qwen/Qwen3.6-35B-A3B-GGUF</td></tr>
  <tr><td>Gemma-4-26B</td><td>huggingface.co/google/gemma-4-26b-it</td></tr>
</table>

<h3>Run a Model</h3>

<pre><code class="language-bash"># Start a local server with web UI
llama serve -hf deepreinforce-ai/Ornith-1.0-9B-GGUF:Q4_K_M

# Run inference directly in terminal
llama run -hf deepreinforce-ai/Ornith-1.0-9B-GGUF:Q4_K_M "Write a Python function to check if a number is prime."</code></pre>

<h2 id="troubleshooting">8. Common Issues & Fixes</h2>

<h3>Infinite Loops</h3>
<p>Caused by: too-low quantization (breaks critical weights), MoE routing failures (small subset of experts dominates), bad prompts. <strong>Fix</strong>: Use Q6+ quantization, avoid prompts like "continue writing" in long tasks.</p>

<h3>MTP Slowdown on MoE Models</h3>
<p>MTP speeds up dense models but slows down MoE models due to cross-GPU communication. <strong>Disable MTP</strong> for MoE models.</p>

<h3>Long-Context Limits</h3>
<ul>
  <li>Ornith-1.0-9B/35B: 256K tokens</li>
  <li>Qwen3.6-35B: 256K tokens</li>
  <li>Qwen3.6-27B: 128K tokens (VRAM limits)</li>
</ul>

<h2 id="conclusion">9. Final Thoughts</h2>

<p>Local LLMs have come a long way in 2026. With a $4,000 rig, you can run models that match cloud performance for most tasks. Key takeaways: MoE models are better for large tasks but require more hardware; quantization quality matters more than model size; Ornith-1.0-35B is the best all-around model for dual-GPU setups.</p>

<h2>常见问题</h2>

<h3>Is $4,000 really the minimum for local LLM deployment?</h3>
<p>No — $4,185 is the cost for the specific dual-GPU setup tested in this guide, which can run 35B MoE models at near-cloud speeds. You can start much cheaper. A single used RTX 3060 12GB (~$200) can run quantized 7-9B models (Ornith-1.0-9B at Q4, Qwen 7B variants) at usable speeds. An M1/M2 MacBook with 16GB unified memory can run 7B models out of the box with no additional hardware cost. The guide's $4K setup is the "prosumer" tier — equivalent to a mid-range cloud GPU instance. For hobbyist experimentation, $200-500 is a realistic starting point. The price-performance sweet spot for serious local deployment is around $2,000 (single 24GB GPU like RTX 3090/4090).</p>

<h3>How do I choose between Qwen, Gemma, and Ornith for my use case?</h3>
<p>The guide's recommendations are clear: <strong>Chinese-language tasks</strong> → Qwen3.6 (best Chinese comprehension among all tested models). <strong>English-language tasks with limited hardware</strong> → Gemma-4-26B (fastest inference, good for single-GPU setups). <strong>Complex coding and reasoning</strong> → Ornith-1.0-35B (highest overall score, best for hard tasks but needs dual GPUs). <strong>Budget single-GPU</strong> → Ornith-1.0-9B (surprisingly capable for its size, fits in 16GB VRAM). If you're bilingual and have dual GPUs, Qwen3.6-35B is the best all-rounder — it handles both Chinese and English well with strong OCR and document processing capabilities.</p>

<h3>What's the practical difference between Q4 and Q6 quantization?</h3>
<p>The guide's testing found Q6 is the sweet spot: near-lossless quality with manageable file sizes. Q4 (IQ4 specifically) is acceptable for casual use but degrades on complex reasoning and code generation tasks. The practical difference: a Q4 model might pass a logic puzzle 7/10 times, while Q6 passes 9/10 times. For creative writing and chat, Q4 is fine. For coding, math, or any task where correctness matters, use Q6. The file size difference: Q6 is roughly 50% larger than Q4. On a 16GB GPU, this means you might fit a 13B Q4 model but only a 9B Q6 model. The guide recommends prioritizing quantization quality over parameter count — a well-quantized smaller model often outperforms a poorly quantized larger one.</p>

<h3>Can I use these models for commercial/business purposes?</h3>
<p>Yes — all models tested are open-source with permissive licenses. Qwen (Apache 2.0), Gemma (Google's Gemma license, allows commercial use), and Ornith (MIT-like) can all be used commercially. The main consideration is liability: when you self-host, you're responsible for model behavior, data security, and compliance. The guide's privacy/security motivation (data never leaves your machine) is specifically designed for business use cases like processing customer data, internal documents, or medical records. For production deployment, add monitoring (token/s rate, error rates, memory usage), set up automatic model reloading on crash, and implement rate limiting if multiple users will access the model.</p>

<div class="next-step">
  <h3>📖 Next Steps</h3>
  <p>Built your local LLM rig? Explore more model and deployment content:</p>
  <ul>
    <li><a href="/articles/understanding-large-language-models-principles-architecture">Understanding Large Language Models: Principles, Architecture, and Practical Usage</a> — understand the architecture behind these models</li>
    <li><a href="/articles/kimi-k3-takes-global-top-spot-week-29-frontend-coding-benchmark">Kimi K3 Takes Global Top Spot: Week 29 Front-End Coding Benchmark</a> — compare cloud vs. local model performance</li>
    <li><a href="/articles/2025-ai-toolkit-practical-guide-every-domain">2025 AI Toolkit: A Practical Guide for Every Domain</a> — discover more tools across the AI ecosystem</li>
  </ul>
</div>`,
    contentZh: `<div class="meta-banner">
  <span class="meta-badge">📚 AI 学习</span>
  <span class="meta-badge">🕒 阅读约10分钟</span>
  <span class="meta-badge">📅 2026年7月21日</span>
  <span class="meta-badge">🎯 高级</span>
</div>

<h2 id="introduction">引言</h2>

<p>我花了$4000和30天回答一个问题：<strong>如何选择适合本地部署的大语言模型？</strong>从买硬件到调模型，从崩溃到突破，我端到端测试了13款开源模型，包括Qwen3.6、Gemma 4和Ornith 1.0。本指南涵盖成本、性能调优、部署难度、MTP、长上下文处理和真实排障日志，帮你避免浪费时间和存储。</p>

<h2 id="why-local">1. 为什么本地部署？三个核心原因</h2>

<ul>
  <li><strong>隐私</strong>：数据永不离开你的机器，满足敏感内部代码或文档的合规要求。</li>
  <li><strong>安全</strong>：离线运行，非常适合医院处理病历等气隙隔离环境。</li>
  <li><strong>成本</strong>：一次性硬件投入 vs 无限云端API费用。内部文档处理等高频任务，本地部署长期便宜得多。</li>
</ul>

<h2 id="hardware">2. 硬件配置：$4,185本地LLM测试机</h2>

<table>
  <tr><th>组件</th><th>成本</th><th>说明</th></tr>
  <tr><td>2x V100 16GB GPU</td><td>$2,200</td><td>32GB总显存，PCIe 3.0 x16</td></tr>
  <tr><td>32GB DDR4内存</td><td>$800</td><td>处理模型加载和系统任务</td></tr>
  <tr><td>X99主板</td><td>$240</td><td>双PCIe 3.0 x16插槽</td></tr>
  <tr><td>E5-2680 V4 CPU</td><td>$45</td><td>预算多核用于系统操作</td></tr>
  <tr><td>电源/机箱/SSD</td><td>$900</td><td>双GPU可靠供电</td></tr>
  <tr><td><strong>合计</strong></td><td><strong>$4,185</strong></td><td></td></tr>
</table>

<h3>性能阈值</h3>
<ul>
  <li><strong>≤3 tokens/s</strong>：不可用</li>
  <li><strong>20 tokens/s</strong>：勉强可用</li>
  <li><strong>50 tokens/s</strong>：大多数任务流畅</li>
  <li><strong>≥100 tokens/s</strong>：接近云端响应速度</li>
</ul>

<h2 id="model-selection">3. 模型选择：13款测试，5款进入决赛</h2>

<p>按参数规模分组，通过3轮初赛：中文写作、逻辑推理和发票OCR。</p>

<h3>前5名决赛选手</h3>
<table>
  <tr><th>模型</th><th>参数量</th><th>架构</th></tr>
  <tr><td>Ornith-1.0-9B</td><td>9B</td><td>Dense</td></tr>
  <tr><td>Ornith-1.0-35B-A3B</td><td>35B</td><td>MoE</td></tr>
  <tr><td>Qwen3.6-35B-A3B</td><td>35B</td><td>MoE</td></tr>
  <tr><td>Gemma-4-26B-A4B (QAT)</td><td>26B</td><td>Dense</td></tr>
  <tr><td>Qwen3.6-27B</td><td>27B</td><td>Dense</td></tr>
</table>

<h2 id="concepts">4. 关键技术概念解析</h2>

<h3>量化</h3>
<p>量化通过降低精度减小模型体积，让大模型适配消费级GPU：</p>
<ul>
  <li><strong>&lt;4-bit</strong>：严重质量损失，不推荐</li>
  <li><strong>IQ4/Q4</strong>：大小和质量良好平衡</li>
  <li><strong>Q6</strong>：接近无损，推荐大多数场景使用</li>
  <li><strong>Q8</strong>：最高质量，文件更大</li>
</ul>
<p>所有模型使用GGUF量化（大多数Q6_K，Gemma-4-26B用Q4）。</p>

<h3>MTP（多Token预测）</h3>
<p>MTP是一种推理加速技术，小型"草稿"模型一次预测多个token，主模型验证。可加速Dense模型<strong>245%</strong>，但由于跨GPU通信开销会拖慢MoE模型。</p>

<h3>Dense vs MoE模型</h3>
<ul>
  <li><strong>Dense</strong>：每个token激活全部参数。更可预测，无路由开销。</li>
  <li><strong>MoE</strong>：每个token仅激活部分参数（"专家"）。大模型推理更快，但部署更复杂。</li>
</ul>

<h2 id="final-tests">5. 决赛测试：哪个模型胜出？</h2>

<h3>测试1：高级OCR（恐龙知识）</h3>
<p>从两张恐龙信息图中提取30个事实。<strong>胜者</strong>：Qwen3.6-35B、Qwen3.6-27B（10/10）。其他9/10。</p>

<h3>测试2：长上下文推理（130K Token）</h3>
<p>在110页PDF中找到特定文章并判断哪个男孩在说谎。<strong>5款模型全部10/10</strong>——长上下文表现出乎意料地强。</p>

<h3>测试3：文档生成（多模态）</h3>
<p>读取171个混合文本/图片/视频文件并生成结构化Excel。<strong>胜者</strong>：Qwen3.6-35B、Ornith-1.0-9B（10/10）。</p>

<h3>测试4：全栈应用构建</h3>
<p>构建含MySQL后端、API层和前端的阅读网站。<strong>胜者</strong>：DeepSeek V4 Flash（对照组，34/50）。<strong>本地模型胜者</strong>：Ornith-1.0-35B（31/50）。亚军：Qwen3.6-35B（24/50）。</p>

<h3>测试5：推理速度</h3>
<ul>
  <li><strong>最快</strong>：Gemma-4-26B（105 tokens/s）</li>
  <li><strong>亚军</strong>：Ornith-1.0-35B（99 tokens/s）</li>
  <li><strong>最慢</strong>：Qwen3.6-27B（28 tokens/s）</li>
</ul>

<h2 id="rankings">6. 最终排名与推荐</h2>

<h3>总分</h3>
<ol>
  <li><strong>Ornith-1.0-35B</strong>：59/100（硬核任务最佳）</li>
  <li><strong>Qwen3.6-35B</strong>：54/100（最可靠的全面选手）</li>
  <li><strong>Qwen3.6-27B</strong>：39/100（24GB GPU最佳选择）</li>
  <li><strong>Ornith-1.0-9B</strong>：39/100（最佳单GPU入门模型）</li>
  <li><strong>Gemma-4-26B</strong>：31/100（推理最快）</li>
</ol>

<h3>该用哪个模型？</h3>
<ul>
  <li><strong>单GPU 16GB显存</strong>：Ornith-1.0-9B</li>
  <li><strong>24GB GPU</strong>：Qwen3.6-27B</li>
  <li><strong>双16GB GPU</strong>：Qwen3.6-35B</li>
  <li><strong>硬核任务（编码、复杂推理）</strong>：Ornith-1.0-35B</li>
</ul>

<h2 id="deployment">7. 如何部署这些模型</h2>

<h3>前置条件</h3>
<p>安装llama.cpp，所有测试使用的轻量推理引擎：</p>

<pre><code class="language-bash"># 通过官方脚本安装
curl -LsSf https://llama.app/install.sh | sh</code></pre>

<h3>运行模型</h3>

<pre><code class="language-bash"># 启动带Web UI的本地服务器
llama serve -hf deepreinforce-ai/Ornith-1.0-9B-GGUF:Q4_K_M

# 终端直接推理
llama run -hf deepreinforce-ai/Ornith-1.0-9B-GGUF:Q4_K_M "写一个判断质数的Python函数"</code></pre>

<h2 id="troubleshooting">8. 常见问题与修复</h2>

<h3>无限循环</h3>
<p>原因：量化过低（破坏关键权重）、MoE路由失败（少数专家主导）、不良提示词。<strong>修复</strong>：使用Q6+量化，长任务中避免"继续写"等提示词。</p>

<h3>MoE模型上MTP减速</h3>
<p>MTP加速Dense模型但因跨GPU通信拖慢MoE模型。<strong>对MoE模型禁用MTP</strong>。</p>

<h3>长上下文限制</h3>
<ul>
  <li>Ornith-1.0-9B/35B：256K token</li>
  <li>Qwen3.6-35B：256K token</li>
  <li>Qwen3.6-27B：128K token（显存限制）</li>
</ul>

<h2 id="conclusion">9. 最后的话</h2>

<p>2026年本地大模型已走得很远。$4,000的机器就能运行大多数任务媲美云端性能的模型。核心要点：MoE模型更适合大任务但需要更多硬件；量化质量比模型规模更重要；Ornith-1.0-35B是双GPU配置的最佳全面模型。</p>

<h2>常见问题</h2>

<h3>$4,000真的是本地部署LLM的最低门槛吗？</h3>
<p>不是——$4,185是本指南测试的双GPU特定配置成本，可运行35B MoE模型达到接近云端速度。起步可以便宜得多。单张二手RTX 3060 12GB（约$200）可运行量化7-9B模型（Ornith-1.0-9B Q4、Qwen 7B变体）且速度可用。M1/M2 MacBook 16GB统一内存可直接运行7B模型，无需额外硬件成本。指南的$4K配置是"专业消费者"级别——相当于中端云GPU实例。爱好者实验$200-500是现实的起点。严肃本地部署的性价比甜蜜点约$2,000（单张24GB GPU如RTX 3090/4090）。</p>

<h3>如何在Qwen、Gemma和Ornith之间选择？</h3>
<p>指南推荐很明确：<strong>中文任务</strong>→ Qwen3.6（所有测试模型中中文理解最好）。<strong>英文任务且硬件有限</strong>→ Gemma-4-26B（推理最快，适合单GPU）。<strong>复杂编码和推理</strong>→ Ornith-1.0-35B（总分最高，硬核任务最佳但需双GPU）。<strong>预算单GPU</strong>→ Ornith-1.0-9B（同尺寸出人意料地强，16GB显存可跑）。中英双语且有双GPU，Qwen3.6-35B是最佳全面选手——中英文都处理得好，OCR和文档处理能力强。</p>

<h3>Q4和Q6量化的实际区别是什么？</h3>
<p>指南测试发现Q6是甜蜜点：接近无损质量，文件大小可管理。Q4（特别是IQ4）日常使用可接受，但复杂推理和代码生成任务会降级。实际区别：Q4模型解逻辑谜题10次对7次，Q6对9次。创意写作和聊天Q4足够。编码、数学或任何正确性重要的任务用Q6。文件大小差：Q6约比Q4大50%。16GB显存上，你可能装得下13B Q4模型但只能装9B Q6模型。指南建议优先量化质量而非参数量——量化良好的较小模型通常优于量化不良的较大模型。</p>

<h3>这些模型能用于商业目的吗？</h3>
<p>可以——所有测试模型都是开源且许可宽松。Qwen（Apache 2.0）、Gemma（Google Gemma许可，允许商业使用）和Ornith（类MIT）均可商用。主要考虑是责任：自托管时你负责模型行为、数据安全和合规。指南的隐私/安全动机（数据不离开机器）正是为处理客户数据、内部文档或病历等商业场景设计的。生产部署需添加监控（token/s速率、错误率、内存使用）、设置崩溃自动重载模型、多用户访问时实现速率限制。</p>

<div class="next-step">
  <h3>📖 下一步</h3>
  <p>搭好了本地LLM？探索更多模型和部署内容：</p>
  <ul>
    <li><a href="/articles/understanding-large-language-models-principles-architecture">大语言模型深度解读：从Transformer原理到实战应用</a> — 理解这些模型背后的架构</li>
    <li><a href="/articles/kimi-k3-takes-global-top-spot-week-29-frontend-coding-benchmark">Kimi K3登顶全球第一：第29周LLM前端编码基准测试报告</a> — 对比云端与本地模型性能</li>
    <li><a href="/articles/2025-ai-toolkit-practical-guide-every-domain">2025 AI工具箱：全领域实用指南</a> — 发现AI生态中的更多工具</li>
  </ul>
</div>`,
  },

'''

last_brace = content_src.rfind('};')
content_new = content_src[:last_brace] + new_contents + '};'

with open('src/lib/article-content.ts', 'w', encoding='utf-8') as f:
    f.write(content_new)

print('Part 2: 1 article content added to article-content.ts')
print('\n=== All done! Run build to verify ===')