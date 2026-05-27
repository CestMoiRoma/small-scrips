# Python Advanced

---

## Virtual environments

```bash
python3 -m venv .venv             # create a virtual environment
source .venv/bin/activate         # activate (macOS/Linux)
.venv\Scripts\activate            # activate (Windows)
deactivate                        # deactivate

# With a specific Python version
python3.11 -m venv .venv

# Check you're in the right env
which python
python --version
```

> Always activate before installing packages. The virtual env is local to the project — never commit it.

---

## Type hints

```python
from typing import Optional, Union, Any

# Basic
def greet(name: str) -> str: ...

# Optional (can be None)
def find(id: int) -> Optional[str]: ...

# Union
def parse(value: Union[str, int]) -> float: ...

# Python 3.10+ shorthand
def parse(value: str | int) -> float: ...

# Collections
from typing import List, Dict, Tuple, Set   # Python 3.8
def process(items: list[str]) -> dict[str, int]: ...  # Python 3.9+

# Callable
from typing import Callable
def apply(fn: Callable[[int], str], x: int) -> str: ...

# TypeVar (generics)
from typing import TypeVar
T = TypeVar("T")
def first(lst: list[T]) -> T: return lst[0]

# Literal
from typing import Literal
def set_mode(mode: Literal["read", "write"]) -> None: ...

# TypedDict
from typing import TypedDict
class User(TypedDict):
    name: str
    age: int
```

---

## Dataclasses

Less boilerplate than regular classes.

```python
from dataclasses import dataclass, field

@dataclass
class Point:
    x: float
    y: float
    label: str = "point"              # default value
    tags: list = field(default_factory=list)  # mutable default

    def distance(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

@dataclass(frozen=True)    # immutable (hashable)
class Color:
    r: int
    g: int
    b: int

@dataclass(order=True)     # enables < > <= >= comparison
class Version:
    major: int
    minor: int
    patch: int
```

---

## Decorators

A function that wraps another function.

```python
import functools

def my_decorator(func):
    @functools.wraps(func)      # preserve original metadata
    def wrapper(*args, **kwargs):
        print("before")
        result = func(*args, **kwargs)
        print("after")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("hello")

# Decorator with arguments
def repeat(n):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("hi")
```

Common built-in decorators:

| Decorator | Effect |
|-----------|--------|
| `@property` | Getter — access method as attribute |
| `@<prop>.setter` | Setter for a property |
| `@staticmethod` | No `self` or `cls` — just a namespaced function |
| `@classmethod` | Receives `cls` — works on the class, not instance |
| `@functools.lru_cache` | Memoize return values |
| `@functools.cache` | Unbounded LRU cache (3.9+) |
| `@abstractmethod` | Force subclasses to implement |
| `@dataclass` | Auto-generate `__init__`, `__repr__`, etc. |

---

## Generators & iterators

```python
# Generator function — yields values lazily
def count_up(n):
    for i in range(n):
        yield i

gen = count_up(5)
next(gen)    # 0
next(gen)    # 1

# Generator expression
gen = (x**2 for x in range(1000000))  # no memory spike

# yield from
def chain(*iterables):
    for it in iterables:
        yield from it

# Custom iterator
class Counter:
    def __init__(self, stop):
        self.current = 0
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        self.current += 1
        return self.current
```

---

## Context managers

```python
# Using with
with open("file.txt") as f:
    data = f.read()

# Custom context manager — class
class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.time() - self.start
        return False    # False = don't suppress exceptions

with Timer() as t:
    do_work()
print(t.elapsed)

# Custom context manager — contextlib
from contextlib import contextmanager

@contextmanager
def managed_resource():
    resource = acquire()
    try:
        yield resource
    finally:
        release(resource)
```

---

## *args and **kwargs

```python
def func(*args, **kwargs):
    print(args)    # tuple of positional args
    print(kwargs)  # dict of keyword args

# Unpacking when calling
lst  = [1, 2, 3]
d    = {"a": 1, "b": 2}
func(*lst)         # same as func(1, 2, 3)
func(**d)          # same as func(a=1, b=2)

# Forward all args
def wrapper(*args, **kwargs):
    return original(*args, **kwargs)
```

---

## Properties

```python
class Circle:
    def __init__(self, radius: float):
        self._radius = radius

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float):
        if value < 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    @property
    def area(self) -> float:
        import math
        return math.pi * self._radius ** 2
```

---

## Abstract classes

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...

    @abstractmethod
    def perimeter(self) -> float: ...

    def describe(self) -> str:           # concrete method
        return f"Area: {self.area():.2f}"

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self):      return 3.14 * self.r ** 2
    def perimeter(self): return 2 * 3.14 * self.r
```

---

## Async / await

```python
import asyncio

async def fetch(url: str) -> str:
    await asyncio.sleep(1)     # non-blocking wait
    return f"data from {url}"

async def main():
    # Sequential
    result = await fetch("https://example.com")

    # Concurrent
    results = await asyncio.gather(
        fetch("https://a.com"),
        fetch("https://b.com"),
        fetch("https://c.com"),
    )

asyncio.run(main())
```

---

## Useful standard library

```python
# os / sys
import os, sys
os.getcwd()
os.listdir(".")
os.environ.get("HOME")
os.path.join("dir", "file.txt")
sys.argv            # command-line arguments
sys.exit(1)

# pathlib
from pathlib import Path
Path.cwd()
Path.home()

# json
import json
json.dumps({"a": 1}, indent=2)   # dict → string
json.loads('{"a": 1}')           # string → dict
json.dump(data, file)            # write to file
json.load(file)                  # read from file

# re
import re
re.search(r"\d+", "abc123")
re.findall(r"\w+", text)
re.sub(r"\s+", " ", text)
re.compile(r"pattern")           # pre-compile for reuse

# datetime
from datetime import datetime, date, timedelta
datetime.now()
datetime.utcnow()
datetime.strptime("2024-01-15", "%Y-%m-%d")
datetime.now().strftime("%Y-%m-%d %H:%M")
timedelta(days=7)

# collections
from collections import defaultdict, Counter, deque, OrderedDict
Counter("aabbcc")                # {"a": 2, "b": 2, "c": 2}
Counter(words).most_common(5)
defaultdict(list)                # missing keys return []
deque(maxlen=5)                  # fixed-size queue

# itertools
from itertools import chain, product, combinations, permutations, islice
list(chain([1,2], [3,4]))        # [1, 2, 3, 4]
list(islice(gen, 10))            # first 10 from generator

# functools
from functools import partial, reduce, lru_cache
double = partial(multiply, 2)
lru_cache(maxsize=128)

# contextlib
from contextlib import suppress
with suppress(FileNotFoundError):
    os.remove("maybe.txt")

# dataclasses, typing, abc  ← see dedicated sections above
```

---

## Dunder methods (magic methods)

| Method | Triggered by |
|--------|-------------|
| `__init__` | `obj = Class()` |
| `__repr__` | `repr(obj)`, debugging |
| `__str__` | `str(obj)`, `print(obj)` |
| `__len__` | `len(obj)` |
| `__getitem__` | `obj[key]` |
| `__setitem__` | `obj[key] = val` |
| `__delitem__` | `del obj[key]` |
| `__contains__` | `x in obj` |
| `__iter__` | `for x in obj` |
| `__next__` | `next(obj)` |
| `__call__` | `obj()` |
| `__enter__` / `__exit__` | `with obj` |
| `__eq__` | `obj == other` |
| `__lt__` | `obj < other` |
| `__hash__` | `hash(obj)`, use in sets/dicts |
| `__add__` | `obj + other` |
| `__bool__` | `bool(obj)`, `if obj` |

---

## Useful patterns

```python
# Unpacking
first, *rest = [1, 2, 3, 4]       # first=1, rest=[2,3,4]
*init, last  = [1, 2, 3, 4]       # init=[1,2,3], last=4
a, b = b, a                        # swap in place

# Walrus operator (3.8+)
while chunk := f.read(8192):
    process(chunk)

if m := re.search(r"\d+", text):
    print(m.group())

# Dict merge (3.9+)
config = defaults | overrides

# Safe dict access chain
value = data.get("user", {}).get("address", {}).get("city", "unknown")

# Flatten a list of lists
flat = [x for sub in matrix for x in sub]

# Most frequent element
from collections import Counter
Counter(lst).most_common(1)[0][0]

# Chunk a list into batches
def batches(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i+n]
```
