l = [9, 648, 53, 874, 23, 5, 6, 7, 8]


#index = 0
#for item in l:
 #   print(f"Index: {index}, Item: {item}")
 #  index += 1

# The above code is a simple loop that iterates over a list and prints the index and item.
# However, it can be improved using the enumerate function, which provides a cleaner and more Pythonic way to achieve the same result.

for index, item in enumerate(l):
    print(f"Index: {index}, Item: {item}")
# The enumerate function takes an iterable (like a list) and returns an iterator that produces pairs of index and item.