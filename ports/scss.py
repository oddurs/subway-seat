import palette as p
from ports._lib import HEADER, Out
from ports._palettes import diff_tokens, kebab, role_name

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
    "notes": "A $ss-* variable for every role and for the diff tints ($ss-diff-add, $ss-diff-del-emph, …), "
    "and a $subway-seat map of the same. The names match across flavors, so switching is a one-word change "
    "to the @use.",
}


def partial(f):
    tokens = {kebab(r): (f.colors[r], role_name(f, r)) for r in p.ROLES}
    tokens |= {name: (value, None) for name, value in diff_tokens(f).items()}
    width = max(map(len, tokens))
    variables = "\n".join(
        f"${'ss-' + name + ':':<{width + 4}} {value};" + (f" // {comment}" if comment else "")
        for name, (value, comment) in tokens.items()
    )
    entries = ",\n".join(f'  "{name}": $ss-{name}' for name in tokens)
    return (
        f"// {HEADER}\n// {f.name}: {f.blurb}\n// Diff grounds: -add/-del/-chg for lines, -emph for changed words, "
        f"-dim for faded diffs.\n\n{variables}\n\n$subway-seat: (\n{entries},\n);\n"
    )


def build(flavors):
    return [
        Out(f"_{f.slug}.scss", partial(f), flavor=f.id, dest=f"styles/_{f.slug}.scss", lang="scss",
            how="in your project, on your Sass load path")
        for f in flavors
    ]
