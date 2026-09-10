from ports._lib import HEADER, Out, ink

META = {
    "id": "zsh-syntax-highlighting",
    "name": "zsh-syntax-highlighting",
    "category": "Shell & prompt",
    "homepage": "https://github.com/zsh-users/zsh-syntax-highlighting",
    "enable": {
        "where": "~/.zshrc, before or after zsh-syntax-highlighting is loaded (the end is fine)",
        "code": "source ~/.config/zsh/{slug}.zsh",
        "lang": "sh",
        "file": "~/.zshrc",
    },
    "detect": [
        "/opt/homebrew/share/zsh-syntax-highlighting",
        "/usr/local/share/zsh-syntax-highlighting",
        "/usr/share/zsh-syntax-highlighting",
        "/usr/share/zsh/plugins/zsh-syntax-highlighting",
        "~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting",
    ],
    "notes": "The same command-line colors as the fish port: gold commands, orange keywords and "
    "separators, sage options, avocado strings, terracotta expansions and redirections. It also "
    "colors zsh-autosuggestions' suggestions to match fish's.",
}


def fg(color, *attrs):
    return ",".join([f"fg={color}", *attrs])


def styles(f):
    cmd, kw, opt, string, special = f.yellow, f.orange, f.sage, f.green, f.clay
    return [
        ("General", {
            "default": fg(f.text),
            "unknown-token": fg(f.red_hi),
            "comment": fg(f.overlay1, "italic"),
        }),
        ("Commands", {
            "reserved-word": fg(kw),
            "alias": fg(cmd),
            "suffix-alias": fg(cmd),
            "global-alias": fg(cmd),
            "builtin": fg(cmd),
            "function": fg(cmd),
            "command": fg(cmd),
            "hashed-command": fg(cmd),
            "precommand": fg(cmd, "italic"),
            "autodirectory": fg(cmd, "italic"),
            "arg0": fg(cmd),
        }),
        ("Separators and redirection", {
            "commandseparator": fg(kw),
            "redirection": fg(special),
            "named-fd": fg(special),
            "numeric-fd": fg(special),
        }),
        ("Arguments and options", {
            "single-hyphen-option": fg(opt),
            "double-hyphen-option": fg(opt),
            "assign": fg(f.text),
            "path": fg(f.subtext1, "underline"),
            "path_pathseparator": fg(f.overlay2, "underline"),
            "path_prefix": fg(f.subtext1, "underline"),
            "path_prefix_pathseparator": fg(f.overlay2, "underline"),
            "globbing": fg(special),
            "history-expansion": fg(special),
            "arithmetic-expansion": fg(f.red_hi),
        }),
        ("Strings", {
            "single-quoted-argument": fg(string),
            "single-quoted-argument-unclosed": fg(f.red_hi),
            "double-quoted-argument": fg(string),
            "double-quoted-argument-unclosed": fg(f.red_hi),
            "dollar-quoted-argument": fg(string),
            "dollar-quoted-argument-unclosed": fg(f.red_hi),
            "rc-quote": fg(special),
            "dollar-double-quoted-argument": fg(special),
            "back-double-quoted-argument": fg(special),
            "back-dollar-quoted-argument": fg(special),
        }),
        ("Substitutions", {
            "command-substitution": "none",
            "command-substitution-unquoted": "none",
            "command-substitution-quoted": fg(string),
            "command-substitution-delimiter": fg(special),
            "command-substitution-delimiter-unquoted": fg(special),
            "command-substitution-delimiter-quoted": fg(special),
            "process-substitution": "none",
            "process-substitution-delimiter": fg(special),
            "back-quoted-argument": "none",
            "back-quoted-argument-unclosed": fg(f.red_hi),
            "back-quoted-argument-delimiter": fg(special),
        }),
        ("brackets and cursor highlighters (only used if enabled in ZSH_HIGHLIGHT_HIGHLIGHTERS)", {
            "bracket-error": fg(f.red_hi, "bold"),
            "bracket-level-1": fg(f.yellow),
            "bracket-level-2": fg(f.orange),
            "bracket-level-3": fg(f.green),
            "bracket-level-4": fg(f.sage),
            "cursor-matchingbracket": fg(f.yellow_hi, "bold"),
            "cursor": f"fg={ink(f)},bg={f.yellow if f.dark else f.orange}",
        }),
    ]


def body(f):
    out = [f"# {HEADER}", f"# {f.name} for zsh-syntax-highlighting. Needs a truecolor terminal.",
           "", "typeset -gA ZSH_HIGHLIGHT_STYLES"]
    for title, keys in styles(f):
        out += ["", f"# {title}"]
        out += [f"ZSH_HIGHLIGHT_STYLES[{k}]='{v}'" for k, v in keys.items()]
    out += ["", "# zsh-autosuggestions (fish's autosuggestion color)",
            f"ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg={f.overlay1}'"]
    return "\n".join(out) + "\n"


def build(flavors):
    return [
        Out(f"{f.slug}.zsh", body(f), flavor=f.id, dest=f"~/.config/zsh/{f.slug}.zsh", lang="sh")
        for f in flavors
    ]
