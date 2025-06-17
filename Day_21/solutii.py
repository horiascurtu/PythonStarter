# Day 21 - Solutions

import json

# Exercise 1:
data = {"name": "Alice", "age": 30}
json_str = json.dumps(data)
print(json_str)

# Exercise 2:
with open("user.json", "w") as f:
    json.dump(data, f)

# Exercise 3:
with open("user.json", "r") as f:
    loaded = json.load(f)
    print(loaded)

# Exercise 4:
s = '{"fruit": "apple", "qty": 10}'
obj = json.loads(s)
print(obj["fruit"])

# Exercise 5 (Bonus):
users = [
    {"name": "Ana", "age": 28},
    {"name": "Mihai", "age": 34}
]
with open("users.json", "w") as f:
    json.dump(users, f, indent=4)
