import json

from ports._lib import Out
from ports.vscode import theme

META = {
    "id": "shiki",
    "name": "Shiki",
    "category": "Palettes",
    "homepage": "https://shiki.style",
    "enable": {
        "where": "your build script (Astro, VitePress, Next.js and others take the same theme object)",
        "code": 'import {{ codeToHtml }} from "shiki";\nimport theme from "./themes/{slug}.json" with {{ type: "json" }};\n\n'
        'const html = await codeToHtml(code, {{ lang: "ts", theme }});',
        "lang": "typescript",
    },
    "auto": {
        "where": "your build script, plus `color-scheme: light dark` on the page",
        "code": 'import { codeToHtml } from "shiki";\n'
        'import light from "./themes/subway-seat-enamel.json" with { type: "json" };\n'
        'import dark from "./themes/subway-seat.json" with { type: "json" };\n\n'
        "// light-dark() (Shiki 3.5+) picks a color from the page's color-scheme\n"
        'const html = await codeToHtml(code, { lang: "ts", themes: { light, dark }, defaultColor: "light-dark()" });',
        "lang": "typescript",
    },
    "notes": "The VS Code theme repackaged for Shiki: the same TextMate token colors as the editor. "
    "Shiki doesn't run a language server, so the extra coloring VS Code adds from semantic tokens isn't there.",
}


def shiki(f):
    t = theme(f)
    del t["$schema"]
    return {**t, "name": f.slug, "displayName": f.name}


def build(flavors):
    return [
        Out(f"{f.slug}.json", json.dumps(shiki(f), indent=2) + "\n", flavor=f.id, lang="json",
            dest=f"themes/{f.slug}.json", how="in your project")
        for f in flavors
    ]
