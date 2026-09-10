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
        "code": 'import {{ codeToHtml }} from "shiki";\nimport theme from "./{slug}.json" with {{ type: "json" }};\n\n'
        'const html = await codeToHtml(code, {{ lang: "ts", theme }});',
        "lang": "typescript",
    },
    "notes": "The VS Code theme repackaged for Shiki, so highlighted code on the web matches the editor exactly.",
}


def shiki(f):
    t = theme(f)
    del t["$schema"]
    return {**t, "name": f.slug, "displayName": f.name}


def build(flavors):
    return [
        Out(f"{f.slug}.json", json.dumps(shiki(f), indent=2) + "\n", flavor=f.id,
            dest=f"your project, e.g. themes/{f.slug}.json", lang="json")
        for f in flavors
    ]
