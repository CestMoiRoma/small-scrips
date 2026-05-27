# Chocolatey Flags Reference

All notable flags, organized by command.

---

## choco install

| Flag | Effect |
|------|--------|
| `-y` / `--yes` / `--confirm` | Auto-confirm all prompts |
| `--version <ver>` | Install a specific version |
| `--pre` / `--prerelease` | Include pre-release versions |
| `-s` / `--source <src>` | Use a specific source or local folder |
| `--source="."` | Install from current directory |
| `-f` / `--force` | Force install even if already installed |
| `--ignore-checksums` | Skip checksum validation (use with care) |
| `--allow-empty-checksums` | Allow packages with no checksum |
| `--no-progress` | Don't show download progress bar |
| `--params <params>` | Pass parameters to the install script |
| `--install-arguments <args>` | Pass args directly to the underlying installer |
| `--override-arguments` | Replace default installer arguments entirely |
| `--not-silent` | Don't pass silent flags to the installer |
| `--apply-args-to-dependencies` | Also pass install args to dependencies |
| `--ignore-dependencies` / `-i` | Don't install dependencies |
| `--skip-automation-scripts` | Skip `chocolateyInstall.ps1` |
| `--x86` | Force 32-bit installation |
| `--skip-virus-check` | Skip virus scanner (Chocolatey Pro) |
| `--require-checksums` | Fail if no checksum is present |
| `-n` / `--dry-run` / `--whatif` | Simulate without installing |
| `--package-parameters-sensitive <p>` | Like `--params` but hidden from logs |
| `--timeout <secs>` | Download timeout in seconds |
| `--cache-location <dir>` | Custom download cache location |
| `--verbose` / `-v` | More output |
| `--debug` / `-d` | Debug output |

---

## choco uninstall

| Flag | Effect |
|------|--------|
| `-y` / `--yes` | No confirmation |
| `--all-versions` | Remove all installed versions |
| `--skip-automation-scripts` | Skip `chocolateyUninstall.ps1` |
| `--ignore-dependencies` / `-i` | Don't check dependants |
| `--force` / `-f` | Force removal even on errors |
| `-n` / `--whatif` | Dry run |
| `--verbose` / `-v` | More output |

---

## choco upgrade

| Flag | Effect |
|------|--------|
| `all` | Upgrade all installed packages |
| `-y` / `--yes` | No confirmation |
| `--version <ver>` | Upgrade to a specific version |
| `--pre` | Include pre-release versions |
| `--except="<pkg1>,<pkg2>"` | Exclude packages from `upgrade all` |
| `-s` / `--source <src>` | Use a specific source |
| `-f` / `--force` | Upgrade even if already on latest |
| `--ignore-checksums` | Skip checksum validation |
| `--no-progress` | No download progress |
| `--params <params>` | Pass parameters to install script |
| `--install-arguments <args>` | Pass args to underlying installer |
| `--override-arguments` | Replace default installer args |
| `--ignore-pinned` | Upgrade even if package is pinned |
| `--fail-on-unfound` | Exit with error if a package isn't found |
| `--fail-on-not-installed` | Exit with error if a package isn't installed |
| `-n` / `--whatif` | Dry run |
| `--skip-if-not-installed` | Skip packages that aren't installed yet |
| `--timeout <secs>` | Download timeout |
| `--verbose` / `-v` | More output |

---

## choco list

| Flag | Effect |
|------|--------|
| `--local-only` / `-l` | Only show installed packages (default behaviour in recent versions) |
| `--include-programs` | Also show entries from Programs & Features |
| `--id-only` | Only print package IDs, no version |
| `--version-only` | Only print version numbers |
| `--all-versions` | Show all installed versions |
| `--exact` / `-e` | Exact name match only |
| `--by-id-only` | Search only in package IDs |
| `--by-tag-only` | Search only in tags |
| `--id-starts-with` | Match packages whose ID starts with the query |
| `--approved-only` | Only show community-approved packages |
| `--not-broken` | Exclude packages with failing tests |
| `-s` / `--source <src>` | Search a specific source |
| `--page <n>` | Page number for results |
| `--page-size <n>` | Results per page (default: 25) |
| `--verbose` / `-v` | Show more details per package |

---

## choco search

Same flags as `choco list`. Key ones:

| Flag | Effect |
|------|--------|
| `--exact` / `-e` | Exact name match |
| `--by-id-only` | Search IDs only |
| `--by-tag-only` | Search tags only |
| `--approved-only` | Community-approved packages only |
| `--not-broken` | Exclude broken packages |
| `-s` / `--source` | Target source |
| `--pre` | Include pre-release versions |
| `--page-size <n>` | Number of results per page |

---

## choco info

| Flag | Effect |
|------|--------|
| `-s` / `--source <src>` | Specific source |
| `--pre` | Include pre-release |
| `--local-only` | Only look at installed packages |
| `--verbose` / `-v` | Extended details |

---

## choco outdated

| Flag | Effect |
|------|--------|
| `--ignore-pinned` | Include pinned packages in the report |
| `--ignore-unfound` | Don't error on packages not found in source |
| `-s` / `--source` | Specific source to check against |
| `--pre` | Include pre-release versions |

---

## choco pin

| Flag | Effect |
|------|--------|
| `--name <name>` | Package name to pin/unpin |
| `--version <ver>` | Pin a specific version (not just the installed one) |

---

## choco source

| Flag | Effect |
|------|--------|
| `--name <name>` | Source identifier |
| `--source <url>` | Feed URL or local path |
| `--user <user>` | Username for authenticated sources |
| `--password <pass>` | Password (stored encrypted) |
| `--cert <path>` | Client certificate path |
| `--cert-password <pass>` | Client certificate password |
| `--priority <n>` | Source priority (lower = higher priority) |
| `--bypass-proxy` | Skip proxy for this source |
| `--allow-self-service` | Allow non-admins to use this source (Pro) |
| `--admin-only` | Restrict source to admins only (Pro) |

---

## choco config

| Flag | Effect |
|------|--------|
| `--name <name>` | Config key name |
| `--value <value>` | Config value to set |

---

## choco pack

| Flag | Effect |
|------|--------|
| `--version <ver>` | Override the version in the nuspec |
| `--out-dir <dir>` | Output directory for the `.nupkg` |

---

## choco push

| Flag | Effect |
|------|--------|
| `--source <url>` | Target feed URL |
| `--api-key <key>` | API key for authentication |
| `--timeout <secs>` | Upload timeout |

---

## Global flags (work with most commands)

| Flag | Effect |
|------|--------|
| `-y` / `--yes` | Confirm all prompts |
| `-v` / `--verbose` | More output |
| `-d` / `--debug` | Debug output |
| `-f` / `--force` | Force operation |
| `--no-progress` | Suppress progress bars |
| `--log-file <path>` | Write output to a log file |
| `--limit-output` / `-r` | Pipe-friendly output (minimal formatting) |
| `--timeout <secs>` | Command timeout in seconds |
| `-n` / `--whatif` | Dry run |
| `--help` / `-h` | Show help |
| `--version` | Print Chocolatey version |
