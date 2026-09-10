import * as stylex from "@stylexjs/stylex";
import type { ShikiTransformer } from "shiki";
import { highlight } from "@/lib/highlight";
import { color } from "@/theme/tokens.stylex";
import { font } from "@/theme/type.stylex";

const cls = (...s: stylex.StyleXStyles[]) => stylex.props(...s).className ?? "";

const blockTransformer: ShikiTransformer = {
  pre(node) {
    this.addClassToHast(node, cls(styles.pre));
  },
  line(node) {
    this.addClassToHast(node, cls(styles.line));
  },
};

/** Syntax-highlighted code in all three flavors (see globals.css for the swap). */
export async function CodeBlock({
  code,
  lang,
  scroll = false,
  maxLines = 400,
}: {
  code: string;
  lang: string;
  scroll?: boolean;
  maxLines?: number;
}) {
  const lines = code.trimEnd().split("\n");
  const clipped = lines.length > maxLines;
  const body = clipped ? `${lines.slice(0, maxLines).join("\n")}\n…` : lines.join("\n");
  const html = await highlight(body, lang, [blockTransformer]);
  return (
    <div>
      <div
        {...stylex.props(styles.frame, scroll && styles.scroll)}
        // Shiki output is generated at build time from our own files.
        dangerouslySetInnerHTML={{ __html: html }}
      />
      {clipped && (
        <p {...stylex.props(styles.note)}>
          Showing {maxLines} of {lines.length} lines. Download for the whole file.
        </p>
      )}
    </div>
  );
}

const styles = stylex.create({
  frame: {
    overflow: "auto",
    backgroundColor: color.base,
    borderColor: color.surface0,
    borderStyle: "solid",
    borderWidth: 1,
    borderRadius: 10,
  },
  scroll: { maxHeight: "26rem" },
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
  line: { display: "inline-block", minHeight: "1lh", verticalAlign: "top" },
  note: { marginTop: 6, fontSize: 12.5, color: color.overlay1 },
});
