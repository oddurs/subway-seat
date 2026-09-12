import * as stylex from "@stylexjs/stylex";
import type { Metadata } from "next";
import Link from "next/link";
import { Footer } from "@/components/Footer";
import { Nav } from "@/components/Nav";
import { ink } from "@/theme/ink.stylex";
import { space } from "@/theme/space.stylex";
import { color } from "@/theme/tokens.stylex";
import { font } from "@/theme/type.stylex";

export const metadata: Metadata = { title: "Not found", robots: { index: false } };

export default function NotFound() {
  return (
    <>
      <Nav />
      <main id="main" {...stylex.props(styles.main)}>
        <p {...stylex.props(styles.label)}>404 · Not in service</p>
        <h1 {...stylex.props(styles.title)}>This train doesn&apos;t stop here.</h1>
        <p {...stylex.props(styles.body)}>
          The page you wanted isn&apos;t on the line. It may have moved, or the link was a little
          off.
        </p>
        <div {...stylex.props(styles.links)}>
          <Link href="/" {...stylex.props(styles.cta, styles.primary)}>
            Back to the start
          </Link>
          <Link href="/#ports" {...stylex.props(styles.cta, styles.secondary)}>
            Find your app
          </Link>
        </div>
      </main>
      <Footer />
    </>
  );
}

const styles = stylex.create({
  main: {
    display: "grid",
    gap: 20,
    justifyItems: "start",
    maxWidth: space.measure,
    minHeight: "50vh",
    paddingInline: space.gutter,
    paddingTop: 96,
    marginInline: "auto",
  },
  label: {
    fontSize: 13,
    fontWeight: 600,
    color: ink.accent,
    textTransform: "uppercase",
    letterSpacing: "0.16em",
  },
  title: {
    maxWidth: "14ch",
    fontFamily: font.display,
    fontSize: "clamp(40px, 6vw, 72px)",
    fontVariationSettings: '"SOFT" 100, "WONK" 1',
    fontWeight: 800,
    lineHeight: 1,
    color: color.textHi,
    textWrap: "balance",
  },
  body: { maxWidth: "52ch", fontSize: 18, color: color.subtext1, textWrap: "pretty" },
  links: { display: "flex", flexWrap: "wrap", gap: 12 },
  cta: {
    paddingBlock: 12,
    paddingInline: space.gutter,
    fontWeight: 700,
    textDecoration: "none",
    outlineWidth: 2,
    outlineStyle: {
      default: "none",
      ":focus-visible": "solid",
    },
    outlineColor: ink.accent,
    outlineOffset: 3,
    borderRadius: 999,
  },
  primary: {
    color: ink.onAccent,
    backgroundColor: {
      default: ink.fill,
      ":hover": ink.fillHover,
    },
  },
  secondary: {
    color: color.text,
    backgroundColor: {
      default: "transparent",
      ":hover": color.surface0,
    },
    borderColor: color.surface2,
    borderStyle: "solid",
    borderWidth: 1,
  },
});
