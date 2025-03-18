"""Create an empty dictionary. Allow 4 friends to enter their favorite language as 
value and use key as their names. Assume that the names are unique"""

a = {}

for i in range(4):
    a.update({input(f"Enter name of friend{i+1}: "): input("Enter his fav lang: ")})

print(a)