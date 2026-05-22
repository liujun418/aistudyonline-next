import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { isValidLocale, getDictionary } from "@/lib/i18n";
import { SITE_URL, SITE_NAME } from "@/lib/constants";
import type { Locale } from "@/lib/i18n";
import BlogListClient from "./BlogListClient";

export async function generateMetadata({
  params,
}: {
  params: Promise<{ locale: string }>;
}): Promise<Metadata> {
  const { locale } = await params;
  if (!isValidLocale(locale)) return {};

  const localeMap: Record<string, string> = { en: "en_US", zh: "zh_CN" };

  return {
    title: `Blog — ${SITE_NAME}`,
    description: "Latest AI news, tutorials, and in-depth analysis from AI Study Online.",
    openGraph: {
      type: "website",
      locale: localeMap[locale] || "en_US",
      url: `${SITE_URL}/${locale}/blog`,
      siteName: SITE_NAME,
      title: `Blog — ${SITE_NAME}`,
      description: "Latest AI news, tutorials, and in-depth analysis from AI Study Online.",
      images: [{ url: `${SITE_URL}/og-default.png`, width: 1200, height: 630, alt: SITE_NAME }],
    },
    twitter: {
      card: "summary_large_image",
      title: `Blog — ${SITE_NAME}`,
      description: "Latest AI news, tutorials, and in-depth analysis from AI Study Online.",
      images: [`${SITE_URL}/og-default.png`],
    },
    alternates: {
      languages: {
        "x-default": `${SITE_URL}/en/blog`,
        en: `${SITE_URL}/en/blog`,
        zh: `${SITE_URL}/zh/blog`,
      },
    },
  };
}

export default async function BlogPage({
  params,
}: {
  params: Promise<{ locale: string }>;
}) {
  const { locale } = await params;
  if (!isValidLocale(locale)) notFound();

  const dict = await getDictionary(locale as Locale);

  return <BlogListClient locale={locale} dict={dict} />;
}
