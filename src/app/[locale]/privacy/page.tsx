import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { isValidLocale } from "@/lib/i18n";
import { SITE_URL, SITE_NAME, CONTACT_EMAIL } from "@/lib/constants";

export async function generateMetadata({
  params,
}: {
  params: Promise<{ locale: string }>;
}): Promise<Metadata> {
  const { locale } = await params;
  if (!isValidLocale(locale)) return {};

  const localeMap: Record<string, string> = { en: "en_US", zh: "zh_CN" };
  const title =
    locale === "zh"
      ? `隐私政策 — ${SITE_NAME}`
      : `Privacy Policy — ${SITE_NAME}`;
  const description =
    locale === "zh"
      ? `${SITE_NAME}隐私政策——我们如何处理您的数据。`
      : `${SITE_NAME} privacy policy — how we handle your data.`;

  return {
    title,
    description,
    openGraph: {
      type: "website",
      locale: localeMap[locale] || "en_US",
      url: `${SITE_URL}/${locale}/privacy`,
      siteName: SITE_NAME,
      title,
      description,
      images: [{ url: `${SITE_URL}/og-default.png`, width: 1200, height: 630, alt: SITE_NAME }],
    },
    alternates: {
      languages: {
        "x-default": `${SITE_URL}/en/privacy`,
        en: `${SITE_URL}/en/privacy`,
        zh: `${SITE_URL}/zh/privacy`,
      },
    },
  };
}

export default async function PrivacyPage({
  params,
}: {
  params: Promise<{ locale: string }>;
}) {
  const { locale } = await params;
  if (!isValidLocale(locale)) notFound();

  const content = locale === "zh" ? zhContent : enContent;

  return (
    <div className="mx-auto max-w-3xl px-4 py-12 sm:px-6">
      <h1 className="mb-8 text-3xl font-bold text-foreground">
        {content.title}
      </h1>
      <p className="mb-8 text-sm text-zinc-500 dark:text-zinc-400">
        {content.lastUpdated}
      </p>

      <section className="mb-8">
        <h2 className="mb-3 text-xl font-semibold text-foreground">
          {content.infoCollection.title}
        </h2>
        <p className="leading-relaxed text-zinc-600 dark:text-zinc-400">
          {content.infoCollection.body}
        </p>
      </section>

      <section className="mb-8">
        <h2 className="mb-3 text-xl font-semibold text-foreground">
          {content.adsense.title}
        </h2>
        <p className="leading-relaxed text-zinc-600 dark:text-zinc-400">
          {content.adsense.bodyBefore}{" "}
          <a
            href="https://www.google.com/settings/ads"
            target="_blank"
            rel="noopener noreferrer"
            className="text-primary-600 underline transition-colors hover:text-primary-700 dark:text-primary-400"
          >
            {content.adsense.linkLabel}
          </a>
          {content.adsense.bodyAfter}
        </p>
      </section>

      <section className="mb-8">
        <h2 className="mb-3 text-xl font-semibold text-foreground">
          {content.analytics.title}
        </h2>
        <p className="leading-relaxed text-zinc-600 dark:text-zinc-400">
          {content.analytics.body}
        </p>
      </section>

      <section className="mb-8">
        <h2 className="mb-3 text-xl font-semibold text-foreground">
          {content.cookies.title}
        </h2>
        <p className="leading-relaxed text-zinc-600 dark:text-zinc-400">
          {content.cookies.intro}
        </p>
        <ul className="mt-2 list-inside list-disc space-y-1 text-zinc-600 dark:text-zinc-400">
          {content.cookies.items.map((item, i) => (
            <li key={i}>{item}</li>
          ))}
        </ul>
      </section>

      <section className="mb-8">
        <h2 className="mb-3 text-xl font-semibold text-foreground">
          {content.thirdParty.title}
        </h2>
        <p className="leading-relaxed text-zinc-600 dark:text-zinc-400">
          {content.thirdParty.body}
        </p>
      </section>

      <section className="mb-8">
        <h2 className="mb-3 text-xl font-semibold text-foreground">
          {content.contact.title}
        </h2>
        <p className="leading-relaxed text-zinc-600 dark:text-zinc-400">
          {content.contact.beforeEmail}{" "}
          <a
            href={`mailto:${CONTACT_EMAIL}`}
            className="text-primary-600 underline transition-colors hover:text-primary-700 dark:text-primary-400"
          >
            {CONTACT_EMAIL}
          </a>
          {content.contact.afterEmail}
        </p>
      </section>
    </div>
  );
}

const enContent = {
  title: "Privacy Policy",
  lastUpdated: "Last updated: May 21, 2026",
  infoCollection: {
    title: "Information We Collect",
    body: "AI Study Online does not collect personal information from its visitors. We do not require registration, accounts, or email sign-ups to use our tools or read our content.",
  },
  adsense: {
    title: "Google AdSense",
    bodyBefore:
      "We use Google AdSense to display advertisements on our website. Google AdSense uses cookies to serve ads based on your previous visits to our website or other websites. You can opt out of personalized advertising by visiting",
    linkLabel: "Google Ads Settings",
    bodyAfter: ".",
  },
  analytics: {
    title: "Google Analytics",
    body: "We use Google Analytics to understand how visitors interact with our website. This data is anonymized and helps us improve our content and user experience. Google Analytics collects information such as page views, referral sources, and browser types.",
  },
  cookies: {
    title: "Cookies",
    intro: "Our website uses cookies for the following purposes:",
    items: [
      "Google AdSense advertising cookies",
      "Google Analytics performance cookies",
      "Language preference cookie (locale)",
      "Theme preference cookie (dark/light mode)",
    ],
  },
  thirdParty: {
    title: "Third-Party Links",
    body: "Our website contains links to third-party websites. We are not responsible for the privacy practices of these websites. We encourage you to review their privacy policies before providing any personal information.",
  },
  contact: {
    title: "Contact",
    beforeEmail:
      "If you have any questions about this privacy policy, please contact us at",
    afterEmail: ".",
  },
};

const zhContent = {
  title: "隐私政策",
  lastUpdated: "最后更新：2026年5月21日",
  infoCollection: {
    title: "我们收集的信息",
    body: "AI Study Online 不会收集访客的个人信息。您无需注册、创建账户或订阅邮件即可使用我们的工具或阅读我们的内容。",
  },
  adsense: {
    title: "Google AdSense",
    bodyBefore:
      "我们使用 Google AdSense 在本网站展示广告。Google AdSense 会根据您之前访问本网站或其他网站的历史，使用 Cookie 投放个性化广告。您可以通过访问",
    linkLabel: "Google 广告设置",
    bodyAfter: "来选择退出个性化广告。",
  },
  analytics: {
    title: "Google Analytics",
    body: "我们使用 Google Analytics 来了解访客如何与我们的网站互动。这些数据经过匿名化处理，帮助我们改进内容和用户体验。Google Analytics 会收集页面浏览、来源渠道和浏览器类型等信息。",
  },
  cookies: {
    title: "Cookie",
    intro: "本网站使用以下类型的 Cookie：",
    items: [
      "Google AdSense 广告 Cookie",
      "Google Analytics 性能 Cookie",
      "语言偏好 Cookie（locale）",
      "主题偏好 Cookie（深色/浅色模式）",
    ],
  },
  thirdParty: {
    title: "第三方链接",
    body: "我们的网站包含指向第三方网站的链接。我们不对这些网站的隐私实践负责。在提供任何个人信息之前，建议您查阅其隐私政策。",
  },
  contact: {
    title: "联系我们",
    beforeEmail: "如果您对本隐私政策有任何疑问，请通过以下邮箱联系我们：",
    afterEmail: "。",
  },
};
