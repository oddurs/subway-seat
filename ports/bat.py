from xml.sax.saxutils import escape

from ports._lib import HEADER, Out, scope_rules, tints

META = {
    "id": "bat",
    "name": "bat",
    "category": "CLI & TUI",
    "homepage": "https://github.com/sharkdp/bat",
    "enable": {
        "where": "your shell, after copying the themes to `$(bat --config-dir)/themes`",
        "code": 'bat cache --build\nset -Ux BAT_THEME "{name}"',
        "lang": "fish",
    },
    "notes": "TextMate themes for bat. delta, aichat and anything else built on syntect can use them too.",
}


def tmtheme(f):
    def d(pairs):
        return "".join(f"<key>{k}</key><string>{escape(v)}</string>" for k, v in pairs.items())

    t = tints(f)
    style = lambda st: " ".join(sorted(st & {"bold", "italic", "underline"}))
    rules = [
        "<dict><key>settings</key><dict>"
        + d({
            "background": f.base, "foreground": f.text, "caret": f.yellow if f.dark else f.orange,
            "lineHighlight": f.surface0 if f.dark else f.mantle, "selection": f.surface2 if f.dark else f.surface1,
            "gutter": f.base, "gutterForeground": f.overlay0, "invisibles": f.surface1,
            "findHighlight": f.yellow, "findHighlightForeground": f.crust,
            "bracketsForeground": f.yellow_hi, "guide": f.surface0, "activeGuide": f.surface2,
        })
        + "</dict></dict>"
    ]
    for scope, color, st in scope_rules(f):
        s = {"foreground": color}
        if style(st):
            s["fontStyle"] = style(st)
        rules.append(f"<dict><key>scope</key><string>{escape(scope)}</string><key>settings</key><dict>{d(s)}</dict></dict>")
    rules.append(f"<dict><key>scope</key><string>markup.inserted.diff</string><key>settings</key><dict>{d({'background': t['add'], 'foreground': f.green})}</dict></dict>")
    rules.append(f"<dict><key>scope</key><string>markup.deleted.diff</string><key>settings</key><dict>{d({'background': t['del'], 'foreground': f.red_hi})}</dict></dict>")
    body = "\n    ".join(rules)
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<!-- {HEADER} -->
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>name</key><string>{f.name}</string>
  <key>semanticClass</key><string>theme.{'dark' if f.dark else 'light'}.{f.slug}</string>
  <key>settings</key>
  <array>
    {body}
  </array>
</dict>
</plist>
"""


def build(flavors):
    return [
        Out(f"{f.name}.tmTheme", tmtheme(f), flavor=f.id,
            dest=f"$(bat --config-dir)/themes/{f.name}.tmTheme", lang="xml")
        for f in flavors
    ]
