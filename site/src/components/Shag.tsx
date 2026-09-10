"use client";

import * as stylex from "@stylexjs/stylex";
import { useEffect, useRef } from "react";
import { currentFlavor, FLAVOR_EVENT } from "@/lib/flavor";
import type { FlavorId } from "@/lib/palette";
import { color } from "@/theme/tokens.stylex";

export type ShagPalette = { ground: string; fibers: string[]; threads: string[] };

// Small, seeded PRNG so the rug is the same rug on every load.
function mulberry32(seed: number) {
  return () => {
    seed |= 0;
    seed = (seed + 0x6d2b79f5) | 0;
    let t = Math.imul(seed ^ (seed >>> 15), 1 | seed);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

function draw(canvas: HTMLCanvasElement, pal: ShagPalette) {
  const w = canvas.clientWidth;
  const h = canvas.clientHeight;
  const dpr = Math.min(window.devicePixelRatio || 1, 1.5);
  canvas.width = Math.round(w * dpr);
  canvas.height = Math.round(h * dpr);
  const ctx = canvas.getContext("2d");
  if (!ctx) return;
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  ctx.fillStyle = pal.ground;
  ctx.fillRect(0, 0, w, h);

  const rand = mulberry32(1970);
  // Phones get a looser pile: the same look for a fraction of the strands.
  const count = Math.floor((w * h) / (w < 640 ? 7 : 4.5));
  // Fibers lie in patches, the way a real rug gets brushed.
  const flow = (x: number, y: number) =>
    Math.sin(x / 70 + Math.cos(y / 45)) * 0.55 + Math.sin(x / 23) * 0.15;
  const strands = Array.from({ length: count }, () => {
    const x = rand() * w;
    const y = h * 0.1 + rand() * h * 1.0;
    return {
      x,
      y,
      len: 14 + rand() * 20,
      lean: flow(x, y) + (rand() - 0.5) * 0.45,
      width: 2 + rand() * 2.2,
      thread: rand() < 0.1,
      pick: rand(),
    };
  });
  // Back to front, so nearer strands lie over the ones behind them.
  strands.sort((a, b) => a.y - b.y);
  ctx.lineCap = "round";
  for (const s of strands) {
    const pool = s.thread ? pal.threads : pal.fibers;
    ctx.strokeStyle = pool[Math.floor(s.pick * pool.length)];
    ctx.lineWidth = s.width;
    ctx.beginPath();
    ctx.moveTo(s.x, s.y);
    ctx.quadraticCurveTo(
      s.x + s.lean * s.len * 0.3,
      s.y - s.len * 0.7,
      s.x + s.lean * s.len,
      s.y - s.len,
    );
    ctx.stroke();
  }
  // Soft shade along the bottom, where the pile goes into shadow.
  const shade = ctx.createLinearGradient(0, h * 0.55, 0, h);
  shade.addColorStop(0, "rgba(0,0,0,0)");
  shade.addColorStop(1, "rgba(0,0,0,0.28)");
  ctx.fillStyle = shade;
  ctx.fillRect(0, 0, w, h);
}

/** A band of 70s shag carpet, drawn in the current flavor's colors. */
export function Shag({
  palettes,
  height = 120,
}: {
  palettes: Record<FlavorId, ShagPalette>;
  height?: number;
}) {
  const ref = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    const canvas = ref.current;
    if (!canvas) return;
    let width = 0;
    const paint = () => {
      width = canvas.clientWidth;
      draw(canvas, palettes[currentFlavor()] ?? palettes.walnut);
    };
    // First paint when the browser is idle, so the rug never holds up the page.
    const idle = window.requestIdleCallback ?? ((cb: () => void) => window.setTimeout(cb, 1));
    const cancelIdle = window.cancelIdleCallback ?? window.clearTimeout;
    const first = idle(paint);
    let timer: ReturnType<typeof setTimeout>;
    // Only a new width needs a new rug; phones resize the height as the URL bar slides.
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
  // Until the canvas draws (or without JavaScript), a brushed pile in CSS.
  canvas: {
    width: "100%",
    backgroundColor: color.mantle,
    backgroundImage: `linear-gradient(to bottom, transparent 55%, rgba(0,0,0,0.28)), repeating-linear-gradient(100deg, ${color.base} 0 3px, ${color.surface0} 3px 5px, ${color.mantle} 5px 8px, ${color.surface1} 8px 9px, ${color.crust} 9px 11px)`,
  },
  height: (height: number) => ({ height }),
});
