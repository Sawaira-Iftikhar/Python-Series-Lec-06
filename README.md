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
|**Built-in** | Pre-defined by Python | 'print()', 'len()', 'max()', 'type()' |
