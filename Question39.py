# Class: Temperature
# Takes a temperature in Celsius.
# Add methods:
# to_fahrenheit() – converts to °F
# is_freezing() – returns "Freezing" if temp ≤ 0, else "Not freezing"

class Temperature:
    def __init__(self,input):
        self.input=input
    def to_fahrenheit(self):
        f=(self.input * 9 / 5) + 32
        return f

    def is_freezing(self):
        if self.input<=0:
            print("Freezing")
        else:
            print("Not freezing")
temp=Temperature(36)
fahrenheit_temp=temp.to_fahrenheit()
print(f"Temperature in fahrenheit is {fahrenheit_temp}")
temp.is_freezing()