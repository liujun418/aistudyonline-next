import { readFileSync, writeFileSync } from "fs";

const ARTICLES_TS = new URL("../src/lib/articles.ts", import.meta.url).pathname.replace(/^\/([a-z]):\//i, "$1:/");
const CATEGORIES_TS = new URL("../src/lib/categories.ts", import.meta.url).pathname.replace(/^\/([a-z]):\//i, "$1:/");

const SITE = "https://aistudyonline.club";
const LOCALES = ["en", "es", "ar"];
const XDEFAULT = "en";

// Parse articles
const articlesSrc = readFileSync(ARTICLES_TS, "utf-8");
const articleSlugs = [];
const slugRe = /slug:\s*"([^"]+)"/g;
let m;
while ((m = slugRe.exec(articlesSrc))) {
  articleSlugs.push(m[1]);
}

// Parse categories
const categoriesSrc = readFileSync(CATEGORIES_TS, "utf-8");
const categoryIds = [];
const catIdRe = /id:\s*"([^"]+)"/g;
while ((m = catIdRe.exec(categoriesSrc))) {
  categoryIds.push(m[1]);
}

function esc(s) {
  return s.replace(/&/g, "&amp;").replace(/'/g, "&apos;").replace(/"/g, "&quot;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

function hreflangLinks(pathFn) {
  let links = "";
  for (const l of LOCALES) {
    links += `<xhtml:link rel="alternate" hreflang="${l}" href="${esc(SITE)}${pathFn(l)}"/>`;
  }
  links += `<xhtml:link rel="alternate" hreflang="x-default" href="${esc(SITE)}${pathFn(XDEFAULT)}"/>`;
  return links;
}

const d = new Date();
const pad = (n) => String(n).padStart(2, "0");
const lm = `${d.getUTCFullYear()}-${pad(d.getUTCMonth() + 1)}-${pad(d.getUTCDate())}T${pad(d.getUTCHours())}:${pad(d.getUTCMinutes())}:${pad(d.getUTCSeconds())}+00:00`;

let xml = '<?xml version="1.0" encoding="utf-8" standalone="yes"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">';

for (const l of LOCALES) {
  // Homepage
  xml += `<url><loc>${esc(SITE)}/${l}</loc><lastmod>${lm}</lastmod><priority>1.0</priority><changefreq>weekly</changefreq>`;
  xml += hreflangLinks((loc) => `/${loc}`);
  xml += `</url>`;

  // Tools page
  xml += `<url><loc>${esc(SITE)}/${l}/tools</loc><lastmod>${lm}</lastmod><priority>0.9</priority><changefreq>weekly</changefreq>`;
  xml += hreflangLinks((loc) => `/${loc}/tools`);
  xml += `</url>`;

  // Learn page
  xml += `<url><loc>${esc(SITE)}/${l}/learn</loc><lastmod>${lm}</lastmod><priority>0.9</priority><changefreq>weekly</changefreq>`;
  xml += hreflangLinks((loc) => `/${loc}/learn`);
  xml += `</url>`;

  // Category pages
  for (const catId of categoryIds) {
    xml += `<url><loc>${esc(SITE)}/${l}/learn/${catId}</loc><lastmod>${lm}</lastmod><priority>0.8</priority><changefreq>weekly</changefreq>`;
    xml += hreflangLinks((loc) => `/${loc}/learn/${catId}`);
    xml += `</url>`;
  }

  // Article pages
  for (const slug of articleSlugs) {
    xml += `<url><loc>${esc(SITE)}/${l}/article/${slug}</loc><lastmod>${lm}</lastmod><priority>0.7</priority><changefreq>monthly</changefreq>`;
    xml += hreflangLinks((loc) => `/${loc}/article/${slug}`);
    xml += `</url>`;
  }

  // Blog page
  xml += `<url><loc>${esc(SITE)}/${l}/blog</loc><lastmod>${lm}</lastmod><priority>0.6</priority><changefreq>weekly</changefreq>`;
  xml += hreflangLinks((loc) => `/${loc}/blog`);
  xml += `</url>`;

  // Blog posts
  const blogSlugs = ["welcome-to-ai-study-online"];
  for (const s of blogSlugs) {
    xml += `<url><loc>${esc(SITE)}/${l}/blog/${s}</loc><lastmod>${lm}</lastmod><priority>0.6</priority><changefreq>monthly</changefreq>`;
    xml += hreflangLinks((loc) => `/${loc}/blog/${s}`);
    xml += `</url>`;
  }

  // Static pages
  for (const pg of ["about", "privacy", "terms"]) {
    xml += `<url><loc>${esc(SITE)}/${l}/${pg}</loc><lastmod>${lm}</lastmod><priority>0.4</priority><changefreq>monthly</changefreq>`;
    xml += hreflangLinks((loc) => `/${loc}/${pg}`);
    xml += `</url>`;
  }
}

xml += `</urlset>`;

const out = new URL("../public/sitemap.xml", import.meta.url).pathname.replace(/^\/([a-z]):\//i, "$1:/");
writeFileSync(out, xml);
console.log(`Generated ${out} (${articleSlugs.length} articles, ${categoryIds.length} categories, ${LOCALES.length} locales, with hreflang)`);
