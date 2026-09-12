// Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
// Paris Catacombes. Enable with localPlugins: ["paris-catacombes"] in ~/.hyper.js.
// selectionColor is a translucent wash of the text color, not the solid selection color the other
// terminals use: Hyper's xterm.js draws the selection over the glyphs, so an opaque color would hide them.
"use strict";

const theme = {
  "backgroundColor": "#121E19",
  "foregroundColor": "#D4DDD7",
  "cursorColor": "#F2BF4B",
  "cursorAccentColor": "#121E19",
  "selectionColor": "#D4DDD733",
  "borderColor": "#1A2921",
  "colors": {
    "black": "#24342C",
    "red": "#CD6B63",
    "green": "#80C28E",
    "yellow": "#F2BF4B",
    "blue": "#709BC8",
    "magenta": "#D0914F",
    "cyan": "#6CA087",
    "white": "#BFC8C2",
    "lightBlack": "#708178",
    "lightRed": "#E1837A",
    "lightGreen": "#8FD59E",
    "lightYellow": "#FFD273",
    "lightBlue": "#8DB6E2",
    "lightMagenta": "#E7AB6D",
    "lightCyan": "#98CCB2",
    "lightWhite": "#E7ECEA"
  }
};

const css = `
  .tabs_nav, .tabs_list { background-color: #0A100D; }
  .tabs_title { color: #A5B1AA; }
  .tab_tab { color: #708178; background-color: #0A100D; }
  .tab_tab.tab_active { color: #E7ECEA; background-color: #121E19; box-shadow: inset 0 -2px 0 #F2BF4B; }
`;

exports.decorateConfig = (config) =>
  Object.assign({}, config, theme, { css: `${css}${config.css || ""}` });
