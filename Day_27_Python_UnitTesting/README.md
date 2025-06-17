# 🌐 Day 27: Introduction to APIs and JSON in Python

Welcome to **Day 27**! Today you'll learn how to work with **APIs (Application Programming Interfaces)** — a key skill in modern development. You'll use Python to send HTTP requests and handle responses in JSON format.

---

## 🧠 What You’ll Learn
- What an API is
- Sending HTTP requests with `requests`
- Understanding status codes
- Parsing JSON responses
- Accessing data from public APIs

---

## 🤖 What is an API?

An **API** lets your Python code communicate with another application or service.

Example: You can use an API to get weather data, cryptocurrency prices, or search results from YouTube.

---

## 📡 Making an API Call with `requests`

```python
import requests

url = "https://api.github.com"
response = requests.get(url)
print(response.status_code)
print(response.json())  # Parse JSON response
```

---

## 🧾 JSON Data

Most APIs return data in **JSON** format.

```json
{
  "login": "octocat",
  "public_repos": 8
}
```

Access it like a Python dictionary:

```python
data = response.json()
print(data["login"])
```

---

## 📊 Status Codes

| Code | Meaning            |
|------|---------------------|
| 200  | OK                  |
| 201  | Created             |
| 400  | Bad Request         |
| 401  | Unauthorized        |
| 404  | Not Found           |
| 500  | Server Error        |

---

## 🧪 Example: GitHub API

```python
res = requests.get("https://api.github.com/users/octocat")
if res.status_code == 200:
    data = res.json()
    print("Public repos:", data["public_repos"])
```

---

## 🧰 Summary

| Task               | Function                        |
|--------------------|----------------------------------|
| Make GET request   | `requests.get(url)`              |
| View status code   | `response.status_code`           |
| Parse JSON         | `response.json()`                |
| Extract value      | `data["key"]`                    |

---

## 🎯 Practice Time!

Use an API to fetch data, extract information from a JSON response, and print meaningful output.

Exercises are in `exercitii.py`, and solutions in `solutii.py`.

➡️ Up next: **Day 28 – Intro to Testing with `unittest`**
