import random
print("Toss the coin")
a=random.randint(0,1)
print(f"The value after the toss is {a} and hence it is:")
if a<=0:
    print("Heads")
else:
    print("Tails")
