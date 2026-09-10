import * as stylex from "@stylexjs/stylex";
import Link from "next/link";
import { ink } from "@/theme/ink.stylex";
import { color } from "@/theme/tokens.stylex";
import { font } from "@/theme/type.stylex";
import { Supergraphic } from "./Supergraphic";

export function Hero({ count }: { count: number }) {
  return (
    // The stripes run off the right edge; the page itself never scrolls sideways.
    <div {...stylex.props(styles.clip)}>
      <section {...stylex.props(styles.hero)}>
        <div {...stylex.props(styles.art)} aria-hidden>
          <Supergraphic />
        </div>
        <div {...stylex.props(styles.copy)}>
          <p {...stylex.props(styles.eyebrow)}>A color scheme for the long ride</p>
          <h1 {...stylex.props(styles.title)}>Sink into a warmer screen.</h1>
          <p {...stylex.props(styles.lede)}>
            Subway Seat is a walnut-brown theme from a 1970s subway car: orange bucket seats,
            wood-grain paneling, cream enamel and a little avocado. Three flavors, {count} ports,
            one palette.
          </p>
          <div {...stylex.props(styles.ctas)}>
            <Link href="/install" {...stylex.props(styles.cta, styles.primary)}>
              Get on board
            </Link>
            <Link href="#ports" {...stylex.props(styles.cta, styles.secondary)}>
              Find your app
            </Link>
          </div>
        </div>
      </section>
    </div>
  );
}

const NARROW = "@media (max-width: 860px)";

const styles = stylex.create({
  clip: { overflowX: "clip" },
  hero: {
    position: "relative",
    display: "grid",
    gridTemplateColumns: {
      [NARROW]: "minmax(0, 1fr)",
      default: "minmax(0, 1.1fr) minmax(0, 0.9fr)",
    },
    alignItems: "center",
    maxWidth: 1200,
    minHeight: {
      [NARROW]: 0,
      default: 520,
    },
    paddingInline: 24,
    paddingTop: {
      [NARROW]: 40,
      default: 72,
    },
    paddingBottom: 40,
    marginInline: "auto",
  },
  art: {
    position: {
      [NARROW]: "absolute",
      default: "absolute",
    },
    top: {
      [NARROW]: -120,
      default: -60,
    },
    right: {
      [NARROW]: -140,
      default: -40,
    },
    width: {
      [NARROW]: 420,
      default: 640,
    },
    pointerEvents: "none",
    opacity: {
      [NARROW]: 0.2,
      default: 1,
    },
  },
  copy: { position: "relative", display: "grid", gap: 22 },
  eyebrow: {
    fontFamily: font.sans,
    fontSize: 13,
    fontWeight: 600,
    color: ink.accent,
    textTransform: "uppercase",
    letterSpacing: "0.16em",
  },
  title: {
    maxWidth: "12ch",
    fontFamily: font.display,
    fontSize: "clamp(48px, 7.4vw, 96px)",
    fontVariationSettings: '"SOFT" 100, "WONK" 1, "opsz" 144',
    fontWeight: 800,
    lineHeight: 0.98,
    color: color.textHi,
    letterSpacing: "-0.02em",
    textWrap: "balance",
  },
  lede: {
    maxWidth: "52ch",
    fontSize: 19,
    lineHeight: 1.6,
    color: color.subtext1,
    textWrap: "pretty",
  },
  ctas: { display: "flex", flexWrap: "wrap", gap: 12 },
  cta: {
    flexGrow: {
      default: 0,
      "@media (max-width: 480px)": 1,
    },
    paddingBlock: 12,
    paddingInline: 24,
    fontSize: 16,
    fontWeight: 700,
    textAlign: "center",
    textDecoration: "none",
    outlineWidth: 2,
    outlineStyle: {
      default: "none",
      ":focus-visible": "solid",
    },
    outlineColor: ink.accent,
    outlineOffset: 3,
    borderRadius: 999,
    transform: {
      default: null,
      ":hover": "translateY(-1px)",
    },
    transitionDuration: "160ms",
    transitionProperty: "transform, background-color",
  },
  primary: {
    color: ink.onAccent,
    backgroundColor: {
      default: color.orange,
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
