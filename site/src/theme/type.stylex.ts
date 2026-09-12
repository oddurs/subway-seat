import * as stylex from "@stylexjs/stylex";

// Two cities, two voices, one set of slots.
//
// New York: the subway's own face is Helvetica (the 1970 Vignelli/Noorda
// manual), but a system Helvetica stack renders as Arial off macOS, so the UI
// is set in Inter — the screen-era neo-grotesque drawn from the same skeleton —
// with Helvetica kept in the stack. Fraunces, SOFT axis turned up, is the
// living-room half: chunky and friendly, like 70s Cooper and Windsor. It wants
// heavy weights, negative tracking and tight leading.
//
// Code is JetBrains Mono in both cities. A code sample is a specimen of the
// theme, not of the city, so it is the one thing that does not change.
//
// London: Edward Johnston drew the Underground's face in 1916 — humanist, a
// near-circular O, a diamond over the i. Johnston isn't licensed for the web,
// so the site sets Cabin, which Pablo Impallari drew from Johnston's and
// Gill's proportions. It is a lighter, more open design than Fraunces and
// breaks if you set it the same way: one weight rather than four, tracking
// near zero instead of tight, and caps opened right up, which is how the
// Underground has set its signage for a century.
//
// Everything below the faces is what changes between them, so a headline is
// one element in the markup rather than one per city. London's values live in
// theme/faces.ts.
export const font = stylex.defineVars({
  sans: 'var(--font-inter), "Helvetica Neue", Helvetica, Arial, sans-serif',
  display: 'var(--font-fraunces), "Cooper Black", Georgia, serif',
  mono: 'var(--font-jetbrains-mono), "JetBrains Mono", ui-monospace, Menlo, monospace',

  /** The hero headline. */
  heroWeight: "800",
  heroTracking: "-0.02em",
  heroLeading: "0.98",
  heroSettings: '"SOFT" 100, "WONK" 1, "opsz" 144',

  /** Section headings. */
  titleWeight: "750",
  titleTracking: "-0.015em",
  titleLeading: "1.04",
  titleSettings: '"SOFT" 100, "WONK" 1',

  /** Uppercase eyebrows and small labels. */
  labelTracking: "0.16em",
  /** The wordmark in the nav. */
  markTracking: "-0.01em",
});
