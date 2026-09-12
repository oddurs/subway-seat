// Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
// London Portland. Enable with localPlugins: ["london-portland"] in ~/.hyper.js.
// selectionColor is a translucent wash of the text color, not the solid selection color the other
// terminals use: Hyper's xterm.js draws the selection over the glyphs, so an opaque color would hide them.
"use strict";

const theme = {
  "backgroundColor": "#E5EAF4",
  "foregroundColor": "#293040",
  "cursorColor": "#A45600",
  "cursorAccentColor": "#E5EAF4",
  "selectionColor": "#29304033",
  "borderColor": "#CDD5E4",
  "colors": {
    "black": "#3C4557",
    "red": "#A40005",
    "green": "#00822E",
    "yellow": "#896800",
    "blue": "#0019A8",
    "magenta": "#A45600",
    "cyan": "#007376",
    "white": "#95A5C4",
    "lightBlack": "#697794",
    "lightRed": "#C92B23",
    "lightGreen": "#008730",
    "lightYellow": "#977300",
    "lightBlue": "#4A6EBD",
    "lightMagenta": "#B86100",
    "lightCyan": "#008688",
    "lightWhite": "#A9B7D4"
  }
};

const css = `
  .tabs_nav, .tabs_list { background-color: #CDD5E4; }
  .tabs_title { color: #4A5469; }
  .tab_tab { color: #697794; background-color: #CDD5E4; }
  .tab_tab.tab_active { color: #1B202B; background-color: #E5EAF4; box-shadow: inset 0 -2px 0 #A45600; }
`;

exports.decorateConfig = (config) =>
  Object.assign({}, config, theme, { css: `${css}${config.css || ""}` });
