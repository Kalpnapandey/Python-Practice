# Class: Laptop
# Define a class Laptop with brand, ram, and price.
# Add a method is_budget() that returns:
# "Budget laptop" if price < 40,000
# "Premium laptop" otherwise

class Laptop:
    def __init__(self,brand,ram,price):
        self.brand=brand
        self.ram=ram
        self.price=price
    def is_budget(self):
        if self.price<40000:
            print("Budget laptop")
        else:
            print("Premium laptop ")
budget=Laptop("Dell",128,50000)
print(budget.is_budget())