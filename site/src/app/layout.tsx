import * as stylex from "@stylexjs/stylex";
import type { Metadata, Viewport } from "next";
import { Fraunces, JetBrains_Mono } from "next/font/google";
import type { ReactNode } from "react";
import { FlavorSync } from "@/components/FlavorSync";
import { ports, version } from "@/lib/manifest";
import { ORIGIN, pageMeta, pageUrl, REPO, SITE_NAME } from "@/lib/seo";
import { enamel, tunnel, walnut } from "@/theme/flavors";
import { enamelInk } from "@/theme/ink";
import { sign } from "@/theme/sign.stylex";
import { color } from "@/theme/tokens.stylex";
import { font } from "@/theme/type.stylex";
import "./globals.css";

// Italic mono is kept for italic comments in highlighted code, but not preloaded.
const mono = JetBrains_Mono({
  subsets: ["latin"],
  style: ["normal", "italic"],
  variable: "--font-jetbrains-mono",
  preload: false,
});

// Fraunces' SOFT and WONK axes give the chunky, friendly 70s display type.
const display = Fraunces({
  subsets: ["latin"],
  axes: ["SOFT", "WONK", "opsz"],
  variable: "--font-fraunces",
});

const count = ports().length;
const description = `A walnut-brown 1970s subway-car color scheme for Ghostty, VS Code, Neovim, Zed, Claude Code and more: ${count} ports in three flavors. Sit back.`;

export const metadata: Metadata = {
  metadataBase: new URL(ORIGIN),
  title: { default: "Subway Seat: a warm 1970s color scheme", template: "%s · Subway Seat" },
  applicationName: SITE_NAME,
  ...pageMeta("/", "Subway Seat: a warm 1970s color scheme", description, {
    name: "home.png",
    alt: "Subway Seat: a walnut-brown 1970s subway-car color scheme in three flavors.",
  }),
};

// The browser bar runs into the station-sign nav, which is the same black in every flavor.
export const viewport: Viewport = { themeColor: sign.bg };

const themeClasses = {
  walnut: stylex.props(walnut).className ?? "",
  tunnel: stylex.props(tunnel).className ?? "",
  enamel: stylex.props(enamel, enamelInk).className ?? "",
};

// Runs before paint: saved choice, else the system's light/dark preference.
const boot = `(() => {
  const d = document.documentElement, c = ${JSON.stringify(themeClasses)};
  let f = null;
  try { f = localStorage.getItem("subway-seat:flavor"); } catch {}
  const q = new URLSearchParams(location.search).get("flavor");
  if (c[q]) f = q;
  if (!c[f]) f = matchMedia("(prefers-color-scheme: light)").matches ? "enamel" : "walnut";
  d.dataset.flavor = f;
  d.style.colorScheme = f === "enamel" ? "light" : "dark";
  for (const k of c[f].split(" ")) if (k) d.classList.add(k);
})();`;

const jsonLd = {
  "@context": "https://schema.org",
  "@type": "SoftwareSourceCode",
  name: SITE_NAME,
  description,
  url: pageUrl("/"),
  codeRepository: REPO,
  license: "https://opensource.org/licenses/MIT",
  programmingLanguage: "Python",
  ...(version() ? { version: version() } : {}),
  author: { "@type": "Person", name: "Oddur Sigurdsson", url: "https://github.com/oddurs" },
};

export default function RootLayout({ children }: { children: ReactNode }) {
  const html = stylex.props(styles.html);
  return (
    <html
      lang="en"
      className={`${mono.variable} ${display.variable} ${html.className ?? ""}`}
      style={html.style}
      data-flavor="walnut"
      data-theme-classes={JSON.stringify(themeClasses)}
      suppressHydrationWarning
    >
      <head>
        {/* biome-ignore lint/security/noDangerouslySetInnerHtml: static boot script */}
        <script dangerouslySetInnerHTML={{ __html: boot }} />
        <script
          type="application/ld+json"
          // biome-ignore lint/security/noDangerouslySetInnerHtml: static structured data
          dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
        />
      </head>
      <body {...stylex.props(styles.body)}>
        <FlavorSync />
        {children}
        <div id="announcer" aria-live="polite" className="sr-only" />
      </body>
    </html>
  );
}

const styles = stylex.create({
  html: {
    scrollBehavior: {
      default: "smooth",
      "@media (prefers-reduced-motion: reduce)": "auto",
    },
    // The canvas below a short page continues the footer.
    backgroundColor: color.crust,
  },
  body: {
    overflowX: "clip",
    fontFamily: font.sans,
    fontSize: 16,
    lineHeight: 1.6,
    color: color.text,
    backgroundColor: color.mantle,
    transitionDuration: "240ms",
    transitionProperty: "background-color, color",
  },
});
