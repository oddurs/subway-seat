"""dunst: a drop-in per flavor with the three urgency sections (dunst 1.8+)."""

from ports._desktop import roles
from ports._lib import HEADER, Out

META = {
    "id": "dunst",
    "name": "dunst",
    "category": "Desktop",
    "homepage": "https://dunst-project.org",
    "requires": "dunst 1.8+",
    "detect": ["dunst"],
    "enable": {
        "where": "a shell (dunst 1.12+ reloads; older versions restart)",
        "code": "dunstctl reload   # or: killall dunst",
        "lang": "sh",
    },
    "notes": "Notifications on the raised paper ground. Low urgency is quiet, normal has a denim frame "
    "and a gold progress bar, critical has an orange frame. It's a drop-in, which dunst only reads "
    "next to a dunstrc of your own: if `~/.config/dunst/dunstrc` doesn't exist, copy `/etc/xdg/dunst/dunstrc` there.",
}


def sections(f):
    r = roles(f)
    return {
        "urgency_low": {
            "background": r["paper"],
            "foreground": r["muted"],
            "frame_color": r["edge"],
            "highlight": r["faint"],
        },
        "urgency_normal": {
            "background": r["paper"],
            "foreground": r["text"],
            "frame_color": r["info"],
            "highlight": r["focus"],
        },
        "urgency_critical": {
            "background": r["paper"],
            "foreground": r["strong"],
            "frame_color": r["urgent"],
            "highlight": r["urgent"],
        },
    }


def conf(f):
    out = [f"# {HEADER}", f"# {f.name} for dunst"]
    for name, keys in sections(f).items():
        out += ["", f"[{name}]", *(f'{k} = "{v}"' for k, v in keys.items())]
    return "\n".join(out) + "\n"


def build(flavors):
    return [
        Out(f"{f.slug}.conf", conf(f), flavor=f.id, dest=f"~/.config/dunst/dunstrc.d/{f.slug}.conf", lang="ini")
        for f in flavors
    ]
