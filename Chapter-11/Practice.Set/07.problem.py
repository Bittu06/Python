# Override the __len__() method on vector of problem 5 to display the dimension of the vector.


class Vector:
    def __init__(self, *args):
        self.values = args

    def __len__(self):
        return len(self.values)

    def __str__(self):
        return str(self.values)
    
    def __repr__(self):
        return str(self.values)
    
    def __add__(self, other):    
        if len(self) != len(other):
            return "Vectors must be of same length"
        return Vector(*(x + y for x, y in zip(self.values, other.values)))
    
    def __sub__(self, other):
        if len(self) != len(other):
            return "Vectors must be of same length"
        return Vector(*(x - y for x, y in zip(self.values, other.values)))
    
    

a = Vector(1, 2, 3)
b = Vector(4, 5, 6)
print(a + b)

print(len(a))
print(len(b))
print(a)
print(b)