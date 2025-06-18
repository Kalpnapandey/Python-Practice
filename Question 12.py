# 6. Time-Based Greeting System
# Ask user to enter time (24-hour format).
# 0–11: Good Morning
# 12–17: Good Afternoon
# 18–20: Good Evening
# 21–23: Good Night
# Else print invalid time.
# if lower <= value <= upper:
time=int(input("Enter the time n 24 hour format"))
if 0 <=time<=11:
    print("Good morning")
elif 12 <= time <=17:
    print("Good afternoon")
elif 18 <= time <=20:
    print("Good Evening")
elif 21 <= time <=23:
    print("Good night")
else:
    print("Invalid time")