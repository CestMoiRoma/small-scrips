# PowerShell Advanced

---

## Functions

```powershell
function Get-Greeting {
    param(
        [Parameter(Mandatory)]
        [string]$Name,

        [string]$Greeting = "Hello",

        [switch]$Loud          # flag — $true if passed, $false if not
    )
    $msg = "$Greeting, $Name!"
    if ($Loud) { $msg.ToUpper() } else { $msg }
}

Get-Greeting -Name "Alice"
Get-Greeting -Name "Alice" -Greeting "Hi" -Loud
```

### Pipeline-aware functions

```powershell
function Double-Number {
    param(
        [Parameter(ValueFromPipeline)]
        [int]$Number
    )
    process {
        $Number * 2
    }
}

1..5 | Double-Number
```

`begin {}` runs once before pipeline. `process {}` runs per object. `end {}` runs once after.

---

## Error handling

```powershell
# Try / Catch / Finally
try {
    Get-Item "missing.txt" -ErrorAction Stop   # -ErrorAction Stop is required to catch
}
catch [System.IO.FileNotFoundException] {
    Write-Error "File not found: $_"
}
catch {
    Write-Error "Unexpected error: $_"
}
finally {
    Write-Host "Always runs"
}

# $ErrorActionPreference
$ErrorActionPreference = "Stop"   # treat all errors as terminating (script-wide)

# Common -ErrorAction values per cmdlet
-ErrorAction Stop          # throw terminating error
-ErrorAction SilentlyContinue  # suppress error
-ErrorAction Continue      # default — show error, keep going
-ErrorAction Ignore        # suppress completely

# Check last error
$Error[0]                  # most recent error
$Error.Clear()
```

---

## Modules

```powershell
Get-Module                          # loaded modules
Get-Module -ListAvailable           # installed modules
Import-Module <name>                # load a module
Remove-Module <name>                # unload

# PSGallery
Find-Module <name>                  # search
Install-Module <name>               # install
Install-Module <name> -Scope CurrentUser  # no admin required
Update-Module <name>                # update
Uninstall-Module <name>
```

---

## Remoting

Run commands on remote machines.

```powershell
# Enable remoting (run as admin on the target)
Enable-PSRemoting -Force

# Interactive session
Enter-PSSession -ComputerName server01
Exit-PSSession

# Run a command on a remote machine
Invoke-Command -ComputerName server01 -ScriptBlock {
    Get-Process | Sort-Object CPU -Descending | Select-Object -First 5
}

# Run on multiple machines
Invoke-Command -ComputerName srv1, srv2, srv3 -ScriptBlock { hostname }

# Pass variables into the remote block
$threshold = 100
Invoke-Command -ComputerName srv1 -ScriptBlock {
    Get-Process | Where-Object CPU -gt $using:threshold
}

# Persistent session
$s = New-PSSession -ComputerName server01
Invoke-Command -Session $s -ScriptBlock { ... }
Remove-PSSession $s
```

---

## Jobs — background tasks

```powershell
# Start a background job
$job = Start-Job -ScriptBlock { Start-Sleep 5; "done" }

# List jobs
Get-Job

# Wait for a job
Wait-Job $job

# Get results
Receive-Job $job

# Remove when done
Remove-Job $job

# Shorter: Start-Job + Receive-Job + Remove-Job
Start-Job { Get-Process } | Wait-Job | Receive-Job | Remove-Job
```

---

## Profile

Runs at every shell startup.

```powershell
$PROFILE                           # path to your profile script
Test-Path $PROFILE                 # check if it exists
New-Item $PROFILE -Force           # create it
notepad $PROFILE                   # edit it
. $PROFILE                         # reload without restarting
```

Example `$PROFILE` content:

```powershell
# Aliases
Set-Alias ll Get-ChildItem
Set-Alias grep Select-String

# Prompt customization
function prompt {
    "PS $($PWD.Path)> "
}

# Auto-load modules
Import-Module posh-git
```

---

## Classes (PowerShell 5+)

```powershell
class Animal {
    [string]$Name
    [int]$Age

    Animal([string]$name, [int]$age) {
        $this.Name = $name
        $this.Age  = $age
    }

    [string] Speak() {
        return "$($this.Name) makes a sound"
    }

    static [string] Kingdom() {
        return "Animalia"
    }
}

class Dog : Animal {
    Dog([string]$name, [int]$age) : base($name, $age) {}

    [string] Speak() {
        return "$($this.Name) barks"
    }
}

$d = [Dog]::new("Rex", 3)
$d.Speak()
[Animal]::Kingdom()
```

---

## Regular expressions

```powershell
"hello123" -match "\d+"          # $true, sets $Matches
$Matches[0]                      # "123"

"abc 123 def" -replace "\d+", "NUM"   # "abc NUM def"

"one two three" -split "\s+"     # @("one", "two", "three")

# Select-String (grep equivalent)
Get-Content file.txt | Select-String "error"
Select-String -Path *.log -Pattern "error" -CaseSensitive
Select-String -Path *.log -Pattern "error" -Context 2,2   # 2 lines before/after
```

---

## Working with JSON, CSV & XML

```powershell
# JSON
$json = Get-Content data.json -Raw | ConvertFrom-Json
$json.users | Select-Object name, email
$obj | ConvertTo-Json -Depth 5 | Set-Content out.json

# CSV
Import-Csv data.csv | Where-Object { $_.Age -gt 30 }
Get-Process | Export-Csv procs.csv -NoTypeInformation
$rows = Import-Csv data.csv
$rows[0].Name

# XML
[xml]$doc = Get-Content config.xml
$doc.configuration.appSettings.add
```

---

## Registry provider

```powershell
# Navigate registry like a filesystem
Set-Location HKCU:\Software\MyApp
Get-ChildItem
Get-ItemProperty .

# Read a value
Get-ItemPropertyValue HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion -Name ProductName

# Write a value
Set-ItemProperty HKCU:\Software\MyApp -Name Setting -Value "hello"
New-Item HKCU:\Software\MyApp -Force
New-ItemProperty HKCU:\Software\MyApp -Name Version -Value "1.0" -PropertyType String

# Delete
Remove-ItemProperty HKCU:\Software\MyApp -Name Setting
Remove-Item HKCU:\Software\MyApp -Recurse
```

---

## Useful one-liners

```powershell
# Find large files
Get-ChildItem -Recurse | Sort-Object Length -Descending | Select-Object -First 10 FullName, Length

# Kill a process by name
Get-Process notepad | Stop-Process -Force

# Find what's listening on port 8080
Get-NetTCPConnection -LocalPort 8080 | Select-Object LocalPort, OwningProcess

# Download a file
Invoke-WebRequest -Uri "https://example.com/file.zip" -OutFile file.zip
# or shorter
iwr "https://example.com/file.zip" -OutFile file.zip

# Get public IP
(Invoke-WebRequest -Uri "https://ifconfig.me").Content

# Restart a service
Restart-Service -Name "wuauserv"

# Check if a port is open
Test-NetConnection -ComputerName google.com -Port 443

# List all open TCP connections with process names
Get-NetTCPConnection | Select-Object LocalPort,State,OwningProcess |
    ForEach-Object { $_ | Add-Member -NotePropertyName Process -NotePropertyValue (Get-Process -Id $_.OwningProcess -ErrorAction SilentlyContinue).Name -PassThru }

# Generate a random password
-join ((65..90) + (97..122) + (48..57) | Get-Random -Count 16 | ForEach-Object { [char]$_ })

# Measure script execution time
Measure-Command { Get-ChildItem -Recurse }
```
