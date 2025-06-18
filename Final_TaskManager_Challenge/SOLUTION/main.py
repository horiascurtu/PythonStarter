import argparse
from utils.core import add_task, list_tasks, mark_done, remove_task
from utils.logger import setup_logging

setup_logging()

parser = argparse.ArgumentParser(description="🗂️ Task Manager CLI")
parser.add_argument("command", choices=["add", "list", "done", "remove"])
parser.add_argument("arg", nargs="?", help="Task description or index")

args = parser.parse_args()

if args.command == "add" and args.arg:
    add_task(args.arg)
elif args.command == "list":
    list_tasks()
elif args.command == "done" and args.arg:
    mark_done(int(args.arg))
elif args.command == "remove" and args.arg:
    remove_task(int(args.arg))
else:
    print("⚠️ Invalid usage. Use --help for guidance.")
