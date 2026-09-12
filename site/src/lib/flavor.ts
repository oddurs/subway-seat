"use client";

import { type FamilyId, type FlavorId, familyById, flavorById } from "./palette";

export const FLAVOR_KEY = "subway-seat:flavor";
export const FAMILY_KEY = "subway-seat:family";
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

export function currentFamily(): FamilyId {
  return (document.documentElement.dataset.family as FamilyId) ?? "new-york";
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
  root.dataset.family = flavorById[id].family;
  root.style.colorScheme = flavorById[id].dark ? "dark" : "light";
  window.dispatchEvent(new CustomEvent(FLAVOR_EVENT, { detail: id }));
}

/** Switch the whole site to a flavor and remember the choice. */
/** The dark default, or the light flavor, of one family. */
function pick(family: string, light: boolean): FlavorId {
  const fam = familyById[family as FamilyId];
  return (light ? fam.light : fam.default) as FlavorId;
}

/** Switch cities, staying on the light or dark you were already riding. */
export function setFamily(family: FamilyId) {
  setFlavor(pick(family, !flavorById[currentFlavor()].dark));
}

export function setFlavor(id: FlavorId) {
  apply(id);
  try {
    localStorage.setItem(FLAVOR_KEY, id);
    localStorage.setItem(FAMILY_KEY, flavorById[id].family);
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
    const fam = (document.documentElement.dataset.family ?? "new-york") as FamilyId;
    apply(pick(fam, light.matches));
  };
  window.addEventListener("storage", onStorage);
  light.addEventListener("change", onScheme);
  return () => {
    window.removeEventListener("storage", onStorage);
    light.removeEventListener("change", onScheme);
  };
}
