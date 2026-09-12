import * as stylex from "@stylexjs/stylex";
import Link from "next/link";
import { font } from "@/theme/type.stylex";
import { CityMark } from "./CityMark";
import { CitySwitch } from "./CitySwitch";
import { NavLinks } from "./NavLinks";

export function Nav() {
  return (
    <header {...stylex.props(styles.band)}>
      <a href="#main" {...stylex.props(styles.skip)}>
        Skip to content
      </a>
      <div {...stylex.props(styles.inner)}>
        <span aria-hidden {...stylex.props(styles.rule)} />
        <Link href="/" {...stylex.props(styles.mark)}>
          <CityMark />
          <span>Subway Seat</span>
        </Link>
        <NavLinks />
        <CitySwitch />
      </div>
    </header>
  );
}

const styles = stylex.create({
  band: { position: "relative", zIndex: 2, backgroundColor: "var(--sign-bg)" },
  skip: {
    position: "absolute",
    top: 10,
    left: 10,
    zIndex: 3,
    paddingBlock: 8,
    paddingInline: 14,
    fontFamily: font.sans,
    fontSize: 14,
    fontWeight: 700,
    color: "var(--sign-bg)",
    textDecoration: "none",
    outlineWidth: 2,
    outlineStyle: "solid",
    outlineColor: "var(--sign-ring)",
    outlineOffset: 2,
    backgroundColor: "var(--sign-text)",
    borderRadius: 999,
    transform: {
      default: "translateY(-200%)",
      ":focus": "none",
    },
  },
  inner: {
    display: "flex",
    flexWrap: "wrap",
    rowGap: 10,
    columnGap: 24,
    alignItems: "center",
    maxWidth: 1200,
    paddingInline: 24,
    paddingTop: 17,
    paddingBottom: 14,
    marginInline: "auto",
  },
  // The sign's top edge, flush and full width, in the city's lead colour.
  rule: {
    position: "absolute",
    top: 0,
    right: 0,
    left: 0,
    height: 3,
    backgroundColor: "var(--sign-mark)",
  },
  mark: {
    display: "flex",
    gap: 10,
    alignItems: "center",
    fontFamily: font.sans,
    fontSize: 20,
    fontWeight: 700,
    lineHeight: 1,
    color: "var(--sign-text)",
    letterSpacing: font.markTracking,
    textDecoration: "none",
    outlineWidth: 2,
    outlineStyle: {
      default: "none",
      ":focus-visible": "solid",
    },
    outlineColor: "var(--sign-ring)",
    outlineOffset: 3,
    borderRadius: 2,
  },
});
