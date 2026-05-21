export interface Article {
  slug: string;
  title: string;
  titleEs: string;
  titleAr: string;
  description: string;
  descriptionEs: string;
  descriptionAr: string;
  category: string;
  tags: string[];
  difficulty: "beginner" | "intermediate" | "advanced";
  toolsMentioned: string[];
  date: string;
}

export const articles: Article[] = [
  {
    slug: "what-is-chatgpt-beginners-guide",
    title: "What Is ChatGPT? A Beginner's Guide to Getting Started",
    titleEs: "¿Qué es ChatGPT? Guía para Principiantes",
    titleAr: "ما هو ChatGPT؟ دليل المبتدئين للبدء",
    description: "New to ChatGPT? Learn what it is, how it works, and how to start using it today — with real examples and tips.",
    descriptionEs: "¿Nuevo en ChatGPT? Aprende qué es, cómo funciona y cómo empezar a usarlo hoy — con ejemplos y consejos reales.",
    descriptionAr: "جديد في ChatGPT؟ تعرف على ما هو، وكيف يعمل، وكيف تبدأ في استخدامه اليوم — مع أمثلة ونصائح حقيقية.",
    category: "ai-tutorials",
    tags: ["chatgpt", "beginners", "getting-started", "guide"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt"],
    date: "2026-05-15",
  },
  {
    slug: "chatgpt-vs-claude-comparison",
    title: "ChatGPT vs Claude: Which AI Assistant Is Right for You?",
    titleEs: "ChatGPT vs Claude: ¿Cuál Asistente IA es Mejor para Ti?",
    titleAr: "ChatGPT مقابل Claude: أي مساعد ذكاء اصطناعي مناسب لك؟",
    description: "An honest side-by-side comparison of ChatGPT and Claude — covering writing, coding, reasoning, pricing, and real-world use cases.",
    descriptionEs: "Una comparación honesta lado a lado de ChatGPT y Claude — cubriendo escritura, programación, razonamiento, precios y casos de uso reales.",
    descriptionAr: "مقارنة صادقة جنباً إلى جنب بين ChatGPT وClaude — تغطي الكتابة والبرمجة والاستدلال والأسعار وحالات الاستخدام الواقعية.",
    category: "ai-comparisons",
    tags: ["chatgpt", "claude", "comparison", "llm"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt", "claude"],
    date: "2026-05-12",
  },
  {
    slug: "best-ai-tools-for-content-creation",
    title: "10 Best AI Tools for Content Creation in 2026",
    titleEs: "Las 10 Mejores Herramientas de IA para Creación de Contenido en 2026",
    titleAr: "أفضل 10 أدوات ذكاء اصطناعي لإنشاء المحتوى في 2026",
    description: "From writing to image generation to video, discover the top AI tools that content creators are using right now.",
    descriptionEs: "Desde escritura hasta generación de imágenes y video, descubre las mejores herramientas de IA que los creadores de contenido están usando ahora.",
    descriptionAr: "من الكتابة إلى توليد الصور والفيديو، اكتشف أفضل أدوات الذكاء الاصطناعي التي يستخدمها منشئو المحتوى حالياً.",
    category: "ai-use-cases",
    tags: ["content-creation", "tools", "writing", "design"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt", "claude", "midjourney", "canva-ai", "elevenlabs"],
    date: "2026-05-10",
  },
  {
    slug: "how-to-write-better-prompts",
    title: "How to Write Better AI Prompts: A Practical Guide",
    titleEs: "Cómo Escribir Mejores Prompts de IA: Guía Práctica",
    titleAr: "كيفية كتابة أوامر ذكاء اصطناعي أفضل: دليل عملي",
    description: "Master the art of prompt engineering with practical techniques that work across ChatGPT, Claude, Gemini, and more.",
    descriptionEs: "Domina el arte de la ingeniería de prompts con técnicas prácticas que funcionan en ChatGPT, Claude, Gemini y más.",
    descriptionAr: "أتقن فن هندسة الأوامر بتقنيات عملية تعمل مع ChatGPT وClaude وGemini والمزيد.",
    category: "ai-tutorials",
    tags: ["prompt-engineering", "tips", "guide", "best-practices"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt", "claude", "gemini"],
    date: "2026-05-08",
  },
  {
    slug: "midjourney-vs-dalle-3-vs-stable-diffusion",
    title: "Midjourney vs DALL-E 3 vs Stable Diffusion: Image Generator Face-Off",
    titleEs: "Midjourney vs DALL-E 3 vs Stable Diffusion: Comparativa de Generadores de Imagen",
    titleAr: "Midjourney مقابل DALL-E 3 مقابل Stable Diffusion: مواجهة مولدات الصور",
    description: "We test all three AI image generators head-to-head on quality, speed, cost, and ease of use. See which one wins.",
    descriptionEs: "Probamos los tres generadores de imágenes IA cara a cara en calidad, velocidad, costo y facilidad de uso. Ve cuál gana.",
    descriptionAr: "نختبر مولدات الصور بالذكاء الاصطناعي الثلاثة وجهاً لوجه من حيث الجودة والسرعة والتكلفة وسهولة الاستخدام. شاهد من يفوز.",
    category: "ai-comparisons",
    tags: ["midjourney", "dalle", "stable-diffusion", "image-generation"],
    difficulty: "intermediate",
    toolsMentioned: ["midjourney", "dalle3", "stable-diffusion"],
    date: "2026-05-05",
  },
  {
    slug: "ai-tools-for-students",
    title: "AI Tools Every Student Should Know About in 2026",
    titleEs: "Herramientas de IA que Todo Estudiante Debería Conocer en 2026",
    titleAr: "أدوات الذكاء الاصطناعي التي يجب على كل طالب معرفتها في 2026",
    description: "From research to writing to presentations, these AI tools can help students save time and learn better.",
    descriptionEs: "Desde investigación hasta escritura y presentaciones, estas herramientas de IA pueden ayudar a los estudiantes a ahorrar tiempo y aprender mejor.",
    descriptionAr: "من البحث إلى الكتابة إلى العروض التقديمية، يمكن لأدوات الذكاء الاصطناعي هذه مساعدة الطلاب على توفير الوقت والتعلم بشكل أفضل.",
    category: "ai-use-cases",
    tags: ["students", "education", "productivity", "study"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt", "perplexity", "notion-ai", "gamma", "grammarly"],
    date: "2026-05-01",
  },
];
