// Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
// Paris Catacombes. Enable with localPlugins: ["paris-catacombes"] in ~/.hyper.js.
// selectionColor is a translucent wash of the text color, not the solid selection color the other
// terminals use: Hyper's xterm.js draws the selection over the glyphs, so an opaque color would hide them.
"use strict";

const theme = {
  "backgroundColor": "#121E19",
  "foregroundColor": "#D4DDD7",
  "cursorColor": "#F1BF4B",
  "cursorAccentColor": "#121E19",
  "selectionColor": "#D4DDD733",
  "borderColor": "#1A2921",
  "colors": {
    "black": "#24342C",
    "red": "#C7665B",
    "green": "#70CAA9",
    "yellow": "#F1BF4B",
    "blue": "#709BC8",
    "magenta": "#CA9245",
    "cyan": "#549B9F",
    "white": "#BFC8C2",
    "lightBlack": "#708178",
    "lightRed": "#E7877B",
    "lightGreen": "#89DEBE",
    "lightYellow": "#FFD57A",
    "lightBlue": "#8DB6E2",
    "lightMagenta": "#DFAA61",
    "lightCyan": "#70B5B9",
    "lightWhite": "#E7ECEA"
  }
};

const css = `
  .tabs_nav, .tabs_list { background-color: #0A100D; }
  .tabs_title { color: #A5B1AA; }
  .tab_tab { color: #708178; background-color: #0A100D; }
  .tab_tab.tab_active { color: #E7ECEA; background-color: #121E19; box-shadow: inset 0 -2px 0 #F1BF4B; }
`;

exports.decorateConfig = (config) =>
  Object.assign({}, config, theme, { css: `${css}${config.css || ""}` });
