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

export const ground = data.ground as ColorName[];
export const textRoles = data.text as ColorName[];
export const accents = data.accents as ColorName[];
export const roleNames = data.roleNames as Partial<Record<ColorName, string>>;
export const accentRoles = data.accentRoles as Partial<Record<ColorName, string>>;
