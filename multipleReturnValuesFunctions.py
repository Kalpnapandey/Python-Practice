# import statistics
# def mean_median_mode(list):
#     return statistics.mean(list),statistics.median(list),statistics.mode(list)
#
# print(mean_median_mode([8,9,76,89,90,12,12,34]))

def sum(a,b):
    if a==0 and b==0:
        return "You have entered zero for both the values"
    else:
        return a+b
n1=int(input("Enter first number"))
n2=int(input("Enter second number"))
print(sum(n1,n2))