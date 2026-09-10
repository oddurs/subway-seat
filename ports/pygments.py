from ports._lib import HEADER, Out
from ports._palettes import token_styles

META = {
    "id": "pygments",
    "name": "Pygments",
    "category": "Palettes",
    "homepage": "https://pygments.org",
    "enable": {
        "where": "any Python code, with the file on your PYTHONPATH",
        "code": "from pygments.formatters import HtmlFormatter\nfrom {snake} import style\n\n"
        'print(HtmlFormatter(style=style).get_style_defs(".highlight"))',
        "lang": "python",
    },
    "notes": "A Pygments Style class per flavor, for Sphinx, MkDocs, Jupyter or your own HTML and terminal output. "
    "`package/` installs them by name (`subway-seat`, `-tunnel`, `-enamel`), which is how Aider picks up its code theme.",
}


def class_name(f):
    return f.name.replace(" ", "") + "Style"


def module(f):
    styles = "\n".join(f'        Token.{path}: "{s}",' for path, s in token_styles(f))
    return f'''# {HEADER}
"""{f.name} — a Pygments style. {f.blurb}"""

from pygments.style import Style
from pygments.token import Token

__all__ = ["{class_name(f)}", "style"]


class {class_name(f)}(Style):
    name = "{f.slug}"
    background_color = "{f.base}"
    highlight_color = "{f.surface0 if f.dark else f.mantle}"
    line_number_color = "{f.overlay0}"
    line_number_background_color = "{f.base}"
    line_number_special_color = "{f.yellow if f.dark else f.orange}"
    line_number_special_background_color = "{f.surface0 if f.dark else f.mantle}"

    styles = {{
        Token: "{f.text}",
{styles}
    }}


style = {class_name(f)}
'''


PACKAGE_URL = "git+https://github.com/oddurs/subway-seat#subdirectory=dist/pygments/package"


def pyproject(flavors):
    from ports.vscode import VERSION

    points = "\n".join(f'{f.slug} = "subway_seat_pygments.{f.snake}:{class_name(f)}"' for f in flavors)
    return f"""# {HEADER}
[project]
name = "subway-seat-pygments"
version = "{VERSION}"
description = "Subway Seat styles for Pygments, so Aider, Sphinx, MkDocs and IPython can use them by name."
readme = "README.md"
license = "MIT"
requires-python = ">=3.9"
dependencies = ["pygments>=2.10"]

[project.urls]
Homepage = "https://github.com/oddurs/subway-seat"

[project.entry-points."pygments.styles"]
{points}

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["subway_seat_pygments"]
"""


def build(flavors):
    outs = [
        Out(f"{f.snake}.py", module(f), flavor=f.id, dest=f"your PYTHONPATH, e.g. docs/_ext/{f.snake}.py", lang="python")
        for f in flavors
    ]
    # The same styles as an installable package, registered by name.
    outs.append(Out("package/pyproject.toml", pyproject(flavors), dest=f"pip install '{PACKAGE_URL}'", lang="toml"))
    outs.append(Out("package/README.md", "# subway-seat-pygments\n\nThe Subway Seat Pygments styles, registered as "
                    + ", ".join(f"`{f.slug}`" for f in flavors) + ".\n", lang="text"))
    outs.append(Out("package/subway_seat_pygments/__init__.py",
                    f"# {HEADER}\n" + "".join(f"from .{f.snake} import {class_name(f)}\n" for f in flavors), lang="python"))
    for f in flavors:
        outs.append(Out(f"package/subway_seat_pygments/{f.snake}.py", module(f), flavor=f.id, lang="python"))
    return outs
