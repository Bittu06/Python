#   Write a program to find the maximum of the numbers in a list using the reduce function

n = [54, 25, 12, 10, 15, 30, 7, 8, 9, 20]

from functools import reduce

"""
def max_of_list(a,b):
    if(a>b):
        return a
    else:
        return b
"""

def max_of_list(numbers):
    """Return the maximum number from a list of numbers."""
    return reduce(lambda x, y: x if x > y else y, numbers)

print("The maximum number in the list is: ", max_of_list(n))