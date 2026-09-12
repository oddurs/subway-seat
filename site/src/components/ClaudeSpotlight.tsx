import * as stylex from "@stylexjs/stylex";
import Link from "next/link";
import type { ReactNode } from "react";
import { readDist } from "@/lib/dist";
import { portById } from "@/lib/manifest";
import { type Family, families, flavorById, flavorsOf, shortName } from "@/lib/palette";
import { claudeTheme, flavorVars } from "@/lib/themeVars";
import { color } from "@/theme/tokens.stylex";
import { font } from "@/theme/type.stylex";
import { CodeBlock } from "./CodeBlock";
import { Ticker } from "./Ticker";
import { Window } from "./Window";

// A Claude Code session, drawn cell for cell the way v2.1.268 draws it in an
// 80-column terminal (checked against tmux captures of the real thing). Claude
// Code's own colors come from the generated theme file, per flavor; the status
// line and subagent rows are what the plugin's scripts print for this session.

type Settings = { spinnerVerbs: { verbs: string[] }; spinnerTipsOverride: { label: string } };
type Tips = { tips: { text: string }[] };

/**
 * Two of these rows name things that belong to a family rather than to the
 * plugin — which flavors it ships, and what it says while it thinks — so they
 * are built per city and the page shows the one you're riding.
 */
const included = (fam: Family) => [
  [
    "A theme for every flavor",
    `${flavorsOf(fam.id)
      .map((f) => shortName(f.id))
      .join(", ")}, with every one of Claude Code's color tokens set. Each also comes in a “terminal colors” version that colors code in diffs with your terminal's palette instead of Claude Code's Monokai.`,
  ],
  [
    "A station-sign status line",
    "The model as a bullet, where you are, the line you're on, how full the car is, and the fare or your plan's pass.",
  ],
  [
    "Subagent rows",
    "Each helper gets a bullet colored by its state and its own little load meter.",
  ],
  [
    "Spinner verbs",
    `${fam.verbs
      .slice(0, 3)
      .map((v) => `“${v}”`)
      .join(", ")}…`,
  ],
  ["“Next stop” tips", "Real Claude Code tips, in the same unhurried voice."],
  ["A relaxed output style", "Warm and plain-spoken, never at the expense of being exact."],
];

// Claude Code keeps these no matter the theme: its syntax highlighter uses
// Monokai Extended over a dark base and GitHub over a light one, removed lines
// stay plain, and the +/- signs have their own green and red.
const FIXED = {
  dark: {
    code: "#F8F8F2",
    keyword: "#F92672",
    key: "#A6E22E",
    number: "#BE84FF",
    string: "#E6DB74",
    sign_add: "#50C850",
    sign_del: "#DC5A5A",
  },
  light: {
    code: "#333333",
    keyword: "#A71D5D",
    key: "#0086B3",
    number: "#0086B3",
    string: "#183691",
    sign_add: "#248A3D",
    sign_del: "#CF222E",
  },
};

// The theme tokens this screen uses, as --cc-* variables for each flavor.
const TOKENS = [
  "text",
  "inverseText",
  "inactive",
  "subtle",
  "claude",
  "success",
  "autoAccept",
  "promptBorder",
  "userMessageBackground",
  "diffAdded",
  "diffRemoved",
  "diffAddedWord",
  "diffRemovedWord",
  "clawd_body",
  "clawd_background",
];

function screenVars() {
  return flavorVars(".claude-screen", (id) => {
    const theme = claudeTheme(id);
    const fixed = flavorById[id].dark ? FIXED.dark : FIXED.light;
    return {
      ...Object.fromEntries(TOKENS.filter((k) => theme[k]).map((k) => [`cc-${k}`, theme[k]])),
      ...Object.fromEntries(Object.entries(fixed).map(([k, v]) => [`cc-fixed-${k}`, v])),
    };
  });
}

const cc = (token: string) => `var(--cc-${token})`;

/** A run of text in one color (a CSS color or a --cc token), optionally bold. */
function T({ c, b, children }: { c?: string; b?: boolean; children: ReactNode }) {
  return (
    <span {...stylex.props(c !== undefined && styles.fg(c), b && styles.bold)}>{children}</span>
  );
}

/** One terminal row; wrapped text continues under the text after `hang` cells, as Claude Code wraps. */
function Row({ hang = 0, children }: { hang?: number; children?: ReactNode }) {
  return <div {...stylex.props(styles.row, styles.hang(`${hang}ch`))}>{children ?? " "}</div>;
}

/** The route bullet the scripts draw: a Nerd Font round cap, a letter cell, a round cap. */
function Bullet({ line, letter }: { line: string; letter: string }) {
  return (
    <span aria-hidden {...stylex.props(styles.bullet)}>
      <svg
        viewBox="0 0 3 2"
        preserveAspectRatio="none"
        {...stylex.props(styles.pill, styles.fg(line))}
      >
        <path d="M1 0h1a1 1 0 0 1 0 2H1a1 1 0 0 1 0-2z" fill="currentColor" />
      </svg>
      <span {...stylex.props(styles.letter)}>{letter}</span>
    </span>
  );
}

/** Nerd Font's branch glyph (U+E0A0), one cell wide. */
function Branch() {
  return (
    <svg viewBox="0 0 6 13" aria-hidden {...stylex.props(styles.glyph)}>
      <path
        d="M1.6 2.2v8.6M1.6 7.6c0-1.6 2.8-1.6 2.8-3.2V2.2"
        fill="none"
        stroke="currentColor"
        strokeWidth="1.1"
      />
    </svg>
  );
}

/**
 * One cell for a symbol the web font lacks (❯ ⏺ ◯ ⏵), so a fallback font's
 * wider glyph can't push the rest of the row off the grid.
 */
function G({ ch, c, w = 1 }: { ch: string; c?: string; w?: number }) {
  return (
    <span {...stylex.props(styles.cell, styles.width(`${w}ch`), c !== undefined && styles.fg(c))}>
      {ch}
    </span>
  );
}

// Box-drawing corners as a terminal draws them: lines through the cell's middle,
// out to its edges (x and y in tenths of the cell).
const TREE = {
  "├": "M5 0V10M5 5H10",
  "└": "M5 0V5H10",
  "⎿": "M5 0V8.5H10",
};

/** ├, └ or ⎿, one cell wide and one row tall. */
function Tree({ ch, c }: { ch: keyof typeof TREE; c?: string }) {
  return (
    <svg
      viewBox="0 0 10 10"
      preserveAspectRatio="none"
      aria-hidden
      {...stylex.props(styles.glyph, c !== undefined && styles.fg(c))}
    >
      <path d={TREE[ch]} fill="none" stroke="currentColor" vectorEffect="non-scaling-stroke" />
    </svg>
  );
}

/**
 * A meter as the scripts print it, ━ cells filled and ─ for the rest. Drawn as
 * lines through the middle of each cell, the way a terminal draws box characters.
 */
function Meter({ fill, cells, c }: { fill: number; cells: number; c: string }) {
  return (
    <span aria-hidden>
      {fill > 0 && (
        <span {...stylex.props(styles.heavy, styles.width(`${fill}ch`), styles.fg(c))} />
      )}
      {cells > fill && (
        <span
          {...stylex.props(
            styles.light,
            styles.width(`${cells - fill}ch`),
            styles.fg(color.surface2),
          )}
        />
      )}
    </span>
  );
}

// Clawd, from the welcome header's quadrant characters ( ▐▛███▛█ / ▝▜██████▀ /
//   ▝▝ ▝▝): 9 cells by 3 rows at two quadrants a cell. `#` is body, `o` an eye.
const CLAWD = [
  "...#############..",
  "...##o#######o##..",
  ".#################",
  "...#############..",
  ".....#.#...#.#....",
];

function Clawd() {
  const rects: ReactNode[] = [];
  CLAWD.forEach((row, y) => {
    [...row].forEach((ch, x) => {
      if (ch === "#" || ch === "o")
        rects.push(
          <rect
            key={`${x}-${y}`}
            x={x}
            y={y}
            width={1.02}
            height={1.02}
            fill={ch === "o" ? cc("clawd_background") : cc("clawd_body")}
          />,
        );
    });
  });
  return (
    <svg viewBox="0 0 18 6" preserveAspectRatio="none" aria-hidden {...stylex.props(styles.clawd)}>
      {rects}
    </svg>
  );
}

/** Claude Code's spinner glyph, which breathes · ✢ ✳ ✶ ✻ ✽ and back. */
const FRAMES = ["·", "✢", "✳", "✶", "✻", "✽", "✽", "✻", "✶", "✳", "✢", "·"];

function Spinner() {
  return (
    <span aria-hidden {...stylex.props(styles.spinner)}>
      {FRAMES.map((glyph, i) => (
        <span
          // biome-ignore lint/suspicious/noArrayIndexKey: frames repeat on purpose
          key={i}
          {...stylex.props(styles.frame, styles.delay(`${(i - FRAMES.length) * 120}ms`))}
        >
          {glyph}
        </span>
      ))}
      <span {...stylex.props(styles.still)}>✻</span>
    </span>
  );
}

/** A diff row: the gutter's line number and sign, then the code, on the line's tint. */
function DiffRow({ n, sign, children }: { n: number; sign?: "+" | "-"; children: ReactNode }) {
  const gutter = ` ${String(n).padStart(2)} ${sign ?? " "}`;
  return (
    <div
      {...stylex.props(
        styles.row,
        styles.diff,
        sign === "+" && styles.bg(cc("diffAdded")),
        sign === "-" && styles.bg(cc("diffRemoved")),
      )}
    >
      {sign ? (
        <T c={cc(sign === "+" ? "fixed-sign_add" : "fixed-sign_del")}>{gutter}</T>
      ) : (
        <span {...stylex.props(styles.dim)}>{gutter.slice(0, -1)}</span>
      )}
      {sign ? "" : " "}
      <T c={cc("fixed-code")}>{children}</T>
    </div>
  );
}

function Word({ sign, children }: { sign: "+" | "-"; children: ReactNode }) {
  return (
    <span {...stylex.props(styles.bg(cc(sign === "+" ? "diffAddedWord" : "diffRemovedWord")))}>
      {children}
    </span>
  );
}

const K = (text: string) => <T c={cc("fixed-key")}>{text}</T>;
const N = (text: string) => <T c={cc("fixed-number")}>{text}</T>;
const S = (text: string) => <T c={cc("fixed-string")}>{text}</T>;

/**
 * A row of the subagent panel: Claude Code's ◯, then what the plugin's script
 * prints for a running agent. Like the script, the row gives up the "doing"
 * text first when it runs out of room.
 */
function AgentRow({
  letter,
  name,
  doing,
  fill,
  tokens,
}: {
  letter: string;
  name: string;
  doing?: string;
  fill: number;
  tokens: string;
}) {
  return (
    <div {...stylex.props(styles.row, styles.agent)}>
      <span {...stylex.props(styles.fixed, styles.fg(cc("inactive")))}>
        {"  "}
        <G ch="◯" />{" "}
      </span>
      <Bullet line={color.yellow} letter={letter} />
      <span {...stylex.props(styles.name, styles.gap("1ch"), styles.fg(color.text))}>{name}</span>
      {doing && (
        <span {...stylex.props(styles.doing, styles.gap("2ch"), styles.fg(color.overlay2))}>
          {doing}
        </span>
      )}
      <span {...stylex.props(styles.fixed, styles.gap("2ch"))}>
        <Meter fill={fill} cells={5} c={color.yellow} />
      </span>
      <span {...stylex.props(styles.fixed, styles.gap("2ch"), styles.fg(color.overlay1))}>
        {tokens}
      </span>
    </div>
  );
}

/** A rule of box-drawing characters as wide as the terminal. */
function Rule() {
  return <div aria-hidden {...stylex.props(styles.row, styles.rule)} />;
}

/** Claude Code, themed all the way down. */
export async function ClaudeSpotlight() {
  const settings = JSON.parse(readDist("claude-code/plugin/settings/subway-seat.json")) as Settings;
  const tips = (JSON.parse(readDist("claude-code/plugin/tips.json")) as Tips).tips.map(
    (t) => `${settings.spinnerTipsOverride.label}: ${t.text}`,
  );
  // The port's own install steps, without the "pick a flavor" comment.
  const install = (portById("claude-code")?.enable?.walnut.code ?? "")
    .split("\n")
    .map((line) => line.replace(/\s+#.*$/, ""))
    .join("\n");

  return (
    <div {...stylex.props(styles.layout)}>
      <Window title="claude — ghostty" label="Claude Code in Ghostty, Subway Seat theme">
        {/* biome-ignore lint/security/noDangerouslySetInnerHtml: generated CSS variables */}
        <style dangerouslySetInnerHTML={{ __html: screenVars() }} />
        {/* biome-ignore lint/a11y/noNoninteractiveTabindex: a scrolling region must take focus */}
        <div
          tabIndex={0}
          role="region"
          aria-label="Claude Code session"
          className={`claude-screen ${stylex.props(styles.screen).className ?? ""}`}
        >
          <div {...stylex.props(styles.header)}>
            <Clawd />
            <div>
              <Row>
                <T b>Claude Code</T> <T c={cc("inactive")}>v2.1.268</T>
              </Row>
              <Row>
                <T c={cc("inactive")}>Opus 4.7 · Claude Max</T>
              </Row>
              <Row>
                <T c={cc("inactive")}>~/Code/subway-seat</T>
              </Row>
            </div>
          </div>
          <Row />
          <Row />
          <Row hang={2}>
            <span {...stylex.props(styles.user)}>
              <G ch="❯" c={cc("subtle")} />{" "}
              <T c={cc("text")}>find me a window seat, and check the seat tests still pass </T>
            </span>
          </Row>
          <Row />
          <Row hang={2}>
            <G ch="⏺" c={cc("success")} /> <T b>2</T> background agents launched{" "}
            <T c={cc("inactive")}>(↓ to manage)</T>
          </Row>
          <Row hang={5}>
            {"   "}
            <Tree ch="├" c={cc("inactive")} /> <T b>Compare seat maps for the R46</T>
          </Row>
          <Row hang={5}>
            {"   "}
            <Tree ch="└" c={cc("inactive")} /> <T b>Run the seat tests</T>
          </Row>
          <Row />
          <Row hang={2}>
            {"  "}
            <T c={cc("inactive")}>
              Read <T b>1</T> file
            </T>
          </Row>
          <Row />
          <Row hang={2}>
            <G ch="⏺" c={cc("success")} /> <T b>Update</T>(src/car.ts)
          </Row>
          <Row hang={5}>
            <T c={cc("inactive")}>
              {"  "}
              <Tree ch="⎿" />
              {"  "}
            </T>
            Added <T b>1</T> line, removed <T b>1</T> line
          </Row>
          <DiffRow n={9}>
            {"  "}
            {K("car")}: {N("7431")},
          </DiffRow>
          <DiffRow n={10}>
            {"  "}
            {K("row")}: {N("7")},
          </DiffRow>
          <DiffRow n={11}>
            {"  "}
            {K("line")}: {S('"F"')},
          </DiffRow>
          <DiffRow n={12} sign="-">
            {"  "}window: <Word sign="-">false</Word>,
          </DiffRow>
          <DiffRow n={12} sign="+">
            {"  "}
            {K("window")}: <Word sign="+">{N("true")}</Word>,
          </DiffRow>
          <DiffRow n={13}>{"};"}</DiffRow>
          <Row />
          <Row hang={2}>
            <G ch="⏺" c={cc("text")} /> Row 7 on the F has the window, and it faces forward.
            I&apos;ve marked it; the seat tests are still running.
          </Row>
          <Row />
          <Row hang={2}>
            <T c={cc("claude")}>
              <Spinner />{" "}
              <span {...stylex.props(styles.flow)}>
                <Ticker items={settings.spinnerVerbs.verbs} suffix="…" />
              </span>
            </T>{" "}
            <T c={cc("inactive")}>(14s · ↓ 1.8k tokens)</T>
          </Row>
          <Row hang={5}>
            <T c={cc("inactive")}>
              {"  "}
              <Tree ch="⎿" />
              {"  "}
              <span {...stylex.props(styles.flow)}>
                <Ticker items={tips} every={5200} />
              </span>
            </T>
          </Row>
          <Row />
          <Rule />
          <Row>
            <G ch="❯" c={cc("inactive")} /> <span {...stylex.props(styles.cursor)}> </span>
          </Row>
          <Rule />
          {/* What the status line script prints for this session: Opus 4.7 (1M context),
              ~/Code/subway-seat on main with 2 changes, 42% of the context, $0.84. */}
          <div {...stylex.props(styles.row, styles.status)}>
            <span {...stylex.props(styles.segment)}>
              <Bullet line={color.orange} letter="O" /> <T c={color.text}>Opus 4.7</T>
            </span>
            <span {...stylex.props(styles.segment)}>
              <T c={color.subtext1}>~/Code/subway-seat</T>
            </span>
            <span {...stylex.props(styles.segment)}>
              <T c={color.yellow}>
                <Branch /> main
              </T>{" "}
              <T c={color.clay}>!2</T>
            </span>
            <span {...stylex.props(styles.segment)}>
              <T c={color.overlay1}>load</T> <Meter fill={4} cells={10} c={color.green} />{" "}
              <T c={color.overlay2}> 42%</T>
            </span>
            <span {...stylex.props(styles.segment)}>
              <T c={color.overlay2}>$0.84</T>
            </span>
          </div>
          <Row hang={2}>
            {"  "}
            <T c={cc("autoAccept")}>
              <G ch="⏵⏵" w={2} /> accept edits on
            </T>{" "}
            <T c={cc("inactive")}>(shift+tab to cycle)</T>
          </Row>
          <Row />
          <Row>
            <T b>
              {"  "}
              <G ch="⏺" /> main
            </T>
          </Row>
          {/* The subagent script's rows for two running Agent calls. */}
          <AgentRow
            letter="C"
            name="Compare seat maps for the R46"
            doing="Reading docs/cars/r46.md"
            fill={1}
            tokens="42.1k"
          />
          <AgentRow letter="R" name="Run the seat tests" fill={0} tokens="8.4k" />
        </div>
      </Window>
      <div {...stylex.props(styles.side)}>
        <p {...stylex.props(styles.intro)}>
          Most themes stop at colors. This one follows Claude Code into every corner it lets you
          touch, and it all comes as one plugin.
        </p>
        {families.map((fam) => (
          <ul key={fam.id} data-only={fam.id} {...stylex.props(styles.list)}>
            {included(fam).map(([title, body]) => (
              <li key={title} {...stylex.props(styles.item)}>
                <b {...stylex.props(styles.itemTitle)}>{title}</b> {body}
              </li>
            ))}
          </ul>
        ))}
        <CodeBlock lang="text" code={install} copy label="Install the Claude Code plugin" />
        <Link href="/ports/claude-code" {...stylex.props(styles.more)}>
          Every file in the plugin →
        </Link>
      </div>
    </div>
  );
}

const NARROW = "@media (max-width: 1100px)";
const REDUCED = "@media (prefers-reduced-motion: reduce)";

const breathe = stylex.keyframes({
  "0%": { opacity: 1 },
  "8.33%": { opacity: 0 },
  "100%": { opacity: 0 },
});

const styles = stylex.create({
  layout: {
    display: "grid",
    gridTemplateColumns: {
      [NARROW]: "minmax(0, 1fr)",
      default: "minmax(0, 1.45fr) minmax(0, 1fr)",
    },
    gap: 32,
    alignItems: "start",
  },
  screen: {
    paddingBlock: 16,
    paddingInline: 16,
    containerType: "inline-size",
    overflowX: "auto",
    fontFamily: font.mono,
    fontSize: {
      default: 13,
      "@media (max-width: 520px)": 11.5,
    },
    lineHeight: 1.4,
    color: color.text,
    backgroundColor: color.base,
  },
  row: {
    minHeight: "1lh",
    overflowWrap: "anywhere",
    whiteSpace: "pre-wrap",
  },
  hang: (hang: string) => ({ paddingLeft: hang, textIndent: `calc(-1 * ${hang})` }),
  fg: (c: string) => ({ color: c }),
  bg: (c: string) => ({ backgroundColor: c }),
  bold: { fontWeight: 700 },
  dim: { opacity: 0.55 },
  header: {
    display: "flex",
    gap: "2ch",
    alignItems: "flex-start",
  },
  clawd: {
    flexShrink: 0,
    width: "9ch",
    height: "3lh",
    shapeRendering: "crispEdges",
  },
  user: {
    boxDecorationBreak: "clone",
    backgroundColor: "var(--cc-userMessageBackground)",
  },
  diff: {
    paddingLeft: "5ch",
    marginRight: "6ch",
    marginLeft: "5ch",
    textIndent: "-5ch",
  },
  bullet: {
    position: "relative",
    display: "inline-block",
    flexShrink: 0,
    width: "3ch",
    textAlign: "center",
    textIndent: 0,
  },
  pill: {
    position: "absolute",
    inset: 0,
    width: "100%",
    height: "100%",
  },
  letter: {
    position: "relative",
    fontWeight: 700,
    color: "var(--cc-inverseText)",
  },
  glyph: {
    display: "inline-block",
    width: "1ch",
    height: "1lh",
    verticalAlign: "top",
  },
  spinner: {
    position: "relative",
    display: "inline-block",
    width: "1ch",
    textIndent: 0,
  },
  frame: {
    position: "absolute",
    insetInlineStart: 0,
    opacity: 0,
    animationName: { [REDUCED]: "none", default: breathe },
    animationDuration: "1440ms",
    animationTimingFunction: "step-end",
    animationIterationCount: "infinite",
  },
  delay: (delay: string) => ({ animationDelay: delay }),
  still: {
    visibility: { [REDUCED]: "visible", default: "hidden" },
  },
  rule: {
    color: "var(--cc-promptBorder)",
    backgroundImage: "linear-gradient(currentColor, currentColor)",
    backgroundRepeat: "no-repeat",
    backgroundPosition: "center",
    backgroundSize: "100% 1px",
  },
  cell: {
    display: "inline-block",
    textAlign: "center",
    textIndent: 0,
  },
  width: (width: string) => ({ width }),
  heavy: {
    display: "inline-block",
    height: "1lh",
    verticalAlign: "top",
    backgroundImage: "linear-gradient(currentColor, currentColor)",
    backgroundRepeat: "no-repeat",
    backgroundPosition: "center",
    backgroundSize: "100% 2px",
  },
  light: {
    display: "inline-block",
    height: "1lh",
    verticalAlign: "top",
    backgroundImage: "linear-gradient(currentColor, currentColor)",
    backgroundRepeat: "no-repeat",
    backgroundPosition: "center",
    backgroundSize: "100% 1px",
  },
  cursor: { backgroundColor: color.text },
  // The status line drops whole segments from the right when the row is too narrow, as the script does.
  status: {
    display: "flex",
    flexWrap: "wrap",
    columnGap: "3ch",
    height: "1lh",
    paddingLeft: "2ch",
    overflow: "hidden",
    whiteSpace: "pre",
  },
  segment: { flexShrink: 0 },
  agent: {
    display: "flex",
    overflow: "hidden",
    whiteSpace: "pre",
  },
  name: {
    flexShrink: 1,
    minWidth: "4ch",
    overflow: "hidden",
    textOverflow: "ellipsis",
  },
  // Like the script, the row drops the "doing" text rather than squeeze it
  // (below 8 columns): this row needs about 61 columns to keep it.
  doing: {
    display: { default: null, "@container (max-width: 62ch)": "none" },
    flexShrink: 1000,
    minWidth: 0,
    overflow: "hidden",
    textOverflow: "ellipsis",
  },
  fixed: { flexShrink: 0 },
  gap: (gap: string) => ({ marginLeft: gap }),
  flow: { display: "inline-block", textIndent: 0 },
  side: { display: "grid", gridTemplateColumns: "minmax(0, 1fr)", gap: 18 },
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
