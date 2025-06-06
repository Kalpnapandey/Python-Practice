late_days=input("Enter the late days")
if late_days<=7:
    print("no fine")
elif late_days<=14:
    fine=(late_days-7)*5
    print(fine)
elif late_days