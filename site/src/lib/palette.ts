import data from "@/theme/palette.json";

export type ColorName = keyof (typeof data.flavors)[number]["colors"];
export type FlavorId = "walnut" | "tunnel" | "enamel";

export type Flavor = {
  id: FlavorId;
  name: string;
  slug: string;
  dark: boolean;
  blurb: string;
  colors: Record<ColorName, string>;
  ansi: ColorName[];
};

export const flavors = data.flavors as Flavor[];
export const flavorById = Object.fromEntries(flavors.map((f) => [f.id, f])) as Record<
  FlavorId,
  Flavor
>;
export const walnut = flavorById.walnut;

/** The short name the site uses for a flavor: Walnut, Tunnel, Enamel. Files keep the full name. */
export function shortName(id: FlavorId) {
  return id.charAt(0).toUpperCase() + id.slice(1);
}

export const roles = data.roles as ColorName[];
export const ground = data.ground as ColorName[];
export const textRoles = data.text as ColorName[];
export const accents = data.accents as ColorName[];
export const roleNames = data.roleNames as Partial<Record<ColorName, string>>;
export const accentRoles = data.accentRoles as Partial<Record<ColorName, string>>;
/** What each role is used for; older palette.json files only describe the accents. */
export const roleUses: Partial<Record<ColorName, string>> = {
  ...accentRoles,
  ...((data as { roleUses?: Partial<Record<ColorName, string>> }).roleUses ?? {}),
};

/** WCAG relative luminance of #RRGGBB. */
export function luminance(hex: string) {
  const [r, g, b] = [1, 3, 5].map((i) => {
    const v = Number.parseInt(hex.slice(i, i + 2), 16) / 255;
    return v <= 0.04045 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4;
  });
  return 0.2126 * r + 0.7152 * g + 0.0722 * b;
}

/** WCAG contrast ratio between two #RRGGBB colors. */
export function contrast(a: string, b: string) {
  const [hi, lo] = [luminance(a), luminance(b)].sort((x, y) => y - x);
  return (hi + 0.05) / (lo + 0.05);
}

/** Whichever of two inks reads better on a fill. */
export function bestInk(fill: string, dark: string, light: string) {
  return contrast(fill, dark) >= contrast(fill, light) ? dark : light;
}
