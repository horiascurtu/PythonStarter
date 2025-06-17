# 🧪 Day 18: List Comprehensions & Functional Style in Python

Welcome to **Day 18**! Today you’ll explore **list comprehensions**, a powerful and elegant way to build lists in Python. You'll also get a taste of the **functional programming style** using `map()`, `filter()`, and `lambda`.

---

## 🧠 What You’ll Learn
- What list comprehensions are and how to use them
- `map()` for transforming data
- `filter()` for selecting data
- `lambda` functions for writing anonymous functions
- When to use comprehensions vs loops

---

## 🔁 Traditional List Creation

```python
squares = []
for x in range(10):
    squares.append(x ** 2)
```

---

## ⚡ List Comprehension

```python
squares = [x ** 2 for x in range(10)]
```

### Syntax:

```python
[expression for item in iterable if condition]
```

### Examples:

```python
evens = [x for x in range(20) if x % 2 == 0]
names = [name.upper() for name in ["alice", "bob", "carol"]]
```

---

## 🧰 Using `map()` and `filter()`

### `map(function, iterable)`

Applies a function to each item:

```python
def double(x):
    return x * 2

nums = [1, 2, 3]
doubled = list(map(double, nums))
```

You can also use `lambda`:

```python
doubled = list(map(lambda x: x * 2, nums))
```

### `filter(function, iterable)`

Keeps only the items where the function returns `True`:

```python
even = list(filter(lambda x: x % 2 == 0, range(10)))
```

---

## 💡 lambda Functions Recap

```python
lambda arguments: expression
```

Example:

```python
square = lambda x: x * x
print(square(5))  # 25
```

---

## 🔍 When to Use Each

| Technique           | Best For                          |
|---------------------|-----------------------------------|
| List Comprehension  | Readable, quick list construction |
| `map()`             | Applying functions to items       |
| `filter()`          | Selecting items                   |
| `lambda`            | One-line throwaway functions      |

---

## 🧠 Nested Comprehensions

```python
matrix = [[i * j for j in range(3)] for i in range(3)]
```

---

## 🎯 Practice Time!

Use comprehensions and functional tools (`map`, `filter`, `lambda`) to manipulate lists concisely.

Tasks are in `exercitii.py`, and solutions in `solutii.py`.

➡️ Coming next: **Day 19 – Recursion and Problem-Solving**
