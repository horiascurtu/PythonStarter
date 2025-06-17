# 🧬 Day 17: Inheritance & Encapsulation in Python OOP

Welcome to **Day 17**! Today you’ll deepen your OOP skills by learning about **inheritance** (reusing classes) and **encapsulation** (controlling access to data). These concepts are key to writing scalable, modular code.

---

## 🧠 What You’ll Learn
- What is inheritance?
- How to create a child class
- Using `super()` to call the parent constructor
- Method overriding
- What is encapsulation?
- Private attributes and access control

---

## 🧬 What is Inheritance?

**Inheritance** allows a class (child/subclass) to **reuse and extend** the functionality of another class (parent/base).

### Example:

```python
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

d = Dog()
d.speak()  # Woof!
```

---

## 🔗 Using `super()`

The `super()` function lets you call methods from the parent class:

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
```

---

## 🔄 Method Overriding

If a child class defines a method with the **same name** as in the parent, it **overrides** it.

---

## 🔒 What is Encapsulation?

**Encapsulation** means hiding internal data to protect it from unintended modification.

Python uses **convention** for access control:
- `public`: `name`
- `_protected`: `_name`
- `__private`: `__name` (name mangling)

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
```

---

## 🛡 Why Encapsulation?

- Protect sensitive data
- Control how data is accessed/changed
- Provide clean interfaces for interacting with objects

---

## 🧰 Summary Table

| Term             | Meaning                                 |
|------------------|-----------------------------------------|
| Inheritance      | Subclass inherits from a parent class   |
| `super()`        | Call parent class methods/constructors  |
| Overriding       | Replace parent method in child class    |
| Encapsulation    | Hide data using private/protected names |
| `__attribute`    | Name-mangled private variable           |

---

## 🏗 Real-World Analogy

- **Class Animal**: has general traits (e.g. move, breathe)
- **Class Bird**: inherits from Animal and adds `fly()`
- **Encapsulation**: like a car engine—you can drive, but not touch the internal mechanics directly

---

## 🎯 Practice Time!

Create base classes and subclasses. Work with protected/private attributes and methods.

Try the exercises in `exercitii.py`. Check the answers in `solutii.py`.

➡️ Coming soon: **Day 18 – List Comprehensions & Functional Style**
