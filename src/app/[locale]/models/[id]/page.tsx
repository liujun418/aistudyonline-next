import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { isValidLocale, getDictionary } from "@/lib/i18n";
import { SITE_URL, SITE_NAME } from "@/lib/constants";
import { models } from "@/lib/models";
import type { Locale } from "@/lib/i18n";
import ModelDetailClient from "./ModelDetailClient";

export async function generateStaticParams() {
  const locales = ["en", "zh"] as const;
  const paths: { locale: string; id: string }[] = [];
  for (const locale of locales) {
    for (const model of models) {
      paths.push({ locale, id: model.id });
    }
  }
  return paths;
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ locale: string; id: string }>;
}): Promise<Metadata> {
  const { locale, id } = await params;
  if (!isValidLocale(locale)) return {};

  const model = models.find((m) => m.id === id);
  if (!model) return {};

  const dict = await getDictionary(locale as Locale);
  const modelDetail = (dict as any)?.modelDetail || {};
  const localeMap: Record<string, string> = { en: "en_US", zh: "zh_CN" };

  const name = locale === "zh" ? model.nameZh : model.name;
  const description = locale === "zh" ? model.descriptionZh : model.description;
  const title = `${name} — ${modelDetail.models || "AI Models"} — ${SITE_NAME}`;

  return {
    title,
    description,
    openGraph: {
      type: "website",
      locale: localeMap[locale] || "en_US",
      url: `${SITE_URL}/${locale}/models/${id}`,
      siteName: SITE_NAME,
      title,
      description,
      images: [{ url: `${SITE_URL}/og-default.png`, width: 1200, height: 630, alt: name }],
    },
    twitter: {
      card: "summary_large_image",
      title,
      description,
    },
    alternates: {
      languages: {
        "x-default": `${SITE_URL}/en/models/${id}`,
        en: `${SITE_URL}/en/models/${id}`,
        zh: `${SITE_URL}/zh/models/${id}`,
      },
    },
  };
}

export default async function ModelDetailPage({
  params,
}: {
  params: Promise<{ locale: string; id: string }>;
}) {
  const { locale, id } = await params;
  if (!isValidLocale(locale)) notFound();

  const model = models.find((m) => m.id === id);
  if (!model) notFound();

  const dict = await getDictionary(locale as Locale);

  const jsonLd = {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    name: locale === "zh" ? model.nameZh : model.name,
    description: locale === "zh" ? model.descriptionZh : model.description,
    applicationCategory: "AI Application",
    operatingSystem: "Web",
    offers: {
      "@type": "Offer",
      price: model.pricing,
      priceCurrency: "USD",
    },
    author: {
      "@type": "Organization",
      name: model.developer,
    },
    datePublished: model.releaseDate,
  };

  return (
    <>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
      />
      <ModelDetailClient model={model} locale={locale as Locale} dict={dict} />
    </>
  );
}
