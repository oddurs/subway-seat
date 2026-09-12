import * as stylex from "@stylexjs/stylex";

/**
 * The typographic system. Faces, a scale, and — because the two cities are set
 * in faces that behave differently — leading and tracking as tokens rather than
 * as numbers scattered through components.
 *
 * New York: Helvetica is the subway's own face (the 1970 Vignelli/Noorda
 * manual); Fraunces, SOFT axis turned up, is the living-room half — chunky and
 * friendly, like 70s Cooper and Windsor. A high-contrast display serif with
 * short descenders, so it takes heavy weights, tight tracking and leading under
 * one.
 *
 * London: Edward Johnston drew the Underground's face in 1916 — humanist, a
 * near-circular O, a diamond over the i. Johnston isn't licensed for the web,
 * so the site sets Cabin, which Pablo Impallari drew from Johnston's and
 * Gill's proportions. Its x-height is much larger than Fraunces', which is why
 * it needs the opposite treatment: tracking at rest, and more leading, not
 * less, or the lines close up.
 *
 * Two faces belong to neither city. Code is JetBrains Mono, and the chrome of
 * the app mockups is Inter, because those are drawings of somebody else's UI.
 * A specimen is of the theme, not of the city, so neither changes.
 *
 * London's values live in theme/faces.ts.
 */
export const font = stylex.defineVars({
  // ── Faces ───────────────────────────────────────────────────────────────
  sans: '"Helvetica Neue", Helvetica, Arial, sans-serif',
  display: 'var(--font-fraunces), "Cooper Black", Georgia, serif',
  mono: 'var(--font-jetbrains-mono), "JetBrains Mono", ui-monospace, Menlo, monospace',
  /** The chrome of an app mockup: an editor's tabs, a window's title bar. */
  ui: 'var(--font-inter), "Helvetica Neue", Helvetica, Arial, sans-serif',

  // ── Scale ───────────────────────────────────────────────────────────────
  sizeHero: "clamp(44px, 7.2vw, 92px)",
  sizeTitle: "clamp(30px, 4.2vw, 50px)",
  sizeHead: "19px",
  sizeLede: "clamp(17px, 1.5vw, 20px)",
  sizeBody: "16px",
  sizeSmall: "14.5px",
  sizeMicro: "12.5px",
  sizeLabel: "12px",
  sizeMark: "20px",

  // ── Leading ─────────────────────────────────────────────────────────────
  leadHero: "0.98",
  leadTitle: "1.06",
  leadHead: "1.25",
  leadLede: "1.55",
  leadBody: "1.62",
  /** For anything that has to sit on a shared baseline: nav, chips, buttons. */
  leadFlat: "1",

  // ── Tracking ────────────────────────────────────────────────────────────
  trackHero: "-0.022em",
  trackTitle: "-0.016em",
  trackHead: "-0.01em",
  trackBody: "0em",
  /** Uppercase eyebrows and small labels. */
  trackLabel: "0.16em",
  /** Caps inside a control, where sprawl reads as loose rather than as signage. */
  trackControl: "0.09em",
  /** The wordmark in the nav. */
  trackMark: "-0.01em",

  // ── Variable-font axes (Fraunces; London sets these to normal) ──────────
  axesHero: '"SOFT" 100, "WONK" 1, "opsz" 144',
  axesTitle: '"SOFT" 100, "WONK" 1',
  weightHero: "800",
  weightTitle: "750",
});
