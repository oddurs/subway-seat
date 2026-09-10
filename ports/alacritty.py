"""Alacritty: a TOML colour file per flavor, pulled in with `general.import`."""

from ports._lib import HEADER, Out
from ports._terminals import ANSI_NAMES, dim, lit, search, search_cur, selection

META = {
    "id": "alacritty",
    "name": "Alacritty",
    "category": "Terminals",
    "homepage": "https://alacritty.org",
    "enable": {
        "where": "~/.config/alacritty/alacritty.toml",
        "code": '[general]\nimport = ["~/.config/alacritty/themes/{slug}.toml"]',
        "lang": "toml",
    },
    "notes": "Normal, bright and dim colours, both cursors, selection, search, hints, footer bar and "
    "line indicator. `general.import` needs Alacritty 0.14 or later; older versions use a top-level `import`.",
}


def pair(a, b, fg, bg):
    return f'{a} = "{fg}"\n{b} = "{bg}"'


def table(name, body):
    return f"[colors.{name}]\n{body}\n"


def palette(colors):
    return "\n".join(f'{n} = "{c}"' for n, c in zip(ANSI_NAMES, colors))


def theme(f):
    sections = [
        table(
            "primary",
            f'background = "{f.base}"\nforeground = "{f.text}"\n'
            f'dim_foreground = "{f.overlay2}"\nbright_foreground = "{f.text_hi}"',
        ),
        table("cursor", pair("text", "cursor", f.base, lit(f))),
        table("vi_mode_cursor", pair("text", "cursor", f.base, f.sage)),
        table("search.matches", pair("foreground", "background", f.text, search(f))),
        table("search.focused_match", pair("foreground", "background", f.text_hi, search_cur(f))),
        table("footer_bar", pair("foreground", "background", f.text, f.surface1)),
        table("hints.start", pair("foreground", "background", f.base, lit(f))),
        table("hints.end", pair("foreground", "background", f.base, f.overlay2)),
        table("line_indicator", pair("foreground", "background", f.subtext0, f.surface0)),
        table("selection", pair("text", "background", f.text_hi, selection(f))),
        table("normal", palette(f.ansi[:8])),
        table("bright", palette(f.ansi[8:])),
        table("dim", palette([dim(f, c) for c in f.ansi[:8]])),
    ]
    return f"# {HEADER}\n# {f.name}\n\n" + "\n".join(sections)


def build(flavors):
    return [
        Out(
            f"{f.slug}.toml",
            theme(f),
            flavor=f.id,
            dest=f"~/.config/alacritty/themes/{f.slug}.toml",
            lang="toml",
        )
        for f in flavors
    ]
