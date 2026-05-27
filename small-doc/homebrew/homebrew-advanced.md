# Homebrew Advanced

---

## Taps

A tap is a git repository of additional formulae or casks outside the core Homebrew repos.

```bash
brew tap                            # list tapped repos
brew tap <user>/<repo>              # add a tap
brew tap <user>/<repo> <url>        # add from a custom git URL
brew untap <user>/<repo>            # remove a tap
brew tap-info <user>/<repo>         # details about a tap

# Install directly from a tap without adding it permanently
brew install <user>/<repo>/<formula>
```

Common taps:
```bash
brew tap homebrew/cask-fonts        # fonts (font-*)
brew tap homebrew/cask-versions     # older/beta versions of casks
brew tap homebrew/command-not-found # suggest brew install when cmd not found
```

---

## Brewfile — reproducible setups

A `Brewfile` declares all your packages, casks and taps. Commit it to source control.

```ruby
# Brewfile
tap "homebrew/cask-fonts"

brew "git"
brew "node"
brew "python@3.12"
brew "wget"

cask "visual-studio-code"
cask "docker"
cask "font-jetbrains-mono"

# Mac App Store apps (requires `mas` formula)
mas "Xcode", id: 497799835
```

```bash
brew bundle                         # install everything in ./Brewfile
brew bundle --file ~/Brewfile       # use a specific Brewfile
brew bundle dump                    # generate Brewfile from what's installed
brew bundle dump --force            # overwrite existing Brewfile
brew bundle check                   # check if all deps are satisfied
brew bundle cleanup                 # list (or remove) packages not in Brewfile
brew bundle cleanup --force         # actually remove them
```

---

## Pinning versions

Prevent a formula from being upgraded.

```bash
brew pin <formula>             # pin — won't be upgraded by `brew upgrade`
brew unpin <formula>           # unpin
brew list --pinned             # show pinned packages
```

---

## Multiple versions

Many formulae offer versioned variants (e.g. `python@3.11`, `node@18`).

```bash
brew install node@18           # install a specific version
brew install node@20

# Switch the active version by linking/unlinking
brew unlink node@20
brew link node@18 --force      # --force needed if another version is linked

# Check what's linked
brew list --versions node
ls $(brew --prefix)/bin/node -la
```

> For Python, consider `pyenv`. For Node, consider `nvm` or `fnm`.

---

## Link & unlink

```bash
brew link <formula>            # create symlinks in the prefix (make it available)
brew unlink <formula>          # remove symlinks (keep installed, just off PATH)
brew link --force <formula>    # force link even if another version is linked
brew link --overwrite <formula> # overwrite conflicting files
```

---

## Building from source

```bash
brew install --build-from-source <formula>   # compile instead of using a bottle
brew install --HEAD <formula>                # build from the latest git commit
```

---

## Caveats & post-install steps

After installing some formulae, Homebrew prints a **Caveats** section with manual steps (e.g. adding to `$PATH`, running `echo "..." >> ~/.zshrc`). Re-read them anytime:

```bash
brew info <formula>            # caveats are at the bottom
```

---

## Auditing & editing formulae

```bash
brew edit <formula>            # open formula in $EDITOR
brew audit <formula>           # run style and correctness checks
brew cat <formula>             # print formula source
brew create <url>              # scaffold a new formula from a source URL
brew style <formula>           # check code style (uses RuboCop)
```

---

## Environment variables

| Variable | Effect |
|----------|--------|
| `HOMEBREW_NO_AUTO_UPDATE=1` | Skip auto-update before install |
| `HOMEBREW_NO_ANALYTICS=1` | Disable telemetry |
| `HOMEBREW_NO_INSECURE_REDIRECT=1` | Fail on HTTP redirects |
| `HOMEBREW_CASK_OPTS="--appdir=~/Apps"` | Default cask install location |
| `HOMEBREW_EDITOR` | Editor used by `brew edit` |
| `HOMEBREW_GITHUB_API_TOKEN` | GitHub token — raises API rate limit |
| `HOMEBREW_NO_ENV_HINTS=1` | Suppress "export …" hints |
| `HOMEBREW_BUNDLE_FILE` | Default Brewfile path for `brew bundle` |

Add persistent ones to `~/.zshrc` or `~/.bash_profile`:
```bash
export HOMEBREW_NO_AUTO_UPDATE=1
export HOMEBREW_NO_ANALYTICS=1
```

---

## Useful patterns

```bash
# See everything installed explicitly (not just as a dependency)
brew leaves

# See the full dependency graph of everything installed
brew deps --installed --tree

# Find which formula provides a file
brew which-formula <file>

# Check what would be removed by autoremove
brew autoremove -n

# Fully reset a broken install
brew uninstall --force <formula>
brew cleanup
brew install <formula>

# Upgrade everything in one shot
brew update && brew upgrade && brew upgrade --cask && brew cleanup
```
