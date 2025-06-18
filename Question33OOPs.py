# Define a class Employee that takes name and salary through a constructor.
# Create two employee objects.
# Add a method display_info() that prints the employee’s name and salary.
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display_info(self):
        print(self.name,self.salary)
obj1=Employee('Kalpna',10)
obj2=Employee('Lovely',20)
print(obj1.name,obj1.salary)
print(obj2.name,obj2.salary)