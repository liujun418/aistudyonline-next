import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { isValidLocale, getDictionary } from "@/lib/i18n";
import { SITE_URL, SITE_NAME } from "@/lib/constants";
import type { Locale } from "@/lib/i18n";

export async function generateMetadata({
  params,
}: {
  params: Promise<{ locale: string }>;
}): Promise<Metadata> {
  const { locale } = await params;
  if (!isValidLocale(locale)) return {};

  const localeMap: Record<string, string> = { en: "en_US", zh: "zh_CN" };
  const title =
    locale === "zh" ? `关于我们 — ${SITE_NAME}` : `About — ${SITE_NAME}`;
  const description =
    locale === "zh"
      ? "了解AI Study Online——我们致力于让AI教育惠及每一个人的使命。"
      : "Learn about AI Study Online — our mission to make AI education accessible to everyone.";

  return {
    title,
    description,
    openGraph: {
      type: "website",
      locale: localeMap[locale] || "en_US",
      url: `${SITE_URL}/${locale}/about`,
      siteName: SITE_NAME,
      title,
      description,
      images: [{ url: `${SITE_URL}/og-default.png`, width: 1200, height: 630, alt: SITE_NAME }],
    },
    alternates: {
      languages: {
        "x-default": `${SITE_URL}/en/about`,
        en: `${SITE_URL}/en/about`,
        zh: `${SITE_URL}/zh/about`,
      },
    },
  };
}

export default async function AboutPage({
  params,
}: {
  params: Promise<{ locale: string }>;
}) {
  const { locale } = await params;
  if (!isValidLocale(locale)) notFound();

  const dict = await getDictionary(locale as Locale);
  const siteTitle = ((dict as any)?.site?.title || SITE_NAME) as string;

  const content = locale === "zh" ? zhContent : enContent;

  return (
    <div className="mx-auto max-w-3xl px-4 py-12 sm:px-6">
      <h1 className="mb-8 text-3xl font-bold text-foreground">
        {content.pageTitle}
      </h1>

      <section className="mb-10">
        <h2 className="mb-4 text-xl font-semibold text-foreground">
          {content.mission.title}
        </h2>
        <p className="leading-relaxed text-zinc-600 dark:text-zinc-400">
          {content.mission.body}
        </p>
      </section>

      <section className="mb-10">
        <h2 className="mb-4 text-xl font-semibold text-foreground">
          {content.offer.title}
        </h2>
        <ul className="space-y-3 text-zinc-600 dark:text-zinc-400">
          {content.offer.items.map((item, i) => (
            <li key={i} className="flex items-start gap-2">
              <span className="mt-1 shrink-0 text-primary-500">&bull;</span>
              <span>
                <strong className="text-foreground">{item.label}</strong>{" "}
                &mdash; {item.desc}
              </span>
            </li>
          ))}
        </ul>
      </section>

      <section className="mb-10">
        <h2 className="mb-4 text-xl font-semibold text-foreground">
          {content.why.title}
        </h2>
        <p className="leading-relaxed text-zinc-600 dark:text-zinc-400">
          {content.why.body}
        </p>
      </section>

      <section>
        <h2 className="mb-4 text-xl font-semibold text-foreground">
          {content.contact.title}
        </h2>
        <p className="text-zinc-600 dark:text-zinc-400">
          {content.contact.beforeEmail}{" "}
          <a
            href="mailto:jzerov@live.com"
            className="text-primary-600 underline transition-colors hover:text-primary-700 dark:text-primary-400"
          >
            jzerov@live.com
          </a>
          {content.contact.afterEmail}
        </p>
      </section>
    </div>
  );
}

const enContent = {
  pageTitle: `About ${SITE_NAME}`,
  mission: {
    title: "Our Mission",
    body: "AI Study Online helps absolute beginners learn artificial intelligence. We believe AI is for everyone — not just developers and data scientists. Our goal is to make AI knowledge accessible, practical, and actually useful in your daily life and work.",
  },
  offer: {
    title: "What We Offer",
    items: [
      {
        label: "AI Tools Directory",
        desc: "100+ AI tools organized by category, with honest ratings and pricing.",
      },
      {
        label: "Step-by-Step Tutorials",
        desc: "Practical guides that show you exactly what to do, with real examples.",
      },
      {
        label: "Real-World Use Cases",
        desc: "AI for resumes, presentations, writing, and more.",
      },
      {
        label: "Honest Comparisons",
        desc: "Side-by-side tool testing with real results.",
      },
      {
        label: "Latest AI News",
        desc: "What is new and what it means for you.",
      },
    ],
  },
  why: {
    title: "Why We Built This",
    body: "AI is transforming every industry, but most resources are either too technical or too superficial. We created AI Study Online to bridge that gap — offering content that is thorough enough to be useful, yet simple enough for anyone to follow. No jargon, no prerequisites, no gatekeeping.",
  },
  contact: {
    title: "Contact",
    beforeEmail: "Have questions or suggestions? Reach out to us at",
    afterEmail: ".",
  },
};

const zhContent = {
  pageTitle: `关于 ${SITE_NAME}`,
  mission: {
    title: "我们的使命",
    body: "AI Study Online 帮助完全零基础的用户学习人工智能。我们相信AI属于每一个人——不仅仅是开发者和数据科学家。我们的目标是让AI知识变得易于获取、实用，并且真正能在你的日常生活和工作中派上用场。",
  },
  offer: {
    title: "我们提供什么",
    items: [
      {
        label: "AI工具目录",
        desc: "100+款AI工具按类别整理，配有真实的评分和价格信息。",
      },
      {
        label: "分步教程",
        desc: "实用的操作指南，配合真实案例，精确指导每一步该怎么做。",
      },
      {
        label: "真实应用场景",
        desc: "AI在简历、演示文稿、写作等方面的实际应用。",
      },
      {
        label: "客观对比",
        desc: "并排测试AI工具，展示真实对比结果。",
      },
      {
        label: "最新AI资讯",
        desc: "了解最新动态及其对你的影响。",
      },
    ],
  },
  why: {
    title: "为什么创建这个网站",
    body: "AI正在改变每一个行业，但大多数资源要么过于技术化，要么过于肤浅。我们创建AI Study Online正是为了填补这个空白——提供的内容既足够深入以真正有用，又足够简洁让每个人都能跟上。没有行话，没有先修要求，没有门槛。",
  },
  contact: {
    title: "联系我们",
    beforeEmail: "有任何问题或建议？请发送邮件至",
    afterEmail: "。",
  },
};
