tasks = []

for i in range(3):
    task = input("Enter a task: ")
    tasks.append(task)

print("Your tasks:")
for t in tasks:
    print("-", t)
