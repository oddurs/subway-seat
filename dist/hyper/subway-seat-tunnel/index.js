// Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
// Subway Seat Tunnel. Enable with localPlugins: ["subway-seat-tunnel"] in ~/.hyper.js.
// selectionColor is a translucent wash of the text color, not the solid selection color the other
// terminals use: Hyper's xterm.js draws the selection over the glyphs, so an opaque color would hide them.
"use strict";

const theme = {
  "backgroundColor": "#24180E",
  "foregroundColor": "#E9D8B6",
  "cursorColor": "#F3BF45",
  "cursorAccentColor": "#24180E",
  "selectionColor": "#E9D8B633",
  "borderColor": "#302115",
  "colors": {
    "black": "#3D2C1D",
    "red": "#E05C45",
    "green": "#ADB956",
    "yellow": "#F3BF45",
    "blue": "#7F9BAE",
    "magenta": "#EC7F31",
    "cyan": "#86AD95",
    "white": "#D6C3A0",
    "lightBlack": "#917759",
    "lightRed": "#F97160",
    "lightGreen": "#BFCB63",
    "lightYellow": "#FFD36B",
    "lightBlue": "#9DB6C6",
    "lightMagenta": "#FF9D55",
    "lightCyan": "#A5C9B0",
    "lightWhite": "#F6EAD1"
  }
};

const css = `
  .tabs_nav, .tabs_list { background-color: #140D07; }
  .tabs_title { color: #C0AA88; }
  .tab_tab { color: #917759; background-color: #140D07; }
  .tab_tab.tab_active { color: #F6EAD1; background-color: #24180E; box-shadow: inset 0 -2px 0 #F3BF45; }
`;

exports.decorateConfig = (config) =>
  Object.assign({}, config, theme, { css: `${css}${config.css || ""}` });
