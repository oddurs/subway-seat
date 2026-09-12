// Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
// London Deep Level. Enable with localPlugins: ["london-deep-level"] in ~/.hyper.js.
// selectionColor is a translucent wash of the text color, not the solid selection color the other
// terminals use: Hyper's xterm.js draws the selection over the glyphs, so an opaque color would hide them.
"use strict";

const theme = {
  "backgroundColor": "#121A2D",
  "foregroundColor": "#D4DAE7",
  "cursorColor": "#F2C03F",
  "cursorAccentColor": "#121A2D",
  "selectionColor": "#D4DAE733",
  "borderColor": "#1A243A",
  "colors": {
    "black": "#232F49",
    "red": "#DB6052",
    "green": "#77C581",
    "yellow": "#F2C03F",
    "blue": "#7595DA",
    "magenta": "#DE8946",
    "cyan": "#54B4B5",
    "white": "#BEC6D5",
    "lightBlack": "#6F7C97",
    "lightRed": "#F17869",
    "lightGreen": "#9AD2A0",
    "lightYellow": "#FFD36C",
    "lightBlue": "#8BB0FF",
    "lightMagenta": "#E5AA7F",
    "lightCyan": "#72D1D3",
    "lightWhite": "#E7EBF3"
  }
};

const css = `
  .tabs_nav, .tabs_list { background-color: #0A0E18; }
  .tabs_title { color: #A5AEC0; }
  .tab_tab { color: #6F7C97; background-color: #0A0E18; }
  .tab_tab.tab_active { color: #E7EBF3; background-color: #121A2D; box-shadow: inset 0 -2px 0 #F2C03F; }
`;

exports.decorateConfig = (config) =>
  Object.assign({}, config, theme, { css: `${css}${config.css || ""}` });
