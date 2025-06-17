# Day 25 - Solutions

# Exercise 1:
# Command: python -m venv venv

# Exercise 2:
# Activate:
# On Windows: venv\Scripts\activate
# On macOS/Linux: source venv/bin/activate
# Then: pip install requests

# Exercise 3:
# pip freeze > requirements.txt

# Exercise 4:
# python -m venv new_env
# source new_env/bin/activate (or new_env\Scripts\activate)
# pip install -r requirements.txt

# Exercise 5 (Bonus):
import requests

response = requests.get("https://api.github.com")
print(response.status_code)
