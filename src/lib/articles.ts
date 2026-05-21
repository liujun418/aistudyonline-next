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
  // ====== Sample: Claude Code (Path: Claude Code 编程入门, Part 1/4) ======
  {
    slug: "claude-code-install-setup",
    title: "Claude Code Installation & Setup: From Zero to Your First AI-Generated Web Page",
    titleEs: "Instalación y Configuración de Claude Code: De Cero a Tu Primera Página Web Generada por IA",
    titleAr: "تثبيت وإعداد Claude Code: من الصفر إلى أول صفحة ويب منشأة بالذكاء الاصطناعي",
    description:
      "Step-by-step guide to installing Claude Code on Windows, Mac, or Linux — with copyable commands, API key setup, and your first AI-generated project.",
    descriptionEs:
      "Guía paso a paso para instalar Claude Code en Windows, Mac o Linux — con comandos copiables, configuración de API key y tu primer proyecto generado por IA.",
    descriptionAr:
      "دليل خطوة بخطوة لتثبيت Claude Code على Windows أو Mac أو Linux — مع أوامر قابلة للنسخ وإعداد مفتاح API وأول مشروع منشأ بالذكاء الاصطناعي.",
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
    titleEs: "Sigo Escuchando Sobre 'LLMs' — Qué Son Realmente en Español Sencillo",
    titleAr: "أستمر في سماع 'LLMs' — ما هي فعلاً بلغة واضحة",
    description:
      "Everyone says 'large language model' like you should know what it means. Here's the actually-simple explanation, with zero technical jargon.",
    descriptionEs:
      "Todo el mundo dice 'modelo de lenguaje grande' como si debieras saber lo que significa. Aquí está la explicación realmente simple, sin jerga técnica.",
    descriptionAr:
      "الجميع يقول 'نموذج لغة كبير' وكأنك يجب أن تعرف ما يعنيه. إليك الشرح البسيط فعلاً، بدون أي مصطلحات تقنية.",
    category: "ai-basics",
    tags: ["llm", "explained", "non-technical", "fundamentals"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt", "claude"],
    date: "2026-05-22",
  },
  {
    slug: "ai-hallucinations-explained-with-examples",
    title: "AI Hallucinations Explained: Why ChatGPT Makes Stuff Up (With Real Examples)",
    titleEs: "Alucinaciones de IA Explicadas: Por Qué ChatGPT Inventa Cosas (Con Ejemplos Reales)",
    titleAr: "شرح هلوسات الذكاء الاصطناعي: لماذا يخترع ChatGPT الأشياء (مع أمثلة حقيقية)",
    description:
      "You asked for a recipe and it invented an ingredient that doesn't exist. Here's why AI hallucinates, how to spot it, and what to do when it happens.",
    descriptionEs:
      "Pediste una receta e inventó un ingrediente que no existe. Esto es por qué la IA alucina, cómo detectarlo y qué hacer cuando sucede.",
    descriptionAr:
      "طلبت وصفة فاخترعت مكوناً غير موجود. إليك لماذا يهلوس الذكاء الاصطناعي، وكيف تكتشفه، وماذا تفعل عندما يحدث.",
    category: "ai-basics",
    tags: ["hallucinations", "chatgpt", "accuracy", "beginner"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt", "claude", "perplexity"],
    date: "2026-05-20",
  },
  {
    slug: "free-vs-paid-ai-tools-worth-it",
    title: "Free vs Paid AI Tools: When It's Actually Worth Paying (and When It's Not)",
    titleEs: "Herramientas IA Gratis vs de Pago: Cuándo Vale la Pena Pagar (y Cuándo No)",
    titleAr: "أدوات الذكاء الاصطناعي المجانية مقابل المدفوعة: متى يستحق الدفع فعلاً (ومتى لا يستحق)",
    description:
      "ChatGPT Plus is $20/month. Claude Pro is $20/month. Midjourney is $10. Do you need any of them? Here's how to decide, based on what you actually use AI for.",
    descriptionEs:
      "ChatGPT Plus cuesta $20/mes. Claude Pro $20/mes. Midjourney $10. ¿Necesitas alguno? Aquí te mostramos cómo decidir, basado en para qué usas realmente la IA.",
    descriptionAr:
      "ChatGPT Plus بـ 20 دولار/شهر. Claude Pro بـ 20 دولار/شهر. Midjourney بـ 10 دولارات. هل تحتاج أياً منها؟ إليك كيفية اتخاذ القرار، بناءً على ما تستخدم الذكاء الاصطناعي من أجله فعلاً.",
    category: "ai-basics",
    tags: ["pricing", "free-vs-paid", "chatgpt", "value", "guide"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt", "claude", "midjourney", "gemini", "perplexity"],
    date: "2026-05-18",
  },
  {
    slug: "what-is-a-gpu-non-techie",
    title: "What's a GPU and Why Does AI Need It? A Non-Techie Explanation",
    titleEs: "¿Qué es una GPU y Por Qué la IA la Necesita? Una Explicación No Técnica",
    titleAr: "ما هي وحدة معالجة الرسومات (GPU) ولماذا يحتاجها الذكاء الاصطناعي؟ شرح غير تقني",
    description:
      "NVIDIA is suddenly worth more than Google because of 'AI chips.' Here's what a GPU actually does, why AI needs thousands of them, and why you should care.",
    descriptionEs:
      "NVIDIA de repente vale más que Google por los 'chips de IA.' Esto es lo que realmente hace una GPU, por qué la IA necesita miles de ellas y por qué debería importarte.",
    descriptionAr:
      "أصبحت NVIDIA فجأة تساوي أكثر من Google بسبب 'رقائق الذكاء الاصطناعي.' إليك ما تفعله وحدة معالجة الرسومات فعلاً، ولماذا يحتاج الذكاء الاصطناعي الآلاف منها، ولماذا يجب أن تهتم.",
    category: "ai-basics",
    tags: ["gpu", "nvidia", "hardware", "explained", "non-technical"],
    difficulty: "beginner",
    toolsMentioned: [],
    date: "2026-05-16",
  },
  {
    slug: "ai-myths-people-still-believe",
    title: "5 AI Myths Your Non-Techie Friends Still Believe (and What's Actually True)",
    titleEs: "5 Mitos de IA que Tus Amigos No Técnicos Siguen Creyendo (y Qué es Realmente Verdad)",
    titleAr: "5 خرافات عن الذكاء الاصطناعي لا يزال أصدقاؤك غير التقنيين يصدقونها (وما هو الصحيح فعلاً)",
    description:
      "\"AI is conscious.\" \"AI will take all jobs.\" \"AI knows everything.\" None of these are true. Here's what the reality looks like in 2026.",
    descriptionEs:
      "\"La IA es consciente.\" \"La IA quitará todos los trabajos.\" \"La IA lo sabe todo.\" Nada de esto es cierto. Así es la realidad en 2026.",
    descriptionAr:
      "\"الذكاء الاصطناعي واعي.\" \"الذكاء الاصطناعي سيأخذ كل الوظائف.\" \"الذكاء الاصطناعي يعرف كل شيء.\" لا شيء من هذا صحيح. إليك كيف يبدو الواقع في عام 2026.",
    category: "ai-basics",
    tags: ["myths", "misconceptions", "explained", "beginner"],
    difficulty: "beginner",
    toolsMentioned: [],
    date: "2026-05-14",
  },

  // ====== AI Tutorials (5) ======
  {
    slug: "chatgpt-voice-mode-job-interview",
    title: "How to Use ChatGPT's Voice Mode to Practice a Job Interview",
    titleEs: "Cómo Usar el Modo de Voz de ChatGPT para Practicar una Entrevista de Trabajo",
    titleAr: "كيفية استخدام وضع الصوت في ChatGPT للتدرب على مقابلة عمل",
    description:
      "You've got an interview next week and nobody to practice with. Here's how to use ChatGPT's voice mode as your mock interviewer — with prompts that actually work.",
    descriptionEs:
      "Tienes una entrevista la próxima semana y nadie con quien practicar. Aquí te mostramos cómo usar el modo de voz de ChatGPT como tu entrevistador de práctica.",
    descriptionAr:
      "لديك مقابلة عمل الأسبوع القادم ولا يوجد أحد لتتمرن معه. إليك كيفية استخدام وضع الصوت في ChatGPT كمحاور تدريبي.",
    category: "ai-tutorials",
    tags: ["chatgpt", "voice-mode", "job-interview", "practice", "hands-on"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt"],
    date: "2026-05-21",
  },
  {
    slug: "claude-projects-organize-chats",
    title: "Claude Projects: How to Organize Your AI Chats Like a Pro (Even If You're Not One)",
    titleEs: "Proyectos de Claude: Cómo Organizar Tus Chats de IA Como un Profesional (Aunque No Lo Seas)",
    titleAr: "مشاريع Claude: كيفية تنظيم محادثات الذكاء الاصطناعي الخاصة بك كمحترف (حتى لو لم تكن كذلك)",
    description:
      "Your Claude sidebar is a mess of random conversations. Projects fix that. Here's how to set them up in 5 minutes and actually find things later.",
    descriptionEs:
      "Tu barra lateral de Claude es un desorden de conversaciones aleatorias. Los Proyectos lo arreglan. Aquí te mostramos cómo configurarlos en 5 minutos.",
    descriptionAr:
      "شريطك الجانبي في Claude فوضى من المحادثات العشوائية. المشاريع تصلح ذلك. إليك كيفية إعدادها في 5 دقائق.",
    category: "ai-tutorials",
    tags: ["claude", "projects", "organization", "productivity", "how-to"],
    difficulty: "beginner",
    toolsMentioned: ["claude"],
    date: "2026-05-19",
  },
  {
    slug: "ai-images-that-dont-look-like-ai",
    title: "How to Generate AI Images That Don't Look Like AI (Beginner's Settings Guide)",
    titleEs: "Cómo Generar Imágenes de IA que No Parezcan de IA (Guía de Configuración para Principiantes)",
    titleAr: "كيفية إنشاء صور بالذكاء الاصطناعي لا تبدو كأنها من الذكاء الاصطناعي (دليل الإعدادات للمبتدئين)",
    description:
      "You can spot AI images from a mile away — weird fingers, plastic skin, that 'AI glow.' Here are the actual settings and prompt tricks that fix each of these.",
    descriptionEs:
      "Puedes detectar imágenes de IA a kilómetros — dedos raros, piel de plástico, ese 'brillo IA.' Aquí están los ajustes y trucos de prompt que arreglan cada uno de estos problemas.",
    descriptionAr:
      "يمكنك تمييز صور الذكاء الاصطناعي من على بعد أميال — أصابع غريبة، بشرة بلاستيكية، ذلك 'التوهج الاصطناعي.' إليك الإعدادات والحيل الفعلية التي تصلح كل منها.",
    category: "ai-tutorials",
    tags: ["image-generation", "midjourney", "dalle", "prompt-tips", "realistic"],
    difficulty: "intermediate",
    toolsMentioned: ["midjourney", "dalle-3", "leonardo-ai"],
    date: "2026-05-17",
  },
  {
    slug: "voice-recording-to-meeting-notes-free",
    title: "How to Turn a Voice Recording Into Meeting Notes Using Free AI Tools",
    titleEs: "Cómo Convertir una Grabación de Voz en Notas de Reunión Usando Herramientas IA Gratuitas",
    titleAr: "كيفية تحويل تسجيل صوتي إلى ملاحظات اجتماع باستخدام أدوات ذكاء اصطناعي مجانية",
    description:
      "You recorded an hour-long meeting on your phone. Now you need notes. Here's a free two-step workflow: transcribe with AI, then summarize — no paid tools needed.",
    descriptionEs:
      "Grabaste una reunión de una hora en tu teléfono. Ahora necesitas notas. Aquí tienes un flujo de trabajo gratuito de dos pasos: transcribe con IA, luego resume.",
    descriptionAr:
      "سجلت اجتماعاً لمدة ساعة على هاتفك. الآن تحتاج ملاحظات. إليك سير عمل مجاني من خطوتين: النسخ بالذكاء الاصطناعي، ثم التلخيص.",
    category: "ai-tutorials",
    tags: ["voice", "transcription", "meeting-notes", "free-tools", "workflow"],
    difficulty: "intermediate",
    toolsMentioned: ["chatgpt", "gemini"],
    date: "2026-05-15",
  },
  {
    slug: "first-ai-coding-project-no-experience",
    title: "Your First AI Coding Project: Build a Simple Web Page Without Knowing How to Code",
    titleEs: "Tu Primer Proyecto de Programación con IA: Construye una Página Web Sin Saber Programar",
    titleAr: "مشروعك الأول في البرمجة بالذكاء الاصطناعي: أنشئ صفحة ويب بسيطة دون معرفة كيفية البرمجة",
    description:
      "You don't need to learn Python to build something useful. We'll use Cursor's free tier to make a personal landing page — and you'll copy-paste the prompts.",
    descriptionEs:
      "No necesitas aprender Python para construir algo útil. Usaremos el nivel gratuito de Cursor para hacer una página personal — y copiarás y pegarás los prompts.",
    descriptionAr:
      "لست بحاجة لتعلم Python لبناء شيء مفيد. سنستخدم الطبقة المجانية من Cursor لإنشاء صفحة هبوط شخصية — وستقوم بنسخ ولصق الأوامر.",
    category: "ai-tutorials",
    tags: ["coding", "cursor", "beginner", "no-code", "project-based"],
    difficulty: "beginner",
    toolsMentioned: ["cursor"],
    date: "2026-05-13",
  },

  // ====== AI Use Cases (5) ======
  {
    slug: "etsy-seller-ai-product-descriptions",
    title: "How a Small Etsy Shop Owner Uses AI to Write Product Descriptions",
    titleEs: "Cómo un Pequeño Vendedor de Etsy Usa IA para Escribir Descripciones de Productos",
    titleAr: "كيف يستخدم صاحب متجر Etsy صغير الذكاء الاصطناعي لكتابة أوصاف المنتجات",
    description:
      "\"I used to spend 2 hours per listing just on the description.\" Here's the exact workflow a real Etsy seller uses — including the prompt template you can steal.",
    descriptionEs:
      "\"Solía pasar 2 horas por anuncio solo en la descripción.\" Aquí está el flujo de trabajo exacto que usa un vendedor real de Etsy — incluyendo la plantilla de prompt que puedes copiar.",
    descriptionAr:
      "\"كنت أقضي ساعتين لكل إعلان على الوصف فقط.\" إليك سير العمل الدقيق الذي يستخدمه بائع Etsy حقيقي — بما في ذلك نموذج الأمر الذي يمكنك سرقته.",
    category: "ai-use-cases",
    tags: ["etsy", "small-business", "product-descriptions", "real-example", "prompt-template"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt", "claude"],
    date: "2026-05-20",
  },
  {
    slug: "ai-wedding-planning-free-tools",
    title: "AI for Wedding Planning: Timeline, Budget, and Speech Help (All Free)",
    titleEs: "IA para Planificación de Bodas: Cronograma, Presupuesto y Ayuda con Discursos (Todo Gratis)",
    titleAr: "الذكاء الاصطناعي لتخطيط حفلات الزفاف: الجدول الزمني والميزانية والمساعدة في الخطاب (كلها مجانية)",
    description:
      "Planning a wedding is basically a part-time job. Here's how to use free AI tools for the timeline, budget tracking, seating chart logic, and even writing your vows.",
    descriptionEs:
      "Planificar una boda es básicamente un trabajo a tiempo parcial. Aquí te mostramos cómo usar herramientas IA gratuitas para el cronograma, presupuesto y hasta escribir tus votos.",
    descriptionAr:
      "التخطيط لحفل زفاف هو في الأساس وظيفة بدوام جزئي. إليك كيفية استخدام أدوات الذكاء الاصطناعي المجانية للجدول الزمني وتتبع الميزانية وحتى كتابة عهود الزواج.",
    category: "ai-use-cases",
    tags: ["wedding", "planning", "free-tools", "life-event", "practical"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt", "gemini", "canva-ai"],
    date: "2026-05-18",
  },
  {
    slug: "ai-travel-itinerary-real-prompts",
    title: "How to Use AI to Plan a 7-Day Trip Itinerary (With Real Prompts You Can Copy)",
    titleEs: "Cómo Usar IA para Planificar un Itinerario de Viaje de 7 Días (Con Prompts Reales que Puedes Copiar)",
    titleAr: "كيفية استخدام الذكاء الاصطناعي لتخطيط برنامج رحلة لمدة 7 أيام (مع أوامر حقيقية يمكنك نسخها)",
    description:
      "Don't pay for a travel agent. Here's how to get ChatGPT to plan your entire 7-day trip — flights, hotels, daily activities, and restaurant recs — with prompts you can copy-paste.",
    descriptionEs:
      "No pagues por un agente de viajes. Aquí te mostramos cómo hacer que ChatGPT planifique todo tu viaje de 7 días — vuelos, hoteles, actividades diarias y recomendaciones de restaurantes.",
    descriptionAr:
      "لا تدفع لوكيل سفر. إليك كيفية جعل ChatGPT يخطط لرحلتك الكاملة لمدة 7 أيام — الرحلات الجوية والفنادق والأنشطة اليومية وتوصيات المطاعم.",
    category: "ai-use-cases",
    tags: ["travel", "itinerary", "chatgpt", "prompt-template", "planning"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt", "gemini"],
    date: "2026-05-16",
  },
  {
    slug: "learn-english-with-ai-free-speaking-practice",
    title: "Learning English With AI: Free Speaking Practice Without a Tutor",
    titleEs: "Aprendiendo Inglés Con IA: Práctica de Conversación Gratis Sin Tutor",
    titleAr: "تعلم الإنجليزية بالذكاء الاصطناعي: ممارسة محادثة مجانية بدون معلم",
    description:
      "English tutors are expensive. Here's how to use ChatGPT's voice mode and other free tools to practice speaking, get pronunciation feedback, and build vocabulary — all for free.",
    descriptionEs:
      "Los tutores de inglés son caros. Aquí te mostramos cómo usar el modo de voz de ChatGPT y otras herramientas gratuitas para practicar conversación y mejorar pronunciación — todo gratis.",
    descriptionAr:
      "مدرسو اللغة الإنجليزية مكلفون. إليك كيفية استخدام وضع الصوت في ChatGPT وأدوات مجانية أخرى لممارسة التحدث والحصول على ملاحظات النطق وبناء المفردات — كل ذلك مجاناً.",
    category: "ai-use-cases",
    tags: ["language-learning", "english", "voice-mode", "free", "speaking"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt", "gemini"],
    date: "2026-05-14",
  },
  {
    slug: "ai-for-parents-quiet-moments",
    title: "AI for Parents: 7 Ways to Use ChatGPT When You Have 10 Minutes of Quiet",
    titleEs: "IA para Padres: 7 Formas de Usar ChatGPT Cuando Tienes 10 Minutos de Tranquilidad",
    titleAr: "الذكاء الاصطناعي للآباء: 7 طرق لاستخدام ChatGPT عندما يكون لديك 10 دقائق من الهدوء",
    description:
      "Kids are finally asleep. You've got 10 minutes. Here are 7 actually-useful things to do with AI — meal plan the week, draft a permission slip, plan a birthday party.",
    descriptionEs:
      "Los niños finalmente están dormidos. Tienes 10 minutos. Aquí hay 7 cosas realmente útiles para hacer con IA — planificar comidas de la semana, redactar una autorización, organizar un cumpleaños.",
    descriptionAr:
      "الأطفال نائمون أخيراً. لديك 10 دقائق. إليك 7 أشياء مفيدة فعلاً يمكنك فعلها بالذكاء الاصطناعي — تخطيط وجبات الأسبوع، كتابة إذن مدرسي، تنظيم حفلة عيد ميلاد.",
    category: "ai-use-cases",
    tags: ["parents", "busy-lifestyle", "quick-tips", "practical", "life-hacks"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt", "claude"],
    date: "2026-05-12",
  },

  // ====== AI Comparisons (5) ======
  {
    slug: "free-ai-image-generators-same-prompt-test",
    title: "I Tested 4 Free AI Image Generators With the Same Prompt — See the Results",
    titleEs: "Probé 4 Generadores de Imagen IA Gratis Con el Mismo Prompt — Mira los Resultados",
    titleAr: "اختبرت 4 مولدات صور مجانية بالذكاء الاصطناعي بنفس الأمر — شاهد النتائج",
    description:
      "Same prompt, four different tools, side by side. I tested DALL-E 3, Leonardo, Firefly, and Stable Diffusion on portraits, landscapes, and text-in-image. One was surprisingly good.",
    descriptionEs:
      "Mismo prompt, cuatro herramientas diferentes, lado a lado. Probé DALL-E 3, Leonardo, Firefly y Stable Diffusion en retratos, paisajes y texto en imagen. Una fue sorprendentemente buena.",
    descriptionAr:
      "نفس الأمر، أربع أدوات مختلفة، جنباً إلى جنب. اختبرت DALL-E 3 وLeonardo وFirefly وStable Diffusion على الصور الشخصية والمناظر الطبيعية والنص في الصورة. واحدة كانت جيدة بشكل مفاجئ.",
    category: "ai-comparisons",
    tags: ["image-generation", "comparison", "free-tools", "side-by-side", "same-prompt"],
    difficulty: "beginner",
    toolsMentioned: ["dalle-3", "leonardo-ai", "adobe-firefly", "stable-diffusion"],
    date: "2026-05-19",
  },
  {
    slug: "chatgpt-free-vs-plus-2026-what-you-get",
    title: "ChatGPT Free vs Plus in 2026: What You Actually Get Without Paying",
    titleEs: "ChatGPT Gratis vs Plus en 2026: Lo Que Realmente Obtienes Sin Pagar",
    titleAr: "ChatGPT المجاني مقابل Plus في 2026: ما تحصل عليه فعلاً بدون دفع",
    description:
      "OpenAI keeps changing what's free and what's not. Here's the updated 2026 breakdown: image generation limits, message caps, GPT-5 access, and which paid features are now free.",
    descriptionEs:
      "OpenAI sigue cambiando lo que es gratis y lo que no. Aquí está el desglose actualizado de 2026: límites de generación de imágenes, topes de mensajes, acceso a GPT-5 y qué funciones pagas ahora son gratis.",
    descriptionAr:
      "تواصل OpenAI تغيير ما هو مجاني وما هو غير مجاني. إليك التفصيل المحدث لعام 2026: حدود إنشاء الصور، وسقف الرسائل، والوصول إلى GPT-5، وأي ميزات مدفوعة أصبحت الآن مجانية.",
    category: "ai-comparisons",
    tags: ["chatgpt", "free-vs-paid", "pricing", "2026", "updated"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt"],
    date: "2026-05-17",
  },
  {
    slug: "notebooklm-vs-perplexity-research",
    title: "NotebookLM vs Perplexity: Which Is Better for Researching a Topic From Scratch?",
    titleEs: "NotebookLM vs Perplexity: ¿Cuál Es Mejor para Investigar un Tema Desde Cero?",
    titleAr: "NotebookLM مقابل Perplexity: أيهما أفضل للبحث في موضوع من الصفر؟",
    description:
      "Both claim to help you research, but they work completely differently. I used both to research the same topic and compared notes — here's which one actually saved me time.",
    descriptionEs:
      "Ambos afirman ayudarte a investigar, pero funcionan de manera completamente diferente. Usé ambos para investigar el mismo tema y comparé notas — aquí está cuál realmente me ahorró tiempo.",
    descriptionAr:
      "كلاهما يدعي مساعدتك في البحث، لكنهما يعملان بشكل مختلف تماماً. استخدمت كليهما للبحث في نفس الموضوع وقارنت الملاحظات — إليك أيهما وفر عليّ الوقت فعلاً.",
    category: "ai-comparisons",
    tags: ["notebooklm", "perplexity", "research", "productivity", "side-by-side"],
    difficulty: "intermediate",
    toolsMentioned: ["perplexity"],
    date: "2026-05-15",
  },
  {
    slug: "claude-vs-chatgpt-writing-blind-test",
    title: "Claude's Writing Style vs ChatGPT: We Asked 10 People Which Sounds More Human",
    titleEs: "Estilo de Escritura de Claude vs ChatGPT: Preguntamos a 10 Personas Cuál Suena Más Humano",
    titleAr: "أسلوب كتابة Claude مقابل ChatGPT: سألنا 10 أشخاص أيهما يبدو أكثر إنسانية",
    description:
      "We generated the same content with both AIs, removed the labels, and asked 10 regular people to pick which version they preferred. The results weren't even close.",
    descriptionEs:
      "Generamos el mismo contenido con ambas IAs, quitamos las etiquetas y preguntamos a 10 personas comunes qué versión preferían. Los resultados no fueron ni siquiera cercanos.",
    descriptionAr:
      "ولدنا نفس المحتوى بكلا الذكاءين الاصطناعيين، وأزلنا العلامات، وسألنا 10 أشخاص عاديين عن النسخة التي يفضلونها. النتائج لم تكن متقاربة حتى.",
    category: "ai-comparisons",
    tags: ["claude", "chatgpt", "writing", "blind-test", "real-people"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt", "claude"],
    date: "2026-05-13",
  },
  {
    slug: "cursor-vs-copilot-complete-beginner",
    title: "Cursor vs GitHub Copilot for a Complete Beginner: Which One Is Less Confusing?",
    titleEs: "Cursor vs GitHub Copilot para un Principiante Total: ¿Cuál Es Menos Confuso?",
    titleAr: "Cursor مقابل GitHub Copilot للمبتدئ تماماً: أيهما أقل إرباكاً؟",
    description:
      "You've never coded before. Both tools promise AI-powered coding, but one has a much gentler learning curve. Here's what each looks like on day one — no experience assumed.",
    descriptionEs:
      "Nunca has programado antes. Ambas herramientas prometen programación con IA, pero una tiene una curva de aprendizaje mucho más suave. Así se ve cada una en el primer día.",
    descriptionAr:
      "لم تبرمج من قبل أبداً. تعدك كلتا الأداتين بالبرمجة المدعومة بالذكاء الاصطناعي، لكن إحداهما لديها منحنى تعلم ألطف بكثير. إليك كيف تبدو كل منهما في اليوم الأول.",
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
    titleEs: "GPT-5: Lo Que Realmente Es Nuevo y Qué Significa para Usuarios Comunes (No Desarrolladores)",
    titleAr: "GPT-5: ما هو الجديد فعلاً وماذا يعني للمستخدمين العاديين (وليس المطورين)",
    description:
      "Every GPT-5 article is written for developers. This one isn't. Here's what's actually changed for normal people: better writing, fewer mistakes, and one feature you'll actually use daily.",
    descriptionEs:
      "Cada artículo sobre GPT-5 está escrito para desarrolladores. Este no. Esto es lo que realmente ha cambiado para la gente normal: mejor escritura, menos errores y una función que realmente usarás a diario.",
    descriptionAr:
      "كل مقال عن GPT-5 مكتوب للمطورين. هذا ليس كذلك. إليك ما تغير فعلاً للأشخاص العاديين: كتابة أفضل، أخطاء أقل، وميزة واحدة ستستخدمها يومياً فعلاً.",
    category: "ai-news",
    tags: ["gpt5", "openai", "update", "for-beginners", "whats-new"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt"],
    date: "2026-05-21",
  },
  {
    slug: "open-source-ai-models-run-on-laptop",
    title: "Open Source AI Models in 2026: Which Ones You Can Actually Run on Your Laptop",
    titleEs: "Modelos IA de Código Abierto en 2026: Cuáles Puedes Realmente Ejecutar en Tu Portátil",
    titleAr: "نماذج الذكاء الاصطناعي مفتوحة المصدر في 2026: أيها يمكنك تشغيله فعلاً على حاسوبك المحمول",
    description:
      "\"Open source AI\" sounds great until you realize most models need a $10,000 GPU. Here are 4 open models that actually run on a normal laptop — and what they're good for.",
    descriptionEs:
      "\"IA de código abierto\" suena genial hasta que te das cuenta de que la mayoría necesita una GPU de $10,000. Aquí hay 4 modelos abiertos que realmente funcionan en un portátil normal.",
    descriptionAr:
      "يبدو 'الذكاء الاصطناعي مفتوح المصدر' رائعاً حتى تدرك أن معظم النماذج تحتاج وحدة معالجة رسومات بـ 10,000 دولار. إليك 4 نماذج مفتوحة تعمل فعلاً على حاسوب محمول عادي.",
    category: "ai-news",
    tags: ["open-source", "local-ai", "laptop", "free", "models"],
    difficulty: "intermediate",
    toolsMentioned: ["deepseek"],
    date: "2026-05-19",
  },
  {
    slug: "eu-ai-act-plain-english",
    title: "EU AI Act in Plain English: What It Means for the Tools You Use Every Day",
    titleEs: "Ley de IA de la UE en Español Sencillo: Qué Significa para las Herramientas que Usas a Diario",
    titleAr: "قانون الذكاء الاصطناعي للاتحاد الأوروبي بلغة واضحة: ماذا يعني للأدوات التي تستخدمها يومياً",
    description:
      "The EU just passed rules that affect every AI tool you use. No legalese — here's what's banned, what requires a label, and how it changes ChatGPT, Midjourney, and the rest.",
    descriptionEs:
      "La UE acaba de aprobar reglas que afectan a cada herramienta de IA que usas. Sin jerga legal — esto es lo que está prohibido, lo que requiere etiqueta y cómo cambia ChatGPT, Midjourney y el resto.",
    descriptionAr:
      "أقر الاتحاد الأوروبي للتو قواعد تؤثر على كل أداة ذكاء اصطناعي تستخدمها. بدون لغة قانونية — إليك ما هو محظور، وما يتطلب تصنيفاً، وكيف يغير ChatGPT وMidjourney والباقي.",
    category: "ai-news",
    tags: ["eu-ai-act", "regulation", "explained", "plain-english", "policy"],
    difficulty: "beginner",
    toolsMentioned: ["chatgpt", "midjourney", "claude"],
    date: "2026-05-17",
  },
  {
    slug: "ai-jobs-that-didnt-exist-3-years-ago",
    title: "AI Jobs That Didn't Exist 3 Years Ago (and How Much They Pay)",
    titleEs: "Trabajos de IA que No Existían Hace 3 Años (y Cuánto Pagan)",
    titleAr: "وظائف الذكاء الاصطناعي التي لم تكن موجودة قبل 3 سنوات (وكم تدفع)",
    description:
      "\"Prompt engineer\" isn't the only one. There's AI safety officer, AI content editor, AI workflow consultant. Here's what these jobs actually do, what they pay, and how to get started.",
    descriptionEs:
      "\"Ingeniero de prompts\" no es el único. Hay oficial de seguridad de IA, editor de contenido de IA, consultor de flujo de trabajo de IA. Esto es lo que realmente hacen estos trabajos, cuánto pagan y cómo empezar.",
    descriptionAr:
      "\"مهندس الأوامر\" ليس الوحيد. هناك مسؤول سلامة الذكاء الاصطناعي، ومحرر محتوى الذكاء الاصطناعي، ومستشار سير عمل الذكاء الاصطناعي. إليك ما تفعله هذه الوظائف فعلاً، وكم تدفع، وكيف تبدأ.",
    category: "ai-news",
    tags: ["jobs", "career", "salary", "new-roles", "trends"],
    difficulty: "beginner",
    toolsMentioned: [],
    date: "2026-05-15",
  },
  {
    slug: "apple-intelligence-6-months-later",
    title: "Apple Intelligence 6 Months Later: Which Features Actually Made It to Your iPhone",
    titleEs: "Apple Intelligence 6 Meses Después: Qué Funciones Realmente Llegaron a Tu iPhone",
    titleAr: "Apple Intelligence بعد 6 أشهر: الميزات التي وصلت فعلاً إلى جهاز iPhone الخاص بك",
    description:
      "Apple announced a lot at WWDC. Half of it shipped late, some of it still says 'coming soon.' Here's what's actually working on your iPhone right now — and what's still vaporware.",
    descriptionEs:
      "Apple anunció mucho en la WWDC. La mitad se lanzó tarde, parte todavía dice 'próximamente.' Esto es lo que realmente funciona en tu iPhone ahora mismo — y lo que sigue siendo humo.",
    descriptionAr:
      "أعلنت Apple عن الكثير في WWDC. نصفه تم شحنه متأخراً، وبعضه لا يزال يقول 'قريباً.' إليك ما يعمل فعلاً على جهاز iPhone الخاص بك الآن — وما لا يزال وعوداً.",
    category: "ai-news",
    tags: ["apple", "intelligence", "iphone", "ios", "features"],
    difficulty: "beginner",
    toolsMentioned: [],
    date: "2026-05-13",
  },
];
