# Windows CMD — Quick Cheat Sheet

---

## Navigation

| Command | Description |
|---------|-------------|
| `cd` | Print current directory |
| `cd <dir>` | Change directory |
| `cd ..` | Go up one level |
| `cd \` | Go to root of current drive |
| `cd /d D:\path` | Change drive and directory |
| `D:` | Switch to drive D |
| `pushd <dir>` | Save current dir and go to `<dir>` |
| `popd` | Return to saved directory |

---

## Listing & viewing

| Command | Description |
|---------|-------------|
| `dir` | List files |
| `dir /a` | Include hidden files |
| `dir /s` | Recursive listing |
| `dir /b` | Names only |
| `dir /o:d` | Sort by date |
| `dir /o:s` | Sort by size |
| `dir *.txt` | Filter by extension |
| `type <file>` | Print file contents |
| `more <file>` | Paginate file |
| `cls` | Clear screen |

---

## Files & directories

| Command | Description |
|---------|-------------|
| `mkdir <dir>` | Create directory |
| `rmdir /s /q <dir>` | Delete directory tree |
| `copy <src> <dst>` | Copy file |
| `copy /y <src> <dst>` | Copy, no confirmation |
| `xcopy <src> <dst> /e /i` | Copy directory tree |
| `robocopy <src> <dst> /e` | Robust copy |
| `robocopy <src> <dst> /mir` | Mirror directories |
| `move <src> <dst>` | Move or rename |
| `ren <old> <new>` | Rename |
| `del <file>` | Delete file |
| `del /f /s /q <file>` | Force delete silently |

---

## Search

| Command | Description |
|---------|-------------|
| `find "text" <file>` | Search string in file |
| `find /i "text" <file>` | Case-insensitive |
| `find /c "text" <file>` | Count matches |
| `findstr "pattern" <file>` | Regex search |
| `findstr /s "text" *.*` | Recursive search |
| `findstr /i /s "text" *.txt` | Case-insensitive recursive |
| `where <cmd>` | Find executable path |

---

## Environment variables

| Command | Description |
|---------|-------------|
| `set` | List all variables |
| `set VAR=value` | Set for current session |
| `echo %VAR%` | Print a variable |
| `setx VAR "value"` | Set permanently (user) |
| `setx VAR "value" /m` | Set permanently (system, admin) |
| `%USERPROFILE%` | User home folder |
| `%TEMP%` | Temp directory |
| `%PATH%` | Executable search path |
| `%COMPUTERNAME%` | Machine name |
| `%USERNAME%` | Current user |

---

## Redirections & pipes

| Syntax | Description |
|--------|-------------|
| `cmd > file` | Stdout to file (overwrite) |
| `cmd >> file` | Stdout to file (append) |
| `cmd 2> err.txt` | Stderr to file |
| `cmd > out.txt 2>&1` | Both to same file |
| `cmd1 \| cmd2` | Pipe |
| `cmd > nul` | Discard stdout |
| `cmd > nul 2>&1` | Discard everything |

---

## Processes

| Command | Description |
|---------|-------------|
| `tasklist` | All running processes |
| `tasklist /fi "imagename eq app.exe"` | Filter by name |
| `taskkill /im <name>.exe /f` | Kill by name |
| `taskkill /pid <PID> /f` | Kill by PID |
| `taskkill /pid <PID> /f /t` | Kill process tree |
| `start <program>` | Launch a program |

---

## Network

| Command | Description |
|---------|-------------|
| `ipconfig` | IP addresses |
| `ipconfig /all` | Full network details |
| `ipconfig /flushdns` | Clear DNS cache |
| `ping <host>` | Test connectivity |
| `ping -t <host>` | Ping continuously |
| `tracert <host>` | Trace route |
| `nslookup <host>` | DNS lookup |
| `netstat -an` | All connections + listening ports |
| `netstat -ano` | With PIDs |
| `netstat -ano \| findstr :8080` | Find what uses port 8080 |

---

## System

| Command | Description |
|---------|-------------|
| `systeminfo` | OS and hardware info |
| `hostname` | Computer name |
| `whoami` | Current user |
| `ver` | Windows version |
| `shutdown /s /t 0` | Shut down immediately |
| `shutdown /r /t 0` | Restart immediately |
| `shutdown /a` | Abort scheduled shutdown |

---

## Batch scripting

| Syntax | Description |
|--------|-------------|
| `@echo off` | Suppress command echoing |
| `:: comment` | Comment |
| `set VAR=val` | Set variable |
| `set /a VAR=1+1` | Arithmetic |
| `set /p VAR=Prompt:` | Read user input |
| `%VAR%` | Use variable |
| `!VAR!` | Use variable inside loop (delayed expansion) |
| `%1 %2 …` | Script arguments |
| `if "%VAR%"=="x" …` | String comparison |
| `if %N% GTR 0 …` | Numeric comparison |
| `if exist <file> …` | File existence check |
| `for %%i in (a b) do …` | Loop over list |
| `for /l %%i in (1,1,10) do …` | Counter loop |
| `for /f "tokens=*" %%l in (f) do …` | Loop over file lines |
| `goto :label` | Jump to label |
| `call :label arg` | Call a sub-routine |
| `exit /b 0` | Exit script with code |
| `cmd \|\| echo failed` | Run on failure |
| `cmd && echo ok` | Run on success |

---

## Useful one-liners

| Command | Description |
|---------|-------------|
| `explorer .` | Open current folder in Explorer |
| `cd \| clip` | Copy current path to clipboard |
| `certutil -hashfile <f> SHA256` | File hash |
| `fc <f1> <f2>` | Compare two files |
| `netstat -ano \| findstr :8080` | Who uses port 8080 |
| `for /d /r . %%d in (node_modules) do rd /s/q "%%d"` | Delete all node_modules |
