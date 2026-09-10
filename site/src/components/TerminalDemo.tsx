import * as stylex from "@stylexjs/stylex";
import type { ReactNode } from "react";
import type { ColorName } from "@/lib/palette";
import { ezaTheme, flavorVars } from "@/lib/themeVars";
import { ink } from "@/theme/ink.stylex";
import { color } from "@/theme/tokens.stylex";
import { font } from "@/theme/type.stylex";
import { Window } from "./Window";

/** Colored run of text; `k` is a palette name. */
export function C({ k, bold, children }: { k: ColorName; bold?: boolean; children: ReactNode }) {
  return <span {...stylex.props(styles.fg(color[k]), bold && styles.bold)}>{children}</span>;
}

// Starship's Gruvbox Rainbow layout with the Subway Seat palette:
// the segments run red → orange → gold → avocado, then a brown clock.
const SEGMENTS: { bg: ColorName; fg: ColorName; text: string }[] = [
  { bg: "red", fg: "crust", text: " oddur" },
  { bg: "orange", fg: "crust", text: "~/Code/subway-seat" },
  { bg: "yellow", fg: "crust", text: "⎇ main !2" },
  { bg: "green", fg: "crust", text: "⬢ v26.4" },
  { bg: "surface1", fg: "subtext1", text: "◷ 12:48" },
];

function Prompt({ children }: { children?: ReactNode }) {
  return (
    <>
      <div {...stylex.props(styles.prompt)}>
        {SEGMENTS.map((seg, i) => {
          const next = SEGMENTS[i + 1];
          return (
            <span key={seg.text} {...stylex.props(styles.segWrap)}>
              <span
                {...stylex.props(styles.seg, styles.bg(color[seg.bg]), styles.fg(color[seg.fg]))}
              >
                {seg.text}
              </span>
              <span {...stylex.props(styles.arrow, next && styles.bg(color[next.bg]))}>
                <span {...stylex.props(styles.tip, styles.bg(color[seg.bg]))} />
              </span>
            </span>
          );
        })}
      </div>
      <div>
        <C k="green" bold>
          ❯
        </C>{" "}
        {children}
      </div>
    </>
  );
}

// eza keys the `ll` rows use; their colors come from the generated eza theme.
const EZA = [
  "filekinds.directory",
  "filekinds.normal",
  "filekinds.executable",
  "punctuation",
  "date",
  "users.user_you",
  "size.number_kilo",
  "size.unit_kilo",
  ...["user", "group", "other"].flatMap((who) =>
    ["read", "write", who === "user" ? "execute_file" : "execute", "execute_other"].map(
      (what) => `perms.${who}_${what}`,
    ),
  ),
];

const ezaVar = (key: string) => `--eza-${key.replace(/\./g, "-")}`;

function ezaVars() {
  return flavorVars(".eza", (id) => {
    const theme = ezaTheme(id);
    const vars: Record<string, string> = {};
    for (const key of EZA) {
      const style = theme[key];
      vars[ezaVar(key).slice(2)] = style?.fg ?? "inherit";
      vars[`${ezaVar(key).slice(2)}-w`] = style?.bold ? "700" : "400";
    }
    return vars;
  });
}

/** A run of text in one of eza's theme colors. */
function E({ k, children }: { k: string; children: ReactNode }) {
  return (
    <span {...stylex.props(styles.eza(`var(${ezaVar(k)})`, `var(${ezaVar(k)}-w)`))}>
      {children}
    </span>
  );
}

/** `drwxr-xr-x` the way eza colors it: each bit by who and what, gaps as punctuation. */
function Perms({ mode }: { mode: string }) {
  const who = ["user", "user", "user", "group", "group", "group", "other", "other", "other"];
  const dir = mode[0] === "d";
  const key = (ch: string, i: number) => {
    if (i === 0) return dir ? "filekinds.directory" : "punctuation";
    const w = who[i - 1];
    if (ch === "r") return `perms.${w}_read`;
    if (ch === "w") return `perms.${w}_write`;
    if (ch === "x")
      return w === "user"
        ? `perms.user_${dir ? "execute_other" : "execute_file"}`
        : `perms.${w}_execute`;
    return "punctuation";
  };
  return (
    <>
      {[...mode].map((ch, i) => (
        // biome-ignore lint/suspicious/noArrayIndexKey: fixed positions
        <E key={i} k={key(ch, i)}>
          {ch}
        </E>
      ))}
    </>
  );
}

/** fish in Ghostty: starship prompt, git, eza and ripgrep output. */
export function TerminalDemo() {
  return (
    <Window title="fish — ghostty" label="fish in Ghostty with the Subway Seat theme">
      {/* biome-ignore lint/security/noDangerouslySetInnerHtml: generated CSS variables */}
      <style dangerouslySetInnerHTML={{ __html: ezaVars() }} />
      {/* biome-ignore lint/a11y/noNoninteractiveTabindex: a scrolling region must take focus */}
      <div tabIndex={0} role="region" aria-label="Terminal output" {...stylex.props(styles.screen)}>
        <Prompt>
          <C k="yellow">git</C> commit <C k="sage">-m</C>{" "}
          <C k="green">&quot;stand clear of the closing doors&quot;</C>
        </Prompt>
        <div>
          [main <C k="yellow">4d0899a</C>] stand clear of the closing doors
        </div>
        <div>
          {" "}
          2 files changed, <C k="green">14 insertions(+)</C>, <C k="red">3 deletions(-)</C>
        </div>
        <br />
        <Prompt>
          <C k="yellow">ll</C>
        </Prompt>
        <div className="eza">
          <Perms mode="drwxr-xr-x" /> <E k="punctuation"> -</E> <E k="users.user_you">oddur</E>{" "}
          <E k="date">10 Sep 12:48</E> <E k="filekinds.directory">dist</E>
        </div>
        <div className="eza">
          <Perms mode=".rw-r--r--" /> <E k="size.number_kilo">3.1</E>
          <E k="size.unit_kilo">k</E> <E k="users.user_you">oddur</E> <E k="date">10 Sep 12:51</E>{" "}
          <E k="filekinds.normal">palette.py</E>
        </div>
        <div className="eza">
          <Perms mode=".rwxr-xr-x" /> <E k="size.number_kilo">2.2</E>
          <E k="size.unit_kilo">k</E> <E k="users.user_you">oddur</E> <E k="date">10 Sep 12:52</E>{" "}
          <E k="filekinds.executable">install.sh</E>
        </div>
        <br />
        <Prompt>
          <C k="yellow">rg</C> <C k="green">arrival</C>
        </Prompt>
        <div>
          <C k="orange">src/board.ts</C>
        </div>
        <div>
          <C k="green">10</C>: async next
          <C k="redHi" bold>
            Arrival
          </C>
          (line: Line, stop = 42)
        </div>
        <div>
          <C k="green">31</C>: const eta ={" "}
          <C k="redHi" bold>
            arrival
          </C>
          .minutes;
        </div>
        <br />
        <Prompt>
          <span {...stylex.props(styles.cursor)}> </span>
          <C k="overlay0">cd ~/Code/savaos</C>
        </Prompt>
      </div>
    </Window>
  );
}

const styles = stylex.create({
  screen: {
    flexGrow: 1,
    paddingBlock: 16,
    paddingInline: 18,
    overflowX: "auto",
    fontFamily: font.mono,
    fontSize: {
      default: 14,
      "@media (max-width: 720px)": 12,
      "@media (min-width: 1200px)": 13,
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
  prompt: { display: "flex", width: "max-content" },
  segWrap: { display: "flex" },
  seg: { paddingInline: "0.5ch" },
  arrow: { display: "block", width: "0.7em" },
  tip: {
    display: "block",
    width: "100%",
    height: "100%",
    clipPath: "polygon(0 0, 100% 50%, 0 100%)",
  },
  cursor: { color: color.base, backgroundColor: color.yellow },
  bg: (bg: string) => ({ backgroundColor: bg }),
  fg: (fg: string) => ({ color: fg }),
  bold: { fontWeight: 700 },
  eza: (fg: string, weight: string) => ({ fontWeight: weight, color: fg }),
});
