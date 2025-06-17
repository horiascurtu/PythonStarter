# ➕ Day 3: Python Operators – Mastering Calculations & Logic

Welcome to Day 3! Today we’ll explore how to do math and logic with **operators**. These are symbols that let Python perform actions like addition, comparison, and decision-making.

---

## 🧠 What You’ll Learn
- 🔢 **Arithmetic operators**: do math
- 🧪 **Comparison operators**: check values
- 🔐 **Logical operators**: make decisions
- 📝 **Assignment operators**: update values

---

## 🔢 Arithmetic Operators

| Operator | Description            | Example         | Result |
|----------|------------------------|-----------------|--------|
| `+`      | Addition                | `3 + 2`         | `5`    |
| `-`      | Subtraction             | `7 - 4`         | `3`    |
| `*`      | Multiplication          | `3 * 4`         | `12`   |
| `/`      | Division (float)        | `10 / 4`        | `2.5`  |
| `//`     | Floor Division          | `10 // 4`       | `2`    |
| `%`      | Modulus (remainder)     | `10 % 4`        | `2`    |
| `**`     | Exponentiation          | `2 ** 3`        | `8`    |

### Example:
```python
a = 10
b = 3
print(a + b)   # 13
print(a ** b)  # 1000
print(a % b)   # 1
```

---

## 🔍 Comparison Operators

Used to compare two values and return `True` or `False`.

| Operator | Description            | Example       | Result    |
|----------|------------------------|---------------|-----------|
| `==`     | Equal to               | `5 == 5`      | `True`    |
| `!=`     | Not equal to           | `5 != 3`      | `True`    |
| `>`      | Greater than           | `7 > 2`       | `True`    |
| `<`      | Less than              | `3 < 9`       | `True`    |
| `>=`     | Greater than or equal  | `6 >= 6`      | `True`    |
| `<=`     | Less than or equal     | `4 <= 5`      | `True`    |

---

## ⚙️ Logical Operators

Combine multiple boolean expressions.

| Operator | Description             | Example                      | Result   |
|----------|-------------------------|------------------------------|----------|
| `and`    | True if both are True   | `True and False`             | `False`  |
| `or`     | True if at least one is True | `True or False`       | `True`   |
| `not`    | Reverses a boolean      | `not True`                   | `False`  |

### Example:
```python
x = True
y = False

print(x and y)  # False
print(x or y)   # True
print(not x)    # False
```

---

## ✍️ Assignment Operators

| Operator | Example        | Meaning             |
|----------|----------------|---------------------|
| `=`      | `x = 5`        | assign value 5      |
| `+=`     | `x += 3`       | `x = x + 3`         |
| `-=`     | `x -= 1`       | `x = x - 1`         |
| `*=`     | `x *= 2`       | `x = x * 2`         |
| `/=`     | `x /= 2`       | `x = x / 2`         |

---

## 🎯 Today’s Challenge

Practice using all types of operators in `exercitii.py`. Then check your answers in `solutii.py`.

👉 Up next: **Making decisions with if/else!**
