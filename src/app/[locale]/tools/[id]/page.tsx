import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { isValidLocale, getDictionary } from "@/lib/i18n";
import { SITE_URL, SITE_NAME } from "@/lib/constants";
import { tools } from "@/lib/tools";
import type { Locale } from "@/lib/i18n";
import ToolDetailClient from "./ToolDetailClient";

export async function generateStaticParams() {
  const locales = ["en", "es", "ar"] as const;
  const paths: { locale: string; id: string }[] = [];
  for (const locale of locales) {
    for (const tool of tools) {
      paths.push({ locale, id: tool.id });
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

  const tool = tools.find((t) => t.id === id);
  if (!tool) return {};

  const dict = await getDictionary(locale as Locale);
  const toolDetail = (dict as any)?.toolDetail || {};
  const localeMap: Record<string, string> = { en: "en_US", es: "es_ES", ar: "ar_SA" };

  const name = tool.name;
  const description =
    locale === "es"
      ? tool.descriptionEs
      : locale === "ar"
        ? tool.descriptionAr
        : tool.description;
  const title = `${name} — ${toolDetail.aiTools || "AI Tools"} — ${SITE_NAME}`;

  return {
    title,
    description,
    openGraph: {
      type: "website",
      locale: localeMap[locale] || "en_US",
      url: `${SITE_URL}/${locale}/tools/${id}`,
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
        "x-default": `${SITE_URL}/en/tools/${id}`,
        en: `${SITE_URL}/en/tools/${id}`,
        es: `${SITE_URL}/es/tools/${id}`,
        ar: `${SITE_URL}/ar/tools/${id}`,
      },
    },
  };
}

export default async function ToolDetailPage({
  params,
}: {
  params: Promise<{ locale: string; id: string }>;
}) {
  const { locale, id } = await params;
  if (!isValidLocale(locale)) notFound();

  const tool = tools.find((t) => t.id === id);
  if (!tool) notFound();

  const dict = await getDictionary(locale as Locale);

  const jsonLd = {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    name: tool.name,
    description:
      locale === "es"
        ? tool.descriptionEs
        : locale === "ar"
          ? tool.descriptionAr
          : tool.description,
    applicationCategory: "AIApplication",
    operatingSystem: "Web",
    offers: {
      "@type": "Offer",
      price: tool.pricing,
      priceCurrency: "USD",
    },
    author: {
      "@type": "Organization",
      name: tool.company,
    },
  };

  return (
    <>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
      />
      <ToolDetailClient tool={tool} locale={locale as Locale} dict={dict} />
    </>
  );
}
