# 🗂️ Day 9: Mastering Dictionaries in Python

Welcome to Day 9! Today you’ll learn how to use **dictionaries**, one of the most versatile and important data structures in Python. Dictionaries allow you to store data in pairs – a **key** and a **value**.

---

## 🧠 What You’ll Learn
- What a dictionary is
- How to create and read from dictionaries
- How to update and remove data
- Useful dictionary methods
- How to loop through dictionaries

---

## 📚 What is a Dictionary?

A **dictionary** is a collection of **key-value pairs**.

Each **key** is unique, and it maps to a **value**:

```python
person = {
    "name": "Alice",
    "age": 25,
    "is_student": True
}
```

Here:
- `"name"`, `"age"`, and `"is_student"` are **keys**
- `"Alice"`, `25`, and `True` are **values**

You can think of it like a real dictionary:
- **Word (key)** ➡️ **Definition (value)**

---

## 🛠 Creating a Dictionary

You use curly braces `{}` and separate keys and values with colons `:`:

```python
car = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2022
}
```

---

## 🔍 Accessing Values

You access a value by referencing its key:

```python
print(car["brand"])  # Output: Toyota
```

To avoid errors when a key might not exist, use `.get()`:

```python
print(car.get("color", "Not available"))  # Safe access
```

---

## ✏️ Modifying a Dictionary

You can change or add data:

```python
car["year"] = 2023         # update value
car["color"] = "red"       # add new key-value pair
```

---

## ❌ Removing Items

- Remove a specific key:
```python
del car["model"]
```

- Use `pop()` to remove and return a value:
```python
car.pop("brand")
```

- Remove everything:
```python
car.clear()
```

---

## 🔁 Looping Through a Dictionary

Loop through **keys**:

```python
for key in car:
    print(key)
```

Loop through **values**:

```python
for value in car.values():
    print(value)
```

Loop through **key-value pairs**:

```python
for key, value in car.items():
    print(f"{key}: {value}")
```

---

## 🧰 Useful Methods

| Method          | Description                      |
|-----------------|----------------------------------|
| `dict.get(key)` | Get value safely                 |
| `dict.keys()`   | Return all keys                  |
| `dict.values()` | Return all values                |
| `dict.items()`  | Return all key-value pairs       |
| `dict.pop(key)` | Remove and return value          |
| `dict.clear()`  | Remove all items from dictionary |

---

## ✅ Real World Example

```python
student = {
    "name": "Maria",
    "grades": [9, 8.5, 10],
    "passed": True
}
print(f"{student['name']} has grades: {student['grades']}")
```

---

## 🎯 Practice Time!

Work with key-value data, access it safely, and print it in useful formats.
Your tasks are in `exercitii.py`. Check solutions in `solutii.py`.

➡️ Up next: **Tuples & Sets – for fixed and unique data!**
