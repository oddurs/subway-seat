"use client";

import * as stylex from "@stylexjs/stylex";
import { useEffect, useRef } from "react";
import { currentFlavor, FLAVOR_EVENT } from "@/lib/flavor";
import type { FlavorId } from "@/lib/palette";
import { color } from "@/theme/tokens.stylex";

export type TilePalette = { grout: string; faces: string[]; accents: string[] };

/**
 * Paris in bevelled tile — the carreaux biseautés that line every vaulted
 * platform in the network, and the third material after New York's shag and
 * London's moquette.
 *
 * Each band is built on a different rule, which is the point of them. Shag is a
 * seeded PRNG, because a cut pile has no order. Moquette is a woven repeat,
 * because a loom has nothing else. Tile is a masonry bond — a rigid grid offset
 * half a tile each course — and the only thing that varies is the light.
 */
const TW = 34; // Paris tile is small; this is about a 2:1 face at band scale
const TH = 17;
const BEVEL = 3.2;
const GROUT = 2;

/**
 * The bevel, drawn once offscreen and stamped over every face.
 *
 * A carreau biseauté is thick glaze over a curved chamfer, so the light doesn't
 * sit in a flat band along the top edge: it wraps the whole rim and falls off
 * across the chamfer. Four gradients, one per edge, get that. Four flat fills
 * do not, which is exactly what the first version of this drew and why it read
 * as graph paper.
 */
function bevelStamp(dpr: number) {
  const c = document.createElement("canvas");
  c.width = Math.max(1, Math.ceil(TW * dpr));
  c.height = Math.max(1, Math.ceil(TH * dpr));
  const g = c.getContext("2d");
  if (!g) return c;
  g.setTransform(dpr, 0, 0, dpr, 0, 0);

  const B = BEVEL;
  const edge = (
    pts: [number, number][],
    from: [number, number],
    to: [number, number],
    stops: [number, string][],
  ) => {
    const grad = g.createLinearGradient(from[0], from[1], to[0], to[1]);
    for (const [at, css] of stops) grad.addColorStop(at, css);
    g.fillStyle = grad;
    g.beginPath();
    g.moveTo(pts[0][0], pts[0][1]);
    for (const [x, y] of pts.slice(1)) g.lineTo(x, y);
    g.closePath();
    g.fill();
  };

  const lit: [number, string][] = [
    [0, "rgba(255,255,255,0.66)"],
    [0.5, "rgba(255,255,255,0.22)"],
    [1, "rgba(255,255,255,0)"],
  ];
  const dim: [number, string][] = [
    [0, "rgba(0,0,0,0.36)"],
    [0.5, "rgba(0,0,0,0.13)"],
    [1, "rgba(0,0,0,0)"],
  ];
  // Lit from above left, as a platform is: top and left catch it, right and
  // bottom fall away. The mitres at the corners fall out of the geometry.
  edge(
    [
      [0, 0],
      [TW, 0],
      [TW - B, B],
      [B, B],
    ],
    [0, 0],
    [0, B],
    lit,
  );
  edge(
    [
      [0, 0],
      [B, B],
      [B, TH - B],
      [0, TH],
    ],
    [0, 0],
    [B, 0],
    lit,
  );
  edge(
    [
      [TW, 0],
      [TW, TH],
      [TW - B, TH - B],
      [TW - B, B],
    ],
    [TW, 0],
    [TW - B, 0],
    dim,
  );
  edge(
    [
      [0, TH],
      [TW, TH],
      [TW - B, TH - B],
      [B, TH - B],
    ],
    [0, TH],
    [0, TH - B],
    dim,
  );
  return c;
}

function draw(canvas: HTMLCanvasElement, pal: TilePalette) {
  const w = canvas.clientWidth;
  const h = canvas.clientHeight;
  if (!w || !h) return;
  const dpr = Math.min(window.devicePixelRatio || 1, 1.5);
  canvas.width = Math.round(w * dpr);
  canvas.height = Math.round(h * dpr);
  const ctx = canvas.getContext("2d");
  if (!ctx) return;
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

  // The grout is the ground the tiles sit on, so the gaps read as recessed.
  ctx.fillStyle = pal.grout;
  ctx.fillRect(0, 0, w, h);

  const stamp = bevelStamp(dpr);
  const rows = Math.ceil(h / (TH + GROUT)) + 1;
  const cols = Math.ceil(w / (TW + GROUT)) + 2;
  for (let row = 0; row < rows; row++) {
    const y = row * (TH + GROUT);
    const offset = row % 2 ? -(TW + GROUT) / 2 : 0;
    for (let col = -1; col < cols; col++) {
      const x = col * (TW + GROUT) + offset;
      const n = row * 7 + col + (col < 0 ? cols : 0);
      // One tile in seventeen is a colour, the way the older stations set their
      // names and their borders. Which tile is accented and which accent it
      // takes step at different rates — share a modulus and every accent comes
      // out the same colour.
      const face =
        n % 17 === 6
          ? pal.accents[((n / 17) | 0) % pal.accents.length]
          : pal.faces[n % pal.faces.length];
      ctx.fillStyle = face;
      ctx.fillRect(x, y, TW, TH);
      ctx.drawImage(stamp, x, y, TW, TH);
    }
  }

  // The same shade the other two bands carry, so all three sit at one depth.
  const shade = ctx.createLinearGradient(0, h * 0.55, 0, h);
  shade.addColorStop(0, "rgba(0,0,0,0)");
  shade.addColorStop(1, "rgba(0,0,0,0.28)");
  ctx.fillStyle = shade;
  ctx.fillRect(0, 0, w, h);
}

export function Carrelage({
  palettes,
  height = 120,
}: {
  palettes: Record<FlavorId, TilePalette>;
  height?: number;
}) {
  const ref = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    const canvas = ref.current;
    if (!canvas) return;
    let width = 0;
    const paint = () => {
      width = canvas.clientWidth;
      draw(canvas, palettes[currentFlavor()] ?? Object.values(palettes)[0]);
    };
    const idle = window.requestIdleCallback ?? ((cb: () => void) => window.setTimeout(cb, 1));
    const cancelIdle = window.cancelIdleCallback ?? window.clearTimeout;
    const first = idle(paint);
    let timer: ReturnType<typeof setTimeout>;
    const resize = () => {
      clearTimeout(timer);
      timer = setTimeout(() => {
        if (canvas.clientWidth !== width) paint();
      }, 120);
    };
    window.addEventListener("resize", resize);
    window.addEventListener(FLAVOR_EVENT, paint);
    return () => {
      cancelIdle(first);
      clearTimeout(timer);
      window.removeEventListener("resize", resize);
      window.removeEventListener(FLAVOR_EVENT, paint);
    };
  }, [palettes]);

  return <canvas ref={ref} aria-hidden {...stylex.props(styles.canvas, styles.height(height))} />;
}

const styles = stylex.create({
  // Before the canvas draws, a flat bond in CSS.
  canvas: {
    borderBlockColor: color.crust,
    borderBlockStyle: "solid",
    borderBlockWidth: 1,
    display: "block",
    width: "100%",
    backgroundColor: color.mantle,
    backgroundImage: `linear-gradient(to bottom, transparent 55%, rgba(0,0,0,0.28)), repeating-linear-gradient(0deg, ${color.surface0} 0 17px, ${color.mantle} 17px 19px)`,
  },
  height: (height: number) => ({ height }),
});
