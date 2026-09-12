"use client";

import * as stylex from "@stylexjs/stylex";
import type { ReactNode } from "react";
import { useState } from "react";
import { announce, copyText } from "@/lib/clipboard";
import { currentFlavor } from "@/lib/flavor";
import type { FlavorId } from "@/lib/palette";
import { ink } from "@/theme/ink.stylex";
import { color } from "@/theme/tokens.stylex";
import { font } from "@/theme/type.stylex";

export type SwatchLabel = { flavor: FlavorId; hex: string; ink: string };

/**
 * A color chip in the current flavor; click copies that flavor's hex. Its name
 * is the visible text (role name and hex), so "Copy" isn't needed in a label.
 */
export function Swatch({
  fill,
  name,
  labels,
}: {
  fill: string;
  name?: ReactNode;
  labels: SwatchLabel[];
}) {
  const [state, setState] = useState<"idle" | "copied" | "failed">("idle");

  async function copy() {
    const hex = labels.find((l) => l.flavor === currentFlavor())?.hex ?? labels[0].hex;
    const ok = await copyText(hex);
    setState(ok ? "copied" : "failed");
    announce(ok ? `Copied ${hex}` : "Couldn't copy");
    setTimeout(() => setState("idle"), 1200);
  }

  return (
    <button
      type="button"
      onClick={copy}
      title="Copy the hex"
      {...stylex.props(styles.chip, styles.fill(fill))}
    >
      {labels.map((l) => (
        <span
          key={l.flavor}
          data-only={l.flavor}
          {...stylex.props(styles.label, styles.ink(l.ink))}
        >
          <b {...stylex.props(styles.name)}>{name ?? " "}</b>
          <code {...stylex.props(styles.hex)}>
            {state === "copied" ? "copied" : state === "failed" ? "couldn't copy" : l.hex}
          </code>
        </span>
      ))}
    </button>
  );
}

const styles = stylex.create({
  chip: {
    display: "flex",
    flexGrow: 1,
    flexShrink: 1,
    flexBasis: 112,
    flexDirection: "column",
    justifyContent: "flex-end",
    height: 84,
    paddingBlock: 10,
    paddingInline: 12,
    textAlign: "left",
    cursor: "pointer",
    outlineWidth: 2,
    outlineStyle: {
      default: "none",
      ":focus-visible": "solid",
    },
    outlineColor: ink.accent,
    outlineOffset: -4,
    borderWidth: 0,
    boxShadow: `inset 0 0 0 1px color-mix(in srgb, ${color.text} 12%, transparent)`,
    transform: {
      default: null,
      ":hover": "translateY(-2px)",
    },
    transitionDuration: "140ms",
    transitionProperty: "transform",
  },
  fill: (bg: string) => ({ backgroundColor: bg }),
  ink: (fg: string) => ({ color: fg }),
  label: { display: "grid", fontFamily: font.sans, fontSize: 13, lineHeight: 1.3 },
  name: { fontWeight: 600 },
  hex: { fontFamily: font.mono, fontSize: 11 },
});
