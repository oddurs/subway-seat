import * as stylex from "@stylexjs/stylex";
import type { FlavorId } from "@/lib/palette";
import { blockHtml, MAX_LINES } from "./blockHtml";
import { CodeFrame } from "./CodeFrame";
import { CopyButton } from "./CopyButton";

/**
 * Syntax-highlighted code. Without `flavor` it carries all three flavors (see
 * globals.css for the swap); with it, only that flavor's theme. Long code is
 * cut at `maxLines`; `full` is where the whole highlighted file can be fetched.
 */
export async function CodeBlock({
  code,
  lang,
  scroll = false,
  maxLines = MAX_LINES,
  flavor,
  copy = false,
  full,
  label = "Code",
}: {
  code: string;
  lang: string;
  scroll?: boolean;
  maxLines?: number;
  flavor?: FlavorId;
  /** Show a copy button over the block (for short snippets). */
  copy?: boolean;
  full?: string;
  /** Names the block for screen readers when it scrolls. */
  label?: string;
}) {
  const lines = code.trimEnd().split("\n");
  const clipped = lines.length > maxLines;
  const body = clipped ? lines.slice(0, maxLines).join("\n") : lines.join("\n");
  const html = await blockHtml(body, lang, flavor, copy);
  return (
    <div {...stylex.props(styles.wrap)}>
      <CodeFrame
        html={html}
        scroll={scroll || clipped}
        label={label}
        total={lines.length}
        shown={clipped ? maxLines : lines.length}
        full={clipped ? full : undefined}
      />
      {copy && (
        <div {...stylex.props(styles.copy)}>
          <CopyButton text={code.trimEnd()} />
        </div>
      )}
    </div>
  );
}

const styles = stylex.create({
  wrap: { position: "relative", minWidth: 0 },
  copy: { position: "absolute", top: 8, right: 8 },
});
