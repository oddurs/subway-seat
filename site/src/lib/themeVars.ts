import { existsSync, readFileSync } from "node:fs";
import path from "node:path";
import { DIST_DIR } from "./dist";
import { type FlavorId, flavorById, flavors } from "./palette";

/**
 * CSS custom properties read from a generated theme file, one block per flavor,
 * so a mock shows exactly the colors the port installs. The first flavor is the
 * default; every other one overrides under html[data-flavor].
 */
export function flavorVars(scope: string, read: (id: FlavorId) => Record<string, string>) {
  return flavors
    .map((f) => {
      const vars = Object.entries(read(f.id))
        .map(([k, v]) => `--${k}:${v};`)
        .join("");
      // The first flavor is the bare rule; the rest override under html[data-flavor].
      const sel = f.id === flavors[0].id ? scope : `html[data-flavor="${f.id}"] ${scope}`;
      return `${sel}{${vars}}`;
    })
    .join("");
}

function distText(rel: string) {
  const file = path.join(DIST_DIR, rel);
  return existsSync(file) ? readFileSync(file, "utf8") : null;
}

type Style = { fg?: string; bold?: boolean };

/** eza's theme.yml as flat `perms.user_read` keys (its one-line `{foreground: …}` entries). */
export function ezaTheme(id: FlavorId): Record<string, Style> {
  const text = distText(`eza/${flavorById[id].slug}.yml`) ?? "";
  const out: Record<string, Style> = {};
  const stack: { indent: number; key: string }[] = [];
  for (const line of text.split("\n")) {
    const m = line.match(/^(\s*)"?([\w.-]+)"?:\s*(.*)$/);
    if (!m || line.trimStart().startsWith("#")) continue;
    const indent = m[1].length;
    while (stack.length && stack[stack.length - 1].indent >= indent) stack.pop();
    const key = [...stack.map((s) => s.key), m[2]].join(".");
    const value = m[3];
    if (value.startsWith("{")) {
      out[key] = {
        fg: value.match(/foreground:\s*"(#[0-9A-Fa-f]{6})"/)?.[1],
        bold: /is_bold:\s*true/.test(value),
      };
    } else if (!value) {
      stack.push({ indent, key: m[2] });
    }
  }
  return out;
}

/** The overrides in the Claude Code theme for a flavor. */
export function claudeTheme(id: FlavorId): Record<string, string> {
  const text = distText(`claude-code/themes/${flavorById[id].slug}.json`);
  if (!text) return {};
  return (JSON.parse(text) as { overrides?: Record<string, string> }).overrides ?? {};
}
