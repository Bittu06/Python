"""
 Write a program to display a/b where a and b are integers. If b=0, display infinite by 
handling the ‘ZeroDivisionError’.
"""

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

if b==0 :
    raise ZeroDivisionError("Enter a valid number")
else:
    print(f"a/b = {a/b}")