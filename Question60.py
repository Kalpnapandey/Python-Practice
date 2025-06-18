# Count how many times the digit 7 appears from 1 to N
num=int(input("Enter the number"))
count=0
for i in range(1,num+1):
    for n in str(i):
        if n=='7':
            count+=1
print(count)