import * as stylex from "@stylexjs/stylex";
import { ink } from "@/theme/ink.stylex";
import { font } from "@/theme/type.stylex";
import { Roundel } from "./Roundel";

/**
 * The mark that names one accent, in whichever city you're riding: an MTA
 * route bullet in New York, a roundel in London. Both are drawn, and CSS shows
 * the one belonging to the active family — the same way flavor-specific content
 * works everywhere else on the site.
 */
export function Bullet({
  letter,
  bg,
  size = "md",
}: {
  letter: string;
  bg: string;
  size?: "sm" | "md";
}) {
  return (
    <>
      <span
        data-only="new-york"
        aria-hidden
        {...stylex.props(styles.bullet, styles[size], styles.bg(bg))}
      >
        {letter}
      </span>
      <span data-only="london" {...stylex.props(styles.slot)}>
        <Roundel label={letter} color={bg} size={size} />
      </span>
    </>
  );
}

const styles = stylex.create({
  slot: { display: "contents" },
  bullet: {
    display: "grid",
    flexShrink: 0,
    placeItems: "center",
    fontFamily: font.sans,
    fontWeight: 700,
    lineHeight: 1,
    color: ink.onAccent,
    borderRadius: "var(--radius-chip)",
  },
  sm: { width: 34, height: 34, fontSize: 19 },
  md: { width: 40, height: 40, fontSize: 22 },
  bg: (bg: string) => ({ backgroundColor: bg }),
});
