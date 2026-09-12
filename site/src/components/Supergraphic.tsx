import * as stylex from "@stylexjs/stylex";
import { art } from "@/theme/art.stylex";
import { color } from "@/theme/tokens.stylex";
import { font } from "@/theme/type.stylex";

/**
 * A painted supergraphic: bands fall from the top, bend around one shared
 * centre and run off to the right, past any screen width — the wall-and-van
 * graphics of the 1970s, and the opposite instinct to London's diagram. That
 * one is drawn to inform; this one is drawn to please.
 *
 * Three things keep it from being a plain rainbow. The bands taper from the
 * outside in, so the sweep reads as speed rather than as a stack of equal
 * rings. They enter at staggered heights, so the eye gets a fan rather than
 * five parallel lines. And the innermost one doesn't run off the top at all:
 * it starts at a route bullet, which is the same mark the palette section uses
 * to name an accent, so the graphic begins somewhere the rest of the page
 * recognises.
 */
const BANDS = [
  // Inner to outer. Burnt orange sits just off the tightest turn, where the eye
  // lands, because it's the accent the rest of the theme leads with.
  { fill: art.red, width: 18, top: 150 },
  { fill: art.orange, width: 22, top: 88 },
  { fill: art.yellow, width: 26, top: 44 },
  { fill: art.green, width: 30, top: 12 },
  { fill: color.text, width: 34, top: -20 },
];

const CX = 430; // centre of the bend
const CY = 214;
const INNER = 42; // inside edge of the tightest band

/** Centre-line radius of each band, walking outwards from INNER. */
const RADII = BANDS.reduce<number[]>((acc, b, i) => {
  const edge = i === 0 ? INNER : acc[i - 1] + BANDS[i - 1].width / 2;
  acc.push(edge + b.width / 2);
  return acc;
}, []);

/** Down the left, a quarter turn, then out to the right forever. */
const path = (r: number, top: number) =>
  `M ${CX - r} ${top} L ${CX - r} ${CY} A ${r} ${r} 0 0 0 ${CX} ${CY + r} L 2600 ${CY + r}`;

const BULLET = { x: CX - RADII[0], y: BANDS[0].top };

export function Supergraphic() {
  return (
    <svg viewBox="0 0 620 470" aria-hidden {...stylex.props(styles.svg)}>
      {/* Outermost first, so every inner band lies over the one behind it. */}
      {[...BANDS].reverse().map((band, i) => {
        const idx = BANDS.length - 1 - i;
        return (
          <path
            key={band.width}
            d={path(RADII[idx], band.top)}
            fill="none"
            strokeWidth={band.width}
            strokeLinecap="butt"
            style={{ stroke: band.fill }}
          />
        );
      })}
      {/* The line starts at a stop, not at the edge of the picture. */}
      <circle cx={BULLET.x} cy={BULLET.y} r={21} style={{ fill: art.red }} />
      <text
        x={BULLET.x}
        y={BULLET.y}
        textAnchor="middle"
        dominantBaseline="central"
        style={{
          fill: color.crust,
          fontFamily: font.sans,
          fontSize: 23,
          fontWeight: 700,
        }}
      >
        S
      </text>
    </svg>
  );
}

const styles = stylex.create({
  svg: { width: "100%", height: "auto", overflow: "visible" },
});
