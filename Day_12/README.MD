# 🧠 Day 12: Advanced Functions in Python

Welcome to Day 12! Today you'll explore more **advanced features** of functions in Python. These tools help you write more flexible, powerful, and elegant code.

---

## 🧠 What You’ll Learn
- Default parameters
- Keyword arguments
- `*args` and `**kwargs`
- Lambda (anonymous) functions
- Nested functions
- Return best practices

---

## ⚙️ Default Parameters

You can provide default values for function arguments:

```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()          # Hello, Guest!
greet("Alice")   # Hello, Alice!
```

---

## 🔑 Keyword Arguments

You can pass arguments by name, which makes code clearer:

```python
def user_info(name, age):
    print(f"{name} is {age} years old.")

user_info(age=30, name="John")
```

---

## 🌟 *args – Variable Positional Arguments

Use `*args` when you want a function to accept **any number of positional arguments**:

```python
def add_all(*numbers):
    total = sum(numbers)
    return total

print(add_all(1, 2, 3))  # 6
print(add_all(5, 10))    # 15
```

`*args` is a tuple of arguments.

---

## 🌟 **kwargs – Variable Keyword Arguments

Use `**kwargs` when your function accepts **any number of keyword arguments**:

```python
def print_info(**data):
    for key, value in data.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25)
```

`**kwargs` is a dictionary of key-value pairs.

---

## ⚡ Lambda Functions

A **lambda** is a small anonymous function used for quick operations:

```python
square = lambda x: x * x
print(square(4))  # 16
```

Used often with `map()`, `filter()`, or sorting:

```python
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x * x, nums))
print(squared)
```

---

## 🔁 Nested Functions

You can define functions inside functions:

```python
def outer():
    def inner():
        print("Inside inner")
    inner()

outer()
```

---

## ✅ Best Practices

- Keep functions short and focused
- Use `*args` and `**kwargs` when you need flexibility
- Avoid overusing lambdas in complex logic

---

## 🎯 Practice Time!

Use advanced techniques like default parameters, `*args`, `**kwargs`, and lambdas to improve your functions.

Exercises are in `exercitii.py`, and solutions in `solutii.py`.

➡️ Next up: **Exception Handling – Making your code safe!**
