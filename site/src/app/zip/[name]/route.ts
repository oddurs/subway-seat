import { bundleMembers, bundles } from "@/lib/bundles";
import { zip } from "@/lib/zip";

// "Download all (.zip)": every file one flavor of a port needs, in one archive.
export const dynamicParams = false;

export function generateStaticParams() {
  return bundles().map((b) => ({ name: b.name }));
}

export async function GET(_request: Request, ctx: RouteContext<"/zip/[name]">) {
  const { name } = await ctx.params;
  const bundle = bundles().find((b) => b.name === name);
  if (!bundle) return new Response("Not found", { status: 404 });
  const body = zip(bundleMembers(bundle.port, bundle.flavor));
  return new Response(body, {
    headers: {
      "Content-Type": "application/zip",
      "Content-Disposition": `attachment; filename="subway-seat-${bundle.name}"`,
    },
  });
}
