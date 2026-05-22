import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { isValidLocale } from "@/lib/i18n";
import { SITE_URL, SITE_NAME, CONTACT_EMAIL, GA_ID } from "@/lib/constants";

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
      ? `${SITE_NAME}隐私政策——我们如何收集、使用和保护您的信息。`
      : `${SITE_NAME} privacy policy — how we collect, use, and protect your information.`;

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
        "x-default": `${SITE_URL}/en/privacy`,
        en: `${SITE_URL}/en/privacy`,
        zh: `${SITE_URL}/zh/privacy`,
      },
    },
  };
}

type Section =
  | { type: "text"; title: string; body: string }
  | { type: "list"; title: string; intro: string; items: string[] }
  | {
      type: "link";
      title: string;
      bodyBefore: string;
      linkLabel: string;
      bodyAfter: string;
      href: string;
    }
  | { type: "email"; title: string; beforeEmail: string; afterEmail: string };

function renderSection(section: Section, i: number) {
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
    case "list":
      return (
        <section key={i} className="mb-8">
          <h2 className="mb-3 text-xl font-semibold text-foreground">
            {section.title}
          </h2>
          <p className="leading-relaxed text-zinc-600 dark:text-zinc-400">
            {section.intro}
          </p>
          <ul className="mt-2 list-inside list-disc space-y-1 text-zinc-600 dark:text-zinc-400">
            {section.items.map((item, j) => (
              <li key={j}>{item}</li>
            ))}
          </ul>
        </section>
      );
    case "link":
      return (
        <section key={i} className="mb-8">
          <h2 className="mb-3 text-xl font-semibold text-foreground">
            {section.title}
          </h2>
          <p className="leading-relaxed text-zinc-600 dark:text-zinc-400">
            {section.bodyBefore}{" "}
            <a
              href={section.href}
              target="_blank"
              rel="noopener noreferrer"
              className="text-primary-600 underline transition-colors hover:text-primary-700 dark:text-primary-400"
            >
              {section.linkLabel}
            </a>
            {section.bodyAfter}
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
}

export default async function PrivacyPage({
  params,
}: {
  params: Promise<{ locale: string }>;
}) {
  const { locale } = await params;
  if (!isValidLocale(locale)) notFound();

  const sections: Section[] =
    locale === "zh" ? zhSections : enSections;
  const title =
    locale === "zh" ? "隐私政策" : "Privacy Policy";
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
      {sections.map((section, i) => renderSection(section, i))}
    </div>
  );
}

const enSections: Section[] = [
  {
    type: "text",
    title: "1. Information We Collect",
    body: `${SITE_NAME} uses Google Analytics 4 (GA4) to collect anonymous usage data, including pages visited, time spent on site, country-level location, device type, and browser information. We store a locale preference cookie to remember your language selection. We do NOT collect names, email addresses, IP addresses (IP is anonymized in GA4), or any other personally identifiable information. We do not require user registration, accounts, or email sign-ups to access our content or use our tools.`,
  },
  {
    type: "list",
    title: "2. Cookies & Tracking Technologies",
    intro:
      "Our website uses the following types of cookies and tracking technologies:",
    items: [
      "Essential Cookies: A locale preference cookie that stores your language selection (en/zh). This cookie is strictly necessary for the proper functioning of the website.",
      "Google Analytics Cookies (GA4): Used to collect anonymized traffic data and analyze how visitors interact with our site. These cookies collect information in aggregated form that does not directly identify individuals.",
      "Google AdSense Cookies: Google AdSense uses cookies, including the DART cookie, to serve personalized advertisements based on your visits to our site and other websites across the internet.",
      'Opt-Out Options: You may opt out of personalized advertising by visiting Google Ads Settings (https://adssettings.google.com) or by visiting www.aboutads.info to opt out of third-party personalized advertising.',
    ],
  },
  {
    type: "text",
    title: "3. How We Use Information",
    body: "We use the information collected to: improve site content and user experience, analyze traffic patterns and usage trends, and serve relevant advertisements via Google AdSense. Data is processed client-side where possible. We do not sell, trade, or transfer your information to third parties, except as necessary to operate our analytics (Google Analytics) and advertising (Google AdSense) services.",
  },
  {
    type: "link",
    title: "4. Google AdSense & DART Cookie",
    bodyBefore:
      "We use Google AdSense to display advertisements on our website. Google, as a third-party vendor, uses cookies (including the DART cookie) to serve ads based on your visits to our site and other sites across the internet. You may opt out of the use of the DART cookie by visiting",
    linkLabel: "Google Ads Settings",
    bodyAfter:
      ". Alternatively, you can opt out of third-party personalized advertising by visiting www.aboutads.info. Google's use of advertising cookies enables it and its partners to serve ads based on your visit to our site and other sites on the Internet.",
    href: "https://adssettings.google.com",
  },
  {
    type: "text",
    title: "5. Google Analytics (GA4)",
    body: `We use Google Analytics 4 (measurement ID: ${GA_ID}) to understand how visitors engage with our site. GA4 collects anonymized data including: page views, session duration, bounce rate, geographic data at country level only, device category, and browser information. IP addresses are anonymized. No personally identifiable information is collected. Data retention for Google Analytics is set to 14 months. You can learn more about Google's data practices by reviewing the Google Privacy Policy.`,
  },
  {
    type: "text",
    title: "6. GDPR Compliance (EU Users)",
    body: `If you are located in the European Economic Area (EEA), you have the following rights under the General Data Protection Regulation (GDPR): right to access your data, right to rectification, right to erasure ("right to be forgotten"), right to restrict processing, right to data portability, and right to object to processing. To exercise any of these rights, please contact us at ${CONTACT_EMAIL}. Our legal basis for processing your data: legitimate interest for analytics and site improvement; consent for advertising cookies. Please note that since we collect minimal data and no personal information, many of these rights may not apply to the limited data we process. We will respond to your request within the timeframes required by applicable law.`,
  },
  {
    type: "text",
    title: "7. CCPA Compliance (California Users)",
    body: `If you are a California resident, the California Consumer Privacy Act (CCPA) grants you the following rights: right to know what personal information is collected, used, shared, or sold; right to request deletion of personal information held by us; and right to opt out of the sale of personal information. We do NOT sell your personal information. For more information or to exercise your California privacy rights, please contact us at ${CONTACT_EMAIL}.`,
  },
  {
    type: "text",
    title: "8. Third-Party Links Disclaimer",
    body: `Our website contains links to external AI tools, services, and resources for your convenience and reference. We are NOT responsible for the privacy practices, content, products, or services of any third-party websites. The inclusion of any link does not imply endorsement by ${SITE_NAME}. We encourage you to review the privacy policies of any third-party sites you visit before providing any personal information.`,
  },
  {
    type: "text",
    title: "9. Data Security",
    body: "All data transmitted between your browser and our website is encrypted using HTTPS (SSL/TLS). We do not operate user accounts, store passwords, or maintain databases containing personal information. Analytics data is stored and secured by Google. We implement reasonable security measures to protect the limited data we process. However, please be aware that no method of transmission over the Internet or method of electronic storage is 100% secure.",
  },
  {
    type: "text",
    title: "10. Children's Privacy",
    body: `Our website is not directed at children under the age of 13 (in compliance with the Children's Online Privacy Protection Act — COPPA) or under the age of 16 (in compliance with GDPR age requirements). We do not knowingly collect any personal information from children. If you believe a child has provided us with personal data, please contact us immediately at ${CONTACT_EMAIL}, and we will take prompt steps to delete such information.`,
  },
  {
    type: "text",
    title: "11. Changes to This Policy",
    body: "We may update this Privacy Policy from time to time to reflect changes in our practices or legal requirements. When we make material changes, we will update the 'Last Updated' date at the top of this page and notify users via a site banner. We encourage you to review this Privacy Policy periodically to stay informed about how we are protecting your information.",
  },
  {
    type: "email",
    title: "12. Contact",
    beforeEmail:
      "If you have any questions, concerns, or requests regarding this Privacy Policy or our data practices, please contact us at",
    afterEmail: ".",
  },
];

const zhSections: Section[] = [
  {
    type: "text",
    title: "一、我们收集的信息",
    body: `${SITE_NAME} 使用 Google Analytics 4（GA4）收集匿名使用数据，包括访问的页面、在网站停留时间、国家级别地理位置、设备类型和浏览器信息。我们存储一个语言偏好 Cookie 以记住您的语言选择。我们不会收集姓名、电子邮件地址、IP 地址（IP 已在 GA4 中匿名化）或任何其他个人身份信息。您无需注册、创建账户或订阅邮件即可访问我们的内容或使用我们的工具。`,
  },
  {
    type: "list",
    title: "二、Cookie 与跟踪技术",
    intro: "本网站使用以下类型的 Cookie 和跟踪技术：",
    items: [
      "必要 Cookie：用于存储您的语言偏好（中文/英文）的 Cookie。该 Cookie 对于网站的正常运行是绝对必要的。",
      "Google Analytics Cookie（GA4）：用于收集匿名流量数据并分析访客与网站的互动方式。这些 Cookie 以聚合形式收集信息，不会直接识别个人身份。",
      "Google AdSense Cookie：Google AdSense 使用 Cookie（包括 DART Cookie）根据您访问本网站及其他网站的历史投放个性化广告。",
      "退出选项：您可以通过访问 Google 广告设置（https://adssettings.google.com）选择退出个性化广告，或访问 www.aboutads.info 选择退出第三方个性化广告。",
    ],
  },
  {
    type: "text",
    title: "三、我们如何使用信息",
    body: "我们使用收集到的信息来：改进网站内容和用户体验，分析流量模式和使用趋势，以及通过 Google AdSense 投放相关广告。数据尽可能在客户端处理。我们不会向第三方出售、交易或转让您的信息，除非是运营我们的分析（Google Analytics）和广告（Google AdSense）服务所必需。",
  },
  {
    type: "link",
    title: "四、Google AdSense 与 DART Cookie",
    bodyBefore:
      "我们使用 Google AdSense 在本网站展示广告。作为第三方供应商，Google 使用 Cookie（包括 DART Cookie）根据您访问本网站及其他网站的历史投放广告。您可以通过访问",
    linkLabel: "Google 广告设置",
    bodyAfter:
      "选择退出 DART Cookie 的使用。或者，您也可以通过访问 www.aboutads.info 选择退出第三方个性化广告。Google 使用广告 Cookie 使其及其合作伙伴能够根据您访问本网站及其他网站的历史投放广告。",
    href: "https://adssettings.google.com",
  },
  {
    type: "text",
    title: "五、Google Analytics（GA4）",
    body: `我们使用 Google Analytics 4（衡量 ID：${GA_ID}）了解访客如何使用我们的网站。GA4 收集的匿名数据包括：页面浏览量、会话时长、跳出率、仅限国家级别的地理位置数据、设备类别和浏览器信息。IP 地址已匿名化处理。不会收集任何个人身份信息。Google Analytics 的数据保留期设置为 14 个月。您可以通过查阅 Google 隐私政策了解更多关于 Google 数据实践的信息。`,
  },
  {
    type: "text",
    title: "六、GDPR 合规（欧盟用户）",
    body: `如果您位于欧洲经济区（EEA），您根据《通用数据保护条例》（GDPR）享有以下权利：知情权（访问您的数据）、更正权、删除权（被遗忘权）、限制处理权、数据可携带权以及拒绝处理权。如需行使任何这些权利，请通过 ${CONTACT_EMAIL} 与我们联系。我们处理您数据的法律依据：分析和网站改进基于合法利益；广告 Cookie 基于您的同意。请注意，由于我们收集的数据极少且不涉及个人信息，这些权利中的许多可能不适用于我们所处理的有限数据。我们将在适用法律要求的时限内回应您的请求。`,
  },
  {
    type: "text",
    title: "七、CCPA 合规（加州用户）",
    body: `如果您是加利福尼亚州居民，《加州消费者隐私法案》（CCPA）赋予您以下权利：了解我们收集、使用、共享或出售哪些个人信息；请求删除我们所持有的个人信息；以及选择退出个人信息的出售。我们不会出售您的个人信息。如需了解更多信息或行使您的加州隐私权，请通过 ${CONTACT_EMAIL} 与我们联系。`,
  },
  {
    type: "text",
    title: "八、第三方链接免责声明",
    body: `本网站包含指向外部 AI 工具、服务和资源的链接，仅为方便您参考而提供。我们不对任何第三方网站的隐私实践、内容、产品或服务负责。任何链接的包含并不构成 ${SITE_NAME} 的认可。在提供任何个人信息之前，建议您查阅所访问的第三方网站的隐私政策。`,
  },
  {
    type: "text",
    title: "九、数据安全",
    body: "您的浏览器与本网站之间传输的所有数据均通过 HTTPS（SSL/TLS）加密。我们不运营用户账户、不存储密码、也不维护包含个人信息的数据库。分析数据由 Google 存储和保护。我们采取合理的安全措施来保护我们所处理的有限数据。但请注意，互联网传输或电子存储的方法并非 100% 安全。",
  },
  {
    type: "text",
    title: "十、儿童隐私保护",
    body: `本网站不面向 13 岁以下儿童（符合《儿童在线隐私保护法》COPPA）或 16 岁以下未成年人（符合 GDPR 年龄要求）。我们不会故意收集任何儿童的个人信息。如果您认为儿童向我们提供了个人数据，请立即通过 ${CONTACT_EMAIL} 与我们联系，我们将迅速采取措施删除此类信息。`,
  },
  {
    type: "text",
    title: "十一、本政策的变更",
    body: "我们可能会不时更新本隐私政策，以反映我们的实践变更或法律要求。当进行重大变更时，我们将更新本页面顶部的「最后更新」日期，并通过网站横幅通知用户。建议您定期查阅本隐私政策，以了解我们如何保护您的信息。",
  },
  {
    type: "email",
    title: "十二、联系方式",
    beforeEmail:
      "如果您对本隐私政策或我们的数据实践有任何疑问、疑虑或请求，请通过以下邮箱联系我们：",
    afterEmail: "。",
  },
];
