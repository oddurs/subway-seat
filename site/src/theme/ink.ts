import * as stylex from "@stylexjs/stylex";
import { ink } from "./ink.stylex";
import { color } from "./tokens.stylex";

// Enamel: accents mixed toward text until small text clears 4.5:1 on mantle and
// base (orange 5.1, code 5.2, flag 5.0, string 5.2 on mantle), buttons carry
// base-colored text, hovers go darker.
export const enamelInk = stylex.createTheme(ink, {
  accent: `color-mix(in srgb, ${color.orange} 75%, ${color.text})`,
  accentHover: `color-mix(in srgb, ${color.orange} 55%, ${color.text})`,
  code: `color-mix(in srgb, ${color.yellow} 70%, ${color.text})`,
  flag: `color-mix(in srgb, ${color.sage} 80%, ${color.text})`,
  string: `color-mix(in srgb, ${color.green} 70%, ${color.text})`,
  onAccent: color.base,
  fillHover: `color-mix(in srgb, ${color.orange} 80%, ${color.text})`,
  okFill: `color-mix(in srgb, ${color.green} 80%, ${color.text})`,
});
