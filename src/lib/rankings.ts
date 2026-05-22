export interface RankingEntry {
  rank: number;
  toolId: string;
  reason: string;
  reasonZh: string;
  score: number;
}

/**
 * Top 10 AI tools ranked by comprehensive score (popularity, capability, value).
 * Used for the homepage "Top 10 AI Tools" section.
 */
export const topTools: RankingEntry[] = [
  {
    rank: 1,
    toolId: "chatgpt",
    reason: "The most widely adopted AI assistant. Powers daily work for 400M+ users worldwide with GPT-5 integration.",
    reasonZh: "最广泛采用的AI助手，GPT-5加持，全球4亿+用户的日常AI伴侣。",
    score: 98,
  },
  {
    rank: 2,
    toolId: "cursor",
    reason: "The fastest-growing AI code editor. AI-first IDE that changed how developers write software.",
    reasonZh: "增长最快的AI代码编辑器，以AI为核心的IDE革新了开发者写代码的方式。",
    score: 95,
  },
  {
    rank: 3,
    toolId: "claude",
    reason: "Best-in-class reasoning and safety. The go-to model for complex analysis, coding, and long-form writing.",
    reasonZh: "推理和安全能力顶尖，复杂分析、编程和长文写作的首选模型。",
    score: 93,
  },
  {
    rank: 4,
    toolId: "gemini",
    reason: "Google's most capable model with 2M-token context. Deep integration with Google ecosystem.",
    reasonZh: "Google最强模型，200万token上下文窗口，深度集成Google生态。",
    score: 91,
  },
  {
    rank: 5,
    toolId: "midjourney",
    reason: "The gold standard for AI image generation. Unmatched artistic quality and community ecosystem.",
    reasonZh: "AI图像生成的黄金标准，艺术质量和社区生态无可匹敌。",
    score: 89,
  },
  {
    rank: 6,
    toolId: "github-copilot",
    reason: "The original AI pair programmer. Now with agent mode and multi-file editing, it is indispensable for modern development.",
    reasonZh: "AI编程搭档的开创者，现已支持代理模式和多文件编辑，现代开发不可或缺。",
    score: 87,
  },
  {
    rank: 7,
    toolId: "perplexity",
    reason: "The AI-powered answer engine that is replacing traditional search for research and fact-finding.",
    reasonZh: "AI驱动的答案引擎，在研究和事实查找场景中正在取代传统搜索引擎。",
    score: 85,
  },
  {
    rank: 8,
    toolId: "notion-ai",
    reason: "Brings AI writing, summarization, and Q&A directly into the most popular productivity workspace.",
    reasonZh: "将AI写作、总结和问答直接带入最流行的生产力工作空间。",
    score: 83,
  },
  {
    rank: 9,
    toolId: "elevenlabs",
    reason: "Industry-leading AI voice synthesis with unmatched realism, now supporting voice cloning and dubbing.",
    reasonZh: "行业领先的AI语音合成，真实感无可比拟，现已支持语音克隆和配音。",
    score: 81,
  },
  {
    rank: 10,
    toolId: "deepseek",
    reason: "The open-source champion proving LLM excellence does not require billions in funding. R1 rivals the best closed models.",
    reasonZh: "开源模型冠军，证明卓越的LLM不需要数十亿美金投入。R1媲美最佳闭源模型。",
    score: 79,
  },
];
