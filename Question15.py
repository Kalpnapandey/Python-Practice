# Health Check Flags
# Ask the user for:
# Temperature (in °C)
# Heart rate
# Oxygen level (%)
# Print:
# “Fever detected” if temperature > 37.5
# “High heart rate” if HR > 100
# “Low oxygen level” if oxygen < 95
# (All three checks should be done independently)
t,hr,o=map(int,input("Enter your Temperature in Celsius, Heart rate  and oxygen level in"
                    "percentage").split())
if t>37:
    print("Fever detected")
else:
    print("No fever detected")
if hr>100:
    print("High heart rate")
else:
    print("Heart rate is normal")
if o<95:
    print("Low oxygen level")
else:
    print("Perfect oxygen level")