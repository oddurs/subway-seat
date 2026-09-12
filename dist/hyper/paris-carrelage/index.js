// Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
// Paris Carrelage. Enable with localPlugins: ["paris-carrelage"] in ~/.hyper.js.
// selectionColor is a translucent wash of the text color, not the solid selection color the other
// terminals use: Hyper's xterm.js draws the selection over the glyphs, so an opaque color would hide them.
"use strict";

const theme = {
  "backgroundColor": "#EEF3ED",
  "foregroundColor": "#2A342B",
  "cursorColor": "#8A5308",
  "cursorAccentColor": "#EEF3ED",
  "selectionColor": "#2A342B33",
  "borderColor": "#D4DCD3",
  "colors": {
    "black": "#3D473E",
    "red": "#932D29",
    "green": "#207F41",
    "yellow": "#8A6700",
    "blue": "#27629C",
    "magenta": "#8A5308",
    "cyan": "#0B714D",
    "white": "#9BAC9A",
    "lightBlack": "#6E7C6E",
    "lightRed": "#BB403B",
    "lightGreen": "#168540",
    "lightYellow": "#997300",
    "lightBlue": "#3E75AD",
    "lightMagenta": "#AE6800",
    "lightCyan": "#3D8666",
    "lightWhite": "#B1C0B0"
  }
};

const css = `
  .tabs_nav, .tabs_list { background-color: #D4DCD3; }
  .tabs_title { color: #4C574D; }
  .tab_tab { color: #6E7C6E; background-color: #D4DCD3; }
  .tab_tab.tab_active { color: #1B221C; background-color: #EEF3ED; box-shadow: inset 0 -2px 0 #8A5308; }
`;

exports.decorateConfig = (config) =>
  Object.assign({}, config, theme, { css: `${css}${config.css || ""}` });
