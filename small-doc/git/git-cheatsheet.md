# Git — Quick Cheat Sheet

---

## Setup

| Command | Description |
|---------|-------------|
| `git config --global user.name "Name"` | Set your name |
| `git config --global user.email "x@x.com"` | Set your email |
| `git config --global alias.<name> "<cmd>"` | Create a shortcut |
| `git config --list` | Show all config values |

---

## Repository

| Command | Description |
|---------|-------------|
| `git init` | Init a repo in the current folder |
| `git clone <url>` | Clone a remote repo |
| `git clone --depth <n> <url>` | Shallow clone (last n commits only) |
| `git clone --recurse-submodules <url>` | Clone and init submodules |
| `git clone --branch <name> <url>` | Clone a specific branch |
| `git clone --single-branch <url>` | Clone only the default branch history |

---

## Status & Diff

| Command | Description |
|---------|-------------|
| `git status` | Show working tree state |
| `git diff` | Unstaged changes |
| `git diff --staged` | Staged changes |
| `git diff --stat` | Summary of changes (no line detail) |
| `git diff --name-only` | Only filenames |
| `git diff --word-diff` | Inline word-level diff |
| `git diff <branch1>..<branch2>` | Compare two branches |

---

## Staging

| Command | Description |
|---------|-------------|
| `git add <file>` | Stage a file |
| `git add .` | Stage all changes |
| `git add -A` | Stage new, modified and deleted files |
| `git add -u` | Stage modified and deleted only (no new files) |
| `git add -p` | Stage interactively, hunk by hunk |
| `git restore --staged <file>` | Unstage a file |
| `git rm --cached <file>` | Stop tracking a file without deleting it |

---

## Commit

| Command | Description |
|---------|-------------|
| `git commit -m "msg"` | Commit with a message |
| `git commit --amend` | Rewrite the last commit |
| `git commit --amend --no-edit` | Amend without changing the message |
| `git commit --allow-empty -m "msg"` | Commit with nothing staged |
| `git commit -v` | Show the diff inside the commit editor |
| `git commit --no-verify` | Skip pre-commit hooks |
| `git commit --dry-run` | Preview what would be committed |

---

## Branches

| Command | Description |
|---------|-------------|
| `git branch` | List local branches |
| `git branch -a` | List local and remote branches |
| `git branch -r` | List remote-tracking branches |
| `git branch <name>` | Create a branch |
| `git branch -m <old> <new>` | Rename a branch |
| `git branch -d <name>` | Delete a merged branch |
| `git branch -D <name>` | Force-delete a branch |
| `git branch --merged` | Branches already merged into current |
| `git branch --no-merged` | Branches not yet merged |
| `git switch <name>` | Switch to a branch |
| `git switch -c <name>` | Create and switch in one step |
| `git switch -c <name> --orphan` | New branch with no history |

---

## Merge & Rebase

| Command | Description |
|---------|-------------|
| `git merge <branch>` | Merge a branch into current |
| `git merge --no-ff <branch>` | Always create a merge commit |
| `git merge --ff-only <branch>` | Abort if not fast-forwardable |
| `git merge --squash <branch>` | Collapse all commits into one staged change |
| `git merge --no-commit <branch>` | Merge without auto-committing |
| `git merge --abort` | Cancel a merge in progress |
| `git rebase <branch>` | Rebase current branch on top of another |
| `git rebase -i HEAD~<n>` | Interactive rebase on last n commits |
| `git rebase --onto <new> <old>` | Transplant a branch onto a new base |
| `git rebase --autosquash` | Auto-apply fixup!/squash! commits |
| `git rebase --autostash` | Stash before rebase, reapply after |
| `git rebase --abort` | Cancel the rebase |
| `git rebase --continue` | Resume after fixing a conflict |
| `git rebase --skip` | Skip current conflicting commit |

---

## Remote

| Command | Description |
|---------|-------------|
| `git remote -v` | List remotes |
| `git remote add <name> <url>` | Add a remote |
| `git remote remove <name>` | Remove a remote |
| `git remote rename <old> <new>` | Rename a remote |
| `git fetch` | Download changes, don't apply |
| `git fetch --all` | Fetch from all remotes |
| `git fetch --prune` | Remove stale remote-tracking refs |
| `git pull` | Fetch and merge |
| `git pull --rebase` | Fetch and rebase instead of merge |
| `git pull --ff-only` | Abort if not fast-forwardable |
| `git push` | Push current branch |
| `git push -u origin <name>` | Push and track remote branch |
| `git push --all` | Push all branches |
| `git push --tags` | Push all tags |
| `git push --follow-tags` | Push annotated tags reachable from push |
| `git push --delete origin <name>` | Delete a remote branch or tag |
| `git push --force` | Force push (dangerous) |
| `git push --force-with-lease` | Force push only if remote hasn't changed |
| `git push --force-with-lease --force-if-includes` | Safest force push (Git 2.30+) |
| `git push --dry-run` | Simulate a push without sending |

---

## Log & History

| Command | Description |
|---------|-------------|
| `git log` | Full commit history |
| `git log --oneline` | One line per commit |
| `git log --oneline --graph --all` | Visual branch graph |
| `git log --stat` | Show file change stats per commit |
| `git log -p` | Show full diff per commit |
| `git log --follow <file>` | History of a file across renames |
| `git log --no-merges` | Exclude merge commits |
| `git log --grep="<text>"` | Filter by commit message |
| `git log --author="<name>"` | Filter by author |
| `git log --since="<date>"` | Commits after a date |
| `git log --until="<date>"` | Commits before a date |
| `git log -S "<string>"` | Commits that added/removed a string |
| `git show <commit>` | Full details of a commit |
| `git blame <file>` | Who last changed each line |
| `git shortlog -sn` | Commit count per author |

---

## Undo

| Command | Description |
|---------|-------------|
| `git restore <file>` | Discard unstaged changes in a file |
| `git restore --staged <file>` | Unstage a file |
| `git reset --soft HEAD~1` | Undo last commit, keep changes staged |
| `git reset HEAD~1` | Undo last commit, unstage changes |
| `git reset --hard HEAD~1` | Undo last commit, discard all changes |
| `git revert <commit>` | New commit that undoes a previous one |
| `git revert --no-commit <commit>` | Revert without committing |
| `git reflog` | Full history of HEAD positions |

---

## Stash

| Command | Description |
|---------|-------------|
| `git stash` | Shelve current changes |
| `git stash -u` | Also stash untracked files |
| `git stash -a` | Stash everything incl. ignored files |
| `git stash --keep-index` | Stash working tree, leave staging alone |
| `git stash -p` | Interactively choose what to stash |
| `git stash pop` | Restore last stash and drop it |
| `git stash apply` | Restore last stash, keep it in list |
| `git stash list` | List all stashes |
| `git stash drop` | Delete the latest stash |
| `git stash clear` | Delete all stashes |

---

## Tags

| Command | Description |
|---------|-------------|
| `git tag <name>` | Create a lightweight tag |
| `git tag -a <name> -m "msg"` | Create an annotated tag (preferred) |
| `git tag -f <name>` | Move a tag to the current commit |
| `git tag -d <name>` | Delete a local tag |
| `git tag -l "v1.*"` | List tags matching a pattern |
| `git push origin <name>` | Push a single tag |
| `git push origin --tags` | Push all tags |
| `git push --delete origin <name>` | Delete a remote tag |

---

## Cherry-pick

| Command | Description |
|---------|-------------|
| `git cherry-pick <hash>` | Apply a commit onto current branch |
| `git cherry-pick <h1> <h2>` | Apply multiple commits |
| `git cherry-pick <h1>..<h2>` | Apply a range of commits |
| `git cherry-pick -n <hash>` | Apply without committing |
| `git cherry-pick -e <hash>` | Apply and edit the commit message |
| `git cherry-pick --abort` | Cancel in-progress cherry-pick |
| `git cherry-pick --continue` | Resume after resolving conflict |

---

## Advanced

| Command | Description |
|---------|-------------|
| `git bisect start` | Start binary search for a bad commit |
| `git bisect good <hash>` | Mark a commit as good |
| `git bisect bad` | Mark current commit as bad |
| `git bisect reset` | Exit bisect mode |
| `git worktree add <path> <branch>` | Check out a branch in a separate folder |
| `git worktree list` | List all worktrees |
| `git worktree remove <path>` | Remove a worktree |
| `git submodule add <url> <path>` | Add a submodule |
| `git submodule update --init` | Init submodules after clone |
| `git submodule update --remote` | Pull latest in all submodules |
| `git clean -n` | Preview untracked files to delete |
| `git clean -fd` | Delete untracked files and folders |
| `git clean -fdx` | Also delete ignored files |
