import * as stylex from "@stylexjs/stylex";
import { accentRoles, type ColorName, flavors } from "@/lib/palette";
import { color } from "@/theme/tokens.stylex";
import { font } from "@/theme/type.stylex";
import { Bullet } from "./Bullet";
import { RoleName } from "./RoleName";

// Each bullet's letter names the syntax role that accent plays.
export const ROUTES: { letter: string; key: ColorName }[] = [
  { letter: "K", key: "orange" },
  { letter: "F", key: "yellow" },
  { letter: "S", key: "green" },
  { letter: "T", key: "sage" },
  { letter: "N", key: "redHi" },
  { letter: "E", key: "clay" },
  { letter: "L", key: "denim" },
];

export function Routes() {
  return (
    <div {...stylex.props(styles.grid)}>
      {ROUTES.map((r) => (
        <div key={r.letter} {...stylex.props(styles.route)}>
          <Bullet letter={r.letter} bg={color[r.key]} />
          <div>
            <b {...stylex.props(styles.name)}>
              <RoleName role={r.key} />
            </b>{" "}
            {flavors.map((f) => (
              <code key={f.id} data-only={f.id} {...stylex.props(styles.hex)}>
                {f.colors[r.key]}
              </code>
            ))}
            <p {...stylex.props(styles.role)}>{accentRoles[r.key]}</p>
          </div>
        </div>
      ))}
    </div>
  );
}

const styles = stylex.create({
  grid: {
    display: "grid",
    gridTemplateColumns: "repeat(auto-fill, minmax(230px, 1fr))",
    rowGap: 20,
    columnGap: 28,
  },
  route: { display: "flex", gap: 14, alignItems: "flex-start" },
  name: { fontWeight: 600, color: color.textHi },
  hex: { fontFamily: font.mono, fontSize: 12, color: color.overlay2 },
  role: { marginTop: 2, fontSize: 14, color: color.subtext0, textWrap: "pretty" },
});
