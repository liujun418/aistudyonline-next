export const locales = ["en", "zh"] as const;
export type Locale = (typeof locales)[number];
export const defaultLocale: Locale = "en";

export const localeNames: Record<Locale, string> = {
  en: "English",
  zh: "中文",
};

export const localeDir: Record<Locale, "ltr" | "rtl"> = {
  en: "ltr",
  zh: "ltr",
};

export function isValidLocale(locale: string): locale is Locale {
  return (locales as readonly string[]).includes(locale);
}

const dictionaries: Record<string, () => Promise<Record<string, unknown>>> = {
  en: () => import("@/locales/en/common.json").then((m) => m.default),
  zh: () => import("@/locales/zh/common.json").then((m) => m.default),
};

export async function getDictionary(locale: Locale): Promise<Record<string, unknown>> {
  return dictionaries[locale]();
}

export const tagLabels: Record<string, { en: string; zh: string }> = {
  // Tools tags
  conversation: { en: "Conversation", zh: "对话" },
  writing: { en: "Writing", zh: "写作" },
  coding: { en: "Coding", zh: "编程" },
  analysis: { en: "Analysis", zh: "分析" },
  reasoning: { en: "Reasoning", zh: "推理" },
  safety: { en: "Safety", zh: "安全" },
  multimodal: { en: "Multimodal", zh: "多模态" },
  search: { en: "Search", zh: "搜索" },
  research: { en: "Research", zh: "研究"  },
  "open-source": { en: "Open Source", zh: "开源" },
  local: { en: "Local", zh: "本地" },
  free: { en: "Free", zh: "免费" },
  design: { en: "Design", zh: "设计" },
  creative: { en: "Creative", zh: "创意" },
  "high-quality": { en: "High Quality", zh: "高质量" },
  professional: { en: "Professional", zh: "专业" },
  customizable: { en: "Customizable", zh: "可自定义" },
  integration: { en: "Integration", zh: "集成" },
  art: { en: "Art", zh: "艺术" },

  // Article tags
  beginner: { en: "Beginner", zh: "入门" },
  fundamentals: { en: "Fundamentals", zh: "基础" },
  "getting-started": { en: "Getting Started", zh: "入门指南" },
  prompts: { en: "Prompts", zh: "提示词" },
  "prompt-engineering": { en: "Prompt Engineering", zh: "提示工程" },
  framework: { en: "Framework", zh: "框架" },
  email: { en: "Email", zh: "邮件" },
  content: { en: "Content", zh: "内容" },
  editing: { en: "Editing", zh: "编辑" },
  productivity: { en: "Productivity", zh: "效率" },
  business: { en: "Business", zh: "商务" },
  communication: { en: "Communication", zh: "沟通" },
  planning: { en: "Planning", zh: "规划" },
  "project-management": { en: "Project Management", zh: "项目管理" },
  "report-writing": { en: "Report Writing", zh: "报告写作" },
  learning: { en: "Learning", zh: "学习" },
  education: { en: "Education", zh: "教育" },
  language: { en: "Language", zh: "语言" },
  "voice-mode": { en: "Voice Mode", zh: "语音模式" },
  "quick-tips": { en: "Quick Tips", zh: "快速技巧" },
  practical: { en: "Practical", zh: "实用" },
  "life-hacks": { en: "Life Hacks", zh: "生活技巧" },
  "image-generation": { en: "Image Generation", zh: "图像生成" },
  tutorial: { en: "Tutorial", zh: "教程" },
  "free-vs-paid": { en: "Free vs Paid", zh: "免费vs付费" },
  pricing: { en: "Pricing", zh: "价格" },
  comparison: { en: "Comparison", zh: "对比" },
  "side-by-side": { en: "Side by Side", zh: "对比评测" },
  "blind-test": { en: "Blind Test", zh: "盲测" },
  "learning-curve": { en: "Learning Curve", zh: "学习曲线" },
  "for-beginners": { en: "For Beginners", zh: "适合新手" },
  "whats-new": { en: "What's New", zh: "最新动态" },
  features: { en: "Features", zh: "功能" },
  update: { en: "Update", zh: "更新" },
  "claude-code": { en: "Claude Code", zh: "Claude Code" },
  mcp: { en: "MCP", zh: "MCP" },
  configuration: { en: "Configuration", zh: "配置" },
  workflow: { en: "Workflow", zh: "工作流" },
  "web-development": { en: "Web Development", zh: "Web开发" },
  advanced: { en: "Advanced", zh: "高级" },
  hooks: { en: "Hooks", zh: "钩子" },
  "ci-cd": { en: "CI/CD", zh: "CI/CD" },
  "custom-commands": { en: "Custom Commands", zh: "自定义命令" },
  "ai-image": { en: "AI Image", zh: "AI图像" },
  techniques: { en: "Techniques", zh: "技巧" },
  guide: { en: "Guide", zh: "指南" },
  copyright: { en: "Copyright", zh: "版权" },
  licensing: { en: "Licensing", zh: "许可" },
  commercial: { en: "Commercial", zh: "商业用途" },
  legal: { en: "Legal", zh: "法律" },

  // Tool-specific tags
  notes: { en: "Notes", zh: "笔记" },
  knowledge: { en: "Knowledge", zh: "知识" },
  organization: { en: "Organization", zh: "组织" },
  sales: { en: "Sales", zh: "销售" },
  "social-media": { en: "Social Media", zh: "社交媒体" },
  marketing: { en: "Marketing", zh: "营销" },
  copywriting: { en: "Copywriting", zh: "文案" },
  brand: { en: "Brand", zh: "品牌" },
  video: { en: "Video", zh: "视频" },
  motion: { en: "Motion", zh: "运动" },
  avatars: { en: "Avatars", zh: "虚拟形象" },
  presentation: { en: "Presentation", zh: "演示" },
  talking: { en: "Talking", zh: "口播" },
  gaming: { en: "Gaming", zh: "游戏" },
  assets: { en: "Assets", zh: "资源" },
  characters: { en: "Characters", zh: "角色" },
  models: { en: "Models", zh: "模型" },
  explained: { en: "Explained", zh: "解释" },
  "non-technical": { en: "Non-Technical", zh: "非技术" },
  myths: { en: "Myths", zh: "迷思" },
  hallucinations: { en: "Hallucinations", zh: "幻觉" },
  accuracy: { en: "Accuracy", zh: "准确性" },
  value: { en: "Value", zh: "价值" },
  hardware: { en: "Hardware", zh: "硬件" },
  gpu: { en: "GPU", zh: "GPU" },
  nvidia: { en: "NVIDIA", zh: "NVIDIA" },
  "eu-ai-act": { en: "EU AI Act", zh: "欧盟AI法案" },
  regulation: { en: "Regulation", zh: "监管" },
  policy: { en: "Policy", zh: "政策" },
  "plain-english": { en: "Plain English", zh: "通俗解释" },
  jobs: { en: "Jobs", zh: "工作" },
  career: { en: "Career", zh: "职业" },
  salary: { en: "Salary", zh: "薪资" },
  "new-roles": { en: "New Roles", zh: "新兴职位" },
  trends: { en: "Trends", zh: "趋势" },
  "local-ai": { en: "Local AI", zh: "本地AI" },
  laptop: { en: "Laptop", zh: "笔记本" },
  apple: { en: "Apple", zh: "Apple" },
  intelligence: { en: "Intelligence", zh: "智能" },
  iphone: { en: "iPhone", zh: "iPhone" },
  ios: { en: "iOS", zh: "iOS" },
  claude: { en: "Claude", zh: "Claude" },
  chatgpt: { en: "ChatGPT", zh: "ChatGPT" },
  gemini: { en: "Gemini", zh: "Gemini" },
  perplexity: { en: "Perplexity", zh: "Perplexity" },
  midjourney: { en: "Midjourney", zh: "Midjourney" },
  openai: { en: "OpenAI", zh: "OpenAI" },
  gpt5: { en: "GPT-5", zh: "GPT-5" },
  notebooklm: { en: "NotebookLM", zh: "NotebookLM" },
  cursor: { en: "Cursor", zh: "Cursor" },
  copilot: { en: "Copilot", zh: "Copilot" },
  dalle3: { en: "DALL-E 3", zh: "DALL-E 3" },
  "adobe-firefly": { en: "Adobe Firefly", zh: "Adobe Firefly" },
  "real-time": { en: "Real-time", zh: "实时" },
  citations: { en: "Citations", zh: "引用" },
  parents: { en: "Parents", zh: "家长" },
  "busy-lifestyle": { en: "Busy Lifestyle", zh: "忙碌生活" },
  "custom-gpts": { en: "Custom GPTs", zh: "自定义GPT" },
  automation: { en: "Automation", zh: "自动化" },
  "gpt-store": { en: "GPT Store", zh: "GPT商店" },
  "no-code": { en: "No Code", zh: "无代码" },
  "file-upload": { en: "File Upload", zh: "文件上传" },
  "data-analysis": { en: "Data Analysis", zh: "数据分析" },
  "web-search": { en: "Web Search", zh: "网页搜索" },
  tools: { en: "Tools", zh: "工具" },
  llm: { en: "LLM", zh: "大语言模型" },
  proposals: { en: "Proposals", zh: "提案" },
  timeline: { en: "Timeline", zh: "时间线" },
  budget: { en: "Budget", zh: "预算" },
  data: { en: "Data", zh: "数据" },
  skills: { en: "Skills", zh: "技能" },
  discord: { en: "Discord", zh: "Discord" },
  audio: { en: "Audio", zh: "音频" },
  "free-open-source": { en: "Free & Open Source", zh: "免费开源" },
  "office-productivity": { en: "Office & Productivity", zh: "办公效率" },
  "content-creation": { en: "Content Creation", zh: "内容创作" },
  "design-video": { en: "Design & Video", zh: "设计与视频" },
  adobe: { en: "Adobe", zh: "Adobe" },
  photography: { en: "Photography", zh: "摄影" },
  google: { en: "Google", zh: "谷歌" },
};

/**
 * Get the localized tag label.
 */
export function getTagLabel(tag: string, locale: string): string {
  const entry = tagLabels[tag.toLowerCase()];
  if (!entry) return tag;
  if (locale === "zh") return entry.zh;
  return entry.en;
}
