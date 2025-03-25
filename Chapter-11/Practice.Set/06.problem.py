#    Write __str__() method to print the vector as follows: 
#                                7i + 8j +10k  
#Assume vector of dimension 3 for this problem.

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)
    
    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag, self.real * other.imag + self.imag * other.real)
    
    def __truediv__(self, other):
        denominator = other.real**2 + other.imag**2
        return Complex((self.real * other.real + self.imag * other.imag) / denominator, (self.imag * other.real - self.real * other.imag) / denominator)
    
    def __str__(self):
        return f"{self.real}i + {self.imag}j + {self.imag}k"
    

a = Complex(1, 2)
b = Complex(3, 4)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a)
print(b)