# 🖨️ Day 4: Input and Output in Python

Today you’ll learn how to **interact with users** by taking input from the keyboard and displaying output on the screen. These are the basic building blocks of any interactive program!

---

## 🧠 What You’ll Learn
- How to display information using `print()`
- How to take input from users with `input()`
- How to format output
- How to convert input data to the right type

---

## 🖨️ Output with `print()`

The `print()` function displays information to the console.

```python
print("Hello, world!")
```

You can print multiple things:

```python
name = "Alice"
print("Your name is", name)
```

---

## ⌨️ Input with `input()`

Use `input()` to ask the user for information. The input is always a **string**!

```python
name = input("What's your name? ")
print("Nice to meet you,", name)
```

---

## 🔄 Type Conversion

Since `input()` returns a string, you may need to convert it:

```python
age = input("Enter your age: ")
age = int(age)
print("Next year you’ll be", age + 1)
```

---

## 🎨 Formatting Output

Use `f-strings` to make your output cleaner:

```python
name = "Alice"
age = 30
print(f"{name} is {age} years old.")
```

---

## 🎯 Today’s Challenge

Work with user input and formatted output in `exercitii.py`. Check your answers in `solutii.py`.

➡️ Next up: **Conditions (if/else)!**
