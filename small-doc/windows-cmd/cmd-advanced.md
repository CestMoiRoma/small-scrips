# Windows CMD Advanced

---

## Batch scripting

Save commands in a `.bat` or `.cmd` file and run it. CMD executes each line sequentially.

```bat
@echo off
setlocal enabledelayedexpansion

:: This is a comment
echo Hello, %USERNAME%!
```

`@echo off` — suppress printing each command line.
`setlocal` — keep variable changes local to the script.
`enabledelayedexpansion` — required to use `!VAR!` inside loops (see below).

---

## Variables in scripts

```bat
set NAME=Alice
echo Hello, %NAME%

:: Arithmetic
set /a RESULT = 10 + 5
echo %RESULT%

:: String length (workaround)
set STR=Hello
echo %STR:~0,3%    :: "Hel"   (chars 0–2)
echo %STR:~-2%     :: "lo"    (last 2 chars)

:: String replace
set PATH_CLEAN=%PATH: =%   :: remove all spaces

:: Prompt user
set /p INPUT=Enter something: 
echo You typed: %INPUT%
```

---

## Conditionals

```bat
if "%VAR%"=="hello" (
    echo match
) else (
    echo no match
)

if exist "file.txt" echo File found
if not exist "file.txt" echo File missing

:: Numeric comparison
if %NUM% GTR 10 echo Greater than 10
if %NUM% EQU 0 echo Zero

:: Operators: EQU NEQ LSS LEQ GTR GEQ

:: ERRORLEVEL check
some_command
if %ERRORLEVEL% NEQ 0 (
    echo Command failed
    exit /b 1
)
:: Shorthand:
some_command || echo failed
some_command && echo success
```

---

## Loops

```bat
:: Loop over a list
for %%i in (a b c) do echo %%i

:: Loop over files
for %%f in (*.txt) do echo %%f

:: Loop with a counter
for /l %%i in (1, 1, 10) do echo %%i
::              start, step, end

:: Loop over lines in a file
for /f "tokens=*" %%l in (file.txt) do echo %%l

:: Loop over command output
for /f "tokens=*" %%l in ('dir /b') do echo %%l

:: Loop over subdirectories recursively
for /r "C:\folder" %%f in (*.log) do del "%%f"

:: Variable inside loop (requires delayed expansion)
setlocal enabledelayedexpansion
set COUNT=0
for %%i in (1 2 3) do (
    set /a COUNT+=1
    echo !COUNT!
)
```

---

## Functions (labels + CALL)

CMD has no real functions, but labels + `call` simulate them.

```bat
@echo off
call :greet Alice
call :greet Bob
exit /b 0

:greet
echo Hello, %1!
exit /b 0
```

`%1`, `%2`… are positional arguments inside a labelled block (or to the script itself).

---

## GOTO

```bat
goto :start

:start
echo Started
goto :end

:end
echo Done
```

---

## robocopy — robust file copy

Preferred over `xcopy` for anything serious.

```cmd
robocopy <src> <dst>                  :: basic copy
robocopy <src> <dst> /e               :: include empty subdirectories
robocopy <src> <dst> /mir             :: mirror (delete files in dst not in src)
robocopy <src> <dst> /z               :: restartable mode
robocopy <src> <dst> /mt:8            :: 8 parallel threads
robocopy <src> <dst> /xf *.tmp        :: exclude files
robocopy <src> <dst> /xd node_modules :: exclude directories
robocopy <src> <dst> /log:out.txt     :: write log to file
robocopy <src> <dst> /tee             :: output to screen AND log
robocopy <src> <dst> /ndl /nfl /njh /njs  :: minimal output
```

robocopy exit codes: `0` = no change, `1` = copied, `2–7` = extra/mismatch, `8+` = error.

---

## Registry (reg)

```cmd
reg query HKCU\Software\MyApp
reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion /v ProductName
reg add   HKCU\Software\MyApp /v Setting /t REG_SZ /d "value" /f
reg delete HKCU\Software\MyApp /v Setting /f
reg delete HKCU\Software\MyApp /f   :: delete whole key
reg export HKCU\Software\MyApp backup.reg
reg import backup.reg
```

Hive abbreviations: `HKLM`, `HKCU`, `HKCR`, `HKU`, `HKCC`.

---

## Scheduled tasks (schtasks)

```cmd
:: Create a task
schtasks /create /tn "MyTask" /tr "C:\script.bat" /sc daily /st 09:00

:: Run at startup
schtasks /create /tn "MyTask" /tr "C:\script.bat" /sc onstart /ru SYSTEM

:: List tasks
schtasks /query /fo list /v

:: Run now
schtasks /run /tn "MyTask"

:: Delete
schtasks /delete /tn "MyTask" /f
```

---

## Services (sc & net)

```cmd
sc query                          :: list all services
sc query <service>                :: status of a service
sc start <service>
sc stop  <service>
sc config <service> start= auto   :: set start type
sc config <service> start= demand
sc config <service> start= disabled

net start <service>               :: simpler alternative
net stop  <service>
net start                         :: list running services
```

---

## Network commands

```cmd
net user                          :: list local users
net user <username> /add          :: create user
net user <username> /delete       :: delete user
net localgroup administrators <u> /add  :: add to admin group

netsh wlan show profiles          :: Wi-Fi profiles
netsh wlan show profile name="X" key=clear  :: show password
netsh interface ip show addresses :: IP addresses

arp -a                            :: ARP table
route print                       :: routing table
nbtstat -n                        :: NetBIOS names
```

---

## Useful one-liners

```cmd
:: Open current directory in Explorer
explorer .

:: Copy current directory path to clipboard
cd | clip

:: Show all open TCP connections with PIDs
netstat -ano

:: Find which process uses port 8080
netstat -ano | findstr :8080

:: Kill process using port 8080 (get PID first)
taskkill /pid <PID> /f

:: Recursively delete all node_modules folders
for /d /r . %%d in (node_modules) do @if exist "%%d" rd /s/q "%%d"

:: Count lines in a file
find /c "" file.txt

:: Get file hash
certutil -hashfile file.txt SHA256
```
