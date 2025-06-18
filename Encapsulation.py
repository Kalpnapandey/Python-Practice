# Encapsulation:Restricting direct access to attributes & methods
class Student:                          # class
    def __init__(self,name,grade,percentage,):      #method
        self.name=name                  #Attribute
        self.grade=grade                #Attribute
        self.__percentage=percentage

    def get_percentage(self):
        return self.__percentage

    def student_details(self):                      #Abstraction method
        print(self.name,self.grade,self.__percentage,)

# Object:Instance of class
student2=Student('Kalpna','A',98,)
student3=Student('Gaurav','A',90,)

print(student2.get_percentage())