import Link from "next/link";
import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { isValidLocale, getDictionary } from "@/lib/i18n";
import { articles } from "@/lib/articles";
import { categories } from "@/lib/categories";
import { SITE_URL, SITE_NAME } from "@/lib/constants";
import ArticleCard from "@/components/ArticleCard";
import type { Locale } from "@/lib/i18n";

function localized(locale: string, en: string, zh: string): string {
  if (locale === "zh") return zh;
  return en;
}

export async function generateStaticParams() {
  const params: { locale: string; category: string }[] = [];
  for (const locale of ["en", "zh"]) {
    for (const cat of categories) {
      params.push({ locale, category: cat.slug });
    }
  }
  return params;
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ locale: string; category: string }>;
}): Promise<Metadata> {
  const { locale, category } = await params;
  if (!isValidLocale(locale)) return {};

  const cat = categories.find((c) => c.slug === category);
  if (!cat) return {};

  const dict = await getDictionary(locale as Locale);
  const learnDict = (dict as any)?.learn || {};
  const catName = localized(locale, cat.name, cat.nameZh);
  const catDesc = localized(
    locale,
    cat.description,
    cat.descriptionZh,
  );

  const localeMap: Record<string, string> = { en: "en_US", zh: "zh_CN" };
  const pageTitle = `${catName} — ${learnDict.title || "Learn AI From Zero"} — ${SITE_NAME}`;

  return {
    title: pageTitle,
    description: catDesc,
    openGraph: {
      type: "website",
      locale: localeMap[locale] || "en_US",
      url: `${SITE_URL}/${locale}/learn/${category}`,
      siteName: SITE_NAME,
      title: pageTitle,
      description: catDesc,
      images: [{ url: `${SITE_URL}/og-default.png`, width: 1200, height: 630, alt: SITE_NAME }],
    },
    twitter: {
      card: "summary_large_image",
      title: pageTitle,
      description: catDesc,
      images: [`${SITE_URL}/og-default.png`],
    },
    alternates: {
      languages: {
        "x-default": `${SITE_URL}/en/learn/${category}`,
        en: `${SITE_URL}/en/learn/${category}`,
        zh: `${SITE_URL}/zh/learn/${category}`,
      },
    },
  };
}

export default async function CategoryPage({
  params,
}: {
  params: Promise<{ locale: string; category: string }>;
}) {
  const { locale, category } = await params;
  if (!isValidLocale(locale)) notFound();

  const cat = categories.find((c) => c.slug === category);
  if (!cat) notFound();

  const dict = await getDictionary(locale as Locale);
  const learnDict = (dict as any)?.learn || {};

  const catName = localized(locale, cat.name, cat.nameZh);
  const catDesc = localized(
    locale,
    cat.description,
    cat.descriptionZh,
  );

  const catArticles = articles
    .filter((a) => a.category === cat.id)
    .sort((a, b) => b.date.localeCompare(a.date));

  return (
    <div className="mx-auto max-w-6xl px-4 py-8 sm:px-6">
      {/* Breadcrumb */}
      <nav className="mb-6 text-sm text-zinc-500 dark:text-zinc-400">
        <Link
          href={`/${locale}/learn`}
          className="transition-colors hover:text-primary-600"
        >
          {learnDict.title || "Learn AI"}
        </Link>
        <span className="mx-2">/</span>
        <span className="text-zinc-800 dark:text-zinc-200">{catName}</span>
      </nav>

      {/* Category header */}
      <div className="mb-8 flex items-center gap-4">
        <span
          className={`flex h-14 w-14 items-center justify-center rounded-2xl text-2xl ${cat.color}`}
          role="img"
          aria-label={catName}
        >
          {cat.icon}
        </span>
        <div>
          <h1 className="text-3xl font-bold text-foreground">{catName}</h1>
          <p className="mt-1 text-zinc-600 dark:text-zinc-400">{catDesc}</p>
          <p className="mt-1 text-sm text-zinc-400 dark:text-zinc-500">
            {locale === "zh"
              ? `${catArticles.length}篇文章`
              : `${catArticles.length} ${catArticles.length === 1 ? "article" : "articles"}`}
          </p>
        </div>
      </div>

      {/* Article grid */}
      {catArticles.length > 0 ? (
        <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
          {catArticles.map((article) => (
            <ArticleCard
              key={article.slug}
              slug={article.slug}
              title={localized(
                locale,
                article.title,
                article.titleZh,
              )}
              description={localized(
                locale,
                article.description,
                article.descriptionZh,
              )}
              category={article.category}
              date={article.date}
              locale={locale}
              tags={article.tags}
              difficulty={article.difficulty}
            />
          ))}
        </div>
      ) : (
        <div className="rounded-xl border border-border bg-surface p-12 text-center">
          <p className="text-zinc-500 dark:text-zinc-400">
            No articles in this category yet. Check back soon!
          </p>
        </div>
      )}
    </div>
  );
}
