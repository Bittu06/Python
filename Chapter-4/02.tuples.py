#A tuple is an immutable data type in python.

a = () # empty tuple

b = (38, 38,92, False, 'Python') # tuple with values

b[0]= 23 # this will give an error as tuple is immutable

print(type(a))  # <class 'tuple'>

print(b.count(38)) # 2

print(b.index(92)) # 2

print(38 in b) # True

print(len(b)) # 5

tuple1 = (1, 2, 3)
a, b, c = tuple1
print(a,b,c) # 1 2 3