# 📄 Day 15: Reading & Writing Files in Python

Welcome to Day 15! Today you’ll learn how to **work with files** in Python — read from and write to them. This is an essential skill for building real-world applications like data loggers, config managers, and more.

---

## 🧠 What You’ll Learn
- How to open and close files
- Reading from a file
- Writing and appending to a file
- Using `with` context manager
- File modes: `"r"`, `"w"`, `"a"`, `"x"`

---

## 📂 Opening Files

```python
file = open("example.txt", "r")
content = file.read()
file.close()
print(content)
```

Always close the file or use a context manager.

---

## ✅ Using `with` (Best Practice)

The `with` statement automatically handles file closing:

```python
with open("example.txt", "r") as file:
    content = file.read()
print(content)
```

---

## 🔍 Reading Files

| Method        | Description                       |
|---------------|-----------------------------------|
| `read()`      | Reads entire file                 |
| `readline()`  | Reads one line                    |
| `readlines()` | Reads all lines as a list         |

```python
with open("example.txt", "r") as f:
    for line in f:
        print(line.strip())
```

---

## ✏️ Writing to Files

### Overwrite mode (`"w"`):

```python
with open("output.txt", "w") as f:
    f.write("Hello world!")
```

### Append mode (`"a"`):

```python
with open("output.txt", "a") as f:
    f.write("\nNew line!")
```

---

## ❗ File Modes

| Mode | Description                      |
|------|----------------------------------|
| `"r"` | Read (default)                  |
| `"w"` | Write (overwrite if exists)     |
| `"a"` | Append (add to file)            |
| `"x"` | Create file, error if exists    |
| `"b"` | Binary mode (e.g. images, PDF)  |

---

## 🔄 Writing Multiple Lines

```python
lines = ["First line\n", "Second line\n"]
with open("log.txt", "w") as f:
    f.writelines(lines)
```

---

## 🎯 Practice Time!

Work with reading and writing files using Python. Try the exercises in `exercitii.py` and check your answers in `solutii.py`.

➡️ Coming next: **Classes and Object-Oriented Programming!**
