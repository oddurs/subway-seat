"use client";

import * as stylex from "@stylexjs/stylex";
import { setFlavor } from "@/lib/flavor";
import type { Flavor } from "@/lib/palette";
import { font } from "@/theme/type.stylex";

// Each card is painted in its own flavor's literal colors, whatever flavor the
// page is in, so the three sit side by side like paint chips.
export function FlavorCards({ flavors }: { flavors: Flavor[] }) {
  return (
    <div {...stylex.props(styles.grid)}>
      {flavors.map((f) => {
        const c = f.colors;
        return (
          <button
            key={f.id}
            type="button"
            onClick={() => setFlavor(f.id)}
            {...stylex.props(styles.card, styles.paint(c.base, c.text, c.surface2))}
          >
            <span {...stylex.props(styles.stripe)}>
              {[c.red, c.orange, c.yellow, c.green, c.text].map((s) => (
                <i key={s} {...stylex.props(styles.band, styles.fill(s))} />
              ))}
            </span>
            <span {...stylex.props(styles.name, styles.ink(c.textHi))}>{f.name}</span>
            <span {...stylex.props(styles.blurb, styles.ink(c.subtext0))}>{f.blurb}</span>
            <code {...stylex.props(styles.code)}>
              <span {...stylex.props(styles.ink(c.orange))}>const</span>{" "}
              <span {...stylex.props(styles.ink(c.text))}>seat</span>{" "}
              <span {...stylex.props(styles.ink(c.overlay2))}>=</span>{" "}
              <span {...stylex.props(styles.ink(c.yellow))}>find</span>
              <span {...stylex.props(styles.ink(c.overlay2))}>(</span>
              <span {...stylex.props(styles.ink(c.green))}>&quot;window&quot;</span>
              <span {...stylex.props(styles.ink(c.overlay2))}>);</span>
            </code>
            <span {...stylex.props(styles.chips)}>
              {[
                c.crust,
                c.mantle,
                c.surface0,
                c.surface2,
                c.overlay1,
                c.subtext1,
                c.sage,
                c.clay,
              ].map((s) => (
                <i key={s} {...stylex.props(styles.chip, styles.fill(s))} />
              ))}
            </span>
          </button>
        );
      })}
    </div>
  );
}

const styles = stylex.create({
  grid: {
    display: "grid",
    gridTemplateColumns: "repeat(auto-fit, minmax(260px, 1fr))",
    gap: 18,
  },
  card: {
    display: "grid",
    gap: 12,
    padding: 20,
    paddingTop: 0,
    overflow: "hidden",
    textAlign: "left",
    cursor: "pointer",
    outlineWidth: 2,
    outlineStyle: {
      default: "none",
      ":focus-visible": "solid",
    },
    outlineColor: "#EC7F31",
    outlineOffset: 3,
    borderStyle: "solid",
    borderWidth: 1,
    borderRadius: 18,
    boxShadow: "0 14px 34px var(--ss-shadow-soft)",
    transform: {
      default: null,
      ":hover": "translateY(-3px) rotate(-0.4deg)",
    },
    transitionDuration: "220ms",
    transitionProperty: "transform",
  },
  paint: (bg: string, fg: string, edge: string) => ({
    color: fg,
    backgroundColor: bg,
    borderColor: edge,
  }),
  stripe: { display: "flex", height: 10, marginInline: -20, marginBottom: 6 },
  band: { flexGrow: 1 },
  fill: (bg: string) => ({ backgroundColor: bg }),
  ink: (fg: string) => ({ color: fg }),
  name: {
    fontFamily: font.display,
    fontSize: 26,
    fontVariationSettings: '"SOFT" 100, "WONK" 1',
    fontWeight: 700,
    lineHeight: 1.1,
  },
  blurb: { fontSize: 14.5, lineHeight: 1.5 },
  code: { fontFamily: font.mono, fontSize: 13 },
  chips: { display: "flex", gap: 5 },
  chip: { width: 22, height: 22, borderRadius: 6 },
});
