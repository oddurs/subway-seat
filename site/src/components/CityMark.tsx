import * as stylex from "@stylexjs/stylex";
import { font } from "@/theme/type.stylex";

/**
 * The one place a city spends its brand colour in the nav: a route bullet in
 * New York, a roundel in London, the Dervaux M in Paris. All three are drawn
 * and CSS shows the active family's, so the lockup is right in the first
 * painted frame and never swaps marks after hydration.
 *
 * Concentrating the identity here is what lets the band itself stay a quiet
 * dark sign in both cities, rather than a wall of colour fighting every page
 * under it.
 *
 * A mark in a lockup is centred against the wordmark, not sat on its baseline —
 * a baseline is for text, and a circle has none. Nor can one be borrowed: an
 * inline box synthesises its baseline from whatever text it happens to contain,
 * so the bullet would take the S's, the metro the M's and the roundel, with no
 * text at all, its bottom edge. Three marks, three different baselines, each
 * moving again with the family's face. The lockup centres instead, and the
 * marks are all one square so the centring is exact.
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

const styles = stylex.create({
  bullet: {
    display: "grid",
    placeItems: "center",
    width: SIZE,
    height: SIZE,
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
