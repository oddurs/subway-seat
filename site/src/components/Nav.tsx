import * as stylex from "@stylexjs/stylex";
import Link from "next/link";
import { font } from "@/theme/type.stylex";
import { FlavorSwitch } from "./FlavorSwitch";

// Station signs are black with white Helvetica, whatever the flavor.
const SIGN = "#0C0805";
const SIGN_TEXT = "#F8ECD4";

const LINKS = [
  { href: "/#ports", label: "Ports" },
  { href: "/palette", label: "Palette" },
  { href: "/ports/claude-code", label: "Claude Code" },
  { href: "https://github.com/oddurs/subway-seat", label: "GitHub" },
];

export function Nav() {
  return (
    <header {...stylex.props(styles.band)}>
      <div {...stylex.props(styles.inner)}>
        <span aria-hidden {...stylex.props(styles.rule)} />
        <Link href="/" {...stylex.props(styles.mark)}>
          Subway Seat
        </Link>
        <nav aria-label="Main" {...stylex.props(styles.links)}>
          {LINKS.map((l) => (
            <Link key={l.href} href={l.href} {...stylex.props(styles.link)}>
              {l.label}
            </Link>
          ))}
        </nav>
        <FlavorSwitch />
      </div>
    </header>
  );
}

const NARROW = "@media (max-width: 640px)";

const styles = stylex.create({
  band: { position: "relative", zIndex: 2, backgroundColor: SIGN },
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
    backgroundColor: SIGN_TEXT,
    opacity: 0.8,
  },
  mark: {
    fontFamily: font.sans,
    fontSize: 21,
    fontWeight: 700,
    color: SIGN_TEXT,
    letterSpacing: "-0.01em",
    textDecoration: "none",
  },
  links: {
    display: "flex",
    flexBasis: {
      [NARROW]: "100%",
      default: "auto",
    },
    flexWrap: "wrap",
    gap: 18,
    order: {
      [NARROW]: 3,
      default: 0,
    },
    marginRight: "auto",
  },
  link: {
    fontFamily: font.sans,
    fontSize: 14,
    color: {
      default: "rgba(248,236,212,0.72)",
      ":hover": SIGN_TEXT,
    },
    textDecoration: "none",
  },
});
