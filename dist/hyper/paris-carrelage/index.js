// Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
// Paris Carrelage. Enable with localPlugins: ["paris-carrelage"] in ~/.hyper.js.
// selectionColor is a translucent wash of the text color, not the solid selection color the other
// terminals use: Hyper's xterm.js draws the selection over the glyphs, so an opaque color would hide them.
"use strict";

const theme = {
  "backgroundColor": "#EEF2F1",
  "foregroundColor": "#27342F",
  "cursorColor": "#764C00",
  "cursorAccentColor": "#EEF2F1",
  "selectionColor": "#27342F33",
  "borderColor": "#D5DBDA",
  "colors": {
    "black": "#3B4742",
    "red": "#88251E",
    "green": "#218366",
    "yellow": "#916D07",
    "blue": "#25629B",
    "magenta": "#764C00",
    "cyan": "#006267",
    "white": "#99ABA6",
    "lightBlack": "#6C7C76",
    "lightRed": "#AC3B32",
    "lightGreen": "#278D6E",
    "lightYellow": "#A07A12",
    "lightBlue": "#3D75AD",
    "lightMagenta": "#885A00",
    "lightCyan": "#027479",
    "lightWhite": "#B0BFBB"
  }
};

const css = `
  .tabs_nav, .tabs_list { background-color: #D5DBDA; }
  .tabs_title { color: #4A5752; }
  .tab_tab { color: #6C7C76; background-color: #D5DBDA; }
  .tab_tab.tab_active { color: #19221E; background-color: #EEF2F1; box-shadow: inset 0 -2px 0 #764C00; }
`;

exports.decorateConfig = (config) =>
  Object.assign({}, config, theme, { css: `${css}${config.css || ""}` });
