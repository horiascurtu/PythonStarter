# 🧩 Day 11: Functions in Python – Reuse Your Code

Welcome to Day 11! Today you’ll learn how to write and use **functions** – one of the most powerful concepts in programming. Functions allow you to **organize**, **reuse**, and **simplify** your code.

---

## 🧠 What You’ll Learn
- What a function is
- How to define and call functions
- Parameters vs. arguments
- Return values
- Scope (local and global variables)

---

## 🔧 What is a Function?

A **function** is a reusable block of code that performs a specific task.

Instead of writing the same code over and over, you can define it once as a function.

---

## ✍️ Defining a Function

```python
def greet():
    print("Hello, world!")
```

To call the function:

```python
greet()
```

---

## 📥 Parameters and Arguments

You can pass data to functions using **parameters**:

```python
def greet(name):
    print(f"Hello, {name}!")
```

Call it with an **argument**:

```python
greet("Alice")
```

---

## 🔁 Returning Values

Use `return` to send data back from a function:

```python
def add(a, b):
    return a + b

result = add(3, 4)
print(result)  # 7
```

---

## 🧪 Multiple Parameters

Functions can take multiple inputs:

```python
def full_name(first, last):
    return f"{first} {last}"
```

---

## 📌 Scope: Local vs Global

Variables defined **inside** a function are **local** to that function:

```python
def say_hi():
    message = "Hi"
    print(message)

say_hi()
# print(message)  ❌ Error: message is not defined outside
```

---

## ✅ Why Use Functions?

- Reuse code instead of duplicating it
- Organize complex programs
- Break problems into smaller tasks

---

## 🧰 Function Tips

| Keyword   | Use                                 |
|-----------|--------------------------------------|
| `def`     | Define a new function                |
| `return`  | Return a value from a function       |
| `None`    | Returned automatically if no return  |

---

## 🎯 Practice Time!

Create your own functions with and without parameters, return values, and reuse them. Your tasks are in `exercitii.py`. Check your answers in `solutii.py`.

➡️ Coming up: **Advanced Functions – lambda, *args, and more!**
