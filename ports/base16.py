"""tinted-theming base16 and base24 schemes (spec 0.11 YAML)."""

import palette as p
from ports._lib import HEADER, REPO, Out

META = {
    "id": "base16",
    "name": "Base16 / Base24",
    "category": "Palettes",
    "homepage": "https://github.com/tinted-theming/home",
    "enable": {
        "where": "tinty, or any tinted-theming builder",
        "code": 'cp {slug}.yaml "$(tinty config --data-dir-path)/custom-schemes/base16/"\ntinty apply base16-{slug}',
        "lang": "sh",
    },
    "notes": "Base16 and Base24 schemes. The accent slots follow the terminal colors, so keywords stay burnt orange "
    "and strings avocado, but base16 templates will show functions in denim and classes in harvest gold.",
}

AUTHOR = f"oddurs ({REPO})"


def slots(f):
    """base0X → role. Grounds run base → text_hi; accents keep base16's terminal hues
    (08 red, 0A yellow, 0B green, 0C cyan, 0D blue, 0E magenta), which is where this
    palette already puts them: burnt orange is the magenta, so keywords (0E) stay orange."""
    return {
        "base00": "base",
        "base01": "surface0",                          # lighter background: status bars, line numbers
        "base02": "surface2" if f.dark else "surface1",  # selection, as in every other port
        "base03": "overlay1",                          # comments
        "base04": "subtext0",                          # dark foreground
        "base05": "text",
        "base06": "text_hi",
        "base07": "text_hi",                           # no brighter step in the palette
        "base08": "red",                               # variables, tags, deletions; ANSI red
        "base09": "red_hi",                            # numbers, constants, booleans
        "base0A": "yellow",                            # classes, search; ANSI yellow
        "base0B": "green",                             # strings, insertions
        "base0C": "sage",                              # support, regex; ANSI cyan
        "base0D": "denim",                             # functions, headings; ANSI blue
        "base0E": "orange",                            # keywords, storage; ANSI magenta
        "base0F": "clay",                              # deprecated, embedded tags
    }


BASE24 = {
    "base10": "mantle",    # darker background
    "base11": "crust",     # darkest background
    "base12": "red_hi",    # bright red
    "base13": "yellow_hi",  # bright yellow
    "base14": "green_hi",  # bright green
    "base15": "sage_hi",   # bright cyan
    "base16": "denim_hi",  # bright blue
    "base17": "orange_hi",  # bright magenta
}


def scheme(f, system):
    mapping = slots(f) | (BASE24 if system == "base24" else {})
    palette = "\n".join(
        f'  {slot}: "{f.colors[role]}" # {role} ({p.ROLE_NAMES[role]})' for slot, role in mapping.items()
    )
    return (
        f"# {HEADER}\n"
        f'system: "{system}"\nname: "{f.name}"\nauthor: "{AUTHOR}"\n'
        f'variant: "{"dark" if f.dark else "light"}"\npalette:\n{palette}\n'
    )


def build(flavors):
    return [
        Out(f"{system}/{f.slug}.yaml", scheme(f, system), flavor=f.id,
            dest=f"$(tinty config --data-dir-path)/custom-schemes/{system}/{f.slug}.yaml", lang="yaml")
        for system in ("base16", "base24")
        for f in flavors
    ]
