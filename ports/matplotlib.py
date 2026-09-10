"""matplotlib: an .mplstyle per flavor."""

from ports._lib import HEADER, Out, h, solid

META = {
    "id": "matplotlib",
    "name": "matplotlib",
    "category": "Palettes",
    "homepage": "https://matplotlib.org",
    "requires": "matplotlib 3.4+",
    "enable": {
        "where": "your notebook or script",
        "code": 'import matplotlib.pyplot as plt\nplt.style.use("{slug}")',
        "lang": "python",
    },
    "notes": "Charts on the walnut (or enamel) ground with parchment labels, quiet grid lines, and a color "
    "cycle that alternates warm and cool so neighboring series stay apart: burnt orange, seafoam, harvest "
    "gold, denim, redbird, avocado, terracotta. Saved figures keep the ground color.",
}

# Series order: warm and cool alternate, and the two reds sit far apart.
CYCLE = ["orange", "sage", "yellow", "denim", "red_hi", "green", "clay"]


def style(f):
    ground = h(f.base)
    muted = h(f.subtext1)
    rc = {
        "figure.facecolor": ground,
        "figure.edgecolor": ground,
        "savefig.facecolor": ground,
        "savefig.edgecolor": ground,
        "axes.facecolor": ground,
        "axes.edgecolor": h(f.overlay0),
        "axes.labelcolor": muted,
        "axes.titlecolor": h(f.text_hi),
        "axes.prop_cycle": "cycler('color', [" + ", ".join(f"'{h(f.colors[r])}'" for r in CYCLE) + "])",
        "text.color": h(f.text),
        "xtick.color": h(f.overlay1),
        "ytick.color": h(f.overlay1),
        "xtick.labelcolor": h(f.subtext0),
        "ytick.labelcolor": h(f.subtext0),
        "grid.color": h(solid("text@L3", f)),
        "legend.facecolor": h(solid("paper", f)),
        "legend.edgecolor": h(solid("text@EDGE", f, over="paper")),
        "patch.facecolor": h(f.colors[CYCLE[0]]),
        "patch.edgecolor": ground,
        "hatch.color": h(f.subtext0),
        "boxplot.boxprops.color": muted,
        "boxplot.whiskerprops.color": muted,
        "boxplot.capprops.color": muted,
        "boxplot.flierprops.color": muted,
        "boxplot.flierprops.markeredgecolor": muted,
        "boxplot.medianprops.color": h(f.orange),
        "boxplot.meanprops.color": h(f.yellow),
        "boxplot.meanprops.markerfacecolor": h(f.yellow),
        "boxplot.meanprops.markeredgecolor": h(f.yellow),
    }
    lines = [f"# {HEADER}", f"# {f.name} for matplotlib. Colors are hex without the leading #, as rc files expect."]
    lines += [f"{k}: {v}" for k, v in rc.items()]
    return "\n".join(lines) + "\n"


def build(flavors):
    return [
        Out(
            f"{f.slug}.mplstyle",
            style(f),
            flavor=f.id,
            lang="conf",
            dest=f"~/.matplotlib/stylelib/{f.slug}.mplstyle",
            how="that's the macOS folder; on Linux use ~/.config/matplotlib/stylelib/ "
            "(matplotlib.get_configdir() prints yours), or pass the file's path to plt.style.use",
        )
        for f in flavors
    ]
