import * as stylex from "@stylexjs/stylex";
import { color } from "@/theme/tokens.stylex";

/**
 * A Beck diagram. Harry Beck's 1933 map threw away geography and kept only
 * order and connection: horizontals, verticals, 45° diagonals, even spacing,
 * and a ring at every interchange. It's the same instinct as the supergraphic
 * on the New York side — a wall-sized mark made of one repeated rule — reached
 * from the opposite direction. The supergraphic is a curve painted to please;
 * this is a straight line drawn to inform, and both end up as pure geometry.
 */
const LINES: { d: string; stroke: string }[] = [
  { d: "M -20 96 L 150 96 L 246 192 L 560 192", stroke: color.red },
  { d: "M -20 148 L 190 148 L 286 244 L 560 244", stroke: color.yellow },
  { d: "M 60 -20 L 60 200 L 148 288 L 560 288", stroke: color.denim },
  { d: "M -20 336 L 236 336 L 332 240 L 560 240", stroke: color.green },
  { d: "M 112 -20 L 112 156 L 300 344 L 560 344", stroke: color.orange },
];

// Interchanges sit where lines meet; plain stops are ticks on one line.
const INTERCHANGES: [number, number][] = [
  [150, 96],
  [286, 244],
  [148, 288],
];
const STOPS: [number, number, number, number][] = [
  [100, 96, 100, 74],
  [200, 192, 200, 170],
  [340, 192, 340, 170],
  [240, 288, 240, 310],
  [400, 288, 400, 310],
];

export function Diagram() {
  return (
    <svg viewBox="0 0 520 400" aria-hidden {...stylex.props(styles.svg)}>
      {LINES.map((l) => (
        <path
          key={l.d}
          d={l.d}
          fill="none"
          strokeWidth={13}
          strokeLinecap="butt"
          strokeLinejoin="round"
          style={{ stroke: l.stroke }}
        />
      ))}
      {STOPS.map(([x1, y1, x2, y2]) => (
        <line
          key={`${x1}-${y1}`}
          x1={x1}
          y1={y1}
          x2={x2}
          y2={y2}
          strokeWidth={4}
          style={{ stroke: color.textHi }}
        />
      ))}
      {INTERCHANGES.map(([cx, cy]) => (
        <circle
          key={`${cx}-${cy}`}
          cx={cx}
          cy={cy}
          r={9.5}
          strokeWidth={4.5}
          style={{ stroke: color.textHi, fill: color.base }}
        />
      ))}
    </svg>
  );
}

const styles = stylex.create({
  svg: { width: "100%", height: "auto", overflow: "visible" },
});
