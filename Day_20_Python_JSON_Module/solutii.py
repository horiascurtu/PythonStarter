# Day 20 - Solutions

from datetime import datetime, date, timedelta

# Exercise 1:
now = datetime.now()
print(now)

# Exercise 2:
birthday = date(1990, 5, 17)
print(birthday)

# Exercise 3:
today = date.today()
new_year = date(today.year + 1, 1, 1)
diff = new_year - today
print(f"Days until New Year: {diff.days}")

# Exercise 4:
dt = datetime.strptime("2025-12-25", "%Y-%m-%d")
print(dt)

# Exercise 5 (Bonus):
print(datetime.now().strftime("%d/%m/%Y"))
