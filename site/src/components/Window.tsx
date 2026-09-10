import * as stylex from "@stylexjs/stylex";
import type { ReactNode } from "react";
import { color } from "@/theme/tokens.stylex";
import { font } from "@/theme/type.stylex";

/** App-window chrome: traffic-light dots, then tabs or a title. */
export function Window({
  tabs,
  title,
  children,
}: {
  tabs?: string[];
  title?: string;
  children: ReactNode;
}) {
  return (
    <figure {...stylex.props(styles.win)}>
      <div {...stylex.props(styles.bar)}>
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
    margin: 0,
    overflow: "hidden",
    backgroundColor: color.base,
    borderRadius: 10,
    boxShadow: "0 24px 60px var(--ss-shadow), 0 0 0 1px var(--ss-shadow-soft)",
  },
  bar: {
    display: "flex",
    gap: 14,
    alignItems: "center",
    minHeight: 36,
    paddingInline: 14,
    fontFamily: font.mono,
    fontSize: 12,
    color: color.overlay1,
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
    borderTopColor: color.orange,
    borderTopStyle: "solid",
    borderTopWidth: 2,
  },
});
