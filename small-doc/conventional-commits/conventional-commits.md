# Conventional Commits

Format: `type(scope): message` — scope is optional.

| Type | When to use | Example |
|------|-------------|---------|
| `feat` | Adding a new feature for the user | `feat(auth): add fingerprint login` |
| `fix` | Fixing a bug or unexpected behaviour | `fix(cart): correct VAT calculation` |
| `docs` | Documentation changes only | `docs: update README` |
| `style` | Formatting changes with no logic impact (spaces, indentation…) | `style: fix missing semicolons` |
| `refactor` | Code restructuring that neither fixes a bug nor adds a feature | `refactor(ui): simplify button component` |
| `perf` | Performance improvements | `perf: optimise image loading time` |
| `test` | Adding or fixing tests | `test: add unit tests for cart` |
| `chore` | Maintenance, cleanup, dependency updates | `chore: remove temp files` |
| `build` | Changes to the build system or external dependencies | `build: upgrade npm version` |
| `ci` | CI configuration or script changes | `ci: update GitHub Actions workflow` |
| `revert` | Reverting a previous commit | `revert: feat(auth): add fingerprint login` |
