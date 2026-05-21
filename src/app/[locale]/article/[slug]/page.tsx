import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { isValidLocale, getDictionary } from "@/lib/i18n";
import { articles } from "@/lib/articles";
import { categories } from "@/lib/categories";
import { SITE_URL, SITE_NAME } from "@/lib/constants";
import ArticleLayout from "@/components/ArticleLayout";
import type { Locale } from "@/lib/i18n";

function localized(locale: string, en: string, es: string, ar: string): string {
  if (locale === "es") return es;
  if (locale === "ar") return ar;
  return en;
}

export async function generateStaticParams() {
  const params: { locale: string; slug: string }[] = [];
  for (const locale of ["en", "es", "ar"]) {
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

  const title = localized(locale, article.title, article.titleEs, article.titleAr);
  const description = localized(
    locale,
    article.description,
    article.descriptionEs,
    article.descriptionAr,
  );

  const cat = categories.find((c) => c.id === article.category);

  const localeMap: Record<string, string> = { en: "en_US", es: "es_ES", ar: "ar_SA" };
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
        es: `${SITE_URL}/es/article/${slug}`,
        ar: `${SITE_URL}/ar/article/${slug}`,
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

  const title = localized(locale, article.title, article.titleEs, article.titleAr);
  const description = localized(
    locale,
    article.description,
    article.descriptionEs,
    article.descriptionAr,
  );

  // Placeholder article content — will be replaced with real content later
  const content = `
    <h2>Introduction</h2>
    <p>Welcome to our guide on <strong>${title}</strong>. ${
    article.category === "ai-basics"
      ? "This article will help you understand the fundamentals."
      : article.category === "ai-tutorials"
        ? "Follow along with our step-by-step instructions to get started."
        : article.category === "ai-comparisons"
          ? "We put these tools head-to-head so you can make an informed decision."
          : article.category === "ai-use-cases"
            ? "Discover practical ways to apply AI to real-world tasks."
            : "Stay up to date with the latest developments in AI."
  }</p>

    <h2>What You Need to Know</h2>
    <p>${description}</p>
    <p>This article is being written. We are preparing detailed, hands-on content to help you get the most out of this topic. Check back soon for the full guide.</p>

    <h2>Getting Started</h2>
    <p>In the meantime, explore our <a href="/${locale}/learn">Learn AI</a> section for more tutorials and guides. You can also browse the <a href="/${locale}/tools">AI Tools Directory</a> to discover tools mentioned in this article.</p>

    <h2>Key Points</h2>
    <ul>
      <li>Full step-by-step instructions are being prepared</li>
      <li>Practical examples and real-world use cases will be included</li>
      <li>Screenshots and visual aids are being created</li>
      <li>Tips and best practices from experienced users will be added</li>
    </ul>
  `;

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
        content={content}
        locale={locale}
        dict={dict}
      />
    </>
  );
}
