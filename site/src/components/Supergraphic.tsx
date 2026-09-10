import * as stylex from "@stylexjs/stylex";
import { color } from "@/theme/tokens.stylex";

// Five stripes that fall in from the top, bend around one shared centre and
// run off to the right, like the painted supergraphics on 70s walls and vans.
const STRIPES = [color.red, color.orange, color.yellow, color.green, color.text];
const W = 30; // stripe width
const CX = 420; // centre of the bend
const CY = 150;
const R = 60; // innermost radius

function path(i: number) {
  const r = R + i * W;
  return `M ${CX - r} -20 L ${CX - r} ${CY} A ${r} ${r} 0 0 0 ${CX} ${CY + r} L 700 ${CY + r}`;
}

export function Supergraphic() {
  return (
    <svg viewBox="0 0 620 420" aria-hidden {...stylex.props(styles.svg)}>
      {STRIPES.map((stroke, i) => (
        <path
          // biome-ignore lint/suspicious/noArrayIndexKey: fixed stripe order
          key={i}
          d={path(i)}
          fill="none"
          strokeWidth={W + 0.5}
          style={{ stroke }}
        />
      ))}
    </svg>
  );
}

const styles = stylex.create({
  svg: { width: "100%", height: "auto", overflow: "visible" },
});
