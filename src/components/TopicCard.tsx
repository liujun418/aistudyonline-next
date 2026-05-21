import Link from "next/link";
import type { Category } from "@/lib/categories";

interface TopicCardProps {
  category: Category;
  locale: string;
  articleCount: number;
}

export default function TopicCard({ category, locale, articleCount }: TopicCardProps) {
  const name = locale === "es" ? category.nameEs : locale === "ar" ? category.nameAr : category.name;
  const description =
    locale === "es" ? category.descriptionEs : locale === "ar" ? category.descriptionAr : category.description;

  return (
    <Link
      href={`/${locale}/learn/${category.slug}`}
      className="flex flex-col rounded-xl border border-border bg-surface p-5 shadow-sm transition hover:shadow-md hover:border-primary-300 dark:hover:border-primary-600"
    >
      {/* Icon */}
      <span className="mb-3 text-3xl" role="img" aria-label={name}>
        {category.icon}
      </span>

      {/* Name */}
      <h3 className="mb-1 text-sm font-semibold text-foreground">{name}</h3>

      {/* Description */}
      <p className="mb-3 flex-1 text-xs leading-relaxed text-zinc-500 dark:text-zinc-400">
        {description}
      </p>

      {/* Article count + arrow */}
      <div className="mt-auto flex items-center justify-between text-xs text-primary-600 dark:text-primary-400">
        <span>
          {articleCount} {locale === "es" ? "artículos" : locale === "ar" ? "مقالات" : "articles"}
        </span>
        <svg className="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
        </svg>
      </div>
    </Link>
  );
}
