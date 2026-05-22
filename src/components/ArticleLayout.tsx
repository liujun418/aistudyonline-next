"use client";

import Link from "next/link";
import { Article, articles as allArticles } from "@/lib/articles";
import { categories } from "@/lib/categories";
import { tools } from "@/lib/tools";
import ToolCard from "@/components/ToolCard";
import ArticleCard from "@/components/ArticleCard";
import AdUnit from "@/components/AdUnit";
import ShareButtons from "@/components/ShareButtons";

interface ArticleLayoutProps {
  article: Article;
  content: React.ReactNode | string;
  locale: string;
  dict: Record<string, unknown>;
  tocItems?: string[];
}

function localized(
  locale: string,
  en: string,
  zh: string,
): string {
  if (locale === "zh") return zh;
  return en;
}

export default function ArticleLayout({
  article,
  content,
  locale,
  dict,
  tocItems = [],
}: ArticleLayoutProps) {
  const aDict = ((dict as any)?.article || {}) as Record<string, string>;
  const siteTitle = ((dict as any)?.site?.title || "AI Study Online") as string;
  const navLearn = ((dict as any)?.nav?.learn || "Learn AI") as string;

  const cat = categories.find((c) => c.id === article.category);
  const catName = cat
    ? localized(locale, cat.name, cat.nameZh)
    : article.category;

  const title = localized(locale, article.title, article.titleZh);

  const mentionedTools = tools.filter((t) =>
    article.toolsMentioned.includes(t.id),
  );

  // Related articles from the same category, excluding current
  const related = allArticles
    .filter((a) => a.category === article.category && a.slug !== article.slug)
    .slice(0, 3);

  const breadcrumbs = [
    { label: siteTitle, href: `/${locale}` },
    { label: navLearn, href: `/${locale}/learn` },
    ...(cat ? [{ label: catName, href: `/${locale}/learn/${cat.slug}` }] : []),
    { label: title, href: "#" },
  ];

  return (
    <div className="mx-auto max-w-6xl px-4 py-8 sm:px-6">
      {/* Breadcrumb */}
      <nav className="mb-6 flex flex-wrap items-center gap-2 text-sm text-zinc-500 dark:text-zinc-400">
        {breadcrumbs.map((item, idx) => (
          <span key={idx} className="flex items-center gap-2">
            {idx > 0 && <span className="text-zinc-300 dark:text-zinc-600">/</span>}
            {idx < breadcrumbs.length - 1 ? (
              <Link
                href={item.href}
                className="transition-colors hover:text-primary-600"
              >
                {item.label}
              </Link>
            ) : (
              <span className="max-w-[200px] truncate text-zinc-800 dark:text-zinc-200">
                {item.label}
              </span>
            )}
          </span>
        ))}
      </nav>

      {/* Two column layout */}
      <div className="flex flex-col gap-8 lg:flex-row">
        {/* Main content 2/3 */}
        <article className="min-w-0 flex-1 lg:w-2/3">
          {/* Header */}
          <div className="mb-6">
            {cat && (
              <span
                className={`inline-block rounded-full px-3 py-1 text-xs font-medium ${cat.color}`}
              >
                {catName}
              </span>
            )}
            <h1 className="mt-3 text-3xl font-bold text-foreground">{title}</h1>
            <div className="mt-3 flex flex-wrap items-center gap-3 text-sm text-zinc-500 dark:text-zinc-400">
              <time dateTime={article.date}>{article.date}</time>
              <span aria-hidden="true">&middot;</span>
              <span>5 min read</span>
            </div>
          </div>

          {/* Content */}
          <div className="article-content">
            {typeof content === "string" ? (
              <div dangerouslySetInnerHTML={{ __html: content }} />
            ) : (
              content
            )}
          </div>
        </article>

        {/* Sidebar 1/3 sticky */}
        <aside className="lg:w-1/3">
          <div className="sticky top-24 space-y-6">
            {/* On This Page */}
            {tocItems.length > 0 && (
              <div className="rounded-xl border border-border bg-surface p-5">
                <h3 className="mb-3 text-sm font-semibold text-foreground">
                  {aDict.tableOfContents || "On This Page"}
                </h3>
                <nav className="article-toc space-y-1">
                  {tocItems.map((item, idx) => (
                    <a key={idx} href={`#${item.toLowerCase().replace(/\s+/g, '-').replace(/[^\w一-鿿-]/g, '')}`}>
                      {item}
                    </a>
                  ))}
                </nav>
              </div>
            )}

            {/* Tools Mentioned */}
            {mentionedTools.length > 0 && (
              <div className="space-y-4">
                <h3 className="text-sm font-semibold text-foreground">
                  {aDict.toolsMentioned || "Tools Mentioned"}
                </h3>
                {mentionedTools.slice(0, 3).map((tool) => (
                  <ToolCard
                    key={tool.id}
                    id={tool.id}
                    name={tool.name}
                    description={localized(
                      locale,
                      tool.description,
                      tool.descriptionZh,
                    )}
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
            )}

            {/* Ad Unit */}
            <AdUnit adSlot="7831293092" format="rectangle" />
          </div>
        </aside>
      </div>

      {/* Share Buttons */}
      <ShareButtons
        url={`https://aistudyonline.club/${locale}/article/${article.slug}`}
        title={title}
        locale={locale}
      />

      {/* Bottom Ad */}
      <div className="mx-auto mt-6 max-w-3xl">
        <AdUnit adSlot="8266407367" format="horizontal" />
      </div>

      {/* Related Articles */}
      {related.length > 0 && (
        <section className="mt-8 border-t border-border pt-8">
          <h2 className="mb-6 text-xl font-bold text-foreground">
            {aDict.relatedArticles || "Related Articles"}
          </h2>
          <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
            {related.map((a) => (
              <ArticleCard
                key={a.slug}
                slug={a.slug}
                title={localized(locale, a.title, a.titleZh)}
                description={localized(
                  locale,
                  a.description,
                  a.descriptionZh,
                )}
                category={a.category}
                date={a.date}
                locale={locale}
                tags={a.tags}
                difficulty={a.difficulty}
              />
            ))}
          </div>
        </section>
      )}
    </div>
  );
}
