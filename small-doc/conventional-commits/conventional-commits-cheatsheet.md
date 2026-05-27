# Conventional Commits — Quick Cheat Sheet

Format: `type(scope): message` — scope is optional.

| Type | Use when | Example |
|------|----------|---------|
| `feat` | Adding a new feature | `feat(auth): add fingerprint login` |
| `fix` | Fixing a bug | `fix(cart): correct VAT calculation` |
| `docs` | Documentation only | `docs: update README` |
| `style` | Formatting, no logic change | `style: fix missing semicolons` |
| `refactor` | Restructuring, no bug fix or feature | `refactor(ui): simplify button component` |
| `perf` | Performance improvement | `perf: optimise image loading` |
| `test` | Adding or fixing tests | `test: add unit tests for cart` |
| `chore` | Maintenance, deps, cleanup | `chore: remove temp files` |
| `build` | Build system or external deps | `build: upgrade npm version` |
| `ci` | CI config or scripts | `ci: update GitHub Actions workflow` |
| `revert` | Reverting a previous commit | `revert: feat(auth): add fingerprint login` |

---

## Breaking changes

Add `!` after the type, or add a `BREAKING CHANGE:` footer.

```
feat!: drop support for Node 14

feat(api)!: rename /users endpoint to /accounts

feat(auth): add OAuth

BREAKING CHANGE: removed password-based login
```

---

## Rules

| Rule | Detail |
|------|--------|
| Message case | Lowercase, no capital letter at start |
| No period | Don't end the subject line with `.` |
| Imperative mood | "add feature" not "added feature" |
| Max length | Keep the subject under 72 characters |
| Scope | Optional, lowercase, describes the affected area |
| Body | Add after a blank line for longer explanations |
| Footer | `BREAKING CHANGE:`, `Closes #123`, `Refs #456` |
