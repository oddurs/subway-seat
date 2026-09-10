import * as stylex from "@stylexjs/stylex";
import { ink } from "@/theme/ink.stylex";
import { font } from "@/theme/type.stylex";

/** An MTA route bullet: a filled circle with one bold letter. */
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
    <span aria-hidden {...stylex.props(styles.bullet, styles[size], styles.bg(bg))}>
      {letter}
    </span>
  );
}

const styles = stylex.create({
  bullet: {
    display: "grid",
    flexShrink: 0,
    placeItems: "center",
    fontFamily: font.sans,
    fontWeight: 700,
    lineHeight: 1,
    color: ink.onAccent,
    borderRadius: "50%",
  },
  sm: { width: 34, height: 34, fontSize: 19 },
  md: { width: 40, height: 40, fontSize: 22 },
  bg: (bg: string) => ({ backgroundColor: bg }),
});
