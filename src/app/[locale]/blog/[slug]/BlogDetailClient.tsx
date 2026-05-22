"use client";

import Link from "next/link";
import { blogPosts, type BlogPost } from "@/lib/blog-posts";
import { tools } from "@/lib/tools";
import { SITE_URL, SITE_NAME } from "@/lib/constants";

const categoryLabels: Record<string, { en: string; zh: string }> = {
  news: { en: "News", zh: "新闻" },
  announcement: { en: "Announcement", zh: "公告" },
  guide: { en: "Guide", zh: "指南" },
  opinion: { en: "Opinion", zh: "观点" },
};

const categoryColors: Record<string, string> = {
  news: "bg-blue-100 text-blue-700 dark:bg-blue-900/40 dark:text-blue-300",
  announcement: "bg-primary-100 text-primary-700 dark:bg-primary-900/40 dark:text-primary-300",
  guide: "bg-green-100 text-green-700 dark:bg-green-900/40 dark:text-green-300",
  opinion: "bg-purple-100 text-purple-700 dark:bg-purple-900/40 dark:text-purple-300",
};

export default function BlogDetailClient({
  post,
  locale,
}: {
  post: BlogPost;
  locale: string;
}) {
  const catLabel =
    locale === "zh" ? categoryLabels[post.category].zh : categoryLabels[post.category].en;
  const catColor = categoryColors[post.category] || "bg-primary-100 text-primary-700";
  const rawContent = locale === "zh" ? post.contentZh : post.content;
  const content = rawContent.replace(
    /href="\/(article|learn|tools|models|blog)\//g,
    `href="/${locale}/$1/`,
  );

  // Related tools
  const relatedTools = tools.filter((t) => post.toolsMentioned.includes(t.id));

  // Related posts
  const relatedPosts = blogPosts
    .filter((p) => p.slug !== post.slug)
    .slice(0, 3);

  // Estimate reading time
  const wordCount = content.replace(/<[^>]*>/g, "").split(/\s+/).length;
  const readingTime = Math.max(1, Math.round(wordCount / 200));

  // JSON-LD schema
  const jsonLd = {
    "@context": "https://schema.org",
    "@type": "BlogPosting",
    headline: locale === "zh" ? post.titleZh : post.title,
    description: locale === "zh" ? post.descriptionZh : post.description,
    datePublished: post.date,
    author: {
      "@type": "Person",
      name: post.authorName,
    },
    publisher: {
      "@type": "Organization",
      name: SITE_NAME,
    },
    mainEntityOfPage: {
      "@type": "WebPage",
      "@id": `${SITE_URL}/${locale}/blog/${post.slug}`,
    },
  };

  return (
    <div className="mx-auto max-w-3xl px-4 py-8 sm:px-6">
      {/* JSON-LD Schema */}
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
      />

      {/* Breadcrumb */}
      <nav className="mb-6 text-sm text-zinc-500 dark:text-zinc-400">
        <Link
          href={`/${locale}`}
          className="transition-colors hover:text-primary-600"
        >
          {locale === "zh" ? "首页" : "Home"}
        </Link>
        <span className="mx-2">/</span>
        <Link
          href={`/${locale}/blog`}
          className="transition-colors hover:text-primary-600"
        >
          {locale === "zh" ? "博客" : "Blog"}
        </Link>
        <span className="mx-2">/</span>
        <span className="text-foreground">
          {locale === "zh" ? post.titleZh : post.title}
        </span>
      </nav>

      {/* Blog Header */}
      <article>
        <div className="mb-3 flex items-center gap-3">
          <span className={`inline-block rounded-full px-3 py-1 text-xs font-medium ${catColor}`}>
            {catLabel}
          </span>
          <time className="text-sm text-zinc-400 dark:text-zinc-500" dateTime={post.date}>
            {post.date}
          </time>
        </div>

        <h1 className="mb-3 text-3xl font-bold text-foreground md:text-4xl">
          {locale === "zh" ? post.titleZh : post.title}
        </h1>

        <div className="mb-6 flex items-center gap-3 text-sm text-zinc-500 dark:text-zinc-400">
          <span>
            {locale === "zh" ? "作者：" : "By "}
            {post.authorName}
          </span>
          <span aria-hidden="true">&middot;</span>
          <span>
            {readingTime} {locale === "zh" ? "分钟阅读" : "min read"}
          </span>
        </div>

        {post.tags.length > 0 && (
          <div className="mb-8 flex flex-wrap gap-1.5">
            {post.tags.map((tag) => (
              <span
                key={tag}
                className="rounded-md bg-zinc-100 px-2 py-0.5 text-xs text-zinc-600 dark:bg-zinc-800 dark:text-zinc-400"
              >
                {tag}
              </span>
            ))}
          </div>
        )}

        {/* Article Content */}
        <div
          className="prose prose-zinc max-w-none dark:prose-invert prose-headings:font-bold prose-headings:text-foreground prose-p:text-zinc-600 dark:prose-p:text-zinc-400 prose-a:text-primary-600 prose-a:underline hover:prose-a:text-primary-700 dark:prose-a:text-primary-400 prose-pre:bg-zinc-900 prose-pre:text-zinc-100 prose-code:text-primary-600 [&_h2]:mt-10 [&_h2]:mb-4 [&_h3]:mt-6 [&_h3]:mb-3"
          dangerouslySetInnerHTML={{ __html: content }}
        />
      </article>

      {/* Related Tools */}
      {relatedTools.length > 0 && (
        <section className="mt-10 border-t border-border pt-8">
          <h2 className="mb-4 text-xl font-bold text-foreground">
            {locale === "zh" ? "相关工具" : "Related Tools"}
          </h2>
          <div className="flex flex-wrap gap-2">
            {relatedTools.map((tool) => (
              <Link
                key={tool.id}
                href={`/${locale}/tools/${tool.id}`}
                className="inline-flex items-center gap-2 rounded-lg border border-border bg-surface px-4 py-2 text-sm font-medium text-foreground transition hover:border-primary-300 hover:shadow-sm"
              >
                <span>{tool.icon}</span>
                {tool.name}
              </Link>
            ))}
          </div>
        </section>
      )}

      {/* Related Posts */}
      {relatedPosts.length > 0 && (
        <section className="mt-10 border-t border-border pt-8">
          <h2 className="mb-4 text-xl font-bold text-foreground">
            {locale === "zh" ? "相关文章" : "Related Posts"}
          </h2>
          <div className="grid gap-4 sm:grid-cols-2">
            {relatedPosts.map((rp) => (
              <Link
                key={rp.slug}
                href={`/${locale}/blog/${rp.slug}`}
                className="rounded-xl border border-border bg-surface p-4 shadow-sm transition hover:shadow-md hover:border-primary-300"
              >
                <h3 className="text-sm font-semibold text-foreground">
                  {locale === "zh" ? rp.titleZh : rp.title}
                </h3>
                <p className="mt-1 text-xs text-zinc-500 dark:text-zinc-400 line-clamp-2">
                  {locale === "zh" ? rp.descriptionZh : rp.description}
                </p>
              </Link>
            ))}
          </div>
        </section>
      )}

      {/* Back link */}
      <div className="mt-10 border-t border-border pt-6">
        <Link
          href={`/${locale}/blog`}
          className="text-sm font-medium text-primary-600 transition-colors hover:text-primary-700 dark:text-primary-400"
        >
          &larr; {locale === "zh" ? "返回博客" : "Back to Blog"}
        </Link>
      </div>
    </div>
  );
}
