pizza=input("Please order your pizza")
small_pizza=100
medium_pizza=200
large_pizza=300
bill=0
pep_small=30
pep_large=50
cheese=20
if small_pizza:
    pepperoni=input("Do you want pepperoni? (Y/N)")
    if pepperoni=='Y' or pepperoni=='y':
        bill=small_pizza+pep_small
    print(f"Now the bill for your small pizza is {bill}")



