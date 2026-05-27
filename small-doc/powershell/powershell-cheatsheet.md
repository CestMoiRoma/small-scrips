# PowerShell — Quick Cheat Sheet

---

## Help & discovery

| Command | Description |
|---------|-------------|
| `Get-Help <cmd>` | Built-in help |
| `Get-Help <cmd> -Examples` | Examples only |
| `Get-Help <cmd> -Full` | Full documentation |
| `Get-Command` | All available commands |
| `Get-Command -Verb Get` | Filter by verb |
| `Get-Command *network*` | Wildcard search |
| `Get-Member` | Properties and methods of an object |
| `Get-Alias` | List all aliases |
| `Update-Help` | Download latest help files |

---

## Navigation & filesystem

| Command | Description |
|---------|-------------|
| `Get-Location` | Print current path |
| `Set-Location <path>` | Change directory |
| `Set-Location ..` | Go up one level |
| `Push-Location <path>` | Save location and go |
| `Pop-Location` | Return to saved location |
| `Get-ChildItem` | List directory contents |
| `Get-ChildItem -Recurse` | Recursive list |
| `Get-ChildItem -Force` | Include hidden |
| `Get-ChildItem *.txt` | Filter by extension |
| `New-Item -ItemType Directory <dir>` | Create directory |
| `New-Item -ItemType File <file>` | Create empty file |
| `Remove-Item <path>` | Delete file |
| `Remove-Item -Recurse -Force <dir>` | Delete directory tree |
| `Copy-Item <src> <dst>` | Copy |
| `Copy-Item -Recurse <src> <dst>` | Copy directory |
| `Move-Item <src> <dst>` | Move or rename |
| `Rename-Item <old> <new>` | Rename |
| `Test-Path <path>` | Check if path exists |

---

## File content

| Command | Description |
|---------|-------------|
| `Get-Content <file>` | Print file |
| `Get-Content -Tail 20 <file>` | Last 20 lines |
| `Get-Content -Raw <file>` | As single string |
| `Get-Content -Wait <file>` | Follow (like `tail -f`) |
| `Set-Content <file> "text"` | Overwrite |
| `Add-Content <file> "text"` | Append |
| `Out-File <file>` | Redirect pipeline to file |
| `"text" \| Out-File -Append <file>` | Append to file |

---

## Variables

| Syntax | Description |
|--------|-------------|
| `$x = 42` | Set variable |
| `$arr = @(1,2,3)` | Array |
| `$ht = @{k="v"}` | Hashtable |
| `"Hello $name"` | String interpolation |
| `'Literal $name'` | No interpolation |
| `"$($obj.Prop)"` | Expression in string |
| `[int]$n = 5` | Typed variable |
| `$_` / `$PSItem` | Current pipeline object |
| `$?` | Last command succeeded? |
| `$LASTEXITCODE` | Exit code of last native cmd |
| `$Error[0]` | Most recent error |
| `$env:PATH` | Environment variable |

---

## Pipeline

| Command | Description |
|---------|-------------|
| `\| ForEach-Object { }` | Process each object |
| `\| Where-Object { $_.X -gt 5 }` | Filter |
| `\| Where-Object X -gt 5` | Simplified filter |
| `\| Select-Object Name, CPU` | Pick properties |
| `\| Select-Object -First 10` | First n |
| `\| Select-Object -Unique` | Deduplicate |
| `\| Sort-Object CPU -Descending` | Sort |
| `\| Group-Object Status` | Group by property |
| `\| Measure-Object -Sum` | Statistics |
| `\| Export-Csv file.csv` | Export as CSV |
| `\| ConvertTo-Json` | Convert to JSON |
| `\| Out-GridView` | Interactive grid |
| `\| Out-File file.txt` | Write to file |
| `\| clip` | Copy to clipboard |

---

## Processes & services

| Command | Description |
|---------|-------------|
| `Get-Process` | List processes |
| `Get-Process <name>` | Filter by name |
| `Stop-Process -Name <name>` | Kill by name |
| `Stop-Process -Id <pid> -Force` | Kill by PID |
| `Start-Process <path>` | Launch a program |
| `Start-Process <path> -Verb RunAs` | Run as admin |
| `Get-Service` | List services |
| `Get-Service <name>` | One service |
| `Start-Service <name>` | Start |
| `Stop-Service <name>` | Stop |
| `Restart-Service <name>` | Restart |
| `Set-Service -Name <n> -StartupType Automatic` | Auto-start |

---

## Network

| Command | Description |
|---------|-------------|
| `Test-NetConnection <host>` | Ping equivalent |
| `Test-NetConnection <host> -Port 443` | Port check |
| `Get-NetIPAddress` | IP addresses |
| `Get-NetTCPConnection` | Open TCP connections |
| `Get-NetTCPConnection -LocalPort 8080` | Who uses port 8080 |
| `Resolve-DnsName <host>` | DNS lookup |
| `Invoke-WebRequest -Uri <url>` | HTTP request |
| `Invoke-WebRequest -Uri <url> -OutFile f` | Download file |
| `Invoke-RestMethod -Uri <url>` | REST API call (auto-parses JSON) |

---

## Strings

| Expression | Description |
|------------|-------------|
| `$s.ToUpper()` | Uppercase |
| `$s.ToLower()` | Lowercase |
| `$s.Trim()` | Strip whitespace |
| `$s.Replace("a","b")` | Replace |
| `$s.Split(",")` | Split |
| `$s.StartsWith("x")` | Prefix check |
| `$s.Contains("x")` | Contains |
| `$s.Substring(0,5)` | Slice |
| `$s -like "*foo*"` | Wildcard match |
| `$s -match "\d+"` | Regex match |
| `$s -replace "\s+","_"` | Regex replace |
| `"{0} is {1}" -f "x", 1` | Format |
| `$s -split "\s+"` | Regex split |

---

## Error handling

| Syntax | Description |
|--------|-------------|
| `try { } catch { }` | Catch terminating errors |
| `catch [ExceptionType] { }` | Catch specific type |
| `finally { }` | Always runs |
| `-ErrorAction Stop` | Make non-terminating into terminating |
| `-ErrorAction SilentlyContinue` | Suppress errors |
| `$ErrorActionPreference = "Stop"` | Global error preference |
| `$?` | Was last command successful? |
| `$Error[0]` | Last error |

---

## Execution policy

| Command | Description |
|---------|-------------|
| `Get-ExecutionPolicy` | Current policy |
| `Set-ExecutionPolicy RemoteSigned` | Allow local scripts |
| `Set-ExecutionPolicy Bypass -Scope Process` | Unrestricted for this session |

---

## Modules

| Command | Description |
|---------|-------------|
| `Get-Module` | Loaded modules |
| `Get-Module -ListAvailable` | Installed modules |
| `Import-Module <name>` | Load a module |
| `Find-Module <name>` | Search PSGallery |
| `Install-Module <name>` | Install from PSGallery |
| `Install-Module <name> -Scope CurrentUser` | No admin required |
| `Update-Module <name>` | Update |
| `Uninstall-Module <name>` | Remove |

---

## Useful one-liners

| Command | Description |
|---------|-------------|
| `Get-ChildItem -Recurse \| Sort-Object Length -Desc \| Select -First 10` | Largest files |
| `Get-Process \| Sort-Object CPU -Desc \| Select -First 10` | Top CPU processes |
| `Get-NetTCPConnection -LocalPort 8080` | Who uses port 8080 |
| `(iwr https://ifconfig.me).Content` | Public IP |
| `Measure-Command { <cmd> }` | Time a command |
| `clip` (as pipeline target) | Copy to clipboard |
| `explorer .` | Open current folder |
| `$PROFILE` | Path to profile script |
| `. $PROFILE` | Reload profile |
