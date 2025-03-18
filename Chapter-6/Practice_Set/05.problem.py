"""Write a program which finds out whether a given name is present in a list or not."""

names = ["Harry", "Shubham", "Sachin", "Rahul", "Sam"]
name = input("Enter the name: ")
if name in names:
    print("Yes, the name is present in the list")
else:
    print("No, the name is not present in the list")
