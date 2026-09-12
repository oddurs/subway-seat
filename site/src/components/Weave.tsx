"use client";

import * as stylex from "@stylexjs/stylex";
import { useEffect, useRef } from "react";
import { currentFlavor, FLAVOR_EVENT } from "@/lib/flavor";
import type { FlavorId } from "@/lib/palette";
import { color } from "@/theme/tokens.stylex";

export type WeavePalette = { ground: string; warp: string[]; motif: string[] };

/**
 * A band of Underground moquette — the woven wool the Tube upholsters its seats
 * in, and the exact counterpart of the shag carpet on the New York side.
 *
 * The two bands are built on opposite rules, which is the whole argument for
 * splitting the system. Shag is a seeded PRNG: thousands of strands at random
 * lengths and leans, because a cut pile has no order. Moquette is woven on a
 * loom, so there is no randomness here at all — one motif, repeated exactly,
 * on a warp of fixed pitch. Same band, same job, opposite logic.
 */
const TILE = 68; // one repeat of the motif
const WARP = 3; // pitch of the woven grain

function draw(canvas: HTMLCanvasElement, pal: WeavePalette) {
  const w = canvas.clientWidth;
  const h = canvas.clientHeight;
  if (!w || !h) return;
  const dpr = Math.min(window.devicePixelRatio || 1, 1.5);
  canvas.width = Math.round(w * dpr);
  canvas.height = Math.round(h * dpr);
  const ctx = canvas.getContext("2d");
  if (!ctx) return;
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  ctx.fillStyle = pal.ground;
  ctx.fillRect(0, 0, w, h);

  const rows = Math.ceil(h / (TILE / 2)) + 1;
  const cols = Math.ceil(w / TILE) + 1;
  for (let row = 0; row < rows; row++) {
    const y = row * (TILE / 2);
    // Every other row steps half a tile, the way a woven repeat is set out.
    const offset = row % 2 ? TILE / 2 : 0;
    for (let col = -1; col < cols; col++) {
      const x = col * TILE + offset;
      // Most lozenges are ground; an accent lands on a fixed, woven interval.
      // Moquette is loud in life, but this family's whole argument is that the
      // color is spent sparingly, and the band has to make the same case.
      const n = row * 7 + col + (col < 0 ? cols : 0);
      const c = n % 5 === 2 ? pal.motif[n % pal.motif.length] : pal.warp[n % pal.warp.length];
      // A lozenge: the simplest shape a loom can hold an edge on.
      ctx.fillStyle = c;
      ctx.beginPath();
      ctx.moveTo(x + TILE / 2, y);
      ctx.lineTo(x + TILE, y + TILE / 4);
      ctx.lineTo(x + TILE / 2, y + TILE / 2);
      ctx.lineTo(x, y + TILE / 4);
      ctx.closePath();
      ctx.fill();
      // A bar through the lozenge, so the motif reads as a roundel at distance.
      ctx.fillStyle = pal.ground;
      ctx.fillRect(x + TILE * 0.28, y + TILE * 0.22, TILE * 0.44, TILE * 0.06);
    }
  }

  // The warp: fine vertical threads laid over everything, as on real moquette.
  ctx.globalAlpha = 0.16;
  for (let x = 0; x < w; x += WARP) {
    ctx.fillStyle = pal.warp[(x / WARP) % pal.warp.length];
    ctx.fillRect(x, 0, 1.4, h);
  }
  ctx.globalAlpha = 1;

  // The same shade Shag carries, so the two bands sit at the same depth.
  const shade = ctx.createLinearGradient(0, h * 0.55, 0, h);
  shade.addColorStop(0, "rgba(0,0,0,0)");
  shade.addColorStop(1, "rgba(0,0,0,0.28)");
  ctx.fillStyle = shade;
  ctx.fillRect(0, 0, w, h);
}

export function Weave({
  palettes,
  height = 120,
}: {
  palettes: Record<FlavorId, WeavePalette>;
  height?: number;
}) {
  const ref = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    const canvas = ref.current;
    if (!canvas) return;
    let width = 0;
    const paint = () => {
      width = canvas.clientWidth;
      draw(canvas, palettes[currentFlavor()] ?? palettes.moquette);
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
  // Before the canvas draws, a flat woven grain in CSS.
  canvas: {
    width: "100%",
    backgroundColor: color.mantle,
    backgroundImage: `linear-gradient(to bottom, transparent 55%, rgba(0,0,0,0.28)), repeating-linear-gradient(90deg, ${color.surface0} 0 2px, ${color.mantle} 2px 4px)`,
  },
  height: (height: number) => ({ height }),
});
