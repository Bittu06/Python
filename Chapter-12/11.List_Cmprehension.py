#   List Comprehension is an elegant way to create lists based on existing lists.

myList = [1, 9, 3, 4, 5]

#squaredList = []
#for i in myList:
#    squaredList.append(i ** 2)

squaredList = [i ** 2 for i in myList]

print(squaredList)