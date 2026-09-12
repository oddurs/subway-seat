import * as stylex from "@stylexjs/stylex";
import type { Metadata } from "next";
import { Command } from "@/components/Command";
import { Configurator, type FlavorPaint, type InstallPort } from "@/components/Configurator";
import { Footer } from "@/components/Footer";
import { Nav } from "@/components/Nav";
import { Section } from "@/components/Section";
import { INSTALL_URL } from "@/lib/install";
import { byCategory, categoryLabel, ports, setupFor } from "@/lib/manifest";
import { families, type FlavorId, flavorById, flavors, shortName } from "@/lib/palette";
import { pageMeta } from "@/lib/seo";
import { ink } from "@/theme/ink.stylex";
import { space } from "@/theme/space.stylex";
import { color } from "@/theme/tokens.stylex";
import { font } from "@/theme/type.stylex";

const DESCRIPTION =
  "Install Subway Seat in one line: pick a flavor (or follow your system's light and dark), pick your apps, and paste. Switch flavors or take it all back out later.";

export const metadata: Metadata = {
  title: "Install",
  ...pageMeta("/install", "Install · Subway Seat", DESCRIPTION, {
    name: "install.png",
    alt: "Install Subway Seat in one line.",
  }),
};

const remote = (args: string) => `curl -fsSL ${INSTALL_URL} | sh -s -- ${args}`;

const LATER = [
  {
    title: "Change seats",
    body: "Points every app it set up at another flavor, in one go.",
    code: remote("switch enamel"),
  },
  {
    title: "Check your ticket",
    body: "Shows what's installed, and in which flavor.",
    code: remote("status"),
  },
  {
    title: "Get off at the next stop",
    body: "Removes every file it linked and every block it added between its markers. The rest of your config stays as it was.",
    code: remote("uninstall"),
  },
];

const RIDE = [
  [
    "Looks around",
    "For each app it checks for the command on your PATH or the app in /Applications.",
  ],
  ["Shows the plan", "Every file it will link and every line it will add, then asks once."],
  ["Links the themes", "Files are linked, not copied, so an update reaches every app at once."],
  [
    "Switches them on",
    "Where a config line turns the theme on, it's added between # >>> subway-seat >>> markers.",
  ],
  [
    "Leaves you a note",
    "Anything it can't do for you (an import dialog, a settings pane) it prints at the end.",
  ],
];

export default function InstallPage() {
  const all = ports();
  const installPorts: InstallPort[] = all.map((p) => ({
    id: p.id,
    name: p.name,
    category: p.category,
    label: categoryLabel(p.category),
    setup: setupFor(p),
    detect: Boolean(p.detect?.length),
    auto: Boolean(p.auto),
  }));
  // One set of cards per city; the Configurator shows the one you're riding.
  const paints: FlavorPaint[] = [
    ...flavors.map((f) => ({
      id: f.id,
      key: f.id,
      family: f.family,
      name: shortName(f.id),
      note: f.blurb,
      bg: f.colors.base,
      fg: f.colors.textHi,
      sub: f.colors.subtext0,
      stripe: [f.colors.red, f.colors.orange, f.colors.yellow, f.colors.green, f.colors.text],
    })),
    ...families.map((fam) => {
      const dark = flavorById[fam.default as FlavorId].colors;
      const light = flavorById[fam.light as FlavorId].colors;
      return {
        id: "auto" as const,
        key: `auto-${fam.id}`,
        family: fam.id,
        name: "Auto",
        note: `${shortName(fam.default as FlavorId)} or ${shortName(fam.light as FlavorId)}, following your system's light and dark.`,
        // The light flavor by day, with the dark one coming up in the corner.
        bg: light.base,
        image: `radial-gradient(circle at 100% 100%, ${dark.base} 0 46px, ${dark.surface1} 47px 49px, transparent 50px)`,
        fg: light.textHi,
        sub: light.subtext0,
        stripe: [light.red, light.orange, light.yellow, light.green, light.text],
      };
    }),
  ];

  return (
    <>
      <Nav />
      <main id="main" {...stylex.props(styles.main)}>
        <Section
          label="Get on board"
          level={1}
          title="Take a seat in one line."
          intro={`Pick a flavor, pick your stops, and paste what comes out. The installer finds the apps you have among all ${all.length} ports, shows its plan, and asks once before it touches anything.`}
        >
          <Configurator
            ports={installPorts}
            paints={paints}
            categories={byCategory().map((g) => ({
              category: g.category,
              label: categoryLabel(g.category),
            }))}
          />
        </Section>

        <Section id="the-ride" label="The ride" title="What it does, stop by stop.">
          <ol {...stylex.props(styles.ride)}>
            {RIDE.map(([title, body], i) => (
              <li key={title} {...stylex.props(styles.rideStop)}>
                <span aria-hidden {...stylex.props(styles.rideNumber)}>
                  {i + 1}
                </span>
                <b {...stylex.props(styles.rideTitle)}>{title}</b>
                <span {...stylex.props(styles.rideBody)}>{body}</span>
              </li>
            ))}
          </ol>
        </Section>

        <Section
          id="later"
          label="Later on"
          title="Change seats, or get off."
          intro="The same script handles the rest of the trip. From a clone, run ./install.sh with the same words."
        >
          <div {...stylex.props(styles.later)}>
            {LATER.map((l) => (
              <div key={l.title} {...stylex.props(styles.laterCard)}>
                <div>
                  <h3 {...stylex.props(styles.laterTitle)}>{l.title}</h3>
                  <p {...stylex.props(styles.laterBody)}>{l.body}</p>
                </div>
                <Command text={l.code} sunk />
              </div>
            ))}
          </div>
        </Section>
      </main>
      <Footer />
    </>
  );
}

const styles = stylex.create({
  main: { maxWidth: space.measure, paddingInline: space.gutter, marginInline: "auto" },
  ride: {
    display: "grid",
    gridTemplateColumns: "repeat(auto-fit, minmax(200px, 1fr))",
    gap: 20,
    listStyle: "none",
  },
  rideStop: { display: "grid", gap: 6, alignContent: "start" },
  rideNumber: {
    display: "grid",
    placeItems: "center",
    width: 34,
    height: 34,
    marginBottom: 4,
    fontWeight: 700,
    color: ink.onAccent,
    backgroundColor: ink.fill,
    borderRadius: "50%",
  },
  rideTitle: { fontSize: 17, color: color.textHi },
  rideBody: { fontSize: 14.5, lineHeight: 1.55, color: color.subtext0, textWrap: "pretty" },
  later: { display: "grid", gridTemplateColumns: "minmax(0, 1fr)", gap: 14, maxWidth: 860 },
  laterCard: {
    display: "grid",
    gridTemplateColumns: "minmax(0, 1fr)",
    gap: 12,
    minWidth: 0,
    padding: 20,
    backgroundColor: color.base,
    borderColor: color.surface0,
    borderStyle: "solid",
    borderWidth: 1,
    borderRadius: 16,
  },
  laterTitle: {
    fontFamily: font.display,
    fontSize: 24,
    fontVariationSettings: '"SOFT" 100, "WONK" 1',
    fontWeight: 700,
    color: color.textHi,
  },
  laterBody: { fontSize: 14.5, color: color.subtext0, textWrap: "pretty" },
});
