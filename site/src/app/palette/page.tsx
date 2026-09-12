import * as stylex from "@stylexjs/stylex";
import type { Metadata } from "next";
import Link from "next/link";
import { action } from "@/components/action";
import { blockHtml } from "@/components/blockHtml";
import { Footer } from "@/components/Footer";
import { Nav } from "@/components/Nav";
import { type PaletteGroup, PaletteTable } from "@/components/PaletteTable";
import { Section } from "@/components/Section";
import { BASE } from "@/lib/base";
import { portById } from "@/lib/manifest";
import {
  accents,
  type ColorName,
  contrast,
  type FlavorId,
  flavors,
  ground,
  roleNames,
  roleUses,
  shortName,
  textRoles,
} from "@/lib/palette";
import { pageMeta } from "@/lib/seo";
import { ink } from "@/theme/ink.stylex";
import { font } from "@/theme/type.stylex";

const TITLE = "The palette";
const DESCRIPTION =
  "Every Subway Seat color in all three flavors, in hex, RGB, HSL and OKLCH, with contrast and what each one is for. Copy any value, or download the palette for your design tools.";

export const metadata: Metadata = {
  title: "Palette",
  ...pageMeta("/palette", `${TITLE} · Subway Seat`, DESCRIPTION, {
    name: "palette.png",
    alt: "The Subway Seat palette: twenty-six colors in three flavors.",
  }),
};

const GROUPS: { title: string; roles: ColorName[]; contrast: boolean }[] = [
  { title: "Ground", roles: ground, contrast: false },
  { title: "Text", roles: textRoles, contrast: true },
  { title: "Accents", roles: accents, contrast: true },
];

const perFlavor = <T,>(fn: (id: FlavorId) => T) =>
  Object.fromEntries(flavors.map((f) => [f.id, fn(f.id)])) as Record<FlavorId, T>;

// Palette formats worth a one-click download, in the order designers reach for them.
const DOWNLOADS: { id: string; label: string }[] = [
  { id: "css", label: "CSS variables" },
  { id: "tailwind", label: "Tailwind" },
  { id: "scss", label: "Sass" },
  { id: "json", label: "JSON" },
  { id: "ase", label: "Adobe (.ase)" },
  { id: "gimp", label: "GIMP, Inkscape (.gpl)" },
  { id: "procreate", label: "Procreate" },
  { id: "txt", label: "Plain text" },
];

function downloads(flavor: FlavorId) {
  return DOWNLOADS.flatMap(({ id, label }) => {
    const port = portById(id);
    const file =
      port?.files.find((f) => f.flavor === flavor) ?? port?.files.find((f) => f.flavor === null);
    return port && file
      ? [
          {
            id,
            label,
            href: `${BASE}/files/${file.path.split("/").map(encodeURIComponent).join("/")}`,
          },
        ]
      : [];
  });
}

// One snippet, highlighted by each flavor's own VS Code theme.
const SAMPLE = `# The next northbound F
from dataclasses import dataclass

@dataclass(frozen=True)
class Seat:
    car: str
    row: int = 7
    window: bool = True

def find(seats, line="F"):
    """A window seat, facing forward."""
    free = [s for s in seats if s.window]
    return free[0] if free else None`;

export default async function PalettePage() {
  const groups: PaletteGroup[] = GROUPS.map((g) => ({
    title: g.title,
    rows: g.roles.map((role) => ({
      role,
      name: roleNames[role] ?? role,
      use: roleUses[role] ?? "",
      values: perFlavor((id) => flavors.find((f) => f.id === id)?.colors[role] ?? ""),
      contrast: g.contrast
        ? perFlavor((id) => {
            const c = flavors.find((f) => f.id === id)?.colors;
            return c ? contrast(c[role], c.base) : 0;
          })
        : undefined,
    })),
  }));
  const side = await Promise.all(
    flavors.map(async (f) => ({ f, html: await blockHtml(SAMPLE, "python", f.id) })),
  );

  return (
    <>
      <Nav />
      <main id="main" {...stylex.props(styles.main)}>
        <Section
          label="The palette"
          level={1}
          title="Twenty-six colors, three flavors."
          intro="Every port is written against these roles, not raw hex, so each flavor fills the same slots. Rows show all three flavors side by side, with each color's contrast on that flavor's base; the big swatch follows the one you're riding. Pick any value to copy it."
        >
          <PaletteTable
            groups={groups}
            flavors={flavors.map((f) => ({ id: f.id, label: shortName(f.id), colors: f.colors }))}
          />
        </Section>

        <Section
          id="downloads"
          label="Take it with you"
          title="For your design tools."
          intro={
            <>
              The palette as files, in the flavor you&apos;re riding. Each one has its own page
              under{" "}
              <Link href="/#ports" {...stylex.props(styles.link)}>
                Palettes &amp; formats
              </Link>
              .
            </>
          }
        >
          {flavors.map((f) => (
            <div key={f.id} data-only={f.id} {...stylex.props(styles.downloads)}>
              {downloads(f.id).map((d) => (
                <a key={d.id} href={d.href} download {...stylex.props(action.base, styles.big)}>
                  ↓ {d.label}
                </a>
              ))}
            </div>
          ))}
        </Section>

        <Section
          id="side-by-side"
          label="Side by side"
          title="The same code, three ways."
          intro="One file, highlighted by each flavor's own generated theme. The roles stay put; only the light changes."
        >
          <div {...stylex.props(styles.side)}>
            {side.map(({ f, html }) => (
              <figure
                key={f.id}
                aria-label={`${shortName(f.id)}: sample code`}
                {...stylex.props(styles.card, styles.paint(f.colors.base, f.colors.surface0))}
              >
                <figcaption {...stylex.props(styles.cardHead, styles.ink(f.colors.textHi))}>
                  {shortName(f.id)}
                  <span {...stylex.props(styles.cardBlurb, styles.ink(f.colors.subtext0))}>
                    {f.dark ? "dark" : "light"}
                  </span>
                </figcaption>
                <div
                  {...stylex.props(styles.cardCode)}
                  // biome-ignore lint/security/noDangerouslySetInnerHtml: build-time Shiki HTML
                  dangerouslySetInnerHTML={{ __html: html }}
                />
              </figure>
            ))}
          </div>
        </Section>
      </main>
      <Footer />
    </>
  );
}

const styles = stylex.create({
  main: { maxWidth: 1200, paddingInline: 24, marginInline: "auto" },
  link: {
    color: {
      default: ink.accent,
      ":hover": ink.accentHover,
    },
  },
  downloads: { display: "flex", flexWrap: "wrap", gap: 8 },
  big: { paddingBlock: 8, paddingInline: 14, fontSize: 13 },
  side: {
    display: "grid",
    gridTemplateColumns: "repeat(auto-fit, minmax(min(100%, 330px), 1fr))",
    gap: 18,
  },
  card: {
    minWidth: 0,
    margin: 0,
    overflow: "hidden",
    borderStyle: "solid",
    borderWidth: 1,
    borderRadius: "var(--radius-card)",
    boxShadow: "0 14px 34px var(--ss-shadow-soft)",
  },
  paint: (bg: string, edge: string) => ({ backgroundColor: bg, borderColor: edge }),
  ink: (fg: string) => ({ color: fg }),
  cardHead: {
    display: "flex",
    gap: 10,
    alignItems: "baseline",
    paddingInline: 16,
    paddingTop: 14,
    fontFamily: font.display,
    fontSize: 24,
    fontVariationSettings: '"SOFT" 100, "WONK" 1',
    fontWeight: 700,
  },
  cardBlurb: { fontFamily: font.sans, fontSize: 13, fontWeight: 400 },
  cardCode: { overflowX: "auto" },
});
