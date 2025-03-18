"""Write a program to calculate the factorial of a given number using for loop"""

num = int(input("enter a number:"))
product = 1
for i in range(1,num):
    product = product * i

print(product)