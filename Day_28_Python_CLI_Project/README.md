# 🧪 Day 28: Introduction to Testing with `unittest` in Python

Welcome to **Day 28**! Today you’ll learn how to write **automated tests** for your code using the built-in `unittest` module. Testing is essential for ensuring your code behaves as expected and remains stable over time.

---

## 🧠 What You’ll Learn
- What unit testing is
- How to create and run test cases
- Using assertions to validate results
- Organizing tests in test classes
- Running tests from the terminal

---

## 🔍 What is Unit Testing?

**Unit testing** involves writing small tests for individual functions or units of code.

---

## 🛠 Basic Example

```python
import unittest

def add(a, b):
    return a + b

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == '__main__':
    unittest.main()
```

---

## ✅ Common Assertions

| Assertion                     | Checks That...                          |
|-------------------------------|------------------------------------------|
| `assertEqual(a, b)`           | a == b                                  |
| `assertNotEqual(a, b)`        | a != b                                  |
| `assertTrue(x)`               | bool(x) is True                         |
| `assertFalse(x)`              | bool(x) is False                        |
| `assertIn(a, b)`              | a in b                                  |
| `assertIsNone(x)`             | x is None                               |

---

## 🧪 Running Tests

From the command line:

```bash
python test_script.py
```

You’ll see output like:

```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

---

## 📦 Organizing Tests

Use descriptive names for your test functions and separate them from your core logic for clarity and maintainability.

---

## 🧰 Summary

- Use `unittest.TestCase` to group tests
- Use `assert` methods to validate results
- Use `unittest.main()` to run tests automatically

---

## 🎯 Practice Time!

Write unit tests for simple functions and run them using `unittest`. Exercises are in `exercitii.py`, and solutions in `solutii.py`.

➡️ Coming next: **Day 29 – Building a Small CLI Project**
