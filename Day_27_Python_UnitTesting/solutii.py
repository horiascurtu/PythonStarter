# Day 27 - Solutions

import requests

# Exercise 1:
r = requests.get("https://api.github.com")
print(r.status_code)

# Exercise 2:
print(r.json())

# Exercise 3:
res = requests.get("https://api.github.com/users/octocat")
data = res.json()
print("Public repos:", data["public_repos"])

# Exercise 4:
ip = requests.get("https://api.ipify.org?format=json")
print("IP Address:", ip.json()["ip"])

# Exercise 5 (Bonus):
response = requests.get("https://api.github.com")
if response.status_code == 200:
    print("Success:", response.json())
else:
    print("Failed with status:", response.status_code)
