# 🔁 Day 7: For Loops in Python

Today you'll learn how to **repeat actions using loops**. The `for` loop is used to go through sequences like lists, strings, or ranges.

---

## 🧠 What You’ll Learn
- How `for` loops work
- Looping through a list or string
- Using `range()` with loops
- Nesting loops
- The `break` and `continue` keywords

---

## 🔄 The For Loop

Basic syntax:

```python
for item in collection:
    # Do something
```

Example:

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

---

## 🔢 Using `range()`

The `range()` function generates a sequence of numbers:

```python
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4
```

```python
for i in range(1, 6):
    print(i)  # 1 to 5
```

---

## 🔁 Looping through a string

```python
for char in "hello":
    print(char)
```

---

## ⛔ break and continue

- `break`: exits the loop early
- `continue`: skips to the next iteration

```python
for num in range(10):
    if num == 5:
        break
    print(num)
```

```python
for num in range(5):
    if num == 2:
        continue
    print(num)
```

---

## 🎯 Today’s Challenge

Loop through numbers and lists in different ways. Try the tasks in `exercitii.py`, and check the answers in `solutii.py`.

➡️ Coming up: **While loops and loop control**
