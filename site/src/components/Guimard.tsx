import * as stylex from "@stylexjs/stylex";
import { art } from "@/theme/art.stylex";
import { color } from "@/theme/tokens.stylex";

/**
 * Hector Guimard's ironwork. New York paints a curve to please; London draws a
 * straight line to inform; Paris casts a stem and lets it grow. Same job —
 * a wall-sized mark built from one rule — and a third geometry, which is the
 * whole reason the city earns a family.
 *
 * The rule here is the coup de fouet, the "whiplash": a stem that leaves its
 * root slowly, accelerates through an S, and ends in a bud. Every stalk below
 * is the same curve at a different scale and lean, the way Guimard cast one
 * mould and repeated it down a railing.
 */
type Stalk = { d: string; stroke: string; width: number; bud: [number, number]; r: number };

/** One whiplash: root at (x, y), reaching `h` high and leaning `lean` across. */
function stalk(
  x: number,
  y: number,
  h: number,
  lean: number,
): { d: string; tip: [number, number] } {
  const tipX = x + lean;
  const tipY = y - h;
  return {
    // Slow out of the root, hard through the middle, easing into the bud.
    d: `M ${x} ${y} C ${x - lean * 0.15} ${y - h * 0.38}, ${x + lean * 1.05} ${y - h * 0.5}, ${tipX} ${tipY}`,
    tip: [tipX, tipY],
  };
}

const SPEC: [number, number, number, number, string, number][] = [
  // x, y (root), height, lean, colour, weight
  [300, 470, 430, 150, art.clay, 15],
  [352, 470, 360, 210, art.yellow, 12],
  [402, 470, 300, 250, art.green, 10],
  [452, 470, 244, 272, art.sage, 8],
  [262, 470, 190, -70, art.orange, 9],
];

const STALKS: Stalk[] = SPEC.map(([x, y, h, lean, stroke, width]) => {
  const { d, tip } = stalk(x, y, h, lean);
  return { d, stroke, width, bud: tip, r: width * 0.95 };
});

export function Guimard() {
  return (
    <svg viewBox="0 0 620 470" aria-hidden {...stylex.props(styles.svg)}>
      {STALKS.map((s) => (
        <path
          key={s.d}
          d={s.d}
          fill="none"
          strokeWidth={s.width}
          strokeLinecap="round"
          style={{ stroke: s.stroke }}
        />
      ))}
      {STALKS.map((s) => (
        <g key={`bud-${s.d}`}>
          <circle cx={s.bud[0]} cy={s.bud[1]} r={s.r} style={{ fill: s.stroke }} />
          <circle cx={s.bud[0]} cy={s.bud[1]} r={s.r * 0.38} style={{ fill: color.base }} />
        </g>
      ))}
    </svg>
  );
}

const styles = stylex.create({
  svg: { width: "100%", height: "auto", overflow: "visible" },
});
