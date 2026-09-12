import * as stylex from "@stylexjs/stylex";
import Link from "next/link";
import { ClaudeSpotlight } from "@/components/ClaudeSpotlight";
import { Command } from "@/components/Command";
import { FlavorCards } from "@/components/FlavorCards";
import { Footer } from "@/components/Footer";
import { HerdrDemo } from "@/components/HerdrDemo";
import { Hero } from "@/components/Hero";
import { LastStop } from "@/components/LastStop";
import { Nav } from "@/components/Nav";
import { Palette } from "@/components/Palette";
import { PortGrid } from "@/components/PortGrid";
import { Routes } from "@/components/Routes";
import { Section } from "@/components/Section";
import { Shag, type ShagPalette } from "@/components/Shag";
import { Weave, type WeavePalette } from "@/components/Weave";
import { TerminalDemo } from "@/components/TerminalDemo";
import { Workbench } from "@/components/Workbench";
import { installCommand } from "@/lib/install";
import { ports } from "@/lib/manifest";
import { type FlavorId, flavors } from "@/lib/palette";
import { ink } from "@/theme/ink.stylex";
import { space } from "@/theme/space.stylex";

const shag = Object.fromEntries(
  flavors.map((f) => {
    const c = f.colors;
    const a = f.art;
    const palette: ShagPalette = {
      ground: c.mantle,
      fibers: [c.crust, c.mantle, c.base, c.surface0, c.surface1, c.surface2, c.overlay0],
      threads: [a.orange, a.yellow, a.clay, a.red, a.green, a.orange],
    };
    return [f.id, palette];
  }),
) as Record<FlavorId, ShagPalette>;

const weave = Object.fromEntries(
  flavors.map((f) => {
    const c = f.colors;
    const a = f.art;
    const palette: WeavePalette = {
      ground: c.mantle,
      // The quiet field the motif is woven into, and the few threads that aren't.
      warp: [c.surface0, c.base, c.surface1, c.crust, c.surface0, c.surface2],
      motif: [a.red, a.denim, a.yellow, a.green, a.orange, a.sage],
    };
    return [f.id, palette];
  }),
) as Record<FlavorId, WeavePalette>;

export default function Home() {
  const count = ports().length;
  return (
    <>
      <Nav />
      <main id="main">
        <Hero count={count} />
        <div data-only="new-york">
          <Shag palettes={shag} height={130} />
        </div>
        <div data-only="london">
          <Weave palettes={weave} height={130} />
        </div>
        <div {...stylex.props(styles.sections)}>
          <Section
            id="flavors"
            label="Two cities, six flavors"
            title="Pick a seat."
            intro="Every flavor defines the same 26 roles, so a port written against roles works in all of them. New York rides warm; London rides cool and spends its color far more carefully. Pick one and the whole site changes with you — type, texture and signage included."
          >
            <div data-only="new-york">
              <FlavorCards flavors={flavors.filter((f) => f.family === "new-york")} />
            </div>
            <div data-only="london">
              <FlavorCards flavors={flavors.filter((f) => f.family === "london")} />
            </div>
          </Section>

          <Section
            id="install"
            label="Get on board"
            title="One line, and you're seated."
            intro="The installer looks for the apps you have, shows you the plan and asks once. It uses the flavor you're riding now, and everything it does comes back out with uninstall."
          >
            <div {...stylex.props(styles.install)}>
              {flavors.map((f) => (
                <div key={f.id} data-only={f.id}>
                  <Command text={installCommand({ flavor: f.id })} />
                </div>
              ))}
              <Link href="/install" {...stylex.props(styles.more)}>
                Pick your apps, follow light and dark, or clone the repo →
              </Link>
            </div>
          </Section>

          <Section
            id="palette"
            label="The palette"
            title="Nine grounds, four texts, thirteen accents."
            intro="The same 26 slots in both cities. New York fills them warm — blue faded to denim, magenta reassigned to burnt orange. London fills them from the network: brick, the platform-edge yellow, District green, Corporate Blue and the standard red. Pick a chip to copy it."
          >
            <Palette />
            <Routes />
          </Section>

          <Section
            id="vscode"
            label="In VS Code"
            title="Layered like a good living room."
            intro="One chrome ground, grooves instead of lines, popovers lifted onto paper, and every hover and selection a thin wash of text color, so they sit right on any surface. This window is painted with the real theme file."
          >
            <Workbench />
          </Section>

          <Section
            id="terminal"
            label="In the terminal"
            title="Ghostty, fish and friends."
            intro="The 16 ANSI colors are chosen so terminal tools land in the palette too: magenta is burnt orange, blue is denim, cyan is seafoam. Starship's segments become a 70s stripe."
          >
            <div {...stylex.props(styles.stack)}>
              <TerminalDemo />
              <HerdrDemo />
            </div>
          </Section>

          <Section id="claude" label="In Claude Code" title="Themed all the way down.">
            <ClaudeSpotlight />
          </Section>

          <Section
            id="ports"
            label="Ports"
            title={`${count} ports and counting.`}
            intro="Every port is generated from the same palette, in all six flavors, with install steps and the full file to copy. Not one of them knows which city it's in."
          >
            <PortGrid />
          </Section>
        </div>
        <LastStop />
      </main>
      <Footer />
    </>
  );
}

const styles = stylex.create({
  sections: {
    maxWidth: space.measure,
    paddingInline: space.gutter,
    marginInline: "auto",
  },
  install: { display: "grid", gridTemplateColumns: "minmax(0, 1fr)", gap: 14, maxWidth: 860 },
  more: {
    justifySelf: "start",
    fontWeight: 600,
    color: {
      default: ink.accent,
      ":hover": ink.accentHover,
    },
    textDecoration: "none",
    outlineWidth: 2,
    outlineStyle: {
      default: "none",
      ":focus-visible": "solid",
    },
    outlineColor: ink.accent,
    outlineOffset: 2,
    borderRadius: 2,
  },
  stack: {
    display: "grid",
    gridTemplateColumns: {
      default: "minmax(0, 1fr)",
      "@media (min-width: 1200px)": "auto minmax(0, 1fr)",
    },
    gap: 28,
  },
});
