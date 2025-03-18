"""Write a program to find out whether a file is identical & matches the content of 
another file."""

with open("file1.c9.p9.txt") as f:
    content1 = f.read()

with open("file2.c9.p9.txt") as f:
    content2 = f.read()

if content1 == content2:
    print("The content of both the files are identical")
else:
    print("The content of both the files are not identical")