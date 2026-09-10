import json

import palette as p
from ports._lib import ANSI_NAMES, REPO, Out, rgb
from ports._palettes import diff_tokens, hsl, kebab, role_name

META = {
    "id": "json",
    "name": "Palette JSON",
    "category": "Palettes",
    "homepage": REPO,
    "enable": {
        "where": "any script or tool that reads JSON",
        "code": "jq -r '.flavors.{id}.colors.orange.hex' subway-seat.json",
        "lang": "sh",
    },
    "notes": "The whole palette as data: every flavor and role in hex, RGB and HSL, with names, uses, ANSI order, "
    "diff tints and syntax roles. subway-seat.tokens.json is the same in W3C design-token form for Tokens Studio "
    "and Style Dictionary.",
}

ANSI = [*ANSI_NAMES, *(f"bright_{n}" for n in ANSI_NAMES)]
GROUP = {**dict.fromkeys(p.GROUND, "ground"), **dict.fromkeys(p.TEXT, "text"), **dict.fromkeys(p.ACCENTS, "accent")}


def palette(flavors):
    return {
        "name": "Subway Seat",
        "homepage": REPO,
        "roles": [
            {"id": r, "name": p.ROLE_NAMES[r], "group": GROUP[r], "use": p.ROLE_USES[r]}
            for r in p.ROLES
        ],
        "flavors": {
            f.id: {
                "name": f.name,
                "slug": f.slug,
                "dark": f.dark,
                "blurb": f.blurb,
                "colors": {
                    r: {"name": role_name(f, r), "hex": f.colors[r], "rgb": list(rgb(f.colors[r])), "hsl": list(hsl(f.colors[r]))}
                    for r in p.ROLES
                },
                "ansi": [
                    {"index": i, "name": ANSI[i], "role": r, "hex": f.colors[r]}
                    for i, r in enumerate(f.ansi_roles)
                ],
                # Line (-add/-del/-chg), word (-emph) and faded (-dim) grounds for diffs
                "diff": diff_tokens(f),
            }
            for f in flavors
        },
        "syntax": {role: {"role": c, "styles": sorted(st)} for role, (c, st) in p.SYNTAX.items()},
    }


def tokens(flavors):
    """W3C design tokens (DTCG): one top-level group per flavor, which Tokens Studio reads as token sets."""
    return {
        f.id: {
            **{kebab(r): {"$type": "color", "$value": f.colors[r], "$description": role_name(f, r)} for r in p.ROLES},
            "diff": {
                name.removeprefix("diff-"): {"$type": "color", "$value": value}
                for name, value in diff_tokens(f).items()
            },
        }
        for f in flavors
    }


def build(flavors):
    return [
        Out("subway-seat.json", json.dumps(palette(flavors), indent=2, ensure_ascii=False) + "\n", lang="json",
            how="read it from any script or tool"),
        Out("subway-seat.tokens.json", json.dumps(tokens(flavors), indent=2, ensure_ascii=False) + "\n", lang="json",
            dest="tokens/subway-seat.tokens.json",
            how="in your project, as a Style Dictionary source; Tokens Studio loads it with Load from file"),
    ]
