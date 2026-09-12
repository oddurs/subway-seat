# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# Paris Catacombes for PowerShell: PSReadLine token colors, and $PSStyle on PowerShell 7.2+.
# Dot-source it from your profile:  . "$PSScriptRoot/paris-catacombes.ps1"
# Needs a terminal with 24-bit color (Windows Terminal, iTerm2, Ghostty, …).

& {
    $esc = [char]27

    $colors = @{
        Default                = "${esc}[38;2;207;222;215m"                  # text
        Command                = "${esc}[38;2;235;195;66m"                   # yellow
        Parameter              = "${esc}[38;2;111;179;147m"                  # sage
        String                 = "${esc}[38;2;115;198;134m"                  # green
        Operator               = "${esc}[38;2;215;142;60m"                   # orange
        Variable               = "${esc}[38;2;231;131;189m"                  # clay
        Member                 = "${esc}[38;2;184;202;194m"                  # subtext1
        Number                 = "${esc}[38;2;239;121;111m"                  # red_hi
        Type                   = "${esc}[38;2;111;179;147m"                  # sage
        Keyword                = "${esc}[38;2;215;142;60m"                   # orange
        Comment                = "${esc}[3;38;2;100;133;118m"                # overlay1, italic
        Error                  = "${esc}[38;2;239;121;111m"                  # red_hi
        Emphasis               = "${esc}[1;38;2;235;195;66m"                 # yellow, bold: search matches
        Selection              = "${esc}[1;38;2;228;238;233;48;2;30;71;56m"  # text_hi on the selection ground
        ContinuationPrompt     = "${esc}[38;2;100;133;118m"                  # overlay1
        InlinePrediction       = "${esc}[38;2;69;106;91m"                    # overlay0, like fish autosuggestions
        ListPrediction         = "${esc}[38;2;215;142;60m"                   # orange: the > marker and source
        ListPredictionSelected = "${esc}[48;2;19;56;42m"                     # surface1 ground
        ListPredictionTooltip  = "${esc}[3;38;2;100;133;118m"                # overlay1, italic
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
            FormatAccent           = "${esc}[1;38;2;235;195;66m"
            TableHeader            = "${esc}[1;38;2;235;195;66m"
            CustomTableHeaderLabel = "${esc}[1;3;38;2;235;195;66m"
            ErrorAccent            = "${esc}[1;38;2;215;142;60m"
            Error                  = "${esc}[1;38;2;239;121;111m"
            Warning                = "${esc}[1;38;2;235;195;66m"
            Verbose                = "${esc}[38;2;99;155;213m"
            Debug                  = "${esc}[38;2;111;179;147m"
            FeedbackName           = "${esc}[38;2;215;142;60m"
            FeedbackText           = "${esc}[38;2;184;202;194m"
            FeedbackAction         = "${esc}[38;2;235;195;66m"
        }
        foreach ($key in $formatting.Keys) {
            if ($PSStyle.Formatting.PSObject.Properties[$key]) { $PSStyle.Formatting.$key = $formatting[$key] }
        }
        $PSStyle.Progress.Style = "${esc}[1;38;2;235;195;66m"

        if ($PSStyle.PSObject.Properties['FileInfo']) {
            $PSStyle.FileInfo.Directory = "${esc}[1;38;2;235;195;66m"
            $PSStyle.FileInfo.SymbolicLink = "${esc}[38;2;111;179;147m"
            $PSStyle.FileInfo.Executable = "${esc}[1;38;2;115;198;134m"
            foreach ($ext in '.zip', '.tgz', '.gz', '.tar', '.nupkg', '.cab', '.7z') { $PSStyle.FileInfo.Extension[$ext] = "${esc}[38;2;239;121;111m" }
            foreach ($ext in '.ps1', '.psd1', '.psm1', '.ps1xml') { $PSStyle.FileInfo.Extension[$ext] = "${esc}[38;2;111;179;147m" }
        }
    }
}
