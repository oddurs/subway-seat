import * as stylex from "@stylexjs/stylex";
import type { Metadata, Viewport } from "next";
import { Fraunces, JetBrains_Mono } from "next/font/google";
import type { ReactNode } from "react";
import { enamel, tunnel, walnut } from "@/theme/flavors";
import { color } from "@/theme/tokens.stylex";
import { font } from "@/theme/type.stylex";
import "./globals.css";

const mono = JetBrains_Mono({
  subsets: ["latin"],
  style: ["normal", "italic"],
  variable: "--font-jetbrains-mono",
});

// Fraunces' SOFT and WONK axes give the chunky, friendly 70s display type.
const display = Fraunces({
  subsets: ["latin"],
  axes: ["SOFT", "WONK", "opsz"],
  style: ["normal", "italic"],
  variable: "--font-fraunces",
});

export const metadata: Metadata = {
  metadataBase: new URL("https://oddurs.github.io/subway-seat/"),
  title: { default: "Subway Seat", template: "%s · Subway Seat" },
  description:
    "A walnut-brown 1970s subway-car color scheme for Ghostty, VS Code, Neovim, Zed, Claude Code and ~90 more apps. Three flavors. Sit back.",
};

export const viewport: Viewport = {
  themeColor: [
    { media: "(prefers-color-scheme: light)", color: "#EBDEC6" },
    { media: "(prefers-color-scheme: dark)", color: "#2A1D13" },
  ],
};

const themeClasses = {
  walnut: stylex.props(walnut).className ?? "",
  tunnel: stylex.props(tunnel).className ?? "",
  enamel: stylex.props(enamel).className ?? "",
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
      </head>
      <body {...stylex.props(styles.body)}>{children}</body>
    </html>
  );
}

const styles = stylex.create({
  html: {
    scrollBehavior: {
      default: "smooth",
      "@media (prefers-reduced-motion: reduce)": "auto",
    },
    backgroundColor: color.mantle,
  },
  body: {
    minHeight: "100vh",
    fontFamily: font.sans,
    fontSize: 16,
    lineHeight: 1.6,
    color: color.text,
    backgroundColor: color.mantle,
    transitionDuration: "240ms",
    transitionProperty: "background-color, color",
  },
});
