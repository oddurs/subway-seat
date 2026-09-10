"""Newsboat: color lines per flavor. Newsboat only knows 256 terminal colors, so these point at the
slots where each flavor's terminal port puts its roles."""

from ports._lib import HEADER, Out

META = {
    "id": "newsboat",
    "name": "Newsboat",
    "category": "CLI & TUI",
    "homepage": "https://newsboat.org",
    "detect": ["newsboat"],
    "requires": "Newsboat 2.25+",
    "enable": {
        "where": "~/.config/newsboat/config (or ~/.newsboat/config if you use that folder)",
        "code": "include ~/.config/newsboat/{slug}",
        "lang": "conf",
        "file": "~/.config/newsboat/config",
    },
    "notes": "Gold unread items, a raised bar for the cursor and the key hints, orange article headers and "
    "denim links. Newsboat can't take hex colors, so each file names the terminal-palette slots where that "
    "flavor's terminal port keeps these roles; use it with the same flavor in your terminal.",
}


def slot(f, role):
    """The terminal color (color0–color15) that holds `role` in this flavor's ANSI palette."""
    return f"color{f.ansi_roles.index(role)}"


def rc(f):
    def s(role):
        return "default" if role is None else slot(f, role)

    bar = "surface1"
    colors = [
        ("background", None, None),
        ("listnormal", None, None),
        ("listfocus", None, bar, "bold"),
        ("listnormal_unread", "yellow", None, "bold"),
        ("listfocus_unread", "yellow", bar, "bold"),
        ("title", "orange", None, "bold"),
        ("info", "subtext1", bar),
        ("hint-key", "yellow", bar, "bold"),
        ("hint-keys-delimiter", "overlay1", bar),
        ("hint-separator", "overlay1", bar),
        ("hint-description", "subtext1", bar),
        ("article", None, None),
        ("end-of-text-marker", "overlay1", None),
    ]
    highlights = [
        (r"^(Feed|Title|Author|Link|Date|Podcast Download URL|Flags):", "orange", None, "bold"),
        (r"https?://[^ ]+", "denim", None, "underline"),
        (r"\\[[0-9]+\\]", "sage", None, "bold"),
        (r"\\((link|image|video|embedded flash|audio)\\)", "overlay1", None),
    ]
    width = max(len(c[0]) for c in colors)
    lines = [
        f"# {HEADER}",
        f"# {f.name} for Newsboat. The colorN slots are {f.name}'s terminal palette,",
        f"# so run it in a terminal set to {f.name}.",
        "",
    ]
    for name, fg, bg, *attrs in colors:
        lines.append(" ".join([f"color {name:<{width}}", f"{s(fg):<8}", s(bg), *attrs]).rstrip())
    lines.append("")
    for regex, fg, bg, *attrs in highlights:
        lines.append(" ".join([f'highlight article "{regex}"', s(fg), s(bg), *attrs]))
    return "\n".join(lines) + "\n"


def build(flavors):
    return [Out(f.slug, rc(f), flavor=f.id, dest=f"~/.config/newsboat/{f.slug}", lang="conf") for f in flavors]
