# Homebrew Basics

---

## Core concepts

| Concept | What it is |
|---------|------------|
| **Formula** | A Ruby script that defines how to install a CLI tool or library. |
| **Cask** | Like a formula but for macOS GUI apps (`.app` bundles, fonts, drivers). |
| **Tap** | A third-party repository of formulae/casks. Homebrew fetches them via git. |
| **Keg** | The installed files for one version of a package, stored in the Cellar. |
| **Cellar** | The directory where all kegs live: `/opt/homebrew/Cellar` (Apple Silicon) or `/usr/local/Cellar` (Intel). |
| **Bottle** | A pre-built binary package. Installing from a bottle is faster than compiling. |
| **Link** | Symlinks from the Cellar into `/opt/homebrew/bin` etc. so the package is on `$PATH`. |
| **Prefix** | Homebrew's root directory. `$(brew --prefix)`. |

---

## Installation

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

After installing on Apple Silicon, add to your shell profile:
```bash
eval "$(/opt/homebrew/bin/brew shellenv)"
```

---

## Formulae — CLI tools & libraries

```bash
brew install <formula>         # install
brew uninstall <formula>       # uninstall
brew reinstall <formula>       # uninstall and reinstall
brew upgrade <formula>         # upgrade to latest
brew upgrade                   # upgrade all outdated formulae
brew info <formula>            # version, deps, options, caveats
brew home <formula>            # open homepage in browser
brew search <text>             # search formulae and casks
brew search /regex/            # search with a regex
brew list                      # all installed formulae
brew list <formula>            # files installed by a formula
brew outdated                  # formulae with a newer version available
```

---

## Casks — GUI apps & fonts

```bash
brew install --cask <cask>     # install a GUI app
brew uninstall --cask <cask>   # uninstall
brew reinstall --cask <cask>   # reinstall
brew upgrade --cask <cask>     # upgrade one cask
brew upgrade --cask            # upgrade all outdated casks
brew list --cask               # all installed casks
brew info --cask <cask>        # details
brew outdated --cask           # casks with updates available
```

---

## Update & upgrade

```bash
brew update                    # fetch latest formula/cask definitions
brew upgrade                   # upgrade all outdated packages
brew upgrade <formula>         # upgrade one package
brew outdated                  # see what can be upgraded
brew outdated --verbose        # include current and latest versions
```

> Run `brew update` before `brew upgrade` to get the freshest list.

---

## Search & info

```bash
brew search <text>             # search names
brew search /^node/            # regex search
brew info <formula>            # version, source, deps, caveats
brew deps <formula>            # direct dependencies
brew deps --tree <formula>     # dependency tree
brew uses <formula>            # what packages depend on this
brew uses --installed <formula> # only among installed packages
```

---

## Services

Manage background services (daemons) installed via Homebrew.

```bash
brew services list             # all managed services
brew services start <formula>  # start and enable at login
brew services stop <formula>   # stop and disable
brew services restart <formula>
brew services run <formula>    # start once, don't enable at login
brew services info <formula>   # status details
```

---

## Cleanup

```bash
brew cleanup                   # remove old versions and stale cache
brew cleanup <formula>         # clean one package only
brew cleanup -n                # dry run — show what would be removed
brew cleanup --prune=all       # also remove all cached downloads
brew autoremove                # remove unused dependencies
```

---

## Diagnostics

```bash
brew doctor                    # check for common issues
brew missing                   # check for missing dependencies
brew config                    # Homebrew configuration and env info
brew --version                 # Homebrew version
brew --prefix                  # installation root
brew --prefix <formula>        # prefix for a specific formula
brew --cellar <formula>        # cellar path for a formula
```
