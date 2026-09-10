"use client";

import type { FlavorId } from "./palette";

export const FLAVOR_KEY = "subway-seat:flavor";
export const FLAVOR_EVENT = "subway-seat:flavor";

/** Theme class names, written into <html data-theme-classes> by the layout. */
function themeClasses(): Record<FlavorId, string> {
  try {
    return JSON.parse(document.documentElement.dataset.themeClasses ?? "{}");
  } catch {
    return {} as Record<FlavorId, string>;
  }
}

export function currentFlavor(): FlavorId {
  return (document.documentElement.dataset.flavor as FlavorId) ?? "walnut";
}

export function setFlavor(id: FlavorId) {
  const root = document.documentElement;
  const classes = themeClasses();
  for (const cls of Object.values(classes)) {
    for (const c of cls.split(" ")) if (c) root.classList.remove(c);
  }
  for (const c of (classes[id] ?? "").split(" ")) if (c) root.classList.add(c);
  root.dataset.flavor = id;
  root.style.colorScheme = id === "enamel" ? "light" : "dark";
  try {
    localStorage.setItem(FLAVOR_KEY, id);
  } catch {}
  window.dispatchEvent(new CustomEvent(FLAVOR_EVENT, { detail: id }));
}
