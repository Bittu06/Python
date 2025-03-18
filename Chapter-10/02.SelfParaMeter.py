class Employee:
    language = "Python" # This is class attribute
    salary = 10000

    def getInfo(self):
        print(f"My favorite language is {self.language} and my salary is {self.salary}")

    @staticmethod   # This is a decorator which is used to define a static method
    def greet():    #Using static method we don't required access of "self" object
        print("Good Morning")

Bittu = Employee()
Bittu.getInfo()
Bittu.greet()