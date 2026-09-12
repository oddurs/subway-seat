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
 * What keeps it off the rack of generic rainbows:
 *
 *   · the taper runs inwards-thick, so the accent the theme leads with is the
 *     widest band and the cream is a keyline rather than the loudest thing here
 *   · a hairline of the page shows between bands, the way paint masked off in
 *     separate passes reads, instead of five colours fused into one mass
 *   · they enter at staggered heights, so the eye gets a fan, not a stack
 *   · the innermost starts at a route bullet — the same mark the palette
 *     section uses to name an accent — so the sweep begins somewhere the rest
 *     of the page recognises
 */
const BANDS = [
  // Inner to outer.
  { fill: art.red, width: 30, top: 156 },
  { fill: art.orange, width: 27, top: 96 },
  { fill: art.yellow, width: 24, top: 50 },
  { fill: art.green, width: 21, top: 14 },
  { fill: color.text, width: 13, top: -20 },
];

const CX = 430; // centre of the bend
const CY = 214;
const INNER = 46; // inside edge of the tightest band
const GAP = 3; // the page showing between two painted bands

/** Centre-line radius of each band, walking outwards from INNER. */
const RADII = BANDS.reduce<number[]>((acc, b, i) => {
  const edge = i === 0 ? INNER : acc[i - 1] + BANDS[i - 1].width / 2 + GAP;
  acc.push(edge + b.width / 2);
  return acc;
}, []);

/** Down the left, a quarter turn, then out to the right forever. */
const path = (r: number, top: number) =>
  `M ${CX - r} ${top} L ${CX - r} ${CY} A ${r} ${r} 0 0 0 ${CX} ${CY + r} L 2600 ${CY + r}`;

const BULLET = { x: CX - RADII[0], y: BANDS[0].top, r: BANDS[0].width / 2 + 6 };

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
      <circle cx={BULLET.x} cy={BULLET.y} r={BULLET.r} style={{ fill: art.red }} />
      <text
        x={BULLET.x}
        y={BULLET.y}
        textAnchor="middle"
        dominantBaseline="central"
        style={{
          fill: color.crust,
          fontFamily: font.sans,
          fontSize: BULLET.r * 1.1,
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
