#!/bin/sh
# Subway Seat installer: links the theme files for the apps on this machine,
# adds the lines that turn them on (between marker comments), and remembers
# what it did, so `switch` and `uninstall` are exact.
#
#   sh install.sh                      # install (your saved flavor, else Walnut)
#   sh install.sh switch enamel        # re-point everything at another flavor
#   sh install.sh uninstall            # take it all out again
#   curl -fsSL https://oddurs.github.io/subway-seat/install.sh | sh -s -- --flavor tunnel
#
# POSIX sh plus awk, sed, grep and cksum. It reads dist/install.tsv, which
# build.py writes (install_table() documents the records). Three apps get a
# little more: Claude Code is installed as a plugin, VS Code and its forks get
# the .vsix through `code --install-extension`, and bat's cache is rebuilt.
#
# Everything below is functions; the last line runs `main`, so under
# `curl | sh` the whole script is read before anything happens.
#
# shellcheck disable=SC2016,SC2088  # awk programs and ~ patterns are meant literally

REPO=oddurs/subway-seat
EXT_ID=oddurs.subway-seat
PLUGIN=subway-seat@subway-seat
MARK='>>> subway-seat >>>'
MARK_END='<<< subway-seat <<<'
NL='
'
TAB='	'

usage() {
  cat <<'EOF'
Subway Seat installer

usage: sh install.sh [command] [options]

  install            link themes into the apps you have (the default)
  switch <flavor>    re-point everything at walnut, tunnel, enamel or auto
  status             what's installed, what drifted, what's left by hand
  uninstall          remove everything the installer placed
  list               every port, and whether it's on this machine

  --flavor <name>    walnut, tunnel, enamel or auto (follow the OS where the
                     app can); default: your saved flavor, else walnut
  --only <ids>       only these ports (comma-separated ids from `list`)
  --skip <ids>       never these ports (takes them out if installed)
  --all              every port with a file to place, even if not detected
  --yes              don't ask             --dry-run   show the plan only
  --copy             copy files instead of linking them
  --no-enable        place theme files only; leave app configs alone
  --ref <tag>        with curl: install this tag or branch instead of main

Settings: ~/.config/subway-seat/config · record: ~/.local/state/subway-seat/installed
EOF
}

die() { printf 'install.sh: %s\n' "$*" >&2; exit 2; }
fail() { printf '%s\n' "$*" >&2; exit 1; }

# ── Arguments ───────────────────────────────────────────────────────────────
parse_args() {
  CMD='' TO='' FLAVOR='' ONLY='' SKIP='' HAS_ONLY='' HAS_SKIP='' REF='' COPY=''
  ALL=0 YES=0 DRY=0 NOENABLE=0
  while [ $# -gt 0 ]; do
    arg=$1
    case $arg in
      --flavor=* | --only=* | --skip=* | --ref=*) val=${arg#*=} arg=${arg%%=*} ;;
      --flavor | --only | --skip | --ref)
        [ $# -ge 2 ] || die "$arg needs a value"
        val=$2
        shift ;;
    esac
    case $arg in
      -h | --help | help) usage; exit 0 ;;
      --flavor) FLAVOR=$val ;;
      --only) ONLY=$val HAS_ONLY=1 ;;
      --skip) SKIP=$val HAS_SKIP=1 ;;
      --ref) REF=$val ;;
      --all) ALL=1 ;;
      --yes | -y) YES=1 ;;
      --dry-run | -n) DRY=1 ;;
      --copy) COPY=1 ;;
      --no-enable) NOENABLE=1 ;;
      -*) die "unknown option $arg (try --help)" ;;
      *)
        if [ -z "$CMD" ]; then CMD=$arg
        elif [ "$CMD" = switch ] && [ -z "$TO" ]; then TO=$arg
        else die "unexpected argument '$arg' (try --help)"
        fi ;;
    esac
    shift
  done
  CMD=${CMD:-install}
  case $CMD in
    install | status | uninstall | list) ;;
    switch)
      TO=${TO:-$FLAVOR}
      [ -n "$TO" ] || die "switch needs a flavor: walnut, tunnel, enamel or auto"
      FLAVOR=$TO ;;
    *) die "unknown command '$CMD' (try --help)" ;;
  esac
  case ${FLAVOR:-walnut} in
    walnut | tunnel | enamel | auto) ;;
    *) die "unknown flavor '$FLAVOR': pick walnut, tunnel, enamel or auto" ;;
  esac
  case $ONLY$SKIP in *[!a-z0-9,-]*) die "--only and --skip take port ids, like ghostty,vim" ;; esac
  case $REF in *[!A-Za-z0-9._/-]*) die "--ref takes a tag or branch name" ;; esac
}

# ── Small helpers ───────────────────────────────────────────────────────────
has() { command -v "$1" >/dev/null 2>&1; }

# unesc TEXT: undo build.py's escaping (sets R).
unesc() {
  case $1 in *\\*) R=$(printf '%b' "$1") ;; *) R=$1 ;; esac
}

# tilde PATH: $HOME/… → ~/… for display (sets R).
tilde() {
  case $1 in "$HOME"/*) R="~/${1#"$HOME"/}" ;; *) R=$1 ;; esac
}

# field N LINE: the Nth tab-separated field, empty ones included (sets R).
field() {
  R=$2 _fn=$1
  while [ "$_fn" -gt 1 ]; do
    case $R in *"$TAB"*) R=${R#*"$TAB"} ;; *) R='' ; return 0 ;; esac
    _fn=$((_fn - 1))
  done
  R=${R%%"$TAB"*}
}

# expand PATH: ~, $HOME and the XDG variables → an absolute path (sets R).
expand() {
  R=''
  case $1 in
    '~') R=$HOME ;;
    '~/'*) R=$HOME/${1#??} ;;
    '$HOME/'* | '${HOME}/'*) R=$HOME/${1#*/} ;;
    '$XDG_CONFIG_HOME/'*) R=${XDG_CONFIG_HOME:-$HOME/.config}/${1#*/} ;;
    '$XDG_DATA_HOME/'*) R=${XDG_DATA_HOME:-$HOME/.local/share}/${1#*/} ;;
    /*) R=$1 ;;
    *) return 1 ;;
  esac
}

plural() { [ "$1" -eq 1 ] || printf s; }

# mkparents PATH: mkdir -p its directory, remembering what was created.
mkparents() {
  _md=${1%/*} _mm=''
  while [ -n "$_md" ] && [ ! -d "$_md" ]; do
    _mm="$_md$NL$_mm"
    _md=${_md%/*}
  done
  [ -n "$_mm" ] || return 0
  mkdir -p "${1%/*}" || return 1
  MADE_DIRS="$MADE_DIRS$_mm"
}

# state_get KIND KEY: the recorded line of that kind for that key (sets R).
# The record is read into STATE_TEXT once; this only matches strings.
state_get() {
  case $STATE_TEXT in
    *"$NL$1$TAB$2$TAB"*) R=${STATE_TEXT#*"$NL$1$TAB$2$TAB"}; R="$1$TAB$2$TAB${R%%"$NL"*}" ;;
    *"$NL$1$TAB$2$NL"*) R="$1$TAB$2" ;;
    *) R=''; return 1 ;;
  esac
}

# ── Where the files are ─────────────────────────────────────────────────────
# Run from a checkout (or an unpacked copy), use it. Piped from curl, fetch the
# repo into ~/.local/share/subway-seat and carry on from there.
locate() {
  ROOT=''
  self=$0
  while [ -L "$self" ]; do
    link=$(readlink "$self")
    case $link in /*) self=$link ;; *) self=${self%/*}/$link ;; esac
  done
  case $self in */*) here=${self%/*} ;; *) here=. ;; esac
  if [ -f "$self" ] && [ -f "$here/dist/install.tsv" ]; then
    ROOT=$(cd -P "$here" && pwd -P)
  fi
  if [ -z "$ROOT" ] || [ -n "$REF" ] || [ -n "${SUBWAY_SEAT_TARBALL:-}" ]; then
    if [ "$CMD" = install ] || [ ! -f "$DATA_DIR/dist/install.tsv" ]; then
      [ "$CMD" = uninstall ] || [ "$CMD" = status ] || fetch
    fi
    [ -f "$DATA_DIR/dist/install.tsv" ] && ROOT=$(cd -P "$DATA_DIR" && pwd -P)
  fi
  DIST=${ROOT:+$ROOT/dist}
  TSV=${DIST:+$DIST/install.tsv}
  if [ -n "${SUBWAY_SEAT_SELF:-}" ]; then SELF=$SUBWAY_SEAT_SELF
  elif [ -n "$ROOT" ] && [ -f "$ROOT/install.sh" ]; then
    tilde "$ROOT/install.sh"
    case $R in *' '*) SELF="sh \"$ROOT/install.sh\"" ;; *) SELF="sh $R" ;; esac
  else SELF="sh install.sh"
  fi
}

fetch() {
  url=${SUBWAY_SEAT_TARBALL:-https://github.com/$REPO/archive/refs/heads/main.tar.gz}
  [ -n "$REF" ] && url=https://github.com/$REPO/archive/$REF.tar.gz
  printf 'Fetching Subway Seat%s…\n' "${REF:+ $REF}"
  case $url in
    http://* | https://*)
      if has curl; then curl -fsSL "$url" -o "$T/repo.tgz"
      elif has wget; then wget -qO "$T/repo.tgz" "$url"
      else fail "Needs curl or wget to download $url."
      fi ;;
    *) cp "$url" "$T/repo.tgz" ;;
  esac </dev/null || fail "Couldn't download $url."
  if ! mkdir "$T/repo" || ! (cd "$T/repo" && gzip -dc ../repo.tgz | tar -xf -); then fail "Couldn't unpack $url."; fi
  set -- "$T/repo"/*
  if [ $# -ne 1 ] || [ ! -f "$1/dist/install.tsv" ]; then fail "$url doesn't look like Subway Seat."; fi
  mkparents "$DATA_DIR/x" || fail "Couldn't create $DATA_DIR."
  rm -rf "$DATA_DIR.old"
  if [ -d "$DATA_DIR" ]; then mv "$DATA_DIR" "$DATA_DIR.old" || fail "Couldn't replace $DATA_DIR."; fi
  mv "$1" "$DATA_DIR" || fail "Couldn't move the download to $DATA_DIR."
  rm -rf "$DATA_DIR.old"
  : >"$DATA_DIR/.downloaded-by-install.sh"
}

# ── Saved settings and the record ───────────────────────────────────────────
# The config is key=value lines, read (never sourced) on every run. The record
# lists every link, copy, block, directory and command, one per line.
load_settings() {
  C_FLAVOR='' C_ONLY='' C_SKIP=''
  if [ -f "$CONF" ]; then
    while IFS='=' read -r key val; do
      case $key in flavor) C_FLAVOR=$val ;; only) C_ONLY=$val ;; skip) C_SKIP=$val ;; esac
    done <"$CONF"
  fi
  S_ROOT='' S_FLAVOR='' S_MODE='' S_APPS=' ' STATE_TEXT=$NL
  if [ -f "$STATE" ]; then
    STATE_TEXT="$NL$(cat "$STATE")$NL"
    while IFS= read -r line; do
      field 2 "$line"
      case $line in
        root"$TAB"*) S_ROOT=$R ;;
        flavor"$TAB"*) S_FLAVOR=$R ;;
        mode"$TAB"*) S_MODE=$R ;;
        app"$TAB"*) S_APPS="$S_APPS$R " ;;
      esac
    done <"$STATE"
  fi
  [ -n "$HAS_ONLY" ] || ONLY=$C_ONLY
  [ -n "$HAS_SKIP" ] || SKIP=$C_SKIP
  FLAVOR=${FLAVOR:-${C_FLAVOR:-${S_FLAVOR:-walnut}}}
  case $FLAVOR in walnut | tunnel | enamel | auto) ;; *) FLAVOR=walnut ;; esac
  if [ -z "$COPY" ]; then
    if [ -n "$S_MODE" ]; then [ "$S_MODE" = copy ] && COPY=1
    elif [ -n "$ROOT" ] && [ ! -e "$ROOT/.git" ]; then COPY=1
    fi
  fi
  COPY=${COPY:-0}
  VERSION=''
  if [ -n "$TSV" ] && [ -f "$TSV" ]; then
    while IFS="$TAB" read -r kind a _; do
      case $kind in version) VERSION=$a ;; port) break ;; esac
    done <"$TSV"
  fi
}

flavor_name() {
  case $1 in
    walnut) R=Walnut ;;
    tunnel) R=Tunnel ;;
    enamel) R=Enamel ;;
    *) R="light and dark (auto)" ;;
  esac
}

# ── Colors: the palette's own accents, when there's a terminal to paint ─────
colors() {
  B='' D='' O='' GOLD='' ORANGE='' GREEN='' RED=''
  [ -t 1 ] && [ -z "${NO_COLOR:-}" ] && [ "${TERM:-}" != dumb ] || return 0
  E=$(printf '\033')
  B="${E}[1m" D="${E}[2m" O="${E}[0m"
  # The plain ANSI slots are the palette itself in a Subway Seat terminal.
  GOLD="${E}[33m" ORANGE="${E}[35m" GREEN="${E}[32m" RED="${E}[91m"
  case ${COLORTERM:-} in truecolor | 24bit) ;; *) return 0 ;; esac
  [ -n "$TSV" ] && [ -f "$TSV" ] || return 0
  paint=walnut
  [ "$FLAVOR" = enamel ] && paint=enamel
  while IFS="$TAB" read -r kind fl role hex; do
    [ "$kind" = port ] && break
    if [ "$kind" != color ] || [ "$fl" != "$paint" ]; then continue; fi
    hex=${hex#\#}
    g=${hex#??}
    c=$(printf '%s[38;2;%d;%d;%dm' "$E" "0x${hex%????}" "0x${g%??}" "0x${hex#????}")
    case $role in yellow) GOLD=$c ;; orange) ORANGE=$c ;; green) GREEN=$c ;; red_hi) RED=$c ;; esac
  done <"$TSV"
}

header() {
  printf '%s%sSubway Seat%s%s %s%s%s\n' "$B" "$GOLD" "$O" "${VERSION:+ $VERSION}" "$D" "$1" "$O"
}

need_tsv() {
  if [ -z "$TSV" ] || [ ! -f "$TSV" ]; then
    fail "Can't find dist/install.tsv. Run this from a Subway Seat checkout, or pipe it from curl."
  fi
}

# ── The plan ────────────────────────────────────────────────────────────────
# One awk pass turns install.tsv into what the chosen apps want, for one
# flavor: `link` (a theme file), `part` (text for the marked block in a config
# file), `run` (an app's own installer) and `step` (something only a person can
# do). Every flavor's files are linked so each app's own theme picker sees all
# three; where flavors share one destination, only the chosen one goes in.
UNESC_AWK='
function unesc(s,   out, i, c, n) {
  if (index(s, "\\") == 0) return s
  out = ""; n = length(s)
  for (i = 1; i <= n; i++) {
    c = substr(s, i, 1)
    if (c == "\\" && i < n) { c = substr(s, ++i, 1); if (c == "n") c = "\n"; else if (c == "t") c = "\t" }
    out = out c
  }
  return out
}
'
PLAN_AWK='
function prose(p) {
  return index(p, "→") || index(p, "›") || index(p, "`") || index(p, "; ") || index(p, ", ") || index(p, " (") || index(p, " or ") || index(p, "<")
}
function expand(p,   i, cmd, w, out) {
  if (p == "" || prose(p)) return ""
  if (p == "~") return HOME
  if (substr(p, 1, 2) == "~/") return HOME substr(p, 2)
  if (p ~ /^\$HOME\// || p ~ /^\$\{HOME\}\//) return HOME substr(p, index(p, "/"))
  if (p ~ /^\$XDG_CONFIG_HOME\//) return XC substr(p, index(p, "/"))
  if (p ~ /^\$XDG_DATA_HOME\//) return XD substr(p, index(p, "/"))
  if (substr(p, 1, 1) == "/") return p
  if (substr(p, 1, 2) == "$(" && (i = index(p, ")/"))) {
    cmd = substr(p, 3, i - 3)
    if (!(cmd in ran)) {
      split(cmd, w, " "); out = ""
      if (w[1] ~ /^[A-Za-z0-9_.-]+$/ && system("command -v " w[1] " >/dev/null 2>&1") == 0) {
        (cmd " </dev/null 2>/dev/null") | getline out; close(cmd " </dev/null 2>/dev/null")
      }
      ran[cmd] = out
    }
    return ran[cmd] == "" ? "" : ran[cmd] substr(p, i + 1)
  }
  return ""
}
function trivial(t) { t = tolower(t); return t ~ /^(packaged|inside|bundled|included)/ }
# Files that exist to follow the OS light/dark setting only matter with --flavor auto.
function autofile(src) { return src ~ /(^|\/)auto\// || src ~ /(^|[\/_.-])auto[_.-][^\/]*$/ }
function clear() {
  nf = nh = ns = has_auto = vsix = 0
  split("", ef); split("", ec); split("", ew); split("", el); split("", es)
}
# step(text, file): a step by hand, merged with others that say the same thing.
function step(text, file,   k) {
  for (k = 1; k <= ns; k++) if (st[k] == text) { sf[k] = sf[k] "\\n" file; return }
  st[++ns] = text; sf[ns] = file
}
function flush(   F, base, i, j, shared, used, placed, code, file, where, lang, sh, dest, bat) {
  if (pid == "" || !sel) return
  F = flavor
  if (F == "auto" && !has_auto) F = "walnut"
  base = F == "auto" ? "walnut" : F
  print "app\t" pid "\t" pname "\t" pcat "\t" preq
  if (pid == "claude-code") { print "run\t" pid "\tclaude"; clear(); return }
  split("", used); split("", placed)
  for (i = 1; i <= nf; i++) {
    if (pid == "vscode" && fs[i] ~ /\.vsix$/) { print "run\t" pid "\tvsix\t" fs[i]; vsix = 1; continue }
    if (ff[i] == "*" && (fd[i] == "" || fm[i] == "append") && autofile(fs[i]) && flavor != "auto") continue
    if (fm[i] == "append") {
      if (ff[i] != "*" && ff[i] != base) continue
      if (fd[i] == "" || noenable) step("Add this to the end of " raw[i], fs[i])
      else print "part\t" fd[i] "\t" pid "\tfile\t" fs[i] "\t"
      continue
    }
    if (ff[i] != "*" && ff[i] != base) {
      shared = fd[i] == ""
      for (j = 1; j <= nf && !shared; j++) if (j != i && raw[j] == raw[i] && ff[j] != ff[i]) shared = 1
      if (shared) continue
    }
    if (fd[i] == "") { if (!trivial(raw[i])) step(raw[i], fs[i]); continue }
    placed[fs[i]] = fd[i]
    if (fd[i] in used) continue
    used[fd[i]] = 1
    print "link\t" pid "\t" fd[i] "\t" fs[i]
    if (pid == "bat") bat = 1
  }
  for (i = 1; i <= nh; i++) {
    if (hf[i] != "*" && hf[i] != base) continue
    if (hf[i] == "*" && autofile(hs[i]) && flavor != "auto") continue
    if (pid == "vscode" && hs[i] ~ /\.vsix$/) { if (!vsix) print "run\t" pid "\tvsix\t" hs[i]; vsix = 1; continue }
    step(ht[i], hs[i] in placed ? placed[hs[i]] : hs[i])
  }
  for (i = 1; i <= ns; i++) print "step\t" pid "\thow\t" st[i] "\t" sf[i]
  if (F == "auto") { file = af; code = ac; where = aw; lang = al; sh = "" }
  else { file = ef[base]; code = ec[base]; where = ew[base]; lang = el[base]; sh = es[base] }
  if (code != "") {
    dest = expand(file)
    if (dest != "" && !noenable && lang !~ /^(json|xml|text)$/ && (dest !~ /\.fish$/ || fishok))
      print "part\t" dest "\t" pid "\tcode\t" code "\t" lang
    else if (lang == "fish" && sh != "" && shell != "fish")
      print "step\t" pid "\tin\tyour shell startup file (~/.zshrc or ~/.bashrc)\t" sh
    else print "step\t" pid "\tin\t" where "\t" code
  }
  if (bat) print "run\tbat\tbat"
  clear()
}
BEGIN {
  FS = "\t"; HOME = ENVIRON["HOME"]; flavor = ENVIRON["SS_FLAVOR"]; targets = ENVIRON["SS_TARGETS"]
  noenable = ENVIRON["SS_NOENABLE"] == 1; fishok = ENVIRON["SS_FISH"] == 1; shell = ENVIRON["SS_SHELL"]
  XC = ENVIRON["XDG_CONFIG_HOME"]; if (XC == "") XC = HOME "/.config"
  XD = ENVIRON["XDG_DATA_HOME"]; if (XD == "") XD = HOME "/.local/share"
}
$1 == "port" { flush(); pid = $2; pname = unesc($3); pcat = unesc($4); preq = unesc($5); sel = targets == "*" || index(targets, " " pid " "); next }
!sel { next }
$1 == "file" && substr($5, 1, 1) == "%" { next }  # a Windows path: nothing to do here
$1 == "file" { nf++; ff[nf] = $3; fs[nf] = unesc($4); raw[nf] = unesc($5); fd[nf] = expand(raw[nf]); fm[nf] = $6; next }
$1 == "how" { nh++; hf[nh] = $3; ht[nh] = $4; hs[nh] = unesc($5); next }
$1 == "enable" { ef[$3] = unesc($4); ec[$3] = $5; ew[$3] = $6; el[$3] = $7; es[$3] = $8; next }
$1 == "auto" { has_auto = 1; af = unesc($3); ac = $4; aw = $5; al = $6; next }
END { flush() }
'

# plan FLAVOR TARGETS: print the plan (TARGETS is " id id " or "*").
plan() {
  fish=0
  has fish && fish=1
  SS_FLAVOR=$1 SS_TARGETS=$2 SS_NOENABLE=$NOENABLE SS_FISH=$fish SS_SHELL=${SUBWAY_SEAT_SHELL:-${SHELL##*/}} \
    awk "$UNESC_AWK$PLAN_AWK" "$TSV"
}

# A port is detected when any probe is a command on PATH or an existing path
# (/Applications/X.app also counts in ~/Applications).
detect_all() {
  DETECTED=' '
  awk -F'\t' '$1 == "detect" { print $2 "\t" $3 }' "$TSV" >"$T/detect"
  while IFS="$TAB" read -r id probe; do
    case $DETECTED in *" $id "*) continue ;; esac
    unesc "$probe"; probe=$R
    case $probe in
      /* | '~'* | '$'*)
        if expand "$probe" && [ -e "$R" ]; then DETECTED="$DETECTED$id "
        else
          case $probe in /Applications/*) [ -e "$HOME$probe" ] && DETECTED="$DETECTED$id " ;; esac
        fi ;;
      *) has "$probe" && DETECTED="$DETECTED$id " ;;
    esac
  done <"$T/detect"
}

# ── Comparing the plan with the disk and the record ─────────────────────────
# A link is ours when it points into this dist, into any Subway Seat dist (an
# older checkout, the curl copy, the old install.fish), or where we left it.
ours_link() {
  case $1 in "$DIST"/* | */subway-seat*/dist/*) return 0 ;; esac
  state_get link "$2" && field 3 "$R" && [ "$R" = "$1" ]
}

# classify_link DEST SRC: new, same, update or conflict (sets R).
classify_link() {
  want=$DIST/$2
  # shellcheck disable=SC3013 # -ef works in dash, bash, busybox ash and macOS sh
  if [ -L "$1" ] && [ "$COPY" = 0 ] && [ "$1" -ef "$want" ] && state_get link "$1"; then R=same
  elif [ -L "$1" ]; then
    target=$(readlink "$1")
    if [ "$target" = "$want" ] && [ "$COPY" = 0 ]; then R=same
    elif ours_link "$target" "$1"; then R=update
    else R=conflict
    fi
  elif [ -d "$1" ]; then R=conflict
  elif [ -e "$1" ]; then
    if cmp -s "$1" "$want"; then
      if [ "$COPY" = 1 ]; then R=same; else R=update; fi
    elif state_get copy "$1" && field 4 "$R" && [ "$R" = "$(cksum <"$1")" ]; then R=update
    else R=conflict
    fi
  else R=new
  fi
}

# edit_block FILE replace|strip [NEWBLOCK] [PREFIX]: rewrite FILE in place,
# through a symlink if it is one. `replace` swaps the first marked block for
# NEWBLOCK and drops any others; `strip` removes every marked block and the
# separator we added in front of ours (PREFIX says which).
EDIT_AWK='
BEGIN { S = ENVIRON["S"]; E = ENVIRON["E"]; mode = ENVIRON["MODE"]; prefix = ENVIRON["PREFIX"]; nonl_in = ENVIRON["NONL"] == 1 }
{ L[++n] = $0 }
END {
  if (mode == "replace") while ((getline l < ENVIRON["NEW"]) > 0) nb[++m] = l
  for (i = 1; i <= n; i++) {
    if (!skip && index(L[i], S)) {
      skip = 1
      if (!pos) { pos = o + 1; if (mode == "replace") for (k = 1; k <= m; k++) O[++o] = nb[k] }
      continue
    }
    if (skip) { if (index(L[i], E)) skip = 0; continue }
    O[++o] = L[i]
  }
  atend = mode == "strip" && pos && pos == o + 1
  if (mode == "strip" && pos > 1 && (prefix == "blank" || prefix == "nl") && O[pos - 1] == "") {
    for (k = pos - 1; k < o; k++) O[k] = O[k + 1]
    o--
  }
  if (atend) nonl = prefix == "nl"
  else nonl = nonl_in && !(mode == "replace" && pos && pos + m - 1 == o)
  for (k = 1; k <= o; k++) printf "%s%s", O[k], (k < o || !nonl) ? "\n" : ""
}
'
edit_block() {
  nonl=0
  [ -s "$1" ] && [ -n "$(tail -c 1 "$1")" ] && nonl=1
  S=$MARK E=$MARK_END MODE=$2 NEW=${3:-} PREFIX=${4:-none} NONL=$nonl awk "$EDIT_AWK" "$1" >"$T/edit" &&
    cat "$T/edit" >"$1"
}

# blocks: build our block for every config file in the plan, in one pass, and
# compare it with the block already there. Writes $T/block.N and prints
# "file N status" (new, same, update or conflict) per file. Appended files bring
# their own marker lines; code gets marker lines in its own comment syntax.
BLOCKS_AWK='
function leader(lang) {
  if (lang == "lua") return "--"
  if (lang == "vim") return "\""
  if (lang == "elisp") return ";;"
  if (lang ~ /^(kdl|js|typescript|go|scss|ron)$/) return "//"
  if (lang == "css") return "/*"
  return "#"
}
BEGIN { FS = "\t"; S = ENVIRON["S"]; E = ENVIRON["E"]; dist = ENVIRON["SS_DIST"]; tmp = ENVIRON["SS_TMP"] }
$1 == "link" { linked[$3] = 1; next }
$1 != "part" { next }
!($2 in num) { num[$2] = ++n; file[n] = $2 }
{
  k = num[$2]
  if ($4 == "file") {
    src = dist "/" $5
    while ((getline l < src) > 0) {
      if (index(l, S)) { if (start[k] == "") start[k] = l; continue }
      if (index(l, E)) { if (end[k] == "") end[k] = l; continue }
      body[k] = body[k] l "\n"
    }
    close(src)
  } else { body[k] = body[k] unesc($5) "\n"; lang[k] = $6 }
}
END {
  for (k = 1; k <= n; k++) {
    c = leader(lang[k]); close_c = c == "/*" ? " */" : ""
    if (start[k] == "") start[k] = c " " S close_c
    if (end[k] == "") end[k] = c " " E close_c
    want = start[k] "\n" body[k] end[k] "\n"
    out = tmp "/block." k
    printf "%s", want > out; close(out)
    cur = ""; inb = bad = nreg = 0
    while ((r = (getline l < file[k])) > 0) {
      if (index(l, S)) { if (inb) bad = 1; inb = 1; nreg++ }
      if (inb && nreg == 1) cur = cur l "\n"
      if (index(l, E)) { if (!inb) bad = 1; inb = 0 }
    }
    close(file[k])
    st = r < 0 || !nreg ? "new" : inb || bad ? "conflict" : nreg > 1 || cur != want ? "update" : "same"
    if (file[k] in linked) st = "ours"
    print file[k] "\t" k "\t" st
  }
}
'

# classify: compare the plan with the disk and the record. Writes $T/act:
#   A id name category             an app
#   L id status dest src           a theme file (new, same, update, conflict)
#   B id status file summary       its part of a marked block
#   X id status what text arg src  a command (claude, ext, bat)
#   S id in|how text extra         a step by hand
#   R key remove kind …            something recorded that nobody wants now
#   T - remove path why            a leftover from the old install.fish
# plus $T/blocks (file, block number, status) and WANT (what stays).
classify() {
  : >"$T/act"
  WANT=$NL
  S=$MARK E=$MARK_END SS_DIST=$DIST SS_TMP=$T awk "$UNESC_AWK$BLOCKS_AWK" "$T/plan" >"$T/blocks.raw"
  # Some files can't take a block: say why instead.
  : >"$T/blocks"
  while IFS="$TAB" read -r file n st; do
    why=''
    if [ -d "$file" ]; then why="it's a directory"
    elif [ -L "$file" ] && [ ! -e "$file" ]; then why="it's a link to nowhere"
    elif [ -L "$file" ]; then
      case $(readlink "$file") in "$DIST"/* | */subway-seat*/dist/*) why="it's one of our own files" ;; esac
    elif [ "$st" = conflict ]; then why="its subway-seat markers are unmatched"
    elif [ "$st" = ours ]; then why="the same port links a whole file there"
    fi
    [ -n "$why" ] && st=conflict
    printf '%s\t%s\t%s\t%s\n' "$file" "$n" "$st" "$why" >>"$T/blocks"
  done <"$T/blocks.raw"
  BLOCKS="$NL$(cat "$T/blocks")$NL"
  while IFS= read -r line; do
    field 1 "$line"; kind=$R
    field 2 "$line"; id=$R
    case $kind in
      app)
        printf 'A\t%s\n' "${line#app"$TAB"}" >>"$T/act" ;;
      link)
        field 3 "$line"; dest=$R
        field 4 "$line"; src=$R
        classify_link "$dest" "$src"
        printf 'L\t%s\t%s\t%s\t%s\n' "$id" "$R" "$dest" "$src" >>"$T/act"
        WANT="$WANT${dest}$NL" ;;
      part)
        file=$id
        field 3 "$line"; id=$R
        field 4 "$line"; pkind=$R
        field 5 "$line"
        if [ "$pkind" = file ]; then summary="the lines in ${R#*/}"
        else
          unesc "$R"; summary=${R%%"$NL"*}
          [ "$summary" = "$R" ] || summary="$summary …"
        fi
        WANT="${WANT}block$TAB$file$NL"
        field 2 "${BLOCKS#*"$NL$file$TAB"}"; st=$R
        if [ "$st" = conflict ]; then field 3 "${BLOCKS#*"$NL$file$TAB"}"; summary="(left alone: ${R%%"$NL"*})"; fi
        printf 'B\t%s\t%s\t%s\t%s\n' "$id" "$st" "$file" "$summary" >>"$T/act" ;;
      run)
        field 3 "$line"; what=$R
        field 4 "$line"
        classify_run "$id" "$what" "$R" ;;
      step)
        printf 'S\t%s\n' "${line#step"$TAB"}" >>"$T/act" ;;
    esac
  done <"$T/plan"
  forget_unwanted
}

vsix_clis() {
  for c in code codium cursor windsurf; do command -v "$c" 2>/dev/null; done
  has code && return 0
  for c in "/Applications/Visual Studio Code.app/Contents/Resources/app/bin/code" \
    "$HOME/Applications/Visual Studio Code.app/Contents/Resources/app/bin/code"; do
    [ -x "$c" ] && printf '%s\n' "$c" && return 0
  done
}

# classify_run ID WHAT ARG: the apps that come with their own installer.
classify_run() {
  case $2 in
    claude)
      if ! has claude; then
        printf 'S\t%s\tin\ta shell, once Claude Code is installed\tclaude plugin marketplace add %s\\nclaude plugin install %s\\n# then, in Claude Code: /subway-seat:setup\n' \
          "$1" "$REPO" "$PLUGIN" >>"$T/act"
        return 0
      fi
      if state_get plugin install; then st=same
      elif claude plugin list </dev/null 2>/dev/null | grep -q -F "$PLUGIN"; then st=present
      else st=new
      fi
      if [ "$st" = new ]; then
        if state_get plugin market; then :
        elif ! claude plugin marketplace list </dev/null 2>/dev/null | grep -q -E "[[:space:]]subway-seat\$"; then
          printf 'X\t%s\tnew\tmarket\tclaude plugin marketplace add %s\n' "$1" "$REPO" >>"$T/act"
        fi
        printf 'S\t%s\tin\tClaude Code, to pick the flavor, status line and verbs\t/subway-seat:setup\n' "$1" >>"$T/act"
      fi
      printf 'X\t%s\t%s\tplugin\tclaude plugin install %s\n' "$1" "$st" "$PLUGIN" >>"$T/act"
      WANT="${WANT}plugin${TAB}install${NL}plugin${TAB}market$NL" ;;
    vsix)
      vsix_clis >"$T/clis"
      if [ ! -s "$T/clis" ]; then
        printf 'S\t%s\tin\tVS Code (or Cursor, VSCodium, Windsurf), then pick Subway Seat in Preferences › Color Theme\tcode --install-extension "%s"\n' \
          "$1" "$DIST/$3" >>"$T/act"
        return 0
      fi
      sum=$(cksum <"$DIST/$3")
      while IFS= read -r cli; do
        if state_get ext "$cli" && field 3 "$R" && [ "$R" = "$sum" ]; then st=same
        elif [ -n "$R" ]; then st=update
        else st=new
        fi
        printf 'X\t%s\t%s\text\t%s\t%s\t%s\t%s\n' "$1" "$st" "${cli##*/} --install-extension ${3##*/}" "$cli" "$3" "$sum" >>"$T/act"
        WANT="${WANT}ext$TAB$cli$NL"
      done <"$T/clis" ;;
    bat)
      has bat && printf 'X\tbat\tlater\tbat\tbat cache --build\n' >>"$T/act" ;;
  esac
}

# wanted THING: is it in the plan? (links are listed by path, the rest as "kind<TAB>key")
wanted() { case $WANT in *"$NL$1$NL"*) return 0 ;; esac; return 1; }

# Recorded things the plan no longer wants are taken out again.
forget_unwanted() {
  [ -f "$STATE" ] || return 0
  while IFS="$TAB" read -r kind key a b c d; do
    case $kind in
      link)  # link dest target id
        wanted "$key" || printf 'R\t%s\tremove\tlink\t%s\t%s\n' "$b" "$key" "$a" >>"$T/act" ;;
      copy)  # copy dest src cksum id
        wanted "$key" || printf 'R\t%s\tremove\tcopy\t%s\t%s\t%s\n' "$c" "$key" "$a" "$b" >>"$T/act" ;;
      block)  # block file prefix made
        wanted "block$TAB$key" || printf 'R\t-\tremove\tblock\t%s\t%s\t%s\n' "$key" "$a" "$b" >>"$T/act" ;;
      ext)  # ext cli cksum preexisting
        wanted "ext$TAB$key" || printf 'R\t-\tremove\text\t%s\t%s\n' "$key" "$b" >>"$T/act" ;;
      plugin)  # plugin install|market
        wanted "plugin$TAB$key" || printf 'R\t-\tremove\tplugin\t%s\n' "$key" >>"$T/act" ;;
    esac
  done <"$STATE"
}

# Links and the conf.d file left by the old install.fish, which kept no record.
LEGACY_DIRS='.config/ghostty/themes .config/kitty/themes .config/alacritty/themes .config/wezterm/colors
.config/fish/themes .config/bat/themes .config/delta .config/btop/themes .config/yazi/flavors .vim/colors
.local/share/nvim/site/pack/subway-seat/start .local/share/nvim/site/colors .config/helix/themes
.config/zed/themes .claude/themes .config/opencode/themes .codex/themes'
legacy() {
  for rel in $LEGACY_DIRS; do
    for f in "$HOME/$rel"/*; do
      [ -L "$f" ] || continue
      case $(readlink "$f") in */subway-seat*/dist/*) ;; *) continue ;; esac
      wanted "$f" && continue
      state_get link "$f" && continue
      why="left by the old install.fish"
      [ "$rel" = .claude/themes ] && why="the Claude Code plugin carries the themes"
      printf 'T\t-\tremove\t%s\t%s\n' "$f" "$why" >>"$T/act"
    done
  done
  f=$HOME/.config/fish/conf.d/subway-seat.fish
  [ -f "$f" ] && [ ! -L "$f" ] || return 0
  sed -n 1p "$f" | grep -q '^# Subway Seat — written by install.fish' || return 0
  # It sets the fish theme and fzf colors, so it stays until a block takes over.
  if [ "$CMD" = uninstall ] || grep -q "^part${TAB}[^$TAB]*${TAB}fish$TAB" "$T/plan"; then
    printf 'T\t-\tremove\t%s\t%s\n' "$f" "written by the old install.fish" >>"$T/act"
  fi
}

# ── Showing it ──────────────────────────────────────────────────────────────
SHOW_AWK='
function tilde(p) { return index(p, HOME "/") == 1 ? "~" substr(p, length(HOME) + 1) : p }
function shown(p) { return index(p, " ") ? "\"" p "\"" : tilde(p) }
function dir(p) { sub(/\/[^\/]*$/, "/", p); return p }
function base(p) { sub(/^.*\//, "", p); return p }
# label(name): the name column; a name too long for it gets a line of its own.
function label(name) {
  if (length(name) < 15) return sprintf("  %-15s", name)
  return "  " name "\n" sprintf("  %-15s", "")
}
function say(v, c, text) {
  if (!app_shown) {
    if (cat != last_cat) { print ""; print BOLD cat OFF; last_cat = cat }
    printf "%s", label(name); app_shown = 1
  } else printf "  %-15s", ""
  printf "%s%-7s%s %s\n", c, v, OFF, text
}
# Links are grouped by verb and directory: "link ~/.vim/colors/ a, b, c".
function flush_links(   k) {
  for (k = 1; k <= lk_n; k++) say(lk_verb[k], GREEN, tilde(lk_dir[k]) "  " lk_names[k])
  lk_n = 0
}
function end_app() {
  flush_links()
  if (mode == "plan" && name != "" && !app_shown && (quiet || hand)) {
    if (cat != last_cat) { print ""; print BOLD cat OFF; last_cat = cat }
    printf "%s%s\n", label(name), DIM (quiet ? "up to date" : "by hand, see the end") OFF
  }
  quiet = hand = app_shown = batmove = 0
}
function end_actions() { if (mode == "plan" && app_shown && req != "") say("", "", DIM "needs " req OFF); req = "" }
BEGIN {
  FS = "\t"; HOME = ENVIRON["HOME"]; mode = ENVIRON["SS_MODE"]; copy = ENVIRON["SS_COPY"] == 1; dist = ENVIRON["SS_DIST"]
  BOLD = ENVIRON["B"]; DIM = ENVIRON["D"]; OFF = ENVIRON["O"]
  GREEN = ENVIRON["GREEN"]; ORANGE = ENVIRON["ORANGE"]; RED = ENVIRON["RED"]; GOLD = ENVIRON["GOLD"]
}
$1 == "A" { end_actions(); end_app(); id = $2; name = $3; cat = $4; req = $5; next }
mode == "steps" {
  if ($1 != "S") next
  if (!hdr) { print ""; print BOLD "By hand" OFF; hdr = 1 }
  printf "%s", ($2 != last_step ? label(name) : sprintf("  %-15s", "")); last_step = $2
  text = unesc($4); sub(/:$/, "", text)
  if ($3 == "in") { print "In " text ":"; n = split(unesc($5), lines, "\n") }
  else {
    print text ":"; n = split(unesc($5), lines, "\n")
    for (k = 1; k <= n; k++) lines[k] = shown(substr(lines[k], 1, 1) == "/" ? lines[k] : dist "/" lines[k])
  }
  for (k = 1; k <= n; k++) printf "  %-15s  %s%s%s\n", "", GOLD, lines[k], OFF
  next
}
$1 == "S" { hand++; next }
$1 == "L" {
  if ($3 == "same") { quiet++; next }
  if ($3 == "conflict") { say("skip", RED, tilde($4) "  " DIM "(not ours; left alone)" OFF); next }
  v = copy ? "copy" : $3 == "new" ? "link" : "relink"
  for (k = 1; k <= lk_n; k++) if (lk_dir[k] == dir($4) && lk_verb[k] == v) break
  if (k > lk_n) { lk_n = k; lk_dir[k] = dir($4); lk_verb[k] = v; lk_names[k] = base($4) }
  else lk_names[k] = lk_names[k] ", " base($4)
  if ($2 == "bat") batmove = 1
  next
}
{ flush_links() }
$1 == "B" {
  if ($3 == "same") { quiet++; next }
  if ($3 == "conflict") say("skip", RED, tilde($4) "  " DIM $5 OFF)
  else say($3 == "new" ? "add" : "update", ORANGE, tilde($4) "  " DIM $5 OFF)
  next
}
$1 == "X" {
  if ($3 == "same" || $3 == "present") quiet++
  else if ($3 != "later" || batmove) say("run", GOLD, $5)
  next
}
$1 == "T" || $1 == "R" {
  if ($1 != group) { end_actions(); end_app(); name = ""; print ""; print BOLD ($1 == "T" ? "Tidying up" : "Taking out") OFF; group = $1 }
  if ($1 == "T") printf "  %-15s%s%-7s%s %s  %s\n", "", RED, "remove", OFF, tilde($4), DIM "(" $5 ")" OFF
  else if ($4 == "block") printf "  %-15s%s%-7s%s %s  %s\n", "", RED, "remove", OFF, tilde($5), DIM "(our block)" OFF
  else if ($4 == "ext") { if ($6 == "0") printf "  %-15s%s%-7s%s %s\n", "", GOLD, "run", OFF, base($5) " --uninstall-extension " ENVIRON["EXT"] }
  else if ($4 == "plugin") printf "  %-15s%s%-7s%s %s\n", "", GOLD, "run", OFF, ($5 == "install" ? "claude plugin uninstall " ENVIRON["PLUGIN"] : "claude plugin marketplace remove subway-seat")
  else printf "  %-15s%s%-7s%s %s\n", "", RED, "remove", OFF, tilde($5)
  next
}
END { end_actions(); end_app() }
'
show() {
  SS_MODE=$1 SS_COPY=$COPY SS_DIST=$DIST EXT=$EXT_ID PLUGIN=$PLUGIN \
    B=$B D=$D O=$O GREEN=$GREEN ORANGE=$ORANGE RED=$RED GOLD=$GOLD \
    awk "$UNESC_AWK$SHOW_AWK" "$T/act"
}

# ── Doing it ────────────────────────────────────────────────────────────────
oops() { FAILED=$((FAILED + 1)); printf '  %sfailed%s  %s\n' "$RED" "$O" "$*" >&2; }
record() { printf '%s\n' "$1" >>"$T/state"; }

# place DEST SRC: link or copy one theme file.
place() {
  mkparents "$1" || return 1
  if [ -L "$1" ] || [ -f "$1" ]; then rm -f "$1" || return 1; fi
  if [ "$COPY" = 1 ]; then cp "$DIST/$2" "$1"; else ln -s "$DIST/$2" "$1"; fi
}

# take_out link|copy DEST TARGET CKSUM: remove a file we placed if it's still
# ours, then put back whatever we had moved aside for it.
take_out() {
  if [ "$1" = link ]; then
    # shellcheck disable=SC3013 # -ef works in dash, bash, busybox ash and macOS sh
    if [ -L "$2" ] && { [ "$2" -ef "$3" ] || [ "$(readlink "$2")" = "$3" ]; }; then rm -f "$2" || return 1
    elif [ -e "$2" ] || [ -L "$2" ]; then tilde "$2"; printf '  %s%s%s    %s (it changed since it was linked)\n' "$D" kept "$O" "$R"
    fi
  elif [ -f "$2" ] && [ ! -L "$2" ] && [ "$(cksum <"$2")" = "$4" ]; then rm -f "$2" || return 1
  elif [ -e "$2" ] || [ -L "$2" ]; then tilde "$2"; printf '  %s%s%s    %s (you changed it since it was copied)\n' "$D" kept "$O" "$R"
  fi
  if state_get bak "$2"; then
    field 3 "$R"
    if [ ! -e "$2" ] && [ ! -L "$2" ] && { [ -e "$R" ] || [ -L "$R" ]; }; then mv "$R" "$2"; fi
  fi
  return 0
}

apply() {  # apply BACKUP: carry out $T/act (BACKUP=1 moves conflicting files aside)
  : >"$T/state"
  FAILED=0 N_LINK=0 N_BLOCK=0 N_RUN=0 BAT_CHANGED=0 REMOVED=0
  # 1. Tidy up, and take out what nobody wants any more.
  while IFS="$TAB" read -r k key st a b c d; do
    case $k in
      T) REMOVED=1; rm -f "$a" || oops "remove $a" ;;
      R)
        REMOVED=1
        case $a in
          link | copy)
            take_out "$a" "$b" "$c" "$d" || oops "remove $b"
            [ "$key" = bat ] && BAT_CHANGED=1 ;;
          block)
            if [ -f "$b" ]; then
              edit_block "$b" strip "" "$c" || oops "remove our block from $b"
              [ "$d" = 1 ] && [ ! -s "$b" ] && rm -f "$b"
            fi ;;
          ext)
            if [ "$c" = 0 ] && [ -x "$b" ]; then
              "$b" --uninstall-extension "$EXT_ID" </dev/null >/dev/null 2>&1 || oops "${b##*/} --uninstall-extension $EXT_ID"
            fi ;;
          plugin)
            has claude || continue
            if [ "$b" = install ]; then
              claude plugin uninstall "$PLUGIN" </dev/null >/dev/null 2>&1 || oops "claude plugin uninstall $PLUGIN"
            else
              claude plugin marketplace remove subway-seat </dev/null >/dev/null 2>&1 || oops "claude plugin marketplace remove subway-seat"
            fi ;;
        esac ;;
    esac
  done <"$T/act"
  # 2. Theme files.
  while IFS="$TAB" read -r k id st dest src; do
    [ "$k" = L ] || continue
    if state_get bak "$dest"; then record "$R"
    elif [ "$st" = conflict ] && [ "$1" = 1 ] && [ ! -d "$dest" ] && [ ! -e "$dest.subway-seat.bak" ]; then
      mv "$dest" "$dest.subway-seat.bak" && record "bak$TAB$dest$TAB$dest.subway-seat.bak" && st=new
    fi
    case $st in
      conflict) continue ;;
      new | update)
        place "$dest" "$src" || { oops "place $dest"; continue; }
        N_LINK=$((N_LINK + 1))
        [ "$id" = bat ] && BAT_CHANGED=1 ;;
    esac
    if [ "$COPY" = 1 ]; then record "copy$TAB$dest$TAB$DIST/$src$TAB$(cksum <"$dest")$TAB$id"
    else record "link$TAB$dest$TAB$DIST/$src$TAB$id"
    fi
  done <"$T/act"
  # 3. Marked blocks in config files, written through symlinks.
  while IFS="$TAB" read -r file n st _; do
    prefix=none made=0 sline=''
    if state_get block "$file"; then
      sline=$R
      field 3 "$sline"; prefix=$R
      field 4 "$sline"; made=${R:-0}
    fi
    case $st in
      conflict) continue ;;
      new)
        if [ -e "$file" ]; then
          if [ ! -s "$file" ]; then prefix=new
          elif [ -n "$(tail -c 1 "$file")" ]; then prefix='nl'; printf '\n\n' >>"$file"
          else prefix=blank; printf '\n' >>"$file"
          fi
        else
          mkparents "$file" || { oops "create ${file%/*}"; continue; }
          prefix=new made=1
        fi
        cat "$T/block.$n" >>"$file" || { oops "add to $file"; continue; }
        N_BLOCK=$((N_BLOCK + 1)) ;;
      update)
        edit_block "$file" replace "$T/block.$n" || { oops "update $file"; continue; }
        N_BLOCK=$((N_BLOCK + 1)) ;;
    esac
    record "block$TAB$file$TAB$prefix$TAB$made"
  done <"$T/blocks"
  # 4. Apps with their own installers.
  while IFS="$TAB" read -r k id st what text arg src sum; do
    [ "$k" = X ] || continue
    case $what in
      market)
        if claude plugin marketplace add "$REPO" </dev/null >/dev/null 2>&1; then
          N_RUN=$((N_RUN + 1)); record "plugin${TAB}market"
        else oops "$text"
        fi ;;
      plugin)
        case $st in
          new)
            if claude plugin install "$PLUGIN" </dev/null >/dev/null 2>&1; then
              N_RUN=$((N_RUN + 1)); record "plugin${TAB}install"
            else oops "$text"
            fi ;;
          same)
            record "plugin${TAB}install"
            if state_get plugin market; then record "$R"; fi ;;
        esac ;;
      ext)
        pre=0
        if state_get ext "$arg"; then field 4 "$R"; pre=$R
        elif "$arg" --list-extensions </dev/null 2>/dev/null | grep -q -i -x -F "$EXT_ID"; then pre=1
        fi
        if [ "$st" != same ]; then
          "$arg" --install-extension "$DIST/$src" --force </dev/null >/dev/null 2>&1 || { oops "$text"; continue; }
          N_RUN=$((N_RUN + 1))
        fi
        record "ext$TAB$arg$TAB$sum$TAB$pre" ;;
    esac
  done <"$T/act"
  if [ "$BAT_CHANGED" = 1 ] && has bat; then
    bat cache --build </dev/null >/dev/null 2>&1 || oops "bat cache --build"
  fi
  # 5. Directories we made that are empty again.
  { [ -f "$STATE" ] && grep "^dir$TAB" "$STATE" | cut -f2-; printf '%s' "$MADE_DIRS"; } | sort -r -u >"$T/dirs"
  MADE_DIRS=''
  while IFS= read -r d; do
    [ -n "$d" ] || continue
    [ "$REMOVED" = 1 ] && rmdir "$d" 2>/dev/null
    if [ -d "$d" ]; then record "dir$TAB$d"; fi
  done <"$T/dirs"
  if [ "$REMOVED" = 1 ]; then
    rmdir "$HOME/.local/share/nvim/site/pack/subway-seat/start" "$HOME/.local/share/nvim/site/pack/subway-seat" 2>/dev/null
  fi
  return 0
}

# save_state APPS: write the record and the settings.
save_state() {
  mkparents "$STATE" || fail "Couldn't create $STATE_DIR."
  mkparents "$CONF" || fail "Couldn't create $CONF_DIR."
  printf '%s' "$MADE_DIRS" | while IFS= read -r d; do [ -n "$d" ] && printf 'dir\t%s\n' "$d"; done >>"$T/state"
  MADE_DIRS=''
  {
    printf '# What install.sh placed, so switch and uninstall are exact. Written by install.sh.\n'
    printf 'root\t%s\nflavor\t%s\nmode\t%s\n' "$ROOT" "$FLAVOR" "$([ "$COPY" = 1 ] && echo copy || echo link)"
    for a in $1; do printf 'app\t%s\n' "$a"; done
    sort -u "$T/state"
  } >"$STATE"
  printf '# Subway Seat installer settings, read on every run.\nflavor=%s\nonly=%s\nskip=%s\n' \
    "$FLAVOR" "$ONLY" "$SKIP" >"$CONF"
}

# ── Choosing the apps ───────────────────────────────────────────────────────
check_ids() {
  for id in $(printf '%s' "$1" | tr ',' ' '); do
    grep -q -x -F -e "$id" "$T/ids" || die "there's no port called '$id' (see: $SELF list)"
  done
}

choose() {
  awk -F'\t' '$1 == "port" { print $2 }' "$TSV" >"$T/ids"
  check_ids "$ONLY"
  check_ids "$SKIP"
  if [ -n "$ONLY" ]; then CAND=$(printf '%s' "$ONLY" | tr ',' ' ')
  elif [ "$ALL" = 1 ]; then CAND=$(plan "$FLAVOR" '*' | awk -F'\t' '$1 == "link" || $1 == "run" { print $2 } $1 == "part" { print $3 }' | sort -u)
  else detect_all; CAND=$DETECTED
  fi
  TARGETS=' '
  for id in $CAND $S_APPS; do
    case ",$SKIP," in *",$id,"*) continue ;; esac
    case $TARGETS in *" $id "*) continue ;; esac
    grep -q -x -F -e "$id" "$T/ids" || continue
    TARGETS="$TARGETS$id "
  done
}

ask() {  # ask QUESTION: read one answer from the terminal, even under curl | sh (sets R)
  if ! { : </dev/tty; } 2>/dev/null; then
    printf '\nThere is no terminal to ask. Run again with --yes to go ahead.\n' >&2
    return 1
  fi
  printf '\n%s ' "$1" >/dev/tty
  read -r R </dev/tty || R=n
}

# ── Commands ────────────────────────────────────────────────────────────────
cmd_install() {
  need_tsv
  choose
  flavor_name "$FLAVOR"
  if [ "$DRY" = 1 ]; then header "· $R · dry run, nothing will change"; else header "· $R · now boarding"; fi
  tilde "$ROOT"
  printf '%s%s from %s%s\n' "$D" "$([ "$COPY" = 1 ] && echo Copying || echo Linking)" "$R" "$O"
  if [ -z "$ONLY" ] && [ "$ALL" = 0 ]; then
    total=$(grep -c -x -v '' "$T/ids")
    found=0
    for id in $DETECTED; do found=$((found + 1)); done
    printf '%sFound %s of the %s apps Subway Seat covers.%s\n' "$D" "$found" "$total" "$O"
  fi
  plan "$FLAVOR" "$TARGETS" >"$T/plan"
  classify
  legacy
  if ! grep -q "^[ATR]$TAB" "$T/act"; then
    printf '\nNone of the apps Subway Seat knows are here. %s list shows them all;\n--only picks some anyway.\n' "$SELF"
    return 0
  fi
  show plan
  nl=$(grep -c -E "^L${TAB}[^$TAB]*$TAB(new|update)$TAB" "$T/act")
  nb=$(grep -c -E "$TAB(new|update)$TAB" "$T/blocks")
  nx=$(grep -c -E "^X${TAB}[^$TAB]*$TAB(new|update)$TAB" "$T/act")
  nr=$(grep -c "^[TR]$TAB" "$T/act")
  nc=$(grep -c -E "^L${TAB}[^$TAB]*${TAB}conflict$TAB" "$T/act")
  if [ $((nl + nb + nx + nr)) -eq 0 ] && { [ "$nc" -eq 0 ] || [ "$YES" = 1 ] || [ "$DRY" = 1 ]; }; then
    printf '\nEverything is in place. Nothing to change.'
    [ "$nc" -gt 0 ] && printf ' (%s file%s marked skip %s yours.)' "$nc" "$(plural "$nc")" "$([ "$nc" -eq 1 ] && echo is || echo are)"
    printf '\n'
    [ "$DRY" = 1 ] || { apply 0; save_state "$TARGETS"; }
    return 0
  fi
  if [ "$DRY" = 1 ]; then
    show steps
    printf '\n%sDry run: nothing was changed.%s\n' "$D" "$O"
    return 0
  fi
  what=''
  [ "$nl" -gt 0 ] && what="$what, $([ "$COPY" = 1 ] && echo copy || echo link) $nl file$(plural "$nl")"
  [ "$nb" -gt 0 ] && what="$what, add to $nb config file$(plural "$nb")"
  [ "$nx" -gt 0 ] && what="$what, run $nx command$(plural "$nx")"
  [ "$nr" -gt 0 ] && what="$what, remove $nr old thing$(plural "$nr")"
  what=${what#, }
  what="$(printf '%s' "$what" | cut -c1 | tr '[:lower:]' '[:upper:]')${what#?}"
  backup=0
  if [ "$YES" != 1 ]; then
    if [ -z "$what" ]; then ask "Back up the $nc file$(plural "$nc") marked skip to *.subway-seat.bak and put ours in? [y/N]" || return 1
      case $R in [Yy]*) R=b ;; *) printf 'Nothing changed.\n'; return 1 ;; esac
    elif [ "$nc" -gt 0 ]; then ask "$what? [Y/n, or b to also back up and replace the $nc marked skip]" || return 1
    else ask "$what? [Y/n]" || return 1
    fi
    case $R in
      '' | [Yy]*) ;;
      [Bb]*) [ "$nc" -gt 0 ] && backup=1 ;;
      *) printf 'Nothing changed.\n'; return 1 ;;
    esac
  fi
  apply "$backup"
  save_state "$TARGETS"
  printf '\n%sDone.%s' "$B" "$O"
  [ "$N_LINK" -gt 0 ] && printf ' %s file%s %s.' "$N_LINK" "$(plural "$N_LINK")" "$([ "$COPY" = 1 ] && echo copied || echo linked)"
  [ "$N_BLOCK" -gt 0 ] && printf ' %s config file%s updated.' "$N_BLOCK" "$(plural "$N_BLOCK")"
  [ "$N_RUN" -gt 0 ] && printf ' %s command%s run.' "$N_RUN" "$(plural "$N_RUN")"
  [ "$FAILED" -gt 0 ] && printf ' %s%s step%s failed (above).%s' "$RED" "$FAILED" "$(plural "$FAILED")" "$O"
  printf '\n'
  show steps
  printf '\n%sChange flavor: %s switch enamel · undo: %s uninstall%s\n' "$D" "$SELF" "$SELF" "$O"
  [ "$FAILED" -eq 0 ]
}

cmd_switch() {
  need_tsv
  [ -f "$STATE" ] || fail "Nothing is installed yet. To install: $SELF --flavor $FLAVOR"
  TARGETS=$S_APPS
  plan "$FLAVOR" "$TARGETS" >"$T/plan"
  classify
  if [ "$DRY" = 1 ]; then show plan; printf '\n%sDry run: nothing was changed.%s\n' "$D" "$O"; return 0; fi
  apply 0
  save_state "$TARGETS"
  flavor_name "$FLAVOR"; fname=$R
  moved=$(awk -F'\t' '($1 == "L" || $1 == "B") && ($3 == "new" || $3 == "update") { print $2 }' "$T/act" | sort -u | wc -l | tr -d ' ')
  # The steps by hand that read differently for the new flavor.
  plan "$S_FLAVOR" "$TARGETS" >"$T/oldplan"
  hand=$(awk -F'\t' 'FNR == NR { if ($1 == "step") old[$0] = 1; next }
    $1 == "app" { name[$2] = $3 }
    $1 == "step" && !($0 in old) && !seen[$2]++ { printf "%s%s", sep, name[$2]; sep = ", " }' "$T/oldplan" "$T/plan")
  skipped=$(grep -c -E "^[LB]${TAB}[^$TAB]*${TAB}conflict$TAB" "$T/act")
  if [ "$moved" -eq 0 ] && [ "$FLAVOR" = "$S_FLAVOR" ]; then printf 'Already riding %s%s%s.' "$GOLD" "$fname" "$O"
  elif [ "$moved" -eq 0 ]; then printf 'Now riding %s%s%s.' "$GOLD" "$fname" "$O"
  else printf 'Now riding %s%s%s: %s app%s switched.' "$GOLD" "$fname" "$O" "$moved" "$(plural "$moved")"
  fi
  [ -n "$hand" ] && printf ' By hand: %s (%s status shows how).' "$hand" "$SELF"
  [ "$skipped" -gt 0 ] && printf ' %s file%s left alone.' "$skipped" "$(plural "$skipped")"
  [ "$FAILED" -gt 0 ] && printf ' %s%s step%s failed.%s' "$RED" "$FAILED" "$(plural "$FAILED")" "$O"
  printf '\n'
  [ "$FAILED" -eq 0 ]
}

cmd_status() {
  if [ ! -f "$STATE" ]; then
    printf 'Nothing is installed by install.sh here. To install: %s\n' "$SELF"
    return 1
  fi
  need_tsv
  flavor_name "$S_FLAVOR"
  header "· riding $R"
  tilde "${S_ROOT:-$ROOT}"
  printf '%s%s from %s%s\n' "$D" "$([ "$S_MODE" = copy ] && echo Copied || echo Linked)" "$R" "$O"
  plan "$S_FLAVOR" "$S_APPS" >"$T/plan"
  classify
  drift=0
  last=''
  awk -F'\t' '$1 == "A" { print $2 "\t" $3 "\t" $4 }' "$T/act" >"$T/apps"
  while IFS="$TAB" read -r id name cat; do
    [ "$cat" = "$last" ] || { printf '\n%s%s%s\n' "$B" "$cat" "$O"; last=$cat; }
    issues=$(awk -F'\t' -v id="$id" -v home="$HOME" '
      function t(p) { return index(p, home "/") == 1 ? "~" substr(p, length(home) + 1) : p }
      FNR == NR { if ($1 == "link" || $1 == "copy") ours[$2] = 1; next }
      $2 != id { next }
      $1 == "L" && $3 == "new" { print (ours[$4] ? "missing " : "not placed yet: ") t($4) }
      $1 == "L" && $3 == "update" { print "out of date: " t($4) }
      $1 == "L" && $3 == "conflict" && ours[$4] { print "changed or replaced: " t($4) }
      $1 == "B" && $3 != "same" && !seen[$4]++ { print ($3 == "new" ? "block missing from " : $3 == "update" ? "block edited or out of date: " : "left alone: ") t($4) }
      $1 == "X" && ($3 == "new" || $3 == "update") { print "not done yet: " $5 }
    ' "$STATE" "$T/act")
    if [ -n "$issues" ]; then
      drift=1
      printf '%s\n' "$issues" | awk -v n="$name" -v c="$ORANGE" -v o="$O" '{ printf "  %-15s%s%s%s\n", (NR == 1 ? n : ""), c, $0, o }'
    elif grep -q "^S$TAB$id$TAB" "$T/act"; then printf '  %-15s%sok, and a step by hand%s\n' "$name" "$D" "$O"
    else printf '  %-15s%sok%s\n' "$name" "$GREEN" "$O"
    fi
  done <"$T/apps"
  show steps
  if [ "$drift" = 1 ]; then
    printf '\n%sSomething drifted. Put it back with: %s%s\n' "$D" "$SELF" "$O"
    return 1
  fi
}

cmd_uninstall() {
  if [ ! -f "$STATE" ] && { [ -z "$TSV" ] || [ ! -f "$TSV" ]; }; then
    printf 'Nothing to uninstall: install.sh has no record here.\n'
    return 0
  fi
  header "· last stop"
  : >"$T/plan"
  classify
  legacy
  if grep -q "^[TR]$TAB" "$T/act"; then
    show plan
    if [ "$DRY" = 1 ]; then printf '\n%sDry run: nothing was changed.%s\n' "$D" "$O"; return 0; fi
    if [ "$YES" != 1 ]; then
      ask "Remove all of that? [Y/n]" || return 1
      case $R in '' | [Yy]*) ;; *) printf 'Nothing changed.\n'; return 1 ;; esac
    fi
    apply 0
    msg="All out. Everything the installer placed is gone"
  else
    [ "$DRY" = 1 ] && { printf '\nNothing of ours is left on this machine.\n'; return 0; }
    msg="Nothing of ours was left on this machine"
  fi
  # The record, the settings, the download, and the directories they sat in.
  dirs=$([ -f "$STATE" ] && grep "^dir$TAB" "$STATE" | cut -f2-)
  rm -f "$STATE" "$CONF"
  rmdir "$STATE_DIR" "$CONF_DIR" 2>/dev/null
  [ -f "$DATA_DIR/.downloaded-by-install.sh" ] && rm -rf "$DATA_DIR"
  printf '%s\n' "$dirs" | sort -r -u | while IFS= read -r d; do [ -n "$d" ] && rmdir "$d" 2>/dev/null; done
  printf '\n%s%s%s' "$B" "$msg" "$O"
  if [ -n "$ROOT" ] && [ -e "$ROOT/.git" ]; then tilde "$ROOT"; printf '; the checkout at %s stays' "$R"; fi
  printf '.\n'
  [ "$FAILED" -eq 0 ]
}

cmd_list() {
  need_tsv
  detect_all
  plan "$FLAVOR" '*' >"$T/plan"
  DET=$DETECTED INST=$S_APPS B=$B D=$D O=$O GREEN=$GREEN GOLD=$GOLD awk -F'\t' '
    BEGIN { det = ENVIRON["DET"]; inst = ENVIRON["INST"]; B = ENVIRON["B"]; D = ENVIRON["D"]; O = ENVIRON["O"] }
    FNR == NR { if ($1 == "detect") probe[$2] = 1; next }
    $1 == "app" { order[++n] = $2; name[$2] = $3; cat[$2] = $4; next }
    $1 == "link" || $1 == "run" { files[$2] = 1; next }
    $1 == "part" { files[$3] = 1; next }
    END {
      for (i = 1; i <= n; i++) {
        id = order[i]
        if (cat[id] != last) { printf "%s%s%s%s\n", (i > 1 ? "\n" : ""), B, cat[id], O; last = cat[id] }
        found = index(det, " " id " ") > 0
        here = found ? ENVIRON["GREEN"] "found    " O : D (probe[id] ? "not found" : "no probe ") O
        how = files[id] ? "files  " : D "by hand" O
        mark = index(inst, " " id " ") ? "  " ENVIRON["GOLD"] "installed" O : ""
        printf "  %-24s %-24s %s  %s%s\n", name[id], id, here, how, mark
        total += found
      }
      printf "\n%d ports, %d found here. Install some that aren'"'"'t found with --only.\n", n, total
    }' "$TSV" "$T/plan"
}

main() {
  parse_args "$@"
  [ -n "${HOME:-}" ] || fail "HOME isn't set."
  CONF_DIR=${XDG_CONFIG_HOME:-$HOME/.config}/subway-seat
  STATE_DIR=${XDG_STATE_HOME:-$HOME/.local/state}/subway-seat
  DATA_DIR=${XDG_DATA_HOME:-$HOME/.local/share}/subway-seat
  CONF=$CONF_DIR/config
  STATE=$STATE_DIR/installed
  MADE_DIRS='' FAILED=0
  T=$(mktemp -d "${TMPDIR:-/tmp}/subway-seat.XXXXXX") || fail "Couldn't make a temporary directory."
  trap 'rm -rf "$T"' EXIT
  trap 'exit 130' INT TERM HUP
  locate
  load_settings
  colors
  "cmd_$CMD"
}

main "$@"
