"use client";

import * as stylex from "@stylexjs/stylex";
import { useSyncExternalStore } from "react";
import { currentFamily, currentFlavor, setFlavor, subscribeFlavor } from "@/lib/flavor";
import { type FamilyId, flavorsOf, shortName } from "@/lib/palette";
import { ink } from "@/theme/ink.stylex";
import { color } from "@/theme/tokens.stylex";
import { font } from "@/theme/type.stylex";

/**
 * Which flavor of the city you're in. It lives down here rather than in the
 * nav: the city is the choice worth putting in front of someone on every page,
 * and the flavor is a preference you set once. The cards in "Pick a seat" set
 * it too, in colour and at size.
 */
export function FlavorPicker() {
  const active = useSyncExternalStore(subscribeFlavor, currentFlavor, () => null);
  const city = useSyncExternalStore(subscribeFlavor, currentFamily, () => null);

  return (
    <div {...stylex.props(styles.row)}>
      <span {...stylex.props(styles.label)}>Riding</span>
      <div role="group" aria-label="Flavor" {...stylex.props(styles.group)}>
        {flavorsOf((city ?? "new-york") as FamilyId).map((f) => {
          const on = active === f.id;
          return (
            <button
              key={f.id}
              type="button"
              aria-pressed={active === null ? undefined : on}
              onClick={() => setFlavor(f.id)}
              {...stylex.props(styles.item, on && styles.on)}
            >
              <span
                aria-hidden
                {...stylex.props(styles.swatch)}
                style={{ backgroundColor: f.colors.base, borderColor: f.colors.surface2 }}
              />
              {shortName(f.id)}
            </button>
          );
        })}
      </div>
    </div>
  );
}

const styles = stylex.create({
  row: { display: "flex", flexWrap: "wrap", gap: 12, alignItems: "center" },
  label: {
    fontSize: 11,
    fontWeight: 700,
    color: color.overlay1,
    textTransform: "uppercase",
    letterSpacing: "0.16em",
  },
  group: { display: "flex", flexWrap: "wrap", gap: 6 },
  item: {
    display: "flex",
    gap: 8,
    alignItems: "center",
    paddingBlock: 6,
    paddingInline: 10,
    fontFamily: font.sans,
    fontSize: 13.5,
    fontWeight: 600,
    color: { default: color.subtext0, ":hover": color.textHi },
    cursor: "pointer",
    outlineWidth: 2,
    outlineStyle: { default: "none", ":focus-visible": "solid" },
    outlineColor: ink.accent,
    outlineOffset: 2,
    backgroundColor: "transparent",
    borderColor: { default: "transparent", ":hover": color.surface2 },
    borderStyle: "solid",
    borderWidth: 1,
    borderRadius: "var(--radius-pill)",
    transitionDuration: "160ms",
    transitionProperty: "color, border-color",
  },
  on: { color: color.textHi, borderColor: ink.accent },
  swatch: {
    width: 14,
    height: 14,
    borderStyle: "solid",
    borderWidth: 1,
    borderRadius: "var(--radius-chip)",
  },
});
