import palette as p
from ports._lib import HEADER, Out, rgb
from ports._palettes import diff_tokens, kebab, role_name

META = {
    "id": "css",
    "name": "CSS variables",
    "category": "Palettes",
    "homepage": "https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables/Using_custom_properties",
    "enable": {
        "where": "your stylesheet",
        "code": '@import url("{slug}.css");\n\nbody {{\n  background: var(--ss-base);\n  color: var(--ss-text);\n}}\n\n'
        ".scrim {{\n  background: rgb(var(--ss-crust-rgb) / 0.8);\n}}",
        "lang": "css",
    },
    "auto": {
        "where": "your stylesheet",
        "code": '@import url("subway-seat-flavors.css");\n\n'
        "/* Enamel when the system is light, Walnut when it's dark;\n"
        '   data-theme="walnut" | "tunnel" | "enamel" on <html> picks one instead. */',
        "lang": "css",
    },
    "notes": "Every role as a custom property, with an -rgb triplet beside it for transparency, and the diff "
    "tints as --ss-diff-* (line and word grounds for added, removed and changed text). "
    "subway-seat-flavors.css holds all three, switched by data-theme or the system light/dark setting.",
}

GROUPS = [("Ground", p.GROUND), ("Text", p.TEXT), ("Accents", p.ACCENTS)]


def declarations(f, indent="  "):
    lines = [f"{indent}color-scheme: {'dark' if f.dark else 'light'};"]
    for title, roles in GROUPS:
        lines.append(f"\n{indent}/* {title} */")
        lines += [f"{indent}--ss-{kebab(r)}: {f.colors[r]}; /* {role_name(f, r)} */" for r in roles]
    lines.append(f"\n{indent}/* Diff grounds: -add/-del/-chg for lines, -emph for changed words, -dim for faded diffs */")
    lines += [f"{indent}--ss-{name}: {value};" for name, value in diff_tokens(f).items()]
    lines.append(f"\n{indent}/* RGB triplets, for rgb(var(--ss-base-rgb) / 0.5) */")
    lines += [f"{indent}--ss-{kebab(r)}-rgb: {' '.join(map(str, rgb(f.colors[r])))};" for r in p.ROLES]
    return "\n".join(lines)


def single(f):
    return f"/* {HEADER} */\n/* {f.name}: {f.blurb} */\n\n:root {{\n{declarations(f)}\n}}\n"


def combined(flavors):
    light = next(f for f in flavors if not f.dark)
    blocks = [
        f"/* {HEADER} */",
        (
            '/* All flavors. Set data-theme="walnut" | "tunnel" | "enamel" on <html> (or any element),\n'
            f"   or leave it off to follow the system: dark → {p.DEFAULT.name}, light → {light.name}. */"
        ),
        f":root,\n[data-theme=\"{p.DEFAULT.id}\"] {{\n{declarations(p.DEFAULT)}\n}}",
        f"@media (prefers-color-scheme: light) {{\n  :root:not([data-theme]) {{\n{declarations(light, '    ')}\n  }}\n}}",
    ]
    blocks += [
        f"[data-theme=\"{f.id}\"] {{\n{declarations(f)}\n}}" for f in flavors if f.id != p.DEFAULT.id
    ]
    return "\n\n".join(blocks) + "\n"


def build(flavors):
    how = "in your project"
    outs = [
        Out(f"{f.slug}.css", single(f), flavor=f.id, dest=f"styles/{f.slug}.css", lang="css", how=how)
        for f in flavors
    ]
    outs.append(Out("subway-seat-flavors.css", combined(flavors), dest="styles/subway-seat-flavors.css",
                    lang="css", how=how))
    return outs
