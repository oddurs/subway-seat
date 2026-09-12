# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# London Portland for PowerShell: PSReadLine token colors, and $PSStyle on PowerShell 7.2+.
# Dot-source it from your profile:  . "$PSScriptRoot/london-portland.ps1"
# Needs a terminal with 24-bit color (Windows Terminal, iTerm2, Ghostty, …).

& {
    $esc = [char]27

    $colors = @{
        Default                = "${esc}[38;2;41;48;64m"                     # text
        Command                = "${esc}[38;2;141;108;8m"                    # yellow
        Parameter              = "${esc}[38;2;0;115;118m"                    # sage
        String                 = "${esc}[38;2;13;129;49m"                    # green
        Operator               = "${esc}[38;2;165;67;0m"                     # orange
        Variable               = "${esc}[38;2;117;95;169m"                   # clay
        Member                 = "${esc}[38;2;60;69;87m"                     # subtext1
        Number                 = "${esc}[38;2;204;46;37m"                    # red_hi
        Type                   = "${esc}[38;2;0;115;118m"                    # sage
        Keyword                = "${esc}[38;2;165;67;0m"                     # orange
        Comment                = "${esc}[3;38;2;105;119;148m"                # overlay1, italic
        Error                  = "${esc}[38;2;204;46;37m"                    # red_hi
        Emphasis               = "${esc}[1;38;2;141;108;8m"                  # yellow, bold: search matches
        Selection              = "${esc}[1;38;2;27;32;43;48;2;168;187;226m"  # text_hi on the selection ground
        ContinuationPrompt     = "${esc}[38;2;105;119;148m"                  # overlay1
        InlinePrediction       = "${esc}[38;2;129;146;180m"                  # overlay0, like fish autosuggestions
        ListPrediction         = "${esc}[38;2;165;67;0m"                     # orange: the > marker and source
        ListPredictionSelected = "${esc}[48;2;168;187;226m"                  # surface1 ground
        ListPredictionTooltip  = "${esc}[3;38;2;105;119;148m"                # overlay1, italic
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
            FormatAccent           = "${esc}[1;38;2;141;108;8m"
            TableHeader            = "${esc}[1;38;2;141;108;8m"
            CustomTableHeaderLabel = "${esc}[1;3;38;2;141;108;8m"
            ErrorAccent            = "${esc}[1;38;2;165;67;0m"
            Error                  = "${esc}[1;38;2;204;46;37m"
            Warning                = "${esc}[1;38;2;141;108;8m"
            Verbose                = "${esc}[38;2;0;25;168m"
            Debug                  = "${esc}[38;2;0;115;118m"
            FeedbackName           = "${esc}[38;2;165;67;0m"
            FeedbackText           = "${esc}[38;2;60;69;87m"
            FeedbackAction         = "${esc}[38;2;141;108;8m"
        }
        foreach ($key in $formatting.Keys) {
            if ($PSStyle.Formatting.PSObject.Properties[$key]) { $PSStyle.Formatting.$key = $formatting[$key] }
        }
        $PSStyle.Progress.Style = "${esc}[1;38;2;141;108;8m"

        if ($PSStyle.PSObject.Properties['FileInfo']) {
            $PSStyle.FileInfo.Directory = "${esc}[1;38;2;141;108;8m"
            $PSStyle.FileInfo.SymbolicLink = "${esc}[38;2;0;115;118m"
            $PSStyle.FileInfo.Executable = "${esc}[1;38;2;13;129;49m"
            foreach ($ext in '.zip', '.tgz', '.gz', '.tar', '.nupkg', '.cab', '.7z') { $PSStyle.FileInfo.Extension[$ext] = "${esc}[38;2;204;46;37m" }
            foreach ($ext in '.ps1', '.psd1', '.psm1', '.ps1xml') { $PSStyle.FileInfo.Extension[$ext] = "${esc}[38;2;0;115;118m" }
        }
    }
}
