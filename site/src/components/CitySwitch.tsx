"use client";

import * as stylex from "@stylexjs/stylex";
import { Fragment, useSyncExternalStore } from "react";
import { currentFamily, setFamily, subscribeFlavor } from "@/lib/flavor";
import { families, flavorById, type FlavorId } from "@/lib/palette";
import { font } from "@/theme/type.stylex";

/**
 * Which city you're riding — the nav's only control.
 *
 * Stops joined by a line, which is the one diagram every one of these networks
 * draws the same way. The stop you're at is filled, in its own city's lead
 * colour; the others are open rings in the sign's own ink. That is the whole
 * use of colour here: it marks where you are and nothing else, so the band
 * stays a quiet sign and the control still reads as one object.
 *
 * It takes however many families there are, so a fourth city costs it nothing.
 */
export function CitySwitch() {
  const city = useSyncExternalStore(subscribeFlavor, currentFamily, () => null);

  return (
    <div role="group" aria-label="City" {...stylex.props(styles.group)}>
      {families.map((fam, i) => {
        const on = city === fam.id;
        const lead = flavorById[fam.default as FlavorId].colors[fam.lead];
        return (
          <Fragment key={fam.id}>
            {i > 0 && <span aria-hidden {...stylex.props(styles.track)} />}
            <button
              type="button"
              aria-pressed={city === null ? undefined : on}
              onClick={() => setFamily(fam.id)}
              {...stylex.props(styles.stop)}
            >
              {/* Both states are drawn and CSS shows the right one, so the
                  control is correct in the first painted frame. */}
              <span data-only={fam.id} aria-hidden {...stylex.props(styles.dot(lead))} />
              <span data-unless={fam.id} aria-hidden {...stylex.props(styles.dot(null))} />
              <span {...stylex.props(styles.name(on))}>{fam.name}</span>
            </button>
          </Fragment>
        );
      })}
    </div>
  );
}

const DOT = 11;

const styles = stylex.create({
  group: { display: "flex", gap: 0, alignItems: "center" },
  stop: {
    display: "flex",
    gap: 8,
    alignItems: "center",
    // Padding for the hand, margin back for the baseline — see NavLinks.
    paddingBlock: 4,
    paddingInline: 2,
    marginBlock: -4,
    cursor: "pointer",
    outlineWidth: 2,
    outlineStyle: { default: "none", ":focus-visible": "solid" },
    outlineColor: "var(--sign-ring)",
    outlineOffset: 4,
    backgroundColor: "transparent",
    borderWidth: 0,
    borderRadius: "var(--radius-pill)",
  },
  name: (on: boolean) => ({
    fontFamily: font.sans,
    fontSize: font.sizeLabel,
    fontWeight: 700,
    lineHeight: font.leadFlat,
    color: "var(--sign-text)",
    textTransform: "uppercase",
    letterSpacing: font.trackControl,
    opacity: on ? 1 : 0.58,
    transitionDelay: "40ms",
    transitionDuration: "360ms",
    transitionProperty: "opacity, color",
  }),
  dot: (lead: string | null) => ({
    flexShrink: 0,
    width: DOT,
    height: DOT,
    backgroundColor: "transparent",
    borderColor: lead ?? "color-mix(in srgb, var(--sign-text) 55%, transparent)",
    borderStyle: "solid",
    borderWidth: lead ? 5.5 : 2,
    borderRadius: "50%",
    transitionTimingFunction: "cubic-bezier(0.2, 0, 0, 1)",
    transitionDuration: "260ms",
    transitionProperty: "border-color, border-width",
  }),
  track: {
    flexShrink: 0,
    width: 20,
    height: 2,
    backgroundColor: "color-mix(in srgb, var(--sign-text) 28%, transparent)",
    transitionDuration: "360ms",
    transitionProperty: "background-color",
  },
});
