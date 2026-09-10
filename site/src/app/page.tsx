import * as stylex from "@stylexjs/stylex";
import Link from "next/link";
import { ClaudeSpotlight } from "@/components/ClaudeSpotlight";
import { Command } from "@/components/Command";
import { FlavorCards } from "@/components/FlavorCards";
import { Footer } from "@/components/Footer";
import { HerdrDemo } from "@/components/HerdrDemo";
import { Hero } from "@/components/Hero";
import { Nav } from "@/components/Nav";
import { Palette } from "@/components/Palette";
import { PortGrid } from "@/components/PortGrid";
import { Routes } from "@/components/Routes";
import { Section } from "@/components/Section";
import { Shag, type ShagPalette } from "@/components/Shag";
import { TerminalDemo } from "@/components/TerminalDemo";
import { Workbench } from "@/components/Workbench";
import { installCommand } from "@/lib/install";
import { ports } from "@/lib/manifest";
import { type FlavorId, flavors } from "@/lib/palette";
import { ink } from "@/theme/ink.stylex";

const shag = Object.fromEntries(
  flavors.map((f) => {
    const c = f.colors;
    const palette: ShagPalette = {
      ground: c.mantle,
      fibers: [c.crust, c.mantle, c.base, c.surface0, c.surface1, c.surface2, c.overlay0],
      threads: [c.orange, c.yellow, c.clay, c.red, c.green, c.orangeHi],
    };
    return [f.id, palette];
  }),
) as Record<FlavorId, ShagPalette>;

export default function Home() {
  const count = ports().length;
  return (
    <>
      <Nav />
      <main id="main">
        <Hero count={count} />
        <Shag palettes={shag} height={130} />
        <div {...stylex.props(styles.sections)}>
          <Section
            id="flavors"
            label="Three flavors"
            title="Pick a seat."
            intro="Walnut is the original. Tunnel is the late local after midnight. Enamel is the same car in morning sun. Pick one and the whole site changes with you."
          >
            <FlavorCards flavors={flavors} />
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
            title="Brown, cream, and the good stuff."
            intro="A brown ground, a cream text ramp, and seven accents. Blue is faded denim and only marks links; magenta got reassigned to burnt orange. Pick a chip to copy it."
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
            intro="Every port is generated from the same palette, in all three flavors, with install steps and the full file to copy."
          >
            <PortGrid />
          </Section>
        </div>
      </main>
      <Footer />
    </>
  );
}

const styles = stylex.create({
  sections: {
    maxWidth: 1200,
    paddingInline: 24,
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
