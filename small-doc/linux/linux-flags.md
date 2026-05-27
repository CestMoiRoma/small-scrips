# Linux Flags Reference

All the notable flags, organized by command.

---

## ls

| Flag | Effect |
|------|--------|
| `-l` | Long format (permissions, owner, size, date) |
| `-a` | Show hidden files (starting with `.`) |
| `-h` | Human-readable sizes (KB, MB…) — use with `-l` |
| `-r` | Reverse sort order |
| `-t` | Sort by modification time (newest first) |
| `-S` | Sort by file size (largest first) |
| `-R` | List recursively |
| `-1` | One file per line |
| `--color` | Colorize output |

---

## cp

| Flag | Effect |
|------|--------|
| `-r` | Copy directories recursively |
| `-p` | Preserve permissions, timestamps, ownership |
| `-a` | Archive mode — recursive + preserve everything |
| `-i` | Prompt before overwriting |
| `-n` | Never overwrite existing files |
| `-u` | Copy only if source is newer than destination |
| `-v` | Verbose — show each file being copied |

---

## mv

| Flag | Effect |
|------|--------|
| `-i` | Prompt before overwriting |
| `-n` | Never overwrite existing files |
| `-u` | Move only if source is newer |
| `-v` | Verbose |

---

## rm

| Flag | Effect |
|------|--------|
| `-r` | Remove directories recursively |
| `-f` | Force — no prompt, ignore missing files |
| `-i` | Prompt before each deletion |
| `-v` | Verbose |
| `--no-preserve-root` | Allow deleting `/` (never use this) |

---

## mkdir

| Flag | Effect |
|------|--------|
| `-p` | Create parent directories as needed, no error if exists |
| `-m <mode>` | Set permissions at creation: `mkdir -m 755 dir` |
| `-v` | Verbose |

---

## find

| Flag | Effect |
|------|--------|
| `-name <pattern>` | Match by filename (case-sensitive) |
| `-iname <pattern>` | Match by filename (case-insensitive) |
| `-type f` | Files only |
| `-type d` | Directories only |
| `-type l` | Symbolic links only |
| `-size +100M` | Larger than 100 MB (`k`=KB, `M`=MB, `G`=GB) |
| `-mtime -7` | Modified in the last 7 days |
| `-mtime +30` | Modified more than 30 days ago |
| `-user <name>` | Owned by user |
| `-perm 644` | Exact permissions |
| `-empty` | Empty files or directories |
| `-maxdepth <n>` | Limit recursion depth |
| `-exec <cmd> {} \;` | Run command on each result |
| `-delete` | Delete matching files |
| `-not` / `!` | Negate the next condition |

---

## grep

| Flag | Effect |
|------|--------|
| `-r` | Search recursively in directories |
| `-i` | Case-insensitive match |
| `-n` | Show line numbers |
| `-v` | Invert match (show non-matching lines) |
| `-l` | Only print filenames with a match |
| `-L` | Only print filenames without a match |
| `-c` | Count matching lines |
| `-w` | Match whole words only |
| `-x` | Match whole lines only |
| `-A <n>` | Show n lines after the match |
| `-B <n>` | Show n lines before the match |
| `-C <n>` | Show n lines before and after |
| `-E` | Use extended regex (same as `egrep`) |
| `-P` | Use Perl-compatible regex |
| `-o` | Print only the matched part |
| `--color` | Highlight matches |

---

## tar

| Flag | Effect |
|------|--------|
| `-c` | Create an archive |
| `-x` | Extract an archive |
| `-t` | List archive contents |
| `-z` | Use gzip compression (`.tar.gz`) |
| `-j` | Use bzip2 compression (`.tar.bz2`) |
| `-J` | Use xz compression (`.tar.xz`) |
| `-f <file>` | Specify the archive filename |
| `-v` | Verbose — show files being processed |
| `-C <dir>` | Extract to a specific directory |
| `--exclude=<pattern>` | Exclude files matching pattern |
| `-p` | Preserve permissions |

---

## curl

| Flag | Effect |
|------|--------|
| `-o <file>` | Save output to a file |
| `-O` | Save with the remote filename |
| `-L` | Follow redirects |
| `-I` | Fetch headers only |
| `-s` | Silent — no progress or errors |
| `-S` | Show errors even with `-s` |
| `-v` | Verbose — show full request and response |
| `-X <method>` | HTTP method: `-X POST`, `-X DELETE` |
| `-H "Header: value"` | Add a request header |
| `-d "data"` | Send request body (POST) |
| `-u user:pass` | Basic authentication |
| `-k` | Skip SSL certificate verification |
| `--compressed` | Request and decompress gzip response |
| `-w "%{http_code}"` | Print specific info after transfer |

---

## ssh

| Flag | Effect |
|------|--------|
| `-p <port>` | Custom port |
| `-i <keyfile>` | Specify private key |
| `-L <local>:<host>:<remote>` | Local port forwarding |
| `-R <remote>:<host>:<local>` | Remote port forwarding |
| `-D <port>` | Dynamic SOCKS proxy |
| `-N` | Don't execute a command (for tunnels) |
| `-T` | Disable pseudo-terminal allocation |
| `-A` | Forward SSH agent |
| `-v` | Verbose (use `-vvv` for more detail) |
| `-o StrictHostKeyChecking=no` | Skip host key prompt (use carefully) |

---

## chmod

| Flag | Effect |
|------|--------|
| `-R` | Apply recursively |
| `-v` | Verbose |
| `+x` | Add execute for all |
| `u+x` | Add execute for owner only |
| `g-w` | Remove write from group |
| `o=r` | Set others to read-only |
| `a=rwx` | Set all (owner, group, others) |

---

## chown

| Flag | Effect |
|------|--------|
| `-R` | Apply recursively |
| `-v` | Verbose |
| `--from=<owner>` | Only change if current owner matches |

---

## ps

| Flag | Effect |
|------|--------|
| `a` | All processes with a terminal |
| `u` | User-oriented format |
| `x` | Include processes without a terminal |
| `-e` | All processes |
| `-f` | Full format (PPID, CMD…) |
| `-p <PID>` | Show a specific process |
| `--sort=-%cpu` | Sort by CPU descending |
| `--sort=-%mem` | Sort by memory descending |

---

## df

| Flag | Effect |
|------|--------|
| `-h` | Human-readable sizes |
| `-T` | Show filesystem type |
| `-i` | Show inode usage instead of block usage |
| `--total` | Add a total row |

---

## du

| Flag | Effect |
|------|--------|
| `-s` | Summary — total size only (no subdirs) |
| `-h` | Human-readable sizes |
| `-a` | Show size for all files, not just directories |
| `-d <n>` | Limit depth: `-d 1` for current level only |
| `--exclude=<pattern>` | Exclude files matching pattern |

---

## sort

| Flag | Effect |
|------|--------|
| `-n` | Numeric sort |
| `-r` | Reverse order |
| `-h` | Human-readable numbers (1K, 2M…) |
| `-u` | Remove duplicates |
| `-k <n>` | Sort by column n |
| `-t <sep>` | Field separator |
| `-f` | Case-insensitive |

---

## wget

| Flag | Effect |
|------|--------|
| `-O <file>` | Save to a specific filename |
| `-q` | Quiet mode |
| `-c` | Continue interrupted download |
| `-r` | Recursive download |
| `-np` | Don't go to parent directories (with `-r`) |
| `--no-check-certificate` | Skip SSL verification |
| `--limit-rate=<rate>` | Limit download speed: `--limit-rate=1M` |
