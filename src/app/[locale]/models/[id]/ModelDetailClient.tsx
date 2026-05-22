"use client";

import Link from "next/link";
import { models as allModels } from "@/lib/models";
import type { AIModel } from "@/lib/models";

function getLabel(d: Record<string, unknown> | undefined, section: string, key: string, fallback: string): string {
  const s = (d as any)?.[section];
  if (s?.[key]) return s[key] as string;
  return fallback;
}

export default function ModelDetailClient({
  model,
  locale,
  dict,
}: {
  model: AIModel;
  locale: string;
  dict: Record<string, unknown>;
}) {
  const md = (dict as any)?.modelDetail || {};
  const mc = (dict as any)?.models || {};

  // Locale-aware field selection
  const name = locale === "zh" ? model.nameZh : model.name;
  const developer = locale === "zh" ? model.developerZh : model.developer;
  const description = locale === "zh" ? model.descriptionZh : model.description;
  const descriptionLong = locale === "zh" ? model.descriptionLongZh : model.descriptionLong;
  const strengths = locale === "zh" ? model.strengthsZh : model.strengths;
  const weaknesses = locale === "zh" ? model.weaknessesZh : model.weaknesses;
  const bestFor = locale === "zh" ? model.bestForZh : model.bestFor;
  const pricing = locale === "zh" ? model.pricingZh : model.pricing;

  // Related models: same category, exclude self, max 4
  const relatedModels = allModels
    .filter((m) => m.category === model.category && m.id !== model.id)
    .slice(0, 4);

  return (
    <main className="mx-auto max-w-5xl px-4 py-8 sm:px-6 lg:px-8" dir="ltr">
      {/* Breadcrumb */}
      <nav className="mb-6 text-sm text-zinc-500 dark:text-zinc-400">
        <Link href={`/${locale}`} className="hover:text-primary-600 transition-colors">
          {md.home || "Home"}
        </Link>
        <span className="mx-2">/</span>
        <Link href={`/${locale}/models`} className="hover:text-primary-600 transition-colors">
          {md.models || "AI Models"}
        </Link>
        <span className="mx-2">/</span>
        <span className="text-foreground">{name}</span>
      </nav>

      {/* Hero Header */}
      <section className="mb-10 rounded-2xl border border-border bg-surface p-6 shadow-sm sm:p-8">
        <div className="flex flex-col gap-6 sm:flex-row sm:items-center sm:justify-between">
          <div className="flex items-center gap-4">
            <span className="text-5xl" role="img" aria-label={name}>
              {model.icon}
            </span>
            <div>
              <div className="flex flex-wrap items-center gap-3">
                <h1 className="text-3xl font-bold text-foreground">{name}</h1>
                {model.openSource && (
                  <span className="rounded-full bg-green-100 px-3 py-1 text-xs font-medium text-green-700 dark:bg-green-900/40 dark:text-green-300">
                    {md.openSource || "Open Source"}
                  </span>
                )}
              </div>
              <p className="mt-1 text-sm text-zinc-500 dark:text-zinc-400">
                {developer} &middot; {model.releaseDate}
              </p>
              <p className="mt-2 text-lg text-zinc-600 dark:text-zinc-400">{description}</p>
            </div>
          </div>
          <a
            href={model.url}
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex shrink-0 items-center gap-2 rounded-lg bg-primary-500 px-6 py-3 text-sm font-medium text-white transition hover:bg-primary-600"
          >
            {md.visitWebsite || "Visit Website"}
            <svg className="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M14 5l7 7m0 0l-7 7m7-7H3" />
            </svg>
          </a>
        </div>
      </section>

      {/* Quick Facts */}
      <section className="mb-10 rounded-2xl border border-border bg-surface p-6 shadow-sm sm:p-8">
        <h2 className="mb-5 text-2xl font-bold text-foreground">{md.quickFacts || "Quick Facts"}</h2>
        <div className="grid grid-cols-2 gap-x-6 gap-y-4 sm:grid-cols-3 lg:grid-cols-4">
          <FactItem label={md.parameters || "Parameters"} value={model.parameters} />
          <FactItem label={md.contextWindow || "Context Window"} value={model.contextWindow} />
          <FactItem label={md.modalitiesLabel || "Modalities"} value={model.modalities.join(", ")} />
          <FactItem
            label={md.openSource || "Open Source"}
            value={model.openSource ? (md.yes || "Yes") : (md.no || "No")}
          />
          {model.license && (
            <FactItem label={md.license || "License"} value={model.license} />
          )}
          <FactItem label={md.pricingRange || "Pricing"} value={pricing} />
          <FactItem label={md.releaseDate || "Release"} value={model.releaseDate} />
          <FactItem label={md.developer || "Developer"} value={developer} />
        </div>
      </section>

      {/* Description */}
      {descriptionLong && (
        <section className="mb-10">
          <h2 className="mb-4 text-2xl font-bold text-foreground">{md.about || "About"}</h2>
          <p className="text-base leading-relaxed text-zinc-600 dark:text-zinc-400">{descriptionLong}</p>
        </section>
      )}

      {/* Strengths & Weaknesses */}
      <div className="mb-10 grid gap-8 lg:grid-cols-2">
        {strengths.length > 0 && (
          <section>
            <h2 className="mb-4 text-2xl font-bold text-foreground">{md.strengths || "Strengths"}</h2>
            <ul className="space-y-3">
              {strengths.map((s: string, i: number) => (
                <li key={i} className="flex items-start gap-3">
                  <span className="mt-0.5 flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-green-100 text-xs font-bold text-green-700 dark:bg-green-900/40 dark:text-green-300">
                    +
                  </span>
                  <span className="text-sm text-zinc-600 dark:text-zinc-400">{s}</span>
                </li>
              ))}
            </ul>
          </section>
        )}

        {weaknesses.length > 0 && (
          <section>
            <h2 className="mb-4 text-2xl font-bold text-foreground">{md.weaknesses || "Weaknesses"}</h2>
            <ul className="space-y-3">
              {weaknesses.map((w: string, i: number) => (
                <li key={i} className="flex items-start gap-3">
                  <span className="mt-0.5 flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-red-100 text-xs font-bold text-red-700 dark:bg-red-900/40 dark:text-red-300">
                    &minus;
                  </span>
                  <span className="text-sm text-zinc-600 dark:text-zinc-400">{w}</span>
                </li>
              ))}
            </ul>
          </section>
        )}
      </div>

      {/* Best For */}
      {bestFor.length > 0 && (
        <section className="mb-10">
          <h2 className="mb-4 text-2xl font-bold text-foreground">{md.bestFor || "Best For"}</h2>
          <div className="grid gap-4 sm:grid-cols-2">
            {bestFor.map((bf: string, i: number) => (
              <div
                key={i}
                className="rounded-xl border border-border bg-surface p-4 shadow-sm transition hover:shadow-md"
              >
                <p className="text-sm text-zinc-600 dark:text-zinc-400">{bf}</p>
              </div>
            ))}
          </div>
        </section>
      )}

      {/* Pricing Tiers */}
      {model.pricingTiers.length > 0 && (
        <section className="mb-10">
          <h2 className="mb-4 text-2xl font-bold text-foreground">{md.pricing || "Pricing"}</h2>
          <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
            {model.pricingTiers.map((tier, i: number) => (
              <div
                key={i}
                className="flex flex-col rounded-xl border border-border bg-surface p-5 shadow-sm transition hover:shadow-md"
              >
                <h3 className="mb-1 text-lg font-semibold text-foreground">
                  {locale === "zh" ? tier.tierZh : tier.tier}
                </h3>
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

      {/* Benchmarks */}
      {model.benchmarks && model.benchmarks.length > 0 && (
        <section className="mb-10">
          <h2 className="mb-4 text-2xl font-bold text-foreground">{md.benchmarks || "Benchmarks"}</h2>
          <div className="overflow-x-auto rounded-xl border border-border bg-surface">
            <table className="w-full text-sm">
              <thead>
                <tr className="border-b border-border bg-zinc-50 dark:bg-zinc-900/50">
                  <th className="px-4 py-3 text-left font-semibold text-foreground">{md.benchmark || "Benchmark"}</th>
                  <th className="px-4 py-3 text-left font-semibold text-foreground">{name}</th>
                  {model.benchmarks[0].competitor && (
                    <th className="px-4 py-3 text-left font-semibold text-foreground">
                      {md.competitor || "Competitor"}
                    </th>
                  )}
                </tr>
              </thead>
              <tbody>
                {model.benchmarks.map((b, i) => (
                  <tr key={i} className="border-b border-border last:border-0 hover:bg-zinc-50 dark:hover:bg-zinc-900/30">
                    <td className="px-4 py-3 font-medium text-foreground">{b.name}</td>
                    <td className="px-4 py-3 text-green-700 dark:text-green-400">{b.score}</td>
                    {b.competitor && (
                      <td className="px-4 py-3 text-zinc-600 dark:text-zinc-400">
                        {b.competitorScore ? `${b.competitor}: ${b.competitorScore}` : b.competitor}
                      </td>
                    )}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </section>
      )}

      {/* Technical Specs */}
      <section className="mb-10">
        <h2 className="mb-4 text-2xl font-bold text-foreground">{md.techSpecs || "Technical Specs"}</h2>
        <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
          <SpecCard
            label={md.parameters || "Parameters"}
            value={model.parameters}
          />
          <SpecCard
            label={md.contextWindow || "Context Window"}
            value={model.contextWindow}
          />
          <SpecCard
            label={md.modalitiesLabel || "Modalities"}
            value={model.modalities.join(", ")}
          />
          <div className="rounded-xl border border-border bg-surface p-4 shadow-sm">
            <p className="mb-1 text-xs font-medium uppercase tracking-wide text-zinc-400">
              {md.languages || "Languages"}
            </p>
            <div className="flex flex-wrap gap-1.5 mt-1">
              {model.languages.slice(0, 5).map((lang, i) => (
                <span
                  key={i}
                  className="rounded-md bg-primary-100 px-2 py-0.5 text-xs text-primary-700 dark:bg-primary-900/40 dark:text-primary-300"
                >
                  {lang}
                </span>
              ))}
              {model.languages.length > 5 && (
                <span className="rounded-md bg-zinc-100 px-2 py-0.5 text-xs text-zinc-500 dark:bg-zinc-800 dark:text-zinc-400">
                  +{model.languages.length - 5}
                </span>
              )}
            </div>
          </div>
          <SpecCard
            label={md.openSource || "Open Source"}
            value={model.openSource ? (md.yes || "Yes") : (md.no || "No")}
          />
          {model.license && (
            <SpecCard label={md.license || "License"} value={model.license} />
          )}
        </div>
      </section>

      {/* Developer Info */}
      <section className="mb-10 rounded-xl border border-border bg-surface p-6 shadow-sm">
        <div className="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
          <div>
            <h2 className="mb-1 text-2xl font-bold text-foreground">{md.developer || "Developer"}</h2>
            <p className="text-zinc-600 dark:text-zinc-400">{developer}</p>
            {model.releaseDate && (
              <p className="mt-1 text-sm text-zinc-500 dark:text-zinc-400">
                {md.releaseDate || "Released"}: {model.releaseDate}
              </p>
            )}
          </div>
          <div className="flex gap-3">
            {model.apiUrl && (
              <a
                href={model.apiUrl}
                target="_blank"
                rel="noopener noreferrer"
                className="rounded-lg border border-primary-300 px-4 py-2 text-sm font-medium text-primary-700 transition hover:bg-primary-50 dark:border-primary-700 dark:text-primary-300 dark:hover:bg-primary-900/30"
              >
                {md.apiDocs || "API Docs"}
              </a>
            )}
            {model.githubUrl && (
              <a
                href={model.githubUrl}
                target="_blank"
                rel="noopener noreferrer"
                className="rounded-lg border border-zinc-300 px-4 py-2 text-sm font-medium text-zinc-700 transition hover:bg-zinc-50 dark:border-zinc-600 dark:text-zinc-300 dark:hover:bg-zinc-800"
              >
                GitHub
              </a>
            )}
          </div>
        </div>
      </section>

      {/* Related Models */}
      {relatedModels.length > 0 && (
        <section className="mb-10">
          <h2 className="mb-4 text-2xl font-bold text-foreground">{md.relatedModels || "Related Models"}</h2>
          <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
            {relatedModels.map((m) => (
              <Link
                key={m.id}
                href={`/${locale}/models/${m.id}`}
                className="flex flex-col rounded-xl border border-border bg-surface p-4 shadow-sm transition hover:shadow-md hover:border-primary-300"
              >
                <div className="flex items-center gap-3">
                  <span className="text-2xl" role="img" aria-label={m.name}>
                    {m.icon}
                  </span>
                  <div>
                    <h3 className="text-sm font-semibold text-foreground">
                      {locale === "zh" ? m.nameZh : m.name}
                    </h3>
                    <p className="text-xs text-zinc-500 dark:text-zinc-400">
                      {locale === "zh" ? m.developerZh : m.developer}
                    </p>
                  </div>
                </div>
                <p className="mt-2 text-xs leading-relaxed text-zinc-500 dark:text-zinc-400 line-clamp-2">
                  {locale === "zh" ? m.descriptionZh : m.description}
                </p>
              </Link>
            ))}
          </div>
        </section>
      )}
    </main>
  );
}

function FactItem({ label, value }: { label: string; value: string }) {
  return (
    <div>
      <p className="text-xs font-medium uppercase tracking-wide text-zinc-400">{label}</p>
      <p className="mt-0.5 text-sm font-medium text-foreground">{value}</p>
    </div>
  );
}

function SpecCard({ label, value }: { label: string; value: string }) {
  return (
    <div className="rounded-xl border border-border bg-surface p-4 shadow-sm">
      <p className="mb-1 text-xs font-medium uppercase tracking-wide text-zinc-400">{label}</p>
      <p className="text-sm font-medium text-foreground">{value}</p>
    </div>
  );
}
