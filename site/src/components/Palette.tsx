import * as stylex from "@stylexjs/stylex";
import { type ColorName, flavors, ground, roleNames, textRoles } from "@/lib/palette";
import { color } from "@/theme/tokens.stylex";
import { Swatch, type SwatchLabel } from "./Swatch";

/** Relative luminance, to pick ink that reads on a chip. */
function luminance(hex: string) {
  const [r, g, b] = [1, 3, 5].map((i) => {
    const v = Number.parseInt(hex.slice(i, i + 2), 16) / 255;
    return v <= 0.03928 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4;
  });
  return 0.2126 * r + 0.7152 * g + 0.0722 * b;
}

export function labelsFor(role: ColorName): SwatchLabel[] {
  return flavors.map((f) => {
    const hex = f.colors[role];
    return { flavor: f.id, hex, ink: luminance(hex) > 0.3 ? "#2A1D13" : "#F8ECD4" };
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
    display: "grid",
    gridTemplateColumns: "repeat(auto-fit, minmax(112px, 1fr))",
    gap: 4,
    overflow: "hidden",
    borderRadius: 14,
  },
});
