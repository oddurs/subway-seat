from ports._lib import HEADER, Out

META = {
    "id": "eza",
    "name": "eza",
    "category": "CLI & TUI",
    "homepage": "https://eza.rocks",
    "enable": {
        "where": "config.fish (bash and zsh: export it from ~/.bashrc or ~/.zshrc). Each flavor is a "
        "theme.yml in its own folder, so switching is changing this one line",
        "code": "set -gx EZA_CONFIG_DIR ~/.config/eza/{slug}",
        "lang": "fish",
        "sh": 'export EZA_CONFIG_DIR="$HOME/.config/eza/{slug}"',
        "file": "~/.config/fish/conf.d/subway-seat.fish",
    },
    "requires": "eza 0.20+",
    "detect": ["eza"],
    "notes": "Gold directories, avocado executables, sage symlinks, and file sizes that warm up from "
    "avocado to red as they grow. LS_COLORS and EZA_COLORS override it; the vivid port sets LS_COLORS "
    "to match.",
}


def s(fg=None, bg=None, **attrs):
    """An eza style as a YAML flow mapping."""
    parts = [f'foreground: "{fg}"'] if fg else []
    parts += [f'background: "{bg}"'] if bg else []
    parts += [f"is_{k}: true" for k, v in attrs.items() if v]
    return "{" + ", ".join(parts) + "}"


def theme(f):
    def dim(role):  # size units: the number's color, quieter (less so on Enamel, where it would fade out)
        return f.mix(role, "base", 0.7 if f.dark else 0.85)

    doc = {
        "colourful": "true",
        "filekinds": {
            "normal": s(f.text),
            "directory": s(f.yellow, bold=True),
            "symlink": s(f.sage),
            "pipe": s(f.clay),
            "block_device": s(f.orange_hi, bold=True),
            "char_device": s(f.orange_hi),
            "socket": s(f.clay, bold=True),
            "special": s(f.clay),
            "executable": s(f.green, bold=True),
            "mount_point": s(f.yellow_hi, bold=True, underline=True),
        },
        "perms": {
            "user_read": s(f.yellow, bold=True),
            "user_write": s(f.orange, bold=True),
            "user_execute_file": s(f.green, bold=True),
            "user_execute_other": s(f.green, bold=True),
            "group_read": s(f.yellow),
            "group_write": s(f.orange),
            "group_execute": s(f.green),
            "other_read": s(f.yellow),
            "other_write": s(f.orange),
            "other_execute": s(f.green),
            "special_user_file": s(f.clay),
            "special_other": s(f.overlay1),
            "attribute": s(f.overlay1),
        },
        "size": {
            "major": s(f.sage),
            "minor": s(f.sage_hi),
            "number_byte": s(f.subtext0),
            "number_kilo": s(f.green),
            "number_mega": s(f.yellow),
            "number_giga": s(f.orange),
            "number_huge": s(f.red_hi),
            "unit_byte": s(dim("subtext0")),
            "unit_kilo": s(dim("green")),
            "unit_mega": s(dim("yellow")),
            "unit_giga": s(dim("orange")),
            "unit_huge": s(dim("red_hi")),
        },
        "users": {
            "user_you": s(f.yellow),
            "user_root": s(f.red_hi),
            "user_other": s(f.subtext0),
            "group_yours": s(f.subtext1),
            "group_other": s(f.overlay2),
            "group_root": s(f.red_hi),
        },
        "links": {
            "normal": s(f.sage),
            "multi_link_file": s(f.orange),
        },
        "git": {
            "new": s(f.green),
            "modified": s(f.yellow),
            "deleted": s(f.red_hi),
            "renamed": s(f.sage),
            "typechange": s(f.clay),
            "ignored": s(f.overlay0),
            "conflicted": s(f.red, bold=True),
        },
        "git_repo": {
            "branch_main": s(f.subtext1),
            "branch_other": s(f.orange),
            "git_clean": s(f.green),
            "git_dirty": s(f.yellow),
        },
        "security_context": {
            "none": s(f.overlay1),
            "selinux": {
                "colon": s(f.overlay0),
                "user": s(f.subtext0),
                "role": s(f.sage),
                "typ": s(f.overlay2),
                "range": s(f.clay),
            },
        },
        "file_type": {
            "image": s(f.clay),
            "video": s(f.orange),
            "music": s(f.orange_hi),
            "lossless": s(f.orange_hi, bold=True),
            "crypto": s(f.red),
            "document": s(f.denim),
            "compressed": s(f.red_hi),
            "temp": s(f.overlay0),
            "compiled": s(f.overlay1),
            "build": s(f.yellow, underline=True),
            "source": s(f.sage),
        },
        "punctuation": s(f.overlay0),
        "date": s(f.subtext0),
        "inode": s(f.overlay1),
        "blocks": s(f.overlay1),
        "header": s(f.subtext1, underline=True),
        "octal": s(f.clay),
        "flags": s(f.overlay2),
        "symlink_path": s(f.subtext0),
        "control_char": s(f.clay),
        "broken_symlink": s(f.red_hi),
        "broken_path_overlay": s(underline=True),
        "filenames": {
            '"README.md"': f"{{filename: {s(f.yellow_hi, bold=True)}}}",
            '"README"': f"{{filename: {s(f.yellow_hi, bold=True)}}}",
            '"LICENSE"': f"{{filename: {s(f.overlay2)}}}",
        },
        "extensions": {
            "lock": f"{{filename: {s(f.overlay1)}}}",
            "log": f"{{filename: {s(f.overlay1)}}}",
        },
    }

    def emit(d, indent=0):
        lines = []
        for k, v in d.items():
            if isinstance(v, dict):
                lines.append(" " * indent + f"{k}:")
                lines += emit(v, indent + 2)
            else:
                lines.append(" " * indent + f"{k}: {v}")
        return lines

    return f"# {HEADER}\n# {f.name} for eza 0.20+.\n" + "\n".join(emit(doc)) + "\n"


def build(flavors):
    return [
        Out(f"{f.slug}.yml", theme(f), flavor=f.id, dest=f"~/.config/eza/{f.slug}/theme.yml", lang="yaml")
        for f in flavors
    ]
