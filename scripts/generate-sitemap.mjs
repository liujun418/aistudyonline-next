import { readFileSync, writeFileSync } from "fs";

const resolve = (p) => new URL(p, import.meta.url).pathname.replace(/^\/([a-z]):\//i, "$1:/");

const SITE = "https://aistudyonline.club";

function esc(s) {
  return s.replace(/&/g, "&amp;").replace(/'/g, "&apos;").replace(/"/g, "&quot;")
          .replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

function addUrl(loc, lastmod, prio, freq) {
  return `<url><loc>${esc(loc)}</loc><lastmod>${lastmod}</lastmod><priority>${prio}</priority><changefreq>${freq}</changefreq></url>`;
}

// Parse articles with dates
const articlesSrc = readFileSync(resolve("../src/lib/articles.ts"), "utf-8");
const articles = [];
const articleRe = /\{\s*slug:\s*"([^"]+)"[\s\S]*?date:\s*"([^"]+)"/g;
let am;
while ((am = articleRe.exec(articlesSrc))) {
  articles.push({ slug: am[1], date: am[2] });
}

// Parse blog posts with dates
const blogSrc = readFileSync(resolve("../src/lib/blog-posts.ts"), "utf-8");
const blogs = [];
const blogRe = /\{\s*slug:\s*"([^"]+)"[\s\S]*?date:\s*"([^"]+)"/g;
let bm;
while ((bm = blogRe.exec(blogSrc))) {
  blogs.push({ slug: bm[1], date: bm[2] });
}

// Parse tools (no date field, use today)
function readSlugs(file, pattern) {
  const src = readFileSync(file, "utf-8");
  const slugs = [];
  const re = new RegExp(pattern, "g");
  let m;
  while ((m = re.exec(src))) slugs.push(m[1]);
  return slugs;
}

const toolSlugs = readSlugs(resolve("../src/lib/tools.ts"), 'id:\\s*"([^"]+)"');
const modelSlugs = readSlugs(resolve("../src/lib/models.ts"), 'id:\\s*"([^"]+)"');
const categoryIds = readSlugs(resolve("../src/lib/categories.ts"), 'id:\\s*"([^"]+)"');

const today = new Date().toISOString().split("T")[0] + "T00:00:00+00:00";

let xml = '<?xml version="1.0" encoding="utf-8" standalone="yes"?>';
xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">';

// Homepages (en + zh)
xml += addUrl(`${SITE}/en`, today, "1.0", "daily");
xml += addUrl(`${SITE}/zh`, today, "1.0", "daily");

// Listing pages
for (const loc of ["en", "zh"]) {
  for (const p of ["/tools", "/models", "/learn", "/blog"]) {
    xml += addUrl(`${SITE}/${loc}${p}`, today, "0.9", "weekly");
  }
  // Static pages
  for (const p of ["/about", "/privacy", "/terms", "/refund"]) {
    xml += addUrl(`${SITE}/${loc}/${p}`, today, "0.5", "monthly");
  }
  // Categories
  for (const c of categoryIds) {
    xml += addUrl(`${SITE}/${loc}/learn/${c}`, today, "0.8", "weekly");
  }
  // Articles (with real dates)
  for (const a of articles) {
    const d = a.date + "T00:00:00+00:00";
    xml += addUrl(`${SITE}/${loc}/article/${a.slug}`, d, "0.8", "weekly");
  }
  // Tools
  for (const s of toolSlugs) {
    xml += addUrl(`${SITE}/${loc}/tools/${s}`, today, "0.8", "weekly");
  }
  // Models
  for (const s of modelSlugs) {
    xml += addUrl(`${SITE}/${loc}/models/${s}`, today, "0.8", "weekly");
  }
  // Blog posts (with real dates)
  for (const b of blogs) {
    const d = b.date + "T00:00:00+00:00";
    xml += addUrl(`${SITE}/${loc}/blog/${b.slug}`, d, "0.7", "monthly");
  }
}

xml += "</urlset>";

const out = resolve("../public/sitemap.xml");
writeFileSync(out, xml);

const urlCount = (xml.match(/<url>/g) || []).length;
console.log(`Sitemap: ${urlCount} URLs (${(Buffer.byteLength(xml)/1024).toFixed(1)}KB)`);
