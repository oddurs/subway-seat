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

/** For useSyncExternalStore: re-render when the flavor changes. */
export function subscribeFlavor(onChange: () => void) {
  window.addEventListener(FLAVOR_EVENT, onChange);
  return () => window.removeEventListener(FLAVOR_EVENT, onChange);
}

function apply(id: FlavorId) {
  const root = document.documentElement;
  const classes = themeClasses();
  if (!classes[id]) return;
  for (const cls of Object.values(classes)) {
    for (const c of cls.split(" ")) if (c) root.classList.remove(c);
  }
  for (const c of classes[id].split(" ")) if (c) root.classList.add(c);
  root.dataset.flavor = id;
  root.style.colorScheme = id === "enamel" ? "light" : "dark";
  window.dispatchEvent(new CustomEvent(FLAVOR_EVENT, { detail: id }));
}

/** Switch the whole site to a flavor and remember the choice. */
export function setFlavor(id: FlavorId) {
  apply(id);
  try {
    localStorage.setItem(FLAVOR_KEY, id);
  } catch {}
}

function saved(): FlavorId | null {
  try {
    return localStorage.getItem(FLAVOR_KEY) as FlavorId | null;
  } catch {
    return null;
  }
}

/** Keep tabs in step, and follow the OS light/dark setting until a flavor is picked. */
export function watchFlavor() {
  const light = matchMedia("(prefers-color-scheme: light)");
  const onStorage = (e: StorageEvent) => {
    if (e.key === FLAVOR_KEY && e.newValue) apply(e.newValue as FlavorId);
  };
  const onScheme = () => {
    if (saved() || new URLSearchParams(location.search).has("flavor")) return;
    apply(light.matches ? "enamel" : "walnut");
  };
  window.addEventListener("storage", onStorage);
  light.addEventListener("change", onScheme);
  return () => {
    window.removeEventListener("storage", onStorage);
    light.removeEventListener("change", onScheme);
  };
}
