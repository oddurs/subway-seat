import * as stylex from "@stylexjs/stylex";
import type { ReactNode } from "react";
import { ink } from "@/theme/ink.stylex";
import { color } from "@/theme/tokens.stylex";
import { font } from "@/theme/type.stylex";
import { CopyButton } from "./CopyButton";

// Install commands, drawn in the palette's code colors (commands gold, flags
// seafoam, URLs avocado). Unlike a CodeBlock they wrap, so a long one-liner stays
// whole on a phone and never slides under its copy button.

function span(key: string, style: stylex.StyleXStyles, text: string) {
  return (
    <span key={key} {...stylex.props(style)}>
      {text}
    </span>
  );
}

/** Shell words: the first of each command, flags, URLs and pipes each get a color. */
export function Shell({ text }: { text: string }) {
  const out: ReactNode[] = [];
  text.split("\n").forEach((line, n) => {
    if (n) out.push("\n");
    let head = true;
    for (const [i, tok] of line.split(/(\s+)/).entries()) {
      const key = `${n}-${i}`;
      if (!tok || /^\s+$/.test(tok)) out.push(tok);
      else if (tok === "|" || tok === "&&") {
        out.push(span(key, tone.op, tok));
        head = true;
      } else if (/^https?:\/\//.test(tok)) out.push(span(key, tone.str, tok));
      else if (tok.startsWith("-")) out.push(span(key, tone.flag, tok));
      else if (head) {
        out.push(span(key, tone.cmd, tok));
        head = false;
      } else out.push(tok);
    }
  });
  return <>{out}</>;
}

/** `key=value` lines. */
export function Config({ text }: { text: string }) {
  return (
    <>
      {text
        .trimEnd()
        .split("\n")
        .map((line, i) => {
          const [k, ...v] = line.split("=");
          return (
            // biome-ignore lint/suspicious/noArrayIndexKey: fixed lines
            <span key={i}>
              {i > 0 && "\n"}
              {span("k", tone.cmd, k)}
              {span("o", tone.op, "=")}
              {v.join("=")}
            </span>
          );
        })}
    </>
  );
}

/** A command (or config file) with a copy button. `sunk` sits it on mantle, for use inside a card. */
export function Command({
  text,
  kind = "shell",
  sunk = false,
  copy = true,
}: {
  text: string;
  kind?: "shell" | "config";
  sunk?: boolean;
  copy?: boolean;
}) {
  return (
    <div {...stylex.props(styles.wrap)}>
      <pre {...stylex.props(styles.code, sunk ? styles.sunk : styles.raised, copy && styles.room)}>
        {kind === "config" ? <Config text={text} /> : <Shell text={text} />}
      </pre>
      {copy && (
        <div {...stylex.props(styles.copy)}>
          <CopyButton text={text.trimEnd()} />
        </div>
      )}
    </div>
  );
}

const tone = stylex.create({
  cmd: { color: ink.code },
  flag: { color: ink.flag },
  str: { color: ink.string },
  op: { color: color.overlay2 },
});

const styles = stylex.create({
  wrap: { position: "relative", minWidth: 0 },
  code: {
    minWidth: 0,
    paddingBlock: 14,
    paddingInline: 16,
    margin: 0,
    fontFamily: font.mono,
    fontSize: 13.5,
    lineHeight: 1.65,
    color: color.text,
    overflowWrap: "anywhere",
    whiteSpace: "pre-wrap",
    borderRadius: 10,
  },
  raised: {
    backgroundColor: color.base,
    borderColor: color.surface0,
    borderStyle: "solid",
    borderWidth: 1,
  },
  sunk: { backgroundColor: color.mantle },
  room: { paddingRight: 84 },
  copy: { position: "absolute", top: 9, right: 9 },
});
