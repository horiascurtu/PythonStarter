# 📘 Day 9: Tuples and List Comprehensions

---

## 🔐 Tuples

Tuples are similar to lists, but **immutable** — you can't change their content after creation.

```python
person = ("Alice", 30, "New York")
print(person[0])  # "Alice"
```

Use cases:
- Safer than lists
- Hashable → usable as dictionary keys
- Lightweight and fast

---

## ⚡ List Comprehensions

List comprehensions allow you to create lists in a single line:

```python
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
```

You can also use conditions:

```python
even = [x for x in range(10) if x % 2 == 0]
```

Nested comprehensions are also possible!

---

## 🎯 Goal

- Understand how and when to use tuples
- Master list comprehensions for clean, powerful list creation
