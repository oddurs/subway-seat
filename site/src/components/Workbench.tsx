import * as stylex from "@stylexjs/stylex";
import type { DecorationItem, ShikiTransformer } from "shiki";
import { highlight, workbenchColors } from "@/lib/highlight";
import { type FlavorId, flavors } from "@/lib/palette";
import { font } from "@/theme/type.stylex";

// A VS Code window painted with the generated VS Code theme itself: every color
// below is a workbench key from dist/vscode, swapped per flavor with CSS variables.

const KEYS = [
  "titleBar.activeBackground",
  "titleBar.activeForeground",
  "titleBar.border",
  "commandCenter.background",
  "commandCenter.border",
  "commandCenter.foreground",
  "activityBar.background",
  "activityBar.foreground",
  "activityBar.inactiveForeground",
  "activityBar.activeBorder",
  "activityBarBadge.background",
  "activityBarBadge.foreground",
  "sideBar.background",
  "sideBar.foreground",
  "sideBar.border",
  "sideBarTitle.foreground",
  "sideBarSectionHeader.background",
  "sideBarSectionHeader.foreground",
  "sideBarSectionHeader.border",
  "list.hoverBackground",
  "list.activeSelectionBackground",
  "list.activeSelectionForeground",
  "list.focusOutline",
  "list.highlightForeground",
  "tree.indentGuidesStroke",
  "gitDecoration.modifiedResourceForeground",
  "gitDecoration.untrackedResourceForeground",
  "editorGroupHeader.tabsBackground",
  "editorGroupHeader.tabsBorder",
  "tab.border",
  "tab.activeBackground",
  "tab.activeForeground",
  "tab.activeBorderTop",
  "tab.activeBorder",
  "tab.inactiveBackground",
  "tab.inactiveForeground",
  "tab.hoverBackground",
  "tab.activeModifiedBorder",
  "breadcrumb.foreground",
  "breadcrumb.focusForeground",
  "editor.background",
  "editor.foreground",
  "editor.lineHighlightBackground",
  "editor.selectionBackground",
  "editor.wordHighlightBackground",
  "editor.wordHighlightStrongBackground",
  "editor.findMatchBackground",
  "editor.findMatchBorder",
  "editor.findMatchHighlightBackground",
  "editorBracketMatch.background",
  "editorBracketMatch.border",
  "editorLineNumber.foreground",
  "editorLineNumber.activeForeground",
  "editorCursor.foreground",
  "editorIndentGuide.background1",
  "editorGutter.modifiedBackground",
  "editorGutter.addedBackground",
  "scrollbarSlider.background",
  "editorSuggestWidget.background",
  "editorSuggestWidget.border",
  "editorSuggestWidget.foreground",
  "editorSuggestWidget.selectedBackground",
  "editorSuggestWidget.selectedForeground",
  "editorSuggestWidget.highlightForeground",
  "widget.shadow",
  "panel.background",
  "panel.border",
  "panelTitle.activeForeground",
  "panelTitle.activeBorder",
  "panelTitle.inactiveForeground",
  "terminal.foreground",
  "terminal.ansiGreen",
  "terminal.ansiYellow",
  "terminal.ansiRed",
  "terminal.ansiMagenta",
  "terminal.ansiBrightBlack",
  "terminal.ansiCyan",
  "statusBar.background",
  "statusBar.foreground",
  "statusBar.border",
  "statusBarItem.remoteBackground",
  "statusBarItem.remoteForeground",
  "statusBarItem.warningForeground",
  "symbolIcon.methodForeground",
  "symbolIcon.propertyForeground",
  "symbolIcon.fieldForeground",
] as const;

const cssVar = (key: string) => `--vsc-${key.replace(/\./g, "-")}`;

function variables() {
  const block = (id: FlavorId) => {
    const c = workbenchColors(id);
    return KEYS.map((k) => `${cssVar(k)}:${c[k] ?? "transparent"};`).join("");
  };
  // One block per flavor, from the palette — the first is the bare rule and the
  // rest override under html[data-flavor], so a new family needs nothing here.
  const [first, ...rest] = flavors;
  return (
    `.vsc{${block(first.id)}}` +
    rest.map((f) => `html[data-flavor="${f.id}"] .vsc{${block(f.id)}}`).join("")
  );
}

const SAMPLE = `// Northbound — next train on the Sixth Avenue line
import { fetchFeed, type Trip } from "./mta";

type Line = "B" | "D" | "F" | "M";

@cached(30)
export class Board<T extends Trip> {
  private readonly stops = new Map<string, number>();

  async nextArrival(line: Line, stop = 42): Promise<number> {
    const feed = await fetchFeed(\`/gtfs/\${line}\`);
    if (!feed.ok) throw new Error("signal problems\\n");
    return feed.trips.filter((t: T) => t.stop === stop).length;
  }
}`;

const LINES = SAMPLE.split("\n");
const CURSOR_LINE = 13;

/** A decoration over the nth occurrence of `text` on a 1-based line. */
function at(line: number, text: string, cls: string, nth = 0): DecorationItem {
  let i = -1;
  for (let n = 0; n <= nth; n++) i = LINES[line - 1].indexOf(text, i + 1);
  return {
    start: { line: line - 1, character: i },
    end: { line: line - 1, character: i + text.length },
    properties: { class: cls },
  };
}

const cls = (...s: (stylex.StyleXStyles | false)[]) => stylex.props(...s).className ?? "";

export async function Workbench() {
  const transformer: ShikiTransformer = {
    pre(node) {
      this.addClassToHast(node, cls(code.pre));
    },
    line(node, n) {
      this.addClassToHast(
        node,
        cls(
          code.line,
          n === CURSOR_LINE && code.current,
          n === 11 && code.modified,
          n === 8 && code.added,
        ),
      );
    },
  };
  const decorations = [
    at(11, "feed", cls(code.word)),
    at(12, "feed", cls(code.word)),
    at(13, "feed", cls(code.word)),
    at(10, "stop", cls(code.findCurrent)),
    at(13, "stop", cls(code.findOther)),
    at(13, "stop", cls(code.findOther), 1),
    at(11, "fetchFeed(`/gtfs/${line}`)", cls(code.selection)),
    at(10, "(", cls(code.bracket)),
    at(10, ")", cls(code.bracket)),
  ];
  const html = await highlight(SAMPLE, "typescript", [transformer], decorations);

  return (
    <figure
      className={`vsc ${cls(s.window)}`}
      aria-label="VS Code with the Subway Seat theme: explorer, editor, suggestions and terminal"
    >
      {/* biome-ignore lint/security/noDangerouslySetInnerHtml: generated CSS variables */}
      <style dangerouslySetInnerHTML={{ __html: variables() }} />
      <div {...stylex.props(s.title)}>
        <span {...stylex.props(s.dots)}>
          <i {...stylex.props(s.dot)} />
          <i {...stylex.props(s.dot)} />
          <i {...stylex.props(s.dot)} />
        </span>
        <span {...stylex.props(s.command)}>subway-seat</span>
      </div>
      <div {...stylex.props(s.body)}>
        <div aria-hidden {...stylex.props(s.activity)}>
          {["files", "search", "git", "run"].map((icon, i) => (
            <span key={icon} {...stylex.props(s.actIcon, i === 0 && s.actActive)}>
              <i {...stylex.props(s.actGlyph)} />
              {icon === "git" && <b {...stylex.props(s.badge)}>3</b>}
            </span>
          ))}
        </div>
        <div {...stylex.props(s.sidebar)}>
          <div {...stylex.props(s.sideTitle)}>EXPLORER</div>
          <div {...stylex.props(s.section)}>▾ SUBWAY-SEAT</div>
          {TREE.map((row) => (
            <div
              key={row.name}
              {...stylex.props(
                s.row,
                row.state === "hover" && s.rowHover,
                row.state === "selected" && s.rowSelected,
              )}
            >
              <span {...stylex.props(s.indent(row.depth))} />
              <span
                {...stylex.props(
                  s.fileBadge,
                  row.badge === "ts" && s.badgeTs,
                  row.badge === "py" && s.badgePy,
                )}
              >
                {row.icon}
              </span>
              <span
                {...stylex.props(
                  s.fileName,
                  row.git === "M" && s.gitModified,
                  row.git === "U" && s.gitUntracked,
                  row.state === "selected" && s.nameSelected,
                )}
              >
                {row.name}
              </span>
              {row.git && (
                <span
                  {...stylex.props(s.gitMark, row.git === "M" ? s.gitModified : s.gitUntracked)}
                >
                  {row.git}
                </span>
              )}
            </div>
          ))}
          <div {...stylex.props(s.section, s.sectionLater)}>▸ OUTLINE</div>
          <div {...stylex.props(s.section)}>▸ TIMELINE</div>
        </div>
        <div {...stylex.props(s.main)}>
          <div {...stylex.props(s.tabs)}>
            <span {...stylex.props(s.tab, s.tabActive)}>board.ts</span>
            <span {...stylex.props(s.tab, s.tabHover)}>
              mta.ts <i {...stylex.props(s.dirty)} />
            </span>
            <span {...stylex.props(s.tab)}>palette.py</span>
            <span {...stylex.props(s.tabFill)} />
          </div>
          <div {...stylex.props(s.crumbs)}>
            src › board.ts › <span {...stylex.props(s.crumbFocus)}>Board</span> › nextArrival
          </div>
          <div {...stylex.props(s.editor)}>
            <div
              // biome-ignore lint/a11y/noNoninteractiveTabindex: a scrolling region must take focus
              tabIndex={0}
              role="region"
              aria-label="board.ts"
              {...stylex.props(s.codeScroll)}
              // biome-ignore lint/security/noDangerouslySetInnerHtml: build-time Shiki HTML
              dangerouslySetInnerHTML={{ __html: html }}
            />
            <div {...stylex.props(s.suggest)}>
              {SUGGEST.map((item, i) => (
                <div key={item.label} {...stylex.props(s.suggestRow, i === 0 && s.suggestSelected)}>
                  <span {...stylex.props(s.kind, item.kind === "method" && s.kindMethod)}>
                    {item.icon}
                  </span>
                  <span>
                    <b {...stylex.props(s.match)}>{item.label.slice(0, 2)}</b>
                    {item.label.slice(2)}
                  </span>
                  <span {...stylex.props(s.suggestType)}>{item.type}</span>
                </div>
              ))}
            </div>
            <span {...stylex.props(s.slider)} />
          </div>
          <div {...stylex.props(s.panel)}>
            <div {...stylex.props(s.panelTabs)}>
              <span {...stylex.props(s.panelTab)}>PROBLEMS</span>
              <span {...stylex.props(s.panelTab, s.wideOnly)}>OUTPUT</span>
              <span {...stylex.props(s.panelTab, s.panelTabActive)}>TERMINAL</span>
            </div>
            <div {...stylex.props(s.term)}>
              <div>
                <span {...stylex.props(s.tGreen)}>❯</span> bun test board
              </div>
              <div>
                <span {...stylex.props(s.tGreen)}>✓</span> nextArrival returns the soonest train{" "}
                <span {...stylex.props(s.tDim)}>[4.2ms]</span>
              </div>
              <div>
                <span {...stylex.props(s.tRed)}>✗</span> handles signal problems{" "}
                <span {...stylex.props(s.tMagenta)}>src/board.ts:12</span>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div {...stylex.props(s.status)}>
        <span {...stylex.props(s.remote)}>» subway</span>
        <span>⎇ main*</span>
        <span {...stylex.props(s.statusWarn, s.wideOnly)}>⚠ 1</span>
        <span {...stylex.props(s.statusRight, s.wideOnly)}>Ln {CURSOR_LINE}, Col 12</span>
        <span {...stylex.props(s.statusEnd)}>TypeScript</span>
      </div>
    </figure>
  );
}

type TreeRow = {
  name: string;
  icon: string;
  badge: string;
  depth: number;
  state?: "hover" | "selected";
  git?: "M" | "U";
};

const TREE: TreeRow[] = [
  { name: "src", icon: "▾", badge: "folder", depth: 0 },
  { name: "board.ts", icon: "TS", badge: "ts", depth: 1, state: "selected" },
  { name: "mta.ts", icon: "TS", badge: "ts", depth: 1, git: "M", state: "hover" },
  { name: "trips.test.ts", icon: "TS", badge: "ts", depth: 1, git: "U" },
  { name: "palette.py", icon: "PY", badge: "py", depth: 0, git: "M" },
  { name: "README.md", icon: "MD", badge: "md", depth: 0 },
];

const SUGGEST = [
  { label: "ok", icon: "◆", kind: "property", type: "boolean" },
  { label: "trips", icon: "◆", kind: "property", type: "Trip[]" },
  { label: "toJSON", icon: "ƒ", kind: "method", type: "() => object" },
  { label: "status", icon: "◆", kind: "field", type: "number" },
] as const;

// Classes for spans inside the Shiki output.
const code = stylex.create({
  line: {
    display: "inline-block",
    minWidth: "100%",
    paddingRight: 24,
    verticalAlign: "top",
    counterIncrement: "line",
    "::before": {
      display: "inline-block",
      width: 48,
      paddingRight: 20,
      color: "var(--vsc-editorLineNumber-foreground)",
      textAlign: "right",
      content: "counter(line)",
      borderLeftColor: "transparent",
      borderLeftStyle: "solid",
      borderLeftWidth: 3,
    },
  },
  current: {
    backgroundColor: "var(--vsc-editor-lineHighlightBackground)",
    "::before": { color: "var(--vsc-editorLineNumber-activeForeground)" },
  },
  modified: { "::before": { borderLeftColor: "var(--vsc-editorGutter-modifiedBackground)" } },
  added: { "::before": { borderLeftColor: "var(--vsc-editorGutter-addedBackground)" } },
  pre: {
    width: "max-content",
    minWidth: "100%",
    paddingBlock: 10,
    margin: 0,
    fontFamily: font.mono,
    fontSize: 13,
    lineHeight: 1.65,
    counterReset: "line",
  },
  word: { backgroundColor: "var(--vsc-editor-wordHighlightBackground)", borderRadius: 2 },
  findCurrent: {
    outlineWidth: 1,
    outlineStyle: "solid",
    outlineColor: "var(--vsc-editor-findMatchBorder)",
    backgroundColor: "var(--vsc-editor-findMatchBackground)",
    borderRadius: 2,
  },
  findOther: { backgroundColor: "var(--vsc-editor-findMatchHighlightBackground)", borderRadius: 2 },
  selection: { backgroundColor: "var(--vsc-editor-selectionBackground)" },
  bracket: {
    outlineWidth: 1,
    outlineStyle: "solid",
    outlineColor: "var(--vsc-editorBracketMatch-border)",
    backgroundColor: "var(--vsc-editorBracketMatch-background)",
  },
});

const NARROW = "@media (max-width: 860px)";

const s = stylex.create({
  window: {
    margin: 0,
    overflow: "hidden",
    fontFamily: font.sans,
    fontSize: 13,
    color: "var(--vsc-editor-foreground)",
    backgroundColor: "var(--vsc-editor-background)",
    borderRadius: 12,
    boxShadow: "0 30px 70px var(--ss-shadow), 0 0 0 1px var(--ss-shadow-soft)",
  },
  title: {
    position: "relative",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    height: 36,
    color: "var(--vsc-titleBar-activeForeground)",
    backgroundColor: "var(--vsc-titleBar-activeBackground)",
    borderBottomColor: "var(--vsc-titleBar-border)",
    borderBottomStyle: "solid",
    borderBottomWidth: 1,
  },
  dots: { position: "absolute", left: 14, display: "flex", gap: 7 },
  dot: {
    width: 11,
    height: 11,
    backgroundColor: "var(--vsc-tree-indentGuidesStroke)",
    borderRadius: "50%",
  },
  command: {
    width: "min(44%, 360px)",
    paddingBlock: 3,
    fontSize: 12,
    color: "var(--vsc-commandCenter-foreground)",
    textAlign: "center",
    backgroundColor: "var(--vsc-commandCenter-background)",
    borderColor: "var(--vsc-commandCenter-border)",
    borderStyle: "solid",
    borderWidth: 1,
    borderRadius: 6,
  },
  body: {
    display: "grid",
    gridTemplateColumns: {
      [NARROW]: "48px minmax(0, 1fr)",
      default: "48px 230px minmax(0, 1fr)",
    },
    minHeight: 560,
  },
  activity: {
    display: "flex",
    flexDirection: "column",
    gap: 4,
    paddingTop: 8,
    backgroundColor: "var(--vsc-activityBar-background)",
  },
  actIcon: {
    position: "relative",
    display: "grid",
    placeItems: "center",
    height: 44,
    color: "var(--vsc-activityBar-inactiveForeground)",
    borderLeftColor: "transparent",
    borderLeftStyle: "solid",
    borderLeftWidth: 2,
  },
  actActive: {
    color: "var(--vsc-activityBar-foreground)",
    borderLeftColor: "var(--vsc-activityBar-activeBorder)",
  },
  actGlyph: {
    width: 18,
    height: 18,
    borderColor: "currentColor",
    borderStyle: "solid",
    borderWidth: 1.5,
    borderRadius: 4,
  },
  badge: {
    position: "absolute",
    top: 7,
    right: 7,
    display: "grid",
    placeItems: "center",
    minWidth: 15,
    height: 15,
    fontSize: 9,
    fontWeight: 700,
    color: "var(--vsc-activityBarBadge-foreground)",
    backgroundColor: "var(--vsc-activityBarBadge-background)",
    borderRadius: 8,
  },
  sidebar: {
    display: {
      [NARROW]: "none",
      default: "block",
    },
    paddingBottom: 10,
    color: "var(--vsc-sideBar-foreground)",
    backgroundColor: "var(--vsc-sideBar-background)",
    borderRightColor: "var(--vsc-sideBar-border)",
    borderRightStyle: "solid",
    borderRightWidth: 1,
  },
  sideTitle: {
    paddingBlock: 10,
    paddingInline: 18,
    fontSize: 11,
    color: "var(--vsc-sideBarTitle-foreground)",
    letterSpacing: "0.06em",
  },
  section: {
    paddingBlock: 3,
    paddingInline: 8,
    fontSize: 11,
    fontWeight: 700,
    color: "var(--vsc-sideBarSectionHeader-foreground)",
    backgroundColor: "var(--vsc-sideBarSectionHeader-background)",
    borderTopColor: "var(--vsc-sideBarSectionHeader-border)",
    borderTopStyle: "solid",
    borderTopWidth: 1,
  },
  sectionLater: { marginTop: 110 },
  row: {
    display: "flex",
    gap: 6,
    alignItems: "center",
    height: 24,
    paddingInline: 8,
    outlineStyle: "none",
    outlineOffset: -1,
  },
  rowHover: { backgroundColor: "var(--vsc-list-hoverBackground)" },
  rowSelected: {
    outlineWidth: 1,
    outlineStyle: "solid",
    outlineColor: "var(--vsc-list-focusOutline)",
    backgroundColor: "var(--vsc-list-activeSelectionBackground)",
  },
  indent: (depth: number) => ({ flexShrink: 0, width: 8 + depth * 14 }),
  fileBadge: {
    width: 20,
    fontFamily: font.mono,
    fontSize: 9,
    fontWeight: 700,
    color: "var(--vsc-sideBar-foreground)",
    textAlign: "center",
  },
  badgeTs: { color: "var(--vsc-symbolIcon-methodForeground)" },
  badgePy: { color: "var(--vsc-list-highlightForeground)" },
  fileName: { flexGrow: 1, overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" },
  nameSelected: { color: "var(--vsc-list-activeSelectionForeground)" },
  gitModified: { color: "var(--vsc-gitDecoration-modifiedResourceForeground)" },
  gitUntracked: { color: "var(--vsc-gitDecoration-untrackedResourceForeground)" },
  gitMark: { paddingRight: 6, fontSize: 11 },
  main: { display: "flex", flexDirection: "column", minWidth: 0 },
  tabs: {
    display: "flex",
    height: 36,
    overflow: "hidden",
    backgroundColor: "var(--vsc-editorGroupHeader-tabsBackground)",
  },
  tab: {
    display: "flex",
    gap: 8,
    alignItems: "center",
    paddingInline: 16,
    color: "var(--vsc-tab-inactiveForeground)",
    backgroundColor: "var(--vsc-tab-inactiveBackground)",
    borderRightColor: "var(--vsc-tab-border)",
    borderRightStyle: "solid",
    borderRightWidth: 1,
    borderBottomColor: "var(--vsc-editorGroupHeader-tabsBorder)",
    borderBottomStyle: "solid",
    borderBottomWidth: 1,
  },
  tabActive: {
    color: "var(--vsc-tab-activeForeground)",
    backgroundColor: "var(--vsc-tab-activeBackground)",
    borderTopColor: "var(--vsc-tab-activeBorderTop)",
    borderTopStyle: "solid",
    borderTopWidth: 2,
    borderBottomColor: "var(--vsc-tab-activeBorder)",
  },
  tabHover: {
    backgroundImage:
      "linear-gradient(var(--vsc-tab-hoverBackground), var(--vsc-tab-hoverBackground))",
  },
  tabFill: {
    flexGrow: 1,
    borderBottomColor: "var(--vsc-editorGroupHeader-tabsBorder)",
    borderBottomStyle: "solid",
    borderBottomWidth: 1,
  },
  dirty: {
    width: 8,
    height: 8,
    backgroundColor: "var(--vsc-tab-activeModifiedBorder)",
    borderRadius: "50%",
  },
  crumbs: {
    paddingBlock: 4,
    paddingInline: 16,
    fontSize: 12,
    color: "var(--vsc-breadcrumb-foreground)",
  },
  crumbFocus: { color: "var(--vsc-breadcrumb-focusForeground)" },
  editor: { position: "relative", flexGrow: 1 },
  codeScroll: {
    overflowX: "auto",
    outlineWidth: 1,
    outlineStyle: {
      default: "none",
      ":focus-visible": "solid",
    },
    outlineColor: "var(--vsc-list-focusOutline)",
    outlineOffset: -1,
  },
  suggest: {
    position: "absolute",
    top: 262,
    left: 190,
    zIndex: 1,
    width: 290,
    paddingBlock: 3,
    fontFamily: font.mono,
    fontSize: 12.5,
    color: "var(--vsc-editorSuggestWidget-foreground)",
    backgroundColor: "var(--vsc-editorSuggestWidget-background)",
    borderColor: "var(--vsc-editorSuggestWidget-border)",
    borderStyle: "solid",
    borderWidth: 1,
    borderRadius: 6,
    boxShadow: "0 8px 22px var(--vsc-widget-shadow)",
  },
  suggestRow: {
    display: "grid",
    gridTemplateColumns: "18px 1fr auto",
    gap: 6,
    paddingBlock: 2,
    paddingInline: 8,
  },
  suggestSelected: {
    color: "var(--vsc-editorSuggestWidget-selectedForeground)",
    backgroundColor: "var(--vsc-editorSuggestWidget-selectedBackground)",
  },
  kind: { color: "var(--vsc-symbolIcon-propertyForeground)", textAlign: "center" },
  kindMethod: { color: "var(--vsc-symbolIcon-methodForeground)" },
  match: { fontWeight: 700, color: "var(--vsc-editorSuggestWidget-highlightForeground)" },
  suggestType: { opacity: 0.6 },
  slider: {
    position: "absolute",
    top: 8,
    right: 3,
    width: 10,
    height: 90,
    backgroundColor: "var(--vsc-scrollbarSlider-background)",
  },
  panel: {
    color: "var(--vsc-terminal-foreground)",
    backgroundColor: "var(--vsc-panel-background)",
    borderTopColor: "var(--vsc-panel-border)",
    borderTopStyle: "solid",
    borderTopWidth: 1,
  },
  panelTabs: {
    display: "flex",
    gap: 22,
    paddingInline: 18,
    paddingTop: 8,
    fontSize: 11,
    letterSpacing: "0.04em",
  },
  panelTab: {
    paddingBottom: 6,
    color: "var(--vsc-panelTitle-inactiveForeground)",
    whiteSpace: "nowrap",
    borderBottomColor: "transparent",
    borderBottomStyle: "solid",
    borderBottomWidth: 1,
  },
  panelTabActive: {
    color: "var(--vsc-panelTitle-activeForeground)",
    borderBottomColor: "var(--vsc-panelTitle-activeBorder)",
  },
  term: {
    paddingInline: 18,
    paddingTop: 8,
    paddingBottom: 14,
    fontFamily: font.mono,
    fontSize: 12.5,
    lineHeight: 1.7,
  },
  tGreen: { color: "var(--vsc-terminal-ansiGreen)" },
  tRed: { color: "var(--vsc-terminal-ansiRed)" },
  tMagenta: { color: "var(--vsc-terminal-ansiMagenta)" },
  tDim: { color: "var(--vsc-terminal-ansiBrightBlack)" },
  status: {
    display: "flex",
    gap: 14,
    alignItems: "center",
    height: 24,
    paddingRight: 12,
    overflow: "hidden",
    fontSize: 12,
    color: "var(--vsc-statusBar-foreground)",
    whiteSpace: "nowrap",
    backgroundColor: "var(--vsc-statusBar-background)",
    borderTopColor: "var(--vsc-statusBar-border)",
    borderTopStyle: "solid",
    borderTopWidth: 1,
  },
  remote: {
    display: "flex",
    alignItems: "center",
    alignSelf: "stretch",
    paddingInline: 10,
    color: "var(--vsc-statusBarItem-remoteForeground)",
    backgroundColor: "var(--vsc-statusBarItem-remoteBackground)",
  },
  statusWarn: { color: "var(--vsc-statusBarItem-warningForeground)" },
  statusRight: { marginLeft: "auto" },
  statusEnd: {
    marginLeft: {
      [NARROW]: "auto",
      default: 0,
    },
  },
  wideOnly: {
    display: {
      [NARROW]: "none",
      default: "inline",
    },
  },
});
