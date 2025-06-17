# 🔁 Day 8: While Loops in Python

Today you'll learn how to use **while loops**, which repeat a block of code as long as a condition is true.

---

## 🧠 What You’ll Learn
- Syntax of a `while` loop
- Infinite loops and how to avoid them
- Loop control with `break` and `continue`
- Creating simple loops with counters and conditions

---

## 🔄 Basic `while` Loop Syntax

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

### Output:
```
0
1
2
3
4
```

The loop continues as long as the condition (`i < 5`) is `True`.

---

## ⚠️ Infinite Loops

Be careful: if you forget to update your condition, the loop might run forever.

```python
# Infinite loop - DON'T DO THIS
while True:
    print("This never ends...")
```

Use `break` to stop the loop if needed.

---

## ⛔ `break` and `continue`

- `break`: exit the loop completely
- `continue`: skip the current iteration

```python
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
```

---

## ✅ Common Use: User Input

```python
password = ""
while password != "secret":
    password = input("Enter password: ")
print("Access granted!")
```

---

## 🎯 Today’s Challenge

Use `while` loops to repeat actions based on conditions and user input. Check the tasks in `exercitii.py` and answers in `solutii.py`.

➡️ Next up: **Dictionaries – key-value power!**
