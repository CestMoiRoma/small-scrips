# Python Basics

---

## Data types

| Type | Example | Notes |
|------|---------|-------|
| `int` | `42`, `-7` | Arbitrary precision |
| `float` | `3.14`, `1e-3` | IEEE 754 double |
| `str` | `"hello"`, `'world'` | Immutable |
| `bool` | `True`, `False` | Subclass of `int` |
| `None` | `None` | Null value |
| `list` | `[1, 2, 3]` | Mutable ordered sequence |
| `tuple` | `(1, 2, 3)` | Immutable ordered sequence |
| `dict` | `{"a": 1}` | Key-value map, insertion-ordered (3.7+) |
| `set` | `{1, 2, 3}` | Unordered, unique values |
| `bytes` | `b"hello"` | Immutable byte sequence |

---

## Variables & operators

```python
x = 10
x, y = 1, 2          # multiple assignment
a = b = c = 0        # chain assignment
x += 1               # augmented assignment

# Arithmetic
+  -  *  /           # add, sub, mul, true div (returns float)
//                   # floor division
%                    # modulo
**                   # exponentiation

# Comparison
==  !=  <  >  <=  >=
is     # identity (same object)
is not
in     # membership
not in

# Logical
and  or  not
```

---

## Strings

```python
s = "Hello, World!"

len(s)               # 13
s.upper()            # "HELLO, WORLD!"
s.lower()            # "hello, world!"
s.strip()            # remove leading/trailing whitespace
s.lstrip() / s.rstrip()
s.replace("Hello", "Hi")
s.split(",")         # ["Hello", " World!"]
s.split()            # split on any whitespace
",".join(["a", "b"]) # "a,b"
s.startswith("He")   # True
s.endswith("!")      # True
s.find("World")      # 7  (-1 if not found)
s.count("l")         # 3
"42".zfill(5)        # "00042"

# Slicing
s[0]       # "H"
s[-1]      # "!"
s[0:5]     # "Hello"
s[::2]     # every other character
s[::-1]    # reversed

# f-strings (3.6+)
name = "Alice"
age  = 30
f"Name: {name}, Age: {age}"
f"{3.14159:.2f}"     # "3.14"
f"{1000000:,}"       # "1,000,000"
f"{42:08b}"          # "00101010" (binary, padded)
f"{name!r}"          # repr of name
```

---

## Lists

```python
lst = [1, 2, 3]

lst.append(4)        # [1, 2, 3, 4]
lst.extend([5, 6])   # [1, 2, 3, 4, 5, 6]
lst.insert(0, 0)     # insert at index
lst.remove(3)        # remove first occurrence of value
lst.pop()            # remove and return last
lst.pop(0)           # remove and return at index
lst.index(2)         # first index of value
lst.count(1)         # count occurrences
lst.sort()           # sort in place
lst.sort(reverse=True)
lst.reverse()        # reverse in place
lst.clear()
sorted(lst)          # returns new sorted list
list(reversed(lst))  # returns new reversed list

# Slicing
lst[1:3]             # sublist
lst[::2]             # every other element
lst[::-1]            # reversed copy
```

---

## Dictionaries

```python
d = {"a": 1, "b": 2}

d["a"]               # 1
d.get("c")           # None (no KeyError)
d.get("c", 0)        # 0 (default)
d["c"] = 3           # add or update
del d["a"]           # delete key
d.keys()             # dict_keys
d.values()           # dict_values
d.items()            # dict_items — (key, value) pairs
d.update({"d": 4})   # merge
d.pop("b")           # remove and return
d.setdefault("e", 5) # set only if not exists

# Merge (3.9+)
d3 = d1 | d2         # new merged dict
d1 |= d2             # update d1 in place
```

---

## Sets

```python
s = {1, 2, 3}

s.add(4)
s.remove(2)          # raises KeyError if missing
s.discard(2)         # no error if missing
s.pop()              # remove and return an arbitrary element

s1 | s2              # union
s1 & s2              # intersection
s1 - s2              # difference
s1 ^ s2              # symmetric difference
s1 <= s2             # is s1 a subset of s2?
s1 >= s2             # is s1 a superset of s2?
```

---

## Control flow

```python
# If
if x > 0:
    print("positive")
elif x == 0:
    print("zero")
else:
    print("negative")

# Ternary
result = "yes" if condition else "no"

# For
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 10, 2):   # 2, 4, 6, 8
    pass

for i, v in enumerate(lst):
    print(i, v)

for k, v in d.items():
    print(k, v)

for a, b in zip(lst1, lst2):
    print(a, b)

# While
while condition:
    break      # exit loop
    continue   # skip to next iteration
else:          # runs if loop completed without break
    pass
```

---

## Functions

```python
def greet(name, greeting="Hello"):
    """Docstring."""
    return f"{greeting}, {name}!"

# *args — variable positional args
def total(*numbers):
    return sum(numbers)

# **kwargs — variable keyword args
def show(**info):
    for k, v in info.items():
        print(f"{k}: {v}")

# Keyword-only args (after *)
def config(*, debug=False, verbose=False):
    pass

# Positional-only args (before /, Python 3.8+)
def add(x, y, /):
    return x + y

# Type hints
def add(a: int, b: int) -> int:
    return a + b

# Lambda
square = lambda x: x ** 2
```

---

## Classes

```python
class Animal:
    species = "unknown"          # class attribute

    def __init__(self, name: str, age: int):
        self.name = name         # instance attribute
        self.age  = age

    def speak(self) -> str:
        return f"{self.name} makes a sound"

    def __repr__(self) -> str:
        return f"Animal(name={self.name!r}, age={self.age})"

    def __str__(self) -> str:
        return self.name

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data["name"], data["age"])

    @staticmethod
    def is_valid_age(age: int) -> bool:
        return age >= 0


class Dog(Animal):
    def speak(self) -> str:         # override
        return f"{self.name} barks"

    def __init__(self, name, age, breed):
        super().__init__(name, age)  # call parent
        self.breed = breed
```

---

## Exception handling

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except (TypeError, ValueError) as e:
    print(f"Type or value error: {e}")
except Exception as e:
    print(f"Unexpected: {e}")
else:
    print("No error")     # runs only if no exception
finally:
    print("Always runs")  # cleanup

# Raise
raise ValueError("must be positive")
raise                     # re-raise current exception

# Custom exception
class AppError(Exception):
    pass
```

---

## Comprehensions

```python
# List
squares   = [x**2 for x in range(10)]
evens     = [x for x in range(20) if x % 2 == 0]
flat      = [n for row in matrix for n in row]

# Dict
lengths   = {s: len(s) for s in words}

# Set
unique_sq = {x**2 for x in numbers}

# Generator (lazy — does not build a list in memory)
total     = sum(x**2 for x in range(1000000))
```

---

## File I/O

```python
# Read
with open("file.txt") as f:
    content = f.read()           # full string
    lines   = f.readlines()      # list of lines

# Write
with open("file.txt", "w") as f:
    f.write("hello\n")

# Append
with open("file.txt", "a") as f:
    f.write("more\n")

# Binary
with open("image.png", "rb") as f:
    data = f.read()

# Pathlib (preferred)
from pathlib import Path

p = Path("dir/file.txt")
p.read_text()
p.write_text("hello")
p.exists()
p.parent        # Path("dir")
p.stem          # "file"
p.suffix        # ".txt"
p.name          # "file.txt"
list(p.parent.glob("*.txt"))
p.mkdir(parents=True, exist_ok=True)
```

---

## Imports

```python
import os
import os.path
from os import getcwd, listdir
from os.path import join, exists
import numpy as np              # alias
from . import module            # relative import
from .. import module           # parent package
```

---

## Common built-ins

```python
len(x)           # length
type(x)          # type of object
isinstance(x, int)
range(start, stop, step)
enumerate(iterable, start=0)
zip(a, b)
map(fn, iterable)
filter(fn, iterable)
sorted(iterable, key=fn, reverse=True)
min(iterable, key=fn)
max(iterable, key=fn)
sum(iterable, start=0)
any(iterable)    # True if at least one is truthy
all(iterable)    # True if all are truthy
abs(x)
round(x, ndigits)
int("42")
str(42)
float("3.14")
list(iterable)
tuple(iterable)
dict(pairs)
set(iterable)
repr(x)
print(*args, sep=" ", end="\n", file=sys.stdout)
input(prompt)
open(file, mode="r", encoding="utf-8")
```
