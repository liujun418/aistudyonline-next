#!/usr/bin/env python3
"""
Add Chinese translations (descriptionZh, tierZh, featuresZh) to tools.ts.
Properly handles both multi-line and compact (single-line) formats.
"""

import re
from pathlib import Path

FILEPATH = Path(r"C:\Users\jun\aistudyonline-next\src\lib\tools.ts")

def q(s):
    return '"' + s + '"'

def get_indent(line):
    m = re.match(r'^(\s*)', line)
    return m.group(1) if m else ''

def extract_quoted(line):
    m = re.search(r'"([^"]*)"', line)
    return m.group(1) if m else ''

def extract_features_from_line(line):
    """Extract only the quoted strings inside features: [...] from a line."""
    m = re.search(r'features:\s*\[([^\]]*)\]', line)
    if m:
        return re.findall(r'"([^"]*)"', m.group(1))
    return []

def find_closing_bracket(lines, start):
    depth = 0
    started = False
    for i in range(start, len(lines)):
        depth += lines[i].count('[') - lines[i].count(']')
        if depth <= 0 and started:
            return i
        started = True
    return start


# ============================================================
# Translation maps
# ============================================================

EXT_DESC_ZH = {
    "Official browser extension": "官方浏览器扩展程序",
    "Native apps for Windows and macOS": "Windows和macOS桌面应用",
    "Command-line coding assistant": "命令行编码助手",
    "Enterprise API with SSO": "企业级API，支持单点登录",
    "AI across Gmail, Docs, Sheets": "Gmail、文档和表格的AI功能",
    "Android/iOS app with voice": "支持语音的Android/iOS应用",
    "REST API for app integration": "用于应用集成的REST API",
    "Run locally via Ollama": "通过Ollama本地运行",
    "Perplexity Browser Extension": "Perplexity浏览器扩展",
    "Search anywhere on the web": "在网页任意位置搜索",
    "Perplexity Mobile": "Perplexity移动应用",
    "iOS and Android apps": "iOS和Android应用",
    "Midjourney Discord Bot": "Midjourney Discord机器人",
    "Primary interface via Discord": "通过Discord使用的主要界面",
    "Midjourney Web": "Midjourney网页版",
    "Web editor and gallery": "网页编辑器和作品集",
    "Built into ChatGPT": "内置于ChatGPT",
    "Access via ChatGPT interface": "通过ChatGPT界面访问",
    "Automatic1111 WebUI": "Automatic1111网页界面",
    "Most popular SD interface": "最流行的Stable Diffusion界面",
    "ComfyUI": "ComfyUI",
    "Node-based workflow interface": "基于节点的可视化工作流界面",
    "Adobe Photoshop": "Adobe Photoshop",
    "Generative Fill built in": "内置生成式填充功能",
    "Adobe Express": "Adobe Express",
    "Quick AI design tool": "快速AI设计工具",
    "Leonardo Web App": "Leonardo网页应用",
    "Full web-based creation platform": "基于网页的完整创作平台",
    "Runway Browser": "Runway浏览器版",
    "Web-based editing platform": "基于网页的编辑平台",
    "Pika Web App": "Pika网页应用",
    "Browser-based video generation": "基于浏览器的视频生成",
    "HeyGen Web": "HeyGen网页版",
    "Browser-based video creation platform": "基于浏览器的视频创作平台",
    "Jasper Chrome Extension": "Jasper Chrome扩展程序",
    "Write anywhere on the web": "在网页任意位置写作",
    "Copy.ai Chrome Extension": "Copy.ai Chrome扩展程序",
    "Write anywhere": "随处写作",
    "Notion AI Built-in": "Notion AI内置功能",
    "Available in all Notion workspaces": "所有Notion工作区可用",
    "Grammarly for Chrome": "Grammarly Chrome扩展",
    "Browser extension for all sites": "支持所有网站的浏览器扩展",
    "Grammarly Desktop": "Grammarly桌面版",
    "Windows and Mac app": "Windows和Mac应用",
    "Cursor Editor": "Cursor编辑器",
    "Standalone VS Code fork with AI": "集成AI的独立VS Code分支",
    "Copilot for VS Code": "Copilot VS Code扩展",
    "VS Code extension": "VS Code扩展",
    "Copilot for JetBrains": "Copilot JetBrains插件",
    "JetBrains IDE plugin": "JetBrains IDE插件",
    "Replit Browser": "Replit浏览器版",
    "Web-based IDE and deployment": "基于网页的IDE和部署平台",
    "Gamma Web App": "Gamma网页应用",
    "Browser-based creation tool": "基于浏览器的创作工具",
    "Beautiful.ai Web": "Beautiful.ai网页版",
    "Browser-based presentation tool": "基于浏览器的演示文稿工具",
    "Canva Web App": "Canva网页版",
    "Full browser-based design platform": "完整的基于浏览器的设计平台",
    "Canva Desktop": "Canva桌面版",
    "ElevenLabs Web": "ElevenLabs网页版",
    "Browser-based TTS platform": "基于浏览器的语音合成平台",
    "Suno Web": "Suno网页版",
    "Browser-based music generation": "基于浏览器的音乐生成",
    "Murf Web": "Murf网页版",
    "Browser-based voiceover studio": "基于浏览器的配音工作室",
    "DeepLearning.AI Website": "DeepLearning.AI网站",
    "Course platform and community": "课程平台和社区",
    "fast.ai Forums": "fast.ai论坛",
    "Community discussion platform": "社区讨论平台",
    "LangChain Python": "LangChain Python包",
    "Python framework package": "Python框架包",
    "LangChain JS": "LangChain JS包",
    "JavaScript/TypeScript framework": "JavaScript/TypeScript框架",
    "Hugging Face Hub": "Hugging Face平台",
    "Web platform and APIs": "网页平台和API",
    "Writesonic Chrome Extension": "Writesonic Chrome扩展",
    "Rytr Web App": "Rytr网页应用",
    "Browser-based writing tool": "基于浏览器的写作工具",
    "QuillBot Chrome Extension": "QuillBot Chrome扩展",
    "Paraphrase anywhere on the web": "在网页任意位置改写",
    "Wordtune Chrome Extension": "Wordtune Chrome扩展",
    "Write better across the web": "在网页各处写出更好的文章",
    "CopySmith Shopify App": "CopySmith Shopify应用",
    "Direct Shopify integration": "Shopify直接集成",
    "Anyword Chrome Extension": "Anyword Chrome扩展",
    "Score copy anywhere": "随处评估文案效果",
    "Sudowrite Web App": "Sudowrite网页应用",
    "Browser-based writing studio": "基于浏览器的写作工作室",
    "Remove.bg Photoshop Plugin": "Remove.bg Photoshop插件",
    "Background removal in Photoshop": "在Photoshop中移除背景",
    "Remove.bg API": "Remove.bg API",
    "Automated background removal": "自动化背景移除",
    "ClipDrop Web App": "ClipDrop网页应用",
    "Browser-based design toolkit": "基于浏览器的设计工具包",
    "CapCut Desktop": "CapCut桌面版",
    "CapCut Mobile": "CapCut移动版",
    "Descript Desktop": "Descript桌面版",
    "Synthesia Web App": "Synthesia网页应用",
    "InVideo Web App": "InVideo网页应用",
    "Browser-based video creation": "基于浏览器的视频创作",
    "Pixlr Web App": "Pixlr网页应用",
    "Browser-based photo editor": "基于浏览器的照片编辑器",
    "Copilot in Word": "Word中的Copilot",
    "AI writing assistant in Word": "Word中的AI写作助手",
    "Copilot in Excel": "Excel中的Copilot",
    "AI data analysis in Excel": "Excel中的AI数据分析",
    "Otter for Zoom": "Otter Zoom集成",
    "Zoom integration": "Zoom集成",
    "Otter for Google Meet": "Otter Google Meet集成",
    "Google Meet integration": "Google Meet集成",
    "Fireflies for Zoom": "Fireflies Zoom机器人",
    "Zoom bot": "Zoom机器人",
    "Fireflies for Salesforce": "Fireflies Salesforce集成",
    "Salesforce integration": "Salesforce集成",
    "SlidesAI Google Workspace": "SlidesAI Google Workspace插件",
    "Google Slides add-on": "Google Slides插件",
    "Tome Web App": "Tome网页应用",
    "Browser-based storytelling tool": "基于浏览器的故事讲述工具",
    "LlamaIndex Python": "LlamaIndex Python包",
    "LlamaIndex TS": "LlamaIndex TypeScript包",
    "TypeScript framework": "TypeScript框架",
    "Tabnine for VS Code": "Tabnine VS Code扩展",
    "Tabnine for JetBrains": "Tabnine JetBrains插件",
    "Codeium for VS Code": "Codeium VS Code扩展",
    "Codeium for JetBrains": "Codeium JetBrains插件",
    "Cody for VS Code": "Cody VS Code扩展",
    "Cody for JetBrains": "Cody JetBrains插件",
    "JetBrains plugin": "JetBrains插件",
    "Warp Desktop": "Warp桌面应用",
    "Native terminal app for macOS/Linux": "macOS/Linux原生终端应用",
    "Replit Browser IDE": "Replit浏览器IDE",
    "Browser-based development environment": "基于浏览器的开发环境",
    "Mintlify Web Platform": "Mintlify网页平台",
    "Hosted documentation platform": "托管的文档平台",
    "Pieces Desktop": "Pieces桌面应用",
    "Desktop app for snippet management": "代码片段管理桌面应用",
    "Pieces for VS Code": "Pieces VS Code扩展",
    "Phind Web App": "Phind网页应用",
    "Browser-based AI search": "基于浏览器的AI搜索",
    "Surfer SEO Chrome Extension": "Surfer SEO Chrome扩展",
    "SERP analyzer": "SERP分析器",
    "Surfer Google Docs Add-on": "Surfer Google Docs插件",
    "Content editor in Google Docs": "Google Docs中的内容编辑器",
    "Frase Chrome Extension": "Frase Chrome扩展",
    "SERP research tool": "SERP研究工具",
    "Frase WordPress Plugin": "Frase WordPress插件",
    "WordPress integration": "WordPress集成",
    "MarketMuse Web Platform": "MarketMuse网页平台",
    "Enterprise content optimization": "企业级内容优化",
    "HubSpot Content Hub": "HubSpot内容中心",
    "AI content platform": "AI内容平台",
    "HubSpot Sales Hub": "HubSpot销售中心",
    "Sales AI features": "销售AI功能",
    "ManyChat for Messenger": "ManyChat Messenger集成",
    "Facebook Messenger integration": "Facebook Messenger集成",
    "ManyChat for Instagram": "ManyChat Instagram集成",
    "Instagram DM integration": "Instagram私信集成",
    "Ollama CLI": "Ollama命令行工具",
    "Command-line tool": "命令行工具",
    "Ollama Python Library": "Ollama Python库",
    "Python API client": "Python API客户端",
    "LM Studio Desktop": "LM Studio桌面应用",
    "Desktop app for Windows/Mac/Linux": "Windows/Mac/Linux桌面应用",
    "GPT4All Desktop": "GPT4All桌面应用",
    "Desktop chat application": "桌面聊天应用",
    "Open Interpreter CLI": "Open Interpreter命令行工具",
    "LibreChat Web App": "LibreChat网页应用",
    "Self-hosted chat platform": "自托管聊天平台",
    "Ideogram Web App": "Ideogram网页应用",
    "Browser-based image generation": "基于浏览器的图像生成",
    "Podcastle Web App": "Podcastle网页应用",
    "Browser-based podcast studio": "基于浏览器的播客工作室",
}

TIER_NAME_ZH = {
    "Free": "免费版",
    "Plus": "Plus版",
    "Pro": "专业版",
    "Basic": "基础版",
    "Standard": "标准版",
    "Starter": "入门版",
    "Team": "团队版",
    "Enterprise": "企业版",
    "Creator": "创作者版",
    "Business": "商务版",
    "Max": "高级版",
    "Premium": "高级版",
    "Individual": "个人版",
    "Add-on": "附加功能版",
    "Audit": "旁听版",
    "Coursera": "Coursera版",
    "Self-hosted": "自托管版",
    "API": "API版",
    "Open Source": "开源版",
    "LangSmith": "LangSmith版",
    "LlamaCloud": "LlamaCloud版",
    "Essential": "基础版",
    "Advanced": "高级版",
    "M365 Copilot": "M365 Copilot版",
    "Free Chat": "免费聊天版",
    "ChatGPT Free": "ChatGPT免费版",
    "ChatGPT Plus": "ChatGPT Plus版",
    "Storyteller": "创作者版",
    "All Courses": "全部课程版",
}

FEATURE_ZH = {
    "GPT-4o mini access": "GPT-4o mini访问权限",
    "Limited GPT-5 messages": "GPT-5消息有限额度",
    "Basic file uploads": "基础文件上传",
    "Unlimited GPT-5": "GPT-5无限使用",
    "Advanced data analysis": "高级数据分析",
    "DALL-E 3": "DALL-E 3图像生成",
    "Custom GPTs": "自定义GPTs",
    "Unlimited GPT-5 Turbo": "GPT-5 Turbo无限使用",
    "Priority access": "优先访问",
    "Extended context": "扩展上下文",
    "Claude 4 Sonnet": "Claude 4 Sonnet模型",
    "Limited daily messages": "每日消息限制",
    "Basic uploads": "基础文件上传",
    "Unlimited Claude 4 Sonnet": "Claude 4 Sonnet无限使用",
    "Claude 4 Opus": "Claude 4 Opus模型",
    "Projects": "项目管理",
    "All Pro features": "所有专业版功能",
    "Higher limits": "更高使用额度",
    "Shared workspaces": "共享工作区",
    "Gemini 2.0 Flash": "Gemini 2.0 Flash模型",
    "Google Search": "谷歌搜索",
    "File uploads": "文件上传",
    "Gemini 2.0 Pro": "Gemini 2.0 Pro模型",
    "1TB Drive storage": "1TB云盘存储",
    "Workspace integration": "工作区集成",
    "Unlimited DeepSeek chat": "DeepSeek无限聊天",
    "DeepSeek-R1": "DeepSeek-R1模型",
    "R1 and V3 API": "R1和V3 API",
    "Rate limits": "速率限制",
    "Fine-tuning": "模型微调",
    "Standard search": "标准搜索",
    "Limited Pro searches": "专业搜索有限额度",
    "Unlimited Pro": "专业搜索无限使用",
    "Unlimited file analysis": "文件分析无限使用",
    "API access": "API访问权限",
    "3.3 hrs/month GPU": "每月3.3小时GPU时长",
    "Commercial license": "商业使用授权",
    "15 hrs/month GPU": "每月15小时GPU时长",
    "Stealth mode": "隐身模式",
    "30 hrs/month GPU": "每月30小时GPU时长",
    "Priority queue": "优先队列",
    "Limited DALL-E 3": "DALL-E 3有限使用",
    "Basic resolution": "基础分辨率",
    "Unlimited DALL-E 3": "DALL-E 3无限使用",
    "HD resolution": "高清分辨率",
    "Unlimited generation": "无限生成",
    "Full privacy": "完全隐私保护",
    "All models": "所有模型",
    "Cloud hosted": "云端托管",
    "No GPU needed": "无需GPU",
    "25 credits/month": "每月25积分",
    "Basic features": "基础功能",
    "Express access": "Express访问权限",
    "100 credits/month": "每月100积分",
    "Full features": "全部功能",
    "Commercial use": "商业使用授权",
    "150 tokens/day": "每日150点数",
    "Standard models": "标准模型",
    "2500 tokens/month": "每月2500点数",
    "Faster generation": "更快的生成速度",
    "8000 tokens/month": "每月8000点数",
    "Limited generations": "有限生成次数",
    "720p export": "720p导出",
    "4K export": "4K导出",
    "Green screen": "绿幕功能",
    "All Pro": "所有专业版功能",
    "Collaboration": "团队协作",
    "Priority support": "优先支持",
    "Standard quality": "标准质量",
    "More generations": "更多生成次数",
    "HD quality": "高清质量",
    "Faster queue": "更快的处理队列",
    "1 min video": "1分钟视频",
    "Watermark": "包含水印",
    "Basic avatars": "基础虚拟形象",
    "10 mins/month": "每月10分钟",
    "No watermark": "无水印",
    "HD export": "高清导出",
    "30 mins/month": "每月30分钟",
    "Custom avatars": "自定义虚拟形象",
    "1 user": "1个用户",
    "50+ templates": "50多个模板",
    "SEO mode": "SEO模式",
    "3 users": "3个用户",
    "Brand voice": "品牌语气",
    "Custom templates": "自定义模板",
    "2000 words/month": "每月2000词",
    "Basic templates": "基础模板",
    "Unlimited words": "无限字数",
    "5 users": "5个用户",
    "Workflows": "工作流自动化",
    "Per member": "按成员计费",
    "AI writing": "AI写作",
    "Auto-fill databases": "自动填充数据库",
    "Basic grammar": "基础语法检查",
    "Spelling": "拼写检查",
    "Punctuation": "标点检查",
    "Full grammar": "完整语法检查",
    "Tone detection": "语气检测",
    "Plagiarism": "查重功能",
    "All Premium": "所有高级版功能",
    "Style guide": "风格指南",
    "Analytics": "数据分析",
    "200 AI completions": "200次AI补全",
    "Basic chat": "基础聊天",
    "Unlimited AI": "AI无限使用",
    "Agent mode": "代理模式",
    "Multi-file edit": "多文件编辑",
    "2000 completions/month": "每月2000次补全",
    "Code chat": "代码聊天",
    "Multi-file": "多文件支持",
    "PR summaries": "PR摘要生成",
    "Limited compute": "有限计算资源",
    "AI agent access": "AI代理访问",
    "Public projects": "公开项目",
    "Unlimited compute": "无限计算资源",
    "Private projects": "私有项目",
    "Faster AI": "更快的AI响应",
    "Limited AI credits": "有限AI额度",
    "All templates": "所有模板",
    "Export options": "导出选项",
    "Unlimited presentations": "无限演示文稿",
    "Export": "导出功能",
    "Team library": "团队资源库",
    "Brand control": "品牌控制",
    "Limited AI": "AI功能有限",
    "250K+ templates": "超过25万个模板",
    "1GB storage": "1GB存储空间",
    "100M+ assets": "超过1亿素材",
    "Brand kits": "品牌工具包",
    "10K chars/month": "每月1万字符",
    "Standard voices": "标准语音",
    "30K chars/month": "每月3万字符",
    "Voice cloning": "语音克隆",
    "100K chars/month": "每月10万字符",
    "5 songs/day": "每天5首",
    "Basic quality": "基础质量",
    "500 songs/month": "每月500首",
    "Full quality": "完整质量",
    "10 mins voice": "10分钟语音",
    "Limited voices": "有限语音选择",
    "24 hours/year": "每年24小时",
    "All voices": "所有语音",
    "Video access": "视频课程访问",
    "Limited exercises": "有限练习",
    "Full courses": "完整课程",
    "Certificate": "结业证书",
    "All course materials": "所有课程资料",
    "Forum access": "论坛访问权限",
    "Book included": "包含教材",
    "All framework features": "所有框架功能",
    "Self-hosted": "自行托管",
    "Debugging": "调试功能",
    "Monitoring": "监控功能",
    "Evaluation": "评估功能",
    "Public models": "公开模型",
    "Datasets": "数据集访问",
    "Limited Spaces": "有限Spaces额度",
    "Private repos": "私有仓库",
    "More Spaces": "更多Spaces额度",
    "Inference API": "推理API",
    "10,000 words/month": "每月1万字",
    "SEO optimization": "SEO优化",
    "5,000 chars/month": "每月5000字符",
    "40+ templates": "40多个模板",
    "50,000 chars/month": "每月5万字符",
    "Plagiarism check": "查重检查",
    "Custom tones": "自定义语气",
    "Limited paraphrasing": "有限改写次数",
    "2 modes": "2种模式",
    "Basic summary": "基础摘要",
    "Unlimited paraphrasing": "无限改写",
    "7 modes": "7种模式",
    "10 rephrases/day": "每天10次改写",
    "Basic modes": "基础模式",
    "Unlimited rephrases": "无限改写",
    "All modes": "所有模式",
    "Tone adjustment": "语气调整",
    "20,000 words/mo": "每月2万字",
    "Bulk generation": "批量生成",
    "Shopify sync": "Shopify同步",
    "5,000 AI words/mo": "每月5000AI词",
    "Basic scoring": "基础评分",
    "20,000 AI words/mo": "每月2万AI词",
    "Advanced scoring": "高级评分",
    "Integrations": "集成功能",
    "Higher quality": "更高质量",
    "Standard resolution": "标准分辨率",
    "Preview quality": "预览质量",
    "Batch processing": "批量处理",
    "Basic tools": "基础工具",
    "All tools": "所有工具",
    "Basic editing": "基础编辑",
    "Auto-captions": "自动字幕",
    "Templates": "模板",
    "Advanced effects": "高级特效",
    "Cloud storage": "云存储",
    "1 hour transcription": "1小时转录",
    "10 hours/mo": "每月10小时",
    "AI features": "AI功能",
    "Screen recording": "录屏功能",
    "10 mins video": "10分钟视频",
    "Standard avatars": "标准虚拟形象",
    "Dedicated support": "专属支持",
    "Watermarked": "含带水印",
    "Limited templates": "有限模板",
    "Stock media": "素材库",
    "Basic editors": "基础编辑器",
    "AI tools limited": "AI工具有限",
    "All AI tools": "所有AI工具",
    "Ad-free": "无广告",
    "Advanced features": "高级功能",
    "Web copilot": "网页版Copilot",
    "Limited daily chats": "每日聊天次数限制",
    "Full Office integration": "完整Office集成",
    "Copilot Studio": "Copilot Studio",
    "Enterprise security": "企业级安全",
    "300 mins/month": "每月300分钟",
    "Basic transcription": "基础转录",
    "1200 mins/month": "每月1200分钟",
    "Search": "搜索功能",
    "Limited transcription": "有限转录",
    "Public meetings": "公开会议",
    "Unlimited transcription": "无限转录",
    "Limited slides": "有限幻灯片数",
    "Basic themes": "基础主题",
    "Unlimited slides": "无限幻灯片",
    "Image generation": "图像生成",
    "Limited presentations": "有限演示文稿",
    "Basic AI": "基础AI功能",
    "Full AI": "全部AI功能",
    "Custom branding": "自定义品牌",
    "Managed indexing": "托管索引",
    "Local completions": "本地补全",
    "Limited suggestions": "有限建议",
    "Full completions": "完整补全",
    "Whole-line": "整行补全",
    "Team models": "团队模型",
    "Priority completions": "优先补全",
    "Limited requests": "有限请求",
    "Basic context": "基础上下文",
    "Unlimited requests": "无限请求",
    "Full context": "完整上下文",
    "Multiple repos": "多个仓库",
    "AI search limited": "AI搜索有限",
    "Team features": "团队功能",
    "Public docs": "公开文档",
    "Custom domain": "自定义域名",
    "Multiple users": "多用户支持",
    "Basic capture": "基础捕获",
    "Limited storage": "有限存储",
    "Unlimited storage": "无限存储",
    "Team sharing": "团队共享",
    "Advanced AI": "高级AI功能",
    "Limited searches": "有限搜索",
    "Basic models": "基础模型",
    "Unlimited searches": "无限搜索",
    "GPT-5/C4 Opus": "GPT-5/Claude Opus",
    "Priority": "优先处理",
    "60 articles": "60篇文章",
    "Basic analysis": "基础分析",
    "200 articles": "200篇文章",
    "AI generation": "AI生成",
    "30 articles/mo": "每月30篇文章",
    "Unlimited articles": "无限文章",
    "Full platform": "完整平台",
    "Custom analysis": "自定义分析",
    "Basic AI tools": "基础AI工具",
    "Limited content": "有限内容",
    "Full AI suite": "完整AI套件",
    "Content assistant": "内容助手",
    "Predictive scoring": "预测评分",
    "1,000 contacts": "1000个联系人",
    "AI flows": "AI流程",
    "Sequences": "序列功能",
    "10,000 contacts": "1万个联系人",
    "Local only": "仅本地运行",
    "CLI + API": "命令行和API",
    "GUI + API": "图形界面和API",
    "Local CPU": "本地CPU运行",
    "Offline": "离线运行",
    "Multi-provider": "多提供商支持",
    "Basic recording": "基础录制",
    "Audio cleanup": "音频清理",
    "Unlimited recording": "无限录制",
    "Revoice": "AI语音修复",
    "Publishing": "发布功能",
    "All features": "全部功能",
    "Unlimited": "无限使用",
    "Unlimited generations": "无限生成",
    "Unlimited slides": "无限幻灯片数",
    "Unlimited recording": "无限录制",
    "Unlimited AI": "AI无限使用",
}


def main():
    with open(FILEPATH, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # ====================================================================
    # PHASE 1: CLEANUP
    # Remove all incorrectly placed tierZh, featuresZh (including content),
    # and extension descriptionZh lines. Keep tool-level descriptionZh.
    # ====================================================================
    cleaned = []
    skipping_features = False
    skip_depth = 0

    for line in lines:
        stripped = line.strip()
        indent = len(line) - len(line.lstrip())

        if skipping_features:
            skip_depth += line.count('[') - line.count(']')
            if skip_depth <= 0:
                skipping_features = False
            continue

        # Remove standalone tierZh lines (from first script's incorrect output)
        if stripped.startswith('tierZh:'):
            continue

        # Remove entire featuresZh: [...] blocks (standalone lines)
        if stripped.startswith('featuresZh:'):
            if '[' in stripped:
                skip_depth = line.count('[') - line.count(']')
                if skip_depth > 0:
                    skipping_features = True
                # If skip_depth <= 0, the array is single-line and we just skip this line
            continue

        # Remove extension descriptionZh lines (indent >= 6)
        if stripped.startswith('descriptionZh:') and indent >= 6:
            continue

        # --- Clean inline artifacts from compact (single-line) format objects ---

        # Remove inline featuresZh from compact tiers: { tier: "...", featuresZh: [...] }
        # (these survive standalone cleanup because they're on the same line as the tier)
        if 'featuresZh:' in stripped and '{' in stripped and '}' in stripped:
            line = re.sub(r',?\s*featuresZh:\s*\[[^\]]*\]', '', line)

        # Remove inline descriptionZh from compact extensions: { name: "...", descriptionZh: "..." }
        if 'descriptionZh:' in stripped and '{' in stripped and '}' in stripped:
            line = re.sub(r',?\s*descriptionZh:\s*"[^"]*"', '', line)
            # Clean up orphan trailing }, from previous buggy runs
            # After removing descriptionZh, we get "... }] },\n" (comma already consumed by prev regex)
            if re.search(r'\]\s*,?\s*\}\s*,?\s*$', line.rstrip()):
                line = re.sub(r'\]\s*,?\s*\}\s*,?\s*', '],', line.rstrip()) + '\n'

        # Remove inline tierZh from compact tiers (will be re-added by Phase 2)
        # BUT only if the tierZh value looks wrong (contains non-Chinese from old run)
        # Actually, just always strip inline tierZh from compact format to be safe
        if 'tierZh:' in stripped and '{' in stripped and '}' in stripped:
            # Only strip if not already cleaned (line may have been modified above)
            line = re.sub(r',?\s*tierZh:\s*"[^"]*"', '', line)

        cleaned.append(line)

    # ====================================================================
    # PHASE 2: CORRECTLY ADD TRANSLATIONS
    # ====================================================================
    result = []
    i = 0
    changes = 0

    while i < len(cleaned):
        line = cleaned[i]
        stripped = line.strip()

        # --- Extension descriptions ---
        if re.search(r'description:\s*"', line) and 'descriptionZh' not in stripped:
            # Only process extension descriptions (indent >= 6 or compact inline format indent >= 4)
            line_indent = len(line) - len(line.lstrip())
            is_compact = '{' in stripped and '}' in stripped
            if line_indent < 6 and not is_compact:
                result.append(line)
                i += 1
                continue
            # Check if next non-empty line already has descriptionZh
            has_zh = False
            for j in range(i + 1, min(i + 3, len(cleaned))):
                s = cleaned[j].strip()
                if s.startswith('descriptionZh:'):
                    has_zh = True
                    break
                if s and not s.startswith('//'):
                    break

            if not has_zh:
                # Extract text from description: field specifically
                desc_m = re.search(r'description:\s*"([^"]*)"', line)
                text = desc_m.group(1) if desc_m else ''
                zh = EXT_DESC_ZH.get(text, text)
                indent = get_indent(line)

                # Is this an inline compact extension?
                # (the line is part of a single-line object with {...} on same line)
                if '{' in stripped and '}' in stripped:
                    # Handle compact extension: `extensions: [{name: "...", description: "..."}]`
                    # or `{name: "...", description: "..."}` alone.
                    # Strategy: find the LAST } (closes the inner object), insert before it.
                    modified = stripped.rstrip().rstrip(',').rstrip()
                    last_brace = modified.rfind('}')
                    if last_brace >= 0:
                        before = modified[:last_brace].rstrip()
                        after = modified[last_brace:]
                        modified = before + ', descriptionZh: ' + q(zh) + ' ' + after.lstrip()
                    else:
                        modified += ', descriptionZh: ' + q(zh)
                    result.append(indent + modified + ',\n')
                    changes += 1
                    i += 1
                    continue
                else:
                    # Multi-line format - add on a new line after
                    # If description doesn't end with comma, add one
                    if stripped.rstrip().endswith(','):
                        result.append(line)
                    else:
                        result.append(line.rstrip() + ',\n')
                    result.append(indent + 'descriptionZh: ' + q(zh) + ',\n')
                    changes += 1
                    i += 1
                    continue

        # --- Pricing tier names ---
        if re.search(r'\btier:\s*"', line) and 'tierZh' not in stripped:
            has_zh = False
            for j in range(i + 1, min(i + 3, len(cleaned))):
                s = cleaned[j].strip()
                if s.startswith('tierZh:'):
                    has_zh = True
                    break
                if s and not s.startswith('//'):
                    break

            if not has_zh:
                text = extract_quoted(line)
                zh = TIER_NAME_ZH.get(text, text + '版')
                indent = get_indent(line)

                if '{' in stripped and '}' in stripped:
                    # Compact format - insert inline after tier:
                    modified = re.sub(
                        r'(\btier:\s*")([^"]*)(")',
                        r'\1\2\3, tierZh: ' + q(zh),
                        stripped,
                        count=1
                    )
                    result.append(indent + modified + '\n')
                    changes += 1
                    i += 1
                    continue
                else:
                    # Multi-line
                    result.append(line)
                    result.append(indent + '  tierZh: ' + q(zh) + ',\n')
                    changes += 1
                    i += 1
                    continue

        # --- Pricing features arrays (only for multi-line format) ---
        if re.search(r'\bfeatures:\s*\[', line) and 'featuresZh' not in stripped:
            # For compact format (tier on same line with { and }), skip features
            # because they're handled inline with the tier
            if '{' in stripped and '}' in stripped:
                # This is a compact format tier - handle features inline
                items = extract_features_from_line(stripped)
                if items:
                    zh_items = [FEATURE_ZH.get(item, item) for item in items]
                    indent = get_indent(line)
                    # Insert featuresZh before the closing }
                    modified = stripped.rstrip()
                    if modified.endswith(','):
                        modified = modified[:-1].rstrip()
                    if modified.endswith('}'):
                        modified = modified[:-1].rstrip()
                    zh_part = ', '.join(q(i) for i in zh_items)
                    modified += ', featuresZh: [' + zh_part + '] },\n'
                    result.append(indent + modified)
                    changes += 1
                    i += 1
                    continue
                else:
                    result.append(line)
                    i += 1
                    continue

            # Multi-line features array
            end_idx = find_closing_bracket(cleaned, i)

            has_zh = False
            for j in range(end_idx + 1, min(end_idx + 4, len(cleaned))):
                if 'featuresZh' in cleaned[j]:
                    has_zh = True
                    break
                if cleaned[j].strip() and not cleaned[j].strip().startswith('//'):
                    break

            if not has_zh:
                feat_lines = cleaned[i:end_idx + 1]
                all_text = ''.join(feat_lines)
                items = re.findall(r'"([^"]*)"', all_text)
                if items:
                    zh_items = [FEATURE_ZH.get(item, item) for item in items]
                    indent = get_indent(line)

                    # Add original lines up to end_idx (exclusive of last line)
                    for j in range(i, end_idx):
                        result.append(cleaned[j])

                    # Fix the closing ] to have a comma
                    last_line = cleaned[end_idx]
                    last_stripped = last_line.strip()
                    if last_stripped == ']' or last_stripped == '],':
                        result.append(get_indent(last_line) + '],\n')
                    else:
                        result.append(last_line)

                    # Add featuresZh
                    if len(zh_items) <= 2:
                        zh_line = indent + 'featuresZh: [' + ', '.join(q(i) for i in zh_items) + '],\n'
                    else:
                        zh_line = indent + 'featuresZh: [\n'
                        for item in zh_items:
                            zh_line += indent + '  ' + q(item) + ',\n'
                        zh_line += indent + '],\n'
                    result.append(zh_line)
                    changes += 1
                    i = end_idx + 1
                    continue

        result.append(line)
        i += 1

    with open(FILEPATH, 'w', encoding='utf-8') as f:
        f.writelines(result)

    print(f"Done. Lines: {len(lines)} -> {len(cleaned)} -> {len(result)}. Changes: {changes}")


if __name__ == '__main__':
    main()
