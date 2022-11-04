import math
n=int(input())
temp=n
a=0
b=0
rev=0
while (n):
    r=n%10
    n=n//10
    rev=rev*10+r
while(rev):
    b+=1
    r=rev%10
    rev=rev//10
    a+=pow(r,b)
if (a==temp):
    print("True")
else:
    print("False")