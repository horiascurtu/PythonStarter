# Day 16 - Solutions

# Exercise 1:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, I'm {self.name}!")

# Exercise 2:
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def info(self):
        print(f"{self.brand} - {self.year}")

# Exercise 3:
p1 = Person("Alice", 30)
p2 = Person("Bob", 22)
p1.greet()
p2.greet()

# Exercise 4:
# Done in Exercises 1 & 2 with __init__

# Exercise 5 (Bonus):
class Citizen:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_adult(self):
        return self.age >= 18
