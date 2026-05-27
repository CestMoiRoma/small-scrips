# Git Advanced

---

## Fork workflow

A fork is your personal copy of someone else's repo on GitHub/GitLab. You push to your fork, then open a Pull Request to the original.

```bash
# 1. Fork on GitHub (UI), then clone your fork
git clone https://github.com/you/repo.git
cd repo

# 2. Add the original repo as a second remote named "upstream"
git remote add upstream https://github.com/original/repo.git

# 3. Verify
git remote -v
# origin    https://github.com/you/repo.git
# upstream  https://github.com/original/repo.git
```

### Keeping your fork up to date

```bash
git fetch upstream                 # download upstream changes
git switch main
git merge upstream/main            # bring your local main up to date
git push origin main               # sync your fork on GitHub
```

> Always branch off an up-to-date `main` before starting work.

---

## Interactive rebase

Rewrite, reorder, squash, or drop commits before sharing them.

```bash
git rebase -i HEAD~3               # edit the last 3 commits
git rebase -i <commit-hash>        # edit everything after that commit
```

Inside the editor, replace `pick` with one of:

| Command | Effect |
|---------|--------|
| `pick` | Keep the commit as-is |
| `reword` | Keep but edit the commit message |
| `edit` | Pause to amend the commit itself |
| `squash` | Merge into the previous commit, combine messages |
| `fixup` | Merge into the previous commit, discard this message |
| `drop` | Delete the commit entirely |

> Never rebase commits already pushed to a shared branch.

---

## Cherry-pick

Apply a specific commit from another branch onto the current one.

```bash
git cherry-pick <commit-hash>              # apply one commit
git cherry-pick <hash1> <hash2>            # apply several
git cherry-pick <hash1>..<hash2>           # apply a range
git cherry-pick <hash> --no-commit         # apply changes without committing
```

---

## Reflog

A local safety net — records every movement of HEAD, even after resets and rebases.

```bash
git reflog                         # full history of HEAD positions
git reflog show <branch>           # history for a specific branch
```

Recover a commit that seems lost:
```bash
git reflog                         # find the hash you want
git switch -c recovery-branch <hash>   # restore it on a new branch
```

> Reflog entries expire after 90 days by default.

---

## Bisect

Binary-search through history to find the commit that introduced a bug.

```bash
git bisect start
git bisect bad                     # current commit is broken
git bisect good <hash>             # last known good commit

# Git checks out a midpoint — test it, then:
git bisect good                    # or: git bisect bad

# Repeat until Git identifies the culprit commit.
git bisect reset                   # exit bisect and return to HEAD
```

---

## Worktrees

Check out multiple branches at the same time in separate folders — no stashing needed.

```bash
git worktree add ../hotfix hotfix-branch    # new folder checked out to that branch
git worktree list
git worktree remove ../hotfix               # clean up when done
```

---

## Submodules

Embed another repo inside yours at a fixed commit.

```bash
git submodule add <url> <path>     # add a submodule
git submodule update --init        # initialise after a fresh clone
git submodule update --remote      # pull latest from the submodule's remote

# Clone a repo that has submodules
git clone --recurse-submodules <url>
```

---

## Useful rebase flags

```bash
git pull --rebase                  # rebase instead of merge when pulling
git rebase --onto <newbase> <oldbase> <branch>   # transplant a branch
git rebase --abort                 # bail out of a conflicted rebase
git rebase --continue              # continue after resolving a conflict
```

---

## force-with-lease vs force

`--force` overwrites the remote branch unconditionally — if a teammate pushed while you were rebasing, their commits are silently erased.

`--force-with-lease` checks that the remote tip is still where you last saw it. If someone pushed in the meantime, the push is rejected and you have to `git fetch` first.

```bash
git push --force               # ❌ dangerous — blindly overwrites remote
git push --force-with-lease    # ✅ safe — fails if remote changed since your last fetch
```

**Typical use case** — you just rebased or amended commits that were already pushed:

```bash
git rebase -i HEAD~3           # rewrite local history
git push --force-with-lease    # update remote safely
```

**Edge case** — `--force-with-lease` can still be dangerous if you ran `git fetch` just before pushing without looking at what came in. The lease only checks the ref you fetched, not whether you reviewed the changes. For extra safety some teams use `--force-if-includes` (Git 2.30+) which additionally requires the remote's new commits to be present in your local reflog:

```bash
git push --force-with-lease --force-if-includes
```

---

## Aliases

Add shortcuts to `~/.gitconfig`:

```ini
[alias]
  st  = status
  co  = switch
  lg  = log --oneline --graph --decorate --all
  undo = reset HEAD~1
  pushf = push --force-with-lease
```

Or from the terminal:
```bash
git config --global alias.lg "log --oneline --graph --decorate --all"
```

---

## Clean

Remove untracked files and folders.

```bash
git clean -n                       # dry run — shows what would be deleted
git clean -fd                      # delete untracked files and folders
git clean -fdx                     # also delete ignored files (.env, build artefacts…)
```

---

## Useful one-liners

```bash
# Show all branches (local + remote)
git branch -a

# Compare two branches
git diff main..feature-branch

# See which branches are merged into main
git branch --merged main

# Move the last commit to a new branch (if you committed on the wrong one)
git switch -c new-branch
git switch main
git reset --hard HEAD~1

# Search commit messages
git log --grep="login"

# Find which commit introduced a specific string
git log -S "functionName" --oneline
```
