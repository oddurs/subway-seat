// Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
// London Portland. Enable with localPlugins: ["london-portland"] in ~/.hyper.js.
// selectionColor is a translucent wash of the text color, not the solid selection color the other
// terminals use: Hyper's xterm.js draws the selection over the glyphs, so an opaque color would hide them.
"use strict";

const theme = {
  "backgroundColor": "#E5EAF6",
  "foregroundColor": "#2F3033",
  "cursorColor": "#9F591B",
  "cursorAccentColor": "#E5EAF6",
  "selectionColor": "#2F303333",
  "borderColor": "#CED5E3",
  "colors": {
    "black": "#434548",
    "red": "#A40005",
    "green": "#357D41",
    "yellow": "#896800",
    "blue": "#0019A8",
    "magenta": "#9F591B",
    "cyan": "#007376",
    "white": "#9BA5B8",
    "lightBlack": "#727781",
    "lightRed": "#CA2822",
    "lightGreen": "#398145",
    "lightYellow": "#977300",
    "lightBlue": "#406BD0",
    "lightMagenta": "#AE672B",
    "lightCyan": "#008689",
    "lightWhite": "#ADB7CB"
  }
};

const css = `
  .tabs_nav, .tabs_list { background-color: #CED5E3; }
  .tabs_title { color: #515459; }
  .tab_tab { color: #727781; background-color: #CED5E3; }
  .tab_tab.tab_active { color: #1F2022; background-color: #E5EAF6; box-shadow: inset 0 -2px 0 #9F591B; }
`;

exports.decorateConfig = (config) =>
  Object.assign({}, config, theme, { css: `${css}${config.css || ""}` });
