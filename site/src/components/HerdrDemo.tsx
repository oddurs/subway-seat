import * as stylex from "@stylexjs/stylex";
import type { ReactNode } from "react";
import { walnut } from "@/lib/palette";
import { claudeTheme, flavorVars } from "@/lib/themeVars";
import { ink } from "@/theme/ink.stylex";
import { color } from "@/theme/tokens.stylex";
import { font } from "@/theme/type.stylex";
import { C } from "./TerminalDemo";
import { Window } from "./Window";

const SPACES = [
  { state: "yellow", name: "subway-seat", detail: "main", active: true },
  { state: "green", name: "extraction eval", detail: "eval/v3 +12" },
  { state: "redHi", name: "document formatting", detail: "docs ~2" },
  { state: "overlay0", name: "savaos", detail: "main" },
] as const;

const AGENTS = [
  { state: "yellow", name: "claude", detail: "working" },
  { state: "redHi", name: "claude", detail: "needs you" },
] as const;

type Row = { state: keyof typeof walnut.colors; name: string; detail: string; active?: boolean };

function SideRow({ row }: { row: Row }) {
  return (
    <div {...stylex.props(styles.row, row.active && styles.activeRow)}>
      <C k={row.state}>●</C>
      <span {...stylex.props(styles.rowName, row.active && styles.activeName)}>{row.name}</span>
      <span {...stylex.props(styles.rowDetail)}>{row.detail}</span>
    </div>
  );
}

function DiffLine({ sign, children }: { sign: "+" | "-"; children: ReactNode }) {
  return (
    <span {...stylex.props(styles.diff, sign === "+" ? styles.added : styles.removed)}>
      {"  "}
      <C k="overlay2">12</C> <C k={sign === "+" ? "green" : "redHi"}>{sign}</C> {children}
    </span>
  );
}

// Diff and prompt grounds come from the generated Claude Code theme itself.
function claudeVars() {
  return flavorVars(".claude-pane", (id) => {
    const t = claudeTheme(id);
    const pick = (key: string) => (t[key] ? { [`cc-${key}`]: t[key] } : {});
    return { ...pick("diffAdded"), ...pick("diffRemoved"), ...pick("userMessageBackground") };
  });
}

/** herdr's sidebar next to a Claude Code session using the custom theme. */
export function HerdrDemo() {
  return (
    <Window title="herdr — claude" label="herdr running Claude Code, Subway Seat theme">
      {/* biome-ignore lint/security/noDangerouslySetInnerHtml: generated CSS variables */}
      <style dangerouslySetInnerHTML={{ __html: claudeVars() }} />
      <div {...stylex.props(styles.split)}>
        <div {...stylex.props(styles.side)}>
          <div {...stylex.props(styles.head)}>SPACES</div>
          {SPACES.map((row) => (
            <SideRow key={row.name} row={row} />
          ))}
          <div {...stylex.props(styles.head)}>AGENTS</div>
          {AGENTS.map((row) => (
            <SideRow key={row.detail} row={row} />
          ))}
        </div>
        {/* biome-ignore lint/a11y/noNoninteractiveTabindex: a scrolling region must take focus */}
        <div
          tabIndex={0}
          role="region"
          aria-label="Claude Code session"
          className={`claude-pane ${stylex.props(styles.pane).className ?? ""}`}
        >
          <span {...stylex.props(styles.user)}>
            <C k="overlay1">❯</C> make the ground read brown, not black
          </span>
          {"\n\n"}
          <C k="green">⏺</C> <b>Update</b>(palette.py){"\n"}
          {"  "}
          <C k="overlay1">⎿</C> Updated palette.py with 1 addition and 1 removal{"\n"}
          <DiffLine sign="-">
            base = <C k="green">&quot;#2A1D14&quot;</C>
          </DiffLine>
          {"\n"}
          <DiffLine sign="+">
            base = <C k="green">&quot;{walnut.colors.base}&quot;</C>
          </DiffLine>
          {"\n\n"}⏺ Walnut now sits at 15% lightness, saturated enough{"\n"}
          {"  "}to read as wood paneling.{"\n\n"}
          <C k="orange">✻ Percolating…</C> <C k="overlay1">(6s · ↓ 312 tokens)</C>
          {"\n"}
          <span {...stylex.props(styles.input)}>
            <C k="overlay1">❯</C> <span {...stylex.props(styles.cursor)}> </span>
          </span>
          {"\n"}
          {"  "}
          <C k="clay">⏵⏵ accept edits on</C> <C k="overlay1">(shift+tab to cycle)</C>
        </div>
      </div>
    </Window>
  );
}

const NARROW = "@media (max-width: 720px)";
const WIDE = "@media (min-width: 1200px)";

const styles = stylex.create({
  split: {
    display: "grid",
    flexGrow: 1,
    gridTemplateColumns: {
      [NARROW]: "minmax(0, 1fr)",
      [WIDE]: "200px minmax(0, 1fr)",
      default: "230px minmax(0, 1fr)",
    },
  },
  side: {
    display: {
      [NARROW]: "none",
      default: "block",
    },
    paddingBlock: 12,
    fontFamily: font.mono,
    fontSize: 13,
    lineHeight: 1.5,
    backgroundColor: color.mantle,
    borderRightColor: color.crust,
    borderRightStyle: "solid",
    borderRightWidth: {
      [NARROW]: 0,
      default: 1,
    },
  },
  head: {
    paddingInline: 14,
    paddingTop: 10,
    paddingBottom: 4,
    fontSize: 11,
    color: color.overlay2,
    letterSpacing: "0.1em",
  },
  row: {
    display: "grid",
    gridTemplateColumns: "auto 1fr",
    columnGap: 8,
    paddingBlock: 5,
    paddingInline: 14,
  },
  activeRow: { backgroundColor: color.surface0 },
  rowName: {
    overflow: "hidden",
    textOverflow: "ellipsis",
    color: color.text,
    whiteSpace: "nowrap",
  },
  activeName: { color: color.textHi },
  rowDetail: { gridColumn: "2", fontSize: 12, color: color.overlay2 },
  pane: {
    paddingBlock: 16,
    paddingInline: 20,
    overflowX: "auto",
    fontFamily: font.mono,
    fontSize: {
      [NARROW]: 12,
      [WIDE]: 13,
      default: 13.5,
    },
    lineHeight: 1.6,
    color: color.text,
    whiteSpace: "pre",
    outlineWidth: 2,
    outlineStyle: {
      default: "none",
      ":focus-visible": "solid",
    },
    outlineColor: ink.accent,
    outlineOffset: -2,
  },
  user: {
    boxSizing: "border-box",
    display: "inline-block",
    width: "calc(100% + 40px)",
    paddingBlock: 4,
    paddingInline: 20,
    marginInline: -20,
    backgroundColor: `var(--cc-userMessageBackground, ${color.surface0})`,
  },
  diff: {
    boxSizing: "border-box",
    display: "inline-block",
    minWidth: "calc(100% + 40px)",
    paddingInline: 20,
    marginInline: -20,
  },
  added: { backgroundColor: "var(--cc-diffAdded)" },
  removed: { backgroundColor: "var(--cc-diffRemoved)" },
  input: {
    display: "inline-block",
    width: "min(100%, 44ch)",
    paddingBlock: 2,
    paddingInline: 8,
    borderColor: color.overlay0,
    borderStyle: "solid",
    borderWidth: 1,
    borderRadius: 6,
  },
  cursor: { backgroundColor: color.text },
});
