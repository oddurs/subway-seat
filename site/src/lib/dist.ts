import { readFileSync } from "node:fs";
import path from "node:path";

/** The generated theme files live one level up, in the repo's dist/. */
export const DIST_DIR = path.join(process.cwd(), "..", "dist");

export function readDist(rel: string): string {
  return readFileSync(path.join(DIST_DIR, rel), "utf8");
}
