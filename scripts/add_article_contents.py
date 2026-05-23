import re
import os

articles_path = r"C:\Users\jun\aistudyonline-next\src\lib\article-content.ts"
wenzhang_dir = r"C:\Users\jun\aistudyonline-next\wenzhang"

articles = [
    {
        "slug": "5-ai-tools-one-person-overseas-business",
        "source": "5 AI Tools to Build Your One-Person Overseas Business_ Let Claude Code Work for You While You Sleep.md",
        "next_step_en": "Explore more AI tools for freelancers: <a href=\"/article/ai-for-freelancers\">AI for Freelancers &#x2192;</a>",
        "next_step_zh": "探索更多AI自由职业者工具：<a href=\"/article/ai-for-freelancers\">AI自由职业者指南 &#x2192;</a>",
    },
    {
        "slug": "git-github-beginners-guide",
        "source": "Git & GitHub Beginner's Guide_ Core Concepts & Operation.md",
        "next_step_en": "Learn Claude Code installation and setup: <a href=\"/article/claude-code-install-setup\">Claude Code Install &amp; Setup &#x2192;</a>",
        "next_step_zh": "学习Claude Code安装与配置：<a href=\"/article/claude-code-install-setup\">Claude Code安装与配置 &#x2192;</a>",
    },
    {
        "slug": "openai-strategic-counterattack-openclaw-codex",
        "source": "OpenAI's Strategic Counterattack_ How OpenClaw Integration and Codex Innovations Are Reshaping the AI Developer Landscape.md",
        "next_step_en": "Understand OpenClaw better: <a href=\"/article/openclaw-demystified-20-lines\">OpenClaw Demystified in 20 Lines &#x2192;</a>",
        "next_step_zh": "深入理解OpenClaw：<a href=\"/article/openclaw-demystified-20-lines\">20行代码揭秘OpenClaw &#x2192;</a>",
    },
    {
        "slug": "agent-skill-harness-explained",
        "source": "Practical Explanation of Agent, Skill and Harness in Modern AI Development.md",
        "next_step_en": "Learn 12 core AI concepts: <a href=\"/article/12-core-ai-concepts-guide\">12 Core AI Concepts Guide &#x2192;</a>",
        "next_step_zh": "学习12个核心AI概念：<a href=\"/article/12-core-ai-concepts-guide\">12个核心AI概念指南 &#x2192;</a>",
    },
    {
        "slug": "5-ai-html-hacks-overseas-websites",
        "source": "Unlock Hidden Potentials_ 5 Practical AI+HTML Hacks for Overseas Websites.md",
        "next_step_en": "Choose the right AI tool for your needs: <a href=\"/article/how-to-choose-right-ai-tool\">How to Choose the Right AI Tool &#x2192;</a>",
        "next_step_zh": "选择适合你的AI工具：<a href=\"/article/how-to-choose-right-ai-tool\">如何选择正确的AI工具 &#x2192;</a>",
    },
]


def clean_text(text):
    """Clean source text: remove markdown backslash escapes, convert HTML entities."""
    # Remove backslash before non-word chars: \. -> ., \- -> -, \& -> &, etc.
    text = re.sub(r'\\([^\w])', r'\1', text)
    # Convert various HTML entity forms to plain characters
    text = text.replace('&#39;', "'").replace("&amp;#39;", "'")
    text = text.replace('&#34;', '"').replace("&amp;#34;", '"')
    text = text.replace('&quot;', '"').replace("&amp;quot;", '"')
    text = text.replace('&lt;', '<').replace("&amp;lt;", '<')
    text = text.replace('&gt;', '>').replace("&amp;gt;", '>')
    text = text.replace('&amp;amp;', '&')
    text = text.replace('&amp;', '&')
    text = text.replace('&#x2192;', '→')
    return text


def escape_ts_template(text):
    """Escape special chars for JS/TS template literal: backtick, ${, backslash."""
    # Order matters: backslash first, then backtick, then ${}
    text = text.replace('\\', '\\\\')
    text = text.replace('`', '\\`')
    text = text.replace('${', '\\${')
    return text


def md_to_html(md_text):
    """Convert cleaned markdown to HTML for the article content field."""
    md_text = clean_text(md_text)
    lines = md_text.split('\n')

    out = []
    i = 0
    in_code = False
    code_buf = []
    in_list = False
    list_type = None
    list_items = []

    def flush_list():
        nonlocal in_list, list_type, list_items
        if not list_items:
            return
        out.append(f'<{list_type}>')
        for item in list_items:
            out.append(f'  <li>{item}</li>')
        out.append(f'</{list_type}>')
        list_items = []
        in_list = False
        list_type = None

    def inline(text):
        text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
        text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
        text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
        return text

    while i < len(lines):
        line = lines[i].rstrip('\r')

        if line.startswith('```'):
            if in_code:
                raw = '\n'.join(code_buf)
                out.append(f'<pre><code>{raw}</code></pre>')
                code_buf = []
                in_code = False
            else:
                flush_list()
                in_code = True
                code_buf = []
            i += 1
            continue

        if in_code:
            code_buf.append(line)
            i += 1
            continue

        s = line.strip()
        if not s:
            flush_list()
            i += 1
            continue

        # Skip first H1 (article title)
        if s.startswith('# ') and len(out) == 0 and not any(out):
            i += 1
            continue

        if s.startswith('# '):
            flush_list()
            out.append(f'<h2>{inline(s[2:])}</h2>')
        elif s.startswith('## '):
            flush_list()
            out.append(f'<h2>{inline(s[3:])}</h2>')
        elif s.startswith('### '):
            flush_list()
            out.append(f'<h3>{inline(s[4:])}</h3>')
        elif s.startswith('#### '):
            flush_list()
            out.append(f'<h4>{inline(s[5:])}</h4>')
        elif s.startswith('- ') or s.startswith('* '):
            if not in_list:
                in_list = True
                list_type = 'ul'
                list_items = []
            list_items.append(inline(s[2:]))
        elif re.match(r'^\d+\.\s', s):
            if not in_list:
                in_list = True
                list_type = 'ol'
                list_items = []
            list_items.append(inline(re.sub(r'^\d+\.\s', '', s)))
        elif s.startswith('> '):
            flush_list()
            out.append(f'<blockquote><p>{inline(s[2:])}</p></blockquote>')
        else:
            flush_list()
            out.append(f'<p>{inline(s)}</p>')

        i += 1

    flush_list()
    if in_code and code_buf:
        out.append(f'<pre><code>{"\\n".join(code_buf)}</code></pre>')

    return '\n\n'.join(out)


# Read existing article-content.ts
with open(articles_path, 'r', encoding='utf-8') as f:
    existing = f.read()

existing = existing.rstrip()
if existing.endswith('};'):
    base = existing[:-2].rstrip()
else:
    print("ERROR: File doesn't end with '};'")
    exit(1)

entries = []
for art in articles:
    src = os.path.join(wenzhang_dir, art["source"])
    with open(src, 'r', encoding='utf-8') as f:
        raw_md = f.read()

    # Generate English HTML
    html_en = md_to_html(raw_md)
    html_en += '\n\n<div class="next-step">\n<p><strong>Next Step:</strong> ' + art["next_step_en"] + '</p>\n</div>'

    # Generate Chinese intro
    title_m = re.search(r'^#\s+(.+)$', raw_md, re.MULTILINE)
    title = clean_text(title_m.group(1)) if title_m else ""
    html_zh = f'<p>本文详细介绍{title}。涵盖实用场景分析、代码示例和分步操作指南，帮助您充分利用AI工具提升海外业务效率。</p>'
    html_zh += '\n\n<div class="next-step">\n<p><strong>下一篇：</strong> ' + art["next_step_zh"] + '</p>\n</div>'

    entries.append(f'\n  // ====== {art["slug"]} ======')
    entries.append(f'  "{art["slug"]}": {{')
    entries.append(f'    content: `{escape_ts_template(html_en)}`,')
    entries.append(f'    contentZh: `{escape_ts_template(html_zh)}`,')
    entries.append(f'  }},')

with open(articles_path, 'w', encoding='utf-8') as f:
    f.write(base + '\n' + '\n'.join(entries) + '\n};')

print(f"OK: Added {len(articles)} article contents to {articles_path}")
