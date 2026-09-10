// Crawl the static export in out/ and check that every internal link resolves.
//
//   STATIC_EXPORT=1 NEXT_PUBLIC_BASE_PATH=/subway-seat bun run build
//   bun run check:links
//
// Checks every href, src, srcset, og:image, twitter:image, canonical, og:url and
// manifest icon in every HTML page: the target must exist in out/, sit under
// the base path, and (for #fragments) have a matching id on the page.

import { existsSync, readdirSync, readFileSync, statSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const OUT = path.join(path.dirname(fileURLToPath(import.meta.url)), "..", "out");
const BASE = process.env.NEXT_PUBLIC_BASE_PATH ?? "/subway-seat";
const ORIGIN = "https://oddurs.github.io";

if (!existsSync(OUT)) {
  console.error("✗ no out/ directory: run the static export build first");
  process.exit(1);
}

function* walk(dir: string): Generator<string> {
  for (const name of readdirSync(dir)) {
    const full = path.join(dir, name);
    if (statSync(full).isDirectory()) yield* walk(full);
    else yield full;
  }
}

const decode = (s: string) =>
  s
    .replace(/&amp;/g, "&")
    .replace(/&quot;/g, '"')
    .replace(/&#x27;|&#39;/g, "'");

/** A URL path under the base path → the file GitHub Pages would serve, or null. */
function resolve(urlPath: string): string | null {
  if (!urlPath.startsWith(`${BASE}/`) && urlPath !== BASE) return null;
  const rel = decodeURIComponent(urlPath.slice(BASE.length)) || "/";
  const target = path.join(OUT, rel);
  if (!target.startsWith(OUT)) return null;
  if (existsSync(target) && statSync(target).isFile()) return target;
  const index = path.join(target, "index.html");
  if (existsSync(index)) return index;
  if (existsSync(`${target}.html`)) return `${target}.html`;
  return null;
}

const ids = new Map<string, Set<string>>();
function idsOf(file: string) {
  let set = ids.get(file);
  if (!set) {
    set = new Set([...readFileSync(file, "utf8").matchAll(/\sid="([^"]+)"/g)].map((m) => m[1]));
    ids.set(file, set);
  }
  return set;
}

const problems: string[] = [];
let pages = 0;
let checked = 0;

for (const file of walk(OUT)) {
  if (!file.endsWith(".html")) continue;
  pages++;
  const html = readFileSync(file, "utf8");
  const page = `/${path.relative(OUT, file)}`;
  const urls = new Set<string>();
  for (const m of html.matchAll(/\s(?:href|src)="([^"]*)"/g)) urls.add(decode(m[1]));
  for (const m of html.matchAll(/\ssrcset="([^"]*)"/g)) {
    for (const part of decode(m[1]).split(",")) urls.add(part.trim().split(/\s+/)[0]);
  }
  for (const m of html.matchAll(
    /<meta (?:property|name)="(?:og:image|og:url|twitter:image)" content="([^"]*)"/g,
  )) {
    urls.add(decode(m[1]));
  }

  for (const raw of urls) {
    if (!raw || /^(mailto:|tel:|data:|javascript:)/.test(raw)) continue;
    let url: URL;
    try {
      url = new URL(raw, `${ORIGIN}${page.replace(/index\.html$/, "")}`);
    } catch {
      problems.push(`${page}: unparseable URL ${raw}`);
      continue;
    }
    if (url.origin !== ORIGIN) continue; // external
    checked++;
    if (raw.startsWith("#")) {
      const id = decodeURIComponent(raw.slice(1));
      if (id && !idsOf(file).has(id)) problems.push(`${page}: no element with id "${id}"`);
      continue;
    }
    const target = resolve(url.pathname);
    if (!target) {
      problems.push(`${page}: ${raw} → nothing at ${url.pathname}`);
      continue;
    }
    if (url.hash && target.endsWith(".html")) {
      const id = decodeURIComponent(url.hash.slice(1));
      if (id && !idsOf(target).has(id)) problems.push(`${page}: ${raw} → no id "${id}" there`);
    }
  }
}

// The web manifest's icons and start URL.
const webmanifest = path.join(OUT, "manifest.webmanifest");
if (existsSync(webmanifest)) {
  const m = JSON.parse(readFileSync(webmanifest, "utf8")) as {
    start_url?: string;
    icons?: { src: string }[];
  };
  for (const src of [m.start_url, ...(m.icons ?? []).map((i) => i.src)].filter(
    Boolean,
  ) as string[]) {
    checked++;
    if (!resolve(new URL(src, ORIGIN).pathname))
      problems.push(`manifest.webmanifest: ${src} → nothing there`);
  }
}

if (problems.length) {
  console.error(problems.slice(0, 80).join("\n"));
  if (problems.length > 80) console.error(`… and ${problems.length - 80} more`);
  console.error(`✗ ${problems.length} broken link(s) in ${pages} pages`);
  process.exit(1);
}
console.log(`✓ ${checked} internal links in ${pages} pages resolve under ${BASE}/`);
