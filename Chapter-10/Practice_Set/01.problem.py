"""Create a class “Programmer” for storing information of few programmers 
working at Microsoft."""

class Programmer:
    company = "Microsoft"
    def __init__(self, name, product, salary):
        self.name = name
        self.product = product
        self.salary = salary

    def getInfo(self):
        print(f"The name of the {self.company} programmer is {self.name} and the product is {self.product}. The salary is {self.salary}")

harry = Programmer("Harry", "Skype", 44000)
rohan = Programmer("Rohan", "GitHub", 25000)
harry.getInfo()
rohan.getInfo()