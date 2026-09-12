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

  leadHero: "0.98",
  leadTitle: "1.06",
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

/**
 * Portland, London's light flavor.
 *
 * The same face on the other polarity. Light type on a dark ground haloes —
 * the glyphs bloom a little and read heavier than they are — so the dark
 * flavors are set with the tracking opened to compensate. Dark type on a pale
 * ground does the reverse: it reads thinner and looser than the same setting
 * looks at night. Cabin has no weight above 700 to answer that with, so the
 * correction is in the fit — tracking closed up and the leading with it, which
 * puts the words back at the colour they have on the dark flavors.
 */
export const portlandType = stylex.createTheme(font, {
  sans: 'var(--font-cabin), "Gill Sans", "Gill Sans MT", Calibri, sans-serif',
  display: 'var(--font-cabin), "Gill Sans", "Gill Sans MT", Calibri, sans-serif',

  leadHero: "0.95",
  leadTitle: "1.03",
  leadHead: "1.28",

  trackHero: "-0.016em",
  trackTitle: "-0.012em",
  trackHead: "-0.008em",
  trackLabel: "0.19em",
  trackControl: "0.11em",

  axesHero: "normal",
  axesTitle: "normal",
  weightHero: "700",
  weightTitle: "700",
});

/**
 * Paris. Guimard's own lettering is Art Nouveau and unrepeatable, and Parisine
 * — what the Metro actually signs itself in today — isn't licensed for the web.
 * So the site sets Jost, which descends from the geometric sans of the same
 * decades the network was being built out, and lets the ornament rather than
 * the type carry the Art Nouveau. Geometric faces have a small x-height and
 * wide round forms, so it wants more leading than Cabin and less tracking than
 * either of the others at display size.
 */
const PARIS_FACE = 'var(--font-jost), "Futura", "Century Gothic", sans-serif';

export const parisType = stylex.createTheme(font, {
  sans: PARIS_FACE,
  display: PARIS_FACE,

  leadHero: "1.0",
  leadTitle: "1.08",
  leadHead: "1.3",

  trackHero: "-0.018em",
  trackTitle: "-0.014em",
  trackHead: "-0.008em",
  trackLabel: "0.2em",
  trackControl: "0.11em",

  axesHero: "normal",
  axesTitle: "normal",
  weightHero: "600",
  weightTitle: "600",
});

/** Carrelage, Paris's light flavor: the same correction Portland gets. */
export const carrelageType = stylex.createTheme(font, {
  sans: PARIS_FACE,
  display: PARIS_FACE,

  leadHero: "0.97",
  leadTitle: "1.05",
  leadHead: "1.28",

  trackHero: "-0.026em",
  trackTitle: "-0.02em",
  trackHead: "-0.012em",
  trackLabel: "0.17em",
  trackControl: "0.1em",

  axesHero: "normal",
  axesTitle: "normal",
  weightHero: "600",
  weightTitle: "600",
});
