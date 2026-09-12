import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { StudioClient } from "@/components/StudioClient";

// A local tool, not part of the site. The GitHub Pages build sets STATIC_EXPORT,
// and this becomes a 404 there; `bun run dev` is where it lives.
export const metadata: Metadata = { title: "Studio", robots: { index: false, follow: false } };

export default function StudioPage() {
  if (process.env.STATIC_EXPORT === "1") notFound();
  return <StudioClient />;
}
