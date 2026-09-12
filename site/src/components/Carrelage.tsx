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
 * because a loom has nothing else. Tile is a masonry bond: a rigid grid, offset
 * by half a tile each course, and the only thing that varies is the light —
 * every tile is bevelled, so it catches a highlight along its top and left and
 * throws a shadow down its bottom and right. That lighting is what makes a wall
 * of identical white rectangles read as tile rather than as graph paper.
 */
const TW = 62; // tile width
const TH = 30; // tile height
const BEVEL = 3;
const GROUT = 2;

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
  ctx.fillStyle = pal.grout;
  ctx.fillRect(0, 0, w, h);

  const rows = Math.ceil(h / (TH + GROUT)) + 1;
  const cols = Math.ceil(w / (TW + GROUT)) + 2;
  for (let row = 0; row < rows; row++) {
    const y = row * (TH + GROUT);
    // A running bond: every other course steps half a tile.
    const offset = row % 2 ? -(TW + GROUT) / 2 : 0;
    for (let col = -1; col < cols; col++) {
      const x = col * (TW + GROUT) + offset;
      const n = row * 5 + col + (col < 0 ? cols : 0);
      // Mostly plain tile; one in eleven is a colour, as the older stations set
      // their station names and their borders.
      const face =
        n % 11 === 4
          ? pal.accents[((n / 11) | 0) % pal.accents.length]
          : pal.faces[n % pal.faces.length];
      ctx.fillStyle = face;
      ctx.fillRect(x, y, TW, TH);
      // The bevel: lit from the top left, as a platform is.
      ctx.fillStyle = "rgba(255,255,255,0.22)";
      ctx.beginPath();
      ctx.moveTo(x, y);
      ctx.lineTo(x + TW, y);
      ctx.lineTo(x + TW - BEVEL, y + BEVEL);
      ctx.lineTo(x + BEVEL, y + BEVEL);
      ctx.closePath();
      ctx.fill();
      ctx.beginPath();
      ctx.moveTo(x, y);
      ctx.lineTo(x + BEVEL, y + BEVEL);
      ctx.lineTo(x + BEVEL, y + TH - BEVEL);
      ctx.lineTo(x, y + TH);
      ctx.closePath();
      ctx.fill();
      ctx.fillStyle = "rgba(0,0,0,0.20)";
      ctx.beginPath();
      ctx.moveTo(x + TW, y);
      ctx.lineTo(x + TW, y + TH);
      ctx.lineTo(x + TW - BEVEL, y + TH - BEVEL);
      ctx.lineTo(x + TW - BEVEL, y + BEVEL);
      ctx.closePath();
      ctx.fill();
      ctx.beginPath();
      ctx.moveTo(x, y + TH);
      ctx.lineTo(x + TW, y + TH);
      ctx.lineTo(x + TW - BEVEL, y + TH - BEVEL);
      ctx.lineTo(x + BEVEL, y + TH - BEVEL);
      ctx.closePath();
      ctx.fill();
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
    display: "block",
    width: "100%",
    borderBlockColor: color.crust,
    borderBlockStyle: "solid",
    borderBlockWidth: 1,
    backgroundColor: color.mantle,
    backgroundImage: `linear-gradient(to bottom, transparent 55%, rgba(0,0,0,0.28)), repeating-linear-gradient(0deg, ${color.surface0} 0 30px, ${color.mantle} 30px 32px)`,
  },
  height: (height: number) => ({ height }),
});
