import type { Metadata } from "next";
import { BASE } from "./base";

/** The site's origin. Next adds the base path to generated image URLs by itself. */
export const ORIGIN = "https://oddurs.github.io";
export const SITE_NAME = "Subway Seat";
export const REPO = "https://github.com/oddurs/subway-seat";

/** Absolute URL of a page, with the base path and the trailing slash Pages serves. */
export function pageUrl(path: string) {
  const clean = path === "/" ? "/" : `${path.replace(/\/$/, "")}/`;
  return `${ORIGIN}${BASE}${clean}`;
}

/** Canonical, Open Graph and share-image fields for one page. `image` is a card in /og/. */
export function pageMeta(
  path: string,
  title: string,
  description: string,
  image: { name: string; alt: string },
): Metadata {
  const url = pageUrl(path);
  const images = [{ url: `${BASE}/og/${image.name}`, width: 1200, height: 630, alt: image.alt }];
  return {
    description,
    alternates: { canonical: url },
    openGraph: {
      type: "website",
      siteName: SITE_NAME,
      url,
      title,
      description,
      locale: "en_US",
      images,
    },
    twitter: { card: "summary_large_image", title, description, images },
  };
}

/** Plain text from notes: no backticks, one or two sentences, at most `max` characters. */
export function summary(text: string, max: number) {
  const plain = text
    .replace(/`([^`]+)`/g, "$1")
    .replace(/\s+/g, " ")
    .trim();
  if (plain.length <= max) return plain;
  const sentences = plain.match(/[^.!?]+[.!?]+(\s|$)/g) ?? [];
  let out = "";
  for (const s of sentences) {
    if ((out + s).trim().length > max) break;
    out += s;
  }
  if (out) return out.trim();
  return `${plain.slice(0, max - 1).replace(/\s+\S*$/, "")}…`;
}
