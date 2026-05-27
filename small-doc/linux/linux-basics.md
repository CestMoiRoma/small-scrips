# Linux Basics

---

## Core concepts

| Concept | What it is |
|---------|------------|
| **Shell** | The program that interprets your commands. Usually `bash` or `zsh`. |
| **Terminal** | The window you type into. Talks to the shell. |
| **Root** | The superuser. Has unrestricted access to everything. UID = 0. |
| **sudo** | Run a single command as root without becoming root. |
| **Path** | Where the shell looks for executables: `echo $PATH`. |
| **stdin / stdout / stderr** | Standard input (0), output (1), error (2). Everything is a stream. |
| **Pipe `\|`** | Feed the output of one command into the input of another. |
| **Permissions** | Every file has read/write/execute bits for owner, group, others. |
| **Process** | A running program. Every process has a PID. |

---

## Navigation

```bash
pwd                    # current directory
cd <dir>               # change directory
cd ..                  # go up one level
cd ~                   # go to home directory
cd -                   # go to previous directory
ls                     # list files
ls -la                 # long format, show hidden files
ls -lh                 # human-readable sizes
tree                   # visual directory tree (install if missing)
```

---

## Files & Directories

```bash
touch <file>           # create empty file / update timestamp
mkdir <dir>            # create directory
mkdir -p a/b/c         # create nested directories
cp <src> <dst>         # copy file
cp -r <src> <dst>      # copy directory recursively
mv <src> <dst>         # move or rename
rm <file>              # delete file
rm -r <dir>            # delete directory recursively
rm -rf <dir>           # force delete, no prompt (careful!)
ln -s <target> <link>  # create symbolic link
```

---

## Viewing files

```bash
cat <file>             # print full file
less <file>            # scroll through file (q to quit)
head <file>            # first 10 lines
head -n 20 <file>      # first 20 lines
tail <file>            # last 10 lines
tail -f <file>         # follow in real time (logs)
tail -n 50 <file>      # last 50 lines
wc -l <file>           # count lines
```

---

## Search

```bash
grep "pattern" <file>          # search in a file
grep -r "pattern" <dir>        # search recursively
grep -i "pattern" <file>       # case-insensitive
grep -n "pattern" <file>       # show line numbers
grep -v "pattern" <file>       # invert match (exclude)
grep -l "pattern" <dir>        # only print filenames

find <dir> -name "*.py"        # find by name
find <dir> -type f             # files only
find <dir> -type d             # directories only
find <dir> -mtime -7           # modified in last 7 days
find <dir> -size +100M         # larger than 100MB
find <dir> -name "*.log" -delete  # find and delete

which <cmd>                    # path of an executable
whereis <cmd>                  # locations of binary, man, source
```

---

## Permissions

```bash
ls -l                  # view permissions

chmod 755 <file>       # rwxr-xr-x  (owner: all, group/others: read+exec)
chmod 644 <file>       # rw-r--r--  (owner: read+write, others: read)
chmod +x <file>        # add execute for everyone
chmod -R 755 <dir>     # apply recursively

chown user <file>           # change owner
chown user:group <file>     # change owner and group
chown -R user:group <dir>   # recursive
```

**Permission bits:**

| Number | Meaning |
|--------|---------|
| `7` | rwx — read, write, execute |
| `6` | rw- — read, write |
| `5` | r-x — read, execute |
| `4` | r-- — read only |
| `0` | --- — no permissions |

---

## Processes

```bash
ps aux                 # all running processes
top                    # live process viewer (q to quit)
htop                   # improved top (install if missing)

kill <PID>             # send SIGTERM (graceful stop)
kill -9 <PID>          # send SIGKILL (force stop)
pkill <name>           # kill by process name
killall <name>         # kill all processes with that name

jobs                   # list background jobs in shell
bg                     # resume a stopped job in background
fg                     # bring background job to foreground
<cmd> &                # run command in background
nohup <cmd> &          # run in background, keep after logout
```

---

## Disk & Storage

```bash
df -h                  # disk usage per partition (human-readable)
du -sh <dir>           # size of a directory
du -sh *               # size of all items in current dir
du -sh * | sort -h     # sorted by size

lsblk                  # list block devices
mount                  # list mounted filesystems
```

---

## Text processing

```bash
sort <file>                    # sort lines alphabetically
sort -n <file>                 # sort numerically
sort -r <file>                 # reverse sort
sort -u <file>                 # sort and remove duplicates

uniq <file>                    # remove consecutive duplicates
uniq -c <file>                 # prefix with occurrence count

cut -d',' -f1 <file>           # extract field 1 (CSV)
cut -c1-10 <file>              # extract characters 1-10

awk '{print $2}' <file>        # print second column
awk -F',' '{print $1}' <file>  # comma-separated, print col 1

sed 's/foo/bar/g' <file>       # replace all "foo" with "bar"
sed -i 's/foo/bar/g' <file>    # replace in-place

tr 'a-z' 'A-Z'                 # transform characters (uppercase)
```

---

## Redirections & Pipes

```bash
cmd > file             # redirect stdout to file (overwrite)
cmd >> file            # redirect stdout to file (append)
cmd 2> file            # redirect stderr to file
cmd &> file            # redirect both stdout and stderr
cmd < file             # use file as stdin
cmd1 | cmd2            # pipe stdout of cmd1 into cmd2
cmd1 | tee file        # pipe and also write to file
```

---

## Archives

```bash
tar -czf archive.tar.gz <dir>     # create gzip archive
tar -czf archive.tar.gz <dir> <file>  # multiple sources
tar -xzf archive.tar.gz           # extract gzip archive
tar -xzf archive.tar.gz -C <dir>  # extract to a specific folder
tar -tzf archive.tar.gz           # list contents without extracting

zip -r archive.zip <dir>          # create zip
unzip archive.zip                 # extract zip
unzip -l archive.zip              # list contents
```

---

## Networking

```bash
ping <host>                    # test connectivity
curl <url>                     # fetch a URL
curl -o file.html <url>        # save to file
curl -I <url>                  # headers only
wget <url>                     # download a file
wget -r <url>                  # download recursively

ssh user@host                  # connect to remote machine
ssh -p 2222 user@host          # custom port
scp file user@host:/path       # copy file to remote
scp user@host:/path file       # copy file from remote
rsync -avz <src> user@host:<dst>  # sync files to remote

ip a                           # show network interfaces and IPs
ss -tuln                       # listening ports
```

---

## Users

```bash
whoami                         # current user
id                             # UID, GID and groups
who                            # who is logged in
sudo <cmd>                     # run command as root
sudo -i                        # open root shell
su <user>                      # switch to another user
passwd                         # change your password
```

---

## Package management

```bash
# Debian / Ubuntu (apt)
apt update                     # refresh package index
apt upgrade                    # upgrade installed packages
apt install <pkg>              # install
apt remove <pkg>               # uninstall
apt search <name>              # search

# Red Hat / Fedora (dnf)
dnf update
dnf install <pkg>
dnf remove <pkg>

# Arch (pacman)
pacman -Syu                    # update everything
pacman -S <pkg>                # install
pacman -R <pkg>                # remove
pacman -Ss <name>              # search
```

---

## Environment variables

```bash
echo $HOME                     # print a variable
export MY_VAR=value            # set for current session and subprocesses
unset MY_VAR                   # remove a variable
env                            # list all environment variables
printenv <VAR>                 # print a specific variable
```

Add to `~/.bashrc` or `~/.zshrc` for persistence:
```bash
export MY_VAR=value
```
