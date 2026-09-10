"use client";

/** Copy text, falling back to a hidden textarea when the clipboard API is missing or refuses. */
export async function copyText(text: string): Promise<boolean> {
  try {
    await navigator.clipboard.writeText(text);
    return true;
  } catch {
    const area = document.createElement("textarea");
    area.value = text;
    area.setAttribute("readonly", "");
    area.style.position = "fixed";
    area.style.opacity = "0";
    document.body.append(area);
    area.select();
    let ok = false;
    try {
      ok = document.execCommand("copy");
    } catch {}
    area.remove();
    return ok;
  }
}

/**
 * Copy a file fetched from `src`. The fetch is handed to the clipboard as a
 * promise so Safari still counts it as part of the click.
 */
export async function copyFrom(src: string): Promise<boolean> {
  const body = fetch(src).then((r) => {
    if (!r.ok) throw new Error(String(r.status));
    return r.text();
  });
  try {
    if (typeof ClipboardItem === "undefined") throw new Error("no ClipboardItem");
    const blob = body.then((t) => new Blob([t], { type: "text/plain" }));
    await navigator.clipboard.write([new ClipboardItem({ "text/plain": blob })]);
    return true;
  } catch {
    try {
      return await copyText(await body);
    } catch {
      return false;
    }
  }
}

/** Say something to screen readers through the page's polite live region (see layout.tsx). */
export function announce(message: string) {
  const region = document.getElementById("announcer");
  if (!region) return;
  region.textContent = "";
  window.setTimeout(() => {
    region.textContent = message;
  }, 50);
}
