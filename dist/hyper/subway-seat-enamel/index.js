// Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
// Subway Seat Enamel. Enable with localPlugins: ["subway-seat-enamel"] in ~/.hyper.js.
// selectionColor is a translucent wash of the text color, not the solid selection color the other
// terminals use: Hyper's xterm.js draws the selection over the glyphs, so an opaque color would hide them.
"use strict";

const theme = {
  "backgroundColor": "#F8EFDF",
  "foregroundColor": "#3E2C1E",
  "cursorColor": "#A04800",
  "cursorAccentColor": "#F8EFDF",
  "selectionColor": "#3E2C1E33",
  "borderColor": "#E4D8C0",
  "colors": {
    "black": "#54402F",
    "red": "#992418",
    "green": "#66740F",
    "yellow": "#976608",
    "blue": "#3F6480",
    "magenta": "#A04800",
    "cyan": "#3E7157",
    "white": "#BAA380",
    "lightBlack": "#8C7254",
    "lightRed": "#BF4233",
    "lightGreen": "#697813",
    "lightYellow": "#A9720A",
    "lightBlue": "#517791",
    "lightMagenta": "#BA4D0A",
    "lightCyan": "#4C8367",
    "lightWhite": "#CBB898"
  }
};

const css = `
  .tabs_nav, .tabs_list { background-color: #E4D8C0; }
  .tabs_title { color: #654F3B; }
  .tab_tab { color: #8C7254; background-color: #E4D8C0; }
  .tab_tab.tab_active { color: #2A1D13; background-color: #F8EFDF; box-shadow: inset 0 -2px 0 #A04800; }
`;

exports.decorateConfig = (config) =>
  Object.assign({}, config, theme, { css: `${css}${config.css || ""}` });
