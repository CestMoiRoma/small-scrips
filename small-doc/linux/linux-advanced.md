# Linux Advanced

---

## Systemd

Manages services, boot targets, and logs on most modern distros.

```bash
systemctl status <service>         # show service status
systemctl start <service>          # start
systemctl stop <service>           # stop
systemctl restart <service>        # restart
systemctl reload <service>         # reload config without restarting
systemctl enable <service>         # start at boot
systemctl disable <service>        # don't start at boot
systemctl enable --now <service>   # enable and start immediately

systemctl list-units --type=service         # all active services
systemctl list-units --type=service --all   # including inactive
```

### Logs with journalctl

```bash
journalctl -u <service>            # logs for a specific service
journalctl -u <service> -f         # follow in real time
journalctl -u <service> --since "1 hour ago"
journalctl -xe                     # last logs with context (good for errors)
journalctl --disk-usage            # how much space logs take
journalctl --vacuum-size=200M      # trim logs to 200 MB
```

---

## SSH keys

```bash
ssh-keygen -t ed25519 -C "comment"     # generate a key pair (preferred algorithm)
ssh-keygen -t rsa -b 4096              # RSA alternative

# Copy your public key to a remote server
ssh-copy-id user@host
# or manually:
cat ~/.ssh/id_ed25519.pub | ssh user@host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"

# Test connection
ssh -T git@github.com
```

### SSH config (`~/.ssh/config`)

Avoid typing full connection strings every time:

```
Host myserver
    HostName 192.168.1.10
    User john
    Port 2222
    IdentityFile ~/.ssh/id_ed25519

Host github
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_github
```

Then just: `ssh myserver`

---

## Cron jobs

Schedule recurring commands. Edit with `crontab -e`.

```
# ┌─ minute (0-59)
# │ ┌─ hour (0-23)
# │ │ ┌─ day of month (1-31)
# │ │ │ ┌─ month (1-12)
# │ │ │ │ ┌─ day of week (0=Sun, 6=Sat)
# │ │ │ │ │
# * * * * *  command

0 3 * * *    /home/user/backup.sh      # every day at 03:00
*/15 * * * * curl https://example.com  # every 15 minutes
0 9 * * 1    echo "Monday morning"     # every Monday at 09:00
```

```bash
crontab -e         # edit your crontab
crontab -l         # list your crontab
crontab -r         # remove your crontab
```

---

## Process management

```bash
nice -n 10 <cmd>           # start a command with lower priority (-20 high → 19 low)
renice 10 -p <PID>         # change priority of a running process

nohup <cmd> &              # run immune to hangup, output → nohup.out
disown %1                  # detach a running job from the shell

# Signals
kill -SIGTERM <PID>        # graceful stop (default)
kill -SIGKILL <PID>        # force kill
kill -SIGHUP  <PID>        # reload config (for daemons)
kill -SIGUSR1 <PID>        # user-defined signal 1

# List all signals
kill -l
```

---

## Screen & Tmux

Keep sessions alive after disconnect.

```bash
# Screen
screen                     # new session
screen -S <name>           # new named session
screen -ls                 # list sessions
screen -r <name>           # reattach
# Inside screen: Ctrl+A then D to detach

# Tmux
tmux                       # new session
tmux new -s <name>         # new named session
tmux ls                    # list sessions
tmux attach -t <name>      # reattach
# Inside tmux: Ctrl+B then D to detach
```

---

## Users & Groups

```bash
useradd -m <user>              # create user with home directory
useradd -m -s /bin/bash <user> # specify shell
passwd <user>                  # set password
userdel -r <user>              # delete user and home directory

groupadd <group>               # create group
groupdel <group>               # delete group
usermod -aG <group> <user>     # add user to group (append)
gpasswd -d <user> <group>      # remove user from group

id <user>                      # show user's UID, GID, groups
groups <user>                  # list groups of a user
cat /etc/passwd                # all users
cat /etc/group                 # all groups
```

---

## Networking

```bash
ip a                           # show interfaces and IPs
ip r                           # show routing table
ip link set <iface> up/down    # enable or disable interface

ss -tuln                       # listening TCP/UDP ports
ss -tulnp                      # include process names

# Firewall (ufw — Debian/Ubuntu)
ufw status
ufw enable
ufw allow 22
ufw allow 80/tcp
ufw deny 3306
ufw delete allow 80/tcp

# Firewall (firewalld — RHEL/Fedora)
firewall-cmd --list-all
firewall-cmd --add-port=80/tcp --permanent
firewall-cmd --reload
```

---

## Filesystem

```bash
lsblk                          # list block devices
fdisk -l                       # list disks and partitions (as root)
blkid                          # show UUIDs of partitions

mount /dev/sdb1 /mnt/data      # mount a partition
umount /mnt/data               # unmount
mount -a                       # mount everything in /etc/fstab

df -h                          # disk space per partition
du -sh <dir>                   # size of a directory

# /etc/fstab — persistent mounts
UUID=xxxx  /mnt/data  ext4  defaults  0  2
```

---

## Bash scripting essentials

```bash
#!/bin/bash               # shebang — always first line

# Variables
NAME="world"
echo "Hello, $NAME"

# Reading input
read -p "Enter name: " NAME

# Conditionals
if [ "$NAME" = "root" ]; then
    echo "You are root"
elif [ -f "$NAME" ]; then
    echo "$NAME is a file"
else
    echo "Unknown"
fi

# Loops
for i in 1 2 3; do echo $i; done
for file in *.txt; do echo "$file"; done
while [ $i -lt 10 ]; do ((i++)); done

# Functions
greet() {
    echo "Hello, $1"
}
greet "Alice"

# Exit codes
command && echo "success" || echo "failed"
exit 0        # success
exit 1        # error
```

### Useful test flags (`[ ]`)

| Flag | Meaning |
|------|---------|
| `-f <file>` | File exists and is a regular file |
| `-d <dir>` | Directory exists |
| `-e <path>` | Path exists (any type) |
| `-z "$VAR"` | Variable is empty |
| `-n "$VAR"` | Variable is not empty |
| `-r / -w / -x` | File is readable / writable / executable |

---

## File descriptors & advanced redirections

```bash
cmd 2>&1            # merge stderr into stdout
cmd > /dev/null     # discard stdout
cmd &> /dev/null    # discard everything
cmd 2>/dev/null     # suppress errors only

# Process substitution
diff <(cmd1) <(cmd2)    # compare outputs of two commands

# Here-doc
cat <<EOF
line 1
line 2
EOF
```

---

## Useful one-liners

```bash
# Count occurrences of each line
sort file.txt | uniq -c | sort -rn

# Find the 10 largest files
du -ah / 2>/dev/null | sort -rh | head -10

# Show open ports with their process
ss -tulnp

# Watch a command every 2 seconds
watch -n 2 df -h

# Monitor a log file and filter
tail -f /var/log/syslog | grep -i error

# Replace a string across multiple files
grep -rl "old" . | xargs sed -i 's/old/new/g'

# Run a command on each line from a file
cat hosts.txt | xargs -I{} ssh {} "uptime"

# Check if a port is open
nc -zv <host> <port>

# Generate a random string
openssl rand -hex 16
```
