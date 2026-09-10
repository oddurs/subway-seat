"""Hyprland: a Lua palette module (0.55+) and a hyprlang palette for older versions.

Both carry every role as `rgb(RRGGBB)` plus the bare hex for building `rgba()`, the
convention Catppuccin's port uses, and the colors for window borders, groups and the
groupbar: gold on the focused window, orange on locked groups, terracotta where a
window can't join a group. The Lua module only changes the config when you call
`.apply()`; the .conf applies its blocks when sourced.
"""

import palette as p
from ports._desktop import bare, roles
from ports._lib import HEADER, Out, resolve

META = {
    "id": "hyprland",
    "name": "Hyprland",
    "category": "Desktop",
    "homepage": "https://hypr.land",
    "detect": ["Hyprland", "hyprctl"],
    "enable": {
        "where": "~/.config/hypr/hyprland.lua (Hyprland 0.55+)",
        "code": 'require("themes.{slug}").apply()',
        "lang": "lua",
        "file": "~/.config/hypr/hyprland.lua",
    },
    "notes": "Window borders, group borders, the groupbar, the shadow and the no-wallpaper background. "
    "Hyprland 0.55 moved to Lua: `require` the module for the palette and call `.apply()` for the "
    "borders. The `.conf` is the same palette for hyprland.conf on 0.54 and older.",
}


def hypr(color):
    """#RRGGBB → rgb(RRGGBB); #RRGGBBAA → rgba(RRGGBBAA)."""
    return f"rgba({bare(color)})" if len(color) == 9 else f"rgb({bare(color)})"


def settings(f):
    """(section path, key, value) for everything the theme sets."""
    r = roles(f)
    faded = {name: f.mix(name, "surface1", 0.4) for name in ("yellow", "orange", "clay")}
    return [
        ("general.col", "active_border", hypr(r["focus"])),
        ("general.col", "inactive_border", hypr(r["inactive"])),
        ("general.col", "nogroup_border", hypr(faded["clay"])),
        ("general.col", "nogroup_border_active", hypr(f.clay)),
        ("group.col", "border_active", hypr(r["focus"])),
        ("group.col", "border_inactive", hypr(faded["yellow"])),
        ("group.col", "border_locked_active", hypr(f.orange)),
        ("group.col", "border_locked_inactive", hypr(faded["orange"])),
        ("group.groupbar", "text_color", hypr(r["strong"])),
        ("group.groupbar", "text_color_inactive", hypr(f.subtext0)),
        ("group.groupbar.col", "active", hypr(r["focus"])),
        ("group.groupbar.col", "inactive", hypr(f.surface2 if f.dark else f.surface1)),
        ("group.groupbar.col", "locked_active", hypr(f.orange)),
        ("group.groupbar.col", "locked_inactive", hypr(faded["orange"])),
        ("decoration.shadow", "color", hypr(resolve("shadow@60" if f.dark else "shadow@14", f))),
        ("misc", "background_color", hypr(f.base)),
    ]


def tree(f, legacy=False):
    """The settings nested the way hl.config's table (and hyprlang's categories) nest them.
    `legacy` leaves out what hyprland.conf only gained in 0.50, so the .conf loads from 0.45."""
    root = {}
    for path, key, value in settings(f):
        if legacy and key.startswith("text_color_"):
            continue
        node = root
        for part in path.split("."):
            node = node.setdefault(part, {})
        node[key] = value
    return root


def lua(f):
    lines = [
        f"-- {HEADER}",
        f"-- {f.name} for Hyprland 0.55+.",
        "--",
        f'--   local colors = require("themes.{f.slug}")   -- the palette',
        "--   colors.apply()                                   -- borders, groups, groupbar",
        "--",
        "local M = {}",
        "",
    ]
    for role in p.ROLES:
        lines += [f"M.{role} = '{hypr(f.colors[role])}'", f"M.{role}Alpha = '{bare(f.colors[role])}'", ""]

    def emit(node, depth):
        pad = "  " * depth
        out = []
        for k, v in node.items():
            out += (
                [f"{pad}{k} = {{", *emit(v, depth + 1), f"{pad}}},"] if isinstance(v, dict) else [f"{pad}{k} = '{v}',"]
            )
        return out

    lines += ["function M.apply()", "  hl.config({", *emit(tree(f), 2), "  })", "end", "", "return M", ""]
    return "\n".join(lines)


def conf(f):
    lines = [f"# {HEADER}", f"# {f.name} for hyprland.conf (Hyprland 0.54 and older).", "", "# The palette"]
    for role in p.ROLES:
        lines += [f"${role} = {hypr(f.colors[role])}", f"${role}Alpha = {bare(f.colors[role])}", ""]

    def emit(node, depth, prefix=""):
        pad = "    " * depth
        out = []
        for k, v in node.items():
            if isinstance(v, dict) and k == "col":  # `col.` is part of the key in hyprlang, not a category
                out += emit(v, depth, "col.")
            elif isinstance(v, dict):
                out += [f"{pad}{k} {{", *emit(v, depth + 1), f"{pad}}}"]
            else:
                out.append(f"{pad}{prefix}{k} = {v}")
        return out

    lines.append("# The theme: delete the blocks below to keep only the variables")
    for k, v in tree(f, legacy=True).items():
        lines += [*emit({k: v}, 0), ""]
    return "\n".join(lines)


def build(flavors):
    outs = []
    for f in flavors:
        outs.append(Out(f"{f.slug}.lua", lua(f), flavor=f.id, dest=f"~/.config/hypr/themes/{f.slug}.lua", lang="lua"))
        outs.append(
            Out(
                f"{f.slug}.conf",
                conf(f),
                flavor=f.id,
                dest=f"~/.config/hypr/{f.slug}.conf",
                lang="conf",
                how=f"Hyprland 0.54 or older: add `source = ~/.config/hypr/{f.slug}.conf` near the top of hyprland.conf",
            )
        )
    return outs
