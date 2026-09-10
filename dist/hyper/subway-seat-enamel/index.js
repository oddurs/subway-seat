// Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
// Subway Seat Enamel. Enable with localPlugins: ["subway-seat-enamel"] in ~/.hyper.js.
// selectionColor is a translucent wash of the text color, not the solid selection color the other
// terminals use: Hyper's xterm.js draws the selection over the glyphs, so an opaque color would hide them.
"use strict";

const theme = {
  "backgroundColor": "#F4E9D4",
  "foregroundColor": "#3E2C1E",
  "cursorColor": "#AD4E00",
  "cursorAccentColor": "#F4E9D4",
  "selectionColor": "#3E2C1E33",
  "borderColor": "#E2D3B6",
  "colors": {
    "black": "#54402F",
    "red": "#992418",
    "green": "#66740F",
    "yellow": "#936200",
    "blue": "#3F6480",
    "magenta": "#AD4E00",
    "cyan": "#3E7157",
    "white": "#BAA07A",
    "lightBlack": "#8C7254",
    "lightRed": "#BC4031",
    "lightGreen": "#697813",
    "lightYellow": "#A56E00",
    "lightBlue": "#517791",
    "lightMagenta": "#C4561A",
    "lightCyan": "#4C8367",
    "lightWhite": "#CAB48E"
  }
};

const css = `
  .tabs_nav, .tabs_list { background-color: #E2D3B6; }
  .tabs_title { color: #654F3B; }
  .tab_tab { color: #8C7254; background-color: #E2D3B6; }
  .tab_tab.tab_active { color: #2A1D13; background-color: #F4E9D4; box-shadow: inset 0 -2px 0 #AD4E00; }
`;

exports.decorateConfig = (config) =>
  Object.assign({}, config, theme, { css: `${css}${config.css || ""}` });
