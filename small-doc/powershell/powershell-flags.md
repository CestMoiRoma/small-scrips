# PowerShell Flags Reference

---

## pwsh.exe / powershell.exe (launcher)

| Flag | Effect |
|------|--------|
| `-Command <cmd>` / `-c` | Run a command string and exit |
| `-File <path>` / `-f` | Run a script file |
| `-NoExit` / `-noe` | Stay open after running `-Command` or `-File` |
| `-NoProfile` / `-nop` | Skip loading the profile (`$PROFILE`) |
| `-NonInteractive` / `-noni` | Don't present an interactive prompt |
| `-ExecutionPolicy <policy>` / `-ep` | Set execution policy for this session |
| `-WindowStyle Hidden` | Start with a hidden window |
| `-EncodedCommand <base64>` / `-enc` | Run a Base64-encoded command |
| `-InputFormat <fmt>` | Input format: `Text` or `XML` |
| `-OutputFormat <fmt>` | Output format: `Text` or `XML` |
| `-Version <n>` | Launch a specific PowerShell version |
| `-WorkingDirectory <path>` / `-wd` | Set initial working directory (pwsh only) |

---

## Get-ChildItem (ls / dir)

| Flag | Effect |
|------|--------|
| `-Path <path>` | Directory or glob to list |
| `-Recurse` / `-r` | Recurse into subdirectories |
| `-Force` | Include hidden and system items |
| `-Filter <pattern>` | Provider-side filter (faster than `-Include`) |
| `-Include <pattern>` | Only items matching the pattern |
| `-Exclude <pattern>` | Skip items matching the pattern |
| `-Depth <n>` | Limit recursion depth |
| `-File` | Files only |
| `-Directory` | Directories only |
| `-Hidden` | Hidden items only |
| `-ReadOnly` | Read-only items only |
| `-System` | System items only |
| `-Name` | Return names as strings instead of objects |
| `-LiteralPath` | Treat path literally (no wildcards) |

---

## Copy-Item

| Flag | Effect |
|------|--------|
| `-Recurse` | Copy directories recursively |
| `-Force` | Overwrite existing, create missing directories |
| `-PassThru` | Return the copied item as output |
| `-WhatIf` | Simulate without copying |
| `-Confirm` | Prompt before each copy |
| `-Exclude <pattern>` | Skip matching items |
| `-Filter <pattern>` | Provider-side filter |

---

## Remove-Item

| Flag | Effect |
|------|--------|
| `-Recurse` | Remove directory and all contents |
| `-Force` | Remove read-only and hidden items, skip prompts |
| `-WhatIf` | Simulate without deleting |
| `-Confirm` | Prompt before each deletion |
| `-Exclude <pattern>` | Skip matching items |
| `-Filter <pattern>` | Provider-side filter |

---

## Get-Content

| Flag | Effect |
|------|--------|
| `-Path <file>` | File to read |
| `-Raw` | Return full content as a single string |
| `-Tail <n>` | Read last n lines |
| `-TotalCount <n>` / `-Head` | Read first n lines |
| `-Encoding <enc>` | `UTF8`, `Unicode`, `ASCII`, `Default`… |
| `-Delimiter <str>` | Custom line delimiter |
| `-Wait` | Poll for new content (like `tail -f`) |
| `-ReadCount <n>` | Lines to send down pipeline per batch |

---

## Select-Object

| Flag | Effect |
|------|--------|
| `-Property <names>` | Properties to include |
| `-ExcludeProperty <names>` | Properties to exclude |
| `-First <n>` | First n objects |
| `-Last <n>` | Last n objects |
| `-Skip <n>` | Skip first n objects |
| `-SkipLast <n>` | Skip last n objects |
| `-Unique` | Remove duplicates |
| `-ExpandProperty <name>` | Return the value of one property directly |
| `-Index <n>` | Return objects at specific indexes |

---

## Where-Object

```powershell
# Simplified syntax (single condition)
Get-Process | Where-Object CPU -gt 100
Get-Service | Where-Object Status -eq "Running"

# Script block syntax (complex conditions)
Get-Process | Where-Object { $_.CPU -gt 100 -and $_.Name -ne "Idle" }
```

| Operator | Meaning |
|----------|---------|
| `-eq` `-ne` | Equal / not equal |
| `-gt` `-lt` `-ge` `-le` | Numeric comparison |
| `-like` `-notlike` | Wildcard match |
| `-match` `-notmatch` | Regex match |
| `-contains` `-notcontains` | Array contains value |
| `-in` `-notin` | Value is/isn't in array |

---

## Sort-Object

| Flag | Effect |
|------|--------|
| `-Property <name>` | Property to sort by |
| `-Descending` | Reverse order |
| `-Unique` | Remove duplicates |
| `-Top <n>` | Return top n after sorting |
| `-Bottom <n>` | Return bottom n after sorting |
| `-Stable` | Preserve original order for equal items |
| `-CaseSensitive` | Case-sensitive string sort |

---

## Invoke-WebRequest (iwr / curl / wget)

| Flag | Effect |
|------|--------|
| `-Uri <url>` | Target URL |
| `-OutFile <path>` | Save response body to file |
| `-Method <verb>` | `GET`, `POST`, `PUT`, `DELETE`… (default `GET`) |
| `-Body <data>` | Request body (string or hashtable) |
| `-Headers <hashtable>` | Custom headers |
| `-ContentType <type>` | Content-Type header |
| `-Credential <cred>` | Authentication credential |
| `-UseBasicParsing` | Skip HTML parsing (faster, no IE engine) |
| `-SessionVariable <name>` | Store session (cookies) in a variable |
| `-WebSession <var>` | Use a stored session |
| `-TimeoutSec <n>` | Timeout in seconds |
| `-MaximumRedirection <n>` | Max redirects to follow (default 5) |
| `-SkipCertificateCheck` | Ignore SSL errors (pwsh 6+) |
| `-Proxy <url>` | Use a proxy |
| `-NoProxy` | Bypass system proxy |

---

## Start-Process

| Flag | Effect |
|------|--------|
| `-FilePath <path>` | Executable to run |
| `-ArgumentList <args>` | Arguments to pass |
| `-WorkingDirectory <dir>` | Starting directory |
| `-Wait` | Wait for the process to exit |
| `-PassThru` | Return the process object |
| `-NoNewWindow` | Run in current window |
| `-WindowStyle <style>` | `Normal`, `Hidden`, `Minimized`, `Maximized` |
| `-Verb RunAs` | Run as administrator (UAC prompt) |
| `-RedirectStandardOutput <file>` | Capture stdout |
| `-RedirectStandardError <file>` | Capture stderr |

---

## Select-String (grep)

| Flag | Effect |
|------|--------|
| `-Pattern <regex>` | Pattern to search for |
| `-Path <files>` | Files to search |
| `-LiteralPath` | Literal path (no wildcards) |
| `-CaseSensitive` | Case-sensitive match |
| `-NotMatch` | Lines that don't match |
| `-AllMatches` | Return all matches per line (not just first) |
| `-List` | Only return first match per file |
| `-Quiet` | Return `$true`/`$false` only |
| `-Context <pre>,<post>` | Lines of context before and after |
| `-Include <pattern>` | File name filter |
| `-Exclude <pattern>` | File name exclusion |
| `-Recurse` | Search subdirectories |
| `-Encoding <enc>` | File encoding |

---

## Common parameters (work with most cmdlets)

| Parameter | Effect |
|-----------|--------|
| `-WhatIf` | Simulate — show what would happen without doing it |
| `-Confirm` | Prompt for confirmation before acting |
| `-Verbose` | Show detailed processing messages |
| `-Debug` | Show debug messages |
| `-ErrorAction <value>` | `Stop`, `SilentlyContinue`, `Continue`, `Ignore` |
| `-ErrorVariable <var>` | Store errors in a variable |
| `-OutVariable <var>` | Store output in a variable AND pass it on |
| `-PipelineVariable <var>` | Store current pipeline object in a variable |
| `-WarningAction <value>` | Same values as `-ErrorAction` |
| `-InformationAction <value>` | Same values as `-ErrorAction` |
