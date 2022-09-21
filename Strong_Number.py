import math
n=int(input())
s=0
temp=n
while (temp>0):
    r=temp%10
    fact=math.factorial(r)
    s+=fact
    temp=temp//10
if (s==n):
    print("The number", n, "is a strong number")
else:
    print("The number", n ,"is not a strong number")