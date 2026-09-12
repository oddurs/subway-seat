# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# Paris Guimard for PowerShell: PSReadLine token colors, and $PSStyle on PowerShell 7.2+.
# Dot-source it from your profile:  . "$PSScriptRoot/paris-guimard.ps1"
# Needs a terminal with 24-bit color (Windows Terminal, iTerm2, Ghostty, …).

& {
    $esc = [char]27

    $colors = @{
        Default                = "${esc}[38;2;217;225;219m"                  # text
        Command                = "${esc}[38;2;235;193;104m"                  # yellow
        Parameter              = "${esc}[38;2;108;160;135m"                  # sage
        String                 = "${esc}[38;2;128;194;142m"                  # green
        Operator               = "${esc}[38;2;208;145;79m"                   # orange
        Variable               = "${esc}[38;2;206;150;180m"                  # clay
        Member                 = "${esc}[38;2;194;203;197m"                  # subtext1
        Number                 = "${esc}[38;2;225;131;122m"                  # red_hi
        Type                   = "${esc}[38;2;108;160;135m"                  # sage
        Keyword                = "${esc}[38;2;208;145;79m"                   # orange
        Comment                = "${esc}[3;38;2;116;133;124m"                # overlay1, italic
        Error                  = "${esc}[38;2;225;131;122m"                  # red_hi
        Emphasis               = "${esc}[1;38;2;235;193;104m"                # yellow, bold: search matches
        Selection              = "${esc}[1;38;2;233;238;236;48;2;62;85;74m"  # text_hi on the selection ground
        ContinuationPrompt     = "${esc}[38;2;116;133;124m"                  # overlay1
        InlinePrediction       = "${esc}[38;2;88;107;97m"                    # overlay0, like fish autosuggestions
        ListPrediction         = "${esc}[38;2;208;145;79m"                   # orange: the > marker and source
        ListPredictionSelected = "${esc}[48;2;48;70;59m"                     # surface1 ground
        ListPredictionTooltip  = "${esc}[3;38;2;116;133;124m"                # overlay1, italic
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
            FormatAccent           = "${esc}[1;38;2;235;193;104m"
            TableHeader            = "${esc}[1;38;2;235;193;104m"
            CustomTableHeaderLabel = "${esc}[1;3;38;2;235;193;104m"
            ErrorAccent            = "${esc}[1;38;2;208;145;79m"
            Error                  = "${esc}[1;38;2;225;131;122m"
            Warning                = "${esc}[1;38;2;235;193;104m"
            Verbose                = "${esc}[38;2;112;155;200m"
            Debug                  = "${esc}[38;2;108;160;135m"
            FeedbackName           = "${esc}[38;2;208;145;79m"
            FeedbackText           = "${esc}[38;2;194;203;197m"
            FeedbackAction         = "${esc}[38;2;235;193;104m"
        }
        foreach ($key in $formatting.Keys) {
            if ($PSStyle.Formatting.PSObject.Properties[$key]) { $PSStyle.Formatting.$key = $formatting[$key] }
        }
        $PSStyle.Progress.Style = "${esc}[1;38;2;235;193;104m"

        if ($PSStyle.PSObject.Properties['FileInfo']) {
            $PSStyle.FileInfo.Directory = "${esc}[1;38;2;235;193;104m"
            $PSStyle.FileInfo.SymbolicLink = "${esc}[38;2;108;160;135m"
            $PSStyle.FileInfo.Executable = "${esc}[1;38;2;128;194;142m"
            foreach ($ext in '.zip', '.tgz', '.gz', '.tar', '.nupkg', '.cab', '.7z') { $PSStyle.FileInfo.Extension[$ext] = "${esc}[38;2;225;131;122m" }
            foreach ($ext in '.ps1', '.psd1', '.psm1', '.ps1xml') { $PSStyle.FileInfo.Extension[$ext] = "${esc}[38;2;108;160;135m" }
        }
    }
}
