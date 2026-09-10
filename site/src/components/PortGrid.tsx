import * as stylex from "@stylexjs/stylex";
import Link from "next/link";
import { byCategory } from "@/lib/manifest";
import { color } from "@/theme/tokens.stylex";
import { font } from "@/theme/type.stylex";

// Each category runs on its own line colour, like the trunk lines on the map.
const LINE: Record<string, string> = {
  Terminals: color.orange,
  Editors: color.yellow,
  Agents: color.clay,
  "Shell & prompt": color.green,
  "CLI & TUI": color.sage,
  Apps: color.denim,
  Palettes: color.redHi,
};

export function PortGrid() {
  const groups = byCategory();
  return (
    <div {...stylex.props(styles.groups)}>
      {groups.map(({ category, ports }) => (
        <section key={category} {...stylex.props(styles.group)}>
          <h3 {...stylex.props(styles.heading)}>
            <span {...stylex.props(styles.dot, styles.fill(LINE[category] ?? color.orange))} />
            {category}
            <span {...stylex.props(styles.count)}>{ports.length}</span>
          </h3>
          <div {...stylex.props(styles.grid)}>
            {ports.map((port) => (
              <Link key={port.id} href={`/ports/${port.id}`} {...stylex.props(styles.card)}>
                <span {...stylex.props(styles.bullet, styles.fill(LINE[category] ?? color.orange))}>
                  {port.name
                    .replace(/[^A-Za-z0-9]/g, "")
                    .charAt(0)
                    .toUpperCase()}
                </span>
                <span {...stylex.props(styles.name)}>{port.name}</span>
              </Link>
            ))}
          </div>
        </section>
      ))}
    </div>
  );
}

const styles = stylex.create({
  groups: { display: "grid", gridTemplateColumns: "minmax(0, 1fr)", gap: 34 },
  group: { display: "grid", gap: 14 },
  heading: {
    display: "flex",
    gap: 10,
    alignItems: "center",
    fontFamily: font.display,
    fontSize: 24,
    fontVariationSettings: '"SOFT" 100',
    fontWeight: 700,
    color: color.textHi,
  },
  dot: { width: 14, height: 14, borderRadius: "50%" },
  count: { fontFamily: font.sans, fontSize: 14, fontWeight: 400, color: color.overlay1 },
  grid: {
    display: "grid",
    gridTemplateColumns: "repeat(auto-fill, minmax(190px, 1fr))",
    gap: 8,
  },
  card: {
    display: "flex",
    gap: 12,
    alignItems: "center",
    paddingBlock: 10,
    paddingInline: 12,
    color: color.text,
    textDecoration: "none",
    outlineWidth: 2,
    outlineStyle: {
      default: "none",
      ":focus-visible": "solid",
    },
    outlineColor: color.orange,
    outlineOffset: 2,
    backgroundColor: {
      default: color.base,
      ":hover": color.surface0,
    },
    borderColor: {
      default: color.surface0,
      ":hover": color.surface2,
    },
    borderStyle: "solid",
    borderWidth: 1,
    borderRadius: 12,
    transitionDuration: "140ms",
    transitionProperty: "background-color, border-color",
  },
  bullet: {
    display: "grid",
    flexShrink: 0,
    placeItems: "center",
    width: 30,
    height: 30,
    fontFamily: font.sans,
    fontSize: 15,
    fontWeight: 700,
    color: color.crust,
    borderRadius: "50%",
  },
  fill: (bg: string) => ({ backgroundColor: bg }),
  name: { fontSize: 15, fontWeight: 500 },
});
