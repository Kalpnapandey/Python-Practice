student_data=[
    {
        "name":'Kalpna',
        'age':22,
        'id':1198,
        'Course':'Python'
    },
    {
        "name":'Sneha',
        'age':24,
        'id':1010,
        'Course':'Java'
    }
]

def add_new_student(name,age,id,course):
    dict = {}
    dict['name']=name
    dict['age']=age
    dict['id']=id
    dict['course']=course
    student_data.append(dict)
add_new_student('Shruti',22,1230,'C')
print(student_data)
