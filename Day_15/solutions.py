# Day 15 - Solutions

# Exercise 1:
with open("data.txt", "w") as f:
    f.write("Hello, File!")

# Exercise 2:
with open("data.txt", "r") as f:
    print(f.read())

# Exercise 3:
with open("data.txt", "a") as f:
    f.write("\nAppending this line.")

# Exercise 4:
with open("data.txt", "r") as f:
    for line in f:
        print(line.strip().upper())

# Exercise 5 (Bonus):
items = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
with open("fruits.txt", "w") as f:
    for item in items:
        f.write(item + "\n")
