# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# Paris Carrelage for PowerShell: PSReadLine token colors, and $PSStyle on PowerShell 7.2+.
# Dot-source it from your profile:  . "$PSScriptRoot/paris-carrelage.ps1"
# Needs a terminal with 24-bit color (Windows Terminal, iTerm2, Ghostty, …).

& {
    $esc = [char]27

    $colors = @{
        Default                = "${esc}[38;2;37;53;44m"                     # text
        Command                = "${esc}[38;2;138;103;0m"                    # yellow
        Parameter              = "${esc}[38;2;8;97;66m"                      # sage
        String                 = "${esc}[38;2;32;127;65m"                    # green
        Operator               = "${esc}[38;2;117;69;0m"                     # orange
        Variable               = "${esc}[38;2;154;85;125m"                   # clay
        Member                 = "${esc}[38;2;55;73;64m"                     # subtext1
        Number                 = "${esc}[38;2;187;64;59m"                    # red_hi
        Type                   = "${esc}[38;2;8;97;66m"                      # sage
        Keyword                = "${esc}[38;2;117;69;0m"                     # orange
        Comment                = "${esc}[3;38;2;98;127;112m"                 # overlay1, italic
        Error                  = "${esc}[38;2;187;64;59m"                    # red_hi
        Emphasis               = "${esc}[1;38;2;138;103;0m"                  # yellow, bold: search matches
        Selection              = "${esc}[1;38;2;24;35;29;48;2;159;198;177m"  # text_hi on the selection ground
        ContinuationPrompt     = "${esc}[38;2;98;127;112m"                   # overlay1
        InlinePrediction       = "${esc}[38;2;120;156;136m"                  # overlay0, like fish autosuggestions
        ListPrediction         = "${esc}[38;2;117;69;0m"                     # orange: the > marker and source
        ListPredictionSelected = "${esc}[48;2;159;198;177m"                  # surface1 ground
        ListPredictionTooltip  = "${esc}[3;38;2;98;127;112m"                 # overlay1, italic
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
            FormatAccent           = "${esc}[1;38;2;138;103;0m"
            TableHeader            = "${esc}[1;38;2;138;103;0m"
            CustomTableHeaderLabel = "${esc}[1;3;38;2;138;103;0m"
            ErrorAccent            = "${esc}[1;38;2;117;69;0m"
            Error                  = "${esc}[1;38;2;187;64;59m"
            Warning                = "${esc}[1;38;2;138;103;0m"
            Verbose                = "${esc}[38;2;39;98;156m"
            Debug                  = "${esc}[38;2;8;97;66m"
            FeedbackName           = "${esc}[38;2;117;69;0m"
            FeedbackText           = "${esc}[38;2;55;73;64m"
            FeedbackAction         = "${esc}[38;2;138;103;0m"
        }
        foreach ($key in $formatting.Keys) {
            if ($PSStyle.Formatting.PSObject.Properties[$key]) { $PSStyle.Formatting.$key = $formatting[$key] }
        }
        $PSStyle.Progress.Style = "${esc}[1;38;2;138;103;0m"

        if ($PSStyle.PSObject.Properties['FileInfo']) {
            $PSStyle.FileInfo.Directory = "${esc}[1;38;2;138;103;0m"
            $PSStyle.FileInfo.SymbolicLink = "${esc}[38;2;8;97;66m"
            $PSStyle.FileInfo.Executable = "${esc}[1;38;2;32;127;65m"
            foreach ($ext in '.zip', '.tgz', '.gz', '.tar', '.nupkg', '.cab', '.7z') { $PSStyle.FileInfo.Extension[$ext] = "${esc}[38;2;187;64;59m" }
            foreach ($ext in '.ps1', '.psd1', '.psm1', '.ps1xml') { $PSStyle.FileInfo.Extension[$ext] = "${esc}[38;2;8;97;66m" }
        }
    }
}
