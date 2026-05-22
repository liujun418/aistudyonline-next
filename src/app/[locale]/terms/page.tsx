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

  return {
    title: `Terms of Service — ${SITE_NAME}`,
    description: `${SITE_NAME} terms of service — rules and guidelines for using our website.`,
    openGraph: {
      type: "website",
      locale: localeMap[locale] || "en_US",
      url: `${SITE_URL}/${locale}/terms`,
      siteName: SITE_NAME,
      title: `Terms of Service — ${SITE_NAME}`,
      description: `${SITE_NAME} terms of service — rules and guidelines for using our website.`,
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

  return (
    <div className="mx-auto max-w-3xl px-4 py-12 sm:px-6">
      <h1 className="mb-8 text-3xl font-bold text-foreground">Terms of Service</h1>
      <p className="mb-8 text-sm text-zinc-500 dark:text-zinc-400">
        Last updated: May 21, 2026
      </p>

      <section className="mb-8">
        <h2 className="mb-3 text-xl font-semibold text-foreground">Educational Purpose</h2>
        <p className="leading-relaxed text-zinc-600 dark:text-zinc-400">
          {SITE_NAME} is an educational website that provides information about
          artificial intelligence tools and techniques. All content is provided
          for informational and educational purposes only. We make no guarantees
          about the accuracy, completeness, or suitability of the information
          provided.
        </p>
      </section>

      <section className="mb-8">
        <h2 className="mb-3 text-xl font-semibold text-foreground">External Links Disclaimer</h2>
        <p className="leading-relaxed text-zinc-600 dark:text-zinc-400">
          Our website contains links to third-party websites and services. These
          links are provided for your convenience and do not constitute endorsement
          or responsibility for the content, products, or services of those
          third-party sites. We are not liable for any damages or losses related
          to your use of external websites.
        </p>
      </section>

      <section className="mb-8">
        <h2 className="mb-3 text-xl font-semibold text-foreground">AI-Generated Content Notice</h2>
        <p className="leading-relaxed text-zinc-600 dark:text-zinc-400">
          Some content on this website may be generated or assisted by artificial
          intelligence. While we strive for accuracy and quality, AI-generated
          content may contain errors, omissions, or inaccuracies. We recommend
          verifying important information from primary sources.
        </p>
      </section>

      <section className="mb-8">
        <h2 className="mb-3 text-xl font-semibold text-foreground">Intellectual Property</h2>
        <p className="leading-relaxed text-zinc-600 dark:text-zinc-400">
          All content on this website, including text, graphics, logos, and
          tools, is the property of {SITE_NAME} unless otherwise stated. You may
          not reproduce, distribute, or modify any content without our prior
          written permission.
        </p>
      </section>

      <section className="mb-8">
        <h2 className="mb-3 text-xl font-semibold text-foreground">Limitation of Liability</h2>
        <p className="leading-relaxed text-zinc-600 dark:text-zinc-400">
          {SITE_NAME} and its operators shall not be liable for any direct,
          indirect, incidental, consequential, or punitive damages arising from
          your use of, or inability to use, our website or the information
          provided therein.
        </p>
      </section>

      <section className="mb-8">
        <h2 className="mb-3 text-xl font-semibold text-foreground">Changes to Terms</h2>
        <p className="leading-relaxed text-zinc-600 dark:text-zinc-400">
          We reserve the right to update or modify these terms at any time
          without prior notice. Your continued use of the website after any
          changes constitutes acceptance of the new terms.
        </p>
      </section>

      <section>
        <h2 className="mb-3 text-xl font-semibold text-foreground">Contact</h2>
        <p className="leading-relaxed text-zinc-600 dark:text-zinc-400">
          If you have any questions about these terms, please contact us at{" "}
          <a
            href={`mailto:${CONTACT_EMAIL}`}
            className="text-primary-600 underline transition-colors hover:text-primary-700 dark:text-primary-400"
          >
            {CONTACT_EMAIL}
          </a>
          .
        </p>
      </section>
    </div>
  );
}
