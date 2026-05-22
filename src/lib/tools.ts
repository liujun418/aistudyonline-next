export interface Tool {
  id: string;
  name: string;
  description: string;
  descriptionEs: string;
  descriptionAr: string;
  category: "chatbots" | "image-generation" | "video-generation" | "writing" | "coding" | "productivity" | "audio" | "learning" | "industry";
  tags: string[];
  difficulty: "beginner" | "intermediate" | "advanced";
  url: string;
  rating: number;
  pricing: string;
  useCase: string;
  icon: string;

  // Company info
  company: string;
  companyEs: string;
  companyAr: string;
  founded: string;
  headquarters: string;

  // Detailed description (250-400 chars)
  descriptionLong: string;
  descriptionLongEs: string;
  descriptionLongAr: string;

  // Advantages (3-5)
  advantages: string[];
  advantagesEs: string[];
  advantagesAr: string[];

  // Use Cases (3-5)
  useCases: string[];
  useCasesEs: string[];
  useCasesAr: string[];

  // Target audience
  targetAudience: string;
  targetAudienceEs: string;
  targetAudienceAr: string;

  // Pricing tiers
  pricingTiers: { tier: string; price: string; features: string[] }[];

  // Extensions / plugins
  extensions: { name: string; description: string; url?: string }[];

  // Related skills
  skills: string[];

  // Pros and Cons
  pros: string[];
  prosEs: string[];
  prosAr: string[];
  cons: string[];
  consEs: string[];
  consAr: string[];
}

export const toolCategories = [
  "chatbots",
  "image-generation",
  "video-generation",
  "writing",
  "coding",
  "productivity",
  "audio",
  "learning",
  "industry",
] as const;

export type ToolCategory = (typeof toolCategories)[number];

export const toolCategoryLabels: Record<ToolCategory, { en: string; es: string; ar: string }> = {
  chatbots: { en: "Chatbots", es: "Chatbots", ar: " chatbots" },
  "image-generation": { en: "Image Gen", es: "Generación de Imágenes", ar: "توليد الصور" },
  "video-generation": { en: "Video Gen", es: "Generación de Video", ar: "توليد الفيديو" },
  writing: { en: "Writing", es: "Escritura", ar: "الكتابة" },
  coding: { en: "Coding", es: "Programación", ar: "البرمجة" },
  productivity: { en: "Productivity", es: "Productividad", ar: "الإنتاجية" },
  audio: { en: "Audio", es: "Audio", ar: "الصوت" },
  learning: { en: "Learning", es: "Aprendizaje", ar: "التعلم" },
  industry: { en: "Industry", es: "Industria", ar: "الصناعة" },
};

function r(n: number): number {
  return Math.min(5, Math.max(1, Math.round(n)));
}

export const tools: Tool[] = [

  {
    id: "chatgpt",
    name: "ChatGPT",
    description: "The most popular AI assistant for conversation, writing, coding, and problem-solving.",
    descriptionEs: "El asistente de IA más popular para conversación, escritura, programación y resolución de problemas.",
    descriptionAr: "أشهر مساعد ذكاء اصطناعي للمحادثة والكتابة والبرمجة وحل المشكلات.",
    category: "chatbots",
    tags: ["conversation", "writing", "coding", "analysis"],
    difficulty: "beginner",
    url: "https://chat.openai.com",
    rating: r(4.7),
    pricing: "Free / $20/mo Plus",
    useCase: "ChatGPT handles general Q&A, content drafting, code generation, and brainstorming. Use it as your daily AI copilot for almost any text-based task.",
    icon: "\u{1F916}",
  company: "OpenAI",
  companyEs: "OpenAI",
  companyAr: "OpenAI",
  founded: "2015",  headquarters: "San Francisco, CA",  
  descriptionLong: "ChatGPT is OpenAI's flagship conversational AI model that has transformed how millions interact with artificial intelligence. Based on GPT-4o and GPT-5, it handles text, images, audio, and code in one unified interface. With web browsing, file uploads, advanced data analysis, custom GPTs, and voice conversations, it serves as a versatile productivity tool.",
  descriptionLongEs: "ChatGPT es el modelo de IA conversacional insignia de OpenAI. Basado en GPT-4o y GPT-5, maneja texto, imagenes, audio y codigo en una interfaz unificada con navegacion web, carga de archivos y analisis avanzado de datos.",
  descriptionLongAr: "ChatGPT هو نموذج الذكاء الاصطناعي التحادثي الرائد من OpenAI. يعتمد على GPT-4o وGPT-5، ويتعامل مع النصوص والصور والصوت والكود في واجهة واحدة.",
  advantages: [
            "Unified multimodal interface for text, images, audio, and code",
            "Extensive plugin ecosystem with custom GPTs and GPT Store",
            "Advanced data analysis with Python execution and file processing"
          ],
  advantagesEs: [
            "Interfaz multimodal unificada para texto, imagenes, audio y codigo",
            "Ecosistema de plugins con GPTs personalizados y GPT Store",
            "Analisis avanzado de datos con ejecucion Python"
          ],
  advantagesAr: [
            "واجهة موحدة متعددة الوسائط للنصوص والصور والصوت والكود",
            "نظام بيئي من الإضافات مع GPTs المخصصة ومتجر GPT",
            "تحليل بيانات متقدم مع تنفيذ Python"
          ],
  useCases: [
            "Draft professional emails, reports, and proposals in minutes",
            "Analyze datasets using natural language instead of SQL",
            "Generate and debug code across multiple languages",
            "Create lesson plans and study guides"
          ],
  useCasesEs: [
            "Redacta correos e informes en minutos",
            "Analiza datos con lenguaje natural",
            "Genera y depura codigo en multiples lenguajes",
            "Crea planes de lecciones y guias"
          ],
  useCasesAr: [
            "صياغة رسائل البريد والتقارير في دقائق",
            "تحليل البيانات باللغة الطبيعية",
            "توليد وتصحيح الأكواد بلغات متعددة",
            "إنشاء خطط الدروس"
          ],
  targetAudience: "Anyone who needs an AI assistant -- students, professionals, writers, developers, and creators.",
  targetAudienceEs: "Cualquier persona que necesite un asistente de IA -- estudiantes, profesionales, escritores, desarrolladores.",
  targetAudienceAr: "أي شخص يحتاج مساعد ذكاء اصطناعي -- الطلاب والمهنيون والكتاب والمطورون.",
  pricingTiers: [
      {
        tier: "Free",
        price: "$0",
        features: [
          "GPT-4o mini access",
          "Limited GPT-5 messages",
          "Basic file uploads"
        ]
      },
      {
        tier: "Plus",
        price: "$20/mo",
        features: [
          "Unlimited GPT-5",
          "Advanced data analysis",
          "DALL-E 3",
          "Custom GPTs"
        ]
      },
      {
        tier: "Pro",
        price: "$200/mo",
        features: [
          "Unlimited GPT-5 Turbo",
          "Priority access",
          "Extended context"
        ]
      }
    ],  
  extensions: [
        {
          name: "ChatGPT for Chrome",
          description: "Official browser extension",
          url: "https://chrome.google.com/webstore"
        },
        {
          name: "ChatGPT Desktop",
          description: "Native apps for Windows and macOS"
        }
      ],  
  skills: [
            "prompt engineering",
            "content creation",
            "data analysis",
            "code generation",
            "conversational AI"
          ],  
  pros: [
            "Free tier with GPT-4o mini and basic features",
            "Massive ecosystem of custom GPTs",
            "Multimodal in a single interface"
          ],
  prosEs: [
            "Nivel gratuito con GPT-4o mini",
            "Ecosistema masivo de GPTs personalizados",
            "Multimodal en una interfaz"
          ],
  prosAr: [
            "طبقة مجانية مع GPT-4o mini",
            "نظام بيئي ضخم من GPTs المخصصة",
            "متعدد الوسائط في واجهة واحدة"
          ],
  cons: [
            "Free tier has limited GPT-5 messages",
            "Can give confidently incorrect answers",
            "No native offline mode"
          ],
  consEs: [
            "Nivel gratuito con mensajes GPT-5 limitados",
            "Puede dar respuestas incorrectas con confianza",
            "Sin modo offline nativo"
          ],
  consAr: [
            "رسائل GPT-5 محدودة في الطبقة المجانية",
            "قد يقدم إجابات غير صحيحة بثقة",
            "لا يوجد وضع غير متصل"
          ],
  },

  {
    id: "claude",
    name: "Claude",
    description: "Anthropic's AI assistant focused on safety, long-form reasoning, and detailed analysis.",
    descriptionEs: "El asistente de IA de Anthropic centrado en seguridad, razonamiento extenso y análisis detallado.",
    descriptionAr: "مساعد الذكاء الاصطناعي من Anthropic يركز على الأمان والاستدلال الطويل والتحليل المفصل.",
    category: "chatbots",
    tags: ["reasoning", "analysis", "writing", "safety"],
    difficulty: "beginner",
    url: "https://claude.ai",
    rating: r(4.6),
    pricing: "Free / $20/mo Pro",
    useCase: "Claude excels at long document analysis, detailed writing tasks, and thoughtful reasoning. Great for research, editing, and complex problem-solving.",
    icon: "\u{1F9E0}",
  company: "Anthropic",
  companyEs: "Anthropic",
  companyAr: "Anthropic",
  founded: "2021",  headquarters: "San Francisco, CA",  
  descriptionLong: "Claude is Anthropic's AI assistant built on advanced language models with emphasis on safety and long-form reasoning. With a 200K+ token context window, Claude excels at processing entire books, research papers, and complex codebases. Known for nuanced writing and thoughtful analysis, it is favored by writers, researchers, and professionals.",
  descriptionLongEs: "Claude es el asistente de IA de Anthropic con enfasis en seguridad y razonamiento extenso. Con mas de 200K tokens de contexto, destaca procesando libros completos y documentos complejos.",
  descriptionLongAr: "Claude هو مساعد الذكاء الاصطناعي من Anthropic مع تركيز على الأمان والاستدلال الطويل. يتفوق في معالجة الكتب والأوراق البحثية.",
  advantages: [
            "200K+ token context window for large documents",
            "Nuanced writing style producing quality prose",
            "Strong safety with Constitutional AI",
            "Excellent at complex instructions"
          ],
  advantagesEs: [
            "Ventana de 200K+ tokens para documentos grandes",
            "Estilo de escritura matizado de calidad",
            "Seguridad solida con IA Constitucional",
            "Excelente en instrucciones complejas"
          ],
  advantagesAr: [
            "نافذة 200 ألف+ رمز للمستندات الكبيرة",
            "أسلوب كتابة دقيق عالي الجودة",
            "أمان قوي بالذكاء الاصطناعي الدستوري",
            "ممتاز في التعليمات المعقدة"
          ],
  useCases: [
            "Analyze 100+ page research papers and legal docs",
            "Edit long-form content like novels and reports",
            "Debug complex codebases step by step",
            "Conduct literature reviews with citations",
            "Generate detailed business reports"
          ],
  useCasesEs: [
            "Analiza documentos de 100+ paginas",
            "Edita contenido extenso",
            "Depura codigo complejo paso a paso",
            "Revisiones bibliograficas con citas"
          ],
  useCasesAr: [
            "تحليل أوراق بحثية من 100+ صفحة",
            "تحرير المحتوى الطويل",
            "تصحيح الأكواد المعقدة خطوة بخطوة",
            "مراجعات أدبية مع استشهادات"
          ],
  targetAudience: "Professionals needing detailed AI assistance -- writers, researchers, lawyers, developers, analysts.",
  targetAudienceEs: "Profesionales que necesitan asistencia detallada de IA.",
  targetAudienceAr: "المهنيون الذين يحتاجون مساعدة ذكاء اصطناعي مفصلة.",
  pricingTiers: [
      {
        tier: "Free",
        price: "$0",
        features: [
          "Claude 4 Sonnet",
          "Limited daily messages",
          "Basic uploads"
        ]
      },
      {
        tier: "Pro",
        price: "$20/mo",
        features: [
          "Unlimited Claude 4 Sonnet",
          "Claude 4 Opus",
          "Projects"
        ]
      },
      {
        tier: "Team",
        price: "$30/user/mo",
        features: [
          "All Pro features",
          "Higher limits",
          "Shared workspaces"
        ]
      }
    ],  
  extensions: [
        {
          name: "Claude Code CLI",
          description: "Command-line coding assistant"
        },
        {
          name: "Claude API",
          description: "Enterprise API with SSO"
        }
      ],  
  skills: [
            "prompt engineering",
            "document analysis",
            "creative writing",
            "code review",
            "research"
          ],  
  pros: [
            "Massive context window for entire books",
            "Superior writing quality",
            "Strong safety without sacrificing capability",
            "Detailed structured responses"
          ],
  prosEs: [
            "Ventana masiva para libros completos",
            "Calidad de escritura superior",
            "Seguridad sin sacrificar capacidad",
            "Respuestas estructuradas"
          ],
  prosAr: [
            "نافذة سياق ضخمة للكتب",
            "جودة كتابة فائقة",
            "أمان دون التضحية بالقدرة",
            "إجابات منظمة"
          ],
  cons: [
            "Strict daily limits on free tier",
            "No image generation",
            "Slower on complex tasks",
            "Limited integrations"
          ],
  consEs: [
            "Limites diarios estrictos",
            "Sin generacion de imagenes",
            "Mas lento en tareas complejas",
            "Integraciones limitadas"
          ],
  consAr: [
            "حدود يومية صارمة",
            "لا توليد صور",
            "أبطأ في المهام المعقدة",
            "تكاملات محدودة"
          ],
  },

  {
    id: "gemini",
    name: "Google Gemini",
    description: "Google's multimodal AI model with deep Google ecosystem integration.",
    descriptionEs: "El modelo de IA multimodal de Google con integración profunda en el ecosistema Google.",
    descriptionAr: "نموذج الذكاء الاصطناعي متعدد الوسائط من Google مع تكامل عميق مع نظام Google البيئي.",
    category: "chatbots",
    tags: ["multimodal", "google", "reasoning", "search"],
    difficulty: "beginner",
    url: "https://gemini.google.com",
    rating: r(4.5),
    pricing: "Free / $19.99/mo Advanced",
    useCase: "Gemini's multimodal capabilities let you upload images, audio, and video for analysis. It integrates with Google apps like Gmail, Docs, and Drive.",
    icon: "\u{1F31F}",
  company: "Google DeepMind",
  companyEs: "Google DeepMind",
  companyAr: "Google DeepMind",
  founded: "2023",  headquarters: "Mountain View, CA",  
  descriptionLong: "Gemini is Google's natively multimodal AI model family built by Google DeepMind. It processes text, images, audio, video, and code simultaneously. Deeply integrated with Gmail, Docs, Drive, and Search, Gemini offers unique advantages for Google ecosystem users with real-time search access and workspace integration.",
  descriptionLongEs: "Gemini es la familia de modelos de IA nativamente multimodal de Google. Procesa texto, imagenes, audio, video y codigo simultaneamente, integrado con Gmail, Docs y Drive.",
  descriptionLongAr: "Gemini هي عائلة نماذج الذكاء الاصطناعي متعددة الوسائط من Google. تعالج النصوص والصور والصوت والفيديو في وقت واحد.",
  advantages: [
            "Native multimodal processing of text/images/audio/video",
            "Deep Google Workspace integration",
            "Real-time Google Search access",
            "Generous free tier"
          ],
  advantagesEs: [
            "Procesamiento multimodal nativo",
            "Integracion profunda con Workspace",
            "Busqueda Google en tiempo real",
            "Nivel gratuito generoso"
          ],
  advantagesAr: [
            "معالجة متعددة الوسائط أصلية",
            "تكامل عميق مع Workspace",
            "بحث Google في الوقت الفعلي",
            "طبقة مجانية سخية"
          ],
  useCases: [
            "Upload video for AI content analysis",
            "Plan trips with Google Maps integration",
            "Analyze Sheets data with natural language",
            "Draft Gmail emails with context"
          ],
  useCasesEs: [
            "Sube video para analisis IA",
            "Planifica viajes con Google Maps",
            "Analiza datos de Sheets",
            "Redacta correos en Gmail"
          ],
  useCasesAr: [
            "تحميل فيديو للتحليل بالذكاء الاصطناعي",
            "تخطيط الرحلات مع Google Maps",
            "تحليل بيانات Sheets",
            "صياغة رسائل Gmail"
          ],
  targetAudience: "Google users who want AI in their workflow -- Gmail, Workspace, and Android users.",
  targetAudienceEs: "Usuarios Google que quieren IA en su flujo de trabajo.",
  targetAudienceAr: "مستخدمو Google الذين يريدون الذكاء الاصطناعي في سير عملهم.",
  pricingTiers: [
      {
        tier: "Free",
        price: "$0",
        features: [
          "Gemini 2.0 Flash",
          "Google Search",
          "File uploads"
        ]
      },
      {
        tier: "Advanced",
        price: "$19.99/mo",
        features: [
          "Gemini 2.0 Pro",
          "1TB Drive storage",
          "Workspace integration"
        ]
      }
    ],  
  extensions: [
        {
          name: "Gemini for Workspace",
          description: "AI across Gmail, Docs, Sheets"
        },
        {
          name: "Gemini Mobile",
          description: "Android/iOS app with voice"
        }
      ],  
  skills: [
            "multimodal AI",
            "Google Workspace",
            "data analysis",
            "video analysis",
            "search"
          ],  
  pros: [
            "Natively multimodal without separate tools",
            "Seamless Google integration",
            "Generous free tier",
            "Real-time search"
          ],
  prosEs: [
            "Nativamente multimodal",
            "Integracion Google perfecta",
            "Nivel gratuito generoso",
            "Busqueda en tiempo real"
          ],
  prosAr: [
            "متعدد الوسائط أصلا",
            "تكامل Google سلس",
            "طبقة مجانية سخية",
            "بحث في الوقت الفعلي"
          ],
  cons: [
            "Weaker creative writing vs Claude/ChatGPT",
            "Privacy concerns with Google",
            "Advanced tier less competitive"
          ],
  consEs: [
            "Escritura creativa debil",
            "Preocupaciones de privacidad",
            "Nivel avanzado menos competitivo"
          ],
  consAr: [
            "كتابة إبداعية أضعف",
            "مخاوف الخصوصية",
            "الطبقة المتقدمة أقل تنافسية"
          ],
  },

  {
    id: "deepseek",
    name: "DeepSeek",
    description: "Open-source LLM with strong reasoning capabilities and competitive performance.",
    descriptionEs: "LLM de código abierto con sólidas capacidades de razonamiento y rendimiento competitivo.",
    descriptionAr: "نموذج لغوي كبير مفتوح المصدر مع قدرات استدلال قوية وأداء تنافسي.",
    category: "chatbots",
    tags: ["reasoning", "open-source", "coding", "analysis"],
    difficulty: "intermediate",
    url: "https://chat.deepseek.com",
    rating: r(4.4),
    pricing: "Free",
    useCase: "DeepSeek offers strong reasoning and coding capabilities at no cost. Its open-source nature allows self-hosting and customization.",
    icon: "\u{1F50D}",
  company: "DeepSeek",
  companyEs: "DeepSeek",
  companyAr: "DeepSeek",
  founded: "2023",  headquarters: "Hangzhou, China",  
  descriptionLong: "DeepSeek is a Chinese AI company known for powerful open-source language models. DeepSeek-R1 and V3 deliver performance comparable to leading proprietary models at a fraction of the cost. Strong in mathematics, coding, and logical reasoning, it is a favorite in the open-source community for transparency and impressive benchmarks.",
  descriptionLongEs: "DeepSeek es una empresa china de IA con potentes modelos open-source. DeepSeek-R1 y V3 ofrecen rendimiento comparable a modelos propietarios a una fraccion del costo.",
  descriptionLongAr: "DeepSeek هي شركة صينية للذكاء الاصطناعي بنماذج مفتوحة المصدر قوية. تقدم أداء comparable بأفضل النماذج المملوكة.",
  advantages: [
            "Fully open-source for self-hosting",
            "Exceptional reasoning and math",
            "Cost-effective API pricing",
            "Strong coding performance"
          ],
  advantagesEs: [
            "Completamente open-source",
            "Razonamiento y matematicas excepcionales",
            "API rentable",
            "Rendimiento en codigo solido"
          ],
  advantagesAr: [
            "مفتوح المصدر بالكامل للاستضافة الذاتية",
            "استدلال ورياضيات استثنائيان",
            "أسعار API فعالة",
            "أداء برمجة قوي"
          ],
  useCases: [
            "Self-host LLM on your infrastructure",
            "Solve complex math problems",
            "Build custom AI apps with open weights",
            "Code generation and debugging"
          ],
  useCasesEs: [
            "Auto-aloja un LLM",
            "Resuelve problemas matematicos",
            "Construye apps de IA",
            "Genera y depura codigo"
          ],
  useCasesAr: [
            "استضافة نموذج لغوي كبير",
            "حل مسائل رياضية معقدة",
            "بناء تطبيقات ذكاء اصطناعي",
            "توليد الأكواد وتصحيحها"
          ],
  targetAudience: "Developers and organizations wanting powerful AI with full control over deployment and privacy.",
  targetAudienceEs: "Desarrolladores que quieren control total sobre su IA.",
  targetAudienceAr: "المطورون الذين يريدون تحكما كاملا في الذكاء الاصطناعي.",
  pricingTiers: [
      {
        tier: "Free Chat",
        price: "$0",
        features: [
          "Unlimited DeepSeek chat",
          "DeepSeek-R1",
          "File uploads"
        ]
      },
      {
        tier: "API",
        price: "From $0.14/M tokens",
        features: [
          "R1 and V3 API",
          "Rate limits",
          "Fine-tuning"
        ]
      }
    ],  
  extensions: [
        {
          name: "DeepSeek API",
          description: "REST API for app integration"
        },
        {
          name: "Ollama Support",
          description: "Run locally via Ollama"
        }
      ],  
  skills: [
            "open-source AI",
            "self-hosting",
            "mathematical reasoning",
            "API integration",
            "fine-tuning"
          ],  
  pros: [
            "Free web chat with no limits",
            "Open-source for self-hosting",
            "Excellent performance-to-cost",
            "Strong reasoning ability"
          ],
  prosEs: [
            "Chat web gratuito sin limites",
            "Open-source para auto-alojamiento",
            "Excelente relacion rendimiento/precio",
            "Gran capacidad de razonamiento"
          ],
  prosAr: [
            "دردشة ويب مجانية بدون حدود",
            "مصدر مفتوح للاستضافة الذاتية",
            "نسبة أداء إلى تكلفة ممتازة",
            "قدرة استدلال قوية"
          ],
  cons: [
            "Inconsistent server availability",
            "Less refined conversation ability",
            "Documentation in Chinese",
            "Limited enterprise support"
          ],
  consEs: [
            "Disponibilidad inconsistente",
            "Conversacion menos refinada",
            "Documentacion en chino",
            "Soporte limitado"
          ],
  consAr: [
            "توفر خادم غير متناسق",
            "محادثة أقل تطورا",
            "وثائق بالصينية",
            "دعم مؤسسي محدود"
          ],
  },

  {
    id: "perplexity",
    name: "Perplexity AI",
    description: "AI-powered search engine that provides answers with real-time citations.",
    descriptionEs: "Buscador impulsado por IA que proporciona respuestas con citas en tiempo real.",
    descriptionAr: "محرك بحث مدعوم بالذكاء الاصطناعي يقدم إجابات مع استشهادات في الوقت الفعلي.",
    category: "chatbots",
    tags: ["search", "research", "citations", "real-time"],
    difficulty: "beginner",
    url: "https://www.perplexity.ai",
    rating: r(4.5),
    pricing: "Free / $20/mo Pro",
    useCase: "Perplexity is an AI search engine that answers questions with cited sources. Perfect for research, fact-checking, and staying updated.",
    icon: "\u{1F4A1}",
  company: "Perplexity AI",
  companyEs: "Perplexity AI",
  companyAr: "Perplexity AI",
  founded: "2022",  headquarters: "San Francisco, CA",  
  descriptionLong: "Perplexity AI combines LLMs with real-time web search to deliver answers with inline citations. Unlike traditional search, it synthesizes multiple sources into coherent answers with references. Supports file uploads, image recognition, and pro features. Its focus on source transparency makes it a favorite for researchers and students.",
  descriptionLongEs: "Perplexity AI combina LLMs con busqueda web en tiempo real para respuestas con citas. Sintetiza multiples fuentes en respuestas coherentes con referencias.",
  descriptionLongAr: "يجمع Perplexity AI بين نماذج اللغة والبحث الفوري لتقديم إجابات مع استشهادات. يجمع المعلومات من مصادر متعددة.",
  advantages: [
            "Answers with real-time citations",
            "Synthesizes multiple sources",
            "File upload analysis",
            "Adjustable focus modes"
          ],
  advantagesEs: [
            "Respuestas con citas en tiempo real",
            "Sintetiza multiples fuentes",
            "Analisis de archivos",
            "Modos de enfoque"
          ],
  advantagesAr: [
            "إجابات مع استشهادات فورية",
            "تجميع مصادر متعددة",
            "تحليل الملفات",
            "أوضاع تركيز"
          ],
  useCases: [
            "Research with cited sources",
            "Fact-check with real-time search",
            "Analyze uploaded documents",
            "Curated news summaries"
          ],
  useCasesEs: [
            "Investigacion con fuentes citadas",
            "Verificacion de datos",
            "Analisis de documentos",
            "Resumenes de noticias"
          ],
  useCasesAr: [
            "بحث بمصادر موثقة",
            "التحقق من الحقائق",
            "تحليل المستندات",
            "ملخصات الأخبار"
          ],
  targetAudience: "Researchers, students, and journalists needing accurate cited information quickly.",
  targetAudienceEs: "Investigadores, estudiantes y periodistas que necesitan informacion precisa con citas.",
  targetAudienceAr: "الباحثون والطلاب والصحفيون الذين يحتاجون معلومات دقيقة مع استشهادات.",
  pricingTiers: [
      {
        tier: "Free",
        price: "$0",
        features: [
          "Standard search",
          "Limited Pro searches",
          "File uploads"
        ]
      },
      {
        tier: "Pro",
        price: "$20/mo",
        features: [
          "Unlimited Pro",
          "Unlimited file analysis",
          "API access"
        ]
      }
    ],  
  extensions: [
        {
          name: "Perplexity Browser Extension",
          description: "Search anywhere on the web"
        },
        {
          name: "Perplexity Mobile",
          description: "iOS and Android apps"
        }
      ],  
  skills: [
            "research",
            "fact-checking",
            "information synthesis",
            "source evaluation",
            "academic writing"
          ],  
  pros: [
            "Cited answers with sources",
            "Excellent for fact-checking",
            "Generous free tier",
            "File analysis capability"
          ],
  prosEs: [
            "Respuestas citadas con fuentes",
            "Excelente para verificacion",
            "Nivel gratuito generoso",
            "Analisis de archivos"
          ],
  prosAr: [
            "إجابات مع استشهادات",
            "ممتاز للتحقق",
            "طبقة مجانية سخية",
            "تحليل الملفات"
          ],
  cons: [
            "Limited creative writing",
            "Pro plan expensive",
            "Quality depends on web search",
            "Weak for coding"
          ],
  consEs: [
            "Escritura creativa limitada",
            "Plan Pro caro",
            "Calidad depende de busqueda",
            "Debil para codigo"
          ],
  consAr: [
            "كتابة إبداعية محدودة",
            "الخطة المدفوعة باهظة",
            "الجودة تعتمد على البحث",
            "ضعيف للبرمجة"
          ],
  },

  {
    id: "midjourney",
    name: "Midjourney",
    description: "Leading AI image generator known for artistic quality and stylistic versatility.",
    descriptionEs: "Generador de imágenes IA líder conocido por su calidad artística y versatilidad estilística.",
    descriptionAr: "مولد الصور بالذكاء الاصطناعي الرائد المعروف بجودته الفنية وتنوعه الأسلوبي.",
    category: "image-generation",
    tags: ["art", "design", "creative", "high-quality"],
    difficulty: "intermediate",
    url: "https://www.midjourney.com",
    rating: r(4.8),
    pricing: "$10/mo starting",
    useCase: "Midjourney produces stunning artistic images from text prompts. Best for concept art, illustrations, branding visuals, and creative projects.",
    icon: "\u{1F3A8}",
  company: "Midjourney Inc.",
  companyEs: "Midjourney Inc.",
  companyAr: "Midjourney Inc.",
  founded: "2021",  headquarters: "San Francisco, CA",  
  descriptionLong: "Midjourney is the highest-quality AI image generation platform, known for its distinctive artistic style. Operating through Discord and web, it excels at concept art, illustrations, and character designs. Its advanced parameter system allows fine-grained control over style, composition, and lighting, making it the go-to for professional artists.",
  descriptionLongEs: "Midjourney es la plataforma de generacion de imagenes IA de mayor calidad. Opera via Discord y web, destacando en arte conceptual e ilustraciones.",
  descriptionLongAr: "Midjourney هي منصة توليد الصور بالذكاء الاصطناعي الأعلى جودة. تعمل عبر Discord والويب وتتفوق في الفن التصوري.",
  advantages: [
            "Highest artistic quality",
            "Advanced parameter control",
            "Strong community references",
            "Regular model updates"
          ],
  advantagesEs: [
            "Maxima calidad artistica",
            "Control avanzado de parametros",
            "Comunidad de referencia",
            "Actualizaciones regulares"
          ],
  advantagesAr: [
            "أعلى جودة فنية",
            "تحكم متقدم بالمعلمات",
            "مراجع مجتمعية قوية",
            "تحديثات منتظمة"
          ],
  useCases: [
            "Concept art for games and films",
            "Brand visuals and marketing",
            "Book illustrations",
            "Product visualizations",
            "Creative prototyping"
          ],
  useCasesEs: [
            "Arte conceptual para juegos",
            "Visuales de marca",
            "Ilustraciones de libros",
            "Visualizaciones de productos"
          ],
  useCasesAr: [
            "فن تصوري للألعاب",
            "تصاميم العلامات التجارية",
            "رسوم توضيحية",
            "تصورات المنتجات"
          ],
  targetAudience: "Artists, designers, and creative professionals needing high-quality AI visuals.",
  targetAudienceEs: "Artistas y disenadores que necesitan imagenes IA de alta calidad.",
  targetAudienceAr: "الفنانون والمصممون الذين يحتاجون صور ذكاء اصطناعي عالية الجودة.",
  pricingTiers: [
      {
        tier: "Basic",
        price: "$10/mo",
        features: [
          "3.3 hrs/month GPU",
          "Commercial license"
        ]
      },
      {
        tier: "Standard",
        price: "$30/mo",
        features: [
          "15 hrs/month GPU",
          "Stealth mode"
        ]
      },
      {
        tier: "Pro",
        price: "$60/mo",
        features: [
          "30 hrs/month GPU",
          "Priority queue"
        ]
      }
    ],  
  extensions: [
        {
          name: "Midjourney Discord Bot",
          description: "Primary interface via Discord"
        },
        {
          name: "Midjourney Web",
          description: "Web editor and gallery"
        }
      ],  
  skills: [
            "prompt engineering",
            "art direction",
            "visual design",
            "composition",
            "color theory"
          ],  
  pros: [
            "Best image quality available",
            "Fine parameter control",
            "Strong community",
            "Regular updates"
          ],
  prosEs: [
            "Mejor calidad de imagen",
            "Control detallado de parametros",
            "Comunidad fuerte",
            "Actualizaciones regulares"
          ],
  prosAr: [
            "أفضل جودة صورة",
            "تحكم دقيق بالمعلمات",
            "مجتمع قوي",
            "تحديثات منتظمة"
          ],
  cons: [
            "Requires Discord",
            "Steep learning curve",
            "No free tier",
            "Limited vs SD with LoRAs"
          ],
  consEs: [
            "Requiere Discord",
            "Curva de aprendizaje",
            "Sin nivel gratuito",
            "Limitado vs SD con LoRAs"
          ],
  consAr: [
            "يتطلب Discord",
            "منحنى تعلم حاد",
            "لا توجد طبقة مجانية",
            "محدود مقارنة بـ SD"
          ],
  },

  {
    id: "dalle3",
    name: "DALL-E 3",
    description: "OpenAI's image generator integrated into ChatGPT with strong prompt adherence.",
    descriptionEs: "Generador de imágenes de OpenAI integrado en ChatGPT con gran fidelidad a las instrucciones.",
    descriptionAr: "مولد الصور من OpenAI المدمج في ChatGPT مع التزام قوي بالتعليمات.",
    category: "image-generation",
    tags: ["openai", "chatgpt", "design", "realistic"],
    difficulty: "beginner",
    url: "https://openai.com/dall-e-3",
    rating: r(4.6),
    pricing: "Included with ChatGPT Plus",
    useCase: "DALL-E 3 generates images directly within ChatGPT. Great for quick visual ideas, social media graphics, and prototyping designs.",
    icon: "\u{1F5BC}️",
  company: "OpenAI",
  companyEs: "OpenAI",
  companyAr: "OpenAI",
  founded: "2015",  headquarters: "San Francisco, CA",  
  descriptionLong: "DALL-E 3 is OpenAI's latest image generation model, integrated into ChatGPT. It excels at following complex prompts with high accuracy, generating detailed images from text. Working within ChatGPT allows iterative refinement through natural conversation. Best for quick visual ideation and integrated workflows.",
  descriptionLongEs: "DALL-E 3 es el modelo de generacion de imagenes de OpenAI integrado en ChatGPT. Destaca siguiendo instrucciones complejas con precision.",
  descriptionLongAr: "DALL-E 3 هو نموذج توليد الصور من OpenAI المدمج في ChatGPT. يتفوق في اتباع التعليمات المعقدة بدقة.",
  advantages: [
            "Integrated into ChatGPT",
            "Excellent prompt adherence",
            "Natural conversation refinement",
            "Included with ChatGPT Plus"
          ],
  advantagesEs: [
            "Integrado en ChatGPT",
            "Excelente adhesion a prompts",
            "Refinamiento por conversacion",
            "Incluido con ChatGPT Plus"
          ],
  advantagesAr: [
            "مدمج في ChatGPT",
            "التزام ممتاز بالتعليمات",
            "تحسين بالمحادثة",
            "مشمول مع ChatGPT Plus"
          ],
  useCases: [
            "Social media graphics",
            "Blog illustrations",
            "Design concept prototyping",
            "Marketing visuals"
          ],
  useCasesEs: [
            "Graficos para redes sociales",
            "Ilustraciones para blogs",
            "Prototipos de diseno",
            "Visuales de marketing"
          ],
  useCasesAr: [
            "رسومات وسائل التواصل",
            "رسوم توضيحية للمدونات",
            "نماذج التصميم",
            "مواد تسويقية"
          ],
  targetAudience: "ChatGPT users wanting integrated image generation without leaving the chat.",
  targetAudienceEs: "Usuarios de ChatGPT que quieren generar imagenes sin salir del chat.",
  targetAudienceAr: "مستخدمو ChatGPT الذين يريدون توليد الصور دون مغادرة الدردشة.",
  pricingTiers: [
      {
        tier: "ChatGPT Free",
        price: "$0",
        features: [
          "Limited DALL-E 3",
          "Basic resolution"
        ]
      },
      {
        tier: "ChatGPT Plus",
        price: "$20/mo",
        features: [
          "Unlimited DALL-E 3",
          "HD resolution"
        ]
      }
    ],  
  extensions: [
        {
          name: "Built into ChatGPT",
          description: "Access via ChatGPT interface"
        }
      ],  
  skills: [
            "prompt engineering",
            "creative visualization",
            "design ideation",
            "image prompting"
          ],  
  pros: [
            "Seamless ChatGPT integration",
            "Excellent prompt following",
            "Fast iteration and refinement"
          ],
  prosEs: [
            "Integracion perfecta con ChatGPT",
            "Sigue instrucciones excelentemente",
            "Iteracion rapida"
          ],
  prosAr: [
            "تكامل سلس مع ChatGPT",
            "اتباع ممتاز للتعليمات",
            "تكرار سريع"
          ],
  cons: [
            "Requires ChatGPT subscription",
            "Less artistic than Midjourney",
            "Not standalone tool"
          ],
  consEs: [
            "Requiere suscripcion ChatGPT",
            "Menos artistico que Midjourney",
            "No es herramienta independiente"
          ],
  consAr: [
            "يتطلب اشتراك ChatGPT",
            "أقل فنية من Midjourney",
            "ليس أداة مستقلة"
          ],
  },

  {
    id: "stable-diffusion",
    name: "Stable Diffusion",
    description: "Open-source image generation model with full local control and customization.",
    descriptionEs: "Modelo de generación de imágenes de código abierto con control local y personalización total.",
    descriptionAr: "نموذج توليد الصور مفتوح المصدر مع تحكم محلي كامل وتخصيص.",
    category: "image-generation",
    tags: ["open-source", "local", "customizable", "free"],
    difficulty: "advanced",
    url: "https://stability.ai",
    rating: r(4.4),
    pricing: "Free (open-source)",
    useCase: "Stable Diffusion runs locally on your hardware with full control. Ideal for developers, researchers, and anyone needing uncensored or customized generation.",
    icon: "\u{26A1}",
  company: "Stability AI",
  companyEs: "Stability AI",
  companyAr: "Stability AI",
  founded: "2020",  headquarters: "London, UK",  
  descriptionLong: "Stable Diffusion is a powerful open-source image generation model running locally on your hardware. Developed by Stability AI, it offers complete control with extensive community support, custom models (LoRAs, Checkpoints), and fine-tuning. Provides unlimited free generation, full privacy, and deep customization through its open ecosystem.",
  descriptionLongEs: "Stable Diffusion es un modelo de generacion de imagenes open-source que se ejecuta localmente. Ofrece control total con extenso soporte comunitario.",
  descriptionLongAr: "Stable Diffusion هو نموذج مفتوح المصدر لتوليد الصور يعمل محليا. يوفر تحكما كاملا بدعم مجتمعي واسع.",
  advantages: [
            "Local execution with full privacy",
            "Free and open-source",
            "Extensive community models",
            "Full customization via fine-tuning"
          ],
  advantagesEs: [
            "Ejecucion local con privacidad",
            "Gratuito y open-source",
            "Modelos comunitarios extensos",
            "Personalizacion completa"
          ],
  advantagesAr: [
            "تشغيل محلي بخصوصية كاملة",
            "مجاني ومفتوح المصدر",
            "نماذج مجتمعية واسعة",
            "تخصيص كامل"
          ],
  useCases: [
            "Unlimited image generation",
            "Custom model fine-tuning",
            "Sensitive content processing",
            "Advanced techniques (ControlNet)",
            "AI image app building"
          ],
  useCasesEs: [
            "Generacion ilimitada",
            "Ajuste de modelos personalizados",
            "Contenido sensible local",
            "Tecnicas avanzadas"
          ],
  useCasesAr: [
            "توليد صور غير محدود",
            "ضبط النماذج المخصصة",
            "معالجة محلية",
            "تقنيات متقدمة"
          ],
  targetAudience: "Developers and power users wanting complete control over AI image generation with no restrictions.",
  targetAudienceEs: "Desarrolladores que quieren control total sobre generacion de imagenes IA.",
  targetAudienceAr: "المطورون الذين يريدون تحكما كاملا في توليد الصور.",
  pricingTiers: [
      {
        tier: "Self-hosted",
        price: "$0",
        features: [
          "Unlimited generation",
          "Full privacy",
          "All models"
        ]
      },
      {
        tier: "API",
        price: "Pay-as-you-go",
        features: [
          "Cloud hosted",
          "API access",
          "No GPU needed"
        ]
      }
    ],  
  extensions: [
        {
          name: "Automatic1111 WebUI",
          description: "Most popular SD interface"
        },
        {
          name: "ComfyUI",
          description: "Node-based workflow interface"
        }
      ],  
  skills: [
            "model fine-tuning",
            "LoRA training",
            "prompt engineering",
            "ControlNet",
            "image processing"
          ],  
  pros: [
            "Free with unlimited generation",
            "Full privacy local execution",
            "Extensive community ecosystem",
            "Deep customization"
          ],
  prosEs: [
            "Gratuito sin limites",
            "Privacidad total local",
            "Ecosistema comunitario extenso",
            "Personalizacion profunda"
          ],
  prosAr: [
            "مجاني بدون حدود",
            "خصوصية كاملة محلية",
            "نظام بيئي مجتمعي واسع",
            "تخصيص عميق"
          ],
  cons: [
            "Requires powerful GPU",
            "Steep learning curve",
            "Complex setup",
            "No official mobile app"
          ],
  consEs: [
            "Requiere GPU potente",
            "Curva de aprendizaje",
            "Instalacion compleja",
            "Sin app movil oficial"
          ],
  consAr: [
            "يتطلب GPU قوي",
            "منحنى تعلم حاد",
            "إعداد معقد",
            "لا يوجد تطبيق جوال رسمي"
          ],
  },

  {
    id: "adobe-firefly",
    name: "Adobe Firefly",
    description: "Adobe's generative AI suite integrated with Creative Cloud for professional design.",
    descriptionEs: "Suite de IA generativa de Adobe integrada con Creative Cloud para diseño profesional.",
    descriptionAr: "مجموعة الذكاء الاصطناعي التوليدي من Adobe المدمجة مع Creative Cloud للتصميم الاحترافي.",
    category: "image-generation",
    tags: ["adobe", "design", "professional", "integration"],
    difficulty: "intermediate",
    url: "https://www.adobe.com/products/firefly.html",
    rating: r(4.3),
    pricing: "Free tier / Creative Cloud subscription",
    useCase: "Firefly integrates AI image generation into Adobe's design tools. Best for designers who already use Photoshop, Illustrator, or Express.",
    icon: "\u{1F525}",
  company: "Adobe Inc.",
  companyEs: "Adobe Inc.",
  companyAr: "Adobe Inc.",
  founded: "1982",  headquarters: "San Jose, CA",  
  descriptionLong: "Adobe Firefly is Adobe's generative AI family integrated into Creative Cloud. It enables designers to generate images, apply effects, and extend compositions using natural language. Commercially safe with licensed training data and enterprise-grade features, Firefly is ideal for professional design workflows in Photoshop, Illustrator, and Express.",
  descriptionLongEs: "Adobe Firefly es la familia de IA generativa de Adobe en Creative Cloud. Permite generar imagenes y efectos con lenguaje natural. Disenado para flujos de trabajo profesionales.",
  descriptionLongAr: "Adobe Firefly هي عائلة الذكاء الاصطناعي التوليدي من Adobe في Creative Cloud. تتيح توليد الصور والتأثيرات باللغة الطبيعية.",
  advantages: [
            "Deep Creative Cloud integration",
            "Commercially safe training",
            "Generative Fill for photo editing",
            "Enterprise-grade security"
          ],
  advantagesEs: [
            "Integracion profunda con Creative Cloud",
            "Entrenamiento comercialmente seguro",
            "Relleno generativo",
            "Seguridad empresarial"
          ],
  advantagesAr: [
            "تكامل عميق مع Creative Cloud",
            "تدريب آمن تجاريا",
            "التعبئة التوليدية",
            "أمان مؤسسي"
          ],
  useCases: [
            "Generative Fill in Photoshop",
            "Social media graphics in Express",
            "AI text effects",
            "Image extension",
            "Brand asset variations"
          ],
  useCasesEs: [
            "Relleno generativo en Photoshop",
            "Graficos en Express",
            "Efectos de texto IA",
            "Extension de imagen"
          ],
  useCasesAr: [
            "التعبئة التوليدية في Photoshop",
            "رسومات Express",
            "تأثيرات نصية بالذكاء الاصطناعي",
            "توسيع الصورة"
          ],
  targetAudience: "Professional designers using Creative Cloud who want integrated AI capabilities.",
  targetAudienceEs: "Disenadores profesionales de Creative Cloud que quieren IA integrada.",
  targetAudienceAr: "المصممون المحترفون في Creative Cloud.",
  pricingTiers: [
      {
        tier: "Free",
        price: "$0",
        features: [
          "25 credits/month",
          "Basic features",
          "Express access"
        ]
      },
      {
        tier: "Premium",
        price: "$4.99/mo",
        features: [
          "100 credits/month",
          "Full features",
          "Commercial use"
        ]
      }
    ],  
  extensions: [
        {
          name: "Adobe Photoshop",
          description: "Generative Fill built in"
        },
        {
          name: "Adobe Express",
          description: "Quick AI design tool"
        }
      ],  
  skills: [
            "photo editing",
            "graphic design",
            "brand design",
            "creative direction",
            "commercial art"
          ],  
  pros: [
            "Seamless Creative Cloud integration",
            "Commercially safe",
            "Best-in-class Generative Fill",
            "Enterprise ready"
          ],
  prosEs: [
            "Integracion Creative Cloud perfecta",
            "Comercialmente seguro",
            "Relleno generativo de primera",
            "Listo para empresas"
          ],
  prosAr: [
            "تكامل سلس مع Creative Cloud",
            "آمن تجاريا",
            "تعبئة توليدية من الطراز الأول",
            "جاهز للمؤسسات"
          ],
  cons: [
            "Requires CC subscription",
            "Limited free credits",
            "Less artistic freedom",
            "Adobe ecosystem only"
          ],
  consEs: [
            "Requiere suscripcion CC",
            "Creditos gratis limitados",
            "Menos libertad artistica",
            "Solo ecosistema Adobe"
          ],
  consAr: [
            "يتطلب اشتراك CC",
            "اعتمادات مجانية محدودة",
            "حرية فنية أقل",
            "نظام Adobe فقط"
          ],
  },

  {
    id: "leonardo-ai",
    name: "Leonardo AI",
    description: "AI image generation platform with fine-tuned models for games, characters, and assets.",
    descriptionEs: "Plataforma de generación de imágenes IA con modelos ajustados para juegos, personajes y activos.",
    descriptionAr: "منصة توليد الصور بالذكاء الاصطناعي بنماذج مضبوطة للألعاب والشخصيات والأصول.",
    category: "image-generation",
    tags: ["gaming", "assets", "characters", "models"],
    difficulty: "intermediate",
    url: "https://leonardo.ai",
    rating: r(4.4),
    pricing: "Free tier / from $10/mo",
    useCase: "Leonardo AI offers specialized models for game assets, character design, and environment art. Great for indie game developers and content creators.",
    icon: "\u{1F58C}️",
  company: "Leonardo AI",
  companyEs: "Leonardo AI",
  companyAr: "Leonardo AI",
  founded: "2022",  headquarters: "Sydney, Australia",  
  descriptionLong: "Leonardo AI is a specialized image generation platform for game assets, character design, and environment art. It offers fine-tuned models for different art styles from realistic to anime. Features include AI canvas for in-painting, real-time generation, and dataset creation tools. Popular among indie game developers and content creators.",
  descriptionLongEs: "Leonardo AI es una plataforma especializada para activos de juegos y diseno de personajes. Ofrece modelos ajustados para diferentes estilos artisticos.",
  descriptionLongAr: "Leonardo AI هي منصة متخصصة لأصول الألعاب وتصميم الشخصيات. تقدم نماذج مضبوطة لأنماط فنية مختلفة.",
  advantages: [
            "Specialized game asset models",
            "AI canvas for in-painting",
            "Real-time generation",
            "Community model sharing"
          ],
  advantagesEs: [
            "Modelos especializados para juegos",
            "Lienzo AI para pintar",
            "Generacion en tiempo real",
            "Modelos comunitarios"
          ],
  advantagesAr: [
            "نماذج متخصصة لأصول الألعاب",
            "لوحة AI للرسم",
            "توليد في الوقت الفعلي",
            "نماذج مجتمعية"
          ],
  useCases: [
            "Game character design",
            "Environment texture creation",
            "Marketing game visuals",
            "Concept art pipeline",
            "Custom model training"
          ],
  useCasesEs: [
            "Diseno de personajes",
            "Texturas de entorno",
            "Visuales de marketing",
            "Arte conceptual"
          ],
  useCasesAr: [
            "تصميم شخصيات الألعاب",
            "أنسجة البيئة",
            "مواد تسويقية",
            "فن تصوري"
          ],
  targetAudience: "Game developers, indie creators, and digital artists needing specialized AI for game assets.",
  targetAudienceEs: "Desarrolladores de juegos y artistas digitales que necesitan IA para activos.",
  targetAudienceAr: "مطورو الألعاب والفنانون الرقميون.",
  pricingTiers: [
      {
        tier: "Free",
        price: "$0",
        features: [
          "150 tokens/day",
          "Standard models"
        ]
      },
      {
        tier: "Starter",
        price: "$10/mo",
        features: [
          "2500 tokens/month",
          "Faster generation"
        ]
      },
      {
        tier: "Pro",
        price: "$24/mo",
        features: [
          "8000 tokens/month",
          "API access"
        ]
      }
    ],  
  extensions: [
        {
          name: "Leonardo Web App",
          description: "Full web-based creation platform"
        }
      ],  
  skills: [
            "game art",
            "character design",
            "environment art",
            "texture creation",
            "concept art"
          ],  
  pros: [
            "Specialized for game assets",
            "Generous free tier",
            "Real-time generation",
            "Custom model training"
          ],
  prosEs: [
            "Especializado en juegos",
            "Nivel gratuito generoso",
            "Generacion en tiempo real",
            "Entrenamiento personalizado"
          ],
  prosAr: [
            "متخصص في أصول الألعاب",
            "طبقة مجانية سخية",
            "توليد فوري",
            "تدريب مخصص"
          ],
  cons: [
            "Token limits on usage",
            "Inconsistent quality",
            "Less photorealistic output",
            "Smaller community"
          ],
  consEs: [
            "Limites de tokens",
            "Calidad inconsistente",
            "Menos fotorrealista",
            "Comunidad pequena"
          ],
  consAr: [
            "حدود الرموز",
            "جودة غير متسقة",
            "أقل واقعية",
            "مجتمع أصغر"
          ],
  },

  {
    id: "runway",
    name: "Runway",
    description: "Professional AI video generation and editing platform with advanced motion control.",
    descriptionEs: "Plataforma profesional de generación y edición de video con IA y control avanzado de movimiento.",
    descriptionAr: "منصة احترافية لتوليد وتحرير الفيديو بالذكاء الاصطناعي مع تحكم متقدم في الحركة.",
    category: "video-generation",
    tags: ["video", "editing", "motion", "professional"],
    difficulty: "intermediate",
    url: "https://runwayml.com",
    rating: r(4.5),
    pricing: "Free tier / from $15/mo",
    useCase: "Runway generates and edits video using AI. Use it for creating short films, social media clips, and professional video content with text prompts.",
    icon: "\u{1F3AC}",
  company: "Runway ML",
  companyEs: "Runway ML",
  companyAr: "Runway ML",
  founded: "2018",  headquarters: "New York, NY",  
  descriptionLong: "Runway is a professional AI video generation and editing platform with advanced motion control. It offers text-to-video, image-to-video, and video-to-video generation along with powerful editing tools like in-painting, motion tracking, and green screen removal. Used by filmmakers, content creators, and studios for rapid video production.",
  descriptionLongEs: "Runway es una plataforma profesional de generacion y edicion de video con IA. Ofrece texto-a-video, imagen-a-video y herramientas de edicion avanzadas.",
  descriptionLongAr: "Runway هي منصة احترافية لتوليد وتحرير الفيديو بالذكاء الاصطناعي. تقدم تحويل النص إلى فيديو والصورة إلى فيديو.",
  advantages: [
            "Advanced motion control",
            "Multiple generation modes",
            "Professional editing tools",
            "Real-time collaboration"
          ],
  advantagesEs: [
            "Control avanzado de movimiento",
            "Multiples modos de generacion",
            "Herramientas de edicion",
            "Colaboracion en tiempo real"
          ],
  advantagesAr: [
            "تحكم متقدم في الحركة",
            "أوضاع توليد متعددة",
            "أدوات تحرير احترافية",
            "تعاون في الوقت الفعلي"
          ],
  useCases: [
            "Short film and video creation",
            "Social media video content",
            "Video background removal",
            "Motion tracking and editing",
            "AI video effects"
          ],
  useCasesEs: [
            "Creacion de cortometrajes",
            "Contenido para redes",
            "Eliminacion de fondos",
            "Edicion con IA"
          ],
  useCasesAr: [
            "إنشاء أفلام قصيرة",
            "محتوى فيديو للتواصل الاجتماعي",
            "إزالة الخلفية",
            "تحرير الفيديو بالذكاء الاصطناعي"
          ],
  targetAudience: "Video creators, filmmakers, and content producers who want AI-powered video generation and editing.",
  targetAudienceEs: "Creadores de video y cineastas que quieren IA para video.",
  targetAudienceAr: "منتجو الفيديو وصناع الأفلام.",
  pricingTiers: [
      {
        tier: "Free",
        price: "$0",
        features: [
          "Limited generations",
          "720p export"
        ]
      },
      {
        tier: "Pro",
        price: "$15/mo",
        features: [
          "Unlimited generations",
          "4K export",
          "Green screen"
        ]
      },
      {
        tier: "Team",
        price: "$30/mo",
        features: [
          "All Pro",
          "Collaboration",
          "Priority support"
        ]
      }
    ],  
  extensions: [
        {
          name: "Runway Browser",
          description: "Web-based editing platform"
        }
      ],  
  skills: [
            "video editing",
            "motion graphics",
            "content creation",
            "visual effects",
            "storyboarding"
          ],  
  pros: [
            "Multiple video generation modes",
            "Professional editing tools",
            "Real-time collaboration",
            "Regular feature updates"
          ],
  prosEs: [
            "Multiples modos de generacion",
            "Herramientas profesionales",
            "Colaboracion en tiempo real",
            "Actualizaciones frecuentes"
          ],
  prosAr: [
            "أوضاع توليد فيديو متعددة",
            "أدوات تحرير احترافية",
            "تعاون فوري",
            "تحديثات منتظمة"
          ],
  cons: [
            "Expensive pro plans",
            "Learning curve for advanced features",
            "Generation quality varies",
            "Limited free tier"
          ],
  consEs: [
            "Planes Pro caros",
            "Curva de aprendizaje",
            "Calidad variable",
            "Nivel gratuito limitado"
          ],
  consAr: [
            "خطط مدفوعة باهظة",
            "منحنى تعلم",
            "جودة متغيرة",
            "طبقة مجانية محدودة"
          ],
  },

  {
    id: "pika",
    name: "Pika",
    description: "Easy-to-use AI video generator focused on quick, high-quality video creation.",
    descriptionEs: "Generador de video IA fácil de usar centrado en la creación rápida de videos de alta calidad.",
    descriptionAr: "مولد فيديو بالذكاء الاصطناعي سهل الاستخدام يركز على إنشاء فيديوهات عالية الجودة بسرعة.",
    category: "video-generation",
    tags: ["video", "quick", "social-media", "easy"],
    difficulty: "beginner",
    url: "https://pika.art",
    rating: r(4.3),
    pricing: "Free tier / from $10/mo",
    useCase: "Pika makes AI video generation accessible to everyone. Great for creating short video clips, animations, and social media content from text prompts.",
    icon: "\u{1F3A5}",
  company: "Pika Labs",
  companyEs: "Pika Labs",
  companyAr: "Pika Labs",
  founded: "2023",  headquarters: "San Francisco, CA",  
  descriptionLong: "Pika is an easy-to-use AI video generator focused on quick, high-quality video creation from text and image prompts. It excels at short-form content with features like video in-painting, style transfer, and motion control. Designed for accessibility, Pika makes AI video generation available to everyone without technical expertise.",
  descriptionLongEs: "Pika es un generador de video IA facil de usar para creacion rapida de videos de calidad a partir de texto e imagenes.",
  descriptionLongAr: "Pika هو مولد فيديو بالذكاء الاصطناعي سهل الاستخدام لإنشاء فيديوهات سريعة من النص والصور.",
  advantages: [
            "Easy to use interface",
            "Quick video generation",
            "Text and image prompts",
            "Video in-painting"
          ],
  advantagesEs: [
            "Interfaz facil de usar",
            "Generacion rapida",
            "Prompts de texto e imagen",
            "Pintura en video"
          ],
  advantagesAr: [
            "واجهة سهلة الاستخدام",
            "توليد سريع",
            "أوامر نصية وصورية",
            "الرسم على الفيديو"
          ],
  useCases: [
            "Short social media clips",
            "Animated marketing content",
            "Creative video effects",
            "Quick video prototyping"
          ],
  useCasesEs: [
            "Clips para redes sociales",
            "Contenido animado",
            "Efectos creativos",
            "Prototipos de video"
          ],
  useCasesAr: [
            "مقاطع قصيرة للتواصل الاجتماعي",
            "محتوى تسويقي متحرك",
            "تأثيرات إبداعية",
            "نماذج فيديو سريعة"
          ],
  targetAudience: "Social media creators and marketers who want easy AI video generation without technical skills.",
  targetAudienceEs: "Creadores de redes sociales que quieren generacion facil de video IA.",
  targetAudienceAr: "منشئو المحتاجون إلى توليد فيديو سهل.",
  pricingTiers: [
      {
        tier: "Free",
        price: "$0",
        features: [
          "Limited generations",
          "Standard quality"
        ]
      },
      {
        tier: "Pro",
        price: "$10/mo",
        features: [
          "More generations",
          "HD quality",
          "Faster queue"
        ]
      }
    ],  
  extensions: [
        {
          name: "Pika Web App",
          description: "Browser-based video generation"
        }
      ],  
  skills: [
            "video creation",
            "social media content",
            "creative effects",
            "animation"
          ],  
  pros: [
            "Very easy to use",
            "Fast generation speed",
            "Good for social media",
            "Free tier available"
          ],
  prosEs: [
            "Muy facil de usar",
            "Generacion rapida",
            "Buena para redes",
            "Nivel gratuito"
          ],
  prosAr: [
            "سهل الاستخدام جدا",
            "توليد سريع",
            "جيد للتواصل الاجتماعي",
            "طبقة مجانية"
          ],
  cons: [
            "Limited video length",
            "Less control over output",
            "Lower quality than Runway",
            "Fewer features"
          ],
  consEs: [
            "Duracion limitada",
            "Menos control",
            "Menor calidad que Runway",
            "Menos funciones"
          ],
  consAr: [
            "مدة فيديو محدودة",
            "تحكم أقل",
            "جودة أقل من Runway",
            "ميزات أقل"
          ],
  },

  {
    id: "heygen",
    name: "HeyGen",
    description: "AI video platform for creating talking avatars and professional presentations.",
    descriptionEs: "Plataforma de video IA para crear avatares parlantes y presentaciones profesionales.",
    descriptionAr: "منصة فيديو بالذكاء الاصطناعي لإنشاء صور رمزية متحدثة وعروض تقديمية احترافية.",
    category: "video-generation",
    tags: ["avatars", "presentation", "talking", "business"],
    difficulty: "intermediate",
    url: "https://www.heygen.com",
    rating: r(4.4),
    pricing: "Free tier / from $29/mo",
    useCase: "HeyGen creates talking-head videos from text or scripts using realistic avatars. Perfect for training videos, marketing content, and global communications.",
    icon: "\u{1F3AD}",
  company: "HeyGen",
  companyEs: "HeyGen",
  companyAr: "HeyGen",
  founded: "2020",  headquarters: "Los Angeles, CA",  
  descriptionLong: "HeyGen is an AI video platform for creating talking avatars and professional presentations. It generates realistic talking-head videos from text or scripts using digital avatars. Features include multi-language support, custom avatar creation, and template-based video production. Popular for training videos, marketing content, and corporate communications.",
  descriptionLongEs: "HeyGen es una plataforma de video IA para crear avatares parlantes. Genera videos realistas a partir de texto con avatares digitales y soporte multilingue.",
  descriptionLongAr: "HeyGen هي منصة فيديو بالذكاء الاصطناعي لإنشاء صور رمزية متحدثة. تولد فيديوهات واقعية من النص.",
  advantages: [
            "Realistic talking avatars",
            "Multi-language support",
            "Custom avatar creation",
            "Template library"
          ],
  advantagesEs: [
            "Avatares parlantes realistas",
            "Soporte multilingue",
            "Avatares personalizados",
            "Biblioteca de plantillas"
          ],
  advantagesAr: [
            "صور رمزية متحدثة واقعية",
            "دعم متعدد اللغات",
            "صور رمزية مخصصة",
            "مكتبة قوالب"
          ],
  useCases: [
            "Training and educational videos",
            "Marketing video content",
            "Corporate communications",
            "Multi-language content",
            "Social media avatars"
          ],
  useCasesEs: [
            "Videos educativos",
            "Contenido de marketing",
            "Comunicaciones corporativas",
            "Contenido multilingue"
          ],
  useCasesAr: [
            "فيديوهات تعليمية",
            "محتوى تسويقي",
            "اتصالات مؤسسية",
            "محتوى متعدد اللغات"
          ],
  targetAudience: "Businesses and content creators who need professional talking-head videos at scale.",
  targetAudienceEs: "Empresas que necesitan videos profesionales con avatares parlantes.",
  targetAudienceAr: "الشركات التي تحتاج فيديوهات احترافية.",
  pricingTiers: [
      {
        tier: "Free",
        price: "$0",
        features: [
          "1 min video",
          "Watermark",
          "Basic avatars"
        ]
      },
      {
        tier: "Creator",
        price: "$29/mo",
        features: [
          "10 mins/month",
          "No watermark",
          "HD export"
        ]
      },
      {
        tier: "Business",
        price: "$89/mo",
        features: [
          "30 mins/month",
          "Custom avatars",
          "Priority support"
        ]
      }
    ],  
  extensions: [
        {
          name: "HeyGen Web",
          description: "Browser-based video creation platform"
        }
      ],  
  skills: [
            "video production",
            "avatar creation",
            "voiceover",
            "multi-language content",
            "corporate training"
          ],  
  pros: [
            "Realistic avatar quality",
            "Multi-language support",
            "Fast video production",
            "Professional templates"
          ],
  prosEs: [
            "Avatares realistas",
            "Soporte multilingue",
            "Produccion rapida",
            "Plantillas profesionales"
          ],
  prosAr: [
            "صور رمزية واقعية",
            "دعم متعدد اللغات",
            "إنتاج سريع",
            "قوالب احترافية"
          ],
  cons: [
            "Expensive compared to alternatives",
            "Avatars can feel uncanny",
            "Limited creative control",
            "Watermark on free tier"
          ],
  consEs: [
            "Caro vs alternativas",
            "Avatares pueden parecer extranos",
            "Control creativo limitado",
            "Marca de agua gratis"
          ],
  consAr: [
            "باهظ مقارنة بالبدائل",
            "الصور الرمزية غير طبيعية",
            "تحكم إبداعي محدود",
            "علامة مائية مجانا"
          ],
  },

  {
    id: "jasper",
    name: "Jasper AI",
    description: "AI writing assistant built for marketing teams and content creators.",
    descriptionEs: "Asistente de escritura IA diseñado para equipos de marketing y creadores de contenido.",
    descriptionAr: "مساعد كتابة بالذكاء الاصطناعي مصمم لفرق التسويق ومنشئي المحتوى.",
    category: "writing",
    tags: ["marketing", "content", "copywriting", "brand"],
    difficulty: "beginner",
    url: "https://www.jasper.ai",
    rating: r(4.3),
    pricing: "from $49/mo",
    useCase: "Jasper specializes in marketing copy, blog posts, and brand content. It uses brand voice customization to produce consistent on-brand writing.",
    icon: "\u{270D}️",
  company: "Jasper AI",
  companyEs: "Jasper AI",
  companyAr: "Jasper AI",
  founded: "2021",  headquarters: "Austin, TX",  
  descriptionLong: "Jasper is an AI writing assistant built for marketing teams and content creators. It specializes in creating brand-aligned copy, blog posts, social media content, and ad copy. With brand voice customization, SEO tools, and team collaboration features, Jasper helps businesses produce consistent on-brand content at scale.",
  descriptionLongEs: "Jasper es un asistente de escritura IA para equipos de marketing. Se especializa en copy alineado con la marca, blogs y contenido para redes.",
  descriptionLongAr: "Jasper هو مساعد كتابة بالذكاء الاصطناعي لفرق التسويق. يتخصص في إنشاء محتوى متوافق مع العلامة التجارية.",
  advantages: [
            "Brand voice customization",
            "SEO-optimized content",
            "Team collaboration",
            "Template library"
          ],
  advantagesEs: [
            "Personalizacion de voz de marca",
            "Contenido SEO",
            "Colaboracion en equipo",
            "Biblioteca de plantillas"
          ],
  advantagesAr: [
            "تخصيص صوت العلامة التجارية",
            "محتوى محسن لمحركات البحث",
            "تعاون فريقي",
            "مكتبة قوالب"
          ],
  useCases: [
            "Marketing copy and ads",
            "Blog post writing",
            "Social media content",
            "Email campaigns",
            "Product descriptions"
          ],
  useCasesEs: [
            "Copy de marketing",
            "Redaccion de blogs",
            "Contenido redes",
            "Campanas de email"
          ],
  useCasesAr: [
            "نسخ تسويقية",
            "كتابة المدونات",
            "محتوى وسائل التواصل",
            "حملات البريد الإلكتروني"
          ],
  targetAudience: "Marketing teams and content creators who need consistent brand-aligned copy at scale.",
  targetAudienceEs: "Equipos de marketing que necesitan copy consistente a escala.",
  targetAudienceAr: "فرق التسويق التي تحتاج محتوى متسق.",
  pricingTiers: [
      {
        tier: "Creator",
        price: "$49/mo",
        features: [
          "1 user",
          "50+ templates",
          "SEO mode"
        ]
      },
      {
        tier: "Pro",
        price: "$69/mo",
        features: [
          "3 users",
          "Brand voice",
          "Custom templates"
        ]
      }
    ],  
  extensions: [
        {
          name: "Jasper Chrome Extension",
          description: "Write anywhere on the web"
        }
      ],  
  skills: [
            "copywriting",
            "content marketing",
            "SEO writing",
            "brand voice",
            "email marketing"
          ],  
  pros: [
            "Brand voice consistency",
            "SEO integration",
            "Team features",
            "Good template variety"
          ],
  prosEs: [
            "Consistencia de voz de marca",
            "Integracion SEO",
            "Funciones de equipo",
            "Variedad de plantillas"
          ],
  prosAr: [
            "اتساق صوت العلامة",
            "تكامل SEO",
            "ميزات الفريق",
            "تنوع القوالب"
          ],
  cons: [
            "Expensive for individuals",
            "Output can feel templated",
            "Better alternatives for free",
            "Overkill for simple tasks"
          ],
  consEs: [
            "Caro para individuos",
            "Output puede ser generico",
            "Mejores alternativas gratis",
            "Excesivo para tareas simples"
          ],
  consAr: [
            "باهظ للأفراد",
            "المخرجات قد تكون نمطية",
            "بدائل مجانية أفضل",
            "مبالغ للمهام البسيطة"
          ],
  },

  {
    id: "copy-ai",
    name: "Copy.ai",
    description: "AI copywriting tool for sales, marketing, and social media content.",
    descriptionEs: "Herramienta de copywriting IA para ventas, marketing y contenido de redes sociales.",
    descriptionAr: "أداة كتابة إعلانات بالذكاء الاصطناعي للمبيعات والتسويق ومحتوى وسائل التواصل الاجتماعي.",
    category: "writing",
    tags: ["copywriting", "sales", "marketing", "social-media"],
    difficulty: "beginner",
    url: "https://www.copy.ai",
    rating: r(4.2),
    pricing: "Free tier / from $36/mo",
    useCase: "Copy.ai generates sales copy, email campaigns, and social media posts quickly. Ideal for marketers who need批量 content fast without sacrificing quality.",
    icon: "\u{1F4DD}",
  company: "Copy.ai",
  companyEs: "Copy.ai",
  companyAr: "Copy.ai",
  founded: "2020",  headquarters: "San Francisco, CA",  
  descriptionLong: "Copy.ai is an AI copywriting tool for sales, marketing, and social media content. It generates sales copy, email campaigns, blog content, and social media posts quickly. With workflow automation features and a user-friendly interface, it helps marketers produce bulk content efficiently without sacrificing quality.",
  descriptionLongEs: "Copy.ai es una herramienta de copywriting IA para ventas, marketing y redes. Genera copy de ventas, campanas de email y contenido rapido.",
  descriptionLongAr: "Copy.ai هي أداة كتابة إعلانات بالذكاء الاصطناعي للمبيعات والتسويق. تولد نصوص مبيعات وحملات بريد إلكتروني.",
  advantages: [
            "Quick content generation",
            "Workflow automation",
            "Multi-platform support",
            "User-friendly interface"
          ],
  advantagesEs: [
            "Generacion rapida",
            "Automatizacion de flujo",
            "Soporte multiplataforma",
            "Interfaz amigable"
          ],
  advantagesAr: [
            "توليد سريع",
            "أتمتة سير العمل",
            "دعم متعدد المنصات",
            "واجهة سهلة"
          ],
  useCases: [
            "Sales copy generation",
            "Email campaign writing",
            "Social media posts",
            "Blog content",
            "Product descriptions"
          ],
  useCasesEs: [
            "Copy de ventas",
            "Campanas de email",
            "Posts redes",
            "Contenido blog"
          ],
  useCasesAr: [
            "نصوص مبيعات",
            "حملات البريد",
            "منشورات التواصل",
            "محتوى المدونات"
          ],
  targetAudience: "Marketers and sales professionals who need fast content generation for multiple platforms.",
  targetAudienceEs: "Profesionales de marketing que necesitan contenido rapido.",
  targetAudienceAr: "مسوقون يحتاجون محتوى سريع لمنصات متعددة.",
  pricingTiers: [
      {
        tier: "Free",
        price: "$0",
        features: [
          "2000 words/month",
          "1 user",
          "Basic templates"
        ]
      },
      {
        tier: "Pro",
        price: "$36/mo",
        features: [
          "Unlimited words",
          "5 users",
          "Workflows"
        ]
      }
    ],  
  extensions: [
        {
          name: "Copy.ai Chrome Extension",
          description: "Write anywhere"
        }
      ],  
  skills: [
            "copywriting",
            "email marketing",
            "social media",
            "content automation",
            "sales writing"
          ],  
  pros: [
            "Fast content generation",
            "Workflow automations",
            "Good free tier",
            "Easy to use"
          ],
  prosEs: [
            "Generacion rapida",
            "Automatizaciones",
            "Buen nivel gratuito",
            "Facil de usar"
          ],
  prosAr: [
            "توليد سريع",
            "أتمتة سير العمل",
            "طبقة مجانية جيدة",
            "سهل الاستخدام"
          ],
  cons: [
            "Output needs editing",
            "Less brand voice control",
            "Generic templates",
            "Limited long-form"
          ],
  consEs: [
            "Output necesita edicion",
            "Menos control de voz",
            "Plantillas genericas",
            "Formato largo limitado"
          ],
  consAr: [
            "المخرجات تحتاج تحرير",
            "تحكم أقل بصوت العلامة",
            "قوالب عامة",
            "نصوص طويلة محدودة"
          ],
  },

  {
    id: "notion-ai",
    name: "Notion AI",
    description: "AI-powered writing and knowledge management integrated into Notion workspaces.",
    descriptionEs: "Escritura impulsada por IA y gestión del conocimiento integrada en espacios de trabajo Notion.",
    descriptionAr: "الكتابة المدعومة بالذكاء الاصطناعي وإدارة المعرفة المدمجة في مساحات عمل Notion.",
    category: "productivity",
    tags: ["notes", "knowledge", "writing", "organization"],
    difficulty: "beginner",
    url: "https://www.notion.so/product/ai",
    rating: r(4.5),
    pricing: "$10/mo add-on to Notion plan",
    useCase: "Notion AI assists with drafting, summarizing, and editing inside your Notion workspace. Use it for meeting notes, project docs, and knowledge base articles.",
    icon: "\u{1F4CB}",
  company: "Notion Labs",
  companyEs: "Notion Labs",
  companyAr: "Notion Labs",
  founded: "2013",  headquarters: "San Francisco, CA",  
  descriptionLong: "Notion AI brings AI-powered writing and knowledge management directly into your Notion workspace. It assists with drafting, summarizing, editing, and brainstorming inside your existing docs and databases. Seamlessly integrated, it can translate, fix spelling, generate action items from meeting notes, and help organize your knowledge base without switching tools.",
  descriptionLongEs: "Notion AI integra escritura IA y gestion del conocimiento en tu espacio de trabajo Notion. Asiste con redaccion, resumen y edicion.",
  descriptionLongAr: "Notion AI يدمج الكتابة بالذكاء الاصطناعي في مساحة عمل Notion. يساعد في الصياغة والتلخيص والتحرير.",
  advantages: [
            "Integrated into Notion workspace",
            "AI writing and editing",
            "Knowledge management",
            "Meeting notes automation"
          ],
  advantagesEs: [
            "Integrado en Notion",
            "Escritura y edicion IA",
            "Gestion del conocimiento",
            "Automacion de notas"
          ],
  advantagesAr: [
            "مدمج في Notion",
            "كتابة وتحرير بالذكاء الاصطناعي",
            "إدارة المعرفة",
            "أتمتة ملاحظات الاجتماعات"
          ],
  useCases: [
            "Meeting notes summarization",
            "Doc drafting and editing",
            "Knowledge base Q&A",
            "Project planning",
            "Content translation"
          ],
  useCasesEs: [
            "Resumen de reuniones",
            "Redaccion de documentos",
            "Base de conocimiento",
            "Planificacion"
          ],
  useCasesAr: [
            "تلخيص الاجتماعات",
            "صياغة المستندات",
            "قاعدة المعرفة",
            "التخطيط"
          ],
  targetAudience: "Existing Notion users who want AI assistance integrated into their workspace without switching tools.",
  targetAudienceEs: "Usuarios de Notion que quieren IA integrada en su espacio.",
  targetAudienceAr: "مستخدمو Notion الذين يريدون الذكاء الاصطناعي في مساحة عملهم.",
  pricingTiers: [
      {
        tier: "Add-on",
        price: "$10/mo",
        features: [
          "Per member",
          "AI writing",
          "Auto-fill databases"
        ]
      }
    ],  
  extensions: [
        {
          name: "Notion AI Built-in",
          description: "Available in all Notion workspaces"
        }
      ],  
  skills: [
            "knowledge management",
            "note-taking",
            "project management",
            "writing",
            "documentation"
          ],  
  pros: [
            "Deep Notion integration",
            "Useful for summarization",
            "Q&A over knowledge base",
            "Non-disruptive workflow"
          ],
  prosEs: [
            "Integracion profunda",
            "Util para resumenes",
            "Preguntas sobre base",
            "Flujo no disruptivo"
          ],
  prosAr: [
            "تكامل عميق مع Notion",
            "مفيد للتلخيص",
            "أسئلة على قاعدة المعرفة",
            "سير عمل غير معطل"
          ],
  cons: [
            "Requires Notion subscription",
            "Add-on cost",
            "Less powerful than dedicated AI",
            "Notion dependency"
          ],
  consEs: [
            "Requiere suscripcion Notion",
            "Costo adicional",
            "Menos potente que IA dedicada",
            "Dependencia de Notion"
          ],
  consAr: [
            "يتطلب اشتراك Notion",
            "تكلفة إضافية",
            "أقل قوة من الذكاء الاصطناعي المخصص",
            "اعتماد على Notion"
          ],
  },

  {
    id: "grammarly",
    name: "Grammarly",
    description: "AI writing assistant for grammar checking, style improvement, and tone adjustment.",
    descriptionEs: "Asistente de escritura IA para corrección gramatical, mejora de estilo y ajuste de tono.",
    descriptionAr: "مساعد كتابة بالذكاء الاصطناعي للتدقيق النحوي وتحسين الأسلوب وضبط النبرة.",
    category: "writing",
    tags: ["grammar", "writing", "editing", "style"],
    difficulty: "beginner",
    url: "https://www.grammarly.com",
    rating: r(4.6),
    pricing: "Free / $12/mo Premium",
    useCase: "Grammarly checks grammar, clarity, engagement, and delivery across emails, documents, and web forms. Essential for professional and error-free writing.",
    icon: "\u{2705}",
  company: "Grammarly",
  companyEs: "Grammarly",
  companyAr: "Grammarly",
  founded: "2009",  headquarters: "San Francisco, CA",  
  descriptionLong: "Grammarly is an AI writing assistant for grammar checking, style improvement, and tone adjustment. It works across emails, documents, and web forms with features including real-time grammar correction, plagiarism detection, tone detection, and style suggestions. Used by millions for professional and error-free writing across all platforms.",
  descriptionLongEs: "Grammarly es un asistente de escritura IA para correccion gramatical, mejora de estilo y ajuste de tono. Funciona en correos, documentos y formularios web.",
  descriptionLongAr: "Grammarly هو مساعد كتابة بالذكاء الاصطناعي للتدقيق النحوي وتحسين الأسلوب. يعمل عبر البريد الإلكتروني والمستندات.",
  advantages: [
            "Real-time grammar checking everywhere",
            "Tone detection and adjustment",
            "Plagiarism detection",
            "Style and clarity suggestions"
          ],
  advantagesEs: [
            "Correccion en tiempo real",
            "Deteccion de tono",
            "Deteccion de plagio",
            "Sugerencias de estilo"
          ],
  advantagesAr: [
            "تدقيق نحوي فوري",
            "كشف النبرة",
            "كشف الاقتباس",
            "اقتراحات الأسلوب"
          ],
  useCases: [
            "Professional email writing",
            "Academic essay editing",
            "Business document polish",
            "Social media posts",
            "Creative writing refinement"
          ],
  useCasesEs: [
            "Escritura de correos",
            "Edicion de ensayos",
            "Documentos profesionales",
            "Posts redes"
          ],
  useCasesAr: [
            "كتابة البريد الإلكتروني",
            "تحرير المقالات",
            "المستندات المهنية",
            "منشورات التواصل"
          ],
  targetAudience: "Anyone who writes professionally -- students, professionals, writers, and non-native speakers wanting error-free writing.",
  targetAudienceEs: "Cualquier persona que escribe profesionalmente -- estudiantes, profesionales y escritores.",
  targetAudienceAr: "أي شخص يكتب بشكل احترافي.",
  pricingTiers: [
      {
        tier: "Free",
        price: "$0",
        features: [
          "Basic grammar",
          "Spelling",
          "Punctuation"
        ]
      },
      {
        tier: "Premium",
        price: "$12/mo",
        features: [
          "Full grammar",
          "Tone detection",
          "Plagiarism"
        ]
      },
      {
        tier: "Business",
        price: "$15/user/mo",
        features: [
          "All Premium",
          "Style guide",
          "Analytics"
        ]
      }
    ],  
  extensions: [
        {
          name: "Grammarly for Chrome",
          description: "Browser extension for all sites"
        },
        {
          name: "Grammarly Desktop",
          description: "Windows and Mac app"
        }
      ],  
  skills: [
            "grammar",
            "writing",
            "editing",
            "proofreading",
            "style"
          ],  
  pros: [
            "Works everywhere via extension",
            "Excellent grammar detection",
            "Tone analysis helpful",
            "Generous free tier"
          ],
  prosEs: [
            "Funciona en todas partes",
            "Deteccion gramatical excelente",
            "Analisis de tono util",
            "Buen nivel gratuito"
          ],
  prosAr: [
            "يعمل في كل مكان",
            "كشف نحوي ممتاز",
            "تحليل النبرة مفيد",
            "طبقة مجانية جيدة"
          ],
  cons: [
            "Premium expensive",
            "Privacy concerns with content",
            "Over-zealous suggestions",
            "Can slow down browsers"
          ],
  consEs: [
            "Premium caro",
            "Preocupaciones de privacidad",
            "Sugerencias excesivas",
            "Ralentiza navegadores"
          ],
  consAr: [
            "بريميوم باهظ",
            "مخاوف الخصوصية",
            "اقتراحات مفرطة",
            "يبطئ المتصفحات"
          ],
  },

  {
    id: "cursor",
    name: "Cursor",
    description: "AI-first code editor built on VS Code with deep AI integration for faster development.",
    descriptionEs: "Editor de código con IA basado en VS Code con integración profunda de IA para desarrollo más rápido.",
    descriptionAr: "محرر أكواد يعتمد على الذكاء الاصطناعي مبني على VS Code مع تكامل عميق للذكاء الاصطناعي لتطوير أسرع.",
    category: "coding",
    tags: ["ide", "code-generation", "vs-code", "productivity"],
    difficulty: "intermediate",
    url: "https://cursor.sh",
    rating: r(4.7),
    pricing: "Free / $20/mo Pro",
    useCase: "Cursor is an AI-native code editor that understands your codebase. It offers autocomplete, inline editing, and chat-based code generation.",
    icon: "\u{1F4BB}",
  company: "Anysphere",
  companyEs: "Anysphere",
  companyAr: "Anysphere",
  founded: "2022",  headquarters: "San Francisco, CA",  
  descriptionLong: "Cursor is an AI-first code editor built on VS Code with deep AI integration. It offers AI-powered autocomplete, inline editing, multi-file editing, and chat-based code generation that understands your entire codebase. With features like AI context awareness and agent mode, Cursor dramatically accelerates development speed.",
  descriptionLongEs: "Cursor es un editor de codigo con IA basado en VS Code. Ofrece autocompletado IA, edicion inline y chat que entiende tu base de codigo.",
  descriptionLongAr: "Cursor هو محرر أكواد يعتمد على الذكاء الاصطناعي مبني على VS Code. يوفر إكمال تلقائي بالذكاء الاصطناعي وتحرير داخلي.",
  advantages: [
            "VS Code compatible",
            "AI understands full codebase",
            "Multi-file editing",
            "Agent mode for complex tasks"
          ],
  advantagesEs: [
            "Compatible con VS Code",
            "IA entiende toda la base",
            "Edicion multi-archivo",
            "Modo agente"
          ],
  advantagesAr: [
            "متوافق مع VS Code",
            "يفهم قاعدة الأكواد الكاملة",
            "تحرير متعدد الملفات",
            "وضع الوكيل"
          ],
  useCases: [
            "Full-stack web development",
            "Code refactoring across files",
            "Bug fixing with AI",
            "Learning new codebases",
            "Rapid prototyping"
          ],
  useCasesEs: [
            "Desarrollo web full-stack",
            "Refactorizacion",
            "Correccion de bugs",
            "Aprendizaje de bases"
          ],
  useCasesAr: [
            "تطوير ويب شامل",
            "إعادة هيكلة الكود",
            "إصلاح الأخطاء",
            "تعلم قواعد الأكواد"
          ],
  targetAudience: "Developers who want AI deeply integrated into their code editor for faster development.",
  targetAudienceEs: "Desarrolladores que quieren IA integrada en su editor de codigo.",
  targetAudienceAr: "المطورون الذين يريدون ذكاء اصطناعيا مدمجا في محرر الأكواد.",
  pricingTiers: [
      {
        tier: "Free",
        price: "$0",
        features: [
          "200 AI completions",
          "Basic chat"
        ]
      },
      {
        tier: "Pro",
        price: "$20/mo",
        features: [
          "Unlimited AI",
          "Agent mode",
          "Multi-file edit"
        ]
      }
    ],  
  extensions: [
        {
          name: "Cursor Editor",
          description: "Standalone VS Code fork with AI"
        }
      ],  
  skills: [
            "software development",
            "code refactoring",
            "debugging",
            "full-stack",
            "pair programming"
          ],  
  pros: [
            "Deep VS Code integration",
            "Codebase-aware AI",
            "Excellent autocomplete",
            "Agent mode powerful"
          ],
  prosEs: [
            "Integracion VS Code",
            "IA consciente del codigo",
            "Autocompletado excelente",
            "Modo agente potente"
          ],
  prosAr: [
            "تكامل VS Code عميق",
            "ذكاء اصطناعي واعي بالكود",
            "إكمال تلقائي ممتاز",
            "وضع وكيل قوي"
          ],
  cons: [
            "Requires subscription for full features",
            "Can be resource heavy",
            "Still maturing",
            "Pro plan expensive"
          ],
  consEs: [
            "Requiere suscripcion",
            "Pesado en recursos",
            "En maduracion",
            "Plan Pro caro"
          ],
  consAr: [
            "يتطلب اشتراكا",
            "ثقيل على الموارد",
            "لا يزال في النضج",
            "الخطة المدفوعة باهظة"
          ],
  },

  {
    id: "github-copilot",
    name: "GitHub Copilot",
    description: "AI pair programmer from GitHub that suggests code in real-time across popular IDEs.",
    descriptionEs: "Programador par IA de GitHub que sugiere código en tiempo real en IDEs populares.",
    descriptionAr: "مبرمج زوجي بالذكاء الاصطناعي من GitHub يقترح الأكواد في الوقت الفعلي عبر بيئات التطوير الشهيرة.",
    category: "coding",
    tags: ["code-generation", "ide", "github", "pair-programming"],
    difficulty: "intermediate",
    url: "https://github.com/features/copilot",
    rating: r(4.6),
    pricing: "Free / $10/mo Individual",
    useCase: "Copilot provides real-time code suggestions as you type. It integrates with VS Code, JetBrains, and Neovim for seamless AI-assisted development.",
    icon: "\u{1F91D}",
  company: "GitHub (Microsoft)",
  companyEs: "GitHub (Microsoft)",
  companyAr: "GitHub (Microsoft)",
  founded: "2008",  headquarters: "San Francisco, CA",  
  descriptionLong: "GitHub Copilot is an AI pair programmer from GitHub that suggests code in real-time across popular IDEs including VS Code, JetBrains, and Neovim. Powered by OpenAI's Codex models, it offers context-aware code completions, chat-based coding help, and pull request summaries. Copilot has become the standard for AI-assisted development.",
  descriptionLongEs: "GitHub Copilot es un programador par IA que sugiere codigo en tiempo real en IDEs populares. Impulsado por modelos Codex de OpenAI.",
  descriptionLongAr: "GitHub Copilot هو مبرمج زوجي بالذكاء الاصطناعي يقترح أكواد في الوقت الفعلي. مدعوم بنماذج Codex من OpenAI.",
  advantages: [
            "Integrated in major IDEs",
            "Context-aware suggestions",
            "Chat-based coding help",
            "PR summary generation"
          ],
  advantagesEs: [
            "Integrado en IDEs principales",
            "Sugerencias contextuales",
            "Ayuda por chat",
            "Resumenes de PR"
          ],
  advantagesAr: [
            "مدمج في بيئات التطوير الرئيسية",
            "اقتراحات سياقية",
            "مساعدة بالدردشة",
            "ملخصات طلبات السحب"
          ],
  useCases: [
            "Real-time code completion",
            "Chat-based code generation",
            "Pull request descriptions",
            "Code explanation",
            "Test generation"
          ],
  useCasesEs: [
            "Completado de codigo",
            "Generacion por chat",
            "Descripciones de PR",
            "Explicacion de codigo"
          ],
  useCasesAr: [
            "إكمال الكود في الوقت الفعلي",
            "توليد الكود بالدردشة",
            "أوصاف طلبات السحب",
            "شرح الكود"
          ],
  targetAudience: "Developers using VS Code, JetBrains, or Neovim who want AI code suggestions in their existing IDE.",
  targetAudienceEs: "Desarrolladores que usan VS Code, JetBrains o Neovim que quieren sugerencias IA.",
  targetAudienceAr: "المطورون الذين يستخدمون VS Code أو JetBrains أو Neovim ويريدون اقتراحات أكواد بالذكاء الاصطناعي في بيئة التطوير الحالية.",
  pricingTiers: [
      {
        tier: "Free",
        price: "$0",
        features: [
          "2000 completions/month",
          "Code chat"
        ]
      },
      {
        tier: "Individual",
        price: "$10/mo",
        features: [
          "Unlimited",
          "Multi-file",
          "PR summaries"
        ]
      }
    ],  
  extensions: [
        {
          name: "Copilot for VS Code",
          description: "VS Code extension"
        },
        {
          name: "Copilot for JetBrains",
          description: "JetBrains IDE plugin"
        }
      ],  
  skills: [
            "software development",
            "code completion",
            "pair programming",
            "debugging",
            "code review"
          ],  
  pros: [
            "Works in existing IDEs",
            "Context-aware completions",
            "Good for boilerplate",
            "Free for students"
          ],
  prosEs: [
            "Funciona en IDEs existentes",
            "Completado contextual",
            "Bueno para boilerplate",
            "Gratis para estudiantes"
          ],
  prosAr: [
            "يعمل في بيئات التطوير الحالية",
            "إكمال سياقي",
            "جيد للكود المتكرر",
            "مجاني للطلاب"
          ],
  cons: [
            "Less powerful than Cursor agent",
            "Can suggest insecure code",
            "Limited multi-file context",
            "Pro plan needed"
          ],
  consEs: [
            "Menos potente que Cursor",
            "Puede sugerir codigo inseguro",
            "Contexto multi-archivo limitado",
            "Requiere plan Pro"
          ],
  consAr: [
            "أقل قوة من Cursor",
            "قد يقترح كودا غير آمن",
            "سياق محدود",
            "يتطلب خطة مدفوعة"
          ],
  },

  {
    id: "replit-ai",
    name: "Replit AI",
    description: "Browser-based IDE with built-in AI agent that can build and deploy apps from prompts.",
    descriptionEs: "IDE basado en navegador con agente IA integrado que puede construir y desplegar apps desde instrucciones.",
    descriptionAr: "بيئة تطوير متكاملة في المتصفح مع وكيل ذكاء اصطناعي مدمج يمكنه بناء ونشر التطبيقات من التعليمات.",
    category: "coding",
    tags: ["ide", "deploy", "no-setup", "agent"],
    difficulty: "beginner",
    url: "https://replit.com",
    rating: r(4.3),
    pricing: "Free / $20/mo Pro",
    useCase: "Replit AI can generate entire applications from a prompt, run them in the browser, and deploy them. Great for prototyping and learning to code.",
    icon: "\u{1F527}",
  company: "Replit",
  companyEs: "Replit",
  companyAr: "Replit",
  founded: "2016",  headquarters: "San Francisco, CA",  
  descriptionLong: "Replit AI is a browser-based IDE with a built-in AI agent that can build and deploy applications from natural language prompts. It requires zero setup -- just describe what you want and the AI agent creates, runs, and deploys the app. Perfect for beginners learning to code, rapid prototyping, and building MVPs without local development setup.",
  descriptionLongEs: "Replit AI es un IDE en navegador con agente IA que construye y despliega apps desde prompts. Ideal para principiantes y prototipado rapido.",
  descriptionLongAr: "Replit AI هي بيئة تطوير متكاملة في المتصفح مع وكيل ذكاء اصطناعي يبني وينشر التطبيقات من الأوامر.",
  advantages: [
            "Zero setup browser IDE",
            "AI builds entire apps",
            "Instant deployment",
            "Collaboration built-in"
          ],
  advantagesEs: [
            "IDE sin configuracion",
            "IA construye apps completas",
            "Despliegue instantaneo",
            "Colaboracion integrada"
          ],
  advantagesAr: [
            "بيئة تطوير بدون إعداد",
            "الذكاء الاصطناعي يبني التطبيقات",
            "نشر فوري",
            "تعاون مدمج"
          ],
  useCases: [
            "Rapid app prototyping",
            "Learning to code interactively",
            "Building MVPs quickly",
            "Collaborative development",
            "Deploying side projects"
          ],
  useCasesEs: [
            "Prototipado rapido",
            "Aprender a programar",
            "Creacion de MVPs",
            "Desarrollo colaborativo"
          ],
  useCasesAr: [
            "نمذجة سريعة",
            "تعلم البرمجة",
            "بناء نماذج أولية",
            "تطوير تعاوني"
          ],
  targetAudience: "Beginners learning to code and developers who want rapid prototyping without local setup.",
  targetAudienceEs: "Principiantes que aprenden a programar y desarrolladores para prototipado rapido.",
  targetAudienceAr: "المبتدئون في تعلم البرمجة والمطورون الذين يريدون نمذجة سريعة بدون إعداد محلي.",
  pricingTiers: [
      {
        tier: "Free",
        price: "$0",
        features: [
          "Limited compute",
          "AI agent access",
          "Public projects"
        ]
      },
      {
        tier: "Pro",
        price: "$20/mo",
        features: [
          "Unlimited compute",
          "Private projects",
          "Faster AI"
        ]
      }
    ],  
  extensions: [
        {
          name: "Replit Browser",
          description: "Web-based IDE and deployment"
        }
      ],  
  skills: [
            "full-stack",
            "rapid prototyping",
            "web development",
            "deployment",
            "collaborative coding"
          ],  
  pros: [
            "Zero setup required",
            "AI builds full apps",
            "Built-in deployment",
            "Great for learning"
          ],
  prosEs: [
            "Sin configuracion",
            "IA construye apps completas",
            "Despliegue integrado",
            "Excelente para aprender"
          ],
  prosAr: [
            "لا حاجة للإعداد",
            "ي builds تطبيقات كاملة",
            "نشر مدمج",
            "ممتاز للتعلم"
          ],
  cons: [
            "Limited for complex apps",
            "Free tier computing limits",
            "Requires internet",
            "Less control than local"
          ],
  consEs: [
            "Limitado para apps complejas",
            "Limites de computo",
            "Requiere internet",
            "Menos control que local"
          ],
  consAr: [
            "محدود للتطبيقات المعقدة",
            "حدود حسابية",
            "يتطلب الإنترنت",
            "تحكم أقل من المحلي"
          ],
  },

  {
    id: "gamma",
    name: "Gamma",
    description: "AI-powered presentation tool that creates slides, documents, and web pages from text.",
    descriptionEs: "Herramienta de presentaciones IA que crea diapositivas, documentos y páginas web desde texto.",
    descriptionAr: "أداة عروض تقديمية بالذكاء الاصطناعي تنشئ شرائح ومستندات وصفحات ويب من النص.",
    category: "productivity",
    tags: ["presentation", "slides", "design", "documents"],
    difficulty: "beginner",
    url: "https://gamma.app",
    rating: r(4.5),
    pricing: "Free tier / from $10/mo",
    useCase: "Gamma generates beautiful presentations, documents, and web pages from a simple text prompt. Perfect for students, educators, and business professionals.",
    icon: "\u{1F4CA}",
  company: "Gamma",
  companyEs: "Gamma",
  companyAr: "Gamma",
  founded: "2020",  headquarters: "San Francisco, CA",  
  descriptionLong: "Gamma is an AI-powered presentation tool that creates slides, documents, and web pages from text prompts. It generates beautifully designed content with smart layouts, images, and consistent themes automatically. Unlike traditional presentation tools, Gamma handles the design so users focus on content. Perfect for students, educators, and professionals.",
  descriptionLongEs: "Gamma es una herramienta de presentaciones IA que crea diapositivas, documentos y paginas web desde texto. Genera disenos hermosos automaticamente.",
  descriptionLongAr: "Gamma هي أداة عروض تقديمية بالذكاء الاصطناعي تنشئ شرائح ومستندات وصفحات ويب من النص.",
  advantages: [
            "AI generates complete presentations",
            "Smart auto-layout",
            "Web pages and docs too",
            "Beautiful design templates"
          ],
  advantagesEs: [
            "Presentaciones completas por IA",
            "Maquetacion automatica",
            "Tambien paginas web",
            "Plantillas hermosas"
          ],
  advantagesAr: [
            "عروض تقديمية كاملة بالذكاء الاصطناعي",
            "تخطيط تلقائي ذكي",
            "صفحات ويب أيضا",
            "قوالب جميلة"
          ],
  useCases: [
            "Business presentations",
            "Educational slide decks",
            "Project proposals",
            "Web page creation",
            "Pitch decks"
          ],
  useCasesEs: [
            "Presentaciones empresariales",
            "Diapositivas educativas",
            "Propuestas",
            "Creacion de paginas web"
          ],
  useCasesAr: [
            "عروض تقديمية تجارية",
            "شرائح تعليمية",
            "مقترحات المشاريع",
            "إنشاء صفحات ويب"
          ],
  targetAudience: "Students, educators, and professionals who want AI-generated presentations and documents quickly.",
  targetAudienceEs: "Estudiantes y profesionales que quieren presentaciones generadas por IA rapidamente.",
  targetAudienceAr: "الطلاب والمعلمون والمهنيون الذين يريدون عروضا تقديمية ومستندات بالذكاء الاصطناعي بسرعة.",
  pricingTiers: [
      {
        tier: "Free",
        price: "$0",
        features: [
          "Limited AI credits",
          "Basic templates"
        ]
      },
      {
        tier: "Pro",
        price: "$10/mo",
        features: [
          "Unlimited AI",
          "All templates",
          "Export options"
        ]
      }
    ],  
  extensions: [
        {
          name: "Gamma Web App",
          description: "Browser-based creation tool"
        }
      ],  
  skills: [
            "presentation design",
            "content creation",
            "visual storytelling",
            "document design"
          ],  
  pros: [
            "Fast presentation creation",
            "Beautiful auto-design",
            "Multi-format output",
            "Easy to use"
          ],
  prosEs: [
            "Creacion rapida",
            "Diseno automatico hermoso",
            "Multi-formato",
            "Facil de usar"
          ],
  prosAr: [
            "إنشاء سريع",
            "تصميم تلقائي جميل",
            "إخراج متعدد التنسيقات",
            "سهل الاستخدام"
          ],
  cons: [
            "Limited customization",
            "Less control than PowerPoint",
            "AI designs not always perfect",
            "Subscription needed"
          ],
  consEs: [
            "Personalizacion limitada",
            "Menos control que PowerPoint",
            "Disenos no siempre perfectos",
            "Suscripcion necesaria"
          ],
  consAr: [
            "تخصيص محدود",
            "تحكم أقل من PowerPoint",
            "تصاميم غير مثالية دائما",
            "اشتراك مطلوب"
          ],
  },

  {
    id: "beautiful-ai",
    name: "Beautiful.ai",
    description: "AI presentation tool with smart templates that auto-layout your content beautifully.",
    descriptionEs: "Herramienta de presentaciones IA con plantillas inteligentes que maquetan tu contenido automáticamente.",
    descriptionAr: "أداة عروض تقديمية بالذكاء الاصطناعي مع قوالب ذكية تقوم تلقائياً بتنسيق المحتوى الخاص بك بشكل جميل.",
    category: "productivity",
    tags: ["presentation", "design", "templates", "business"],
    difficulty: "beginner",
    url: "https://www.beautiful.ai",
    rating: r(4.2),
    pricing: "from $12/mo",
    useCase: "Beautiful.ai's smart slides auto-arrange your content into professional layouts. Best for business presentations where design consistency matters.",
    icon: "✨",
  company: "Beautiful.ai",
  companyEs: "Beautiful.ai",
  companyAr: "Beautiful.ai",
  founded: "2015",  headquarters: "San Francisco, CA",  
  descriptionLong: "Beautiful.ai is an AI presentation tool with smart templates that auto-layout your content. As you add content, the AI automatically arranges it into professional designs with consistent spacing, alignment, and styling. It enforces design rules so presentations always look polished without manual formatting. Best for business presentations needing design consistency.",
  descriptionLongEs: "Beautiful.ai es una herramienta de presentaciones con plantillas inteligentes que maquetan tu contenido automaticamente en disenos profesionales.",
  descriptionLongAr: "Beautiful.ai هي أداة عروض تقديمية بقوالب ذكية تقوم تلقائيا بتنسيق المحتوى بشكل احترافي.",
  advantages: [
            "Smart auto-layout technology",
            "Design consistency enforcement",
            "Professional templates",
            "Team collaboration"
          ],
  advantagesEs: [
            "Maquetacion inteligente",
            "Consistencia de diseno",
            "Plantillas profesionales",
            "Colaboracion en equipo"
          ],
  advantagesAr: [
            "تخطيط تلقائي ذكي",
            "اتساق التصميم",
            "قوالب احترافية",
            "تعاون فريقي"
          ],
  useCases: [
            "Business presentations",
            "Sales decks",
            "Investor pitches",
            "Team reports",
            "Brand presentations"
          ],
  useCasesEs: [
            "Presentaciones de negocio",
            "Deck de ventas",
            "Pitches de inversion",
            "Informes de equipo"
          ],
  useCasesAr: [
            "عروض تجارية",
            "عروض المبيعات",
            "عروض المستثمرين",
            "تقارير الفريق"
          ],
  targetAudience: "Business professionals who need consistent, professional presentations without design skills.",
  targetAudienceEs: "Profesionales que necesitan presentaciones profesionales consistentes sin habilidades de diseno.",
  targetAudienceAr: "المهنيون في مجال الأعمال الذين يحتاجون عروضا تقديمية متسقة واحترافية دون مهارات تصميم.",
  pricingTiers: [
      {
        tier: "Pro",
        price: "$12/mo",
        features: [
          "Unlimited presentations",
          "All templates",
          "Export"
        ]
      },
      {
        tier: "Team",
        price: "$40/user/mo",
        features: [
          "All Pro",
          "Team library",
          "Brand control"
        ]
      }
    ],  
  extensions: [
        {
          name: "Beautiful.ai Web",
          description: "Browser-based presentation tool"
        }
      ],  
  skills: [
            "presentation design",
            "business communication",
            "visual storytelling",
            "brand consistency"
          ],  
  pros: [
            "Auto-layout saves time",
            "Design consistency",
            "Professional output",
            "Good for teams"
          ],
  prosEs: [
            "Maquetacion automatica",
            "Consistencia de diseno",
            "Output profesional",
            "Bueno para equipos"
          ],
  prosAr: [
            "توفير الوقت بالتخطيط التلقائي",
            "اتساق التصميم",
            "مخرجات احترافية",
            "جيد للفرق"
          ],
  cons: [
            "Less creative freedom",
            "Expensive for individuals",
            "Limited templates",
            "AI can be restrictive"
          ],
  consEs: [
            "Menos libertad creativa",
            "Caro para individuos",
            "Plantillas limitadas",
            "IA restrictiva"
          ],
  consAr: [
            "حرية إبداعية أقل",
            "باهظ للأفراد",
            "قوالب محدودة",
            "الذكاء الاصطناعي مقيد"
          ],
  },

  {
    id: "canva-ai",
    name: "Canva AI",
    description: "All-in-one design platform with AI features for generating images, copy, and layouts.",
    descriptionEs: "Plataforma de diseño integral con funciones IA para generar imágenes, texto y diseños.",
    descriptionAr: "منصة تصميم شاملة مع ميزات الذكاء الاصطناعي لتوليد الصور والنصوص والتخطيطات.",
    category: "productivity",
    tags: ["design", "templates", "social-media", "all-in-one"],
    difficulty: "beginner",
    url: "https://www.canva.com",
    rating: r(4.7),
    pricing: "Free / $12.99/mo Pro",
    useCase: "Canva AI includes Magic Design, Magic Write, and AI image generation. Ideal for non-designers creating social media graphics, flyers, and presentations.",
    icon: "\u{1F3AF}",
  company: "Canva",
  companyEs: "Canva",
  companyAr: "Canva",
  founded: "2013",  headquarters: "Sydney, Australia",  
  descriptionLong: "Canva AI brings AI-powered design features into the popular Canva platform. Features include Magic Design (generates complete templates from descriptions), Magic Write (AI copy generation), AI image generation, background removal, and smart resize. Canva AI makes professional design accessible to non-designers with an all-in-one platform for social media, presentations, and print.",
  descriptionLongEs: "Canva AI integra funciones de diseno IA en la plataforma Canva. Incluye Magic Design, Magic Write y generacion de imagenes IA.",
  descriptionLongAr: "Canva AI يدمج ميزات التصميم بالذكاء الاصطناعي في منصة Canva. يشمل Magic Design وMagic Write.",
  advantages: [
            "All-in-one design platform",
            "Magic Design from text",
            "Magic Write copy generation",
            "AI image generation",
            "Background removal"
          ],
  advantagesEs: [
            "Plataforma integral",
            "Magic Design desde texto",
            "Magic Write",
            "Generacion de imagenes IA",
            "Eliminacion de fondos"
          ],
  advantagesAr: [
            "منصة تصميم شاملة",
            "Magic Design من النص",
            "Magic Write",
            "توليد الصور",
            "إزالة الخلفية"
          ],
  useCases: [
            "Social media graphics",
            "Presentation design",
            "Marketing materials",
            "Video creation",
            "Brand kits"
          ],
  useCasesEs: [
            "Graficos redes",
            "Diseno presentaciones",
            "Materiales marketing",
            "Creacion de video"
          ],
  useCasesAr: [
            "رسومات التواصل",
            "تصميم العروض",
            "مواد تسويقية",
            "إنشاء فيديو"
          ],
  targetAudience: "Non-designers and social media managers who want easy professional design with AI assistance.",
  targetAudienceEs: "No-disenadores y community managers que quieren diseno profesional facil.",
  targetAudienceAr: "غير المصممين ومديرو وسائل التواصل الاجتماعي الذين يريدون تصميما احترافيا سهلا بمساعدة الذكاء الاصطناعي.",
  pricingTiers: [
      {
        tier: "Free",
        price: "$0",
        features: [
          "Limited AI",
          "250K+ templates",
          "1GB storage"
        ]
      },
      {
        tier: "Pro",
        price: "$12.99/mo",
        features: [
          "Unlimited AI",
          "100M+ assets",
          "Brand kits"
        ]
      }
    ],  
  extensions: [
        {
          name: "Canva Web App",
          description: "Full browser-based design platform"
        },
        {
          name: "Canva Desktop",
          description: "Windows and Mac app"
        }
      ],  
  skills: [
            "graphic design",
            "social media",
            "brand design",
            "content creation",
            "visual marketing"
          ],  
  pros: [
            "All-in-one design",
            "Magic Design is powerful",
            "Huge template library",
            "Team collaboration"
          ],
  prosEs: [
            "Diseno integral",
            "Magic Design potente",
            "Gran biblioteca de plantillas",
            "Colaboracion"
          ],
  prosAr: [
            "تصميم شامل",
            "Magic Design قوي",
            "مكتبة قوالب ضخمة",
            "تعاون فريقي"
          ],
  cons: [
            "Pro subscription needed for AI",
            "Can feel overwhelming",
            "Export limited without Pro",
            "Brand control limited on Free"
          ],
  consEs: [
            "Suscripcion Pro necesaria",
            "Puede ser abrumador",
            "Exportacion limitada",
            "Control de marca limitado"
          ],
  consAr: [
            "اشتراك Pro مطلوب",
            "قد يكون مربكا",
            "تصدير محدود",
            "تحكم العلامة محدود"
          ],
  },

  {
    id: "elevenlabs",
    name: "ElevenLabs",
    description: "Industry-leading AI voice synthesis with realistic, expressive speech generation.",
    descriptionEs: "Síntesis de voz IA líder en la industria con generación de voz realista y expresiva.",
    descriptionAr: "توليف صوتي بالذكاء الاصطناعي رائد في الصناعة مع توليد كلام واقعي ومعبّر.",
    category: "audio",
    tags: ["voice", "tts", "audiobooks", "realistic"],
    difficulty: "beginner",
    url: "https://elevenlabs.io",
    rating: r(4.7),
    pricing: "Free tier / from $5/mo",
    useCase: "ElevenLabs generates ultra-realistic speech from text, supports voice cloning, and multi-language narration. Perfect for audiobooks, videos, and voiceovers.",
    icon: "\u{1F399}️",
  company: "ElevenLabs",
  companyEs: "ElevenLabs",
  companyAr: "ElevenLabs",
  founded: "2022",  headquarters: "New York, NY",  
  descriptionLong: "ElevenLabs is the industry-leading AI voice synthesis platform known for ultra-realistic, expressive speech generation. It offers text-to-speech, voice cloning, voice library, and multi-language narration in 29+ languages. With features like voice design, emotion control, and API access, ElevenLabs is used for audiobooks, videos, voiceovers, and content creation.",
  descriptionLongEs: "ElevenLabs es la plataforma lider de sintesis de voz IA con generacion de voz realista y expresiva. Ofrece texto-a-voz y clonacion de voz.",
  descriptionLongAr: "ElevenLabs هي المنصة الرائدة في تركيب الصوت بالذكاء الاصطناعي بتوليد كلام واقعي ومعبر.",
  advantages: [
            "Ultra-realistic voice quality",
            "Voice cloning technology",
            "29+ language support",
            "Emotion and tone control"
          ],
  advantagesEs: [
            "Voz ultra realista",
            "Clonacion de voz",
            "29+ idiomas",
            "Control de emocion"
          ],
  advantagesAr: [
            "صوت واقعي للغاية",
            "استنساخ الصوت",
            "29+ لغة",
            "تحكم في العاطفة"
          ],
  useCases: [
            "Audiobook narration",
            "Video voiceovers",
            "Content creator voice",
            "Language learning audio",
            "Accessibility solutions"
          ],
  useCasesEs: [
            "Narracion de audiolibros",
            "Locuciones de video",
            "Voz de creador",
            "Aprendizaje de idiomas"
          ],
  useCasesAr: [
            "سرد الكتب الصوتية",
            "تعليق صوتي للفيديو",
            "صوت منشئ المحتوى",
            "تعلم اللغات"
          ],
  targetAudience: "Content creators, publishers, and developers needing realistic AI voice generation for audio content.",
  targetAudienceEs: "Creadores de contenido, editores y desarrolladores que necesitan generación de voz AI realista para contenido de audio.",
  targetAudienceAr: "منشئو المحتوى والناشرون والمطورون الذين يحتاجون توليد صوت بالذكاء الاصطناعي واقعي للمحتوى الصوتي.",
  pricingTiers: [
      {
        tier: "Free",
        price: "$0",
        features: [
          "10K chars/month",
          "Standard voices"
        ]
      },
      {
        tier: "Starter",
        price: "$5/mo",
        features: [
          "30K chars/month",
          "Voice cloning"
        ]
      },
      {
        tier: "Creator",
        price: "$22/mo",
        features: [
          "100K chars/month",
          "API access"
        ]
      }
    ],  
  extensions: [
        {
          name: "ElevenLabs Web",
          description: "Browser-based TTS platform"
        }
      ],  
  skills: [
            "voice synthesis",
            "audio production",
            "voice cloning",
            "TTS",
            "audiobook production"
          ],  
  pros: [
            "Most realistic AI voices",
            "Excellent voice cloning",
            "Multi-language support",
            "Good API"
          ],
  prosEs: [
            "Voces IA mas realistas",
            "Clonacion excelente",
            "Soporte multilingue",
            "Buena API"
          ],
  prosAr: [
            "أصوات ذكاء اصطناعي واقعية",
            "استنساخ صوت ممتاز",
            "دعم متعدد اللغات",
            "API جيدة"
          ],
  cons: [
            "Expensive for high usage",
            "Voice cloning ethical concerns",
            "Free tier limited",
            "Long processing for long text"
          ],
  consEs: [
            "Caro para uso intensivo",
            "Preocupaciones eticas",
            "Nivel gratuito limitado",
            "Procesamiento lento"
          ],
  consAr: [
            "باهظ للاستخدام المكثف",
            "مخاوف أخلاقية",
            "طبقة مجانية محدودة",
            "معالجة بطيئة"
          ],
  },

  {
    id: "suno",
    name: "Suno",
    description: "AI music generation that creates original songs with lyrics from text prompts.",
    descriptionEs: "Generación de música IA que crea canciones originales con letras a partir de texto.",
    descriptionAr: "توليد موسيقى بالذكاء الاصطناعي ينشئ أغاني أصلية مع كلمات من تعليمات نصية.",
    category: "audio",
    tags: ["music", "song", "creative", "audio"],
    difficulty: "beginner",
    url: "https://suno.com",
    rating: r(4.5),
    pricing: "Free tier / from $10/mo",
    useCase: "Suno creates original songs with vocals and instruments from text descriptions. Great for content creators, musicians, and anyone exploring AI music.",
    icon: "\u{1F3B5}",
  company: "Suno",
  companyEs: "Suno",
  companyAr: "Suno",
  founded: "2022",  headquarters: "Cambridge, MA",  
  descriptionLong: "Suno is an AI music generation platform that creates original songs with vocals and instruments from text prompts. It can generate complete songs in various genres including pop, rock, hip-hop, electronic, and classical. Users provide lyrics or let Suno generate them, choose a style, and the AI produces a complete musical composition. Great for content creators and music exploration.",
  descriptionLongEs: "Suno es una plataforma de generacion de musica IA que crea canciones originales con voces e instrumentos desde prompts de texto.",
  descriptionLongAr: "Suno هي منصة لتوليد الموسيقى بالذكاء الاصطناعي تنشئ أغاني أصلية بالصوت والآلات من أوامر نصية.",
  advantages: [
            "Complete song generation",
            "Multiple genres supported",
            "Lyrics generation included",
            "Fast creation process"
          ],
  advantagesEs: [
            "Cancion completa",
            "Multiples generos",
            "Letras incluidas",
            "Proceso rapido"
          ],
  advantagesAr: [
            "أغنية كاملة",
            "أنواع موسيقية متعددة",
            "توليد كلمات",
            "عملية سريعة"
          ],
  useCases: [
            "Background music creation",
            "Content creator intro songs",
            "Music exploration",
            "Creative inspiration",
            "Personal enjoyment"
          ],
  useCasesEs: [
            "Musica de fondo",
            "Canciones para creadores",
            "Exploracion musical",
            "Inspiracion creativa"
          ],
  useCasesAr: [
            "موسيقى خلفية",
            "أغاني لمنشئي المحتوى",
            "استكشاف موسيقي",
            "إلهام إبداعي"
          ],
  targetAudience: "Content creators, musicians exploring AI, and anyone wanting original AI-generated music.",
  targetAudienceEs: "Creadores de contenido, músicos que exploran IA y cualquier persona que quiera música original generada por IA.",
  targetAudienceAr: "منشئو المحتوى والموسيقيون الذين يستكشفون الذكاء الاصطناعي وأي شخص يريد موسيقى أصلية بالذكاء الاصطناعي.",
  pricingTiers: [
      {
        tier: "Free",
        price: "$0",
        features: [
          "5 songs/day",
          "Basic quality"
        ]
      },
      {
        tier: "Pro",
        price: "$10/mo",
        features: [
          "500 songs/month",
          "Full quality",
          "Commercial use"
        ]
      }
    ],  
  extensions: [
        {
          name: "Suno Web",
          description: "Browser-based music generation"
        }
      ],  
  skills: [
            "music production",
            "songwriting",
            "creative AI",
            "audio production"
          ],  
  pros: [
            "Generates complete songs",
            "Multiple genres",
            "Easy to use",
            "Good quality output"
          ],
  prosEs: [
            "Canciones completas",
            "Multiples generos",
            "Facil de usar",
            "Buena calidad"
          ],
  prosAr: [
            "أغان كاملة",
            "أنواع متعددة",
            "سهل الاستخدام",
            "جودة جيدة"
          ],
  cons: [
            "Limited control over details",
            "Not for professional music",
            "Similar sounding songs",
            "Free tier limitations"
          ],
  consEs: [
            "Control limitado",
            "No para musica profesional",
            "Canciones similares",
            "Limitaciones gratis"
          ],
  consAr: [
            "تحكم محدود",
            "ليس للموسيقى الاحترافية",
            "أغان متشابهة",
            "قيود مجانية"
          ],
  },

  {
    id: "murf-ai",
    name: "Murf AI",
    description: "AI voiceover platform with natural-sounding voices for professional content creation.",
    descriptionEs: "Plataforma de locución IA con voces naturales para creación de contenido profesional.",
    descriptionAr: "منصة تعليق صوتي بالذكاء الاصطناعي بأصوات طبيعية لإنشاء المحتوى الاحترافي.",
    category: "audio",
    tags: ["voiceover", "tts", "professional", "narration"],
    difficulty: "beginner",
    url: "https://murf.ai",
    rating: r(4.3),
    pricing: "Free tier / from $19/mo",
    useCase: "Murf AI turns text into voiceovers for videos, e-learning, and presentations. It offers a wide range of natural voices with pitch and emphasis control.",
    icon: "\u{1F3A4}",
  company: "Murf AI",
  companyEs: "Murf AI",
  companyAr: "Murf AI",
  founded: "2020",  headquarters: "Boston, MA",  
  descriptionLong: "Murf AI is a voiceover platform with natural-sounding AI voices for professional content creation. It offers 120+ voices across 20+ languages with features like pitch control, emphasis adjustment, and pause insertion. Murf is widely used for e-learning, presentations, advertising, and corporate videos with a user-friendly editor.",
  descriptionLongEs: "Murf AI es una plataforma de locucion con voces IA naturales. Ofrece 120+ voces en 20+ idiomas con control de tono y enfasis.",
  descriptionLongAr: "Murf AI هي منصة تعليق صوتي بأصوات ذكاء اصطناعي طبيعية. تقدم 120+ صوتا بـ 20+ لغة.",
  advantages: [
            "120+ natural voices",
            "20+ languages",
            "Pitch and emphasis control",
            "User-friendly editor"
          ],
  advantagesEs: [
            "120+ voces naturales",
            "20+ idiomas",
            "Control de tono y enfasis",
            "Editor facil"
          ],
  advantagesAr: [
            "120+ صوتا طبيعيا",
            "20+ لغة",
            "تحكم في النبرة والتأكيد",
            "محرر سهل الاستخدام"
          ],
  useCases: [
            "E-learning narration",
            "Voiceover for videos",
            "Corporate training",
            "Podcast creation",
            "Advertising audio"
          ],
  useCasesEs: [
            "Narracion educativa",
            "Locucion de videos",
            "Capacitacion corporativa",
            "Creacion de podcasts"
          ],
  useCasesAr: [
            "سرد تعليمي",
            "تعليق صوتي للفيديو",
            "تدريب مؤسسي",
            "إنشاء بودكاست"
          ],
  targetAudience: "Content creators, educators, and businesses needing professional voiceovers without hiring voice actors.",
  targetAudienceEs: "Creadores de contenido, educadores y empresas que necesitan locuciones profesionales sin contratar actores de voz.",
  targetAudienceAr: "منشئو المحتوى والمعلمون والشركات الذين يحتاجون تعليقات صوتية احترافية دون توظيف ممثلين صوتيين.",
  pricingTiers: [
      {
        tier: "Free",
        price: "$0",
        features: [
          "10 mins voice",
          "Limited voices"
        ]
      },
      {
        tier: "Basic",
        price: "$19/mo",
        features: [
          "24 hours/year",
          "All voices",
          "Commercial use"
        ]
      }
    ],  
  extensions: [
        {
          name: "Murf Web",
          description: "Browser-based voiceover studio"
        }
      ],  
  skills: [
            "voiceover",
            "audio production",
            "e-learning",
            "narration",
            "corporate training"
          ],  
  pros: [
            "Many voice options",
            "Natural sounding",
            "Good editing controls",
            "Multi-language"
          ],
  prosEs: [
            "Muchas opciones de voz",
            "Sonido natural",
            "Buen control de edicion",
            "Multilingue"
          ],
  prosAr: [
            "خيارات صوت متعددة",
            "صوت طبيعي",
            "ضوابط تحرير جيدة",
            "متعدد اللغات"
          ],
  cons: [
            "Can be robotic at times",
            "Expensive for full features",
            "Limited free tier",
            "Voice quality varies"
          ],
  consEs: [
            "A veces roboticas",
            "Caro funciones completas",
            "Nivel gratuito limitado",
            "Calidad variable"
          ],
  consAr: [
            "قد تكون آلية أحيانا",
            "باهظ للميزات الكاملة",
            "طبقة مجانية محدودة",
            "جودة متغيرة"
          ],
  },

  {
    id: "deeplearning-ai",
    name: "DeepLearning.AI",
    description: "World-class AI education platform offering courses from Andrew Ng and industry experts.",
    descriptionEs: "Plataforma de educación en IA de clase mundial con cursos de Andrew Ng y expertos de la industria.",
    descriptionAr: "منصة تعليم ذكاء اصطناعي عالمية المستوى تقدم دورات من Andrew Ng وخبراء الصناعة.",
    category: "learning",
    tags: ["courses", "education", "deep-learning", "certificate"],
    difficulty: "intermediate",
    url: "https://www.deeplearning.ai",
    rating: r(4.8),
    pricing: "Free / from $49/mo",
    useCase: "DeepLearning.AI offers structured AI courses from beginner to advanced. Andrew Ng's courses are the gold standard for learning machine learning and AI fundamentals.",
    icon: "\u{1F4DA}",
  company: "DeepLearning.AI",
  companyEs: "DeepLearning.AI",
  companyAr: "DeepLearning.AI",
  founded: "2017",  headquarters: "Palo Alto, CA",  
  descriptionLong: "DeepLearning.AI offers world-class AI education founded by Andrew Ng, one of the most influential figures in machine learning. It provides structured courses from beginner to advanced levels including the famous Deep Learning Specialization, Generative AI for Everyone, and more. Courses feature video lectures, quizzes, and hands-on projects. The gold standard for learning AI fundamentals.",
  descriptionLongEs: "DeepLearning.AI ofrece educacion en IA de clase mundial fundada por Andrew Ng. Cursos estructurados desde principiante a avanzado.",
  descriptionLongAr: "DeepLearning.AI تقدم تعليما عالميا في الذكاء الاصطناعي أسسه Andrew Ng. دورات منظمة من المبتدئ إلى المتقدم.",
  advantages: [
            "Taught by Andrew Ng",
            "Structured learning paths",
            "Hands-on projects",
            "Industry-recognized certificates"
          ],
  advantagesEs: [
            "Ensenado por Andrew Ng",
            "Rutas de aprendizaje",
            "Proyectos practicos",
            "Certificados reconocidos"
          ],
  advantagesAr: [
            "يدرسه Andrew Ng",
            "مسارات تعلم منظمة",
            "مشاريع عملية",
            "شهادات معترف بها"
          ],
  useCases: [
            "Starting AI learning journey",
            "Deep learning mastery",
            "Generative AI skills",
            "Career transition to AI",
            "ML fundamentals"
          ],
  useCasesEs: [
            "Inicio en IA",
            "Dominio de deep learning",
            "Habilidades de IA generativa",
            "Transicion a carrera IA"
          ],
  useCasesAr: [
            "بدء رحلة تعلم الذكاء الاصطناعي",
            "إتقان التعلم العميق",
            "مهارات الذكاء الاصطناعي التوليدي",
            "التحول المهني للذكاء الاصطناعي"
          ],
  targetAudience: "Anyone wanting to learn AI from scratch -- beginners to experienced developers seeking structured courses.",
  targetAudienceEs: "Cualquier persona que quiera aprender IA desde cero -- principiantes hasta desarrolladores experimentados que buscan cursos estructurados.",
  targetAudienceAr: "أي شخص يريد تعلم الذكاء الاصطناعي من الصفر -- من المبتدئين إلى المطورين ذوي الخبرة الذين يبحثون عن دورات منظمة.",
  pricingTiers: [
      {
        tier: "Audit",
        price: "$0",
        features: [
          "Video access",
          "Limited exercises"
        ]
      },
      {
        tier: "Coursera",
        price: "From $49/mo",
        features: [
          "Full courses",
          "Projects",
          "Certificate"
        ]
      }
    ],  
  extensions: [
        {
          name: "DeepLearning.AI Website",
          description: "Course platform and community"
        }
      ],  
  skills: [
            "machine learning",
            "deep learning",
            "generative AI",
            "neural networks",
            "AI fundamentals"
          ],  
  pros: [
            "World-class instruction",
            "Structured curriculum",
            "Hands-on projects",
            "Certificate value"
          ],
  prosEs: [
            "Instruccion de clase mundial",
            "Curriculum estructurado",
            "Proyectos practicos",
            "Valor del certificado"
          ],
  prosAr: [
            "تعليم عالمي المستوى",
            "منهج منظم",
            "مشاريع عملية",
            "قيمة الشهادة"
          ],
  cons: [
            "Can be expensive",
            "Courses take time",
            "More academic focus",
            "Some content dated"
          ],
  consEs: [
            "Puede ser caro",
            "Los cursos toman tiempo",
            "Enfoque academico",
            "Contenido desactualizado"
          ],
  consAr: [
            "قد يكون باهظا",
            "الدورات تستغرق وقتا",
            "تركيز أكاديمي",
            "بعض المحتوى قديم"
          ],
  },

  {
    id: "fast-ai",
    name: "fast.ai",
    description: "Practical deep learning education with a top-down teaching approach for developers.",
    descriptionEs: "Educación práctica en deep learning con un enfoque de enseñanza descendente para desarrolladores.",
    descriptionAr: "تعليم عملي للتعلم العميق بنهج تعليمي من الأعلى إلى الأسفل للمطورين.",
    category: "learning",
    tags: ["courses", "practical", "free", "deep-learning"],
    difficulty: "intermediate",
    url: "https://www.fast.ai",
    rating: r(4.6),
    pricing: "Free",
    useCase: "fast.ai teaches deep learning using a practical, code-first approach. Their free courses let you build production models quickly without heavy math prerequisites.",
    icon: "\u{1F3C3}",
  company: "fast.ai",
  companyEs: "fast.ai",
  companyAr: "fast.ai",
  founded: "2016",  headquarters: "San Francisco, CA",  
  descriptionLong: "fast.ai provides practical deep learning education with a unique top-down teaching approach. Their famous Practical Deep Learning for Coders course teaches you to build production-ready models from lesson one without requiring heavy math prerequisites. All courses are free and focus on getting results quickly. The fast.ai library abstracts complexity while maintaining flexibility.",
  descriptionLongEs: "fast.ai ofrece educacion practica en deep learning con enfoque descendente. Ensena a construir modelos listos para produccion desde la primera leccion.",
  descriptionLongAr: "fast.ai يقدم تعليما عمليا في التعلم العميق بنهج تعليمي من الأعلى إلى الأسفل. يعلم بناء نماذج جاهزة للإنتاج.",
  advantages: [
            "Free high-quality courses",
            "Top-down practical approach",
            "Build production models early",
            "Active community"
          ],
  advantagesEs: [
            "Cursos gratis de calidad",
            "Enfoque practico",
            "Modelos productivos temprano",
            "Comunidad activa"
          ],
  advantagesAr: [
            "دورات مجانية عالية الجودة",
            "نهج عملي من القمة",
            "نماذج إنتاج مبكرة",
            "مجتمع نشط"
          ],
  useCases: [
            "Learning deep learning practically",
            "Building production ML models",
            "AI research exploration",
            "Teaching DL concepts"
          ],
  useCasesEs: [
            "Aprendizaje profundo practico",
            "Construir modelos produccion",
            "Exploracion investigacion IA",
            "Ensenanza DL"
          ],
  useCasesAr: [
            "تعلم التعلم العميق عمليا",
            "بناء نماذج إنتاج",
            "استكشاف أبحاث الذكاء الاصطناعي",
            "تدريس DL"
          ],
  targetAudience: "Developers wanting to learn deep learning with a practical code-first approach.",
  targetAudienceEs: "Desarrolladores que quieren aprender deep learning con un enfoque práctico y centrado en código.",
  targetAudienceAr: "المطورون الذين يريدون تعلم التعلم العميق بنهج عملي يركز على البرمجة.",
  pricingTiers: [
      {
        tier: "All Courses",
        price: "$0",
        features: [
          "All course materials",
          "Forum access",
          "Book included"
        ]
      }
    ],  
  extensions: [
        {
          name: "fast.ai Forums",
          description: "Community discussion platform"
        }
      ],  
  skills: [
            "deep learning",
            "practical ML",
            "neural networks",
            "model deployment",
            "AI development"
          ],  
  pros: [
            "Completely free",
            "Practical approach",
            "Build real models quickly",
            "Great for coders"
          ],
  prosEs: [
            "Completamente gratis",
            "Enfoque practico",
            "Modelos reales rapido",
            "Excelente para programadores"
          ],
  prosAr: [
            "مجاني بالكامل",
            "نهج عملي",
            "نماذج حقيقية بسرعة",
            "ممتاز للمبرمجين"
          ],
  cons: [
            "Not for absolute beginners",
            "Less theoretical depth",
            "Python focused only",
            "Self-paced no certification"
          ],
  consEs: [
            "No para principiantes absolutos",
            "Menos profundidad teorica",
            "Solo Python",
            "Sin certificacion"
          ],
  consAr: [
            "ليس للمبتدئين تماما",
            "عمق نظري أقل",
            "Python فقط",
            "بدون شهادة"
          ],
  },

  {
    id: "langchain",
    name: "LangChain",
    description: "Framework for building LLM-powered applications with composable chains and agents.",
    descriptionEs: "Framework para construir aplicaciones impulsadas por LLM con cadenas y agentes componibles.",
    descriptionAr: "إطار عمل لبناء تطبيقات مدعومة بنماذج اللغة الكبيرة بسلاسل ووكلاء قابلين للتكوين.",
    category: "coding",
    tags: ["framework", "llm", "agents", "python"],
    difficulty: "advanced",
    url: "https://www.langchain.com",
    rating: r(4.5),
    pricing: "Free (open-source) / LangSmith paid",
    useCase: "LangChain builds applications on top of LLMs. Use it to create chatbots, RAG systems, AI agents, and automated workflows with chain composition.",
    icon: "\u{26D3}️",
  company: "LangChain Inc.",
  companyEs: "LangChain Inc.",
  companyAr: "LangChain Inc.",
  founded: "2022",  headquarters: "San Francisco, CA",  
  descriptionLong: "LangChain is a framework for building LLM-powered applications with composable chains and agents. It provides tools for prompt management, memory, retrieval-augmented generation (RAG), tool calling, and multi-agent systems. With LangSmith for debugging and LangGraph for stateful agents, it has become the standard framework for production LLM applications.",
  descriptionLongEs: "LangChain es un framework para construir aplicaciones impulsadas por LLM con cadenas y agentes componibles. Es el estandar para aplicaciones LLM en produccion.",
  descriptionLongAr: "LangChain هو إطار عمل لبناء تطبيقات مدعومة بنماذج اللغة الكبيرة بسلاسل ووكلاء قابلين للتكوين.",
  advantages: [
            "Standard LLM framework",
            "RAG support built-in",
            "Multi-agent orchestration",
            "LangSmith debugging"
          ],
  advantagesEs: [
            "Framework LLM estandar",
            "Soporte RAG integrado",
            "Orquestacion multi-agente",
            "Depuracion LangSmith"
          ],
  advantagesAr: [
            "إطار عمل LLM قياسي",
            "دعم RAG مدمج",
            "تنسيق متعدد الوكلاء",
            "تصحيح LangSmith"
          ],
  useCases: [
            "Building RAG applications",
            "Creating AI chatbots",
            "Multi-agent systems",
            "Document Q&A systems",
            "Workflow automation"
          ],
  useCasesEs: [
            "Apps de RAG",
            "Chatbots IA",
            "Sistemas multi-agente",
            "Preguntas sobre documentos"
          ],
  useCasesAr: [
            "تطبيقات RAG",
            "روبوتات الدردشة",
            "أنظمة متعددة الوكلاء",
            "أسئلة على المستندات"
          ],
  targetAudience: "Developers building production LLM applications who need a structured framework for chains and agents.",
  targetAudienceEs: "Desarrolladores que construyen aplicaciones LLM en producción y necesitan un framework estructurado para cadenas y agentes.",
  targetAudienceAr: "المطورون الذين يبنون تطبيقات نماذج لغوية كبيرة في الإنتاج ويحتاجون إطار عمل منظم للسلاسل والوكلاء.",
  pricingTiers: [
      {
        tier: "Open Source",
        price: "$0",
        features: [
          "All framework features",
          "Self-hosted"
        ]
      },
      {
        tier: "LangSmith",
        price: "Pay-as-you-go",
        features: [
          "Debugging",
          "Monitoring",
          "Evaluation"
        ]
      }
    ],  
  extensions: [
        {
          name: "LangChain Python",
          description: "Python framework package"
        },
        {
          name: "LangChain JS",
          description: "JavaScript/TypeScript framework"
        }
      ],  
  skills: [
            "LLM development",
            "RAG systems",
            "agent development",
            "Python",
            "prompt engineering"
          ],  
  pros: [
            "Industry standard framework",
            "Excellent RAG support",
            "Active development",
            "Strong community"
          ],
  prosEs: [
            "Framework estandar",
            "Soporte RAG excelente",
            "Desarrollo activo",
            "Comunidad fuerte"
          ],
  prosAr: [
            "إطار عمل قياسي",
            "دعم RAG ممتاز",
            "تطوير نشط",
            "مجتمع قوي"
          ],
  cons: [
            "Fast-changing API",
            "Can be complex",
            "Overkill for simple apps",
            "Documentation can lag"
          ],
  consEs: [
            "API cambiante",
            "Puede ser complejo",
            "Excesivo para apps simples",
            "Documentacion atrasada"
          ],
  consAr: [
            "API متغيرة بسرعة",
            "قد يكون معقدا",
            "مبالغ للتطبيقات البسيطة",
            "توثيق متأخر"
          ],
  },

  {
    id: "huggingface",
    name: "Hugging Face",
    description: "Leading platform for open-source AI models, datasets, and collaborative ML development.",
    descriptionEs: "Plataforma líder para modelos de IA de código abierto, datasets y desarrollo colaborativo de ML.",
    descriptionAr: "المنصة الرائدة لنماذج الذكاء الاصطناعي مفتوحة المصدر ومجموعات البيانات وتطوير التعلم الآلي التعاوني.",
    category: "industry",
    tags: ["models", "open-source", "community", "mlops"],
    difficulty: "advanced",
    url: "https://huggingface.co",
    rating: r(4.7),
    pricing: "Free / paid inference and storage",
    useCase: "Hugging Face is the GitHub of AI. Access thousands of pre-trained models, datasets, and Spaces apps. Essential for ML engineers and AI researchers.",
    icon: "\u{1F917}",
  company: "Hugging Face",
  companyEs: "Hugging Face",
  companyAr: "Hugging Face",
  founded: "2016",  headquarters: "New York, NY",  
  descriptionLong: "Hugging Face is the leading platform for open-source AI models, datasets, and collaborative ML development. Often called the GitHub of AI, it hosts 500K+ models, 150K+ datasets, and Spaces apps. The Transformers library provides a unified API for thousands of models. Essential for ML engineers and AI researchers for model discovery, sharing, and deployment.",
  descriptionLongEs: "Hugging Face es la plataforma lider para modelos de IA open-source. Con 500K+ modelos, 150K+ datasets y Spaces, es esencial para ingenieros ML.",
  descriptionLongAr: "Hugging Face هي المنصة الرائدة لنماذج الذكاء الاصطناعي مفتوحة المصدر. تستضيف 500 ألف+ نموذج.",
  advantages: [
            "500K+ open-source models",
            "150K+ datasets",
            "Spaces for demo apps",
            "Transformers library"
          ],
  advantagesEs: [
            "500K+ modelos",
            "150K+ datasets",
            "Spaces para demos",
            "Biblioteca Transformers"
          ],
  advantagesAr: [
            "500 ألف+ نموذج",
            "150 ألف+ مجموعة بيانات",
            "Spaces للتطبيقات",
            "مكتبة Transformers"
          ],
  useCases: [
            "Model discovery and download",
            "Fine-tuning open models",
            "Dataset sharing",
            "ML research collaboration",
            "Deploying model demos"
          ],
  useCasesEs: [
            "Descubrimiento de modelos",
            "Ajuste de modelos abiertos",
            "Compartir datasets",
            "Colaboracion investigacion ML",
            "Desplegar demos"
          ],
  useCasesAr: [
            "اكتشاف النماذج وتنزيلها",
            "ضبط النماذج المفتوحة",
            "مشاركة مجموعات البيانات",
            "تعاون أبحاث ML",
            "نشر عروض توضيحية"
          ],
  targetAudience: "ML engineers, AI researchers, and developers who work with open-source AI models and datasets.",
  targetAudienceEs: "Ingenieros de ML, investigadores de IA y desarrolladores que trabajan con modelos y datasets de IA de código abierto.",
  targetAudienceAr: "مهندسو التعلم الآلي وباحثو الذكاء الاصطناعي والمطورون الذين يعملون مع نماذج ومجموعات بيانات مفتوحة المصدر.",
  pricingTiers: [
      {
        tier: "Free",
        price: "$0",
        features: [
          "Public models",
          "Datasets",
          "Limited Spaces"
        ]
      },
      {
        tier: "Pro",
        price: "$9/mo",
        features: [
          "Private repos",
          "More Spaces",
          "Inference API"
        ]
      }
    ],  
  extensions: [
        {
          name: "Hugging Face Hub",
          description: "Web platform and APIs"
        }
      ],  
  skills: [
            "machine learning",
            "model deployment",
            "NLP",
            "model fine-tuning",
            "MLOps"
          ],  
  pros: [
            "Huge model repository",
            "Strong community",
            "Transformers industry standard",
            "Spaces for demos"
          ],
  prosEs: [
            "Gran repositorio de modelos",
            "Comunidad fuerte",
            "Transformers estandar",
            "Spaces para demos"
          ],
  prosAr: [
            "مستودع نماذج ضخم",
            "مجتمع قوي",
            "Transformers معيار صناعي",
            "Spaces للعروض"
          ],
  cons: [
            "Can be overwhelming",
            "Pro features cost money",
            "Model quality varies",
            "Dependency on platform"
          ],
  consEs: [
            "Puede ser abrumador",
            "Las funciones Pro cuestan dinero",
            "La calidad del modelo varía",
            "Dependencia de la plataforma"
          ],
  consAr: [
            "قد يكون مربكا",
            "الميزات المدفوعة تكلف مالا",
            "جودة النموذج متغيرة",
            "الاعتماد على المنصة"
          ],
  },
];
