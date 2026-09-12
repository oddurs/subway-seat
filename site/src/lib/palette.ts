import data from "@/theme/palette.json";

export type ColorName = keyof (typeof data.flavors)[number]["colors"];
export type FlavorId = "walnut" | "tunnel" | "enamel" | "moquette" | "deep" | "portland";
export type FamilyId = "new-york" | "london";

export type Flavor = {
  id: FlavorId;
  family: FamilyId;
  name: string;
  slug: string;
  dark: boolean;
  blurb: string;
  colors: Record<ColorName, string>;
  ansi: ColorName[];
};

export type Family = {
  id: FamilyId;
  name: string;
  blurb: string;
  /** The one accent this family spends on identity. */
  lead: ColorName;
  roleNames: Partial<Record<ColorName, string>>;
  flavors: FlavorId[];
  default: FlavorId;
  light: FlavorId;
};

export const flavors = data.flavors as Flavor[];
export const flavorById = Object.fromEntries(flavors.map((f) => [f.id, f])) as Record<
  FlavorId,
  Flavor
>;
export const walnut = flavorById.walnut;

export const families = data.families as Family[];
export const familyById = Object.fromEntries(families.map((f) => [f.id, f])) as Record<
  FamilyId,
  Family
>;

/** The family a flavor belongs to. */
export function familyOf(id: FlavorId): Family {
  return familyById[flavorById[id].family];
}

/** The flavors of one family, in order. */
export function flavorsOf(family: FamilyId) {
  return flavors.filter((f) => f.family === family);
}

/** The short name the site uses for a flavor — the part after the city. */
const SHORT: Record<FlavorId, string> = {
  walnut: "Walnut",
  tunnel: "Tunnel",
  enamel: "Enamel",
  moquette: "Moquette",
  deep: "Deep Level",
  portland: "Portland",
};

export function shortName(id: FlavorId) {
  return SHORT[id];
}

/** What this flavor's own family calls a role. */
export function roleName(id: FlavorId, role: ColorName) {
  return familyOf(id).roleNames[role] ?? roleNames[role];
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
