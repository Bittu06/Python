st = "Bittu is a very polite person."

f = open("myfile.txt", "w")

f.write(st)

f.close()


r = open("myfile.txt", "r")
data = r.read()
print(data)
r.close()