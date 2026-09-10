import { readFileSync } from "node:fs";
import path from "node:path";
import { DIST_DIR } from "@/lib/dist";
import { allFiles } from "@/lib/manifest";

// Every generated file is known at build time; anything else is a 404.
export const dynamicParams = false;

export function generateStaticParams() {
  return allFiles().map((file) => ({ path: file.path.split("/") }));
}

const TYPES: Record<string, string> = {
  ".json": "application/json; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".zip": "application/zip",
  ".xpi": "application/x-xpinstall",
  ".jar": "application/java-archive",
  ".vsix": "application/octet-stream",
};

export async function GET(_request: Request, ctx: RouteContext<"/files/[...path]">) {
  const { path: parts } = await ctx.params;
  const rel = parts.map(decodeURIComponent).join("/");
  const file = allFiles().find((f) => f.path === rel);
  if (!file) return new Response("Not found", { status: 404 });

  const body = new Uint8Array(readFileSync(path.join(DIST_DIR, file.path)));
  const ext = path.extname(file.path).toLowerCase();
  return new Response(body, {
    headers: {
      "Content-Type":
        TYPES[ext] ?? (file.binary ? "application/octet-stream" : "text/plain; charset=utf-8"),
      "Content-Disposition": `attachment; filename="${path.basename(file.path)}"`,
    },
  });
}
