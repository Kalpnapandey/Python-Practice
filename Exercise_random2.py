import random
# names=["kalpna","Lovely","Gautam","Pooja"]
# print(names)
# a=random.choice(names)
# print(f"{a} will pay the bill")

names=input("Enter your friends' name separated by comma")
print(names)
s_text=names.split(",")
print(s_text)
random.shuffle(s_text)
payer=s_text[0]
print(f"{payer} is going to pay the bill")