student_marks={
    'Jenny':92,
    'Harry':78,
    'Dimpy':56,
    'Rahul':41,
    'Aniket':99,
    'Prem':34
}
grades={}
for i in student_marks:
    # marks=student_marks[i]
    if student_marks[i]>90:
        grades[i]='A+'
    elif student_marks[i] > 80:
            grades[i] = 'A'
    elif student_marks[i]>70:
        grades[i]='B+'
    elif student_marks[i]>60:
        grades[i]='B'
    elif student_marks[i]>50:
        grades[i]='C'
    elif student_marks[i]>40:
        grades[i]='D'
    else:
        grades[i]='F'
print(grades)