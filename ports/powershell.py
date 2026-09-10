"""PowerShell: PSReadLine token colors plus $PSStyle (PowerShell 7.2+), as a script to dot-source."""

import palette as p
from ports._lib import HEADER, Out, selection

META = {
    "id": "powershell",
    "name": "PowerShell",
    "category": "Shell & prompt",
    "homepage": "https://learn.microsoft.com/powershell/",
    "detect": ["pwsh"],
    "requires": "PSReadLine 2.0+",
    "enable": {
        "where": "your profile ($PROFILE: ~/.config/powershell/Microsoft.PowerShell_profile.ps1 on macOS "
        "and Linux, Documents\\PowerShell\\ on Windows)",
        "code": '. "$PSScriptRoot/{slug}.ps1"',
        "lang": "powershell",
        "file": "~/.config/powershell/Microsoft.PowerShell_profile.ps1",
    },
    "auto": {
        "where": "your profile, instead of the line above (picks a flavor from the system appearance when "
        "PowerShell starts; Linux stays dark)",
        "code": "$dark = $true\n"
        "if ($IsMacOS) { $dark = (defaults read -g AppleInterfaceStyle 2>$null) -eq 'Dark' }\n"
        "elseif ($IsWindows -or $PSVersionTable.PSEdition -eq 'Desktop') {\n"
        "    $dark = (Get-ItemPropertyValue 'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize' "
        "AppsUseLightTheme -ErrorAction Ignore) -ne 1\n"
        "}\n"
        ". \"$PSScriptRoot/$(if ($dark) { 'subway-seat' } else { 'subway-seat-enamel' }).ps1\"",
        "lang": "powershell",
        "file": "~/.config/powershell/Microsoft.PowerShell_profile.ps1",
    },
    "notes": "Command-line colors in PSReadLine, the same as the fish port: gold commands, orange keywords "
    "and pipes, sage parameters and types, avocado strings, terracotta variables. On PowerShell 7.2+ it also "
    "sets $PSStyle, so tables, errors, progress bars and Get-ChildItem listings (gold directories) match. "
    "Keys an older PSReadLine doesn't know are skipped. The terminal's own colors come from your terminal's port.",
}


def sgr(color=None, bg=None, *attrs):
    """A truecolor escape as PowerShell source: "${esc}[1;38;2;243;191;69m"."""
    codes = [{"bold": "1", "italic": "3", "underline": "4"}[a] for a in attrs]
    if color:
        codes.append("38;2;" + ";".join(str(v) for v in p.hex_to_rgb(color)))
    if bg:
        codes.append("48;2;" + ";".join(str(v) for v in p.hex_to_rgb(bg)))
    return '"${esc}[' + ";".join(codes) + 'm"'


def readline(f):
    """PSReadLine -Colors keys → (escape, comment)."""
    return {
        "Default": (sgr(f.text), "text"),
        "Command": (sgr(f.yellow), "yellow"),
        "Parameter": (sgr(f.sage), "sage"),
        "String": (sgr(f.green), "green"),
        "Operator": (sgr(f.orange), "orange"),
        "Variable": (sgr(f.clay), "clay"),
        "Member": (sgr(f.subtext1), "subtext1"),
        "Number": (sgr(f.red_hi), "red_hi"),
        "Type": (sgr(f.sage), "sage"),
        "Keyword": (sgr(f.orange), "orange"),
        "Comment": (sgr(f.overlay1, None, "italic"), "overlay1, italic"),
        "Error": (sgr(f.red_hi), "red_hi"),
        "Emphasis": (sgr(f.yellow, None, "bold"), "yellow, bold: search matches"),
        "Selection": (sgr(f.text_hi, selection(f), "bold"), "text_hi on the selection ground"),
        "ContinuationPrompt": (sgr(f.overlay1), "overlay1"),
        "InlinePrediction": (sgr(f.overlay0), "overlay0, like fish autosuggestions"),
        "ListPrediction": (sgr(f.orange), "orange: the > marker and source"),
        "ListPredictionSelected": (sgr(None, f.surface1), "surface1 ground"),
        "ListPredictionTooltip": (sgr(f.overlay1, None, "italic"), "overlay1, italic"),
    }


def formatting(f):
    return {
        "FormatAccent": sgr(f.yellow, None, "bold"),
        "TableHeader": sgr(f.yellow, None, "bold"),
        "CustomTableHeaderLabel": sgr(f.yellow, None, "bold", "italic"),
        "ErrorAccent": sgr(f.orange, None, "bold"),
        "Error": sgr(f.red_hi, None, "bold"),
        "Warning": sgr(f.yellow, None, "bold"),
        "Verbose": sgr(f.denim),
        "Debug": sgr(f.sage),
        "FeedbackName": sgr(f.orange),
        "FeedbackText": sgr(f.subtext1),
        "FeedbackAction": sgr(f.yellow),
    }


ARCHIVES = (".zip", ".tgz", ".gz", ".tar", ".nupkg", ".cab", ".7z")
SCRIPTS = (".ps1", ".psd1", ".psm1", ".ps1xml")


def quoted(names):
    return ", ".join(f"'{n}'" for n in names)


def script(f):
    width = max(len(k) for k in readline(f))
    vwidth = max(len(v) for v, _ in readline(f).values())
    rl = "\n".join(f"        {k:<{width}} = {v:<{vwidth}}  # {c}" for k, (v, c) in readline(f).items())
    fwidth = max(len(k) for k in formatting(f))
    fm = "\n".join(f"            {k:<{fwidth}} = {v}" for k, v in formatting(f).items())
    return f"""# {HEADER}
# {f.name} for PowerShell: PSReadLine token colors, and $PSStyle on PowerShell 7.2+.
# Dot-source it from your profile:  . "$PSScriptRoot/{f.slug}.ps1"
# Needs a terminal with 24-bit color (Windows Terminal, iTerm2, Ghostty, …).

& {{
    $esc = [char]27

    $colors = @{{
{rl}
    }}

    if (Get-Command Set-PSReadLineOption -ErrorAction Ignore) {{
        # Drop keys this PSReadLine doesn't have (2.0 lacks the prediction colors).
        $known = (Get-PSReadLineOption).PSObject.Properties.Name
        foreach ($key in @($colors.Keys)) {{
            $property = if ($key -eq 'Default') {{ 'DefaultTokenColor' }} else {{ "${{key}}Color" }}
            if ($property -notin $known) {{ $colors.Remove($key) }}
        }}
        Set-PSReadLineOption -Colors $colors
    }}

    if ($PSStyle) {{
        $formatting = @{{
{fm}
        }}
        foreach ($key in $formatting.Keys) {{
            if ($PSStyle.Formatting.PSObject.Properties[$key]) {{ $PSStyle.Formatting.$key = $formatting[$key] }}
        }}
        $PSStyle.Progress.Style = {sgr(f.yellow, None, "bold")}

        if ($PSStyle.PSObject.Properties['FileInfo']) {{
            $PSStyle.FileInfo.Directory = {sgr(f.yellow, None, "bold")}
            $PSStyle.FileInfo.SymbolicLink = {sgr(f.sage)}
            $PSStyle.FileInfo.Executable = {sgr(f.green, None, "bold")}
            foreach ($ext in {quoted(ARCHIVES)}) {{ $PSStyle.FileInfo.Extension[$ext] = {sgr(f.red_hi)} }}
            foreach ($ext in {quoted(SCRIPTS)}) {{ $PSStyle.FileInfo.Extension[$ext] = {sgr(f.sage)} }}
        }}
    }}
}}
"""


def build(flavors):
    return [
        Out(
            f"{f.slug}.ps1",
            script(f),
            flavor=f.id,
            dest=f"~/.config/powershell/{f.slug}.ps1",
            lang="powershell",
            how="on Windows, put it next to $PROFILE (Documents\\PowerShell\\).",
        )
        for f in flavors
    ]
