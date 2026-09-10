"use client";

import * as stylex from "@stylexjs/stylex";
import { useState } from "react";
import { currentFlavor } from "@/lib/flavor";
import type { FlavorId } from "@/lib/palette";
import { color } from "@/theme/tokens.stylex";
import { font } from "@/theme/type.stylex";

export type SwatchLabel = { flavor: FlavorId; hex: string; ink: string };

/** A colour chip in the current flavor; click copies that flavor's hex. */
export function Swatch({
  fill,
  name,
  labels,
}: {
  fill: string;
  name?: string;
  labels: SwatchLabel[];
}) {
  const [copied, setCopied] = useState(false);

  async function copy() {
    const hex = labels.find((l) => l.flavor === currentFlavor())?.hex ?? labels[0].hex;
    await navigator.clipboard.writeText(hex);
    setCopied(true);
    setTimeout(() => setCopied(false), 1200);
  }

  return (
    <button
      type="button"
      onClick={copy}
      aria-label={`Copy ${name ?? "colour"}`}
      {...stylex.props(styles.chip, styles.fill(fill))}
    >
      {labels.map((l) => (
        <span
          key={l.flavor}
          data-only={l.flavor}
          {...stylex.props(styles.label, styles.ink(l.ink))}
        >
          <b {...stylex.props(styles.name)}>{name ?? " "}</b>
          <code {...stylex.props(styles.hex)}>{copied ? "copied" : l.hex}</code>
        </span>
      ))}
    </button>
  );
}

const styles = stylex.create({
  chip: {
    display: "flex",
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
    outlineColor: color.orange,
    outlineOffset: 2,
    borderWidth: 0,
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
  hex: { fontFamily: font.mono, fontSize: 11, opacity: 0.8 },
});
