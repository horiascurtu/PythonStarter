# Day 5 - Solutions

# Exercise 1:
age = int(input("Enter your age: "))
if age <= 12:
    print("You are a child.")
elif age <= 17:
    print("You are a teenager.")
else:
    print("You are an adult.")

# Exercise 2:
num = float(input("Enter a number: "))
if num > 0:
    print("Positive number.")
elif num < 0:
    print("Negative number.")
else:
    print("Zero.")

# Exercise 3:
username = input("Enter username: ")
if username == "admin":
    print("Access granted.")
else:
    print("Access denied.")

# Exercise 4:
raining = input("Is it raining? (yes/no): ").lower()
umbrella = input("Do you have an umbrella? (yes/no): ").lower()
if raining == "yes" and umbrella == "yes":
    print("You can go outside.")
elif raining == "yes" and umbrella == "no":
    print("Better stay inside.")
else:
    print("Enjoy the weather!")

# Exercise 5 (Bonus):
score = int(input("Enter your score (0-100): "))
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
