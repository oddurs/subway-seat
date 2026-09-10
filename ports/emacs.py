"""Emacs: three custom themes sharing one palette table and one face list (MELPA-ready)."""

import palette as p
from ports._editors import ui
from ports._lib import HEADER, REPO, VERSION, Out, tints

META = {
    "id": "emacs",
    "name": "Emacs",
    "category": "Editors",
    "homepage": "https://www.gnu.org/software/emacs/",
    "enable": {
        "where": "init.el, with the three files on `load-path` and `custom-theme-load-path` (or installed as a package)",
        "code": "(load-theme '{slug} t)",
        "lang": "elisp",
    },
    "notes": "Three themes in one package, for Emacs 27.1 and later. They cover the tree-sitter font-lock faces "
    "and org, magit, vertico, corfu, company and which-key.",
}

AUTHOR = "Oddur Sigurdsson"
YEAR = 2026


def el(role):
    """palette role → elisp alist key (text_hi → text-hi)."""
    return role.replace("_", "-")


def palette_alist(f):
    """Every color a face can name, as (key . "#hex") pairs."""
    t, u = tints(f), ui(f)
    pairs = [(el(r), f.colors[r]) for r in p.ROLES]
    pairs += [
        ("ink", u["ink"]), ("cursor", u["cursor"]), ("hl-line", u["line"]), ("region", u["selection"]),
        ("line-nr", u["line_nr"]), ("line-nr-cur", u["line_nr_cur"]),
        ("bg-add", t["add"]), ("bg-add-hl", p.blend(t["add_emph"], t["add"], 0.35)), ("bg-add-emph", t["add_emph"]),
        ("bg-del", t["del"]), ("bg-del-hl", p.blend(t["del_emph"], t["del"], 0.35)), ("bg-del-emph", t["del_emph"]),
        ("bg-chg", t["chg"]), ("bg-chg-emph", t["chg_emph"]),
        ("bg-info", t["info"]), ("bg-hint", t["hint"]),
        ("bg-search", t["search"]), ("bg-search-cur", t["search_cur"]),
        ("bg-inlay", f.mix("surface0", "base", 0.6)),
    ]
    pairs += [(f"ansi{i}", c) for i, c in enumerate(f.ansi)]
    width = max(len(k) for k, _ in pairs)
    body = "\n     ".join(f'({k + " " * (width - len(k))} . "{v}")' for k, v in pairs)
    return f"    ({f.slug}\n     {body})"


def syn(role):
    """Face attributes for a palette.SYNTAX role, naming colors by key."""
    color, styles = p.SYNTAX[role]
    s = f":foreground ,.{el(color)}"
    if "italic" in styles:
        s += " :slant italic"
    if "bold" in styles:
        s += " :weight bold"
    return s


def wave(key):
    return f":underline (:style wave :color ,.{key})"


HEADINGS = ["orange", "yellow", "green", "sage", "clay", "subtext1", "orange", "yellow"]
RAINBOW = ["yellow", "orange", "sage", "clay", "green", "subtext1", "yellow", "orange", "sage"]
ANSI = ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]

# (face, attributes). Colors are alist keys bound by `subway-seat-theme-with-colors`.
FACES = [
    # ── basics ──
    ("default", ":foreground ,.text :background ,.base"),
    ("cursor", ":background ,.cursor"),
    ("region", ":background ,.region :extend t"),
    ("secondary-selection", ":background ,.surface1 :extend t"),
    ("hl-line", ":background ,.hl-line :extend t"),
    ("highlight", ":background ,.surface1"),
    ("shadow", ":foreground ,.overlay1"),
    ("fringe", ":foreground ,.overlay0 :background ,.base"),
    ("line-number", ":foreground ,.line-nr :background ,.base"),
    ("line-number-current-line", ":inherit line-number :foreground ,.line-nr-cur :weight bold"),
    ("vertical-border", ":foreground ,.crust"),
    ("window-divider", ":foreground ,.crust"),
    ("window-divider-first-pixel", ":foreground ,.crust"),
    ("window-divider-last-pixel", ":foreground ,.crust"),
    ("child-frame-border", ":background ,.surface2"),
    ("minibuffer-prompt", ":foreground ,.orange :weight bold"),
    ("mode-line", ":foreground ,.subtext1 :background ,.mantle"),
    ("mode-line-inactive", ":foreground ,.overlay0 :background ,.crust"),
    ("mode-line-buffer-id", ":foreground ,.text-hi :weight bold"),
    ("mode-line-emphasis", ":foreground ,.yellow :weight bold"),
    ("mode-line-highlight", ":foreground ,.text-hi :background ,.surface1"),
    ("header-line", ":foreground ,.subtext0 :background ,.mantle"),
    ("header-line-highlight", ":inherit mode-line-highlight"),
    ("tooltip", ":foreground ,.text :background ,.mantle"),
    ("tab-bar", ":foreground ,.overlay1 :background ,.crust"),
    ("tab-bar-tab", ":foreground ,.text-hi :background ,.base :weight bold"),
    ("tab-bar-tab-inactive", ":foreground ,.overlay1 :background ,.crust"),
    ("tab-line", ":foreground ,.overlay1 :background ,.crust"),
    ("tab-line-tab", ":foreground ,.subtext0 :background ,.mantle"),
    ("tab-line-tab-current", ":foreground ,.text-hi :background ,.base :weight bold"),
    ("tab-line-tab-inactive", ":foreground ,.overlay1 :background ,.crust"),
    ("tab-line-highlight", ":background ,.surface0"),
    ("link", ":foreground ,.denim :underline t"),
    ("link-visited", ":foreground ,.denim-hi :underline t"),
    ("button", ":inherit link"),
    ("escape-glyph", ":foreground ,.clay"),
    ("homoglyph", ":foreground ,.clay"),
    ("nobreak-space", ":foreground ,.clay :underline t"),
    ("nobreak-hyphen", ":foreground ,.clay"),
    ("trailing-whitespace", ":background ,.bg-del"),
    ("fill-column-indicator", ":foreground ,.surface0"),
    ("error", ":foreground ,.red-hi :weight bold"),
    ("warning", ":foreground ,.yellow :weight bold"),
    ("success", ":foreground ,.green :weight bold"),
    ("match", ":background ,.bg-search"),
    ("isearch", ":foreground ,.text-hi :background ,.bg-search-cur :weight bold"),
    ("isearch-fail", ":foreground ,.red-hi :background ,.bg-del"),
    ("lazy-highlight", ":background ,.bg-search"),
    ("query-replace", ":inherit isearch"),
    ("show-paren-match", ":foreground ,.yellow-hi :background ,.surface1 :weight bold"),
    ("show-paren-match-expression", ":background ,.surface0"),
    ("show-paren-mismatch", ":foreground ,.ink :background ,.red-hi :weight bold"),
    ("completions-common-part", ":foreground ,.yellow :weight bold"),
    ("completions-first-difference", ":foreground ,.text-hi :weight bold"),
    ("completions-annotations", ":foreground ,.overlay1 :slant italic"),
    ("completions-group-title", ":foreground ,.orange :slant italic"),
    ("completions-highlight", ":background ,.surface1"),
    ("help-key-binding", ":foreground ,.yellow :background ,.surface0 :box (:line-width -1 :color ,.surface1)"),
    ("help-argument-name", syn("parameter")),
    ("widget-field", ":foreground ,.text :background ,.surface0"),
    ("widget-single-line-field", ":inherit widget-field"),
    ("custom-group-tag", ":foreground ,.orange :weight bold"),
    ("custom-variable-tag", ":foreground ,.yellow :weight bold"),
    ("custom-state", ":foreground ,.green"),
    ("pulse-highlight-start-face", ":background ,.surface2"),
    ("whitespace-space", ":foreground ,.surface1"),
    ("whitespace-hspace", ":foreground ,.surface1"),
    ("whitespace-tab", ":foreground ,.surface1"),
    ("whitespace-newline", ":foreground ,.surface1"),
    ("whitespace-trailing", ":foreground ,.red-hi :background ,.bg-del"),
    ("whitespace-line", ":background ,.bg-chg"),
    ("whitespace-empty", ":background ,.bg-chg"),
    ("whitespace-indentation", ":foreground ,.yellow :background ,.bg-chg"),
    ("whitespace-space-before-tab", ":foreground ,.yellow :background ,.bg-chg"),
    ("whitespace-space-after-tab", ":foreground ,.yellow :background ,.bg-chg"),
    ("whitespace-big-indent", ":background ,.bg-del"),
    ("whitespace-missing-newline-at-eof", ":background ,.bg-chg"),
    # ── font-lock (the Emacs 29 tree-sitter faces are harmless on 27/28) ──
    ("font-lock-comment-face", syn("comment")),
    ("font-lock-comment-delimiter-face", ":inherit font-lock-comment-face"),
    ("font-lock-doc-face", ":foreground ,.green :slant italic"),
    ("font-lock-doc-markup-face", ":foreground ,.clay"),
    ("font-lock-string-face", syn("string")),
    ("font-lock-keyword-face", syn("keyword")),
    ("font-lock-builtin-face", syn("function.builtin")),
    ("font-lock-function-name-face", syn("function")),
    ("font-lock-function-call-face", syn("function")),
    ("font-lock-variable-name-face", syn("variable")),
    ("font-lock-variable-use-face", syn("variable")),
    ("font-lock-type-face", syn("type")),
    ("font-lock-constant-face", syn("constant")),
    ("font-lock-number-face", syn("number")),
    ("font-lock-operator-face", syn("operator")),
    ("font-lock-property-name-face", syn("property")),
    ("font-lock-property-use-face", syn("property")),
    ("font-lock-punctuation-face", syn("punctuation")),
    ("font-lock-bracket-face", syn("punctuation")),
    ("font-lock-delimiter-face", syn("punctuation")),
    ("font-lock-misc-punctuation-face", ":foreground ,.clay"),
    ("font-lock-escape-face", syn("string.escape")),
    ("font-lock-regexp-face", syn("regexp")),
    ("font-lock-regexp-grouping-backslash", syn("string.escape")),
    ("font-lock-regexp-grouping-construct", syn("regexp")),
    ("font-lock-preprocessor-face", ":foreground ,.clay"),
    ("font-lock-negation-char-face", syn("operator")),
    ("font-lock-warning-face", ":foreground ,.yellow :weight bold"),
    *((f"rainbow-delimiters-depth-{i + 1}-face", f":foreground ,.{c}") for i, c in enumerate(RAINBOW)),
    ("rainbow-delimiters-unmatched-face", ":foreground ,.red-hi :weight bold"),
    ("rainbow-delimiters-mismatched-face", ":foreground ,.red-hi :weight bold"),
    # ── diagnostics: flycheck, flymake, compilation, eglot, lsp-mode ──
    ("flycheck-error", wave("red-hi")),
    ("flycheck-warning", wave("yellow")),
    ("flycheck-info", wave("denim")),
    ("flycheck-fringe-error", ":foreground ,.red-hi"),
    ("flycheck-fringe-warning", ":foreground ,.yellow"),
    ("flycheck-fringe-info", ":foreground ,.denim"),
    ("flycheck-error-list-error", ":foreground ,.red-hi"),
    ("flycheck-error-list-warning", ":foreground ,.yellow"),
    ("flycheck-error-list-info", ":foreground ,.denim"),
    ("flycheck-error-list-highlight", ":background ,.surface1"),
    ("flycheck-error-list-line-number", ":foreground ,.overlay0"),
    ("flycheck-error-list-column-number", ":foreground ,.overlay0"),
    ("flycheck-error-list-id", ":foreground ,.overlay1"),
    ("flymake-error", wave("red-hi")),
    ("flymake-warning", wave("yellow")),
    ("flymake-note", wave("denim")),
    ("compilation-error", ":foreground ,.red-hi :weight bold"),
    ("compilation-warning", ":foreground ,.yellow :weight bold"),
    ("compilation-info", ":foreground ,.green"),
    ("compilation-line-number", ":foreground ,.overlay1"),
    ("compilation-column-number", ":foreground ,.overlay1"),
    ("compilation-mode-line-exit", ":foreground ,.green :weight bold"),
    ("compilation-mode-line-fail", ":foreground ,.red-hi :weight bold"),
    ("compilation-mode-line-run", ":foreground ,.yellow"),
    ("eglot-highlight-symbol-face", ":background ,.surface1"),
    ("eglot-inlay-hint-face", ":foreground ,.overlay1 :background ,.bg-inlay :slant italic"),
    ("eglot-parameter-hint-face", ":inherit eglot-inlay-hint-face"),
    ("eglot-type-hint-face", ":inherit eglot-inlay-hint-face"),
    ("eglot-diagnostic-tag-unnecessary-face", ":foreground ,.overlay1"),
    ("eglot-diagnostic-tag-deprecated-face", ":strike-through t"),
    ("lsp-face-highlight-textual", ":background ,.surface1"),
    ("lsp-face-highlight-read", ":background ,.surface1"),
    ("lsp-face-highlight-write", ":background ,.surface1 :underline t"),
    ("lsp-inlay-hint-face", ":foreground ,.overlay1 :background ,.bg-inlay :slant italic"),
    # ── completion: vertico, orderless, marginalia, consult, corfu, company, ivy ──
    ("vertico-current", ":foreground ,.text-hi :background ,.surface1 :weight bold :extend t"),
    ("vertico-group-title", ":foreground ,.orange :slant italic"),
    ("vertico-group-separator", ":foreground ,.surface2 :strike-through t"),
    ("vertico-multiline", ":foreground ,.overlay1"),
    ("orderless-match-face-0", ":foreground ,.yellow :weight bold"),
    ("orderless-match-face-1", ":foreground ,.orange :weight bold"),
    ("orderless-match-face-2", ":foreground ,.sage :weight bold"),
    ("orderless-match-face-3", ":foreground ,.clay :weight bold"),
    ("marginalia-documentation", ":foreground ,.overlay1 :slant italic"),
    ("marginalia-key", ":foreground ,.yellow"),
    ("consult-preview-line", ":background ,.hl-line :extend t"),
    ("consult-file", ":foreground ,.subtext1"),
    ("corfu-default", ":foreground ,.subtext1 :background ,.mantle"),
    ("corfu-current", ":foreground ,.text-hi :background ,.surface1 :weight bold"),
    ("corfu-border", ":background ,.surface2"),
    ("corfu-bar", ":background ,.overlay0"),
    ("corfu-annotations", ":foreground ,.overlay1 :slant italic"),
    ("corfu-deprecated", ":foreground ,.overlay0 :strike-through t"),
    ("company-tooltip", ":foreground ,.subtext1 :background ,.mantle"),
    ("company-tooltip-selection", ":foreground ,.text-hi :background ,.surface1 :weight bold"),
    ("company-tooltip-common", ":foreground ,.yellow :weight bold"),
    ("company-tooltip-common-selection", ":foreground ,.yellow-hi :weight bold"),
    ("company-tooltip-annotation", ":foreground ,.overlay1 :slant italic"),
    ("company-tooltip-annotation-selection", ":foreground ,.subtext0"),
    ("company-tooltip-search", ":foreground ,.ink :background ,.yellow"),
    ("company-tooltip-search-selection", ":foreground ,.ink :background ,.yellow"),
    ("company-tooltip-mouse", ":background ,.surface0"),
    ("company-tooltip-scrollbar-thumb", ":background ,.overlay0"),
    ("company-tooltip-scrollbar-track", ":background ,.surface0"),
    ("company-scrollbar-fg", ":background ,.overlay0"),
    ("company-scrollbar-bg", ":background ,.surface0"),
    ("company-preview", ":foreground ,.overlay0 :slant italic"),
    ("company-preview-common", ":foreground ,.overlay1 :slant italic"),
    ("company-echo-common", ":foreground ,.yellow"),
    ("ivy-current-match", ":foreground ,.text-hi :background ,.surface1 :weight bold :extend t"),
    ("ivy-minibuffer-match-face-1", ":foreground ,.overlay1"),
    ("ivy-minibuffer-match-face-2", ":foreground ,.yellow :weight bold"),
    ("ivy-minibuffer-match-face-3", ":foreground ,.orange :weight bold"),
    ("ivy-minibuffer-match-face-4", ":foreground ,.sage :weight bold"),
    ("ivy-subdir", ":foreground ,.yellow"),
    ("ivy-remote", ":foreground ,.denim"),
    # ── keys & motion: which-key, transient, avy, evil ──
    ("which-key-key-face", ":foreground ,.yellow"),
    ("which-key-separator-face", ":foreground ,.overlay0"),
    ("which-key-group-description-face", ":foreground ,.orange"),
    ("which-key-command-description-face", ":foreground ,.subtext1"),
    ("which-key-local-map-description-face", ":foreground ,.sage"),
    ("which-key-special-key-face", ":foreground ,.clay :weight bold"),
    ("which-key-highlighted-command-face", ":foreground ,.text-hi :underline t"),
    ("which-key-note-face", ":foreground ,.overlay1 :slant italic"),
    ("which-key-docstring-face", ":foreground ,.overlay1 :slant italic"),
    ("transient-heading", ":foreground ,.orange :weight bold"),
    ("transient-key", ":foreground ,.yellow"),
    ("transient-value", ":foreground ,.green"),
    ("transient-inactive-argument", ":foreground ,.overlay0"),
    ("transient-inactive-value", ":foreground ,.overlay0"),
    ("transient-unreachable", ":foreground ,.overlay0"),
    ("transient-enabled-suffix", ":foreground ,.ink :background ,.green :weight bold"),
    ("transient-disabled-suffix", ":foreground ,.ink :background ,.red-hi :weight bold"),
    ("avy-lead-face", ":foreground ,.ink :background ,.orange :weight bold"),
    ("avy-lead-face-0", ":foreground ,.ink :background ,.yellow :weight bold"),
    ("avy-lead-face-1", ":foreground ,.text-hi :background ,.surface2"),
    ("avy-lead-face-2", ":foreground ,.ink :background ,.clay :weight bold"),
    ("avy-background-face", ":foreground ,.overlay0"),
    ("evil-ex-search", ":inherit isearch"),
    ("evil-ex-lazy-highlight", ":inherit lazy-highlight"),
    ("evil-ex-substitute-matches", ":foreground ,.red-hi :strike-through t"),
    ("evil-ex-substitute-replacement", ":foreground ,.green :weight bold"),
    # ── version control: magit, diff, smerge, ediff, diff-hl, git-gutter ──
    ("magit-section-heading", syn("heading")),
    ("magit-section-heading-selection", ":foreground ,.orange :weight bold"),
    ("magit-section-secondary-heading", ":foreground ,.sage :weight bold"),
    ("magit-section-highlight", ":background ,.hl-line :extend t"),
    ("magit-branch-local", ":foreground ,.yellow"),
    ("magit-branch-current", ":foreground ,.yellow :weight bold"),
    ("magit-branch-remote", ":foreground ,.sage"),
    ("magit-branch-remote-head", ":foreground ,.sage :weight bold"),
    ("magit-head", ":foreground ,.yellow :weight bold"),
    ("magit-tag", ":foreground ,.clay"),
    ("magit-hash", ":foreground ,.overlay1"),
    ("magit-dimmed", ":foreground ,.overlay0"),
    ("magit-filename", ":foreground ,.subtext1"),
    ("magit-keyword", ":foreground ,.orange"),
    ("magit-diff-added", ":foreground ,.green :background ,.bg-add :extend t"),
    ("magit-diff-added-highlight", ":foreground ,.green-hi :background ,.bg-add-hl :extend t"),
    ("magit-diff-removed", ":foreground ,.red-hi :background ,.bg-del :extend t"),
    ("magit-diff-removed-highlight", ":foreground ,.red-hi :background ,.bg-del-hl :extend t"),
    ("magit-diff-context", ":foreground ,.overlay2 :extend t"),
    ("magit-diff-context-highlight", ":foreground ,.subtext0 :background ,.mantle :extend t"),
    ("magit-diff-hunk-heading", ":foreground ,.subtext1 :background ,.surface0 :extend t"),
    ("magit-diff-hunk-heading-highlight", ":foreground ,.text-hi :background ,.surface1 :weight bold :extend t"),
    ("magit-diff-hunk-heading-selection", ":inherit magit-diff-hunk-heading-highlight :foreground ,.orange"),
    ("magit-diff-file-heading", ":foreground ,.text :weight bold"),
    ("magit-diff-file-heading-highlight", ":inherit magit-section-highlight"),
    ("magit-diff-lines-heading", ":foreground ,.ink :background ,.orange :extend t"),
    ("magit-diffstat-added", ":foreground ,.green"),
    ("magit-diffstat-removed", ":foreground ,.red-hi"),
    ("magit-log-author", ":foreground ,.clay"),
    ("magit-log-date", ":foreground ,.overlay1"),
    ("magit-log-graph", ":foreground ,.overlay1"),
    ("magit-process-ok", ":foreground ,.green :weight bold"),
    ("magit-process-ng", ":foreground ,.red-hi :weight bold"),
    ("magit-blame-heading", ":foreground ,.subtext0 :background ,.surface0 :extend t"),
    ("magit-blame-highlight", ":foreground ,.subtext0 :background ,.surface0 :extend t"),
    ("magit-signature-good", ":foreground ,.green"),
    ("magit-signature-bad", ":foreground ,.red-hi :weight bold"),
    ("magit-signature-untrusted", ":foreground ,.yellow"),
    ("magit-mode-line-process", ":foreground ,.yellow"),
    ("diff-added", ":foreground ,.green :background ,.bg-add :extend t"),
    ("diff-removed", ":foreground ,.red-hi :background ,.bg-del :extend t"),
    ("diff-changed", ":foreground ,.yellow :background ,.bg-chg :extend t"),
    ("diff-refine-added", ":background ,.bg-add-emph"),
    ("diff-refine-removed", ":background ,.bg-del-emph"),
    ("diff-refine-changed", ":background ,.bg-chg-emph"),
    ("diff-indicator-added", ":foreground ,.green"),
    ("diff-indicator-removed", ":foreground ,.red-hi"),
    ("diff-indicator-changed", ":foreground ,.yellow"),
    ("diff-header", ":foreground ,.denim :background ,.mantle :extend t"),
    ("diff-file-header", ":foreground ,.denim :background ,.mantle :weight bold :extend t"),
    ("diff-hunk-header", ":foreground ,.denim :background ,.surface0 :extend t"),
    ("diff-context", ":foreground ,.subtext0"),
    ("diff-function", ":foreground ,.yellow"),
    ("diff-nonexistent", ":foreground ,.overlay0"),
    ("diff-error", ":foreground ,.red-hi :weight bold"),
    ("smerge-upper", ":background ,.bg-del :extend t"),
    ("smerge-lower", ":background ,.bg-add :extend t"),
    ("smerge-base", ":background ,.bg-chg :extend t"),
    ("smerge-markers", ":foreground ,.overlay1 :background ,.surface0 :extend t"),
    ("smerge-refined-added", ":background ,.bg-add-emph"),
    ("smerge-refined-removed", ":background ,.bg-del-emph"),
    ("ediff-current-diff-A", ":background ,.bg-del :extend t"),
    ("ediff-current-diff-B", ":background ,.bg-add :extend t"),
    ("ediff-current-diff-C", ":background ,.bg-chg :extend t"),
    ("ediff-fine-diff-A", ":background ,.bg-del-emph"),
    ("ediff-fine-diff-B", ":background ,.bg-add-emph"),
    ("ediff-fine-diff-C", ":background ,.bg-chg-emph"),
    ("ediff-even-diff-A", ":background ,.surface0"),
    ("ediff-even-diff-B", ":background ,.surface0"),
    ("ediff-even-diff-C", ":background ,.surface0"),
    ("ediff-odd-diff-A", ":background ,.surface0"),
    ("ediff-odd-diff-B", ":background ,.surface0"),
    ("ediff-odd-diff-C", ":background ,.surface0"),
    ("diff-hl-insert", ":foreground ,.green :background ,.bg-add"),
    ("diff-hl-delete", ":foreground ,.red-hi :background ,.bg-del"),
    ("diff-hl-change", ":foreground ,.yellow :background ,.bg-chg"),
    ("git-gutter:added", ":foreground ,.green"),
    ("git-gutter:deleted", ":foreground ,.red-hi"),
    ("git-gutter:modified", ":foreground ,.yellow"),
    ("git-gutter-fr:added", ":foreground ,.green"),
    ("git-gutter-fr:deleted", ":foreground ,.red-hi"),
    ("git-gutter-fr:modified", ":foreground ,.yellow"),
    # ── org ──
    *((f"org-level-{i + 1}", f":foreground ,.{c} :weight bold") for i, c in enumerate(HEADINGS)),
    ("org-document-title", ":foreground ,.text-hi :weight bold"),
    ("org-document-info", ":foreground ,.subtext0"),
    ("org-document-info-keyword", ":foreground ,.overlay1"),
    ("org-meta-line", ":foreground ,.overlay1 :slant italic"),
    ("org-block", ":background ,.mantle :extend t"),
    ("org-block-begin-line", ":foreground ,.overlay1 :background ,.mantle :slant italic :extend t"),
    ("org-block-end-line", ":inherit org-block-begin-line"),
    ("org-code", syn("code")),
    ("org-verbatim", ":foreground ,.clay"),
    ("org-quote", ":inherit org-block :foreground ,.subtext0 :slant italic"),
    ("org-verse", ":inherit org-quote"),
    ("org-date", ":foreground ,.clay :underline t"),
    ("org-todo", ":foreground ,.red-hi :weight bold"),
    ("org-done", ":foreground ,.green :weight bold"),
    ("org-headline-done", ":foreground ,.overlay1"),
    ("org-priority", ":foreground ,.orange"),
    ("org-link", ":inherit link"),
    ("org-footnote", ":foreground ,.clay"),
    ("org-target", ":underline t"),
    ("org-table", ":foreground ,.subtext1"),
    ("org-formula", ":foreground ,.clay"),
    ("org-tag", ":foreground ,.overlay1 :weight normal"),
    ("org-checkbox", ":foreground ,.yellow :weight bold"),
    ("org-checkbox-statistics-todo", ":foreground ,.yellow"),
    ("org-checkbox-statistics-done", ":foreground ,.green"),
    ("org-list-dt", ":foreground ,.yellow :weight bold"),
    ("org-special-keyword", ":foreground ,.overlay1"),
    ("org-drawer", ":foreground ,.overlay1"),
    ("org-property-value", ":foreground ,.subtext0"),
    ("org-ellipsis", ":foreground ,.overlay0 :underline nil"),
    ("org-hide", ":foreground ,.base"),
    ("org-archived", ":foreground ,.overlay0"),
    ("org-macro", ":foreground ,.clay"),
    ("org-latex-and-related", ":foreground ,.clay"),
    ("org-warning", ":foreground ,.yellow :weight bold"),
    ("org-scheduled", ":foreground ,.green"),
    ("org-scheduled-today", ":foreground ,.green-hi :weight bold"),
    ("org-scheduled-previously", ":foreground ,.yellow"),
    ("org-upcoming-deadline", ":foreground ,.orange"),
    ("org-time-grid", ":foreground ,.overlay0"),
    ("org-agenda-structure", ":foreground ,.orange :weight bold"),
    ("org-agenda-date", ":foreground ,.yellow"),
    ("org-agenda-date-today", ":foreground ,.yellow-hi :weight bold"),
    ("org-agenda-date-weekend", ":foreground ,.overlay2"),
    ("org-agenda-done", ":foreground ,.overlay1"),
    ("org-agenda-current-time", ":foreground ,.orange"),
    ("org-agenda-dimmed-todo-face", ":foreground ,.overlay0"),
    # ── markdown ──
    ("markdown-header-face", syn("heading")),
    *((f"markdown-header-face-{i + 1}", f":foreground ,.{c} :weight bold") for i, c in enumerate(HEADINGS[:6])),
    ("markdown-header-delimiter-face", ":foreground ,.overlay1"),
    ("markdown-code-face", ":background ,.mantle :extend t"),
    ("markdown-inline-code-face", ":foreground ,.green :background ,.mantle"),
    ("markdown-pre-face", syn("code")),
    ("markdown-language-keyword-face", ":foreground ,.overlay1 :slant italic"),
    ("markdown-link-face", ":foreground ,.sage"),
    ("markdown-url-face", ":foreground ,.denim :underline t"),
    ("markdown-plain-url-face", ":inherit markdown-url-face"),
    ("markdown-bold-face", syn("strong")),
    ("markdown-italic-face", syn("emphasis")),
    ("markdown-strike-through-face", ":foreground ,.overlay1 :strike-through t"),
    ("markdown-blockquote-face", syn("quote")),
    ("markdown-list-face", ":foreground ,.orange"),
    ("markdown-markup-face", ":foreground ,.overlay1"),
    ("markdown-table-face", ":foreground ,.subtext1"),
    ("markdown-hr-face", ":foreground ,.overlay0"),
    ("markdown-gfm-checkbox-face", ":foreground ,.yellow"),
    ("markdown-footnote-marker-face", ":foreground ,.clay"),
    ("markdown-metadata-key-face", ":foreground ,.sage"),
    ("markdown-metadata-value-face", ":foreground ,.subtext0"),
    # ── files & shells: dired, eshell, comint, info ──
    ("dired-directory", ":foreground ,.yellow"),
    ("dired-header", ":foreground ,.orange :weight bold"),
    ("dired-symlink", ":foreground ,.denim"),
    ("dired-broken-symlink", ":foreground ,.red-hi :background ,.bg-del"),
    ("dired-mark", ":foreground ,.orange :weight bold"),
    ("dired-marked", ":foreground ,.yellow-hi :weight bold"),
    ("dired-flagged", ":foreground ,.red-hi :weight bold"),
    ("dired-ignored", ":foreground ,.overlay0"),
    ("dired-perm-write", ":foreground ,.clay"),
    ("dired-set-id", ":foreground ,.clay"),
    ("dired-special", ":foreground ,.clay"),
    ("dired-warning", ":foreground ,.yellow"),
    ("eshell-prompt", ":foreground ,.orange :weight bold"),
    ("eshell-ls-directory", ":foreground ,.yellow :weight bold"),
    ("eshell-ls-executable", ":foreground ,.green"),
    ("eshell-ls-symlink", ":foreground ,.denim"),
    ("eshell-ls-archive", ":foreground ,.clay"),
    ("eshell-ls-backup", ":foreground ,.overlay0"),
    ("eshell-ls-clutter", ":foreground ,.overlay0"),
    ("eshell-ls-missing", ":foreground ,.red-hi"),
    ("eshell-ls-product", ":foreground ,.overlay1"),
    ("eshell-ls-readonly", ":foreground ,.overlay1"),
    ("eshell-ls-special", ":foreground ,.clay"),
    ("eshell-ls-unreadable", ":foreground ,.overlay0"),
    ("comint-highlight-prompt", ":foreground ,.orange :weight bold"),
    ("comint-highlight-input", ":weight bold"),
    ("info-title-1", ":foreground ,.orange :weight bold"),
    ("info-title-2", ":foreground ,.yellow :weight bold"),
    ("info-title-3", ":foreground ,.green :weight bold"),
    ("info-title-4", ":foreground ,.sage :weight bold"),
    ("info-menu-header", ":foreground ,.orange :weight bold"),
    ("info-menu-star", ":foreground ,.clay"),
    ("info-node", ":foreground ,.yellow :weight bold"),
    ("Info-quoted", syn("code")),
    # ── terminal colors: ansi-color (28+), term (27) ──
    *((f"ansi-color-{n}", f":foreground ,.ansi{i} :background ,.ansi{i}") for i, n in enumerate(ANSI)),
    *((f"ansi-color-bright-{n}", f":foreground ,.ansi{i + 8} :background ,.ansi{i + 8}") for i, n in enumerate(ANSI)),
    *((f"term-color-{n}", f":foreground ,.ansi{i} :background ,.ansi{i}") for i, n in enumerate(ANSI)),
    *((f"term-color-bright-{n}", f":foreground ,.ansi{i + 8} :background ,.ansi{i + 8}") for i, n in enumerate(ANSI)),
]


MIT = """\
;; Permission is hereby granted, free of charge, to any person obtaining a copy
;; of this software and associated documentation files (the "Software"), to deal
;; in the Software without restriction, including without limitation the rights
;; to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
;; copies of the Software, and to permit persons to whom the Software is
;; furnished to do so, subject to the following conditions:
;;
;; The above copyright notice and this permission notice shall be included in all
;; copies or substantial portions of the Software.
;;
;; THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
;; IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
;; FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
;; AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
;; LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
;; OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
;; SOFTWARE."""


def doc(f):
    """deftheme docstring: the name, then the blurb."""
    return f"{f.name}: {f.blurb}".replace('"', '\\"')


def main_file(flavors):
    faces = "\n      ".join(f"({face} ((t ({attrs}))))" for face, attrs in FACES)
    palettes = "\n".join(palette_alist(f) for f in flavors)
    themes = "\n\n".join(
        f'(deftheme {f.slug}\n  "{doc(f)}")\n(subway-seat-theme-apply \'{f.slug})' for f in flavors
    )
    ansi = " ".join(f",.ansi{i}" for i in range(8))
    return f""";;; subway-seat-theme.el --- A warm 1970s subway-car color theme -*- lexical-binding: t; -*-

;; Copyright (C) {YEAR} {AUTHOR}

;; Author: {AUTHOR}
;; URL: {REPO}
;; Version: {VERSION}
;; Package-Requires: ((emacs "27.1"))
;; Keywords: faces, theme
;; SPDX-License-Identifier: MIT

;; This file is not part of GNU Emacs.

{MIT}

;;; Commentary:

;; Subway Seat: walnut-brown ground, parchment text, harvest gold, burnt
;; orange, avocado, sage and faded denim -- a 1970s subway car with shag
;; carpet, kept relaxed.  Three themes share one palette table and one face
;; list:
;;
;;   `subway-seat'         Walnut, the original dark
;;   `subway-seat-tunnel'  Tunnel, a deeper dark
;;   `subway-seat-enamel'  Enamel, the light one
;;
;; Enable one with
;;
;;   (load-theme 'subway-seat t)
;;
;; To tweak a face with the theme's colors, bind them with
;; `subway-seat-theme-with-colors':
;;
;;   (subway-seat-theme-with-colors 'subway-seat
;;     (set-face-attribute 'hl-line nil :background .surface1))
;;
;; {HEADER}

;;; Code:

(defgroup subway-seat-theme nil
  "The Subway Seat color themes."
  :group 'faces
  :prefix "subway-seat-theme-"
  :link '(url-link "{REPO}"))

(defconst subway-seat-theme-palettes
  '(
{palettes})
  "Colors for each Subway Seat theme, keyed by theme name.
Each entry maps a color key (a palette role such as `base' or
`orange', or a derived ground such as `hl-line' or `bg-add') to a
hex string.")

(defmacro subway-seat-theme-with-colors (theme &rest body)
  "Evaluate BODY with the colors of THEME bound as `.KEY' symbols.
THEME is a symbol such as `subway-seat'; see
`subway-seat-theme-palettes' for the keys, e.g. `.base' or `.orange'."
  (declare (indent 1))
  `(let-alist (alist-get ,theme subway-seat-theme-palettes) ,@body))

(defun subway-seat-theme--faces (theme)
  "Return face specs for THEME, as arguments to `custom-theme-set-faces'."
  (subway-seat-theme-with-colors theme
    `({faces})))

(defun subway-seat-theme-apply (theme)
  "Record the faces and variables of THEME, one of the Subway Seat themes."
  (apply #'custom-theme-set-faces theme (subway-seat-theme--faces theme))
  (subway-seat-theme-with-colors theme
    (custom-theme-set-variables
     theme
     `(ansi-color-names-vector [{ansi}])
     `(pdf-view-midnight-colors '(,.text . ,.base)))))

;; The Tunnel and Enamel files `require' this one, so all three themes are
;; known once any of them is loaded.
{themes}

;;;###autoload
(when (and (boundp 'custom-theme-load-path) load-file-name)
  (add-to-list 'custom-theme-load-path
               (file-name-as-directory (file-name-directory load-file-name))))

(provide-theme 'subway-seat)

;;; subway-seat-theme.el ends here
"""


def flavor_file(f):
    return f""";;; {f.slug}-theme.el --- {f.name}, the {f.id.capitalize()} flavor -*- lexical-binding: t; -*-

;; Copyright (C) {YEAR} {AUTHOR}

;; Author: {AUTHOR}
;; URL: {REPO}
;; Version: {VERSION}
;; Package-Requires: ((emacs "27.1"))
;; SPDX-License-Identifier: MIT

;; This file is not part of GNU Emacs.

;;; Commentary:

;; {f.blurb}
;; The palette and faces live in subway-seat-theme.el; this file lets
;; `load-theme' find `{f.slug}'.
;;
;; {HEADER}

;;; Code:

(require 'subway-seat-theme)

(deftheme {f.slug}
  "{doc(f)}")

;; `load-theme' clears a theme's settings before loading its file, so record them again.
(subway-seat-theme-apply '{f.slug})

(provide-theme '{f.slug})

;;; {f.slug}-theme.el ends here
"""


def build(flavors):
    dest = "a directory on `load-path` and `custom-theme-load-path` (or install the package)"
    outs = []
    for f in flavors:
        if f.slug == "subway-seat":
            outs.append(Out("subway-seat-theme.el", main_file(flavors), flavor=f.id, dest=dest, lang="elisp"))
        else:
            outs.append(Out(f"{f.slug}-theme.el", flavor_file(f), flavor=f.id, dest=dest, lang="elisp"))
    return outs
