n=int(input())
s=0
for i in range(1,n):
    if (n%i==0):
        s+=i
m=int(input())
if (s==m):
    print("Amicable")
else:
    print("Not Amicable")