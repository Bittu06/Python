s = {1,2,3,3,7,3,6}

a = set() # empty set

print(s) # {1, 2, 3, 6, 7} because set does not allow duplicate values

s.add(9) # add 4 to the set
print(s) # {1, 2, 3, 6, 7, 9}
s.remove(2) # remove 2 from the set
print(s) # {1, 3, 6, 7, 9}
s.clear # it will clear the set

A1 = {1,2,7,4,9}
A2 = {5,6,7,8,9}

print(A1.union(A2)) # {1, 2, 4, 5, 6, 7, 8, 9}
print(A1.intersection(A2)) # {9, 7} 
print(A1.difference(A2)) # {1, 2, 4}