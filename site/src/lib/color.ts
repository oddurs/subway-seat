/** Color formats for the palette page: hex, rgb(), hsl(), oklch() and CSS variables. */

export type Format = "hex" | "rgb" | "hsl" | "oklch";

export const FORMATS: { id: Format; label: string }[] = [
  { id: "hex", label: "HEX" },
  { id: "rgb", label: "RGB" },
  { id: "hsl", label: "HSL" },
  { id: "oklch", label: "OKLCH" },
];

function channels(hex: string) {
  return [1, 3, 5].map((i) => Number.parseInt(hex.slice(i, i + 2), 16));
}

const round = (n: number, digits = 0) => {
  const f = 10 ** digits;
  return Math.round(n * f) / f;
};

function hsl(hex: string) {
  const [r, g, b] = channels(hex).map((v) => v / 255);
  const max = Math.max(r, g, b);
  const min = Math.min(r, g, b);
  const l = (max + min) / 2;
  const d = max - min;
  if (d === 0) return [0, 0, l * 100];
  const s = d / (1 - Math.abs(2 * l - 1));
  let h = max === r ? ((g - b) / d) % 6 : max === g ? (b - r) / d + 2 : (r - g) / d + 4;
  h *= 60;
  if (h < 0) h += 360;
  return [h, s * 100, l * 100];
}

function oklch(hex: string) {
  const [r, g, b] = channels(hex).map((v) => {
    const c = v / 255;
    return c <= 0.04045 ? c / 12.92 : ((c + 0.055) / 1.055) ** 2.4;
  });
  const l = Math.cbrt(0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b);
  const m = Math.cbrt(0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b);
  const s = Math.cbrt(0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b);
  const L = 0.2104542553 * l + 0.793617785 * m - 0.0040720468 * s;
  const A = 1.9779984951 * l - 2.428592205 * m + 0.4505937099 * s;
  const B = 0.0259040371 * l + 0.7827717662 * m - 0.808675766 * s;
  const C = Math.sqrt(A * A + B * B);
  let H = (Math.atan2(B, A) * 180) / Math.PI;
  if (H < 0) H += 360;
  return [L, C, H];
}

export function formatColor(hex: string, format: Format) {
  switch (format) {
    case "rgb":
      return `rgb(${channels(hex).join(" ")})`;
    case "hsl": {
      const [h, s, l] = hsl(hex);
      return `hsl(${round(h)} ${round(s)}% ${round(l)}%)`;
    }
    case "oklch": {
      const [L, C, H] = oklch(hex);
      return `oklch(${round(L * 100, 1)}% ${round(C, 3)} ${round(H, 1)})`;
    }
    default:
      return hex;
  }
}

/** `--ss-text-hi` from `textHi`, the same names as the CSS port. */
export function cssVarName(role: string) {
  return `--ss-${role.replace(/[A-Z]/g, (c) => `-${c.toLowerCase()}`)}`;
}

export function cssVariables(colors: Record<string, string>, format: Format) {
  const lines = Object.entries(colors).map(
    ([role, hex]) => `  ${cssVarName(role)}: ${formatColor(hex, format)};`,
  );
  return `:root {\n${lines.join("\n")}\n}\n`;
}
