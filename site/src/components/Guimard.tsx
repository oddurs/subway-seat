import * as stylex from "@stylexjs/stylex";
import { art } from "@/theme/art.stylex";
import { color } from "@/theme/tokens.stylex";

/**
 * Hector Guimard's ironwork. New York paints a curve to please; London draws a
 * straight line to inform; Paris casts a stem and lets it grow. Same job — a
 * wall-sized mark built from one repeated rule — and a third geometry, which is
 * most of why the city earns a family.
 *
 * The rule is the coup de fouet, the whiplash: a stem that leaves its root
 * thick, swells through the bend and tapers into a bud. That varying width is
 * the whole character of cast iron, and it can't be had from a stroke — a
 * stroke is one width from end to end, which is why a drawing made of them
 * reads as wire. So every stem here is a closed outline: the centre line is a
 * cubic, sampled along its length, and each sample is pushed out along its own
 * normal by half the width the stem has at that point.
 */

type Pt = [number, number];

const bezier = (a: Pt, b: Pt, c: Pt, d: Pt, t: number): Pt => {
  const u = 1 - t;
  return [
    u * u * u * a[0] + 3 * u * u * t * b[0] + 3 * u * t * t * c[0] + t * t * t * d[0],
    u * u * u * a[1] + 3 * u * u * t * b[1] + 3 * u * t * t * c[1] + t * t * t * d[1],
  ];
};

/** Unit normal of the curve at t — the direction a sample gets pushed out. */
function normal(a: Pt, b: Pt, c: Pt, d: Pt, t: number): Pt {
  const u = 1 - t;
  const dx = 3 * u * u * (b[0] - a[0]) + 6 * u * t * (c[0] - b[0]) + 3 * t * t * (d[0] - c[0]);
  const dy = 3 * u * u * (b[1] - a[1]) + 6 * u * t * (c[1] - b[1]) + 3 * t * t * (d[1] - c[1]);
  const len = Math.hypot(dx, dy) || 1;
  return [-dy / len, dx / len];
}

/**
 * Width along the stem: thick at the root, a swell through the first third
 * where a casting is strongest, then a long taper into the bud.
 */
const widthAt = (t: number, root: number, tip: number) =>
  (tip + (root - tip) * (1 - t) ** 1.45) * (1 + 0.16 * Math.sin(Math.PI * t ** 0.75));

/** One stem, as a closed outline: out along one side, back along the other. */
function stem(a: Pt, b: Pt, c: Pt, d: Pt, root: number, tip: number, steps = 56) {
  const left: string[] = [];
  const right: string[] = [];
  for (let i = 0; i <= steps; i++) {
    const t = i / steps;
    const [x, y] = bezier(a, b, c, d, t);
    const [nx, ny] = normal(a, b, c, d, t);
    const w = widthAt(t, root, tip) / 2;
    left.push(`${(x + nx * w).toFixed(1)} ${(y + ny * w).toFixed(1)}`);
    right.push(`${(x - nx * w).toFixed(1)} ${(y - ny * w).toFixed(1)}`);
  }
  right.reverse();
  return `M ${left.join(" L ")} L ${right.join(" L ")} Z`;
}

// Every stem springs from the same root cluster at the foot, the way one cast
// panel of railing does, and two of them cross on the way up.
const ROOT: Pt = [372, 500];

const SPEC: { to: Pt; c1: Pt; c2: Pt; root: number; tip: number; fill: string }[] = [
  { to: [300, 40], c1: [300, 380], c2: [430, 190], root: 26, tip: 7, fill: art.yellow },
  { to: [468, 66], c1: [400, 372], c2: [300, 176], root: 22, tip: 6, fill: art.orange },
  { to: [560, 210], c1: [452, 420], c2: [420, 236], root: 17, tip: 5, fill: art.green },
  { to: [214, 214], c1: [346, 416], c2: [206, 340], root: 14, tip: 4.5, fill: art.sage },
  { to: [596, 372], c1: [470, 486], c2: [500, 404], root: 11, tip: 4, fill: art.denim },
];

const STEMS = SPEC.map((s) => ({
  d: stem(ROOT, s.c1, s.c2, s.to, s.root, s.tip),
  bud: s.to,
  r: s.tip * 1.9,
  fill: s.fill,
}));

export function Guimard() {
  return (
    <svg viewBox="0 0 620 470" aria-hidden {...stylex.props(styles.svg)}>
      {/* Thickest last, so the heavy stems sit over the light ones at the root. */}
      {[...STEMS].reverse().map((s) => (
        <path key={s.d} d={s.d} style={{ fill: s.fill }} />
      ))}
      {STEMS.map((s) => (
        <g key={`bud-${s.d}`}>
          <circle cx={s.bud[0]} cy={s.bud[1]} r={s.r} style={{ fill: s.fill }} />
          <circle cx={s.bud[0]} cy={s.bud[1]} r={s.r * 0.36} style={{ fill: color.base }} />
        </g>
      ))}
    </svg>
  );
}

const styles = stylex.create({
  svg: { width: "100%", height: "auto", overflow: "visible" },
});
