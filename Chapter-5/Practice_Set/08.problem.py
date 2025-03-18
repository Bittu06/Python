"""If languages of two friends are same; what will happen to the program in problem 6?"""

a = {}

for i in range(4):
    a.update({input(f"Enter name of friend{i+1}: "): input("Enter his fav lang: ")})

print(a)



"""As a is a directory and we performe update operation so when the name is reppiting
 or same then it will only update Name no adding operartion happen"""