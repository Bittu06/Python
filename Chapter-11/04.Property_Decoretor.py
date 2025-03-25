class Employee:
    company = "Microsoft"
    @classmethod
    def show(cls):
        print(f"Employee Company name is: {cls.company}")
    
    @property
    def name(self):
       return f"{self.fname} {self.lname}"

    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]    # This will split the name and assign the first part to fname and second part to lname
        self.lname = value.split(" ")[1]    # This will split the name and assign the first part to fname and second part to lname


e = Employee()
e.company = "Google"        # This will change the company name for this object onlye
e.name = "Bittu Dey"
print(e.fname)
print(e.lname)
print(e.name)
e.show()