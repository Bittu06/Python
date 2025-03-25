class Employee:
    company = "Microsoft"
    @classmethod
    def show(cls):  # cls is used to access class variable
        print(f"Employee Company name is: {cls.company}")
    #def show(self):
    #    print(f"Employee Company name is: {self.company}")


e = Employee()
e.company = "Google"        # This will change the company name for this object only

e.show()