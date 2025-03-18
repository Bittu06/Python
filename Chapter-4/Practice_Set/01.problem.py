#Write a program to store seven fruits in a list entered by the user. 

fruits = []
for i in range(7):
    fruit = input(f"Enter the name of fruit {i+1}: ")
    fruits.append(fruit)
print("The list of fruits is:", fruits)