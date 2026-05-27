# Python & pip Flags Reference

---

## python / python3

| Flag | Effect |
|------|--------|
| `-c "<code>"` | Run a string of code: `python -c "print(42)"` |
| `-m <module>` | Run a module as a script: `python -m http.server` |
| `-i` | Inspect — drop into interactive shell after running script |
| `-u` | Unbuffered stdout/stderr (useful in Docker / CI logs) |
| `-v` | Verbose imports — print each module as it is loaded |
| `-vv` | Even more verbose |
| `-W <filter>` | Warning filter: `-W ignore`, `-W error` |
| `-O` | Optimize — strip assertions and `__debug__` blocks |
| `-OO` | Also strip docstrings |
| `-B` | Don't write `.pyc` files |
| `-S` | Skip importing the `site` module (no `site-packages`) |
| `-E` | Ignore all `PYTHON*` environment variables |
| `-I` | Isolated mode — `-E` + `-S` + no user site |
| `-x` | Skip the first line of the script (for scripts with a non-Python header) |
| `--version` / `-V` | Print Python version |
| `--check-hash-based-pycs` | Check `.pyc` hash validity |

### Useful `-m` modules

| Command | Description |
|---------|-------------|
| `python -m http.server 8080` | Serve current directory over HTTP |
| `python -m json.tool file.json` | Pretty-print JSON |
| `python -m venv .venv` | Create a virtual environment |
| `python -m pip install <pkg>` | Run pip safely (always the right pip) |
| `python -m pytest` | Run tests |
| `python -m pdb script.py` | Run with the debugger |
| `python -m cProfile script.py` | Profile a script |
| `python -m timeit "expr"` | Time a small expression |
| `python -m py_compile file.py` | Check syntax without running |
| `python -m zipapp <dir>` | Bundle a directory into a runnable `.pyz` |
| `python -m ensurepip` | Bootstrap pip if missing |

---

## pip install

| Flag | Effect |
|------|--------|
| `<package>` | Install latest version |
| `<package>==1.2.3` | Install exact version |
| `<package>>=1.0,<2.0` | Version range |
| `-r requirements.txt` | Install from a file |
| `-e .` | Editable install (dev mode — changes reflect instantly) |
| `-e <path>` | Editable install from a local path |
| `--upgrade` / `-U` | Upgrade to the latest version |
| `--pre` | Include pre-release versions |
| `--no-deps` | Don't install dependencies |
| `--only-binary :all:` | Only use wheels, no source builds |
| `--no-binary :all:` | Force source builds |
| `--index-url <url>` | Use a different package index |
| `--extra-index-url <url>` | Add an additional package index |
| `--find-links <dir>` | Also search a local directory for packages |
| `--no-index` | Don't use PyPI — only `--find-links` |
| `--target <dir>` | Install into a specific directory |
| `--user` | Install to user site (`~/.local/`) instead of system |
| `-q` / `--quiet` | Less output |
| `-v` / `--verbose` | More output |
| `--dry-run` | Show what would be installed without installing |
| `--ignore-requires-python` | Bypass Python version check |
| `--no-cache-dir` | Don't use cached packages |
| `--cache-dir <dir>` | Use a custom cache directory |

---

## pip uninstall

| Flag | Effect |
|------|--------|
| `-y` / `--yes` | Don't prompt for confirmation |
| `-r requirements.txt` | Uninstall all packages listed in file |

---

## pip list

| Flag | Effect |
|------|--------|
| `--outdated` / `-o` | Show only packages with newer versions available |
| `--uptodate` / `-u` | Show only up-to-date packages |
| `--not-required` | Packages not required by any other package |
| `--format columns` | Default columnar format |
| `--format json` | Machine-readable output |
| `--format freeze` | Like `pip freeze` output |
| `-v` | Include installer and location |

---

## pip show

```bash
pip show <package>           # name, version, location, deps
pip show -f <package>        # also list installed files
```

---

## pip freeze

```bash
pip freeze                   # all installed packages with pinned versions
pip freeze > requirements.txt          # save to file
pip freeze | grep -v "^-e"            # exclude editable installs
```

---

## pip download

| Flag | Effect |
|------|--------|
| `-d <dir>` | Download destination directory |
| `--platform <tag>` | Target platform (e.g. `manylinux1_x86_64`) |
| `--python-version <ver>` | Target Python version |
| `--no-deps` | Download package only, no dependencies |

---

## pip cache

```bash
pip cache info               # cache size and location
pip cache list               # cached packages
pip cache remove <pattern>   # remove matching cached files
pip cache purge              # clear all cache
```

---

## pip config

```bash
pip config list                          # show all config values
pip config get global.index-url         # get one value
pip config set global.index-url <url>   # set globally
pip config unset global.index-url
```

---

## pip check

```bash
pip check          # verify installed packages have compatible dependencies
```

---

## pip wheel

```bash
pip wheel <package> -w ./wheels     # build wheel without installing
pip wheel -r requirements.txt -w ./wheels
```

---

## venv

```bash
python3 -m venv .venv                    # create
python3 -m venv .venv --prompt myapp     # custom shell prompt label
python3 -m venv .venv --upgrade-deps     # also upgrade pip/setuptools
python3 -m venv .venv --system-site-packages  # inherit global packages
source .venv/bin/activate                # activate (macOS/Linux)
deactivate                               # deactivate
```

---

## PYTHONPATH & environment variables

| Variable | Effect |
|----------|--------|
| `PYTHONPATH` | Extra directories to add to `sys.path` |
| `PYTHONSTARTUP` | Script to run at interactive shell startup |
| `PYTHONDONTWRITEBYTECODE=1` | Don't write `.pyc` files (same as `-B`) |
| `PYTHONUNBUFFERED=1` | Unbuffered output (same as `-u`) — common in Docker |
| `PYTHONWARNINGS` | Warning filter (same as `-W`) |
| `PYTHONINSPECT` | Drop into shell after script (same as `-i`) |
| `VIRTUAL_ENV` | Set by `activate` — path to active virtual env |
| `PIP_INDEX_URL` | Default package index for pip |
| `PIP_EXTRA_INDEX_URL` | Extra index for pip |
| `PIP_NO_CACHE_DIR=1` | Disable pip cache |
