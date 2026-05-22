"use client";

import { useState } from "react";
import { useRouter, usePathname } from "next/navigation";
import Image from "next/image";
import Link from "next/link";
import ThemeToggle from "@/components/ThemeToggle";
import { locales, localeNames, Locale } from "@/lib/i18n";

function getNav(dict: Record<string, unknown> | undefined) {
  const nav = (dict as any)?.nav || {};
  return {
    models: (nav.models as string) || "AI Models",
    tools: (nav.tools as string) || "AI Tools",
    learn: (nav.learn as string) || "Learn AI",
    blog: (nav.blog as string) || "Blog",
    about: (nav.about as string) || "About",
  };
}

export default function Header({
  locale = "en",
  dict,
}: {
  locale?: string;
  dict?: Record<string, unknown>;
}) {
  const [showLang, setShowLang] = useState(false);
  const [showMobile, setShowMobile] = useState(false);
  const nav = getNav(dict);
  const router = useRouter();
  const pathname = usePathname();

  const switchLocale = (newLocale: Locale) => {
    document.cookie = `locale=${newLocale}; path=/; max-age=31536000`;
    const segments = pathname.split("/").filter(Boolean);
    if (segments.length > 0 && ["en", "zh"].includes(segments[0])) {
      segments[0] = newLocale;
    } else {
      segments.unshift(newLocale);
    }
    router.push("/" + segments.join("/"));
  };

  return (
    <header className="border-b border-primary-200 bg-white dark:border-primary-900 dark:bg-zinc-950">
      <div className="mx-auto flex max-w-6xl items-center justify-between px-4 py-4 sm:px-6">
        {/* Logo */}
        <Link href={`/${locale}`} className="flex-shrink-0">
          <Image
            src="/logo-b.png"
            alt="AI Study Online"
            width={160}
            height={36}
            className="h-9 w-auto dark:hidden"
            priority
          />
          <Image
            src="/logo-h.png"
            alt="AI Study Online"
            width={160}
            height={36}
            className="hidden h-9 w-auto dark:inline-block"
            priority
          />
        </Link>

        {/* Desktop nav */}
        <nav className="hidden items-center gap-5 text-sm text-zinc-600 md:flex dark:text-zinc-400">
          <Link href={`/${locale}/models`} className="hover:text-zinc-900 dark:hover:text-white">
            {nav.models}
          </Link>
          <Link href={`/${locale}/tools`} className="hover:text-zinc-900 dark:hover:text-white">
            {nav.tools}
          </Link>
          <Link href={`/${locale}/learn`} className="hover:text-zinc-900 dark:hover:text-white">
            {nav.learn}
          </Link>
          <Link href={`/${locale}/blog`} className="hover:text-zinc-900 dark:hover:text-white">
            {nav.blog}
          </Link>
          <Link href={`/${locale}/about`} className="hover:text-zinc-900 dark:hover:text-white">
            {nav.about}
          </Link>

          {/* Language switcher */}
          <div className="relative">
            <button
              onClick={() => setShowLang(!showLang)}
              className="rounded px-2 py-1 hover:text-zinc-900 dark:hover:text-white"
              aria-label={((dict as any)?.nav?.changeLanguage as string) || "Change language"}
            >
              {localeNames[locale as Locale] || "English"}
              <svg className="ms-1 inline-block h-3 w-3" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
              </svg>
            </button>
            {showLang && (
              <div className="absolute end-0 z-50 mt-1 rounded-lg border border-zinc-200 bg-white py-1 shadow-lg dark:border-zinc-700 dark:bg-zinc-900">
                {locales.map((l) => (
                  <button
                    key={l}
                    onClick={() => switchLocale(l)}
                    className={`block w-full px-4 py-1.5 text-start text-sm hover:bg-zinc-100 dark:hover:bg-zinc-800 ${
                      l === locale ? "font-semibold text-zinc-900 dark:text-white" : "text-zinc-600 dark:text-zinc-400"
                    }`}
                  >
                    {localeNames[l]}
                  </button>
                ))}
              </div>
            )}
          </div>

          <ThemeToggle locale={locale} dict={dict} />
        </nav>

        {/* Mobile hamburger */}
        <button
          onClick={() => setShowMobile(!showMobile)}
          className="p-2 text-zinc-600 md:hidden dark:text-zinc-400"
          aria-label="Toggle menu"
        >
          {showMobile ? (
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
              <line x1="18" y1="6" x2="6" y2="18" />
              <line x1="6" y1="6" x2="18" y2="18" />
            </svg>
          ) : (
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
              <line x1="3" y1="12" x2="21" y2="12" />
              <line x1="3" y1="6" x2="21" y2="6" />
              <line x1="3" y1="18" x2="21" y2="18" />
            </svg>
          )}
        </button>
      </div>

      {/* Mobile menu */}
      {showMobile && (
        <div className="border-t border-primary-200 bg-white px-4 py-4 md:hidden dark:border-primary-900 dark:bg-zinc-950">
          <div className="flex flex-col gap-3 text-sm text-zinc-600 dark:text-zinc-400">
            <Link
              href={`/${locale}/models`}
              className="hover:text-zinc-900 dark:hover:text-white"
              onClick={() => setShowMobile(false)}
            >
              {nav.models}
            </Link>
            <Link
              href={`/${locale}/tools`}
              className="hover:text-zinc-900 dark:hover:text-white"
              onClick={() => setShowMobile(false)}
            >
              {nav.tools}
            </Link>
            <Link
              href={`/${locale}/learn`}
              className="hover:text-zinc-900 dark:hover:text-white"
              onClick={() => setShowMobile(false)}
            >
              {nav.learn}
            </Link>
            <Link
              href={`/${locale}/blog`}
              className="hover:text-zinc-900 dark:hover:text-white"
              onClick={() => setShowMobile(false)}
            >
              {nav.blog}
            </Link>
            <Link
              href={`/${locale}/about`}
              className="hover:text-zinc-900 dark:hover:text-white"
              onClick={() => setShowMobile(false)}
            >
              {nav.about}
            </Link>
            <div className="flex items-center gap-3 pt-2">
              {locales.map((l) => (
                <button
                  key={l}
                  onClick={() => {
                    switchLocale(l);
                    setShowMobile(false);
                  }}
                  className={`text-sm ${
                    l === locale
                      ? "font-semibold text-primary-700 dark:text-primary-400"
                      : "text-zinc-500"
                  }`}
                >
                  {localeNames[l]}
                </button>
              ))}
              <ThemeToggle locale={locale} dict={dict} />
            </div>
          </div>
        </div>
      )}
    </header>
  );
}
