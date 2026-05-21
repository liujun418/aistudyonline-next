import Link from "next/link";
import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { isValidLocale, getDictionary } from "@/lib/i18n";
import { SITE_URL, SITE_NAME } from "@/lib/constants";
import type { Locale } from "@/lib/i18n";

// For now, only the welcome post exists
const blogPosts = [
  {
    slug: "welcome-to-ai-study-online",
    title: "Welcome to AI Study Online",
    date: "2026-05-21",
    category: "Announcement",
    content: `
      <h2>Hello and Welcome!</h2>
      <p>We are thrilled to announce the launch of <strong>AI Study Online</strong> — a brand new resource designed to help absolute beginners learn about artificial intelligence.</p>
      <p>AI is changing the world, but most learning resources are either too technical for beginners or too shallow to be useful. We built AI Study Online to bridge that gap.</p>

      <h2>What You Will Find Here</h2>
      <ul>
        <li><strong>AI Tools Directory</strong> — Browse 100+ AI tools organized by category, with honest ratings, pricing, and use cases.</li>
        <li><strong>Step-by-Step Tutorials</strong> — Practical guides that show you exactly how to use AI tools, from ChatGPT to Midjourney and beyond.</li>
        <li><strong>Comparisons</strong> — Side-by-side testing of popular AI tools so you can choose the right one for your needs.</li>
        <li><strong>Use Cases</strong> — Real-world applications of AI for resumes, presentations, writing, and more.</li>
      </ul>

      <h2>Where to Start</h2>
      <p>If you are brand new to AI, head over to our <a href="/{locale}/learn/ai-basics">AI Basics</a> section to learn the fundamentals. For hands-on tutorials, check out our <a href="/{locale}/learn/ai-tutorials">AI Tutorials</a> page.</p>
      <p>Ready to explore tools? Visit the <a href="/{locale}/tools">AI Tools Directory</a> to discover what is available.</p>

      <h2>What Is Next</h2>
      <p>We will be adding new articles, tutorials, and tools regularly. Follow along as we grow. Have suggestions? We would love to hear from you at <a href="mailto:jzerov@live.com">jzerov@live.com</a>.</p>
      <p>Thank you for joining us on this journey!</p>
    `,
  },
];

export async function generateStaticParams() {
  const params: { locale: string; slug: string }[] = [];
  for (const locale of ["en", "es", "ar"]) {
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

  const localeMap: Record<string, string> = { en: "en_US", es: "es_ES", ar: "ar_SA" };

  return {
    title: `${post.title} — ${SITE_NAME}`,
    description: "Welcome to AI Study Online — your friendly guide to understanding and using artificial intelligence.",
    openGraph: {
      type: "article",
      locale: localeMap[locale] || "en_US",
      url: `${SITE_URL}/${locale}/blog/${slug}`,
      siteName: SITE_NAME,
      title: `${post.title} — ${SITE_NAME}`,
      description: "Welcome to AI Study Online — your friendly guide to understanding and using artificial intelligence.",
      images: [{ url: `${SITE_URL}/og-default.png`, width: 1200, height: 630, alt: SITE_NAME }],
      publishedTime: post.date,
    },
    twitter: {
      card: "summary_large_image",
      title: `${post.title} — ${SITE_NAME}`,
      description: "Welcome to AI Study Online — your friendly guide to understanding and using artificial intelligence.",
      images: [`${SITE_URL}/og-default.png`],
    },
    alternates: {
      languages: {
        "x-default": `${SITE_URL}/en/blog/${slug}`,
        en: `${SITE_URL}/en/blog/${slug}`,
        es: `${SITE_URL}/es/blog/${slug}`,
        ar: `${SITE_URL}/ar/blog/${slug}`,
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
  const blogNav = ((dict as any)?.nav?.blog || "Blog") as string;

  // Fix placeholder in content
  const content = post.content.replace(/\{locale\}/g, locale);

  return (
    <div className="mx-auto max-w-3xl px-4 py-8 sm:px-6">
      {/* Breadcrumb */}
      <nav className="mb-6 text-sm text-zinc-500 dark:text-zinc-400">
        <Link
          href={`/${locale}`}
          className="transition-colors hover:text-primary-600"
        >
          Home
        </Link>
        <span className="mx-2">/</span>
        <Link
          href={`/${locale}/blog`}
          className="transition-colors hover:text-primary-600"
        >
          {blogNav}
        </Link>
        <span className="mx-2">/</span>
        <span className="text-zinc-800 dark:text-zinc-200">{post.title}</span>
      </nav>

      {/* Blog header */}
      <article>
        <div className="mb-3">
          <span className="inline-block rounded-full bg-primary-100 px-3 py-1 text-xs font-medium text-primary-700 dark:bg-primary-900/40 dark:text-primary-300">
            {post.category}
          </span>
        </div>

        <h1 className="mb-3 text-3xl font-bold text-foreground">{post.title}</h1>

        <div className="mb-8 flex items-center gap-3 text-sm text-zinc-500 dark:text-zinc-400">
          <time dateTime={post.date}>{post.date}</time>
          <span aria-hidden="true">&middot;</span>
          <span>3 min read</span>
        </div>

        {/* Content */}
        <div
          className="prose prose-zinc max-w-none dark:prose-invert [&_a]:text-primary-600 [&_a]:underline [&_a:hover]:text-primary-700 dark:[&_a]:text-primary-400"
          dangerouslySetInnerHTML={{ __html: content }}
        />
      </article>

      {/* Back link */}
      <div className="mt-10 border-t border-border pt-6">
        <Link
          href={`/${locale}/blog`}
          className="text-sm font-medium text-primary-600 transition-colors hover:text-primary-700 dark:text-primary-400"
        >
          &larr; Back to Blog
        </Link>
      </div>
    </div>
  );
}
