"""Write a python program to rename a file to “renamed_by_ python.txt"""

"""with open("rename.old.txt", "r") as f:
    content = f.read()

with open("rename.new.txt", "w") as f:
    f.write(content)"""

import os
os.rename("rename.old.txt", "renamed_by_python.txt")
print("File renamed successfully")

