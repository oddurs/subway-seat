from xml.sax.saxutils import escape

from ports._lib import HEADER, Out, scope_rules, tints

META = {
    "id": "bat",
    "name": "bat",
    "category": "CLI & TUI",
    "homepage": "https://github.com/sharkdp/bat",
    "enable": {
        "where": "config.fish (bash and zsh: ~/.bashrc or ~/.zshrc), after copying the themes to "
        "`$(bat --config-dir)/themes` and running `bat cache --build`",
        "code": 'set -gx BAT_THEME "{name}"',
        "lang": "fish",
        "sh": 'export BAT_THEME="{name}"',
        "file": "~/.config/fish/conf.d/subway-seat.fish",
    },
    "auto": {
        "where": "config.fish, with BAT_THEME left unset (bat 0.25+ asks the terminal which to use)",
        "code": 'set -gx BAT_THEME_DARK "Subway Seat"\nset -gx BAT_THEME_LIGHT "Subway Seat Enamel"',
        "lang": "fish",
        "file": "~/.config/fish/conf.d/subway-seat.fish",
    },
    "detect": ["bat", "batcat"],
    "notes": "TextMate themes for bat. delta (through the delta port), aichat and anything else built on "
    "syntect can use them too.",
}


def tmtheme(f):
    def d(pairs):
        return "".join(f"<key>{k}</key><string>{escape(v)}</string>" for k, v in pairs.items())

    t = tints(f)
    def style(st):
        return " ".join(sorted(st & {"bold", "italic", "underline"}))

    rules = [
        "<dict><key>settings</key><dict>"
        + d({
            "background": f.base, "foreground": f.text, "caret": f.yellow if f.dark else f.orange,
            "lineHighlight": f.surface0 if f.dark else f.mantle, "selection": f.surface2 if f.dark else f.surface1,
            "gutter": f.base, "gutterForeground": f.overlay0, "invisibles": f.surface1,
            "findHighlight": t["search"], "findHighlightForeground": f.text_hi,
            "bracketsForeground": f.yellow_hi if f.dark else f.orange, "guide": f.surface0,
            "activeGuide": f.surface2, "accent": f.orange, "misspelling": f.red_hi,
        })
        + "</dict></dict>"
    ]
    for scope, color, st in scope_rules(f):
        s = {"foreground": color}
        if style(st):
            s["fontStyle"] = style(st)
        rules.append(f"<dict><key>scope</key><string>{escape(scope)}</string><key>settings</key><dict>{d(s)}</dict></dict>")
    # Diff files: bat and delta draw no scope backgrounds, so the colors follow the
    # foreground-only rule (bold file headers, denim hunk headers); the tints are for
    # syntect apps that do paint them.
    diff = [
        ("meta.diff.header, meta.diff.header.from-file, meta.diff.header.to-file, "
         "punctuation.definition.from-file.diff, punctuation.definition.to-file.diff",
         {"foreground": f.text_hi, "fontStyle": "bold"}),
        ("meta.diff.range, punctuation.definition.range.diff", {"foreground": f.denim}),
        ("markup.inserted.diff", {"background": t["add"], "foreground": f.green}),
        ("markup.deleted.diff", {"background": t["del"], "foreground": f.red_hi}),
    ]
    for scope, st_ in diff:
        rules.append(f"<dict><key>scope</key><string>{escape(scope)}</string><key>settings</key><dict>{d(st_)}</dict></dict>")
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
        Out(f"{f.name}.tmTheme", tmtheme(f), flavor=f.id, dest=f"~/.config/bat/themes/{f.name}.tmTheme", lang="xml",
            how="then run `bat cache --build` (on Windows the folder is %APPDATA%\\bat\\themes)")
        for f in flavors
    ]
