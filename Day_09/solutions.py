numbers = (7, 11, 42)
# numbers[0] = 10  # This will raise an error: tuples are immutable

squares = [x**2 for x in range(10)]
evens = [x for x in range(21) if x % 2 == 0]

print(squares)
print(evens)
