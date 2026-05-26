import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { isValidLocale, getDictionary } from "@/lib/i18n";
import { SITE_URL, SITE_NAME } from "@/lib/constants";
import ModelListClient from "./ModelListClient";
import type { Locale } from "@/lib/i18n";

export async function generateMetadata({
  params,
}: {
  params: Promise<{ locale: string }>;
}): Promise<Metadata> {
  const { locale } = await params;
  if (!isValidLocale(locale)) return {};

  const dict = await getDictionary(locale as Locale);
  const models = (dict as any)?.models || {};

  const localeMap: Record<string, string> = { en: "en_US", zh: "zh_CN" };

  return {
    title: `${models.title || "AI Models Directory"} — ${SITE_NAME}`,
    description: models.description || "Explore cutting-edge AI models from top developers worldwide.",
    openGraph: {
      type: "website",
      locale: localeMap[locale] || "en_US",
      url: `${SITE_URL}/${locale}/models`,
      siteName: SITE_NAME,
      title: `${models.title || "AI Models Directory"} — ${SITE_NAME}`,
      description: models.description || "Explore cutting-edge AI models from top developers worldwide.",
      images: [{ url: `${SITE_URL}/og-default.png`, width: 1200, height: 630, alt: SITE_NAME }],
    },
    twitter: {
      card: "summary_large_image",
      title: `${models.title || "AI Models Directory"} — ${SITE_NAME}`,
      description: models.description || "Explore cutting-edge AI models from top developers worldwide.",
    },
    alternates: {
      languages: {
        "x-default": `${SITE_URL}/en/models`,
        en: `${SITE_URL}/en/models`,
        zh: `${SITE_URL}/zh/models`,
      },
    },
  };
}

export default async function ModelsPage({
  params,
}: {
  params: Promise<{ locale: string }>;
}) {
  const { locale } = await params;
  if (!isValidLocale(locale)) notFound();

  const dict = await getDictionary(locale as Locale);

  return <ModelListClient locale={locale} dict={dict} />;
}
