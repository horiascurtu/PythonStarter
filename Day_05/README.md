# 🔀 Day 5: Conditional Statements (if / elif / else)

Today you’ll learn how to **make decisions in your code**. Conditional statements allow your program to react differently based on different situations.

---

## 🧠 What You’ll Learn
- `if`, `elif`, and `else` statements
- Comparison and logical conditions in decisions
- Nesting and chaining conditions
- Writing simple decision-based programs

---

## 📌 Basic Syntax

```python
age = 18

if age >= 18:
    print("You're an adult.")
elif age >= 13:
    print("You're a teenager.")
else:
    print("You're a child.")
```

### Important:
- Indentation matters in Python. Use 4 spaces.
- You can have as many `elif` statements as needed.
- `else` is optional, but runs if no condition is met.

---

## 🔁 Logical Conditions

You can combine conditions using:
- `and`: both must be True
- `or`: at least one must be True
- `not`: reverses the condition

```python
age = 25
has_ticket = True

if age >= 18 and has_ticket:
    print("You can enter the event.")
```

---

## 🎯 Today’s Challenge

Practice writing conditions and decision-making logic in `exercitii.py`. Check your answers in `solutii.py`.

➡️ Coming next: **Lists and Loops!**
