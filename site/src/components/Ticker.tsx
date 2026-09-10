"use client";

import * as stylex from "@stylexjs/stylex";
import { useEffect, useState } from "react";

/** Cycles through lines like Claude Code's spinner verbs and tips. */
export function Ticker({
  items,
  every = 2600,
  suffix = "",
}: {
  items: string[];
  every?: number;
  suffix?: string;
}) {
  const [i, setI] = useState(0);

  useEffect(() => {
    if (matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    const t = setInterval(() => setI((n) => (n + 1) % items.length), every);
    return () => clearInterval(t);
  }, [items.length, every]);

  return (
    <span key={i} {...stylex.props(styles.item)}>
      {items[i]}
      {suffix}
    </span>
  );
}

const fade = stylex.keyframes({
  from: { opacity: 0, transform: "translateY(3px)" },
  to: { opacity: 1, transform: "none" },
});

const styles = stylex.create({
  item: {
    display: "inline-block",
    animationName: {
      default: fade,
      "@media (prefers-reduced-motion: reduce)": "none",
    },
    animationDuration: "360ms",
    animationTimingFunction: "ease-out",
  },
});
