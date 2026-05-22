import { readFileSync, writeFileSync } from "fs";

const resolve = (p) => new URL(p, import.meta.url).pathname.replace(/^\/([a-z]):\//i, "$1:/");

function readSlugs(file, pattern) {
  const src = readFileSync(file, "utf-8");
  const slugs = [];
  const re = new RegExp(pattern, "g");
  let m;
  while ((m = re.exec(src))) slugs.push(m[1]);
  return slugs;
}

const SITE = "https://aistudyonline.club";
const LOCALES = ["en", "zh"];
const XDEFAULT = "en";
const LASTMOD = new Date().toISOString().replace(/\.\d{3}Z$/, "+00:00");

const articleSlugs = readSlugs(resolve("../src/lib/articles.ts"), 'slug:\\s*"([^"]+)"');
const toolSlugs = readSlugs(resolve("../src/lib/tools.ts"), 'id:\\s*"([^"]+)"');
const modelSlugs = readSlugs(resolve("../src/lib/models.ts"), 'id:\\s*"([^"]+)"');
const blogSlugs = readSlugs(resolve("../src/lib/blog-posts.ts"), 'slug:\\s*"([^"]+)"');
const categoryIds = readSlugs(resolve("../src/lib/categories.ts"), 'id:\\s*"([^"]+)"');

const staticPages = ["about", "privacy", "terms", "refund"];

function esc(s) {
  return s.replace(/&/g, "&amp;").replace(/"/g, "&quot;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

function hreflang(url) {
  let links = "";
  for (const l of LOCALES) {
    const u = url.replace("/__LOCALE__/", `/${l}/`);
    links += `<xhtml:link rel="alternate" hreflang="${l}" href="${esc(u)}"/>`;
  }
  const xd = url.replace("/__LOCALE__/", `/${XDEFAULT}/`);
  links += `<xhtml:link rel="alternate" hreflang="x-default" href="${esc(xd)}"/>`;
  return links;
}

function urlEntry(path, prio, freq) {
  let xml = "";
  for (const l of LOCALES) {
    const u = `${SITE}/${l}${path}`;
    xml += `<url><loc>${esc(u)}</loc><lastmod>${LASTMOD}</lastmod><priority>${prio}</priority><changefreq>${freq}</changefreq>`;
    // Build hreflang links for each locale
    for (const hl of LOCALES) {
      xml += `<xhtml:link rel="alternate" hreflang="${hl}" href="${esc(SITE)}/${hl}${path}"/>`;
    }
    xml += `<xhtml:link rel="alternate" hreflang="x-default" href="${esc(SITE)}/${XDEFAULT}${path}"/>`;
    xml += `</url>`;
  }
  return xml;
}

// Remove unused hreflang function

let count = 0;
let xml = '<?xml version="1.0" encoding="utf-8" standalone="yes"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n';

// Homepage
xml += urlEntry("", "1.0", "daily"); count += 2;
// Tools
xml += urlEntry("/tools", "0.9", "weekly"); count += 2;
// Models
xml += urlEntry("/models", "0.9", "weekly"); count += 2;
// Learn
xml += urlEntry("/learn", "0.9", "weekly"); count += 2;
// Blog
xml += urlEntry("/blog", "0.7", "weekly"); count += 2;

// Categories
for (const c of categoryIds) { xml += urlEntry(`/learn/${c}`, "0.8", "weekly"); count += 2; }
// Articles
for (const s of articleSlugs) { xml += urlEntry(`/article/${s}`, "0.8", "weekly"); count += 2; }
// Tools detail
for (const s of toolSlugs) { xml += urlEntry(`/tools/${s}`, "0.8", "weekly"); count += 2; }
// Models detail
for (const s of modelSlugs) { xml += urlEntry(`/models/${s}`, "0.8", "weekly"); count += 2; }
// Blog posts
for (const s of blogSlugs) { xml += urlEntry(`/blog/${s}`, "0.7", "monthly"); count += 2; }
// Static pages
for (const p of staticPages) { xml += urlEntry(`/${p}`, "0.5", "monthly"); count += 2; }

xml += "</urlset>\n";

const out = resolve("../public/sitemap.xml");
writeFileSync(out, xml);
console.log(`Sitemap: ${count} URLs (${articleSlugs.length} articles, ${toolSlugs.length} tools, ${modelSlugs.length} models, ${blogSlugs.length} blogs, ${categoryIds.length} categories)`);
