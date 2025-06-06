import random
# a=[1,2,3,4,5]
# ran=random.sample(a,2)
# print(ran)

a=list(range(1,25))
lottery_draw=random.sample(a,5)
print(f"Your lottery draw pattern is", lottery_draw)
