# i=0
# while i<=10:
#     print(i)
#     i+=1
#     if i==5:
#         break
#         print("Kalpna")
# print("Out of the loop")

list=["Hi","Hello","Ola"]
names=['Kalpna','Sneha','Lovely']
for i in list:
    for name in names:
        print(i,name)
        if i=="Hello" and name=="Sneha":
            break
    print("Out of inner loop")
print("Out of outer loop")