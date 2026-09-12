import * as stylex from "@stylexjs/stylex";

/**
 * The spacing system: one rhythm, shared by both cities.
 *
 * Colour, type and ornament are where a family gets to be itself. Structure
 * isn't — a page that changed its measure and its rhythm between cities would
 * read as two sites rather than one system wearing two liveries. So the scale,
 * the page frame and the vertical rhythm live here and are the same in New
 * York and London, the way the 26 roles and the lightness ladder are.
 *
 * The steps are a 4px base, doubling twice and then widening, so a gap is
 * always recognisably one step from its neighbours rather than a value someone
 * typed.
 */
export const space = stylex.defineVars({
  s1: "4px",
  s2: "8px",
  s3: "12px",
  s4: "16px",
  s5: "24px",
  s6: "32px",
  s7: "48px",
  s8: "64px",
  s9: "96px",

  /** The page frame: one measure and one gutter, everywhere. */
  measure: "1200px",
  gutter: "clamp(20px, 4vw, 28px)",
  /** Between one section and the next. */
  section: "clamp(64px, 8vw, 104px)",
  /** Between a section's heading block and its content. */
  heading: "clamp(22px, 2.4vw, 30px)",
});
