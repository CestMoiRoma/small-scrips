# Python & pip — Quick Cheat Sheet

---

## Data types

| Type | Literal | Mutable |
|------|---------|---------|
| `int` | `42` | No |
| `float` | `3.14` | No |
| `str` | `"hi"` | No |
| `bool` | `True` | No |
| `None` | `None` | — |
| `list` | `[1, 2]` | Yes |
| `tuple` | `(1, 2)` | No |
| `dict` | `{"a": 1}` | Yes |
| `set` | `{1, 2}` | Yes |
| `bytes` | `b"hi"` | No |

---

## Strings

| Expression | Result |
|------------|--------|
| `s.upper()` | Uppercase |
| `s.lower()` | Lowercase |
| `s.strip()` | Remove whitespace |
| `s.split(",")` | Split to list |
| `",".join(lst)` | Join list |
| `s.replace("a","b")` | Replace |
| `s.startswith("hi")` | Prefix check |
| `s.endswith("!")` | Suffix check |
| `s.find("x")` | Index or `-1` |
| `s[0:5]` | Slice |
| `s[::-1]` | Reversed |
| `f"{val:.2f}"` | Format float |
| `f"{n:,}"` | Thousands separator |
| `f"{n:08b}"` | Binary padded |

---

## Lists

| Expression | Description |
|------------|-------------|
| `lst.append(x)` | Add to end |
| `lst.extend(other)` | Extend with iterable |
| `lst.insert(i, x)` | Insert at index |
| `lst.remove(x)` | Remove first occurrence |
| `lst.pop()` | Remove and return last |
| `lst.pop(i)` | Remove and return at index |
| `lst.index(x)` | First index of value |
| `lst.count(x)` | Count occurrences |
| `lst.sort()` | Sort in place |
| `lst.sort(reverse=True)` | Sort descending |
| `lst.reverse()` | Reverse in place |
| `sorted(lst)` | New sorted list |
| `lst[1:3]` | Slice |
| `lst[::-1]` | Reversed copy |

---

## Dicts

| Expression | Description |
|------------|-------------|
| `d[key]` | Get (raises `KeyError`) |
| `d.get(key, default)` | Safe get |
| `d[key] = val` | Set |
| `del d[key]` | Delete key |
| `d.keys()` | All keys |
| `d.values()` | All values |
| `d.items()` | Key-value pairs |
| `d.update(other)` | Merge into d |
| `d.pop(key)` | Remove and return |
| `d.setdefault(k, v)` | Set if missing |
| `d1 \| d2` | Merged dict (3.9+) |

---

## Sets

| Expression | Description |
|------------|-------------|
| `s.add(x)` | Add element |
| `s.remove(x)` | Remove (raises if missing) |
| `s.discard(x)` | Remove (no error) |
| `s1 \| s2` | Union |
| `s1 & s2` | Intersection |
| `s1 - s2` | Difference |
| `s1 ^ s2` | Symmetric difference |
| `s1 <= s2` | Is subset |

---

## Control flow

| Syntax | Description |
|--------|-------------|
| `if / elif / else` | Conditional |
| `x if cond else y` | Ternary |
| `for x in iterable` | For loop |
| `for i, v in enumerate(lst)` | With index |
| `for k, v in d.items()` | Dict loop |
| `for a, b in zip(x, y)` | Parallel loop |
| `while condition` | While loop |
| `break` | Exit loop |
| `continue` | Skip iteration |
| `pass` | No-op placeholder |
| `match x: case val:` | Pattern match (3.10+) |

---

## Functions

| Syntax | Description |
|--------|-------------|
| `def fn(a, b=1)` | With default arg |
| `def fn(*args)` | Variable positional |
| `def fn(**kwargs)` | Variable keyword |
| `def fn(*, kw)` | Keyword-only arg |
| `def fn(x, /, y)` | Positional-only arg (3.8+) |
| `lambda x: x+1` | Anonymous function |
| `-> int` | Return type hint |

---

## Comprehensions

| Syntax | Description |
|--------|-------------|
| `[x for x in it]` | List |
| `[x for x in it if cond]` | Filtered list |
| `{k: v for k, v in it}` | Dict |
| `{x for x in it}` | Set |
| `(x for x in it)` | Generator (lazy) |

---

## Exception handling

| Syntax | Description |
|--------|-------------|
| `try / except` | Catch exceptions |
| `except (A, B) as e` | Multiple types |
| `else` | Runs if no exception |
| `finally` | Always runs |
| `raise ValueError("msg")` | Raise an exception |
| `raise` | Re-raise current |

---

## Classes

| Syntax | Description |
|--------|-------------|
| `class Foo:` | Define a class |
| `class Foo(Bar):` | Inherit from Bar |
| `def __init__(self)` | Constructor |
| `super().__init__()` | Call parent constructor |
| `@classmethod` | Receives `cls` |
| `@staticmethod` | No `self` or `cls` |
| `@property` | Getter as attribute |
| `@prop.setter` | Setter |

---

## File I/O

| Expression | Description |
|------------|-------------|
| `open(f)` | Open for reading |
| `open(f, "w")` | Write (overwrite) |
| `open(f, "a")` | Append |
| `open(f, "rb")` | Read binary |
| `f.read()` | Full content |
| `f.readlines()` | List of lines |
| `f.write(s)` | Write string |
| `Path(f).read_text()` | Read with pathlib |
| `Path(f).write_text(s)` | Write with pathlib |

---

## Common built-ins

| Function | Description |
|----------|-------------|
| `len(x)` | Length |
| `type(x)` | Type |
| `isinstance(x, T)` | Type check |
| `range(n)` | Integer range |
| `enumerate(it)` | Index + value |
| `zip(a, b)` | Parallel iteration |
| `map(fn, it)` | Apply function |
| `filter(fn, it)` | Filter iterable |
| `sorted(it, key=fn)` | New sorted |
| `min(it) / max(it)` | Min / max |
| `sum(it)` | Sum |
| `any(it) / all(it)` | Boolean aggregation |
| `abs(x)` | Absolute value |
| `round(x, n)` | Round to n digits |
| `repr(x)` | Developer string |
| `hash(x)` | Hash value |
| `id(x)` | Memory address |
| `vars(obj)` | Object `__dict__` |
| `dir(obj)` | Attributes and methods |
| `help(obj)` | Inline documentation |

---

## pip

| Command | Description |
|---------|-------------|
| `pip install <pkg>` | Install |
| `pip install <pkg>==1.2.3` | Exact version |
| `pip install -r requirements.txt` | From file |
| `pip install -e .` | Editable install |
| `pip install -U <pkg>` | Upgrade |
| `pip install --pre <pkg>` | Include pre-releases |
| `pip install --no-deps <pkg>` | No dependencies |
| `pip uninstall <pkg>` | Uninstall |
| `pip uninstall -y <pkg>` | No confirmation |
| `pip list` | Installed packages |
| `pip list --outdated` | Outdated packages |
| `pip freeze` | Pinned list |
| `pip freeze > requirements.txt` | Save dependencies |
| `pip show <pkg>` | Package details |
| `pip check` | Verify compatibility |
| `pip cache purge` | Clear download cache |

---

## venv

| Command | Description |
|---------|-------------|
| `python3 -m venv .venv` | Create virtual environment |
| `source .venv/bin/activate` | Activate (macOS/Linux) |
| `.venv\Scripts\activate` | Activate (Windows) |
| `deactivate` | Deactivate |
| `which python` | Confirm active env |

---

## python CLI

| Command | Description |
|---------|-------------|
| `python -c "code"` | Run inline code |
| `python -m <module>` | Run a module |
| `python -m http.server` | Quick HTTP server |
| `python -m json.tool file.json` | Pretty-print JSON |
| `python -m pdb script.py` | Debug a script |
| `python -m venv .venv` | Create virtual env |
| `python -m pip install <pkg>` | Safest way to call pip |
| `python -u script.py` | Unbuffered output |
| `python -i script.py` | Interactive after run |
| `python --version` | Show version |
