# Day 22 - Solutions

import logging

# Exercise 1:
logging.basicConfig(level=logging.INFO)
logging.info("Program started")

# Exercise 2:
logging.warning("This is a warning")
logging.error("This is an error")

# Exercise 3:
logging.basicConfig(filename="logfile.log", level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s")

# Exercise 4:
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        logging.error("Cannot divide by zero")

# Exercise 5 (Bonus):
def get_age():
    try:
        age = int(input("Enter your age: "))
        logging.info(f"User entered age: {age}")
        return age
    except ValueError:
        logging.error("Invalid input, not a number")
        return None
