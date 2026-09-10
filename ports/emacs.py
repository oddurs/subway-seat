"""Emacs: three custom themes sharing one palette table and one face list (MELPA-ready)."""

import palette as p
from ports._editors import ui
from ports._lib import ANSI_NAMES, HEADER, REPO, VERSION, Out, tints

THEMES_DIR = "~/.config/emacs/themes/"

META = {
    "id": "emacs",
    "name": "Emacs",
    "category": "Editors",
    "homepage": "https://www.gnu.org/software/emacs/",
    "enable": {
        "where": f"init.el, with the three files in {THEMES_DIR}",
        "code": f"(add-to-list 'load-path \"{THEMES_DIR}\")\n"
        f"(add-to-list 'custom-theme-load-path \"{THEMES_DIR}\")\n"
        "(load-theme '{slug} t)",
        "lang": "elisp",
    },
    "auto": {
        "where": "init.el, with the auto-dark package from MELPA (it swaps the theme when the OS appearance changes)",
        "code": "(use-package auto-dark\n"
        "  :ensure t\n"
        "  :custom (auto-dark-themes '((subway-seat) (subway-seat-enamel)))\n"
        "  :init (auto-dark-mode))",
        "lang": "elisp",
    },
    "requires": "Emacs 27.1+",
    "detect": ["emacs", "/Applications/Emacs.app"],
    "notes": "Three themes in one package, covering the tree-sitter font-lock faces, org, magit, diff and ediff, "
    "vertico, corfu, company, helm, treemacs, lsp-ui, doom-modeline and more. To install straight from GitHub "
    "instead of copying files, use `(use-package subway-seat-theme :vc (:url "
    '"https://github.com/oddurs/subway-seat" :lisp-dir "dist/emacs" :rev :newest))` on Emacs 30+, or '
    "`(package-vc-install '(subway-seat-theme :url \"https://github.com/oddurs/subway-seat\" :lisp-dir "
    "\"dist/emacs\"))` on Emacs 29, then `(load-theme 'subway-seat t)`.",
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
        ("ink", u["ink"]), ("cursor", u["cursor"]), ("hl-line", u["line"]),
        ("region", u["selection"]), ("region-inactive", u["selection_inactive"]),
        ("line-nr", u["line_nr"]), ("line-nr-cur", u["line_nr_cur"]),
        ("bracket", u["bracket_fg"]), ("bracket-bg", u["bracket_bg"]),
        ("paper", u["paper"]), ("edge", u["edge"]), ("row", u["row"]),
        ("bg-add", t["add"]), ("bg-add-hl", p.blend(t["add_emph"], t["add"], 0.35)), ("bg-add-emph", t["add_emph"]),
        ("bg-del", t["del"]), ("bg-del-hl", p.blend(t["del_emph"], t["del"], 0.35)), ("bg-del-emph", t["del_emph"]),
        ("bg-chg", t["chg"]), ("bg-chg-emph", t["chg_emph"]),
        ("bg-error", u["error_bg"]), ("bg-warning", u["warning_bg"]), ("bg-info", u["info_bg"]), ("bg-hint", u["hint_bg"]),
        ("bg-search", u["search"]), ("bg-search-cur", u["search_cur"]),
        ("bg-inlay", u["inlay_bg"]),
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
CITED = ["sage", "clay", "denim", "overlay2"]


def hunk_fg(key):
    """A hunk-line foreground magit drops when `magit-diff-specify-hunk-foreground' is nil
    (set that and `magit-diff-fontify-hunk' to keep syntax colors on the diff grounds)."""
    return f",@(subway-seat-theme--hunk-fg .{key})"


# nerd-icons (and the doom-modeline icons that use them): the palette's hues, one family per name
NERD = {
    "red": "red-hi", "lred": "red-hi", "dred": "red", "red-alt": "red",
    "orange": "orange", "lorange": "orange-hi", "dorange": "orange",
    "yellow": "yellow", "lyellow": "yellow-hi", "dyellow": "yellow",
    "green": "green", "lgreen": "green-hi", "dgreen": "green",
    "cyan": "sage", "lcyan": "sage-hi", "dcyan": "sage", "cyan-alt": "sage-hi",
    "blue": "denim", "lblue": "denim-hi", "dblue": "denim", "blue-alt": "denim-hi",
    "maroon": "clay", "lmaroon": "clay", "dmaroon": "clay",
    "purple": "clay", "lpurple": "clay", "dpurple": "clay", "purple-alt": "clay",
    "pink": "clay", "lpink": "clay", "dpink": "clay",
    "silver": "subtext0", "lsilver": "subtext1", "dsilver": "overlay1",
}

# (face, attributes). Colors are alist keys bound by `subway-seat-theme-with-colors`.
FACES = [
    # ── basics ──
    ("default", ":foreground ,.text :background ,.base"),
    ("cursor", ":background ,.cursor"),
    ("region", ":background ,.region :extend t"),
    ("secondary-selection", ":background ,.region-inactive :extend t"),
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
    ("internal-border", ":background ,.crust"),
    ("child-frame-border", ":background ,.edge"),
    ("separator-line", ":height 0.1 :background ,.surface2"),
    ("minibuffer-prompt", ":foreground ,.orange :weight bold"),
    ("minibuffer-nonselected", ":foreground ,.text-hi :background ,.region-inactive"),
    ("mode-line", ":foreground ,.subtext1 :background ,.mantle"),
    ("mode-line-inactive", ":foreground ,.overlay0 :background ,.crust"),
    ("mode-line-buffer-id", ":foreground ,.text-hi :weight bold"),
    ("mode-line-emphasis", ":foreground ,.yellow :weight bold"),
    ("mode-line-highlight", ":foreground ,.text-hi :background ,.surface1"),
    ("header-line", ":foreground ,.subtext0 :background ,.mantle"),
    ("header-line-highlight", ":inherit mode-line-highlight"),
    ("tooltip", ":foreground ,.text :background ,.paper"),
    ("tty-menu-enabled-face", ":foreground ,.text :background ,.paper"),
    ("tty-menu-disabled-face", ":foreground ,.overlay0 :background ,.paper"),
    ("tty-menu-selected-face", ":foreground ,.text-hi :background ,.row :weight bold"),
    ("tab-bar", ":foreground ,.overlay1 :background ,.crust"),
    ("tab-bar-tab", ":foreground ,.text-hi :background ,.base :weight bold"),
    ("tab-bar-tab-inactive", ":foreground ,.overlay1 :background ,.crust"),
    ("tab-bar-tab-highlight", ":foreground ,.text-hi :background ,.surface1"),
    ("tab-bar-tab-group-current", ":inherit tab-bar-tab :foreground ,.orange"),
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
    ("trailing-whitespace", ":background ,.bg-error"),
    ("fill-column-indicator", ":foreground ,.surface0"),
    ("error", ":foreground ,.red-hi :weight bold"),
    ("warning", ":foreground ,.yellow :weight bold"),
    ("success", ":foreground ,.green :weight bold"),
    # ── search and matching parens: every match on the search tint, the current one stronger ──
    ("match", ":background ,.bg-search"),
    ("isearch", ":foreground ,.text-hi :background ,.bg-search-cur :weight bold"),
    ("isearch-fail", ":foreground ,.red-hi :background ,.bg-error"),
    ("isearch-group-1", ":foreground ,.text-hi :background ,.bg-add-emph :weight bold"),
    ("isearch-group-2", ":foreground ,.text-hi :background ,.bg-chg-emph :weight bold"),
    ("lazy-highlight", ":background ,.bg-search"),
    ("query-replace", ":inherit isearch"),
    ("pulse-highlight-start-face", ":background ,.bg-search"),
    ("pulse-highlight-face", ":background ,.bg-search"),
    ("show-paren-match", ":foreground ,.bracket :background ,.bracket-bg :weight bold"),
    ("show-paren-match-expression", ":background ,.bracket-bg"),
    ("show-paren-mismatch", ":foreground ,.ink :background ,.red-hi :weight bold"),
    # ── minibuffer completion and help ──
    ("completions-common-part", ":foreground ,.yellow :weight bold"),
    ("completions-first-difference", ":foreground ,.text-hi :weight bold"),
    ("completions-annotations", ":foreground ,.overlay1 :slant italic"),
    ("completions-group-title", ":foreground ,.orange :slant italic"),
    ("completions-highlight", ":background ,.surface1"),
    ("completion-preview", ":foreground ,.overlay1"),
    ("completion-preview-exact", ":inherit completion-preview-common :underline ,.green"),
    ("icomplete-selected-match", ":background ,.surface1"),
    ("help-key-binding", ":foreground ,.yellow :background ,.surface0 :box (:line-width -1 :color ,.surface1)"),
    ("help-argument-name", syn("parameter")),
    ("read-multiple-choice-face", ":inherit help-key-binding :weight bold :underline t"),
    # ── customize and widgets ──
    ("widget-field", ":foreground ,.text :background ,.surface0 :extend t"),
    ("widget-single-line-field", ":inherit widget-field"),
    ("widget-button", ":weight bold"),
    ("widget-button-pressed", ":foreground ,.orange"),
    ("widget-documentation", ":foreground ,.subtext0"),
    ("custom-group-tag", ":foreground ,.orange :weight bold :height 1.2"),
    ("custom-group-tag-1", ":foreground ,.yellow :weight bold :height 1.2"),
    ("custom-variable-tag", ":foreground ,.yellow :weight bold"),
    ("custom-variable-obsolete", ":foreground ,.overlay1"),
    ("custom-comment", ":foreground ,.subtext0 :background ,.surface0"),
    ("custom-comment-tag", ":foreground ,.overlay1"),
    ("custom-state", ":foreground ,.green"),
    ("custom-button", ":foreground ,.text :background ,.surface1 :box (:line-width 1 :color ,.surface2)"),
    ("custom-button-mouse", ":foreground ,.text-hi :background ,.surface2 :box (:line-width 1 :color ,.surface2)"),
    ("custom-button-pressed", ":foreground ,.text-hi :background ,.surface2 :box (:line-width 1 :color ,.orange)"),
    ("custom-changed", ":foreground ,.text-hi :background ,.bg-info"),
    ("custom-modified", ":foreground ,.text-hi :background ,.bg-info"),
    ("custom-themed", ":foreground ,.text-hi :background ,.bg-hint"),
    ("custom-set", ":foreground ,.text-hi :background ,.bg-hint"),
    ("custom-invalid", ":foreground ,.ink :background ,.red-hi"),
    ("custom-rogue", ":foreground ,.red-hi :background ,.crust"),
    # ── whitespace ──
    ("whitespace-space", ":foreground ,.surface1"),
    ("whitespace-hspace", ":foreground ,.surface1"),
    ("whitespace-tab", ":foreground ,.surface1"),
    ("whitespace-newline", ":foreground ,.surface1"),
    ("whitespace-trailing", ":foreground ,.red-hi :background ,.bg-error"),
    ("whitespace-line", ":background ,.bg-warning"),
    ("whitespace-empty", ":background ,.bg-warning"),
    ("whitespace-indentation", ":foreground ,.yellow :background ,.bg-warning"),
    ("whitespace-space-before-tab", ":foreground ,.yellow :background ,.bg-warning"),
    ("whitespace-space-after-tab", ":foreground ,.yellow :background ,.bg-warning"),
    ("whitespace-big-indent", ":background ,.bg-error"),
    ("whitespace-missing-newline-at-eof", ":background ,.bg-warning"),
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
    # shell scripts
    ("sh-heredoc", syn("string")),
    ("sh-quoted-exec", syn("string.escape")),
    # Emacs Lisp's semantic faces (Emacs 31); the rest inherit font-lock faces
    ("elisp-shorthand-font-lock-face", syn("namespace")),
    ("elisp-rx", syn("regexp")),
    ("elisp-condition", ":foreground ,.red-hi"),
    ("elisp-major-mode-name", syn("type")),
    ("elisp-unknown-call", ":inherit elisp-function :foreground ,.subtext1"),
    ("elisp-non-local-exit", ":inherit elisp-function :underline ,.red-hi"),
    ("elisp-symbol-role", ":inherit font-lock-function-call-face"),
    ("elisp-symbol-role-definition", ":inherit font-lock-function-name-face"),
    ("elisp-symbol-at-mouse", ":background ,.surface1"),
    # LSP semantic tokens (Emacs 31 eglot): macros and decorators read alike
    ("eglot-semantic-macro", syn("decorator")),
    ("eglot-semantic-decorator", syn("decorator")),
    *((f"rainbow-delimiters-depth-{i + 1}-face", f":foreground ,.{c}") for i, c in enumerate(RAINBOW)),
    ("rainbow-delimiters-unmatched-face", ":foreground ,.red-hi :weight bold"),
    ("rainbow-delimiters-mismatched-face", ":foreground ,.red-hi :weight bold"),
    ("hl-todo", ":weight bold"),
    # ── spelling and diagnostics: flyspell, flycheck, flymake, compilation, eglot, lsp-mode ──
    ("flyspell-incorrect", wave("red-hi")),
    ("flyspell-duplicate", wave("yellow")),
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
    ("flymake-error-echo-at-eol", ":foreground ,.red-hi :background ,.bg-error :height 0.85"),
    ("flymake-warning-echo-at-eol", ":foreground ,.yellow :background ,.bg-warning :height 0.85"),
    ("flymake-note-echo-at-eol", ":foreground ,.denim :background ,.bg-info :height 0.85"),
    ("compilation-error", ":foreground ,.red-hi :weight bold"),
    ("compilation-warning", ":foreground ,.yellow :weight bold"),
    ("compilation-info", ":foreground ,.green"),
    ("compilation-line-number", ":foreground ,.overlay1"),
    ("compilation-column-number", ":foreground ,.overlay1"),
    ("compilation-mode-line-exit", ":foreground ,.green :weight bold"),
    ("compilation-mode-line-fail", ":foreground ,.red-hi :weight bold"),
    ("compilation-mode-line-run", ":foreground ,.yellow"),
    ("eglot-highlight-symbol-face", ":background ,.bracket-bg"),
    ("eglot-inlay-hint-face", ":foreground ,.overlay1 :background ,.bg-inlay :slant italic"),
    ("eglot-parameter-hint-face", ":inherit eglot-inlay-hint-face"),
    ("eglot-type-hint-face", ":inherit eglot-inlay-hint-face"),
    ("eglot-diagnostic-tag-unnecessary-face", ":foreground ,.overlay1"),
    ("eglot-diagnostic-tag-deprecated-face", ":strike-through t"),
    ("lsp-face-highlight-textual", ":background ,.bracket-bg"),
    ("lsp-face-highlight-read", ":background ,.bracket-bg"),
    ("lsp-face-highlight-write", ":background ,.bracket-bg :underline t"),
    ("lsp-inlay-hint-face", ":foreground ,.overlay1 :background ,.bg-inlay :slant italic"),
    # lsp-ui: the doc and peek windows are popovers, so they sit on paper
    ("lsp-ui-doc-background", ":background ,.paper"),
    ("lsp-ui-doc-header", ":foreground ,.text-hi :background ,.row :weight bold"),
    ("lsp-ui-doc-url", ":inherit link"),
    ("lsp-ui-doc-highlight-hover", ":background ,.row"),
    ("lsp-ui-peek-peek", ":background ,.paper"),
    ("lsp-ui-peek-list", ":background ,.paper"),
    ("lsp-ui-peek-header", ":foreground ,.text-hi :background ,.row :weight bold"),
    ("lsp-ui-peek-footer", ":background ,.row"),
    ("lsp-ui-peek-selection", ":foreground ,.text-hi :background ,.row :weight bold"),
    ("lsp-ui-peek-filename", ":foreground ,.yellow :weight bold"),
    ("lsp-ui-peek-line-number", ":foreground ,.line-nr"),
    ("lsp-ui-peek-highlight", ":foreground ,.text-hi :background ,.bg-search-cur"),
    ("lsp-ui-sideline-symbol", ":foreground ,.overlay1 :box (:line-width -1 :color ,.overlay0)"),
    ("lsp-ui-sideline-current-symbol", ":foreground ,.yellow :weight bold :box (:line-width -1 :color ,.yellow)"),
    ("lsp-ui-sideline-symbol-info", ":foreground ,.overlay1 :slant italic"),
    ("lsp-ui-sideline-code-action", ":foreground ,.yellow"),
    ("lsp-ui-sideline-global", ":background ,.hl-line"),
    # ── completion popovers on paper: corfu, company, eldoc-box ──
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
    ("corfu-default", ":foreground ,.subtext1 :background ,.paper"),
    ("corfu-current", ":foreground ,.text-hi :background ,.row :weight bold :extend t"),
    ("corfu-border", ":background ,.edge"),
    ("corfu-bar", ":background ,.overlay0"),
    ("corfu-annotations", ":foreground ,.overlay1 :slant italic"),
    ("corfu-deprecated", ":foreground ,.overlay0 :strike-through t"),
    ("company-tooltip", ":foreground ,.subtext1 :background ,.paper"),
    ("company-tooltip-selection", ":foreground ,.text-hi :background ,.row :weight bold"),
    ("company-tooltip-common", ":foreground ,.yellow :weight bold"),
    ("company-tooltip-common-selection", ":foreground ,.yellow :weight bold"),
    ("company-tooltip-annotation", ":foreground ,.overlay1 :slant italic"),
    ("company-tooltip-annotation-selection", ":foreground ,.subtext0"),
    ("company-tooltip-search", ":foreground ,.text-hi :background ,.bg-search"),
    ("company-tooltip-search-selection", ":foreground ,.text-hi :background ,.bg-search-cur"),
    ("company-tooltip-mouse", ":background ,.row"),
    ("company-tooltip-scrollbar-thumb", ":background ,.overlay0"),
    ("company-tooltip-scrollbar-track", ":background ,.edge"),
    ("company-scrollbar-fg", ":background ,.overlay0"),
    ("company-scrollbar-bg", ":background ,.edge"),
    ("company-preview", ":foreground ,.overlay0 :slant italic"),
    ("company-preview-common", ":foreground ,.overlay1 :slant italic"),
    ("company-preview-search", ":foreground ,.text-hi :background ,.bg-search"),
    ("company-echo-common", ":foreground ,.yellow"),
    ("eldoc-box-body", ":foreground ,.text :background ,.paper"),
    ("eldoc-box-border", ":background ,.edge"),
    ("ivy-current-match", ":foreground ,.text-hi :background ,.surface1 :weight bold :extend t"),
    ("ivy-minibuffer-match-face-1", ":foreground ,.overlay1"),
    ("ivy-minibuffer-match-face-2", ":foreground ,.yellow :weight bold"),
    ("ivy-minibuffer-match-face-3", ":foreground ,.orange :weight bold"),
    ("ivy-minibuffer-match-face-4", ":foreground ,.sage :weight bold"),
    ("ivy-subdir", ":foreground ,.yellow"),
    ("ivy-remote", ":foreground ,.denim"),
    # helm
    ("helm-header", ":foreground ,.subtext0 :background ,.mantle :extend t"),
    ("helm-source-header", ":foreground ,.orange :background ,.mantle :weight bold :extend t"),
    ("helm-selection", ":foreground ,.text-hi :background ,.surface1 :weight bold :extend t"),
    ("helm-visible-mark", ":foreground ,.text-hi :background ,.bg-search :extend t"),
    ("helm-match", ":foreground ,.yellow :weight bold"),
    ("helm-candidate-number", ":foreground ,.yellow"),
    ("helm-separator", ":foreground ,.overlay0"),
    ("helm-action", ":foreground ,.subtext1"),
    ("helm-prefarg", ":foreground ,.orange"),
    ("helm-minibuffer-prompt", ":foreground ,.orange :weight bold"),
    ("helm-dim-prompt", ":foreground ,.overlay0"),
    ("helm-ff-directory", ":foreground ,.yellow"),
    ("helm-ff-dotted-directory", ":foreground ,.overlay1"),
    ("helm-ff-file", ":foreground ,.subtext1"),
    ("helm-ff-file-extension", ":foreground ,.overlay2"),
    ("helm-ff-executable", ":foreground ,.green"),
    ("helm-ff-symlink", ":foreground ,.denim"),
    ("helm-ff-invalid-symlink", ":foreground ,.red-hi :background ,.bg-error"),
    ("helm-ff-prefix", ":foreground ,.ink :background ,.yellow"),
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
    # ── version control: diff, magit, smerge, ediff, diff-hl, git-gutter, vc ──
    # Line grounds keep the code's own colors on top (diff-mode fontifies hunks by default);
    # the +/- signs and gutter marks carry green and red, changed words sit on a stronger tint.
    ("diff-added", ":background ,.bg-add :extend t"),
    ("diff-removed", ":background ,.bg-del :extend t"),
    ("diff-changed", ":background ,.bg-chg :extend t"),
    ("diff-changed-unspecified", ":background ,.bg-chg :extend t"),
    ("diff-refine-added", ":background ,.bg-add-emph"),
    ("diff-refine-removed", ":background ,.bg-del-emph"),
    ("diff-refine-changed", ":background ,.bg-chg-emph"),
    ("diff-indicator-added", ":foreground ,.green :weight bold"),
    ("diff-indicator-removed", ":foreground ,.red-hi :weight bold"),
    ("diff-indicator-changed", ":foreground ,.yellow :weight bold"),
    ("diff-header", ":foreground ,.subtext1 :background ,.mantle :extend t"),
    ("diff-file-header", ":foreground ,.text-hi :background ,.mantle :weight bold :extend t"),
    ("diff-hunk-header", ":foreground ,.denim :background ,.surface0 :extend t"),
    ("diff-context", ":foreground ,.subtext0"),
    ("diff-function", ":foreground ,.yellow"),
    ("diff-nonexistent", ":foreground ,.overlay0"),
    ("diff-error", ":foreground ,.red-hi :weight bold"),
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
    ("magit-diff-added", f":background ,.bg-add :extend t {hunk_fg('green')}"),
    ("magit-diff-added-highlight", f":background ,.bg-add-hl :extend t {hunk_fg('green')}"),
    ("magit-diff-removed", f":background ,.bg-del :extend t {hunk_fg('red-hi')}"),
    ("magit-diff-removed-highlight", f":background ,.bg-del-hl :extend t {hunk_fg('red-hi')}"),
    ("magit-diff-base", f":background ,.bg-chg :extend t {hunk_fg('yellow')}"),
    ("magit-diff-base-highlight", f":background ,.bg-chg-emph :extend t {hunk_fg('yellow')}"),
    ("magit-diff-context", f":extend t {hunk_fg('overlay2')}"),
    ("magit-diff-context-highlight", f":background ,.mantle :extend t {hunk_fg('subtext0')}"),
    ("magit-diff-added-indicator", ":foreground ,.green :weight bold"),
    ("magit-diff-removed-indicator", ":foreground ,.red-hi :weight bold"),
    ("magit-diff-base-indicator", ":foreground ,.yellow :weight bold"),
    ("magit-diff-hunk-heading", ":foreground ,.subtext1 :background ,.surface0 :extend t"),
    ("magit-diff-hunk-heading-highlight", ":foreground ,.text-hi :background ,.surface1 :weight bold :extend t"),
    ("magit-diff-hunk-heading-selection", ":inherit magit-diff-hunk-heading-highlight :foreground ,.orange"),
    ("magit-diff-hunk-region", ":inherit bold :extend t"),
    ("magit-diff-conflict-heading", ":inherit magit-diff-hunk-heading :foreground ,.orange"),
    ("magit-diff-conflict-heading-highlight", ":inherit magit-diff-hunk-heading-highlight :foreground ,.orange"),
    ("magit-diff-file-heading", ":foreground ,.text-hi :weight bold"),
    ("magit-diff-file-heading-highlight", ":inherit magit-section-highlight"),
    ("magit-diff-file-heading-selection", ":inherit magit-diff-file-heading-highlight :foreground ,.orange"),
    ("magit-diff-lines-heading", ":foreground ,.ink :background ,.orange :extend t"),
    ("magit-diff-lines-boundary", ":background ,.orange"),
    ("magit-diff-revision-summary", ":inherit magit-diff-hunk-heading"),
    ("magit-diff-revision-summary-highlight", ":inherit magit-diff-hunk-heading-highlight"),
    ("magit-diff-whitespace-warning", ":background ,.bg-error"),
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
    ("smerge-upper", ":background ,.bg-del :extend t"),
    ("smerge-lower", ":background ,.bg-add :extend t"),
    ("smerge-base", ":background ,.bg-chg :extend t"),
    ("smerge-markers", ":foreground ,.overlay1 :background ,.surface0 :extend t"),
    ("smerge-refined-added", ":background ,.bg-add-emph"),
    ("smerge-refined-removed", ":background ,.bg-del-emph"),
    ("smerge-refined-changed", ":background ,.bg-chg-emph"),
    ("ediff-current-diff-A", ":background ,.bg-del :extend t"),
    ("ediff-current-diff-B", ":background ,.bg-add :extend t"),
    ("ediff-current-diff-C", ":background ,.bg-chg :extend t"),
    ("ediff-current-diff-Ancestor", ":background ,.bg-info :extend t"),
    ("ediff-fine-diff-A", ":background ,.bg-del-emph"),
    ("ediff-fine-diff-B", ":background ,.bg-add-emph"),
    ("ediff-fine-diff-C", ":background ,.bg-chg-emph"),
    ("ediff-fine-diff-Ancestor", ":background ,.bg-search"),
    *((f"ediff-{kind}-diff-{side}", ":background ,.surface0 :extend t")
      for kind in ("even", "odd") for side in ("A", "B", "C", "Ancestor")),
    ("diff-hl-insert", ":foreground ,.green :background ,.green"),
    ("diff-hl-delete", ":foreground ,.red-hi :background ,.red-hi"),
    ("diff-hl-change", ":foreground ,.yellow :background ,.yellow"),
    ("git-gutter:added", ":foreground ,.green"),
    ("git-gutter:deleted", ":foreground ,.red-hi"),
    ("git-gutter:modified", ":foreground ,.yellow"),
    ("git-gutter-fr:added", ":foreground ,.green"),
    ("git-gutter-fr:deleted", ":foreground ,.red-hi"),
    ("git-gutter-fr:modified", ":foreground ,.yellow"),
    ("vc-edited-state", ":foreground ,.yellow"),
    ("vc-locally-added-state", ":foreground ,.green"),
    ("vc-removed-state", ":foreground ,.red-hi"),
    ("vc-missing-state", ":foreground ,.red-hi"),
    ("vc-conflict-state", ":foreground ,.orange :weight bold"),
    ("vc-needs-update-state", ":foreground ,.denim"),
    ("vc-locked-state", ":foreground ,.clay"),
    ("vc-ignored-state", ":foreground ,.overlay0"),
    # ── org and outline ──
    *((f"outline-{i + 1}", f":foreground ,.{c} :weight bold") for i, c in enumerate(HEADINGS)),
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
    ("org-sexp-date", ":foreground ,.clay"),
    ("org-todo", ":foreground ,.red-hi :weight bold"),
    ("org-done", ":foreground ,.green :weight bold"),
    ("org-headline-todo", ":foreground ,.clay"),
    ("org-headline-done", ":foreground ,.overlay1"),
    ("org-priority", ":foreground ,.orange"),
    ("org-link", ":inherit link"),
    ("org-footnote", ":foreground ,.clay"),
    ("org-target", ":underline t"),
    ("org-table", ":foreground ,.subtext1"),
    ("org-table-header", ":inherit org-table :foreground ,.text-hi :background ,.surface0 :weight bold"),
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
    ("org-column", ":background ,.surface0 :weight normal :slant normal :strike-through nil :underline nil"),
    ("org-column-title", ":background ,.surface1 :underline t :weight bold"),
    ("org-clock-overlay", ":foreground ,.text-hi :background ,.surface1"),
    ("org-dispatcher-highlight", ":foreground ,.yellow :background ,.surface0 :weight bold"),
    ("org-mode-line-clock-overrun", ":inherit mode-line :foreground ,.ink :background ,.red-hi"),
    ("org-scheduled", ":foreground ,.green"),
    ("org-scheduled-today", ":foreground ,.green-hi :weight bold"),
    ("org-scheduled-previously", ":foreground ,.yellow"),
    ("org-upcoming-deadline", ":foreground ,.orange"),
    ("org-time-grid", ":foreground ,.overlay0"),
    ("org-agenda-structure", ":foreground ,.orange :weight bold"),
    ("org-agenda-date", ":foreground ,.yellow"),
    ("org-agenda-date-today", ":foreground ,.yellow-hi :weight bold"),
    ("org-agenda-date-weekend", ":foreground ,.overlay2"),
    ("org-agenda-date-weekend-today", ":foreground ,.yellow :weight bold"),
    ("org-agenda-done", ":foreground ,.overlay1"),
    ("org-agenda-current-time", ":foreground ,.orange"),
    ("org-agenda-dimmed-todo-face", ":foreground ,.overlay0"),
    ("org-agenda-restriction-lock", ":background ,.surface0"),
    # ── markdown ──
    ("markdown-header-face", syn("heading")),
    *((f"markdown-header-face-{i + 1}", f":foreground ,.{c} :weight bold") for i, c in enumerate(HEADINGS[:6])),
    ("markdown-header-delimiter-face", ":foreground ,.overlay1"),
    ("markdown-code-face", ":background ,.mantle :extend t"),
    ("markdown-inline-code-face", ":foreground ,.green :background ,.mantle"),
    ("markdown-pre-face", syn("code")),
    ("markdown-language-keyword-face", ":foreground ,.overlay1 :slant italic"),
    ("markdown-link-face", syn("link")),
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
    # ── mail: message-mode (Gnus, mu4e and notmuch compose with it) ──
    ("message-header-name", ":foreground ,.overlay1"),
    ("message-header-subject", ":foreground ,.yellow :weight bold"),
    ("message-header-to", ":foreground ,.orange :weight bold"),
    ("message-header-cc", ":foreground ,.subtext1"),
    ("message-header-newsgroups", ":foreground ,.sage"),
    ("message-header-other", ":foreground ,.subtext0"),
    ("message-header-xheader", ":foreground ,.overlay1"),
    ("message-separator", ":foreground ,.overlay0"),
    ("message-mml", ":foreground ,.clay"),
    ("message-signature-separator", ":foreground ,.overlay1"),
    *((f"message-cited-text-{i + 1}", f":foreground ,.{c}") for i, c in enumerate(CITED)),
    # ── files & shells: dired, diredfl, eshell, comint, info ──
    ("dired-directory", ":foreground ,.yellow"),
    ("dired-header", ":foreground ,.orange :weight bold"),
    ("dired-symlink", ":foreground ,.denim"),
    ("dired-broken-symlink", ":foreground ,.red-hi :background ,.bg-error"),
    ("dired-mark", ":foreground ,.orange :weight bold"),
    ("dired-marked", ":foreground ,.yellow-hi :weight bold"),
    ("dired-flagged", ":foreground ,.red-hi :weight bold"),
    ("dired-ignored", ":foreground ,.overlay0"),
    ("dired-perm-write", ":foreground ,.clay"),
    ("dired-set-id", ":foreground ,.clay"),
    ("dired-special", ":foreground ,.clay"),
    ("dired-warning", ":foreground ,.yellow"),
    ("diredfl-dir-heading", ":foreground ,.orange :weight bold"),
    ("diredfl-dir-name", ":foreground ,.yellow"),
    ("diredfl-file-name", ":foreground ,.subtext1"),
    ("diredfl-file-suffix", ":foreground ,.overlay2"),
    ("diredfl-symlink", ":foreground ,.denim"),
    ("diredfl-number", ":foreground ,.subtext0"),
    ("diredfl-date-time", ":foreground ,.overlay1"),
    ("diredfl-compressed-file-name", ":foreground ,.clay"),
    ("diredfl-compressed-file-suffix", ":foreground ,.clay"),
    ("diredfl-ignored-file-name", ":foreground ,.overlay0"),
    ("diredfl-executable-tag", ":foreground ,.green"),
    ("diredfl-flag-mark", ":foreground ,.yellow :weight bold"),
    ("diredfl-flag-mark-line", ":background ,.bg-search :extend t"),
    ("diredfl-deletion", ":foreground ,.ink :background ,.red-hi :weight bold"),
    ("diredfl-deletion-file-name", ":foreground ,.red-hi"),
    ("diredfl-autofile-name", ":foreground ,.sage"),
    ("diredfl-tagged-autofile-name", ":foreground ,.sage"),
    ("diredfl-dir-priv", ":foreground ,.yellow"),
    ("diredfl-read-priv", ":foreground ,.green"),
    ("diredfl-write-priv", ":foreground ,.orange"),
    ("diredfl-exec-priv", ":foreground ,.red-hi"),
    ("diredfl-link-priv", ":foreground ,.denim"),
    ("diredfl-other-priv", ":foreground ,.clay"),
    ("diredfl-rare-priv", ":foreground ,.clay :weight bold"),
    ("diredfl-no-priv", ":foreground ,.overlay0"),
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
    # ── side trees: treemacs, neotree ──
    ("treemacs-window-background-face", ":background ,.mantle"),
    ("treemacs-hl-line-face", ":background ,.surface0 :extend t"),
    ("treemacs-root-face", ":foreground ,.orange :weight bold"),
    ("treemacs-root-unreadable-face", ":foreground ,.red-hi :strike-through t"),
    ("treemacs-root-remote-face", ":foreground ,.denim :weight bold"),
    ("treemacs-root-remote-unreadable-face", ":foreground ,.red-hi :strike-through t"),
    ("treemacs-root-remote-disconnected-face", ":foreground ,.yellow"),
    ("treemacs-directory-face", ":foreground ,.yellow"),
    ("treemacs-directory-collapsed-face", ":foreground ,.yellow"),
    ("treemacs-file-face", ":foreground ,.subtext1"),
    ("treemacs-tags-face", ":foreground ,.sage"),
    ("treemacs-term-node-face", ":foreground ,.clay"),
    ("treemacs-help-title-face", ":foreground ,.orange :weight bold"),
    ("treemacs-help-column-face", ":foreground ,.yellow :underline t"),
    ("treemacs-header-button-face", ":foreground ,.overlay1"),
    ("treemacs-marked-file-face", ":foreground ,.yellow-hi :weight bold"),
    ("treemacs-fringe-indicator-face", ":foreground ,.orange"),
    ("treemacs-async-loading-face", ":foreground ,.overlay1"),
    ("treemacs-peek-mode-indicator-face", ":background ,.orange"),
    ("treemacs-on-success-pulse-face", ":foreground ,.ink :background ,.green"),
    ("treemacs-on-failure-pulse-face", ":foreground ,.ink :background ,.red-hi"),
    ("treemacs-git-added-face", ":foreground ,.green"),
    ("treemacs-git-modified-face", ":foreground ,.yellow"),
    ("treemacs-git-renamed-face", ":foreground ,.sage"),
    ("treemacs-git-untracked-face", ":foreground ,.green"),
    ("treemacs-git-ignored-face", ":foreground ,.overlay0"),
    ("treemacs-git-conflict-face", ":foreground ,.orange :weight bold"),
    ("treemacs-git-unmodified-face", ":foreground ,.subtext1"),
    ("treemacs-git-commit-diff-face", ":foreground ,.clay"),
    ("neo-banner-face", ":foreground ,.orange :weight bold"),
    ("neo-header-face", ":foreground ,.text-hi"),
    ("neo-root-dir-face", ":foreground ,.orange :weight bold"),
    ("neo-dir-link-face", ":foreground ,.yellow"),
    ("neo-file-link-face", ":foreground ,.subtext1"),
    ("neo-expand-btn-face", ":foreground ,.overlay1"),
    ("neo-button-face", ":underline nil"),
    ("neo-vc-default-face", ":foreground ,.subtext1"),
    ("neo-vc-up-to-date-face", ":foreground ,.subtext1"),
    ("neo-vc-user-face", ":foreground ,.clay"),
    ("neo-vc-edited-face", ":foreground ,.yellow"),
    ("neo-vc-added-face", ":foreground ,.green"),
    ("neo-vc-removed-face", ":foreground ,.red-hi"),
    ("neo-vc-missing-face", ":foreground ,.red-hi"),
    ("neo-vc-conflict-face", ":foreground ,.orange :weight bold"),
    ("neo-vc-needs-merge-face", ":foreground ,.orange"),
    ("neo-vc-needs-update-face", ":foreground ,.denim"),
    ("neo-vc-unlocked-changes-face", ":foreground ,.clay"),
    ("neo-vc-unregistered-face", ":foreground ,.overlay1"),
    ("neo-vc-ignored-face", ":foreground ,.overlay0"),
    # ── doom-modeline (modes are route bullets, like the other editors) and nerd-icons ──
    ("doom-modeline-bar", ":background ,.orange"),
    ("doom-modeline-bar-inactive", ":background ,.crust"),
    ("doom-modeline-buffer-file", ":foreground ,.text-hi :weight bold"),
    ("doom-modeline-buffer-path", ":foreground ,.subtext0"),
    ("doom-modeline-buffer-modified", ":foreground ,.yellow :weight bold"),
    ("doom-modeline-buffer-major-mode", ":foreground ,.sage :weight bold"),
    ("doom-modeline-buffer-minor-mode", ":foreground ,.overlay1"),
    ("doom-modeline-project-dir", ":foreground ,.orange :weight bold"),
    ("doom-modeline-project-name", ":foreground ,.orange"),
    ("doom-modeline-project-parent-dir", ":foreground ,.overlay1"),
    ("doom-modeline-project-root-dir", ":foreground ,.subtext0"),
    ("doom-modeline-highlight", ":foreground ,.orange"),
    ("doom-modeline-emphasis", ":foreground ,.yellow :weight bold"),
    ("doom-modeline-panel", ":foreground ,.ink :background ,.orange"),
    ("doom-modeline-info", ":foreground ,.green"),
    ("doom-modeline-warning", ":foreground ,.yellow"),
    ("doom-modeline-urgent", ":foreground ,.red-hi :weight bold"),
    ("doom-modeline-notification", ":foreground ,.yellow"),
    ("doom-modeline-unread-number", ":foreground ,.denim"),
    ("doom-modeline-debug", ":foreground ,.clay"),
    ("doom-modeline-lsp-success", ":foreground ,.green"),
    ("doom-modeline-lsp-warning", ":foreground ,.yellow"),
    ("doom-modeline-lsp-error", ":foreground ,.red-hi"),
    ("doom-modeline-lsp-running", ":foreground ,.overlay1"),
    ("doom-modeline-evil-normal-state", ":foreground ,.orange :weight bold"),
    ("doom-modeline-evil-insert-state", ":foreground ,.green :weight bold"),
    ("doom-modeline-evil-visual-state", ":foreground ,.yellow :weight bold"),
    ("doom-modeline-evil-replace-state", ":foreground ,.red-hi :weight bold"),
    ("doom-modeline-evil-motion-state", ":foreground ,.sage :weight bold"),
    ("doom-modeline-evil-operator-state", ":foreground ,.sage :weight bold"),
    ("doom-modeline-evil-emacs-state", ":foreground ,.clay :weight bold"),
    *((f"nerd-icons-{name}", f":foreground ,.{role}") for name, role in NERD.items()),
    # ── terminal colors: ansi-color (28+), term (27) ──
    *((f"ansi-color-{n}", f":foreground ,.ansi{i} :background ,.ansi{i}") for i, n in enumerate(ANSI_NAMES)),
    *((f"ansi-color-bright-{n}", f":foreground ,.ansi{i + 8} :background ,.ansi{i + 8}") for i, n in enumerate(ANSI_NAMES)),
    *((f"term-color-{n}", f":foreground ,.ansi{i} :background ,.ansi{i}") for i, n in enumerate(ANSI_NAMES)),
    *((f"term-color-bright-{n}", f":foreground ,.ansi{i + 8} :background ,.ansi{i + 8}") for i, n in enumerate(ANSI_NAMES)),
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
;; Put the three files in one folder on `load-path' and
;; `custom-theme-load-path' (or install the package), then enable one with
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

(defvar magit-diff-specify-hunk-foreground)

(defun subway-seat-theme--hunk-fg (color)
  "Return (:foreground COLOR) for a Magit hunk face, or nil.
Nil when `magit-diff-specify-hunk-foreground' is nil, so hunks fontified
with `magit-diff-fontify-hunk' keep their syntax colors on the diff grounds."
  (unless (and (boundp 'magit-diff-specify-hunk-foreground)
               (not magit-diff-specify-hunk-foreground))
    (list :foreground color)))

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
     `(hl-todo-keyword-faces
       '(("TODO" . ,.yellow) ("NEXT" . ,.yellow) ("FIXME" . ,.red-hi) ("BUG" . ,.red-hi)
         ("XXX" . ,.red-hi) ("HACK" . ,.clay) ("KLUDGE" . ,.clay) ("NOTE" . ,.sage)
         ("DONE" . ,.green) ("OKAY" . ,.green) ("DEPRECATED" . ,.overlay1)))
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
    outs = []
    for f in flavors:
        name = "subway-seat-theme.el" if f.slug == "subway-seat" else f"{f.slug}-theme.el"
        body = main_file(flavors) if f.slug == "subway-seat" else flavor_file(f)
        outs.append(Out(name, body, flavor=f.id, dest=THEMES_DIR + name, lang="elisp",
                        how=None if f.slug == "subway-seat" else "needs subway-seat-theme.el in the same folder"))
    return outs
