"""Write a recursive function to calculate the sum of first n natural numbers."""

def sum(n):
    if n == 1:
        return 1
    return n + sum(n-1)

n = int(input("Enter the number:"))

print(f"The sum of first {n} natural numbers is:{sum(n)}")
