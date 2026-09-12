import * as stylex from "@stylexjs/stylex";
import { font } from "./type.stylex";

// New York's voice is Helvetica — the 1970 Vignelli/Noorda manual — with
// Fraunces, SOFT turned up, for the living-room half.
//
// London's is Johnston's. Edward Johnston drew the Underground's face in 1916:
// humanist, near-circular O, and the diamond tittle over the i. Johnston isn't
// licensed for the web, so the site uses Cabin, which Pablo Impallari drew from
// Johnston's and Gill's proportions — the closest honest stand-in on Google
// Fonts. There is no display serif: Tube signage has one voice, set in one face,
// at two weights, and the discipline is the point.
export const londonType = stylex.createTheme(font, {
  sans: 'var(--font-cabin), "Gill Sans", "Gill Sans MT", Calibri, sans-serif',
  display: 'var(--font-cabin), "Gill Sans", "Gill Sans MT", Calibri, sans-serif',
  mono: font.mono,
});
