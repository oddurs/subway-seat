"use client";

import * as stylex from "@stylexjs/stylex";
import { useSyncExternalStore } from "react";
import { currentFlavor, setFlavor, subscribeFlavor } from "@/lib/flavor";
import { type FlavorId, flavorById, shortName } from "@/lib/palette";
import { color } from "@/theme/tokens.stylex";
import { font } from "@/theme/type.stylex";

// Each bullet is painted in its own flavor: its ground, and one of its accents.
const OPTIONS = (
  [
    ["walnut", "yellow"],
    ["tunnel", "orange"],
    ["enamel", "orange"],
  ] as const
).map(([id, accent]) => ({
  id: id as FlavorId,
  letter: shortName(id).charAt(0),
  label: shortName(id),
  swatch: flavorById[id].colors.base,
  ink: flavorById[id].colors[accent],
}));

/** Three route bullets that change the flavor of the whole site. */
export function FlavorSwitch() {
  const active = useSyncExternalStore(subscribeFlavor, currentFlavor, () => null);

  return (
    <div role="group" aria-label="Flavor" {...stylex.props(styles.group)}>
      {OPTIONS.map((o) => {
        const on = active === o.id;
        return (
          <button
            key={o.id}
            type="button"
            aria-pressed={active === null ? undefined : on}
            aria-label={o.label}
            title={o.label}
            onClick={() => setFlavor(o.id)}
            {...stylex.props(styles.bullet, styles.fill(o.swatch, o.ink), on && styles.on)}
          >
            {o.letter}
          </button>
        );
      })}
    </div>
  );
}

const styles = stylex.create({
  group: { display: "flex", gap: 6 },
  bullet: {
    display: "grid",
    placeItems: "center",
    width: 32,
    height: 32,
    padding: 0,
    fontFamily: font.sans,
    fontSize: 16,
    fontWeight: 700,
    lineHeight: 1,
    cursor: "pointer",
    outlineWidth: 2,
    outlineStyle: {
      default: "none",
      ":focus-visible": "solid",
    },
    outlineColor: color.orange,
    outlineOffset: 2,
    borderColor: "rgba(248,236,212,0.35)",
    borderStyle: "solid",
    borderWidth: 1,
    borderRadius: "50%",
    transform: {
      default: null,
      ":hover": "translateY(-1px)",
    },
    transitionDuration: "160ms",
    transitionProperty: "transform, box-shadow",
  },
  fill: (bg: string, ink: string) => ({ color: ink, backgroundColor: bg }),
  on: {
    borderColor: "rgba(248,236,212,0.9)",
    boxShadow: "0 0 0 3px rgba(236,127,49,0.55)",
  },
});
