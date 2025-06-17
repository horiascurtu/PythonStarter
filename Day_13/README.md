# 🚨 Day 13: Exception Handling in Python – Writing Safe Programs

Errors happen. Whether it's invalid user input or a file that doesn't exist, your program needs to handle problems **gracefully**. That’s where **exception handling** comes in.

---

## 🧠 What You’ll Learn
- What exceptions are
- How to catch errors using `try`, `except`
- Using `else` and `finally`
- Common exception types
- Raising your own errors

---

## ❗ What is an Exception?

An **exception** is an error that occurs during program execution and interrupts the normal flow.

Example:

```python
x = int("abc")  # ValueError
```

This would crash your program unless handled properly.

---

## 🛡 Basic try/except

```python
try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("That’s not a number!")
```

---

## 🔍 Multiple except blocks

You can catch different errors with different responses.

```python
try:
    # risky code
except TypeError:
    # handle type errors
except ValueError:
    # handle value errors
```

---

## 🔄 else and finally

- `else`: runs **if no exception** occurred.
- `finally`: always runs, used for cleanup (closing files, etc).

```python
try:
    num = int(input("Enter number: "))
except ValueError:
    print("Invalid input.")
else:
    print("You entered:", num)
finally:
    print("Done!")
```

---

## 💥 Raising Exceptions

You can raise your own exceptions using `raise`:

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age
```

---

## 🧰 Common Exception Types

| Exception         | When it happens                         |
|------------------|------------------------------------------|
| `ValueError`      | Wrong value type (e.g. int("abc"))       |
| `ZeroDivisionError` | Division by 0                         |
| `TypeError`       | Wrong type used                         |
| `IndexError`      | List index out of range                 |
| `KeyError`        | Missing dictionary key                  |
| `FileNotFoundError` | File doesn't exist                    |

---

## 🧹 Best Practices

- Use specific exceptions (`ValueError`, not just `except:`)
- Keep `try` blocks short
- Use `finally` for cleanup (like closing files)

---

## ✅ Real World Example

```python
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
```

---

## 🎯 Practice Time!

Write programs that safely handle user input and runtime errors. Try the tasks in `exercitii.py` and check your answers in `solutii.py`.

➡️ Coming up: **Working with Modules and Libraries**
