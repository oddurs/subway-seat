# Security

Subway Seat is mostly color files, but a few pieces run code on your machine: the installers (`install.fish`, `install.sh`), the Claude Code status line scripts, the GNOME Terminal setup scripts, and the Claude Code plugin's setup skill.

If you find a way any of them could do something unexpected (write outside the paths they claim, run injected input, leak data), please report it privately through [GitHub's private vulnerability reporting](https://github.com/oddurs/subway-seat/security/advisories/new) rather than in a public issue. Only the maintainer can read it. You'll get a reply within a week.

## Supported versions

The latest release and `main`. Fixes aren't backported to older releases.
