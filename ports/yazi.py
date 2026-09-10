from ports._cli import ink, selection
from ports._lib import HEADER, Out
from ports.bat import tmtheme

META = {
    "id": "yazi",
    "name": "Yazi",
    "category": "CLI & TUI",
    "homepage": "https://yazi-rs.github.io",
    "enable": {
        "where": "~/.config/yazi/theme.toml",
        "code": '[flavor]\ndark  = "{slug}"\nlight = "{slug}"',
        "lang": "toml",
    },
    "notes": "Yazi flavors with gold directories, an orange mode badge and a gold bar on the hovered "
    "file; previews use the bundled tmTheme. File and extension icons keep Yazi's own colors.",
}


def style(fg=None, bg=None, **attrs):
    parts = [f'fg = "{fg}"'] if fg else []
    parts += [f'bg = "{bg}"'] if bg else []
    parts += [f"{k} = true" for k, v in attrs.items() if v]
    return "{ " + ", ".join(parts) + " }" if parts else "{}"


def flavor(f):
    on, sel = ink(f), selection(f)
    accent = style(f.orange)
    sections = {
        "app": {"overall": style(bg=f.base)},
        "mgr": {
            "cwd": style(f.yellow),
            "find_keyword": style(f.yellow, bold=True, italic=True, underline=True),
            "find_position": f'{{ fg = "{f.orange}", bg = "reset", bold = true, italic = true }}',
            "symlink_target": style(f.sage, italic=True),
            "marker_copied": style(f.green, f.green),
            "marker_cut": style(f.red_hi, f.red_hi),
            "marker_marked": style(f.sage, f.sage),
            "marker_selected": style(f.yellow, f.yellow),
            "count_copied": style(on, f.green),
            "count_cut": style(on, f.red_hi),
            "count_selected": style(on, f.yellow),
            "border_style": style(f.surface2),
        },
        "tabs": {
            "active": style(on, f.orange, bold=True),
            "inactive": style(f.subtext1, f.surface1),
        },
        "mode": {
            "normal_main": style(on, f.orange, bold=True),
            "normal_alt": style(f.orange, f.surface0),
            "select_main": style(on, f.green, bold=True),
            "select_alt": style(f.green, f.surface0),
            "unset_main": style(on, f.red_hi, bold=True),
            "unset_alt": style(f.red_hi, f.surface0),
        },
        "indicator": {
            "parent": style(f.text_hi, f.surface1),
            "current": style(on, f.yellow),
            "preview": style(f.text_hi, f.surface1),
        },
        "status": {
            "perm_sep": style(f.overlay0),
            "perm_type": style(f.sage),
            "perm_read": style(f.yellow),
            "perm_write": style(f.orange),
            "perm_exec": style(f.green),
            "progress_label": style(f.text_hi, bold=True),
            "progress_normal": style(f.green, f.surface1),
            "progress_error": style(f.red_hi, f.surface1),
        },
        "which": {
            "border": accent,
            "mask": style(bg=f.mantle),
            "cand": style(f.yellow),
            "rest": style(f.overlay1),
            "desc": style(f.subtext1),
            "separator_style": style(f.surface2),
        },
        "confirm": {
            "border": accent,
            "title": style(f.orange, bold=True),
            "body": "{}",
            "list": "{}",
            "btn_yes": style(on, f.orange, bold=True),
            "btn_no": style(f.subtext1),
        },
        "spot": {
            "border": accent,
            "title": accent,
            "tbl_col": style(f.sage),
            "tbl_cell": style(on, f.yellow),
        },
        "notify": {
            "title_info": style(f.denim),
            "title_warn": style(f.yellow),
            "title_error": style(f.red_hi),
        },
        "pick": {"border": accent, "active": style(f.orange, bold=True), "inactive": "{}"},
        "input": {"border": accent, "title": "{}", "value": "{}", "selected": style(f.text_hi, sel)},
        "cmp": {"border": accent, "active": style(f.text_hi, f.surface1), "inactive": "{}"},
        "tasks": {"border": accent, "title": "{}", "hovered": style(f.orange, bold=True)},
        "help": {
            "border": accent,
            "chord": style(f.yellow),
            "action": style(f.subtext1),
            "hovered": style(bg=f.surface1, bold=True),
        },
    }
    out = [f"# {HEADER}", f"# {f.name} flavor for Yazi.", ""]
    for name, keys in sections.items():
        out.append(f"[{name}]")
        width = max(map(len, keys))
        out += [f"{k:<{width}} = {v}" for k, v in keys.items()]
        out.append("")

    rules = [
        "# Media",
        f'{{ mime = "**/image/*", fg = "{f.clay}" }}',
        f'{{ mime = "**/{{audio,video}}/*", fg = "{f.orange}" }}',
        "# Archives",
        (
            '{ mime = "**/application/{zip,rar,7z*,tar,gzip,xz,zstd,bzip*,lzma,compress,archive,cpio,arj,xar,ms-cab*}", '
            f'fg = "{f.red_hi}" }}'
        ),
        "# Documents",
        f'{{ mime = "**/application/{{pdf,doc,rtf}}", fg = "{f.denim}" }}',
        "# Virtual file system",
        f'{{ mime = "vfs/{{absent,stale}}", fg = "{f.overlay0}" }}',
        "# Special files",
        f'{{ url = "*", is = "orphan", bg = "{f.red}" }}',
        f'{{ url = "*", is = "exec", fg = "{f.green}" }}',
        "# Dummy files",
        f'{{ url = "*", is = "dummy", bg = "{f.red}" }}',
        f'{{ url = "*/", is = "dummy", bg = "{f.red}" }}',
        "# Fallback",
        f'{{ url = "*/", fg = "{f.yellow}", bold = true }}',
    ]
    out.append("[filetype]\nrules = [")
    out += [f"\t{r}" + ("" if r.startswith("#") else ",") for r in rules]
    out += ["]", ""]

    dirs = [
        (".config", "\ue5fc"), (".git", "\ue5fb"), (".github", "\ue5fd"), (".npm", "\ue5fa"),
        ("Desktop", "\uf108"), ("Development", "\ue70c"), ("Documents", "\uf401"), ("Downloads", "\uf498"),
        ("Library", "\ueb9c"), ("Movies", "\uf447"), ("Music", "\uf025"), ("Pictures", "\ue244"),
        ("Public", "\uf42b"), ("Videos", "\uf447"),
    ]
    conds = [
        ("orphan", "\uf127", f.red_hi), ("link", "\uf481", f.sage),
        ("block", "\uf0c9", f.clay), ("char", "\uf1c0", f.clay), ("fifo", "\uf1d1", f.clay),
        ("sock", "\uf1e4", f.clay), ("sticky", "\uf08d", f.clay), ("dummy", "\uf057", f.red_hi),
        ("dir & hovered", "\ue5fe", f.yellow), ("dir", "\ue5ff", f.yellow),
        ("exec", "\uf489", f.green), ("!dir", "\uf15b", f.subtext1),
    ]
    out.append("[icon]\ndirs = [")
    out += [f'\t{{ name = "{n}", text = "{g}", fg = "{f.yellow}" }},' for n, g in dirs]
    out.append("]\nconds = [")
    out += [f'\t{{ if = "{c}", text = "{g}", fg = "{col}" }},' for c, g, col in conds]
    out += ["]", ""]
    return "\n".join(out)


def build(flavors):
    outs = []
    for f in flavors:
        base = f"~/.config/yazi/flavors/{f.slug}.yazi"
        outs.append(Out(f"{f.slug}.yazi/flavor.toml", flavor(f), flavor=f.id, dest=f"{base}/flavor.toml", lang="toml"))
        outs.append(Out(f"{f.slug}.yazi/tmtheme.xml", tmtheme(f), flavor=f.id, dest=f"{base}/tmtheme.xml", lang="xml"))
    return outs
