"use client";

import * as stylex from "@stylexjs/stylex";
import type { ReactNode } from "react";
import { useState, useSyncExternalStore } from "react";
import { announce, copyText } from "@/lib/clipboard";
import { cssVariables, FORMATS, type Format, formatColor } from "@/lib/color";
import { currentFlavor, subscribeFlavor } from "@/lib/flavor";
import type { ColorName, FamilyId, FlavorId } from "@/lib/palette";
import { ink } from "@/theme/ink.stylex";
import { color } from "@/theme/tokens.stylex";
import { font } from "@/theme/type.stylex";
import { action } from "./action";

export type PaletteRow = {
  role: string;
  name: ReactNode;
  use: string;
  values: Record<FlavorId, string>;
  /** Contrast on the flavor's base, for text and accents. */
  contrast?: Record<FlavorId, number>;
};
export type PaletteGroup = { title: string; rows: PaletteRow[] };
export type PaletteFlavor = {
  id: FlavorId;
  family: FamilyId;
  label: string;
  colors: Record<string, string>;
};

/** AA for body text, AA for large text, or below either. */
const grade = (ratio: number) =>
  ratio >= 7 ? "AAA" : ratio >= 4.5 ? "AA" : ratio >= 3 ? "large" : "";

function Value({ hex, format }: { hex: string; format: Format }) {
  const [state, setState] = useState<"idle" | "copied" | "failed">("idle");
  const text = formatColor(hex, format);
  async function copy() {
    const ok = await copyText(text);
    setState(ok ? "copied" : "failed");
    announce(ok ? `Copied ${text}` : "Couldn't copy");
    setTimeout(() => setState("idle"), 1200);
  }
  return (
    <button type="button" onClick={copy} title="Copy" {...stylex.props(styles.value)}>
      <span aria-hidden {...stylex.props(styles.mini, styles.fill(hex))} />
      <code {...stylex.props(styles.code)}>
        {state === "copied" ? "copied" : state === "failed" ? "couldn't copy" : text}
      </code>
    </button>
  );
}

/** The three palette tables with a format switch; every value copies on click. */
export function PaletteTable({
  groups,
  flavors,
}: {
  groups: PaletteGroup[];
  flavors: PaletteFlavor[];
}) {
  const [format, setFormat] = useState<Format>("hex");
  const active = useSyncExternalStore(subscribeFlavor, currentFlavor, () => "walnut" as FlavorId);
  const [copied, setCopied] = useState(false);
  const activeFlavor = flavors.find((f) => f.id === active) ?? flavors[0];

  async function copyVars() {
    const ok = await copyText(cssVariables(activeFlavor.colors, format));
    setCopied(ok);
    announce(ok ? `Copied ${activeFlavor.label} as CSS variables` : "Couldn't copy");
    setTimeout(() => setCopied(false), 1400);
  }

  return (
    <div {...stylex.props(styles.stack)}>
      <div {...stylex.props(styles.toolbar)}>
        {/* biome-ignore lint/a11y/useSemanticElements: a group of toggle buttons */}
        <div role="group" aria-label="Color format" {...stylex.props(styles.formats)}>
          {FORMATS.map((f) => (
            <button
              key={f.id}
              type="button"
              aria-pressed={format === f.id}
              onClick={() => setFormat(f.id)}
              {...stylex.props(styles.format, format === f.id && styles.formatOn)}
            >
              {f.label}
            </button>
          ))}
        </div>
        <button
          type="button"
          onClick={copyVars}
          {...stylex.props(action.base, copied && action.done)}
        >
          {copied ? "Copied" : `Copy ${activeFlavor.label} as CSS variables`}
        </button>
      </div>

      {groups.map((group) => (
        <div key={group.title} {...stylex.props(styles.tableWrap)}>
          <table {...stylex.props(styles.table)}>
            <caption {...stylex.props(styles.caption)}>{group.title}</caption>
            <colgroup>
              <col {...stylex.props(styles.colChip)} />
              <col {...stylex.props(styles.colRole)} />
              {flavors.map((f) => (
                <col
                  key={f.id}
                  data-only={f.family}
                  data-narrow-only={f.id}
                  {...stylex.props(styles.colFlavor)}
                />
              ))}
              <col />
            </colgroup>
            <thead>
              <tr>
                <th {...stylex.props(styles.th)}>
                  <span className="sr-only">Swatch</span>
                </th>
                <th {...stylex.props(styles.th)}>Role</th>
                {flavors.map((f) => (
                  <th
                    key={f.id}
                    data-only={f.family}
                    data-narrow-only={f.id}
                    {...stylex.props(styles.th)}
                  >
                    {f.label}
                  </th>
                ))}
                <th {...stylex.props(styles.th)}>Used for</th>
              </tr>
            </thead>
            <tbody>
              {group.rows.map((row) => (
                <tr key={row.role}>
                  <td {...stylex.props(styles.td)}>
                    <span
                      aria-hidden
                      {...stylex.props(styles.chip, styles.fill(color[row.role as ColorName]))}
                    />
                  </td>
                  <td {...stylex.props(styles.td)}>
                    <b {...stylex.props(styles.name)}>{row.name}</b>
                    <code {...stylex.props(styles.role)}>{row.role}</code>
                  </td>
                  {flavors.map((f) => {
                    const ratio = row.contrast?.[f.id];
                    return (
                      <td
                        key={f.id}
                        data-only={f.family}
                        data-narrow-only={f.id}
                        {...stylex.props(styles.td)}
                      >
                        <Value hex={row.values[f.id]} format={format} />
                        {ratio !== undefined && (
                          <span {...stylex.props(styles.ratio)}>
                            {ratio.toFixed(1)}:1{grade(ratio) && ` · ${grade(ratio)}`}
                          </span>
                        )}
                      </td>
                    );
                  })}
                  <td {...stylex.props(styles.td, styles.use)}>{row.use}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      ))}
    </div>
  );
}

const NARROW = "@media (max-width: 720px)";

const styles = stylex.create({
  stack: { display: "grid", gridTemplateColumns: "minmax(0, 1fr)", gap: 22 },
  toolbar: {
    display: "flex",
    flexWrap: "wrap",
    gap: 12,
    alignItems: "center",
    justifyContent: "space-between",
  },
  formats: {
    display: "flex",
    padding: 3,
    backgroundColor: color.base,
    borderColor: color.surface0,
    borderStyle: "solid",
    borderWidth: 1,
    borderRadius: 999,
  },
  format: {
    paddingBlock: 6,
    paddingInline: 14,
    fontFamily: font.mono,
    fontSize: 12.5,
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
    outlineOffset: 1,
    backgroundColor: "transparent",
    borderWidth: 0,
    borderRadius: 999,
  },
  formatOn: { color: ink.onAccent, backgroundColor: ink.fill },
  tableWrap: {
    overflowX: "auto",
    backgroundColor: color.base,
    borderColor: color.surface0,
    borderStyle: "solid",
    borderWidth: 1,
    borderRadius: 16,
  },
  table: {
    width: "100%",
    minWidth: {
      [NARROW]: 0,
      default: 820,
    },
    fontSize: 14,
    tableLayout: "fixed",
    borderCollapse: "collapse",
  },
  colChip: { width: { [NARROW]: 52, default: 68 } },
  colRole: { width: { [NARROW]: 118, default: 170 } },
  colFlavor: { width: { [NARROW]: 150, default: 176 } },
  caption: {
    paddingInline: 18,
    paddingTop: 16,
    fontFamily: font.display,
    fontSize: 24,
    fontVariationSettings: '"SOFT" 100',
    fontWeight: 700,
    color: color.textHi,
    textAlign: "left",
  },
  th: {
    paddingBlock: 10,
    paddingInline: 12,
    fontSize: 12,
    fontWeight: 600,
    color: color.subtext0,
    textAlign: "left",
    textTransform: "uppercase",
    letterSpacing: "0.08em",
  },
  td: {
    paddingBlock: 10,
    paddingInline: 12,
    verticalAlign: "middle",
    borderTopColor: color.surface0,
    borderTopStyle: "solid",
    borderTopWidth: 1,
  },
  chip: {
    display: "block",
    width: { [NARROW]: 32, default: 44 },
    height: { [NARROW]: 32, default: 44 },
    borderRadius: 12,
    boxShadow: `inset 0 0 0 1px ${color.surface2}`,
  },
  fill: (bg: string) => ({ backgroundColor: bg }),
  name: { display: "block", color: color.textHi },
  role: { fontFamily: font.mono, fontSize: 12, color: color.subtext0 },
  value: {
    display: "inline-flex",
    gap: 8,
    alignItems: "center",
    maxWidth: "100%",
    paddingBlock: 3,
    paddingInline: 6,
    marginInline: -6,
    color: {
      default: color.text,
      ":hover": color.textHi,
    },
    textAlign: "left",
    cursor: "pointer",
    outlineWidth: 2,
    outlineStyle: {
      default: "none",
      ":focus-visible": "solid",
    },
    outlineColor: ink.accent,
    outlineOffset: 0,
    backgroundColor: {
      default: "transparent",
      ":hover": color.surface0,
    },
    borderWidth: 0,
    borderRadius: 6,
  },
  mini: {
    flexShrink: 0,
    width: 14,
    height: 14,
    borderRadius: 4,
    boxShadow: `inset 0 0 0 1px ${color.surface2}`,
  },
  code: { overflow: "hidden", textOverflow: "ellipsis", fontFamily: font.mono, fontSize: 12.5 },
  ratio: {
    display: "block",
    marginTop: 2,
    marginLeft: 22,
    fontFamily: font.mono,
    fontSize: 11,
    color: color.subtext0,
  },
  use: { color: color.subtext0, textWrap: "pretty" },
});
