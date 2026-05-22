export interface Category {
  id: string;
  name: string;
  nameZh: string;
  description: string;
  descriptionZh: string;
  icon: string;
  slug: string;
  color: string;
}

export const categories: Category[] = [
  {
    id: "ai-basics",
    name: "AI Basics",
    nameZh: "AI基础",
    description: "What is AI, how does it work, and what you need to know first.",
    descriptionZh: "什么是AI，它如何工作，以及你需要首先了解什么。",
    icon: "🧠",
    slug: "ai-basics",
    color: "bg-amber-100 text-amber-800 dark:bg-amber-900 dark:text-amber-200",
  },
  {
    id: "ai-tutorials",
    name: "AI Tutorials",
    nameZh: "AI教程",
    description: "Step-by-step guides for ChatGPT, Claude, Midjourney and more.",
    descriptionZh: "ChatGPT、Claude、Midjourney等的分步指南。",
    icon: "📖",
    slug: "ai-tutorials",
    color: "bg-blue-100 text-blue-800 dark:bg-blue-900 dark:text-blue-200",
  },
  {
    id: "ai-use-cases",
    name: "AI Use Cases",
    nameZh: "AI应用场景",
    description: "AI for resumes, presentations, scripts, and real-world tasks.",
    descriptionZh: "AI用于简历、演示文稿、脚本和现实任务。",
    icon: "💼",
    slug: "ai-use-cases",
    color: "bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200",
  },
  {
    id: "ai-comparisons",
    name: "AI Comparisons",
    nameZh: "AI对比",
    description: "ChatGPT vs Claude, Midjourney vs DALL-E — honest side-by-side tests.",
    descriptionZh: "ChatGPT vs Claude，Midjourney vs DALL-E — 客观的对比测试。",
    icon: "⚖️",
    slug: "ai-comparisons",
    color: "bg-purple-100 text-purple-800 dark:bg-purple-900 dark:text-purple-200",
  },
  {
    id: "ai-news",
    name: "AI News",
    nameZh: "AI新闻",
    description: "New models, major updates, and what they actually mean for you.",
    descriptionZh: "新模型、重大更新，以及它们对你的实际意义。",
    icon: "📰",
    slug: "ai-news",
    color: "bg-red-100 text-red-800 dark:bg-red-900 dark:text-red-200",
  },
];
