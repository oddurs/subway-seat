import * as stylex from "@stylexjs/stylex";
import type { ReactNode } from "react";
import { ink } from "@/theme/ink.stylex";
import { color } from "@/theme/tokens.stylex";
import { font } from "@/theme/type.stylex";

/** App-window chrome: traffic-light dots, then tabs or a title. */
export function Window({
  tabs,
  title,
  label,
  children,
}: {
  tabs?: string[];
  title?: string;
  /** What the window shows, for screen readers, e.g. "Claude Code in Ghostty". */
  label?: string;
  children: ReactNode;
}) {
  return (
    <figure aria-label={label} {...stylex.props(styles.win)}>
      <div aria-hidden={label ? true : undefined} {...stylex.props(styles.bar)}>
        <span {...stylex.props(styles.dots)}>
          <i {...stylex.props(styles.dot)} />
          <i {...stylex.props(styles.dot)} />
          <i {...stylex.props(styles.dot)} />
        </span>
        {tabs?.map((tab, i) => (
          <span key={tab} {...stylex.props(styles.tab, i === 0 && styles.activeTab)}>
            {tab}
          </span>
        ))}
        {title && <span>{title}</span>}
      </div>
      {children}
    </figure>
  );
}

const styles = stylex.create({
  win: {
    display: "flex",
    flexDirection: "column",
    margin: 0,
    overflow: "hidden",
    backgroundColor: color.base,
    borderRadius: "var(--radius-card)",
    boxShadow: "0 24px 60px var(--ss-shadow), 0 0 0 1px var(--ss-shadow-soft)",
  },
  bar: {
    display: "flex",
    gap: 14,
    alignItems: "center",
    minHeight: 36,
    paddingInline: 14,
    // A window's title bar is the OS's chrome, not the terminal's.
    fontFamily: font.ui,
    fontSize: 12,
    color: color.overlay2,
    backgroundColor: color.mantle,
  },
  dots: { display: "flex", gap: 6 },
  dot: {
    width: 11,
    height: 11,
    backgroundColor: color.surface2,
    borderRadius: "50%",
  },
  tab: {
    display: "flex",
    alignItems: "center",
    alignSelf: "stretch",
    paddingInline: 12,
  },
  activeTab: {
    color: color.text,
    backgroundColor: color.base,
    borderTopColor: ink.fill,
    borderTopStyle: "solid",
    borderTopWidth: 2,
  },
});
