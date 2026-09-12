import * as stylex from "@stylexjs/stylex";
import Link from "next/link";
import { space } from "@/theme/space.stylex";
import { font } from "@/theme/type.stylex";
import { Lockup } from "./Lockup";
import { CitySwitch } from "./CitySwitch";
import { NavLinks } from "./NavLinks";

/**
 * The station sign. One band, dark in both cities, carrying the wordmark, the
 * links and the one control the nav owns — which city you're riding.
 *
 * Balance here is a matter of one measurement: the mark is 24px, and nothing in
 * the row is allowed to be taller. The links and the switch keep tap padding
 * for the hand but take it back out of the layout with a negative margin, so
 * the row is 24px in every city, on every face, and the band is always the same
 * 66px tall — it doesn't grow a couple of pixels when you switch to London
 * because Cabin has a deeper descender than Helvetica.
 *
 * With one height to centre, everything centres against it, and the band's air
 * is 20 above and 20 below. The platform edge along the bottom, in the city's
 * lead colour, is the exception the padding has to pay for: it sits inside the
 * band, so the bottom takes 22 to leave 20 clear of the rule.
 */
export function Nav() {
  return (
    <header {...stylex.props(styles.band)}>
      <a href="#main" {...stylex.props(styles.skip)}>
        Skip to content
      </a>
      <div {...stylex.props(styles.inner)}>
        <Link href="/" {...stylex.props(styles.mark)}>
          <Lockup />
        </Link>
        <NavLinks />
        <CitySwitch />
      </div>
      <span aria-hidden {...stylex.props(styles.edge)} />
    </header>
  );
}

/** Deceleration curve: leaves quickly, arrives softly, like a train stopping. */
const EASE = "cubic-bezier(0.2, 0, 0, 1)";
const CALM = "@media (prefers-reduced-motion: reduce)";

const styles = stylex.create({
  band: {
    position: "relative",
    zIndex: 2,
    backgroundColor: "var(--sign-bg)",
    transitionDelay: "80ms",
    transitionTimingFunction: EASE,
    // Changing city is a move along a line, not a cut. The band, its edge and
    // its type all cross over, but not together: the platform edge turns first,
    // the type follows, the ground lands last. Staggered like that the swap
    // reads as the bar shifting towards the next city rather than blinking.
    transitionDuration: { [CALM]: "1ms", default: "440ms" },
    transitionProperty: "background-color",
  },
  skip: {
    position: "absolute",
    top: 10,
    left: 10,
    zIndex: 3,
    paddingBlock: 8,
    paddingInline: 14,
    fontFamily: font.sans,
    fontSize: font.sizeSmall,
    fontWeight: 700,
    color: "var(--sign-bg)",
    textDecoration: "none",
    outlineWidth: 2,
    outlineStyle: "solid",
    outlineColor: "var(--sign-ring)",
    outlineOffset: 2,
    backgroundColor: "var(--sign-text)",
    borderRadius: "var(--radius-pill)",
    transform: {
      default: "translateY(-200%)",
      ":focus": "none",
    },
  },
  inner: {
    position: "relative",
    display: "flex",
    flexWrap: "wrap",
    rowGap: 14,
    columnGap: 30,
    alignItems: "center",
    maxWidth: space.measure,
    paddingTop: 20,
    paddingRight: space.gutter,
    paddingBottom: 22,
    paddingLeft: space.gutter,
    marginInline: "auto",
  },
  // A lockup: the mark and the wordmark centred on each other, the pair centred
  // in the band with the links and the switch. Its height is the mark's, which
  // is what sets the band's.
  mark: {
    display: "flex",
    fontFamily: font.sans,
    whiteSpace: "nowrap",
    textDecoration: "none",
    outlineWidth: 2,
    outlineStyle: {
      default: "none",
      ":focus-visible": "solid",
    },
    outlineColor: "var(--sign-ring)",
    outlineOffset: 5,
    borderRadius: "var(--radius-pill)",
    transitionDelay: "40ms",
    transitionTimingFunction: EASE,
    transitionDuration: { [CALM]: "1ms", default: "360ms" },
    transitionProperty: "color",
  },
  // The platform edge, in the city's lead colour.
  edge: {
    position: "absolute",
    right: 0,
    bottom: 0,
    left: 0,
    height: 2,
    backgroundColor: "var(--sign-mark)",
    opacity: 0.9,
    transitionTimingFunction: EASE,
    transitionDuration: { [CALM]: "1ms", default: "260ms" },
    transitionProperty: "background-color",
  },
});
