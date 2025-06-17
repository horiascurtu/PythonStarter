# Day 18 - Solutions

# Exercise 1:
squares = [x ** 2 for x in range(1, 11)]

# Exercise 2:
nums = [1, 2, 3, 4, 5, 6]
evens = [x for x in nums if x % 2 == 0]

# Exercise 3:
nums = [1, 2, 3]
tripled = list(map(lambda x: x * 3, nums))

# Exercise 4:
names = ["Ana", "Jonathan", "Leo", "Elizabeth"]
filtered = list(filter(lambda name: len(name) > 4, names))

# Exercise 5 (Bonus):
result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, range(21))))
