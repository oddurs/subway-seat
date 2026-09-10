import * as stylex from "@stylexjs/stylex";
import type { ShikiTransformer } from "shiki";
import { highlight } from "@/lib/highlight";
import type { FlavorId } from "@/lib/palette";
import { font } from "@/theme/type.stylex";

const cls = (...s: stylex.StyleXStyles[]) => stylex.props(...s).className ?? "";

const transformer = (roomForCopy: boolean): ShikiTransformer => ({
  pre(node) {
    this.addClassToHast(node, roomForCopy ? cls(styles.pre, styles.roomForCopy) : cls(styles.pre));
  },
  line(node) {
    this.addClassToHast(node, cls(styles.line));
  },
});

/** Lines a page carries; the rest load on "Show all". */
export const MAX_LINES = 150;

/** A code block's highlighted <pre>, shared by CodeBlock and the /code route. */
export function blockHtml(code: string, lang: string, flavor?: FlavorId, roomForCopy = false) {
  return highlight(code, lang, [transformer(roomForCopy)], [], flavor);
}

const styles = stylex.create({
  pre: {
    width: "max-content",
    minWidth: "100%",
    paddingBlock: 14,
    paddingInline: 16,
    margin: 0,
    fontFamily: font.mono,
    fontSize: 13,
    lineHeight: 1.6,
  },
  // keeps short lines clear of the copy button
  roomForCopy: { paddingRight: 84 },
  line: { display: "inline-block", minHeight: "1lh", verticalAlign: "top" },
});
