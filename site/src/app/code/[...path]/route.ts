import { blockHtml, MAX_LINES } from "@/components/blockHtml";
import { readDist } from "@/lib/dist";
import { allFiles } from "@/lib/manifest";

// The whole of a long file, highlighted, for a port page's "Show all" button.
// Pages only carry the first MAX_LINES lines, so they stay small.
export const dynamicParams = false;

const long = () =>
  allFiles().filter((f) => !f.binary && readDist(f.path).trimEnd().split("\n").length > MAX_LINES);

export function generateStaticParams() {
  return long().map((file) => ({ path: file.path.split("/") }));
}

export async function GET(_request: Request, ctx: RouteContext<"/code/[...path]">) {
  const { path: parts } = await ctx.params;
  const rel = parts.map(decodeURIComponent).join("/");
  const file = long().find((f) => f.path === rel);
  if (!file) return new Response("Not found", { status: 404 });
  const html = await blockHtml(readDist(file.path).trimEnd(), file.lang, file.flavor ?? undefined);
  return new Response(html, { headers: { "Content-Type": "text/html; charset=utf-8" } });
}
