import json

import palette as p
from ports._lib import HEADER, Out
from ports._palettes import kebab

META = {
    "id": "tailwind",
    "name": "Tailwind CSS",
    "category": "Palettes",
    "homepage": "https://tailwindcss.com",
    "enable": {
        "where": "your main CSS file (Tailwind v4)",
        "code": '@import "tailwindcss";\n@import "./{slug}.css";\n\n/* bg-ss-base text-ss-text border-ss-surface1 text-ss-orange */',
        "lang": "css",
    },
    "notes": "Tailwind v4 theme files add ss-* colours (bg-ss-base, text-ss-orange) for one flavor. "
    "For v3, subway-seat-preset.js has all three as ss-walnut-*, ss-tunnel-* and ss-enamel-*.",
}


def theme_css(f):
    lines = "\n".join(f"  --color-ss-{kebab(r)}: {f.colors[r]};" for r in p.ROLES)
    return f"/* {HEADER} */\n/* {f.name} for Tailwind v4: bg-ss-base, text-ss-text, … */\n\n@theme {{\n{lines}\n}}\n"


def preset(flavors):
    colors = {"ss": {f.id: {kebab(r): f.colors[r] for r in p.ROLES} for f in flavors}}
    body = json.dumps({"theme": {"extend": {"colors": colors}}}, indent=2)
    return (
        f"// {HEADER}\n// Tailwind v3 preset: presets: [require(\"./subway-seat-preset.js\")]\n"
        f"// Classes: bg-ss-walnut-base, text-ss-enamel-orange, …\n\nmodule.exports = {body};\n"
    )


def build(flavors):
    outs = [
        Out(f"{f.slug}.css", theme_css(f), flavor=f.id, dest="next to your main CSS file", lang="css")
        for f in flavors
    ]
    outs.append(Out("subway-seat-preset.js", preset(flavors), dest="your project root, next to tailwind.config.js",
                    lang="js"))
    return outs
