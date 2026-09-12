// Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
// Paris Catacombes. Enable with localPlugins: ["paris-catacombes"] in ~/.hyper.js.
// selectionColor is a translucent wash of the text color, not the solid selection color the other
// terminals use: Hyper's xterm.js draws the selection over the glyphs, so an opaque color would hide them.
"use strict";

const theme = {
  "backgroundColor": "#062017",
  "foregroundColor": "#CFDED7",
  "cursorColor": "#EBC342",
  "cursorAccentColor": "#062017",
  "selectionColor": "#CFDED733",
  "borderColor": "#0A2B20",
  "colors": {
    "black": "#13382A",
    "red": "#DA6058",
    "green": "#73C686",
    "yellow": "#EBC342",
    "blue": "#639BD5",
    "magenta": "#D78E3C",
    "cyan": "#6FB393",
    "white": "#B8CAC2",
    "lightBlack": "#648576",
    "lightRed": "#EF796F",
    "lightGreen": "#82D896",
    "lightYellow": "#FBD664",
    "lightBlue": "#82B7EE",
    "lightMagenta": "#EEA85C",
    "lightCyan": "#8ECFAF",
    "lightWhite": "#E4EEE9"
  }
};

const css = `
  .tabs_nav, .tabs_list { background-color: #05120C; }
  .tabs_title { color: #9EB3AA; }
  .tab_tab { color: #648576; background-color: #05120C; }
  .tab_tab.tab_active { color: #E4EEE9; background-color: #062017; box-shadow: inset 0 -2px 0 #EBC342; }
`;

exports.decorateConfig = (config) =>
  Object.assign({}, config, theme, { css: `${css}${config.css || ""}` });
