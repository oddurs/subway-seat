// Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
// London Moquette. Enable with localPlugins: ["london-moquette"] in ~/.hyper.js.
// selectionColor is a translucent wash of the text color, not the solid selection color the other
// terminals use: Hyper's xterm.js draws the selection over the glyphs, so an opaque color would hide them.
"use strict";

const theme = {
  "backgroundColor": "#1E2941",
  "foregroundColor": "#D8DEEA",
  "cursorColor": "#F2C03F",
  "cursorAccentColor": "#1E2941",
  "selectionColor": "#D8DEEA33",
  "borderColor": "#263451",
  "colors": {
    "black": "#303F61",
    "red": "#DB6052",
    "green": "#77C581",
    "yellow": "#F2C03F",
    "blue": "#7595DA",
    "magenta": "#DE8946",
    "cyan": "#54B4B5",
    "white": "#C1C9D8",
    "lightBlack": "#73819C",
    "lightRed": "#F17869",
    "lightGreen": "#9AD2A0",
    "lightYellow": "#FFD36C",
    "lightBlue": "#8BB0FF",
    "lightMagenta": "#E5AA7F",
    "lightCyan": "#72D1D3",
    "lightWhite": "#E9EDF5"
  }
};

const css = `
  .tabs_nav, .tabs_list { background-color: #121826; }
  .tabs_title { color: #A9B2C4; }
  .tab_tab { color: #73819C; background-color: #121826; }
  .tab_tab.tab_active { color: #E9EDF5; background-color: #1E2941; box-shadow: inset 0 -2px 0 #F2C03F; }
`;

exports.decorateConfig = (config) =>
  Object.assign({}, config, theme, { css: `${css}${config.css || ""}` });
