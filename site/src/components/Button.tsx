import * as stylex from "@stylexjs/stylex";
import Link from "next/link";
import type { ReactNode } from "react";
import { ink } from "@/theme/ink.stylex";
import { space } from "@/theme/space.stylex";
import { color } from "@/theme/tokens.stylex";
import { font } from "@/theme/type.stylex";

type Variant = "primary" | "secondary" | "quiet";
type Size = "md" | "sm";

/**
 * One button, three jobs, two cities.
 *
 * The shape comes from the family — New York rounds everything the way 70s
 * signage did, London sets its signs in rectangles — so nothing here names a
 * radius; `--radius-pill` does. The fill is `ink.fill`, which is burnt orange
 * in New York and the red in London, so the primary action is always the one
 * colour that family spends on identity.
 *
 * Every variant shares the same box: the same padding step, the same flat line
 * height, the same focus ring. A secondary button next to a primary one should
 * differ in weight, not in size.
 */
export function Button({
  href,
  variant = "secondary",
  size = "md",
  children,
  ...rest
}: {
  href: string;
  variant?: Variant;
  size?: Size;
  children: ReactNode;
} & Omit<React.ComponentProps<typeof Link>, "href" | "children">) {
  return (
    <Link href={href} {...rest} {...stylex.props(styles.base, styles[size], styles[variant])}>
      {children}
    </Link>
  );
}

const styles = stylex.create({
  base: {
    display: "inline-flex",
    gap: space.s2,
    alignItems: "center",
    justifyContent: "center",
    fontFamily: font.sans,
    fontWeight: 700,
    lineHeight: font.leadFlat,
    textAlign: "center",
    textDecoration: "none",
    cursor: "pointer",
    outlineWidth: 2,
    outlineStyle: { default: "none", ":focus-visible": "solid" },
    outlineColor: ink.accent,
    outlineOffset: 3,
    borderStyle: "solid",
    borderWidth: 1,
    borderColor: "transparent",
    borderRadius: "var(--radius-pill)",
    transform: { default: null, ":hover": "translateY(-1px)" },
    transitionDuration: "160ms",
    transitionProperty: "transform, background-color, border-color, color",
  },
  md: { paddingBlock: 13, paddingInline: space.s5, fontSize: font.sizeBody },
  sm: { paddingBlock: 9, paddingInline: space.s4, fontSize: font.sizeSmall },
  primary: {
    color: ink.onAccent,
    backgroundColor: { default: ink.fill, ":hover": ink.fillHover },
  },
  secondary: {
    color: color.text,
    backgroundColor: { default: "transparent", ":hover": color.surface0 },
    borderColor: { default: color.surface2, ":hover": color.overlay0 },
  },
  quiet: {
    paddingInline: 0,
    color: { default: ink.accent, ":hover": ink.accentHover },
    backgroundColor: "transparent",
    transform: null,
  },
});
