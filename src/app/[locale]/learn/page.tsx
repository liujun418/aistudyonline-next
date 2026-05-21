import Link from "next/link";
import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { isValidLocale, getDictionary } from "@/lib/i18n";
import { articles } from "@/lib/articles";
import { categories } from "@/lib/categories";
import { SITE_URL, SITE_NAME } from "@/lib/constants";
import ArticleCard from "@/components/ArticleCard";
import type { Locale } from "@/lib/i18n";

function localized(locale: string, en: string, es: string, ar: string): string {
  if (locale === "es") return es;
  if (locale === "ar") return ar;
  return en;
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ locale: string }>;
}): Promise<Metadata> {
  const { locale } = await params;
  if (!isValidLocale(locale)) return {};

  const dict = await getDictionary(locale as Locale);
  const learnDict = (dict as any)?.learn || {};

  const localeMap: Record<string, string> = { en: "en_US", es: "es_ES", ar: "ar_SA" };

  return {
    title: `${learnDict.title || "Learn AI From Zero"} — ${SITE_NAME}`,
    description:
      learnDict.description ||
      "Practical tutorials and guides for AI beginners. No jargon, just step-by-step instructions.",
    openGraph: {
      type: "website",
      locale: localeMap[locale] || "en_US",
      url: `${SITE_URL}/${locale}/learn`,
      siteName: SITE_NAME,
      title: `${learnDict.title || "Learn AI From Zero"} — ${SITE_NAME}`,
      description:
        learnDict.description ||
        "Practical tutorials and guides for AI beginners.",
      images: [{ url: `${SITE_URL}/og-default.png`, width: 1200, height: 630, alt: SITE_NAME }],
    },
    twitter: {
      card: "summary_large_image",
      title: `${learnDict.title || "Learn AI From Zero"} — ${SITE_NAME}`,
      description:
        learnDict.description ||
        "Practical tutorials and guides for AI beginners.",
      images: [`${SITE_URL}/og-default.png`],
    },
    alternates: {
      languages: {
        "x-default": `${SITE_URL}/en/learn`,
        en: `${SITE_URL}/en/learn`,
        es: `${SITE_URL}/es/learn`,
        ar: `${SITE_URL}/ar/learn`,
      },
    },
  };
}

export default async function LearnPage({
  params,
}: {
  params: Promise<{ locale: string }>;
}) {
  const { locale } = await params;
  if (!isValidLocale(locale)) notFound();

  const dict = await getDictionary(locale as Locale);
  const learnDict = (dict as any)?.learn || {};

  const pageTitle = (learnDict.title as string) || "Learn AI From Zero";
  const pageDescription =
    (learnDict.description as string) ||
    "Practical tutorials and guides for AI beginners.";

  return (
    <div className="mx-auto max-w-6xl px-4 py-8 sm:px-6">
      {/* Page header */}
      <div className="mb-10">
        <h1 className="text-3xl font-bold text-foreground">{pageTitle}</h1>
        <p className="mt-2 text-zinc-600 dark:text-zinc-400">
          {pageDescription}
        </p>
      </div>

      {/* Articles grouped by category */}
      <div className="space-y-12">
        {categories.map((cat) => {
          const catArticles = articles.filter((a) => a.category === cat.id);
          if (catArticles.length === 0) return null;

          const catName = localized(locale, cat.name, cat.nameEs, cat.nameAr);
          const catDesc = localized(
            locale,
            cat.description,
            cat.descriptionEs,
            cat.descriptionAr,
          );

          return (
            <section key={cat.id}>
              {/* Category header */}
              <div className="mb-6 flex items-center gap-3">
                <span className="text-2xl" role="img" aria-label={catName}>
                  {cat.icon}
                </span>
                <div>
                  <h2 className="text-xl font-bold text-foreground">
                    {catName}
                  </h2>
                  <p className="text-sm text-zinc-500 dark:text-zinc-400">
                    {catDesc}
                  </p>
                </div>
              </div>

              {/* Article grid */}
              <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
                {catArticles.slice(0, 4).map((article) => (
                  <ArticleCard
                    key={article.slug}
                    slug={article.slug}
                    title={localized(
                      locale,
                      article.title,
                      article.titleEs,
                      article.titleAr,
                    )}
                    description={localized(
                      locale,
                      article.description,
                      article.descriptionEs,
                      article.descriptionAr,
                    )}
                    category={article.category}
                    date={article.date}
                    locale={locale}
                    tags={article.tags}
                    difficulty={article.difficulty}
                  />
                ))}
              </div>

              {/* View all link */}
              {catArticles.length > 4 && (
                <div className="mt-4 text-right">
                  <Link
                    href={`/${locale}/learn/${cat.slug}`}
                    className="text-sm font-medium text-primary-600 transition-colors hover:text-primary-700 dark:text-primary-400"
                  >
                    View all in {catName} &rarr;
                  </Link>
                </div>
              )}
            </section>
          );
        })}
      </div>
    </div>
  );
}
