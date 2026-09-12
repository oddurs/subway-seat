import * as stylex from "@stylexjs/stylex";
import type { ReactNode } from "react";
import { ink } from "@/theme/ink.stylex";
import { color } from "@/theme/tokens.stylex";
import { space } from "@/theme/space.stylex";
import { font } from "@/theme/type.stylex";

const slug = (s: string) =>
  s
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-|-$/g, "");

export function Section({
  id,
  label,
  title,
  intro,
  level = 2,
  children,
}: {
  id?: string;
  label: string;
  title?: string;
  intro?: ReactNode;
  /** 1 for a page's own heading (the palette and install pages). */
  level?: 1 | 2;
  children: ReactNode;
}) {
  const heading = `${id ?? slug(label)}-title`;
  const Title = level === 1 ? "h1" : "h2";
  return (
    <section
      id={id}
      aria-labelledby={title ? heading : undefined}
      aria-label={title ? undefined : label}
      {...stylex.props(styles.section)}
    >
      <header {...stylex.props(styles.head)}>
        <p {...stylex.props(styles.label)}>{label}</p>
        {title && (
          <Title id={heading} {...stylex.props(styles.title)}>
            {title}
          </Title>
        )}
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
    gap: space.heading,
    paddingTop: space.section,
    scrollMarginTop: 24,
  },
  head: { display: "grid", gap: 10 },
  label: {
    fontSize: font.sizeLabel,
    fontWeight: 700,
    color: ink.accent,
    textTransform: "uppercase",
    letterSpacing: font.trackLabel,
  },
  title: {
    maxWidth: "20ch",
    fontFamily: font.display,
    fontSize: font.sizeTitle,
    fontVariationSettings: font.axesTitle,
    fontWeight: font.weightTitle,
    lineHeight: font.leadTitle,
    color: color.textHi,
    letterSpacing: font.trackTitle,
    textWrap: "balance",
  },
  intro: {
    maxWidth: "62ch",
    fontSize: font.sizeLede,
    lineHeight: font.leadLede,
    color: color.subtext0,
    textWrap: "pretty",
  },
});
