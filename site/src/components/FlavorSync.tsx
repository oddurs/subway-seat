"use client";

import { useEffect } from "react";
import { watchFlavor } from "@/lib/flavor";

/** Keeps the flavor in step across tabs and with the OS setting. Renders nothing. */
export function FlavorSync() {
  useEffect(watchFlavor, []);
  return null;
}
