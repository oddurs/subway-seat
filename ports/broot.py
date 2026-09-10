"""broot: a skin per flavor (hjson), imported from conf.hjson by terminal luma."""

import palette as p
from ports._cli import stripe
from ports._lib import HEADER, Out, ink, tints

META = {
    "id": "broot",
    "name": "broot",
    "category": "CLI & TUI",
    "homepage": "https://dystroy.org/broot/",
    "detect": ["broot"],
    "requires": "broot 1.14+",
    "enable": {
        "where": "the imports list in ~/.config/broot/conf.hjson (replace the skin entry for your terminal)",
        "code": '{{ "luma": ["dark", "light", "unknown"], "file": "skins/{slug}.hjson" }}',
        "lang": "json",
    },
    "auto": {
        "where": "the imports list in ~/.config/broot/conf.hjson, instead of the default skin entries",
        "code": '{ "luma": ["dark", "unknown"], "file": "skins/subway-seat.hjson" }\n'
        '{ "luma": "light", "file": "skins/subway-seat-enamel.hjson" }',
        "lang": "json",
    },
    "notes": "The tree in the eza port's colors: gold directories, avocado executables, sage links, the same "
    "permission and git colors, and file sizes and disk use along the avocado-to-redbird stripe. Panels you "
    "aren't in go quieter, the status line sits on the darker chrome, and previews of diffs use the shared "
    "tinted grounds. broot can only highlight previews with syntect's built-in themes, so the skins pick "
    "the closest: Mocha for the dark flavors, Solarized Light for Enamel. broot picks the import that "
    "matches your terminal's background, so the auto pair follows light and dark.",
}


def rgb(color):
    return "rgb({}, {}, {})".format(*p.hex_to_rgb(color))


def style(fg=None, bg=None, *attrs):
    parts = [rgb(fg) if fg else "none", rgb(bg) if bg else "none", *attrs]
    return " ".join(parts)


def skin(f):
    t = tints(f)
    # key: focused panel, or (focused, unfocused)
    entries = {
        "default": (style(f.text), style(f.subtext0)),
        "tree": (style(f.overlay0), style(f.surface2)),
        "parent": (style(f.subtext0), style(f.overlay1)),
        "file": (style(f.text), style(f.subtext0)),
        "directory": (style(f.yellow, None, "Bold"), style(f.yellow)),
        "exe": style(f.green, None, "Bold"),
        "link": style(f.sage),
        "pruning": style(f.overlay1, None, "Italic"),
        "perm__": style(f.overlay0),
        "perm_r": style(f.yellow),
        "perm_w": style(f.orange),
        "perm_x": style(f.green),
        "owner": style(f.yellow),
        "group": style(f.subtext1),
        "count": style(f.overlay2),
        "dates": style(f.subtext0),
        "sparse": style(f.clay),
        "content_extract": style(f.subtext1),
        "content_match": style(f.yellow, None, "Bold"),
        "device_id_major": style(f.subtext0),
        "device_id_sep": style(f.overlay0),
        "device_id_minor": style(f.subtext0),
        "git_branch": style(f.orange),
        "git_insertions": style(f.green),
        "git_deletions": style(f.red_hi),
        "git_status_current": style(f.overlay1),
        "git_status_modified": style(f.yellow),
        "git_status_staged": style(f.green),
        "git_status_new": style(f.green, None, "Bold"),
        "git_status_ignored": style(f.overlay0),
        "git_status_conflicted": style(f.red, None, "Bold"),
        "git_status_other": style(f.clay),
        "selected_line": (style(None, f.surface0), style(None, f.mantle)),
        "char_match": style(f.yellow, None, "Bold"),
        "file_error": style(f.red_hi),
        "flag_label": style(f.subtext0),
        "flag_value": style(f.orange, None, "Bold"),
        "input": (style(f.text), style(f.subtext0)),
        "status_error": style(ink(f), f.red),
        "status_job": style(f.yellow, f.mantle),
        "status_normal": style(f.subtext1, f.mantle),
        "status_italic": style(f.yellow, f.mantle, "Italic"),
        "status_bold": style(f.orange, f.mantle, "Bold"),
        "status_code": style(f.sage, f.mantle),
        "status_ellipsis": style(f.overlay1, f.mantle),
        "purpose_normal": style(f.subtext1, f.mantle),
        "purpose_italic": style(f.yellow, f.mantle, "Italic"),
        "purpose_bold": style(f.orange, f.mantle, "Bold"),
        "purpose_ellipsis": style(f.overlay1, f.mantle),
        "scrollbar_track": (style(f.surface1), style(f.surface0)),
        "scrollbar_thumb": (style(f.overlay1), style(f.overlay0)),
        "help_paragraph": style(f.text),
        "help_bold": style(f.orange, None, "Bold"),
        "help_italic": style(f.yellow, None, "Italic"),
        "help_code": style(f.green, f.surface0),
        "help_headers": style(f.yellow, None, "Bold"),
        "help_table_border": style(f.overlay0),
        "preview": (style(f.text), style(f.subtext0)),
        "preview_title": (style(f.text_hi), style(f.subtext0)),
        "preview_line_number": style(f.overlay0),
        "preview_separator": (style(f.surface2), style(f.surface1)),
        "preview_match": style(None, t["search"]),
        "diff_line_number": style(f.overlay1),
        "diff_added": style(None, t["add"]),
        "diff_removed": style(None, t["del"]),
        "hex_null": style(f.overlay0),
        "hex_ascii_graphic": style(f.subtext1),
        "hex_ascii_whitespace": style(f.green),
        "hex_ascii_other": style(f.orange),
        "hex_non_ascii": style(f.red_hi),
        "staging_area_title": (style(f.text_hi), style(f.subtext0)),
        "mode_command_mark": style(ink(f), f.orange, "Bold"),
    }
    # good_to_bad_*: file sizes, disk use and other gauges, from avocado to redbird
    entries |= {f"good_to_bad_{i}": rgb(c) for i, c in enumerate(stripe(f, 10))}

    width = max(len(k) for k in entries)
    lines = [f"# {HEADER}", f"# {f.name} for broot.", "skin: {"]
    for key, value in entries.items():
        value = " / ".join(value) if isinstance(value, tuple) else value
        lines.append(f"    {key + ':':<{width + 1}} {value}")
    lines.append("}")
    # The preview's syntax colors come from syntect's built-in themes; these two are the warmest fits.
    lines += ["", f"syntax_theme: {'MochaDark' if f.dark else 'SolarizedLight'}"]
    return "\n".join(lines) + "\n"


def build(flavors):
    return [
        Out(f"{f.slug}.hjson", skin(f), flavor=f.id, dest=f"~/.config/broot/skins/{f.slug}.hjson", lang="text")
        for f in flavors
    ]
