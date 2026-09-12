// Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
// Paris Carrelage. Enable with localPlugins: ["paris-carrelage"] in ~/.hyper.js.
// selectionColor is a translucent wash of the text color, not the solid selection color the other
// terminals use: Hyper's xterm.js draws the selection over the glyphs, so an opaque color would hide them.
"use strict";

const theme = {
  "backgroundColor": "#E2EDE8",
  "foregroundColor": "#21352D",
  "cursorColor": "#9B5D00",
  "cursorAccentColor": "#E2EDE8",
  "selectionColor": "#21352D33",
  "borderColor": "#C8DAD1",
  "colors": {
    "black": "#334A41",
    "red": "#A30013",
    "green": "#00823B",
    "yellow": "#856A00",
    "blue": "#0961A9",
    "magenta": "#9B5D00",
    "cyan": "#007752",
    "white": "#88AF9E",
    "lightBlack": "#5C8171",
    "lightRed": "#C82C2C",
    "lightGreen": "#00863D",
    "lightYellow": "#937500",
    "lightBlue": "#2E75B9",
    "lightMagenta": "#AE6800",
    "lightCyan": "#2A8862",
    "lightWhite": "#9DC1B1"
  }
};

const css = `
  .tabs_nav, .tabs_list { background-color: #C8DAD1; }
  .tabs_title { color: #405B4F; }
  .tab_tab { color: #5C8171; background-color: #C8DAD1; }
  .tab_tab.tab_active { color: #16241E; background-color: #E2EDE8; box-shadow: inset 0 -2px 0 #9B5D00; }
`;

exports.decorateConfig = (config) =>
  Object.assign({}, config, theme, { css: `${css}${config.css || ""}` });
