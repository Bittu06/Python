"""Add a static method in problem 2, to greet the user with hello. """

class Calculator:
    def __init__(self, num):
        self.num = num

    def square(self):
        return self.num ** 2

    def cube(self):
        return self.num ** 3

    def square_root(self):
        return self.num ** 0.5

num = int(input("Enter a number: "))  
Calculator = Calculator(num)
print(Calculator.square())
print(Calculator.cube())
print(Calculator.square_root())
    
# Static method
@staticmethod
def greet():
    print("Hello")

greet()