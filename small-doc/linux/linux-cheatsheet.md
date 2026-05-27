# Linux — Quick Cheat Sheet

---

## Navigation

| Command | Description |
|---------|-------------|
| `pwd` | Print current directory |
| `cd <dir>` | Change directory |
| `cd ..` | Go up one level |
| `cd ~` | Go to home directory |
| `cd -` | Go to previous directory |
| `ls` | List files |
| `ls -la` | Long format, show hidden files |
| `ls -lh` | Long format, human-readable sizes |
| `ls -lt` | Sort by modification time |
| `ls -lS` | Sort by size |
| `tree` | Visual directory tree |

---

## Files & Directories

| Command | Description |
|---------|-------------|
| `touch <file>` | Create empty file |
| `mkdir <dir>` | Create directory |
| `mkdir -p a/b/c` | Create nested directories |
| `cp <src> <dst>` | Copy file |
| `cp -r <src> <dst>` | Copy directory recursively |
| `cp -a <src> <dst>` | Copy preserving all attributes |
| `mv <src> <dst>` | Move or rename |
| `rm <file>` | Delete file |
| `rm -r <dir>` | Delete directory recursively |
| `rm -rf <dir>` | Force delete, no prompt |
| `ln -s <target> <link>` | Create symbolic link |
| `readlink -f <link>` | Resolve symlink to real path |

---

## Viewing & Editing Files

| Command | Description |
|---------|-------------|
| `cat <file>` | Print full file |
| `less <file>` | Scrollable view (q to quit) |
| `head <file>` | First 10 lines |
| `head -n 20 <file>` | First 20 lines |
| `tail <file>` | Last 10 lines |
| `tail -n 50 <file>` | Last 50 lines |
| `tail -f <file>` | Follow in real time |
| `wc -l <file>` | Count lines |
| `wc -w <file>` | Count words |
| `diff <f1> <f2>` | Compare two files |
| `nano <file>` | Simple terminal editor |
| `vim <file>` | Advanced terminal editor |

---

## Search

| Command | Description |
|---------|-------------|
| `grep "pat" <file>` | Search in a file |
| `grep -r "pat" <dir>` | Search recursively |
| `grep -i "pat" <file>` | Case-insensitive |
| `grep -n "pat" <file>` | Show line numbers |
| `grep -v "pat" <file>` | Invert match |
| `grep -l "pat" <dir>` | Only filenames with a match |
| `grep -C 3 "pat" <file>` | Show 3 lines of context |
| `find <dir> -name "*.py"` | Find by name |
| `find <dir> -type f` | Files only |
| `find <dir> -type d` | Directories only |
| `find <dir> -mtime -7` | Modified in last 7 days |
| `find <dir> -size +100M` | Larger than 100 MB |
| `find <dir> -name "*.log" -delete` | Find and delete |
| `which <cmd>` | Path of an executable |

---

## Permissions

| Command | Description |
|---------|-------------|
| `chmod 755 <file>` | rwxr-xr-x |
| `chmod 644 <file>` | rw-r--r-- |
| `chmod +x <file>` | Add execute for all |
| `chmod -R 755 <dir>` | Apply recursively |
| `chown user <file>` | Change owner |
| `chown user:group <file>` | Change owner and group |
| `chown -R user:group <dir>` | Recursive |
| `umask 022` | Default permission mask |

---

## Processes

| Command | Description |
|---------|-------------|
| `ps aux` | All running processes |
| `ps aux --sort=-%cpu` | Sorted by CPU usage |
| `top` | Live process viewer |
| `htop` | Improved top |
| `kill <PID>` | Graceful stop (SIGTERM) |
| `kill -9 <PID>` | Force kill (SIGKILL) |
| `pkill <name>` | Kill by name |
| `killall <name>` | Kill all matching |
| `nice -n 10 <cmd>` | Start with lower priority |
| `renice 10 -p <PID>` | Change running process priority |
| `nohup <cmd> &` | Run immune to hangup |
| `watch -n 2 <cmd>` | Repeat a command every 2 seconds |

---

## Disk & Storage

| Command | Description |
|---------|-------------|
| `df -h` | Disk usage per partition |
| `du -sh <dir>` | Size of a directory |
| `du -sh *` | Size of all items here |
| `du -sh * \| sort -h` | Sorted by size |
| `lsblk` | List block devices |
| `mount` | List mounted filesystems |
| `mount /dev/sdb1 /mnt` | Mount a partition |
| `umount /mnt` | Unmount |

---

## Text Processing

| Command | Description |
|---------|-------------|
| `sort <file>` | Sort lines |
| `sort -n <file>` | Numeric sort |
| `sort -rh <file>` | Reverse human-readable sort |
| `sort -u <file>` | Sort and deduplicate |
| `uniq <file>` | Remove consecutive duplicates |
| `uniq -c <file>` | Count occurrences |
| `cut -d',' -f1 <file>` | Extract field 1 (CSV) |
| `cut -c1-10 <file>` | Extract characters 1–10 |
| `awk '{print $2}' <file>` | Print column 2 |
| `awk -F',' '{print $1}'` | Comma-separated column 1 |
| `sed 's/foo/bar/g' <file>` | Replace all occurrences |
| `sed -i 's/foo/bar/g' <file>` | Replace in-place |
| `tr 'a-z' 'A-Z'` | Convert to uppercase |
| `xargs` | Build and run commands from stdin |

---

## Redirections & Pipes

| Syntax | Description |
|--------|-------------|
| `cmd > file` | Redirect stdout (overwrite) |
| `cmd >> file` | Redirect stdout (append) |
| `cmd 2> file` | Redirect stderr |
| `cmd &> file` | Redirect stdout and stderr |
| `cmd < file` | Use file as stdin |
| `cmd1 \| cmd2` | Pipe stdout to next command |
| `cmd \| tee file` | Pipe and also write to file |
| `cmd 2>&1` | Merge stderr into stdout |
| `cmd > /dev/null` | Discard stdout |
| `cmd &> /dev/null` | Discard everything |

---

## Archives

| Command | Description |
|---------|-------------|
| `tar -czf out.tar.gz <dir>` | Create gzip archive |
| `tar -xzf archive.tar.gz` | Extract gzip archive |
| `tar -xzf archive.tar.gz -C <dir>` | Extract to a specific folder |
| `tar -tzf archive.tar.gz` | List contents |
| `tar -cjf out.tar.bz2 <dir>` | Create bzip2 archive |
| `zip -r out.zip <dir>` | Create zip |
| `unzip archive.zip` | Extract zip |
| `unzip -l archive.zip` | List zip contents |

---

## Networking

| Command | Description |
|---------|-------------|
| `ping <host>` | Test connectivity |
| `ip a` | Show interfaces and IPs |
| `ip r` | Show routing table |
| `ss -tuln` | Listening ports |
| `ss -tulnp` | Listening ports with process names |
| `curl <url>` | Fetch a URL |
| `curl -o file <url>` | Save to file |
| `curl -I <url>` | Headers only |
| `curl -X POST -d "data" <url>` | POST request |
| `curl -H "Auth: token" <url>` | Custom header |
| `wget <url>` | Download a file |
| `wget -c <url>` | Resume interrupted download |
| `ssh user@host` | Connect to remote |
| `ssh -p 2222 user@host` | Custom port |
| `scp file user@host:/path` | Copy file to remote |
| `rsync -avz <src> user@host:<dst>` | Sync files to remote |
| `nc -zv <host> <port>` | Check if a port is open |

---

## Users & Permissions

| Command | Description |
|---------|-------------|
| `whoami` | Current user |
| `id` | UID, GID and groups |
| `who` | Who is logged in |
| `sudo <cmd>` | Run as root |
| `sudo -i` | Open root shell |
| `su <user>` | Switch user |
| `passwd` | Change your password |
| `useradd -m <user>` | Create user with home dir |
| `userdel -r <user>` | Delete user and home dir |
| `usermod -aG <group> <user>` | Add user to a group |
| `groupadd <group>` | Create a group |
| `groups <user>` | List user's groups |

---

## Systemd

| Command | Description |
|---------|-------------|
| `systemctl status <svc>` | Service status |
| `systemctl start <svc>` | Start |
| `systemctl stop <svc>` | Stop |
| `systemctl restart <svc>` | Restart |
| `systemctl enable <svc>` | Start at boot |
| `systemctl disable <svc>` | Don't start at boot |
| `systemctl enable --now <svc>` | Enable and start now |
| `systemctl list-units --type=service` | All active services |
| `journalctl -u <svc>` | Service logs |
| `journalctl -u <svc> -f` | Follow service logs |
| `journalctl -xe` | Recent logs with context |

---

## SSH

| Command | Description |
|---------|-------------|
| `ssh user@host` | Connect |
| `ssh -p <port> user@host` | Custom port |
| `ssh -i <key> user@host` | Specific key |
| `ssh-keygen -t ed25519` | Generate key pair |
| `ssh-copy-id user@host` | Copy public key to server |
| `ssh -L 8080:localhost:80 user@host` | Local port forward |
| `ssh -N -D 1080 user@host` | SOCKS proxy |

---

## Environment & Shell

| Command | Description |
|---------|-------------|
| `echo $VAR` | Print a variable |
| `export VAR=value` | Set for session and subprocesses |
| `unset VAR` | Remove a variable |
| `env` | List all environment variables |
| `alias ll='ls -la'` | Create a shortcut |
| `history` | Command history |
| `!!` | Repeat last command |
| `!<n>` | Repeat command n from history |
| `Ctrl+R` | Search command history |
| `source ~/.bashrc` | Reload shell config |
