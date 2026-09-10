// Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
// Subway Seat Enamel. Enable with localPlugins: ["subway-seat-enamel"] in ~/.hyper.js.
"use strict";

const theme = {
  "backgroundColor": "#F4E9D4",
  "foregroundColor": "#3E2C1E",
  "cursorColor": "#C4561A",
  "cursorAccentColor": "#F4E9D4",
  "selectionColor": "#3E2C1E33",
  "borderColor": "#E2D3B6",
  "colors": {
    "black": "#54402F",
    "red": "#B43B27",
    "green": "#697813",
    "yellow": "#A56E00",
    "blue": "#3F6480",
    "magenta": "#C4561A",
    "cyan": "#3E7157",
    "white": "#BAA07A",
    "lightBlack": "#8C7254",
    "lightRed": "#C44A33",
    "lightGreen": "#7B8B22",
    "lightYellow": "#BA8210",
    "lightBlue": "#517791",
    "lightMagenta": "#D66A27",
    "lightCyan": "#4C8367",
    "lightWhite": "#CAB48E"
  }
};

const css = `
  .tabs_nav, .tabs_list { background-color: #E2D3B6; }
  .tabs_title { color: #654F3B; }
  .tab_tab { color: #8C7254; background-color: #E2D3B6; }
  .tab_tab.tab_active { color: #2A1D13; background-color: #F4E9D4; box-shadow: inset 0 -2px 0 #C4561A; }
`;

exports.decorateConfig = (config) =>
  Object.assign({}, config, theme, { css: `${css}${config.css || ""}` });
