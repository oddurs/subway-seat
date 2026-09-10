import type { MetadataRoute } from "next";
import { ports } from "@/lib/manifest";
import { pageUrl } from "@/lib/seo";

export const dynamic = "force-static";

export default function sitemap(): MetadataRoute.Sitemap {
  const pages = ["/", "/install", "/palette", ...ports().map((p) => `/ports/${p.id}`)];
  return pages.map((path) => ({
    url: pageUrl(path),
    changeFrequency: "monthly",
    priority: path === "/" ? 1 : path.startsWith("/ports/") ? 0.6 : 0.8,
  }));
}
