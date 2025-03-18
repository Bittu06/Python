"""A function is a group of statements performing a specific task."""

def avg():
    a = int(input("Enter first number: "))
    b= int(input("Enter second number: "))
    c = int(input("Enter third number: "))

    avg = (a+b+c)/3
    print("Average of three numbers is: ", avg)


avg()