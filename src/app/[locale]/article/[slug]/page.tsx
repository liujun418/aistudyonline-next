import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { isValidLocale, getDictionary } from "@/lib/i18n";
import { articles } from "@/lib/articles";
import { articleContents } from "@/lib/article-content";
import { categories } from "@/lib/categories";
import { SITE_URL, SITE_NAME } from "@/lib/constants";
import ArticleLayout from "@/components/ArticleLayout";
import type { Locale } from "@/lib/i18n";

function localized(locale: string, en: string, zh: string): string {
  if (locale === "zh") return zh;
  return en;
}

export async function generateStaticParams() {
  const params: { locale: string; slug: string }[] = [];
  for (const locale of ["en", "zh"]) {
    for (const article of articles) {
      params.push({ locale, slug: article.slug });
    }
  }
  return params;
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ locale: string; slug: string }>;
}): Promise<Metadata> {
  const { locale, slug } = await params;
  if (!isValidLocale(locale)) return {};

  const article = articles.find((a) => a.slug === slug);
  if (!article) return {};

  const title = localized(locale, article.title, article.titleZh);
  const description = localized(
    locale,
    article.description,
    article.descriptionZh,
  );

  const cat = categories.find((c) => c.id === article.category);

  const localeMap: Record<string, string> = { en: "en_US", zh: "zh_CN" };
  const OG_IMAGE = `${SITE_URL}/og-default.png`;

  return {
    title: `${title} — ${SITE_NAME}`,
    description,
    openGraph: {
      type: "article",
      locale: localeMap[locale] || "en_US",
      url: `${SITE_URL}/${locale}/article/${slug}`,
      siteName: SITE_NAME,
      title: `${title} — ${SITE_NAME}`,
      description,
      images: [{ url: OG_IMAGE, width: 1200, height: 630, alt: SITE_NAME }],
      publishedTime: article.date,
      tags: article.tags,
      ...(cat ? { section: cat.name } : {}),
    },
    twitter: {
      card: "summary_large_image",
      title: `${title} — ${SITE_NAME}`,
      description,
      images: [OG_IMAGE],
    },
    alternates: {
      languages: {
        "x-default": `${SITE_URL}/en/article/${slug}`,
        en: `${SITE_URL}/en/article/${slug}`,
        zh: `${SITE_URL}/zh/article/${slug}`,
      },
    },
  };
}

export default async function ArticlePage({
  params,
}: {
  params: Promise<{ locale: string; slug: string }>;
}) {
  const { locale, slug } = await params;
  if (!isValidLocale(locale)) notFound();

  const article = articles.find((a) => a.slug === slug);
  if (!article) notFound();

  const dict = await getDictionary(locale as Locale);

  const title = localized(locale, article.title, article.titleZh);
  const description = localized(
    locale,
    article.description,
    article.descriptionZh,
  );

  const entry = articleContents[article.slug];
  const rawContent = entry
    ? (locale === "zh" ? entry.contentZh : entry.content)
    : `<p>${description}</p><p>Full article content coming soon.</p>`;
  const localizedContent = rawContent.replace(
    /href="\/(article|learn|tools|models|blog)\//g,
    `href="/${locale}/$1/`,
  );

  return (
    <>
      {/* JSON-LD structured data */}
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{
          __html: JSON.stringify([
            {
              "@context": "https://schema.org",
              "@type": "Article",
              headline: title,
              description,
              datePublished: article.date,
              author: {
                "@type": "Organization",
                name: SITE_NAME,
                url: SITE_URL,
              },
              publisher: {
                "@type": "Organization",
                name: SITE_NAME,
                url: SITE_URL,
                logo: {
                  "@type": "ImageObject",
                  url: `${SITE_URL}/favicon-512.png`,
                  width: 512,
                  height: 512,
                },
              },
              image: `${SITE_URL}/og-default.png`,
              mainEntityOfPage: {
                "@type": "WebPage",
                "@id": `${SITE_URL}/${locale}/article/${slug}`,
              },
            },
            {
              "@context": "https://schema.org",
              "@type": "BreadcrumbList",
              itemListElement: [
                {
                  "@type": "ListItem",
                  position: 1,
                  name: SITE_NAME,
                  item: `${SITE_URL}/${locale}`,
                },
                {
                  "@type": "ListItem",
                  position: 2,
                  name: "Learn AI",
                  item: `${SITE_URL}/${locale}/learn`,
                },
                {
                  "@type": "ListItem",
                  position: 3,
                  name: title,
                  item: `${SITE_URL}/${locale}/article/${slug}`,
                },
              ],
            },
          ]),
        }}
      />

      <ArticleLayout
        article={article}
        content={localizedContent}
        locale={locale}
        dict={dict}
      />
    </>
  );
}
