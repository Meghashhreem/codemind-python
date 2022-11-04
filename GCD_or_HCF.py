n,m=map(int,input().split())
max=0
if n>m:
    n,m=m,n
for i in range(1,n+1):
    if n%i==0 and m%i==0:
        if i>max:
            max=i
print(max)