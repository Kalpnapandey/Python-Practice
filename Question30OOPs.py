class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        if marks >50:
            print("Pass")
        else:
            print("fail")
stu1=Student('kalpna',98)
