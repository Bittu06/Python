#Write a program to input eight numbers from the user and display all the unique numbers (once).

a =set()

for i in range(8):
    a.add(int(input(f"Enter the number{i+1}:")))

print(a)