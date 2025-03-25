#    Write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot(.) product of them

class Vector:
    def __init__(self, *args):
        self.values = args  

    def __add__(self, other):
        if len(self.values) != len(other.values):
            raise ValueError("Vectors must have the same number of dimensions")
        result = Vector(*[x + y for x, y in zip(self.values, other.values)])
        return result
    
    def __mul__(self, other):
        if len(self.values) != len(other.values):
            raise ValueError("Vectors must have the same number of dimensions")
        result = sum([x * y for x, y in zip(self.values, other.values)])
        return result
    
    def __str__(self):
        return f"Vector{self.values}"


v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print(v1 + v2)
print(v1 * v2)
print(v1)
print(v2)