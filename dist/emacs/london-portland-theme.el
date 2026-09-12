;;; london-portland-theme.el --- London Portland, the Portland flavor -*- lexical-binding: t; -*-

;; Copyright (C) 2026 Oddur Sigurdsson

;; Author: Oddur Sigurdsson
;; URL: https://github.com/oddurs/subway-seat
;; Version: 0.3.0
;; Package-Requires: ((emacs "27.1"))
;; SPDX-License-Identifier: MIT

;; This file is not part of GNU Emacs.

;;; Commentary:

;; Holden's Portland stone. Links are the exact Corporate Blue.
;; The palette and faces live in subway-seat-theme.el; this file lets
;; `load-theme' find `london-portland'.
;;
;; Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.

;;; Code:

(require 'subway-seat-theme)

(deftheme london-portland
  "London Portland: Holden's Portland stone. Links are the exact Corporate Blue.")

;; `load-theme' clears a theme's settings before loading its file, so record them again.
(subway-seat-theme-apply 'london-portland)

(provide-theme 'london-portland)

;;; london-portland-theme.el ends here
