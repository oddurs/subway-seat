import * as stylex from "@stylexjs/stylex";
import { ink } from "@/theme/ink.stylex";
import { space } from "@/theme/space.stylex";
import { color } from "@/theme/tokens.stylex";
import { font } from "@/theme/type.stylex";
import { Button } from "./Button";
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
            <Button href="/install" variant="primary">
              Get on board
            </Button>
            <Button href="#ports">Find your app</Button>
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
    maxWidth: space.measure,
    // Both cities' copy fits this, so the band under the hero — shag in New
    // York, moquette in London — stays exactly where it is when you switch.
    // A hero that resized would drag the material up and down the page.
    minHeight: {
      [NARROW]: 0,
      default: 600,
    },
    paddingInline: space.gutter,
    paddingTop: {
      [NARROW]: 40,
      default: 72,
    },
    paddingBottom: 40,
    marginInline: "auto",
  },
  art: {
    // A bleed: the graphic runs off the right edge, and fades out on the left
    // instead of stopping at a seam, so it reads as a system passing through
    // the frame rather than a picture sitting in it.
    maskImage: "linear-gradient(to right, transparent 0, rgba(0,0,0,0.35) 9%, #000 26%)",
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
  copy: { position: "relative", display: "grid", gap: space.s5 },
  eyebrow: {
    fontFamily: font.sans,
    fontSize: font.sizeLabel,
    fontWeight: 700,
    color: ink.accent,
    textTransform: "uppercase",
    letterSpacing: font.trackLabel,
  },
  diagram: { display: "block", marginTop: 40 },
  // Cabin sets wider than Fraunces at the same size, so London's headline gets
  // a couple more characters before it wraps. Everything else about how it is
  // set comes from the family's type theme, not from here.
  titleLondon: { maxWidth: "15ch" },
  title: {
    maxWidth: "12ch",
    fontFamily: font.display,
    fontSize: font.sizeHero,
    fontVariationSettings: font.axesHero,
    fontWeight: font.weightHero,
    lineHeight: font.leadHero,
    color: color.textHi,
    letterSpacing: font.trackHero,
    textWrap: "balance",
  },
  lede: {
    maxWidth: "52ch",
    fontSize: font.sizeLede,
    lineHeight: font.leadLede,
    color: color.subtext1,
    textWrap: "pretty",
  },
  ctas: { display: "flex", flexWrap: "wrap", gap: space.s3 },
});
