# . Create a class Car with attributes brand and price.
# Create an object with values "Toyota" and 1200000.
# Print:
# "The car brand is Toyota and it costs ₹1200000."

class Car:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
car1=Car('Toyota',1200000)
print(f"The car brand is {car1.brand} and it costs rs.{car1.price}")