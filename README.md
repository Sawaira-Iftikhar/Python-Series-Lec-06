# Python-Series-Lec-06

## 📚 Topics Covered

| # | Topic | Status |
|---|-------|:------:|
| 1 | Function Basics (`def`, `return`, Parameters & Arguments) | ✅ |
| 2 | Types of Functions (Built-in, User-defined, Lambda, Void) | ✅ |
| 3 | Default Parameters & Keyword Arguments | ✅ |
| 4 | `*args` and `**kwargs` (Variable-length Arguments) | ✅ |
| 5 | Recursion (Base Case, Recursive Case, Call Stack) | ✅ |
| 6 | Recursion vs Iteration & Real-world Recursive Problems | ✅ |

## 📂 Practice Files

| File | Topics | Difficulty | Questions |
|------|--------|:----------:|:---------:|
| [01_Functions_basics.py](01_Functions_basics.py) | `def`, `return`, Parameters, Types of Functions | 08 |
| [02_Default_and_advanced.py](02_Default_and_advanced.py) | Default Params, Keyword Args, `*args`, `**kwargs` | 09 |
| [03_recursion.py](03_recursion.py) | Recursion, Base Case, Factorial, Fibonacci | 08 |
| [04_Challenge.py}](04_Challenge.py) | ALL Topics Mixed (Boss Level) | 03 |

## 💡 Quick Cheat Sheet (Lecture 6 Highlights)

<details>
<summary><b>Click to expand quick revision notes</b></summary>

<br>

### 1. Function Anatomy

```python
def function_name(parameter1, parameter2=default_value):
    """Docstring: describes what the function does."""
    # Function body
    result = parameter1 + parameter2
    return result          # Returns value to caller

# Calling the function
output = function_name(10, 20)
```

### 2. Types of Functions

| Type | Descripton | Example|
|------|------------|--------|
|**Built-in** | Pre-defined by Python | `print()`, `len()`,`max()`, `type()` |
|**User-defined** | Created by you using `def` | `def greet(name): ...` |
| **Lambda** | Anonymous one-liner function | `square = lambda x: x ** 2` |
| **Void** | Performs action but returns `None` | `def log(msg): print(msg)` |
| **Recursive** | Calls itself | `def factorial(n): ...` |

### 3. Parameters & Arguments

```python
# Positional Arguments
def add(a, b):
    return a + b
add(5, 3)           # a=5, b=3

# Default Parameters
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
greet("Ali")         # "Hello, Ali!"
greet("Ali", "Hi")   # "Hi, Ali!"

# Keyword Arguments (order doesn't matter)
greet(greeting="Hey", name="Sara")  # "Hey, Sara!"

# *args (variable positional arguments → tuple)
def total(*args):
    return sum(args)
total(1, 2, 3, 4)    # 10

# **kwargs (variable keyword arguments → dict)
def profile(**kwargs):
    print(kwargs)
profile(name="Ali", age=22)  # {'name': 'Ali', 'age': 22}
```

### 4. Recursion Pattern

```python
def recursive_function(n):
    # 1. BASE CASE — stops the recursion
    if n <= 0:
        return 0

    # 2. RECURSIVE CASE — calls itself with smaller input
    return n + recursive_function(n - 1)
```

**Golden Rules of Recursion:**

Always define a base case (or you get RecursionError).
Each call must move closer to the base case.
Python's default recursion limit is 1000 (sys.getrecursionlimit()).

### 5. Common Gotchas

```Python
# ❌ Mutable default argument trap:
def add_item(item, lst=[]):   # DANGEROUS!
    lst.append(item)
    return lst

# ✅ Correct approach:
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```
</details>

## 📅 Series Progress

- [x] **Lecture 01** — Basics, Data Types & Operators ✅
- [x] **Lecture 02** — Strings, Slicing & Conditionals ✅
- [x] **Lecture 03** — Lists, Tuples & Methods ✅
- [x] **Lecture 04** — Dictionaries & Sets ✅
- [x] **Lecture 05** — Loops, Lists & Tuples in Loops ✅
- [x] **Lecture 06** — Functions, Default Params & Recursion 📍 *(Current)*
- [ ] **Lecture 07** — Coming Soon
- [ ] **Lecture 08** — Coming Soon
- [ ] **Lecture 09** — Coming Soon

