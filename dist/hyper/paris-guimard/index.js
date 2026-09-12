// Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
// Paris Guimard. Enable with localPlugins: ["paris-guimard"] in ~/.hyper.js.
// selectionColor is a translucent wash of the text color, not the solid selection color the other
// terminals use: Hyper's xterm.js draws the selection over the glyphs, so an opaque color would hide them.
"use strict";

const theme = {
  "backgroundColor": "#0E3125",
  "foregroundColor": "#D3E2DB",
  "cursorColor": "#EBC342",
  "cursorAccentColor": "#0E3125",
  "selectionColor": "#D3E2DB33",
  "borderColor": "#113E2E",
  "colors": {
    "black": "#194A39",
    "red": "#DA6058",
    "green": "#73C686",
    "yellow": "#EBC342",
    "blue": "#639BD5",
    "magenta": "#D78E3C",
    "cyan": "#6FB393",
    "white": "#BBCDC5",
    "lightBlack": "#67897A",
    "lightRed": "#EF796F",
    "lightGreen": "#82D896",
    "lightYellow": "#FBD664",
    "lightBlue": "#82B7EE",
    "lightMagenta": "#EEA85C",
    "lightCyan": "#8ECFAF",
    "lightWhite": "#E6F0EB"
  }
};

const css = `
  .tabs_nav, .tabs_list { background-color: #0A1D15; }
  .tabs_title { color: #A2B7AE; }
  .tab_tab { color: #67897A; background-color: #0A1D15; }
  .tab_tab.tab_active { color: #E6F0EB; background-color: #0E3125; box-shadow: inset 0 -2px 0 #EBC342; }
`;

exports.decorateConfig = (config) =>
  Object.assign({}, config, theme, { css: `${css}${config.css || ""}` });
