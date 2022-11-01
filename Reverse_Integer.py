import math
n=int(input())
s=0
temp=n
k=abs(n)
while(k):
    r=k%10
    k=k//10
    s=s*10+r
if(temp<0):
    print(-s)
else:
    print(s)