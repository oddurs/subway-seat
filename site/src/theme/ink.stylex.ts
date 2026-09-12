import * as stylex from "@stylexjs/stylex";
import { color } from "./tokens.stylex";

// Site-only text colors derived from the palette. On the dark flavors they are
// the accents themselves; Enamel's accents are tuned for code on paper and run a
// little light for small UI text, so the site mixes them toward text to reach
// 4.5:1 on every ground, and hovers go darker instead of lighter (see enamelInk).
export const ink = stylex.defineVars({
  /** Eyebrows, section labels, text links. */
  accent: color.orange,
  accentHover: color.orangeHi,
  /** Inline code and file names; commands in an install line. */
  code: color.yellow,
  /** Flags and URLs in an install line. */
  flag: color.sage,
  string: color.green,
  /** The lead accent as a fill: primary buttons, the active bullet. New York
   * leads with burnt orange, which also leads keywords; London leads with the
   * red, which leads nothing else, so it stays rare. */
  fill: color.orange,
  /** Text on that fill: _lib's ink(f). */
  onAccent: color.crust,
  /** The primary button's hover fill. */
  fillHover: color.orangeHi,
  /** The "Copied" fill, under onAccent text. */
  okFill: color.green,
});
