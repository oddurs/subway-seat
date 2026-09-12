import * as stylex from "@stylexjs/stylex";
import { ink } from "@/theme/ink.stylex";
import { font } from "@/theme/type.stylex";

/**
 * A roundel: a ring with a bar straight through it, name on the bar. London's
 * answer to the MTA route bullet — the same job (one color, one label, read at
 * a glance from across a platform) solved by a different network.
 *
 * The real thing is a red ring and a blue bar. Here the ring takes the accent
 * being named, so the mark identifies the color rather than the Underground.
 */
export function Roundel({
  label,
  color,
  size = "md",
}: {
  label: string;
  color: string;
  size?: "sm" | "md";
}) {
  return (
    <span aria-hidden {...stylex.props(styles.wrap, styles[size])}>
      <span {...stylex.props(styles.ring, styles.ringColor(color))} />
      <span {...stylex.props(styles.bar, styles.barColor(color))}>{label}</span>
    </span>
  );
}

const styles = stylex.create({
  wrap: {
    position: "relative",
    display: "grid",
    flexShrink: 0,
    placeItems: "center",
  },
  sm: { width: 34, height: 34 },
  md: { width: 40, height: 40 },
  ring: {
    position: "absolute",
    inset: 0,
    borderStyle: "solid",
    // The Underground's ring is about a sixth of its diameter.
    borderWidth: "16%",
    borderRadius: "50%",
  },
  ringColor: (c: string) => ({ borderColor: c }),
  bar: {
    position: "relative",
    display: "grid",
    placeItems: "center",
    width: "100%",
    height: "40%",
    fontFamily: font.sans,
    fontSize: "42%",
    fontWeight: 700,
    lineHeight: 1,
    color: ink.onAccent,
    textTransform: "uppercase",
    letterSpacing: font.trackLabel,
  },
  barColor: (c: string) => ({ backgroundColor: c }),
});
