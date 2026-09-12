# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# Subway Seat Tunnel for PowerShell: PSReadLine token colors, and $PSStyle on PowerShell 7.2+.
# Dot-source it from your profile:  . "$PSScriptRoot/subway-seat-tunnel.ps1"
# Needs a terminal with 24-bit color (Windows Terminal, iTerm2, Ghostty, …).

& {
    $esc = [char]27

    $colors = @{
        Default                = "${esc}[38;2;233;216;182m"                  # text
        Command                = "${esc}[38;2;243;191;69m"                   # yellow
        Parameter              = "${esc}[38;2;134;173;149m"                  # sage
        String                 = "${esc}[38;2;173;185;86m"                   # green
        Operator               = "${esc}[38;2;236;127;49m"                   # orange
        Variable               = "${esc}[38;2;244;168;126m"                  # clay
        Member                 = "${esc}[38;2;214;195;160m"                  # subtext1
        Number                 = "${esc}[38;2;255;131;115m"                  # red_hi
        Type                   = "${esc}[38;2;134;173;149m"                  # sage
        Keyword                = "${esc}[38;2;236;127;49m"                   # orange
        Comment                = "${esc}[3;38;2;145;119;89m"                 # overlay1, italic
        Error                  = "${esc}[38;2;255;131;115m"                  # red_hi
        Emphasis               = "${esc}[1;38;2;243;191;69m"                 # yellow, bold: search matches
        Selection              = "${esc}[1;38;2;246;234;209;48;2;79;57;39m"  # text_hi on the selection ground
        ContinuationPrompt     = "${esc}[38;2;145;119;89m"                   # overlay1
        InlinePrediction       = "${esc}[38;2;116;91;69m"                    # overlay0, like fish autosuggestions
        ListPrediction         = "${esc}[38;2;236;127;49m"                   # orange: the > marker and source
        ListPredictionSelected = "${esc}[48;2;61;44;29m"                     # surface1 ground
        ListPredictionTooltip  = "${esc}[3;38;2;145;119;89m"                 # overlay1, italic
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
            FormatAccent           = "${esc}[1;38;2;243;191;69m"
            TableHeader            = "${esc}[1;38;2;243;191;69m"
            CustomTableHeaderLabel = "${esc}[1;3;38;2;243;191;69m"
            ErrorAccent            = "${esc}[1;38;2;236;127;49m"
            Error                  = "${esc}[1;38;2;255;131;115m"
            Warning                = "${esc}[1;38;2;243;191;69m"
            Verbose                = "${esc}[38;2;127;155;174m"
            Debug                  = "${esc}[38;2;134;173;149m"
            FeedbackName           = "${esc}[38;2;236;127;49m"
            FeedbackText           = "${esc}[38;2;214;195;160m"
            FeedbackAction         = "${esc}[38;2;243;191;69m"
        }
        foreach ($key in $formatting.Keys) {
            if ($PSStyle.Formatting.PSObject.Properties[$key]) { $PSStyle.Formatting.$key = $formatting[$key] }
        }
        $PSStyle.Progress.Style = "${esc}[1;38;2;243;191;69m"

        if ($PSStyle.PSObject.Properties['FileInfo']) {
            $PSStyle.FileInfo.Directory = "${esc}[1;38;2;243;191;69m"
            $PSStyle.FileInfo.SymbolicLink = "${esc}[38;2;134;173;149m"
            $PSStyle.FileInfo.Executable = "${esc}[1;38;2;173;185;86m"
            foreach ($ext in '.zip', '.tgz', '.gz', '.tar', '.nupkg', '.cab', '.7z') { $PSStyle.FileInfo.Extension[$ext] = "${esc}[38;2;255;131;115m" }
            foreach ($ext in '.ps1', '.psd1', '.psm1', '.ps1xml') { $PSStyle.FileInfo.Extension[$ext] = "${esc}[38;2;134;173;149m" }
        }
    }
}
