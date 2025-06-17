# Day 24 - Solutions

import os
import shutil

# Exercise 1:
print(os.getcwd())

# Exercise 2:
os.mkdir("test_folder")

# Exercise 3:
os.rename("test_folder", "renamed_folder")

# Exercise 4:
with open("renamed_folder/info.txt", "w") as f:
    f.write("Hello from Python!")

# Exercise 5 (Bonus):
os.mkdir("backup")
shutil.copy("renamed_folder/info.txt", "backup/info.txt")
