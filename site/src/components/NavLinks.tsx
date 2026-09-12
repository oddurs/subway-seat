"use client";

import * as stylex from "@stylexjs/stylex";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { font } from "@/theme/type.stylex";

const LINKS = [
  { href: "/install", label: "Install" },
  { href: "/#ports", label: "Ports" },
  { href: "/palette", label: "Palette" },
  { href: "/ports/claude-code", label: "Claude Code" },
  { href: "https://github.com/oddurs/subway-seat", label: "GitHub" },
];

/** Which link is "you are here": the page itself, or Ports for any other port page. */
function current(path: string, href: string): "page" | "true" | undefined {
  if (href === path) return "page";
  if (href === "/#ports" && path.startsWith("/ports/") && path !== "/ports/claude-code") {
    return "true";
  }
  return undefined;
}

export function NavLinks() {
  const path = (usePathname() ?? "/").replace(/(.)\/$/, "$1");
  return (
    <nav aria-label="Main" {...stylex.props(styles.links)}>
      {LINKS.map((l) => {
        const here = current(path, l.href);
        return (
          <Link
            key={l.href}
            href={l.href}
            prefetch={false}
            aria-current={here}
            {...stylex.props(styles.link, here && styles.here)}
          >
            {l.label}
          </Link>
        );
      })}
    </nav>
  );
}

const NARROW = "@media (max-width: 640px)";

const styles = stylex.create({
  links: {
    display: "flex",
    flexBasis: {
      [NARROW]: "100%",
      default: "auto",
    },
    flexWrap: "wrap",
    rowGap: 2,
    columnGap: 18,
    order: {
      [NARROW]: 3,
      default: 0,
    },
    marginRight: "auto",
  },
  link: {
    paddingBlock: 6,
    fontFamily: font.sans,
    fontSize: 14,
    // A fixed line box, so the links centre against the wordmark and the city
    // switch whichever face the family sets them in.
    lineHeight: 1,
    color: {
      default: "color-mix(in srgb, var(--sign-text) 72%, transparent)",
      ":hover": "var(--sign-text)",
    },
    textDecorationLine: "none",
    textDecorationThickness: 2,
    textUnderlineOffset: 6,
    outlineWidth: 2,
    outlineStyle: {
      default: "none",
      ":focus-visible": "solid",
    },
    outlineColor: "var(--sign-ring)",
    outlineOffset: 2,
    borderRadius: 2,
  },
  here: {
    color: "var(--sign-text)",
    textDecorationLine: "underline",
    textDecorationColor: "var(--sign-ring)",
  },
});
