import type { MetadataRoute } from "next";
import { BASE } from "@/lib/base";
import { flavorById } from "@/lib/palette";
import { sign } from "@/theme/sign.stylex";

export const dynamic = "force-static";

export default function manifest(): MetadataRoute.Manifest {
  const walnut = flavorById.walnut.colors;
  return {
    name: "Subway Seat",
    short_name: "Subway Seat",
    description: "A warm 1970s subway-car color scheme in three flavors.",
    start_url: `${BASE}/`,
    scope: `${BASE}/`,
    display: "standalone",
    background_color: walnut.mantle,
    theme_color: sign.bg,
    icons: [
      { src: `${BASE}/icon.svg`, type: "image/svg+xml", sizes: "any" },
      { src: `${BASE}/icon-192.png`, type: "image/png", sizes: "192x192" },
      { src: `${BASE}/icon-512.png`, type: "image/png", sizes: "512x512" },
    ],
  };
}
