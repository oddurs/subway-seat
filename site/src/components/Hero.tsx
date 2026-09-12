import * as stylex from "@stylexjs/stylex";
import Link from "next/link";
import { ink } from "@/theme/ink.stylex";
import { color } from "@/theme/tokens.stylex";
import { font } from "@/theme/type.stylex";
import { Diagram } from "./Diagram";
import { Supergraphic } from "./Supergraphic";

export function Hero({ count }: { count: number }) {
  return (
    // The stripes run off the right edge; the page itself never scrolls sideways.
    <div {...stylex.props(styles.clip)}>
      <section {...stylex.props(styles.hero)}>
        <div {...stylex.props(styles.art)} aria-hidden>
          <span data-only="new-york">
            <Supergraphic />
          </span>
          <span data-only="london" {...stylex.props(styles.diagram)}>
            <Diagram />
          </span>
        </div>
        <div {...stylex.props(styles.copy)}>
          <p data-only="new-york" {...stylex.props(styles.eyebrow)}>
            A color scheme for the long ride
          </p>
          <p data-only="london" {...stylex.props(styles.eyebrow)}>
            Mind the gap
          </p>
          <h1 data-only="new-york" {...stylex.props(styles.title)}>
            Sink into a warmer screen.
          </h1>
          <h1 data-only="london" {...stylex.props(styles.title, styles.titleLondon)}>
            Stand clear of the closing tabs.
          </h1>
          <p data-only="new-york" {...stylex.props(styles.lede)}>
            Subway Seat is a walnut-brown theme from a 1970s subway car: orange bucket seats,
            wood-grain paneling, cream enamel and a little avocado. Three flavors, {count} ports,
            one palette.
          </p>
          <p data-only="london" {...stylex.props(styles.lede)}>
            London is the same system riding a different network: Corporate Blue turned right down,
            London brick, the yellow off the platform edge, and the standard red kept rare so it
            still means something. Three flavors, {count} ports, the same 26 roles.
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
    letterSpacing: font.labelTracking,
  },
  diagram: { display: "block", marginTop: 40 },
  // Johnston is set tight and upright; the 70s display face wants the opposite.
  titleLondon: {
    maxWidth: "14ch",
    fontVariationSettings: "normal",
    fontWeight: 700,
    lineHeight: 1.02,
    letterSpacing: "-0.012em",
  },
  title: {
    maxWidth: "12ch",
    fontFamily: font.display,
    fontSize: "clamp(48px, 7.4vw, 96px)",
    fontVariationSettings: font.heroSettings,
    fontWeight: font.heroWeight,
    lineHeight: font.heroLeading,
    color: color.textHi,
    letterSpacing: font.heroTracking,
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
    borderRadius: "var(--radius-pill)",
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
