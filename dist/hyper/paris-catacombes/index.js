// Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
// Paris Catacombes. Enable with localPlugins: ["paris-catacombes"] in ~/.hyper.js.
// selectionColor is a translucent wash of the text color, not the solid selection color the other
// terminals use: Hyper's xterm.js draws the selection over the glyphs, so an opaque color would hide them.
"use strict";

const theme = {
  "backgroundColor": "#141D19",
  "foregroundColor": "#D5DCD8",
  "cursorColor": "#EBC168",
  "cursorAccentColor": "#141D19",
  "selectionColor": "#D5DCD833",
  "borderColor": "#1D2822",
  "colors": {
    "black": "#27332D",
    "red": "#CD6B63",
    "green": "#80C28E",
    "yellow": "#EBC168",
    "blue": "#709BC8",
    "magenta": "#D0914F",
    "cyan": "#7BB096",
    "white": "#C0C7C3",
    "lightBlack": "#738079",
    "lightRed": "#E1837A",
    "lightGreen": "#8FD59E",
    "lightYellow": "#FBD380",
    "lightBlue": "#8DB6E2",
    "lightMagenta": "#E7AB6D",
    "lightCyan": "#98CCB2",
    "lightWhite": "#E8ECEA"
  }
};

const css = `
  .tabs_nav, .tabs_list { background-color: #0B100D; }
  .tabs_title { color: #A7B0AB; }
  .tab_tab { color: #738079; background-color: #0B100D; }
  .tab_tab.tab_active { color: #E8ECEA; background-color: #141D19; box-shadow: inset 0 -2px 0 #EBC168; }
`;

exports.decorateConfig = (config) =>
  Object.assign({}, config, theme, { css: `${css}${config.css || ""}` });
