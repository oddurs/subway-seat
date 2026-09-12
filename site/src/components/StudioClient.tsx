"use client";

import dynamic from "next/dynamic";

/**
 * The studio is a local tool with no server half: it reads its saved edits out
 * of localStorage on the first render, which only works if there is no server
 * render to disagree with. Loading it client-only is what buys that.
 */
const Studio = dynamic(() => import("./Studio").then((m) => m.Studio), { ssr: false });

export function StudioClient() {
  return <Studio />;
}
