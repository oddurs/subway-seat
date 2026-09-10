#!/bin/sh
# Subway Seat for tmux, as a TPM plugin. In ~/.tmux.conf, before TPM's `run` line:
#
#   set -g @subway_seat_flavor 'walnut'   # walnut (default), tunnel, enamel, or auto (tmux 3.6+)
#   set -g @plugin 'oddurs/subway-seat'
#
# List it before tmux-continuum and other plugins that add to the status bar.
# The themes themselves are the generated files in dist/tmux/.

dir=$(cd "$(dirname "$0")" && pwd)/dist/tmux

conf() {
    case "$1" in
        tunnel | subway-seat-tunnel) echo "$dir/subway-seat-tunnel.conf" ;;
        enamel | subway-seat-enamel) echo "$dir/subway-seat-enamel.conf" ;;
        *) echo "$dir/subway-seat.conf" ;;
    esac
}

flavor=$(tmux show-option -gqv @subway_seat_flavor)

if [ "$flavor" = auto ]; then
    # follow the terminal's light/dark reports; Walnut until the first one arrives
    tmux source-file "$(conf walnut)"
    tmux set-hook -g client-dark-theme "source-file '$(conf walnut)'"
    tmux set-hook -g client-light-theme "source-file '$(conf enamel)'"
else
    tmux source-file "$(conf "$flavor")"
fi
