;;; subway-seat-tunnel-theme.el --- Subway Seat Tunnel, the Tunnel flavor -*- lexical-binding: t; -*-

;; Copyright (C) 2026 Oddur Sigurdsson

;; Author: Oddur Sigurdsson
;; URL: https://github.com/oddurs/subway-seat
;; Version: 0.3.0
;; Package-Requires: ((emacs "27.1"))
;; SPDX-License-Identifier: MIT

;; This file is not part of GNU Emacs.

;;; Commentary:

;; The late local after midnight: espresso-deep, same warm lights.
;; The palette and faces live in subway-seat-theme.el; this file lets
;; `load-theme' find `subway-seat-tunnel'.
;;
;; Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.

;;; Code:

(require 'subway-seat-theme)

(deftheme subway-seat-tunnel
  "Subway Seat Tunnel: The late local after midnight: espresso-deep, same warm lights.")

;; `load-theme' clears a theme's settings before loading its file, so record them again.
(subway-seat-theme-apply 'subway-seat-tunnel)

(provide-theme 'subway-seat-tunnel)

;;; subway-seat-tunnel-theme.el ends here
