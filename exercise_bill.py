height=int(input("Enter your height"))
bill=0
if height>=3:
    print("You can ride")
    age=int(input("Enter your age"))
    if age<12:
        bill=150
        print("Your bill is 150")
    elif age<=18:
        bill=200
        print("Your bill is 200")
    else:
        bill=500
        print("Your bill is 500")

    photo=input("Do you want a photo(Y/N)")
    if photo=='Y' or photo=='y':
        bill=bill+50
    print("Your bill is",bill)

else:
    print("Can't ride")