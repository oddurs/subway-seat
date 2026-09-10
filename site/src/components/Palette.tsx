import * as stylex from "@stylexjs/stylex";
import {
  bestInk,
  type ColorName,
  contrast,
  flavors,
  ground,
  roleNames,
  textRoles,
} from "@/lib/palette";
import { sign } from "@/theme/sign.stylex";
import { color } from "@/theme/tokens.stylex";
import { Swatch, type SwatchLabel } from "./Swatch";

/**
 * Per flavor, the chip's hex and whichever ink reads best on it: the flavor's
 * darkest or lightest, or the station-sign black for the mid-tones in between.
 */
export function labelsFor(role: ColorName): SwatchLabel[] {
  return flavors.map((f) => {
    const hex = f.colors[role];
    const [dark, light] = f.dark
      ? [f.colors.crust, f.colors.textHi]
      : [f.colors.textHi, f.colors.base];
    const deep = contrast(hex, dark) >= 4.5 ? dark : sign.bg;
    return { flavor: f.id, hex, ink: bestInk(hex, deep, light) };
  });
}

/** The ground ramp and the cream ramp, as two joined strips of chips. */
export function Palette() {
  return (
    <div {...stylex.props(styles.stack)}>
      {[ground, textRoles].map((ramp) => (
        <div key={ramp[0]} {...stylex.props(styles.strip)}>
          {ramp.map((role) => (
            <Swatch key={role} fill={color[role]} name={roleNames[role]} labels={labelsFor(role)} />
          ))}
        </div>
      ))}
    </div>
  );
}

const styles = stylex.create({
  stack: { display: "grid", gridTemplateColumns: "minmax(0, 1fr)", gap: 6 },
  strip: {
    display: "flex",
    flexWrap: "wrap",
    gap: 4,
    overflow: "hidden",
    borderRadius: 14,
  },
});
