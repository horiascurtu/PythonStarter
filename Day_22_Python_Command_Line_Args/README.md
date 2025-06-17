# 🐞 Day 22: Error Logging and Debugging in Python

Welcome to **Day 22**! Today you'll learn how to handle problems in your code using **logging** and **debugging** tools. These skills are essential for finding bugs and making your programs reliable and maintainable.

---

## 🧠 What You’ll Learn
- The difference between print, errors, and logs
- How to use the `logging` module
- Logging levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
- How to write logs to a file
- Basic debugging strategies
- Using breakpoints and inspecting variables

---

## 🪵 The `logging` Module

Logging lets you **record events and errors** without interrupting your program:

```python
import logging
logging.basicConfig(level=logging.INFO)
logging.info("App started")
```

---

## 🔢 Logging Levels

| Level     | When to Use                              |
|-----------|-------------------------------------------|
| DEBUG     | Detailed internal info (dev only)         |
| INFO      | General events (start/stop processes)     |
| WARNING   | Something unexpected, but still works     |
| ERROR     | A problem that stops part of the program  |
| CRITICAL  | Serious error (might crash the app)       |

```python
logging.warning("This is a warning")
logging.error("An error occurred")
```

---

## 📝 Logging to a File

```python
logging.basicConfig(filename="app.log", level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s")
```

---

## 🧪 Logging vs Printing

| print()                   | logging                        |
|---------------------------|--------------------------------|
| For debugging during dev  | For tracking info in prod      |
| Always visible            | Can be controlled by level     |
| Not time-stamped          | Time-stamped and formatted     |

---

## 🕵️ Basic Debugging Techniques

- Read error messages carefully
- Use `print()` to inspect variable values
- Comment out code to isolate problems
- Use try/except to catch errors

---

## 🐛 Using Breakpoints

In an IDE like VS Code or PyCharm:
- Add breakpoints
- Run in debug mode
- Step through code line-by-line
- Watch variables in real time

---

## 🧰 Common Errors

| Error Type       | Cause                            |
|------------------|----------------------------------|
| `SyntaxError`     | Invalid Python syntax           |
| `TypeError`       | Wrong type used                 |
| `NameError`       | Variable not defined            |
| `IndexError`      | List index out of range         |
| `KeyError`        | Missing dictionary key          |
| `ValueError`      | Invalid value passed            |

---

## 🎯 Practice Time!

Use the `logging` module in your scripts and practice catching, logging, and debugging errors.

Tasks are in `exercitii.py`, solutions in `solutii.py`.

➡️ Coming up: **Day 23 – Command Line Arguments**
