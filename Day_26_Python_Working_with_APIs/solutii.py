# Day 26 - Solutions

import requests
from bs4 import BeautifulSoup

# Exercise 1:
res = requests.get("https://example.com")
print(res.status_code)

# Exercise 2:
soup = BeautifulSoup(res.text, "html.parser")
print(soup.title.text)

# Exercise 3:
for a in soup.find_all("a"):
    print(a.get("href"))

# Exercise 4:
p = soup.find("p")
print(p.text)

# Exercise 5 (Bonus):
hrefs = [a.get("href") for a in soup.find_all("a") if a.get("href")]
print(hrefs)
