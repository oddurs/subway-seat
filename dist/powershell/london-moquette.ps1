# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# London Moquette for PowerShell: PSReadLine token colors, and $PSStyle on PowerShell 7.2+.
# Dot-source it from your profile:  . "$PSScriptRoot/london-moquette.ps1"
# Needs a terminal with 24-bit color (Windows Terminal, iTerm2, Ghostty, …).

& {
    $esc = [char]27

    $colors = @{
        Default                = "${esc}[38;2;216;222;234m"                   # text
        Command                = "${esc}[38;2;242;192;63m"                    # yellow
        Parameter              = "${esc}[38;2;84;180;181m"                    # sage
        String                 = "${esc}[38;2;119;197;129m"                   # green
        Operator               = "${esc}[38;2;222;137;70m"                    # orange
        Variable               = "${esc}[38;2;174;158;220m"                   # clay
        Member                 = "${esc}[38;2;193;201;216m"                   # subtext1
        Number                 = "${esc}[38;2;241;120;105m"                   # red_hi
        Type                   = "${esc}[38;2;84;180;181m"                    # sage
        Keyword                = "${esc}[38;2;222;137;70m"                    # orange
        Comment                = "${esc}[3;38;2;115;129;156m"                 # overlay1, italic
        Error                  = "${esc}[38;2;241;120;105m"                   # red_hi
        Emphasis               = "${esc}[1;38;2;242;192;63m"                  # yellow, bold: search matches
        Selection              = "${esc}[1;38;2;233;237;245;48;2;61;79;114m"  # text_hi on the selection ground
        ContinuationPrompt     = "${esc}[38;2;115;129;156m"                   # overlay1
        InlinePrediction       = "${esc}[38;2;87;102;133m"                    # overlay0, like fish autosuggestions
        ListPrediction         = "${esc}[38;2;222;137;70m"                    # orange: the > marker and source
        ListPredictionSelected = "${esc}[48;2;48;63;97m"                      # surface1 ground
        ListPredictionTooltip  = "${esc}[3;38;2;115;129;156m"                 # overlay1, italic
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
            FormatAccent           = "${esc}[1;38;2;242;192;63m"
            TableHeader            = "${esc}[1;38;2;242;192;63m"
            CustomTableHeaderLabel = "${esc}[1;3;38;2;242;192;63m"
            ErrorAccent            = "${esc}[1;38;2;222;137;70m"
            Error                  = "${esc}[1;38;2;241;120;105m"
            Warning                = "${esc}[1;38;2;242;192;63m"
            Verbose                = "${esc}[38;2;117;149;218m"
            Debug                  = "${esc}[38;2;84;180;181m"
            FeedbackName           = "${esc}[38;2;222;137;70m"
            FeedbackText           = "${esc}[38;2;193;201;216m"
            FeedbackAction         = "${esc}[38;2;242;192;63m"
        }
        foreach ($key in $formatting.Keys) {
            if ($PSStyle.Formatting.PSObject.Properties[$key]) { $PSStyle.Formatting.$key = $formatting[$key] }
        }
        $PSStyle.Progress.Style = "${esc}[1;38;2;242;192;63m"

        if ($PSStyle.PSObject.Properties['FileInfo']) {
            $PSStyle.FileInfo.Directory = "${esc}[1;38;2;242;192;63m"
            $PSStyle.FileInfo.SymbolicLink = "${esc}[38;2;84;180;181m"
            $PSStyle.FileInfo.Executable = "${esc}[1;38;2;119;197;129m"
            foreach ($ext in '.zip', '.tgz', '.gz', '.tar', '.nupkg', '.cab', '.7z') { $PSStyle.FileInfo.Extension[$ext] = "${esc}[38;2;241;120;105m" }
            foreach ($ext in '.ps1', '.psd1', '.psm1', '.ps1xml') { $PSStyle.FileInfo.Extension[$ext] = "${esc}[38;2;84;180;181m" }
        }
    }
}
