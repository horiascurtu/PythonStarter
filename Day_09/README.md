# 🗂️ Day 9: Dictionaries in Python

Today you’ll learn about **dictionaries**, a powerful data structure in Python that stores data in **key-value pairs**.

---

## 🧠 What You’ll Learn
- What a dictionary is
- How to create and access dictionary elements
- Adding, modifying, and deleting items
- Useful dictionary methods
- Looping through a dictionary

---

## 📘 What is a Dictionary?

A dictionary is like a real-life dictionary: you look up a **key** (e.g. a word) and get its **value** (e.g. the definition).

```python
person = {
    "name": "Alice",
    "age": 25,
    "is_student": True
}
```

---

## 🔍 Accessing and Modifying Data

```python
print(person["name"])         # Alice
person["age"] = 26            # update value
person["city"] = "New York"   # add new key-value pair
```

Use `.get()` to avoid errors:

```python
print(person.get("email", "Not found"))
```

---

## ❌ Removing Items

```python
del person["age"]         # remove by key
person.pop("city")        # remove and return value
person.clear()            # remove all items
```

---

## 🛠 Useful Methods

```python
person.keys()      # all keys
person.values()    # all values
person.items()     # key-value pairs
```

---

## 🔁 Looping Through a Dictionary

```python
for key in person:
    print(key, "->", person[key])

for key, value in person.items():
    print(f"{key}: {value}")
```

---

## 🎯 Today’s Challenge

Create and use dictionaries to store structured data and loop through key-value pairs. Check the tasks in `exercitii.py` and answers in `solutii.py`.

➡️ Next up: **Tuples and Sets!**
