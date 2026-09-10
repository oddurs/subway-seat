# Installing Subway Seat

`install.sh` puts Subway Seat into the apps on your machine and keeps a record of what it did, so it can switch flavors or take everything out again exactly. It runs on macOS and Linux with nothing but `sh`, `awk`, `sed`, `grep` and `curl` (or `wget`).

```sh
curl -fsSL https://oddurs.github.io/subway-seat/install.sh | sh
```

From a clone, `./install.sh` does the same with the checkout's files. `./install.fish` is the same installer for fish users: it prints steps in fish syntax and still takes the old `./install.fish tunnel` form.

## Commands

| Command | What it does |
|---|---|
| `install` (the default) | Finds your apps, shows the plan, asks once, then does it. |
| `switch <flavor>` | Re-points every installed app at `walnut`, `tunnel`, `enamel` or `auto`. It doesn't ask, and prints one line. |
| `status` | Shows the flavor, each installed app, anything that drifted (a missing link, an edited block) and the steps left by hand. |
| `uninstall` | Removes every link, copy and block it placed, puts back anything it moved aside, and deletes its record and settings. |
| `list` | Shows every port, whether it was found here, and whether it has files to place or only steps by hand. |

## Options

| Option | |
|---|---|
| `--flavor walnut\|tunnel\|enamel\|auto` | `auto` follows the system's light or dark setting in the apps that can, and uses Walnut elsewhere. The default is your saved flavor, else Walnut. |
| `--only ghostty,vim` | Only these ports, found or not; apps installed earlier stay. The ids come from `list`. The list is saved, and `--only ''` clears it. |
| `--skip kitty` | Never these ports. A skipped port that's already installed is taken out. |
| `--all` | Every port with a file to place, even if the app wasn't found. |
| `--yes` | Don't ask. Files that aren't ours are still left alone. |
| `--dry-run` | Print the plan and change nothing. |
| `--copy` | Copy files instead of linking them. This is the default when the files don't come from a git checkout (the curl install). |
| `--no-enable` | Place theme files but leave app configs alone. The lines to add are listed as steps. |
| `--ref v0.4.0` | With curl, install this tag or branch instead of `main`. |

Exit codes: `0` done (or nothing to do), `1` something failed, you answered no, or `status` found drift, `2` a usage error.

## What it touches

- **Theme files** go where each app looks for them (`~/.config/ghostty/themes/`, `~/.vim/colors/` and so on). All three flavors are placed, so each app's own theme picker lists them. Where the flavors share one path, only the chosen one is placed, and `switch` re-points it.
- **Config lines** that turn an app on are added to its config file inside one marked block. The markers use the file's own comment syntax:

  ```
  # >>> subway-seat >>>
  theme = Subway Seat
  # <<< subway-seat <<<
  ```

  Running it again replaces the block in place rather than adding a second one. A config file that is a symlink (into a dotfiles repo, say) is written through, so the link stays a link. A port only has a block when appending is a correct and complete way to turn it on; otherwise you get a step to do by hand.
- **Files it didn't place** are never replaced. The plan marks them `skip`, and the prompt offers `b` to move them aside to `<name>.subway-seat.bak` first. `uninstall` puts them back.
- **Claude Code** gets the plugin (`claude plugin marketplace add oddurs/subway-seat`, then `claude plugin install subway-seat@subway-seat`). After that, `/subway-seat:setup` in Claude Code picks the flavor, status line and verbs. It never links into `~/.claude/themes`. If the plugin was already there, it's left alone, and `uninstall` doesn't remove it.
- **VS Code, Cursor, VSCodium and Windsurf** get the `.vsix` through `<cli> --install-extension`. Choosing the theme in settings is a step by hand.
- **bat**: its cache is rebuilt after its themes change.

## Settings and the record

- `${XDG_CONFIG_HOME:-~/.config}/subway-seat/config` holds `flavor=`, `only=` and `skip=`. It's written after each install and read on every run, and you can edit it.
- `${XDG_STATE_HOME:-~/.local/state}/subway-seat/installed` lists every link, copy, block, directory and command the installer made. `switch` and `uninstall` work from it. Don't edit it.
- `${XDG_DATA_HOME:-~/.local/share}/subway-seat` is where the curl install keeps its copy of the repo. Running the curl command again updates it, and `uninstall` deletes it.

## Coming from the old install.fish

The first run finds what the old `install.fish` left:

- Links it made into a Subway Seat `dist/` are adopted when they're still wanted and removed when they aren't. That includes `~/.claude/themes/subway-seat*.json`, since the plugin carries those themes.
- Its `~/.config/fish/conf.d/subway-seat.fish` stays until a marked fish block takes over that job.

## Uninstalling by hand

Each port's `dist/<id>/README.md` lists its files and where they go. Delete those files, then delete the lines between `>>> subway-seat >>>` and `<<< subway-seat <<<` in any config file that has them.

## For port authors

The installer reads `dist/install.tsv`, which `build.py` writes from each port's META (see `install_table()` in `build.py` for the records):

- `detect`: commands or paths that show the app is installed.
- `dest` on each file: where it goes.
- `enable["file"]`: the config file the enable line may be appended to.
- `auto`: how to follow light and dark.

Everything else in the port turns into a step by hand.
