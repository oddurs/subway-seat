// Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
// Paris Guimard. Enable with localPlugins: ["paris-guimard"] in ~/.hyper.js.
// selectionColor is a translucent wash of the text color, not the solid selection color the other
// terminals use: Hyper's xterm.js draws the selection over the glyphs, so an opaque color would hide them.
"use strict";

const theme = {
  "backgroundColor": "#1E2E26",
  "foregroundColor": "#D9E1DB",
  "cursorColor": "#F2BF4B",
  "cursorAccentColor": "#1E2E26",
  "selectionColor": "#D9E1DB33",
  "borderColor": "#263930",
  "colors": {
    "black": "#30463B",
    "red": "#CD6B63",
    "green": "#80C28E",
    "yellow": "#F2BF4B",
    "blue": "#709BC8",
    "magenta": "#D0914F",
    "cyan": "#5FA09D",
    "white": "#C2CBC5",
    "lightBlack": "#74857C",
    "lightRed": "#EE8F85",
    "lightGreen": "#8FD59E",
    "lightYellow": "#FFD273",
    "lightBlue": "#8DB6E2",
    "lightMagenta": "#E7AB6D",
    "lightCyan": "#8CCCC9",
    "lightWhite": "#E9EEEC"
  }
};

const css = `
  .tabs_nav, .tabs_list { background-color: #131A17; }
  .tabs_title { color: #A9B5AE; }
  .tab_tab { color: #74857C; background-color: #131A17; }
  .tab_tab.tab_active { color: #E9EEEC; background-color: #1E2E26; box-shadow: inset 0 -2px 0 #F2BF4B; }
`;

exports.decorateConfig = (config) =>
  Object.assign({}, config, theme, { css: `${css}${config.css || ""}` });
