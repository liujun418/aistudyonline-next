"use client";

import Link from "next/link";
import { tools as allTools } from "@/lib/tools";
import { articles } from "@/lib/articles";
import AdUnit from "@/components/AdUnit";
import ShareButtons from "@/components/ShareButtons";
import type { Tool } from "@/lib/tools";

function getLabel(d: Record<string, unknown> | undefined, section: string, key: string, fallback: string): string {
  const s = (d as any)?.[section];
  if (s?.[key]) return s[key] as string;
  return fallback;
}

function StarRating({ rating }: { rating: number }) {
  return (
    <span className="inline-flex gap-0.5" aria-label={`${rating} out of 5 stars`}>
      {[1, 2, 3, 4, 5].map((star) => (
        <svg
          key={star}
          className={`h-5 w-5 ${star <= rating ? "text-amber-400" : "text-zinc-200 dark:text-zinc-600"}`}
          fill="currentColor"
          viewBox="0 0 20 20"
        >
          <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
        </svg>
      ))}
    </span>
  );
}

const difficultyStyles: Record<string, string> = {
  beginner: "bg-green-100 text-green-700 dark:bg-green-900/40 dark:text-green-300",
  intermediate: "bg-amber-100 text-amber-700 dark:bg-amber-900/40 dark:text-amber-300",
  advanced: "bg-red-100 text-red-700 dark:bg-red-900/40 dark:text-red-300",
};

function DifficultyBadge({ difficulty }: { difficulty: string }) {
  const labels: Record<string, string> = {
    beginner: "Beginner",
    intermediate: "Intermediate",
    advanced: "Advanced",
  };
  return (
    <span className={`rounded-full px-3 py-1 text-xs font-medium ${difficultyStyles[difficulty] || ""}`}>
      {labels[difficulty] || difficulty}
    </span>
  );
}

export default function ToolDetailClient({
  tool,
  locale,
  dict,
}: {
  tool: Tool;
  locale: string;
  dict: Record<string, unknown>;
}) {
  const td = (dict as any)?.toolDetail || {};

  // Locale-aware field selection
  const description = locale === "zh" ? tool.descriptionZh : tool.description;
  const descriptionLong =
    locale === "zh" ? tool.descriptionLongZh : tool.descriptionLong;
  const advantages =
    locale === "zh" ? tool.advantagesZh : tool.advantages;
  const useCases =
    locale === "zh" ? tool.useCasesZh : tool.useCases;
  const targetAudience =
    locale === "zh" ? tool.targetAudienceZh : tool.targetAudience;
  const company = locale === "zh" ? tool.companyZh : tool.company;
  const pros = locale === "zh" ? tool.prosZh : tool.pros;
  const cons = locale === "zh" ? tool.consZh : tool.cons;

  // Related tools: same category, exclude self, max 4
  const relatedTools = allTools
    .filter((t) => t.category === tool.category && t.id !== tool.id)
    .slice(0, 4);

  // Related articles: articles mentioning this tool, max 3
  const relatedArticles = articles
    .filter((a) => a.toolsMentioned.includes(tool.id))
    .slice(0, 3);

  return (
    <main className="mx-auto max-w-5xl px-4 py-8 sm:px-6 lg:px-8" dir="ltr">
      {/* Breadcrumb */}
      <nav className="mb-6 text-sm text-zinc-500 dark:text-zinc-400">
        <Link href={`/${locale}`} className="hover:text-primary-600 transition-colors">
          {td.home || "Home"}
        </Link>
        <span className="mx-2">/</span>
        <Link href={`/${locale}/tools`} className="hover:text-primary-600 transition-colors">
          {td.aiTools || "AI Tools"}
        </Link>
        <span className="mx-2">/</span>
        <span className="text-foreground">{tool.name}</span>
      </nav>

      {/* Hero Header */}
      <section className="mb-10 rounded-2xl border border-border bg-surface p-6 shadow-sm sm:p-8">
        <div className="flex flex-col gap-6 sm:flex-row sm:items-center sm:justify-between">
          <div className="flex items-center gap-4">
            <span className="text-5xl" role="img" aria-label={tool.name}>
              {tool.icon}
            </span>
            <div>
              <div className="flex flex-wrap items-center gap-3">
                <h1 className="text-3xl font-bold text-foreground">{tool.name}</h1>
                <DifficultyBadge difficulty={tool.difficulty} />
              </div>
              <div className="mt-1 flex items-center gap-3">
                <StarRating rating={tool.rating} />
                <span className="text-sm text-zinc-500 dark:text-zinc-400">{tool.category}</span>
              </div>
              <p className="mt-2 text-lg text-zinc-600 dark:text-zinc-400">{description}</p>
            </div>
          </div>
          <div className="flex flex-col items-start gap-2">
            <div className="flex flex-wrap gap-2">
              <a
                href={tool.url}
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex shrink-0 items-center gap-2 rounded-lg bg-primary-500 px-6 py-3 text-sm font-medium text-white transition hover:bg-primary-600"
              >
                {td.visitWebsite || "Visit Website"}
                <svg className="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M14 5l7 7m0 0l-7 7m7-7H3" />
                </svg>
              </a>
              {tool.hasAffiliate && tool.affiliateUrl && (
                <a
                  href={tool.affiliateUrl}
                  target="_blank"
                  rel="sponsored noopener noreferrer"
                  className="inline-flex shrink-0 items-center gap-2 rounded-lg border-2 border-primary-500 bg-white px-6 py-3 text-sm font-medium text-primary-600 transition hover:bg-primary-50 dark:bg-transparent dark:hover:bg-primary-950"
                >
                  {td.affiliateLink || "Get Started (Affiliate Link)"}
                  <svg className="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M14 5l7 7m0 0l-7 7m7-7H3" />
                  </svg>
                </a>
              )}
            </div>
            {tool.hasAffiliate && (
              <p className="text-xs text-zinc-400 dark:text-zinc-500">
                {td.affiliateNotice || "We may earn a commission at no extra cost to you."}
              </p>
            )}
          </div>
        </div>

        {/* Quick Facts */}
        <div className="mt-6 grid grid-cols-2 gap-4 border-t border-border pt-6 sm:grid-cols-3 lg:grid-cols-6">
          {company && (
            <div>
              <p className="text-xs font-medium uppercase tracking-wide text-zinc-400">{td.company || "Company"}</p>
              <p className="mt-0.5 text-sm font-medium text-foreground">{company}</p>
            </div>
          )}
          {tool.founded && (
            <div>
              <p className="text-xs font-medium uppercase tracking-wide text-zinc-400">{td.founded || "Founded"}</p>
              <p className="mt-0.5 text-sm font-medium text-foreground">{tool.founded}</p>
            </div>
          )}
          {tool.headquarters && (
            <div>
              <p className="text-xs font-medium uppercase tracking-wide text-zinc-400">{td.headquarters || "Headquarters"}</p>
              <p className="mt-0.5 text-sm font-medium text-foreground">{tool.headquarters}</p>
            </div>
          )}
          <div>
            <p className="text-xs font-medium uppercase tracking-wide text-zinc-400">{td.pricingRange || "Pricing Range"}</p>
            <p className="mt-0.5 text-sm font-medium text-foreground">{tool.pricing}</p>
          </div>
          <div>
            <p className="text-xs font-medium uppercase tracking-wide text-zinc-400">{td.difficulty || "Difficulty"}</p>
            <p className="mt-0.5 text-sm font-medium text-foreground">{tool.difficulty}</p>
          </div>
          {targetAudience && (
            <div className="col-span-2 sm:col-span-1 lg:col-span-2">
              <p className="text-xs font-medium uppercase tracking-wide text-zinc-400">{td.targetAudience || "Target Audience"}</p>
              <p className="mt-0.5 text-sm font-medium text-foreground">{targetAudience}</p>
            </div>
          )}
        </div>
      </section>

      {/* About / Description */}
      {descriptionLong && (
        <section className="mb-10">
          <h2 className="mb-4 text-2xl font-bold text-foreground">{td.about || "About"}</h2>
          <p className="text-base leading-relaxed text-zinc-600 dark:text-zinc-400">{descriptionLong}</p>
        </section>
      )}

      {/* Key Advantages + Pros & Cons */}
      <div className="mb-10 grid gap-8 lg:grid-cols-2">
        {/* Key Advantages */}
        {advantages.length > 0 && (
          <section>
            <h2 className="mb-4 text-2xl font-bold text-foreground">{td.advantages || "Advantages"}</h2>
            <ul className="space-y-3">
              {advantages.map((adv: string, i: number) => (
                <li key={i} className="flex items-start gap-3">
                  <span className="mt-0.5 flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-primary-100 text-xs font-bold text-primary-700 dark:bg-primary-900/40 dark:text-primary-300">
                    {i + 1}
                  </span>
                  <span className="text-sm text-zinc-600 dark:text-zinc-400">{adv}</span>
                </li>
              ))}
            </ul>
          </section>
        )}

        {/* Pros & Cons */}
        {(pros.length > 0 || cons.length > 0) && (
          <section>
            <h2 className="mb-4 text-2xl font-bold text-foreground">{td.prosCons || "Pros & Cons"}</h2>
            <div className="space-y-4">
              {pros.length > 0 && (
                <div>
                  <h3 className="mb-2 text-sm font-semibold text-green-700 dark:text-green-400">
                    {td.pros || "Pros"}
                  </h3>
                  <ul className="space-y-1.5">
                    {pros.map((p: string, i: number) => (
                      <li key={i} className="flex items-start gap-2 text-sm text-zinc-600 dark:text-zinc-400">
                        <span className="mt-0.5 text-green-500">+</span>
                        {p}
                      </li>
                    ))}
                  </ul>
                </div>
              )}
              {cons.length > 0 && (
                <div>
                  <h3 className="mb-2 text-sm font-semibold text-red-700 dark:text-red-400">
                    {td.cons || "Cons"}
                  </h3>
                  <ul className="space-y-1.5">
                    {cons.map((c: string, i: number) => (
                      <li key={i} className="flex items-start gap-2 text-sm text-zinc-600 dark:text-zinc-400">
                        <span className="mt-0.5 text-red-500">&minus;</span>
                        {c}
                      </li>
                    ))}
                  </ul>
                </div>
              )}
            </div>
          </section>
        )}
      </div>

      {/* Use Cases */}
      {useCases.length > 0 && (
        <section className="mb-10">
          <h2 className="mb-4 text-2xl font-bold text-foreground">{td.useCases || "Use Cases"}</h2>
          <div className="grid gap-4 sm:grid-cols-2">
            {useCases.map((uc: string, i: number) => (
              <div
                key={i}
                className="rounded-xl border border-border bg-surface p-4 shadow-sm transition hover:shadow-md"
              >
                <p className="text-sm text-zinc-600 dark:text-zinc-400">{uc}</p>
              </div>
            ))}
          </div>
        </section>
      )}

      {/* Pricing Table */}
      {tool.pricingTiers.length > 0 && (
        <section className="mb-10">
          <h2 className="mb-4 text-2xl font-bold text-foreground">{td.pricing || "Pricing"}</h2>
          <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
            {tool.pricingTiers.map((tier, i: number) => (
              <div
                key={i}
                className="flex flex-col rounded-xl border border-border bg-surface p-5 shadow-sm transition hover:shadow-md"
              >
                <h3 className="mb-1 text-lg font-semibold text-foreground">{locale === "zh" ? tier.tierZh : tier.tier}</h3>
                <p className="mb-4 text-2xl font-bold text-primary-600">{tier.price}</p>
                <ul className="space-y-2">
                  {(locale === "zh" ? tier.featuresZh : tier.features).map((f: string, j: number) => (
                    <li key={j} className="flex items-start gap-2 text-sm text-zinc-600 dark:text-zinc-400">
                      <svg className="mt-0.5 h-4 w-4 shrink-0 text-green-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                      </svg>
                      {f}
                    </li>
                  ))}
                </ul>
              </div>
            ))}
          </div>
        </section>
      )}

      {/* Ad */}
      <div className="mb-10 flex justify-center">
        <AdUnit adSlot="7831293092" format="rectangle" />
      </div>

      {/* Extensions & Plugins */}
      {tool.extensions.length > 0 && (
        <section className="mb-10">
          <h2 className="mb-4 text-2xl font-bold text-foreground">{td.extensions || "Extensions & Plugins"}</h2>
          <div className="grid gap-4 sm:grid-cols-2">
            {tool.extensions.map((ext, i: number) => (
              <div
                key={i}
                className="rounded-xl border border-border bg-surface p-4 shadow-sm transition hover:shadow-md"
              >
                <h3 className="text-sm font-semibold text-foreground">{ext.name}</h3>
                <p className="mt-1 text-sm text-zinc-500 dark:text-zinc-400">{locale === "zh" ? ext.descriptionZh : ext.description}</p>
                {ext.url && (
                  <a
                    href={ext.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="mt-2 inline-block text-xs font-medium text-primary-600 hover:text-primary-700 transition-colors"
                  >
                    {ext.url}
                  </a>
                )}
              </div>
            ))}
          </div>
        </section>
      )}

      {/* Skills */}
      {tool.skills.length > 0 && (
        <section className="mb-10">
          <h2 className="mb-4 text-2xl font-bold text-foreground">{td.skills || "Skills"}</h2>
          <div className="flex flex-wrap gap-2">
            {tool.skills.map((skill: string, i: number) => (
              <span
                key={i}
                className="rounded-full border border-primary-200 bg-primary-50 px-3 py-1 text-xs font-medium text-primary-700 dark:border-primary-800 dark:bg-primary-900/30 dark:text-primary-300"
              >
                {skill}
              </span>
            ))}
          </div>
        </section>
      )}

      <section className="mb-10">
      <ShareButtons url={`https://aistudyonline.club/${locale}/tools/${tool.id}`} title={tool.name} locale={locale} />

      </section>

      {/* Related Tools */}
      {relatedTools.length > 0 && (
        <section className="mb-10">
          <h2 className="mb-4 text-2xl font-bold text-foreground">{td.relatedTools || "Related Tools"}</h2>
          <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
            {relatedTools.map((t) => (
              <Link
                key={t.id}
                href={`/${locale}/tools/${t.id}`}
                className="flex flex-col rounded-xl border border-border bg-surface p-4 shadow-sm transition hover:shadow-md hover:border-primary-300"
              >
                <div className="flex items-center gap-3">
                  <span className="text-2xl" role="img" aria-label={t.name}>
                    {t.icon}
                  </span>
                  <div>
                    <h3 className="text-sm font-semibold text-foreground">{t.name}</h3>
                    <StarRating rating={t.rating} />
                  </div>
                </div>
                <p className="mt-2 text-xs leading-relaxed text-zinc-500 dark:text-zinc-400 line-clamp-2">
                  {locale === "zh" ? t.descriptionZh : t.description}
                </p>
              </Link>
            ))}
          </div>
        </section>
      )}

      {/* Related Articles */}
      {relatedArticles.length > 0 && (
        <section className="mb-10">
          <h2 className="mb-4 text-2xl font-bold text-foreground">{td.relatedArticles || "Related Articles"}</h2>
          <div className="space-y-3">
            {relatedArticles.map((a) => (
              <Link
                key={a.slug}
                href={`/${locale}/blog/${a.slug}`}
                className="block rounded-xl border border-border bg-surface p-4 shadow-sm transition hover:shadow-md hover:border-primary-300"
              >
                <h3 className="text-sm font-semibold text-foreground">
                  {locale === "zh" ? a.titleZh : a.title}
                </h3>
                <p className="mt-1 text-xs text-zinc-500 dark:text-zinc-400 line-clamp-2">
                  {locale === "zh" ? a.descriptionZh : a.description}
                </p>
              </Link>
            ))}
          </div>
        </section>
      )}
    </main>
  );
}
