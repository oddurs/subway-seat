;;; paris-catacombes-theme.el --- Paris Catacombes, the Catacombes flavor -*- lexical-binding: t; -*-

;; Copyright (C) 2026 Oddur Sigurdsson

;; Author: Oddur Sigurdsson
;; URL: https://github.com/oddurs/subway-seat
;; Version: 0.3.0
;; Package-Requires: ((emacs "27.1"))
;; SPDX-License-Identifier: MIT

;; This file is not part of GNU Emacs.

;;; Commentary:

;; Under the quarries: the same green with the lights turned down.
;; The palette and faces live in subway-seat-theme.el; this file lets
;; `load-theme' find `paris-catacombes'.
;;
;; Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.

;;; Code:

(require 'subway-seat-theme)

(deftheme paris-catacombes
  "Paris Catacombes: Under the quarries: the same green with the lights turned down.")

;; `load-theme' clears a theme's settings before loading its file, so record them again.
(subway-seat-theme-apply 'paris-catacombes)

(provide-theme 'paris-catacombes)

;;; paris-catacombes-theme.el ends here
