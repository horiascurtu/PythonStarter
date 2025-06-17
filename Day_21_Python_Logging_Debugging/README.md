# 📦 Day 21: Working with JSON in Python

Welcome to **Day 21**! Today you’ll learn how to work with **JSON (JavaScript Object Notation)** – a widely used format for storing and exchanging data, especially in APIs and web applications.

---

## 🧠 What You’ll Learn
- What is JSON?
- Converting Python objects to JSON (`json.dumps`)
- Saving JSON to a file (`json.dump`)
- Reading JSON from a file (`json.load`)
- Converting JSON to Python (`json.loads`)

---

## 📄 What is JSON?

**JSON** is a text-based format for representing structured data.

```json
{
  "name": "Alice",
  "age": 30,
  "is_admin": false
}
```

Python dictionaries and lists map well to JSON.

---

## 🔄 Converting Python to JSON

```python
import json

data = {"name": "Bob", "age": 25}
json_str = json.dumps(data)
print(json_str)  # {"name": "Bob", "age": 25}
```

---

## 💾 Saving JSON to a File

```python
with open("data.json", "w") as f:
    json.dump(data, f)
```

---

## 📥 Reading JSON from a File

```python
with open("data.json", "r") as f:
    content = json.load(f)
    print(content["name"])
```

---

## 🔁 Converting JSON to Python

```python
json_input = '{"name": "Carol", "age": 22}'
parsed = json.loads(json_input)
print(parsed["age"])
```

---

## 🧾 JSON and Python Types

| JSON        | Python          |
|-------------|------------------|
| Object      | dict             |
| Array       | list             |
| String      | str              |
| Number      | int / float      |
| true/false  | True / False     |
| null        | None             |

---

## 🛡 Tips

- JSON keys must be strings
- Use `indent=4` in `dumps()` or `dump()` for pretty output
- Avoid non-serializable types (e.g. custom objects)

```python
print(json.dumps(data, indent=4))
```

---

## 🧰 Real World Uses

- Saving settings
- Data transfer via APIs
- Config files
- Persisting dictionaries

---

## 🎯 Practice Time!

Practice reading, writing, and converting JSON in Python. Exercises are in `exercitii.py`, solutions in `solutii.py`.

➡️ Next up: **Day 22 – Error Logging and Debugging**
