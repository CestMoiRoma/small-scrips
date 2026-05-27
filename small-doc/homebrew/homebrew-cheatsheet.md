# Homebrew — Quick Cheat Sheet

---

## Install & uninstall

| Command | Description |
|---------|-------------|
| `brew install <formula>` | Install a CLI tool or library |
| `brew install --cask <cask>` | Install a GUI app |
| `brew uninstall <formula>` | Uninstall |
| `brew uninstall --cask <cask>` | Uninstall a GUI app |
| `brew uninstall --force <formula>` | Remove all versions |
| `brew uninstall --zap --cask <cask>` | Remove app + all associated files |
| `brew reinstall <formula>` | Uninstall and reinstall |
| `brew install --build-from-source <formula>` | Compile from source |
| `brew install --HEAD <formula>` | Install latest git commit |
| `brew install -n <formula>` | Dry run — show what would be installed |

---

## Update & upgrade

| Command | Description |
|---------|-------------|
| `brew update` | Fetch latest formula/cask definitions |
| `brew upgrade` | Upgrade all outdated formulae |
| `brew upgrade <formula>` | Upgrade one formula |
| `brew upgrade --cask` | Upgrade all outdated casks |
| `brew upgrade --cask <cask>` | Upgrade one cask |
| `brew upgrade --greedy --cask` | Include self-updating casks |
| `brew upgrade -n` | Dry run |
| `brew outdated` | Show outdated formulae |
| `brew outdated --cask` | Show outdated casks |
| `brew outdated --verbose` | Show current vs latest versions |

---

## Search & info

| Command | Description |
|---------|-------------|
| `brew search <text>` | Search formulae and casks by name |
| `brew search --desc <text>` | Search in descriptions too |
| `brew search /regex/` | Regex search |
| `brew info <formula>` | Version, deps, caveats |
| `brew info --cask <cask>` | Cask details |
| `brew home <formula>` | Open homepage |
| `brew cat <formula>` | Print formula source |
| `brew deps <formula>` | Direct dependencies |
| `brew deps --tree <formula>` | Dependency tree |
| `brew uses <formula>` | What depends on this |
| `brew uses --installed <formula>` | Installed packages that depend on this |
| `brew leaves` | Installed formulae not required by others |

---

## List & status

| Command | Description |
|---------|-------------|
| `brew list` | All installed formulae |
| `brew list --cask` | All installed casks |
| `brew list --versions` | With version numbers |
| `brew list --pinned` | Pinned formulae |
| `brew list <formula>` | Files installed by a formula |

---

## Taps

| Command | Description |
|---------|-------------|
| `brew tap` | List tapped repos |
| `brew tap <user>/<repo>` | Add a tap |
| `brew untap <user>/<repo>` | Remove a tap |
| `brew tap-info <user>/<repo>` | Tap details |

---

## Pinning

| Command | Description |
|---------|-------------|
| `brew pin <formula>` | Prevent upgrades |
| `brew unpin <formula>` | Allow upgrades again |
| `brew list --pinned` | Show pinned packages |

---

## Link & unlink

| Command | Description |
|---------|-------------|
| `brew link <formula>` | Symlink into prefix (put on PATH) |
| `brew unlink <formula>` | Remove symlinks (keep installed) |
| `brew link --force <formula>` | Force link (overrides another version) |
| `brew link --overwrite <formula>` | Overwrite conflicting files |

---

## Services

| Command | Description |
|---------|-------------|
| `brew services list` | All managed services and status |
| `brew services start <formula>` | Start and enable at login |
| `brew services stop <formula>` | Stop and disable |
| `brew services restart <formula>` | Restart |
| `brew services run <formula>` | Start once, don't enable at login |
| `brew services info <formula>` | Service status details |

---

## Cleanup

| Command | Description |
|---------|-------------|
| `brew cleanup` | Remove old versions and stale cache |
| `brew cleanup -n` | Dry run |
| `brew cleanup --prune=all` | Also clear all cached downloads |
| `brew autoremove` | Remove unused dependencies |
| `brew autoremove -n` | Dry run |

---

## Brewfile

| Command | Description |
|---------|-------------|
| `brew bundle` | Install everything in `./Brewfile` |
| `brew bundle --file <path>` | Use a specific Brewfile |
| `brew bundle dump` | Generate Brewfile from installed packages |
| `brew bundle dump --force` | Overwrite existing Brewfile |
| `brew bundle check` | Check if all deps are satisfied |
| `brew bundle cleanup` | List packages not in Brewfile |
| `brew bundle cleanup --force` | Remove packages not in Brewfile |

---

## Diagnostics

| Command | Description |
|---------|-------------|
| `brew doctor` | Check for common issues |
| `brew missing` | Check for missing dependencies |
| `brew config` | Homebrew config and environment |
| `brew --version` | Homebrew version |
| `brew --prefix` | Installation root |
| `brew --prefix <formula>` | Prefix for a specific formula |
| `brew --cellar <formula>` | Cellar path for a formula |

---

## Useful one-liners

| Command | Description |
|---------|-------------|
| `brew update && brew upgrade && brew upgrade --cask && brew cleanup` | Full update |
| `brew leaves` | Packages installed explicitly (not as deps) |
| `brew deps --installed --tree` | Full dependency tree of everything installed |
| `brew list --versions` | All installed packages with versions |
| `brew outdated --verbose` | What can be upgraded (with version numbers) |
