"use client";

import Link from "next/link";
import { useState, useMemo } from "react";
import { blogPosts } from "@/lib/blog-posts";

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

export default function BlogListClient({
  locale,
}: {
  locale: string;
  dict: Record<string, unknown>;
}) {
  const [activeCategory, setActiveCategory] = useState<string>("all");

  const filteredPosts = useMemo(() => {
    if (activeCategory === "all") return blogPosts;
    return blogPosts.filter((p) => p.category === activeCategory);
  }, [activeCategory]);

  const categories = ["all", "news", "announcement", "guide", "opinion"];

  return (
    <div className="mx-auto max-w-4xl px-4 py-8 sm:px-6">
      {/* Breadcrumb */}
      <nav className="mb-6 text-sm text-zinc-500 dark:text-zinc-400">
        <Link href={`/${locale}`} className="transition-colors hover:text-primary-600">
          {locale === "zh" ? "首页" : "Home"}
        </Link>
        <span className="mx-2">/</span>
        <span className="text-foreground">{locale === "zh" ? "博客" : "Blog"}</span>
      </nav>

      <h1 className="mb-2 text-3xl font-bold text-foreground md:text-4xl">
        {locale === "zh" ? "博客" : "Blog"}
      </h1>
      <p className="mb-8 text-zinc-600 dark:text-zinc-400">
        {locale === "zh"
          ? "最新的AI资讯、教程和深度分析。"
          : "Latest AI news, tutorials, and in-depth analysis."}
      </p>

      {/* Category Filter */}
      <div className="mb-8 overflow-x-auto">
        <div className="flex gap-2 pb-2">
          {categories.map((cat) => (
            <button
              key={cat}
              onClick={() => setActiveCategory(cat)}
              className={`shrink-0 rounded-full px-4 py-2 text-sm font-medium transition ${
                activeCategory === cat
                  ? "bg-primary-500 text-white"
                  : "bg-surface border border-border text-zinc-600 hover:bg-primary-50 dark:text-zinc-400 dark:hover:bg-primary-950"
              }`}
            >
              {cat === "all"
                ? locale === "zh"
                  ? "全部"
                  : "All"
                : locale === "zh"
                  ? categoryLabels[cat].zh
                  : categoryLabels[cat].en}
            </button>
          ))}
        </div>
      </div>

      {/* Posts List */}
      {filteredPosts.length > 0 ? (
        <div className="space-y-6">
          {filteredPosts.map((post) => (
            <BlogPostCard key={post.slug} post={post} locale={locale} />
          ))}
        </div>
      ) : (
        <div className="rounded-xl border border-border bg-surface p-12 text-center">
          <p className="text-zinc-500 dark:text-zinc-400">
            {locale === "zh"
              ? "该分类暂无文章。"
              : "No posts in this category yet."}
          </p>
        </div>
      )}
    </div>
  );
}

function BlogPostCard({ post, locale }: { post: (typeof blogPosts)[number]; locale: string }) {
  const catLabel =
    locale === "zh" ? categoryLabels[post.category].zh : categoryLabels[post.category].en;
  const catColor = categoryColors[post.category] || "bg-primary-100 text-primary-700";

  return (
    <article className="rounded-xl border border-border bg-surface p-6 shadow-sm transition hover:shadow-md">
      <div className="mb-3 flex items-center gap-3">
        <span className={`inline-block rounded-full px-3 py-1 text-xs font-medium ${catColor}`}>
          {catLabel}
        </span>
        <time className="text-xs text-zinc-400 dark:text-zinc-500" dateTime={post.date}>
          {post.date}
        </time>
      </div>

      <h2 className="mb-2 text-xl font-semibold text-foreground">
        <Link
          href={`/${locale}/blog/${post.slug}`}
          className="transition-colors hover:text-primary-600"
        >
          {locale === "zh" ? post.titleZh : post.title}
        </Link>
      </h2>

      <p className="mb-4 leading-relaxed text-zinc-600 dark:text-zinc-400">
        {locale === "zh" ? post.descriptionZh : post.description}
      </p>

      {post.tags.length > 0 && (
        <div className="mb-4 flex flex-wrap gap-1.5">
          {post.tags.map((tag: string) => (
            <span
              key={tag}
              className="rounded-md bg-zinc-100 px-2 py-0.5 text-xs text-zinc-600 dark:bg-zinc-800 dark:text-zinc-400"
            >
              {tag}
            </span>
          ))}
        </div>
      )}

      <Link
        href={`/${locale}/blog/${post.slug}`}
        className="inline-flex items-center gap-1 text-sm font-medium text-primary-600 transition-colors hover:text-primary-700 dark:text-primary-400"
      >
        {locale === "zh" ? "阅读全文" : "Read more"} &rarr;
      </Link>
    </article>
  );
}
