import * as stylex from "@stylexjs/stylex";
import Link from "next/link";
import type { ReactNode } from "react";
import { readDist } from "@/lib/dist";
import { color } from "@/theme/tokens.stylex";
import { font } from "@/theme/type.stylex";
import { CodeBlock } from "./CodeBlock";
import { C } from "./TerminalDemo";
import { Ticker } from "./Ticker";
import { Window } from "./Window";

type Settings = { spinnerVerbs: { verbs: string[] } };
type Tips = { tips: { text: string }[] };

const INCLUDED = [
  [
    "Three themes",
    "Walnut, Tunnel and Enamel, with every token set, down to the ultrathink rainbow.",
  ],
  [
    "A station-sign status line",
    "Model as a route bullet, the line you're on, how full the car is, the fare so far.",
  ],
  ["Subagent rows", "Each helper gets a bullet coloured by state and its own little load meter."],
  ["Spinner verbs", "“Sinking into the shag”, “Flipping the record”, “Changing at 14th Street”…"],
  ["“Next stop” tips", "Real Claude Code tips, in the same unhurried voice."],
  ["A relaxed output style", "Warm and plain-spoken, never at the expense of being exact."],
];

function Bullet({ bg, children }: { bg: string; children: ReactNode }) {
  return <span {...stylex.props(styles.bullet, styles.bg(bg))}>{children}</span>;
}

/** Claude Code, themed all the way down. */
export async function ClaudeSpotlight() {
  const settings = JSON.parse(readDist("claude-code/plugin/settings/subway-seat.json")) as Settings;
  const tips = (JSON.parse(readDist("claude-code/plugin/tips.json")) as Tips).tips.map(
    (t) => t.text,
  );

  return (
    <div {...stylex.props(styles.layout)}>
      <Window title="claude — ghostty">
        <div {...stylex.props(styles.screen)}>
          <span {...stylex.props(styles.user)}>
            <C k="overlay1">&gt;</C> find me a seat by the window
          </span>
          {"\n\n"}
          <C k="green">⏺</C> <b>Read</b>(src/car.ts){"\n"}
          {"  "}
          <C k="overlay1">⎿</C> Read 48 lines{"\n\n"}
          <C k="text">⏺</C> Row 7 has the window seat, and it faces forward. I&apos;ve put it in
          {"\n"}
          {"  "}
          <C k="yellow">seats.reserve()</C> so it&apos;s held for the ride.{"\n\n"}
          <C k="orange">
            ✻ <Ticker items={settings.spinnerVerbs.verbs} suffix="…" />
          </C>{" "}
          <C k="overlay1">(esc to interrupt)</C>
          {"\n"}
          {"  "}
          <C k="overlay1">⎿</C> <C k="overlay1">Next stop:</C>{" "}
          <C k="subtext0">
            <Ticker items={tips} every={5200} />
          </C>
          {"\n\n"}
          <span {...stylex.props(styles.agent)}>
            <Bullet bg={color.yellow}>R</Bullet> <C k="text">researcher</C>
            {"  "}
            <C k="overlay1">Comparing seat maps for the R46</C>
            {"  "}
            <C k="yellow">━━</C>
            <C k="surface2">───</C> <C k="overlay0">42.1k</C>
          </span>
          {"\n"}
          <span {...stylex.props(styles.agent)}>
            <Bullet bg={color.green}>T</Bullet> <C k="text">tester</C>
            {"  "}
            <C k="overlay1">All 12 seats pass</C>
            {"  "}
            <C k="green">━</C>
            <C k="surface2">────</C> <C k="overlay0">8.4k</C>
          </span>
          {"\n\n"}
          <span {...stylex.props(styles.prompt)}>
            <C k="overlay1">&gt;</C> <span {...stylex.props(styles.cursor)}> </span>
          </span>
          {"\n"}
          <Bullet bg={color.orange}>O</Bullet> <C k="text">Opus</C>
          {"   "}
          <C k="subtext1">~/Code/subway-seat</C>
          {"   "}
          <C k="yellow">main</C> <C k="clay">!2</C>
          {"   "}
          <C k="overlay0">load</C> <C k="green">━━━━</C>
          <C k="surface2">──────</C> <C k="overlay1"> 42%</C>
          {"   "}
          <C k="overlay1">$0.84</C>
        </div>
      </Window>
      <div {...stylex.props(styles.side)}>
        <p {...stylex.props(styles.intro)}>
          Most themes stop at colours. This one follows Claude Code into every corner it lets you
          touch, and it all comes as one plugin.
        </p>
        <ul {...stylex.props(styles.list)}>
          {INCLUDED.map(([title, body]) => (
            <li key={title} {...stylex.props(styles.item)}>
              <b {...stylex.props(styles.itemTitle)}>{title}</b> {body}
            </li>
          ))}
        </ul>
        <CodeBlock
          lang="text"
          code={
            "/plugin marketplace add oddurs/subway-seat\n/plugin install subway-seat@subway-seat\n/subway-seat:setup"
          }
        />
        <Link href="/ports/claude-code" {...stylex.props(styles.more)}>
          Every file in the plugin →
        </Link>
      </div>
    </div>
  );
}

const NARROW = "@media (max-width: 960px)";

const styles = stylex.create({
  layout: {
    display: "grid",
    gridTemplateColumns: {
      [NARROW]: "minmax(0, 1fr)",
      default: "minmax(0, 1.25fr) minmax(0, 1fr)",
    },
    gap: 32,
    alignItems: "start",
  },
  screen: {
    paddingBlock: 18,
    paddingInline: 20,
    overflowX: "auto",
    fontFamily: font.mono,
    fontSize: 13.5,
    lineHeight: 1.65,
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
  agent: { display: "inline-block" },
  bullet: {
    display: "inline-grid",
    placeItems: "center",
    width: "1.6em",
    height: "1.25em",
    fontWeight: 700,
    verticalAlign: "-0.15em",
    color: color.crust,
    borderRadius: 999,
  },
  bg: (bg: string) => ({ backgroundColor: bg }),
  prompt: {
    display: "inline-block",
    width: "min(100%, 48ch)",
    paddingBlock: 2,
    paddingInline: 8,
    borderColor: color.overlay0,
    borderStyle: "solid",
    borderWidth: 1,
    borderRadius: 6,
  },
  cursor: { backgroundColor: color.text },
  side: { display: "grid", gap: 18 },
  intro: { fontSize: 18, lineHeight: 1.55, color: color.subtext1, textWrap: "pretty" },
  list: { display: "grid", gap: 10, listStyle: "none" },
  item: { fontSize: 15, lineHeight: 1.5, color: color.subtext0 },
  itemTitle: { color: color.textHi },
  more: {
    fontWeight: 600,
    color: {
      default: color.orange,
      ":hover": color.orangeHi,
    },
    textDecoration: "none",
  },
});
