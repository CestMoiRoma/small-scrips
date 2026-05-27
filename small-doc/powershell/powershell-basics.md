# PowerShell Basics

---

## Core concepts

| Concept | What it is |
|---------|------------|
| **Cmdlet** | A built-in command. Always `Verb-Noun` format: `Get-Process`, `Set-Item`. |
| **Pipeline** | Pass objects (not text) from one cmdlet to the next with `\|`. |
| **Object** | Everything in PowerShell is a .NET object with properties and methods. |
| **Provider** | Exposes data stores (filesystem, registry, env vars…) as drives (`C:`, `HKCU:`, `Env:`). |
| **Module** | A package of cmdlets. Installed from PSGallery with `Install-Module`. |
| **Profile** | A script that runs at shell startup: `$PROFILE`. |
| **Execution Policy** | Controls which scripts can run: `Restricted`, `RemoteSigned`, `Unrestricted`. |
| `$_` / `$PSItem` | The current object in the pipeline. |
| `$?` | `$true` if last command succeeded. |
| `$LASTEXITCODE` | Exit code of the last native command. |

---

## Getting help

```powershell
Get-Help <cmdlet>               # built-in help
Get-Help <cmdlet> -Examples     # show examples only
Get-Help <cmdlet> -Full         # full documentation
Get-Help <cmdlet> -Online       # open browser
Update-Help                     # download latest help files

Get-Command                     # list all available commands
Get-Command -Verb Get           # filter by verb
Get-Command -Noun Process       # filter by noun
Get-Command *network*           # wildcard search

Get-Member                      # inspect object properties and methods
Get-Process | Get-Member
```

---

## Variables

```powershell
$name = "Alice"
$num  = 42
$list = @(1, 2, 3)
$map  = @{ key = "value"; count = 5 }

# Types
[int]$n    = 10
[string]$s = "hello"
[bool]$b   = $true

# String interpolation
"Hello, $name"             # variables expanded
'Hello, $name'             # literal — no expansion
"Value: $($obj.Property)"  # expression inside string

# Multiline string (here-string)
$text = @"
Line one
Line two, $name
"@
```

---

## Navigation & filesystem

```powershell
Get-Location                    # pwd
Set-Location <path>             # cd
Set-Location ..                 # go up
Push-Location <path>            # pushd
Pop-Location                    # popd

Get-ChildItem                   # ls / dir
Get-ChildItem -Recurse          # recursive
Get-ChildItem -Force            # include hidden
Get-ChildItem *.txt             # filter

New-Item -ItemType Directory <dir>    # mkdir
New-Item -ItemType File <file>        # touch
Remove-Item <path>                    # rm
Remove-Item -Recurse -Force <dir>     # rm -rf
Copy-Item <src> <dst>                 # cp
Copy-Item -Recurse <src> <dst>        # cp -r
Move-Item <src> <dst>                 # mv
Rename-Item <old> <new>               # rename

Get-Content <file>              # cat
Get-Content -Tail 20 <file>     # tail
Set-Content <file> "text"       # overwrite
Add-Content <file> "text"       # append
```

---

## Pipeline

```powershell
# Pipe objects, not text
Get-Process | Sort-Object CPU -Descending | Select-Object -First 10
Get-Service | Where-Object { $_.Status -eq "Running" }
Get-ChildItem *.log | Remove-Item

# ForEach-Object — process each item
1..5 | ForEach-Object { $_ * 2 }
Get-Process | ForEach-Object { Write-Host $_.Name }

# Select-Object — pick properties
Get-Process | Select-Object Name, CPU, WorkingSet
Get-Process | Select-Object -First 5
Get-Process | Select-Object -Last 5
Get-Process | Select-Object -Unique Name

# Where-Object — filter
Get-Process | Where-Object CPU -gt 100
Get-Process | Where-Object { $_.WorkingSet -gt 100MB }

# Sort-Object
Get-Process | Sort-Object CPU -Descending
Get-ChildItem | Sort-Object LastWriteTime

# Measure-Object — statistics
Get-Process | Measure-Object CPU -Sum -Average -Max
Get-Content file.txt | Measure-Object -Line -Word -Character

# Group-Object
Get-Service | Group-Object Status
```

---

## Output & formatting

```powershell
Write-Host "Hello"              # print to screen (not pipeline)
Write-Output "Hello"            # print to pipeline
Write-Error "Something failed"  # write to error stream
Write-Warning "Watch out"       # write to warning stream
Write-Verbose "Detail"          # write to verbose stream (shown with -Verbose)

Format-Table                    # tabular output
Format-List                     # property list output
Format-Wide                     # wide column output
Out-GridView                    # interactive grid (Windows only)
Out-File <path>                 # write to file
Export-Csv <path>               # export as CSV
ConvertTo-Json                  # convert to JSON
ConvertFrom-Json                # parse JSON
```

---

## Strings

```powershell
$s = "Hello, World!"
$s.Length                       # 13
$s.ToUpper()
$s.ToLower()
$s.Trim()
$s.Replace("Hello", "Hi")
$s.Split(",")                   # array of substrings
$s.StartsWith("He")             # $true
$s.Contains("World")            # $true
$s.Substring(0, 5)              # "Hello"
$s.IndexOf("World")             # 7
$s -like "*World*"              # wildcard match
$s -match "\d+"                 # regex match (sets $Matches)
$s -replace "\s+", "_"          # regex replace
"{0} is {1}" -f "age", 30      # format string
```

---

## Arrays & hashtables

```powershell
# Array
$arr = @(1, 2, 3)
$arr += 4                       # append
$arr[0]                         # first element
$arr[-1]                        # last element
$arr[1..3]                      # slice
$arr.Count
$arr | ForEach-Object { $_ * 2 }
[array]::Sort($arr)

# Hashtable
$ht = @{ name = "Alice"; age = 30 }
$ht["name"]                     # "Alice"
$ht.name                        # same
$ht["city"] = "Paris"           # add key
$ht.Remove("city")
$ht.Keys
$ht.Values
$ht.ContainsKey("name")
```

---

## Control flow

```powershell
# If
if ($x -gt 0) {
    "positive"
} elseif ($x -eq 0) {
    "zero"
} else {
    "negative"
}

# Switch
switch ($x) {
    1       { "one" }
    2       { "two" }
    default { "other" }
}
# Switch also works with -regex, -wildcard, -file

# For
for ($i = 0; $i -lt 5; $i++) { $i }

# ForEach
foreach ($item in $collection) { $item }
1..10 | ForEach-Object { $_ }

# While
while ($condition) { }

# Do-While
do { } while ($condition)

# Break / Continue / Return
foreach ($i in 1..10) {
    if ($i -eq 5) { break }
    if ($i % 2) { continue }
    $i
}
```

---

## Comparison operators

| Operator | Meaning |
|----------|---------|
| `-eq` | Equal |
| `-ne` | Not equal |
| `-gt` | Greater than |
| `-lt` | Less than |
| `-ge` | Greater or equal |
| `-le` | Less or equal |
| `-like` | Wildcard match (`*`, `?`) |
| `-notlike` | Wildcard non-match |
| `-match` | Regex match |
| `-notmatch` | Regex non-match |
| `-contains` | Array contains value |
| `-notcontains` | Array doesn't contain |
| `-in` | Value in array |
| `-notin` | Value not in array |
| `-and` | Logical AND |
| `-or` | Logical OR |
| `-not` / `!` | Logical NOT |

---

## Execution policy

```powershell
Get-ExecutionPolicy
Set-ExecutionPolicy RemoteSigned           # allow local + signed remote scripts
Set-ExecutionPolicy Bypass -Scope Process  # unrestricted for this session only
```

| Policy | Effect |
|--------|--------|
| `Restricted` | No scripts at all (default on Windows) |
| `AllSigned` | Only signed scripts |
| `RemoteSigned` | Local scripts ok, downloaded scripts need signature |
| `Unrestricted` | All scripts run (with warning for downloaded) |
| `Bypass` | Nothing is blocked, no warnings |
