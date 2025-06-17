# 🌐 Day 26: Web Scraping with `requests` and `BeautifulSoup`

Welcome to **Day 26**! Today you'll learn how to extract data from web pages using **web scraping** with `requests` and `BeautifulSoup`. This is great for collecting information like headlines, stock prices, or product listings.

---

## 🧠 What You’ll Learn
- How to make HTTP requests with `requests`
- Parsing HTML with `BeautifulSoup`
- Selecting and extracting data from tags
- Navigating HTML trees
- Avoiding common pitfalls

---

## 📥 Installing Required Libraries

```bash
pip install requests beautifulsoup4
```

---

## 🔗 Fetching a Web Page

```python
import requests

response = requests.get("https://example.com")
print(response.text)  # raw HTML
```

---

## 🧽 Parsing HTML with BeautifulSoup

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, "html.parser")
print(soup.title.text)
```

---

## 🧭 Navigating HTML

```python
# Find first <p> tag
paragraph = soup.find("p")

# Find all <a> tags
links = soup.find_all("a")

# Get attributes
for link in links:
    print(link.get("href"))
```

---

## 🔎 Searching by Class or ID

```python
# By class name
items = soup.find_all("div", class_="product")

# By id
title = soup.find(id="main-title")
```

---

## ⚠️ Be Respectful

- Check `robots.txt` on the website
- Don't overload servers
- Use scraping ethically

---

## 🧰 Summary

| Task               | Method                       |
|--------------------|------------------------------|
| Get page           | `requests.get(url)`          |
| Parse HTML         | `BeautifulSoup(..., "html.parser")` |
| Find one tag       | `soup.find()`                |
| Find all tags      | `soup.find_all()`            |
| Access attributes  | `tag.get("href")`            |

---

## 🎯 Practice Time!

Scrape data from a basic HTML page, extract titles or links, and filter based on class or tag. Exercises are in `exercitii.py`, solutions in `solutii.py`.

➡️ Next: **Day 27 – Introduction to APIs and JSON**
