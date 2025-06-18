# Employee Salary System
#
# Create an abstract class Employee with a method calculate_salary().
# Inherit two classes: FullTimeEmployee and PartTimeEmployee, each with their own logic to calculate salary.

from abc import ABC, abstractmethod
class Employee(ABC):
    def calculate_salary(self):
        pass

class FullTimeEmployee:
    def calculate_salary(self,salary):
        return salary

class PartTimeEmployee:
    def calculate_salary(self,hours_worked,hourly_rate):
        return hours_worked*hourly_rate

f=FullTimeEmployee()
p=PartTimeEmployee()
print(f"Full time employee's salary = {f.calculate_salary(50000)}")
print(f"Part time employee's salary = {p.calculate_salary(40,4000)}")