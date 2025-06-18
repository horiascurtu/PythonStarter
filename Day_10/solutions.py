person = {
    "name": "Ana",
    "age": 28,
    "color": "blue"
}

person["hobby"] = "reading"
person["age"] = 29
del person["color"]

for key, value in person.items():
    print(f"{key}: {value}")
