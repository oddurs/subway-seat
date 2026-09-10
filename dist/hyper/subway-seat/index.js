// Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
// Subway Seat. Enable with localPlugins: ["subway-seat"] in ~/.hyper.js.
"use strict";

const theme = {
  "backgroundColor": "#362619",
  "foregroundColor": "#EDDCBC",
  "cursorColor": "#F3BF45",
  "cursorAccentColor": "#362619",
  "selectionColor": "#EDDCBC33",
  "borderColor": "#43301F",
  "colors": {
    "black": "#513B27",
    "red": "#D2503A",
    "green": "#A3AE4B",
    "yellow": "#F3BF45",
    "blue": "#7F9BAE",
    "magenta": "#EC7F31",
    "cyan": "#86AD95",
    "white": "#D9C6A3",
    "lightBlack": "#7B6047",
    "lightRed": "#EC6A50",
    "lightGreen": "#BFCB63",
    "lightYellow": "#FFD36B",
    "lightBlue": "#9DB6C6",
    "lightMagenta": "#FF9D55",
    "lightCyan": "#A5C9B0",
    "lightWhite": "#F8ECD4"
  }
};

const css = `
  .tabs_nav, .tabs_list { background-color: #20160E; }
  .tabs_title { color: #C4AE8C; }
  .tab_tab { color: #967B5C; background-color: #20160E; }
  .tab_tab.tab_active { color: #F8ECD4; background-color: #362619; box-shadow: inset 0 -2px 0 #F3BF45; }
`;

exports.decorateConfig = (config) =>
  Object.assign({}, config, theme, { css: `${css}${config.css || ""}` });
