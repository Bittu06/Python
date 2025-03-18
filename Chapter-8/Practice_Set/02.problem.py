"""Write a python program using function to convert Celsius to Fahrenheit."""

def temp(c):
    f = (c*9/5)+32
    return f

c = int(input("Enter the temperature in Celsius:"))
f = temp(c)
print(f"The temperature in Fahrenheit is:{round(f, 2)}")
