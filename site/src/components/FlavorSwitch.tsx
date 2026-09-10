"use client";

import * as stylex from "@stylexjs/stylex";
import { useSyncExternalStore } from "react";
import { currentFlavor, FLAVOR_EVENT, setFlavor } from "@/lib/flavor";
import type { FlavorId } from "@/lib/palette";
import { color } from "@/theme/tokens.stylex";
import { font } from "@/theme/type.stylex";

const OPTIONS: { id: FlavorId; letter: string; label: string; swatch: string; ink: string }[] = [
  { id: "walnut", letter: "W", label: "Walnut", swatch: "#362619", ink: "#F3BF45" },
  { id: "tunnel", letter: "T", label: "Tunnel", swatch: "#24180E", ink: "#EC7F31" },
  { id: "enamel", letter: "E", label: "Enamel", swatch: "#F4E9D4", ink: "#C4561A" },
];

function subscribe(onChange: () => void) {
  window.addEventListener(FLAVOR_EVENT, onChange);
  return () => window.removeEventListener(FLAVOR_EVENT, onChange);
}

/** Three route bullets that change the flavor of the whole site. */
export function FlavorSwitch() {
  const active = useSyncExternalStore(subscribe, currentFlavor, () => null);

  return (
    <div role="radiogroup" aria-label="Flavor" {...stylex.props(styles.group)}>
      {OPTIONS.map((o) => {
        const on = active === o.id;
        return (
          // biome-ignore lint/a11y/useSemanticElements: a styled radio button
          <button
            key={o.id}
            type="button"
            role="radio"
            aria-checked={on}
            title={`Subway Seat ${o.label}`}
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
