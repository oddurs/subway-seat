import palette as p
from ports._lib import HEADER, Out
from ports._palettes import kebab

META = {
    "id": "scss",
    "name": "Sass",
    "category": "Palettes",
    "homepage": "https://sass-lang.com",
    "enable": {
        "where": "any stylesheet, with the partial on your load path",
        "code": '@use "sass:map";\n@use "{slug}" as *;\n\nbody {{\n  background: $ss-base;\n'
        '  color: map.get($subway-seat, "text");\n}}',
        "lang": "scss",
    },
    "notes": "A $ss-* variable for every role and a $subway-seat map of the same. "
    "The names match across flavors, so switching is a one-word change to the @use.",
}


def partial(f):
    width = max(len(kebab(r)) for r in p.ROLES)
    variables = "\n".join(
        f"${'ss-' + kebab(r) + ':':<{width + 4}} {f.colors[r]}; // {p.ROLE_NAMES[r]}" for r in p.ROLES
    )
    entries = ",\n".join(f'  "{kebab(r)}": $ss-{kebab(r)}' for r in p.ROLES)
    return (
        f"// {HEADER}\n// {f.name}: {f.blurb}\n\n{variables}\n\n$subway-seat: (\n{entries},\n);\n"
    )


def build(flavors):
    return [
        Out(f"_{f.slug}.scss", partial(f), flavor=f.id, dest=f"your Sass load path, e.g. styles/_{f.slug}.scss",
            lang="scss")
        for f in flavors
    ]
