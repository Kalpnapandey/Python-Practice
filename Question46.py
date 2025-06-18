# Class: Person → Encapsulation
# Create a class Person with private attributes __name and __age.
# Add methods:
# set_details(name, age)
# get_details()
# Make sure age cannot be set below 0.
class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def set_details(self):
        if self.__age<=0:
            return False
        self.__age=age

    def get_details(self):
        print(self.__name,self.__age)

details=Person('kalpna',0)
details.get_details()


