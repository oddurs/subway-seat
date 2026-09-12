import * as stylex from "@stylexjs/stylex";
import { font } from "./type.stylex";

/**
 * London's voice. Cabin carries Johnston's proportions but none of Fraunces'
 * weight or its short descenders, so it is set the way the Underground sets its
 * own: a single heavy weight, tracking at rest rather than pulled tight, and —
 * because its x-height is so much larger — more leading rather than less, or
 * the lines of a headline close up on each other.
 *
 * Caps open well past New York's: the tracking on a platform sign is what makes
 * it read down a tunnel.
 */
export const londonType = stylex.createTheme(font, {
  sans: 'var(--font-cabin), "Gill Sans", "Gill Sans MT", Calibri, sans-serif',
  display: 'var(--font-cabin), "Gill Sans", "Gill Sans MT", Calibri, sans-serif',

  leadHero: "1.06",
  leadTitle: "1.14",
  leadHead: "1.3",

  trackHero: "-0.006em",
  trackTitle: "-0.004em",
  trackHead: "-0.002em",
  trackLabel: "0.22em",
  trackControl: "0.13em",
  trackMark: "0.004em",

  axesHero: "normal",
  axesTitle: "normal",
  weightHero: "700",
  weightTitle: "700",
});
