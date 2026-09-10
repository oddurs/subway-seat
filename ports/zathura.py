"""zathura: a zathurarc fragment per flavor, with recoloring on."""

import palette as p
from ports._lib import HEADER, Out, ink, selection, ui_colors

META = {
    "id": "zathura",
    "name": "zathura",
    "category": "Apps",
    "homepage": "https://pwmt.org/projects/zathura/",
    "detect": ["zathura"],
    "enable": {
        "where": "~/.config/zathura/zathurarc",
        "code": "include {slug}",
        "lang": "conf",
        "file": "~/.config/zathura/zathurarc",
    },
    "notes": "The window, status bar, completion and index in walnut and cream, with recoloring on so pages "
    "read as cream on walnut (Enamel: brown ink on cream). Colored figures keep their hue and images keep "
    "their own colors; Ctrl+R toggles back to the original pages. Search hits use the same gold and orange "
    "washes as every other port.",
}


def rgba(color, a):
    r, g, b = p.hex_to_rgb(color)
    return f"rgba({r},{g},{b},{a:g})"


def rc(f):
    c = ui_colors(f)
    settings = [
        ("# window", None),
        ("default-bg", f.base),
        ("default-fg", f.text),
        ("statusbar-bg", f.mantle),
        ("statusbar-fg", f.subtext1),
        ("inputbar-bg", f.mantle),
        ("inputbar-fg", f.text),
        ("# notifications", None),
        ("notification-bg", c["paper"]),
        ("notification-fg", f.text),
        ("notification-error-bg", f.red),
        ("notification-error-fg", ink(f)),
        ("notification-warning-bg", f.yellow),
        ("notification-warning-fg", ink(f)),
        ("# completion", None),
        ("completion-bg", c["paper"]),
        ("completion-fg", f.text),
        ("completion-group-bg", f.mantle),
        ("completion-group-fg", f.subtext0),
        ("completion-highlight-bg", selection(f)),
        ("completion-highlight-fg", f.text_hi),
        ("# index (table of contents)", None),
        ("index-bg", f.base),
        ("index-fg", f.text),
        ("index-active-bg", selection(f)),
        ("index-active-fg", f.text_hi),
        ("# search hits and link hints, washed over the page", None),
        ("highlight-color", rgba(f.yellow, 0.30)),
        ("highlight-active-color", rgba(f.orange, 0.50)),
        ("highlight-fg", f.text_hi),
        ("# pages while they render", None),
        ("render-loading-bg", f.base),
        ("render-loading-fg", f.overlay1),
        ("# digital signatures", None),
        ("signature-success-color", f.green),
        ("signature-warning-color", f.yellow),
        ("signature-error-color", f.red_hi),
        ("# recoloring: white paper → base, black ink → text; Ctrl+R toggles it", None),
        ("recolor-lightcolor", f.base),
        ("recolor-darkcolor", f.text),
        ("recolor", "true"),
        ("recolor-keephue", "true"),
        ("recolor-reverse-video", "true"),
    ]
    width = max(len(k) for k, v in settings if v)
    lines = [f"# {HEADER}", f"# {f.name} for zathura. In zathurarc: include {f.slug}"]
    for key, value in settings:
        if value is None:
            lines += ["", key]
        else:
            lines.append(f'set {key:<{width}} "{value}"')
    return "\n".join(lines) + "\n"


def build(flavors):
    return [Out(f.slug, rc(f), flavor=f.id, dest=f"~/.config/zathura/{f.slug}", lang="conf") for f in flavors]
