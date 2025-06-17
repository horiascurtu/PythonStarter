# Day 9 - Solutions

# Exercise 1:
person = {
    "name": "John",
    "age": 30,
    "favorite_color": "blue"
}

# Exercise 2:
print(person["age"])

# Exercise 3:
person["city"] = "London"
print(person)

# Exercise 4:
for key, value in person.items():
    print(f"{key}: {value}")

# Exercise 5 (Bonus):
key = input("Enter a key to look up: ")
print(person.get(key, "Not found"))
