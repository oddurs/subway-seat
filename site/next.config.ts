import type { NextConfig } from "next";

// `STATIC_EXPORT=1 NEXT_PUBLIC_BASE_PATH=/subway-seat bun run build` produces the
// GitHub Pages site in out/; a plain build serves it with `next start`.
const basePath = process.env.NEXT_PUBLIC_BASE_PATH || undefined;

const nextConfig: NextConfig = {
  basePath,
  ...(process.env.STATIC_EXPORT === "1" ? { output: "export", trailingSlash: true } : {}),
};

export default nextConfig;
