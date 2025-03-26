# Map Example
# The map() function applies a given function to all items in an iterable (like a list) and returns a map object (which is an iterator).
l = [1, 2, 3, 4, 5, 6]

squared = map(lambda x: x**2, l)

print(list(squared))

# Filter Example
# The filter() function constructs an iterator from those elements of iterable for which the function returns true.

def even(n):
    if(n%2 == 0):
        return True
    else:
        return False
    
only_even = filter(even, l)
print(list(only_even))


# Reduce Example
# The reduce() function applies a rolling computation to sequential pairs of values in a list.

def sum(x, y):
    return x + y

from functools import reduce
print(reduce(sum, l))

