import * as stylex from "@stylexjs/stylex";
import { font } from "./type.stylex";

/**
 * London's voice. Cabin carries Johnston's proportions but none of Fraunces'
 * weight, so it is set the way the Underground sets its own: a single heavy
 * weight, tracking at rest rather than pulled tight, leading closed up to suit
 * a large x-height, and caps opened well past New York's for the small labels
 * — the tracking on a platform sign is what makes it read down a tunnel.
 */
export const londonType = stylex.createTheme(font, {
  sans: 'var(--font-cabin), "Gill Sans", "Gill Sans MT", Calibri, sans-serif',
  display: 'var(--font-cabin), "Gill Sans", "Gill Sans MT", Calibri, sans-serif',
  mono: 'var(--font-jetbrains-mono), "JetBrains Mono", ui-monospace, Menlo, monospace',

  heroWeight: "700",
  heroTracking: "-0.005em",
  heroLeading: "1.0",
  heroSettings: "normal",

  titleWeight: "700",
  titleTracking: "-0.004em",
  titleLeading: "1.08",
  titleSettings: "normal",

  labelTracking: "0.22em",
  markTracking: "0.004em",
});
