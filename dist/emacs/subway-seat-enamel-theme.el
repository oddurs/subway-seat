;;; subway-seat-enamel-theme.el --- Subway Seat Enamel, the Enamel flavor -*- lexical-binding: t; -*-

;; Copyright (C) 2026 Oddur Sigurdsson

;; Author: Oddur Sigurdsson
;; URL: https://github.com/oddurs/subway-seat
;; Version: 0.2.0
;; Package-Requires: ((emacs "27.1"))
;; SPDX-License-Identifier: MIT

;; This file is not part of GNU Emacs.

;;; Commentary:

;; Cream enamel panels in the morning sun. The light one.
;; The palette and faces live in subway-seat-theme.el; this file lets
;; `load-theme' find `subway-seat-enamel'.
;;
;; Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.

;;; Code:

(require 'subway-seat-theme)

(deftheme subway-seat-enamel
  "Subway Seat Enamel: Cream enamel panels in the morning sun. The light one.")

;; `load-theme' clears a theme's settings before loading its file, so record them again.
(subway-seat-theme-apply 'subway-seat-enamel)

(provide-theme 'subway-seat-enamel)

;;; subway-seat-enamel-theme.el ends here
