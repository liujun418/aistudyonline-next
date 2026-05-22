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
const LASTMOD = new Date().toISOString().replace(/\.\d{3}Z$/, "+00:00").replace("T", "T").replace("+00:00", "+00:00");

const articleSlugs = readSlugs(resolve("../src/lib/articles.ts"), 'slug:\\s*"([^"]+)"');
const toolSlugs = readSlugs(resolve("../src/lib/tools.ts"), 'id:\\s*"([^"]+)"');
const modelSlugs = readSlugs(resolve("../src/lib/models.ts"), 'id:\\s*"([^"]+)"');
const blogSlugs = readSlugs(resolve("../src/lib/blog-posts.ts"), 'slug:\\s*"([^"]+)"');
const categoryIds = readSlugs(resolve("../src/lib/categories.ts"), 'id:\\s*"([^"]+)"');

const staticPages = ["about", "privacy", "terms", "refund"];

function esc(s) {
  return s.replace(/&/g, "&amp;").replace(/'/g, "&apos;").replace(/"/g, "&quot;")
          .replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

function urlEntry(path, prio, freq) {
  const canonical = `${SITE}/${XDEFAULT}${path}`;
  let s = `<url><loc>${esc(canonical)}</loc><lastmod>${LASTMOD}</lastmod><priority>${prio}</priority><changefreq>${freq}</changefreq>`;
  for (const l of LOCALES) {
    s += `<xhtml:link rel="alternate" hreflang="${l}" href="${esc(SITE)}/${l}${path}"/>`;
  }
  s += `<xhtml:link rel="alternate" hreflang="x-default" href="${esc(canonical)}"/>`;
  s += `</url>`;
  return s;
}

let xml = '<?xml version="1.0" encoding="utf-8" standalone="yes"?>';
xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">';

// Homepage
xml += urlEntry("", "1.0", "daily");
// Listing pages
for (const p of ["/tools", "/models", "/learn", "/blog"]) {
  xml += urlEntry(p, "0.9", "weekly");
}
// Categories
for (const c of categoryIds) { xml += urlEntry(`/learn/${c}`, "0.8", "weekly"); }
// Articles
for (const s of articleSlugs) { xml += urlEntry(`/article/${s}`, "0.8", "weekly"); }
// Tools
for (const s of toolSlugs) { xml += urlEntry(`/tools/${s}`, "0.8", "weekly"); }
// Models
for (const s of modelSlugs) { xml += urlEntry(`/models/${s}`, "0.8", "weekly"); }
// Blogs
for (const s of blogSlugs) { xml += urlEntry(`/blog/${s}`, "0.7", "monthly"); }
// Static
for (const p of staticPages) { xml += urlEntry(`/${p}`, "0.5", "monthly"); }

xml += "</urlset>";

const out = resolve("../public/sitemap.xml");
writeFileSync(out, xml);
const size = (Buffer.byteLength(xml) / 1024).toFixed(1);
console.log(`Sitemap: ${articleSlugs.length + toolSlugs.length + modelSlugs.length + blogSlugs.length + categoryIds.length + staticPages.length + 5} canonical URLs (${size}KB)`);
