# Day 12 - Solutions

# Exercise 1:
def greet(name="Guest"):
    print(f"Hello, {name}!")

# Exercise 2:
def average(*nums):
    return sum(nums) / len(nums)

# Exercise 3:
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Exercise 4:
pairs = [("a", 3), ("b", 1), ("c", 2)]
pairs.sort(key=lambda x: x[1])
print(pairs)

# Exercise 5 (Bonus):
def outer(message):
    def inner():
        print(f"Message: {message}")
    return inner

f = outer("Hello from inside!")
f()
