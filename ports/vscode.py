"""VS Code (and Cursor, Windsurf, Kiro, VSCodium): one extension with a workbench theme per flavor.

The workbench is layered: one chrome ground (mantle), crust only as grooves,
popovers on paper, and hovers, rows and focus a translucent wash of text. The
editor's selection, matches, brackets and diff grounds use the shared editor
recipes (`_editors.ui`, `tints`), glazed so they land on exactly the same color
as in every other editor port while staying translucent.
"""

import json

import palette as p
from ports._editors import extra_scope_rules, glaze, ui
from ports._lib import REPO, ROOT, VERSION, Out, resolve, scope_rules, tints, zip_bytes

VSIX = "subway-seat.vsix"  # a stable name, so its URL doesn't change between releases

META = {
    "id": "vscode",
    "name": "VS Code",
    "category": "Editors",
    "homepage": "https://code.visualstudio.com",
    "enable": {
        "where": "a shell, or Extensions › ⋯ › Install from VSIX… (VS Code, Cursor, Windsurf, VSCodium)",
        "code": f"code --install-extension {VSIX}   # cursor, windsurf and codium take the same flag\n"
        '# then in settings.json: "workbench.colorTheme": "{name}"',
        "lang": "sh",
    },
    "auto": {
        "where": "settings.json",
        "code": '"window.autoDetectColorScheme": true,\n'
        '"workbench.preferredDarkColorTheme": "Subway Seat",\n'
        '"workbench.preferredLightColorTheme": "Subway Seat Enamel"',
        "lang": "json",
    },
    "requires": "VS Code 1.85+",
    "detect": [
        "code", "/Applications/Visual Studio Code.app",
        "cursor", "/Applications/Cursor.app",
        "windsurf", "/Applications/Windsurf.app",
        "codium", "/Applications/VSCodium.app",
    ],
    "notes": "All three flavors in one extension, with a layered workbench, TextMate and semantic token colors, "
    "and the AI panels in Cursor, Windsurf and Kiro. It isn't on the Marketplace or Open VSX yet, so install "
    "the VSIX from this page; it works in VS Code, Cursor, Windsurf and VSCodium.",
}

ON_ACCENT = ("crust", "paper")  # text on an orange/yellow/red fill, dark and Enamel
BUTTON = ("orange", "mix(text,orange,0.15)")  # Enamel's orange is deepened a touch under cream text

# (key, dark expression, light expression or None for the same). Expressions are
# `_lib.resolve` layering expressions: a role, `role@L3` / `role@35`, `mix(a,b,t)`.
LAYERS = [
    # ── grounds
    ("editor.background", "base", None),
    ("editorGutter.background", "base", None),
    ("editorPane.background", "base", None),
    ("breadcrumb.background", "base", None),
    ("editorGroupHeader.tabsBackground", "mantle", None),
    ("editorGroupHeader.noTabsBackground", "base", None),
    ("tab.activeBackground", "base", None),
    ("tab.unfocusedActiveBackground", "mix(base,mantle,0.5)", None),
    ("tab.inactiveBackground", "mantle", None),
    ("tab.hoverBackground", "text@L1", None),
    ("tab.unfocusedHoverBackground", "text@3", None),
    ("sideBar.background", "mantle", None),
    ("sideBarTitle.background", "mantle", None),
    ("sideBarSectionHeader.background", "mantle", None),
    ("sideBarStickyScroll.background", "mantle", None),
    ("activityBar.background", "mantle", None),
    ("titleBar.activeBackground", "mantle", None),
    ("titleBar.inactiveBackground", "crust", None),
    ("statusBar.background", "mantle", None),
    ("statusBar.noFolderBackground", "mantle", None),
    ("panel.background", "mantle", None),
    ("panelStickyScroll.background", "mantle", None),
    ("panelSectionHeader.background", "mantle", None),
    ("outputView.background", "mantle", None),
    ("outputViewStickyScroll.background", "mantle", None),
    ("editorStickyScroll.background", "base", None),
    ("editorStickyScrollGutter.background", "base", None),
    ("editorStickyScrollHover.background", "text@L1", None),
    ("welcomePage.background", "base", None),
    ("walkThrough.embeddedEditorBackground", "mantle", None),
    # ── structural seams
    ("sideBar.border", "crust", "text@EDGE"),
    ("activityBar.border", "mantle", None),
    ("sideBarActivityBarTop.border", "crust", "text@EDGE"),
    ("titleBar.border", "crust", "text@EDGE"),
    ("statusBar.border", "crust", "text@EDGE"),
    ("statusBar.noFolderBorder", "crust", "text@EDGE"),
    ("panel.border", "crust", "text@EDGE"),
    ("panelSection.border", "crust", "text@EDGE"),
    ("panelSectionHeader.border", "crust", "text@EDGE"),
    ("editorGroup.border", "crust", "text@EDGE"),
    ("editorGroupHeader.tabsBorder", "crust", "text@EDGE"),
    ("sideBySideEditor.horizontalBorder", "crust", "text@EDGE"),
    ("sideBySideEditor.verticalBorder", "crust", "text@EDGE"),
    ("tab.border", "mantle", None),
    ("tab.activeBorder", "base", None),
    ("tab.activeBorderTop", "orange", None),
    ("tab.unfocusedActiveBorder", "base", None),
    ("tab.unfocusedActiveBorderTop", "orange@35", None),
    ("tab.lastPinnedBorder", "text@L3", None),
    ("tab.dragAndDropBorder", "orange", None),
    ("sideBarSectionHeader.border", "text@6", "text@8"),
    ("sideBarStickyScroll.shadow", "shadow@45", "shadow@10"),
    ("editorStickyScroll.shadow", "shadow@45", "shadow@10"),
    ("panelStickyScroll.shadow", "shadow@45", "shadow@10"),
    ("scrollbar.shadow", "shadow@45", "shadow@10"),
    ("focusBorder", "orange@50", "orange@60"),
    ("sash.hoverBorder", "orange@70", None),
    ("profiles.sashBorder", "crust", "text@EDGE"),
    ("settings.sashBorder", "crust", "text@EDGE"),
    ("simpleFindWidget.sashBorder", "text@L3", None),
    # ── widgets / popovers (on paper, with a hairline edge)
    ("widget.shadow", "shadow@60", "shadow@14"),
    ("widget.border", "text@EDGE", None),
    ("editorWidget.background", "paper", None),
    ("editorWidget.foreground", "text", None),
    ("editorWidget.border", "text@EDGE", None),
    ("editorWidget.resizeBorder", "orange@60", None),
    ("editorSuggestWidget.background", "paper", None),
    ("editorSuggestWidget.border", "text@EDGE", None),
    ("editorSuggestWidget.selectedBackground", "text@L3", None),
    ("editorSuggestWidgetStatus.foreground", "overlay1", None),
    ("editorHoverWidget.background", "paper", None),
    ("editorHoverWidget.foreground", "text", None),
    ("editorHoverWidget.border", "text@EDGE", None),
    ("editorHoverWidget.statusBarBackground", "text@L1", None),
    ("editorHoverWidget.highlightForeground", "yellow", None),
    ("editorActionList.background", "paper", None),
    ("editorActionList.foreground", "text", None),
    ("editorActionList.focusBackground", "text@L3", None),
    ("editorActionList.focusForeground", "text_hi", None),
    ("quickInput.background", "paper", None),
    ("quickInputTitle.background", "text@L1", None),
    ("quickInputList.focusBackground", "text@L3", None),
    ("pickerGroup.foreground", "orange", None),
    ("pickerGroup.border", "text@L2", None),
    ("menu.background", "paper", None),
    ("menu.border", "text@EDGE", None),
    ("menu.selectionBackground", "text@L3", None),
    ("menu.selectionBorder", "transparent", None),
    ("menu.separatorBackground", "text@L2", None),
    ("menubar.selectionBackground", "text@L2", None),
    ("menubar.selectionForeground", "text_hi", None),
    ("menubar.selectionBorder", "transparent", None),
    ("notifications.background", "paper", None),
    ("notifications.border", "text@EDGE", None),
    ("notificationToast.border", "text@EDGE", None),
    ("notificationCenter.border", "text@EDGE", None),
    ("notificationCenterHeader.background", "text@L1", None),
    ("notificationCenterHeader.foreground", "subtext1", None),
    ("notificationLink.foreground", "denim", None),
    ("debugToolBar.background", "paper", None),
    ("debugToolBar.border", "text@EDGE", None),
    ("breadcrumbPicker.background", "paper", None),
    ("listFilterWidget.background", "paper", None),
    ("listFilterWidget.outline", "orange@60", None),
    ("listFilterWidget.noMatchesOutline", "red_hi", "red"),
    ("listFilterWidget.shadow", "shadow@45", "shadow@10"),
    ("editorGroup.dropIntoPromptBackground", "paper", None),
    ("editorGroup.dropIntoPromptForeground", "text", None),
    ("peekView.border", "orange@50", None),
    ("peekViewTitle.background", "paper", None),
    ("peekViewTitleLabel.foreground", "text_hi", None),
    ("peekViewTitleDescription.foreground", "overlay1", None),
    ("peekViewEditor.background", "mantle", None),
    ("peekViewEditorGutter.background", "mantle", None),
    ("peekViewEditorStickyScroll.background", "mantle", None),
    ("peekViewEditorStickyScrollGutter.background", "mantle", None),
    ("peekViewResult.background", "mantle", None),
    ("peekViewResult.selectionBackground", "text@L3", None),
    ("peekViewResult.selectionForeground", "text_hi", None),
    ("peekViewResult.fileForeground", "text", None),
    ("peekViewResult.lineForeground", "subtext0", None),
    ("debugExceptionWidget.background", "mix(red,paper,0.10)", None),
    ("debugExceptionWidget.border", "red", None),
    ("editorMarkerNavigation.background", "paper", None),
    ("editorMarkerNavigationError.background", "red_hi", "red"),
    ("editorMarkerNavigationError.headerBackground", "red@12", None),
    ("editorMarkerNavigationWarning.background", "yellow", None),
    ("editorMarkerNavigationWarning.headerBackground", "yellow@12", None),
    ("editorMarkerNavigationInfo.background", "denim", None),
    ("editorMarkerNavigationInfo.headerBackground", "denim@14", None),
    # ── controls
    ("input.background", "base", "paper"),
    ("input.border", "text@10", "text@EDGE"),
    ("inputOption.activeBackground", "orange@20", "orange@16"),
    ("inputOption.activeBorder", "orange@60", None),
    ("inputOption.hoverBackground", "text@L2", None),
    ("inputValidation.errorBackground", "mix(red,paper,0.12)", None),
    ("inputValidation.errorForeground", "text", None),
    ("inputValidation.errorBorder", "red_hi", "red"),
    ("inputValidation.warningBackground", "mix(yellow,paper,0.12)", None),
    ("inputValidation.warningForeground", "text", None),
    ("inputValidation.warningBorder", "yellow", None),
    ("inputValidation.infoBackground", "mix(denim,paper,0.12)", None),
    ("inputValidation.infoForeground", "text", None),
    ("inputValidation.infoBorder", "denim", None),
    ("panelInput.border", "text@10", "text@EDGE"),
    ("searchEditor.textInputBorder", "text@10", "text@EDGE"),
    ("dropdown.background", "base", "paper"),
    ("dropdown.listBackground", "paper", None),
    ("dropdown.border", "text@10", "text@EDGE"),
    ("checkbox.background", "base", "paper"),
    ("checkbox.border", "text@L4", None),
    ("checkbox.foreground", "yellow", "orange"),
    ("checkbox.selectBackground", "paper", None),
    ("radio.activeBackground", "orange@20", "orange@16"),
    ("radio.activeBorder", "orange@60", None),
    ("radio.activeForeground", "text_hi", None),
    ("radio.inactiveBackground", "transparent", None),
    ("radio.inactiveBorder", "text@L3", None),
    ("radio.inactiveForeground", "subtext0", None),
    ("radio.inactiveHoverBackground", "text@L2", None),
    ("button.background", *BUTTON),
    ("button.foreground", *ON_ACCENT),
    ("button.hoverBackground", "orange_hi", "orange"),
    ("button.border", "transparent", None),
    ("button.secondaryBackground", "text@L3", None),
    ("button.secondaryHoverBackground", "text@L4", None),
    ("button.separator", "crust@40", "base@40"),
    ("extensionButton.background", *BUTTON),
    ("extensionButton.foreground", *ON_ACCENT),
    ("extensionButton.hoverBackground", "orange_hi", "orange"),
    ("extensionButton.separator", "crust@40", "base@40"),
    ("extensionButton.prominentBackground", *BUTTON),
    ("extensionButton.prominentForeground", *ON_ACCENT),
    ("extensionButton.prominentHoverBackground", "orange_hi", "orange"),
    ("extensionBadge.remoteBackground", *BUTTON),
    ("extensionBadge.remoteForeground", *ON_ACCENT),
    ("extensionIcon.starForeground", "yellow", None),
    ("extensionIcon.verifiedForeground", "denim", None),
    ("extensionIcon.preReleaseForeground", "clay", None),
    ("extensionIcon.sponsorForeground", "red_hi", None),
    ("extensionIcon.privateForeground", "overlay1", None),
    ("mcpIcon.starForeground", "yellow", None),
    ("progressBar.background", "orange", None),
    ("badge.background", "text@L3", "text@L3"),
    ("activityBarBadge.background", "orange", None),
    ("activityErrorBadge.background", "red_hi", "red"),
    ("activityErrorBadge.foreground", *ON_ACCENT),
    ("activityWarningBadge.background", "yellow", None),
    ("activityWarningBadge.foreground", *ON_ACCENT),
    ("panelTitleBadge.background", "orange", None),
    ("panelTitleBadge.foreground", *ON_ACCENT),
    ("profileBadge.background", "text@L3", None),
    ("profileBadge.foreground", "text", None),
    ("keybindingLabel.background", "text@6", None),
    ("keybindingLabel.border", "text@L3", None),
    ("keybindingLabel.bottomBorder", "text@L5", None),
    ("toolbar.hoverBackground", "text@L2", None),
    ("toolbar.activeBackground", "text@L3", None),
    ("actionBar.toggledBackground", "orange@18", "orange@14"),
    ("commandCenter.background", "text@L1", "paper"),
    ("commandCenter.foreground", "subtext0", None),
    ("commandCenter.border", "text@10", "text@EDGE"),
    ("commandCenter.activeBackground", "text@L2", None),
    ("commandCenter.activeForeground", "text", None),
    ("commandCenter.activeBorder", "orange@50", None),
    ("commandCenter.inactiveForeground", "overlay0", None),
    ("commandCenter.inactiveBorder", "text@L1", None),
    ("commandCenter.debuggingBackground", "mix(red,mantle,0.35)", "mix(red,mantle,0.22)"),
    ("selection.background", "text@20", "text@16"),
    ("banner.background", "text@L2", None),
    ("banner.foreground", "text", None),
    ("banner.iconForeground", "denim", None),
    # ── lists
    ("list.hoverBackground", "text@L1", None),
    ("list.inactiveSelectionBackground", "text@L2", None),
    ("list.activeSelectionBackground", "text@L3", None),
    ("list.focusBackground", "text@L3", None),
    ("list.inactiveFocusBackground", "text@L2", None),
    ("list.focusOutline", "orange@35", "orange@45"),
    ("list.inactiveFocusOutline", "transparent", None),
    ("list.focusAndSelectionOutline", "transparent", None),
    ("list.dropBackground", "orange@15", "orange@12"),
    ("list.dropBetweenBackground", "orange", None),
    ("list.filterMatchBorder", "transparent", None),
    ("list.errorForeground", "red_hi", "red"),
    ("list.warningForeground", "yellow", None),
    ("list.invalidItemForeground", "red_hi", "red"),
    ("list.deemphasizedForeground", "overlay0", None),
    ("editorGroup.dropBackground", "orange@10", "orange@8"),
    ("sideBar.dropBackground", "orange@10", "orange@8"),
    ("panelSection.dropBackground", "orange@10", "orange@8"),
    ("panel.dropBorder", "orange", None),
    ("terminal.dropBackground", "orange@10", "orange@8"),
    ("tree.indentGuidesStroke", "text@L5", None),
    ("tree.inactiveIndentGuidesStroke", "text@L2", None),
    ("tree.tableColumnsBorder", "text@L2", None),
    ("tree.tableOddRowsBackground", "text@3", None),
    ("statusBarItem.hoverBackground", "text@L2", None),
    ("statusBarItem.hoverForeground", "text", None),
    ("statusBarItem.activeBackground", "text@L3", None),
    ("statusBarItem.compactHoverBackground", "text@L2", None),
    ("statusBarItem.focusBorder", "orange", None),
    ("statusBarItem.prominentBackground", "text@L3", None),
    ("statusBarItem.prominentHoverBackground", "text@L4", None),
    ("statusBarItem.prominentHoverForeground", "text_hi", None),
    ("statusBarItem.remoteBackground", *BUTTON),
    ("statusBarItem.remoteForeground", *ON_ACCENT),
    ("statusBarItem.remoteHoverBackground", "orange_hi", "orange"),
    ("statusBarItem.remoteHoverForeground", *ON_ACCENT),
    ("statusBarItem.errorBackground", "transparent", None),
    ("statusBarItem.errorHoverBackground", "text@L2", None),
    ("statusBarItem.errorHoverForeground", "red_hi", "red"),
    ("statusBarItem.warningBackground", "transparent", None),
    ("statusBarItem.warningHoverBackground", "text@L2", None),
    ("statusBarItem.warningHoverForeground", "yellow", None),
    ("statusBarItem.offlineBackground", "mix(red,mantle,0.35)", "mix(red,mantle,0.22)"),
    ("statusBarItem.offlineForeground", "text_hi", None),
    ("statusBarItem.offlineHoverBackground", "mix(red,mantle,0.5)", "mix(red,mantle,0.32)"),
    ("statusBarItem.offlineHoverForeground", "text_hi", None),
    ("statusBar.focusBorder", "orange", None),
    ("statusBar.debuggingBackground", "mix(red,mantle,0.35)", "mix(red,mantle,0.22)"),
    ("statusBar.debuggingBorder", "red@60", None),
    ("activityBar.activeBorder", "orange", None),
    ("activityBar.activeFocusBorder", "orange", None),
    ("activityBarTop.activeBorder", "orange", None),
    ("panelTitle.activeBorder", "orange", None),
    ("panelTitle.border", "crust", "text@EDGE"),
    ("terminal.tab.activeBorder", "orange", None),
    # ── editor interior (selection, matches and brackets are in `recipes`)
    ("editor.lineHighlightBackground", "text@L1", None),
    ("editor.lineHighlightBorder", "transparent", None),
    ("editor.selectionHighlightBackground", "text@L2", None),
    ("editor.selectionHighlightBorder", "transparent", None),
    ("editor.wordHighlightBackground", "text@L2", None),
    ("editor.wordHighlightStrongBackground", "denim@18", "denim@14"),
    ("editor.wordHighlightTextBackground", "text@L2", None),
    ("editor.findMatchBorder", "orange@80", "orange"),
    ("editor.findMatchHighlightBorder", "transparent", None),
    ("editor.findRangeHighlightBackground", "text@L1", None),
    ("editor.rangeHighlightBackground", "yellow@8", "yellow@12"),
    ("editor.hoverHighlightBackground", "text@L2", None),
    ("editor.linkedEditingBackground", "denim@14", "denim@12"),
    ("editor.foldBackground", "text@5", None),
    ("editor.foldPlaceholderForeground", "overlay1", None),
    ("editor.placeholder.foreground", "overlay0", None),
    ("editor.compositionBorder", "text", None),
    ("editor.inlineValuesForeground", "overlay1", None),
    ("editor.inlineValuesBackground", "yellow@8", "yellow@12"),
    ("editor.snippetTabstopHighlightBackground", "text@L2", None),
    ("editor.snippetTabstopHighlightBorder", "transparent", None),
    ("editor.snippetFinalTabstopHighlightBackground", "transparent", None),
    ("editor.snippetFinalTabstopHighlightBorder", "orange@60", None),
    ("editor.stackFrameHighlightBackground", "yellow@12", "yellow@16"),
    ("editor.focusedStackFrameHighlightBackground", "green@12", "green@14"),
    ("editorLink.activeForeground", "denim_hi", "denim"),
    ("editorIndentGuide.background1", "text@7", "text@8"),
    ("editorIndentGuide.activeBackground1", "text@20", "text@22"),
    ("editorWhitespace.foreground", "text@14", "text@16"),
    ("editorRuler.foreground", "text@L2", None),
    ("editorInlayHint.foreground", "overlay1", None),
    ("editorInlayHint.background", "text@6", "text@5"),
    ("editorInlayHint.typeForeground", "overlay1", None),
    ("editorInlayHint.typeBackground", "text@6", "text@5"),
    ("editorInlayHint.parameterForeground", "overlay1", None),
    ("editorInlayHint.parameterBackground", "text@6", "text@5"),
    ("editorOverviewRuler.border", "transparent", None),
    ("editorLineNumber.foreground", "overlay0", None),
    ("editorLineNumber.activeForeground", "yellow", "orange"),
    ("editorActiveLineNumber.foreground", "yellow", "orange"),  # the deprecated alias
    ("editorLineNumber.dimmedForeground", "surface2", "surface1"),
    ("editorCodeLens.foreground", "overlay0", None),
    ("editorGhostText.foreground", "overlay0", None),
    ("editorUnnecessaryCode.opacity", "#000000A0", None),  # VS Code only reads the alpha
    ("editorLightBulb.foreground", "yellow", None),
    ("editorLightBulbAutoFix.foreground", "green", None),
    ("editorLightBulbAi.foreground", "clay", None),
    ("editorGutter.foldingControlForeground", "overlay1", None),
    ("editorGutter.commentGlyphForeground", "overlay1", None),
    ("editorGutter.commentRangeForeground", "text@L3", None),
    ("editorGutter.commentUnresolvedGlyphForeground", "orange", None),
    ("editorGutter.commentDraftGlyphForeground", "yellow", None),
    ("editorGutter.itemBackground", "text@L2", None),
    ("editorGutter.itemGlyphForeground", "subtext0", None),
    ("editorCommentsWidget.resolvedBorder", "overlay1", None),
    ("editorCommentsWidget.unresolvedBorder", "orange", None),
    ("editorCommentsWidget.rangeBackground", "yellow@8", "yellow@12"),
    ("editorCommentsWidget.rangeActiveBackground", "yellow@16", "yellow@20"),
    ("editorCommentsWidget.replyInputBackground", "paper", None),
    ("commentsView.resolvedIcon", "overlay1", None),
    ("commentsView.unresolvedIcon", "orange", None),
    ("editorUnicodeHighlight.border", "yellow", None),
    ("editorUnicodeHighlight.background", "yellow@12", "yellow@16"),
    ("editorMultiCursor.primary.foreground", "yellow", "orange"),
    ("editorMultiCursor.primary.background", "crust", "base"),
    ("editorMultiCursor.secondary.foreground", "mix(yellow,base,0.55)", "mix(orange,base,0.55)"),
    ("editorMultiCursor.secondary.background", "crust", "base"),
    # diagnostics: colored squiggles, no fills
    ("editorError.foreground", "red_hi", None),
    ("editorError.background", "transparent", None),
    ("editorError.border", "transparent", None),
    ("editorWarning.foreground", "yellow", None),
    ("editorWarning.background", "transparent", None),
    ("editorWarning.border", "transparent", None),
    ("editorInfo.foreground", "denim", None),
    ("editorInfo.background", "transparent", None),
    ("editorInfo.border", "transparent", None),
    ("editorHint.foreground", "sage", None),
    ("editorHint.border", "transparent", None),
    ("problemsErrorIcon.foreground", "red_hi", "red"),
    ("problemsWarningIcon.foreground", "yellow", None),
    ("problemsInfoIcon.foreground", "denim", None),
    ("notificationsErrorIcon.foreground", "red_hi", "red"),
    ("notificationsWarningIcon.foreground", "yellow", None),
    ("notificationsInfoIcon.foreground", "denim", None),
    ("errorForeground", "red_hi", "red"),
    ("markdownAlert.note.foreground", "denim", None),
    ("markdownAlert.tip.foreground", "green", None),
    ("markdownAlert.important.foreground", "clay", None),
    ("markdownAlert.warning.foreground", "yellow", None),
    ("markdownAlert.caution.foreground", "red_hi", "red"),
    # ── brackets (hue @ alpha so they sit under identifiers)
    ("editorBracketHighlight.foreground1", "yellow@85", None),
    ("editorBracketHighlight.foreground2", "orange@85", None),
    ("editorBracketHighlight.foreground3", "sage@85", None),
    ("editorBracketHighlight.foreground4", "clay@85", None),
    ("editorBracketHighlight.foreground5", "denim@85", None),
    ("editorBracketHighlight.foreground6", "overlay2", None),
    ("editorBracketHighlight.unexpectedBracket.foreground", "red_hi", "red"),
    *((f"editorBracketPairGuide.activeBackground{i}", f"{c}@60", None)
      for i, c in enumerate(("yellow", "orange", "sage", "clay", "denim", "overlay2"), 1)),
    *((f"editorBracketPairGuide.background{i}", f"{c}@20", None)
      for i, c in enumerate(("yellow", "orange", "sage", "clay", "denim", "overlay2"), 1)),
    # ── scrollbar / minimap / overview ruler
    ("scrollbarSlider.background", "text@9", "text@12"),
    ("scrollbarSlider.hoverBackground", "text@L4", "text@18"),
    ("scrollbarSlider.activeBackground", "orange@40", None),
    ("notebookScrollbarSlider.background", "text@9", "text@12"),
    ("notebookScrollbarSlider.hoverBackground", "text@L4", "text@18"),
    ("notebookScrollbarSlider.activeBackground", "orange@40", None),
    ("minimapSlider.background", "text@7", "text@10"),
    ("minimapSlider.hoverBackground", "text@12", "text@15"),
    ("minimapSlider.activeBackground", "orange@30", None),
    ("minimap.selectionHighlight", "text@30", "text@25"),
    ("minimap.selectionOccurrenceHighlight", "text@20", None),
    ("minimap.findMatchHighlight", "yellow@70", None),
    ("minimap.errorHighlight", "red_hi", None),
    ("minimap.warningHighlight", "yellow", None),
    ("minimap.infoHighlight", "denim", None),
    ("editorOverviewRuler.errorForeground", "red_hi", None),
    ("editorOverviewRuler.warningForeground", "yellow", None),
    ("editorOverviewRuler.infoForeground", "denim", None),
    ("editorOverviewRuler.findMatchForeground", "orange@80", None),
    ("editorOverviewRuler.rangeHighlightForeground", "yellow@40", None),
    ("editorOverviewRuler.selectionHighlightForeground", "text@40", None),
    ("editorOverviewRuler.wordHighlightForeground", "text@40", None),
    ("editorOverviewRuler.wordHighlightStrongForeground", "denim@60", None),
    ("editorOverviewRuler.wordHighlightTextForeground", "text@40", None),
    ("editorOverviewRuler.bracketMatchForeground", "yellow@60", "orange@60"),
    ("editorOverviewRuler.currentContentForeground", "green@60", None),
    ("editorOverviewRuler.incomingContentForeground", "denim@60", None),
    ("editorOverviewRuler.commonContentForeground", "text@40", None),
    ("editorOverviewRuler.inlineChatInserted", "green@60", None),
    ("editorOverviewRuler.inlineChatRemoved", "red_hi@60", None),
    ("terminalOverviewRuler.cursorForeground", "yellow", "orange"),
    ("terminalOverviewRuler.findMatchForeground", "orange@80", None),
    # ── diff / merge / scm (grounds are in `recipes`; bars and signs are green / yellow / red_hi in every flavor)
    ("diffEditor.diagonalFill", "text@L2", None),
    ("diffEditor.border", "crust", "text@EDGE"),
    ("diffEditor.unchangedRegionBackground", "mantle", None),
    ("diffEditor.unchangedRegionForeground", "overlay1", None),
    ("diffEditor.unchangedRegionShadow", "shadow@45", "shadow@10"),
    ("diffEditor.unchangedCodeBackground", "text@L1", None),
    ("diffEditor.move.border", "overlay1@60", None),
    ("diffEditor.moveActive.border", "orange", None),
    ("diffEditorOverview.insertedForeground", "green@60", None),
    ("diffEditorOverview.removedForeground", "red_hi@60", None),
    ("editorGutter.addedBackground", "green", None),
    ("editorGutter.modifiedBackground", "yellow", None),
    ("editorGutter.deletedBackground", "red_hi", None),
    ("editorGutter.addedSecondaryBackground", "green@50", None),
    ("editorGutter.modifiedSecondaryBackground", "yellow@50", None),
    ("editorGutter.deletedSecondaryBackground", "red_hi@50", None),
    ("minimapGutter.addedBackground", "green@70", None),
    ("minimapGutter.modifiedBackground", "yellow@70", None),
    ("minimapGutter.deletedBackground", "red_hi@70", None),
    ("editorOverviewRuler.addedForeground", "green@70", None),
    ("editorOverviewRuler.modifiedForeground", "yellow@70", None),
    ("editorOverviewRuler.deletedForeground", "red_hi@70", None),
    ("merge.currentHeaderBackground", "green@35", "green@30"),
    ("merge.currentContentBackground", "green@12", None),
    ("merge.incomingHeaderBackground", "denim@35", "denim@30"),
    ("merge.incomingContentBackground", "denim@12", None),
    ("merge.commonHeaderBackground", "text@20", "text@16"),
    ("merge.commonContentBackground", "text@6", "text@5"),
    ("merge.border", "text@EDGE", None),
    ("mergeEditor.conflict.input1.background", "green@12", None),
    ("mergeEditor.conflict.input2.background", "denim@12", None),
    ("mergeEditor.conflict.handledFocused.border", "text@40", None),
    ("mergeEditor.conflict.handledUnfocused.border", "text@20", None),
    ("mergeEditor.conflict.handled.minimapOverViewRuler", "text@40", None),
    ("mergeEditor.conflict.unhandledFocused.border", "orange", None),
    ("mergeEditor.conflict.unhandledUnfocused.border", "orange@50", None),
    ("mergeEditor.conflict.unhandled.minimapOverViewRuler", "orange", None),
    ("multiDiffEditor.background", "base", None),
    ("multiDiffEditor.headerBackground", "mantle", None),
    ("multiDiffEditor.border", "crust", "text@EDGE"),
    ("git.blame.editorDecorationForeground", "overlay1", None),
    ("scmGraph.historyItemRefColor", "orange", None),
    ("scmGraph.historyItemRemoteRefColor", "denim", None),
    ("scmGraph.historyItemBaseRefColor", "sage", None),
    ("scmGraph.historyItemHoverDefaultLabelBackground", "text@L3", None),
    ("scmGraph.historyItemHoverDefaultLabelForeground", "text", None),
    ("scmGraph.historyItemHoverLabelForeground", *ON_ACCENT),
    ("scmGraph.historyItemHoverAdditionsForeground", "green", None),
    ("scmGraph.historyItemHoverDeletionsForeground", "red_hi", None),
    *((f"scmGraph.foreground{i}", c, None) for i, c in enumerate(("yellow", "orange", "green", "sage", "clay"), 1)),
    ("gitDecoration.addedResourceForeground", "green_hi", None),
    ("gitDecoration.modifiedResourceForeground", "yellow", None),
    ("gitDecoration.deletedResourceForeground", "red_hi", None),
    ("gitDecoration.renamedResourceForeground", "sage", None),
    ("gitDecoration.untrackedResourceForeground", "green", None),
    ("gitDecoration.ignoredResourceForeground", "overlay0", None),
    ("gitDecoration.conflictingResourceForeground", "orange", None),
    ("gitDecoration.submoduleResourceForeground", "denim", None),
    ("gitDecoration.stageModifiedResourceForeground", "yellow_hi", "yellow"),
    ("gitDecoration.stageDeletedResourceForeground", "red_hi", None),
    # ── terminal
    ("terminal.background", "mantle", None),
    ("terminal.foreground", "text", None),
    ("terminal.border", "crust", "text@EDGE"),
    ("terminal.findMatchBorder", "orange@80", "orange"),
    ("terminal.findMatchHighlightBorder", "transparent", None),
    ("terminal.hoverHighlightBackground", "text@L2", None),
    ("terminal.initialHintForeground", "overlay0", None),
    ("terminalCursor.foreground", "yellow", "orange"),
    ("terminalCursor.background", "crust", "base"),
    ("terminalStickyScroll.background", "mantle", None),
    ("terminalStickyScrollHover.background", "text@L1", None),
    ("terminalCommandDecoration.defaultBackground", "overlay0", None),
    ("terminalCommandDecoration.successBackground", "green", None),
    ("terminalCommandDecoration.errorBackground", "red_hi", None),
    ("terminalCommandGuide.foreground", "text@L3", None),
    ("ports.iconRunningProcessForeground", "green", None),
    # ── notebooks
    ("notebook.editorBackground", "base", None),
    ("notebook.cellEditorBackground", "mantle", None),
    ("notebook.cellBorderColor", "text@L2", None),
    ("notebook.cellHoverBackground", "text@3", None),
    ("notebook.focusedCellBackground", "text@L1", None),
    ("notebook.focusedCellBorder", "orange@50", "orange@60"),
    ("notebook.focusedEditorBorder", "orange@50", "orange@60"),
    ("notebook.inactiveFocusedCellBorder", "text@L3", None),
    ("notebook.selectedCellBackground", "text@L1", None),
    ("notebook.selectedCellBorder", "text@L3", None),
    ("notebook.inactiveSelectedCellBorder", "text@L3", None),
    ("notebook.cellInsertionIndicator", "orange", None),
    ("notebook.cellStatusBarItemHoverBackground", "text@L2", None),
    ("notebook.cellToolbarSeparator", "text@L3", None),
    ("notebook.outputContainerBackgroundColor", "mantle", None),
    ("notebook.outputContainerBorderColor", "text@L2", None),
    ("notebook.symbolHighlightBackground", "text@L2", None),
    ("notebookStatusSuccessIcon.foreground", "green", None),
    ("notebookStatusErrorIcon.foreground", "red_hi", "red"),
    ("notebookStatusRunningIcon.foreground", "yellow", None),
    ("notebookEditorOverviewRuler.runningCellForeground", "yellow", None),
    ("interactive.activeCodeBorder", "orange@50", None),
    ("interactive.inactiveCodeBorder", "text@L3", None),
    # ── debug / testing / coverage
    ("debugIcon.breakpointForeground", "red_hi", "red"),
    ("debugIcon.breakpointDisabledForeground", "overlay0", None),
    ("debugIcon.breakpointUnverifiedForeground", "overlay1", None),
    ("debugIcon.breakpointCurrentStackframeForeground", "yellow", None),
    ("debugIcon.breakpointStackframeForeground", "green", None),
    ("debugIcon.startForeground", "green", None),
    ("debugIcon.continueForeground", "green", None),
    ("debugIcon.pauseForeground", "yellow", None),
    ("debugIcon.stopForeground", "red_hi", "red"),
    ("debugIcon.disconnectForeground", "red_hi", "red"),
    ("debugIcon.restartForeground", "green", None),
    ("debugIcon.stepOverForeground", "denim", None),
    ("debugIcon.stepIntoForeground", "denim", None),
    ("debugIcon.stepOutForeground", "denim", None),
    ("debugIcon.stepBackForeground", "denim", None),
    ("debugConsole.infoForeground", "denim", None),
    ("debugConsole.warningForeground", "yellow", None),
    ("debugConsole.errorForeground", "red_hi", "red"),
    ("debugConsole.sourceForeground", "subtext0", None),
    ("debugConsoleInputIcon.foreground", "orange", None),
    ("debugView.exceptionLabelBackground", "red", None),
    ("debugView.exceptionLabelForeground", *ON_ACCENT),
    ("debugView.stateLabelBackground", "text@L3", None),
    ("debugView.stateLabelForeground", "text", None),
    ("debugView.valueChangedHighlight", "yellow@30", None),
    ("debugTokenExpression.name", "subtext1", None),
    ("debugTokenExpression.value", "text", None),
    ("debugTokenExpression.string", "green", None),
    ("debugTokenExpression.number", "red_hi", None),
    ("debugTokenExpression.boolean", "red_hi", None),
    ("debugTokenExpression.type", "sage", None),
    ("debugTokenExpression.error", "red_hi", "red"),
    ("testing.runAction", "green", None),
    ("testing.iconPassed", "green", None),
    ("testing.iconFailed", "red_hi", "red"),
    ("testing.iconErrored", "red_hi", "red"),
    ("testing.iconQueued", "yellow", None),
    ("testing.iconSkipped", "overlay1", None),
    ("testing.iconUnset", "overlay0", None),
    ("testing.iconPassed.retired", "green@60", None),
    ("testing.iconFailed.retired", "red_hi@60", "red@60"),
    ("testing.iconErrored.retired", "red_hi@60", "red@60"),
    ("testing.iconQueued.retired", "yellow@60", None),
    ("testing.iconSkipped.retired", "overlay1@60", None),
    ("testing.iconUnset.retired", "overlay0@60", None),
    ("testing.peekBorder", "red_hi", "red"),
    ("testing.peekHeaderBackground", "red@12", None),
    ("testing.messagePeekBorder", "denim", None),
    ("testing.messagePeekHeaderBackground", "denim@14", None),
    ("testing.message.error.badgeBackground", "red_hi", "red"),
    ("testing.message.error.badgeBorder", "red_hi", "red"),
    ("testing.message.error.badgeForeground", *ON_ACCENT),
    ("testing.message.error.lineBackground", "red@12", None),
    ("testing.message.info.decorationForeground", "overlay1", None),
    ("testing.message.info.lineBackground", "denim@14", None),
    ("testing.coveredBackground", "green@12", "green@16"),
    ("testing.coveredBorder", "transparent", None),
    ("testing.coveredGutterBackground", "green@50", None),
    ("testing.coveredMinimapBackground", "green@50", None),
    ("testing.uncoveredBackground", "red@12", None),
    ("testing.uncoveredBorder", "transparent", None),
    ("testing.uncoveredBranchBackground", "red@26", "red@20"),
    ("testing.uncoveredGutterBackground", "red_hi@50", None),
    ("testing.uncoveredMinimapBackground", "red_hi@50", None),
    ("testing.coverCountBadgeBackground", "text@L3", None),
    ("testing.coverCountBadgeForeground", "text", None),
    # ── settings, welcome, markdown and chrome text
    ("settings.headerForeground", "text_hi", None),
    ("settings.modifiedItemIndicator", "orange", None),
    ("settings.focusedRowBackground", "text@L1", None),
    ("settings.rowHoverBackground", "text@3", None),
    ("welcomePage.tileBackground", "text@L1", None),
    ("welcomePage.tileHoverBackground", "text@L2", None),
    ("welcomePage.tileBorder", "text@L2", None),
    ("welcomePage.progress.background", "text@L3", None),
    ("welcomePage.progress.foreground", "orange", None),
    ("walkthrough.stepTitle.foreground", "text_hi", None),
    ("textLink.foreground", "denim", None),
    ("textLink.activeForeground", "denim_hi", "denim"),
    ("textPreformat.foreground", "green", None),
    ("textPreformat.background", "text@L2", None),
    ("textPreformat.border", "transparent", None),
    ("textCodeBlock.background", "text@L2", None),
    ("textBlockQuote.background", "text@L1", None),
    ("textBlockQuote.border", "orange@60", None),
    ("textSeparator.foreground", "text@L3", None),
    ("search.resultsInfoForeground", "overlay1", None),
    ("charts.foreground", "text", None),
    ("charts.lines", "text@L3", None),
    ("charts.red", "red_hi", None),
    ("charts.orange", "orange", None),
    ("charts.yellow", "yellow", None),
    ("charts.green", "green", None),
    ("charts.blue", "denim", None),
    ("charts.purple", "clay", None),
    ("chart.axis", "text@40", None),
    ("chart.guide", "text@20", None),
    ("chart.line", "orange", None),
]

# Foregrounds that go with the layered grounds.
LAYERS += [
    ("foreground", "subtext1", None),
    ("disabledForeground", "overlay0", None),
    ("descriptionForeground", "overlay1", None),
    ("strongForeground", "text_hi", None),
    ("editor.foreground", "text", None),
    ("sideBar.foreground", "subtext0", None),
    ("sideBarTitle.foreground", "subtext1", None),
    ("sideBarSectionHeader.foreground", "subtext1", None),
    ("panelSectionHeader.foreground", "subtext1", None),
    ("tab.activeForeground", "text_hi", None),
    ("tab.inactiveForeground", "overlay1", None),
    ("tab.hoverForeground", "text", None),
    ("tab.unfocusedActiveForeground", "subtext0", None),
    ("tab.unfocusedInactiveForeground", "overlay0", None),
    ("tab.activeModifiedBorder", "yellow", None),
    ("tab.inactiveModifiedBorder", "yellow@50", None),
    ("tab.unfocusedActiveModifiedBorder", "yellow@50", None),
    ("tab.unfocusedInactiveModifiedBorder", "yellow@30", None),
    ("list.activeSelectionForeground", "text_hi", None),
    ("list.activeSelectionIconForeground", "text_hi", None),
    ("list.inactiveSelectionForeground", "text", None),
    ("list.hoverForeground", "text", None),
    ("list.highlightForeground", "yellow", None),
    ("list.focusHighlightForeground", "yellow_hi", "yellow"),
    ("titleBar.activeForeground", "subtext0", None),
    ("titleBar.inactiveForeground", "overlay0", None),
    ("statusBar.foreground", "subtext0", None),
    ("statusBar.noFolderForeground", "subtext0", None),
    ("statusBar.debuggingForeground", "text_hi", None),
    ("activityBar.foreground", "text", None),
    ("activityBar.inactiveForeground", "overlay1", None),
    ("activityBarTop.foreground", "text", None),
    ("activityBarTop.inactiveForeground", "overlay1", None),
    ("activityBarBadge.foreground", *ON_ACCENT),
    ("badge.foreground", "text_hi", None),
    ("button.secondaryForeground", "text", None),
    ("statusBarItem.errorForeground", "red_hi", "red"),
    ("statusBarItem.warningForeground", "yellow", None),
    ("statusBarItem.prominentForeground", "text_hi", None),
    ("panelTitle.activeForeground", "text_hi", None),
    ("panelTitle.inactiveForeground", "overlay1", None),
    ("quickInput.foreground", "text", None),
    ("quickInputList.focusForeground", "text_hi", None),
    ("quickInputList.focusIconForeground", "text_hi", None),
    ("quickInputList.focusHighlightForeground", "yellow_hi", "yellow"),
    ("menu.foreground", "text", None),
    ("menu.selectionForeground", "text_hi", None),
    ("editorSuggestWidget.foreground", "subtext1", None),
    ("editorSuggestWidget.selectedForeground", "text_hi", None),
    ("editorSuggestWidget.selectedIconForeground", "text_hi", None),
    ("editorSuggestWidget.highlightForeground", "yellow", None),
    ("editorSuggestWidget.focusHighlightForeground", "yellow_hi", "yellow"),
    ("notifications.foreground", "text", None),
    ("input.foreground", "text", None),
    ("input.placeholderForeground", "overlay0", None),
    ("inputOption.activeForeground", "text_hi", None),
    ("dropdown.foreground", "text", None),
    ("keybindingLabel.foreground", "text", None),
    ("breadcrumb.foreground", "overlay1", None),
    ("breadcrumb.focusForeground", "text", None),
    ("breadcrumb.activeSelectionForeground", "yellow", None),
    ("editorCursor.foreground", "yellow", "orange"),
    ("editorCursor.background", "crust", "base"),
    ("icon.foreground", "subtext0", None),
]

# Chat, inline chat and inline edits (VS Code's own AI surfaces).
LAYERS += [
    ("chat.requestBackground", "text@L1", None),
    ("chat.requestBorder", "text@L2", None),
    ("chat.requestBubbleBackground", "text@L2", None),
    ("chat.requestBubbleHoverBackground", "text@L3", None),
    ("chat.requestCodeBorder", "orange@40", None),
    ("chat.checkpointSeparator", "text@L3", None),
    ("chat.slashCommandBackground", "orange@18", "orange@14"),
    ("chat.slashCommandForeground", "orange", None),
    ("chat.avatarBackground", "text@L3", None),
    ("chat.avatarForeground", "text", None),
    ("chat.editedFileForeground", "yellow", None),
    ("chat.linesAddedForeground", "green", None),
    ("chat.linesRemovedForeground", "red_hi", "red"),
    ("chat.thinkingShimmer", "text_hi", None),
    ("chat.inputWorkingBorderColor1", "orange", None),
    ("chat.inputWorkingBorderColor2", "yellow", None),
    ("chat.inputWorkingBorderColor3", "clay", None),
    ("agentsChatInput.background", "base", "paper"),
    ("agentsChatInput.border", "text@10", "text@EDGE"),
    ("agentsChatInput.focusBorder", "orange@50", "orange@60"),
    ("agentsChatInput.foreground", "text", None),
    ("agentsChatInput.placeholderForeground", "overlay0", None),
    ("agentsPanel.background", "mantle", None),
    ("agentsPanel.border", "crust", "text@EDGE"),
    ("agentsPanel.foreground", "subtext1", None),
    ("agentsVoice.speakingBackground", "orange@8", None),
    ("agentsVoice.speakingForeground", "orange", None),
    ("inlineChat.background", "paper", None),
    ("inlineChat.border", "text@EDGE", None),
    ("inlineChat.shadow", "shadow@60", "shadow@14"),
    ("inlineChat.foreground", "text", None),
    ("inlineChatInput.background", "base", "paper"),
    ("inlineChatInput.border", "text@10", "text@EDGE"),
    ("inlineChatInput.focusBorder", "orange@50", "orange@60"),
    ("inlineChatInput.placeholderForeground", "overlay0", None),
    ("inlineEdit.originalBorder", "red_hi@50", None),
    ("inlineEdit.modifiedBorder", "green@50", None),
    ("inlineEdit.tabWillAcceptOriginalBorder", "orange", None),
    ("inlineEdit.tabWillAcceptModifiedBorder", "orange", None),
    ("inlineEdit.gutterIndicator.background", "mantle", None),
    ("inlineEdit.gutterIndicator.primaryBackground", "orange@20", "orange@16"),
    ("inlineEdit.gutterIndicator.primaryBorder", "orange", None),
    ("inlineEdit.gutterIndicator.primaryForeground", "orange", None),
    ("inlineEdit.gutterIndicator.secondaryBackground", "text@L3", None),
    ("inlineEdit.gutterIndicator.secondaryBorder", "text@L4", None),
    ("inlineEdit.gutterIndicator.secondaryForeground", "subtext1", None),
    ("inlineEdit.gutterIndicator.successfulBackground", "green@20", "green@16"),
    ("inlineEdit.gutterIndicator.successfulBorder", "green", None),
    ("inlineEdit.gutterIndicator.successfulForeground", "green", None),
]

# Symbol icons (outline, breadcrumbs, suggest, terminal suggest), following the syntax roles.
LAYERS += [
    (f"symbolIcon.{kind}Foreground", role, None)
    for kind, role in [
        ("array", "clay"), ("boolean", "red_hi"), ("class", "sage"), ("color", "clay"),
        ("constant", "red_hi"), ("constructor", "sage"), ("enumerator", "sage"),
        ("enumeratorMember", "red_hi"), ("event", "clay"), ("field", "subtext1"), ("file", "text"),
        ("folder", "yellow"), ("function", "yellow"), ("interface", "sage"), ("key", "orange"),
        ("keyword", "orange"), ("method", "yellow"), ("module", "subtext0"), ("namespace", "subtext0"),
        ("null", "red_hi"), ("number", "red_hi"), ("object", "sage"), ("operator", "overlay2"),
        ("package", "subtext0"), ("property", "subtext1"), ("reference", "denim"), ("snippet", "clay"),
        ("string", "green"), ("struct", "sage"), ("text", "text"), ("typeParameter", "sage"),
        ("unit", "red_hi"), ("variable", "text"),
    ]
]
LAYERS += [
    (f"terminalSymbolIcon.{kind}", role, None)
    for kind, role in [
        ("aliasForeground", "clay"), ("argumentForeground", "subtext1"), ("branchForeground", "sage"),
        ("commitForeground", "yellow"), ("fileForeground", "text"), ("flagForeground", "orange"),
        ("folderForeground", "yellow"), ("inlineSuggestionForeground", "overlay1"),
        ("methodForeground", "yellow"), ("optionForeground", "orange"), ("optionValueForeground", "green"),
        ("pullRequestForeground", "green"), ("pullRequestDoneForeground", "clay"),
        ("remoteForeground", "denim"), ("stashForeground", "clay"),
        ("symbolicLinkFileForeground", "denim"), ("symbolicLinkFolderForeground", "denim"),
        ("symbolText", "text"), ("tagForeground", "clay"),
    ]
]

# Keys the VS Code forks add for their own AI panels. VS Code ignores them;
# the $schema squiggles them when you open a theme file, which is expected.
FORKS = [
    # Cursor
    ("editorWatermark.foreground", "overlay0", None),
    ("tab.worktreeBorder", "sage", None),
    # Windsurf (the Cascade diff grounds are in `recipes`)
    ("list.hoverBackground.subtle", "text@3", None),
    ("starkButton.background", *BUTTON),
    ("starkButton.foreground", *ON_ACCENT),
    ("starkButton.hoverBackground", "orange_hi", "orange"),
    ("windsurf.black", "crust", None),
    ("windsurf.sea", "orange", None),
    ("windsurf.sea.shade", "mix(orange,base,0.7)", None),
    ("windsurf.sea.tint", "orange_hi", None),
    ("windsurf.sessionStatus.blue", "denim", None),
    ("windsurf.sessionStatus.green", "green", None),
    ("windsurf.sessionStatus.orange", "orange", None),
    ("windsurf.sessionStatus.purple", "clay", None),
    ("windsurf.sessionStatus.red", "red_hi", "red"),
    # Kiro
    ("accent", "orange", None),
    ("background.gradientStart", "mantle", None),
    ("background.gradientEnd", "base", None),
    ("activityBar.activeGradientStart", "orange", None),
    ("activityBar.activeGradientEnd", "yellow", None),
    ("button.gradient", "orange", None),
    ("alertButton.background", "yellow", None),
    ("alertButton.foreground", *ON_ACCENT),
    ("alertButton.hoverBackground", "yellow_hi", None),
    ("alertButton.hoverForeground", *ON_ACCENT),
    ("alertButton.secondaryBackground", "text@L3", None),
    ("alertButton.secondaryForeground", "text", None),
    ("alertButton.secondaryHoverBackground", "text@L4", None),
    ("alertButton.secondaryHoverForeground", "text_hi", None),
    ("autonomyToggle.background", "text@L2", None),
    ("autonomyToggle.foreground", "subtext1", None),
    ("autonomyToggle.selectedBackground", "orange@20", "orange@16"),
    ("autonomyToggle.selectedIconForeground", "orange", None),
    ("autonomyToggle.selectedGradientStart", "orange", None),
    ("autonomyToggle.selectedGradientEnd", "yellow", None),
    ("inlineDiffToolbar.hotkeyBackground", "text@L3", None),
    ("inlineDiffToolbar.hotkeyForeground", "text", None),
    ("keybindingLabel.shadow", "shadow@45", "shadow@10"),
    ("panelTitle.activeBackground", "text@L1", None),
    ("quickInput.overlayBackground", "shadow@50", "shadow@20"),
]

# Colors popular extensions contribute: GitLens, Error Lens, GitHub Pull Requests.
EXTENSIONS = [
    ("gitlens.gutterBackgroundColor", "text@L1", None),
    ("gitlens.gutterForegroundColor", "subtext0", None),
    ("gitlens.gutterUncommittedForegroundColor", "yellow", None),
    ("gitlens.trailingLineBackgroundColor", "transparent", None),
    ("gitlens.trailingLineForegroundColor", "overlay1", None),
    ("gitlens.lineHighlightBackgroundColor", "yellow@12", "yellow@16"),
    ("gitlens.lineHighlightOverviewRulerColor", "yellow@70", None),
    ("gitlens.openAutolinkedIssueIconColor", "green", None),
    ("gitlens.closedAutolinkedIssueIconColor", "clay", None),
    ("gitlens.openPullRequestIconColor", "green", None),
    ("gitlens.closedPullRequestIconColor", "red_hi", "red"),
    ("gitlens.mergedPullRequestIconColor", "clay", None),
    ("gitlens.unpublishedChangesIconColor", "green", None),
    ("gitlens.unpublishedCommitIconColor", "green", None),
    ("gitlens.unpulledChangesIconColor", "orange", None),
    ("gitlens.decorations.addedForegroundColor", "green", None),
    ("gitlens.decorations.copiedForegroundColor", "green", None),
    ("gitlens.decorations.deletedForegroundColor", "red_hi", None),
    ("gitlens.decorations.ignoredForegroundColor", "overlay0", None),
    ("gitlens.decorations.modifiedForegroundColor", "yellow", None),
    ("gitlens.decorations.renamedForegroundColor", "sage", None),
    ("gitlens.decorations.untrackedForegroundColor", "green", None),
    ("gitlens.decorations.branchAheadForegroundColor", "green", None),
    ("gitlens.decorations.branchBehindForegroundColor", "orange", None),
    ("gitlens.decorations.branchDivergedForegroundColor", "yellow", None),
    ("gitlens.decorations.branchUnpublishedForegroundColor", "green", None),
    ("gitlens.decorations.branchMissingUpstreamForegroundColor", "orange", None),
    ("gitlens.decorations.statusMergingOrRebasingConflictForegroundColor", "red_hi", "red"),
    ("gitlens.decorations.statusMergingOrRebasingForegroundColor", "yellow", None),
    ("gitlens.decorations.workspaceRepoMissingForegroundColor", "overlay1", None),
    ("gitlens.decorations.workspaceCurrentForegroundColor", "orange", None),
    ("gitlens.decorations.workspaceRepoOpenForegroundColor", "orange", None),
    ("gitlens.decorations.worktreeHasUncommittedChangesForegroundColor", "yellow", None),
    ("gitlens.decorations.worktreeMissingForegroundColor", "red_hi", "red"),
    ("gitlens.decorations.branchUpToDateForegroundColor", "subtext0", None),
    ("gitlens.decorations.statusPausedOperationReadyForegroundColor", "green", None),
    ("gitlens.timelineAdditionsColor", "green", None),
    ("gitlens.timelineDeletionsColor", "red_hi", None),
    ("gitlens.launchpadIndicatorMergeableColor", "green", None),
    ("gitlens.launchpadIndicatorMergeableHoverColor", "green_hi", "green"),
    ("gitlens.launchpadIndicatorBlockedColor", "red_hi", "red"),
    ("gitlens.launchpadIndicatorBlockedHoverColor", "red_hi", "red"),
    ("gitlens.launchpadIndicatorAttentionColor", "yellow", None),
    ("gitlens.launchpadIndicatorAttentionHoverColor", "yellow_hi", "yellow"),
    *((f"gitlens.graphLane{i}Color", c, None) for i, c in enumerate(
        ("orange", "yellow", "sage", "clay", "green", "denim", "orange_hi", "yellow_hi", "sage_hi", "red_hi"), 1)),
    ("gitlens.graphChangesColumnAddedColor", "green", None),
    ("gitlens.graphChangesColumnDeletedColor", "red_hi", None),
    *((f"gitlens.graph{kind}Marker{what}Color", c, None)
      for kind in ("Minimap", "Scroll")
      for what, c in (("Head", "yellow"), ("Upstream", "sage"), ("Highlights", "orange"),
                      ("LocalBranches", "green"), ("RemoteBranches", "denim"), ("Stashes", "clay"),
                      ("Tags", "red_hi"))),
    ("gitlens.graphMinimapMarkerPullRequestsColor", "orange_hi", None),
    ("gitlens.graphScrollMarkerPullRequestsColor", "orange_hi", None),
    ("gitlens.graphMinimapMarkerWorktreeColor", "clay", None),
    ("gitlens.graphScrollMarkerMergeTargetColor", "denim_hi", None),
    ("gitlens.graphScrollMarkerPinnedColor", "sage_hi", None),
    ("gitlens.graphScrollMarkerWipColor", "yellow_hi", None),
    *((f"errorLens.{lvl}{part}", f"{c}@12" if "Background" in part else c, None)
      for lvl, c in (("error", "red"), ("warning", "yellow"), ("info", "denim"), ("hint", "sage"))
      for part in ("Background", "BackgroundLight", "MessageBackground")),
    *((f"errorLens.{lvl}{part}", c, None)
      for lvl, c in (("error", "red_hi"), ("warning", "yellow"), ("info", "denim"), ("hint", "sage"))
      for part in ("Foreground", "ForegroundLight")),
    *((f"errorLens.{lvl}RangeBackground", f"{c}@10", None)
      for lvl, c in (("error", "red"), ("warning", "yellow"), ("info", "denim"), ("hint", "sage"))),
    ("errorLens.statusBarErrorForeground", "red_hi", "red"),
    ("errorLens.statusBarWarningForeground", "yellow", None),
    ("errorLens.statusBarInfoForeground", "denim", None),
    ("errorLens.statusBarHintForeground", "sage", None),
    ("errorLens.statusBarIconErrorForeground", "red_hi", "red"),
    ("errorLens.statusBarIconWarningForeground", "yellow", None),
    ("pullRequests.open", "green", None),
    ("pullRequests.merged", "clay", None),
    ("pullRequests.closed", "red_hi", "red"),
    ("pullRequests.draft", "overlay1", None),
    ("pullRequests.notification", "orange", None),
    ("issues.open", "green", None),
    ("issues.closed", "clay", None),
    ("github.issues.closed", "clay", None),
    ("issues.newIssueDecoration", "overlay1", None),
]


def layered(f):
    rows = LAYERS + FORKS + EXTENSIONS
    return {key: resolve(light if (light and not f.dark) else dark, f) for key, dark, light in rows}


def recipes(f):
    """The shared editor recipes, glazed: on the editor ground each lands on
    exactly the color every other editor port uses, and stays translucent."""
    u, t = ui(f), tints(f)

    def g(color, over="base"):
        return glaze(f, color, over)

    add, rm = g(t["add"]), g(t["del"])
    # a changed word sits on its line's tint, so glaze it over that tint
    add_word, rm_word = g(t["add_emph"], t["add"]), g(t["del_emph"], t["del"])
    return {
        # selection
        "editor.selectionBackground": g(u["selection"]),
        "editor.inactiveSelectionBackground": g(u["selection_inactive"]),
        "terminal.selectionBackground": g(u["selection"], "mantle"),
        "terminal.inactiveSelectionBackground": g(u["selection_inactive"], "mantle"),
        # matches: every hit on the search tint, the current one on search_cur with text_hi
        "editor.findMatchBackground": g(u["search_cur"]),
        "editor.findMatchForeground": u["search_cur_fg"],
        "editor.findMatchHighlightBackground": g(u["search"]),
        "searchEditor.findMatchBackground": g(u["search"]),
        "searchEditor.findMatchBorder": "#00000000",
        "editor.symbolHighlightBackground": g(u["search"]),
        "peekViewEditor.matchHighlightBackground": g(u["search"], "mantle"),
        "peekViewResult.matchHighlightBackground": g(u["search"], "mantle"),
        "terminal.findMatchBackground": g(u["search_cur"], "mantle"),
        "terminal.findMatchHighlightBackground": g(u["search"], "mantle"),
        "list.filterMatchBackground": g(u["search"], "mantle"),
        # the matching bracket
        "editorBracketMatch.foreground": u["bracket_fg"],
        "editorBracketMatch.background": g(u["bracket_bg"]),
        "editorBracketMatch.border": "#00000000",
        # diffs: line tints, words stronger on top, syntax colors kept
        "diffEditor.insertedLineBackground": add,
        "diffEditor.removedLineBackground": rm,
        "diffEditor.insertedTextBackground": add_word,
        "diffEditor.removedTextBackground": rm_word,
        "diffEditorGutter.insertedLineBackground": add,
        "diffEditorGutter.removedLineBackground": rm,
        "mergeEditor.change.background": add,
        "mergeEditor.change.word.background": add_word,
        "mergeEditor.changeBase.background": rm,
        "mergeEditor.changeBase.word.background": rm_word,
        "mergeEditor.conflictingLines.background": g(t["chg"]),
        "inlineEdit.originalBackground": rm,
        "inlineEdit.modifiedBackground": add,
        "inlineEdit.originalChangedLineBackground": rm,
        "inlineEdit.originalChangedTextBackground": rm_word,
        "inlineEdit.modifiedChangedLineBackground": add,
        "inlineEdit.modifiedChangedTextBackground": add_word,
        "inlineChatDiff.inserted": add_word,
        "inlineChatDiff.removed": rm_word,
        "editorMinimap.inlineChatInserted": g(t["add_emph"]),
        # Windsurf's Cascade diffs
        "diffEditor.insertedTextBackgroundCustom": add_word,
        "diffEditor.insertedTextBackgroundFallback": add_word,
        "diffEditor.removedTextBackgroundCustom": rm_word,
        "diffEditor.removedTextBackgroundFallback": rm_word,
        "diffEditor.windsurfRemovedTextBackground": rm_word,
    }


ANSI = ["Black", "Red", "Green", "Yellow", "Blue", "Magenta", "Cyan", "White"]


def font(styles):
    return " ".join(s for s in ("italic", "bold", "underline", "strikethrough") if s in styles)


def theme(f):
    colors = layered(f)
    colors.update(recipes(f))
    for i, name in enumerate(ANSI):
        colors[f"terminal.ansi{name}"] = f.ansi[i]
        colors[f"terminal.ansiBright{name}"] = f.ansi[i + 8]

    token_colors = []
    for scope, color, st in [*scope_rules(f), *extra_scope_rules(f)]:
        s = {"foreground": color}
        if font(st):
            s["fontStyle"] = font(st)
        token_colors.append({"scope": [x.strip() for x in scope.split(",")], "settings": s})

    def sem(role):
        color, st = f.syntax(role)
        return {"foreground": color, "fontStyle": font(st)} if st else color

    semantic = {
        "namespace": sem("namespace"),
        "type": sem("type"), "class": sem("type"), "interface": sem("type"),
        "enum": sem("type"), "struct": sem("type"),
        "typeParameter": {"foreground": f.sage, "fontStyle": "italic"},
        "type.defaultLibrary": sem("type.builtin"),
        "class.builtin:python": sem("type.builtin"),
        "variable.typeHint:python": sem("type"),
        "function": sem("function"), "method": sem("function"),
        "function.defaultLibrary": sem("function.builtin"),
        "macro": sem("decorator"), "decorator": sem("decorator"),
        "function.decorator:python": sem("decorator"),
        "builtinAttribute.attribute.library:rust": sem("decorator"),
        "parameter": sem("parameter"),
        "property": sem("property"),
        "enumMember": sem("constant"),
        "variable": sem("variable"),
        "variable.defaultLibrary": sem("variable.builtin"),
        "variable.readonly.defaultLibrary": sem("constant"),
        "selfKeyword": sem("variable.builtin"), "selfParameter": sem("variable.builtin"),
        "builtinConstant": sem("constant"),
        "keyword": sem("keyword"), "string": sem("string"), "number": sem("number"),
        "boolean": sem("boolean"),
        "regexp": sem("regexp"), "comment": sem("comment"), "label": sem("decorator"),
        "tomlArrayKey": sem("function"), "tomlTableKey": sem("function"),
        "heading": sem("heading"), "text.emph": sem("emphasis"), "text.strong": sem("strong"),
        "*.deprecated": {"fontStyle": "strikethrough"},
    }
    # TypeScript marks every `const` readonly; keep those plain variables, not constants.
    for lang in ("javascript", "typescript", "javascriptreact", "typescriptreact"):
        semantic[f"variable.readonly:{lang}"] = sem("variable")
        semantic[f"property.readonly:{lang}"] = sem("property")
    return {
        "$schema": "vscode://schemas/color-theme",
        "name": f.name,
        "type": "dark" if f.dark else "light",
        "semanticHighlighting": True,
        "colors": colors,
        "tokenColors": token_colors,
        "semanticTokenColors": semantic,
    }


KEYWORDS = ["theme", "dark", "light", "brown", "retro", "70s", "warm", "vintage", "subway seat"]


def package():
    return {
        "name": "subway-seat",
        "displayName": "Subway Seat",
        "description": "Walnut-brown 1970s NYC subway theme: parchment text, harvest gold, burnt orange, "
        "avocado. Dark, deep dark and light.",
        "version": VERSION,
        "publisher": "oddurs",
        "license": "MIT",
        "icon": "icon.png",
        "galleryBanner": {"color": p.DEFAULT.base, "theme": "dark"},
        "repository": {"type": "git", "url": REPO},
        "homepage": REPO,
        "bugs": {"url": f"{REPO}/issues"},
        "engines": {"vscode": "^1.85.0"},
        "categories": ["Themes"],
        "keywords": KEYWORDS,
        "contributes": {
            "themes": [
                {"label": f.name, "uiTheme": "vs-dark" if f.dark else "vs", "path": f"./themes/{f.slug}-color-theme.json"}
                for f in p.FLAVORS
            ]
        },
    }


SHOTS = "https://raw.githubusercontent.com/oddurs/subway-seat/main/assets/screenshots"

README = f"""# Subway Seat

A walnut-brown color theme from a 1970s subway car: parchment text, harvest gold, burnt orange and avocado, with orange bucket seats and wood paneling in mind.

![Subway Seat in VS Code]({SHOTS}/vscode.png)

- **Subway Seat**: Walnut, the original dark flavor
- **Subway Seat Tunnel**: the late local after midnight, a deeper dark
- **Subway Seat Enamel**: cream enamel panels in the morning sun, the light one

The workbench is layered on purpose: one chrome ground, grooves instead of lines, popovers lifted onto paper, and every hover and row a thin wash of text color, so they sit right on any surface. Selections, search matches and diffs use the same colors as the Neovim, JetBrains, Zed and other ports. It also themes the AI panels in VS Code, Cursor, Windsurf and Kiro, and the colors GitLens, Error Lens and GitHub Pull Requests contribute.

## Install

Pick **Preferences: Color Theme › Subway Seat** (or Tunnel, or Enamel). If you have the `.vsix` file:

```sh
code --install-extension {VSIX}
```

Cursor (`cursor`), Windsurf (`windsurf`) and VSCodium (`codium`) take the same flag, or use **Extensions › ⋯ › Install from VSIX…**.

## Follow the system's light and dark mode

```json
"window.autoDetectColorScheme": true,
"workbench.preferredDarkColorTheme": "Subway Seat",
"workbench.preferredLightColorTheme": "Subway Seat Enamel"
```

![Subway Seat Tunnel]({SHOTS}/vscode-tunnel.png)

![Subway Seat Enamel]({SHOTS}/vscode-enamel.png)

Subway Seat is available for over 100 apps, from Ghostty and Neovim to Claude Code: [github.com/oddurs/subway-seat](https://github.com/oddurs/subway-seat).
"""

CONTENT_TYPES = """<?xml version="1.0" encoding="utf-8"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension=".json" ContentType="application/json"/><Default Extension=".vsixmanifest" ContentType="text/xml"/><Default Extension=".md" ContentType="text/markdown"/><Default Extension=".png" ContentType="image/png"/><Default Extension=".txt" ContentType="text/plain"/></Types>
"""


def vsix_manifest(pkg):
    from xml.sax.saxutils import escape

    props = {
        "Microsoft.VisualStudio.Code.Engine": pkg["engines"]["vscode"],
        "Microsoft.VisualStudio.Code.ExtensionDependencies": "",
        "Microsoft.VisualStudio.Code.ExtensionPack": "",
        "Microsoft.VisualStudio.Code.ExtensionKind": "ui,workspace,web",
        "Microsoft.VisualStudio.Code.LocalizedLanguages": "",
        "Microsoft.VisualStudio.Services.Links.Source": REPO,
        "Microsoft.VisualStudio.Services.Links.GitHub": REPO,
        "Microsoft.VisualStudio.Services.Links.Support": f"{REPO}/issues",
        "Microsoft.VisualStudio.Services.Links.Learn": REPO,
        "Microsoft.VisualStudio.Services.Branding.Color": pkg["galleryBanner"]["color"],
        "Microsoft.VisualStudio.Services.Branding.Theme": pkg["galleryBanner"]["theme"],
        "Microsoft.VisualStudio.Services.GitHubFlavoredMarkdown": "true",
        "Microsoft.VisualStudio.Services.Content.Pricing": "Free",
    }
    prop_xml = "".join(f'<Property Id="{k}" Value="{escape(v)}" />' for k, v in props.items())
    tags = ",".join(dict.fromkeys([*pkg["keywords"], "color-theme", "__web_extension"]))
    return f"""<?xml version="1.0" encoding="utf-8"?>
<PackageManifest Version="2.0.0" xmlns="http://schemas.microsoft.com/developer/vsx-schema/2011" xmlns:d="http://schemas.microsoft.com/developer/vsx-schema-design/2011">
  <Metadata>
    <Identity Language="en-US" Id="{pkg['name']}" Version="{pkg['version']}" Publisher="{pkg['publisher']}" />
    <DisplayName>{escape(pkg['displayName'])}</DisplayName>
    <Description xml:space="preserve">{escape(pkg['description'])}</Description>
    <Tags>{escape(tags)}</Tags>
    <Categories>Themes</Categories>
    <GalleryFlags>Public</GalleryFlags>
    <Properties>{prop_xml}</Properties>
    <License>extension/LICENSE.txt</License>
    <Icon>extension/icon.png</Icon>
  </Metadata>
  <Installation><InstallationTarget Id="Microsoft.VisualStudio.Code"/></Installation>
  <Dependencies/>
  <Assets>
    <Asset Type="Microsoft.VisualStudio.Code.Manifest" Path="extension/package.json" Addressable="true" />
    <Asset Type="Microsoft.VisualStudio.Services.Content.Details" Path="extension/README.md" Addressable="true" />
    <Asset Type="Microsoft.VisualStudio.Services.Content.Changelog" Path="extension/CHANGELOG.md" Addressable="true" />
    <Asset Type="Microsoft.VisualStudio.Services.Content.License" Path="extension/LICENSE.txt" Addressable="true" />
    <Asset Type="Microsoft.VisualStudio.Services.Icons.Default" Path="extension/icon.png" Addressable="true" />
  </Assets>
</PackageManifest>
"""


def build(flavors):
    """The extension folder, as `vsce package` would read it, plus the ready-to-install
    VSIX built from it (deterministic, so `vsce publish --packagePath` can ship it)."""
    pkg = package()
    folder = {
        "package.json": json.dumps(pkg, indent=2) + "\n",
        "README.md": README,
        "CHANGELOG.md": (ROOT / "CHANGELOG.md").read_text(encoding="utf-8"),
        "LICENSE.txt": (ROOT / "LICENSE").read_text(encoding="utf-8"),
        "icon.png": (ROOT / "assets" / "icon.png").read_bytes(),
        ".vscodeignore": "*.vsix\n",
        **{f"themes/{f.slug}-color-theme.json": json.dumps(theme(f), indent=2) + "\n" for f in flavors},
    }
    vsix = zip_bytes({
        "[Content_Types].xml": CONTENT_TYPES,
        "extension.vsixmanifest": vsix_manifest(pkg),
        **{f"extension/{path}": body for path, body in folder.items() if path != ".vscodeignore"},
    })
    packaged = "packaged in subway-seat.vsix"
    outs = []
    for path, body in folder.items():
        flavor = next((f.id for f in flavors if path == f"themes/{f.slug}-color-theme.json"), None)
        lang = "json" if path.endswith(".json") else "text"
        outs.append(Out(path, body, flavor=flavor, lang=lang, how=packaged if path.startswith("themes/") else None))
    outs.append(Out(VSIX, vsix, how="code --install-extension subway-seat.vsix, or Extensions › ⋯ › Install from VSIX…"))
    return outs
