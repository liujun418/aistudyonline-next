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
      ? `退款政策 — ${SITE_NAME}`
      : `Refund Policy — ${SITE_NAME}`;
  const description =
    locale === "zh"
      ? `${SITE_NAME}退款政策——当前所有服务完全免费，以及未来付费服务的退款说明。`
      : `${SITE_NAME} refund policy — currently all services are free, with information about future paid services.`;

  return {
    title,
    description,
    openGraph: {
      type: "website",
      locale: localeMap[locale] || "en_US",
      url: `${SITE_URL}/${locale}/refund`,
      siteName: SITE_NAME,
      title,
      description,
      images: [
        {
          url: `${SITE_URL}/og-default.png`,
          width: 1200,
          height: 630,
          alt: SITE_NAME,
        },
      ],
    },
    alternates: {
      languages: {
        "x-default": `${SITE_URL}/en/refund`,
        en: `${SITE_URL}/en/refund`,
        zh: `${SITE_URL}/zh/refund`,
      },
    },
  };
}

type Section =
  | { type: "text"; title: string; body: string }
  | { type: "email"; title: string; beforeEmail: string; afterEmail: string };

export default async function RefundPage({
  params,
}: {
  params: Promise<{ locale: string }>;
}) {
  const { locale } = await params;
  if (!isValidLocale(locale)) notFound();

  const sections: Section[] =
    locale === "zh" ? zhSections : enSections;
  const title =
    locale === "zh" ? "退款政策" : "Refund Policy";
  const lastUpdated =
    locale === "zh"
      ? "最后更新：2026年5月22日"
      : "Last updated: May 22, 2026";

  return (
    <div className="mx-auto max-w-3xl px-4 py-12 sm:px-6">
      <h1 className="mb-8 text-3xl font-bold text-foreground">{title}</h1>
      <p className="mb-8 text-sm text-zinc-500 dark:text-zinc-400">
        {lastUpdated}
      </p>
      {sections.map((section, i) => {
        switch (section.type) {
          case "text":
            return (
              <section key={i} className="mb-8">
                <h2 className="mb-3 text-xl font-semibold text-foreground">
                  {section.title}
                </h2>
                <p className="leading-relaxed text-zinc-600 dark:text-zinc-400">
                  {section.body}
                </p>
              </section>
            );
          case "email":
            return (
              <section key={i} className="mb-8">
                <h2 className="mb-3 text-xl font-semibold text-foreground">
                  {section.title}
                </h2>
                <p className="leading-relaxed text-zinc-600 dark:text-zinc-400">
                  {section.beforeEmail}{" "}
                  <a
                    href={`mailto:${CONTACT_EMAIL}`}
                    className="text-primary-600 underline transition-colors hover:text-primary-700 dark:text-primary-400"
                  >
                    {CONTACT_EMAIL}
                  </a>
                  {section.afterEmail}
                </p>
              </section>
            );
        }
      })}
    </div>
  );
}

const enSections: Section[] = [
  {
    type: "text",
    title: "1. Free Service",
    body: `${SITE_NAME} currently provides ALL content, AI tool directories, tutorials, articles, and learning resources completely FREE of charge. There are no paid products, subscriptions, or services requiring payment at this time. You can access and use all features of our website without any financial obligation.`,
  },
  {
    type: "text",
    title: "2. Future Paid Services",
    body: "Should we introduce paid services in the future (such as premium tutorials, courses, advanced tools, or membership plans), a detailed refund policy specific to those services will be developed and posted on this page prior to launch. That policy will include: refund eligibility conditions, the refund request procedure, expected processing timelines, and applicable contact information. Any paid service will be clearly marked as such, and no charges will be incurred without your explicit consent.",
  },
  {
    type: "text",
    title: "3. Donations",
    body: `${SITE_NAME} does not currently accept monetary donations. If a donation or voluntary contribution feature is introduced in the future, a separate refund and cancellation policy will be established for such transactions.`,
  },
  {
    type: "text",
    title: "4. Third-Party Tools",
    body: "Our website provides directory listings and links to external AI tools, services, and platforms. These third-party services may have their own pricing, subscription fees, and refund policies. We are NOT responsible for purchases, subscriptions, or transactions made on third-party platforms. If you have purchased a product or service from a third-party provider listed on our site, please contact that provider directly for any refund inquiries, as their terms and conditions apply to such transactions.",
  },
  {
    type: "email",
    title: "5. Contact",
    beforeEmail:
      "If you have any questions about this Refund Policy, please contact us at",
    afterEmail: ".",
  },
];

const zhSections: Section[] = [
  {
    type: "text",
    title: "一、免费服务",
    body: `${SITE_NAME} 目前完全免费提供所有内容、AI 工具目录、教程、文章和学习资源。现阶段没有任何需要付费的产品、订阅或服务。您可以无需承担任何财务义务即可访问和使用我们网站的所有功能。`,
  },
  {
    type: "text",
    title: "二、未来付费服务",
    body: "如果将来我们推出付费服务（如高级教程、课程、进阶工具或会员计划），将在上线前制定并在本页面发布相应的详细退款政策。该政策将包括：退款资格条件、退款申请流程、预期处理时限以及适用的联系信息。任何付费服务都将明确标注，未经您的明确同意不会产生任何费用。",
  },
  {
    type: "text",
    title: "三、捐赠",
    body: `${SITE_NAME} 目前不接受任何形式的货币捐赠。如果将来推出捐赠或自愿资助功能，将为此类交易制定单独的退款和取消政策。`,
  },
  {
    type: "text",
    title: "四、第三方工具",
    body: "本网站提供外部 AI 工具、服务和平台的目录链接。这些第三方服务可能有自己的定价、订阅费用和退款政策。我们不对在第三方平台上的购买、订阅或交易负责。如果您通过我们网站列出的第三方提供商购买了产品或服务，请直接联系该提供商处理退款事宜，因为此类交易适用其自身的条款和条件。",
  },
  {
    type: "email",
    title: "五、联系方式",
    beforeEmail:
      "如果您对本退款政策有任何疑问，请通过以下邮箱联系我们：",
    afterEmail: "。",
  },
];
