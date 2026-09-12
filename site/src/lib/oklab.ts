/**
 * The colour math the palette is actually solved in, ported from palette.py so
 * the studio computes exactly what `build.py` would.
 *
 * Everything here works in OKLCH: lightness, chroma and hue as three numbers
 * you can move independently. That's the whole reason the palette is built this
 * way — in hex or HSL there is no knob for "same colour, more colourful", and
 * "same lightness, different hue" doesn't hold its lightness.
 */

const srgbToLinear = (c: number) => (c <= 0.04045 ? c / 12.92 : ((c + 0.055) / 1.055) ** 2.4);
const linearToSrgb = (c: number) => (c <= 0.0031308 ? 12.92 * c : 1.055 * c ** (1 / 2.4) - 0.055);

export const rgbOf = (hex: string) =>
  [1, 3, 5].map((i) => Number.parseInt(hex.slice(i, i + 2), 16)) as [number, number, number];

export type Lch = { L: number; C: number; h: number };

export function toLch(hex: string): Lch {
  const [r, g, b] = rgbOf(hex).map((v) => srgbToLinear(v / 255));
  const l = Math.cbrt(0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b);
  const m = Math.cbrt(0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b);
  const s = Math.cbrt(0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b);
  const L = 0.2104542553 * l + 0.793617785 * m - 0.0040720468 * s;
  const a = 1.9779984951 * l - 2.428592205 * m + 0.4505937099 * s;
  const bb = 0.0259040371 * l + 0.7827717662 * m - 0.808675766 * s;
  return { L, C: Math.hypot(a, bb), h: ((Math.atan2(bb, a) * 180) / Math.PI + 360) % 360 };
}

function linearOf(L: number, C: number, h: number) {
  const a = C * Math.cos((h * Math.PI) / 180);
  const b = C * Math.sin((h * Math.PI) / 180);
  const l = (L + 0.3963377774 * a + 0.2158037573 * b) ** 3;
  const m = (L - 0.1055613458 * a - 0.0638541728 * b) ** 3;
  const s = (L - 0.0894841775 * a - 1.291485548 * b) ** 3;
  return [
    4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
    -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
    -0.0041960863 * l - 0.7034186147 * m + 1.707614701 * s,
  ];
}

/** OKLCH → #RRGGBB, with chroma binary-searched down into the sRGB gamut. */
export function fromLch({ L, C, h }: Lch): string {
  let lo = 0;
  let hi = C;
  for (let i = 0; i < 28; i++) {
    const mid = (lo + hi) / 2;
    if (linearOf(L, mid, h).every((v) => v >= -1e-4 && v <= 1 + 1e-4)) lo = mid;
    else hi = mid;
  }
  return `#${linearOf(L, lo, h)
    .map((v) =>
      Math.round(Math.min(1, Math.max(0, linearToSrgb(v))) * 255)
        .toString(16)
        .padStart(2, "0"),
    )
    .join("")
    .toUpperCase()}`;
}

export function luminance(hex: string) {
  const [r, g, b] = rgbOf(hex).map((v) => srgbToLinear(v / 255));
  return 0.2126 * r + 0.7152 * g + 0.0722 * b;
}

export function contrast(a: string, b: string) {
  const [hi, lo] = [luminance(a), luminance(b)].sort((x, y) => y - x);
  return (hi + 0.05) / (lo + 0.05);
}

/** palette.blend: mix fg over bg at alpha. */
export function blend(fg: string, bg: string, alpha: number) {
  const f = rgbOf(fg);
  const b = rgbOf(bg);
  return `#${f
    .map((v, i) =>
      Math.round(v * alpha + b[i] * (1 - alpha))
        .toString(16)
        .padStart(2, "0"),
    )
    .join("")
    .toUpperCase()}`;
}
