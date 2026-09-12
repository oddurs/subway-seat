;;; london-deep-level-theme.el --- London Deep Level, the Deep flavor -*- lexical-binding: t; -*-

;; Copyright (C) 2026 Oddur Sigurdsson

;; Author: Oddur Sigurdsson
;; URL: https://github.com/oddurs/subway-seat
;; Version: 0.3.0
;; Package-Requires: ((emacs "27.1"))
;; SPDX-License-Identifier: MIT

;; This file is not part of GNU Emacs.

;;; Commentary:

;; Below the cut-and-cover lines. The ground drops; the signals don't.
;; The palette and faces live in subway-seat-theme.el; this file lets
;; `load-theme' find `london-deep-level'.
;;
;; Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.

;;; Code:

(require 'subway-seat-theme)

(deftheme london-deep-level
  "London Deep Level: Below the cut-and-cover lines. The ground drops; the signals don't.")

;; `load-theme' clears a theme's settings before loading its file, so record them again.
(subway-seat-theme-apply 'london-deep-level)

(provide-theme 'london-deep-level)

;;; london-deep-level-theme.el ends here
