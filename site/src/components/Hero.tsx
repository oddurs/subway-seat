import * as stylex from "@stylexjs/stylex";
import Link from "next/link";
import { color } from "@/theme/tokens.stylex";
import { font } from "@/theme/type.stylex";
import { Supergraphic } from "./Supergraphic";

export function Hero({ count }: { count: number }) {
  return (
    <section {...stylex.props(styles.hero)}>
      <div {...stylex.props(styles.art)} aria-hidden>
        <Supergraphic />
      </div>
      <div {...stylex.props(styles.copy)}>
        <p {...stylex.props(styles.eyebrow)}>A color scheme for the long ride</p>
        <h1 {...stylex.props(styles.title)}>Sink into a warmer screen.</h1>
        <p {...stylex.props(styles.lede)}>
          Subway Seat is a walnut-brown theme from a 1970s subway car: orange bucket seats,
          wood-grain paneling, cream enamel and a little avocado. Three flavors, {count} apps, one
          palette.
        </p>
        <div {...stylex.props(styles.ctas)}>
          <Link href="#ports" {...stylex.props(styles.cta, styles.primary)}>
            Find your app
          </Link>
          <Link href="/palette" {...stylex.props(styles.cta, styles.secondary)}>
            See the palette
          </Link>
        </div>
      </div>
    </section>
  );
}

const NARROW = "@media (max-width: 860px)";

const styles = stylex.create({
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
    top: -60,
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
      [NARROW]: 0.35,
      default: 1,
    },
  },
  copy: { position: "relative", display: "grid", gap: 22 },
  eyebrow: {
    fontFamily: font.sans,
    fontSize: 13,
    fontWeight: 600,
    color: color.orange,
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
    paddingBlock: 12,
    paddingInline: 24,
    fontSize: 16,
    fontWeight: 700,
    textDecoration: "none",
    outlineWidth: 2,
    outlineStyle: {
      default: "none",
      ":focus-visible": "solid",
    },
    outlineColor: color.yellow,
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
    color: color.crust,
    backgroundColor: {
      default: color.orange,
      ":hover": color.orangeHi,
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
