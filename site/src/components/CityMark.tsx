import * as stylex from "@stylexjs/stylex";
import { font } from "@/theme/type.stylex";

/**
 * The one place a city spends its brand color in the nav. New York gets a route
 * bullet, London a roundel. Both are drawn; CSS shows the active family's.
 *
 * Concentrating the identity here is what lets the band itself stay a quiet
 * dark sign in both cities, instead of a wall of Corporate Blue that fights
 * every page under it.
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

const SIZE = 22;

const styles = stylex.create({
  bullet: {
    display: "grid",
    flexShrink: 0,
    placeItems: "center",
    width: SIZE,
    height: SIZE,
    fontFamily: font.sans,
    fontSize: 13,
    fontWeight: 700,
    lineHeight: 1,
    color: "var(--sign-mark-alt)",
    backgroundColor: "var(--sign-mark)",
    borderRadius: "50%",
  },
  roundel: {
    position: "relative",
    display: "grid",
    flexShrink: 0,
    placeItems: "center",
    width: SIZE,
    height: SIZE,
  },
  ring: {
    position: "absolute",
    inset: 0,
    borderColor: "var(--sign-mark)",
    borderStyle: "solid",
    // The Underground's ring is about a sixth of its diameter.
    borderWidth: 3.5,
    borderRadius: "50%",
  },
  bar: {
    position: "relative",
    width: "100%",
    height: 6,
    backgroundColor: "var(--sign-mark-alt)",
  },
});
