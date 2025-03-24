class employee:
    company = "Microsoft"
    def show(self):
        print(f"Employee Company name is: {self.company}")

class coder:
    language = "Python"
    def print_language(self):
        print(f"Language: {self.language}")

class programmer(employee, coder):
    language = "C++"
    company = "Google"
    def company_name(self):
        print(f"programmer Company name is: {self.company}")


a = employee()
b = programmer()
c = coder()


a.show()
b.show()
b.company_name()
b.print_language()
c.print_language()

