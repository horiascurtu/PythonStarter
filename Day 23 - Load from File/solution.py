tasks = []

with open("tasks.txt", "r") as f:
    for line in f:
        name, done = line.strip().split("|")
        tasks.append({"name": name, "done": done == "True"})

for task in tasks:
    print(task)
