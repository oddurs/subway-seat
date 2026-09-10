"use client";

import * as stylex from "@stylexjs/stylex";
import Link from "next/link";
import { useDeferredValue, useState } from "react";
import { ink } from "@/theme/ink.stylex";
import { color } from "@/theme/tokens.stylex";
import { font } from "@/theme/type.stylex";

type Group = {
  category: string;
  label: string;
  ports: { id: string; name: string; auto: boolean }[];
};

// Each category runs on its own line color, like the trunk lines on the map.
const LINE: Record<string, string> = {
  Terminals: color.orange,
  Editors: color.yellow,
  Agents: color.clay,
  "Shell & prompt": color.green,
  "CLI & TUI": color.sage,
  Apps: color.denim,
  Desktop: color.subtext1,
  Palettes: color.redHi,
};

const squash = (s: string) => s.toLowerCase().replace(/[^a-z0-9]/g, "");

export function PortFinder({ groups }: { groups: Group[] }) {
  const [query, setQuery] = useState("");
  const [only, setOnly] = useState<string | null>(null);
  const q = squash(useDeferredValue(query));
  const total = groups.reduce((n, g) => n + g.ports.length, 0);

  const shown = groups
    .filter((g) => !only || g.category === only)
    .map((g) => ({
      ...g,
      ports: q
        ? g.ports.filter((p) => [p.name, p.id, g.label].some((s) => squash(s).includes(q)))
        : g.ports,
    }))
    .filter((g) => g.ports.length > 0);
  const count = shown.reduce((n, g) => n + g.ports.length, 0);

  return (
    <div {...stylex.props(styles.wrap)}>
      <search {...stylex.props(styles.bar)}>
        <label {...stylex.props(styles.field)}>
          <span className="sr-only">Find a port</span>
          <input
            type="search"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Find your app…"
            autoComplete="off"
            spellCheck={false}
            {...stylex.props(styles.input)}
          />
        </label>
        {/* biome-ignore lint/a11y/useSemanticElements: a group of toggle buttons */}
        <div role="group" aria-label="Category" {...stylex.props(styles.chips)}>
          <button
            type="button"
            aria-pressed={only === null}
            onClick={() => setOnly(null)}
            {...stylex.props(styles.chip, only === null && styles.chipOn)}
          >
            All
          </button>
          {groups.map((g) => (
            <button
              key={g.category}
              type="button"
              aria-pressed={only === g.category}
              onClick={() => setOnly(only === g.category ? null : g.category)}
              {...stylex.props(styles.chip, only === g.category && styles.chipOn)}
            >
              <span
                {...stylex.props(styles.chipDot, styles.fill(LINE[g.category] ?? color.orange))}
              />
              {g.label}
            </button>
          ))}
        </div>
        <p aria-live="polite" {...stylex.props(styles.count)}>
          {count === total ? `${total} ports` : `${count} of ${total} ports`}
        </p>
      </search>

      {shown.length === 0 && (
        <p {...stylex.props(styles.empty)}>
          No port for “{query}” yet.{" "}
          <a
            href="https://github.com/oddurs/subway-seat/issues/new?template=port-request.yml"
            {...stylex.props(styles.emptyLink)}
          >
            Ask for one
          </a>
          , or make it yourself: a port is one small Python file.
        </p>
      )}

      <div {...stylex.props(styles.groups)}>
        {shown.map(({ category, label, ports }) => (
          <section key={category} aria-label={label} {...stylex.props(styles.group)}>
            <h3 {...stylex.props(styles.heading)}>
              <span
                aria-hidden
                {...stylex.props(styles.dot, styles.fill(LINE[category] ?? color.orange))}
              />
              {label}
              <span {...stylex.props(styles.groupCount)}>{ports.length}</span>
            </h3>
            <div {...stylex.props(styles.grid)}>
              {ports.map((port) => (
                <Link
                  key={port.id}
                  href={`/ports/${port.id}`}
                  prefetch={false}
                  title={port.name}
                  {...stylex.props(styles.card)}
                >
                  <span
                    aria-hidden
                    {...stylex.props(styles.bullet, styles.fill(LINE[category] ?? color.orange))}
                  >
                    {port.name
                      .replace(/[^A-Za-z0-9]/g, "")
                      .charAt(0)
                      .toUpperCase()}
                  </span>
                  <span {...stylex.props(styles.name)}>{port.name}</span>
                  {port.auto && (
                    <span title="Follows light and dark" {...stylex.props(styles.auto)}>
                      <span aria-hidden>◐</span>
                      <span className="sr-only">, follows light and dark</span>
                    </span>
                  )}
                </Link>
              ))}
            </div>
          </section>
        ))}
      </div>
    </div>
  );
}

const focus = {
  outlineWidth: 2,
  outlineStyle: {
    default: "none",
    ":focus-visible": "solid",
  },
  outlineColor: ink.accent,
  outlineOffset: 2,
} as const;

const styles = stylex.create({
  wrap: { display: "grid", gridTemplateColumns: "minmax(0, 1fr)", gap: 30 },
  bar: { display: "flex", flexWrap: "wrap", gap: 12, alignItems: "center" },
  field: { flexGrow: 1, flexBasis: 260, maxWidth: 360 },
  input: {
    width: "100%",
    paddingBlock: 10,
    paddingInline: 16,
    fontFamily: font.sans,
    fontSize: 16,
    color: color.textHi,
    outlineStyle: "none",
    backgroundColor: color.base,
    borderColor: {
      default: color.surface1,
      ":focus": color.orange,
    },
    borderStyle: "solid",
    borderWidth: 1,
    borderRadius: 999,
    "::placeholder": { color: color.overlay2 },
  },
  chips: { display: "flex", flexWrap: "wrap", gap: 6 },
  chip: {
    display: "inline-flex",
    gap: 7,
    alignItems: "center",
    paddingBlock: 6,
    paddingInline: 12,
    fontFamily: font.sans,
    fontSize: 13.5,
    color: {
      default: color.subtext1,
      ":hover": color.textHi,
    },
    cursor: "pointer",
    backgroundColor: {
      default: "transparent",
      ":hover": color.base,
    },
    borderColor: color.surface1,
    borderStyle: "solid",
    borderWidth: 1,
    borderRadius: 999,
    ...focus,
  },
  chipOn: {
    color: color.textHi,
    backgroundColor: color.surface0,
    borderColor: color.surface2,
  },
  chipDot: { width: 9, height: 9, borderRadius: "50%" },
  count: { marginLeft: "auto", fontSize: 13.5, color: color.subtext0 },
  empty: { fontSize: 16, color: color.subtext0 },
  emptyLink: { color: { default: ink.accent, ":hover": ink.accentHover } },
  groups: { display: "grid", gridTemplateColumns: "minmax(0, 1fr)", gap: 34 },
  group: { display: "grid", gridTemplateColumns: "minmax(0, 1fr)", gap: 14 },
  heading: {
    display: "flex",
    gap: 10,
    alignItems: "center",
    fontFamily: font.display,
    fontSize: 24,
    fontVariationSettings: '"SOFT" 100',
    fontWeight: 700,
    color: color.textHi,
  },
  dot: { width: 14, height: 14, borderRadius: "50%" },
  groupCount: { fontFamily: font.sans, fontSize: 14, fontWeight: 400, color: color.overlay2 },
  grid: {
    display: "grid",
    gridTemplateColumns: {
      default: "repeat(auto-fill, minmax(200px, 1fr))",
      "@media (max-width: 640px)": "repeat(auto-fill, minmax(min(150px, 100%), 1fr))",
    },
    gap: 8,
  },
  card: {
    display: "flex",
    gap: 12,
    alignItems: "center",
    minWidth: 0,
    paddingBlock: 10,
    paddingInline: 12,
    color: color.text,
    textDecoration: "none",
    backgroundColor: {
      default: color.base,
      ":hover": color.surface0,
    },
    borderColor: {
      default: color.surface0,
      ":hover": color.surface2,
    },
    borderStyle: "solid",
    borderWidth: 1,
    borderRadius: 12,
    transitionDuration: "140ms",
    transitionProperty: "background-color, border-color",
    ...focus,
  },
  bullet: {
    display: "grid",
    flexShrink: 0,
    placeItems: "center",
    width: 30,
    height: 30,
    fontFamily: font.sans,
    fontSize: 15,
    fontWeight: 700,
    color: ink.onAccent,
    borderRadius: "50%",
  },
  fill: (bg: string) => ({ backgroundColor: bg }),
  auto: { flexShrink: 0, marginLeft: "auto", fontSize: 14, color: color.subtext0 },
  name: {
    overflow: "hidden",
    textOverflow: "ellipsis",
    fontSize: 15,
    fontWeight: 500,
    whiteSpace: "nowrap",
  },
});
