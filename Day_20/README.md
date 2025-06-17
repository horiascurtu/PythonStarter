# ⏰ Day 20: Working with Dates and Times in Python

Welcome to **Day 20**! Today you’ll learn how to use Python's `datetime` module to handle dates, times, durations, and formatting. This is essential for logging, time-based calculations, and real-world apps like calendars or reminders.

---

## 🧠 What You’ll Learn
- How to get the current date and time
- How to create and format dates/times
- Timedelta (date arithmetic)
- Parsing strings into dates
- Common datetime operations

---

## 📆 Getting Current Date and Time

```python
from datetime import datetime

now = datetime.now()
print(now)
```

---

## 🏗 Creating Date and Time Objects

```python
from datetime import date, time, datetime

d = date(2024, 1, 1)
t = time(14, 30)
dt = datetime(2024, 1, 1, 14, 30)
```

---

## 🧮 Timedelta (Date Arithmetic)

```python
from datetime import timedelta

delta = timedelta(days=7)
new_date = datetime.now() + delta
print(new_date)
```

You can subtract, compare, and calculate differences between dates.

---

## 🧾 Formatting Dates (strftime)

```python
now = datetime.now()
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)
```

### Common Format Codes

| Code | Meaning            |
|------|--------------------|
| `%Y` | Year (2024)        |
| `%m` | Month (01–12)      |
| `%d` | Day of the month   |
| `%H` | Hour (00–23)       |
| `%M` | Minute             |
| `%S` | Second             |

---

## 🧪 Parsing Strings into Dates (strptime)

```python
date_str = "2024-06-17"
parsed_date = datetime.strptime(date_str, "%Y-%m-%d")
```

---

## ⏳ Difference Between Two Dates

```python
from datetime import datetime

d1 = datetime(2024, 6, 1)
d2 = datetime(2024, 6, 17)
diff = d2 - d1
print(diff.days)  # 16
```

---

## 🔁 Practical Uses

- Countdown timers
- Scheduling
- Logging events
- Measuring execution time

---

## 🧰 Summary

| Function                     | Use                              |
|------------------------------|----------------------------------|
| `datetime.now()`             | Current date and time            |
| `datetime(year, m, d, h, m)` | Create datetime object           |
| `timedelta(days=n)`          | Add/subtract time                |
| `strftime()`                 | Format datetime to string        |
| `strptime()`                 | Convert string to datetime       |

---

## 🎯 Practice Time!

Work with current time, format/parse strings, and calculate differences. Tasks are in `exercitii.py`, solutions in `solutii.py`.

➡️ Coming next: **Day 21 – Working with JSON**
