// Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
// Paris Guimard. Enable with localPlugins: ["paris-guimard"] in ~/.hyper.js.
// selectionColor is a translucent wash of the text color, not the solid selection color the other
// terminals use: Hyper's xterm.js draws the selection over the glyphs, so an opaque color would hide them.
"use strict";

const theme = {
  "backgroundColor": "#212D27",
  "foregroundColor": "#DAE0DC",
  "cursorColor": "#EBC168",
  "cursorAccentColor": "#212D27",
  "selectionColor": "#DAE0DC33",
  "borderColor": "#2A3831",
  "colors": {
    "black": "#34453C",
    "red": "#CD6B63",
    "green": "#80C28E",
    "yellow": "#EBC168",
    "blue": "#709BC8",
    "magenta": "#D0914F",
    "cyan": "#7BB096",
    "white": "#C3CAC6",
    "lightBlack": "#77847D",
    "lightRed": "#E1837A",
    "lightGreen": "#8FD59E",
    "lightYellow": "#FBD380",
    "lightBlue": "#8DB6E2",
    "lightMagenta": "#E7AB6D",
    "lightCyan": "#98CCB2",
    "lightWhite": "#EAEEEC"
  }
};

const css = `
  .tabs_nav, .tabs_list { background-color: #141A17; }
  .tabs_title { color: #ABB4AF; }
  .tab_tab { color: #77847D; background-color: #141A17; }
  .tab_tab.tab_active { color: #EAEEEC; background-color: #212D27; box-shadow: inset 0 -2px 0 #EBC168; }
`;

exports.decorateConfig = (config) =>
  Object.assign({}, config, theme, { css: `${css}${config.css || ""}` });
