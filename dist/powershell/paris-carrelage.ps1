# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# Paris Carrelage for PowerShell: PSReadLine token colors, and $PSStyle on PowerShell 7.2+.
# Dot-source it from your profile:  . "$PSScriptRoot/paris-carrelage.ps1"
# Needs a terminal with 24-bit color (Windows Terminal, iTerm2, Ghostty, …).

& {
    $esc = [char]27

    $colors = @{
        Default                = "${esc}[38;2;39;52;47m"                     # text
        Command                = "${esc}[38;2;145;109;7m"                    # yellow
        Parameter              = "${esc}[38;2;0;98;103m"                     # sage
        String                 = "${esc}[38;2;33;131;102m"                   # green
        Operator               = "${esc}[38;2;118;76;0m"                     # orange
        Variable               = "${esc}[38;2;179;107;81m"                   # clay
        Member                 = "${esc}[38;2;59;71;66m"                     # subtext1
        Number                 = "${esc}[38;2;172;59;50m"                    # red_hi
        Type                   = "${esc}[38;2;0;98;103m"                     # sage
        Keyword                = "${esc}[38;2;118;76;0m"                     # orange
        Comment                = "${esc}[3;38;2;108;124;118m"                # overlay1, italic
        Error                  = "${esc}[38;2;172;59;50m"                    # red_hi
        Emphasis               = "${esc}[1;38;2;145;109;7m"                  # yellow, bold: search matches
        Selection              = "${esc}[1;38;2;25;34;30;48;2;176;191;187m"  # text_hi on the selection ground
        ContinuationPrompt     = "${esc}[38;2;108;124;118m"                  # overlay1
        InlinePrediction       = "${esc}[38;2;133;151;146m"                  # overlay0, like fish autosuggestions
        ListPrediction         = "${esc}[38;2;118;76;0m"                     # orange: the > marker and source
        ListPredictionSelected = "${esc}[48;2;176;191;187m"                  # surface1 ground
        ListPredictionTooltip  = "${esc}[3;38;2;108;124;118m"                # overlay1, italic
    }

    if (Get-Command Set-PSReadLineOption -ErrorAction Ignore) {
        # Drop keys this PSReadLine doesn't have (2.0 lacks the prediction colors).
        $known = (Get-PSReadLineOption).PSObject.Properties.Name
        foreach ($key in @($colors.Keys)) {
            $property = if ($key -eq 'Default') { 'DefaultTokenColor' } else { "${key}Color" }
            if ($property -notin $known) { $colors.Remove($key) }
        }
        Set-PSReadLineOption -Colors $colors
    }

    if ($PSStyle) {
        $formatting = @{
            FormatAccent           = "${esc}[1;38;2;145;109;7m"
            TableHeader            = "${esc}[1;38;2;145;109;7m"
            CustomTableHeaderLabel = "${esc}[1;3;38;2;145;109;7m"
            ErrorAccent            = "${esc}[1;38;2;118;76;0m"
            Error                  = "${esc}[1;38;2;172;59;50m"
            Warning                = "${esc}[1;38;2;145;109;7m"
            Verbose                = "${esc}[38;2;37;98;155m"
            Debug                  = "${esc}[38;2;0;98;103m"
            FeedbackName           = "${esc}[38;2;118;76;0m"
            FeedbackText           = "${esc}[38;2;59;71;66m"
            FeedbackAction         = "${esc}[38;2;145;109;7m"
        }
        foreach ($key in $formatting.Keys) {
            if ($PSStyle.Formatting.PSObject.Properties[$key]) { $PSStyle.Formatting.$key = $formatting[$key] }
        }
        $PSStyle.Progress.Style = "${esc}[1;38;2;145;109;7m"

        if ($PSStyle.PSObject.Properties['FileInfo']) {
            $PSStyle.FileInfo.Directory = "${esc}[1;38;2;145;109;7m"
            $PSStyle.FileInfo.SymbolicLink = "${esc}[38;2;0;98;103m"
            $PSStyle.FileInfo.Executable = "${esc}[1;38;2;33;131;102m"
            foreach ($ext in '.zip', '.tgz', '.gz', '.tar', '.nupkg', '.cab', '.7z') { $PSStyle.FileInfo.Extension[$ext] = "${esc}[38;2;172;59;50m" }
            foreach ($ext in '.ps1', '.psd1', '.psm1', '.ps1xml') { $PSStyle.FileInfo.Extension[$ext] = "${esc}[38;2;0;98;103m" }
        }
    }
}
