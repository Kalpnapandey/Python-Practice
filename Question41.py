# Class: Employee
# Create a class Employee with name and salary.
# Add a method tax() that returns:
# "No tax" if salary < ₹2,50,000
# "Taxable" otherwise
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def tax(self):
        if self.salary<250000:
            print("No tax")
        else:
            print("Taxale")

taxes=Employee('kalpna',100000)
taxes.tax()