#!/usr/bin/env fish
# Subway Seat for fish users: runs install.sh, the real installer, and tells it
# fish is your shell so the steps it prints are in fish syntax.
#
#   ./install.fish                  # install (your saved flavor, else Walnut)
#   ./install.fish tunnel           # install as Tunnel (the old form still works)
#   ./install.fish switch enamel    # re-point everything at Enamel
#   ./install.fish status           # also: uninstall, list, --help
#
# Every option of install.sh works here too (see ./install.fish --help). An
# install made by the old install.fish is picked up and tidied: its links are
# adopted or removed, and its conf.d file goes once the fish block replaces it.

set -l root (path dirname (path resolve (status filename)))
set -l args $argv
# The old form: a bare flavor first.
if set -q args[1]; and contains -- (string lower -- $args[1]) walnut tunnel enamel auto
    set args --flavor (string lower -- $args[1]) $args[2..-1]
end

set -l self $root/install.fish
if string match -q -- "$HOME/*" $self
    set self "~"(string sub -s (math (string length -- $HOME) + 1) -- $self)
end
string match -q -- '* *' $self; and set self (string escape -- $root/install.fish)

set -lx SUBWAY_SEAT_SHELL fish
set -lx SUBWAY_SEAT_SELF $self
exec sh $root/install.sh $args
