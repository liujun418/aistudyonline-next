export const locales = ["en", "zh"] as const;
export type Locale = (typeof locales)[number];
export const defaultLocale: Locale = "en";

export const localeNames: Record<Locale, string> = {
  en: "English",
  zh: "中文",
};

export const localeDir: Record<Locale, "ltr" | "rtl"> = {
  en: "ltr",
  zh: "ltr",
};

export function isValidLocale(locale: string): locale is Locale {
  return (locales as readonly string[]).includes(locale);
}

const dictionaries: Record<string, () => Promise<Record<string, unknown>>> = {
  en: () => import("@/locales/en/common.json").then((m) => m.default),
  zh: () => import("@/locales/zh/common.json").then((m) => m.default),
};

export async function getDictionary(locale: Locale): Promise<Record<string, unknown>> {
  return dictionaries[locale]();
}
