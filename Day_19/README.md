# 🔁 Day 19: Recursion in Python – Thinking Recursively

Welcome to **Day 19**! Today you’ll learn how to write **recursive functions** — functions that call themselves to solve problems. Recursion is a powerful technique in computer science, especially for tasks like traversing trees, solving puzzles, or breaking problems into smaller parts.

---

## 🧠 What You’ll Learn
- What recursion is
- How to define a recursive function
- Base case vs recursive case
- Common recursion examples
- Pros and cons of recursion

---

## 🧬 What is Recursion?

**Recursion** is when a function calls itself:

```python
def countdown(n):
    if n <= 0:
        print("Done!")
    else:
        print(n)
        countdown(n - 1)
```

---

## 🔁 Base Case and Recursive Case

Every recursive function must have:

1. **Base case** – when to stop calling itself
2. **Recursive case** – call itself with a smaller/simpler input

Example: factorial

```python
def factorial(n):
    if n == 0:
        return 1  # base case
    else:
        return n * factorial(n - 1)  # recursive case
```

---

## 🧮 Examples

### Sum of numbers:

```python
def sum_to_n(n):
    if n == 1:
        return 1
    return n + sum_to_n(n - 1)
```

### Fibonacci (inefficient version):

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

---

## ⚠️ Recursion vs Iteration

| Feature     | Recursion                         | Iteration                      |
|-------------|-----------------------------------|--------------------------------|
| Code style  | Short, elegant                    | More explicit and readable     |
| Memory use  | Can be heavy (call stack)         | More efficient                 |
| Use case    | Tree structures, divide & conquer | Loops, repetitive tasks        |

---

## 🛡 Tips for Recursion

- Always define a **base case** to avoid infinite recursion
- Be careful with performance on large inputs
- Use recursion for problems that naturally break into subproblems

---

## 🧰 When to Use Recursion

- Factorial, Fibonacci
- Tree/graph traversal
- Divide and conquer algorithms (e.g. merge sort)
- Nested data structures (e.g. nested lists, JSON)

---

## 🎯 Practice Time!

Practice writing recursive functions to build confidence. Tasks are in `exercitii.py`, and solutions in `solutii.py`.

➡️ Next up: **Day 20 – Date and Time in Python**
