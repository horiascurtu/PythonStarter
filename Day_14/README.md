# 📦 Day 14: Modules and Imports in Python

Welcome to Day 14! Today you'll learn how to **organize your code** using modules and how to reuse functionality by importing built-in and external Python modules.

---

## 🧠 What You’ll Learn
- What a module is
- How to import built-in modules
- Using `import`, `from ... import`, and `as`
- Creating your own modules
- Installing and using external libraries

---

## 📁 What is a Module?

A **module** is a file containing Python definitions and functions. You can use it to:
- Reuse code across projects
- Keep your code clean and organized
- Access powerful tools built by others

---

## 🧰 Importing Built-in Modules

Python includes many **standard modules**:

```python
import math
print(math.sqrt(25))  # 5.0
```

You can also import specific parts:

```python
from math import pi
print(pi)
```

Or give a module a nickname:

```python
import math as m
print(m.pi)
```

---

## 🔧 Useful Built-in Modules

| Module   | Use                          |
|----------|------------------------------|
| `math`   | Advanced math functions      |
| `random` | Generate random values       |
| `datetime` | Work with dates and times |
| `os`     | Interact with the operating system |
| `sys`    | System-specific parameters   |

Example:

```python
import random
print(random.randint(1, 10))
```

---

## 🛠 Creating Your Own Module

Save a Python file (e.g. `mymodule.py`) with functions:

```python
# mymodule.py
def greet(name):
    return f"Hello, {name}!"
```

Then use it in another file:

```python
import mymodule
print(mymodule.greet("Alice"))
```

---

## 🌐 Installing External Modules

Use `pip` to install third-party libraries:

```bash
pip install requests
```

Then:

```python
import requests
```

---

## 🚨 Notes on Importing

- Python searches for modules in the current folder and system paths
- Avoid naming your file the same as built-in modules (e.g. `random.py`)

---

## 🎯 Practice Time!

Practice importing and using built-in modules, and try creating your own. Tasks are in `exercitii.py` and answers in `solutii.py`.

➡️ Coming next: **Reading & Writing Files!**
