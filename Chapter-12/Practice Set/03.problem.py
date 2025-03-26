"""
Write a list comprehension to print a list which contains the multiplication table of a 
user entered number
"""

number = int(input("Enter a number: "))
multiplication_table = [number * i for i in range(1, 11)]
print(f"Multiplication table of {number}: {multiplication_table}")