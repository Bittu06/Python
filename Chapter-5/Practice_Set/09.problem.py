"""Can you change the values inside a list which is contained in set S?  
s = {8, 7, 12, "Harry", [1,2]}"""

s = {8, 7, 12, "Harry", [1,2]}
s[4] = 3
print(s) # TypeError: unhashable type: 'list'