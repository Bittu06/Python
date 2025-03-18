"""Write a program to make a copy of a text file “this. txt” """

with open("this.c9.p8.txt") as f:
    content = f.read()

with open("copy.c9.p8.txt", "w") as f:
    f.write(content)
