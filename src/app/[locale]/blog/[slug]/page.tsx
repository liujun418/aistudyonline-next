import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { isValidLocale, getDictionary } from "@/lib/i18n";
import { SITE_URL, SITE_NAME } from "@/lib/constants";
import type { Locale } from "@/lib/i18n";
import { blogPosts } from "@/lib/blog-posts";
import BlogDetailClient from "./BlogDetailClient";

export async function generateStaticParams() {
  const params: { locale: string; slug: string }[] = [];
  for (const locale of ["en", "zh"]) {
    for (const post of blogPosts) {
      params.push({ locale, slug: post.slug });
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

  const post = blogPosts.find((p) => p.slug === slug);
  if (!post) return {};

  const localeMap: Record<string, string> = { en: "en_US", zh: "zh_CN" };
  const title = locale === "zh" ? post.titleZh : post.title;
  const description = locale === "zh" ? post.descriptionZh : post.description;

  return {
    title: `${title} — ${SITE_NAME}`,
    description,
    openGraph: {
      type: "article",
      locale: localeMap[locale] || "en_US",
      url: `${SITE_URL}/${locale}/blog/${slug}`,
      siteName: SITE_NAME,
      title: `${title} — ${SITE_NAME}`,
      description,
      images: [{ url: `${SITE_URL}/og-default.png`, width: 1200, height: 630, alt: SITE_NAME }],
      publishedTime: post.date,
    },
    twitter: {
      card: "summary_large_image",
      title: `${title} — ${SITE_NAME}`,
      description,
      images: [`${SITE_URL}/og-default.png`],
    },
    alternates: {
      languages: {
        "x-default": `${SITE_URL}/en/blog/${slug}`,
        en: `${SITE_URL}/en/blog/${slug}`,
        zh: `${SITE_URL}/zh/blog/${slug}`,
      },
    },
  };
}

export default async function BlogArticlePage({
  params,
}: {
  params: Promise<{ locale: string; slug: string }>;
}) {
  const { locale, slug } = await params;
  if (!isValidLocale(locale)) notFound();

  const post = blogPosts.find((p) => p.slug === slug);
  if (!post) notFound();

  const dict = await getDictionary(locale as Locale);

  return <BlogDetailClient post={post} locale={locale} />;
}
