;;; london-moquette-theme.el --- London Moquette, the Moquette flavor -*- lexical-binding: t; -*-

;; Copyright (C) 2026 Oddur Sigurdsson

;; Author: Oddur Sigurdsson
;; URL: https://github.com/oddurs/subway-seat
;; Version: 0.3.0
;; Package-Requires: ((emacs "27.1"))
;; SPDX-License-Identifier: MIT

;; This file is not part of GNU Emacs.

;;; Commentary:

;; The seat you're sitting on. Corporate Blue, turned right down.
;; The palette and faces live in subway-seat-theme.el; this file lets
;; `load-theme' find `london-moquette'.
;;
;; Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.

;;; Code:

(require 'subway-seat-theme)

(deftheme london-moquette
  "London Moquette: The seat you're sitting on. Corporate Blue, turned right down.")

;; `load-theme' clears a theme's settings before loading its file, so record them again.
(subway-seat-theme-apply 'london-moquette)

(provide-theme 'london-moquette)

;;; london-moquette-theme.el ends here
