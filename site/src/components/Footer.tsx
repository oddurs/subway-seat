import * as stylex from "@stylexjs/stylex";
import Link from "next/link";
import { ports, version } from "@/lib/manifest";
import { REPO } from "@/lib/seo";
import { ink } from "@/theme/ink.stylex";
import { color } from "@/theme/tokens.stylex";
import { font } from "@/theme/type.stylex";

const LINKS = [
  { href: "/install", label: "Install" },
  { href: "/palette", label: "Palette" },
  { href: REPO, label: "GitHub" },
  { href: `${REPO}/blob/main/CHANGELOG.md`, label: "Changelog" },
  { href: `${REPO}/blob/main/CONTRIBUTING.md`, label: "Add a port" },
  { href: `${REPO}/issues/new?template=port-request.yml`, label: "Request an app" },
  { href: `${REPO}/blob/main/LICENSE`, label: "MIT license" },
];

export function Footer() {
  const v = version();
  return (
    <footer {...stylex.props(styles.footer)}>
      <div {...stylex.props(styles.inner)}>
        <p {...stylex.props(styles.signoff)}>Stand clear of the closing doors.</p>
        <p {...stylex.props(styles.fine)}>
          Every file on this site comes out of one{" "}
          <code {...stylex.props(styles.code)}>palette.py</code>. Change a color, run{" "}
          <code {...stylex.props(styles.code)}>./build.py</code>, and all {ports().length} ports
          follow.
        </p>
        <nav aria-label="Footer" {...stylex.props(styles.links)}>
          {LINKS.map((l) => (
            <Link key={l.href} href={l.href} prefetch={false} {...stylex.props(styles.link)}>
              {l.label}
            </Link>
          ))}
          {v && <span {...stylex.props(styles.version)}>v{v}</span>}
        </nav>
      </div>
    </footer>
  );
}

const styles = stylex.create({
  footer: {
    marginTop: 80,
    backgroundColor: color.crust,
    borderTopColor: color.surface0,
    borderTopStyle: "solid",
    borderTopWidth: 1,
  },
  inner: {
    display: "grid",
    gap: 14,
    maxWidth: 1200,
    paddingInline: 24,
    paddingTop: 48,
    paddingBottom: 56,
    marginInline: "auto",
  },
  signoff: {
    fontFamily: font.display,
    fontSize: "clamp(28px, 4vw, 42px)",
    fontVariationSettings: '"SOFT" 100, "WONK" 1',
    fontWeight: 700,
    lineHeight: 1.05,
    color: color.textHi,
    textWrap: "balance",
  },
  fine: { maxWidth: "62ch", fontSize: 15, color: color.subtext0 },
  code: { fontFamily: font.mono, fontSize: "0.9em", color: ink.code },
  links: { display: "flex", flexWrap: "wrap", rowGap: 4, columnGap: 20, alignItems: "center" },
  link: {
    paddingBlock: 6,
    fontSize: 14,
    color: {
      default: color.subtext1,
      ":hover": ink.accent,
    },
    textDecoration: "none",
    outlineWidth: 2,
    outlineStyle: {
      default: "none",
      ":focus-visible": "solid",
    },
    outlineColor: ink.accent,
    outlineOffset: 2,
    borderRadius: 2,
  },
  version: { fontFamily: font.mono, fontSize: 13, color: color.subtext0 },
});
