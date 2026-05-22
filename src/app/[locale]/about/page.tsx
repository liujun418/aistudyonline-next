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

  const localeMap: Record<string, string> = { en: "en_US", zh: "zh_CN" };

  return {
    title: `About — ${SITE_NAME}`,
    description: "Learn about AI Study Online — our mission to make AI education accessible to everyone.",
    openGraph: {
      type: "website",
      locale: localeMap[locale] || "en_US",
      url: `${SITE_URL}/${locale}/about`,
      siteName: SITE_NAME,
      title: `About — ${SITE_NAME}`,
      description: "Learn about AI Study Online — our mission to make AI education accessible to everyone.",
      images: [{ url: `${SITE_URL}/og-default.png`, width: 1200, height: 630, alt: SITE_NAME }],
    },
    alternates: {
      languages: {
        "x-default": `${SITE_URL}/en/about`,
        en: `${SITE_URL}/en/about`,
        zh: `${SITE_URL}/zh/about`,
      },
    },
  };
}

export default async function AboutPage({
  params,
}: {
  params: Promise<{ locale: string }>;
}) {
  const { locale } = await params;
  if (!isValidLocale(locale)) notFound();

  const dict = await getDictionary(locale as Locale);
  const siteTitle = ((dict as any)?.site?.title || SITE_NAME) as string;

  return (
    <div className="mx-auto max-w-3xl px-4 py-12 sm:px-6">
      <h1 className="mb-8 text-3xl font-bold text-foreground">About {siteTitle}</h1>

      <section className="mb-10">
        <h2 className="mb-4 text-xl font-semibold text-foreground">Our Mission</h2>
        <p className="leading-relaxed text-zinc-600 dark:text-zinc-400">
          AI Study Online helps absolute beginners learn artificial intelligence.
          We believe AI is for everyone — not just developers and data scientists.
          Our goal is to make AI knowledge accessible, practical, and actually useful
          in your daily life and work.
        </p>
      </section>

      <section className="mb-10">
        <h2 className="mb-4 text-xl font-semibold text-foreground">What We Offer</h2>
        <ul className="space-y-3 text-zinc-600 dark:text-zinc-400">
          <li className="flex items-start gap-2">
            <span className="mt-1 shrink-0 text-primary-500">&bull;</span>
            <span>
              <strong className="text-foreground">AI Tools Directory</strong> &mdash; 100+ AI tools organized by category, with honest ratings and pricing.
            </span>
          </li>
          <li className="flex items-start gap-2">
            <span className="mt-1 shrink-0 text-primary-500">&bull;</span>
            <span>
              <strong className="text-foreground">Step-by-Step Tutorials</strong> &mdash; Practical guides that show you exactly what to do, with real examples.
            </span>
          </li>
          <li className="flex items-start gap-2">
            <span className="mt-1 shrink-0 text-primary-500">&bull;</span>
            <span>
              <strong className="text-foreground">Real-World Use Cases</strong> &mdash; AI for resumes, presentations, writing, and more.
            </span>
          </li>
          <li className="flex items-start gap-2">
            <span className="mt-1 shrink-0 text-primary-500">&bull;</span>
            <span>
              <strong className="text-foreground">Honest Comparisons</strong> &mdash; Side-by-side tool testing with real results.
            </span>
          </li>
          <li className="flex items-start gap-2">
            <span className="mt-1 shrink-0 text-primary-500">&bull;</span>
            <span>
              <strong className="text-foreground">Latest AI News</strong> &mdash; What is new and what it means for you.
            </span>
          </li>
        </ul>
      </section>

      <section className="mb-10">
        <h2 className="mb-4 text-xl font-semibold text-foreground">Why We Built This</h2>
        <p className="leading-relaxed text-zinc-600 dark:text-zinc-400">
          AI is transforming every industry, but most resources are either too technical
          or too superficial. We created AI Study Online to bridge that gap — offering
          content that is thorough enough to be useful, yet simple enough for anyone
          to follow. No jargon, no prerequisites, no gatekeeping.
        </p>
      </section>

      <section>
        <h2 className="mb-4 text-xl font-semibold text-foreground">Contact</h2>
        <p className="text-zinc-600 dark:text-zinc-400">
          Have questions or suggestions? Reach out to us at{" "}
          <a
            href="mailto:jzerov@live.com"
            className="text-primary-600 underline transition-colors hover:text-primary-700 dark:text-primary-400"
          >
            jzerov@live.com
          </a>
          .
        </p>
      </section>
    </div>
  );
}
