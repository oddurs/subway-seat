import * as stylex from "@stylexjs/stylex";
import type { Metadata } from "next";
import { Footer } from "@/components/Footer";
import { Nav } from "@/components/Nav";
import { Section } from "@/components/Section";
import { accentRoles, accents, flavors, ground, roleNames, textRoles } from "@/lib/palette";
import { color } from "@/theme/tokens.stylex";
import { font } from "@/theme/type.stylex";

export const metadata: Metadata = {
  title: "Palette",
  description:
    "Every Subway Seat colour in all three flavors, with hex, RGB and what each one is for.",
};

const rgb = (hex: string) =>
  [1, 3, 5].map((i) => Number.parseInt(hex.slice(i, i + 2), 16)).join(" ");

const GROUPS = [
  { title: "Ground", roles: ground },
  { title: "Text", roles: textRoles },
  { title: "Accents", roles: accents },
];

export default function PalettePage() {
  return (
    <>
      <Nav />
      <main {...stylex.props(styles.main)}>
        <Section
          label="The palette"
          title="Twenty-six colours, three flavors."
          intro="Every port is written against these roles, not raw hex, so each flavor fills the same slots. Rows show all three flavors side by side; the swatch on the left follows the one you've picked."
        >
          {GROUPS.map((group) => (
            <div key={group.title} {...stylex.props(styles.tableWrap)}>
              <table {...stylex.props(styles.table)}>
                <caption {...stylex.props(styles.caption)}>{group.title}</caption>
                <thead>
                  <tr>
                    <th {...stylex.props(styles.th)} />
                    <th {...stylex.props(styles.th)}>Role</th>
                    {flavors.map((f) => (
                      <th key={f.id} {...stylex.props(styles.th)}>
                        {f.name.replace("Subway Seat", "").trim() || "Walnut"}
                      </th>
                    ))}
                    <th {...stylex.props(styles.th)}>Used for</th>
                  </tr>
                </thead>
                <tbody>
                  {group.roles.map((role) => (
                    <tr key={role}>
                      <td {...stylex.props(styles.td)}>
                        <span {...stylex.props(styles.chip, styles.fill(color[role]))} />
                      </td>
                      <td {...stylex.props(styles.td)}>
                        <b {...stylex.props(styles.name)}>{roleNames[role] ?? role}</b>
                        <code {...stylex.props(styles.role)}>{role}</code>
                      </td>
                      {flavors.map((f) => (
                        <td key={f.id} {...stylex.props(styles.td)}>
                          <span {...stylex.props(styles.mini, styles.fill(f.colors[role]))} />
                          <code {...stylex.props(styles.hex)}>{f.colors[role]}</code>
                          <code {...stylex.props(styles.rgb)}>{rgb(f.colors[role])}</code>
                        </td>
                      ))}
                      <td {...stylex.props(styles.td, styles.use)}>{accentRoles[role] ?? ""}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          ))}
        </Section>
      </main>
      <Footer />
    </>
  );
}

const styles = stylex.create({
  main: { maxWidth: 1200, paddingInline: 24, marginInline: "auto" },
  tableWrap: {
    overflowX: "auto",
    backgroundColor: color.base,
    borderColor: color.surface0,
    borderStyle: "solid",
    borderWidth: 1,
    borderRadius: 16,
  },
  table: { width: "100%", minWidth: 760, fontSize: 14, borderCollapse: "collapse" },
  caption: {
    paddingInline: 18,
    paddingTop: 16,
    fontFamily: font.display,
    fontSize: 22,
    fontVariationSettings: '"SOFT" 100',
    fontWeight: 700,
    color: color.textHi,
    textAlign: "left",
  },
  th: {
    paddingBlock: 10,
    paddingInline: 12,
    fontSize: 12,
    fontWeight: 600,
    color: color.overlay1,
    textAlign: "left",
    textTransform: "uppercase",
    letterSpacing: "0.08em",
  },
  td: {
    paddingBlock: 10,
    paddingInline: 12,
    verticalAlign: "middle",
    borderTopColor: color.surface0,
    borderTopStyle: "solid",
    borderTopWidth: 1,
  },
  chip: { display: "block", width: 44, height: 44, borderRadius: 12 },
  mini: {
    display: "inline-block",
    width: 14,
    height: 14,
    marginRight: 8,
    verticalAlign: "-2px",
    borderColor: "rgba(0,0,0,0.15)",
    borderStyle: "solid",
    borderWidth: 1,
    borderRadius: 4,
  },
  fill: (bg: string) => ({ backgroundColor: bg }),
  name: { display: "block", color: color.textHi },
  role: { fontFamily: font.mono, fontSize: 12, color: color.overlay1 },
  hex: { fontFamily: font.mono, fontSize: 13, color: color.text },
  rgb: {
    display: "block",
    marginLeft: 22,
    fontFamily: font.mono,
    fontSize: 11,
    color: color.overlay1,
  },
  use: { color: color.subtext0 },
});
