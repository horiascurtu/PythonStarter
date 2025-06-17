# 📚 Day 6: Understanding Python Lists – Your First Collection

Welcome! Today you're going to learn about **lists**, one of Python's most powerful and flexible data structures. Lists allow you to **store multiple items in a single variable**, and they're used everywhere in programming.

---

## 🧠 What You’ll Learn
- What a list is and why it's useful
- How to create a list
- Accessing, modifying, and removing elements
- Useful list methods
- How to loop through lists

---

## 📦 What is a List?

A **list** is an ordered collection of items. You can think of it like a container that holds multiple values.

```python
fruits = ["apple", "banana", "cherry"]
```

Each item in the list is **indexed**, starting from 0.

---

## 🛠 Creating Lists

You define a list using square brackets `[]`.

```python
numbers = [1, 2, 3, 4]
names = ["Alice", "Bob", "Charlie"]
mixed = [42, "hello", True]
```

Lists can even contain **other lists**:
```python
nested = [[1, 2], [3, 4]]
```

---

## 🔍 Accessing Elements

You can access any item by its index:

```python
print(fruits[0])  # apple
print(fruits[1])  # banana
print(fruits[-1]) # cherry (last item)
```

---

## 🧾 Modifying Lists

```python
fruits[1] = "kiwi"
print(fruits)  # ['apple', 'kiwi', 'cherry']
```

---

## ➕ Adding Items

- Add to the end:
```python
fruits.append("orange")
```

- Insert at a specific index:
```python
fruits.insert(1, "mango")
```

---

## ❌ Removing Items

- Remove by value:
```python
fruits.remove("banana")
```

- Remove by index:
```python
del fruits[0]
```

- Pop last item (and get it):
```python
last = fruits.pop()
```

---

## 🧰 Other Useful Methods

```python
fruits.sort()     # Sort alphabetically
fruits.reverse()  # Reverse the list
len(fruits)       # Number of items in list
```

---

## 🔁 Looping Through Lists

```python
for fruit in fruits:
    print(fruit)
```

You can also loop using indexes:

```python
for i in range(len(fruits)):
    print(fruits[i])
```

---

## 🎯 Practice Time!

- Work with real-world lists (like favorite foods)
- Practice adding, removing, and sorting
- Use loops to display your list items

All tasks are in `exercitii.py`. Check your answers in `solutii.py`.

➡️ Coming up: **For loops in detail!**
