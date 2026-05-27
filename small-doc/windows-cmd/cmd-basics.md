# Windows CMD Basics

---

## Core concepts

| Concept | What it is |
|---------|------------|
| **CMD** | `cmd.exe` — the classic Windows command interpreter, inherited from DOS. |
| **Prompt** | `C:\Users\You>` — shows current drive and directory. |
| **Drive** | Windows uses lettered drives: `C:`, `D:`. Switching is done by typing the drive letter. |
| **Path separator** | Backslash `\` (forward slash `/` also works in most commands). |
| **Environment variable** | Named value stored in the session: `%VARNAME%`. |
| **Batch file** | A `.bat` or `.cmd` file containing a sequence of commands. |
| **ERRORLEVEL** | Exit code of the last command. `0` = success, anything else = failure. |

---

## Navigation

```cmd
cd                          :: print current directory
cd <dir>                    :: change directory
cd ..                       :: go up one level
cd \                        :: go to root of current drive
cd /d D:\projects           :: change drive and directory at once
D:                          :: switch to drive D

dir                         :: list files and folders
dir /a                      :: include hidden files
dir /s                      :: recursive listing
dir /b                      :: bare format (names only)
dir /o:n                    :: sort by name
dir /o:d                    :: sort by date
dir *.txt                   :: list only .txt files

pushd <dir>                 :: save current dir and go to <dir>
popd                        :: return to saved dir
```

---

## Files & directories

```cmd
mkdir <dir>                 :: create a directory
mkdir a\b\c                 :: create nested directories
rmdir <dir>                 :: remove an empty directory
rmdir /s <dir>              :: remove directory and all contents
rmdir /s /q <dir>           :: same, no confirmation

copy <src> <dst>            :: copy a file
copy /y <src> <dst>         :: overwrite without asking
xcopy <src> <dst> /e /i     :: copy directory tree
robocopy <src> <dst> /e     :: robust copy (preferred for dirs)

move <src> <dst>            :: move or rename a file/dir
ren <old> <new>             :: rename a file
del <file>                  :: delete a file
del /f <file>               :: force delete (read-only files)
del /s *.tmp                :: delete all .tmp recursively
```

---

## Viewing files

```cmd
type <file>                 :: print file contents
more <file>                 :: paginate file contents (Space to continue)
more /e <file>              :: extended mode with navigation keys
find "text" <file>          :: search for a string in a file
findstr "pattern" <file>    :: search with regex support
findstr /s "text" *.*       :: search recursively in all files
```

---

## Environment variables

```cmd
set                         :: list all variables
set VAR                     :: show variables starting with VAR
set MY_VAR=hello            :: set for current session
echo %MY_VAR%               :: use a variable
set /p MY_VAR=Enter value:  :: prompt the user for input
setx MY_VAR "hello"         :: set permanently (user scope)
setx MY_VAR "hello" /m      :: set permanently (system scope, admin required)
```

System variables:

| Variable | Value |
|----------|-------|
| `%USERPROFILE%` | Current user's home folder |
| `%APPDATA%` | Roaming AppData |
| `%LOCALAPPDATA%` | Local AppData |
| `%TEMP%` / `%TMP%` | Temp directory |
| `%SYSTEMROOT%` | `C:\Windows` |
| `%PROGRAMFILES%` | `C:\Program Files` |
| `%PATH%` | Executable search path |
| `%COMPUTERNAME%` | Machine name |
| `%USERNAME%` | Current user |
| `%OS%` | `Windows_NT` |

---

## Redirection & pipes

```cmd
cmd > file.txt              :: redirect stdout to file (overwrite)
cmd >> file.txt             :: redirect stdout to file (append)
cmd 2> errors.txt           :: redirect stderr
cmd > out.txt 2>&1          :: redirect both to same file
cmd < input.txt             :: use file as stdin
cmd1 | cmd2                 :: pipe output of cmd1 into cmd2
cmd > nul                   :: discard stdout
cmd > nul 2>&1              :: discard everything
```

---

## Network

```cmd
ipconfig                    :: show IP addresses
ipconfig /all               :: full details incl. MAC, DNS
ipconfig /flushdns          :: clear DNS cache
ipconfig /release           :: release DHCP lease
ipconfig /renew             :: renew DHCP lease

ping <host>                 :: test connectivity
ping -n 10 <host>           :: send 10 packets
tracert <host>              :: trace route
nslookup <host>             :: DNS lookup
netstat -an                 :: all connections and listening ports
netstat -b                  :: include executable names (admin)
```

---

## Processes

```cmd
tasklist                    :: list running processes
tasklist /fi "imagename eq notepad.exe"  :: filter by name
taskkill /im <name>.exe /f  :: force kill by name
taskkill /pid <PID> /f      :: force kill by PID
start <program>             :: launch a program
start "" "C:\path\app.exe"  :: launch with a specific path
```

---

## System

```cmd
systeminfo                  :: detailed OS and hardware info
hostname                    :: computer name
whoami                      :: current user
ver                         :: Windows version
date                        :: show or set the date
time                        :: show or set the time
shutdown /s /t 0            :: shut down immediately
shutdown /r /t 0            :: restart immediately
shutdown /a                 :: abort a scheduled shutdown
cls                         :: clear the screen
echo off                    :: stop printing commands
@echo off                   :: stop printing commands (without printing this line)
pause                       :: wait for a key press
exit                        :: close the current CMD window or end a batch
exit /b <code>              :: exit a batch script with an exit code
```

---

## Useful utilities

```cmd
clip                        :: copy stdin to clipboard: dir | clip
where <cmd>                 :: find the path of an executable
fc <file1> <file2>          :: compare two files
attrib <file>               :: show/change file attributes
compact /c <file>           :: compress a file (NTFS)
assoc .ext                  :: show file type associated with extension
ftype <type>                :: show command for a file type
```
