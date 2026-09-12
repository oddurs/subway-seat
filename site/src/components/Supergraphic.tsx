import * as stylex from "@stylexjs/stylex";
import { art } from "@/theme/art.stylex";
import { color } from "@/theme/tokens.stylex";

/**
 * A painted supergraphic: bands fall from the top, bend around one shared
 * centre and run off to the right, past any screen width — the wall-and-van
 * graphics of the 1970s, and the opposite instinct to London's diagram. That
 * one is drawn to inform; this one is drawn to please.
 *
 * Two things give it depth the plain rainbow didn't have. The bands taper from
 * the outside in, so the sweep reads as speed rather than as a set of equal
 * rings; and the innermost band starts at a terminus instead of running off
 * the top, so the whole thing comes from somewhere.
 */
const BANDS = [
  // Inner to outer. Burnt orange sits just off the tightest turn, where the eye
  // lands, because it's the accent the rest of the theme leads with.
  { fill: art.red, width: 19 },
  { fill: art.orange, width: 23 },
  { fill: art.yellow, width: 27 },
  { fill: art.green, width: 31 },
  { fill: color.text, width: 35 },
];

const CX = 430; // centre of the bend
const CY = 190;
const INNER = 44; // inside edge of the tightest band

/** Centre-line radius of each band, walking outwards from INNER. */
const RADII = BANDS.reduce<number[]>((acc, b, i) => {
  const edge = i === 0 ? INNER : acc[i - 1] + BANDS[i - 1].width / 2;
  acc.push(edge + b.width / 2);
  return acc;
}, []);

/** Down the left, a quarter turn, then out to the right forever. */
const path = (r: number, top: number) =>
  `M ${CX - r} ${top} L ${CX - r} ${CY} A ${r} ${r} 0 0 0 ${CX} ${CY + r} L 2600 ${CY + r}`;

export function Supergraphic() {
  return (
    <svg viewBox="0 0 620 450" aria-hidden {...stylex.props(styles.svg)}>
      {/* Outermost first, so every inner band lies over the one behind it. */}
      {[...BANDS].reverse().map((band, i) => {
        const idx = BANDS.length - 1 - i;
        const terminus = idx === 0;
        return (
          <path
            key={band.width}
            d={path(RADII[idx], terminus ? 112 : -20)}
            fill="none"
            strokeWidth={band.width}
            // The innermost band ends in a half-round cap: a line terminus.
            strokeLinecap={terminus ? "round" : "butt"}
            style={{ stroke: band.fill }}
          />
        );
      })}
    </svg>
  );
}

const styles = stylex.create({
  svg: { width: "100%", height: "auto", overflow: "visible" },
});
