import * as stylex from "@stylexjs/stylex";

// Station signs are black with white Helvetica, whatever the flavor. `ring` is
// the focus ring on the sign: Walnut's orange, which reads on black in every flavor.
export const sign = stylex.defineConsts({
  bg: "#0C0805",
  text: "#F8ECD4",
  ring: "#EC7F31",
});
