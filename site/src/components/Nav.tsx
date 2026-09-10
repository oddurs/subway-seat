import * as stylex from "@stylexjs/stylex";
import Link from "next/link";
import { sign } from "@/theme/sign.stylex";
import { font } from "@/theme/type.stylex";
import { FlavorSwitch } from "./FlavorSwitch";
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
          Subway Seat
        </Link>
        <NavLinks />
        <FlavorSwitch />
      </div>
    </header>
  );
}

const styles = stylex.create({
  band: { position: "relative", zIndex: 2, backgroundColor: sign.bg },
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
    color: sign.bg,
    textDecoration: "none",
    outlineWidth: 2,
    outlineStyle: "solid",
    outlineColor: sign.ring,
    outlineOffset: 2,
    backgroundColor: sign.text,
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
    paddingTop: 12,
    paddingBottom: 12,
    marginInline: "auto",
  },
  rule: {
    position: "absolute",
    top: 6,
    right: 0,
    left: 0,
    height: 2,
    backgroundColor: sign.text,
    opacity: 0.8,
  },
  mark: {
    fontFamily: font.sans,
    fontSize: 21,
    fontWeight: 700,
    color: sign.text,
    letterSpacing: "-0.01em",
    textDecoration: "none",
    outlineWidth: 2,
    outlineStyle: {
      default: "none",
      ":focus-visible": "solid",
    },
    outlineColor: sign.ring,
    outlineOffset: 3,
    borderRadius: 2,
  },
});
