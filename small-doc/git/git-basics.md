# Git Basics

---

## Core concepts

| Concept | What it is |
|---------|------------|
| **Repository** | A folder tracked by Git. Contains your files + the full history in `.git/`. |
| **Working tree** | The files you actually see and edit. |
| **Staging area** | A buffer between your edits and a commit. You choose what goes in. |
| **Commit** | A snapshot of the staging area, saved permanently in history. |
| **Branch** | A movable pointer to a commit. `main` is just the default name. |
| **Remote** | A copy of the repo hosted elsewhere (GitHub, GitLab…). Typically named `origin`. |
| **HEAD** | Where you are right now — usually the tip of your current branch. |

---

## Setup

```bash
git config --global user.name  "Your Name"
git config --global user.email "you@example.com"
```

---

## Start a repo

```bash
git init                   # turn the current folder into a repo
git clone <url>            # download an existing repo
```

---

## Daily workflow

```bash
git status                 # see what changed
git diff                   # see exact line changes (unstaged)
git diff --staged          # see what's staged

git add <file>             # stage a file
git add .                  # stage everything
git add -p                 # stage interactively, chunk by chunk

git commit -m "message"    # commit what's staged
git commit --amend         # edit the last commit (before pushing)
```

---

## Branches

```bash
git branch                 # list local branches
git branch <name>          # create a branch
git switch <name>          # move to a branch
git switch -c <name>       # create and move in one step

git merge <name>           # merge a branch into the current one
git rebase <name>          # replay your commits on top of another branch

git branch -d <name>       # delete a branch (safe — checks it's merged)
git branch -D <name>       # force delete
```

---

## Remote

```bash
git remote -v              # list remotes
git remote add origin <url>

git fetch                  # download changes, don't apply them
git pull                   # fetch + merge (or rebase, depending on config)
git push                   # upload local commits
git push -u origin <name>  # push a new branch and track it
git push --force-with-lease # force push safely (fails if remote changed)
```

---

## History

```bash
git log                    # full history
git log --oneline          # compact view
git log --oneline --graph  # with branch graph

git show <commit>          # details of a commit
git blame <file>           # who wrote each line
```

---

## Undo things

| Situation | Command |
|-----------|---------|
| Discard unstaged changes in a file | `git restore <file>` |
| Unstage a file | `git restore --staged <file>` |
| Undo last commit, keep changes staged | `git reset --soft HEAD~1` |
| Undo last commit, keep changes unstaged | `git reset HEAD~1` |
| Undo last commit, discard all changes | `git reset --hard HEAD~1` |
| Revert a commit without rewriting history | `git revert <commit>` |

> **Rule of thumb:** use `revert` on shared branches, `reset` only on commits you haven't pushed yet.

---

## Stash

```bash
git stash                  # shelve current changes
git stash pop              # bring them back
git stash list             # see all stashes
git stash drop             # delete the latest stash
```

---

## Tags

```bash
git tag v1.0.0                        # lightweight tag
git tag -a v1.0.0 -m "First release"  # annotated tag (preferred)
git push origin v1.0.0                # push a tag
git push origin --tags                # push all tags
```

---

## .gitignore

Patterns to exclude files from tracking. Put the file at the root of the repo.

```
*.log          # all .log files
/dist/         # only the root dist/ folder
build/         # any build/ folder
.env           # exact filename
```

> Already-tracked files are **not** ignored retroactively. Use `git rm --cached <file>` to stop tracking a file without deleting it.
