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
      ? `服务条款 — ${SITE_NAME}`
      : `Terms of Service — ${SITE_NAME}`;
  const description =
    locale === "zh"
      ? `${SITE_NAME}服务条款——使用我们网站的规则与指南。`
      : `${SITE_NAME} terms of service — rules and guidelines for using our website.`;

  return {
    title,
    description,
    openGraph: {
      type: "website",
      locale: localeMap[locale] || "en_US",
      url: `${SITE_URL}/${locale}/terms`,
      siteName: SITE_NAME,
      title,
      description,
      images: [{ url: `${SITE_URL}/og-default.png`, width: 1200, height: 630, alt: SITE_NAME }],
    },
    alternates: {
      languages: {
        "x-default": `${SITE_URL}/en/terms`,
        en: `${SITE_URL}/en/terms`,
        zh: `${SITE_URL}/zh/terms`,
      },
    },
  };
}

export default async function TermsPage({
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
          {content.educationalPurpose.title}
        </h2>
        <p className="leading-relaxed text-zinc-600 dark:text-zinc-400">
          {content.educationalPurpose.body}
        </p>
      </section>

      <section className="mb-8">
        <h2 className="mb-3 text-xl font-semibold text-foreground">
          {content.externalLinks.title}
        </h2>
        <p className="leading-relaxed text-zinc-600 dark:text-zinc-400">
          {content.externalLinks.body}
        </p>
      </section>

      <section className="mb-8">
        <h2 className="mb-3 text-xl font-semibold text-foreground">
          {content.aiContent.title}
        </h2>
        <p className="leading-relaxed text-zinc-600 dark:text-zinc-400">
          {content.aiContent.body}
        </p>
      </section>

      <section className="mb-8">
        <h2 className="mb-3 text-xl font-semibold text-foreground">
          {content.intellectualProperty.title}
        </h2>
        <p className="leading-relaxed text-zinc-600 dark:text-zinc-400">
          {content.intellectualProperty.body}
        </p>
      </section>

      <section className="mb-8">
        <h2 className="mb-3 text-xl font-semibold text-foreground">
          {content.limitation.title}
        </h2>
        <p className="leading-relaxed text-zinc-600 dark:text-zinc-400">
          {content.limitation.body}
        </p>
      </section>

      <section className="mb-8">
        <h2 className="mb-3 text-xl font-semibold text-foreground">
          {content.changes.title}
        </h2>
        <p className="leading-relaxed text-zinc-600 dark:text-zinc-400">
          {content.changes.body}
        </p>
      </section>

      <section>
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
  title: "Terms of Service",
  lastUpdated: "Last updated: May 21, 2026",
  educationalPurpose: {
    title: "Educational Purpose",
    body: `${SITE_NAME} is an educational website that provides information about artificial intelligence tools and techniques. All content is provided for informational and educational purposes only. We make no guarantees about the accuracy, completeness, or suitability of the information provided.`,
  },
  externalLinks: {
    title: "External Links Disclaimer",
    body: "Our website contains links to third-party websites and services. These links are provided for your convenience and do not constitute endorsement or responsibility for the content, products, or services of those third-party sites. We are not liable for any damages or losses related to your use of external websites.",
  },
  aiContent: {
    title: "AI-Generated Content Notice",
    body: "Some content on this website may be generated or assisted by artificial intelligence. While we strive for accuracy and quality, AI-generated content may contain errors, omissions, or inaccuracies. We recommend verifying important information from primary sources.",
  },
  intellectualProperty: {
    title: "Intellectual Property",
    body: `All content on this website, including text, graphics, logos, and tools, is the property of ${SITE_NAME} unless otherwise stated. You may not reproduce, distribute, or modify any content without our prior written permission.`,
  },
  limitation: {
    title: "Limitation of Liability",
    body: `${SITE_NAME} and its operators shall not be liable for any direct, indirect, incidental, consequential, or punitive damages arising from your use of, or inability to use, our website or the information provided therein.`,
  },
  changes: {
    title: "Changes to Terms",
    body: "We reserve the right to update or modify these terms at any time without prior notice. Your continued use of the website after any changes constitutes acceptance of the new terms.",
  },
  contact: {
    title: "Contact",
    beforeEmail:
      "If you have any questions about these terms, please contact us at",
    afterEmail: ".",
  },
};

const zhContent = {
  title: "服务条款",
  lastUpdated: "最后更新：2026年5月21日",
  educationalPurpose: {
    title: "教育目的",
    body: `${SITE_NAME} 是一个提供人工智能工具和技术相关信息的教育网站。所有内容仅供信息参考和教育目的使用。我们不对所提供信息的准确性、完整性或适用性作出任何保证。`,
  },
  externalLinks: {
    title: "外部链接免责声明",
    body: "我们的网站包含指向第三方网站和服务的链接。这些链接仅为方便您使用而提供，并不构成我们对这些第三方网站的内容、产品或服务的认可或承担责任。因使用外部网站而产生的任何损害或损失，我们概不负责。",
  },
  aiContent: {
    title: "AI生成内容声明",
    body: "本网站的部分内容可能由人工智能生成或辅助生成。尽管我们力求准确和高质量，但AI生成的内容可能包含错误、遗漏或不准确之处。建议您通过原始来源核实重要信息。",
  },
  intellectualProperty: {
    title: "知识产权",
    body: `本网站上的所有内容，包括文字、图形、标志和工具，除非另有说明，均为 ${SITE_NAME} 的财产。未经我们事先书面许可，您不得复制、分发或修改任何内容。`,
  },
  limitation: {
    title: "责任限制",
    body: `${SITE_NAME} 及其运营者不对因您使用或无法使用本网站及其提供的信息而导致的任何直接、间接、偶然、后果性或惩罚性损害赔偿承担责任。`,
  },
  changes: {
    title: "条款变更",
    body: "我们保留随时更新或修改这些条款的权利，恕不另行通知。您在条款变更后继续使用本网站即表示接受新的条款。",
  },
  contact: {
    title: "联系我们",
    beforeEmail: "如果您对这些条款有任何疑问，请通过以下邮箱联系我们：",
    afterEmail: "。",
  },
};
