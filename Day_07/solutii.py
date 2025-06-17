# Day 7 - Solutions

# Exercise 1:
for i in range(1, 11):
    print(i)

# Exercise 2:
name = "Alice"
for char in name:
    print(char)

# Exercise 3:
movies = ["Inception", "Matrix", "Interstellar", "Titanic", "The Godfather"]
for movie in movies:
    print(movie)

# Exercise 4:
for i in range(2, 21, 2):
    print(i)

# Exercise 5:
for i in range(11):
    if i == 3:
        continue
    if i == 8:
        break
    print(i)

# Exercise 6 (Bonus):
numbers = [1, 4, 7, 10, 13]
for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
