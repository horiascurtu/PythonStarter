# Day 13 - Solutions

# Exercise 1:
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("That is not a valid number.")

# Exercise 2:
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid input.")

# Exercise 3:
my_list = [1, 2, 3]
try:
    print(my_list[5])
except IndexError:
    print("That index does not exist.")

# Exercise 4:
def check_positive(n):
    if n < 0:
        raise ValueError("Negative number not allowed")
    return n

# Exercise 5 (Bonus):
try:
    with open("nonexistent.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("The file was not found.")
