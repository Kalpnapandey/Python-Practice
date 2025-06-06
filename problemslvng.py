maths_n=input("Enter your maths marks in digits")
eng_n=input("Enter your english marks in digits")
sci_n=input("Enter your maths marks in digits")
if float(maths_n) and float(eng_n) and float(sci_n):
    maths = float()
    if maths>=40 and eng>=40 and sci>=40:
    print("Pass")
    avg = maths + eng + sci / 3
    print(f"Your average is {avg}")
    if avg >= 50:
            print("Pass")
        # else :
        #     print('fail')
    else:
        print("fail")

else :
    print('error')