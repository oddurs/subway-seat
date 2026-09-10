import * as stylex from "@stylexjs/stylex";
import type { ReactNode } from "react";
import type { ColorName } from "@/lib/palette";
import { color } from "@/theme/tokens.stylex";
import { font } from "@/theme/type.stylex";
import { Window } from "./Window";

/** Coloured run of text; `k` is a palette name. */
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

function Perms({ mode }: { mode: string }) {
  const k = (ch: string): ColorName =>
    ch === "d"
      ? "denim"
      : ch === "r"
        ? "yellow"
        : ch === "w"
          ? "red"
          : ch === "x"
            ? "green"
            : "overlay0";
  return (
    <>
      {[...mode].map((ch, i) => (
        <C key={i} k={k(ch)}>
          {ch}
        </C>
      ))}
    </>
  );
}

/** fish in Ghostty: starship prompt, git, eza and ripgrep output. */
export function TerminalDemo() {
  return (
    <Window title="fish — ghostty">
      <div {...stylex.props(styles.screen)}>
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
        <div>
          <Perms mode="drwxr-xr-x" /> <C k="overlay0"> -</C> <C k="yellow">oddur</C>{" "}
          <C k="denim">10 Sep 12:48</C>{" "}
          <C k="denim" bold>
            dist
          </C>
        </div>
        <div>
          <Perms mode=".rw-r--r--" />{" "}
          <C k="green" bold>
            3.1k
          </C>{" "}
          <C k="yellow">oddur</C> <C k="denim">10 Sep 12:51</C> palette.py
        </div>
        <div>
          <Perms mode=".rwxr-xr-x" />{" "}
          <C k="green" bold>
            2.2k
          </C>{" "}
          <C k="yellow">oddur</C> <C k="denim">10 Sep 12:52</C>{" "}
          <C k="green" bold>
            install.fish
          </C>
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
    paddingBlock: 16,
    paddingInline: 18,
    overflowX: "auto",
    fontFamily: font.mono,
    fontSize: 14,
    lineHeight: 1.6,
    color: color.text,
    whiteSpace: "pre",
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
});
