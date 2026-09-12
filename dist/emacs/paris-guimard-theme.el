;;; paris-guimard-theme.el --- Paris Guimard, the Guimard flavor -*- lexical-binding: t; -*-

;; Copyright (C) 2026 Oddur Sigurdsson

;; Author: Oddur Sigurdsson
;; URL: https://github.com/oddurs/subway-seat
;; Version: 0.3.0
;; Package-Requires: ((emacs "27.1"))
;; SPDX-License-Identifier: MIT

;; This file is not part of GNU Emacs.

;;; Commentary:

;; Cast-iron green off a Metro entrance. The original green.
;; The palette and faces live in subway-seat-theme.el; this file lets
;; `load-theme' find `paris-guimard'.
;;
;; Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.

;;; Code:

(require 'subway-seat-theme)

(deftheme paris-guimard
  "Paris Guimard: Cast-iron green off a Metro entrance. The original green.")

;; `load-theme' clears a theme's settings before loading its file, so record them again.
(subway-seat-theme-apply 'paris-guimard)

(provide-theme 'paris-guimard)

;;; paris-guimard-theme.el ends here
