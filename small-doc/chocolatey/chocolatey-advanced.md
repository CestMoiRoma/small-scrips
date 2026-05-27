# Chocolatey Advanced

---

## packages.config — reproducible setups

The equivalent of a Brewfile. An XML list of packages to install in one shot.

```xml
<!-- packages.config -->
<?xml version="1.0" encoding="utf-8"?>
<packages>
  <package id="git"             version="2.44.0" />
  <package id="nodejs"          version="20.11.0" />
  <package id="python"          version="3.12.0" />
  <package id="vscode"          />  <!-- latest -->
  <package id="googlechrome"    />
  <package id="7zip"            />
  <package id="vlc"             />
</packages>
```

```powershell
choco install packages.config   # install all listed packages
choco install packages.config -y   # no prompts
```

> There is no built-in `dump` command like Homebrew. To export what's installed:
> ```powershell
> choco list --local-only --id-only | ForEach-Object { "<package id=`"$_`" />" }
> ```

---

## Private & custom sources

```powershell
# Add a NuGet-compatible private feed
choco source add `
  --name="internal" `
  --source="https://nexus.company.com/repository/nuget-hosted/" `
  --user="ci-user" `
  --password="secret" `
  --priority=1         # lower number = higher priority

# Add a local folder as a source
choco source add --name="local-pkgs" --source="C:\chocolatey-packages"

# Push a package to a private source (requires API key)
choco push mypkg.1.0.0.nupkg --source="https://nexus.company.com/..." --api-key="xxx"
```

---

## Creating a package

```powershell
# Scaffold a new package
choco new <pkgname>
```

Generates:
```
<pkgname>/
├── <pkgname>.nuspec          # metadata (name, version, deps, description)
└── tools/
    ├── chocolateyInstall.ps1
    ├── chocolateyUninstall.ps1   # optional
    └── chocolateyBeforeModify.ps1  # optional
```

**Minimal nuspec:**
```xml
<?xml version="1.0"?>
<package>
  <metadata>
    <id>mypkg</id>
    <version>1.0.0</version>
    <authors>You</authors>
    <description>My package.</description>
    <dependencies>
      <dependency id="git" version="2.0.0" />
    </dependencies>
  </metadata>
</package>
```

**Minimal install script (`tools/chocolateyInstall.ps1`):**
```powershell
$ErrorActionPreference = "Stop"

$packageArgs = @{
  packageName   = $env:ChocolateyPackageName
  fileType      = "exe"
  url           = "https://example.com/installer.exe"
  checksum      = "abc123..."
  checksumType  = "sha256"
  silentArgs    = "/S"        # silent install flag for the installer
  validExitCodes = @(0)
}

Install-ChocolateyPackage @packageArgs
```

```powershell
# Build the package
choco pack                        # in the directory with the .nuspec
choco pack mypkg.nuspec           # explicit path

# Test it locally
choco install mypkg --source="."  # install from current folder
```

---

## Useful helper functions (in install scripts)

| Function | Description |
|----------|-------------|
| `Install-ChocolateyPackage` | Download + run an installer |
| `Install-ChocolateyZipPackage` | Download + extract a zip |
| `Get-ChocolateyWebFile` | Download a file |
| `Install-ChocolateyPath` | Add a directory to `PATH` |
| `Install-ChocolateyEnvironmentVariable` | Set an env variable |
| `Get-ToolsLocation` | Return Chocolatey tools directory |
| `Get-PackageParameters` | Parse `--params` from the install command |
| `Uninstall-ChocolateyPackage` | Run an uninstaller |
| `Get-UninstallRegistryKey` | Find the uninstall key in the registry |

---

## Install-time parameters

Packages can accept custom parameters via `--params`:

```powershell
choco install git --params "'/GitAndUnixToolsOnPath /NoShellIntegration'"
choco install nodejs --params "'/version:20'"
```

The install script reads them with:
```powershell
$pp = Get-PackageParameters
if ($pp["NoShellIntegration"]) { ... }
```

---

## Ignoring checksums (use carefully)

```powershell
choco install <pkg> --ignore-checksums
choco install <pkg> --allow-empty-checksums
```

> Only use this for internal/trusted packages. Never for public ones.

---

## Proxy configuration

```powershell
choco config set --name="proxy" --value="http://proxy.company.com:8080"
choco config set --name="proxyUser" --value="domain\user"
choco config set --name="proxyPassword" --value="password"
choco config set --name="proxyBypassList" --value="localhost,*.internal.com"
choco config set --name="proxyBypassOnLocal" --value="true"
```

---

## Environment variables

| Variable | Effect |
|----------|--------|
| `ChocolateyInstall` | Chocolatey root directory (default: `C:\ProgramData\chocolatey`) |
| `ChocolateyToolsLocation` | Where tools are extracted (default: `C:\tools`) |
| `ChocolateyLastPathUpdate` | Timestamp of last PATH update |
| `ChocolateyPackageName` | Set during install — the package being installed |
| `ChocolateyPackageVersion` | Set during install — the version being installed |
| `ChocolateyBinRoot` | Where shims are placed |

---

## Useful patterns

```powershell
# Upgrade everything without any prompts
choco upgrade all -y

# Upgrade everything except a pinned list
choco upgrade all -y --except="nodejs,python"

# Install a list of packages in one line
choco install git vscode 7zip vlc -y

# Export currently installed packages as packages.config
choco list --local-only --id-only | ForEach-Object {
    "<package id=`"$_`" />"
} | Set-Content packages.config

# Check what would be upgraded without doing it
choco outdated

# Completely remove Chocolatey
Remove-Item -Recurse -Force "$env:ChocolateyInstall"
```
