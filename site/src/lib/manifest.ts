import { readFileSync } from "node:fs";
import path from "node:path";
import { DIST_DIR } from "./dist";
import type { FlavorId } from "./palette";

export type PortFile = {
  path: string;
  flavor: FlavorId | null;
  dest: string | null;
  lang: string;
  append: boolean;
  binary: boolean;
};

export type Enable = { where: string; code: string; lang: string };

export type Port = {
  id: string;
  name: string;
  category: string;
  homepage: string;
  notes: string;
  enable: Record<FlavorId, Enable> | null;
  files: PortFile[];
};

type Manifest = { categories: string[]; ports: Port[] };

let cached: Manifest | undefined;

export function manifest(): Manifest {
  cached ??= JSON.parse(readFileSync(path.join(DIST_DIR, "manifest.json"), "utf8")) as Manifest;
  return cached;
}

export function ports() {
  return manifest().ports;
}

export function portById(id: string) {
  return ports().find((p) => p.id === id);
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
