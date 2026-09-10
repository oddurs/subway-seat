import * as stylex from "@stylexjs/stylex";
import type { ReactNode } from "react";
import { color } from "@/theme/tokens.stylex";
import { font } from "@/theme/type.stylex";

export function Section({
  id,
  label,
  title,
  intro,
  children,
}: {
  id?: string;
  label: string;
  title?: string;
  intro?: ReactNode;
  children: ReactNode;
}) {
  return (
    <section id={id} aria-label={label} {...stylex.props(styles.section)}>
      <header {...stylex.props(styles.head)}>
        <p {...stylex.props(styles.label)}>{label}</p>
        {title && <h2 {...stylex.props(styles.title)}>{title}</h2>}
        {intro && <p {...stylex.props(styles.intro)}>{intro}</p>}
      </header>
      {children}
    </section>
  );
}

const styles = stylex.create({
  section: {
    display: "grid",
    gridTemplateColumns: "minmax(0, 1fr)",
    gap: 26,
    paddingTop: 88,
    scrollMarginTop: 24,
  },
  head: { display: "grid", gap: 10 },
  label: {
    fontSize: 13,
    fontWeight: 600,
    color: color.orange,
    textTransform: "uppercase",
    letterSpacing: "0.16em",
  },
  title: {
    maxWidth: "20ch",
    fontFamily: font.display,
    fontSize: "clamp(32px, 4.4vw, 52px)",
    fontVariationSettings: '"SOFT" 100, "WONK" 1',
    fontWeight: 750,
    lineHeight: 1.04,
    color: color.textHi,
    letterSpacing: "-0.015em",
    textWrap: "balance",
  },
  intro: {
    maxWidth: "62ch",
    fontSize: 17,
    lineHeight: 1.6,
    color: color.subtext0,
    textWrap: "pretty",
  },
});
