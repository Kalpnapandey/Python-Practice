# num=int(input("Enter a number"))
# if num>10:
#     print("Greater number")
#     if(num%2==0):
#         print("even number")
# else:
#     print("Odd and smaller number")

height=int(input("Enter your input"))
if height>=3:
    print("You can go for ride")
    age=int(input("Enter your age"))
    if age>=10:
        print("you need to pay 150")
    elif age>=20:
        print("need to pay 200")
    elif age>=30:
        print("you need to pay250")
    else:
        print("Please pay as per the requirement")
else:
    print("Can't ride")
print("Bye")