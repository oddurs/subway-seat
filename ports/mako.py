"""mako: a config per flavor with urgency criteria, pulled in with `include=` (mako 1.10+)."""

from ports._desktop import roles
from ports._lib import HEADER, Out

META = {
    "id": "mako",
    "name": "mako",
    "category": "Desktop",
    "homepage": "https://github.com/emersion/mako",
    "requires": "mako 1.10+",
    "detect": ["mako", "makoctl"],
    "enable": {
        "where": "~/.config/mako/config, at the top before any [section], then `makoctl reload`",
        "code": "include=~/.config/mako/{slug}.conf",
        "lang": "ini",
    },
    "notes": "Notifications on the raised paper ground. Low urgency is quiet, normal has a denim border, "
    "critical an orange one, and progress fills in behind the text as a wash that keeps it readable. "
    "Settings after the `include=` line still win. Before mako 1.10, paste the file's contents instead.",
}


def conf(f):
    r = roles(f)
    lines = [
        f"# {HEADER}",
        f"# {f.name} for mako",
        "",
        f"background-color={r['paper']}",
        f"text-color={r['text']}",
        f"border-color={r['info']}",
        f"progress-color=over {r['selection']}",
        "",
        "[urgency=low]",
        f"text-color={r['muted']}",
        f"border-color={r['edge']}",
        "",
        "[urgency=critical]",
        f"text-color={r['strong']}",
        f"border-color={r['urgent']}",
        "",
    ]
    return "\n".join(lines)


def build(flavors):
    return [
        Out(f"{f.slug}.conf", conf(f), flavor=f.id, dest=f"~/.config/mako/{f.slug}.conf", lang="ini") for f in flavors
    ]
