import type { MetadataRoute } from "next";
import { BASE } from "@/lib/base";
import { ORIGIN } from "@/lib/seo";

// Crawlers only read robots.txt at a domain's root, so under /subway-seat/ this
// file is a signpost to the sitemap; it starts counting on a custom domain.
export const dynamic = "force-static";

export default function robots(): MetadataRoute.Robots {
  return {
    rules: { userAgent: "*", allow: "/", disallow: "/shot/" },
    sitemap: `${ORIGIN}${BASE}/sitemap.xml`,
  };
}
