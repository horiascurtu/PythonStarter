# 📘 Day 10: Dictionaries in Python

Today we explore `dict`, one of Python’s most powerful data structures.

---

## 🔑 What is a Dictionary?

- Key-value pair storage
- Unordered (until Python 3.7+), mutable

```python
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
```

---

## 🛠️ Common Operations

- Access: `person["name"]` or `person.get("name")`
- Add/Update: `person["age"] = 30`
- Delete: `del person["city"]`

---

## 🔍 Useful Methods

- `.keys()`, `.values()`, `.items()`
- `.get()`, `.update()`, `.pop()`

---

## 🧠 Use Cases

- Fast lookup
- Grouping or categorizing
- Nested data (dictionaries inside dictionaries)

---

## 🎯 Goal

Master dictionaries for storing and managing structured data.
