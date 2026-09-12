// Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
// Paris Carrelage. Enable with localPlugins: ["paris-carrelage"] in ~/.hyper.js.
// selectionColor is a translucent wash of the text color, not the solid selection color the other
// terminals use: Hyper's xterm.js draws the selection over the glyphs, so an opaque color would hide them.
"use strict";

const theme = {
  "backgroundColor": "#DEF0E6",
  "foregroundColor": "#25352C",
  "cursorColor": "#754500",
  "cursorAccentColor": "#DEF0E6",
  "selectionColor": "#25352C33",
  "borderColor": "#BFDDCD",
  "colors": {
    "black": "#374940",
    "red": "#932D29",
    "green": "#207F41",
    "yellow": "#8A6700",
    "blue": "#27629C",
    "magenta": "#754500",
    "cyan": "#086142",
    "white": "#84B09A",
    "lightBlack": "#627F70",
    "lightRed": "#BB403B",
    "lightGreen": "#168540",
    "lightYellow": "#997300",
    "lightBlue": "#3E75AD",
    "lightMagenta": "#AE6800",
    "lightCyan": "#3D8666",
    "lightWhite": "#96C4AC"
  }
};

const css = `
  .tabs_nav, .tabs_list { background-color: #BFDDCD; }
  .tabs_title { color: #45594F; }
  .tab_tab { color: #627F70; background-color: #BFDDCD; }
  .tab_tab.tab_active { color: #18231D; background-color: #DEF0E6; box-shadow: inset 0 -2px 0 #754500; }
`;

exports.decorateConfig = (config) =>
  Object.assign({}, config, theme, { css: `${css}${config.css || ""}` });
