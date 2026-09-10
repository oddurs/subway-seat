import { categoryLabel, ports } from "@/lib/manifest";
import { ogCard } from "@/og/card";

// Share images: /og/home.png, /og/palette.png, /og/install.png and /og/<port id>.png.
// Route handlers rather than opengraph-image files, so each page sets its own alt text.
export const dynamicParams = false;

type Card = Parameters<typeof ogCard>[0];

function cards(): Record<string, Card> {
  const count = ports().length;
  return {
    "home.png": {
      kicker: "A color scheme for the long ride",
      title: "Sink into a warmer screen.",
      line: `A walnut-brown color scheme from a 1970s subway car. ${count} ports, three flavors.`,
      rug: true,
    },
    "palette.png": {
      kicker: "The palette",
      title: "Twenty-six colors, three flavors.",
      line: "Brown, cream, and the good stuff. Hex, RGB, HSL and OKLCH, ready to copy.",
    },
    "install.png": {
      kicker: "Get on board",
      title: "Take a seat in one line.",
      line: "Pick a flavor and your apps, then paste one line. Switch or get off any time.",
    },
    ...Object.fromEntries(
      ports().map((p) => [
        `${p.id}.png`,
        {
          kicker: categoryLabel(p.category),
          title: p.name,
          line: "A warm 1970s subway-car theme, in Walnut, Tunnel and Enamel.",
        },
      ]),
    ),
  };
}

export function generateStaticParams() {
  return Object.keys(cards()).map((name) => ({ name }));
}

export async function GET(_request: Request, ctx: RouteContext<"/og/[name]">) {
  const { name } = await ctx.params;
  const card = cards()[name];
  if (!card) return new Response("Not found", { status: 404 });
  return ogCard(card);
}
