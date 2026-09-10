import { existsSync, readFileSync } from "node:fs";
import path from "node:path";
import { DIST_DIR } from "./dist";
import { type Port, ports } from "./manifest";
import { type FlavorId, flavors } from "./palette";

/** The files a flavor needs from a port: its own plus the shared ones. */
export function filesFor(port: Port, flavor: FlavorId) {
  return port.files.filter((f) => f.flavor === flavor || f.flavor === null);
}

/** One "Download all" zip per port and flavor, when there's more than one file to get. */
export function bundles() {
  return ports().flatMap((port) =>
    flavors
      .filter((f) => filesFor(port, f.id).length > 1)
      .map((f) => ({ port, flavor: f.id, name: `${port.id}-${f.id}.zip` })),
  );
}

export function bundleFor(port: Port, flavor: FlavorId) {
  return filesFor(port, flavor).length > 1 ? `${port.id}-${flavor}.zip` : null;
}

/** Zip members: `subway-seat-<id>/<path>`, plus the port's README when it has one. */
export function bundleMembers(port: Port, flavor: FlavorId) {
  const root = `subway-seat-${port.id}`;
  const members = filesFor(port, flavor).map((f) => ({
    name: `${root}/${f.path.split("/").slice(1).join("/")}`,
    data: new Uint8Array(readFileSync(path.join(DIST_DIR, f.path))),
  }));
  const readme = path.join(DIST_DIR, port.id, "README.md");
  if (existsSync(readme)) {
    members.unshift({ name: `${root}/README.md`, data: new Uint8Array(readFileSync(readme)) });
  }
  return members;
}
