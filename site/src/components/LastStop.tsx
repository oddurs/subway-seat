import * as stylex from "@stylexjs/stylex";
import Link from "next/link";
import { installCommand } from "@/lib/install";
import { flavors } from "@/lib/palette";
import { ink } from "@/theme/ink.stylex";
import { color } from "@/theme/tokens.stylex";
import { font } from "@/theme/type.stylex";
import { Command } from "./Command";

/**
 * The closing band: the whole of /install, boiled down to the one line most
 * people want. It carries the flavor you're actually riding, so the command is
 * the one that installs what's on your screen.
 *
 * Both cities get the same three facts and a different way of saying them —
 * the sign over a New York exit, and the one on a London platform.
 */
const FACTS = [
  ["117", "apps covered"],
  ["1", "question, once"],
  ["0", "left behind on uninstall"],
];

export function LastStop() {
  return (
    <section id="get-on-board" {...stylex.props(styles.band)}>
      <span aria-hidden {...stylex.props(styles.rule)} />
      <div {...stylex.props(styles.inner)}>
        <div {...stylex.props(styles.copy)}>
          <p data-only="new-york" {...stylex.props(styles.eyebrow)}>
            Last stop
          </p>
          <p data-only="london" {...stylex.props(styles.eyebrow)}>
            Alight here
          </p>
          <h2 data-only="new-york" {...stylex.props(styles.title)}>
            Take a seat.
          </h2>
          <h2 data-only="london" {...stylex.props(styles.title)}>
            Mind the gap.
          </h2>
          <p {...stylex.props(styles.lede)}>
            One line finds the apps you have, shows you the plan, and asks once before it touches
            anything. Everything it does comes back out again.
          </p>
        </div>

        <div {...stylex.props(styles.ticket)}>
          {flavors.map((f) => (
            <div key={f.id} data-only={f.id}>
              <Command text={installCommand({ flavor: f.id })} />
            </div>
          ))}
          <dl {...stylex.props(styles.facts)}>
            {FACTS.map(([n, label]) => (
              <div key={label} {...stylex.props(styles.fact)}>
                <dt {...stylex.props(styles.factNum)}>{n}</dt>
                <dd {...stylex.props(styles.factLabel)}>{label}</dd>
              </div>
            ))}
          </dl>
          <Link href="/install" {...stylex.props(styles.more)}>
            Pick your apps, follow light and dark, or clone the repo →
          </Link>
        </div>
      </div>
    </section>
  );
}

const WIDE = "@media (min-width: 960px)";

const styles = stylex.create({
  band: {
    position: "relative",
    marginTop: 40,
    paddingBlock: 0,
    backgroundColor: color.mantle,
  },
  // The platform edge: the city's own lead colour, full width.
  rule: { display: "block", height: 4, backgroundColor: ink.fill },
  inner: {
    display: "grid",
    gridTemplateColumns: { default: "minmax(0, 1fr)", [WIDE]: "minmax(0, 0.9fr) minmax(0, 1.1fr)" },
    gap: { default: 28, [WIDE]: 56 },
    alignItems: "center",
    maxWidth: 1200,
    paddingInline: 24,
    paddingBlock: { default: 48, [WIDE]: 72 },
    marginInline: "auto",
  },
  copy: { display: "grid", gap: 14 },
  eyebrow: {
    fontFamily: font.sans,
    fontSize: font.sizeLabel,
    fontWeight: 700,
    lineHeight: font.leadFlat,
    color: ink.accent,
    textTransform: "uppercase",
    letterSpacing: font.trackLabel,
  },
  title: {
    fontFamily: font.display,
    fontSize: font.sizeTitle,
    fontVariationSettings: font.axesTitle,
    fontWeight: font.weightTitle,
    lineHeight: font.leadTitle,
    letterSpacing: font.trackTitle,
    color: color.textHi,
    textWrap: "balance",
  },
  lede: {
    maxWidth: "46ch",
    fontSize: font.sizeSmall,
    lineHeight: font.leadLede,
    color: color.subtext0,
    textWrap: "pretty",
  },
  ticket: { display: "grid", gap: 20 },
  facts: { display: "flex", flexWrap: "wrap", gap: "18px 36px", margin: 0 },
  fact: { display: "flex", gap: 9, alignItems: "baseline" },
  factNum: {
    fontFamily: font.display,
    fontSize: 26,
    fontVariationSettings: font.axesTitle,
    fontWeight: font.weightTitle,
    lineHeight: font.leadFlat,
    letterSpacing: font.trackTitle,
    fontVariantNumeric: "tabular-nums",
    color: color.textHi,
  },
  factLabel: {
    margin: 0,
    fontSize: font.sizeMicro,
    lineHeight: font.leadFlat,
    color: color.subtext0,
  },
  more: {
    justifySelf: "start",
    fontSize: font.sizeSmall,
    fontWeight: 600,
    color: { default: ink.accent, ":hover": ink.accentHover },
    textDecoration: "none",
    outlineWidth: 2,
    outlineStyle: { default: "none", ":focus-visible": "solid" },
    outlineColor: ink.accent,
    outlineOffset: 3,
    borderRadius: "var(--radius-pill)",
  },
});
