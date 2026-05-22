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
      ? `${SITE_NAME}服务条款——使用我们网站的规则与法律约定。`
      : `${SITE_NAME} terms of service — rules and legal agreements for using our website.`;

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
        "x-default": `${SITE_URL}/en/terms`,
        en: `${SITE_URL}/en/terms`,
        zh: `${SITE_URL}/zh/terms`,
      },
    },
  };
}

type Section =
  | { type: "text"; title: string; body: string }
  | { type: "list"; title: string; intro: string; items: string[] }
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

export default async function TermsPage({
  params,
}: {
  params: Promise<{ locale: string }>;
}) {
  const { locale } = await params;
  if (!isValidLocale(locale)) notFound();

  const sections: Section[] =
    locale === "zh" ? zhSections : enSections;
  const title =
    locale === "zh" ? "服务条款" : "Terms of Service";
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
    title: "1. Acceptance of Terms",
    body: `By accessing or using ${SITE_NAME} ("aistudyonline.club"), you agree to be bound by these Terms of Service. If you do not agree with any part of these terms, you must not access or use our website. Your continued use of the website constitutes acceptance of any changes to these terms.`,
  },
  {
    type: "text",
    title: "2. Service Description",
    body: `${SITE_NAME} ("we", "us", "our") is an educational platform that provides AI tool directories, tutorials, articles, learning resources, and related content. The website is operated under the ${SITE_NAME} brand. All content is provided for informational and educational purposes only and does not constitute professional advice.`,
  },
  {
    type: "text",
    title: "3. License & Permitted Use",
    body: `${SITE_NAME} grants you a personal, non-commercial, non-exclusive, revocable license to access and use the website and its content. You may: browse AI tools and resources, read articles and tutorials, follow step-by-step guides, and share links to our content. You may NOT: reproduce, redistribute, sell, sublicense, or commercially exploit any content from our website without our prior written permission.`,
  },
  {
    type: "list",
    title: "4. Prohibited Conduct",
    intro: "You agree NOT to engage in any of the following prohibited activities:",
    items: [
      "Scraping, crawling, or data mining any part of our website without our prior written consent.",
      "Reverse engineering, decompiling, hacking, or attempting to compromise the website's security or functionality.",
      "Using the website for any illegal, fraudulent, or unauthorized purpose.",
      "Posting, uploading, or transmitting any malicious code, viruses, worms, or harmful software.",
      "Impersonating any person or entity, or providing false or misleading information.",
      "Making excessive automated or programmatic requests that could disrupt, overload, or impair the website's infrastructure.",
      "Interfering with other users' access or use of the website.",
    ],
  },
  {
    type: "text",
    title: "5. Intellectual Property",
    body: `All content on this website, including but not limited to articles, code, design, logos, graphics, site architecture, and educational materials, is owned by ${SITE_NAME} or licensed from third parties. This content is protected by copyright, trademark, and other intellectual property laws. Unauthorized reproduction, modification, distribution, or commercial use of any content is strictly prohibited without our prior written consent.`,
  },
  {
    type: "text",
    title: "6. Third-Party Links & Tools",
    body: `Our website contains directory links to external AI tools, services, and resources. These links are provided for your convenience only. We do not control, endorse, or assume responsibility for the content, products, services, privacy practices, or terms of any third-party websites or services. Your use of third-party websites is at your own risk. We encourage you to review the terms of service and privacy policies of any third-party sites you visit.`,
  },
  {
    type: "text",
    title: "7. Disclaimer of Warranties",
    body: `${SITE_NAME} is provided on an "AS IS" and "AS AVAILABLE" basis. We make no warranties, express or implied, regarding the operation, availability, or accuracy of the website. We do not guarantee: uninterrupted access to the website, error-free content, the accuracy or completeness of information, or fitness for a particular purpose. AI tools and services listed on our website may change their pricing, features, or availability at any time without notice.`,
  },
  {
    type: "text",
    title: "8. Limitation of Liability",
    body: `To the maximum extent permitted by applicable law, ${SITE_NAME} and its operators shall not be liable for any indirect, incidental, special, consequential, or punitive damages, including but not limited to loss of data, profits, or business, damages resulting from third-party tools or links, or damages arising from the inability to access or use the website. Our total liability to you shall not exceed the amount paid by you to us, if any.`,
  },
  {
    type: "text",
    title: "9. Indemnification",
    body: `You agree to indemnify, defend, and hold harmless ${SITE_NAME} and its operators, affiliates, and contributors from and against any and all claims, liabilities, damages, losses, costs, and expenses (including reasonable legal fees) arising out of or relating to your use of the website, your violation of these Terms of Service, or your infringement of any third-party rights.`,
  },
  {
    type: "text",
    title: "10. Service Modifications",
    body: "We reserve the right to modify, suspend, or discontinue any aspect of our website, including content, features, or services, at any time without prior notice. We may also update, change, or remove content at our discretion. We shall not be liable to you or any third party for any modification, suspension, or discontinuation of our services.",
  },
  {
    type: "text",
    title: "11. Termination",
    body: "We reserve the right to terminate or suspend your access to the website, without prior notice or liability, for any reason, including but not limited to violation of these Terms of Service. Upon termination, your right to use the website will immediately cease. Provisions of these Terms that by their nature should survive termination shall survive, including intellectual property provisions, disclaimers, and limitations of liability.",
  },
  {
    type: "text",
    title: "12. Governing Law & Dispute Resolution",
    body: `These Terms shall be governed by and construed in accordance with applicable international laws. In the event of any dispute arising out of or relating to these Terms or your use of the website, the parties agree to first attempt to resolve the dispute through good-faith negotiation. If the dispute cannot be resolved through negotiation, it shall be settled by binding arbitration in accordance with international commercial arbitration rules. For users within the European Union, applicable EU consumer protection laws shall apply and may provide additional protections.`,
  },
  {
    type: "text",
    title: "13. Severability",
    body: "If any provision of these Terms of Service is found to be invalid, illegal, or unenforceable by a court of competent jurisdiction, the remaining provisions shall remain in full force and effect. The invalid provision shall be modified to the minimum extent necessary to make it valid and enforceable while preserving its intent to the greatest extent possible.",
  },
  {
    type: "email",
    title: "14. Contact",
    beforeEmail:
      "If you have any questions, concerns, or requests regarding these Terms of Service, please contact us at",
    afterEmail: ".",
  },
];

const zhSections: Section[] = [
  {
    type: "text",
    title: "一、条款接受",
    body: `访问或使用 ${SITE_NAME}（aistudyonline.club）即表示您同意受本服务条款的约束。如果您不同意本条款的任何部分，请勿访问或使用我们的网站。您继续使用本网站即视为接受对本条款的任何变更。`,
  },
  {
    type: "text",
    title: "二、服务说明",
    body: `${SITE_NAME}（"我们"、"我们的"）是一个教育平台，提供 AI 工具目录、教程、文章、学习资源及相关内容。本网站由 ${SITE_NAME} 品牌运营。所有内容仅供信息参考和教育目的使用，不构成专业建议。`,
  },
  {
    type: "text",
    title: "三、许可与允许使用",
    body: `${SITE_NAME} 授予您个人、非商业性、非独占性、可撤销的许可，以访问和使用本网站及其内容。您可以：浏览 AI 工具和资源、阅读文章和教程、按照分步指南操作、分享我们内容的链接。您不得：未经我们事先书面许可，复制、再分发、出售、再许可或商业性利用本网站的任何内容。`,
  },
  {
    type: "list",
    title: "四、禁止行为",
    intro: "您同意不得从事以下任何禁止行为：",
    items: [
      "未经我们事先书面同意，抓取、爬取或挖掘本网站的任何部分。",
      "反向工程、反编译、黑客攻击或试图破坏本网站的安全或功能。",
      "将本网站用于任何非法、欺诈或未经授权的目的。",
      "发布、上传或传输任何恶意代码、病毒、蠕虫或有害软件。",
      "冒充任何个人或实体，或提供虚假或误导性信息。",
      "发送过量自动或程序化请求，可能破坏、超载或损害网站基础设施。",
      "干扰其他用户访问或使用本网站。",
    ],
  },
  {
    type: "text",
    title: "五、知识产权",
    body: `本网站上的所有内容，包括但不限于文章、代码、设计、标志、图形、网站架构和教育材料，均归 ${SITE_NAME} 所有或从第三方获得许可。这些内容受版权、商标和其他知识产权法律保护。未经我们事先书面同意，严禁未经授权复制、修改、分发或商业性使用任何内容。`,
  },
  {
    type: "text",
    title: "六、第三方链接与工具",
    body: `本网站包含指向外部 AI 工具、服务和资源的目录链接。这些链接仅为方便您使用而提供。我们不对任何第三方网站或服务的内容、产品、服务、隐私实践或条款进行控制、认可或承担责任。您使用第三方网站的风险由您自行承担。建议您在访问任何第三方网站时查阅其服务条款和隐私政策。`,
  },
  {
    type: "text",
    title: "七、免责声明",
    body: `${SITE_NAME} 按「现状」和「可用」基础提供。我们不对网站的运营、可用性或准确性作出任何明示或暗示的保证。我们不保证：网站的不间断访问、无错误内容、信息的准确性或完整性、或适用于特定目的。本网站列出的 AI 工具和服务可能随时更改其价格、功能或可用性，恕不另行通知。`,
  },
  {
    type: "text",
    title: "八、责任限制",
    body: `在适用法律允许的最大范围内，${SITE_NAME} 及其运营者不对任何间接、附带、特殊、后果性或惩罚性损害赔偿承担责任，包括但不限于数据丢失、利润或业务损失、因第三方工具或链接造成的损害、或因无法访问或使用本网站而产生的损害。我们对您的总赔偿责任不超过您向我们支付的任何金额（如有）。`,
  },
  {
    type: "text",
    title: "九、赔偿",
    body: `您同意赔偿、辩护并使 ${SITE_NAME} 及其运营者、关联方和贡献者免受任何及所有索赔、责任、损害、损失、成本和费用（包括合理的律师费）的损害，这些索赔因您使用本网站、违反本服务条款或侵犯第三方权利而引起或与之相关。`,
  },
  {
    type: "text",
    title: "十、服务变更",
    body: "我们保留随时修改、暂停或终止我们网站任何方面的权利，包括内容、功能或服务，恕不另行通知。我们也可以自行决定更新、更改或删除内容。我们不对您或任何第三方因任何修改、暂停或终止服务而承担责任。",
  },
  {
    type: "text",
    title: "十一、终止",
    body: "我们保留因任何原因（包括但不限于违反本服务条款）在不事先通知或不承担责任的情况下终止或暂停您访问本网站的权利。终止后，您使用本网站的权利立即终止。根据其性质应在终止后继续有效的条款应继续有效，包括知识产权条款、免责声明和责任限制。",
  },
  {
    type: "text",
    title: "十二、管辖法律与争议解决",
    body: `本条款应受适用国际法律管辖并依其解释。对于因本条款或您使用本网站而产生或相关的任何争议，双方同意首先通过善意协商解决争议。如果争议无法通过协商解决，则应按照国际商业仲裁规则通过具有约束力的仲裁解决。对于欧盟境内的用户，适用的欧盟消费者保护法律应适用并可能提供额外保护。`,
  },
  {
    type: "text",
    title: "十三、可分割性",
    body: "如果本服务条款的任何条款被有管辖权的法院认定为无效、非法或不可执行，其余条款仍应完全有效。该无效条款应被修改为使其有效和可执行所需的最低限度，同时尽可能保留其意图。",
  },
  {
    type: "email",
    title: "十四、联系方式",
    beforeEmail:
      "如果您对本服务条款有任何疑问、疑虑或请求，请通过以下邮箱联系我们：",
    afterEmail: "。",
  },
];
