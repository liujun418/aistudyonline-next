"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import Link from "next/link";
import ToolCard from "@/components/ToolCard";
import ArticleCard from "@/components/ArticleCard";
import TopicCard from "@/components/TopicCard";
import { tools } from "@/lib/tools";
import { models } from "@/lib/models";
import { articles } from "@/lib/articles";
import { categories } from "@/lib/categories";
import { topTools } from "@/lib/rankings";
import type { Locale } from "@/lib/i18n";

// Hardcoded featured tool IDs for the homepage
const FEATURED_TOOL_IDS = ["chatgpt", "midjourney", "cursor", "elevenlabs"];

// Hardcoded featured model IDs for the homepage
const FEATURED_MODEL_IDS = ["gpt-4o", "claude-4-opus", "gemini-2-5-pro", "deepseek-r1"];

// Editor's Picks — auto-selected: 4 newest articles across different categories, updated daily
function getEditorsPicks() {
  // Sort by date desc, then pick up to 4 with unique categories for variety
  const byDate = [...articles].sort((a, b) => b.date.localeCompare(a.date));
  const seen = new Set<string>();
  const picks: typeof articles = [];
  for (const a of byDate) {
    if (!seen.has(a.category) && picks.length < 4) {
      seen.add(a.category);
      picks.push(a);
    }
  }
  // If we didn't get 4 unique categories, fill from remaining newest
  if (picks.length < 4) {
    for (const a of byDate) {
      if (!picks.includes(a)) {
        picks.push(a);
        if (picks.length >= 4) break;
      }
    }
  }
  return picks.map((a) => a.slug);
}

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
    searchPlaceholder: (h.searchPlaceholder as string) || "Search any AI tool...",
    hotTools: (h.hotTools as string) || "Top 10 AI Tools This Week",
    exploreTools: (h.exploreTools as string) || "Explore Tools",
    startLearning: (h.startLearning as string) || "Start Learning",
    featuredTools: (h.featuredTools as string) || "Featured AI Tools",
    viewAllTools: (h.viewAllTools as string) || "View All 100+ Tools →",
    featuredModels: (h.featuredModels as string) || "Featured AI Models",
    viewAllModels: (h.viewAllModels as string) || "View All 25+ Models →",
    editorPicks: (h.editorPicks as string) || "Editor's Picks",
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
        desc: (h.features?.multilingual?.desc as string) || "Content available in English and Chinese. Learn in your preferred language.",
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
  const router = useRouter();
  const [heroSearch, setHeroSearch] = useState("");

  const home = getHome(dict);
  const featuredTools = tools.filter((t) => FEATURED_TOOL_IDS.includes(t.id));
  const featuredModels = models.filter((m) => FEATURED_MODEL_IDS.includes(m.id));
  const editorsPicks = getEditorsPicks()
    .map((slug) => articles.find((a) => a.slug === slug))
    .filter(Boolean) as typeof articles;
  const featuredArticles = articles.filter((a) => FEATURED_ARTICLE_SLUGS.includes(a.slug));
  const latestArticles = articles
    .sort((a, b) => b.date.localeCompare(a.date))
    .slice(0, 6);

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

          {/* Hero Search Box */}
          <form
            onSubmit={(e) => {
              e.preventDefault();
              const q = heroSearch.trim();
              if (q) router.push(`/${locale}/tools?q=${encodeURIComponent(q)}`);
            }}
            className="mx-auto mb-8 max-w-xl"
          >
            <div className="relative">
              <svg
                className="absolute left-4 top-1/2 h-5 w-5 -translate-y-1/2 text-zinc-400"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
              </svg>
              <input
                type="text"
                value={heroSearch}
                onChange={(e) => setHeroSearch(e.target.value)}
                placeholder={home.searchPlaceholder || "Search any AI tool..."}
                className="w-full rounded-xl border border-border bg-surface/80 py-4 pl-12 pr-4 text-sm text-foreground placeholder-zinc-400 shadow-sm backdrop-blur outline-none transition focus:border-primary-500 focus:ring-2 focus:ring-primary-200 dark:focus:ring-primary-800"
                aria-label={home.searchPlaceholder || "Search any AI tool..."}
              />
            </div>
          </form>

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

      {/* Section 2: Featured Models */}
      <section className="bg-surface-alt px-4 py-16 md:py-20 dark:bg-zinc-900/50">
        <div className="mx-auto max-w-6xl">
          <div className="mb-8 flex items-center justify-between">
            <h2 className="text-2xl font-bold text-foreground md:text-3xl">{home.featuredModels}</h2>
            <Link
              href={`/${locale}/models`}
              className="text-sm font-medium text-primary-600 hover:text-primary-500 dark:text-primary-400"
            >
              {home.viewAllModels}
            </Link>
          </div>
          <div className="grid grid-cols-2 gap-4 md:grid-cols-4">
            {featuredModels.map((model) => (
              <Link
                key={model.id}
                href={`/${locale}/models/${model.id}`}
                className="flex flex-col rounded-xl border border-border bg-surface p-4 shadow-sm transition hover:shadow-md hover:border-primary-300 group"
              >
                <div className="flex items-center gap-3 mb-2">
                  <span className="text-2xl" role="img" aria-label={model.name}>
                    {model.icon}
                  </span>
                  <div>
                    <h3 className="text-sm font-semibold text-foreground group-hover:text-primary-600 transition-colors">
                      {locale === "zh" ? model.nameZh : model.name}
                    </h3>
                    <p className="text-xs text-zinc-500 dark:text-zinc-400">
                      {locale === "zh" ? model.developerZh : model.developer}
                    </p>
                  </div>
                </div>
                <p className="text-xs leading-relaxed text-zinc-600 dark:text-zinc-400 line-clamp-2">
                  {locale === "zh" ? model.descriptionZh : model.description}
                </p>
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* Section 3: Hot Tools Ranking */}
      <section className="px-4 py-16 md:py-20">
        <div className="mx-auto max-w-6xl">
          <div className="mb-8 flex items-center justify-between">
            <h2 className="text-2xl font-bold text-foreground md:text-3xl">{home.hotTools}</h2>
            <Link
              href={`/${locale}/tools`}
              className="text-sm font-medium text-primary-600 hover:text-primary-500 dark:text-primary-400"
            >
              {home.viewAllTools}
            </Link>
          </div>
          <div className="grid grid-cols-2 gap-4 md:grid-cols-5">
            {topTools.map((entry) => {
              const tool = tools.find((t) => t.id === entry.toolId);
              if (!tool) return null;
              return (
                <Link
                  key={entry.rank}
                  href={`/${locale}/tools/${tool.id}`}
                  className="group flex flex-col rounded-xl border border-border bg-surface p-4 shadow-sm transition hover:shadow-md hover:border-primary-300"
                >
                  <div className="mb-2 flex items-center justify-between">
                    <span className="flex h-7 w-7 items-center justify-center rounded-full bg-primary-500 text-xs font-bold text-white">
                      {entry.rank}
                    </span>
                    <span className="text-xl" role="img" aria-label={tool.name}>
                      {tool.icon}
                    </span>
                  </div>
                  <h3 className="mb-1 text-sm font-semibold text-foreground group-hover:text-primary-600 transition-colors">
                    {tool.name}
                  </h3>
                  <p className="text-xs leading-relaxed text-zinc-500 dark:text-zinc-400 line-clamp-3">
                    {locale === "zh" ? entry.reasonZh : entry.reason}
                  </p>
                </Link>
              );
            })}
          </div>
        </div>
      </section>

      {/* Section 4: Editor's Picks */}
      <section className="bg-surface-alt px-4 py-16 md:py-20 dark:bg-zinc-900/50">
        <div className="mx-auto max-w-6xl">
          <div className="mb-8 flex items-center justify-between">
            <h2 className="text-2xl font-bold text-foreground md:text-3xl">
              <span className="mr-2" role="img" aria-label="star">⭐</span>
              {home.editorPicks}
            </h2>
            <Link
              href={`/${locale}/learn`}
              className="text-sm font-medium text-primary-600 hover:text-primary-500 dark:text-primary-400"
            >
              {home.viewAllArticles}
            </Link>
          </div>
          <div className="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-4">
            {editorsPicks.map((article) => (
              <ArticleCard
                key={article.slug}
                slug={article.slug}
                title={locale === "zh" ? article.titleZh : article.title}
                description={
                  locale === "zh" ? article.descriptionZh : article.description
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

      {/* Section 5: Latest Articles */}
      <section className="px-4 py-16 md:py-20">
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
            {latestArticles.map((article) => (
              <ArticleCard
                key={article.slug}
                slug={article.slug}
                title={locale === "zh" ? article.titleZh : article.title}
                description={
                  locale === "zh" ? article.descriptionZh : article.description
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

      {/* Section 6: Browse by Category */}
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

      {/* Section 6: Features */}
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
