"use client";

import * as stylex from "@stylexjs/stylex";
import { useSyncExternalStore } from "react";
import { currentFlavor, setFlavor, subscribeFlavor } from "@/lib/flavor";
import { type Flavor, shortName } from "@/lib/palette";
import { font } from "@/theme/type.stylex";

// Each card is painted in its own flavor's literal colors, whatever flavor the
// page is in, so the three sit side by side like paint chips.
export function FlavorCards({ flavors }: { flavors: Flavor[] }) {
  const active = useSyncExternalStore(subscribeFlavor, currentFlavor, () => null);
  return (
    <div {...stylex.props(styles.grid)}>
      {flavors.map((f) => {
        const c = f.colors;
        const on = active === f.id;
        return (
          <button
            key={f.id}
            type="button"
            onClick={() => setFlavor(f.id)}
            aria-pressed={active === null ? undefined : on}
            aria-label={`Use ${shortName(f.id)}`}
            {...stylex.props(
              styles.card,
              styles.paint(c.base, c.text, c.surface2),
              on && styles.on(c.orange),
            )}
          >
            <span {...stylex.props(styles.stripe)}>
              {[c.red, c.orange, c.yellow, c.green, c.text].map((s) => (
                <i key={s} {...stylex.props(styles.band, styles.fill(s))} />
              ))}
            </span>
            <span {...stylex.props(styles.head)}>
              <span {...stylex.props(styles.name, styles.ink(c.textHi))}>{shortName(f.id)}</span>
              <span
                {...stylex.props(
                  styles.badge,
                  styles.badgePaint(c.orange, f.dark ? c.crust : c.base),
                  on && styles.badgeOn,
                )}
              >
                Riding
              </span>
            </span>
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
    gridTemplateColumns: "repeat(auto-fit, minmax(220px, 1fr))",
    gap: 18,
  },
  card: {
    display: "grid",
    gap: 12,
    alignContent: "start",
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
    borderRadius: "var(--radius-card)",
    boxShadow: "0 14px 34px var(--ss-shadow-soft)",
    transform: {
      default: null,
      ":hover": "translateY(-3px) rotate(-0.4deg)",
    },
    transitionDuration: "220ms",
    transitionProperty: "transform, box-shadow",
  },
  paint: (bg: string, fg: string, edge: string) => ({
    color: fg,
    backgroundColor: bg,
    borderColor: edge,
  }),
  on: (ring: string) => ({
    borderColor: ring,
    boxShadow: `0 0 0 2px ${ring}, 0 14px 34px var(--ss-shadow-soft)`,
  }),
  stripe: { display: "flex", height: 10, marginInline: -20, marginBottom: 6 },
  band: { flexGrow: 1 },
  fill: (bg: string) => ({ backgroundColor: bg }),
  ink: (fg: string) => ({ color: fg }),
  head: { display: "flex", gap: 10, alignItems: "center", justifyContent: "space-between" },
  name: {
    fontFamily: font.display,
    fontSize: 28,
    fontVariationSettings: '"SOFT" 100, "WONK" 1',
    fontWeight: 700,
    lineHeight: 1.1,
  },
  badge: {
    paddingBlock: 2,
    paddingInline: 9,
    fontSize: 11,
    fontWeight: 700,
    textTransform: "uppercase",
    letterSpacing: "0.08em",
    borderRadius: "var(--radius-card)",
    opacity: 0,
    transitionDuration: "200ms",
    transitionProperty: "opacity",
  },
  badgePaint: (bg: string, fg: string) => ({ color: fg, backgroundColor: bg }),
  badgeOn: { opacity: 1 },
  blurb: { fontSize: 14.5, lineHeight: 1.5, textWrap: "pretty" },
  code: { fontFamily: font.mono, fontSize: 13 },
  chips: { display: "flex", gap: 5 },
  chip: { width: 22, height: 22, borderRadius: "var(--radius-chip)" },
});
