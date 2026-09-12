;;; paris-carrelage-theme.el --- Paris Carrelage, the Carrelage flavor -*- lexical-binding: t; -*-

;; Copyright (C) 2026 Oddur Sigurdsson

;; Author: Oddur Sigurdsson
;; URL: https://github.com/oddurs/subway-seat
;; Version: 0.3.0
;; Package-Requires: ((emacs "27.1"))
;; SPDX-License-Identifier: MIT

;; This file is not part of GNU Emacs.

;;; Commentary:

;; Bevelled white tile under a vaulted platform. The light one.
;; The palette and faces live in subway-seat-theme.el; this file lets
;; `load-theme' find `paris-carrelage'.
;;
;; Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.

;;; Code:

(require 'subway-seat-theme)

(deftheme paris-carrelage
  "Paris Carrelage: Bevelled white tile under a vaulted platform. The light one.")

;; `load-theme' clears a theme's settings before loading its file, so record them again.
(subway-seat-theme-apply 'paris-carrelage)

(provide-theme 'paris-carrelage)

;;; paris-carrelage-theme.el ends here
