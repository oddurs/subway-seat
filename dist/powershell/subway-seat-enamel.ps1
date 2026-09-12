# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# Subway Seat Enamel for PowerShell: PSReadLine token colors, and $PSStyle on PowerShell 7.2+.
# Dot-source it from your profile:  . "$PSScriptRoot/subway-seat-enamel.ps1"
# Needs a terminal with 24-bit color (Windows Terminal, iTerm2, Ghostty, …).

& {
    $esc = [char]27

    $colors = @{
        Default                = "${esc}[38;2;62;44;30m"                     # text
        Command                = "${esc}[38;2;151;102;8m"                    # yellow
        Parameter              = "${esc}[38;2;62;113;87m"                    # sage
        String                 = "${esc}[38;2;102;116;15m"                   # green
        Operator               = "${esc}[38;2;160;72;0m"                     # orange
        Variable               = "${esc}[38;2;132;56;17m"                    # clay
        Member                 = "${esc}[38;2;84;64;47m"                     # subtext1
        Number                 = "${esc}[38;2;191;66;51m"                    # red_hi
        Type                   = "${esc}[38;2;62;113;87m"                    # sage
        Keyword                = "${esc}[38;2;160;72;0m"                     # orange
        Comment                = "${esc}[3;38;2;140;114;84m"                 # overlay1, italic
        Error                  = "${esc}[38;2;191;66;51m"                    # red_hi
        Emphasis               = "${esc}[1;38;2;151;102;8m"                  # yellow, bold: search matches
        Selection              = "${esc}[1;38;2;42;29;19;48;2;203;184;152m"  # text_hi on the selection ground
        ContinuationPrompt     = "${esc}[38;2;140;114;84m"                   # overlay1
        InlinePrediction       = "${esc}[38;2;165;141;109m"                  # overlay0, like fish autosuggestions
        ListPrediction         = "${esc}[38;2;160;72;0m"                     # orange: the > marker and source
        ListPredictionSelected = "${esc}[48;2;203;184;152m"                  # surface1 ground
        ListPredictionTooltip  = "${esc}[3;38;2;140;114;84m"                 # overlay1, italic
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
            FormatAccent           = "${esc}[1;38;2;151;102;8m"
            TableHeader            = "${esc}[1;38;2;151;102;8m"
            CustomTableHeaderLabel = "${esc}[1;3;38;2;151;102;8m"
            ErrorAccent            = "${esc}[1;38;2;160;72;0m"
            Error                  = "${esc}[1;38;2;191;66;51m"
            Warning                = "${esc}[1;38;2;151;102;8m"
            Verbose                = "${esc}[38;2;63;100;128m"
            Debug                  = "${esc}[38;2;62;113;87m"
            FeedbackName           = "${esc}[38;2;160;72;0m"
            FeedbackText           = "${esc}[38;2;84;64;47m"
            FeedbackAction         = "${esc}[38;2;151;102;8m"
        }
        foreach ($key in $formatting.Keys) {
            if ($PSStyle.Formatting.PSObject.Properties[$key]) { $PSStyle.Formatting.$key = $formatting[$key] }
        }
        $PSStyle.Progress.Style = "${esc}[1;38;2;151;102;8m"

        if ($PSStyle.PSObject.Properties['FileInfo']) {
            $PSStyle.FileInfo.Directory = "${esc}[1;38;2;151;102;8m"
            $PSStyle.FileInfo.SymbolicLink = "${esc}[38;2;62;113;87m"
            $PSStyle.FileInfo.Executable = "${esc}[1;38;2;102;116;15m"
            foreach ($ext in '.zip', '.tgz', '.gz', '.tar', '.nupkg', '.cab', '.7z') { $PSStyle.FileInfo.Extension[$ext] = "${esc}[38;2;191;66;51m" }
            foreach ($ext in '.ps1', '.psd1', '.psm1', '.ps1xml') { $PSStyle.FileInfo.Extension[$ext] = "${esc}[38;2;62;113;87m" }
        }
    }
}
