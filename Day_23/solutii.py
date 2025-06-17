# Day 23 - Solutions

# Exercise 1:
# Run this script from the CLI with args: python script.py a b c
import sys
print(sys.argv)

# Exercise 2:
a = int(sys.argv[1])
b = int(sys.argv[2])
print(a + b)

# Exercise 3:
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("name")
parser.add_argument("age", type=int)
args = parser.parse_args()
print(f"Hello {args.name}, you are {args.age} years old.")

# Exercise 4:
parser = argparse.ArgumentParser()
parser.add_argument("filename")
args = parser.parse_args()

with open(args.filename, "r") as f:
    print(f.read())

# Exercise 5 (Bonus):
parser = argparse.ArgumentParser()
parser.add_argument("name")
parser.add_argument("--verbose", action="store_true")
args = parser.parse_args()

if args.verbose:
    print("Verbose mode is ON")
print(f"Hello, {args.name}")
