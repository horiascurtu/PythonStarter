# Day 29 - CLI To-Do Project Solution

import argparse
import json
import os

DATA_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(description):
    tasks = load_tasks()
    tasks.append({"task": description, "done": False})
    save_tasks(tasks)
    print(f'Task added: "{description}"')

def show_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks, start=1):
        status = "[x]" if task["done"] else "[ ]"
        print(f"{idx}. {status} {task['task']}")

def remove_task(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f'Removed: {removed["task"]}')
    else:
        print("Invalid index.")

def mark_done(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        tasks[index - 1]["done"] = True
        save_tasks(tasks)
        print(f'Marked as done: {tasks[index - 1]["task"]}')
    else:
        print("Invalid index.")

parser = argparse.ArgumentParser(description="Simple To-Do CLI")
parser.add_argument("command", help="add/show/remove/done")
parser.add_argument("arg", nargs="?", help="Task description or index")
args = parser.parse_args()

if args.command == "add" and args.arg:
    add_task(args.arg)
elif args.command == "show":
    show_tasks()
elif args.command == "remove" and args.arg:
    remove_task(int(args.arg))
elif args.command == "done" and args.arg:
    mark_done(int(args.arg))
else:
    print("Invalid command or missing argument.")
