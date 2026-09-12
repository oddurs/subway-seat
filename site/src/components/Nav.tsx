import * as stylex from "@stylexjs/stylex";
import Link from "next/link";
import { space } from "@/theme/space.stylex";
import { font } from "@/theme/type.stylex";
import { CityMark } from "./CityMark";
import { CitySwitch } from "./CitySwitch";
import { NavLinks } from "./NavLinks";

/**
 * The station sign. One band, dark in both cities, carrying the wordmark, the
 * links and the one control the nav owns — which city you're riding.
 *
 * The whole row sits on a single baseline: the wordmark is one line box with
 * the mark set inline against it, the links and the switch have flat line
 * heights, and nothing is centred against anything else. The only rule is the
 * platform edge along the bottom, in the city's lead colour, which is also
 * what the closing band opens with.
 */
export function Nav() {
  return (
    <header {...stylex.props(styles.band)}>
      <a href="#main" {...stylex.props(styles.skip)}>
        Skip to content
      </a>
      <div {...stylex.props(styles.inner)}>
        <Link href="/" {...stylex.props(styles.mark)}>
          <CityMark />
          <span>Subway Seat</span>
        </Link>
        <NavLinks />
        <CitySwitch />
      </div>
      <span aria-hidden {...stylex.props(styles.edge)} />
    </header>
  );
}

const styles = stylex.create({
  band: {
    position: "relative",
    zIndex: 2,
    backgroundColor: "var(--sign-bg)",
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
    display: "flex",
    flexWrap: "wrap",
    rowGap: 14,
    columnGap: 30,
    alignItems: "center",
    maxWidth: space.measure,
    paddingInline: space.gutter,
    paddingBlock: 20,
    marginInline: "auto",
  },
  // A lockup: the mark centred on the wordmark's cap height, the pair centred
  // in the band with the links and the switch.
  mark: {
    display: "flex",
    gap: 11,
    alignItems: "center",
    fontFamily: font.sans,
    fontSize: font.sizeMark,
    fontWeight: 700,
    lineHeight: font.leadFlat,
    color: "var(--sign-text)",
    letterSpacing: font.trackMark,
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
  },
});
