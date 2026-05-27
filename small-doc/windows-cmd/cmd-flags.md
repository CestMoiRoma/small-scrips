# Windows CMD Flags Reference

---

## dir

| Flag | Effect |
|------|--------|
| `/a` | Show all files including hidden and system |
| `/a:h` | Hidden files only |
| `/a:s` | System files only |
| `/a:d` | Directories only |
| `/a:-h` | Non-hidden files only |
| `/b` | Bare format — filenames only, no heading or summary |
| `/s` | Recurse into subdirectories |
| `/p` | Pause after each screen |
| `/w` | Wide list format |
| `/o:n` | Sort by name (alphabetical) |
| `/o:e` | Sort by extension |
| `/o:s` | Sort by size |
| `/o:d` | Sort by date |
| `/o:-d` | Sort by date, newest first |
| `/t:c` | Use creation time |
| `/t:a` | Use last access time |
| `/t:w` | Use last write time (default) |
| `/q` | Show file ownership |
| `/x` | Show short (8.3) filenames |
| `/l` | Lowercase output |
| `/r` | Show alternate data streams |

---

## copy

| Flag | Effect |
|------|--------|
| `/y` | Overwrite without confirmation |
| `/-y` | Always ask before overwriting |
| `/b` | Binary mode (default for non-text) |
| `/a` | ASCII mode |
| `/v` | Verify after copy |
| `/z` | Restartable mode (for network copies) |

---

## xcopy

| Flag | Effect |
|------|--------|
| `/e` | Copy subdirectories including empty ones |
| `/s` | Copy subdirectories excluding empty ones |
| `/i` | Assume destination is a directory if copying multiple files |
| `/y` | Overwrite without confirmation |
| `/h` | Copy hidden and system files |
| `/r` | Overwrite read-only files |
| `/t` | Copy directory structure only (no files) |
| `/k` | Keep read-only attributes |
| `/f` | Display full source and destination names |
| `/l` | List only — don't copy (dry run) |
| `/d` | Copy only files newer than destination |
| `/d:mm-dd-yyyy` | Copy files modified on or after date |
| `/z` | Restartable mode |
| `/q` | Quiet mode |
| `/exclude:file.txt` | Exclude files listed in a text file |

---

## robocopy

| Flag | Effect |
|------|--------|
| `/e` | Copy subdirectories including empty ones |
| `/s` | Copy subdirectories excluding empty ones |
| `/mir` | Mirror — copy + delete files in dst not in src |
| `/mov` | Move files (delete source after copy) |
| `/move` | Move files and directories |
| `/z` | Restartable mode |
| `/b` | Backup mode (bypasses access restrictions) |
| `/mt[:n]` | Multi-threaded copy, n threads (default 8) |
| `/r:n` | Retries on failure (default 1000000) |
| `/w:n` | Wait n seconds between retries (default 30) |
| `/xf <files>` | Exclude files (wildcards allowed) |
| `/xd <dirs>` | Exclude directories |
| `/xa:h` | Exclude hidden files |
| `/xo` | Exclude older files (skip if dst is newer) |
| `/xx` | Exclude extra files in dst (don't delete) |
| `/l` | List only — dry run |
| `/log:file.txt` | Write log to file |
| `/tee` | Output to screen AND log |
| `/nfl` | No file list in output |
| `/ndl` | No directory list in output |
| `/njh` | No job header |
| `/njs` | No job summary |
| `/np` | No progress percentage |

---

## del

| Flag | Effect |
|------|--------|
| `/f` | Force deletion of read-only files |
| `/s` | Delete from all subdirectories |
| `/q` | Quiet — no confirmation for wildcards |
| `/a:h` | Delete hidden files |
| `/a:r` | Delete read-only files |

---

## rmdir / rd

| Flag | Effect |
|------|--------|
| `/s` | Remove directory tree (all contents) |
| `/q` | Quiet — no confirmation |

---

## find

| Flag | Effect |
|------|--------|
| `/v` | Invert — display lines that do NOT match |
| `/c` | Count matching lines only |
| `/n` | Prefix each matching line with its line number |
| `/i` | Case-insensitive search |

---

## findstr

| Flag | Effect |
|------|--------|
| `/i` | Case-insensitive |
| `/v` | Invert match |
| `/n` | Show line numbers |
| `/s` | Search recursively in subdirectories |
| `/r` | Use regular expressions (default when pattern has special chars) |
| `/l` | Use literal string (no regex) |
| `/m` | Print only filenames with a match |
| `/x` | Match entire line |
| `/c:"string"` | Use string as literal search phrase |
| `/f:file.txt` | Read list of files to search from a file |
| `/g:pat.txt` | Read patterns from a file |

---

## tasklist

| Flag | Effect |
|------|--------|
| `/fo table` | Table format (default) |
| `/fo csv` | CSV format |
| `/fo list` | List format |
| `/v` | Verbose — include window title, status, memory |
| `/svc` | Show services hosted by each process |
| `/fi "filter"` | Filter: `"imagename eq notepad.exe"`, `"pid eq 1234"` |
| `/nh` | No header row |

---

## taskkill

| Flag | Effect |
|------|--------|
| `/im <name>` | Kill by image (process) name |
| `/pid <n>` | Kill by PID |
| `/f` | Force — use `SIGKILL` equivalent |
| `/t` | Kill process tree (parent + all children) |

---

## netstat

| Flag | Effect |
|------|--------|
| `-a` | All connections and listening ports |
| `-n` | Numeric addresses (no DNS resolution) |
| `-o` | Include PID |
| `-b` | Include executable name (admin required) |
| `-p <proto>` | Filter by protocol: `tcp`, `udp` |
| `-r` | Show routing table |
| `-s` | Per-protocol statistics |
| `-e` | Ethernet statistics |

---

## ping

| Flag | Effect |
|------|--------|
| `-n <n>` | Number of echo requests (default 4) |
| `-t` | Ping continuously until stopped with Ctrl+C |
| `-l <size>` | Buffer size in bytes |
| `-f` | Set "Don't Fragment" flag |
| `-i <ttl>` | Time To Live |
| `-4` | Force IPv4 |
| `-6` | Force IPv6 |
| `-a` | Resolve addresses to hostnames |

---

## schtasks

| Flag | Effect |
|------|--------|
| `/create` | Create a new task |
| `/delete` | Delete a task |
| `/query` | List tasks |
| `/run` | Run a task immediately |
| `/end` | Stop a running task |
| `/change` | Modify a task |
| `/tn <name>` | Task name |
| `/tr <cmd>` | Command to run |
| `/sc <schedule>` | Schedule: `daily`, `weekly`, `monthly`, `once`, `onstart`, `onlogon`, `onidle` |
| `/st <HH:MM>` | Start time |
| `/d <day>` | Day of week or month |
| `/mo <modifier>` | Modifier (e.g. every 2 weeks) |
| `/ru <user>` | Run as user |
| `/rp <password>` | Password for run-as user |
| `/f` | Force (overwrite existing task) |
| `/fo list` | Query output as list |
| `/v` | Verbose query |

---

## cmd.exe itself

| Flag | Effect |
|------|--------|
| `/c <cmd>` | Run command then exit |
| `/k <cmd>` | Run command and stay open |
| `/q` | Turn off echo |
| `/d` | Disable AutoRun registry entries |
| `/a` | ANSI output |
| `/u` | Unicode output |
| `/t:bg` | Set text/background color: `/t:0a` = black bg, green text |
| `/f:on` | Enable filename and directory tab completion |
