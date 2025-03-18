"""Write a program to find out the line number where python is present from ques 6"""

with open("log.c9.p6.txt") as f:
    lines = f.readlines()


lineNo = 1
for line in lines:
    if ("python" in line.lower()):
        print(f"Python is present on line number {lineNo}")
    lineNo += 1    
