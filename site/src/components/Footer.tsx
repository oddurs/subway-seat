import * as stylex from "@stylexjs/stylex";
import Link from "next/link";
import { color } from "@/theme/tokens.stylex";
import { font } from "@/theme/type.stylex";

export function Footer() {
  return (
    <footer {...stylex.props(styles.footer)}>
      <div {...stylex.props(styles.inner)}>
        <p {...stylex.props(styles.signoff)}>Stand clear of the closing doors.</p>
        <p {...stylex.props(styles.fine)}>
          Every file on this site comes out of one{" "}
          <code {...stylex.props(styles.code)}>palette.py</code>. Change a colour, run{" "}
          <code {...stylex.props(styles.code)}>./build.py</code>, and ~90 apps follow. MIT licensed.
        </p>
        <nav aria-label="Footer" {...stylex.props(styles.links)}>
          <Link href="https://github.com/oddurs/subway-seat" {...stylex.props(styles.link)}>
            GitHub
          </Link>
          <Link href="/palette" {...stylex.props(styles.link)}>
            Palette
          </Link>
          <Link
            href="https://github.com/oddurs/subway-seat/blob/main/CONTRIBUTING.md"
            {...stylex.props(styles.link)}
          >
            Add a port
          </Link>
          <Link
            href="https://github.com/oddurs/subway-seat/issues/new/choose"
            {...stylex.props(styles.link)}
          >
            Request an app
          </Link>
        </nav>
      </div>
    </footer>
  );
}

const styles = stylex.create({
  footer: {
    marginTop: 80,
    backgroundColor: color.crust,
    borderTopColor: color.surface0,
    borderTopStyle: "solid",
    borderTopWidth: 1,
  },
  inner: {
    display: "grid",
    gap: 14,
    maxWidth: 1200,
    paddingInline: 24,
    paddingTop: 48,
    paddingBottom: 56,
    marginInline: "auto",
  },
  signoff: {
    fontFamily: font.display,
    fontSize: "clamp(28px, 4vw, 42px)",
    fontVariationSettings: '"SOFT" 100, "WONK" 1',
    fontWeight: 700,
    color: color.textHi,
  },
  fine: { maxWidth: "62ch", fontSize: 15, color: color.subtext0 },
  code: { fontFamily: font.mono, fontSize: "0.9em", color: color.yellow },
  links: { display: "flex", flexWrap: "wrap", gap: 20 },
  link: {
    fontSize: 14,
    color: {
      default: color.subtext1,
      ":hover": color.orange,
    },
    textDecoration: "none",
  },
});
