# Check that a tuple type cannot be changed in python.

tuple1 = (1, "Bittu", 3.14)

"tuple1[1]=3" # it will give error because tuple is immutable

tuple2 = (1,2,3,[4,5,6])

tuple2[3].append(7)
print(tuple2) # it will print (1,2,3,[4,5,6,7]) because list is mutable