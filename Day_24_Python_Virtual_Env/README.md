# 🗂️ Day 24: File Management with OS Module in Python

Welcome to **Day 24**! Today you'll learn how to manage files and directories in Python using the powerful `os` and `shutil` modules. These tools help automate system-level tasks like navigating directories, creating folders, renaming files, and more.

---

## 🧠 What You’ll Learn
- How to navigate the file system with `os`
- How to create, rename, and delete files/folders
- How to list directory contents
- Using `shutil` for copying and moving files

---

## 📁 The `os` Module – Working with the File System

```python
import os
print(os.getcwd())  # Current working directory
```

---

## 📂 Listing Files and Folders

```python
for item in os.listdir():
    print(item)
```

You can also specify a path: `os.listdir("path/to/folder")`

---

## 📦 Creating and Removing Directories

```python
os.mkdir("new_folder")       # Create one directory
os.makedirs("a/b/c")         # Create nested folders
os.rmdir("new_folder")       # Remove empty folder
os.removedirs("a/b/c")       # Remove nested empty folders
```

---

## ✏️ Renaming and Deleting Files

```python
os.rename("old.txt", "new.txt")
os.remove("new.txt")
```

---

## 📋 Absolute and Relative Paths

```python
os.path.abspath("file.txt")      # Absolute path
os.path.exists("file.txt")       # Check if exists
os.path.isfile("file.txt")       # Is a file?
os.path.isdir("folder")          # Is a directory?
```

---

## 📦 Copying & Moving Files – `shutil`

```python
import shutil

shutil.copy("source.txt", "destination.txt")     # Copy file
shutil.move("file.txt", "folder/file.txt")       # Move or rename file
```

---

## 🛑 Caution

- `os.remove()` deletes files permanently
- `shutil.rmtree()` removes non-empty folders (use with care!)

---

## 🧰 Summary Table

| Task                  | Function                        |
|-----------------------|---------------------------------|
| Get current dir       | `os.getcwd()`                   |
| Change dir            | `os.chdir(path)`                |
| List dir contents     | `os.listdir(path)`              |
| Create folder         | `os.mkdir()` / `os.makedirs()`  |
| Delete file           | `os.remove()`                   |
| Copy/move file        | `shutil.copy()` / `shutil.move()`|

---

## 🎯 Practice Time!

Manage folders and files using `os` and `shutil`. Create scripts that automate directory organization.

Exercises are in `exercitii.py`, and solutions in `solutii.py`.

➡️ Next: **Day 25 – Using Virtual Environments**
