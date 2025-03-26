a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

if(b==0):
    raise ZeroDivisionError("Division by zero is not allowed.")
else:
    c = a / b
    print("Result:", c)
# The above code will raise a ZeroDivisionError if the user tries to divide by zero.