"use client";

import * as stylex from "@stylexjs/stylex";
import { type KeyboardEvent, type ReactNode, useId, useSyncExternalStore } from "react";
import { ink } from "@/theme/ink.stylex";
import { color } from "@/theme/tokens.stylex";
import { font } from "@/theme/type.stylex";

const KEY = "subway-seat:shell";
const EVENT = "subway-seat:shell";
type Shell = "fish" | "sh";
const TABS: { id: Shell; label: string }[] = [
  { id: "fish", label: "fish" },
  { id: "sh", label: "bash · zsh" },
];

function saved(): Shell {
  try {
    return localStorage.getItem(KEY) === "sh" ? "sh" : "fish";
  } catch {
    return "fish";
  }
}

function subscribe(onChange: () => void) {
  window.addEventListener(EVENT, onChange);
  window.addEventListener("storage", onChange);
  return () => {
    window.removeEventListener(EVENT, onChange);
    window.removeEventListener("storage", onChange);
  };
}

/** fish and POSIX versions of the same step. The pick is remembered and shared by every tab set. */
export function ShellTabs({ fish, sh }: { fish: ReactNode; sh: ReactNode }) {
  const shell = useSyncExternalStore(subscribe, saved, () => "fish" as const);
  const id = useId();

  function pick(next: Shell) {
    try {
      localStorage.setItem(KEY, next);
    } catch {}
    window.dispatchEvent(new Event(EVENT));
  }

  function onKey(e: KeyboardEvent<HTMLButtonElement>) {
    if (e.key !== "ArrowLeft" && e.key !== "ArrowRight") return;
    const next = shell === "fish" ? "sh" : "fish";
    pick(next);
    document.getElementById(`${id}-${next}-tab`)?.focus();
  }

  return (
    <div {...stylex.props(styles.wrap)}>
      <div role="tablist" aria-label="Shell" {...stylex.props(styles.list)}>
        {TABS.map((t) => (
          <button
            key={t.id}
            id={`${id}-${t.id}-tab`}
            type="button"
            role="tab"
            aria-selected={shell === t.id}
            aria-controls={`${id}-${t.id}`}
            tabIndex={shell === t.id ? 0 : -1}
            onClick={() => pick(t.id)}
            onKeyDown={onKey}
            {...stylex.props(styles.tab, shell === t.id && styles.on)}
          >
            {t.label}
          </button>
        ))}
      </div>
      {TABS.map((t) => (
        <div
          key={t.id}
          id={`${id}-${t.id}`}
          role="tabpanel"
          aria-labelledby={`${id}-${t.id}-tab`}
          hidden={shell !== t.id}
        >
          {t.id === "fish" ? fish : sh}
        </div>
      ))}
    </div>
  );
}

const styles = stylex.create({
  wrap: { display: "grid", gridTemplateColumns: "minmax(0, 1fr)", gap: 8 },
  list: { display: "flex", gap: 4 },
  tab: {
    paddingBlock: 5,
    paddingInline: 12,
    fontFamily: font.mono,
    fontSize: 12,
    color: {
      default: color.subtext0,
      ":hover": color.textHi,
    },
    cursor: "pointer",
    outlineWidth: 2,
    outlineStyle: {
      default: "none",
      ":focus-visible": "solid",
    },
    outlineColor: ink.accent,
    outlineOffset: 2,
    backgroundColor: "transparent",
    borderColor: color.surface1,
    borderStyle: "solid",
    borderWidth: 1,
    borderRadius: 999,
  },
  on: {
    color: color.textHi,
    backgroundColor: color.surface0,
    borderColor: color.surface2,
  },
});
