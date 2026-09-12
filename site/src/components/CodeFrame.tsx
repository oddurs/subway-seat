"use client";

import * as stylex from "@stylexjs/stylex";
import { useEffect, useRef, useState } from "react";
import { ink } from "@/theme/ink.stylex";
import { color } from "@/theme/tokens.stylex";
import { action } from "./action";

/**
 * The frame around highlighted code. When it scrolls it can be focused (so
 * the keyboard can scroll it) and fades at the bottom until you reach the end.
 * "Show all" swaps in the whole file from `full`.
 */
export function CodeFrame({
  html,
  scroll,
  label,
  total,
  shown,
  full,
}: {
  html: string;
  scroll: boolean;
  label: string;
  total: number;
  shown: number;
  full?: string;
}) {
  const [body, setBody] = useState(html);
  const [state, setState] = useState<"clipped" | "loading" | "all" | "failed">(
    full ? "clipped" : "all",
  );
  const [atEnd, setAtEnd] = useState(false);
  const ref = useRef<HTMLDivElement>(null);

  function onScroll() {
    const el = ref.current;
    if (el) setAtEnd(el.scrollTop + el.clientHeight >= el.scrollHeight - 4);
  }

  // biome-ignore lint/correctness/useExhaustiveDependencies: re-measure when the code changes
  useEffect(onScroll, [body]);

  async function showAll() {
    if (!full) return;
    setState("loading");
    try {
      const res = await fetch(full);
      if (!res.ok) throw new Error(String(res.status));
      setBody(await res.text());
      setState("all");
      setAtEnd(false);
    } catch {
      setState("failed");
    }
  }

  return (
    <>
      <div
        ref={ref}
        onScroll={scroll ? onScroll : undefined}
        // biome-ignore lint/a11y/noNoninteractiveTabindex: scrollable code must be reachable by keyboard
        tabIndex={scroll ? 0 : undefined}
        role={scroll ? "region" : undefined}
        aria-label={scroll ? label : undefined}
        {...stylex.props(styles.frame, scroll && styles.scroll, scroll && !atEnd && styles.fade)}
        // Shiki output is generated at build time from our own files.
        dangerouslySetInnerHTML={{ __html: body }}
      />
      {full && state !== "all" && (
        <p {...stylex.props(styles.note)}>
          Showing {shown} of {total.toLocaleString("en-US")} lines.{" "}
          <button
            type="button"
            onClick={showAll}
            disabled={state === "loading"}
            {...stylex.props(action.base)}
          >
            {state === "loading"
              ? "Loading…"
              : state === "failed"
                ? "Couldn't load it; download instead"
                : "Show all"}
          </button>
        </p>
      )}
    </>
  );
}

const styles = stylex.create({
  frame: {
    overflow: "auto",
    outlineWidth: 2,
    outlineStyle: {
      default: "none",
      ":focus-visible": "solid",
    },
    outlineColor: ink.accent,
    outlineOffset: 2,
    backgroundColor: color.base,
    borderColor: color.surface0,
    borderStyle: "solid",
    borderWidth: 1,
    borderRadius: "var(--radius-card)",
  },
  scroll: { maxHeight: "26rem" },
  fade: {
    maskImage: "linear-gradient(to bottom, #000 calc(100% - 40px), transparent)",
  },
  note: {
    display: "flex",
    flexWrap: "wrap",
    gap: 10,
    alignItems: "center",
    marginTop: 8,
    fontSize: 13,
    color: color.overlay2,
  },
});
