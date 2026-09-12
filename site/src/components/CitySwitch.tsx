"use client";

import * as stylex from "@stylexjs/stylex";
import { useSyncExternalStore } from "react";
import { currentFamily, setFamily, subscribeFlavor } from "@/lib/flavor";
import { families, flavorById, type FlavorId } from "@/lib/palette";
import { font } from "@/theme/type.stylex";

/**
 * The nav's only control: which city you're riding.
 *
 * Two stops on a line. Each carries a rule in its own family's lead accent —
 * New York's burnt orange, London's red — so the pair reads as two route
 * segments and the one you're on is the lit one. The flavor within a city is
 * chosen where the flavors are actually shown, not up here.
 */
export function CitySwitch() {
  const city = useSyncExternalStore(subscribeFlavor, currentFamily, () => null);

  return (
    <div role="group" aria-label="City" {...stylex.props(styles.group)}>
      {families.map((fam) => {
        const on = city === fam.id;
        const lead = flavorById[fam.default as FlavorId].colors[fam.lead];
        return (
          <button
            key={fam.id}
            type="button"
            aria-pressed={city === null ? undefined : on}
            onClick={() => setFamily(fam.id)}
            {...stylex.props(styles.stop)}
          >
            <span {...stylex.props(styles.name(on))}>{fam.name}</span>
            <span aria-hidden {...stylex.props(styles.line(lead, on))} />
          </button>
        );
      })}
    </div>
  );
}

const styles = stylex.create({
  group: { display: "flex", gap: 4, alignItems: "center" },
  stop: {
    display: "grid",
    gap: 6,
    padding: 0,
    paddingInline: 10,
    paddingTop: 4,
    cursor: "pointer",
    outlineWidth: 2,
    outlineStyle: { default: "none", ":focus-visible": "solid" },
    outlineColor: "var(--sign-ring)",
    outlineOffset: 3,
    borderWidth: 0,
    borderRadius: 0,
    backgroundColor: "transparent",
  },
  name: (on: boolean) => ({
    fontFamily: font.sans,
    fontSize: 12,
    fontWeight: 700,
    lineHeight: 1,
    letterSpacing: font.labelTracking,
    textTransform: "uppercase",
    color: "var(--sign-text)",
    opacity: on ? 1 : 0.52,
    transitionDuration: "180ms",
    transitionProperty: "opacity",
  }),
  // The route segment under the name: full strength on the stop you're at.
  line: (lead: string, on: boolean) => ({
    height: 3,
    backgroundColor: lead,
    opacity: on ? 1 : 0.32,
    transitionDuration: "180ms",
    transitionProperty: "opacity",
  }),
});
