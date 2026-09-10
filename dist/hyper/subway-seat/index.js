// Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
// Subway Seat. Enable with localPlugins: ["subway-seat"] in ~/.hyper.js.
// selectionColor is a translucent wash of the text color, not the solid selection color the other
// terminals use: Hyper's xterm.js draws the selection over the glyphs, so an opaque color would hide them.
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
    "red": "#E05C45",
    "green": "#ADB956",
    "yellow": "#F3BF45",
    "blue": "#7F9BAE",
    "magenta": "#EC7F31",
    "cyan": "#86AD95",
    "white": "#D9C6A3",
    "lightBlack": "#967B5C",
    "lightRed": "#F97160",
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
