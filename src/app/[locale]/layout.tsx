import type { Metadata } from "next";
import Script from "next/script";
import { Suspense } from "react";
import { notFound } from "next/navigation";
import "@/app/globals.css";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import GoogleAnalytics from "@/components/GoogleAnalytics";
import CookieConsent from "@/components/CookieConsent";
import { locales, isValidLocale, localeDir, getDictionary } from "@/lib/i18n";
import { SITE_URL, SITE_NAME } from "@/lib/constants";
import type { Locale } from "@/lib/i18n";


export async function generateStaticParams() {
  return locales.map((locale) => ({ locale }));
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ locale: string }>;
}): Promise<Metadata> {
  const { locale } = await params;
  if (!isValidLocale(locale)) return {};

  const dict = await getDictionary(locale);
  const site = (dict as any)?.site || {};

  const localeMap: Record<string, string> = { en: "en_US", zh: "zh_CN" };
  const OG_IMAGE = `${SITE_URL}/og-default.png`;

  return {
    title: `${SITE_NAME} — ${site.tagline || "Learn AI. Actually Use It."}`,
    description: site.subtitle || "Learn AI from zero. Discover the best AI tools and learn how to use them.",
    openGraph: {
      type: "website",
      locale: localeMap[locale] || "en_US",
      url: `${SITE_URL}/${locale}`,
      siteName: SITE_NAME,
      title: `${SITE_NAME} — ${site.tagline || "Learn AI. Actually Use It."}`,
      description: site.subtitle || "Learn AI from zero.",
      images: [{ url: OG_IMAGE, width: 1200, height: 630, alt: SITE_NAME }],
    },
    twitter: {
      card: "summary_large_image",
      title: `${SITE_NAME} — ${site.tagline || "Learn AI. Actually Use It."}`,
      description: site.subtitle || "Learn AI from zero.",
      images: [OG_IMAGE],
    },
    alternates: {
      languages: {
        "x-default": `${SITE_URL}/en`,
        en: `${SITE_URL}/en`,
        zh: `${SITE_URL}/zh`,
      },
    },
    other: {
      "google-adsense-account": "ca-pub-9954245854077897",
    },
  };
}

export default async function LocaleLayout({
  params,
  children,
}: {
  params: Promise<{ locale: string }>;
  children: React.ReactNode;
}) {
  const { locale } = await params;
  if (!isValidLocale(locale)) notFound();

  const dict = await getDictionary(locale as Locale);
  const dir = localeDir[locale as Locale];
  const fontClass = "";

  return (
    <html
      lang={locale}
      dir={dir}
      className={`${fontClass} h-full antialiased`}
    >
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" crossOrigin="anonymous" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
        <link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&display=swap" rel="stylesheet" />
        <link rel="icon" type="image/x-icon" href="/favicon.ico" />
        <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png" />
        <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png" />
        <link rel="apple-touch-icon" sizes="512x512" href="/favicon-512.png" />
        <link rel="preconnect" href="https://pagead2.googlesyndication.com" crossOrigin="anonymous" />
        <link rel="preconnect" href="https://googleads.g.doubleclick.net" crossOrigin="anonymous" />
        <Script
          async
          src="https://www.googletagmanager.com/gtag/js?id=G-MXS4P3XP87"
          strategy="afterInteractive"
        />
        <Script
          id="ga4-init"
          strategy="afterInteractive"
          dangerouslySetInnerHTML={{
            __html: `
              window.dataLayer = window.dataLayer || [];
              function gtag(){dataLayer.push(arguments);}
              gtag('js', new Date());
              gtag('config', 'G-MXS4P3XP87');
            `,
          }}
        />
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{
            __html: JSON.stringify({
              "@context": "https://schema.org",
              "@type": "WebSite",
              name: "AI Study Online",
              url: "https://aistudyonline.club",
              description:
                "Learn AI from zero. Discover the best AI tools and learn how to use them.",
              inLanguage: ["en", "zh"],
              potentialAction: {
                "@type": "SearchAction",
                target: {
                  "@type": "EntryPoint",
                  urlTemplate:
                    "https://aistudyonline.club/en?q={search_term_string}",
                },
                "query-input": "required name=search_term_string",
              },
              publisher: {
                "@type": "Organization",
                name: "AI Study Online",
                url: "https://aistudyonline.club",
                logo: {
                  "@type": "ImageObject",
                  url: "https://aistudyonline.club/favicon-512.png",
                  width: 512,
                  height: 512,
                },
              },
            }),
          }}
        />
      </head>
      <body className="flex min-h-dvh flex-col overflow-x-hidden bg-white text-zinc-900 dark:bg-zinc-950 dark:text-zinc-100">
        <Script
          async
          src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9954245854077897"
          crossOrigin="anonymous"
          strategy="afterInteractive"
        />
        <Header locale={locale} dict={dict} />
        <main className="flex-1">{children}</main>
        <Footer locale={locale} dict={dict} />
        <Suspense fallback={null}>
          <GoogleAnalytics />
        </Suspense>
        <CookieConsent />
      </body>
    </html>
  );
}
