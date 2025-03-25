#   Create a class ‘Employee’ and add salary and increment properties to it.

#Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter which changes the value of increment based on the salary. 
class Employee:
    salary = 1000
    increment = 15  # 15% increment
    
    @property
    def salary_after_increment(self):
        return self.salary + (self.salary * self.increment/100)  # Calculate percentage increase

    @salary_after_increment.setter
    def salary_after_increment(self, val):
        self.increment = (val - self.salary) * 100 / self.salary  # Calculate percentage increase   

e = Employee()
print(f"Original Salary: {e.salary}")
print(f"Salary after {e.increment}% increment: {e.salary_after_increment}")
e.increment = 20  # Change to 20% increment
print(f"Salary after {e.increment}% increment: {e.salary_after_increment}")


e.salary_after_increment = 1200  # Change to 1200 salary
print(f"Salary after {e.increment}% increment: {e.salary_after_increment}")
print(f"New Salary: {e.salary}")
print(f"New Increment: {e.increment}")