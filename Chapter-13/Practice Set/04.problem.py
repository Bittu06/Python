#   Write a program to filter a list of numbers which are divisible by 5.

def divisile_by_5(numbers):
    """Return a list of numbers that are divisible by 5."""
    return [number for number in numbers if number % 5 == 0]

n = [54, 25, 12, 10, 15, 30, 7, 8, 9, 20]
print("The numbers that are divisible by 5 are: ", divisile_by_5(n))