export interface Category {
  id: string;
  name: string;
  nameEs: string;
  nameAr: string;
  description: string;
  descriptionEs: string;
  descriptionAr: string;
  icon: string;
  slug: string;
  color: string;
}

export const categories: Category[] = [
  {
    id: "ai-basics",
    name: "AI Basics",
    nameEs: "Fundamentos de IA",
    nameAr: "أساسيات الذكاء الاصطناعي",
    description: "What is AI, how does it work, and what you need to know first.",
    descriptionEs: "Qué es la IA, cómo funciona y lo que necesitas saber primero.",
    descriptionAr: "ما هو الذكاء الاصطناعي وكيف يعمل وما تحتاج معرفته أولاً.",
    icon: "🧠",
    slug: "ai-basics",
    color: "bg-amber-100 text-amber-800 dark:bg-amber-900 dark:text-amber-200",
  },
  {
    id: "ai-tutorials",
    name: "AI Tutorials",
    nameEs: "Tutoriales de IA",
    nameAr: "دروس الذكاء الاصطناعي",
    description: "Step-by-step guides for ChatGPT, Claude, Midjourney and more.",
    descriptionEs: "Guías paso a paso para ChatGPT, Claude, Midjourney y más.",
    descriptionAr: "أدلة خطوة بخطوة لـ ChatGPT وClaude وMidjourney والمزيد.",
    icon: "📖",
    slug: "ai-tutorials",
    color: "bg-blue-100 text-blue-800 dark:bg-blue-900 dark:text-blue-200",
  },
  {
    id: "ai-use-cases",
    name: "AI Use Cases",
    nameEs: "Casos de Uso de IA",
    nameAr: "حالات استخدام الذكاء الاصطناعي",
    description: "AI for resumes, presentations, scripts, and real-world tasks.",
    descriptionEs: "IA para currículums, presentaciones, guiones y tareas reales.",
    descriptionAr: "الذكاء الاصطناعي للسير الذاتية والعروض التقديمية والنصوص والمهام الواقعية.",
    icon: "💼",
    slug: "ai-use-cases",
    color: "bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200",
  },
  {
    id: "ai-comparisons",
    name: "AI Comparisons",
    nameEs: "Comparativas de IA",
    nameAr: "مقارنات الذكاء الاصطناعي",
    description: "ChatGPT vs Claude, Midjourney vs DALL-E — honest side-by-side tests.",
    descriptionEs: "ChatGPT vs Claude, Midjourney vs DALL-E — pruebas honestas lado a lado.",
    descriptionAr: "ChatGPT مقابل Claude، Midjourney مقابل DALL-E — مقارنات صادقة جنباً إلى جنب.",
    icon: "⚖️",
    slug: "ai-comparisons",
    color: "bg-purple-100 text-purple-800 dark:bg-purple-900 dark:text-purple-200",
  },
  {
    id: "ai-news",
    name: "AI News",
    nameEs: "Noticias de IA",
    nameAr: "أخبار الذكاء الاصطناعي",
    description: "New models, major updates, and what they actually mean for you.",
    descriptionEs: "Nuevos modelos, actualizaciones importantes y qué significan para ti.",
    descriptionAr: "نماذج جديدة، تحديثات مهمة، وماذا تعني لك فعلاً.",
    icon: "📰",
    slug: "ai-news",
    color: "bg-red-100 text-red-800 dark:bg-red-900 dark:text-red-200",
  },
];
