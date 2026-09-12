// Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
// Paris Carrelage. Enable with localPlugins: ["paris-carrelage"] in ~/.hyper.js.
// selectionColor is a translucent wash of the text color, not the solid selection color the other
// terminals use: Hyper's xterm.js draws the selection over the glyphs, so an opaque color would hide them.
"use strict";

const theme = {
  "backgroundColor": "#E4EDE8",
  "foregroundColor": "#25352C",
  "cursorColor": "#9B5D00",
  "cursorAccentColor": "#E4EDE8",
  "selectionColor": "#25352C33",
  "borderColor": "#CAD9D1",
  "colors": {
    "black": "#374940",
    "red": "#9E171B",
    "green": "#18803F",
    "yellow": "#8A6700",
    "blue": "#27629C",
    "magenta": "#9B5D00",
    "cyan": "#277555",
    "white": "#8EAD9D",
    "lightBlack": "#627F70",
    "lightRed": "#BB403B",
    "lightGreen": "#168540",
    "lightYellow": "#997300",
    "lightBlue": "#3E75AD",
    "lightMagenta": "#AE6800",
    "lightCyan": "#3D8666",
    "lightWhite": "#A3BFB0"
  }
};

const css = `
  .tabs_nav, .tabs_list { background-color: #CAD9D1; }
  .tabs_title { color: #45594F; }
  .tab_tab { color: #627F70; background-color: #CAD9D1; }
  .tab_tab.tab_active { color: #18231D; background-color: #E4EDE8; box-shadow: inset 0 -2px 0 #9B5D00; }
`;

exports.decorateConfig = (config) =>
  Object.assign({}, config, theme, { css: `${css}${config.css || ""}` });
