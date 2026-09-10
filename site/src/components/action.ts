import * as stylex from "@stylexjs/stylex";
import { color } from "@/theme/tokens.stylex";
import { font } from "@/theme/type.stylex";

/** Shared look for the small actions above a code block (Copy, Download). */
export const action = stylex.create({
  base: {
    display: "inline-flex",
    alignItems: "center",
    paddingBlock: 4,
    paddingInline: 10,
    fontFamily: font.mono,
    fontSize: 12,
    color: {
      default: color.subtext1,
      ":hover": color.textHi,
    },
    textDecoration: "none",
    cursor: "pointer",
    outlineWidth: 2,
    outlineStyle: {
      default: "none",
      ":focus-visible": "solid",
    },
    outlineColor: color.orange,
    outlineOffset: 2,
    backgroundColor: {
      default: color.surface0,
      ":hover": color.surface1,
    },
    borderColor: color.surface1,
    borderStyle: "solid",
    borderWidth: 1,
    borderRadius: 4,
  },
  done: {
    color: color.crust,
    backgroundColor: color.green,
    borderColor: color.green,
  },
});
