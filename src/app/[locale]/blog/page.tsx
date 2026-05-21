import Link from "next/link";
import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { isValidLocale, getDictionary } from "@/lib/i18n";
import { SITE_URL, SITE_NAME } from "@/lib/constants";
import type { Locale } from "@/lib/i18n";

export async function generateMetadata({
  params,
}: {
  params: Promise<{ locale: string }>;
}): Promise<Metadata> {
  const { locale } = await params;
  if (!isValidLocale(locale)) return {};

  const localeMap: Record<string, string> = { en: "en_US", es: "es_ES", ar: "ar_SA" };

  return {
    title: `Blog — ${SITE_NAME}`,
    description: "Latest updates, tips, and insights from AI Study Online.",
    openGraph: {
      type: "website",
      locale: localeMap[locale] || "en_US",
      url: `${SITE_URL}/${locale}/blog`,
      siteName: SITE_NAME,
      title: `Blog — ${SITE_NAME}`,
      description: "Latest updates, tips, and insights from AI Study Online.",
      images: [{ url: `${SITE_URL}/og-default.png`, width: 1200, height: 630, alt: SITE_NAME }],
    },
    twitter: {
      card: "summary_large_image",
      title: `Blog — ${SITE_NAME}`,
      description: "Latest updates, tips, and insights from AI Study Online.",
      images: [`${SITE_URL}/og-default.png`],
    },
    alternates: {
      languages: {
        "x-default": `${SITE_URL}/en/blog`,
        en: `${SITE_URL}/en/blog`,
        es: `${SITE_URL}/es/blog`,
        ar: `${SITE_URL}/ar/blog`,
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
  const blogNav = ((dict as any)?.nav?.blog || "Blog") as string;

  return (
    <div className="mx-auto max-w-4xl px-4 py-8 sm:px-6">
      <h1 className="mb-8 text-3xl font-bold text-foreground">{blogNav}</h1>

      {/* Welcome blog post rendered as ArticleCard style */}
      <article className="rounded-xl border border-border bg-surface p-6 shadow-sm transition hover:shadow-md">
        <div className="mb-3">
          <span className="inline-block rounded-full bg-primary-100 px-3 py-1 text-xs font-medium text-primary-700 dark:bg-primary-900/40 dark:text-primary-300">
            Announcement
          </span>
        </div>

        <h2 className="mb-2 text-xl font-semibold text-foreground">
          <Link
            href={`/${locale}/blog/welcome-to-ai-study-online`}
            className="transition-colors hover:text-primary-600"
          >
            Welcome to AI Study Online
          </Link>
        </h2>

        <p className="mb-3 leading-relaxed text-zinc-600 dark:text-zinc-400">
          We are excited to launch AI Study Online — your friendly guide to
          understanding and using artificial intelligence. Whether you are
          completely new to AI or looking to expand your skills, we have
          something for you.
        </p>

        <div className="mb-4 flex items-center gap-3 text-xs text-zinc-400 dark:text-zinc-500">
          <time dateTime="2026-05-21">2026-05-21</time>
          <span aria-hidden="true">&middot;</span>
          <span>3 min read</span>
        </div>

        <Link
          href={`/${locale}/blog/welcome-to-ai-study-online`}
          className="inline-flex items-center gap-1 text-sm font-medium text-primary-600 transition-colors hover:text-primary-700 dark:text-primary-400"
        >
          Read more &rarr;
        </Link>
      </article>
    </div>
  );
}
