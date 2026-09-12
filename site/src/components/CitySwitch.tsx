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
 * chosen in the footer and on the cards, where the flavors are actually shown.
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
  group: { display: "flex", gap: 22, alignItems: "baseline" },
  stop: {
    display: "grid",
    // The rule sits a clear step below the cap line, not tucked under it.
    gap: 9,
    padding: 0,
    cursor: "pointer",
    outlineWidth: 2,
    outlineStyle: { default: "none", ":focus-visible": "solid" },
    outlineColor: "var(--sign-ring)",
    outlineOffset: 5,
    borderWidth: 0,
    borderRadius: 0,
    backgroundColor: "transparent",
  },
  name: (on: boolean) => ({
    fontFamily: font.sans,
    fontSize: font.sizeLabel,
    fontWeight: 700,
    lineHeight: font.leadFlat,
    letterSpacing: font.trackLabel,
    // The tracking adds a trailing gap after the last letter; pulling it back
    // keeps the rule the same width as the word it belongs to.
    marginRight: "-0.22em",
    textTransform: "uppercase",
    color: "var(--sign-text)",
    opacity: on ? 1 : 0.62,
    transitionDuration: "180ms",
    transitionProperty: "opacity",
  }),
  line: (lead: string, on: boolean) => ({
    height: on ? 3 : 2,
    marginRight: "-0.22em",
    marginTop: on ? 0 : 1,
    backgroundColor: lead,
    opacity: on ? 1 : 0.45,
    transitionDuration: "180ms",
    transitionProperty: "opacity, height",
  }),
});
