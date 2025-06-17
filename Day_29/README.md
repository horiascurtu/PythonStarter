# 🧰 Day 29: Building a Small CLI Project in Python

Welcome to **Day 29**! Today you'll apply what you've learned by building a **simple command-line interface (CLI) project**. We'll use `argparse` and functions to create a tool you can run from the terminal.

---

## 🧠 What You’ll Learn
- How to plan and structure a CLI project
- Using `argparse` for command-line options
- Organizing code into functions
- Handling different operations based on user input

---

## 📋 Project Idea: To-Do List Manager

We'll build a simple task manager that lets users:

- Add a task
- View all tasks
- Remove a task
- Mark a task as done

---

## 🗂 File Structure

```
todo.py         # main script
tasks.json      # data file
```

---

## 🧱 Using argparse

```python
import argparse

parser = argparse.ArgumentParser(description="Simple To-Do CLI")
parser.add_argument("command", help="add/show/remove/done")
parser.add_argument("task", nargs="?", help="Task description")
args = parser.parse_args()
```

---

## 💾 Saving Data in JSON

```python
import json

with open("tasks.json", "w") as f:
    json.dump(tasks, f)
```

---

## 🔄 Loading and Updating Tasks

Load from `tasks.json`, update it, and save changes after each operation.

---

## 🧰 Summary

| Command             | Function                            |
|---------------------|--------------------------------------|
| `python todo.py add "Buy milk"` | Add new task               |
| `python todo.py show`           | Show all tasks             |
| `python todo.py done 1`         | Mark task #1 as done       |
| `python todo.py remove 2`       | Remove task #2             |

---

## 🎯 Practice Time!

Build the full project following the steps and code in `exercitii.py`. Test it with different arguments in your terminal.

➡️ Next: **Day 30 – Final Challenge and Wrap-up**
