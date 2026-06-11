"use client";

import { useState, useEffect } from "react";

declare global {
  interface Window {
    __cookieConsent?: "accepted" | "rejected";
    gtag?: (...args: unknown[]) => void;
    dataLayer?: unknown[];
  }
}

const COOKIE_CONSENT_KEY = "aistudyonline-cookie-consent";

type ConsentChoice = "accepted" | "rejected" | null;

export default function CookieConsent() {
  const [consent, setConsent] = useState<ConsentChoice>(null);
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    setMounted(true);
    const stored = localStorage.getItem(COOKIE_CONSENT_KEY) as ConsentChoice;
    if (stored) {
      setConsent(stored);
      applyConsent(stored);
    }
  }, []);

  function applyConsent(choice: "accepted" | "rejected") {
    if (choice === "accepted") {
      // Enable GA4 and AdSense — no-op since scripts are already loaded,
      // but we can set a flag for future reference.
      window.__cookieConsent = "accepted";
    } else {
      // Reject non-essential: disable GA4
      window.__cookieConsent = "rejected";
      if (typeof window.gtag === "function") {
        window.gtag("consent", "update", {
          analytics_storage: "denied",
          ad_storage: "denied",
          ad_user_data: "denied",
          ad_personalization: "denied",
        });
      }
      // Disable GA4 by overriding dataLayer pushes
      const noop = () => {};
      window.dataLayer = [];
      window.gtag = noop;
    }
  }

  function handleAccept() {
    localStorage.setItem(COOKIE_CONSENT_KEY, "accepted");
    setConsent("accepted");
    applyConsent("accepted");
  }

  function handleReject() {
    localStorage.setItem(COOKIE_CONSENT_KEY, "rejected");
    setConsent("rejected");
    applyConsent("rejected");
  }

  // Don't render during SSR or if consent already given
  if (!mounted || consent !== null) return null;

  return (
    <div
      className="fixed bottom-0 left-0 right-0 z-50 border-t border-zinc-200 bg-white/95 p-4 shadow-lg backdrop-blur-sm dark:border-zinc-800 dark:bg-zinc-950/95"
      role="dialog"
      aria-label="Cookie consent"
    >
      <div className="mx-auto flex max-w-6xl flex-col items-center gap-3 sm:flex-row sm:justify-between">
        <p className="text-center text-sm text-zinc-600 dark:text-zinc-400 sm:text-left">
          This site uses cookies for analytics and advertising. By continuing,
          you agree to our use of cookies. See our{" "}
          <a
            href="/en/privacy"
            className="underline underline-offset-2 hover:text-zinc-900 dark:hover:text-white"
          >
            Privacy Policy
          </a>{" "}
          for details.
        </p>
        <div className="flex shrink-0 flex-wrap items-center gap-2">
          <button
            onClick={handleReject}
            className="rounded-lg border border-zinc-300 px-4 py-2 text-sm font-medium text-zinc-700 transition-colors hover:bg-zinc-100 dark:border-zinc-600 dark:text-zinc-300 dark:hover:bg-zinc-800"
          >
            Reject Non-Essential
          </button>
          <button
            onClick={handleAccept}
            className="rounded-lg bg-primary-600 px-4 py-2 text-sm font-medium text-white transition-colors hover:bg-primary-700 dark:bg-primary-500 dark:hover:bg-primary-600"
          >
            Accept All Cookies
          </button>
        </div>
      </div>
    </div>
  );
}
