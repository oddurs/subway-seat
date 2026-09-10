import {
  bundledLanguages,
  createHighlighter,
  type DecorationItem,
  type LanguageRegistration,
  type ShikiTransformer,
  type ThemeRegistrationRaw,
} from "shiki";
import { readDist } from "./dist";
import type { FlavorId } from "./palette";

// Highlight with the real generated VS Code themes — what you see is what you install.
const theme = (slug: string) =>
  JSON.parse(readDist(`vscode/themes/${slug}-color-theme.json`)) as ThemeRegistrationRaw;

const THEMES = {
  walnut: theme("subway-seat"),
  tunnel: theme("subway-seat-tunnel"),
  enamel: theme("subway-seat-enamel"),
} satisfies Record<FlavorId, ThemeRegistrationRaw>;

// Ghostty config, fish theme files and gitconfig are all "key [=] value" with
// full-line comments. Stock ini/properties grammars treat `#513B27` as a comment.
const conf: LanguageRegistration = {
  name: "conf",
  scopeName: "source.conf",
  patterns: [
    { match: "^\\s*[#;].*$", name: "comment.line.conf" },
    { match: "^\\s*\\[[^\\]]+\\]", name: "entity.name.section.conf" },
    { match: "^\\s*([\\w.@-]+)", captures: { 1: { name: "support.type.property-name.conf" } } },
    { match: "=", name: "keyword.operator.assignment.conf" },
    { match: '"[^"]*"', name: "string.quoted.double.conf" },
    { match: "#?\\b[0-9A-Fa-f]{6}\\b", name: "constant.other.color.conf" },
    { match: "--[\\w-]+", name: "variable.parameter.option.conf" },
  ],
  repository: {},
};

const ALIASES: Record<string, string> = {
  sh: "shellscript",
  bash: "shellscript",
  ini: "ini",
  elisp: "emacs-lisp",
  vim: "viml",
  python: "python",
  js: "javascript",
  kdl: "kdl",
  ron: "rust",
};

let highlighter: ReturnType<typeof createHighlighter> | undefined;

function lang(name: string) {
  const resolved = ALIASES[name] ?? name;
  if (resolved === "conf" || resolved === "text") return resolved;
  return resolved in bundledLanguages ? resolved : "text";
}

/** Code as HTML carrying all three flavors: the default colour is Walnut, the
 * others ride along as --shiki-tunnel / --shiki-enamel for globals.css to swap in. */
export async function highlight(
  code: string,
  language: string,
  transformers: ShikiTransformer[] = [],
  decorations: DecorationItem[] = [],
) {
  highlighter ??= createHighlighter({ themes: Object.values(THEMES), langs: [conf] });
  const shiki = await highlighter;
  const l = lang(language);
  if (l !== "text" && l !== "conf" && !shiki.getLoadedLanguages().includes(l)) {
    await shiki.loadLanguage(l as keyof typeof bundledLanguages);
  }
  return shiki.codeToHtml(code, {
    lang: l,
    themes: {
      walnut: THEMES.walnut.name ?? "Subway Seat",
      tunnel: THEMES.tunnel.name ?? "Subway Seat Tunnel",
      enamel: THEMES.enamel.name ?? "Subway Seat Enamel",
    },
    defaultColor: "walnut",
    transformers,
    decorations,
  });
}

/** Workbench colours from the VS Code themes, for the editor mock. */
export function workbenchColors(id: FlavorId) {
  return (THEMES[id] as { colors: Record<string, string> }).colors;
}
