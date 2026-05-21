"use client";

import { useState, useMemo } from "react";
import ToolCard from "@/components/ToolCard";
import { tools, toolCategories, toolCategoryLabels } from "@/lib/tools";
import type { ToolCategory } from "@/lib/tools";

function getToolsDict(dict: Record<string, unknown> | undefined) {
  const t = (dict as any)?.tools || {};
  return {
    title: (t.title as string) || "AI Tools Directory",
    description: (t.description as string) || "Browse 100+ AI tools organized by category.",
    searchPlaceholder: (t.searchPlaceholder as string) || "Search tools...",
    allTools: (t.allTools as string) || "All",
    noResults: (t.noResults as string) || "No tools found. Try a different search or filter.",
  };
}

const difficulties = ["beginner", "intermediate", "advanced"] as const;

export default function ToolsClient({
  locale,
  dict,
}: {
  locale: string;
  dict: Record<string, unknown>;
}) {
  const [searchQuery, setSearchQuery] = useState("");
  const [activeCategory, setActiveCategory] = useState<string>("all");
  const [activeDifficulty, setActiveDifficulty] = useState<string>("all");

  const toolsDict = getToolsDict(dict);

  const filteredTools = useMemo(() => {
    return tools.filter((tool) => {
      // Search filter: match name or description
      if (searchQuery.trim()) {
        const q = searchQuery.trim().toLowerCase();
        const nameMatch = tool.name.toLowerCase().includes(q);
        const descMatch = tool.description.toLowerCase().includes(q);
        if (!nameMatch && !descMatch) return false;
      }

      // Category filter
      if (activeCategory !== "all" && tool.category !== activeCategory) {
        return false;
      }

      // Difficulty filter
      if (activeDifficulty !== "all" && tool.difficulty !== activeDifficulty) {
        return false;
      }

      return true;
    });
  }, [searchQuery, activeCategory, activeDifficulty]);

  function getCatLabel(cat: ToolCategory): string {
    if (locale === "es") return toolCategoryLabels[cat].es;
    if (locale === "ar") return toolCategoryLabels[cat].ar;
    return toolCategoryLabels[cat].en;
  }

  function getDiffLabel(diff: string): string {
    const d = (dict as any)?.tools?.difficulty;
    if (d?.[diff]) return d[diff] as string;
    const fallback: Record<string, string> = {
      beginner: "Beginner",
      intermediate: "Intermediate",
      advanced: "Advanced",
    };
    return fallback[diff] || diff;
  }

  return (
    <div className="px-4 py-10 md:py-14">
      <div className="mx-auto max-w-6xl">
        {/* Page header */}
        <div className="mb-8">
          <h1 className="mb-2 text-3xl font-bold text-foreground md:text-4xl">{toolsDict.title}</h1>
          <p className="text-zinc-600 dark:text-zinc-400">{toolsDict.description}</p>
        </div>

        {/* Search */}
        <div className="mb-6">
          <input
            type="text"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            placeholder={toolsDict.searchPlaceholder}
            className="w-full rounded-lg border border-border bg-surface px-4 py-3 text-sm text-foreground placeholder-zinc-400 outline-none transition focus:border-primary-500 focus:ring-2 focus:ring-primary-200 dark:focus:ring-primary-800"
            aria-label={toolsDict.searchPlaceholder}
          />
        </div>

        {/* Category tabs */}
        <div className="mb-4 overflow-x-auto">
          <div className="flex gap-2 pb-2">
            <button
              onClick={() => setActiveCategory("all")}
              className={`shrink-0 rounded-full px-4 py-2 text-sm font-medium transition ${
                activeCategory === "all"
                  ? "bg-primary-500 text-white"
                  : "bg-surface border border-border text-zinc-600 hover:bg-primary-50 dark:text-zinc-400 dark:hover:bg-primary-950"
              }`}
            >
              {toolsDict.allTools}
            </button>
            {toolCategories.map((cat) => (
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

        {/* Difficulty filter chips */}
        <div className="mb-8 flex gap-2">
          <button
            onClick={() => setActiveDifficulty("all")}
            className={`rounded-lg px-3 py-1.5 text-xs font-medium transition ${
              activeDifficulty === "all"
                ? "bg-zinc-800 text-white dark:bg-zinc-200 dark:text-zinc-900"
                : "bg-surface border border-border text-zinc-600 hover:bg-zinc-100 dark:text-zinc-400 dark:hover:bg-zinc-800"
            }`}
          >
            {toolsDict.allTools}
          </button>
          {difficulties.map((diff) => (
            <button
              key={diff}
              onClick={() => setActiveDifficulty(diff)}
              className={`rounded-lg px-3 py-1.5 text-xs font-medium transition ${
                activeDifficulty === diff
                  ? "bg-zinc-800 text-white dark:bg-zinc-200 dark:text-zinc-900"
                  : "bg-surface border border-border text-zinc-600 hover:bg-zinc-100 dark:text-zinc-400 dark:hover:bg-zinc-800"
              }`}
            >
              {getDiffLabel(diff)}
            </button>
          ))}
        </div>

        {/* Count display */}
        <p className="mb-4 text-sm text-zinc-500 dark:text-zinc-400">
          {locale === "es"
            ? `Mostrando ${filteredTools.length} de ${tools.length} herramientas`
            : locale === "ar"
              ? `عرض ${filteredTools.length} من ${tools.length} أداة`
              : `Showing ${filteredTools.length} of ${tools.length} tools`}
        </p>

        {/* Tool cards grid */}
        {filteredTools.length > 0 ? (
          <div className="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3">
            {filteredTools.map((tool) => (
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
        ) : (
          <div className="rounded-xl border border-border bg-surface p-12 text-center">
            <p className="text-zinc-500 dark:text-zinc-400">{toolsDict.noResults}</p>
          </div>
        )}
      </div>
    </div>
  );
}
