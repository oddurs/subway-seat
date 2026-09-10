"use client";

import * as stylex from "@stylexjs/stylex";
import { useState } from "react";
import { action } from "./action";

export function CopyButton({ text, label = "Copy" }: { text: string; label?: string }) {
  const [copied, setCopied] = useState(false);

  async function copy() {
    await navigator.clipboard.writeText(text);
    setCopied(true);
    setTimeout(() => setCopied(false), 1400);
  }

  return (
    <button type="button" onClick={copy} {...stylex.props(action.base, copied && action.done)}>
      {copied ? "Copied" : label}
    </button>
  );
}
