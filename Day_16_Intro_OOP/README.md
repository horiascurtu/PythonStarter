# 🧱 Day 16: Introduction to Classes and OOP in Python

Welcome to **Day 16**! You're now entering the world of **Object-Oriented Programming (OOP)** — a powerful way to organize and structure your code by modeling real-world objects and behaviors.

---

## 🧠 What You’ll Learn
- What is OOP and why it matters
- How to define and use a `class`
- How to create and use `objects`
- What is the `__init__` constructor
- What is the `self` keyword
- How to create attributes and methods

---

## 🧰 What is OOP?

**Object-Oriented Programming** is a style of programming that allows you to group:
- **Data (attributes)** and
- **Behaviors (methods)**

into one unit called an **object**.

This is useful for:
- Modeling real-life entities (e.g. cars, users, animals)
- Keeping code organized, reusable, and scalable

---

## 🏗 What is a Class?

A **class** is a **blueprint** for creating **objects**.

Example:

```python
class Dog:
    def bark(self):
        print("Woof!")
```

An **object** is an **instance** of that class:

```python
my_dog = Dog()
my_dog.bark()  # Woof!
```

---

## 🧱 The `__init__()` Constructor

The `__init__()` method is **automatically called** when you create a new object. It sets up the initial state.

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")

dog1 = Dog("Rex")
dog1.bark()  # Rex says Woof!
```

---

## 🔑 Understanding `self`

The `self` parameter refers to **the current object instance**. It allows access to the object’s variables and methods.

```python
class Cat:
    def meow(self):
        print("Meow!")

kitty = Cat()
kitty.meow()
```

Under the hood: `kitty.meow()` → `Cat.meow(kitty)`

---

## 🧾 Instance Attributes

Attributes are variables that **belong to a specific object**. You usually set them in `__init__()`.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 30)
print(p.name)  # Alice
```

---

## 🔁 Instance Methods

Instance methods are **functions inside a class** that operate on object data.

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
```

---

## ✅ Advantages of OOP

- **Encapsulation**: Bind data and behavior together
- **Reusability**: Define a class once and reuse it
- **Maintainability**: Easier to manage large codebases
- **Scalability**: OOP code can grow without becoming messy

---

## 🧰 Summary Table

| Concept      | Description                            | Example                     |
|--------------|----------------------------------------|-----------------------------|
| Class        | Blueprint for objects                  | `class Car:`                |
| Object       | Instance of a class                    | `my_car = Car()`            |
| `__init__`   | Constructor method                     | `def __init__(self):`       |
| Attribute    | Variable inside an object              | `self.color = "blue"`       |
| Method       | Function inside a class                | `def drive(self):`          |
| `self`       | Refers to current object               | `self.name`                 |

---

## 📦 Real-Life Analogy

Class: **Cookie Cutter**  
Object: **Each cookie made from the cutter**

---

## 🎯 Practice Time!

Define your own classes and create objects with attributes and methods.
- Check `exercitii.py` to apply what you’ve learned.
- Validate your answers in `solutii.py`.

➡️ Next: **Day 17 - Inheritance and Encapsulation in OOP**
