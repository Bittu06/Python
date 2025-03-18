"""Write a program using functions to find greatest of three numbers."""

def great(a,b,c):
    if(a>b and b>c):
        print(f"The greatest number is:{a}")
    elif(b>a and a>c):
        print(f"The greatest number is:{b}")
    else:
        print(f"The greatest number is{c}")


a = int(input("Enter the first no:"))
b = int(input("Enter the second no:"))
c = int(input("Enter the third no:"))

great(a,b,c)