"use client";

import * as stylex from "@stylexjs/stylex";
import { useDeferredValue, useId, useState, useSyncExternalStore } from "react";
import { currentFlavor, subscribeFlavor } from "@/lib/flavor";
import {
  CONFIG_PATH,
  cloneCommand,
  configFile,
  type Extra,
  INSTALL_URL,
  type InstallFlavor,
  installCommand,
} from "@/lib/install";
import type { Setup } from "@/lib/manifest";
import { ink } from "@/theme/ink.stylex";
import { color } from "@/theme/tokens.stylex";
import { font } from "@/theme/type.stylex";
import { Command } from "./Command";

export type InstallPort = {
  id: string;
  name: string;
  category: string;
  label: string;
  setup: Setup;
  detect: boolean;
  auto: boolean;
};

export type FlavorPaint = {
  id: InstallFlavor;
  name: string;
  note: string;
  bg: string;
  /** A second ground laid over bg (Auto is half Enamel). */
  image?: string;
  fg: string;
  sub: string;
  stripe: string[];
};

type Mode = "detect" | "only" | "all";
type Tab = "line" | "config" | "clone";

const SETUP: Record<Setup, { label: string; hint: string }> = {
  auto: { label: "automatic", hint: "Linked and switched on for you" },
  step: {
    label: "one step",
    hint: "Linked for you; the installer tells you the one thing to do by hand",
  },
  manual: { label: "by hand", hint: "Nothing to link; the installer prints the steps" },
};

const EXTRAS: { id: Extra; label: string; hint: string }[] = [
  { id: "dry-run", label: "Just show me the plan", hint: "Prints what it would do and stops" },
  {
    id: "no-enable",
    label: "Leave my config files alone",
    hint: "Links the themes but adds no lines",
  },
  { id: "copy", label: "Copy files instead of linking", hint: "Copies won't update on git pull" },
];

/** The setup configurator: a flavor, some stops, and a ticket to paste. */
export function Configurator({
  ports,
  paints,
  categories,
}: {
  ports: InstallPort[];
  paints: FlavorPaint[];
  categories: { category: string; label: string }[];
}) {
  // Starts on the flavor you're riding, until you pick one here.
  const riding = useSyncExternalStore(subscribeFlavor, currentFlavor, () => "walnut" as const);
  const [choice, setFlavor] = useState<InstallFlavor | null>(null);
  const flavor = choice ?? riding;
  const [mode, setMode] = useState<Mode>("detect");
  const [picked, setPicked] = useState<Set<string>>(() => new Set());
  const [skipped, setSkipped] = useState<Set<string>>(() => new Set());
  const [extras, setExtras] = useState<Set<Extra>>(() => new Set());
  const [query, setQuery] = useState("");
  const [only, setOnly] = useState<string | null>(null);
  const [tab, setTab] = useState<Tab>("line");
  const id = useId();
  const q = useDeferredValue(query)
    .toLowerCase()
    .replace(/[^a-z0-9]/g, "");

  const knowsDetect = ports.some((p) => p.detect);
  const inOrder = (set: Set<string>) => ports.filter((p) => set.has(p.id)).map((p) => p.id);
  const plan = {
    flavor,
    all: mode === "all",
    only: mode === "only" ? inOrder(picked) : undefined,
    skip: mode === "detect" ? inOrder(skipped) : undefined,
    extras: EXTRAS.map((e) => e.id).filter((e) => extras.has(e)),
  };
  const empty = mode === "only" && picked.size === 0;
  const chosen =
    mode === "only"
      ? ports.filter((p) => picked.has(p.id))
      : mode === "all"
        ? ports
        : ports.filter((p) => !skipped.has(p.id) && (p.detect || !knowsDetect));
  const tally = (s: Setup) => chosen.filter((p) => p.setup === s).length;

  const visible = ports.filter(
    (p) =>
      (!only || p.category === only) &&
      (!q ||
        [p.name, p.id, p.label].some((s) =>
          s
            .toLowerCase()
            .replace(/[^a-z0-9]/g, "")
            .includes(q),
        )),
  );

  function toggle(set: Set<string>, update: (s: Set<string>) => void, pid: string) {
    const next = new Set(set);
    if (next.has(pid)) next.delete(pid);
    else next.add(pid);
    update(next);
  }

  const checked = (p: InstallPort) =>
    mode === "all" ? true : mode === "only" ? picked.has(p.id) : !skipped.has(p.id);

  const ticket =
    tab === "line" ? installCommand(plan) : tab === "clone" ? cloneCommand(plan) : configFile(plan);

  return (
    <div {...stylex.props(s.layout)}>
      <ol {...stylex.props(s.route)}>
        {/* ── 1. Flavor ─────────────────────────────────────────── */}
        <li {...stylex.props(s.stop)}>
          <span aria-hidden {...stylex.props(s.station)}>
            1
          </span>
          <fieldset {...stylex.props(s.fieldset)}>
            <legend {...stylex.props(s.stopTitle)}>Pick your flavor</legend>
            <div {...stylex.props(s.flavors)}>
              {paints.map((p) => (
                <label
                  key={p.id}
                  {...stylex.props(
                    s.flavor,
                    s.paint(p.bg, p.image ?? "none", p.fg),
                    flavor === p.id && s.flavorOn,
                  )}
                >
                  <input
                    type="radio"
                    name={`${id}-flavor`}
                    value={p.id}
                    checked={flavor === p.id}
                    onChange={() => setFlavor(p.id)}
                    className="sr-only"
                  />
                  <span aria-hidden {...stylex.props(s.flavorStripe)}>
                    {p.stripe.map((c) => (
                      <i key={c} {...stylex.props(s.band, s.fill(c))} />
                    ))}
                  </span>
                  <span {...stylex.props(s.flavorName)}>{p.name}</span>
                  <span {...stylex.props(s.flavorNote, s.ink(p.sub))}>{p.note}</span>
                </label>
              ))}
            </div>
            {flavor === "auto" && (
              <p {...stylex.props(s.aside)}>
                Apps that can follow your system&apos;s light and dark mode switch on their own;{" "}
                {ports.filter((p) => p.auto).length} ports know how.
              </p>
            )}
          </fieldset>
        </li>

        {/* ── 2. Apps ───────────────────────────────────────────── */}
        <li {...stylex.props(s.stop)}>
          <span aria-hidden {...stylex.props(s.station)}>
            2
          </span>
          <fieldset {...stylex.props(s.fieldset)}>
            <legend {...stylex.props(s.stopTitle)}>Pick your stops</legend>
            <div {...stylex.props(s.modes)}>
              {(
                [
                  [
                    "detect",
                    "Whatever I have",
                    "It looks for each app and themes the ones it finds.",
                  ],
                  ["only", "Just these", "Only the apps you tick below."],
                  ["all", "Everything", `All ${ports.length} ports. Handy on a fresh machine.`],
                ] as const
              ).map(([m, label, hint]) => (
                <label key={m} {...stylex.props(s.mode, mode === m && s.modeOn)}>
                  <input
                    type="radio"
                    name={`${id}-mode`}
                    value={m}
                    checked={mode === m}
                    onChange={() => setMode(m)}
                    className="sr-only"
                  />
                  <span aria-hidden {...stylex.props(s.modeDot, mode === m && s.modeDotOn)} />
                  <span>
                    <b {...stylex.props(s.modeLabel)}>{label}</b>
                    <span {...stylex.props(s.modeHint)}>{hint}</span>
                  </span>
                </label>
              ))}
            </div>

            {mode !== "all" && (
              <div {...stylex.props(s.picker)}>
                <p {...stylex.props(s.aside)}>
                  {mode === "detect"
                    ? `Untick anything you'd rather keep as it is.${knowsDetect && ports.some((p) => !p.detect) ? " Dimmed apps can't be spotted on their own; pick them with Just these." : ""}`
                    : "Tick the apps you want themed."}{" "}
                  <span {...stylex.props(s.legend)}>
                    {(Object.keys(SETUP) as Setup[]).map((k) => (
                      <span key={k} title={SETUP[k].hint} {...stylex.props(s.legendItem)}>
                        <i aria-hidden {...stylex.props(s.setupDot, s[`setup_${k}`])} />
                        {SETUP[k].label}
                      </span>
                    ))}
                  </span>
                </p>
                <div {...stylex.props(s.filters)}>
                  <label {...stylex.props(s.search)}>
                    <span className="sr-only">Find an app</span>
                    <input
                      type="search"
                      value={query}
                      onChange={(e) => setQuery(e.target.value)}
                      placeholder="Find an app…"
                      autoComplete="off"
                      spellCheck={false}
                      {...stylex.props(s.input)}
                    />
                  </label>
                  <select
                    aria-label="Category"
                    value={only ?? ""}
                    onChange={(e) => setOnly(e.target.value || null)}
                    {...stylex.props(s.select)}
                  >
                    <option value="">Every category</option>
                    {categories.map((c) => (
                      <option key={c.category} value={c.category}>
                        {c.label}
                      </option>
                    ))}
                  </select>
                  {mode === "only" && picked.size > 0 && (
                    <button
                      type="button"
                      onClick={() => setPicked(new Set())}
                      {...stylex.props(s.clear)}
                    >
                      Clear {picked.size}
                    </button>
                  )}
                  {mode === "detect" && skipped.size > 0 && (
                    <button
                      type="button"
                      onClick={() => setSkipped(new Set())}
                      {...stylex.props(s.clear)}
                    >
                      Put back {skipped.size}
                    </button>
                  )}
                </div>
                <div {...stylex.props(s.apps)}>
                  {categories.map((c) => {
                    const group = visible.filter((p) => p.category === c.category);
                    if (!group.length) return null;
                    const all = group.every((p) =>
                      mode === "only" ? picked.has(p.id) : !skipped.has(p.id),
                    );
                    const flip = () => {
                      const ids = group.map((p) => p.id);
                      if (mode === "only") {
                        const next = new Set(picked);
                        for (const pid of ids) {
                          if (all) next.delete(pid);
                          else next.add(pid);
                        }
                        setPicked(next);
                      } else {
                        const next = new Set(skipped);
                        for (const pid of ids) {
                          if (all) next.add(pid);
                          else next.delete(pid);
                        }
                        setSkipped(next);
                      }
                    };
                    return (
                      <div
                        key={c.category}
                        role="group"
                        aria-label={c.label}
                        {...stylex.props(s.group)}
                      >
                        <div {...stylex.props(s.groupHead)}>
                          <span>{c.label}</span>
                          <button type="button" onClick={flip} {...stylex.props(s.groupFlip)}>
                            {all ? "none" : "all"}
                            <span className="sr-only"> of {c.label}</span>
                          </button>
                        </div>
                        {group.map((p) => {
                          const off = mode === "detect" && knowsDetect && !p.detect;
                          return (
                            <label
                              key={p.id}
                              title={
                                off
                                  ? "The installer can't spot this one; pick it with Just these"
                                  : SETUP[p.setup].hint
                              }
                              {...stylex.props(
                                s.app,
                                checked(p) && !off && s.appOn,
                                off && s.appOff,
                              )}
                            >
                              <input
                                type="checkbox"
                                checked={checked(p) && !off}
                                disabled={off}
                                onChange={() =>
                                  mode === "only"
                                    ? toggle(picked, setPicked, p.id)
                                    : toggle(skipped, setSkipped, p.id)
                                }
                                {...stylex.props(s.check)}
                              />
                              <span {...stylex.props(s.appName)}>{p.name}</span>
                              <i aria-hidden {...stylex.props(s.setupDot, s[`setup_${p.setup}`])} />
                              <span className="sr-only">, {SETUP[p.setup].label}</span>
                            </label>
                          );
                        })}
                      </div>
                    );
                  })}
                  {visible.length === 0 && <p {...stylex.props(s.aside)}>No app by that name.</p>}
                </div>
              </div>
            )}
          </fieldset>
        </li>

        {/* ── 3. Ticket ─────────────────────────────────────────── */}
        <li {...stylex.props(s.stop, s.lastStop)}>
          <span aria-hidden {...stylex.props(s.station)}>
            3
          </span>
          <section aria-labelledby={`${id}-ticket`} {...stylex.props(s.ticket)}>
            <h2 id={`${id}-ticket`} {...stylex.props(s.stopTitle)}>
              Punch your ticket
            </h2>
            <p {...stylex.props(s.summary)}>
              {mode === "detect"
                ? `The apps you have${skipped.size ? `, minus ${skipped.size}` : ""}`
                : mode === "all"
                  ? `All ${ports.length} ports`
                  : `${picked.size} app${picked.size === 1 ? "" : "s"}`}
              {!empty && mode !== "detect" && (
                <>
                  : {tally("auto")} automatic, {tally("step")} with one step
                  {tally("manual") ? `, ${tally("manual")} by hand` : ""}
                </>
              )}
              .
            </p>
            <div role="tablist" aria-label="How to run it" {...stylex.props(s.tabs)}>
              {(
                [
                  ["line", "One line"],
                  ["config", "Config file"],
                  ["clone", "From a clone"],
                ] as const
              ).map(([t, label]) => (
                <button
                  key={t}
                  id={`${id}-${t}`}
                  type="button"
                  role="tab"
                  aria-selected={tab === t}
                  aria-controls={`${id}-panel`}
                  tabIndex={tab === t ? 0 : -1}
                  onClick={() => setTab(t)}
                  onKeyDown={(e) => {
                    const order: Tab[] = ["line", "config", "clone"];
                    const step = e.key === "ArrowRight" ? 1 : e.key === "ArrowLeft" ? -1 : 0;
                    if (!step) return;
                    const next = order[(order.indexOf(tab) + step + 3) % 3];
                    setTab(next);
                    document.getElementById(`${id}-${next}`)?.focus();
                  }}
                  {...stylex.props(s.tab, tab === t && s.tabOn)}
                >
                  {label}
                </button>
              ))}
            </div>
            <div id={`${id}-panel`} role="tabpanel" aria-labelledby={`${id}-${tab}`}>
              {empty ? (
                <p {...stylex.props(s.aside)}>Tick at least one app and your line appears here.</p>
              ) : (
                <>
                  {tab === "config" && (
                    <p {...stylex.props(s.path)}>
                      Save as <code>{CONFIG_PATH}</code>
                    </p>
                  )}
                  <Command text={ticket} kind={tab === "config" ? "config" : "shell"} sunk />
                  {tab === "config" && (
                    <p {...stylex.props(s.aside)}>
                      Then a bare run picks it up, and so does every{" "}
                      <code {...stylex.props(s.inline)}>switch</code>:
                    </p>
                  )}
                  {tab === "config" && <Command text={`curl -fsSL ${INSTALL_URL} | sh`} sunk />}
                </>
              )}
            </div>
            {tab !== "config" && (
              <fieldset {...stylex.props(s.extras)}>
                <legend className="sr-only">Options</legend>
                {EXTRAS.map((e) => (
                  <label key={e.id} title={e.hint} {...stylex.props(s.extra)}>
                    <input
                      type="checkbox"
                      checked={extras.has(e.id)}
                      onChange={() => {
                        const next = new Set(extras);
                        if (next.has(e.id)) next.delete(e.id);
                        else next.add(e.id);
                        setExtras(next);
                      }}
                      {...stylex.props(s.check)}
                    />
                    {e.label}
                  </label>
                ))}
              </fieldset>
            )}
            <p {...stylex.props(s.fine)}>
              It shows the plan and asks once before touching anything. Read it first if you like:{" "}
              <a href={INSTALL_URL} {...stylex.props(s.link)}>
                install.sh
              </a>
              .
            </p>
          </section>
        </li>
      </ol>
    </div>
  );
}

const focus = {
  outlineColor: ink.accent,
  outlineWidth: 2,
  outlineOffset: 2,
} as const;

const RAIL = 6;
const NARROW = "@media (max-width: 720px)";

const s = stylex.create({
  layout: { display: "grid", gridTemplateColumns: "minmax(0, 1fr)" },
  route: {
    position: "relative",
    display: "grid",
    gridTemplateColumns: "minmax(0, 1fr)",
    gap: 44,
    listStyle: "none",
    "::before": {
      position: "absolute",
      top: 20,
      bottom: 40,
      left: { [NARROW]: 15, default: 19 },
      width: RAIL,
      content: '""',
      backgroundColor: color.orange,
      borderRadius: RAIL,
    },
  },
  stop: { position: "relative", minWidth: 0, paddingLeft: { [NARROW]: 50, default: 68 } },
  lastStop: {},
  station: {
    position: "absolute",
    top: 0,
    left: 0,
    display: "grid",
    placeItems: "center",
    width: { [NARROW]: 36, default: 44 },
    height: { [NARROW]: 36, default: 44 },
    fontFamily: font.sans,
    fontSize: { [NARROW]: 18, default: 22 },
    fontWeight: 700,
    color: color.textHi,
    backgroundColor: color.mantle,
    borderColor: color.orange,
    borderStyle: "solid",
    borderWidth: RAIL,
    borderRadius: "50%",
  },
  fieldset: { display: "grid", gap: 16, minWidth: 0, borderWidth: 0 },
  stopTitle: {
    paddingTop: { [NARROW]: 2, default: 4 },
    marginBottom: 4,
    fontFamily: font.display,
    fontSize: 28,
    fontVariationSettings: '"SOFT" 100, "WONK" 1',
    fontWeight: 700,
    lineHeight: 1.2,
    color: color.textHi,
  },
  flavors: {
    display: "grid",
    gridTemplateColumns: "repeat(auto-fit, minmax(150px, 1fr))",
    gap: 12,
  },
  flavor: {
    position: "relative",
    display: "grid",
    gap: 4,
    alignContent: "start",
    minHeight: 104,
    padding: 14,
    paddingTop: 22,
    overflow: "hidden",
    cursor: "pointer",
    outlineStyle: {
      default: "none",
      ":has(:focus-visible)": "solid",
    },
    borderColor: "rgba(128,100,70,0.35)",
    borderStyle: "solid",
    borderWidth: 1,
    borderRadius: 14,
    boxShadow: "0 10px 26px var(--ss-shadow-soft)",
    ...focus,
    transform: {
      default: null,
      ":hover": "translateY(-2px)",
    },
    transitionDuration: "160ms",
    transitionProperty: "transform, box-shadow",
  },
  flavorOn: {
    boxShadow: `0 0 0 3px ${color.orange}, 0 10px 26px var(--ss-shadow-soft)`,
  },
  paint: (bg: string, image: string, fg: string) => ({
    color: fg,
    backgroundColor: bg,
    backgroundImage: image,
  }),
  ink: (fg: string) => ({ color: fg }),
  fill: (bg: string) => ({ backgroundColor: bg }),
  flavorStripe: { position: "absolute", top: 0, right: 0, left: 0, display: "flex", height: 8 },
  band: { flexGrow: 1 },
  flavorName: {
    fontFamily: font.display,
    fontSize: 24,
    fontVariationSettings: '"SOFT" 100, "WONK" 1',
    fontWeight: 700,
    lineHeight: 1.1,
  },
  flavorNote: { fontSize: 13.5, lineHeight: 1.4, textWrap: "pretty" },
  aside: { fontSize: 14.5, color: color.subtext0, textWrap: "pretty" },
  modes: {
    display: "grid",
    gridTemplateColumns: "repeat(auto-fit, minmax(190px, 1fr))",
    gap: 10,
  },
  mode: {
    display: "flex",
    gap: 12,
    alignItems: "flex-start",
    paddingBlock: 12,
    paddingInline: 14,
    cursor: "pointer",
    outlineStyle: {
      default: "none",
      ":has(:focus-visible)": "solid",
    },
    backgroundColor: {
      default: "transparent",
      ":hover": color.base,
    },
    borderColor: color.surface1,
    borderStyle: "solid",
    borderWidth: 1,
    borderRadius: 12,
    ...focus,
  },
  modeOn: { backgroundColor: color.base, borderColor: color.orange },
  modeDot: {
    flexShrink: 0,
    width: 18,
    height: 18,
    marginTop: 2,
    borderColor: color.surface2,
    borderStyle: "solid",
    borderWidth: 2,
    borderRadius: "50%",
  },
  modeDotOn: { borderColor: color.orange, borderWidth: 6 },
  modeLabel: { display: "block", fontWeight: 700, color: color.textHi },
  modeHint: { display: "block", fontSize: 13.5, lineHeight: 1.45, color: color.subtext0 },
  picker: { display: "grid", gap: 12, minWidth: 0 },
  legend: { display: "inline-flex", flexWrap: "wrap", gap: 12, marginLeft: 6 },
  legendItem: { display: "inline-flex", gap: 6, alignItems: "center", whiteSpace: "nowrap" },
  setupDot: { flexShrink: 0, width: 9, height: 9, borderRadius: "50%" },
  setup_auto: { backgroundColor: color.green },
  setup_step: { backgroundColor: color.yellow },
  setup_manual: { backgroundColor: color.overlay1 },
  filters: { display: "flex", flexWrap: "wrap", gap: 8, alignItems: "center" },
  search: { flexGrow: 1, flexBasis: 220, maxWidth: 320 },
  input: {
    width: "100%",
    paddingBlock: 8,
    paddingInline: 14,
    fontFamily: font.sans,
    fontSize: 15,
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
  select: {
    paddingBlock: 8,
    paddingInline: 12,
    fontFamily: font.sans,
    fontSize: 14,
    color: color.text,
    outlineStyle: {
      default: "none",
      ":focus-visible": "solid",
    },
    backgroundColor: color.base,
    borderColor: color.surface1,
    borderStyle: "solid",
    borderWidth: 1,
    borderRadius: 999,
    ...focus,
  },
  clear: {
    paddingBlock: 6,
    paddingInline: 10,
    fontSize: 13.5,
    color: {
      default: ink.accent,
      ":hover": ink.accentHover,
    },
    textDecorationLine: "underline",
    textUnderlineOffset: 3,
    cursor: "pointer",
    backgroundColor: "transparent",
    borderWidth: 0,
  },
  apps: {
    display: "grid",
    gridTemplateColumns: "repeat(auto-fill, minmax(min(100%, 176px), 1fr))",
    rowGap: 2,
    columnGap: 6,
    maxHeight: 420,
    padding: 10,
    overflowY: "auto",
    backgroundColor: color.base,
    borderColor: color.surface0,
    borderStyle: "solid",
    borderWidth: 1,
    borderRadius: 14,
  },
  group: { display: "contents" },
  groupHead: {
    display: "flex",
    gridColumnStart: "1",
    gridColumnEnd: "-1",
    gap: 10,
    alignItems: "baseline",
    paddingInline: 10,
    paddingTop: 10,
    paddingBottom: 2,
    fontSize: 12,
    fontWeight: 600,
    color: color.subtext0,
    textTransform: "uppercase",
    letterSpacing: "0.12em",
  },
  groupFlip: {
    padding: 0,
    fontSize: 12,
    color: {
      default: ink.accent,
      ":hover": ink.accentHover,
    },
    textTransform: "none",
    letterSpacing: "normal",
    textDecorationLine: "underline",
    textUnderlineOffset: 3,
    cursor: "pointer",
    backgroundColor: "transparent",
    borderWidth: 0,
  },
  app: {
    display: "flex",
    gap: 9,
    alignItems: "center",
    minWidth: 0,
    paddingBlock: 6,
    paddingInline: 10,
    fontSize: 14,
    color: color.subtext0,
    cursor: "pointer",
    backgroundColor: {
      default: "transparent",
      ":hover": color.surface0,
    },
    borderRadius: 8,
  },
  appOn: { color: color.textHi },
  appOff: { cursor: "not-allowed", opacity: 0.55 },
  check: { flexShrink: 0, width: 16, height: 16, accentColor: color.orange, cursor: "inherit" },
  appName: { flexGrow: 1, overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" },
  ticket: {
    display: "grid",
    gap: 14,
    minWidth: 0,
    padding: { [NARROW]: 16, default: 24 },
    backgroundColor: color.base,
    backgroundImage: `radial-gradient(circle at 0 50%, ${color.mantle} 11px, transparent 12px), radial-gradient(circle at 100% 50%, ${color.mantle} 11px, transparent 12px)`,
    borderColor: color.surface1,
    borderStyle: "dashed",
    borderWidth: 1,
    borderRadius: 16,
    boxShadow: "0 18px 40px var(--ss-shadow-soft)",
  },
  summary: { fontSize: 15, color: color.subtext1 },
  tabs: { display: "flex", flexWrap: "wrap", gap: 4 },
  tab: {
    paddingBlock: 6,
    paddingInline: 14,
    fontSize: 14,
    color: {
      default: color.subtext0,
      ":hover": color.textHi,
    },
    cursor: "pointer",
    outlineStyle: {
      default: "none",
      ":focus-visible": "solid",
    },
    backgroundColor: "transparent",
    borderColor: color.surface1,
    borderStyle: "solid",
    borderWidth: 1,
    borderRadius: 999,
    ...focus,
  },
  tabOn: { color: ink.onAccent, backgroundColor: color.orange, borderColor: color.orange },
  path: { marginBottom: 8, fontSize: 13.5, color: color.subtext0 },
  inline: { fontFamily: font.mono, fontSize: "0.9em", color: ink.code },
  extras: { display: "flex", flexWrap: "wrap", rowGap: 6, columnGap: 18, borderWidth: 0 },
  extra: {
    display: "inline-flex",
    gap: 8,
    alignItems: "center",
    fontSize: 14,
    color: color.subtext1,
    cursor: "pointer",
  },
  fine: { fontSize: 13.5, color: color.subtext0 },
  link: { color: { default: ink.accent, ":hover": ink.accentHover } },
});
