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
 * Both marks are inline-grid and sit on the text baseline through
 * `vertical-align`, so the wordmark stays a single line box and lines up with
 * the nav links instead of pushing them around.
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
    </>
  );
}

const SIZE = 26;

const styles = stylex.create({
  bullet: {
    display: "inline-grid",
    placeItems: "center",
    width: SIZE,
    height: SIZE,
    marginRight: 10,
    verticalAlign: "-0.26em",
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
    display: "inline-grid",
    placeItems: "center",
    width: SIZE,
    height: SIZE,
    marginRight: 10,
    verticalAlign: "-0.26em",
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
  // The bar runs past the ring on both sides — that overhang is most of what
  // makes a roundel read as a roundel and not as a disc.
  bar: {
    position: "relative",
    width: "128%",
    height: 5,
    backgroundColor: "var(--sign-mark-alt)",
  },
});
