# Day 19 - Solutions

# Exercise 1:
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Exercise 2:
def sum_to_n(n):
    if n == 1:
        return 1
    return n + sum_to_n(n - 1)

# Exercise 3:
def countdown(n):
    if n < 0:
        return
    print(n)
    countdown(n - 1)

# Exercise 4:
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Exercise 5 (Bonus):
def reverse_string(s):
    if len(s) <= 1:
        return s
    return s[-1] + reverse_string(s[:-1])
