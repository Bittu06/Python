class Employee:
    language = 'Python'
    salary = 10000

    def __init__(self):
        print("I am creating a constructor") # this is also calles as dunder method

    def _getInfo_(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language


Bittu = Employee("Bittu", 12000, "Java")

print(Bittu.name, Bittu.salary, Bittu.language)