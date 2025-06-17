# 💻 Day 23: Command Line Arguments in Python

Welcome to **Day 23**! Today you'll learn how to make your Python scripts interactive and flexible by accepting **arguments from the command line** using the `sys` and `argparse` modules.

---

## 🧠 What You’ll Learn
- How to use `sys.argv`
- How to use the `argparse` module
- Accepting multiple arguments
- Making scripts more dynamic
- Providing help and default values

---

## 🧾 Using `sys.argv`

```python
import sys

print(sys.argv)
```

If you run your script like:

```bash
python myscript.py hello world
```

`sys.argv` will be:

```python
['myscript.py', 'hello', 'world']
```

---

## 🧰 Example: Add Two Numbers from CLI

```python
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
print("Sum:", a + b)
```

---

## 🧙‍♂️ Using `argparse` (Recommended)

The `argparse` module gives you:
- Named arguments
- Help messages
- Default values
- Type conversion

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("name", help="Your name")
args = parser.parse_args()

print(f"Hello, {args.name}!")
```

Run like this:

```bash
python greet.py John
```

---

## ✅ Benefits of `argparse`

| Feature             | sys.argv     | argparse       |
|---------------------|--------------|----------------|
| Parses automatically| ❌            | ✅              |
| Provides help       | ❌            | ✅              |
| Handles types       | ❌            | ✅              |
| Optional args       | ❌            | ✅              |

---

## 🧪 Optional Arguments

```python
parser.add_argument("--age", type=int, help="Your age", default=0)
```

Run with:

```bash
python script.py John --age 25
```

---

## 🧰 Real Uses

- Scripts that take input files
- Automated tools
- Command-line utilities
- Processing data dynamically

---

## 🎯 Practice Time!

Create scripts that accept arguments via `sys.argv` and `argparse`.

Exercises are in `exercitii.py`, and solutions in `solutii.py`.

➡️ Up next: **Day 24 – File Management with OS Module**
