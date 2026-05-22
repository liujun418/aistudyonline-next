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
    title: `Privacy Policy — ${SITE_NAME}`,
    description: `${SITE_NAME} privacy policy — how we handle your data.`,
    openGraph: {
      type: "website",
      locale: localeMap[locale] || "en_US",
      url: `${SITE_URL}/${locale}/privacy`,
      siteName: SITE_NAME,
      title: `Privacy Policy — ${SITE_NAME}`,
      description: `${SITE_NAME} privacy policy — how we handle your data.`,
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

  return (
    <div className="mx-auto max-w-3xl px-4 py-12 sm:px-6">
      <h1 className="mb-8 text-3xl font-bold text-foreground">Privacy Policy</h1>
      <p className="mb-8 text-sm text-zinc-500 dark:text-zinc-400">
        Last updated: May 21, 2026
      </p>

      <section className="mb-8">
        <h2 className="mb-3 text-xl font-semibold text-foreground">Information We Collect</h2>
        <p className="leading-relaxed text-zinc-600 dark:text-zinc-400">
          AI Study Online does not collect personal information from its visitors.
          We do not require registration, accounts, or email sign-ups to use our
          tools or read our content.
        </p>
      </section>

      <section className="mb-8">
        <h2 className="mb-3 text-xl font-semibold text-foreground">Google AdSense</h2>
        <p className="leading-relaxed text-zinc-600 dark:text-zinc-400">
          We use Google AdSense to display advertisements on our website. Google
          AdSense uses cookies to serve ads based on your previous visits to our
          website or other websites. You can opt out of personalized advertising
          by visiting{" "}
          <a
            href="https://www.google.com/settings/ads"
            target="_blank"
            rel="noopener noreferrer"
            className="text-primary-600 underline transition-colors hover:text-primary-700 dark:text-primary-400"
          >
            Google Ads Settings
          </a>
          .
        </p>
      </section>

      <section className="mb-8">
        <h2 className="mb-3 text-xl font-semibold text-foreground">Google Analytics</h2>
        <p className="leading-relaxed text-zinc-600 dark:text-zinc-400">
          We use Google Analytics to understand how visitors interact with our
          website. This data is anonymized and helps us improve our content and
          user experience. Google Analytics collects information such as page
          views, referral sources, and browser types.
        </p>
      </section>

      <section className="mb-8">
        <h2 className="mb-3 text-xl font-semibold text-foreground">Cookies</h2>
        <p className="leading-relaxed text-zinc-600 dark:text-zinc-400">
          Our website uses cookies for the following purposes:
        </p>
        <ul className="mt-2 list-inside list-disc space-y-1 text-zinc-600 dark:text-zinc-400">
          <li>Google AdSense advertising cookies</li>
          <li>Google Analytics performance cookies</li>
          <li>Language preference cookie (locale)</li>
          <li>Theme preference cookie (dark/light mode)</li>
        </ul>
      </section>

      <section className="mb-8">
        <h2 className="mb-3 text-xl font-semibold text-foreground">Third-Party Links</h2>
        <p className="leading-relaxed text-zinc-600 dark:text-zinc-400">
          Our website contains links to third-party websites. We are not
          responsible for the privacy practices of these websites. We encourage
          you to review their privacy policies before providing any personal
          information.
        </p>
      </section>

      <section className="mb-8">
        <h2 className="mb-3 text-xl font-semibold text-foreground">Contact</h2>
        <p className="leading-relaxed text-zinc-600 dark:text-zinc-400">
          If you have any questions about this privacy policy, please contact us
          at{" "}
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
