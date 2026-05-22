export interface Article {
  slug: string;
  title: string;
  titleZh: string;
  description: string;
  descriptionZh: string;
  category: string;
  tags: string[];
  difficulty: "beginner" | "intermediate" | "advanced";
  toolsMentioned: string[];
  date: string;
}

export const articles: Article[] = [
  // ====== Sample: Claude Code (Path: Claude Code 编程入门, Part 1/4) ======
  {
    slug: "claude-code-install-setup",
    title: "Claude Code Installation & Setup: From Zero to Your First AI-Generated Web Page",
    titleZh: "Instalación y Configuración de Claude Code: De Cero a Tu Primera Página Web Generada por IA [CN]",
    description:
      "Step-by-step guide to installing Claude Code on Windows, Mac, or Linux — with copyable commands, API key setup, and your first AI-generated project.",
    descriptionZh:
      "Guía paso a paso para instalar Claude Code en Windows, Mac o Linux — con comandos copiables, configuración de API key y tu primer proyecto generado por IA. [CN]",
    category: "ai-tutorials",
    tags: ["claude-code", "installation", "setup", "command-line", "coding", "beginner"],
    difficulty: "beginner",
    toolsMentioned: ["claude"],
    date: "2026-05-22",
  },

  // ====== AI Basics (5) ======
  {
    slug: "llms-in-plain-english",
    title: "I Keep Hearing About 'LLMs' — What They Actually Are in Plain English",
    titleZh: "Sigo Escuchando Sobre 'LLMs' — Qué Son Realmente en Español Sencillo [CN]",
    description:
      "Everyone says 'large language model' like you should know what it means. Here's the actually-simple explanation, with zero technical jargon.",
    descriptionZh:
      "Todo el mundo dice 'modelo de lenguaje grande' como si debieras saber lo que significa. Aquí está la explicación realmente simple, sin jerga técnica. [CN]",
    category: "ai-basics",
    tags: ["llm", "explained", "non-technical", "fundamentals"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt", "claude"],
    date: "2026-05-22",
  },
  {
    slug: "ai-hallucinations-explained-with-examples",
    title: "AI Hallucinations Explained: Why ChatGPT Makes Stuff Up (With Real Examples)",
    titleZh: "Alucinaciones de IA Explicadas: Por Qué ChatGPT Inventa Cosas (Con Ejemplos Reales) [CN]",
    description:
      "You asked for a recipe and it invented an ingredient that doesn't exist. Here's why AI hallucinates, how to spot it, and what to do when it happens.",
    descriptionZh:
      "Pediste una receta e inventó un ingrediente que no existe. Esto es por qué la IA alucina, cómo detectarlo y qué hacer cuando sucede. [CN]",
    category: "ai-basics",
    tags: ["hallucinations", "chatgpt", "accuracy", "beginner"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt", "claude", "perplexity"],
    date: "2026-05-20",
  },
  {
    slug: "how-to-choose-right-ai-tool",
    title: "Which AI Tool Should You Use? A Decision Framework for Beginners",
    titleZh: "¿Qué Herramienta de IA Deberías Usar? Un Marco de Decisión para Principiantes [CN]",
    description:
      "ChatGPT vs Claude vs Gemini vs Perplexity vs Midjourney — which one do you actually need? A practical decision matrix based on what you're trying to do.",
    descriptionZh:
      "ChatGPT vs Claude vs Gemini vs Perplexity vs Midjourney — ¿cuál necesitas realmente? Una matriz de decisión práctica basada en lo que intentas hacer. [CN]",
    category: "ai-basics",
    tags: ["comparison", "tools", "chatgpt", "claude", "gemini", "perplexity", "midjourney", "beginner"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt", "claude", "gemini", "perplexity", "midjourney"],
    date: "2026-05-22",
  },
  {
    slug: "free-vs-paid-ai-tools-worth-it",
    title: "Free vs Paid AI Tools: When It's Actually Worth Paying (and When It's Not)",
    titleZh: "Herramientas IA Gratis vs de Pago: Cuándo Vale la Pena Pagar (y Cuándo No) [CN]",
    description:
      "ChatGPT Plus is $20/month. Claude Pro is $20/month. Midjourney is $10. Do you need any of them? Here's how to decide, based on what you actually use AI for.",
    descriptionZh:
      "ChatGPT Plus cuesta $20/mes. Claude Pro $20/mes. Midjourney $10. ¿Necesitas alguno? Aquí te mostramos cómo decidir, basado en para qué usas realmente la IA. [CN]",
    category: "ai-basics",
    tags: ["pricing", "free-vs-paid", "chatgpt", "value", "guide"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt", "claude", "midjourney", "gemini", "perplexity"],
    date: "2026-05-18",
  },
  {
    slug: "what-is-a-gpu-non-techie",
    title: "What's a GPU and Why Does AI Need It? A Non-Techie Explanation",
    titleZh: "¿Qué es una GPU y Por Qué la IA la Necesita? Una Explicación No Técnica [CN]",
    description:
      "NVIDIA is suddenly worth more than Google because of 'AI chips.' Here's what a GPU actually does, why AI needs thousands of them, and why you should care.",
    descriptionZh:
      "NVIDIA de repente vale más que Google por los 'chips de IA.' Esto es lo que realmente hace una GPU, por qué la IA necesita miles de ellas y por qué debería importarte. [CN]",
    category: "ai-basics",
    tags: ["gpu", "nvidia", "hardware", "explained", "non-technical"],
    difficulty: "beginner",
    toolsMentioned: [],
    date: "2026-05-16",
  },
  {
    slug: "ai-myths-people-still-believe",
    title: "5 AI Myths Your Non-Techie Friends Still Believe (and What's Actually True)",
    titleZh: "5 Mitos de IA que Tus Amigos No Técnicos Siguen Creyendo (y Qué es Realmente Verdad) [CN]",
    description:
      "\"AI is conscious.\" \"AI will take all jobs.\" \"AI knows everything.\" None of these are true. Here's what the reality looks like in 2026.",
    descriptionZh:
      "\"La IA es consciente.\" \"La IA quitará todos los trabajos.\" \"La IA lo sabe todo.\" Nada de esto es cierto. Así es la realidad en 2026. [CN]",
    category: "ai-basics",
    tags: ["myths", "misconceptions", "explained", "beginner"],
    difficulty: "beginner",
    toolsMentioned: [],
    date: "2026-05-14",
  },

  // ====== AI Tutorials (5) ======
  {
    slug: "chatgpt-voice-mode-job-interview",
    title: "ChatGPT Fundamentals: Interface, Settings, and Your First 10 Prompts",
    titleZh: "Fundamentos de ChatGPT: Interfaz, Configuración y tus Primeros 10 Prompts [CN]",
    description:
      "New to ChatGPT? Here is the complete beginner's guide — account setup, interface tour, settings to configure, and 10 starter prompts to get real value from day one.",
    descriptionZh:
      "Nuevo en ChatGPT? Aquí tienes la guía completa para principiantes — configuración de cuenta, recorrido de interfaz, ajustes y 10 prompts iniciales. [CN]",
    category: "ai-tutorials",
    tags: ["chatgpt", "beginner", "fundamentals", "prompts", "getting-started"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt"],
    date: "2026-05-22",
  },
  {
    slug: "claude-projects-organize-chats",
    title: "How to Write Prompts That Actually Work: The 5-Point Framework",
    titleZh: "Cómo Escribir Prompts Que Realmente Funcionan: El Marco de 5 Puntos [CN]",
    description:
      "Vague prompts get mediocre answers. Master the 5-Point Prompt Framework — Role, Context, Task, Format, Constraints — and get dramatically better results from any AI tool.",
    descriptionZh:
      "Los prompts vagos obtienen respuestas mediocres. Domina el Marco de 5 Puntos — Rol, Contexto, Tarea, Formato, Restricciones — y obtén resultados dramáticamente mejores. [CN]",
    category: "ai-tutorials",
    tags: ["prompts", "prompt-engineering", "framework", "writing", "chatgpt"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt", "claude"],
    date: "2026-05-22",
  },
  {
    slug: "ai-images-that-dont-look-like-ai",
    title: "ChatGPT for Writing: Emails, Reports, and Creative Projects",
    titleZh: "ChatGPT para Escribir: Correos, Informes y Proyectos Creativos [CN]",
    description:
      "Move beyond basic prompts. Master AI writing with tone control, outline-first reports, creative techniques, and editing workflows that produce professional-grade content.",
    descriptionZh:
      "Ve más allá de los prompts básicos. Domina la escritura con IA con control de tono, informes estructurados, técnicas creativas y flujos de edición profesionales. [CN]",
    category: "ai-tutorials",
    tags: ["chatgpt", "writing", "email", "content", "editing"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt"],
    date: "2026-05-22",
  },
  {
    slug: "voice-recording-to-meeting-notes-free",
    title: "ChatGPT for Research and Analysis: Web Search, File Upload, and Data",
    titleZh: "ChatGPT para Investigación y Análisis: Búsqueda Web, Carga de Archivos y Datos [CN]",
    description:
      "ChatGPT is more than a chatbot. Use it for web search, document analysis, data processing with Advanced Data Analysis, and long-form research — all in one place.",
    descriptionZh:
      "ChatGPT es más que un chatbot. Úsalo para búsqueda web, análisis de documentos, procesamiento de datos con Análisis Avanzado de Datos e investigación avanzada. [CN]",
    category: "ai-tutorials",
    tags: ["chatgpt", "research", "file-upload", "data-analysis", "web-search"],
    difficulty: "intermediate",
    toolsMentioned: ["chatgpt"],
    date: "2026-05-22",
  },
  {
    slug: "first-ai-coding-project-no-experience",
    title: "Custom GPTs and Automation: Build Your Own AI Assistant",
    titleZh: "GPTs Personalizados y Automatización: Crea tu Propio Asistente de IA [CN]",
    description:
      "Create custom versions of ChatGPT for your specific needs. Learn to build, configure with knowledge files, and share GPTs — no coding required.",
    descriptionZh:
      "Crea versiones personalizadas de ChatGPT para tus necesidades específicas. Aprende a construir, configurar con archivos de conocimiento y compartir GPTs. [CN]",
    category: "ai-tutorials",
    tags: ["chatgpt", "custom-gpts", "automation", "gpt-store", "no-code"],
    difficulty: "intermediate",
    toolsMentioned: ["chatgpt"],
    date: "2026-05-22",
  },

  // ====== AI Use Cases (5) ======
  {
    slug: "etsy-seller-ai-product-descriptions",
    title: "AI for Business Communication: Emails, Proposals, and Client Outreach",
    titleZh: "IA para Comunicación Empresarial: Correos, Propuestas y Atención al Cliente [CN]",
    description:
      "Professional communication takes hours each day. Use AI to draft emails, proposals, pitches, and product descriptions faster while maintaining your professional tone.",
    descriptionZh:
      "La comunicación profesional toma horas cada día. Usa IA para redactar correos, propuestas y descripciones de productos más rápido manteniendo tu tono profesional. [CN]",
    category: "ai-use-cases",
    tags: ["business", "communication", "email", "proposals", "productivity"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt", "claude"],
    date: "2026-05-22",
  },
  {
    slug: "ai-wedding-planning-free-tools",
    title: "AI for Project Planning and Organization: From Timelines to Budgets",
    titleZh: "IA para Planificación y Organización de Proyectos: De Cronogramas a Presupuestos [CN]",
    description:
      "AI excels at structured planning. Use it for timelines, budgets, task breakdowns, decision matrices, and status reports — whether for work projects or personal events.",
    descriptionZh:
      "La IA sobresale en planificación estructurada. Úsala para cronogramas, presupuestos, desgloses de tareas y matrices de decisión — para proyectos laborales o personales. [CN]",
    category: "ai-use-cases",
    tags: ["planning", "project-management", "timeline", "budget", "productivity"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt", "claude"],
    date: "2026-05-22",
  },
  {
    slug: "ai-travel-itinerary-real-prompts",
    title: "AI for Research and Report Writing: Find, Analyze, and Summarize",
    titleZh: "IA para Investigación y Redacción de Informes: Encuentra, Analiza y Resume [CN]",
    description:
      "Accelerate your research workflow with AI. Plan your approach, analyze sources, interpret data, and write reports — with prompting techniques that produce reliable results.",
    descriptionZh:
      "Acelera tu flujo de trabajo de investigación con IA. Planifica tu enfoque, analiza fuentes, interpreta datos y escribe informes — con técnicas de prompting fiables. [CN]",
    category: "ai-use-cases",
    tags: ["research", "report-writing", "analysis", "productivity", "data"],
    difficulty: "intermediate",
    toolsMentioned: ["chatgpt", "perplexity"],
    date: "2026-05-22",
  },
  {
    slug: "learn-english-with-ai-free-speaking-practice",
    title: "AI for Learning and Skill Development: Language, Tech, and More",
    titleZh: "IA para Aprendizaje y Desarrollo de Habilidades: Idiomas, Tecnología y Más [CN]",
    description:
      "AI is the most powerful self-education tool ever created. Use it for language practice with voice mode, interview prep, concept learning, and certification study.",
    descriptionZh:
      "La IA es la herramienta de autoeducación más poderosa jamás creada. Úsala para práctica de idiomas con modo de voz, preparación de entrevistas y estudio de certificaciones. [CN]",
    category: "ai-use-cases",
    tags: ["learning", "education", "language", "skills", "voice-mode"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt", "claude"],
    date: "2026-05-22",
  },
  {
    slug: "ai-for-parents-quiet-moments",
    title: "AI for Parents: 7 Ways to Use ChatGPT When You Have 10 Minutes of Quiet",
    titleZh: "IA para Padres: 7 Formas de Usar ChatGPT Cuando Tienes 10 Minutos de Tranquilidad [CN]",
    description:
      "Kids are finally asleep. You've got 10 minutes. Here are 7 actually-useful things to do with AI — meal plan the week, draft a permission slip, plan a birthday party.",
    descriptionZh:
      "Los niños finalmente están dormidos. Tienes 10 minutos. Aquí hay 7 cosas realmente útiles para hacer con IA — planificar comidas de la semana, redactar una autorización, organizar un cumpleaños. [CN]",
    category: "ai-use-cases",
    tags: ["parents", "busy-lifestyle", "quick-tips", "practical", "life-hacks"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt", "claude"],
    date: "2026-05-12",
  },

  // ====== AI Comparisons (5) ======
  {
    slug: "free-ai-image-generators-same-prompt-test",
    title: "Midjourney Basics: Getting Started with AI Image Creation",
    titleZh: "Fundamentos de Midjourney: Cómo Empezar con la Creación de Imágenes con IA [CN]",
    description:
      "Midjourney produces the highest-quality AI images, but it requires Discord. Here is how to set up, write your first /imagine prompt, and master essential parameters.",
    descriptionZh:
      "Midjourney produce las imágenes de IA de mayor calidad, pero requiere Discord. Aquí te mostramos cómo configurarlo, escribir tu primer prompt /imagine y dominar los parámetros esenciales. [CN]",
    category: "ai-comparisons",
    tags: ["midjourney", "image-generation", "tutorial", "discord", "beginner"],
    difficulty: "beginner",
    toolsMentioned: ["midjourney"],
    date: "2026-05-22",
  },
  {
    slug: "chatgpt-free-vs-plus-2026-what-you-get",
    title: "ChatGPT Free vs Plus in 2026: What You Actually Get Without Paying",
    titleZh: "ChatGPT Gratis vs Plus en 2026: Lo Que Realmente Obtienes Sin Pagar [CN]",
    description:
      "OpenAI keeps changing what's free and what's not. Here's the updated 2026 breakdown: image generation limits, message caps, GPT-5 access, and which paid features are now free.",
    descriptionZh:
      "OpenAI sigue cambiando lo que es gratis y lo que no. Aquí está el desglose actualizado de 2026: límites de generación de imágenes, topes de mensajes, acceso a GPT-5 y qué funciones pagas ahora son gratis. [CN]",
    category: "ai-comparisons",
    tags: ["chatgpt", "free-vs-paid", "pricing", "2026", "updated"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt"],
    date: "2026-05-17",
  },
  {
    slug: "notebooklm-vs-perplexity-research",
    title: "NotebookLM vs Perplexity: Which Is Better for Researching a Topic From Scratch?",
    titleZh: "NotebookLM vs Perplexity: ¿Cuál Es Mejor para Investigar un Tema Desde Cero? [CN]",
    description:
      "Both claim to help you research, but they work completely differently. I used both to research the same topic and compared notes — here's which one actually saved me time.",
    descriptionZh:
      "Ambos afirman ayudarte a investigar, pero funcionan de manera completamente diferente. Usé ambos para investigar el mismo tema y comparé notas — aquí está cuál realmente me ahorró tiempo. [CN]",
    category: "ai-comparisons",
    tags: ["notebooklm", "perplexity", "research", "productivity", "side-by-side"],
    difficulty: "intermediate",
    toolsMentioned: ["perplexity"],
    date: "2026-05-15",
  },
  {
    slug: "claude-vs-chatgpt-writing-blind-test",
    title: "Claude's Writing Style vs ChatGPT: We Asked 10 People Which Sounds More Human",
    titleZh: "Estilo de Escritura de Claude vs ChatGPT: Preguntamos a 10 Personas Cuál Suena Más Humano [CN]",
    description:
      "We generated the same content with both AIs, removed the labels, and asked 10 regular people to pick which version they preferred. The results weren't even close.",
    descriptionZh:
      "Generamos el mismo contenido con ambas IAs, quitamos las etiquetas y preguntamos a 10 personas comunes qué versión preferían. Los resultados no fueron ni siquiera cercanos. [CN]",
    category: "ai-comparisons",
    tags: ["claude", "chatgpt", "writing", "blind-test", "real-people"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt", "claude"],
    date: "2026-05-13",
  },
  {
    slug: "cursor-vs-copilot-complete-beginner",
    title: "Cursor vs GitHub Copilot for a Complete Beginner: Which One Is Less Confusing?",
    titleZh: "Cursor vs GitHub Copilot para un Principiante Total: ¿Cuál Es Menos Confuso? [CN]",
    description:
      "You've never coded before. Both tools promise AI-powered coding, but one has a much gentler learning curve. Here's what each looks like on day one — no experience assumed.",
    descriptionZh:
      "Nunca has programado antes. Ambas herramientas prometen programación con IA, pero una tiene una curva de aprendizaje mucho más suave. Así se ve cada una en el primer día. [CN]",
    category: "ai-comparisons",
    tags: ["cursor", "copilot", "coding", "beginner", "learning-curve"],
    difficulty: "beginner",
    toolsMentioned: ["cursor", "github-copilot"],
    date: "2026-05-11",
  },

  // ====== AI News (5) ======
  {
    slug: "gpt5-for-regular-users",
    title: "GPT-5: What's Actually New and What It Means for Regular Users (Not Developers)",
    titleZh: "GPT-5: Lo Que Realmente Es Nuevo y Qué Significa para Usuarios Comunes (No Desarrolladores) [CN]",
    description:
      "Every GPT-5 article is written for developers. This one isn't. Here's what's actually changed for normal people: better writing, fewer mistakes, and one feature you'll actually use daily.",
    descriptionZh:
      "Cada artículo sobre GPT-5 está escrito para desarrolladores. Este no. Esto es lo que realmente ha cambiado para la gente normal: mejor escritura, menos errores y una función que realmente usarás a diario. [CN]",
    category: "ai-news",
    tags: ["gpt5", "openai", "update", "for-beginners", "whats-new"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt"],
    date: "2026-05-21",
  },
  {
    slug: "open-source-ai-models-run-on-laptop",
    title: "Open Source AI Models in 2026: Which Ones You Can Actually Run on Your Laptop",
    titleZh: "Modelos IA de Código Abierto en 2026: Cuáles Puedes Realmente Ejecutar en Tu Portátil [CN]",
    description:
      "\"Open source AI\" sounds great until you realize most models need a $10,000 GPU. Here are 4 open models that actually run on a normal laptop — and what they're good for.",
    descriptionZh:
      "\"IA de código abierto\" suena genial hasta que te das cuenta de que la mayoría necesita una GPU de $10,000. Aquí hay 4 modelos abiertos que realmente funcionan en un portátil normal. [CN]",
    category: "ai-news",
    tags: ["open-source", "local-ai", "laptop", "free", "models"],
    difficulty: "intermediate",
    toolsMentioned: ["deepseek"],
    date: "2026-05-19",
  },
  {
    slug: "eu-ai-act-plain-english",
    title: "EU AI Act in Plain English: What It Means for the Tools You Use Every Day",
    titleZh: "Ley de IA de la UE en Español Sencillo: Qué Significa para las Herramientas que Usas a Diario [CN]",
    description:
      "The EU just passed rules that affect every AI tool you use. No legalese — here's what's banned, what requires a label, and how it changes ChatGPT, Midjourney, and the rest.",
    descriptionZh:
      "La UE acaba de aprobar reglas que afectan a cada herramienta de IA que usas. Sin jerga legal — esto es lo que está prohibido, lo que requiere etiqueta y cómo cambia ChatGPT, Midjourney y el resto. [CN]",
    category: "ai-news",
    tags: ["eu-ai-act", "regulation", "explained", "plain-english", "policy"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt", "midjourney", "claude"],
    date: "2026-05-17",
  },
  {
    slug: "ai-jobs-that-didnt-exist-3-years-ago",
    title: "AI Jobs That Didn't Exist 3 Years Ago (and How Much They Pay)",
    titleZh: "Trabajos de IA que No Existían Hace 3 Años (y Cuánto Pagan) [CN]",
    description:
      "\"Prompt engineer\" isn't the only one. There's AI safety officer, AI content editor, AI workflow consultant. Here's what these jobs actually do, what they pay, and how to get started.",
    descriptionZh:
      "\"Ingeniero de prompts\" no es el único. Hay oficial de seguridad de IA, editor de contenido de IA, consultor de flujo de trabajo de IA. Esto es lo que realmente hacen estos trabajos, cuánto pagan y cómo empezar. [CN]",
    category: "ai-news",
    tags: ["jobs", "career", "salary", "new-roles", "trends"],
    difficulty: "beginner",
    toolsMentioned: [],
    date: "2026-05-15",
  },
  {
    slug: "apple-intelligence-6-months-later",
    title: "Apple Intelligence 6 Months Later: Which Features Actually Made It to Your iPhone",
    titleZh: "Apple Intelligence 6 Meses Después: Qué Funciones Realmente Llegaron a Tu iPhone [CN]",
    description:
      "Apple announced a lot at WWDC. Half of it shipped late, some of it still says 'coming soon.' Here's what's actually working on your iPhone right now — and what's still vaporware.",
    descriptionZh:
      "Apple anunció mucho en la WWDC. La mitad se lanzó tarde, parte todavía dice 'próximamente.' Esto es lo que realmente funciona en tu iPhone ahora mismo — y lo que sigue siendo humo. [CN]",
    category: "ai-news",
    tags: ["apple", "intelligence", "iphone", "ios", "features"],
    difficulty: "beginner",
    toolsMentioned: [],
    date: "2026-05-13",
  },

  // ====== Claude Code Path (Part 2/4) ======
  {
    slug: "claude-code-mcp-configuration",
    title: "Configure MCP Servers in Claude Code: File Access, APIs, and Databases",
    titleZh: "Configura Servidores MCP en Claude Code: Acceso a Archivos, APIs y Bases de Datos [CN]",
    description:
      "Extend Claude Code's capabilities with MCP (Model Context Protocol) servers. Learn to configure file system access, API integration, and database connections.",
    descriptionZh:
      "Extiende las capacidades de Claude Code con servidores MCP. Aprende a configurar acceso al sistema de archivos, integración de APIs y conexiones a bases de datos. [CN]",
    category: "ai-tutorials",
    tags: ["claude-code", "mcp", "configuration", "servers", "tools"],
    difficulty: "intermediate",
    toolsMentioned: ["claude"],
    date: "2026-05-22",
  },

  // ====== Claude Code Path (Part 3/4) ======
  {
    slug: "claude-code-in-action",
    title: "Claude Code in Action: Build a Real Project from Scratch",
    titleZh: "Claude Code en Acción: Construye un Proyecto Real Desde Cero [CN]",
    description:
      "Watch Claude Code build a complete web application from a single prompt. See the full workflow — planning, coding, debugging, and deployment.",
    descriptionZh:
      "Observa a Claude Code construir una aplicación web completa desde un solo prompt. Ve el flujo de trabajo completo — planificación, codificación, depuración y despliegue. [CN]",
    category: "ai-tutorials",
    tags: ["claude-code", "project", "web-development", "workflow"],
    difficulty: "intermediate",
    toolsMentioned: ["claude"],
    date: "2026-05-22",
  },

  // ====== Claude Code Path (Part 4/4) ======
  {
    slug: "claude-code-advanced",
    title: "Advanced Claude Code: Custom Slash Commands, Hooks, and CI/CD Integration",
    titleZh: "Claude Code Avanzado: Comandos Slash Personalizados, Hooks e Integración CI/CD [CN]",
    description:
      "Take Claude Code to production. Build custom slash commands, pre-commit hooks for code quality, and integrate with your CI/CD pipeline.",
    descriptionZh:
      "Lleva Claude Code a producción. Crea comandos slash personalizados, hooks de pre-commit para calidad de código e intégralo con tu pipeline CI/CD. [CN]",
    category: "ai-tutorials",
    tags: ["claude-code", "advanced", "hooks", "ci-cd", "custom-commands"],
    difficulty: "advanced",
    toolsMentioned: ["claude"],
    date: "2026-05-22",
  },

  // ====== AI Image Generation Path (Part 2/4) ======
  {
    slug: "ai-image-dalle-firefly",
    title: "DALL-E vs Firefly vs Midjourney: Which AI Image Generator Should You Use?",
    titleZh: "DALL-E vs Firefly vs Midjourney: Qué Generador de Imágenes por IA Deberías Usar [CN]",
    description:
      "Compare the three leading AI image generators head-to-head. See real outputs, pricing, and use cases to decide which one fits your workflow.",
    descriptionZh:
      "Compara los tres principales generadores de imágenes por IA cara a cara. Ve resultados reales, precios y casos de uso para decidir cuál se adapta a tu flujo de trabajo. [CN]",
    category: "ai-tutorials",
    tags: ["ai-image", "dalle3", "adobe-firefly", "midjourney", "comparison"],
    difficulty: "beginner",
    toolsMentioned: ["dalle3", "midjourney", "adobe-firefly"],
    date: "2026-05-22",
  },

  // ====== AI Image Generation Path (Part 3/4) ======
  {
    slug: "ai-image-prompt-guide",
    title: "The Ultimate AI Image Prompt Guide: Techniques That Actually Work",
    titleZh: "La Guía Definitiva de Prompts para Imágenes por IA: Técnicas Que Realmente Funcionan [CN]",
    description:
      "Go beyond 'a cat in space.' Learn professional prompt techniques — style references, lighting specs, composition rules, and negative prompts that deliver stunning results.",
    descriptionZh:
      "Ve más allá de 'un gato en el espacio.' Aprende técnicas profesionales de prompts — referencias de estilo, especificaciones de iluminación, reglas de composición y prompts negativos. [CN]",
    category: "ai-tutorials",
    tags: ["ai-image", "prompts", "prompt-engineering", "techniques", "guide"],
    difficulty: "intermediate",
    toolsMentioned: ["dalle3", "midjourney", "adobe-firefly", "stable-diffusion"],
    date: "2026-05-22",
  },

  // ====== AI Image Generation Path (Part 4/4) ======
  {
    slug: "ai-image-commercial-licensing",
    title: "AI Image Copyright and Commercial Licensing: What You Can and Can't Sell",
    titleZh: "Derechos de Autor y Licencias Comerciales de Imágenes por IA: Qué Puedes y No Puedes Vender [CN]",
    description:
      "Navigate the legal landscape of AI-generated images. Understand copyright rules, commercial licenses, and platform-specific terms for DALL-E, Firefly, and Midjourney.",
    descriptionZh:
      "Navega el panorama legal de las imágenes generadas por IA. Comprende las reglas de derechos de autor, licencias comerciales y términos específicos de cada plataforma. [CN]",
    category: "ai-tutorials",
    tags: ["ai-image", "copyright", "licensing", "commercial", "legal"],
    difficulty: "beginner",
    toolsMentioned: ["dalle3", "midjourney", "adobe-firefly"],
    date: "2026-05-22",
  },
];
