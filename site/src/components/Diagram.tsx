import * as stylex from "@stylexjs/stylex";
import { art } from "@/theme/art.stylex";
import { color } from "@/theme/tokens.stylex";

/**
 * A Beck diagram. Harry Beck threw away geography in 1933 and kept only order
 * and connection: horizontals, verticals, 45° diagonals, even line spacing, a
 * tick at every stop and a ring at every interchange. It is the same instinct
 * as the supergraphic on the New York side — a wall-sized mark made of one
 * repeated rule — arrived at from the other direction.
 *
 * The rules it follows, which is what makes it read as a network rather than
 * as five lines that happen to cross:
 *
 *   · lines run parallel in a trunk at one fixed spacing, then fan out
 *   · every corner is 45°, and every diagonal is a true diagonal
 *   · where lines meet, a ring; where one line stops, a tick
 *   · several platforms under one name are one interchange, tied with a bar
 */
const GAP = 30; // trunk spacing
const TOP = 96; // the first trunk line
const W = 12; // line weight
const X_INT = 168; // the interchange, where the vertical crosses the trunk
const y = (n: number) => TOP + n * GAP;

/** A 45° drop from (x, y) down to `to`, then straight on to the right edge. */
const fan = (x: number, from: number, to: number) =>
  `M -20 ${from} H ${x} L ${x + (to - from)} ${to} H 580`;

// Where each line leaves the right edge. Beck's spacing rule holds after the
// fan too, so no two lines end up close enough to read as one.
const OUT = { red: y(0), yellow: 218, green: 284, denim: 328, orange: 372 };

const LINES: { d: string; stroke: string }[] = [
  // Trunk: three lines in from the left, fanning at different points.
  { d: `M -20 ${y(0)} H 580`, stroke: art.red },
  { d: fan(300, y(1), OUT.yellow), stroke: art.yellow },
  { d: fan(246, y(2), OUT.green), stroke: art.green },
  // A vertical down the left, turning 45° out under the trunk.
  {
    d: `M ${X_INT} -20 V 250 L ${X_INT + (OUT.denim - 250)} ${OUT.denim} H 580`,
    stroke: art.denim,
  },
  // One more in from under the bottom edge, rising to meet the fan.
  { d: `M -20 438 H 118 L ${118 + (438 - OUT.orange)} ${OUT.orange} H 580`, stroke: art.orange },
];

/** Three platforms under one name: a ring on each line, tied with a bar. */
const INTERCHANGE = [y(0), y(1), y(2)];

/** Single-line stops: a tick across the line. */
const STOPS: { x: number; y: number; v?: boolean }[] = [
  { x: 84, y: y(0) },
  { x: 380, y: y(0) },
  { x: 470, y: y(0) },
  { x: 250, y: y(1) },
  { x: 470, y: OUT.yellow },
  { x: 196, y: y(2) },
  { x: 470, y: OUT.green },
  { x: 500, y: OUT.denim },
  { x: 430, y: OUT.orange },
  { x: X_INT, y: 62, v: true },
];

export function Diagram() {
  return (
    <svg viewBox="0 0 540 400" aria-hidden {...stylex.props(styles.svg)}>
      {LINES.map((l) => (
        <path
          key={l.d}
          d={l.d}
          fill="none"
          strokeWidth={W}
          strokeLinecap="butt"
          strokeLinejoin="round"
          style={{ stroke: l.stroke }}
        />
      ))}

      {STOPS.map((s) => (
        <line
          key={`${s.x}-${s.y}`}
          x1={s.v ? s.x - 11 : s.x}
          y1={s.v ? s.y : s.y - 11}
          x2={s.v ? s.x + 11 : s.x}
          y2={s.v ? s.y : s.y + 11}
          strokeWidth={3.5}
          style={{ stroke: color.textHi }}
        />
      ))}

      {/* The tie bar sits under the rings, so they read as one station. */}
      <line
        x1={X_INT}
        y1={INTERCHANGE[0]}
        x2={X_INT}
        y2={INTERCHANGE[INTERCHANGE.length - 1]}
        strokeWidth={5}
        style={{ stroke: color.textHi }}
      />
      {INTERCHANGE.map((cy) => (
        <circle
          key={cy}
          cx={X_INT}
          cy={cy}
          r={8.5}
          strokeWidth={4}
          style={{ stroke: color.textHi, fill: color.base }}
        />
      ))}
    </svg>
  );
}

const styles = stylex.create({
  svg: { width: "100%", height: "auto", overflow: "visible" },
});
