from ports._lib import HEADER, Out

META = {
    "id": "atuin",
    "name": "Atuin",
    "category": "CLI & TUI",
    "homepage": "https://atuin.sh",
    "enable": {"where": "~/.config/atuin/config.toml", "code": '[theme]\nname = "{slug}"', "lang": "toml"},
    "notes": "Colours for the history search: gold titles, orange highlights, calm annotations, and "
    "command-line colours that match the fish port.",
}


def theme(f):
    colors = {
        "AlertInfo": f.green,
        "AlertWarn": f.yellow,
        "AlertError": f.red_hi,
        "Annotation": f.overlay1,
        "Base": f.text,
        "Guidance": f.subtext0,
        "Important": f.orange,
        "Title": f.yellow,
        "Muted": f.overlay0,
        "SyntaxCommand": f.yellow,
        "SyntaxFlag": f.sage,
        "SyntaxString": f.green,
        "SyntaxVariable": f.clay,
        "SyntaxOperator": f.orange,
        "SyntaxComment": f.overlay1,
    }
    body = "\n".join(f'{k} = "{v}"' for k, v in colors.items())
    return f'# {HEADER}\n# {f.name} for Atuin.\n[theme]\nname = "{f.slug}"\n\n[colors]\n{body}\n'


def build(flavors):
    return [
        Out(f"{f.slug}.toml", theme(f), flavor=f.id, dest=f"~/.config/atuin/themes/{f.slug}.toml", lang="toml")
        for f in flavors
    ]
