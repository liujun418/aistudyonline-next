import type { Metadata } from "next";
import { SITE_URL, SITE_NAME, CONTACT_EMAIL } from "@/lib/constants";
import { isValidLocale } from "@/lib/i18n";

export async function generateMetadata({
  params,
}: {
  params: Promise<{ locale: string }>;
}): Promise<Metadata> {
  const { locale } = await params;
  const isZh = locale === "zh";

  return {
    title: isZh ? `联系我们 — ${SITE_NAME}` : `Contact Us — ${SITE_NAME}`,
    description: isZh
      ? "联系AI Study Online团队，获取AI学习资源和工具目录的帮助。"
      : "Get in touch with the AI Study Online team for help with AI learning resources and tools directory.",
    openGraph: {
      title: isZh ? `联系我们 — ${SITE_NAME}` : `Contact Us — ${SITE_NAME}`,
      description: isZh
        ? "联系AI Study Online团队。"
        : "Contact the AI Study Online team.",
      url: `${SITE_URL}/${locale}/contact`,
      siteName: SITE_NAME,
    },
    alternates: {
      languages: {
        "x-default": `${SITE_URL}/en/contact`,
        en: `${SITE_URL}/en/contact`,
        zh: `${SITE_URL}/zh/contact`,
      },
    },
  };
}

export default async function ContactPage({
  params,
}: {
  params: Promise<{ locale: string }>;
}) {
  const { locale } = await params;
  if (!isValidLocale(locale)) return null;
  const isZh = locale === "zh";

  return (
    <div className="mx-auto max-w-3xl px-4 py-12 sm:px-6">
      <h1 className="mb-8 text-3xl font-bold text-foreground">
        {isZh ? "联系我们" : "Contact Us"}
      </h1>

      <div className="space-y-8">
        {/* Email */}
        <section>
          <h2 className="mb-3 text-xl font-semibold text-foreground">
            {isZh ? "电子邮件" : "Email"}
          </h2>
          <p className="text-zinc-600 dark:text-zinc-400">
            {isZh
              ? "有任何问题、建议或合作意向？请发送邮件至："
              : "Have questions, suggestions, or business inquiries? Reach us at:"}
          </p>
          <a
            href={`mailto:${CONTACT_EMAIL}`}
            className="mt-2 inline-block text-lg font-medium text-primary-600 hover:text-primary-700 dark:text-primary-400"
          >
            {CONTACT_EMAIL}
          </a>
        </section>

        {/* What to contact us about */}
        <section>
          <h2 className="mb-3 text-xl font-semibold text-foreground">
            {isZh ? "您可以联系我们关于" : "What You Can Contact Us About"}
          </h2>
          <ul className="list-disc space-y-2 pl-5 text-zinc-600 dark:text-zinc-400">
            <li>
              {isZh
                ? "AI工具收录建议 — 推荐新的AI工具加入我们的目录"
                : "AI Tool Suggestions — Recommend new AI tools for our directory"}
            </li>
            <li>
              {isZh
                ? "内容反馈 — 文章勘误、翻译建议、内容改进"
                : "Content Feedback — Article corrections, translation suggestions, content improvements"}
            </li>
            <li>
              {isZh
                ? "广告合作 — AdSense及赞助合作咨询"
                : "Advertising — AdSense and sponsorship inquiries"}
            </li>
            <li>
              {isZh
                ? "技术问题 — 网站Bug报告、功能建议"
                : "Technical Issues — Bug reports and feature requests"}
            </li>
            <li>
              {isZh ? "其他咨询" : "General Inquiries"}
            </li>
          </ul>
        </section>

        {/* Response Time */}
        <section>
          <h2 className="mb-3 text-xl font-semibold text-foreground">
            {isZh ? "回复时间" : "Response Time"}
          </h2>
          <p className="text-zinc-600 dark:text-zinc-400">
            {isZh
              ? "我们通常在1-2个工作日内回复邮件。感谢您的耐心等待。"
              : "We typically respond within 1-2 business days. Thank you for your patience."}
          </p>
        </section>
      </div>
    </div>
  );
}
