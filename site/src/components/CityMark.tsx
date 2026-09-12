import * as stylex from "@stylexjs/stylex";
import { font } from "@/theme/type.stylex";

/**
 * The one place a city spends its brand colour in the nav: a route bullet in
 * New York, a roundel in London. Both are drawn; CSS shows the active family's.
 *
 * Concentrating the identity here is what lets the band itself stay a quiet
 * dark sign in both cities, rather than a wall of colour fighting every page
 * under it.
 *
 * A mark in a lockup is centred on the wordmark's cap height, not sat on its
 * baseline — a baseline is for text, and a circle has none. The nudge below is
 * the difference between the em box's centre, which is what flexbox centres on,
 * and the cap centre, which is what the eye reads.
 */
export function CityMark() {
  return (
    <>
      <span data-only="new-york" aria-hidden {...stylex.props(styles.bullet)}>
        S
      </span>
      <span data-only="london" aria-hidden {...stylex.props(styles.roundel)}>
        <span {...stylex.props(styles.ring)} />
        <span {...stylex.props(styles.bar)} />
      </span>
      <span data-only="paris" aria-hidden {...stylex.props(styles.metro)}>
        <span {...stylex.props(styles.ring)} />
        <span {...stylex.props(styles.letter)}>M</span>
      </span>
    </>
  );
}

const SIZE = 24;
/** Em-box centre sits a touch below cap centre; lift the mark to match. */
const LIFT = 2;

const styles = stylex.create({
  bullet: {
    display: "grid",
    placeItems: "center",
    width: SIZE,
    height: SIZE,
    marginBottom: LIFT,
    fontFamily: font.sans,
    fontSize: 14,
    fontWeight: 700,
    lineHeight: 1,
    color: "var(--sign-mark-alt)",
    backgroundColor: "var(--sign-mark)",
    borderRadius: "50%",
  },
  roundel: {
    position: "relative",
    display: "grid",
    placeItems: "center",
    width: SIZE,
    height: SIZE,
    marginBottom: LIFT,
  },
  ring: {
    position: "absolute",
    inset: 0,
    borderColor: "var(--sign-mark)",
    borderStyle: "solid",
    // The Underground's ring is about a seventh of its diameter.
    borderWidth: 3.5,
    borderRadius: "50%",
  },
  // Paris signs its entrances with an M inside a ring — the Dervaux standard,
  // the one that replaced most of Guimard's ironwork.
  metro: {
    position: "relative",
    display: "grid",
    placeItems: "center",
    width: SIZE,
    height: SIZE,
    marginBottom: LIFT,
  },
  letter: {
    position: "relative",
    fontFamily: font.sans,
    fontSize: 12,
    fontWeight: 600,
    lineHeight: 1,
    color: "var(--sign-mark)",
  },
  // The bar runs past the ring on both sides — that overhang is most of what
  // makes a roundel read as a roundel and not as a disc.
  bar: {
    position: "relative",
    width: "128%",
    height: 5,
    backgroundColor: "var(--sign-mark-alt)",
  },
});
