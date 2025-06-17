# 🧪 Day 25: Using Virtual Environments in Python

Welcome to **Day 25**! Today you'll learn how to use **virtual environments** – a vital tool in Python development that allows you to isolate project dependencies and avoid conflicts between packages.

---

## 🧠 What You’ll Learn
- What is a virtual environment?
- How to create a virtual environment
- Activating and deactivating environments
- Installing packages inside a virtual env
- Using `requirements.txt` for sharing environments

---

## 🔍 Why Virtual Environments?

Different Python projects often require **different versions** of the same packages. Virtual environments help you:
- Avoid conflicts
- Keep projects clean and independent
- Easily reproduce and share setups

---

## ⚙️ Create a Virtual Environment

In your terminal:

```bash
python -m venv env
```

This creates a folder `env/` with a full Python installation.

---

## ▶️ Activate the Environment

### On Windows:

```bash
env\Scripts\activate
```

### On macOS/Linux:

```bash
source env/bin/activate
```

You'll see the environment name in your terminal prompt.

---

## 🛑 Deactivate

```bash
deactivate
```

---

## 📦 Installing Packages

While inside the virtual environment:

```bash
pip install requests
```

To list installed packages:

```bash
pip freeze
```

---

## 📃 requirements.txt

Create a list of packages to share your environment:

```bash
pip freeze > requirements.txt
```

Install from it:

```bash
pip install -r requirements.txt
```

---

## 🧰 Summary

| Task                     | Command                           |
|--------------------------|------------------------------------|
| Create venv              | `python -m venv env`               |
| Activate (Windows)       | `env\Scripts\activate`           |
| Activate (Unix/macOS)    | `source env/bin/activate`          |
| Deactivate               | `deactivate`                       |
| Install package          | `pip install package_name`         |
| Export dependencies      | `pip freeze > requirements.txt`    |
| Import dependencies      | `pip install -r requirements.txt`  |

---

## 🎯 Practice Time!

Work with virtual environments: create one, activate it, install packages, and export your dependencies.

Tasks are in `exercitii.py`, and solutions in `solutii.py`.

➡️ Next up: **Day 26 – Web Scraping with `requests` and `BeautifulSoup`**
