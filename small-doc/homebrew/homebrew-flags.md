# Homebrew Flags Reference

All notable flags, organized by command.

---

## brew install

| Flag | Effect |
|------|--------|
| `--cask` | Install a cask (GUI app) instead of a formula |
| `--formula` | Force treating the argument as a formula |
| `--build-from-source` / `-s` | Compile from source, skip the bottle |
| `--force-bottle` | Install from a bottle even if it would normally build from source |
| `--HEAD` | Install the HEAD (latest git commit) version |
| `--fetch-HEAD` | Fetch HEAD even if already up to date |
| `--ignore-dependencies` | Don't install any missing dependencies |
| `--only-dependencies` | Install dependencies but not the formula itself |
| `--include-test` | Install test dependencies |
| `--keep-tmp` | Keep temp build files (useful for debugging) |
| `--debug` / `-d` | Verbose debug output |
| `--verbose` / `-v` | Print more information |
| `--dry-run` / `-n` | Show what would be installed without installing |
| `--force` / `-f` | Install even if already installed |
| `--overwrite` | Overwrite existing files when linking |
| `--appdir <dir>` | Target directory for casks (default: `/Applications`) |

---

## brew uninstall

| Flag | Effect |
|------|--------|
| `--cask` | Uninstall a cask |
| `--force` / `-f` | Delete all installed versions, ignore errors |
| `--zap` | Remove all files associated with the cask (including preferences) |
| `--ignore-dependencies` | Don't check if other formulae depend on this |

---

## brew upgrade

| Flag | Effect |
|------|--------|
| `--cask` | Upgrade casks only (or a specific cask) |
| `--formula` | Upgrade formulae only |
| `--all` | Include pinned formulae |
| `--dry-run` / `-n` | Show what would be upgraded |
| `--greedy` | Also upgrade casks that auto-update themselves |
| `--greedy-latest` | Upgrade casks whose latest version is "latest" |
| `--build-from-source` / `-s` | Compile instead of using a bottle |
| `--force` | Upgrade even if pinned |
| `--verbose` / `-v` | More output |
| `--debug` / `-d` | Debug output |

---

## brew list

| Flag | Effect |
|------|--------|
| `--cask` | List installed casks |
| `--formula` | List installed formulae |
| `--versions` | Show installed versions |
| `--pinned` | Only show pinned formulae |
| `--full-name` | Include the tap name: `tap/formula` |
| `-1` | One entry per line |
| `-l` | Long format with timestamps |
| `-r` | Sort by most recent installation |
| `-t` | Sort by installation time |

---

## brew outdated

| Flag | Effect |
|------|--------|
| `--cask` | Check casks only |
| `--formula` | Check formulae only |
| `--verbose` / `-v` | Show current and latest version numbers |
| `--greedy` | Include casks that auto-update themselves |
| `--greedy-latest` | Include casks whose version is "latest" |
| `--json` | Output as JSON |

---

## brew search

| Flag | Effect |
|------|--------|
| `--formula` | Search formulae only |
| `--cask` | Search casks only |
| `--desc` | Search in descriptions too |
| `--pull-request` | Search for GitHub pull requests |
| `--open` | Only open pull requests |
| `--closed` | Only closed pull requests |

---

## brew info

| Flag | Effect |
|------|--------|
| `--cask` | Show cask info |
| `--formula` | Show formula info |
| `--json` | Output as JSON (`--json=v2` for extended) |
| `--github` | Open the formula's GitHub page |
| `--analytics` | Show install analytics data |
| `--installed` | Only show installed formulae/casks |

---

## brew cleanup

| Flag | Effect |
|------|--------|
| `--dry-run` / `-n` | Show what would be removed without removing |
| `--prune=<days>` | Remove cache files older than n days |
| `--prune=all` | Remove all cached downloads |
| `-s` | Scrub the cache (remove old versions of downloaded packages) |

---

## brew tap

| Flag | Effect |
|------|--------|
| `--force-auto-update` | Auto-update this tap even if it's not Homebrew-hosted |
| `--custom-remote` | Use a custom remote URL |
| `--repair` | Re-install missing or broken symlinks |
| `--list-pinned` | Show pinned taps |

---

## brew services

| Flag | Effect |
|------|--------|
| `--all` | Apply to all managed services |
| `--user` | Manage services at user level (default) |
| `--system` | Manage services at system level (requires `sudo`) |
| `--file <plist>` | Use a specific plist file |

---

## brew bundle

| Flag | Effect |
|------|--------|
| `--file <path>` | Use a specific Brewfile |
| `--global` | Use `~/.Brewfile` |
| `--force` | Overwrite existing Brewfile (for `dump`) |
| `--no-upgrade` | Don't upgrade already-installed packages |
| `--verbose` / `-v` | Print each package as it's installed |
| `--no-lock` | Don't generate a `Brewfile.lock.json` |
| `--all` | Include all tap, formula and cask entries (for `cleanup`) |
| `--force` | Remove packages not in Brewfile (for `cleanup`) |
| `--describe` | Add a one-line description comment for each package (for `dump`) |

---

## brew deps

| Flag | Effect |
|------|--------|
| `--tree` | Display as a dependency tree |
| `--graph` | Display as a DOT graph |
| `--installed` | Only consider installed formulae |
| `--include-build` | Include build dependencies |
| `--include-optional` | Include optional dependencies |
| `--include-test` | Include test dependencies |
| `--skip-recommended` | Exclude recommended dependencies |
| `--union` | Union of all listed formulae's deps |
| `--full-name` | Use fully-qualified names |

---

## brew link

| Flag | Effect |
|------|--------|
| `--force` / `-f` | Force linking even if another version is linked |
| `--overwrite` | Overwrite existing files |
| `--dry-run` / `-n` | Show what would be linked |
| `--HEAD` | Link the HEAD version |

---

## Global flags (work with most commands)

| Flag | Effect |
|------|--------|
| `--verbose` / `-v` | More output |
| `--debug` / `-d` | Debug output |
| `--quiet` / `-q` | Less output |
| `--help` / `-h` | Show help |
| `--version` | Show Homebrew version |
