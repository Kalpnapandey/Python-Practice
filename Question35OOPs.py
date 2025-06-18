# 1. Define a Student class with attributes name, grade, percentage, and team.
# • Include an __init__ method to initialize these attributes.
# • Add a method student_details that prints the student’s details in the format:
# "<name> is in <grade> grade with <percentage>%, from team <team>".
# 2. Create two teams (team1 and team2) as string variables.
# 3. Create at least two student objects, each belonging to one of the teams.
# 4. Call the student_details method for each student to display their details.

class Student:                          # class
    def __init__(self,name,grade,percentage,team):      #method
        self.name=name                  #Attribute
        self.grade=grade                #Attribute
        self.percentage=percentage
        self.team=team

    def student_details(self):                      #Abstraction method
        print(self.name,self.grade,self.percentage+2,self.team) # hidden grace marks logic
team1='A'
team2='B'
# Object1:Instance of the class
student2=Student('Kalpna','A',98,team1)
# print(student2.name,student2.grade)
#
# #Object2
student3=Student('Gaurav','A',90,team2)
# print(student3.name,student3.grade)

student2.student_details()
print(student2.team)