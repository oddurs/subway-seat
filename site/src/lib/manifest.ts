import { existsSync, readFileSync } from "node:fs";
import path from "node:path";
import { DIST_DIR } from "./dist";
import type { FlavorId } from "./palette";

export type PortFile = {
  path: string;
  flavor: FlavorId | null;
  /** A real path (`~/…`, `/…`, `%APPDATA%\…`) or null. Older manifests put prose here. */
  dest: string | null;
  /** Prose install step when there's no path to copy to. */
  how?: string | null;
  lang: string;
  append: boolean;
  binary: boolean;
};

export type Enable = {
  where: string;
  code: string;
  lang: string;
  /** POSIX-shell equivalent of a fish `code`. */
  sh?: string;
  /** The config file install.sh appends `code` to. */
  file?: string;
};

export type Auto = { where: string; code: string; lang: string; file?: string };

export type Port = {
  id: string;
  name: string;
  category: string;
  homepage: string;
  notes: string;
  enable: Record<FlavorId, Enable> | null;
  auto?: Auto | null;
  requires?: string | null;
  detect?: string[] | null;
  files: PortFile[];
  /** install.sh sets it up on its own (build.py's `installs`, checked against install.sh). */
  installs: boolean;
};

type Manifest = { version?: string; categories: string[]; ports: Port[] };

let cached: Manifest | undefined;

export function manifest(): Manifest {
  cached ??= JSON.parse(readFileSync(path.join(DIST_DIR, "manifest.json"), "utf8")) as Manifest;
  return cached;
}

export function ports() {
  return manifest().ports;
}

export function version() {
  return manifest().version ?? null;
}

export function portById(id: string) {
  return ports().find((p) => p.id === id);
}

/** Category names as shown on the site; the manifest keys stay as they are. */
const CATEGORY_LABELS: Record<string, string> = { Palettes: "Palettes & formats" };

export function categoryLabel(category: string) {
  return CATEGORY_LABELS[category] ?? category;
}

export function byCategory() {
  const { categories, ports } = manifest();
  return categories
    .map((category) => ({ category, ports: ports.filter((p) => p.category === category) }))
    .filter((group) => group.ports.length > 0);
}

export function allFiles() {
  return ports().flatMap((p) => p.files);
}

export function distExists(rel: string) {
  return existsSync(path.join(DIST_DIR, rel));
}

/** `dest` values that are paths, not directions (older manifests mix the two). */
export function isPath(dest: string) {
  return /^(~|\/|%|\$|<|[A-Za-z]:\\)/.test(dest) || /^[\w.-]+\/[\w./-]+$/.test(dest);
}

/** What install.sh can do for a port on its own, and what it has to leave to you. */
export type Setup = "auto" | "step" | "manual";

export function setupFor(port: Port): Setup {
  if (!port.installs) return "manual";
  const steps = port.files.some((f) => f.how || (f.dest && !isPath(f.dest)));
  const enable = port.enable ? Object.values(port.enable)[0] : null;
  if (steps || (enable && !enable.file)) return "step";
  return "auto";
}
