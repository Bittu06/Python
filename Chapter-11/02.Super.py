class employee:
    company = "Microsoft"
    def show(self):
        print(f"constructor of employee class called")

class programmer(employee):
    def __init__(self):
        print(f"constructor of programmer class called")
        super().__init__()
        

a = employee()
b = programmer()

b.__init__()