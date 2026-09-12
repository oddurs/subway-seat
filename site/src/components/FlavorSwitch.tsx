"use client";

import * as stylex from "@stylexjs/stylex";
import { useSyncExternalStore } from "react";
import { currentFamily, currentFlavor, setFamily, setFlavor, subscribeFlavor } from "@/lib/flavor";
import {
  families,
  type FamilyId,
  type FlavorId,
  flavorById,
  flavorsOf,
  shortName,
} from "@/lib/palette";
import { font } from "@/theme/type.stylex";

/**
 * Two rows of one control: the city, then the flavor within it. Each mark is
 * painted in the colors it switches to — a route bullet for New York, a roundel
 * bar for London — so the control is a specimen of the thing it selects.
 */
export function FlavorSwitch() {
  const active = useSyncExternalStore(subscribeFlavor, currentFlavor, () => null);
  const city = useSyncExternalStore(subscribeFlavor, currentFamily, () => null);
  const shown = (city ?? "new-york") as FamilyId;

  return (
    <div {...stylex.props(styles.wrap)}>
      <div role="group" aria-label="City" {...stylex.props(styles.group)}>
        {families.map((fam) => {
          const on = city === fam.id;
          const swatch = flavorById[fam.default as FlavorId].colors;
          return (
            <button
              key={fam.id}
              type="button"
              aria-pressed={city === null ? undefined : on}
              onClick={() => setFamily(fam.id)}
              {...stylex.props(styles.city, on && styles.cityOn)}
              style={{ backgroundColor: swatch.base, color: swatch.textHi }}
            >
              <span
                aria-hidden
                {...stylex.props(styles.tick)}
                style={{ backgroundColor: fam.id === "london" ? swatch.red : swatch.orange }}
              />
              {fam.name}
            </button>
          );
        })}
      </div>
      <div role="group" aria-label="Flavor" {...stylex.props(styles.group)}>
        {flavorsOf(shown).map((f) => {
          const on = active === f.id;
          const accent = f.family === "london" ? f.colors.red : f.colors.yellow;
          return (
            <button
              key={f.id}
              type="button"
              aria-pressed={active === null ? undefined : on}
              aria-label={shortName(f.id)}
              title={shortName(f.id)}
              onClick={() => setFlavor(f.id)}
              {...stylex.props(
                styles.bullet,
                f.family === "london" && styles.square,
                on && styles.on,
              )}
              style={{
                backgroundColor: f.colors.base,
                color: f.family === "london" ? f.colors.textHi : accent,
              }}
            >
              {shortName(f.id).charAt(0)}
            </button>
          );
        })}
      </div>
    </div>
  );
}

const styles = stylex.create({
  wrap: { display: "flex", flexWrap: "wrap", gap: 8, alignItems: "center" },
  group: { display: "flex", gap: 6 },
  city: {
    display: "flex",
    gap: 7,
    alignItems: "center",
    paddingBlock: 6,
    paddingInline: 10,
    fontFamily: font.sans,
    fontSize: 12,
    fontWeight: 700,
    letterSpacing: "0.04em",
    cursor: "pointer",
    outlineWidth: 2,
    outlineStyle: { default: "none", ":focus-visible": "solid" },
    outlineColor: "var(--sign-ring)",
    outlineOffset: 2,
    borderColor: "rgba(255,255,255,0.28)",
    borderStyle: "solid",
    borderWidth: 1,
    borderRadius: 2,
    opacity: { default: 0.62, ":hover": 1 },
  },
  cityOn: { borderColor: "var(--sign-text)", opacity: 1 },
  tick: { width: 10, height: 10, borderRadius: 2 },
  bullet: {
    display: "grid",
    placeItems: "center",
    width: 32,
    height: 32,
    padding: 0,
    fontFamily: font.sans,
    fontSize: 15,
    fontWeight: 700,
    lineHeight: 1,
    cursor: "pointer",
    outlineWidth: 2,
    outlineStyle: { default: "none", ":focus-visible": "solid" },
    outlineColor: "var(--sign-ring)",
    outlineOffset: 2,
    borderColor: "rgba(255,255,255,0.35)",
    borderStyle: "solid",
    borderWidth: 1,
    borderRadius: "50%",
    transform: { default: null, ":hover": "translateY(-1px)" },
    transitionDuration: "160ms",
    transitionProperty: "transform, box-shadow, border-radius",
  },
  // London's signage is set in rectangles, not bullets.
  square: { borderRadius: 2 },
  on: {
    borderColor: "var(--sign-text)",
    boxShadow: "0 0 0 3px var(--sign-ring)",
  },
});
