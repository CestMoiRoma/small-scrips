# Git Flags Reference

All the notable `--` flags, organized by command.

---

## git push

| Flag | Effect |
|------|--------|
| `--force` | Overwrite the remote branch unconditionally. Dangerous on shared branches. |
| `--force-with-lease` | Force push only if the remote tip matches your last fetch. Safe alternative to `--force`. |
| `--force-if-includes` | Extra safety on top of `--force-with-lease` — requires remote commits to be in your local reflog. Git 2.30+. |
| `--all` | Push all local branches. |
| `--tags` | Push all tags (not pushed by default). |
| `--follow-tags` | Push only annotated tags reachable from pushed commits. |
| `--delete` | Delete a remote branch or tag: `git push --delete origin <name>`. |
| `--set-upstream` / `-u` | Track the remote branch: future `git push/pull` need no arguments. |
| `--dry-run` | Simulate the push without actually sending anything. |

---

## git fetch

| Flag | Effect |
|------|--------|
| `--all` | Fetch from all remotes, not just `origin`. |
| `--prune` | Remove local references to remote branches that no longer exist. |
| `--tags` | Fetch all tags even if the commits they point to aren't fetched. |
| `--dry-run` | Show what would be fetched without doing it. |

---

## git pull

| Flag | Effect |
|------|--------|
| `--rebase` | Rebase local commits on top of fetched changes instead of merging. |
| `--no-rebase` | Force a merge even if `pull.rebase` is set to true in config. |
| `--ff-only` | Abort if a fast-forward is not possible (no merge commit created). |
| `--all` | Fetch from all remotes before merging/rebasing. |
| `--no-commit` | Merge but don't auto-commit the result. |

---

## git commit

| Flag | Effect |
|------|--------|
| `--amend` | Rewrite the last commit (message and/or content). |
| `--no-edit` | Amend without changing the commit message. |
| `--allow-empty` | Create a commit even if nothing is staged. |
| `--verbose` / `-v` | Show the diff in the editor when writing the message. |
| `--dry-run` | Show what would be committed without committing. |
| `--no-verify` | Skip pre-commit and commit-msg hooks. |

---

## git add

| Flag | Effect |
|------|--------|
| `--all` / `-A` | Stage all changes (new, modified, deleted). |
| `--update` / `-u` | Stage only modified and deleted files, not new ones. |
| `--patch` / `-p` | Interactively choose which hunks to stage. |

---

## git diff

| Flag | Effect |
|------|--------|
| `--staged` / `--cached` | Show changes staged for the next commit. |
| `--stat` | Show a summary (files changed, insertions, deletions) instead of the full diff. |
| `--name-only` | Show only the names of changed files. |
| `--word-diff` | Highlight changed words inline instead of whole lines. |

---

## git log

| Flag | Effect |
|------|--------|
| `--oneline` | One line per commit (short hash + message). |
| `--graph` | Draw an ASCII branch graph on the left. |
| `--decorate` | Show branch and tag names next to commits. |
| `--all` | Include all branches and tags, not just the current branch. |
| `--stat` | Show file change stats below each commit. |
| `--patch` / `-p` | Show the full diff for each commit. |
| `--follow` | Follow renames when showing history of a single file. |
| `--no-merges` | Exclude merge commits. |
| `--grep=<text>` | Filter commits whose message matches the text. |
| `--author=<name>` | Filter commits by author. |
| `--since=<date>` | Show commits after a date: `--since="2 weeks ago"`. |
| `--until=<date>` | Show commits before a date. |
| `-S <string>` | Find commits that added or removed a specific string (pickaxe). |

---

## git reset

| Flag | Effect |
|------|--------|
| `--soft` | Move HEAD back, keep changes staged. |
| `--mixed` | Move HEAD back, unstage changes (default). |
| `--hard` | Move HEAD back, discard all changes. Irreversible without reflog. |

---

## git merge

| Flag | Effect |
|------|--------|
| `--no-ff` | Always create a merge commit, even if fast-forward is possible. |
| `--ff-only` | Abort if a fast-forward is not possible. |
| `--squash` | Squash all incoming commits into one staged change (you still commit manually). |
| `--no-commit` | Perform the merge but stop before committing. |
| `--abort` | Cancel a merge in progress and restore the previous state. |

---

## git rebase

| Flag | Effect |
|------|--------|
| `--interactive` / `-i` | Open the rebase editor to reorder, squash, drop commits. |
| `--onto <newbase>` | Transplant a branch onto a different base. |
| `--autosquash` | Automatically apply `fixup!` / `squash!` commit messages when used with `-i`. |
| `--autostash` | Stash uncommitted changes before rebasing, reapply after. |
| `--abort` | Cancel the rebase and return to the original branch state. |
| `--continue` | Resume after resolving a conflict. |
| `--skip` | Skip the current conflicting commit and continue. |

---

## git stash

| Flag | Effect |
|------|--------|
| `--include-untracked` / `-u` | Also stash untracked files. |
| `--all` / `-a` | Stash everything including ignored files. |
| `--keep-index` | Stash working tree changes but leave the staging area untouched. |
| `--patch` / `-p` | Interactively choose which changes to stash. |

---

## git clone

| Flag | Effect |
|------|--------|
| `--recurse-submodules` | Initialise and clone submodules automatically. |
| `--depth <n>` | Shallow clone — only fetch the last `n` commits. Faster for large repos. |
| `--branch <name>` | Clone and check out a specific branch instead of the default. |
| `--single-branch` | Only fetch history for the cloned branch (use with `--branch`). |
| `--bare` | Clone without a working tree — just the `.git` contents. Used for servers/mirrors. |
| `--mirror` | Like `--bare` but also tracks all remote refs. |

---

## git branch

| Flag | Effect |
|------|--------|
| `--all` / `-a` | List local and remote branches. |
| `--remotes` / `-r` | List remote-tracking branches only. |
| `--merged` | List branches already merged into the current one. |
| `--no-merged` | List branches not yet merged. |
| `--move` / `-m` | Rename a branch: `git branch -m <old> <new>`. |
| `--delete` / `-d` | Delete a merged branch (safe). |
| `--set-upstream-to` | Change which remote branch this branch tracks. |

---

## git clean

| Flag | Effect |
|------|--------|
| `--dry-run` / `-n` | Show what would be deleted without deleting. |
| `--force` / `-f` | Required to actually delete (safety measure). |
| `--directories` / `-d` | Also remove untracked directories. |
| `--ignored` / `-x` | Also remove files ignored by `.gitignore`. |

---

## git cherry-pick

| Flag | Effect |
|------|--------|
| `--no-commit` / `-n` | Apply changes without creating a commit. |
| `--edit` / `-e` | Edit the commit message before committing. |
| `--abort` | Cancel and restore the pre-cherry-pick state. |
| `--continue` | Resume after resolving a conflict. |

---

## git tag

| Flag | Effect |
|------|--------|
| `--annotate` / `-a` | Create an annotated tag (stores tagger, date, message). Preferred over lightweight tags. |
| `--message` / `-m` | Set the tag message inline. |
| `--delete` / `-d` | Delete a local tag. |
| `--list` / `-l` | List tags, supports glob patterns: `git tag -l "v1.*"`. |
| `--force` / `-f` | Move an existing tag to a new commit. |
