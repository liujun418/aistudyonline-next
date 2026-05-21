"use client";

import Link from "next/link";
import ToolCard from "@/components/ToolCard";
import ArticleCard from "@/components/ArticleCard";
import TopicCard from "@/components/TopicCard";
import { tools } from "@/lib/tools";
import { articles } from "@/lib/articles";
import { categories } from "@/lib/categories";
import type { Locale } from "@/lib/i18n";

// Hardcoded featured tool IDs for the homepage
const FEATURED_TOOL_IDS = ["chatgpt", "midjourney", "cursor", "elevenlabs"];

// Hardcoded featured article slugs for the homepage
const FEATURED_ARTICLE_SLUGS = [
  "what-is-chatgpt-beginners-guide",
  "chatgpt-vs-claude-comparison",
  "best-ai-tools-for-content-creation",
  "how-to-write-better-prompts",
  "midjourney-vs-dalle-3-vs-stable-diffusion",
  "ai-tools-for-students",
];

function getHome(dict: Record<string, unknown> | undefined) {
  const h = (dict as any)?.home || {};
  return {
    heroTitle: (h.heroTitle as string) || "Learn AI. <span>Actually Use It.</span>",
    heroSubtitle: (h.heroSubtitle as string) || "Zero to productive. Discover AI tools that matter and learn how to use them.",
    exploreTools: (h.exploreTools as string) || "Explore Tools",
    startLearning: (h.startLearning as string) || "Start Learning",
    featuredTools: (h.featuredTools as string) || "Featured AI Tools",
    viewAllTools: (h.viewAllTools as string) || "View All 100+ Tools →",
    latestArticles: (h.latestArticles as string) || "Latest Articles",
    viewAllArticles: (h.viewAllArticles as string) || "View All Articles →",
    browseByCategory: (h.browseByCategory as string) || "Browse by Category",
    features: {
      curated: {
        title: (h.features?.curated?.title as string) || "Curated Tools",
        desc: (h.features?.curated?.desc as string) || "100+ AI tools hand-picked and organized by what you want to do.",
      },
      beginner: {
        title: (h.features?.beginner?.title as string) || "Beginner Friendly",
        desc: (h.features?.beginner?.desc as string) || "No jargon, no prerequisites. Every guide is written for someone starting from zero.",
      },
      tutorials: {
        title: (h.features?.tutorials?.title as string) || "Step-by-Step Guides",
        desc: (h.features?.tutorials?.desc as string) || "Practical tutorials that show you exactly what to click, type, and expect.",
      },
      multilingual: {
        title: (h.features?.multilingual?.title as string) || "Multi-Language",
        desc: (h.features?.multilingual?.desc as string) || "Content available in English, Spanish, and Arabic. Learn in your preferred language.",
      },
    },
  };
}

export default function HomeClient({
  locale,
  dict,
}: {
  locale: string;
  dict: Record<string, unknown>;
}) {
  const home = getHome(dict);
  const featuredTools = tools.filter((t) => FEATURED_TOOL_IDS.includes(t.id));
  const featuredArticles = articles.filter((a) => FEATURED_ARTICLE_SLUGS.includes(a.slug));

  const articleCountMap: Record<string, number> = {};
  articles.forEach((a) => {
    articleCountMap[a.category] = (articleCountMap[a.category] || 0) + 1;
  });

  const features = [
    { title: home.features.curated.title, desc: home.features.curated.desc },
    { title: home.features.beginner.title, desc: home.features.beginner.desc },
    { title: home.features.tutorials.title, desc: home.features.tutorials.desc },
    { title: home.features.multilingual.title, desc: home.features.multilingual.desc },
  ];

  return (
    <div>
      {/* Section 1: Hero */}
      <section className="bg-gradient-to-b from-primary-100 to-primary-50 px-4 py-20 md:py-28 dark:from-primary-950 dark:to-zinc-950">
        <div className="mx-auto max-w-3xl text-center">
          <h1
            className="mb-4 text-4xl font-extrabold leading-tight text-foreground md:text-5xl lg:text-6xl"
            dangerouslySetInnerHTML={{ __html: home.heroTitle }}
          />
          <p className="mx-auto mb-8 max-w-2xl text-lg text-zinc-600 dark:text-zinc-400">
            {home.heroSubtitle}
          </p>
          <div className="flex flex-col items-center justify-center gap-4 sm:flex-row">
            <Link
              href={`/${locale}/tools`}
              className="rounded-lg bg-primary-500 px-8 py-3 text-sm font-semibold text-white shadow-md transition hover:bg-primary-600"
            >
              {home.exploreTools}
            </Link>
            <Link
              href={`/${locale}/learn`}
              className="rounded-lg border-2 border-primary-500 px-8 py-3 text-sm font-semibold text-primary-600 transition hover:bg-primary-50 dark:text-primary-400 dark:hover:bg-primary-950"
            >
              {home.startLearning}
            </Link>
          </div>
        </div>
      </section>

      {/* Section 2: Featured Tools */}
      <section className="px-4 py-16 md:py-20">
        <div className="mx-auto max-w-6xl">
          <div className="mb-8 flex items-center justify-between">
            <h2 className="text-2xl font-bold text-foreground md:text-3xl">{home.featuredTools}</h2>
            <Link
              href={`/${locale}/tools`}
              className="text-sm font-medium text-primary-600 hover:text-primary-500 dark:text-primary-400"
            >
              {home.viewAllTools}
            </Link>
          </div>
          <div className="grid grid-cols-2 gap-4 md:grid-cols-4">
            {featuredTools.map((tool) => (
              <ToolCard
                key={tool.id}
                id={tool.id}
                name={tool.name}
                description={tool.description}
                category={tool.category}
                tags={tool.tags}
                difficulty={tool.difficulty}
                url={tool.url}
                rating={tool.rating}
                pricing={tool.pricing}
                icon={tool.icon}
                locale={locale}
                dict={dict}
              />
            ))}
          </div>
        </div>
      </section>

      {/* Section 3: Latest Articles */}
      <section className="bg-surface-alt px-4 py-16 md:py-20 dark:bg-zinc-900/50">
        <div className="mx-auto max-w-6xl">
          <div className="mb-8 flex items-center justify-between">
            <h2 className="text-2xl font-bold text-foreground md:text-3xl">{home.latestArticles}</h2>
            <Link
              href={`/${locale}/learn`}
              className="text-sm font-medium text-primary-600 hover:text-primary-500 dark:text-primary-400"
            >
              {home.viewAllArticles}
            </Link>
          </div>
          <div className="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3">
            {featuredArticles.map((article) => (
              <ArticleCard
                key={article.slug}
                slug={article.slug}
                title={locale === "es" ? article.titleEs : locale === "ar" ? article.titleAr : article.title}
                description={
                  locale === "es" ? article.descriptionEs : locale === "ar" ? article.descriptionAr : article.description
                }
                category={article.category}
                date={article.date}
                locale={locale}
                tags={article.tags}
                difficulty={article.difficulty}
              />
            ))}
          </div>
        </div>
      </section>

      {/* Section 4: Browse by Category */}
      <section className="px-4 py-16 md:py-20">
        <div className="mx-auto max-w-6xl">
          <h2 className="mb-8 text-center text-2xl font-bold text-foreground md:text-3xl">
            {home.browseByCategory}
          </h2>
          <div className="grid grid-cols-2 gap-4 md:grid-cols-3 lg:grid-cols-5">
            {categories.map((cat) => (
              <TopicCard
                key={cat.id}
                category={cat}
                locale={locale}
                articleCount={articleCountMap[cat.id] || 1}
              />
            ))}
          </div>
        </div>
      </section>

      {/* Section 5: Features */}
      <section className="bg-surface-alt px-4 py-16 md:py-20 dark:bg-zinc-900/50">
        <div className="mx-auto max-w-6xl">
          <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-4">
            {features.map((feature, i) => (
              <div
                key={i}
                className="rounded-xl border border-border bg-surface p-6 text-center shadow-sm"
              >
                <h3 className="mb-2 text-base font-semibold text-foreground">{feature.title}</h3>
                <p className="text-sm leading-relaxed text-zinc-600 dark:text-zinc-400">{feature.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>
    </div>
  );
}
