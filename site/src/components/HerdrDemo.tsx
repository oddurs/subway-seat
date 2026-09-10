import * as stylex from "@stylexjs/stylex";
import type { ReactNode } from "react";
import { walnut } from "@/lib/palette";
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
      <C k="overlay1">12</C> <C k={sign === "+" ? "green" : "redHi"}>{sign}</C> {children}
    </span>
  );
}

/** herdr's sidebar next to a Claude Code session using the custom theme. */
export function HerdrDemo() {
  return (
    <Window title="herdr — claude">
      <div {...stylex.props(styles.split)}>
        <aside {...stylex.props(styles.side)}>
          <div {...stylex.props(styles.head)}>SPACES</div>
          {SPACES.map((row) => (
            <SideRow key={row.name} row={row} />
          ))}
          <div {...stylex.props(styles.head)}>AGENTS</div>
          {AGENTS.map((row) => (
            <SideRow key={row.detail} row={row} />
          ))}
        </aside>
        <div {...stylex.props(styles.pane)}>
          <span {...stylex.props(styles.user)}>
            <C k="overlay1">&gt;</C> make the ground read brown, not black
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
          <C k="orange">✻ Percolating…</C> <C k="overlay1">(esc to interrupt)</C>
          {"\n"}
          <span {...stylex.props(styles.input)}>
            <C k="overlay1">&gt;</C> <span {...stylex.props(styles.cursor)}> </span>
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

const styles = stylex.create({
  split: {
    display: "grid",
    gridTemplateColumns: {
      [NARROW]: "1fr",
      default: "230px 1fr",
    },
  },
  side: {
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
    color: color.overlay0,
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
  rowDetail: { gridColumn: "2", fontSize: 12, color: color.overlay1 },
  pane: {
    paddingBlock: 16,
    paddingInline: 20,
    overflowX: "auto",
    fontFamily: font.mono,
    fontSize: 13.5,
    lineHeight: 1.6,
    color: color.text,
    whiteSpace: "pre",
  },
  user: {
    boxSizing: "border-box",
    display: "inline-block",
    width: "calc(100% + 40px)",
    paddingBlock: 4,
    paddingInline: 20,
    marginInline: -20,
    backgroundColor: color.surface0,
  },
  diff: { display: "inline-block", minWidth: "100%" },
  added: { backgroundColor: `color-mix(in srgb, ${color.green} 20%, ${color.base})` },
  removed: { backgroundColor: `color-mix(in srgb, ${color.red} 22%, ${color.base})` },
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
