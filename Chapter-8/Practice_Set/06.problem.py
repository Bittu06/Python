"""Write a python function which converts inches to cms."""

def inchInCms(i):
    return i*2.5

n = int(input("Enter the inch:"))
print(f"{n} inch = {inchInCms(n)} cm")