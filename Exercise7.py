weight=int(input("Enter your weight in kgs"))
height=float(input("Enter your height in metres"))
bmi=weight/height**2
print(bmi)
if bmi<18.5:
    print(f"Your BMI is{bmi} and you're underweight")
elif bmi<25:
    print(f"Your BMI is{bmi} and you have a normal weight")
elif bmi<30:
    print(f"Your BMI is{bmi} and you're overweight")
elif bmi<35:
    print(f"Your BMI is{bmi} and you're obese")
else:
    print(f"Your BMI is{bmi} and you're hghly obese")