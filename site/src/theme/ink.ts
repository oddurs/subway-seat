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

// Portland: the same idea for London's light flavor. Its accents are already
// solved against a pale stone ground, so only the ones the site uses for small
// UI text are pulled toward text; links stay the exact Corporate Blue, which
// clears 4.5:1 on every ground in the flavor on its own.
export const portlandInk = stylex.createTheme(ink, {
  accent: color.red,
  accentHover: `color-mix(in srgb, ${color.red} 78%, ${color.text})`,
  code: color.orange,
  flag: color.sage,
  string: color.green,
  fill: color.red,
  onAccent: color.base,
  fillHover: `color-mix(in srgb, ${color.red} 82%, ${color.text})`,
  okFill: color.green,
});

// London's dark flavors. The lead accent is the red — it carries chrome,
// buttons and links-as-actions, and nothing else, so it stays rare. Inline code
// takes the brick and flags the hazard yellow, which is where those two do their
// quietest work.
export const londonInk = stylex.createTheme(ink, {
  accent: color.red,
  accentHover: color.redHi,
  code: color.orange,
  flag: color.sage,
  string: color.green,
  fill: color.red,
  onAccent: color.crust,
  fillHover: color.redHi,
  okFill: color.green,
});
