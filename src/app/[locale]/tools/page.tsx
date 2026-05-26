import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { isValidLocale, getDictionary } from "@/lib/i18n";
import { SITE_URL, SITE_NAME } from "@/lib/constants";
import ToolsClient from "./ToolsClient";
import type { Locale } from "@/lib/i18n";

export async function generateMetadata({
  params,
}: {
  params: Promise<{ locale: string }>;
}): Promise<Metadata> {
  const { locale } = await params;
  if (!isValidLocale(locale)) return {};

  const dict = await getDictionary(locale as Locale);
  const tools = (dict as any)?.tools || {};

  const localeMap: Record<string, string> = { en: "en_US", zh: "zh_CN" };

  return {
    title: `${tools.title || "AI Tools Directory"} — ${SITE_NAME}`,
    description: tools.description || "Browse AI tools organized by category.",
    openGraph: {
      type: "website",
      locale: localeMap[locale] || "en_US",
      url: `${SITE_URL}/${locale}/tools`,
      siteName: SITE_NAME,
      title: `${tools.title || "AI Tools Directory"} — ${SITE_NAME}`,
      description: tools.description || "Browse AI tools organized by category.",
      images: [{ url: `${SITE_URL}/og-default.png`, width: 1200, height: 630, alt: SITE_NAME }],
    },
    twitter: {
      card: "summary_large_image",
      title: `${tools.title || "AI Tools Directory"} — ${SITE_NAME}`,
      description: tools.description || "Browse AI tools organized by category.",
    },
    alternates: {
      languages: {
        "x-default": `${SITE_URL}/en/tools`,
        en: `${SITE_URL}/en/tools`,
        zh: `${SITE_URL}/zh/tools`,
      },
    },
  };
}

export default async function ToolsPage({
  params,
}: {
  params: Promise<{ locale: string }>;
}) {
  const { locale } = await params;
  if (!isValidLocale(locale)) notFound();

  const dict = await getDictionary(locale as Locale);

  return <ToolsClient locale={locale} dict={dict} />;
}
