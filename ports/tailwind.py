import json

import palette as p
from ports._lib import HEADER, Out
from ports._palettes import diff_tokens, kebab

META = {
    "id": "tailwind",
    "name": "Tailwind CSS",
    "category": "Palettes",
    "homepage": "https://tailwindcss.com",
    "enable": {
        "where": "your main CSS file (Tailwind v4)",
        "code": '@import "tailwindcss";\n@import "./{slug}.css";\n\n/* bg-ss-base text-ss-text border-ss-surface1 text-ss-orange bg-ss-diff-add */',
        "lang": "css",
    },
    "auto": {
        "where": "your main CSS file (Tailwind v4)",
        "code": '@import "tailwindcss";\n@import "./subway-seat-auto.css";\n\n'
        "/* The same ss-* classes, in Enamel while the system is light and Walnut while it's dark */",
        "lang": "css",
    },
    "notes": "Tailwind v4 theme files add ss-* colors (bg-ss-base, text-ss-orange, bg-ss-diff-add) for one flavor, "
    "and subway-seat-auto.css switches the same names between Enamel and Walnut with the system. "
    "For v3, subway-seat-preset.js has all three as ss-walnut-*, ss-tunnel-* and ss-enamel-*.",
}


def tokens(f):
    """Color name → hex: every role, then the diff tints."""
    return {kebab(r): f.colors[r] for r in p.ROLES} | diff_tokens(f)


def theme_css(f):
    lines = "\n".join(f"  --color-ss-{name}: {value};" for name, value in tokens(f).items())
    return f"/* {HEADER} */\n/* {f.name} for Tailwind v4: bg-ss-base, text-ss-text, … */\n\n@theme {{\n{lines}\n}}\n"


def auto_css(light, dark):
    theme = "\n".join(f"  --color-ss-{name}: {value};" for name, value in tokens(light).items())
    night = "\n".join(f"    --color-ss-{name}: {value};" for name, value in tokens(dark).items())
    return (
        f"/* {HEADER} */\n/* Subway Seat for Tailwind v4, following the system: {light.name} when it's light, "
        f"{dark.name} when it's dark.\n   The utilities read these variables, so bg-ss-base and the rest switch "
        "with it. */\n\n"
        f"@theme {{\n{theme}\n}}\n\n@media (prefers-color-scheme: dark) {{\n  :root {{\n{night}\n  }}\n}}\n"
    )


def preset(flavors):
    colors = {"ss": {f.id: tokens(f) for f in flavors}}
    body = json.dumps({"theme": {"extend": {"colors": colors}}}, indent=2)
    return (
        f"// {HEADER}\n// Tailwind v3 preset: presets: [require(\"./subway-seat-preset.js\")]\n"
        f"// Classes: bg-ss-walnut-base, text-ss-enamel-orange, bg-ss-tunnel-diff-add, …\n\nmodule.exports = {body};\n"
    )


def build(flavors):
    by = {f.id: f for f in flavors}
    how = "in your project, next to your main CSS file"
    outs = [Out(f"{f.slug}.css", theme_css(f), flavor=f.id, dest=f"src/{f.slug}.css", lang="css", how=how)
            for f in flavors]
    outs.append(Out("subway-seat-auto.css", auto_css(by["enamel"], by["walnut"]), dest="src/subway-seat-auto.css",
                    lang="css", how=how))
    outs.append(Out("subway-seat-preset.js", preset(flavors), dest="./subway-seat-preset.js", lang="js",
                    how="at your project root, next to tailwind.config.js (Tailwind v3)"))
    return outs
