import Link from "next/link";
import { CONTACT_EMAIL } from "@/lib/constants";

function getFooter(dict: Record<string, unknown> | undefined) {
  const f = (dict as any)?.footer || {};
  return {
    copyright: (f.copyright as string) || "AI Study Online. All rights reserved.",
    about: (f.about as string) || "About",
    privacy: (f.privacy as string) || "Privacy Policy",
    terms: (f.terms as string) || "Terms of Service",
    contact: (f.contact as string) || "Contact",
    blog: (f.blog as string) || "Blog",
    tools: (f.tools as string) || "AI Tools",
    learn: (f.learn as string) || "Learn AI",
  };
}

export default function Footer({
  locale = "en",
  dict,
}: {
  locale?: string;
  dict?: Record<string, unknown>;
}) {
  const f = getFooter(dict);

  return (
    <footer className="border-t border-primary-200 bg-white dark:border-zinc-800 dark:bg-zinc-950">
      <div className="mx-auto max-w-6xl px-4 py-8 sm:px-6">
        <div className="flex flex-col items-center gap-4 text-center sm:flex-row sm:justify-between">
          <p className="text-sm text-zinc-500 dark:text-zinc-400">
            &copy; {new Date().getFullYear()} {f.copyright}
          </p>
          <div className="flex flex-wrap items-center justify-center gap-4 text-sm text-zinc-500 dark:text-zinc-400">
            <Link href={`/${locale}/tools`} className="hover:text-zinc-900 dark:hover:text-white">
              {f.tools}
            </Link>
            <Link href={`/${locale}/learn`} className="hover:text-zinc-900 dark:hover:text-white">
              {f.learn}
            </Link>
            <Link href={`/${locale}/blog`} className="hover:text-zinc-900 dark:hover:text-white">
              {f.blog}
            </Link>
            <Link href={`/${locale}/about`} className="hover:text-zinc-900 dark:hover:text-white">
              {f.about}
            </Link>
            <Link href={`/${locale}/privacy`} className="hover:text-zinc-900 dark:hover:text-white">
              {f.privacy}
            </Link>
            <Link href={`/${locale}/terms`} className="hover:text-zinc-900 dark:hover:text-white">
              {f.terms}
            </Link>
            <Link href={`/${locale}/contact`} className="hover:text-zinc-900 dark:hover:text-white">
              {f.contact}
            </Link>
            <span className="text-zinc-400">{CONTACT_EMAIL}</span>
          </div>
        </div>
      </div>
    </footer>
  );
}
