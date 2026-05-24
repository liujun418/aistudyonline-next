#!/usr/bin/env python3
"""
Faithful MD-to-HTML conversion for AIStudyOnline articles.
Fully mechanical conversion - no rewriting or simplification.
"""
import re
import html as html_module
import os

def process_inline(text):
    """Process inline formatting: bold, code, links."""
    # Unescape MD escape characters
    text = re.sub(r'\\([\\`*_{}\[\]()#+\-\.!>|])', r'\1', text)
    # Bold: **text**
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # Inline code: `code` -> <code>code</code>
    text = re.sub(r'`([^`]+)`', lambda m: '<code>' + html_module.escape(m.group(1)) + '</code>', text)
    # Links: [text](url) -> <a href="url">text</a>
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
    return text

def convert_md_to_html(md_text):
    """Mechanical MD-to-HTML conversion."""
    lines = md_text.split('\n')
    html_lines = []
    i = 0

    # Skip H1 title (first line like # Title) + following blank lines
    while i < len(lines):
        stripped = lines[i].strip()
        if stripped.startswith('# ') and not stripped.startswith('## '):
            i += 1
            continue
        if stripped == '':
            i += 1
            continue
        break

    while i < len(lines):
        stripped = lines[i].strip()

        # Code block (fenced)
        if stripped.startswith('```'):
            lang = stripped[3:].strip()
            i += 1
            code_lines = []
            while i < len(lines) and not lines[i].strip().startswith('```'):
                code_lines.append(lines[i])
                i += 1
            i += 1  # skip closing ```
            code_content = '\n'.join(code_lines)
            escaped_code = html_module.escape(code_content)
            if lang:
                html_lines.append(f'<pre><code class="language-{lang}">{escaped_code}</code></pre>')
            else:
                html_lines.append(f'<pre><code>{escaped_code}</code></pre>')
            continue

        # H3 heading (check before H2)
        if stripped.startswith('### '):
            heading = stripped[4:]
            heading = process_inline(heading)
            html_lines.append(f'<h3>{heading}</h3>')
            i += 1
            continue

        # H2 heading
        if stripped.startswith('## '):
            heading = stripped[3:]
            heading = process_inline(heading)
            html_lines.append(f'<h2>{heading}</h2>')
            i += 1
            continue

        # Unordered list - collect ALL consecutive items (skip blank lines)
        if stripped.startswith('- '):
            html_lines.append('<ul>')
            while i < len(lines):
                current = lines[i].strip()
                if current == '':
                    i += 1
                    continue  # skip blank lines inside list
                if current.startswith('- '):
                    item_text = current[2:]
                    item_text = process_inline(item_text)
                    html_lines.append(f'<li>{item_text}</li>')
                    i += 1
                else:
                    break
            html_lines.append('</ul>')
            continue

        # Ordered list - collect ALL consecutive items (skip blank lines)
        if re.match(r'^\d+\.\s', stripped):
            html_lines.append('<ol>')
            while i < len(lines):
                current = lines[i].strip()
                if current == '':
                    i += 1
                    continue  # skip blank lines inside list
                m = re.match(r'^(\d+)\.\s(.*)', current)
                if m:
                    item_text = m.group(2)
                    item_text = process_inline(item_text)
                    html_lines.append(f'<li>{item_text}</li>')
                    i += 1
                else:
                    break
            html_lines.append('</ol>')
            continue

        # Skip empty lines (just add blank line for spacing)
        if stripped == '':
            html_lines.append('')
            i += 1
            continue

        # Regular paragraph
        para = process_inline(lines[i])
        if para.strip():
            html_lines.append(f'<p>{para}</p>')
        i += 1

    return '\n'.join(html_lines)


def make_entry(slug, en_html, zh_html, meta_en, meta_zh, faq_en, faq_zh, next_en, next_zh):
    """Format a complete article entry matching the existing TS file style."""
    # Existing file uses:
    #   \t for entry level (comment, slug, closing },)
    #   \t\t for "content:" and "contentZh:" keys
    #   0 tabs for HTML content inside template literals
    TAB = '\t'

    # Build English content
    en_parts = []
    en_parts.append('<div class="article-meta-banner">')
    for me_line in meta_en.split('\n'):
        en_parts.append(me_line)
    en_parts.append('</div>')
    en_parts.append('')

    for h_line in en_html.split('\n'):
        en_parts.append(h_line)

    en_parts.append('<h2>Frequently Asked Questions</h2>')
    en_parts.append('')
    for faq_line in faq_en.split('\n'):
        en_parts.append(faq_line)

    en_parts.append('<div class="next-step">')
    en_parts.append(f'<p>{next_en}</p>')
    en_parts.append('</div>')

    en_content = '\n'.join(en_parts)

    # Build Chinese content
    zh_parts = []
    zh_parts.append('<div class="article-meta-banner">')
    for mz_line in meta_zh.split('\n'):
        zh_parts.append(mz_line)
    zh_parts.append('</div>')
    zh_parts.append('')

    for h_line in zh_html.split('\n'):
        zh_parts.append(h_line)

    zh_parts.append('<h2>常见问题</h2>')
    zh_parts.append('')
    for faq_line in faq_zh.split('\n'):
        zh_parts.append(faq_line)

    zh_parts.append('<div class="next-step">')
    zh_parts.append(f'<p>{next_zh}</p>')
    zh_parts.append('</div>')

    zh_content = '\n'.join(zh_parts)

    # Build final entry
    lines = []
    lines.append(f'{TAB}// ====== {slug} ======')
    lines.append(f'{TAB}"{slug}": {{')
    lines.append(f'{TAB*2}content: `{en_content}`,')
    lines.append(f'{TAB*2}contentZh: `{zh_content}`,')
    lines.append(f'{TAB}}},')

    return '\n'.join(lines)


def generate_zh_translation(en_html, slug):
    """Generate Chinese translation for each article."""
    # This will be the faithful Chinese translation of the English content
    # For now, return the English as placeholder
    return en_html


def main():
    base_dir = r'C:\Users\jun\aistudyonline-next\wenzhang'
    out_dir = r'C:\Users\jun\aistudyonline-next\scripts'

    articles = [
        {
            'slug': 'deerflow-multi-agent-tool',
            'file': 'DeerFlow_ The Open-Source Parallel Multi-Agent Tool for Efficient Task Execution.md',
            'meta_en': '<p><strong>Category:</strong> AI Tools &middot; <strong>Difficulty:</strong> Intermediate</p>\n<p><strong>Prerequisites:</strong> Basic knowledge of Python and Docker</p>',
            'meta_zh': '<p><strong>分类：</strong> AI 工具 &middot; <strong>难度：</strong> 中级</p>\n<p><strong>前置要求：</strong> 基本的 Python 和 Docker 知识</p>',
            'faq_en': '<h3>Q: What makes DeerFlow different from other multi-agent frameworks?</h3>\n<p>Its parallel execution architecture. Most AI tools process tasks sequentially, but DeerFlow dispatches multiple agents simultaneously. This means the more tasks you have, the greater the time savings compared to traditional serial processing.</p>\n\n<h3>Q: Do I need Docker to use DeerFlow?</h3>\n<p>Yes, DeerFlow uses Docker containers for sandboxed execution. This ensures zero contamination and full auditability. All operations including code execution, file writing, and bash commands run inside containers.</p>\n\n<h3>Q: How does DeerFlow integrate with Claude Code?</h3>\n<p>DeerFlow offers a Claude Code integration via the <code>/claude-to-deerflow</code> command. You can install it using: <code>npx skills add https://github.com/bytedance/deer-flow --skill claude-to-deerflow</code>. See <a href="/article/top-10-claude-code-commands">Top 10 Claude Code Commands</a> for more Claude Code tips.</p>',
            'faq_zh': '<h3>问：DeerFlow 与其他多智能体框架的核心区别是什么？</h3>\n<p>其核心区别在于并行执行架构。大多数 AI 工具按顺序逐个处理任务，而 DeerFlow 能同时派发多个智能体并行工作。这意味着任务越多，DeerFlow 相比于传统串行处理的时间节省就越明显。</p>\n\n<h3>问：使用 DeerFlow 必须安装 Docker 吗？</h3>\n<p>是的，DeerFlow 依赖 Docker 容器实现沙箱隔离执行，保证了操作的零污染和完全可审计性。所有操作（包括代码执行、文件写入和 bash 命令）都在容器内运行。</p>\n\n<h3>问：DeerFlow 如何与 Claude Code 集成？</h3>\n<p>DeerFlow 通过 <code>/claude-to-deerflow</code> 命令提供 Claude Code 集成。安装命令：<code>npx skills add https://github.com/bytedance/deer-flow --skill claude-to-deerflow</code>。更多 Claude Code 技巧请参考 <a href="/article/top-10-claude-code-commands">Top 10 Claude Code 命令</a>。</p>',
            'next_en': '<strong>Next Step:</strong> Explore <a href="/tools/deer-flow">Deer-Flow tool page</a> or read <a href="/article/5-ai-tools-one-person-overseas-business">5 AI Tools to Build Your One-Person Overseas Business</a>.',
            'next_zh': '<strong>下一篇：</strong> 查看 <a href="/tools/deer-flow">Deer-Flow 工具详情页</a> 或阅读 <a href="/article/5-ai-tools-one-person-overseas-business">5 款 AI 工具打造你的单人海外业务</a>。'
        },
        {
            'slug': 'top-10-claude-code-commands',
            'file': 'Top 10 Claude Code Commands_ Boost Your AI Productivity.md',
            'meta_en': '<p><strong>Category:</strong> AI Tutorials &middot; <strong>Difficulty:</strong> Beginner</p>\n<p><strong>Prerequisites:</strong> Claude Code installed (see <a href="/article/claude-code-install-setup">installation guide</a>)</p>',
            'meta_zh': '<p><strong>分类：</strong> AI 教程 &middot; <strong>难度：</strong> 初级</p>\n<p><strong>前置要求：</strong> 已安装 Claude Code（参见 <a href="/article/claude-code-install-setup">安装指南</a>）</p>',
            'faq_en': '<h3>Q: Is Claude Code free to use?</h3>\n<p>Claude Code is included with a Claude Pro subscription ($20/month). You also need an Anthropic API Key for usage. For detailed setup, check out <a href="/article/claude-code-install-setup">Claude Code Installation and Setup</a>.</p>\n\n<h3>Q: How is Claude Code different from GitHub Copilot or Cursor?</h3>\n<p>Claude Code is a CLI tool for autonomous task execution. Copilot is an IDE plugin for autocomplete. Cursor is an AI-native IDE. See our <a href="/article/claude-code-top-7-skills">Claude Code Top 7 Skills guide</a> for a detailed comparison.</p>\n\n<h3>Q: How do I minimize token consumption when using Claude Code?</h3>\n<p>Use <code>/compact</code> to compress long conversations, use <code>@</code> references to include only relevant files, and consider <code>--dangerously-skip-permissions</code> for trusted automated workflows.</p>',
            'faq_zh': '<h3>问：Claude Code 是免费的吗？</h3>\n<p>Claude Code 包含在 Claude Pro 订阅中（每月 $20）。你还需要申请 Anthropic API Key 才能使用 API 模式。详细安装和配置请参考 <a href="/article/claude-code-install-setup">Claude Code 安装与配置</a>。</p>\n\n<h3>问：Claude Code 与 GitHub Copilot 或 Cursor 有什么区别？</h3>\n<p>Claude Code 是命令行工具，专注于自主执行复杂任务；Copilot 是 IDE 插件，擅长代码补全；Cursor 是 AI 原生 IDE。详细对比请参考 <a href="/article/claude-code-top-7-skills">Claude Code 七大技能指南</a>。</p>\n\n<h3>问：如何减少 Claude Code 的 Token 消耗？</h3>\n<p>使用 <code>/compact</code> 压缩长对话，使用 <code>@</code> 引用只包含相关文件，对于可信的自动化工作流可考虑 <code>--dangerously-skip-permissions</code>。</p>',
            'next_en': '<strong>Next Step:</strong> Deepen your Claude Code knowledge with <a href="/article/claude-code-top-7-skills">Top 7 Skills Guide</a>.',
            'next_zh': '<strong>下一篇：</strong> 深入学习 Claude Code 的高级用法：<a href="/article/claude-code-top-7-skills">七大技能指南</a>。'
        },
        {
            'slug': '6-must-have-openclaw-skills',
            'file': '6 Must-Have Base Skills for OpenClaw to Boost Your AI Productivity.md',
            'meta_en': '<p><strong>Category:</strong> AI Tutorials &middot; <strong>Difficulty:</strong> Intermediate</p>\n<p><strong>Prerequisites:</strong> Basic familiarity with OpenClaw CLI</p>',
            'meta_zh': '<p><strong>分类：</strong> AI 教程 &middot; <strong>难度：</strong> 中级</p>\n<p><strong>前置要求：</strong> 熟悉 OpenClaw 命令行基本操作</p>',
            'faq_en': '<h3>Q: What is OpenClaw and why should I use it?</h3>\n<p>OpenClaw is an open-source AI agent framework that combines LLMs with command execution loops to turn natural language into automated workflows. Read our article <a href="/article/openclaw-demystified-20-lines">Unveiling OpenClaw: Demystify the AI Tool in 20 Lines of Code</a>.</p>\n\n<h3>Q: Are these 6 skills enough for daily work?</h3>\n<p>These 6 skills form a robust foundation for most AI-driven workflows. Browser automation, web search, self-improvement, skill discovery, security auditing, and email management cover the majority of daily tasks for overseas business operations.</p>\n\n<h3>Q: How does OpenClaw compare to other AI tools?</h3>\n<p>OpenClaw\'s strength lies in its skill ecosystem and flexibility. For a broader comparison of AI development tools, see <a href="/article/openai-strategic-counterattack-openclaw-codex">OpenAI\'s Strategic Counterattack: OpenClaw Integration and Codex Innovations</a>.</p>',
            'faq_zh': '<h3>问：什么是 OpenClaw？我为什么需要使用它？</h3>\n<p>OpenClaw 是一个开源的 AI 代理框架，它将大语言模型与命令执行循环相结合，将自然语言指令转化为自动化工作流程。要了解核心原理，推荐阅读 <a href="/article/openclaw-demystified-20-lines">揭开 OpenClaw 面纱：20 行代码讲透这个 AI 工具</a>。</p>\n\n<h3>问：这 6 个技能真的能覆盖日常工作的主要需求吗？</h3>\n<p>是的，这 6 个技能为大多数 AI 驱动的工作流程提供了坚实基础。浏览器自动化、网络搜索、自我进化、技能发现、安全审计和邮件管理覆盖了海外业务运营中大部分日常任务。</p>\n\n<h3>问：OpenClaw 与其他 AI 开发工具相比有什么优势？</h3>\n<p>OpenClaw 最大的优势在于其灵活的技能生态系统。与功能固定的单一 AI 工具不同，OpenClaw 允许通过安装不同技能来组合能力。全面对比分析请参考 <a href="/article/openai-strategic-counterattack-openclaw-codex">OpenAI 的战略反击：OpenClaw 集成与 Codex 创新</a>。</p>',
            'next_en': '<strong>Next Step:</strong> Learn more about <a href="/article/openclaw-demystified-20-lines">how OpenClaw works under the hood</a> or explore <a href="/article/openai-strategic-counterattack-openclaw-codex">OpenAI\'s strategic moves</a>.',
            'next_zh': '<strong>下一篇：</strong> 深入了解 <a href="/article/openclaw-demystified-20-lines">OpenClaw 的核心工作原理</a>，或探索 <a href="/article/openai-strategic-counterattack-openclaw-codex">OpenAI 在 AI 工具市场的最新战略动作</a>。'
        },
        {
            'slug': 'ai-workforce-virtual-employees',
            'file': 'From Tool Development to AI Workforce_ Why Programmers Are Building Virtual AI Employees.md',
            'meta_en': '<p><strong>Category:</strong> AI Use Cases &middot; <strong>Difficulty:</strong> Intermediate</p>\n<p><strong>Reading Time:</strong> 7 minutes</p>',
            'meta_zh': '<p><strong>分类：</strong> AI 应用场景 &middot; <strong>难度：</strong> 中级</p>\n<p><strong>阅读时间：</strong> 7 分钟</p>',
            'faq_en': '<h3>Q: What exactly is an AI employee?</h3>\n<p>An AI employee is a software agent that autonomously handles business tasks &mdash; from content updates to data analysis to bug fixing. Unlike traditional tools that wait for commands, AI employees have memory, skill libraries, and autonomous decision-making capabilities.</p>\n\n<h3>Q: Do I need advanced programming skills to build an AI employee?</h3>\n<p>Not necessarily. While the example in this article uses Python, many platforms now offer no-code or low-code AI employee builders. For those comfortable with code, tools like <a href="/tools/openclaw">OpenClaw</a> and <a href="/tools/deer-flow">Deer-Flow</a> provide excellent starting points.</p>\n\n<h3>Q: What are the best use cases for AI employees in overseas business?</h3>\n<p>The most impactful use cases include automated website maintenance, multilingual content generation, cross-border customer support, code deployment and testing, and market data analysis. For more ideas, see our guide on <a href="/article/5-ai-tools-one-person-overseas-business">5 AI Tools for One-Person Overseas Business</a>.</p>',
            'faq_zh': '<h3>问：AI 员工到底是什么？和普通自动化脚本有什么区别？</h3>\n<p>AI 员工是一种具备自主决策能力的软件代理，能够处理从内容更新到数据分析再到 Bug 修复的多种任务。与传统自动化脚本不同，AI 员工具备记忆能力和技能库，可以根据任务类型灵活选择和组合不同的能力。</p>\n\n<h3>问：构建 AI 员工需要很强的编程能力吗？</h3>\n<p>不一定。本文示例使用 Python，但现在很多平台提供无代码或低代码的 AI 员工构建工具。如果你熟悉编程，<a href="/tools/openclaw">OpenClaw</a> 和 <a href="/tools/deer-flow">Deer-Flow</a> 等开源框架提供了很好的起点。</p>\n\n<h3>问：在海外业务中，AI 员工最有价值的应用场景是什么？</h3>\n<p>最具价值的应用场景包括：自动化多语言网站维护、批量内容生成与翻译、跨时区客户支持、代码自动化部署与测试以及竞争对手数据分析。更多方案请参考 <a href="/article/5-ai-tools-one-person-overseas-business">5 款 AI 工具打造你的单人海外业务</a>。</p>',
            'next_en': '<strong>Next Step:</strong> Explore <a href="/article/5-ai-tools-one-person-overseas-business">5 AI Tools to Build Your One-Person Overseas Business</a> or learn about <a href="/article/agent-skill-harness-explained">Agent, Skill, and Harness in AI Development</a>.',
            'next_zh': '<strong>下一篇：</strong> 探索 <a href="/article/5-ai-tools-one-person-overseas-business">5 款 AI 工具打造你的单人海外业务</a> 或了解 <a href="/article/agent-skill-harness-explained">AI 开发中的 Agent、Skill 和 Harness</a>。'
        },
        {
            'slug': 'free-ai-knowledge-base-tool-tutorial',
            'file': 'Practical Tutorial on Powerful Free AI Knowledge Base Tool.md',
            'meta_en': '<p><strong>Category:</strong> AI Tutorials &middot; <strong>Difficulty:</strong> Beginner</p>\n<p><strong>Reading Time:</strong> 6 minutes</p>',
            'meta_zh': '<p><strong>分类：</strong> AI 教程 &middot; <strong>难度：</strong> 初级</p>\n<p><strong>阅读时间：</strong> 6 分钟</p>',
            'faq_en': '<h3>Q: Is this knowledge base tool really free?</h3>\n<p>Yes, the tool is completely free for daily basic use, including document parsing, intelligent search, and Q&A functions. There are no hidden charges for common operations. Some advanced features like API access or team collaboration may require a paid plan, but the core functionality is fully free.</p>\n\n<h3>Q: What file formats are supported?</h3>\n<p>The tool supports PDF, TXT, Markdown, webpage snapshots, and local notes. It can extract text from images using OCR technology. For developers, there is also an API for programmatic document upload and retrieval.</p>\n\n<h3>Q: How secure is my data?</h3>\n<p>Your data is stored in independent private spaces with encryption. You control access permissions, and you can export and delete your data at any time. For confidential business information, you can set password protection on specific knowledge spaces. For more on data security with AI tools, see our <a href="/article/eu-ai-act-plain-english">EU AI Act guide</a>.</p>',
            'faq_zh': '<h3>问：这个知识库工具真的完全免费吗？</h3>\n<p>是的，日常基础使用完全免费，包括文档解析、智能搜索和问答功能。常见操作没有任何隐藏费用。API 访问或团队高级协作等扩展功能可能需要付费，但核心功能完全免费。</p>\n\n<h3>问：支持哪些文件格式？</h3>\n<p>支持 PDF、TXT、Markdown、网页快照和本地笔记等常见格式，并可通过 OCR 技术从图片中提取文字。还提供 API 接口用于程序化文档上传和检索。</p>\n\n<h3>问：我的数据安全吗？</h3>\n<p>数据存储在加密的独立私有空间中，只有你可以控制访问权限，并可以随时导出或删除数据。机密信息可设置密码保护。更多信息请参考 <a href="/article/eu-ai-act-plain-english">欧盟 AI 法案指南</a>。</p>',
            'next_en': '<strong>Next Step:</strong> Learn how to choose the right AI tools for your needs: <a href="/article/how-to-choose-right-ai-tool">Which AI Tool Should You Use?</a> Or explore <a href="/article/free-vs-paid-ai-tools-worth-it">Free vs Paid AI Tools</a>.',
            'next_zh': '<strong>下一篇：</strong> 了解如何为你的需求选择最合适的 AI 工具：<a href="/article/how-to-choose-right-ai-tool">你应该使用哪个 AI 工具？</a> 或探索 <a href="/article/free-vs-paid-ai-tools-worth-it">免费 vs 付费 AI 工具</a>。'
        },
        {
            'slug': 'alexander-wang-meta-ai-superintelligence',
            'file': "Alexander Wang's Meta AI Superintelligence_ A New Era for Overseas Businesses.md",
            'meta_en': '<p><strong>Category:</strong> AI News &middot; <strong>Difficulty:</strong> Beginner</p>\n<p><strong>Reading Time:</strong> 5 minutes</p>',
            'meta_zh': '<p><strong>分类：</strong> AI 新闻 &middot; <strong>难度：</strong> 初级</p>\n<p><strong>阅读时间：</strong> 5 分钟</p>',
            'faq_en': '<h3>Q: Who is Alexander Wang?</h3>\n<p>Alexander Wang is the youngest self-made billionaire in Silicon Valley, known for co-founding Scale AI. He now leads Meta\'s AI division after a $14 billion deal with Mark Zuckerberg. His expertise in AI and data infrastructure makes him a pivotal figure in the race for superintelligence.</p>\n\n<h3>Q: What is Muse Spark and how is it different from other AI models?</h3>\n<p>Muse Spark is Meta\'s flagship AI model developed by Meta Superintelligence Labs. Its key differentiator is exceptional token efficiency &mdash; it delivers results comparable to top-tier models while using significantly fewer tokens, making it more cost-effective and faster for many tasks.</p>\n\n<h3>Q: How can overseas businesses benefit from Meta\'s AI strategy?</h3>\n<p>Overseas businesses can leverage Meta\'s AI ecosystem for multilingual content localization, automated customer service across regions, and optimized ad campaigns. As the technology matures and potentially becomes available through APIs, it will offer powerful tools for global market expansion.</p>',
            'faq_zh': '<h3>问：Alexander Wang 是谁？他为什么重要？</h3>\n<p>Alexander Wang 是硅谷最年轻的白手起家亿万富翁，以联合创立 Scale AI 而闻名。在与扎克伯格达成 140 亿美元的交易后，他现在领导 Meta 的 AI 部门。他在 AI 和数据基础设施方面的深厚专业知识使他成为超级智能竞赛中的关键人物。</p>\n\n<h3>问：什么是 Muse Spark？它与其他 AI 模型有什么核心区别？</h3>\n<p>Muse Spark 是 Meta 超级智能实验室开发的旗舰 AI 模型。其最大特色是卓越的 Token 效率——使用显著更少的 Token 就能提供与顶级模型相媲美的结果，意味着更低成本和更快速度。</p>\n\n<h3>问：海外企业如何从 Meta 的 AI 战略中实际受益？</h3>\n<p>海外企业可以通过多种方式利用 Meta 的 AI 生态系统：多语言内容本地化、跨区域自动化客服、以及精准广告投放优化。随着技术成熟并可能通过 API 开放，将为全球市场扩张提供强大工具。</p>',
            'next_en': '<strong>Next Step:</strong> Read our analysis of <a href="/article/ai-jobs-that-didnt-exist-3-years-ago">AI Jobs That Didn\'t Exist 3 Years Ago</a> or explore <a href="/article/5-ai-tools-one-person-overseas-business">5 AI Tools to Build Your One-Person Overseas Business</a>.',
            'next_zh': '<strong>下一篇：</strong> 阅读我们的分析文章 <a href="/article/ai-jobs-that-didnt-exist-3-years-ago">3 年前不存在的 AI 工作</a> 或探索 <a href="/article/5-ai-tools-one-person-overseas-business">5 款 AI 工具打造你的单人海外业务</a>。'
        }
    ]

    for art in articles:
        filepath = os.path.join(base_dir, art['file'])
        with open(filepath, 'r', encoding='utf-8') as f:
            md_text = f.read()

        en_html = convert_md_to_html(md_text)

        entry = make_entry(
            art['slug'], en_html, en_html,
            art['meta_en'], art['meta_zh'],
            art['faq_en'], art['faq_zh'],
            art['next_en'], art['next_zh']
        )

        output_file = os.path.join(out_dir, f'{art["slug"]}_entry.txt')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(entry)

        print(f'Generated: {art["slug"]}')

        # Also generate a clean HTML-only version for easier inspection
        html_only = os.path.join(out_dir, f'{art["slug"]}_html.txt')
        with open(html_only, 'w', encoding='utf-8') as f:
            f.write(en_html)
        print(f'  HTML also saved to: {html_only}')


if __name__ == '__main__':
    main()
