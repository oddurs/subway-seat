// Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
// London Portland. Enable with localPlugins: ["london-portland"] in ~/.hyper.js.
// selectionColor is a translucent wash of the text color, not the solid selection color the other
// terminals use: Hyper's xterm.js draws the selection over the glyphs, so an opaque color would hide them.
"use strict";

const theme = {
  "backgroundColor": "#E0EAFE",
  "foregroundColor": "#293040",
  "cursorColor": "#B14A07",
  "cursorAccentColor": "#E0EAFE",
  "selectionColor": "#29304033",
  "borderColor": "#C5D5F3",
  "colors": {
    "black": "#3C4557",
    "red": "#9B211A",
    "green": "#0D8131",
    "yellow": "#896800",
    "blue": "#0019A8",
    "magenta": "#B14A07",
    "cyan": "#007376",
    "white": "#8FA5D0",
    "lightBlack": "#697794",
    "lightRed": "#C92B23",
    "lightGreen": "#008730",
    "lightYellow": "#977300",
    "lightBlue": "#4A6EBD",
    "lightMagenta": "#B86100",
    "lightCyan": "#008688",
    "lightWhite": "#A1B7E5"
  }
};

const css = `
  .tabs_nav, .tabs_list { background-color: #C5D5F3; }
  .tabs_title { color: #4A5469; }
  .tab_tab { color: #697794; background-color: #C5D5F3; }
  .tab_tab.tab_active { color: #1B202B; background-color: #E0EAFE; box-shadow: inset 0 -2px 0 #B14A07; }
`;

exports.decorateConfig = (config) =>
  Object.assign({}, config, theme, { css: `${css}${config.css || ""}` });
