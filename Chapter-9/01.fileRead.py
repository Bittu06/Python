# write a program that reads a file and prints its contents

f = open("file.txt", "r")

data = f.read()

print(data)

f.close()