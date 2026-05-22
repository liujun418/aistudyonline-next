"use client";

import AdUnit from "@/components/AdUnit";

import { useState, useMemo } from "react";
import Link from "next/link";
import { models, modelCategories, modelCategoryLabels } from "@/lib/models";
import type { ModelCategory } from "@/lib/models";

function getModelsDict(dict: Record<string, unknown> | undefined) {
  const m = (dict as any)?.models || {};
  return {
    title: (m.title as string) || "AI Models Directory",
    description: (m.description as string) || "Explore 25 cutting-edge AI models from top developers worldwide.",
    searchPlaceholder: (m.searchPlaceholder as string) || "Search models...",
    allModels: (m.allModels as string) || "All",
    noResults: (m.noResults as string) || "No models found. Try a different search or filter.",
    parameters: (m.parameters as string) || "Parameters",
    contextWindow: (m.contextWindow as string) || "Context",
  };
}

export default function ModelListClient({
  locale,
  dict,
}: {
  locale: string;
  dict: Record<string, unknown>;
}) {
  const [searchQuery, setSearchQuery] = useState("");
  const [activeCategory, setActiveCategory] = useState<string>("all");

  const modelsDict = getModelsDict(dict);

  const filteredModels = useMemo(() => {
    return models.filter((model) => {
      if (searchQuery.trim()) {
        const q = searchQuery.trim().toLowerCase();
        const nameMatch = model.name.toLowerCase().includes(q);
        const nameZhMatch = model.nameZh.toLowerCase().includes(q);
        const descMatch = model.description.toLowerCase().includes(q);
        const devMatch = model.developer.toLowerCase().includes(q);
        if (!nameMatch && !nameZhMatch && !descMatch && !devMatch) return false;
      }
      if (activeCategory !== "all" && model.category !== activeCategory) {
        return false;
      }
      return true;
    });
  }, [searchQuery, activeCategory]);

  function getCatLabel(cat: ModelCategory): string {
    if (locale === "zh") return modelCategoryLabels[cat].zh;
    return modelCategoryLabels[cat].en;
  }

  return (
    <div className="px-4 py-10 md:py-14">
      <div className="mx-auto max-w-6xl">
        {/* Page header */}
        <div className="mb-8">
          <h1 className="mb-2 text-3xl font-bold text-foreground md:text-4xl">{modelsDict.title}</h1>
          <p className="text-zinc-600 dark:text-zinc-400">{modelsDict.description}</p>
        </div>

        {/* Search */}
        <div className="mb-6">
          <input
            type="text"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            placeholder={modelsDict.searchPlaceholder}
            className="w-full rounded-lg border border-border bg-surface px-4 py-3 text-sm text-foreground placeholder-zinc-400 outline-none transition focus:border-primary-500 focus:ring-2 focus:ring-primary-200 dark:focus:ring-primary-800"
            aria-label={modelsDict.searchPlaceholder}
          />
        </div>

        {/* Category tabs */}
        <div className="mb-6 overflow-x-auto">
          <div className="flex gap-2 pb-2">
            <button
              onClick={() => setActiveCategory("all")}
              className={`shrink-0 rounded-full px-4 py-2 text-sm font-medium transition ${
                activeCategory === "all"
                  ? "bg-primary-500 text-white"
                  : "bg-surface border border-border text-zinc-600 hover:bg-primary-50 dark:text-zinc-400 dark:hover:bg-primary-950"
              }`}
            >
              {modelsDict.allModels}
            </button>
            {modelCategories.map((cat) => (
              <button
                key={cat}
                onClick={() => setActiveCategory(cat)}
                className={`shrink-0 rounded-full px-4 py-2 text-sm font-medium transition ${
                  activeCategory === cat
                    ? "bg-primary-500 text-white"
                    : "bg-surface border border-border text-zinc-600 hover:bg-primary-50 dark:text-zinc-400 dark:hover:bg-primary-950"
                }`}
              >
                {getCatLabel(cat)}
              </button>
            ))}
          </div>
        </div>

        {/* Count */}
        <p className="mb-4 text-sm text-zinc-500 dark:text-zinc-400">
          {locale === "zh"
            ? `显示 ${filteredModels.length} / ${models.length} 个模型`
            : `Showing ${filteredModels.length} of ${models.length} models`}
        </p>

        {/* Model cards grid */}
        {filteredModels.length > 0 ? (
          <div className="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3">
            {filteredModels.map((model) => (
              <Link
                key={model.id}
                href={`/${locale}/models/${model.id}`}
                className="flex flex-col rounded-xl border border-border bg-surface p-5 shadow-sm transition hover:shadow-md hover:border-primary-300 group"
              >
                {/* Icon + Name + Developer */}
                <div className="mb-3 flex items-start gap-3">
                  <span className="text-3xl" role="img" aria-label={model.name}>
                    {model.icon}
                  </span>
                  <div className="min-w-0 flex-1">
                    <h3 className="text-base font-semibold text-foreground group-hover:text-primary-600 transition-colors">
                      {locale === "zh" ? model.nameZh : model.name}
                    </h3>
                    <p className="text-xs text-zinc-500 dark:text-zinc-400">
                      {locale === "zh" ? model.developerZh : model.developer}
                    </p>
                  </div>
                </div>

                {/* Description */}
                <p className="mb-3 flex-1 text-sm leading-relaxed text-zinc-600 dark:text-zinc-400 line-clamp-2">
                  {locale === "zh" ? model.descriptionZh : model.description}
                </p>

                {/* Tags / Quick info */}
                <div className="mb-2 flex flex-wrap gap-2">
                  {model.contextWindow !== "N/A" && model.contextWindow && (
                    <span className="rounded-md bg-primary-100 px-2 py-0.5 text-xs text-primary-700 dark:bg-primary-900/40 dark:text-primary-300">
                      {model.contextWindow}
                    </span>
                  )}
                  {model.parameters && model.parameters !== "N/A" && (
                    <span className="rounded-md bg-amber-100 px-2 py-0.5 text-xs text-amber-700 dark:bg-amber-900/40 dark:text-amber-300">
                      {model.parameters}
                    </span>
                  )}
                  {model.openSource && (
                    <span className="rounded-md bg-green-100 px-2 py-0.5 text-xs text-green-700 dark:bg-green-900/40 dark:text-green-300">
                      Open Source
                    </span>
                  )}
                </div>

                {/* Pricing */}
                <div className="mt-auto text-xs text-zinc-500 dark:text-zinc-400">
                  {locale === "zh" ? model.pricingZh : model.pricing}
                </div>
              </Link>
            ))}
          </div>
        ) : (
          <div className="rounded-xl border border-border bg-surface p-12 text-center">
            <p className="text-zinc-500 dark:text-zinc-400">{modelsDict.noResults}</p>
          </div>
        )}
        {/* Banner Ad */}
        <div className="mt-8 flex justify-center">
          <AdUnit adSlot="8266407367" format="horizontal" />
        </div>
      </div>
    </div>
  );
}
