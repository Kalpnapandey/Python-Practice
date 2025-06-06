age=input("ENter your age")
day=input("Enter the day")
if age>13:
    price=80
elif age>=60:
    price=100
else:
    price=150
if day=='Wednesday':
    price -= 20