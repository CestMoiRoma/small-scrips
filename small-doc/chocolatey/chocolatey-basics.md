# Chocolatey Basics

---

## Core concepts

| Concept | What it is |
|---------|------------|
| **Package** | A `.nupkg` file (NuGet format) containing install scripts and metadata. |
| **Source** | A feed of packages. Default is the Chocolatey Community Repository (`chocolatey.org`). |
| **nupkg** | The package archive — a zip with a `.nuspec` manifest + PowerShell install scripts. |
| **nuspec** | XML metadata file describing the package (name, version, deps, scripts). |
| **shimgen** | Chocolatey's tool that creates shims so CLI tools are available on `PATH`. |
| **Shim** | A lightweight proxy executable placed in `%ChocolateyInstall%\bin` so tools work everywhere. |
| **packages.config** | An XML file listing packages to install in bulk — Chocolatey's equivalent of a Brewfile. |

> **Always run PowerShell as Administrator.** Chocolatey installs system-wide by default.

---

## Installation

Open PowerShell **as Administrator**:

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

Verify:
```powershell
choco --version
```

---

## Install & uninstall

```powershell
choco install <pkg>             # install a package
choco install <pkg> -y          # install without confirmation prompts
choco install <pkg> --version 1.2.3  # specific version
choco install <pkg1> <pkg2>     # multiple packages at once
choco install packages.config   # install from a config file

choco uninstall <pkg>           # uninstall
choco uninstall <pkg> -y        # no confirmation
choco uninstall <pkg> --all-versions   # remove all installed versions

choco reinstall <pkg>           # uninstall and reinstall
```

---

## Update & upgrade

```powershell
choco upgrade <pkg>             # upgrade a package
choco upgrade <pkg> -y          # no confirmation
choco upgrade all               # upgrade everything
choco upgrade all -y            # upgrade everything, no prompts
choco upgrade all --except="pkg1,pkg2"  # upgrade all except listed
```

---

## Search & info

```powershell
choco search <term>             # search the community repo
choco search <term> --local-only  # search installed packages
choco info <pkg>                # details, version history, description
choco list                      # all installed packages
choco list --local-only         # same (explicit)
choco list --include-programs   # also show Programs & Features entries
choco outdated                  # packages with newer versions available
```

---

## Sources

```powershell
choco source list               # list configured package sources
choco source add --name="local" --source="C:\packages"   # add local folder
choco source add --name="myrepo" --source="https://..." --user="u" --password="p"
choco source remove --name="local"
choco source disable --name="chocolatey"   # temporarily disable a source
choco source enable  --name="chocolatey"
```

---

## Pinning

Prevent a package from being upgraded.

```powershell
choco pin add --name="<pkg>"                 # pin current version
choco pin add --name="<pkg>" --version 1.2  # pin a specific version
choco pin remove --name="<pkg>"             # unpin
choco pin list                              # show pinned packages
```

---

## Features & config

```powershell
choco feature list                          # all features and their state
choco feature enable  --name="<feature>"
choco feature disable --name="<feature>"

choco config list                           # all config values
choco config get <setting>
choco config set --name="<setting>" --value="<value>"
choco config unset --name="<setting>"
```

Useful features:

| Feature | Description |
|---------|-------------|
| `allowGlobalConfirmation` | Auto-confirm all prompts (like `-y` globally) |
| `useRememberedArgumentsForUpgrades` | Reuse install flags on upgrade |
| `showDownloadProgress` | Show download progress bar |
| `exitOnRebootDetected` | Stop if a reboot is needed |

---

## Diagnostics

```powershell
choco --version                 # Chocolatey version
choco --help                    # general help
choco <command> --help          # help for a specific command
choco outdated                  # what can be upgraded
```
