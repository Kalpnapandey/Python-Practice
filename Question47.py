# Create a Python class named Person that demonstrates the concept of
# encapsulation using the following requirements:
# The class should have:
# A public attribute name (string)
# A protected attribute _city with a default value "Unknown"
# A private attribute __age (integer), initialized via the constructor
# Implement getter and setter methods for the private attribute __age:
# get_age() should return the current age.
# set_age(age) should update the age only if the value is positive.
# Create an object of the Person class with the name "Alice" and age 30.
# Print
# The person's name using direct access
# The city using protected access
# The age using the getter method
# Update the age to 35 using the setter method and print it again using the getter

class Person:
    def __init__(self,name,age):
        self.name=name
        self._city='unknown'
        self.__age=age
    def get_age(self):
        return self.__age
    def set_age(self):
        if self.__age>0:
            age=self.__age


person=Person("ALice",30)
person.get_age()
person.set_age()
