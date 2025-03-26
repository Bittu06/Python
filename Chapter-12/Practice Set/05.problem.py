"""
Store the multiplication tables generated in problem 3 in a file named Tables.txt.
"""

number = int(input("Enter a number: "))
multiplication_table = [number * i for i in range(1, 11)]
print(f"Multiplication table of {number}: {multiplication_table}")

with open("Tables.txt", "w") as file:
    file.write(f"Multiplication table of {number}:\n")
    for i in range(1, 11):
        file.write(f"{number} x {i} = {number * i}\n")

print("Multiplication table has been written to Tables.txt.")