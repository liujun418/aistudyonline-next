import Link from "next/link";
import { categories, Category } from "@/lib/categories";
import { toolDifficultyLabels } from "@/lib/tools";
import { getTagLabel } from "@/lib/i18n";

interface ArticleCardProps {
  slug: string;
  title: string;
  description: string;
  category: string;
  date: string;
  locale: string;
  tags: string[];
  difficulty: "beginner" | "intermediate" | "advanced";
  readingTime?: string;
}

const difficultyStyles: Record<string, string> = {
  beginner: "bg-green-100 text-green-700 dark:bg-green-900/40 dark:text-green-300",
  intermediate: "bg-amber-100 text-amber-700 dark:bg-amber-900/40 dark:text-amber-300",
  advanced: "bg-red-100 text-red-700 dark:bg-red-900/40 dark:text-red-300",
};

export default function ArticleCard({
  slug,
  title,
  description,
  category,
  date,
  locale,
  tags,
  difficulty,
  readingTime,
}: ArticleCardProps) {
  const defaultReadingTime = readingTime || (locale === "zh" ? "5分钟阅读" : "5 min read");
  const cat: Category | undefined = categories.find((c) => c.id === category);
  const catColor = cat?.color?.split(" ")[0] || "bg-primary-100";
  const catTextColor = cat?.color?.split(" ")[1] || "text-primary-700";

  return (
    <article className="flex flex-col rounded-xl border border-border bg-surface p-5 shadow-sm transition hover:shadow-md">
      {/* Category badge */}
      <div className="mb-3 flex items-center justify-between">
        <span className={`inline-block rounded-full px-3 py-1 text-xs font-medium ${catColor || "bg-primary-100"} ${catTextColor || "text-primary-700"}`}>
          {locale === "zh" && cat?.nameZh ? cat.nameZh : (cat?.name || category)}
        </span>
        <span
          className={`rounded-full px-2.5 py-0.5 text-xs font-medium ${difficultyStyles[difficulty]}`}
        >
          {locale === "zh"
            ? (toolDifficultyLabels[difficulty]?.zh || difficulty)
            : (toolDifficultyLabels[difficulty]?.en || difficulty)}
        </span>
      </div>

      {/* Title */}
      <h3 className="mb-2 text-base font-semibold text-foreground">
        <Link
          href={`/${locale}/article/${slug}`}
          className="hover:text-primary-600 transition-colors"
        >
          {title}
        </Link>
      </h3>

      {/* Description */}
      <p className="mb-3 flex-1 text-sm leading-relaxed text-zinc-600 dark:text-zinc-400">
        {description}
      </p>

      {/* Date + Reading time */}
      <div className="mb-3 flex items-center gap-3 text-xs text-zinc-400 dark:text-zinc-500">
        <time dateTime={date}>{date}</time>
        <span aria-hidden="true">&middot;</span>
        <span>{defaultReadingTime}</span>
      </div>

      {/* Tags */}
      {tags.length > 0 && (
        <div className="flex flex-wrap gap-1.5">
          {tags.slice(0, 3).map((tag) => (
            <span
              key={tag}
              className="rounded-md bg-zinc-100 px-2 py-0.5 text-xs text-zinc-600 dark:bg-zinc-800 dark:text-zinc-400"
            >
              {getTagLabel(tag, locale)}
            </span>
          ))}
        </div>
      )}
    </article>
  );
}
