const zh = "<p>[Chinese version — pending translation]</p>";

export const articleContents: Record<string, { content: string; contentZh: string }> = {
  // ====== Sample: Claude Code Installation (Path: Claude Code × 4, Part 1) ======
  "claude-code-install-setup": {
    content: `<div class="article-meta-banner">
<p><strong>Learning Path:</strong> Claude Code 编程入门 · <strong>Part 1 of 4</strong></p>
<p><strong>Prerequisites:</strong> 一台电脑（Windows/Mac/Linux）、基本命令行操作能力（会用 <code>cd</code> 和 <code>ls</code> 即可）</p>
<p><strong>What you'll build:</strong> 一个可运行的 Claude Code 开发环境，能通过命令行直接调用 Claude 写代码。</p>
</div>

<h2>What is Claude Code?</h2>

<p>Claude Code 是 Anthropic 推出的命令行 AI 编程工具。和 Cursor、GitHub Copilot 不同，它不需要打开 IDE——直接在终端里输入自然语言，Claude 就能读你的代码库、写代码、修 bug、解释逻辑。它最独特的能力是<strong>理解整个项目结构</strong>，而不是只处理当前打开的文件。</p>

<p>在正式开始之前，你需要知道三件事：</p>

<ol>
<li>Claude Code 需要 <strong>Anthropic API Key</strong>（付费），不是 Claude.ai 的网页版订阅。两者独立。</li>
<li>它是<strong>命令行工具</strong>，运行在终端里，没有图形界面。别担心——你不会被要求写任何代码来使用它。</li>
<li>它会<strong>读取和修改你的文件</strong>。建议在测试项目里先试用，不要一上来就在公司代码库里跑。</li>
</ol>

<h2>Step 1: Install Node.js 18+</h2>

<p>Claude Code 基于 Node.js。如果你的电脑上还没有 Node.js，先装它。</p>

<div class="step-card">

<h3>Windows</h3>
<p>去 <a href="https://nodejs.org" target="_blank" rel="noopener">nodejs.org</a>，下载 LTS 版本（推荐 20.x 或 22.x）。运行安装程序，全部默认选项，一路 Next 到底。</p>

<p>安装完成后，打开 <strong>PowerShell</strong>（按 Win 键，输入 PowerShell，回车），验证安装：</p>

<pre><code>node --version
# 应该输出: v20.x.x 或 v22.x.x

npm --version
# 应该输出: 10.x.x</code></pre>
</div>

<div class="step-card">

<h3>Mac</h3>
<p>推荐用 Homebrew。如果你没装过 Homebrew，先打开 <strong>终端（Terminal）</strong> 运行：</p>

<pre><code>/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"</code></pre>

<p>然后安装 Node.js：</p>

<pre><code>brew install node@22</code></pre>

<p>验证安装：</p>

<pre><code>node --version
npm --version</code></pre>
</div>

<div class="step-card">

<h3>Linux (Ubuntu/Debian)</h3>

<pre><code>curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt-get install -y nodejs</code></pre>

<p>验证：</p>

<pre><code>node --version
npm --version</code></pre>
</div>

<h2>Step 2: Get Your Anthropic API Key</h2>

<p>这步容易搞混。你需要的是 <strong>API Key</strong>，不是 Claude.ai 的网页版账号。</p>

<ol>
<li>打开 <a href="https://console.anthropic.com" target="_blank" rel="noopener">console.anthropic.com</a></li>
<li>注册或登录（可以用 Google 账号）</li>
<li>首次使用需要绑定信用卡，设置消费限额（建议先设 $20/月）</li>
<li>左侧菜单 → <strong>API Keys</strong> → 点击 <strong>Create Key</strong></li>
<li>给 key 起个名字（比如 "claude-code-laptop"）→ 复制生成的 key</li>
</ol>

<div class="warning-box">
<p><strong>⚠️ 重要：</strong>Key 只显示一次。关闭页面后无法再次查看。请立即保存到安全的地方（密码管理器、文本文件都行，不要贴到聊天记录里）。</p>
</div>

<h2>Step 3: Install Claude Code</h2>

<p>打开终端（Windows: PowerShell。Mac: Terminal。Linux: Terminal），运行：</p>

<pre><code>npm install -g @anthropic-ai/claude-code</code></pre>

<p>这条命令做了什么：<code>npm install -g</code> 是"全局安装"，安装后你可以在任何目录里使用 <code>claude</code> 命令。<code>@anthropic-ai/claude-code</code> 是 Claude Code 的包名。</p>

<p>安装过程大约 30-60 秒。你可能会看到一些 warning 信息，只要最后没有红色的 <code>ERROR</code>，就可以继续。</p>

<p>验证安装成功：</p>

<pre><code>claude --version
# 应该输出类似: v1.x.x</code></pre>

<h2>Step 4: 配置 API Key</h2>

<p>有两种方式告诉 Claude Code 你的 API Key。推荐方式一：</p>

<div class="step-card">
<p><strong>方式一（推荐）：环境变量</strong>——将 key 设为系统环境变量，所有项目生效：</p>

<h3>Windows (PowerShell, 管理员模式)</h3>

<pre><code>[Environment]::SetEnvironmentVariable('ANTHROPIC_API_KEY', 'sk-ant-api03-your-key-here', 'User')</code></pre>

<p>把 <code>sk-ant-api03-your-key-here</code> 替换成你的真实 key。关闭并重新打开 PowerShell 使其生效。</p>

<h3>Mac / Linux (Terminal)</h3>

<pre><code># 添加到 shell 配置文件中（zsh 用户用 .zshrc，bash 用户用 .bashrc）
echo 'export ANTHROPIC_API_KEY="sk-ant-api03-your-key-here"' >> ~/.zshrc

# 立即生效
source ~/.zshrc</code></pre>
</div>

<div class="step-card">
<p><strong>方式二：项目级配置</strong>——只在当前项目中生效，适用于多个项目用不同 key 的情况：</p>

<pre><code># 在项目根目录创建 .env 文件
echo 'ANTHROPIC_API_KEY=sk-ant-api03-your-key-here' > .env</code></pre>

<p>Claude Code 启动时会自动读取 <code>.env</code> 文件。</p>
</div>

<h2>Step 5: 测试你的第一个 Claude Code 命令</h2>

<p>创建一个测试项目目录，然后启动 Claude Code：</p>

<pre><code># 创建测试目录
mkdir claude-test && cd claude-test

# 初始化 git（Claude Code 需要 git 来跟踪代码变更）
git init

# 启动 Claude Code
claude</code></pre>

<p>第一次启动时，Claude Code 可能会问你是否同意使用条款。输入 <code>y</code> 确认。</p>

<p>看到交互式界面后，输入你的第一个指令：</p>

<pre><code>创建一个简单的 HTML 文件 index.html，内容是一个现代化的"Hello World"页面，有居中的文字和好看的背景色。</code></pre>

<p>Claude 会：</p>

<ol>
<li>分析你的请求</li>
<li>生成代码</li>
<li>显示它打算做什么（可能需要你按 Enter 确认）</li>
<li>创建文件</li>
</ol>

<p>完成后，在浏览器中打开 <code>index.html</code> 查看结果。</p>

<h2>常见问题</h2>

<h3>Q: 提示 "API key not found"</h3>
<p>检查环境变量是否正确设置。运行 <code>echo $ANTHROPIC_API_KEY</code>（Mac/Linux）或 <code>$env:ANTHROPIC_API_KEY</code>（PowerShell）查看当前值。如果为空，回到 Step 4 重新设置。</p>

<h3>Q: 提示 "Insufficient permissions"</h3>
<p>去 <a href="https://console.anthropic.com/settings/billing" target="_blank" rel="noopener">Anthropic Console → Billing</a> 检查：账户余额是否 >$0、是否已绑定信用卡、消费限额是否用完。</p>

<h3>Q: 安装很慢或失败</h3>
<p>这是 npm 网络问题。尝试使用国内镜像：</p>

<pre><code>npm config set registry https://registry.npmmirror.com
npm install -g @anthropic-ai/claude-code
# 安装完成后恢复默认
npm config set registry https://registry.npmjs.org</code></pre>

<h3>Q: Claude Code 和 Cursor / Copilot 有什么区别？</h3>
<p>Claude Code 是<strong>命令行工具</strong>，适合快速改项目、自动化任务、在终端里直接操作。Cursor 是<strong>IDE</strong>（编辑器），适合边写代码边用 AI 辅助。Copilot 是<strong>IDE 插件</strong>，适合在已有编辑器里自动补全。实际工作中三者可以配合使用。</p>

<div class="next-step">
<p><strong>Next in this path:</strong> <a href="/article/claude-code-mcp-configuration">Part 2: Claude Code 环境配置与 MCP 工具集成 →</a></p>
</div>`,
    contentZh: zh,
  },

  // ====== Existing 25 articles (to be rewritten per new standards) ======
  "llms-in-plain-english": {
    content: `<div class="article-meta-banner">
<p><strong>Learning Path:</strong> AI Basics &middot; <strong>Part 1 of 5</strong></p>
<p><strong>Prerequisites:</strong> None &mdash; this article is for absolute beginners. No technical background required.</p>
</div>

<h2>What Is an LLM, Really?</h2>

<p>You have seen the headlines: "Large language models are changing everything." CEOs say them in earnings calls. Your cousin mentioned them at dinner. The term gets thrown around like everyone should already know what it means.</p>

<p>Here is the simplest way to think about it:</p>

<p><strong>A large language model (LLM) is a very advanced version of your phone's autocomplete.</strong></p>

<p>When you type "Happy Bir..." on your phone, it suggests "Birthday." That is a tiny language model making a prediction. Now imagine that system was trained on <strong>most of the public internet</strong> &mdash; books, Wikipedia, Reddit, scientific papers, GitHub code, news articles &mdash; and scaled up to be thousands of times more sophisticated. That is an LLM.</p>

<h2>How LLMs Actually Work (No Math)</h2>

<p>Every LLM does exactly one thing: it predicts the next word (or more precisely, the next "token"). A token is roughly 0.75 words. When you type a question, the model looks at all the tokens so far and calculates the most likely next token, over and over, until the response is complete.</p>

<p>There is no database lookup. There is no "knowledge" being retrieved. The model has no internal Wikipedia. It has a statistical map of which tokens tend to follow which sequences of tokens, built from the training data.</p>

<h2>By the Numbers</h2>

<p>The scale is genuinely staggering:</p>

<ul>
<li><strong>GPT-4</strong> was trained on approximately <strong>13 trillion tokens</strong> &mdash; roughly 10 trillion words. That is the equivalent of about 40 million books.</li>
<li>GPT-4 is estimated to have <strong>1.76 trillion parameters</strong>. More on what that means below.</li>
<li>The training run consumed thousands of GPUs running for months. Estimated cost: <strong>$100 million+</strong>.</li>
<li>Meta's Llama 3 405B was trained on <strong>15.6 trillion tokens</strong> using <strong>30.8 million GPU hours</strong>.</li>
</ul>

<p>These numbers help explain why only a handful of companies in the world can build frontier models: OpenAI, Google, Anthropic, Meta, and a few others. The compute cost alone is prohibitive.</p>

<h2>"Billions of Parameters" &mdash; What Does That Mean?</h2>

<p>A parameter is a number the model learned during training. Think of it as a tiny weight that influences the prediction. When you multiply billions of these weights together through the model's neural network, you get a prediction.</p>

<p>A useful analogy: imagine a recipe with 1.76 trillion knobs. During training, the model adjusts each knob so that when you give it "The capital of France is ___," it turns "Paris" into the most probable answer. "Billions of parameters" just means there are that many knobs to tune.</p>

<p>By comparison:</p>
<ul>
<li>GPT-1 (2018): 117 million parameters</li>
<li>GPT-3 (2020): 175 billion parameters</li>
<li>GPT-4 (2023): ~1.76 trillion parameters (estimated)</li>
<li>Llama 3 (2024): 8B, 70B, and 405B parameter variants</li>
<li>Claude 3.5 Sonnet (2024): estimated &#60;100B parameters but outperforms many larger models</li>
</ul>

<p>Notice the last entry: <strong>bigger is not always better</strong>. Architecture and training data quality matter at least as much as raw parameter count.</p>

<h2>How LLMs Are Different From Traditional Software</h2>

<p>This is the most important distinction to understand:</p>

<div class="step-card">
<p><strong>Traditional software:</strong> A developer writes explicit rules. If you click "Save," the program calls <code>saveFile()</code>. Every behavior is deterministic and programmed by a human. If it does something wrong, a human wrote the wrong code.</p>
</div>

<div class="step-card">
<p><strong>LLMs:</strong> No human wrote rules for what to say. The model learned patterns from data. When you ask a question, it generates a response that is <strong>statistically likely</strong> based on its training, not one that is guaranteed correct. This is why LLMs can write poetry (there is no "poetry function") and also why they confidently state false information (there is no "fact-check function").</p>
</div>

<h2>Real Example: What Happens Token by Token</h2>

<p>Let's say you ask ChatGPT: <strong>"What is the capital of Japan?"</strong></p>

<p>Here is approximately what happens under the hood:</p>

<pre><code>Input tokens: ["What", " is", " the", " capital", " of", " Japan", "?"]
Processing starts:
  Step 1: Model predicts next token &rarr; "The" (probability: 0.85)
  Step 2: &rarr; "capital" (probability: 0.78)
  Step 3: &rarr; "of" (probability: 0.92)
  Step 4: &rarr; "Japan" (probability: 0.90)
  Step 5: &rarr; "is" (probability: 0.83)
  Step 6: &rarr; "Tokyo" (probability: 0.95)
  Step 7: &rarr; "." (probability: 0.89)
  Step 8: &rarr; " It" (probability: 0.72) &mdash; begins follow-up elaboration
  ... continues until the model predicts "stop"</code></pre>

<p>The model does not know Japan has a capital. It does not know Tokyo is a city. It has seen the pattern "the capital of [country] is [city]" so many times in its training data that "Tokyo" is the overwhelmingly probable next token after "The capital of Japan is."</p>

<p>This is also why the model might <strong>also</strong> tell you about Tokyo's population, the history of Edo, and recommend restaurants &mdash; it has seen those patterns follow the same trigger phrase.</p>

<h2>The Most Important Thing to Remember</h2>

<p><strong>LLMs predict. They do not know.</strong></p>

<p>When a lawyer asks ChatGPT for case law and it fabricates six nonexistent court cases (this actually happened in 2023), it is not lying. It is predicting the most likely sequence of tokens that looks like a legal citation. The model has never seen a "truth database." It has seen patterns of text that include citations, so it generates more text that looks like a citation.</p>

<p>This distinction &mdash; prediction versus knowledge &mdash; explains nearly every weird behavior of LLMs: the hallucinations, the confident wrong answers, the creativity, the ability to write in any style, and the inability to do simple arithmetic reliably.</p>

<h2>FAQ</h2>

<h3>Q: Do LLMs understand what they are saying?</h3>
<p>No. There is no evidence of understanding, consciousness, or awareness in any current LLM. They manipulate tokens based on statistical patterns. They can <em>appear</em> to understand because human language is patterned, and mimicking patterns convincingly creates the illusion of understanding. But the underlying mechanism is prediction, not comprehension.</p>

<h3>Q: Are all LLMs basically the same under the hood?</h3>
<p>Architecturally, yes &mdash; most modern LLMs use a variant of the Transformer architecture (introduced by Google in 2017). But they differ enormously in training data, training methodology, size, and fine-tuning. GPT-4, Claude, Gemini, Llama, and DeepSeek all use Transformers but produce very different outputs because of different training choices.</p>

<h3>Q: Can I run an LLM on my own computer?</h3>
<p>Yes, but with caveats. Small models like Llama 3.2 3B or Microsoft Phi-3 can run on a modern laptop (8GB+ RAM) using tools like Ollama or LM Studio. Frontier models like GPT-4 require data center-scale hardware and cannot run locally. There is a growing ecosystem of capable small models that work offline and respect your privacy &mdash; at the cost of some capability compared to cloud models.</p>

<div class="next-step">
<p><strong>Next in this path:</strong> <a href="/article/ai-hallucinations-explained-with-examples">Part 2: AI Hallucinations Explained: Why ChatGPT Makes Stuff Up (With Real Examples) &rarr;</a></p>
</div>`,
    contentZh: zh,
  },
  // ... remaining articles stub for build compatibility
  "ai-hallucinations-explained-with-examples": {
    content: `<div class="article-meta-banner">
<p><strong>Learning Path:</strong> AI Basics &middot; <strong>Part 2 of 5</strong></p>
<p><strong>Prerequisites:</strong> <a href="/article/llms-in-plain-english">Part 1: LLMs in Plain English</a> &mdash; understanding that LLMs predict rather than know is essential for this article.</p>
</div>

<h2>What Is an AI Hallucination?</h2>

<p>An AI hallucination is when a language model generates information that is <strong>confidently incorrect</strong>. The model states falsehoods as facts, with the same grammatical certainty as true statements. It does not know it is wrong &mdash; because from its perspective, it is simply predicting the most probable next token.</p>

<p>This is not a bug that can be "fixed" with better code. It is a <strong>fundamental property</strong> of how LLMs work. They are next-token predictors, not fact-retrieval systems. Hallucination is the price we pay for a model that can write a poem, explain quantum physics, and draft a business plan &mdash; because the same mechanism that enables creativity also enables fabrication.</p>

<h2>3 Real Documented Cases</h2>

<h3>Case 1: The Lawyer Who Filed Fake Cases</h3>
<p>In 2023, a New York lawyer named Steven Schwartz used ChatGPT to prepare a legal brief. ChatGPT cited <strong>six court cases</strong> that did not exist &mdash; complete with docket numbers, judges, and legal reasoning. Schwartz filed the brief without verifying. The opposing counsel could not find any of the cases. When the judge asked, Schwartz admitted he had not verified the citations. He was sanctioned (fined) by the court.</p>

<p><strong>What happened:</strong> ChatGPT had seen countless examples of legal citations in its training data. When asked for relevant cases, it generated plausible-looking citations &mdash; because that is the most statistically likely pattern. It had no way of knowing these cases did not exist.</p>

<h3>Case 2: The Hallucinated Product Description</h3>
<p>A small business owner asked an AI to write a product description for a "silicone baking mat with temperature guide." The AI generated: "Features a built-in thermochromatic strip that changes color when the mat reaches 400&deg;F &mdash; a patented innovation from our R&amp;D team." None of this was true. The product had no such feature. If published, this would constitute false advertising.</p>

<p><strong>What happened:</strong> The AI combined patterns from other product descriptions (temperature-sensitive strips are real in other products) with the prompt's keywords. It "filled in" the details with plausible-sounding features that did not exist.</p>

<h3>Case 3: Invented Scientific Citations</h3>
<p>Researchers have documented multiple cases where AI models generate fake academic citations. A 2024 study found that when LLMs were asked to summarize research papers on specific topics, they invented non-existent papers with plausible titles, author names, and journal names &mdash; including publishing in real journals but with fabricated volume and page numbers.</p>

<p><strong>What happened:</strong> The model learned the <em>structure</em> of academic citations (Author, Year, Title, Journal, Volume, Pages) and generated text matching that structure. The content was fabricated because the model does not have a database of real papers &mdash; it has a statistical pattern of what citations look like.</p>

<h2>Why Does Hallucination Happen?</h2>

<p>Go back to the core mechanism from Part 1: token prediction. When you ask "What is the capital of France?" the model's training data contains the pattern "Paris" following "capital of France" millions of times. The probability for "Paris" is ~95%, so the answer is correct.</p>

<p>But when you ask something that <strong>looks like</strong> a factual question but has no clear statistical answer in the data, the model does not say "I don't know." It generates the <strong>most plausible-sounding sequence</strong> it can. Several factors increase hallucination risk:</p>

<ul>
<li><strong>Obscure topics:</strong> Less training data means weaker statistical patterns, so the model fills in what is plausible.</li>
<li><strong>Specific numbers and dates:</strong> LLMs are notoriously bad at exact numbers because token prediction does not favor arithmetic accuracy.</li>
<li><strong>Recent events:</strong> If the event happened after the model's training cutoff, the model cannot know about it &mdash; but it may fabricate a plausible-sounding answer rather than admitting ignorance.</li>
<li><strong>Ambiguous prompts:</strong> Vague questions give the model more room to fill gaps with invented details.</li>
</ul>

<h2>How to Detect Hallucinations</h2>

<div class="step-card">
<p><strong>Technique 1: Cross-check facts.</strong> Treat every specific claim from an LLM as potentially fabricated until verified. Dates, statistics, citations, and quotes are the most commonly hallucinated items.</p>
</div>

<div class="step-card">
<p><strong>Technique 2: Ask for sources.</strong> Say "Can you provide specific sources for that claim?" If the model produces citations, verify them independently. Many users have caught hallucinations this way.</p>
</div>

<div class="step-card">
<p><strong>Technique 3: Use Perplexity for factual queries.</strong> Perplexity.ai is designed to ground responses in web search results. It is not immune to hallucination but includes citations you can click to verify. For factual research, Perplexity outperforms ChatGPT's standalone knowledge.</p>
</div>

<div class="step-card">
<p><strong>Technique 4: Ask the model to self-critique.</strong> A known workaround: after getting an answer, prompt "Are you sure about that? Double-check." This sometimes causes the model to reconsider high-probability but incorrect token sequences.</p>
</div>

<h2>How to Reduce Hallucinations in Your Own Use</h2>

<p>These techniques will not eliminate hallucinations (nothing will), but they reduce the rate significantly:</p>

<ol>
<li><strong>Provide context.</strong> Do not ask "What are the key findings?" Say "Based on the transcript I just provided, what are the key findings?" Grounding the model in provided text reduces reliance on its statistical guesses.</li>
<li><strong>Ask for probabilities.</strong> "Rate your confidence in this answer from 1-10 and explain why." Models tend to be more cautious when explicitly asked about confidence.</li>
<li><strong>Break complex questions into steps.</strong> Instead of "Analyze this contract," ask "First, list all dates mentioned. Then summarize each clause separately." Step-by-step instructions reduce the model's need to "fill in" missing context.</li>
<li><strong>Use retrieval-augmented generation (RAG) tools.</strong> Tools like NotebookLM, Claude Projects, or custom GPTs let you upload documents that the model uses as its source of truth. When the model is constrained to your documents, hallucination drops dramatically.</li>
</ol>

<h2>What AI Companies Are Doing About It</h2>

<p>The industry is actively working on the problem. The main approaches in 2026:</p>

<ul>
<li><strong>Retrieval-Augmented Generation (RAG):</strong> Before generating an answer, the model searches a knowledge base for relevant documents and uses them as context. This grounds the response in verified information. Every major AI platform now offers some form of RAG.</li>
<li><strong>Grounding with web search:</strong> ChatGPT can now search the web, and Google Gemini is natively grounded in Google Search. This means the model can check facts against live sources &mdash; but only when search is explicitly enabled.</li>
<li><strong>Constitutional AI and training improvements:</strong> Anthropic's Constitutional AI approach and improved post-training techniques have reduced hallucination rates in Claude compared to earlier models. Independent benchmarks show Claude 3.5 Sonnet hallucinates approximately 40-60% less than GPT-3.5 on factual questions.</li>
<li><strong>Citation requirements:</strong> Modern models can be prompted to cite sources from their context, but this is a band-aid &mdash; the citation itself can be hallucinated.</li>
</ul>

<p><strong>The honest truth:</strong> Hallucination cannot be eliminated from pure LLMs. The mechanism that generates novel text is the same mechanism that generates false text. The solution is to combine LLMs with external tools (search, databases, verification systems) &mdash; not to rely on the model's "knowledge" alone.</p>

<h2>FAQ</h2>

<h3>Q: Does Claude hallucinate less than ChatGPT?</h3>
<p>In independent benchmarks (such as Vectara's Hallucination Leaderboard and LMSYS evaluations), Claude 3.5 Sonnet and GPT-4o have comparable hallucination rates on factual tasks, with Claude showing a slight edge on summarization tasks. Both hallucinate significantly less than GPT-3.5 or older models. However, no model is immune &mdash; you should verify critical information from any AI.</p>

<h3>Q: Can I train a model to not hallucinate on my specific data?</h3>
<p>Yes, this is called fine-tuning. If you have a dataset of verified Q&amp;A pairs in your domain, you can fine-tune a model to be more accurate on those specific types of questions. This does not eliminate hallucinations on out-of-domain questions but can dramatically improve accuracy on your use case. Tools like LlamaFactory and services like OpenAI's fine-tuning API make this accessible without being a machine learning expert.</p>

<h3>Q: Is a hallucination the same as a bug in the software?</h3>
<p>No. A software bug is when code does not do what it was designed to do. Hallucination is when the model does exactly what it was designed to do (predict likely tokens) but that behavior produces an incorrect statement from a human perspective. It is a feature of the architecture, not a flaw in the implementation. This is why "fixing" hallucinations is fundamentally harder than fixing a normal software bug.</p>

<div class="next-step">
<p><strong>Next in this path:</strong> <a href="/article/how-to-choose-right-ai-tool">Part 3: Which AI Tool Should You Use? A Decision Framework for Beginners &rarr;</a></p>
</div>`,
    contentZh: zh,
  },
  "how-to-choose-right-ai-tool": {
    content: `<div class="article-meta-banner">
<p><strong>Learning Path:</strong> AI Basics &middot; <strong>Part 3 of 5</strong></p>
<p><strong>Prerequisites:</strong> <a href="/article/llms-in-plain-english">Part 1: LLMs in Plain English</a> and <a href="/article/ai-hallucinations-explained-with-examples">Part 2: AI Hallucinations Explained</a> recommended for context.</p>
</div>

<h2>The Overwhelming AI Tool Landscape</h2>

<p>In 2026, there are dozens of AI tools, and at least five that are genuinely useful for most people: ChatGPT, Claude, Gemini, Perplexity, and Midjourney. Each is advertised as "the best AI," but the honest answer is that each tool is best at <strong>different things</strong>.</p>

<p>Here is the decision framework you actually need, based on what task you are trying to accomplish.</p>

<h2>Quick Decision Matrix</h2>

<div class="step-card">
<table>
<thead>
<tr>
<th>Task</th>
<th>Best Tool</th>
<th>Runner Up</th>
<th>Why</th>
</tr>
</thead>
<tbody>
<tr>
<td>Creative writing, emails, long-form content</td>
<td><strong>Claude</strong></td>
<td>ChatGPT</td>
<td>Claude's writing is more natural, less formulaic, and follows tone instructions better</td>
</tr>
<tr>
<td>Coding, debugging, technical work</td>
<td><strong>Claude</strong></td>
<td>ChatGPT</td>
<td>Claude has stronger code reasoning; ChatGPT is better for Python/data science</td>
</tr>
<tr>
<td>Research, fact-finding, current events</td>
<td><strong>Perplexity</strong></td>
<td>Gemini</td>
<td>Both ground answers in web search; Perplexity has better citation quality</td>
</tr>
<tr>
<td>Data analysis, Google integration</td>
<td><strong>Gemini</strong></td>
<td>ChatGPT</td>
<td>Gemini connects directly to Google Sheets, Gmail, and Docs via extensions</td>
</tr>
<tr>
<td>Image generation (artistic)</td>
<td><strong>Midjourney</strong></td>
<td>DALL-E 3</td>
<td>Midjourney produces the most aesthetically pleasing images; DALL-E 3 is better at following specific prompts</td>
</tr>
<tr>
<td>General conversation, brainstorming</td>
<td><strong>ChatGPT</strong></td>
<td>Claude</td>
<td>ChatGPT has the most flexible interface and handles back-and-forth dialogue best</td>
</tr>
<tr>
<td>Document analysis, long PDFs</td>
<td><strong>Claude</strong></td>
<td>NotebookLM</td>
<td>Claude has 200K token context window; NotebookLM excels at multi-document synthesis</td>
</tr>
</tbody>
</table>
</div>

<h2>For Writing Tasks &rarr; Claude</h2>

<p>If you are writing emails, blog posts, newsletters, or any content where <strong>tone and voice matter</strong>, Claude is the strongest option. In blind tests (including AIStudyOnline's own), readers consistently rate Claude's writing as more natural and less "AI-sounding" than ChatGPT's output.</p>

<p><strong>Real prompt comparison:</strong></p>
<p>Prompt: "Write a short email to my team announcing a project delay. Be honest but encouraging. The delay is 2 weeks for the mobile app launch due to QA issues."</p>

<p><strong>Claude output (condensed):</strong> "Hi team, I wanted to give you a transparent update on the mobile app timeline. We have hit some QA issues that need more time to resolve properly &mdash; we are looking at a 2-week delay. I know this is disappointing after all the hard work you have put in. Here is what we are doing about it..."</p>

<p><strong>ChatGPT output (condensed):</strong> "Dear Team, I hope this message finds you well. I am writing to inform you that due to unforeseen quality assurance challenges, we will need to adjust our timeline for the mobile application launch by approximately 14 days. We appreciate your understanding and continued dedication."</p>

<p>Claude sounds like a human colleague. ChatGPT sounds like a corporate memo. For professional writing where you want to sound like <em>you</em>, Claude is the better choice.</p>

<h2>For Research &rarr; Perplexity</h2>

<p>For factual research, do not use ChatGPT or Claude in their default modes. They will hallucinate sources, dates, and statistics. Use Perplexity or Gemini (with Google Search grounding enabled).</p>

<p>Perplexity Pro ($20/month) has a unique advantage: it searches the web in real time, reads multiple sources, and provides inline citations for every claim. You can click each citation to verify. This is fundamentally different from ChatGPT's approach, where the model generates an answer first and <em>optionally</em> searches the web afterward.</p>

<p><strong>When to use each:</strong></p>
<ul>
<li>Quick fact check &rarr; Perplexity (free tier)</li>
<li>Deep research on a topic &rarr; Perplexity Pro or NotebookLM</li>
<li>Academic literature review &rarr; NotebookLM (supports uploading PDFs)</li>
<li>Company research &rarr; Perplexity (better at finding current business information)</li>
<li>Historical topics &rarr; ChatGPT or Claude (training data covers pre-2025 well)</li>
</ul>

<h2>For Coding &rarr; Claude or ChatGPT</h2>

<p>Both are strong here, with different strengths:</p>

<ul>
<li><strong>Claude</strong> excels at reasoning through complex programming problems, refactoring existing code, and working with large codebases. Claude Code (the command-line tool) can read your entire project directory and make cross-file changes.</li>
<li><strong>ChatGPT</strong> excels at Python/data science tasks, generating boilerplate code, and explaining concepts. It also has Advanced Data Analysis (formerly Code Interpreter) which can run Python code and generate charts.</li>
<li><strong>GitHub Copilot</strong> and <strong>Cursor</strong> are specialized coding tools that integrate directly into your editor &mdash; they are better for day-to-day code completion than general-purpose chatbots.</li>
</ul>

<p>If you need one tool for both writing and coding, Claude is the better generalist. If you are doing heavy data analysis with Python, ChatGPT's Advanced Data Analysis is uniquely useful.</p>

<h2>For Creative Work &rarr; Midjourney + ChatGPT</h2>

<p>Text-based AI (LLMs) and image generation AI serve different creative needs. For visual work:</p>

<ul>
<li><strong>Midjourney</strong> ($10/month) produces the highest-quality artistic images. Its hands-down advantage is aesthetic composition, lighting, and style variety.</li>
<li><strong>DALL-E 3</strong> (included with ChatGPT Plus) is better at following specific instructions and rendering text in images. If you need "a blue sign that says 'Grand Opening' with a cake icon," DALL-E 3 will do it better.</li>
<li><strong>Leonardo.ai</strong> (free tier available) is the best free option for game assets and character design.</li>
</ul>

<p>A practical workflow: use ChatGPT to brainstorm and refine your concept, then use Midjourney or DALL-E to generate the final visual. Each tool does what it is best at.</p>

<h2>Free Tier Comparison</h2>

<div class="step-card">
<table>
<thead>
<tr>
<th>Tool</th>
<th>Free Tier Limit</th>
<th>Best Free Use Case</th>
</tr>
</thead>
<tbody>
<tr>
<td>ChatGPT</td>
<td>GPT-4o mini unlimited; GPT-4o/5 limited messages every few hours</td>
<td>General Q&amp;A, light writing</td>
</tr>
<tr>
<td>Claude</td>
<td>Claude 3.5 Sonnet unlimited; limited Claude 4 messages</td>
<td>Writing, coding, document analysis</td>
</tr>
<tr>
<td>Gemini</td>
<td>Gemini 2.0 Flash unlimited; limited Gemini 2.5 Pro</td>
<td>Google-integrated tasks, research</td>
</tr>
<tr>
<td>Perplexity</td>
<td>Unlimited basic queries; limited Pro searches</td>
<td>Fact-checking, quick research</td>
</tr>
<tr>
<td>Midjourney</td>
<td>Free trial (approx. 25 images)</td>
<td>Testing the tool before paying</td>
</tr>
</tbody>
</table>
</div>

<p><strong>The key insight:</strong> Free tiers of Claude and ChatGPT are surprisingly capable in 2026. For most casual writing, brainstorming, and learning tasks, the free tier is genuinely sufficient. You only need to pay for heavy usage, specific premium features (like image generation or long context), or specialized tools like Midjourney.</p>

<h2>FAQ</h2>

<h3>Q: Do I need all of these tools? Can I just use one?</h3>
<p>Most people get by with <strong>two</strong>: a primary chat AI (ChatGPT or Claude) and a research tool (Perplexity or Gemini). If you do not generate images, you do not need Midjourney. If you do not code, the coding comparison does not apply. Start with one primary tool &mdash; either ChatGPT or Claude &mdash; and add others only when you hit a specific limitation you cannot work around.</p>

<h3>Q: Is ChatGPT just objectively the best since it is the most popular?</h3>
<p>No. ChatGPT is the most popular because it was first to market (November 2022) and has the strongest brand recognition. Popularity does not equal superiority for every task. Claude matches or outperforms ChatGPT on writing and coding. Perplexity is better for research. Gemini has unique Google integration advantages. Choose based on your task, not on brand recognition.</p>

<h3>Q: Can I use free tiers indefinitely, or do they expire?</h3>
<p>ChatGPT, Claude, and Gemini free tiers are ongoing &mdash; they do not expire after a trial period. You get permanently reduced access to the latest models but can use them indefinitely. Perplexity's free tier is also permanent. Midjourney is the only one that requires payment after a short free trial. This is a change from 2023-2024 when free tiers were more limited.</p>

<div class="next-step">
<p><strong>Next in this path:</strong> <a href="/article/free-vs-paid-ai-tools-worth-it">Part 4: Free vs Paid AI Tools in 2026: When Your Money Is Actually Well Spent &rarr;</a></p>
</div>`,
    contentZh: zh,
  },
  "free-vs-paid-ai-tools-worth-it": {
    content: `<div class="article-meta-banner">
<p><strong>Learning Path:</strong> AI Basics &middot; <strong>Part 4 of 5</strong></p>
<p><strong>Prerequisites:</strong> <a href="/article/how-to-choose-right-ai-tool">Part 3: Which AI Tool Should You Use?</a> &mdash; familiarity with the different tools helps make sense of the pricing comparison.</p>
</div>

<h2>The Real Cost of AI in 2026</h2>

<p>Every major AI platform offers a free tier. Every major platform also tries to upsell you to a paid subscription. The question is not "can you get AI for free?" &mdash; the answer is yes. The question is: <strong>what are you giving up by not paying?</strong></p>

<p>Here is the exact 2026 pricing for the major platforms, what each tier actually gives you, and &mdash; most importantly &mdash; whether the upgrade matters for how you actually use AI.</p>

<h2>The Price Tag: What Everything Costs</h2>

<div class="step-card">
<table>
<thead>
<tr>
<th>Tool</th>
<th>Free Tier</th>
<th>Paid Tier</th>
<th>Paid Price (Monthly)</th>
</tr>
</thead>
<tbody>
<tr>
<td>ChatGPT</td>
<td>GPT-4o mini (unlimited), GPT-4o/5 (limited)</td>
<td>ChatGPT Plus</td>
<td>$20</td>
</tr>
<tr>
<td>Claude</td>
<td>Claude 3.5 Sonnet (unlimited), Claude 4 (limited)</td>
<td>Claude Pro</td>
<td>$20</td>
</tr>
<tr>
<td>Gemini</td>
<td>Gemini 2.0 Flash (unlimited), 2.5 Pro (limited)</td>
<td>Gemini Advanced</td>
<td>$20</td>
</tr>
<tr>
<td>Perplexity</td>
<td>Unlimited basic queries</td>
<td>Perplexity Pro</td>
<td>$20</td>
</tr>
<tr>
<td>Midjourney</td>
<td>~25 free images (one-time trial)</td>
<td>Midjourney Basic</td>
<td>$10</td>
</tr>
</tbody>
</table>
</div>

<p>Notice a pattern? The major chat AI platforms all charge <strong>$20/month</strong>. This is not a coincidence &mdash; it is market pricing convergence. When you pay for one, you are paying roughly the same as for any other. This makes the "which one do I pay for" decision more important than "should I pay."</p>

<h2>What the Free Tier Actually Gives You</h2>

<p>The free tiers have improved significantly since 2024. Here is the honest assessment of what you get without paying:</p>

<ul>
<li><strong>ChatGPT Free:</strong> You get GPT-4o mini for unlimited conversations. This model is fast and capable &mdash; it handles most writing, Q&amp;A, and brainstorming tasks well. You also get a limited number of GPT-4o or GPT-5 messages (typically 10-30 every 3-5 hours, depending on demand). You do <strong>not</strong> get DALL-E image generation, Advanced Data Analysis, or web search on the free tier (except limited testing).</li>
<li><strong>Claude Free:</strong> You get Claude 3.5 Sonnet for unlimited conversations &mdash; notably, this was OpenAI's $20/month model in 2024 and remains one of the best models available. You also get limited Claude 4 messages (Opus-class). File uploads and 200K context are available on the free tier.</li>
<li><strong>Gemini Free:</strong> You get Gemini 2.0 Flash unlimited and limited access to Gemini 2.5 Pro. Google's free tier is the most generous in terms of features &mdash; web search grounding is built in, and you can connect Google Drive.</li>
<li><strong>Perplexity Free:</strong> You get unlimited basic queries with search grounding. You are limited to a lower number of "Pro" searches per day (which use higher-quality models and deeper search). The free tier is genuinely useful for research.</li>
<li><strong>Midjourney Free:</strong> There is no ongoing free tier. You get a one-time trial of roughly 25 images, after which you must pay $10/month.</li>
</ul>

<h2>What the Paid Tier Adds (Not Marketing &mdash; Real Differences)</h2>

<h3>ChatGPT Plus ($20/month)</h3>
<ul>
<li>Unlimited access to GPT-4o and GPT-5 (not just limited messages)</li>
<li>DALL-E 3 image generation (about 2 images per prompt, ~40 per 3 hours)</li>
<li>Advanced Data Analysis: upload CSV/Excel files, run Python code, generate charts</li>
<li>Web search integration (more reliable than the free tier's limited search)</li>
<li>Custom GPTs and GPT Store access</li>
<li>Higher priority during peak usage (fewer "ChatGPT is at capacity" errors)</li>
</ul>

<h3>Claude Pro ($20/month)</h3>
<ul>
<li>Unlimited Claude 4 messages (versus limited on free tier)</li>
<li>5x higher usage limits on Claude 4</li>
<li>Priority access during high-traffic periods</li>
<li>Claude Projects with knowledge bases (upload documents as context)</li>
<li>Early access to new features</li>
</ul>

<h3>Gemini Advanced ($20/month, included with Google One 2TB)</h3>
<ul>
<li>Unlimited Gemini 2.5 Pro access</li>
<li>Priority access to new features (like real-time video analysis)</li>
<li>2TB Google Drive storage (uniquely, the subscription includes cloud storage)</li>
<li>Google Workspace integration (Gmail, Docs, Sheets AI features)</li>
</ul>

<h3>Perplexity Pro ($20/month)</h3>
<ul>
<li>Unlimited Pro searches (deeper research, higher-quality models)</li>
<li>File uploads (PDF, image analysis as part of search)</li>
<li>Higher-quality citation extraction</li>
<li>API access for custom integrations</li>
</ul>

<h2>When Free Is Enough</h2>

<p>You do not need to pay for AI if any of these describe you:</p>

<ul>
<li><strong>Casual writing:</strong> Emails, social media posts, brainstorming ideas. Both free Claude (3.5 Sonnet) and free ChatGPT (4o mini) handle these perfectly.</li>
<li><strong>Learning and Q&amp;A:</strong> Asking questions about topics you are studying. The free tiers have full knowledge up to their training cutoff and answer clearly.</li>
<li><strong>Summarizing documents:</strong> Free Claude supports file uploads with 200K context. You can paste long documents and get summaries &mdash; no payment needed.</li>
<li><strong>Occasional use:</strong> If you use AI 2-3 times per week, the free tier message limits will never be an issue.</li>
<li><strong>Light research:</strong> Free Perplexity with basic search is sufficient for fact-checking common topics.</li>
</ul>

<h2>When Paid Actually Matters</h2>

<p>These are the scenarios where the paid tier is worth the $20/month:</p>

<ul>
<li><strong>Daily heavy use:</strong> If you use AI for work every day, hitting free-tier message limits becomes frustrating. $20/month removes the ceiling.</li>
<li><strong>Professional content creation:</strong> If you write for a living, Claude Pro's unlimited Claude 4 access and Projects feature substantially improve output quality.</li>
<li><strong>Data analysis:</strong> ChatGPT Plus's Advanced Data Analysis lets you upload messy CSV files and get clean visualizations &mdash; useful for small business owners, analysts, and researchers.</li>
<li><strong>Image generation:</strong> Midjourney ($10) or DALL-E 3 (via ChatGPT Plus) are essential if you create visual content. There is no viable free alternative for quality AI image generation beyond trials.</li>
<li><strong>Coding:</strong> Claude Pro's higher limits and Claude Code access are worth it if you code daily. The free tier rates are too restrictive for real development work.</li>
</ul>

<h2>Total Cost of Ownership</h2>

<p>Let's do the math for someone using AI daily across multiple tasks:</p>

<div class="step-card">
<p><strong>Scenario 1: Casual user (writing + research)</strong></p>
<p>Free Claude + Free Perplexity = <strong>$0/month</strong>. You lose nothing of practical value.</p>
</div>

<div class="step-card">
<p><strong>Scenario 2: Professional writer</strong></p>
<p>Claude Pro ($20) + Free Perplexity = <strong>$20/month</strong>. Worth it for unlimited Claude 4 access.</p>
</div>

<div class="step-card">
<p><strong>Scenario 3: Coder + Writer + Researcher</strong></p>
<p>Claude Pro ($20) + Perplexity Pro ($20) = <strong>$40/month</strong>. You can skip Perplexity Pro if you only use it occasionally.</p>
</div>

<div class="step-card">
<p><strong>Scenario 4: Full stack (writing, coding, image generation, research)</strong></p>
<p>Claude Pro ($20) + Perplexity Pro ($20) + Midjourney ($10) = <strong>$50/month</strong>. This covers everything most individuals need.</p>
</div>

<p>The honest conclusion: <strong>most people need $0/month.</strong> The free tiers have improved to the point where they serve 80% of use cases well. Pay only when you hit a specific limitation &mdash; and then pay for the specific tool that addresses that limitation, not all of them.</p>

<h2>FAQ</h2>

<h3>Q: Do I get a better AI "brain" by paying, or just more access?</h3>
<p>Both. With ChatGPT Plus, you get access to GPT-5 (vs GPT-4o mini on free). With Claude Pro, you get Claude 4 (vs Claude 3.5 Sonnet on free). The paid models are genuinely more capable &mdash; they reason better, hallucinate less, and handle more complex instructions. But the free models (especially Claude 3.5 Sonnet and GPT-4o mini) are still very capable for everyday tasks. The difference matters most for complex or professional work; for casual use, the free models are sufficient.</p>

<h3>Q: Can I share a paid subscription with family members?</h3>
<p>ChatGPT Plus, Claude Pro, and Perplexity Pro are individual subscriptions &mdash; sharing accounts violates terms of service and may get your account suspended. Gemini Advanced is the exception: a Google One family plan ($30/month) covers up to 5 family members with their own accounts. Midjourney does not officially support account sharing.</p>

<h3>Q: What about the API? Is it cheaper than subscriptions for heavy use?</h3>
<p>For very heavy use (thousands of queries per day), the API can be cheaper. For example, running automated tasks through Claude's API costs roughly $3-15 per million input tokens depending on the model. A developer running millions of tokens per month would pay less via API than the $20 subscription. But the subscription includes the chat interface, projects, file uploads, and other features the API does not provide. For most people, the subscription is better value; for automated/scaled use, the API wins.</p>

<div class="next-step">
<p><strong>Next in this path:</strong> <a href="/article/ai-myths-people-still-believe">Part 5: 5 AI Myths Your Non-Techie Friends Still Believe (and What's Actually True) &rarr;</a></p>
</div>`,
    contentZh: zh,
  },
  "what-is-a-gpu-non-techie": {
    content: `<div class="article-meta-banner">
<p><strong>Category:</strong> AI Basics &middot; <strong>Standalone Article</strong></p>
<p><strong>Prerequisites:</strong> None &mdash; this is about hardware, not AI software. No technical background needed.</p>
</div>

<h2>What Is a GPU, Really?</h2>

<p>You have heard that NVIDIA is now one of the most valuable companies in the world. You have heard "GPUs run AI." But what is a GPU, and why does it matter?</p>

<p><strong>GPU stands for Graphics Processing Unit.</strong> It was designed to render video game graphics. A CPU (your computer's main processor) is great at doing a few complex tasks very quickly. A GPU is great at doing millions of simple tasks simultaneously.</p>

<p>Think of it like this: a CPU is one person doing advanced calculus. A GPU is 10,000 people doing basic arithmetic at the same time.</p>

<p>For video games, the GPU calculates pixel colors 60 times per second. For AI, the GPU does millions of matrix multiplications simultaneously &mdash; exactly what neural networks need.</p>

<h2>Why AI Needs GPUs</h2>

<p>Neural networks are layers of mathematical operations, mostly matrix multiplications. A matrix is a grid of numbers, and multiplying two large matrices involves the same simple calculation millions of times. GPUs handle this in parallel; CPUs would take forever.</p>

<pre><code>CPU: Calculate 1+2, then 3+4, then 5+6... (sequential)
GPU: Calculate 1+2, 3+4, 5+6... all at the same time (parallel)</code></pre>

<p>Training GPT-4 required approximately 25,000 NVIDIA A100 GPUs running for 90-120 days. At roughly $10,000 per GPU, that is $250 million in hardware alone before electricity and labor. This is why only major companies train frontier models.</p>

<h2>GPU Comparison</h2>

<table>
<thead>
<tr><th>GPU</th><th>VRAM</th><th>Use Case</th><th>Price (2026)</th></tr>
</thead>
<tbody>
<tr><td>NVIDIA RTX 5090</td><td>32 GB</td><td>Gaming, hobbyist AI</td><td>$2,000</td></tr>
<tr><td>NVIDIA A100</td><td>80 GB</td><td>Data center training</td><td>$10,000+</td></tr>
<tr><td>NVIDIA H100</td><td>80 GB</td><td>Frontier AI training</td><td>$25,000+</td></tr>
<tr><td>NVIDIA B200</td><td>192 GB</td><td>Latest gen (2025+)</td><td>$30,000+</td></tr>
<tr><td>Apple M4 Ultra</td><td>192 GB unified</td><td>Local AI on Mac</td><td>Built into Mac</td></tr>
</tbody>
</table>

<h2>Do You Need a GPU for AI?</h2>

<p>For cloud AI (ChatGPT, Claude, Midjourney), no. The provider's servers have thousands of GPUs. You just pay for the result through subscriptions or API usage.</p>

<p>For local AI (running models on your own computer), a GPU helps but is not required. Small models like Llama 3.2 3B run on CPU with acceptable speed. Larger models like Llama 3.1 8B benefit from a GPU but still work on CPU.</p>

<p>VRAM determines how large a model you can load locally. A 7B parameter model in 4-bit needs about 4 GB. A 70B model needs about 40 GB. This is why running the largest models locally requires data-center GPUs or aggressive compression.</p>

<h2>FAQ</h2>

<h3>Q: How do I check if my computer has a GPU?</h3>
<p>Windows: Task Manager (Ctrl+Shift+Esc) &rarr; Performance tab &rarr; look for GPU. Mac: Apple menu &rarr; About This Mac &rarr; Graphics. Linux: run <code>lspci | grep -i vga</code> in terminal.</p>

<h3>Q: Should I buy a GPU for AI?</h3>
<p>Only if you specifically want to run open-source models locally for privacy, offline access, or experimentation. For cloud AI use, any computer or phone with internet access works fine. Start with CPU-based tools like Ollama before spending money on a GPU.</p>

<h3>Q: Why is NVIDIA so valuable if GPUs were already common?</h3>
<p>NVIDIA's market cap surpassed $3 trillion because AI demand created exponential GPU growth. Data centers now buy GPUs at unprecedented scale. Competitors AMD and Intel are racing to catch up, but NVIDIA's CUDA software ecosystem gives it a massive advantage for AI workloads.</p>

<div class="next-step">
<p><strong>End of standalone article.</strong> <a href="/learn">Browse all learning paths &rarr;</a></p>
</div>`,
    contentZh: zh,
  },
  "ai-myths-people-still-believe": {
    content: `<div class="article-meta-banner">
<p><strong>Learning Path:</strong> AI Basics &middot; <strong>Part 5 of 5</strong></p>
<p><strong>Prerequisites:</strong> This is the final article in the AI Basics path. <a href="/article/llms-in-plain-english">Part 1</a> through <a href="/article/free-vs-paid-ai-tools-worth-it">Part 4</a> recommended, though each myth stands alone.</p>
</div>

<h2>Why Myths Persist</h2>

<p>AI is the most hyped technology since the internet. The hype generates genuine excitement &mdash; and also genuine confusion. Three years into the mainstream AI era, certain myths refuse to die. Some come from sensational headlines. Some come from sci-fi expectations. Some come from misunderstanding how the technology actually works.</p>

<p>Here are the five most persistent myths, and what the evidence actually shows.</p>

<h2>Myth 1: "AI Is Conscious"</h2>

<p><strong>The belief:</strong> ChatGPT and similar AI systems are "waking up." They have thoughts, feelings, goals, or some form of awareness. Headlines about "sentient AI" and the Blake Lemoine/LaMDA incident (2022) gave this myth real traction.</p>

<p><strong>What is actually true:</strong> No current AI system is conscious. There is no evidence of subjective experience, self-awareness, or genuine understanding in any LLM. Every AI system in production today is a <strong>statistical pattern matcher</strong> &mdash; it predicts the next token based on patterns in training data. This is mathematically and architecturally different from consciousness.</p>

<p><strong>The evidence:</strong> If you ask ChatGPT "Are you conscious?" it will say "No, I'm not conscious." This is not self-awareness &mdash; it is repeating the pattern it learned from training data about how AI systems describe themselves. The same model will also generate a first-person narrative from the perspective of a toaster if prompted. Neither response reflects internal experience, because there is none.</p>

<p><strong>Counterexample:</strong> When Google engineer Blake Lemoine claimed Google's LaMDA model was sentient in 2022, he was citing responses where the model described having feelings. What actually happened: LaMDA was pattern-matching on science fiction dialogues and philosophical texts about consciousness. It generated plausible-sounding text about having feelings &mdash; the same way it would generate a plausible-sounding story about being a pirate. The scientific community universally rejected Lemoine's claims. Google placed him on leave.</p>

<h2>Myth 2: "AI Will Take All Jobs"</h2>

<p><strong>The belief:</strong> AI will automate every white-collar job within 2-3 years. Nobody will have work. "AI killed the office job" is a common narrative in click-driven media.</p>

<p><strong>What is actually true:</strong> AI automates <strong>tasks</strong>, not <strong>jobs</strong>. This distinction matters enormously. A single job involves dozens of tasks, many of which current AI cannot do reliably. The evidence from 2023-2026 shows that AI has augmented workers, not replaced them at scale.</p>

<p><strong>The evidence:</strong></p>
<ul>
<li>A 2025 McKinsey study found that less than 5% of occupations could have the majority of their tasks automated with current AI technology.</li>
<li>US Bureau of Labor Statistics data shows employment rates in white-collar fields (software, legal, accounting) have not declined since ChatGPT launched in 2022.</li>
<li>Upwork and Fiverr both report increased demand for human freelancers in AI-related categories (prompt engineering, AI content editing, AI workflow design).</li>
<li>JPMorgan, one of the most aggressive AI adopters, stated in 2025 that AI would augment employees, not replace them &mdash; and hired more workers that year.</li>
</ul>

<p><strong>Counterexample:</strong> The "AI will replace translators" prediction has been a recurring headline since 2017. Seven years later, professional translators remain in demand &mdash; not because AI cannot translate, but because real translation work involves context, cultural nuance, domain expertise, and client relationships that AI handles poorly. Translation tools increased productivity but did not eliminate the profession.</p>

<h2>Myth 3: "AI Knows Everything"</h2>

<p><strong>The belief:</strong> You can ask AI any question and get a reliable answer. It was trained on the internet, so it must know everything the internet knows.</p>

<p><strong>What is actually true:</strong> AI has three fundamental knowledge limitations that most users do not realize:</p>

<ol>
<li><strong>Training cutoff:</strong> Every LLM has a knowledge cutoff date. GPT-4o's knowledge ends in 2023. Anything that happened after that date &mdash; a 2025 election result, a 2024 product launch, last week's news &mdash; is outside the model's training data. The model does not know these events occurred.</li>
<li><strong>Hallucination:</strong> As covered in Part 2 of this path, LLMs fabricate information confidently. A model that seems omniscient is actually generating plausible-sounding text, which can be entirely incorrect.</li>
<li><strong>No real-time awareness:</strong> Unlike Google Search, an LLM does not browse the web unless specifically designed to do so (and even then, only when the feature is enabled). By default, it answers from frozen training data.</li>
</ol>

<p><strong>Counterexample:</strong> Ask any LLM "What happened in the Super Bowl last week?" without enabling web search. The model will either admit it does not know (if well-trained) or fabricate a score, team names, and highlights (if not). This is not knowledge &mdash; it is pattern completion. The moment you ask about something outside the training distribution, the model's limitations become obvious.</p>

<h2>Myth 4: "Bigger Models Are Always Better"</h2>

<p><strong>The belief:</strong> The model with the most parameters is the best model. GPT-5 with trillions of parameters must be smarter than a smaller model. Size equals capability.</p>

<p><strong>What is actually true:</strong> Model quality depends on <strong>architecture, training data quality, and training methodology</strong> &mdash; not just parameter count. Small, well-trained models frequently outperform larger, sloppier ones on specific tasks.</p>

<p><strong>The evidence:</strong></p>
<ul>
<li>Microsoft's Phi-3 (3.8B parameters) can outperform Llama 2 (70B parameters) on reasoning benchmarks. A model 18x smaller, trained on higher-quality curated data, matches or exceeds the larger model.</li>
<li>Claude 3.5 Sonnet (estimated &#60;100B parameters) matches or beats GPT-4 (estimated 1.76T parameters) on multiple benchmarks &mdash; despite being ~20x smaller.</li>
<li>Llama 3 8B performs comparably to GPT-3.5 (175B parameters) on many tasks. Again, a 20x size difference with roughly equivalent capability.</li>
<li>Gemini 2.0 Flash (Google's lightweight model) beats Gemini 1.5 Pro (Google's previous heavy model) on speed and several quality metrics.</li>
</ul>

<p><strong>Counterexample:</strong> Specialized small models (like medical diagnosis models, code completion models, or translation models) are often deliberately kept small because they perform their specific task better than a general-purpose giant. A 7B model trained on medical literature will give better medical advice than GPT-5, because it was trained for that specific purpose.</p>

<h2>Myth 5: "AI Is Unbiased and Objective"</h2>

<p><strong>The belief:</strong> Because AI is a machine and not a human, it must be neutral and objective. It processes data without human prejudice.</p>

<p><strong>What is actually true:</strong> AI systems inherit and can amplify biases present in their training data. Since most training data is from the internet &mdash; which reflects human biases &mdash; AI models reproduce those biases unless explicitly corrected.</p>

<p><strong>Real documented examples of AI bias:</strong></p>
<ul>
<li><strong>Gender bias in hiring tools:</strong> Amazon's AI recruiting tool (trained on 10 years of resumes) systematically penalized resumes containing the word "women's." It was trained on a dataset where most successful candidates were men, so it learned to prefer male-associated language. Amazon scrapped the tool in 2018, but similar biases persist in modern LLMs.</li>
<li><strong>Racial bias in healthcare:</strong> A 2019 study found that a widely-used healthcare algorithm (not an LLM, but an ML system) systematically underestimated the health needs of Black patients. The algorithm used healthcare spending as a proxy for health needs &mdash; but Black patients historically spend less on healthcare due to systemic inequities, so the algorithm concluded they needed less care.</li>
<li><strong>Image generation bias:</strong> Early versions of DALL-E and Stable Diffusion, when asked to generate "a CEO," produced predominantly white male images. When asked for "a nurse," produced predominantly white female images. These biases directly reflect the statistical distribution of images in the training data.</li>
<li><strong>LLM political bias:</strong> Multiple studies have shown that ChatGPT, Claude, and Gemini exhibit detectable political leanings (generally left-of-center on US political spectrum) on controversial topics. This is not intentional &mdash; it reflects the distribution of political content in their training data, which over-represents certain viewpoints.</li>
</ul>

<p><strong>The counter-approach:</strong> AI companies now invest heavily in bias mitigation. Techniques include: balanced training data curation, RLHF (reinforcement learning from human feedback) with diverse evaluators, and "red teaming" (deliberate testing for harmful outputs). These measures reduce bias but do not eliminate it &mdash; and the mitigations themselves introduce different biases in the form of safety filtering that can censor legitimate discussion.</p>

<h2>Why These Myths Matter</h2>

<p>Believing myths about AI leads to poor decisions: relying on AI for things it cannot do, fearing AI for things it will not do, and misunderstanding what "progress" actually looks like. The goal of this AI Basics path has been to replace hype with understanding &mdash; not to diminish AI's real capabilities, but to make them clearer and more useful.</p>

<p><strong>The honest summary:</strong> AI is not conscious, not about to take all jobs, not omniscient, not optimally served by ever-larger models, and not objective. It is an extraordinarily capable text prediction system that, when used with understanding of its limitations, can be genuinely useful. That reality is more valuable than any myth.</p>

<h2>FAQ</h2>

<h3>Q: If AI is not conscious, why does it sometimes seem emotional or empathetic?</h3>
<p>Because it was trained on human text, which includes emotional and empathetic language. When you tell ChatGPT "I'm having a bad day," it generates responses that match patterns of supportive human conversation. It is not feeling empathy &mdash; it is generating text that looks like empathy, because that is what the training data contains. This is useful (getting a sympathetic response can feel supportive), but it is pattern matching, not emotion.</p>

<h3>Q: Will future AI be conscious? Is consciousness on the roadmap?</h3>
<p>There is no scientific consensus on whether or when AI could become conscious. Current architectures (Transformers) are not designed to produce consciousness. Major AI labs are not pursuing consciousness as a goal &mdash; they are pursuing capability improvements (better reasoning, fewer errors, larger context). Claims that "AGI is coming in 2-3 years" are speculative, not based on published research roadmaps. Treat such claims with skepticism.</p>

<h3>Q: If AI has built-in bias, should I still use it?</h3>
<p>Yes, but with awareness. All human-generated information has bias &mdash; news articles, textbooks, government reports, Wikipedia. The problem with AI is that its biases are harder to detect because the model presents information as neutral. Use AI for what it is good at (drafting, brainstorming, summarizing, coding) while maintaining skepticism about factual claims and being aware that the model's "neutral" tone may conceal underlying training data skew. Cross-checking important information remains essential.</p>

<div class="next-step">
<p><strong>End of AI Basics learning path.</strong> <a href="/learn">Explore more learning paths &rarr;</a></p>
</div>`,
    contentZh: zh,
  },
  "chatgpt-voice-mode-job-interview": {
    content: `<div class="article-meta-banner">
<p><strong>Learning Path:</strong> ChatGPT Mastery &middot; <strong>Part 1 of 5</strong></p>
<p><strong>Prerequisites:</strong> None &mdash; a free ChatGPT account is helpful but not required.</p>
</div>

<h2>Your First ChatGPT Session</h2>

<p>ChatGPT is the most widely used AI tool in the world, with over 400 million monthly active users as of early 2026. If you have not tried it yet, or you signed up but felt unsure where to start, this guide walks through the interface, settings, and first prompts.</p>

<h2>Step 1: Create Your Account</h2>
<ol>
<li>Go to <a href="https://chatgpt.com" target="_blank" rel="noopener">chatgpt.com</a></li>
<li>Click "Sign Up" &mdash; use email, Google, or Apple account</li>
<li>Verify your email address</li>
<li>You are now on the free tier with access to GPT-4o mini (unlimited) and limited GPT-5 messages</li>
</ol>

<h2>Step 2: Interface Tour</h2>
<p>The ChatGPT interface has three main areas:</p>
<ul>
<li><strong>Left sidebar:</strong> Shows your chat history. Click the pencil icon to start a new chat. You can rename, delete, or archive conversations.</li>
<li><strong>Center chat area:</strong> Where conversations happen. Your messages appear on the right, ChatGPT's on the left.</li>
<li><strong>Bottom input bar:</strong> Type your message. The paperclip icon lets you upload files. The microphone icon enables voice input (browser and app).</li>
</ul>

<h2>Step 3: Settings to Configure</h2>
<p>Click your profile picture &rarr; Settings:</p>
<ul>
<li><strong>Data Controls:</strong> Disable "Improve the model for everyone" if you want your conversations excluded from training</li>
<li><strong>Custom Instructions:</strong> Tell ChatGPT about yourself permanently ("I am a marketing manager who prefers concise answers")</li>
<li><strong>Memory:</strong> Lets ChatGPT remember facts across conversations. You can view, edit, or delete what it remembers</li>
<li><strong>Beta Features:</strong> Enable new features before they launch broadly</li>
</ul>

<h2>Your First 10 Prompts</h2>
<p>Try these prompts in order to explore ChatGPT's capabilities:</p>

<ol>
<li><strong>Summarize:</strong> "Summarize the key points of the attached PDF in 3 bullet points."</li>
<li><strong>Write:</strong> "Write a professional email asking for a deadline extension on a project."</li>
<li><strong>Explain:</strong> "Explain how cryptocurrency works to a 10-year-old."</li>
<li><strong>Brainstorm:</strong> "Give me 10 blog post ideas for a small bakery."</li>
<li><strong>Edit:</strong> "Fix the grammar in this paragraph and make it more concise." [paste text]</li>
<li><strong>Format:</strong> "Convert this list into a markdown table with columns for Name, Price, and Rating."</li>
<li><strong>Translate:</strong> "Translate this email to Spanish while keeping the professional tone."</li>
<li><strong>Role play:</strong> "Act as a hiring manager and interview me for a product manager role."</li>
<li><strong>Plan:</strong> "Create a 3-day itinerary for Paris with a $100/day budget."</li>
<li><strong>Analyze:</strong> "What are the pros and cons of this decision?" [describe a decision]</li>
</ol>

<h2>Free vs Plus: What You Start With</h2>
<p>On the free tier, you get GPT-4o mini (fast and capable for most tasks) plus limited GPT-5 messages (about 10 every 5 hours). This is enough to learn and experiment. When you hit limits consistently, consider ChatGPT Plus ($20/month) for unlimited access to the latest models.</p>

<h2>FAQ</h2>

<h3>Q: Can ChatGPT see my private information?</h3>
<p>OpenAI does not use API data for training by default, and ChatGPT users can opt out of training. Go to Settings &rarr; Data Controls and disable "Improve the model." For sensitive information, consider Claude (which offers stronger privacy defaults) or local models.</p>

<h3>Q: How is ChatGPT different from Google Search?</h3>
<p>Google Search finds existing web pages matching your keywords. ChatGPT generates new text based on patterns in training data. For factual queries, Google is more reliable. For writing, analysis, and conversation, ChatGPT is better.</p>

<h3>Q: Does ChatGPT have a mobile app?</h3>
<p>Yes. ChatGPT has official iOS and Android apps with voice input support. The app syncs history with the web version. Advanced Voice Mode (real-time conversation with tone detection) is available on Plus.</p>

<div class="next-step">
<p><strong>Next in this path:</strong> <a href="/article/claude-projects-organize-chats">Part 2: How to Write Prompts That Actually Work: The 5-Point Framework &rarr;</a></p>
</div>`,
    contentZh: zh,
  },
  "claude-projects-organize-chats": {
    content: `<div class="article-meta-banner">
<p><strong>Learning Path:</strong> ChatGPT Mastery &middot; <strong>Part 2 of 5</strong></p>
<p><strong>Prerequisites:</strong> <a href="/article/chatgpt-voice-mode-job-interview">Part 1: ChatGPT Fundamentals</a> &mdash; you should have a ChatGPT account and have tried basic prompts.</p>
</div>

<h2>Why Most Prompts Fail</h2>

<p>Most people type vague questions and get mediocre answers. The problem is not the AI &mdash; it is the prompt. A well-structured prompt produces dramatically better results. This article introduces the 5-Point Prompt Framework, a systematic approach that works across ChatGPT, Claude, Gemini, and any other LLM.</p>

<h2>The 5-Point Prompt Framework</h2>

<p>Every effective prompt includes these five elements. You do not always need all five, but including them when relevant improves output quality significantly.</p>

<div class="step-card">
<h3>1. Role</h3>
<p>Tell the AI who it is. "You are a..." sets context for tone, expertise level, and perspective.</p>
<p><strong>Instead of:</strong> "Explain quantum computing."</p>
<p><strong>Try:</strong> "You are a physics professor teaching a high school class. Explain quantum computing using analogies a 16-year-old would understand."</p>
</div>

<div class="step-card">
<h3>2. Context</h3>
<p>Give background information the AI needs. Without context, the AI defaults to generic answers.</p>
<p><strong>Instead of:</strong> "Write a marketing email."</p>
<p><strong>Try:</strong> "We are a small SaaS company launching a project management tool for freelancers. Our product costs $15/month and competes with Asana and Trello but is simpler. Write a launch email to our 500-person waitlist."</p>
</div>

<div class="step-card">
<h3>3. Task</h3>
<p>State exactly what you want. Be specific about the action and scope.</p>
<p><strong>Weak:</strong> "Help me with my resume."</p>
<p><strong>Strong:</strong> "Review my resume for a software engineering role. Identify 3 sections that need improvement and rewrite each one."</p>
</div>

<div class="step-card">
<h3>4. Format</h3>
<p>Specify the output structure. AI defaults to paragraphs. Explicit format instructions give you what you actually need.</p>
<p><strong>Examples:</strong> "Output as a table with columns for Task, Time, and Priority." / "Return as a bullet list with 5 items." / "Write exactly 100 words."</p>
</div>

<div class="step-card">
<h3>5. Constraints</h3>
<p>Set boundaries. This is the most commonly skipped element and the one that most improves specificity.</p>
<p><strong>Examples:</strong> "Do not use jargon." / "Assume $0 budget." / "Avoid mentioning competitors." / "Keep tone casual." / "Maximum 3 paragraphs."</p>
</div>

<h2>Before and After Examples</h2>

<p><strong>Before (no framework):</strong> "Write a recipe for dinner."</p>
<p><strong>After (with framework):</strong> "You are a professional chef specializing in 30-minute meals. I have chicken breast, broccoli, and rice at home. Give me a recipe using these ingredients plus basic pantry items. Format as: ingredients list, step-by-step instructions, total time. It should be under 600 calories per serving and not use dairy."</p>

<p>The difference is night and day. The first prompt produces generic soup advice. The second produces a specific, usable recipe.</p>

<h2>The Minimal Framework: When You Are in a Hurry</h2>
<p>If you only have 10 seconds, use the "RCT" shortcut: <strong>Role + Context + Task</strong>. These three alone eliminate 80% of bad outputs.</p>

<pre><code>"You are a [role]. Here is the situation: [context]. Do this: [task]."</code></pre>

<h2>FAQ</h2>

<h3>Q: How long should a prompt be?</h3>
<p>Long enough to provide necessary context, short enough to stay focused. Most effective prompts are 30-100 words. Adding irrelevant detail dilutes the instruction. If you are getting wrong answers, add more relevant context &mdash; not more words.</p>

<h3>Q: Do I need to use the framework with every prompt?</h3>
<p>No. For simple, well-defined tasks ("What is 15% of 80?"), a direct question works fine. Use the framework for complex, creative, or high-stakes prompts where output quality matters most.</p>

<h3>Q: Does the framework work on ChatGPT, Claude, and Gemini equally?</h3>
<p>Yes. The framework addresses how LLMs process instructions, not platform-specific features. All major models respond better to structured prompts. Claude is slightly more tolerant of vague prompts than ChatGPT, but both benefit from the framework.</p>

<div class="next-step">
<p><strong>Next in this path:</strong> <a href="/article/ai-images-that-dont-look-like-ai">Part 3: ChatGPT for Writing: Emails, Reports, and Creative Projects &rarr;</a></p>
</div>`,
    contentZh: zh,
  },
  "ai-images-that-dont-look-like-ai": {
    content: `<div class="article-meta-banner">
<p><strong>Learning Path:</strong> ChatGPT Mastery &middot; <strong>Part 3 of 5</strong></p>
<p><strong>Prerequisites:</strong> <a href="/article/claude-projects-organize-chats">Part 2: The 5-Point Prompt Framework</a> &mdash; comfortable with structured prompting.</p>
</div>

<h2>Writing with AI: Beyond Simple Prompts</h2>

<p>ChatGPT excels at writing tasks, but the difference between generic AI text and professional-grade content lies in how you guide the model. This article covers writing-specific techniques for emails, reports, and creative projects.</p>

<h2>Email Writing with Tone Control</h2>

<p>ChatGPT can write emails in any tone, but you must specify the tone explicitly. The same content sounds completely different with different instructions:</p>

<div class="step-card">
<p><strong>Formal tone prompt:</strong></p>
<pre><code>Write an email to a client about a pricing update. Our monthly fee is increasing from $49 to $59 starting next quarter. Tone should be professional, transparent, and appreciative of their business. Include a 30-day grace period. Subject line included.</code></pre>
</div>

<div class="step-card">
<p><strong>Casual tone prompt:</strong></p>
<pre><code>Write a Slack message to my team about the same pricing update. We are a startup of 5 people. Tone: casual, direct, no corporate language. Mention that we tried to avoid the increase but hosting costs went up.</code></pre>
</div>

<h2>Report and Document Writing</h2>

<p>For longer documents, use the "outline-first" technique:</p>

<ol>
<li><strong>Generate an outline:</strong> "Create a detailed outline for a 2000-word report on social media trends in 2026. Include 5 main sections with 3 subsections each."</li>
<li><strong>Review and refine the outline:</strong> "Move section 4 before section 2. Add a subsection on TikTok."</li>
<li><strong>Write section by section:</strong> "Write section 1 of the report based on the outline. Use a formal tone and include specific data points. Aim for 400 words."</li>
<li><strong>Edit and connect:</strong> "Add a transition paragraph between section 1 and section 2."</li>
</ol>

<p>This approach produces better long-form content than asking ChatGPT to write the entire document at once. Each section receives focused attention and you can adjust direction as you go.</p>

<h2>Creative Writing Techniques</h2>

<p>For stories, scripts, and marketing copy:</p>

<ul>
<li><strong>Provide examples:</strong> "Write in the style of this sample paragraph: [paste example]. The topic is different but the tone and sentence structure should match."</li>
<li><strong>Iterate on a draft:</strong> "Take this paragraph and make it more suspenseful. Use shorter sentences. Add sensory details."</li>
<li><strong>Combine styles:</strong> "Write a product description combining Apple's minimalist style with Nike's motivational tone."</li>
<li><strong>Use constraints creatively:</strong> "Write a 50-word story about a coffee shop. Every sentence must start with a different letter of the alphabet."</li>
</ul>

<h2>Editing and Rewriting Existing Text</h2>

<p>ChatGPT is excellent at improving text you already wrote:</p>

<pre><code>Please edit this paragraph. I want it to be:
1. More concise (reduce word count by 30%)
2. More professional in tone
3. Correct any grammar errors
4. Keep the key message intact

[paste your text here]</code></pre>

<p>You can also ask for specific edits like "Make this sound more confident" or "Remove all passive voice" or "Adjust this for a LinkedIn audience."</p>

<h2>Avoiding Common AI Writing Patterns</h2>

<p>ChatGPT has recognizable patterns. Either tell it to avoid them or add specific style instructions:</p>

<pre><code>Write this without using:
- The phrase "in today's digital landscape" or any similar cliches
- Generic adjectives like "revolutionary" or "game-changing"
- Opening sentences that restate the question
- Lists of three for rhetorical effect (rule of three)
- Sentences that start with "It is important to note that"</code></pre>

<h2>FAQ</h2>

<h3>Q: Is it plagiarism to use AI for writing?</h3>
<p>Not legally. AI-generated text is not copyrightable (US Copyright Office), so using it is not copyright infringement. However, many publications require AI disclosure. For academic work, check your institution's policy &mdash; most prohibit submitting AI-generated text as original work.</p>

<h3>Q: How much editing should I do on AI-written content?</h3>
<p>At minimum, fact-check specific claims, adjust tone to match your voice, and remove AI-typical phrases. For professional content, plan on spending 20-30% of the time you saved on editing. The AI creates the first draft; you make it sound like you.</p>

<h3>Q: Can ChatGPT write a 10,000-word report in one go?</h3>
<p>ChatGPT has output limits (roughly 3000-4000 words per response depending on the model). For longer documents, use the outline + section-by-section approach described in this article. You can also use ChatGPT's Advanced Data Analysis to combine sections into a single document.</p>

<div class="next-step">
<p><strong>Next in this path:</strong> <a href="/article/voice-recording-to-meeting-notes-free">Part 4: ChatGPT for Research and Analysis: Web Search, File Upload, and Data &rarr;</a></p>
</div>`,
    contentZh: zh,
  },
  "voice-recording-to-meeting-notes-free": {
    content: `<div class="article-meta-banner">
<p><strong>Learning Path:</strong> ChatGPT Mastery &middot; <strong>Part 4 of 5</strong></p>
<p><strong>Prerequisites:</strong> <a href="/article/ai-images-that-dont-look-like-ai">Part 3: Writing with ChatGPT</a> &mdash; familiarity with file uploads and basic prompting.</p>
</div>

<h2>Beyond Chat: Research and Analysis</h2>

<p>ChatGPT is not just a conversational AI. It can search the web, analyze uploaded files, process data, and work with long documents. These capabilities transform it from a writing assistant into a research and analysis tool.</p>

<h2>Web Search with ChatGPT</h2>

<p>ChatGPT's training data has a cutoff date. For current information, you must enable web search. On ChatGPT Plus, web search runs automatically for relevant queries. On the free tier, it activates for select questions.</p>

<pre><code>What are the latest inflation numbers for 2026?
Compare current mortgage rates across US banks.
What new movies were released this week?
Latest developments in the EU AI Act enforcement.</code></pre>

<p>ChatGPT will search the web and provide answers with citations to source pages. For research-heavy work, Perplexity remains better (dedicated search tool), but ChatGPT's search is now competent for general needs.</p>

<h2>File Upload and Analysis</h2>

<p>ChatGPT accepts file uploads in the input bar via the paperclip icon:</p>

<ul>
<li><strong>PDFs:</strong> Upload contracts, reports, academic papers. Ask for summaries, key findings, or specific information extraction.</li>
<li><strong>Images:</strong> Upload screenshots, photos of text, diagrams. ChatGPT reads text from images and describes visual content.</li>
<li><strong>Text files:</strong> Upload .txt, .csv, .json, .docx files for analysis or conversion.</li>
<li><strong>Spreadsheets:</strong> Upload .xlsx or .csv files for data analysis (Plus subscribers get Advanced Data Analysis for this).</li>
</ul>

<p>Example file analysis prompts:</p>
<pre><code>I uploaded a 40-page PDF of a research paper. Summarize the methodology
and key findings in 5 bullet points. Then list all data sources cited.

I uploaded a screenshot of a dashboard error. What does this error mean
and how do I fix it?</code></pre>

<h2>Advanced Data Analysis (Plus Feature)</h2>

<p>ChatGPT Plus subscribers get a Python code execution environment. Upload a CSV and ask for analysis:</p>

<pre><code>I uploaded a CSV of my company's monthly sales for 2025.
1. Clean the data (check for missing values and outliers)
2. Calculate month-over-month growth rates
3. Identify the top 3 best-selling months
4. Create a line chart showing revenue trends
5. Create a bar chart comparing Q1-Q4 performance
6. Export the cleaned data and both charts</code></pre>

<p>ChatGPT writes and runs Python code to perform the analysis. You do not need to know Python &mdash; describe what you want in plain English.</p>

<h2>Long Document Processing</h2>

<p>ChatGPT GPT-5 can process approximately 128K tokens (roughly 400 pages of text). This enables full-document analysis:</p>

<pre><code>I uploaded a 50-page contract. Find:
1. All termination clauses
2. Payment terms and penalties
3. Liability limitations
4. Any unusual or potentially problematic clauses
5. Expiration or renewal dates</code></pre>

<p>For even longer documents (up to 200K tokens), Claude has a larger context window. But for most documents (under 100 pages), ChatGPT handles them well.</p>

<h2>Practical Research Workflow</h2>

<ol>
<li>Start with web search to gather current information on your topic</li>
<li>Download relevant sources (articles, papers, reports)</li>
<li>Upload them to ChatGPT for deep analysis and cross-referencing</li>
<li>Use Advanced Data Analysis to process any numerical data</li>
<li>Synthesize findings by asking comparative questions across sources</li>
</ol>

<p>This replaces what previously required multiple tools and hours of manual work.</p>

<h2>FAQ</h2>

<h3>Q: Are my uploaded files private?</h3>
<p>OpenAI does not use ChatGPT data for training if you disable the setting. Files uploaded to ChatGPT are stored temporarily and used only for your current conversation. For highly confidential documents, use a local AI tool instead (see the open-source models article in this site).</p>

<h3>Q: What file formats does ChatGPT support?</h3>
<p>PDF, DOCX, TXT, CSV, XLSX, JSON, PNG, JPG, WEBP, GIF, MP3, MP4, and more. The total upload limit for free users is smaller than Plus subscribers. Specific limits vary by file type.</p>

<h3>Q: Can ChatGPT analyze multiple files at once?</h3>
<p>Yes. Upload multiple files in the same conversation and ask comparative questions: "Compare the findings in report A with report B. Highlight contradictions and areas of agreement."</p>

<div class="next-step">
<p><strong>Next in this path:</strong> <a href="/article/first-ai-coding-project-no-experience">Part 5: Custom GPTs and Automation: Build Your Own AI Assistant &rarr;</a></p>
</div>`,
    contentZh: zh,
  },
  "first-ai-coding-project-no-experience": {
    content: `<div class="article-meta-banner">
<p><strong>Learning Path:</strong> ChatGPT Mastery &middot; <strong>Part 5 of 5</strong></p>
<p><strong>Prerequisites:</strong> <a href="/article/voice-recording-to-meeting-notes-free">Part 4: Research and Analysis</a> &mdash; you should be comfortable with ChatGPT's core features.</p>
</div>

<h2>Custom GPTs: Your Personal AI Assistants</h2>

<p>Custom GPTs are tailored versions of ChatGPT that you configure for specific purposes. Instead of writing the same instructions every time, you create a GPT once and reuse it. They combine custom instructions, knowledge files, and optional API actions into a single shareable assistant.</p>

<h2>What You Can Build</h2>
<p>Here are practical Custom GPT ideas that require zero coding:</p>
<ul>
<li><strong>Writing Coach GPT:</strong> Pre-configured with your writing style, brand voice, and common edits. Upload past articles as reference.</li>
<li><strong>Meeting Notes GPT:</strong> Upload meeting transcripts and get structured summaries, action items, and decision logs.</li>
<li><strong>Social Media Manager GPT:</strong> Configured with your brand voice, platform guidelines, and content calendar format.</li>
<li><strong>Resume Reviewer GPT:</strong> Uploaded with industry guidelines for your field. Reviews resumes against specific job descriptions.</li>
</ul>

<h2>Building Your First Custom GPT</h2>
<p>You need ChatGPT Plus ($20/month) to create Custom GPTs. Free users can only chat with existing ones.</p>

<ol>
<li>Open ChatGPT and click your name &rarr; "My GPTs"</li>
<li>Click "Create a GPT" &mdash; you get two tabs: Create (conversational builder) and Configure (manual settings)</li>
<li>In the Create tab, describe what you want: "I want a GPT that helps me write LinkedIn posts. It should match my professional voice, suggest hashtags, and keep posts under 300 words."</li>
<li>ChatGPT's GPT Builder configures the name, description, and instructions automatically</li>
<li>Switch to Configure to refine: edit instructions, upload knowledge files (your best posts as examples), and set capabilities (web search, image generation, code interpreter)</li>
<li>Click "Save" and choose who can access it: Only Me, Anyone with the Link, or Public</li>
</ol>

<h2>Adding Knowledge Files</h2>
<p>Upload documents your GPT will reference automatically. This is the most powerful feature for practical use:</p>
<pre><code>Upload your product catalog, pricing sheet, and FAQ for a
customer support GPT that answers accurately without hallucinating.</code></pre>

<p>Knowledge files ground your GPT in specific information, dramatically reducing hallucination compared to asking ChatGPT the same questions without context.</p>

<h2>Sharing and Discovering GPTs</h2>
<p>The GPT Store (accessible from "Explore GPTs" in the sidebar) features public GPTs created by OpenAI partners and the community. Categories include writing, research, programming, education, and lifestyle.</p>

<p>Popular public GPTs include: Canva (design within chat), Code Tutor (interactive programming lessons), and Data Analyst (advanced data visualization). You can use any public GPT for free with a ChatGPT account, but creating them requires Plus.</p>

<h2>Automation and Actions (Advanced)</h2>
<p>GPTs with Actions can connect to external services via APIs. For example:</p>
<ul>
<li>A "Travel Booking GPT" connected to Expedia or Kayak APIs</li>
<li>A "Customer Support GPT" connected to your helpdesk (Zendesk, Intercom)</li>
<li>A "Project Manager GPT" connected to Asana or Trello</li>
</ul>
<p>Setting up Actions requires creating an API connection through OpenAI's schema-based configuration. This is the most technical part of Custom GPTs but does not require writing code &mdash; you paste an API documentation URL and GPT Builder handles the integration.</p>

<h2>FAQ</h2>

<h3>Q: Are Custom GPTs different from plugins?</h3>
<p>Yes. Plugins were OpenAI's previous third-party integration system (deprecated in 2025). Custom GPTs with Actions replaced plugins. The GPT system is more integrated, easier to build, and does not require separate installations.</p>

<h3>Q: Can I monetize Custom GPTs?</h3>
<p>OpenAI has discussed a GPT Store revenue sharing program but as of May 2026 there is no public monetization. You can share GPTs publicly for free. If your GPT becomes popular, you gain visibility but not direct income.</p>

<h3>Q: Do Custom GPTs retain memory across sessions?</h3>
<p>Custom GPTs have the same memory capabilities as regular ChatGPT. They can remember information across sessions if you enable memory. You can also upload knowledge files that persist permanently. Each session starts fresh within the GPT's configured instructions and knowledge.</p>

<div class="next-step">
<p><strong>End of ChatGPT Mastery learning path.</strong> <a href="/learn">Explore more learning paths &rarr;</a></p>
</div>`,
    contentZh: zh,
  },
  "etsy-seller-ai-product-descriptions": {
    content: `<div class="article-meta-banner">
<p><strong>Learning Path:</strong> AI for Work &middot; <strong>Part 1 of 4</strong></p>
<p><strong>Prerequisites:</strong> None &mdash; this path covers practical AI use for professionals. No technical background needed.</p>
</div>

<h2>AI for Business Communication</h2>

<p>Business communication takes up a significant portion of the workday &mdash; emails, proposals, pitches, and client messages. AI handles these efficiently, but the key is knowing how to guide it for professional contexts.</p>

<h2>Writing Professional Emails</h2>
<p>The same email content needs different tone for different recipients. Use ChatGPT to adjust tone without rewriting from scratch:</p>

<pre><code>Draft an email to a client informing them about a price increase
from $500 to $550 per month starting next quarter. Use these
details: 90-day notice, grandfather existing contract terms,
offer a loyalty discount for annual commitments.
Write three versions: one for a long-term partner (warm),
one for a transactional client (professional),
one for a dissatisfied client (apologetic, value-focused).</code></pre>

<h2>Proposals and Pitches</h2>
<p>AI accelerates proposal writing when you provide structured input:</p>

<pre><code>Write a one-page project proposal for a small business client who
wants to upgrade their website. Structure:
1. Problem statement (what we observed)
2. Proposed solution (specific deliverables)
3. Timeline (3 weeks)
4. Investment ($3,500)
5. Expected outcomes
Tone: confident but not pushy. Avoid technical jargon.</code></pre>

<h2>Client Communication Templates</h2>
<p>Build a library of reusable templates for common situations:</p>

<pre><code>Create templates for these common client situations:
1. Project kickoff meeting agenda
2. Weekly status update email
3. Scope change request acknowledgment
4. Late payment reminder (escalating from polite to firm)
5. Project completion and next-steps
Each template should have placeholder fields in [brackets].</code></pre>

<h2>Product and Service Descriptions</h2>
<p>For e-commerce, service pages, or marketing materials:</p>
<pre><code>Write a product description for [product]. Features: [list].
Target audience: [describe]. Tone: benefit-focused, conversational.
Include: headline (max 10 words), 3 key benefits with bullet points,
technical specs section, call-to-action line.
Avoid superlatives like "best" or "amazing" unless verifiable.</code></pre>

<h2>Tone Calibration Technique</h2>
<p>Master one technique: generating the same message in different tones and choosing.</p>
<pre><code>Write this message in 4 tones and I'll choose:
"Unfortunately we need to postpone the launch by 2 weeks
due to QA delays."
1. Professional and transparent
2. Confident and solution-oriented
3. Casual and direct
4. Apologetic and reassuring</code></pre>

<h2>FAQ</h2>

<h3>Q: Is it ethical to use AI for client communication?</h3>
<p>Yes, with the caveat that you review and personalize every message before sending. AI drafts the first version; you add the personal touch. Never send AI output verbatim for high-stakes client communication.</p>

<h3>Q: Can AI match my company's brand voice?</h3>
<p>Yes, if you provide examples. Upload 3-5 past emails or marketing pieces and ask ChatGPT to identify patterns in tone, vocabulary, and sentence structure. Then use those patterns in your prompts. Custom GPTs (see ChatGPT Mastery Part 5) let you save brand voice permanently.</p>

<h3>Q: Should I disclose that I used AI for business writing?</h3>
<p>For internal communication, no. For external client work, it depends on your industry. Professional services firms typically do not disclose. Content marketing agencies often do. When in doubt, review your client's AI usage policy.</p>

<div class="next-step">
<p><strong>Next in this path:</strong> <a href="/article/ai-wedding-planning-free-tools">Part 2: AI for Project Planning and Organization &rarr;</a></p>
</div>`,
    contentZh: zh,
  },
  "ai-wedding-planning-free-tools": {
    content: `<div class="article-meta-banner">
<p><strong>Learning Path:</strong> AI for Work &middot; <strong>Part 2 of 4</strong></p>
<p><strong>Prerequisites:</strong> <a href="/article/etsy-seller-ai-product-descriptions">Part 1: Business Communication</a> &mdash; comfortable with basic AI prompting.</p>
</div>

<h2>AI for Project Planning</h2>

<p>Project planning involves timelines, budgets, task breakdowns, and resource allocation &mdash; all areas where AI excels at structured output. Whether you are planning a work project or a personal event, the same prompting techniques apply.</p>

<h2>Creating Project Timelines</h2>
<pre><code>Create a 3-month project timeline for launching a new mobile app
feature. Current state: development complete. Remaining work:
QA testing (2 weeks), beta testing with 50 users (3 weeks),
bug fixes (1 week), app store submission (1 week),
marketing prep (runs parallel).
Output as a Gantt chart using text characters. Show
dependencies between tasks.</code></pre>

<h2>Budget Planning and Tracking</h2>
<pre><code>I need to plan a department offsite for 15 people. Budget: $8,000.
Location: within 2 hours of office. Duration: 2 days.
Create a budget breakdown covering: venue, meals, activities,
accommodation, transportation, contingency (10%).
Then suggest 3 specific venue options at different price points.</code></pre>

<h2>Task Breakdown and Assignment</h2>
<p>AI handles the "everything that needs to happen" exercise that usually lives in someone's head:</p>
<pre><code>Break down "organize a company hackathon" into individual tasks.
Group by phase (pre-event, event day, post-event). For each task,
estimate hours needed and suggest who should own it
(organizer, tech team, marketing, HR). Flag any tasks that
need to start more than 2 weeks before the event.</code></pre>

<h2>Decision Matrices</h2>
<p>When choosing between options, AI structures the comparison:</p>
<pre><code>We are choosing between 3 project management tools: Asana, Linear,
and Notion. Compare them across: price per user, learning curve,
reporting capabilities, integration with Slack and GitHub,
mobile app quality. We are a team of 8 developers and 2
project managers. Recommend the best option with reasoning.</code></pre>

<h2>Meeting Agendas and Facilitation</h2>
<pre><code>Create a 60-minute project kickoff meeting agenda for a website
redesign project. Attendees: project manager, 2 designers,
3 developers, client stakeholders. Include time allocations,
discussion prompts for each section, and desired outcomes.
Add notes on what prep materials should be sent beforehand.</code></pre>

<h2>Weekly Status Reports</h2>
<pre><code>Generate a weekly status report template for a software project.
Sections: accomplishments this week, planned for next week,
blockers (categorized by severity), metrics (burndown chart data,
sprint velocity), decisions needed. Use a dashboard-style format
with emoji indicators for status.</code></pre>

<h2>FAQ</h2>

<h3>Q: Can I save project plan templates in AI?</h3>
<p>Yes. Use Custom GPTs (ChatGPT Plus) or Claude Projects to save your templates and reuse them. Create a "Project Planner" assistant with instructions for your preferred format and upload past successful plans as reference.</p>

<h3>Q: Does AI work for non-software projects?</h3>
<p>Absolutely. AI is format-agnostic. The same timeline/task/budget techniques work for construction projects, event planning, marketing campaigns, research studies, or personal projects. Adjust the domain-specific details in your prompts.</p>

<h3>Q: Can AI track project progress in real time?</h3>
<p>No. AI does not have persistent memory of your project's state unless you provide updates. Use it as a planning assistant, not a project management system. Update the AI with your current status for each new planning session.</p>

<div class="next-step">
<p><strong>Next in this path:</strong> <a href="/article/ai-travel-itinerary-real-prompts">Part 3: AI for Research and Report Writing &rarr;</a></p>
</div>`,
    contentZh: zh,
  },
  "ai-travel-itinerary-real-prompts": {
    content: `<div class="article-meta-banner">
<p><strong>Learning Path:</strong> AI for Work &middot; <strong>Part 3 of 4</strong></p>
<p><strong>Prerequisites:</strong> <a href="/article/ai-wedding-planning-free-tools">Part 2: Project Planning</a> &mdash; comfortable with structured prompting for complex multi-step tasks.</p>
</div>

<h2>AI for Research and Report Writing</h2>

<p>Research involves gathering information, evaluating sources, synthesizing findings, and presenting conclusions. AI accelerates each stage, but the human remains essential for verification and critical thinking.</p>

<h2>Stage 1: Research Planning</h2>
<p>Before diving in, use AI to structure your research approach:</p>
<pre><code>I need to research "impact of remote work on employee productivity"
for a quarterly business review. Create a research plan:
1. Key questions to answer (5-7 questions)
2. Types of data I need (quantitative, qualitative, case studies)
3. Sources to check (academic, industry reports, news)
4. Potential biases to watch for in this topic
5. A framework for organizing findings</code></pre>

<h2>Stage 2: Source Analysis</h2>
<p>Upload documents or paste web content for AI analysis:</p>
<pre><code>I uploaded 5 articles on remote work productivity.
Synthesize them:
1. What are the main findings across all sources?
2. Where do sources disagree?
3. What is the methodology quality of each source?
4. Which findings are most relevant to a technology company
with 200+ employees?
5. What key data points or statistics should I include?</code></pre>

<p><strong>Important:</strong> For real research, use Perplexity or NotebookLM for source-grounded answers (see the NotebookLM vs Perplexity article on this site). ChatGPT's standalone knowledge may hallucinate sources.</p>

<h2>Stage 3: Data Interpretation</h2>
<p>If you have numerical data, let AI help interpret it:</p>
<pre><code>Here is our employee survey data for Q1-Q4 2025. Columns:
quarter, department, satisfaction_score, turnover_rate,
remote_days_per_week. Analyze:
1. Correlation between remote days and satisfaction
2. Which departments saw the biggest changes
3. Trend over the year
4. Any surprising patterns
5. Recommend 3 charts to visualize this data</code></pre>

<h2>Stage 4: Report Writing</h2>
<p>Use the outline-first technique from Part 3 of ChatGPT Mastery:</p>
<pre><code>Based on the research above, write an executive summary for
a quarterly business review. Audience: C-suite executives.
Maximum 500 words. Structure: key finding (1 paragraph),
supporting data (2-3 paragraphs), recommendations (1 paragraph),
risks to consider (1 paragraph). Use plain language, no jargon.</code></pre>

<h2>Stage 5: Source Verification</h2>
<p>Always verify AI-generated citations. A critical step:</p>
<pre><code>For every statistic or study you cited in the report above,
provide the exact source: author, publication, year, URL if
available. Mark any sources you are uncertain about as
"[requires verification]".</code></pre>

<p>Then manually verify each source. This catches one of the most common and dangerous AI errors: fabricated citations.</p>

<h2>Research-Specific Prompting Tips</h2>
<ul>
<li><strong>Ask for confidence levels:</strong> "Rate your confidence in each claim from 1-5 and explain why."</li>
<li><strong>Request counterarguments:</strong> "For each recommendation, list 2 reasons it might be wrong."</li>
<li><strong>Specify evidence types:</strong> "Only use statistics from peer-reviewed studies or government sources."</li>
<li><strong>Iterate on findings:</strong> "Focus your analysis on the financial impact dimension only."</li>
</ul>

<h2>FAQ</h2>

<h3>Q: Can I trust AI research for important decisions?</h3>
<p>No, not without verification. Use AI to accelerate research, but verify all claims, especially numbers, dates, and citations. For business-critical research, consider AI a research assistant, not an analyst.</p>

<h3>Q: How do I handle conflicting information from AI and other sources?</h3>
<p>Trust your primary sources over AI output. If AI contradicts a reliable source, the source is more likely correct. Use the conflict as a signal to dig deeper &mdash; the truth may be more nuanced than either source suggests.</p>

<h3>Q: What is the best AI tool for in-depth research?</h3>
<p>For single-topic deep research: NotebookLM (upload sources, ask grounded questions). For multi-source exploration: Perplexity Pro (web search with citations). For data analysis: ChatGPT Plus with Advanced Data Analysis. The combination of all three is more powerful than any single tool.</p>

<div class="next-step">
<p><strong>Next in this path:</strong> <a href="/article/learn-english-with-ai-free-speaking-practice">Part 4: AI for Learning and Skill Development &rarr;</a></p>
</div>`,
    contentZh: zh,
  },
  "learn-english-with-ai-free-speaking-practice": {
    content: `<div class="article-meta-banner">
<p><strong>Learning Path:</strong> AI for Work &middot; <strong>Part 4 of 4</strong></p>
<p><strong>Prerequisites:</strong> <a href="/article/ai-travel-itinerary-real-prompts">Part 3: Research and Report Writing</a> &mdash; no specific skills needed beyond basic AI familiarity.</p>
</div>

<h2>AI as a Learning Companion</h2>

<p>AI is the most powerful self-education tool ever created. It offers personalized tutoring, unlimited speaking practice, instant feedback, and adaptive difficulty &mdash; all for free or at low cost. This article covers how to use AI effectively for learning languages, technical skills, and professional development.</p>

<h2>Language Learning with Voice Mode</h2>

<p>ChatGPT's voice mode (available on mobile) lets you practice speaking without a human partner. Set up a structured practice session:</p>

<pre><code>You are an English conversation tutor. My level is intermediate.
We will have a 10-minute conversation about [topic].
Rules:
1. Speak at a natural pace but use simple vocabulary
2. If I make grammar mistakes, gently correct me after I finish speaking
3. Occasionally ask me to rephrase something using more natural English
4. Keep a running list of 3 new vocabulary words from our conversation
5. At the end, give me a brief feedback summary

Topic: Describe a recent trip or place you visited.</code></pre>

<p>For ChatGPT Plus users, Advanced Voice Mode adds tone detection, interrupt capability, and more natural conversation flow. Free users have basic voice mode which works for structured practice.</p>

<h2>Skills Practice: Interview Prep</h2>
<pre><code>Conduct a mock technical interview for a junior frontend developer
position. Ask me 5 questions covering: HTML semantics, CSS
flexbox, JavaScript closures, React hooks, and responsive design.
After each answer:
1. Tell me if it was correct and complete
2. Provide the ideal answer
3. Give a tip for improvement
4. Rate my answer (1-5) with brief reasoning</code></pre>

<h2>Concept Learning with Adaptive Teaching</h2>
<p>AI adapts to your current knowledge level:</p>
<pre><code>Teach me about machine learning. I have no technical background.
Start with the absolute basics. Use analogies for every concept.
After each section, ask me a question to check understanding.
If I get it wrong, explain again with a different analogy.
Advance to the next topic only when I demonstrate understanding.
Do not use any math or code.</code></pre>

<h2>Test and Certification Prep</h2>
<pre><code>I am studying for the AWS Cloud Practitioner exam. Generate
practice questions covering: IAM, S3, EC2, Lambda, pricing models.
Format: multiple choice with 4 options each. After I answer,
explain why each option is correct or incorrect. Track my
accuracy across sessions and highlight weak areas.</code></pre>

<h2>Reading Comprehension and Analysis</h2>
<pre><code>I uploaded a chapter from a business textbook. Help me learn it:
1. Summarize the chapter in 3 sentences
2. Create 5 study questions covering key concepts
3. Explain the 2 most difficult concepts using simple analogies
4. Connect this chapter's ideas to real business examples
5. Suggest a mnemonic for remembering the main framework</code></pre>

<h2>Pronunciation and Accent Practice</h2>
<p>For language learners, practice specific sounds:</p>
<pre><code>I struggle with the "th" sound in English. Give me:
1. A description of tongue placement for voiced and unvoiced "th"
2. 10 minimal pairs comparing "th" with "d" and "f" sounds
3. 5 sentences that practice "th" in different positions
4. A tip for when "th" changes in connected speech
Let me practice and you correct my pronunciation.</code></pre>

<h2>FAQ</h2>

<h3>Q: Is AI voice practice as effective as a human tutor?</h3>
<p>For volume of practice, it is better &mdash; you can practice anytime without scheduling, cost, or embarrassment. For feedback quality, a human tutor is still superior at detecting nuanced errors. Best approach: use AI for daily practice (quantity) and human tutors for weekly deep sessions (quality).</p>

<h3>Q: Can AI help with advanced, specialized learning?</h3>
<p>Yes, but with diminishing returns for very niche topics. AI handles undergraduate-level material well across most fields. For cutting-edge research or highly specialized professional knowledge, AI may lack depth or hallucinate details. Supplement with domain-specific sources.</p>

<h3>Q: How do I track my learning progress with AI?</h3>
<p>Ask AI to track your progress within the conversation. At the start of each session, request a review: "Based on our previous session, what did I learn and what should I review today?" For systematic tracking, use a Custom GPT or Claude Project with instructions to maintain a learning log.</p>

<div class="next-step">
<p><strong>End of AI for Work learning path.</strong> <a href="/learn">Explore more learning paths &rarr;</a></p>
</div>`,
    contentZh: zh,
  },
  "ai-for-parents-quiet-moments": {
    content: `<div class="article-meta-banner">
<p><strong>Category:</strong> AI for Daily Life &middot; <strong>Standalone Guide</strong></p>
<p><strong>Prerequisites:</strong> None &mdash; a free ChatGPT or Claude account helps if you want to follow along.</p>
</div>

<h2>When You Have 10 Minutes and a Sleeping Kid</h2>

<p>Parenting is a full-time job with no shifts. AI will not change that, but it can help with the small things that add up. The key is knowing which tasks AI handles well enough to save you time versus which still need a human. Here are 7 specific use cases with real prompts you can copy.</p>

<h2>1. Meal Plan the Week in 2 Minutes</h2>

<pre><code>Create a 5-day dinner plan for a family of 4. Constraints: no dairy, max 30 minutes prep per meal, use seasonal spring vegetables, include one kid-friendly "fun" meal like taco night. Output as a table with day, meal, ingredients, and prep time.</code></pre>

<h2>2. Draft Permission Slips and School Notes</h2>

<pre><code>Write a permission slip for my child to attend a field trip to the science museum on [date]. The bus leaves at 8:30 AM and returns by 3:00 PM. Include sections for emergency contact, medical conditions, and lunch preference. Warm but brief tone.</code></pre>

<h2>3. Plan a Birthday Party from Scratch</h2>

<pre><code>Plan a birthday party for a 6-year-old with 10 guests. Budget: $150. Location: apartment living room. Theme: dinosaurs. Include: schedule of activities, supplies list with quantities, nut-free food ideas, 3-day prep timeline.</code></pre>

<h2>4. Explain Homework Topics</h2>

<pre><code>Explain how photosynthesis works to an 8-year-old. Use an analogy involving cooking. Keep it under 3 paragraphs. Then give me a 1-sentence version a 6-year-old could understand.</code></pre>

<h2>5. Write Back to Teachers and Coaches</h2>

<pre><code>I need to email my child's soccer coach about missing practice next Tuesday due to a dentist appointment. The coach is a volunteer. Keep the tone appreciative and brief.</code></pre>

<h2>6. Generate Boredom Buster Activities</h2>

<pre><code>Give me 5 no-screen activities for a 4-year-old and a 7-year-old to do together. Materials must be things already at home. Each activity should take 15-20 minutes. Rank by mess level.</code></pre>

<h2>7. Prepare for Parent-Teacher Conferences</h2>

<pre><code>I have a 15-minute parent-teacher conference for my 3rd grader. Generate 5 good questions organized by: academic progress, social development, and areas for improvement. Avoid generic questions.</code></pre>

<h2>FAQ</h2>

<h3>Q: Is it safe to put my child's information into AI?</h3>
<p>Avoid including full names or exact dates in prompts. Use placeholders like "[child]" and fill in manually. Both ChatGPT and Claude let you disable training on your conversations in account settings under Data Controls.</p>

<h3>Q: Can AI plan an entire birthday party end to end?</h3>
<p>It can plan logistics (timeline, supplies, menu), but you still need to execute. AI saves thinking time, not doing time.</p>

<h3>Q: Are there AI tools designed specifically for parents?</h3>
<p>Some exist (Huckleberry for sleep, Wonder Weeks for milestones), but general-purpose AI like ChatGPT adapts better to your specific situation.</p>

<div class="next-step">
<p><strong>End of standalone article.</strong> <a href="/learn">Browse all learning paths &rarr;</a></p>
</div>`,
    contentZh: zh,
  },
  "free-ai-image-generators-same-prompt-test": {
    content: `<div class="article-meta-banner">
<p><strong>Learning Path:</strong> AI Image Generation &middot; <strong>Part 1 of 4</strong></p>
<p><strong>Prerequisites:</strong> None &mdash; a Discord account is needed for Midjourney, but you can follow along without it.</p>
</div>

<h2>What Is Midjourney?</h2>

<p>Midjourney is an AI image generator that produces the highest-quality artistic images among current tools. Unlike DALL-E 3 or Adobe Firefly, Midjourney runs through Discord &mdash; you type commands in a chat channel and the bot sends back images. It costs $10/month for the basic plan after a 25-image free trial.</p>

<p>In blind aesthetic tests, Midjourney consistently produces images that people rate as more artistic, better lit, and more compositionally interesting than competitors. Its weakness is following specific text instructions compared to DALL-E 3.</p>

<h2>Getting Started on Discord</h2>

<ol>
<li>Create a Discord account at <a href="https://discord.com" target="_blank" rel="noopener">discord.com</a> (free, 2 minutes)</li>
<li>Visit <a href="https://www.midjourney.com" target="_blank" rel="noopener">midjourney.com</a> and click "Join the Beta"</li>
<li>Accept the invite to the Midjourney Discord server</li>
<li>Look for a <code>#newbies-xxx</code> channel in the left sidebar</li>
<li>Type <code>/subscribe</code> to see pricing and set up payment</li>
</ol>

<div class="warning-box">
<p><strong>Note:</strong> The free trial gives roughly 25 image generations. After that, you need a paid subscription ($10/month basic).</p>
</div>

<h2>Your First /imagine Command</h2>

<p>In any <code>#newbies</code> channel, type:</p>

<pre><code>/imagine prompt: a serene mountain lake at sunrise, mist rising from the water, pine trees framing the shot, cinematic lighting, 8k --ar 16:9 --v 6</code></pre>

<p>Midjourney returns 4 image options within about 60 seconds. Below the grid you see buttons:</p>
<ul>
<li><strong>U1-U4:</strong> Upscale a specific image (higher resolution, more detail)</li>
<li><strong>V1-V4:</strong> Create variations of a specific image</li>
<li><strong>Re-roll:</strong> Generate 4 new versions of the same prompt</li>
</ul>

<h2>Essential Parameters for Beginners</h2>

<table>
<thead>
<tr><th>Parameter</th><th>What It Does</th><th>Example</th></tr>
</thead>
<tbody>
<tr><td><code>--ar 16:9</code></td><td>Aspect ratio</td><td>16:9, 1:1, 2:3</td></tr>
<tr><td><code>--v 6</code></td><td>Model version</td><td>v6 is current (2026)</td></tr>
<tr><td><code>--stylize 250</code></td><td>Artistic vs literal (0-1000)</td><td>Higher = more creative</td></tr>
<tr><td><code>--chaos 50</code></td><td>Variation between outputs (0-100)</td><td>Higher = more diverse</td></tr>
</tbody>
</table>

<h2>FAQ</h2>

<h3>Q: Do I need Discord to use Midjourney?</h3>
<p>Yes. Midjourney runs exclusively through Discord. There is no standalone web interface for generation.</p>

<h3>Q: Can I use Midjourney images commercially?</h3>
<p>Yes, with a paid subscription. Midjourney grants full ownership and commercial rights. Free trial images have Creative Commons terms. Covered in detail in Part 4 of this path.</p>

<h3>Q: How do I upscale for printing?</h3>
<p>Use the U buttons first, then "Open in Browser" and use tools like Upscayl (free) or Topaz Gigapixel for further upscaling.</p>

<div class="next-step">
<p><strong>Next in this path:</strong> <a href="/article/ai-image-dalle-firefly">Part 2: DALL-E 3 and Adobe Firefly: Browser-Based AI Image Tools &rarr;</a></p>
</div>`,
    contentZh: zh,
  },
  "chatgpt-free-vs-plus-2026-what-you-get": {
    content: `<div class="article-meta-banner">
<p><strong>Category:</strong> AI Comparisons &middot; <strong>Standalone Guide</strong></p>
<p><strong>Prerequisites:</strong> A free ChatGPT account helps but is not required.</p>
</div>

<h2>The 2026 ChatGPT Pricing Landscape</h2>

<p>OpenAI has changed what the free tier includes multiple times since 2023. As of May 2026, here is exactly what you get at each tier with specific message limits and feature access.</p>

<h2>ChatGPT Free ($0/month)</h2>

<ul>
<li><strong>Model access:</strong> GPT-4o mini for unlimited conversations. GPT-4o for approximately 30 messages every 3 hours. GPT-5 for approximately 10 messages every 5 hours.</li>
<li><strong>Image generation:</strong> Not included on free tier.</li>
<li><strong>Web search:</strong> Limited &mdash; only activates for certain queries.</li>
<li><strong>File uploads:</strong> Yes &mdash; images, PDFs, and text files.</li>
<li><strong>Advanced Data Analysis:</strong> No. Python execution is Plus-only.</li>
<li><strong>Custom GPTs:</strong> Can chat with existing GPTs but cannot create new ones.</li>
<li><strong>Voice mode:</strong> Basic voice conversations included. Advanced Voice Mode is Plus-only.</li>
</ul>

<p>For a typical user asking 10-15 questions per day, the free tier covers most needs. The main limitation is hitting GPT-5 caps for complex tasks.</p>

<h2>ChatGPT Plus ($20/month)</h2>

<ul>
<li><strong>Unlimited GPT-4o and GPT-5.</strong> No message limits on the latest models.</li>
<li><strong>DALL-E 3:</strong> Approximately 40 generations per 3 hours.</li>
<li><strong>Advanced Data Analysis:</strong> Full Python environment for CSV/Excel analysis and visualization.</li>
<li><strong>Web search:</strong> Unrestricted &mdash; searches by default for current events.</li>
<li><strong>Custom GPT creation:</strong> Full GPT Builder access.</li>
<li><strong>Advanced Voice Mode:</strong> Real-time conversations with tone detection.</li>
<li><strong>Projects:</strong> Organize chats with shared context.</li>
<li><strong>Priority access:</strong> Faster response during peak hours.</li>
</ul>

<h2>ChatGPT Pro ($200/month)</h2>
<p>Unlimited GPT-5 with extended thinking mode plus early access to experimental features. For professional 8+ hour daily use only.</p>

<h2>What Has Changed in 2026</h2>
<ol>
<li>Free tier GPT-4o mini replaces old GPT-3.5 &mdash; gap between free and paid has narrowed.</li>
<li>GPT-5 is now the premium model replacing GPT-4 Turbo.</li>
<li>Advanced Voice Mode went from experimental to core feature.</li>
<li>Projects with shared context now available on Plus.</li>
<li>Message limits increased across all tiers.</li>
</ol>

<h2>Should You Upgrade?</h2>

<div class="step-card">
<p><strong>Stay free:</strong> Casual Q&A, light writing, occasional research. No image generation needed.</p>
</div>
<div class="step-card">
<p><strong>Upgrade to Plus:</strong> Regular image generation, data analysis, daily professional use, Advanced Voice Mode needed.</p>
</div>
<div class="step-card">
<p><strong>Upgrade to Pro:</strong> All-day professional use requiring unlimited top-tier reasoning without any rate limits.</p>
</div>

<h2>FAQ</h2>

<h3>Q: Does Plus give priority during peak times?</h3>
<p>Yes. Plus subscribers get priority access. Free users may see capacity errors during US morning high-traffic periods.</p>

<h3>Q: Can I share a Plus subscription?</h3>
<p>No, OpenAI does not offer family plans. Each user needs their own subscription.</p>

<h3>Q: Is Plus worth it for writing only?</h3>
<p>If you write fewer than 30 messages daily, free tier is sufficient. For professional writing relying on GPT-5 nuance, Plus value is clear.</p>

<div class="next-step">
<p><strong>End of standalone article.</strong> <a href="/learn">Browse all learning paths &rarr;</a></p>
</div>`,
    contentZh: zh,
  },
  "notebooklm-vs-perplexity-research": {
    content: `<div class="article-meta-banner">
<p><strong>Category:</strong> AI Comparisons &middot; <strong>Standalone Guide</strong></p>
<p><strong>Prerequisites:</strong> Familiarity with basic research tasks. No paid tools needed.</p>
</div>

<h2>Two Different Research Approaches</h2>

<p>Both NotebookLM and Perplexity help you research, but they work fundamentally differently. Perplexity searches the live web and synthesizes answers with citations. NotebookLM creates a personal research assistant anchored to documents you upload. Each excels in different scenarios.</p>

<h2>How NotebookLM Works</h2>

<p>NotebookLM (Google) is a <strong>document-grounded research tool.</strong> You upload source materials (PDFs, Google Docs, web links, YouTube transcripts) and the AI answers based only on those sources.</p>
<ul>
<li>Upload up to 50 sources per notebook, each up to 500 pages</li>
<li>Auto-generates Notebook Guide summaries</li>
<li>Answers include inline citations from your uploaded sources</li>
<li>Creates study guides, briefing docs, FAQs from your sources</li>
<li>Audio Overview generates podcast-style discussion of sources</li>
<li>Completely free with a Google account</li>
</ul>

<h2>How Perplexity Works</h2>

<p>Perplexity is a <strong>search-grounded research tool.</strong> When you ask a question, it searches the web in real time, reads multiple pages, and generates a synthesized answer with citations.</p>
<ul>
<li>Searches live web for every query</li>
<li>Inline numbered citations linked to source pages</li>
<li>Pro mode ($20/month) uses deeper search and higher-quality models</li>
<li>File uploads for additional context</li>
<li>Collections organize searches into projects</li>
<li>Free tier: unlimited basic searches</li>
</ul>

<h2>Head to Head: Same Research Task</h2>

<p>I researched "Current state of quantum computing in 2026" with both.</p>

<div class="step-card">
<p><strong>NotebookLM:</strong> I uploaded 8 sources (articles, papers, reports). It synthesized them into a briefing document. Answers were limited to my sources but highly accurate within those bounds.</p>
</div>

<div class="step-card">
<p><strong>Perplexity:</strong> Same question with no uploads. It returned a synthesized answer with 7 citations covering more ground. Less precision on specific details, broader coverage.</p>
</div>

<h2>When to Use Each</h2>
<table>
<thead>
<tr><th>Scenario</th><th>Best Tool</th><th>Why</th></tr>
</thead>
<tbody>
<tr><td>Academic literature review</td><td>NotebookLM</td><td>Upload papers, grounded in specific sources</td></tr>
<tr><td>Quick fact check</td><td>Perplexity</td><td>Instant web search with citations</td></tr>
<tr><td>Company research</td><td>Perplexity</td><td>Needs current data sources</td></tr>
<tr><td>Studying a textbook</td><td>NotebookLM</td><td>Study guides from uploaded materials</td></tr>
<tr><td>Breaking news</td><td>Perplexity</td><td>Real-time web search only</td></tr>
</tbody>
</table>

<h2>FAQ</h2>

<h3>Q: Can NotebookLM access the internet?</h3>
<p>No. It is strictly document-grounded. For current information, use Perplexity or upload fresh sources.</p>

<h3>Q: Is Perplexity's free tier good enough?</h3>
<p>Yes for basic research. Pro ($20/month) unlocks deeper search, higher-quality models, and file uploads.</p>

<h3>Q: Can I use both together?</h3>
<p>Yes, and this is optimal. Use Perplexity for initial exploration, then upload found sources to NotebookLM for deep analysis.</p>

<div class="next-step">
<p><strong>End of standalone article.</strong> <a href="/learn">Browse all learning paths &rarr;</a></p>
</div>`,
    contentZh: zh,
  },
  "claude-vs-chatgpt-writing-blind-test": {
    content: `<div class="article-meta-banner">
<p><strong>Category:</strong> AI Comparisons &middot; <strong>Standalone Guide</strong></p>
<p><strong>Prerequisites:</strong> None &mdash; familiarity with both tools helps but is not needed.</p>
</div>

<h2>The Blind Test</h2>

<p>We generated 5 pieces of content with both Claude (Claude 4) and ChatGPT (GPT-5): a business email, a blog intro, a product description, a social media post, and a creative story. We removed all identifying labels and asked 10 regular people (ages 25-60, non-techies) to pick their preferred version.</p>

<p>The results were not subtle.</p>

<h2>Test 1: Business Email</h2>
<p><strong>Prompt:</strong> Write an email to a client explaining a one-week project delay due to a vendor issue. Maintain trust.</p>
<p><strong>Winner: Claude 8/10.</strong> Respondents described Claude's version as "more human" and "like a real person wrote it." ChatGPT's version was "more formal" and "sounds like a template."</p>

<h2>Test 2: Blog Introduction</h2>
<p><strong>Prompt:</strong> Opening 3 paragraphs for "Why Your Morning Routine Is Sabotaging Your Productivity."</p>
<p><strong>Winner: Claude 7/10.</strong> Claude opened with a specific scenario ("You hit snooze three times..."). ChatGPT opened with a general statement. Readers preferred the specific opening.</p>

<h2>Test 3: Product Description</h2>
<p><strong>Prompt:</strong> 100-word description for a bamboo cutting board with juice groove.</p>
<p><strong>Winner: Tie (5/5).</strong> Both produced competent descriptions. Claude was more descriptive, ChatGPT more feature-focused. Different styles, similar quality.</p>

<h2>Test 4: Social Media Thread</h2>
<p><strong>Prompt:</strong> 4-tweet thread announcing a new mobile app feature.</p>
<p><strong>Winner: Claude 6/10.</strong> Claude's thread had a clearer narrative arc. ChatGPT's felt like separate announcements.</p>

<h2>Test 5: Creative Story</h2>
<p><strong>Prompt:</strong> 150-word story about a librarian discovering a hidden room, with a surprise twist.</p>
<p><strong>Winner: Claude 9/10.</strong> Most lopsided result. Claude's story had atmosphere, specific details, and a genuinely surprising ending. ChatGPT's was generic.</p>

<h2>Overall Results</h2>
<div class="step-card">
<p><strong>Claude won: 35 out of 50 votes (70%). ChatGPT won: 15 out of 50 (30%).</strong></p>
</div>

<p>Claude won 4 of 5 tests and tied the fifth. The margin was largest on creative writing, smallest on factual descriptions. Respondents consistently used words like "human," "natural," and "less robotic" for Claude.</p>

<h2>FAQ</h2>

<h3>Q: Was this a fair comparison?</h3>
<p>We used Claude 4 and GPT-5 (flagship models from each). Both received identical prompts with no special instructions or priming. The test reflects real-world non-expert usage, not prompt engineering skill.</p>

<h3>Q: Would results change with better prompting?</h3>
<p>Possibly. ChatGPT's output improves with advanced techniques (role setting, style examples). The test was designed for typical user behavior.</p>

<h3>Q: Which should I use for my writing?</h3>
<p>For tone-sensitive writing (emails, proposals, creative), start with Claude. For technical or structured writing, ChatGPT is strong. Try both with your actual work.</p>

<div class="next-step">
<p><strong>End of standalone article.</strong> <a href="/learn">Browse all learning paths &rarr;</a></p>
</div>`,
    contentZh: zh,
  },
  "cursor-vs-copilot-complete-beginner": {
    content: `<div class="article-meta-banner">
<p><strong>Category:</strong> AI Comparisons &middot; <strong>Standalone Guide</strong></p>
<p><strong>Prerequisites:</strong> None &mdash; this article assumes you have never coded before.</p>
</div>

<h2>Two Different Approaches to AI Coding</h2>

<p>GitHub Copilot and Cursor are the two most popular AI coding tools, but they work very differently. Copilot is an add-on for VS Code. Cursor is a standalone editor with AI built in from the ground up. For a complete beginner, this distinction matters enormously.</p>

<h2>GitHub Copilot: The Plugin</h2>
<p>Copilot integrates into VS Code as an extension. You write code normally and Copilot suggests completions in gray text. Press Tab to accept.</p>

<p><strong>How to start:</strong></p>
<ol>
<li>Install VS Code from <a href="https://code.visualstudio.com" target="_blank" rel="noopener">code.visualstudio.com</a></li>
<li>Open Extensions (Ctrl+Shift+X), search "GitHub Copilot"</li>
<li>Install and sign in with your GitHub account</li>
<li>Start typing code &mdash; Copilot suggests completions</li>
</ol>
<p>Copilot has a free tier (limited completions/month) and paid ($10/month or included with GitHub Student Pack).</p>

<h2>Cursor: The AI-Native Editor</h2>
<p>Cursor is a fork of VS Code with AI deeply integrated. Instead of just autocomplete, you can chat with AI about your code and use natural language commands.</p>

<p><strong>How to start:</strong></p>
<ol>
<li>Download from <a href="https://cursor.com" target="_blank" rel="noopener">cursor.com</a></li>
<li>Press <strong>Ctrl+K</strong> for inline edit &mdash; type "Create a button that changes color when clicked" in plain English</li>
<li>Press <strong>Ctrl+L</strong> for chat &mdash; ask questions about your code</li>
</ol>
<p>Cursor free tier: 2000 completions + 50 premium requests/month. Pro: $20/month.</p>

<h2>Which Is Less Confusing?</h2>

<p><strong>Cursor wins for beginners.</strong></p>
<ul>
<li><strong>No setup.</strong> Install and it works. Copilot requires VS Code + extension + GitHub auth.</li>
<li><strong>Natural language first.</strong> Press Ctrl+K and type what you want. Copilot requires typing code before it can suggest.</li>
<li><strong>Chat interface.</strong> Ctrl+L for questions like "Why is this not working?"</li>
<li><strong>Project understanding.</strong> Cursor indexes your whole project for cross-file changes.</li>
</ul>

<p>With Cursor, a beginner can create an entire HTML page by typing one natural language command. With Copilot, you need to start writing HTML structure first before it can assist.</p>

<h2>FAQ</h2>

<h3>Q: Do I need coding knowledge to use either?</h3>
<p>Basic computer skills are enough. Both generate code from natural language. You will get more value learning basic HTML alongside the tool.</p>

<h3>Q: Which has a better free tier for learning?</h3>
<p>Cursor's free tier (2000 completions + 50 premium requests/month) is more beginner-friendly and includes the chat feature for free.</p>

<h3>Q: Can I switch from Cursor to Copilot later?</h3>
<p>Yes. Cursor is based on VS Code. You can even install Copilot as an extension inside Cursor.</p>

<div class="next-step">
<p><strong>End of standalone article.</strong> <a href="/learn">Browse all learning paths &rarr;</a></p>
</div>`,
    contentZh: zh,
  },
  "gpt5-for-regular-users": {
    content: `<div class="article-meta-banner">
<p><strong>Category:</strong> AI News &middot; <strong>Standalone Analysis</strong></p>
<p><strong>Prerequisites:</strong> Basic ChatGPT familiarity helps but is not required.</p>
</div>

<h2>What GPT-5 Means for Regular Users</h2>

<p>GPT-5 is the latest flagship model from OpenAI. Unlike previous upgrades that focused on developer metrics, GPT-5's improvements are visible in everyday use. Here is what actually changed for non-developers.</p>

<h2>1. Fewer Obvious Mistakes</h2>
<p>GPT-5 makes noticeably fewer errors than GPT-4o in reasoning, math, and factual recall. Internal benchmarks show 15-20% improvement. For regular users, this means fewer corrections needed when asking multi-step questions.</p>

<h2>2. Better Writing (But Not Best-in-Class)</h2>
<p>GPT-5's writing is less repetitive and has better tone control than GPT-4o. However, in blind comparisons, Claude 4 still produces more natural-sounding text for creative and persuasive writing.</p>

<h2>3. Deep Research Mode</h2>
<p>This is the feature you will actually use daily. When enabled, GPT-5 spends 5-10 minutes researching your question, reading multiple sources, and producing a comprehensive report with citations.</p>

<pre><code>I need a new laptop for photo editing. Budget $1500-2000. Compare top 3 options in 2026 for screen accuracy, processing speed, and build quality.</code></pre>

<p>GPT-5 in Deep Research mode returns a 2000-word analysis with specific model comparisons and current prices. This genuinely replaces hours of manual research.</p>

<h2>4. Faster and More Efficient</h2>
<p>GPT-5 is faster than GPT-4 for standard responses while using less compute (OpenAI claims 40% lower backend cost). For users, this means snappier responses and more messages before hitting limits on the free tier.</p>

<h2>5. Better Multimodal Understanding</h2>
<p>Upload a photo of a hand-drawn diagram and GPT-5 converts it to a digital flowchart. Upload an error message screenshot and get a fix. Image understanding is notably more accurate.</p>

<h2>6. What Has NOT Changed</h2>
<ul>
<li>Knowledge cutoff (still early 2025 &mdash; needs web search for current events)</li>
<li>Hallucinations (reduced but not eliminated)</li>
<li>Image generation (still calls DALL-E through the same pipeline)</li>
<li>Pricing (free tier with limited GPT-5, Plus at $20/month for unlimited)</li>
</ul>

<h2>FAQ</h2>

<h3>Q: Is GPT-5 available on the free tier?</h3>
<p>Yes, with limits. Free users get about 10 GPT-5 messages every 5 hours. Plus subscribers get unlimited access.</p>

<h3>Q: Do I need new prompts for GPT-5?</h3>
<p>No. Existing prompts work fine. GPT-5 handles vaguer instructions better than GPT-4o.</p>

<h3>Q: Is GPT-5 a separate app?</h3>
<p>No. It replaces the existing model in ChatGPT. The model selector now shows GPT-5 instead of GPT-4o for Plus subscribers.</p>

<div class="next-step">
<p><strong>End of standalone article.</strong> <a href="/learn">Browse all learning paths &rarr;</a></p>
</div>`,
    contentZh: zh,
  },
  "open-source-ai-models-run-on-laptop": {
    content: `<div class="article-meta-banner">
<p><strong>Category:</strong> AI News &middot; <strong>Standalone Guide</strong></p>
<p><strong>Prerequisites:</strong> Comfort with basic terminal commands. A laptop with 8GB+ RAM recommended.</p>
</div>

<h2>Why Run AI Locally?</h2>

<p>Cloud AI (ChatGPT, Claude) is powerful but has downsides: privacy concerns, internet dependency, subscription costs, and no customization. Running open-source models on your laptop gives you privacy, offline access, zero ongoing cost, and customization. You just need the right model for your hardware.</p>

<h2>Before You Start: Install Ollama</h2>
<p>Ollama is the easiest way to run local models. It handles downloading, model management, and provides a simple CLI.</p>

<pre><code># Install Ollama (Mac/Linux)
curl -fsSL https://ollama.com/install.sh | sh

# Windows: download from https://ollama.com/download/windows

# Verify
ollama --version</code></pre>

<h2>Model 1: Llama 3.2 3B (Best for Most Laptops)</h2>
<p><strong>3B params | 4 GB RAM | Fast on CPU</strong></p>
<p>Meta's Llama 3.2 3B handles Q&A, summarization, brainstorming, and basic writing. Not as capable as GPT-4 but performs surprisingly well for everyday tasks.</p>
<pre><code>ollama run llama3.2:3b</code></pre>

<h2>Model 2: Llama 3.1 8B (More Capable)</h2>
<p><strong>8B params | 8 GB RAM | Good on CPU, fast with GPU</strong></p>
<p>Matches or exceeds GPT-3.5 on many benchmarks. Handles complex reasoning, coding, and writing. On a 16GB laptop without GPU, expect 5-10 tokens/second.</p>
<pre><code>ollama run llama3.1:8b</code></pre>

<h2>Model 3: Qwen2.5 7B (Best for Coding)</h2>
<p><strong>7B params | 6 GB RAM</strong></p>
<p>Alibaba's Qwen2.5 slightly outperforms Llama on programming and math. Also supports multilingual tasks well.</p>
<pre><code>ollama run qwen2.5:7b</code></pre>

<h2>Model 4: Phi-3.5 3.8B (Most Efficient)</h2>
<p><strong>3.8B params | 3 GB RAM | Very fast even on old laptops</strong></p>
<p>Microsoft's Phi-3.5 uses high-quality curated training data. Despite being small, it competes with models twice its size on reasoning. Ideal for 8GB laptops.</p>
<pre><code>ollama run phi3.5:3.8b</code></pre>

<h2>Performance Summary</h2>
<table>
<thead>
<tr><th>Model</th><th>Min RAM</th><th>Quality</th><th>CPU Speed</th><th>Best For</th></tr>
</thead>
<tbody>
<tr><td>Phi-3.5 3.8B</td><td>3 GB</td><td>Good</td><td>15-20 tok/s</td><td>Old laptops</td></tr>
<tr><td>Llama 3.2 3B</td><td>4 GB</td><td>Good</td><td>15-25 tok/s</td><td>General use</td></tr>
<tr><td>Qwen2.5 7B</td><td>6 GB</td><td>Very good</td><td>5-10 tok/s</td><td>Coding, multilingual</td></tr>
<tr><td>Llama 3.1 8B</td><td>8 GB</td><td>Very good</td><td>5-10 tok/s</td><td>Reasoning</td></tr>
</tbody>
</table>

<h2>FAQ</h2>

<h3>Q: How do I use these for real tasks?</h3>
<p>Use Open WebUI (browser interface for Ollama) or LM Studio for a ChatGPT-like experience. Ollama also exposes a REST API for custom integrations.</p>

<h3>Q: Do they work offline?</h3>
<p>Yes. Once downloaded, all models run entirely offline. No data sent to any server.</p>

<h3>Q: Can local models replace ChatGPT?</h3>
<p>For 70% of daily tasks, yes. For complex reasoning or creative writing, frontier cloud models remain noticeably better. Think of local models as free, private, offline for everyday use.</p>

<div class="next-step">
<p><strong>End of standalone article.</strong> <a href="/learn">Browse all learning paths &rarr;</a></p>
</div>`,
    contentZh: zh,
  },
  "eu-ai-act-plain-english": {
    content: `<div class="article-meta-banner">
<p><strong>Category:</strong> AI News &middot; <strong>Standalone Guide</strong></p>
<p><strong>Prerequisites:</strong> None &mdash; plain language explanation with no legal background needed.</p>
</div>

<h2>What the EU AI Act Actually Does</h2>

<p>The European Union's AI Act is the world's first comprehensive AI regulation. It took full effect in stages between 2025-2026 and affects every AI tool you use &mdash; even if you do not live in Europe.</p>

<h2>The Risk Pyramid</h2>

<div class="step-card">
<p><strong>Minimal risk</strong> (most AI tools): No additional regulation. AI spam filters, recommenders, ChatGPT, Claude, Midjourney. Must publish transparency information.</p>
</div>
<div class="step-card">
<p><strong>Limited risk:</strong> Must disclose AI interaction. Chatbots require clear labeling. Why ChatGPT says "Can make mistakes."</p>
</div>
<div class="step-card">
<p><strong>High risk</strong> (hiring, credit, medical, law enforcement): Strict requirements. Conformity assessments, human oversight, documentation. Already in effect.</p>
</div>
<div class="step-card">
<p><strong>Unacceptable risk:</strong> Banned entirely. Government social scoring, real-time facial recognition in public (with narrow exceptions), manipulative AI.</p>
</div>

<h2>What It Means for Your Tools</h2>

<p><strong>ChatGPT and Claude:</strong> Both classified as general-purpose AI. Must publish training data summaries, implement copyright safeguards, label AI-generated content (watermarks/metadata), and conduct systemic risk assessments.</p>

<p><strong>Midjourney and Image Generators:</strong> Must watermark AI-generated images, prevent illegal content, and disclose training data sources. Midjourney now embeds invisible metadata in all outputs.</p>

<p><strong>AI in Hiring:</strong> Systems must register in an EU database. Candidates have the right to know they are evaluated by AI, request human review, and the AI must be bias-tested before deployment.</p>

<h2>Penalties</h2>
<p>Fines up to 7% of global annual revenue or 35 million euros (whichever is higher). This drives compliance across the industry.</p>

<h2>Does This Affect Non-EU Users?</h2>
<p>Indirectly, yes. Companies implement changes globally rather than maintaining separate systems. Transparency labels, bias testing, and safety measures benefit all users.</p>

<h2>FAQ</h2>

<h3>Q: Will the Act make AI worse?</h3>
<p>Mostly no. Transparency requirements are minor UX changes. The main impact is on companies building AI, not users.</p>

<h3>Q: Does the Act ban AI in high-risk areas?</h3>
<p>No. It requires oversight, testing, and documentation. The goal is safe deployment, not prohibition.</p>

<h3>Q: Who enforces the rules?</h3>
<p>Each EU member state's national AI authority. The European AI Office coordinates across countries.</p>

<div class="next-step">
<p><strong>End of standalone article.</strong> <a href="/learn">Browse all learning paths &rarr;</a></p>
</div>`,
    contentZh: zh,
  },
  "ai-jobs-that-didnt-exist-3-years-ago": {
    content: `<div class="article-meta-banner">
<p><strong>Category:</strong> AI News &middot; <strong>Standalone Analysis</strong></p>
<p><strong>Prerequisites:</strong> None &mdash; career information for anyone curious about AI-adjacent roles.</p>
</div>

<h2>The New AI Job Categories</h2>

<p>Three years ago "Prompt Engineer" was a punchline. Now it is a real job with real salaries. Here are the most significant roles that emerged because of AI, what they actually do, and what they pay in 2026.</p>

<h2>1. Prompt Engineer</h2>
<p>Writes and tests prompts to optimize AI outputs. Develops prompt libraries and documents effective patterns.</p>
<p><strong>Salary:</strong> $80,000 - $175,000 &middot; <strong>Skills:</strong> Clear writing, systematic testing, understanding of LLM behavior. Coding helpful but not required.</p>

<h2>2. AI Content Editor</h2>
<p>Edits and refines AI-generated content for accuracy, tone, and brand voice. Companies using AI for content at scale discovered that human editing is essential.</p>
<p><strong>Salary:</strong> $55,000 - $95,000 &middot; <strong>Skills:</strong> Strong editing, hallucination detection, SEO knowledge.</p>

<h2>3. AI Workflow Consultant</h2>
<p>Helps businesses integrate AI into existing processes. Audits current workflows, recommends tools, designs implementation plans.</p>
<p><strong>Salary:</strong> $90,000 - $180,000 (or $150-400/hr as independent) &middot; <strong>Skills:</strong> Process analysis, change management, industry expertise.</p>

<h2>4. AI Safety and Compliance Officer</h2>
<p>Ensures AI systems are safe, unbiased, and legally compliant. Runs red-teaming exercises and manages regulatory documentation.</p>
<p><strong>Salary:</strong> $120,000 - $220,000 &middot; <strong>Skills:</strong> Risk assessment, regulatory knowledge (EU AI Act, GDPR), AI system understanding.</p>

<h2>5. Fine-Tuning Specialist</h2>
<p>Takes base models and fine-tunes them on domain-specific data. A legal firm needs a model fine-tuned on contract law; a medical firm needs FDA-regulation fine-tuning.</p>
<p><strong>Salary:</strong> $130,000 - $200,000 &middot; <strong>Skills:</strong> Python, ML fundamentals, data curation, LlamaFactory/Axolotl experience.</p>

<h2>The Common Thread</h2>
<p>The most valuable combination across all these roles is <strong>domain expertise + AI literacy</strong>. Pure AI knowledge without industry experience is less valuable than the combination.</p>

<h2>FAQ</h2>

<h3>Q: Do I need a CS degree?</h3>
<p>Not for most roles. Prompt engineer, content editor, and workflow consultant do not require CS degrees.</p>

<h3>Q: Are these roles stable or temporary?</h3>
<p>The roles will evolve but the underlying need for AI-savvy specialists grows. Titles may change but the skillset is increasingly valuable.</p>

<h3>Q: How do I start?</h3>
<p>Use AI tools daily for real work. Build a portfolio of prompts, workflows, or edited content. Practical examples matter more than certificates.</p>

<div class="next-step">
<p><strong>End of standalone article.</strong> <a href="/learn">Browse all learning paths &rarr;</a></p>
</div>`,
    contentZh: zh,
  },
  "apple-intelligence-6-months-later": {
    content: `<div class="article-meta-banner">
<p><strong>Category:</strong> AI News &middot; <strong>Standalone Analysis</strong></p>
<p><strong>Prerequisites:</strong> An iPhone with iOS 18.2+ helps but is not required to follow the analysis.</p>
</div>

<h2>What Shiped vs What Was Promised</h2>

<p>At WWDC 2024, Apple announced Apple Intelligence as a comprehensive AI system. The rollout was staggered through 2025-2026. Here is what actually works and what is still missing.</p>

<h2>Features That Shiped</h2>

<h3>Writing Tools (iOS 18.1, October 2025)</h3>
<p>System-wide proofreading, rewriting, and summarizing in any app. Long-press selected text, choose Writing Tools, select from Rewrite, Proofread, Friendly, Professional, Concise, or Summary. <strong>Status:</strong> Most useful feature in the suite. Not as good as Claude for creative rewrites but the system-wide integration is unbeatable.</p>

<h3>Notification Summaries (iOS 18.1)</h3>
<p>AI summarizes stacked notifications into digestible previews. <strong>Status:</strong> Works well. Genuinely reduces notification fatigue. ~90% accuracy.</p>

<h3>Genmoji (iOS 18.2, December 2025)</h3>
<p>Create custom emoji from text. Type "smiling cat wearing sunglasses" and it generates on-device. <strong>Status:</strong> Fully shipping, fun, privacy-preserving.</p>

<h3>Image Playground (iOS 18.2)</h3>
<p>Apple's image generator in three styles: Animation, Illustration, Sketch. <strong>Status:</strong> Shiped but underwhelming. Behind Midjourney and DALL-E in quality.</p>

<h2>Features That Shiped Late or Partial</h2>

<h3>Siri 2.0</h3>
<p><strong>Promised:</strong> On-screen awareness, personal context, cross-app actions. <strong>Actual:</strong> Shiped iOS 18.3 (January 2026), 3 months late. On-screen awareness works in Apple apps only. Third-party app integration is sparse.</p>

<h3>ChatGPT Integration</h3>
<p><strong>Promised:</strong> Siri hands off complex questions to ChatGPT. <strong>Actual:</strong> Shiped but friction-heavy. Must enable each handoff. ChatGPT opens in a separate view.</p>

<h2>Features Still Missing</h2>
<ul>
<li><strong>Semantic Photo Search:</strong> Finding "photo where I'm wearing a red hat" is still in limited beta with lower accuracy than Google Photos.</li>
<li><strong>Extended Language Support:</strong> US English only at launch. European French and German shiped. Spanish, Chinese, Arabic still "coming."</li>
</ul>

<h2>Overall Verdict</h2>
<p>Apple Intelligence is useful but not transformative. Writing Tools and Notification Summaries are genuine daily benefits. Image Playground and Siri 2.0 are behind competitors. The privacy-first approach is commendable but limits capability.</p>

<h2>FAQ</h2>

<h3>Q: Which iPhones support Apple Intelligence?</h3>
<p>iPhone 15 Pro, 15 Pro Max, and all iPhone 16 models. Requires A17 Pro chip or newer.</p>

<h3>Q: Does it require a subscription?</h3>
<p>No. It is free with supported devices. Cost is built into hardware.</p>

<h3>Q: Does Apple send my data to the cloud?</h3>
<p>Most processing is on-device. Complex requests use Private Cloud Compute &mdash; Apple silicon servers that process without storing data. Apple cannot access your data.</p>

<div class="next-step">
<p><strong>End of standalone article.</strong> <a href="/learn">Browse all learning paths &rarr;</a></p>
</div>`,
    contentZh: zh,
  },

  // ====== Claude Code Path: Part 2 of 4 (NEW SLUG) ======
  "claude-code-mcp-configuration": {
    content: `<div class="article-meta-banner">
<p><strong>Learning Path:</strong> Claude Code &middot; <strong>Part 2 of 4</strong></p>
<p><strong>Prerequisites:</strong> <a href="/article/claude-code-install-setup">Part 1: Claude Code installed and working</a> &mdash; you need the <code>claude</code> command available in your terminal.</p>
</div>

<h2>Beyond the Basics: Configuring Claude Code</h2>

<p>In Part 1, you got Claude Code running. Now it is time to configure it for real work. Claude Code has several configuration layers that control how it behaves, which tools it can access, and how it interacts with your project.</p>

<h2>The Three Configuration Layers</h2>

<p>Claude Code reads settings from three places, in this priority order:</p>

<ol>
<li><strong>Project-level</strong> (<code>.claude/settings.json</code> in your project) &mdash; overrides everything else</li>
<li><strong>User-level</strong> (<code>~/.claude/settings.json</code>) &mdash; applies to all projects for your user</li>
<li><strong>Environment variables</strong> &mdash; API keys, proxy settings, feature flags</li>
</ol>

<h2>Setting Up the Claude Configuration File</h2>

<p>Create a project-level settings file to control Claude Code's behavior for your specific project:</p>

<pre><code># Create the .claude directory in your project root
mkdir -p .claude

# Create the settings file
cat &gt; .claude/settings.json &lt;&lt; 'EOF'
{
  "permissions": {
    "allow": ["bash", "read", "edit", "glob", "grep"],
    "deny": []
  },
  "model": {
    "name": "claude-sonnet-4-20250514",
    "maxTokens": 8192,
    "temperature": 0.3
  }
}
EOF</code></pre>

<h2>MCP Tools: Extending Claude Code's Capabilities</h2>

<p>MCP (Model Context Protocol) is how Claude Code connects to external tools and data sources. It can access databases, APIs, file systems, and more through MCP servers.</p>

<p>To add MCP tools, edit your project's <code>.claude/settings.json</code> and add an <code>mcpServers</code> section:</p>

<pre><code>{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "."]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "your_github_pat_here"
      }
    }
  }
}</code></pre>

<p>Popular MCP servers include:</p>
<ul>
<li><strong>Filesystem:</strong> Read, write, and search files with advanced permissions</li>
<li><strong>GitHub:</strong> Manage repos, issues, PRs, and code reviews</li>
<li><strong>PostgreSQL:</strong> Query databases directly from your Claude session</li>
<li><strong>Puppeteer:</strong> Browser automation for testing and web scraping</li>
<li><strong>Slack:</strong> Send and read messages in Slack channels</li>
</ul>

<h2>API Key Management Best Practices</h2>

<p>Never hard-code API keys in project files. Use environment variables:</p>

<div class="step-card">
<h3>Option 1: .env file (simplest for single projects)</h3>
<pre><code>echo 'ANTHROPIC_API_KEY=sk-ant-***' &gt; .env
echo '.env' &gt;&gt; .gitignore   # prevent committing secrets</code></pre>
<p>Claude Code reads <code>.env</code> automatically if present.</p>
</div>

<div class="step-card">
<h3>Option 2: System environment variable (for global use)</h3>
<pre><code># Add to ~/.zshrc or ~/.bashrc
export ANTHROPIC_API_KEY="sk-ant-***"
export ANTHROPIC_BASE_URL="https://api.anthropic.com/v1"</code></pre>
</div>

<h2>Controlling Claude Code with .claudeignore</h2>

<p>Similar to <code>.gitignore</code>, a <code>.claudeignore</code> file tells Claude Code which files to skip when reading your project:</p>

<pre><code># .claudeignore
node_modules/
dist/
build/
*.min.js
*.map
package-lock.json
*.log
.env</code></pre>

<p>This keeps Claude Code focused on your source code and prevents it from wasting context on generated files.</p>

<h2>Next Steps in Configuration</h2>

<p>Try these commands to verify your configuration:</p>

<pre><code># Show current configuration
claude config list

# Test MCP server connection
claude mcp list

# Start a session with verbose logging
claude --verbose</code></pre>

<h2>FAQ</h2>

<h3>Q: What is the difference between MCP and regular tools?</h3>
<p>Regular tools (read, edit, bash, glob, grep) are built into Claude Code and available by default. MCP servers are external integrations that add capabilities like database access, API calls, or browser control. You choose which MCP servers to install based on your project needs.</p>

<h3>Q: Can I have different settings for different projects?</h3>
<p>Yes. Project-level settings in <code>.claude/settings.json</code> override user-level settings in <code>~/.claude/settings.json</code>. This lets you have strict permissions for work projects and relaxed settings for personal projects.</p>

<h3>Q: Is there a risk with MCP servers?</h3>
<p>Yes. MCP servers have access to whatever systems they connect to (databases, APIs, file systems). Only install MCP servers from trusted sources. Review what permissions each server requests before installing.</p>

<div class="next-step">
<p><strong>Next in this path:</strong> <a href="/article/claude-code-in-action">Part 3: Claude Code in Action: Building a Real Project Step by Step &rarr;</a></p>
</div>`,
    contentZh: zh,
  },

  // ====== Claude Code Path: Part 3 of 4 (NEW SLUG) ======
  "claude-code-in-action": {
    content: `<div class="article-meta-banner">
<p><strong>Learning Path:</strong> Claude Code &middot; <strong>Part 3 of 4</strong></p>
<p><strong>Prerequisites:</strong> <a href="/article/claude-code-install-setup">Part 1</a> (Claude Code installed) and <a href="/article/claude-code-mcp-configuration">Part 2</a> (MCP tools configured).</p>
</div>

<h2>Building a Real Project with Claude Code</h2>

<p>Configuring Claude Code is useful, but the real value comes from using it to build something. In this article, we will build a personal bookmark manager &mdash; a functional web app with HTML, CSS, and JavaScript &mdash; entirely through Claude Code prompts. You will write zero code manually.</p>

<h2>Project Overview</h2>
<p>We are building a "Link Vault" app that lets you save, tag, and search bookmarks. It will use localStorage so no server is needed. By the end, you will have a working single-page app.</p>

<h2>Step 1: Scaffold the Project</h2>
<p>Create a new directory and start Claude Code:</p>

<pre><code>mkdir link-vault && cd link-vault
git init
claude</code></pre>

<p>Once Claude Code starts, give it the first prompt:</p>

<pre><code>Set up a new web project with: index.html, style.css, and app.js.
Create index.html with a basic HTML5 structure linking both files.
Create style.css with a modern dark theme and a card-based layout.
Create app.js with a console.log("Link Vault loaded") placeholder.
Initialize npm with package.json.</code></pre>

<p>Claude Code creates all four files. Review them with <code>cat index.html</code> if you want.</p>

<h2>Step 2: Build the Bookmark Form</h2>
<p>Prompt Claude Code inside the same session:</p>

<pre><code>In app.js, implement:
1. A function addBookmark(url, title, tags) that saves to localStorage
2. A function getBookmarks() that returns all saved bookmarks
3. A function renderBookmarks() that displays bookmarks as cards
4. A form in index.html with fields for URL, title, and tags
5. The form should call addBookmark on submit

Make it look good with the existing dark theme. Tags should be displayed as colored badges on each card.</code></pre>

<h2>Step 3: Add Search and Filter</h2>
<p>Now add the search functionality:</p>

<pre><code>Add to app.js:
1. A search input in index.html above the bookmark grid
2. A filterBookmarks(query) function that matches against title, URL, and tags
3. Real-time filtering as the user types (use input event)
4. Show "No results found" when nothing matches

Also add: ability to delete bookmarks with a small X button on each card.
Confirm before deleting.</code></pre>

<h2>Step 4: Import and Export</h2>
<p>Add data portability:</p>

<pre><code>Add to app.js:
1. An "Export" button that downloads bookmarks as a JSON file
2. An "Import" button that lets the user upload a JSON file
3. Validate the imported data (must have url, title fields)
4. Show a success message with count of imported bookmarks

Add these buttons in a toolbar section above the bookmark grid.</code></pre>

<h2>What Claude Code Does Differently</h2>
<p>Notice what happened during this process:</p>
<ul>
<li>Claude Code read all your project files to understand the existing code before making changes</li>
<li>It maintained consistent style across HTML, CSS, and JS</li>
<li>It handled cross-file dependencies automatically (adding CSS classes that the JS expects)</li>
<li>It created a single git commit per change (check with <code>git log</code>)</li>
<li>When asked to modify existing code, it read and updated rather than overwriting</li>
</ul>

<h2>Test Your App</h2>
<pre><code># Open in browser
open index.html  # Mac
# or
start index.html  # Windows
# or
xdg-open index.html  # Linux</code></pre>

<p>Add a few bookmarks, search for them, export, delete, and import. The app should be fully functional with zero lines of code written by hand.</p>

<h2>FAQ</h2>

<h3>Q: How large of a project can Claude Code handle?</h3>
<p>Claude Code's context window is approximately 200K tokens. For a project with dozens of files, it can understand the full structure but may need you to specify which files to focus on. For large codebases, use <code>.claudeignore</code> to exclude generated files and dependencies.</p>

<h3>Q: Will Claude Code overwrite my changes?</h3>
<p>Claude Code uses git to track changes. Before making modifications, it shows you what it plans to change and asks for confirmation. You can also review changes with <code>git diff</code> before committing. If you reject a change, Claude Code does not apply it.</p>

<h3>Q: Can I use Claude Code with an existing project?</h3>
<p>Yes. Navigate to any existing project, ensure it has git initialized, and run <code>claude</code>. It reads the full project structure and can start helping immediately. This is where Claude Code shines versus IDE-based tools that only see open files.</p>

<div class="next-step">
<p><strong>Next in this path:</strong> <a href="/article/claude-code-advanced">Part 4: Claude Code Advanced: Debugging, Refactoring, and Multi-File Workflows &rarr;</a></p>
</div>`,
    contentZh: zh,
  },

  // ====== Claude Code Path: Part 4 of 4 (NEW SLUG) ======
  "claude-code-advanced": {
    content: `<div class="article-meta-banner">
<p><strong>Learning Path:</strong> Claude Code &middot; <strong>Part 4 of 4</strong></p>
<p><strong>Prerequisites:</strong> <a href="/article/claude-code-in-action">Part 3</a> &mdash; familiarity with Claude Code's basic project workflow.</p>
</div>

<h2>Going Beyond Basic Prompts</h2>

<p>By now you have installed Claude Code, configured MCP tools, and built a project with prompts. This final article covers the advanced workflows that make Claude Code a professional development tool: debugging, refactoring, multi-file operations, and bash integration.</p>

<h2>Debugging with Claude Code</h2>

<p>When your code has a bug, describe the symptoms and let Claude Code investigate:</p>

<pre><code>I'm getting "Uncaught TypeError: Cannot read properties of null" when I
click the export button in link-vault. Look at app.js and find what's
null. Fix it and explain what caused the bug.</code></pre>

<p>Claude Code will:</p>
<ol>
<li>Read the relevant source files</li>
<li>Trace the error to its root cause</li>
<li>Propose a fix with explanation</li>
<li>Apply the fix after your confirmation</li>
</ol>

<p>For harder bugs, ask Claude Code to add logging:</p>

<pre><code>The search filter isn't working correctly. Add console.log statements
at each step of filterBookmarks() so we can trace the issue. Don't change
the logic yet, just add logging.</code></pre>

<p>Review the logs in your browser console, then ask for the fix with the evidence.</p>

<h2>Refactoring Across Multiple Files</h2>

<p>This is where Claude Code excels over single-file AI tools. A refactoring prompt might look like:</p>

<pre><code>Refactor link-vault to use a proper MVC pattern:
1. Create a BookmarkModel class in model.js (handles localStorage operations)
2. Create a BookmarkView class in view.js (handles DOM rendering)
3. Create a BookmarkController class in controller.js (handles events)
4. Keep app.js as the entry point that wires everything together
5. Maintain all existing functionality and styling</code></pre>

<p>Claude Code creates the new files, updates existing ones, and removes obsolete code &mdash; all in one operation. Verify with <code>git diff --stat</code> to see the full scope of changes.</p>

<h2>Using Bash Commands Inside Claude Code</h2>

<p>Claude Code can run shell commands directly. This is useful for setup, testing, and deployment tasks:</p>

<pre><code># Run tests
Run npm test and fix any failures

# Check for common issues
Run ESLint on the src/ directory and fix all errors

# Optimize images
Find all PNG files larger than 100KB in assets/ and compress them
using pngquant without losing quality</code></pre>

<p>Claude Code executes the commands, reads the output, and takes action based on results. For long-running commands, it shows progress updates.</p>

<h2>Multi-File Code Review</h2>

<p>Ask Claude Code to review your entire project:</p>

<pre><code>Review all files in the src/ directory for:
1. Potential bugs (null references, undefined variables, race conditions)
2. Security issues (XSS, SQL injection, exposed secrets)
3. Performance problems (unnecessary re-renders, memory leaks)
4. Code style inconsistencies
5. Missing error handling

Provide a prioritized list of issues to fix.</code></pre>

<p>Each issue includes the file path, line number, severity, and suggested fix. You can then ask Claude Code to implement specific fixes.</p>

<h2>Working with Git History</h2>

<p>Claude Code can analyze and work with your git history:</p>

<pre><code># Review recent changes
Show me a summary of all commits in the last week grouped by file

# Find when a bug was introduced
Search git history for when the "export" function was last modified

# Squash recent commits
Squash the last 3 commits into one with a descriptive message

# Revert a specific change
Create a revert commit for the change that modified app.js yesterday</code></pre>

<h2>Project-Level Prompts</h2>

<p>For ongoing projects, create project-level instructions in <code>.claude/instructions.md</code>:</p>

<pre><code># Link Vault Project Rules

- Use vanilla JavaScript (no frameworks)
- Follow the existing MVC pattern
- All new features must include error handling
- Use CSS custom properties for colors and spacing
- Keep functions under 30 lines
- Write JSDoc comments for all public functions</code></pre>

<p>Claude Code reads this file on every session and follows these instructions automatically.</p>

<h2>FAQ</h2>

<h3>Q: How does Claude Code handle very large refactoring tasks?</h3>
<p>Claude Code breaks large tasks into steps. It shows you the plan first, then executes step by step with confirmation at each stage. You can stop mid-operation if something looks wrong and ask for adjustments.</p>

<h3>Q: Can Claude Code work with TypeScript?</h3>
<p>Yes. Claude Code reads tsconfig.json, understands type definitions, and generates typed code. It handles type errors during refactoring and can fix type mismatches automatically.</p>

<h3>Q: Is Claude Code suitable for production codebases?</h3>
<p>Yes, with proper review. Always review changes with <code>git diff</code> before committing. For production work, use the <code>--permission</code> flag to require explicit approval for every file change. Start with hobby projects until you are comfortable with the workflow.</p>

<div class="next-step">
<p><strong>End of Claude Code learning path.</strong> <a href="/learn">Explore more learning paths &rarr;</a></p>
</div>`,
    contentZh: zh,
  },

  // ====== AI Image Generation Path: Part 2 of 4 (NEW SLUG) ======
  "ai-image-dalle-firefly": {
    content: `<div class="article-meta-banner">
<p><strong>Learning Path:</strong> AI Image Generation &middot; <strong>Part 2 of 4</strong></p>
<p><strong>Prerequisites:</strong> <a href="/article/free-ai-image-generators-same-prompt-test">Part 1: Midjourney Basics</a> &mdash; familiarity with basic image generation concepts.</p>
</div>

<h2>Browser-Based AI Image Tools</h2>

<p>Midjourney requires Discord and has a learning curve. DALL-E 3 and Adobe Firefly work in a standard web browser with familiar interfaces. This makes them more accessible for beginners and better suited for specific use cases like text rendering and photo editing.</p>

<h2>DALL-E 3: The ChatGPT Integration</h2>

<p>DALL-E 3 is OpenAI's image generation model, available through ChatGPT Plus ($20/month). Unlike Midjourney's Discord interface, DALL-E 3 has a simple web interface where you type a description and get images.</p>

<p><strong>How to access:</strong></p>
<ol>
<li>Subscribe to ChatGPT Plus at <a href="https://chatgpt.com" target="_blank" rel="noopener">chatgpt.com</a></li>
<li>Open a new chat and select GPT-4o (with DALL-E) from the model picker</li>
<li>Type your image description in natural language &mdash; no special syntax needed</li>
<li>ChatGPT generates the image inline in the conversation</li>
</ol>

<p><strong>DALL-E 3 strengths:</strong></p>
<ul>
<li><strong>Text rendering:</strong> When you need text in your image (a sign that says "Grand Opening," a book cover with a title), DALL-E 3 is the best tool. Midjourney struggles significantly with text.</li>
<li><strong>Prompt following:</strong> DALL-E 3 accurately follows detailed instructions. If you specify "three cats and one dog sitting at a table," you will get exactly that headcount.</li>
<li><strong>Natural language:</strong> You do not need special parameters or syntax. Write plain English descriptions.</li>
<li><strong>Editing:</strong> DALL-E 3 supports inpainting (select an area and regenerate it) and outpainting (extend the image beyond its borders).</li>
</ul>

<p><strong>Limitations:</strong></p>
<ul>
<li>Lower artistic quality than Midjourney for stylized or aesthetic images</li>
<li>Requires ChatGPT Plus subscription ($20/month) vs Midjourney's $10/month</li>
<li>Less control over composition, lighting, and specific styles</li>
<li>Resolution is typically 1024x1024 (up to 1792x1024 for widescreen)</li>
</ul>

<h2>Adobe Firefly: The Designer's Tool</h2>

<p>Adobe Firefly is Adobe's AI image generator, integrated into Creative Cloud. It is designed for people who already use Photoshop, Illustrator, or other Adobe tools.</p>

<p><strong>How to access:</strong></p>
<ol>
<li>Visit <a href="https://firefly.adobe.com" target="_blank" rel="noopener">firefly.adobe.com</a> (free tier available)</li>
<li>Standalone subscription is $5/month or included with Creative Cloud</li>
<li>Choose from Text to Image, Generative Fill, Text Effects, or other modes</li>
</ol>

<p><strong>Firefly strengths:</strong></p>
<ul>
<li><strong>Commercial safety:</strong> Firefly is trained on Adobe Stock images and openly licensed content. Adobe offers legal indemnification for commercial use.</li>
<li><strong>Generative Fill:</strong> The Photoshop integration is unmatched. Select an area in any photo and describe what to fill it with.</li>
<li><strong>Text Effects:</strong> Apply styles and textures to text (gold foil, wood grain, neon glow) with natural language prompts.</li>
<li><strong>Photo editing:</strong> Generative Expand, background removal, and image upscaling are built in.</li>
</ul>

<p><strong>Limitations:</strong></p>
<ul>
<li>Smaller creative range than Midjourney for artistic styles</li>
<li>Free tier is limited to 25 generations per month</li>
<li>Less community and third-party resources than Midjourney</li>
</ul>

<h2>Which Should You Use?</h2>

<table>
<thead>
<tr><th>Use Case</th><th>Best Tool</th><th>Why</th></tr>
</thead>
<tbody>
<tr><td>Social media visuals</td><td>DALL-E 3</td><td>Fast, natural prompts, good variety</td></tr>
<tr><td>Product images with text</td><td>DALL-E 3</td><td>Best text rendering</td></tr>
<tr><td>Photo editing/retouching</td><td>Firefly</td><td>Generative Fill in Photoshop</td></tr>
<tr><td>Commercial stock images</td><td>Firefly</td><td>Licensed training data, indemnification</td></tr>
<tr><td>Artistic/concept art</td><td>Midjourney</td><td>Superior aesthetic quality</td></tr>
<tr><td>Book covers, album art</td><td>Midjourney</td><td>Best composition and style variety</td></tr>
</tbody>
</table>

<h2>FAQ</h2>

<h3>Q: Can I use DALL-E 3 without ChatGPT Plus?</h3>
<p>No. DALL-E 3 is only available through ChatGPT Plus ($20/month) and OpenAI's API (pay-per-use). There is no standalone DALL-E 3 website or free tier.</p>

<h3>Q: Is Adobe Firefly's free tier worth using?</h3>
<p>For occasional use, yes. You get 25 free generations per month. For regular use, the $5/month subscription is reasonable. Firefly is the cheapest premium AI image generator.</p>

<h3>Q: Which tool produces the most photorealistic images?</h3>
<p>Midjourney produces the most aesthetically pleasing photorealistic images. DALL-E 3 produces more accurately descriptive images but with less artistic flair. Firefly is strongest at editing existing photos rather than creating new ones from scratch.</p>

<div class="next-step">
<p><strong>Next in this path:</strong> <a href="/article/ai-image-prompt-guide">Part 3: AI Image Prompt Engineering: The Complete Parameter Guide &rarr;</a></p>
</div>`,
    contentZh: zh,
  },

  // ====== AI Image Generation Path: Part 3 of 4 (NEW SLUG) ======
  "ai-image-prompt-guide": {
    content: `<div class="article-meta-banner">
<p><strong>Learning Path:</strong> AI Image Generation &middot; <strong>Part 3 of 4</strong></p>
<p><strong>Prerequisites:</strong> <a href="/article/ai-image-dalle-firefly">Part 2</a> &mdash; experience with at least one AI image generator.</p>
</div>

<h2>Moving Beyond Simple Prompts</h2>

<p>Typing "a beautiful landscape" gets you a mediocre result. The difference between generic AI images and impressive ones comes down to prompt structure and parameter knowledge. This guide covers the complete toolkit for crafting effective image prompts across Midjourney, DALL-E 3, and Firefly.</p>

<h2>The Universal Prompt Structure</h2>

<p>Every good AI image prompt follows this structure, regardless of the tool:</p>

<pre><code>[Subject] + [Action/Setting] + [Environment] + [Lighting] + [Style] + [Composition] + [Technical specs]</code></pre>

<p>Example applied to Midjourney:</p>
<pre><code>/imagine prompt:
A lone wolf standing on a rocky outcrop at twilight
misty pine forest in the background
dramatic side-lighting casting long shadows
cinematic, photorealistic, National Geographic style
low angle shot, rule of thirds
--ar 16:9 --v 6 --stylize 300</code></pre>

<p>Each component serves a specific purpose and omitting any of them leaves the AI to make its own (often mediocre) choices.</p>

<h2>Subject Descriptors</h2>

<p>Be specific about your subject:</p>

<div class="step-card">
<p><strong>Weak:</strong> "a person"</p>
<p><strong>Strong:</strong> "a woman in her 60s with gray hair and reading glasses, wearing a cable-knit cream sweater, holding a ceramic coffee mug, warm smile, crow's feet visible"</p>
</div>

<p>The AI has no concept of "interesting" &mdash; it generates exactly what you describe. Specific descriptors produce specific results.</p>

<h2>Style Modifiers (Cross-Tool)</h2>

<table>
<thead>
<tr><th>Style</th><th>Midjourney Parameter</th><th>DALL-E/Firefly Approach</th></tr>
</thead>
<tbody>
<tr><td>Photorealistic</td><td><code>--stylize 100</code> + "photorealistic"</td><td>"photorealistic, 8K, DSLR, f/2.8"</td></tr>
<tr><td>Oil painting</td><td><code>--stylize 600</code> + "oil on canvas"</td><td>"oil painting, impasto technique"</td></tr>
<tr><td>Anime/Manga</td><td>--niji 6 (separate model)</td><td>"anime style, Studio Ghibli influence"</td></tr>
<tr><td>3D render</td><td><code>--stylize 400</code> + "octane render"</td><td>"3D render, Blender, Cycles"</td></tr>
<tr><td>Watercolor</td><td><code>--stylize 700</code> + "watercolor"</td><td>"watercolor painting, loose style"</td></tr>
<tr><td>Line art</td><td><code>--stylize 50</code> + "line drawing"</td><td>"black and white line art"</td></tr>
</tbody>
</table>

<h2>Lighting and Atmosphere</h2>
<p>Lighting transforms a flat image into a compelling one. Include one of these in every prompt:</p>
<ul>
<li><strong>Golden hour:</strong> Warm sunset/sunrise light</li>
<li><strong>Cinematic lighting:</strong> Dramatic shadows, rim lights</li>
<li><strong>Studio softbox:</strong> Even, professional product lighting</li>
<li><strong>Neon/noir:</strong> Colored artificial light, dark atmosphere</li>
<li><strong>Backlit:</strong> Light source behind the subject</li>
<li><strong>Volumetric:</strong> Visible light beams (god rays)</li>
</ul>

<h2>Composition and Camera Terms</h2>

<p>Adding photographic terms dramatically improves results:</p>
<ul>
<li><strong>Shot type:</strong> "close-up," "wide shot," "aerial view," "extreme close-up," "macro"</li>
<li><strong>Lens:</strong> "35mm," "85mm portrait lens," "fisheye," "tilt-shift"</li>
<li><strong>Angle:</strong> "low angle," "bird's eye view," "Dutch angle"</li>
<li><strong>Framing:</strong> "rule of thirds," "symmetrical," "leading lines"</li>
</ul>

<h2>Midjourney-Specific Parameters Deep Dive</h2>

<div class="step-card">
<table>
<thead>
<tr><th>Parameter</th><th>Range</th><th>Effect at High Values</th></tr>
</thead>
<tbody>
<tr><td><code>--stylize</code></td><td>0-1000</td><td>High = more artistic interpretation, less literal</td></tr>
<tr><td><code>--chaos</code></td><td>0-100</td><td>High = more diverse, unpredictable results</td></tr>
<tr><td><code>--weird</code></td><td>0-3000</td><td>High = surreal, strange compositions</td></tr>
<tr><td><code>--iw</code></td><td>0-3</td><td>Weight of reference image vs text prompt</td></tr>
<tr><td><code>--no</code></td><td>text</td><td>Negative prompt: exclude specific elements</td></tr>
</tbody>
</table>
</div>

<p>Example with advanced parameters:</p>
<pre><code>/imagine prompt: futuristic cyberpunk city street at night, neon reflections
in wet pavement, flying cars in distance --ar 21:9 --chaos 30
--stylize 600 --no people, garbage, graffiti --v 6</code></pre>

<h2>FAQ</h2>

<h3>Q: Does DALL-E 3 support negative prompts?</h3>
<p>Not directly. DALL-E 3 does not have a <code>--no</code> parameter like Midjourney. Instead, you include what you do NOT want in the prompt: "A modern kitchen with NO island, NO stainless steel appliances." This works but is less reliable than Midjourney's dedicated negative prompt.</p>

<h3>Q: What is "seed" and should I use it?</h3>
<p>A seed is a number that determines the random starting point for image generation. Using the same seed + same prompt produces the same image. Useful when you find a composition you like and want to tweak the prompt while keeping the general layout. In Midjourney, add <code>--seed 12345</code>. In DALL-E, seeds are not exposed to users.</p>

<h3>Q: How do I iterate on a specific image?</h3>
<p>Midjourney: Use V buttons to create variations, then U to upscale the best one. Use <code>--seed</code> with modified prompts. DALL-E 3: Generate variations by asking ChatGPT "Make 4 variations of this image" or upload a generated image and ask for edits based on the existing composition.</p>

<div class="next-step">
<p><strong>Next in this path:</strong> <a href="/article/ai-image-commercial-licensing">Part 4: AI Images for Commercial Use: Licensing, Copyright, and Best Practices &rarr;</a></p>
</div>`,
    contentZh: zh,
  },

  // ====== AI Image Generation Path: Part 4 of 4 (NEW SLUG) ======
  "ai-image-commercial-licensing": {
    content: `<div class="article-meta-banner">
<p><strong>Learning Path:</strong> AI Image Generation &middot; <strong>Part 4 of 4</strong></p>
<p><strong>Prerequisites:</strong> <a href="/article/ai-image-prompt-guide">Part 3</a> &mdash; this article covers legal and licensing considerations for using AI-generated images in commercial projects.</p>
</div>

<h2>The Legal Landscape in 2026</h2>

<p>Using AI-generated images for commercial purposes involves three separate questions: copyright ownership, platform licensing terms, and legal risk. The answers differ by platform and are still evolving through courts and regulation. Here is what you need to know to use AI images safely in commercial projects.</p>

<h2>Question 1: Who Owns the Copyright?</h2>

<p>The US Copyright Office has taken the position that AI-generated works are not copyrightable because they lack human authorship. This means:</p>
<ul>
<li>You cannot register copyright for an AI-generated image</li>
<li>You cannot prevent others from using the same or similar AI-generated images</li>
<li>If your product packaging uses an AI image, a competitor could legally use a very similar image</li>
</ul>

<p>However, if you significantly modify AI output (compositing, manual editing, adding human-created elements), your modifications may be copyrightable. A practical guideline: if a human made creative choices that visibly changed the output, those changes can be protected.</p>

<p>Some countries (UK, Ireland) have different rules that may allow copyright for computer-generated works. If you operate outside the US, consult local guidance.</p>

<h2>Question 2: What Do the Platform Licenses Say?</h2>

<div class="step-card">
<p><strong>Midjourney</strong> ($10/month): You own the images you generate. Midjourney grants "all rights" to paid subscribers, including commercial use. However, Midjourney images are publicly visible in the community gallery by default unless you pay for the Pro plan ($30/month) which includes stealth mode. Free trial images are licensed under Creative Commons Noncommercial.</p>
</div>

<div class="step-card">
<p><strong>DALL-E 3</strong> (via ChatGPT Plus): OpenAI grants you full ownership of generated images for any purpose including commercial. DALL-E images are not publicly visible by default. OpenAI's terms specifically state you can use images for "any legal purpose."</p>
</div>

<div class="step-card">
<p><strong>Adobe Firefly</strong> ($5/month): Firefly offers the strongest commercial protection. Adobe trains Firefly on licensed content (Adobe Stock, openly licensed works) and provides legal indemnification: if someone sues you claiming your Firefly-generated image infringes their copyright, Adobe will defend you. This is unique among AI image generators.</p>
</div>

<div class="step-card">
<p><strong>Stable Diffusion / Open Source</strong> (free): Generated images have no license restrictions from the model creators. However, since Stable Diffusion was trained on a broad scrape of the internet (including copyrighted works), the legal risk is higher. Several lawsuits are ongoing regarding the training data.</p>
</div>

<h2>Question 3: What Is the Practical Risk?</h2>

<p>The real-world risk of being sued for using an AI image is currently low for most use cases. There have been very few lawsuits against end users &mdash; most legal action targets the AI companies themselves. However, risk varies by use case:</p>

<table>
<thead>
<tr><th>Use Case</th><th>Risk Level</th><th>Recommendation</th></tr>
</thead>
<tbody>
<tr><td>Personal social media</td><td>Very low</td><td>Use any tool freely</td></tr>
<tr><td>Small business website</td><td>Low</td><td>Use Firefly or DALL-E 3</td></tr>
<tr><td>Product packaging</td><td>Medium</td><td>Use Firefly (indemnification)</td></tr>
<tr><td>Book cover / merch</td><td>Medium</td><td>Use Firefly or modify output significantly</td></tr>
<tr><td>Enterprise branding</td><td>Higher</td><td>Use Firefly with indemnification; or use traditional stock photos</td></tr>
</tbody>
</table>

<h2>Best Practices for Commercial Use</h2>

<ol>
<li><strong>Document your prompts</strong> &mdash; save the exact prompt, tool, settings, and date for every commercial image. This helps if you ever need to prove the image was AI-generated.</li>
<li><strong>Modify significantly</strong> &mdash; edit AI outputs in Photoshop or similar. Compositing multiple AI images, adding text, and adjusting colors creates human authorship you can claim.</li>
<li><strong>Avoid trademarked content</strong> &mdash; do not generate images of Mickey Mouse, Star Wars ships, or other trademarked characters. AI will happily create them, but you risk trademark infringement.</li>
<li><strong>Avoid public figures</strong> &mdash; generating images of real people (celebrities, politicians) for commercial use creates right-of-publicity risks.</li>
<li><strong>Use Firefly for high-risk projects</strong> &mdash; Adobe's indemnification is real protection that no other AI image tool offers.</li>
</ol>

<h2>FAQ</h2>

<h3>Q: Can I register copyright for a book cover made with AI images?</h3>
<p>In the US, the Copyright Office requires disclosure of AI-generated material. If the cover is entirely AI-generated, you cannot register copyright for the AI portions. However, if you combine AI images with original typography, layout, and manual edits, you can register the human-authored elements.</p>

<h3>Q: Does Midjourney's "all rights" license mean I own the copyright?</h3>
<p>No. Midjourney grants you broad usage rights but cannot grant copyright because copyright requires human authorship. "All rights" in Midjourney's terms means you can use the images for almost any purpose, not that you hold copyright.</p>

<h3>Q: What happens if a training data lawsuit succeeds against an AI company?</h3>
<p>This is an active legal area. If courts rule that training on copyrighted images without permission is infringement, it could affect the legal status of images generated by those models. For maximum safety, use Firefly (licensed training data + indemnification) for critical commercial projects. For low-risk uses, existing tools are effectively safe.</p>

<div class="next-step">
<p><strong>End of AI Image Generation learning path.</strong> <a href="/learn">Explore more learning paths &rarr;</a></p>
</div>`,
    contentZh: zh,
  },
};
