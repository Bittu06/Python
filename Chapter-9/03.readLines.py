st1 = "Twinkle twinkle little star."
st2 = "How I wonder what you are."
st3 = "Up above the world so high."
st4 = "Like a diamond in the sky."
st5 = "Twinkle twinkle little star."
st6 = "How I wonder what you are."

f = open("myfile.txt", "w")
f.write(st1)
f.write(st2)
f.write(st3)
f.write(st4)
f.write(st5)
f.write(st6)
f.close()

f = open("myfile.txt", "r")
"""line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
line3 = f.readline()
print(line3)
line4 = f.readline()
print(line4)
line5 = f.readline()
print(line5)
line6 = f.readline()
print(line6)
line7 = f.readline()
print(line7)"""

line = f.readline()
while line:
    print(line, end='')  # Remove end='' to keep the default newline behavior
    line = f.readline()


f.close()