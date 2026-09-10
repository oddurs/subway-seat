"use client";

import * as stylex from "@stylexjs/stylex";
import { useState } from "react";
import { announce, copyFrom, copyText } from "@/lib/clipboard";
import { action } from "./action";

/**
 * Copies `text`, or the file at `src` (fetched on click, so big files aren't
 * inlined in the page). `name` makes the button's label specific for screen readers.
 */
export function CopyButton({
  text,
  src,
  label = "Copy",
  name,
}: {
  text?: string;
  src?: string;
  label?: string;
  name?: string;
}) {
  const [state, setState] = useState<"idle" | "done" | "failed">("idle");

  async function copy() {
    const ok = text !== undefined ? await copyText(text) : src ? await copyFrom(src) : false;
    setState(ok ? "done" : "failed");
    announce(ok ? `Copied${name ? ` ${name}` : ""}` : "Couldn't copy");
    setTimeout(() => setState("idle"), 1600);
  }

  return (
    <button
      type="button"
      onClick={copy}
      aria-label={name ? `${label} ${name}` : undefined}
      {...stylex.props(action.base, state === "done" && action.done)}
    >
      {state === "done" ? "Copied" : state === "failed" ? "Couldn't copy" : label}
    </button>
  );
}
