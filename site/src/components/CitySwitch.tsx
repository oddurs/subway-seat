"use client";

import * as stylex from "@stylexjs/stylex";
import { useSyncExternalStore } from "react";
import { currentFamily, setFamily, subscribeFlavor } from "@/lib/flavor";
import { families, flavorById, type FlavorId } from "@/lib/palette";
import { font } from "@/theme/type.stylex";

/**
 * Which city you're riding — the nav's only control.
 *
 * Two stops joined by a line, which is the one diagram both networks draw the
 * same way. The stop you're at is filled, in its own city's lead colour; the
 * other is an open ring in the sign's own ink. That's the whole use of colour
 * here: it marks where you are and nothing else, so the band stays a quiet
 * sign and the switch still reads as one object rather than two links.
 */
export function CitySwitch() {
  const city = useSyncExternalStore(subscribeFlavor, currentFamily, () => null);
  const [first, second] = families;

  const stop = (fam: (typeof families)[number], labelFirst: boolean) => {
    const on = city === fam.id;
    const lead = flavorById[fam.default as FlavorId].colors[fam.lead];
    const label = <span {...stylex.props(styles.name(on))}>{fam.name}</span>;
    return (
      <button
        key={fam.id}
        type="button"
        aria-pressed={city === null ? undefined : on}
        onClick={() => setFamily(fam.id)}
        {...stylex.props(styles.stop)}
      >
        {labelFirst && label}
        {/* Both states are drawn and CSS shows the right one, so the control is
            correct in the first painted frame rather than after hydration. */}
        <span data-only={fam.id} aria-hidden {...stylex.props(styles.dot(lead))} />
        <span data-unless={fam.id} aria-hidden {...stylex.props(styles.dot(null))} />
        {!labelFirst && label}
      </button>
    );
  };

  return (
    <div role="group" aria-label="City" {...stylex.props(styles.group)}>
      {stop(first, true)}
      <span aria-hidden {...stylex.props(styles.track)} />
      {stop(second, false)}
    </div>
  );
}

const DOT = 11;

const styles = stylex.create({
  group: { display: "flex", alignItems: "center", gap: 0 },
  stop: {
    display: "flex",
    gap: 9,
    alignItems: "center",
    paddingBlock: 4,
    paddingInline: 2,
    cursor: "pointer",
    outlineWidth: 2,
    outlineStyle: { default: "none", ":focus-visible": "solid" },
    outlineColor: "var(--sign-ring)",
    outlineOffset: 4,
    borderWidth: 0,
    borderRadius: "var(--radius-pill)",
    backgroundColor: "transparent",
  },
  name: (on: boolean) => ({
    fontFamily: font.sans,
    fontSize: font.sizeLabel,
    fontWeight: 700,
    lineHeight: font.leadFlat,
    letterSpacing: font.trackControl,
    textTransform: "uppercase",
    color: "var(--sign-text)",
    opacity: on ? 1 : 0.58,
    transitionDuration: "180ms",
    transitionProperty: "opacity",
  }),
  // Filled where you are; an open ring where you aren't.
  dot: (lead: string | null) => ({
    width: DOT,
    height: DOT,
    flexShrink: 0,
    borderColor: lead ?? "color-mix(in srgb, var(--sign-text) 55%, transparent)",
    borderStyle: "solid",
    borderWidth: lead ? 5.5 : 2,
    borderRadius: "50%",
    backgroundColor: "transparent",
    transitionDuration: "180ms",
    transitionProperty: "border-color, border-width",
  }),
  // The line between the two stops.
  track: {
    width: 26,
    height: 2,
    backgroundColor: "color-mix(in srgb, var(--sign-text) 28%, transparent)",
  },
});
