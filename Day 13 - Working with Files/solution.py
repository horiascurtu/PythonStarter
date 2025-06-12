with open("message.txt", "w") as f:
    f.write("This is a message from Day 13!")

with open("message.txt", "r") as f:
    content = f.read()
    print(content)
