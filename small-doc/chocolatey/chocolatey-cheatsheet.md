# Chocolatey — Quick Cheat Sheet

> Run PowerShell **as Administrator** for all commands.

---

## Install & uninstall

| Command | Description |
|---------|-------------|
| `choco install <pkg>` | Install a package |
| `choco install <pkg> -y` | Install without prompts |
| `choco install <pkg> --version 1.2.3` | Specific version |
| `choco install <pkg1> <pkg2> -y` | Multiple packages at once |
| `choco install packages.config` | Install from a config file |
| `choco install <pkg> --source="."` | Install from current folder |
| `choco install <pkg> --params "/Key:Value"` | With install parameters |
| `choco install <pkg> -n` | Dry run |
| `choco uninstall <pkg>` | Uninstall |
| `choco uninstall <pkg> -y` | No confirmation |
| `choco uninstall <pkg> --all-versions` | Remove all versions |
| `choco reinstall <pkg> -y` | Uninstall and reinstall |

---

## Update & upgrade

| Command | Description |
|---------|-------------|
| `choco upgrade <pkg>` | Upgrade a package |
| `choco upgrade <pkg> -y` | No confirmation |
| `choco upgrade all` | Upgrade everything |
| `choco upgrade all -y` | Upgrade everything, no prompts |
| `choco upgrade all -y --except="pkg1,pkg2"` | Upgrade all except listed |
| `choco upgrade <pkg> --version 2.0.0` | Upgrade to a specific version |
| `choco upgrade all -n` | Dry run |
| `choco outdated` | Show packages with newer versions |

---

## Search & info

| Command | Description |
|---------|-------------|
| `choco search <term>` | Search the community repo |
| `choco search <term> --exact` | Exact name match |
| `choco search <term> --by-id-only` | Search IDs only |
| `choco info <pkg>` | Details, version history, description |
| `choco list` | All installed packages |
| `choco list --include-programs` | Also show Programs & Features entries |
| `choco list --all-versions` | All installed versions |
| `choco list --id-only` | IDs only (good for scripting) |

---

## Pinning

| Command | Description |
|---------|-------------|
| `choco pin add --name="<pkg>"` | Prevent upgrades |
| `choco pin add --name="<pkg>" --version 1.2` | Pin a specific version |
| `choco pin remove --name="<pkg>"` | Allow upgrades again |
| `choco pin list` | Show pinned packages |

---

## Sources

| Command | Description |
|---------|-------------|
| `choco source list` | All configured sources |
| `choco source add --name="x" --source="url"` | Add a source |
| `choco source remove --name="x"` | Remove a source |
| `choco source disable --name="x"` | Temporarily disable |
| `choco source enable --name="x"` | Re-enable |

---

## Features & config

| Command | Description |
|---------|-------------|
| `choco feature list` | All features and status |
| `choco feature enable --name="allowGlobalConfirmation"` | Auto-confirm globally |
| `choco feature disable --name="allowGlobalConfirmation"` | Disable |
| `choco config list` | All config values |
| `choco config get <key>` | One value |
| `choco config set --name="<key>" --value="<val>"` | Set a value |
| `choco config unset --name="<key>"` | Reset to default |

---

## Package creation

| Command | Description |
|---------|-------------|
| `choco new <pkgname>` | Scaffold a new package |
| `choco pack` | Build `.nupkg` from `.nuspec` |
| `choco push <pkg>.nupkg --source="<url>"` | Push to a feed |

---

## Diagnostics

| Command | Description |
|---------|-------------|
| `choco --version` | Chocolatey version |
| `choco outdated` | What can be upgraded |
| `choco list --local-only` | Everything installed via Chocolatey |

---

## packages.config

```xml
<?xml version="1.0" encoding="utf-8"?>
<packages>
  <package id="git"       version="2.44.0" />
  <package id="nodejs"    />
  <package id="vscode"    />
  <package id="7zip"      />
</packages>
```

```powershell
choco install packages.config -y
```

---

## Useful one-liners

| Command | Description |
|---------|-------------|
| `choco upgrade all -y` | Full upgrade, no prompts |
| `choco list --local-only --id-only` | All installed IDs (for scripting) |
| `choco outdated` | What has updates |
| `choco install git vscode 7zip googlechrome -y` | Bulk install |
